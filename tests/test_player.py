import pytest

from snapsim3000.deck import Card, CardFace, CardValue
from snapsim3000.game import Game
from snapsim3000.player import Player, SnapResult


@pytest.mark.asyncio
async def test_player_works_with_game():
    game = Game()
    game.new_game(decks=1)

    player = Player(name="Test Player")

    game.add_player(player)
    game.deal_cards()

    await game.play_turn()


@pytest.mark.asyncio
async def test_player_calls_snap():
    test_card = Card(CardFace.SPADES, CardValue.ACE)

    test_player = Player(name="Test Player")

    first_result = await test_player.check_for_snap(test_card)
    second_result = await test_player.check_for_snap(test_card)
    third_result = await test_player.check_for_snap(test_card)

    assert first_result == SnapResult(False, test_player)
    assert second_result == SnapResult(True, test_player)
    assert third_result == SnapResult(False, test_player)


def test_player_adds_score():
    test_player = Player(name="Test Player")

    test_player.add_score(5)

    assert test_player.score == 5
