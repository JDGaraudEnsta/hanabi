import hanabi

game = hanabi.Game(2)  # 2 players
ai = hanabi.ai.Cheater(game)

# pour jouer toute une partie
game.ai = ai
game.run()



