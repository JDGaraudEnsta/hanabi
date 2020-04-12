import hanabi
import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_RandomAI():
    game = hanabi.Game(2)  # 2 players

    ai = hanabi.RandomAI(game)

    # pour jouer toute une partie
    game.ai = ai
    game.run()


def test_Cheater():
    game = hanabi.Game(2)  # 2 players
    ai = hanabi.ai.Cheater(game)

    # pour jouer toute une partie
    game.ai = ai
    game.run()
