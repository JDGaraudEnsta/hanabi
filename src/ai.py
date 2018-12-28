

class Cheater:
    """
    This player can see his own cards!

    Algorithm:
      * if 1-or-more card is playable: play the lowest one.
      * if blue_coin<8: discard the largest one, except if it's the last of its kind
      * give a random clue
    """
    def __init__(self):
        pass

    def play(self, game):
        action = "p1"
        return action
