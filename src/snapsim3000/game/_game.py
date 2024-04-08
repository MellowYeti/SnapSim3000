import asyncio
import random
from itertools import cycle
from typing import List

from snapsim3000.deck import Card, Deck
from snapsim3000.player import Player


class Game:
    def __init__(self, decks: int) -> None:
        self.hand: List[Card] = list()
        self.pile: List[Card] = list()
        self.discard: List[Card] = list()
        self.players: List[Player] = list()

        for _ in range(decks):
            self.hand.extend(Deck())

        random.shuffle(self.hand)

    def add_player(self, player: Player):
        self.players.append(player)

    def deal_cards(self):
        for player, card in zip(cycle(self.players), self.hand):
            player.take_card(card)

    async def play_turn(self):
        player = self.players.pop(0)
        self.players.append(player)

        played_card = player.play_card()
        print(f"{player.name} played {played_card}")

        self.pile.append(played_card)

        notify_routines = [
            player.check_for_snap(played_card) for player in self.players
        ]

        for task in asyncio.as_completed(notify_routines):
            result = await task

            if result.snap:
                score = len(self.pile)
                result.player.add_score(score)

                print(f"⭐️ {result.player.name} called snap!")
                print(f"🏆 {score} points for {result.player.name}!")

                self.discard.extend(self.pile)
                self.pile.clear()
                break

        if len(self.pile) + len(self.discard) < len(self.hand):
            return True

    def get_scores(self):
        ranked = sorted(self.players, reverse=True, key=lambda player: player.score)
        return [{"name": player.name, "score": player.score} for player in ranked]
