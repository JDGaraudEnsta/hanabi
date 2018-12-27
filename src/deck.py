"""
Hanabi deck.
"""

from enum import Enum          
from enum import unique        
import random


@unique
class Color(Enum):
    Red = 1
    Blue = 2
    Green = 3
    White = 4
    Yellow = 5
#    Multi = 6

    def __str__(self):
        return self.name
    
class Card:
    def __init__(self, color=None, number=None):
        "A hanabi card."
        assert (1 <= number <= 5), "Wrong number"
        self.color = color
        self.number = number

    def __str__(self):
        return (str(self.color)[0] + str(self.number))
    
    def __eq__(self, c):
        "Return whether 2 cards are equal. Can compare 2 Card objects or their string value."
        return str(self) == str(c)


class Hand:
    def __init__(self, deck, n=5):
        "A Hanabi hand, with n cards, drawn from the deck."
        self.cards = []
        for i in range(n):
            self.cards.append(deck.draw())
    def __str__(self):
        return " ".join(map(str, self.cards))

    def play(self, card):
        "Play the given card. Raise ValueError if it is not playable."
        self.cards.remove(card) # raises the ValueError 
        self.cards
    
class Deck:
    # Rules for making decks:
    ones = 3
    twos = threes = fours = 2
    fives = 1
    # Rules for dealing:
    cards_by_player = { 2:5, 3:5, 4:4, 5:4}
    def __init__(self):
        self.cards  \
            = [ Card(c, 1) for c in list(Color) ] * self.ones \
            + [ Card(c, 2) for c in list(Color) ] * self.twos \
            + [ Card(c, 3) for c in list(Color) ] * self.threes \
            + [ Card(c, 4) for c in list(Color) ] * self.fours \
            + [ Card(c, 5) for c in list(Color) ] * self.fives

    def __str__(self):
        return " ".join(map(str, self.cards))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        "Draw the first card."
        return self.cards.pop(0)
        
    def deal(self, nhands):
        "Deal n hands and return them."
        hands = []
        for i in range(nhands):
            hands.append(Hand(self, self.cards_by_player[nhands]))
        return hands



if __name__ == "__main__":
    print ("Red 4 is:", Card(Color.Red, 4))

    deck = Deck()
    print("Unshuffled:", deck)
    deck.shuffle()
    print("Shuffled:", deck)
    
    hands = deck.deal(5)
    alice, benji, clara, devon, elric = hands
    players = {0:"Alice", 1: "Benji", 2:"Clara", 3:"Devon", 4:"Elric"}
    for i, h in enumerate(hands): print("%s's hand is %s"%(players[i], h))

    print ("Is B1 in Alice's hand?", "R1" in alice.cards)
    
    alice.play("R1")
    
