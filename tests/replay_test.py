import hanabi


def test_replay():
    score = [4, 20, 24, 25, 21, 21]
    for i in range(1, len(score) + 1):
        filepath = "resources/game" + str(i)
        game = hanabi.Game(2)
        game.load(filepath)
        assert game.score == score[i - 1]
