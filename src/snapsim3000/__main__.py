import asyncio
import sys

from snapsim3000.game import Game
from snapsim3000.player import Player


async def main():
    print("🚨 Snap Simulator 3000 🚨")

    try:
        decks = int(input("How many decks? "))
    except ValueError:
        print("Not a valid number of decks!")
        return 1

    if decks not in range(1, 11):
        print("Number of decks must be between 1 and 10!")
        return 2

    game = Game(decks=decks)

    game.add_player(Player(name="Alice"))
    game.add_player(Player(name="Bob"))

    game.deal_cards()

    while await game.play_turn():
        pass

    print("Game over!")
    scores = game.get_scores()

    print("Final scores:")
    for score in scores:
        print(f"{score['name']}: {score['score']}")

    print(f"{scores[0]['name']} wins with {scores[0]['score']} points!")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
