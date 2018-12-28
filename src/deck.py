"""
Hanabi deck.
"""

import copy
import random

from enum import Enum          
from enum import unique        

@unique
class Color(Enum):
    "Card colors. Int values correspond to xterm's."
    Red = 31
    Blue = 34
    Green = 32
    White = 37
    Yellow = 33
    # Red = 41
    # Blue = 44
    # Green = 42
    # White = 47
    # Yellow = 43
#    Multi = 6

    def __str__(self):
        return self.name
    def __repr__(self):
        return 'Color.'+self.name
    def colorize(self, *args):
        return '\033[%im'%self.value + ' '.join(map(str,args)) + '\033[0m'
    
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
    def __repr__(self):
        return ("Card(%r, %d)"%(self.color, self.number))
        
    def str_color(self):
        return self.color.colorize(str(self))

    def __eq__(self, c):
        "Return whether 2 cards are equal. Can compare 2 Card objects or their string value."
        return str(self) == str(c)

    def str_clue(self):
        "What I know about this card."
        return (self.color_clue or '*') + (self.number_clue or '*') 

class Hand:
    def __init__(self, deck, n=5):
        """A Hanabi hand, with n cards, drawn from the deck.
        Also used for the discard pile.
        """
        #TODO: see if it's easier to derive from list
        self.cards = []
        for i in range(n):
            self.cards.append(deck.draw())
        self._deck = deck  # no sure if I need it 

    def __str__(self):
        return " ".join([c.str_color() for c in self.cards])
    def __repr__(self):
        return str(self)

    def str_clue(self):
        return " ".join([c.str_clue() for c in self.cards])

    def pop(self, i):
        "Pop a card from the hand, and draw a new one."
        if not 1 <= i <= len(self):
            raise ValueError("%d is not a valid card index."%i)
        i = i-1 # back to 0-based-indices
        card = self.cards.pop(i)
        self.cards.append(self._deck.draw())
        return card

    def append(self, c): self.cards.append(c)
    def sort(self): self.cards.sort(key=str)
    
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
        return " ".join([c.str_color() for c in self.cards])

    def __repr__(self):
        s = '['
        s += ", ".join(map(repr, self.cards))
        s += ']'
        return s

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

        # record deck and moves, for replay
        self.moves = []
        self.starting_deck = copy.deepcopy(self.deck)

        self.hands = self.deck.deal(len(self.players))

        self.discard_pile = Hand(None, 0)  #  I don't give it the deck, so it can't draw accidentaly a card
        self.piles = {}
        for c in list(Color): self.piles[c]=0

        self.blue_coins = 8
        self.red_coins = 0
        
        self.next_player()

        self.actions = {
            'd': self.discard,
            'p': self.play,
            'c': self.clue,
            'x': self.examine_piles,
            '>': self.command  # cheat-code !
        }
        
    def turn(self):
        "One round: ask the player what she wants to do, then update the game."
        print (self.current_player_name,
               "this is what you remember:",
               self.current_hand.str_clue(),
               "\n      this is what you see:     ",
               self.hands[(self.current_player+1)%2],
               "\n                                ",
               self.hands[(self.current_player+1)%2].str_clue(),
        )
               
        choice = input("""What do you want to play?
        (d)iscard a card (12345) 
        give a (c)lue (RBGWY 12345)
        (p)lay a card (12345)
        e(x)amine the piles
hanabi> """)
        
        # so here, choice is a 2 or 3 letters code:
        #  d2 (discard 2nd card)
        #  cR (give Red clue) ... will become cRA (give Red to Alice)
        #  p5 (play 5th card)

        self.moves.append(choice)
        try:
            self.actions[choice[0]](choice[1:])
        except KeyError as e:
            print (e, "is not a valid action. Try again.")
            self.turn()
        except (ValueError, IndexError) as e:
            print (e, "Try again")
            self.turn()
        
    def add_blue_coin(self):
        if self.blue_coins == 8:
            raise ValueError("Already 8 blue coins. Can't get an extra one.")
        self.blue_coins += 1
    def remove_blue_coin(self):
        if self.blue_coins == 0:
            raise ValueError("No blue coin left.")
        self.blue_coins -= 1

    def add_red_coin(self):
        self.red_coins += 1
        if self.red_coins == 3:
            # StopIteration will stop the main loop!
            raise StopIteration()

         
    def discard(self, args):
        "Discard the args-th card from current hand (the first if args is an empty string)."
        if args.strip() == "": args = "1"
        icard = int(args)
        self.add_blue_coin()
        try:
            card = self.current_hand.pop(icard)
        except ValueError:
            self.remove_blue_coin()
            raise
        self.discard_pile.append(card)
        self.discard_pile.sort()
        print (self.current_player_name, "discards", card.str_color())
        
    def play(self, args):
        icard = int(args)
        card = self.current_hand.pop(icard)
        print (self.current_player_name, "tries to play", card, "... ",end="")

        if (self.piles[card.color]+1 == card.number):
            self.piles[card.color] += 1
            print ("successfully!")
            if self.piles[card.color] == 5:
                try:
                    self.add_blue_coin()
                except ValueError: # it is valid to play a 5 when we have 8 coins. It is simply lost
                    pass
        else:
            # misplay!
            self.discard_pile.append(card)
            print ("Kaboom! That was a bad idea!")
            self.add_red_coin()
        self.print_piles()
        
    def clue(self, args):
        "Give a clue."
        hint = args[0].upper()  # so cr is valid to clue Red
        if not hint in "12345RBGWY":
            raise ValueError("%s is not a valid clue."%hint)
        print (self.current_player_name, "gives a clue:", hint)
        #  player = args[1]  # if >=3 players
        for card in self.hands[self.other_player].cards:
            if hint in str(card):
                if hint in "12345":
                    card.number_clue = hint
                else:
                    card.color_clue = hint
        self.remove_blue_coin()

    def examine_piles(self, unused_args):
        self.print_piles()
        raise ValueError()  # so next turn is not triggered


    def _bw_print_piles(self):
        print("    Discard:", self.discard_pile)
        for c in list(Color):
            print("%6s"%c, "pile:", self.piles[c])
        print ("Coins:", self.blue_coins, "blue,", self.red_coins, "red")
    def _color_print_piles(self):
        print("    Discard:", self.discard_pile)
        for c in list(Color):
            print(c.colorize("%6s"%c, "pile:", self.piles[c]))
        print ("Coins:", self.blue_coins, "blue,", self.red_coins, "red")
    def print_piles(self):
        self._color_print_piles()
        
        
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

    def command(self, args):
        "Internal: run a python command from Hanabi"
        print('About to run `%s`'%args)
        try:
            exec(args)
        except Exception as e:
            print('Error:', e)
        raise ValueError()  # so next turn is not triggered

    def run(self):
        try:
            while True:
                self.turn()
                self.next_player()
        except (KeyboardInterrupt, EOFError, StopIteration):
            pass
        self.save('autosave.py')
        print("\nGoodbye. Your score is", sum(self.piles.values()))

    def save(self, filename):
        f = open(filename, 'w')
        f.write("""
        game = Game()
        game.deck.cards = %r
        moves = %r
        """%( self.starting_deck,
              self.moves
        ))
        
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
        card = alice.pop(1)
        print("Alice plays", card)
    except ValueError:
        print("Alice can't play her 1st card")
        
    print ("\nLet's start a new game")
    game = Game(2)
    print ("Here are the hands:")
    print (game.hands)

    game.run()
