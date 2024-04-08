from unittest.mock import AsyncMock, Mock

import pytest

from snapsim3000.deck import Card, CardFace, CardValue, Deck
from snapsim3000.game import Game
from snapsim3000.player import SnapResult


def test_game_setup():
    test_num_decks = 2
    standard_first_card = Deck().pop(0)
    standard_last_card = Deck().pop()

    game = Game(decks=test_num_decks)

    assert len(game.hand) == test_num_decks * 52

    assert game.hand[0] != standard_first_card
    assert game.hand[-1] != standard_last_card


def test_game_deal_cards():
    game = Game(decks=1)

    player1 = Mock()
    player2 = Mock()

    game.add_player(player1)
    game.add_player(player2)

    game.deal_cards()

    assert player1.take_card.call_count == 26
    assert player2.take_card.call_count == 26


@pytest.mark.asyncio
async def test_game_test_turn():
    game = Game(decks=1)

    test_card = Card(CardFace.SPADES, CardValue.ACE)

    player1 = Mock()
    player1.play_card.return_value = test_card
    player1.check_for_snap = AsyncMock(return_value=SnapResult(True, player1))

    game.add_player(player1)

    game.deal_cards()

    turn_result = await game.play_turn()

    player1.play_card.assert_called_once()
    player1.check_for_snap.assert_awaited_once_with(test_card)
    player1.add_score.assert_called_once_with(1)

    assert turn_result


def test_game_get_scores():
    game = Game(decks=1)

    player1 = Mock()
    player1.name = "Player 1"
    player1.score = 5

    player2 = Mock()
    player2.name = "Player 2"
    player2.score = 10

    game.add_player(player1)
    game.add_player(player2)

    scores = game.get_scores()

    assert scores == [
        {"name": "Player 2", "score": 10},
        {"name": "Player 1", "score": 5},
    ]
