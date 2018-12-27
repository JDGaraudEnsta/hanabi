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
        self.color_clue = False
        self.number_clue = False

    def __str__(self):
        return (str(self.color)[0] + str(self.number))
    
    def __eq__(self, c):
        "Return whether 2 cards are equal. Can compare 2 Card objects or their string value."
        return str(self) == str(c)

    def str_clue(self):
        "What I know about this card."
        return (self.color_clue or '*') + (self.number_clue or '*') 

class Hand:
    def __init__(self, deck, n=5):
        "A Hanabi hand, with n cards, drawn from the deck."
        self.cards = []
        for i in range(n):
            self.cards.append(deck.draw())
    def __str__(self):
        return " ".join(map(str, self.cards))
    def __repr__(self): return str(self)

    def str_clue(self):
        return " ".join([c.str_clue() for c in self.cards])
    
    def play(self, card):
        "Play the given card. Raise ValueError if it is not playable."
        self.cards.remove(card) # raises the ValueError 
        self.cards

    def __len__(self): return len(self.cards)
        
class Deck:
    # Rules for making decks:
    card_count = {1:3, 2:2, 3:2, 4:2, 5:1 }
    # Rules for dealing:
    cards_by_player = { 2:5, 3:5, 4:4, 5:4 }
    def __init__(self):
        self.cards = []
        for number, count in self.card_count.items():
            for color in list(Color):
                for _ in range(count):
                    self.cards.append(Card(color, number))
        
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


class Game:
    Players = ("Alice", "Benji", "Clara", "Dante", "Elric")
    def __init__(self, multi=False, players=2):
        "A game of Hanabi"
        if isinstance(players, int):
            assert(2 <= players <= 5)
            self.players = self.Players[:players]
        else: # assume it's the list of players
            self.players = players

        self.deck = Deck()
        self.deck.shuffle()
        self.hands = self.deck.deal(len(self.players))

        self.next_player()

        self.actions = {
            'd': self.discard,
            'p': self.play,
            'c': self.clue
        }
        
    def turn(self):
        "One round: ask the player what she wants to do, then update the game."
        print (self.current_player_name,
               "this is what you remember:",
               self.current_hand.str_clue(),
               "\nthis is what you see:", self.hands[(self.current_player+1)%2]
        )
               
        choice = input("""What do you want to play?
        (d)iscard a card (12345) 
        give a (c)lue (RBGWY 12345), 
        (p)lay a card (12345)
        ?""")
        
        # so here, choice is a 2 or 3 letters code:
        #  d2 (discard 2nd card)
        #  cR (give Red clue) ... will become cRA (give Red to Alice)
        #  p5 (play 5th card)
        self.actions[choice[0]](choice[1:])
        

    def discard(self, args):
        "Discard the args-th card from current hand."
        pass

    def play(self, args):
        print("playing", args)
        
    def clue(self, args):
        print (self.current_player_name, "gives a clue:", args)
        hint = args[0]
        #  player = args[1]  # if >=3 players
        for card in self.hands[self.other_player].cards:
            if hint in str(card):
                if hint in "12345":
                    card.number_clue = hint
                else:
                    card.color_clue = hint
                    
    def next_player(self):
        "Switch to next player."
        try:
            self.other_player = self.current_player
            self.current_player = (self.current_player+1)%len(self.players)
        except AttributeError:  # very first time we call this function
            self.current_player = 0
            self.other_player = 1

        self.current_player_name = self.players[self.current_player]
        self.current_hand = self.hands[self.current_player]

        
if __name__ == "__main__":
    print ("Red 4 is:", Card(Color.Red, 4))

    deck = Deck()
    print("Unshuffled:", deck)
    deck.shuffle()
    print("Shuffled:", deck)
    
    hands = deck.deal(5)
    alice, benji, clara, devon, elric = hands
    players = {0:"Alice", 1: "Benji", 2:"Clara", 3:"Dante", 4:"Elric"}
    for i, h in enumerate(hands): print("%s's hand is %s"%(players[i], h))

    print ("Is B1 in Alice's hand?", "B1" in alice.cards)
    
    try:
        alice.play("B1")
        print("Alice plays B1")
    except ValueError:
        print("Alice can't play B1")
        
    print ("\nLet's start a new game")
    game = Game(2)
    print ("Here are the hands:")
    print (game.hands)
    
    while True:
        game.turn()
        game.next_player()
