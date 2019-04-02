"""
Hanabi deck and game engine.
"""

import copy
import random
import readline  # this greatly improves `input`

from enum import Enum
from enum import unique

from . import ascii_art
from . import ai


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
        "Colorize the given string"
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
        "Colorized string for this card."
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
        self._deck = deck  # not sure if I need it

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
        try:
            self.cards.append(self._deck.draw())
        except IndexError: pass  # deck is empty
        return card

    def append(self, c): self.cards.append(c)
    def sort(self): self.cards.sort(key=str)

    def __len__(self): return len(self.cards)


class Deck:
    # Rules for making decks:
    card_count = {1:3, 2:2, 3:2, 4:2, 5:1 }
    # Rules for dealing:
    cards_by_player = { 2:5, 3:5, 4:4, 5:4 }
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
            for number, count in self.card_count.items():
                for color in list(Color):
                    for _ in range(count):
                        self.cards.append(Card(color, number))
        else:
            self.cards = cards

    def __str__(self):
        return " ".join([c.str_color() for c in self.cards])

    def __repr__(self):
        s =  '['
        s += ", ".join(map(repr, self.cards))
        s += ']'
        return s

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        "Draw a card from the deck."
        return self.cards.pop(0)

    def deal(self, nhands):
        "Deal n hands and return them."
        hands = []
        for i in range(nhands):
            hands.append(Hand(self, self.cards_by_player[nhands]))
        return hands


class Game:
    Players = ("Alice", "Benji", "Clara", "Dante", "Elric")
    def __init__(self, players=2, multi=False):
        "A game of Hanabi."

        # Actions are functions that a player may do.
        # They should finish by a call to next_player, if needed.
        self.actions = {
            'd': self.discard,
            'p': self.play,
            'c': self.clue,
            'x': self.examine_piles,
            'l': self.load,
            '>': self.command,  # cheat-code !
            '?': (lambda x: print(ai.Cheater(self).play()))
        }
        self.reset()

    def reset(self, players=2, multi=False, cards=None):
        "Reset this game."
        if isinstance(players, int):
            assert(2 <= players <= 5)
            self.players = self.Players[:players]
        else: # assume it's the list of players
            self.players = players

        self.deck = Deck(cards)
        if cards is None:
            self.deck.shuffle()

        # print (self.deck)

        # record deck and moves, for replay
        self.moves = []
        self.starting_deck = copy.deepcopy(self.deck)

        self.hands = self.deck.deal(len(self.players))

        self.current_player = None
        self.next_player()
        self.last_player = None  # will be set the the last player, to allow last turn

        self.discard_pile = Hand(None, 0)  #  I don't give it the deck, so it can't draw accidentaly a card
        self.piles = dict(zip(list(Color), [0]*len(Color)))

        self.blue_coins = 8
        self.red_coins = 0

        self.ai = None


    def turn(self, _choice=None):
        """
        Play one round: ask the player what she wants to do, then update the game.
        If _choice is not None, play it instead of asking.

        Note:
        If provided, _choice has to be a list of actions, because I chose to
        record invalid actions too (and these loop within this file).
        """
        print()
        print (self.current_player_name,
               "this is what you remember:",
#               self.current_hand.str_clue(),
               self.current_hand,
               "\n      this is what you see:     ",
               self.hands[(self.current_player+1)%2],
               "\n                                ",
               self.hands[(self.current_player+1)%2].str_clue(),
        )
        print("""What do you want to play?
        (d)iscard a card (12345) 
        give a (c)lue (RBGWY 12345)
        (p)lay a card (12345)
        e(x)amine the piles""")

        ai.Cheater(self).play()

        while True:
            if _choice is None:
                choice = input("hanabi> ")
                if choice.strip()=='':
                    continue
            elif isinstance(_choice, ai.AI):
                choice = _choice.play()
            else:
                choice = _choice.pop(0)
                print ('hanabi (auto)>', choice)
            # so here, choice is a 2 or 3 letters code:
            #  d2 (discard 2nd card)
            #  cR (give Red clue) ... will become cRA (give Red to Alice)
            #  p5 (play 5th card)

            self.moves.append(choice)
            try:
                self.actions[choice[0]](choice[1:])
                return
            except KeyError as e:
                print (e, "is not a valid action. Try again.")
            except (ValueError, IndexError) as e:
                print (e, "Try again")

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


    def discard(self, index):
        "Action: Discard the given card from current hand (the first if index is an empty string)."
        try:
            if index.strip() == "": index = "1"
        except: pass
        icard = int(index)
        self.add_blue_coin()
        try:
            card = self.current_hand.pop(icard)
        except ValueError:
            self.remove_blue_coin()
            raise
        self.discard_pile.append(card)
        self.discard_pile.sort()
        print (self.current_player_name, "discards", card.str_color(),
               "and now we have %d blue coins."%self.blue_coins)
        self.next_player()

    def play(self, index):
        "Action: play the given card."
        icard = int(index)
        card = self.current_hand.pop(icard)
        print (self.current_player_name, "tries to play", card, "... ",end="")

        if (self.piles[card.color]+1 == card.number):
            self.piles[card.color] += 1
            print ("successfully!")
            print (card.color.colorize(
                ascii_art.fireworks[self.piles[card.color]]))
            if self.piles[card.color] == 5:
                try:
                    self.add_blue_coin()
                except ValueError: # it is valid to play a 5 when we have 8 coins. It is simply lost
                    pass
        else:
            # misplay!
            self.discard_pile.append(card)
            print ("That was a bad idea!")
            print (ascii_art.kaboom)
            self.add_red_coin()
        self.print_piles()
        self.next_player()

    def clue(self, clue):
        "Action: give a clue."
        hint = clue[0].upper()  # so cr is valid to clue Red
        if not hint in "12345RBGWY":
            raise ValueError("%s is not a valid clue."%hint)
        self.remove_blue_coin() # will raise if no blue coin left

        print (self.current_player_name, "gives a clue:", hint)
        #  player = clue[1]  # if >=3 players
        for card in self.hands[self.other_player].cards:
            if hint in str(card):
                if hint in "12345":
                    card.number_clue = hint
                else:
                    card.color_clue = hint
        self.next_player()

    def examine_piles(self, *unused):
        "Action: look at the table."
        self.print_piles()

    def _bw_print_piles(self):
        print("    Discard:", self.discard_pile)
        for c in list(Color):
            print("%6s"%c, "pile:", self.piles[c])
        print ("     Coins:", self.blue_coins, "blue,", self.red_coins, "red")
    def _color_print_piles(self):
        print("       Deck:", len(self.deck.cards))
        print("    Discard:", self.discard_pile)
        for c in list(Color):
            print(c.colorize("%6s"%c, "pile:", self.piles[c]))
        print ("     Coins:", self.blue_coins, "blue,", self.red_coins, "red")
    def print_piles(self):
        self._color_print_piles()


    def next_player(self):
        "Switch to next player."
        try:
            self.other_player = self.current_player
            self.current_player = (self.current_player+1)%len(self.players)
        except TypeError:  # triggered when self.current_player=None
            self.current_player = 0
            self.other_player = 1

        self.current_player_name = '\033[1m%s\033[0m'%self.players[self.current_player]
        self.current_hand = self.hands[self.current_player]

        # other nice ideas: https://stackoverflow.com/questions/23416381/circular-list-iterator-in-python
        # itertools.cycle or players.append(pop(0))

    def command(self, args):
        "Action: Run a python command from Hanabi (yes, it is a cheat code: self is the current Game)."
        print('About to run `%s`'%args)
        try:
            exec(args)
        except Exception as e:
            print('Error:', e)

    @property
    def score(self):
        return sum(self.piles.values())

    def run(self):
        try:
            last_players = list(self.players)
            while last_players:
                if len(self.deck.cards) == 0:
                    print()
                    print("--> Last turns:",
                          " ".join(last_players),
                          "may still play once.")
                    try:
                        last_players.remove(self.players[self.current_player])
                    except ValueError:
                        pass  # if Alice 'x', she is removed but plays again
                self.turn(self.ai)
                if self.score == 25: raise StopIteration("it is perfect!")
#            print ("Game finished because deck exhausted")
        except (KeyboardInterrupt, EOFError, StopIteration) as e:
            print ('Game finished because of', e)
            pass
        self.save('autosave.py')

        print("\nOne final glance at the table:")
        print(self.starting_deck)
        self.print_piles()
        print("\nGoodbye. Your score is %d"%self.score)

    def save(self, filename):
        """Save starting deck and list of moves."""
        f = open(filename, 'w')
        f.write("""
players = %r
cards = %r
moves = %r
"""%( self.players,
              self.starting_deck,
              self.moves
        ))
        # fixme: seems that a deck's repr is its list of cards?

    def load(self, filename):
        """Load a saved game, replay the moves.

        A saved game consists of the variables players, cards and moves.
        """
        f = open(filename)
        # in python3, it is tricky to modify a variable with exec:
        #   https://stackoverflow.com/questions/15086040/behavior-of-exec-function-in-python-2-and-python-3
        # need globals for the Card and Color definitions, and loaded-dict for returned values
        loaded = {}
        for l in f:
            exec(l, globals(), loaded)

        print ('Loaded:', loaded)
        multi = False
        players = loaded['players']
        cards = loaded['cards']
        moves = loaded['moves']

        self.reset(players, multi, cards)
        # for m in moves:
        #     self.turn(m)
        ## was simpler, but infinity-looped when user made a mistake
        while moves:
            self.turn(moves)

if __name__ == "__main__":
    # print ("Red 4 is:", Card(Color.Red, 4))

    # deck = Deck()
    # print("Unshuffled:", deck)
    # deck.shuffle()
    # print("Shuffled:", deck)

    # hands = deck.deal(5)
    # alice, benji, clara, devon, elric = hands
    # players = {0:"Alice", 1: "Benji", 2:"Clara", 3:"Dante", 4:"Elric"}
    # for i, h in enumerate(hands): print("%s's hand is %s"%(players[i], h))

    # print ("Is B1 in Alice's hand?", "B1" in alice.cards)

    # try:
    #     card = alice.pop(1)
    #     print("Alice plays", card)
    # except ValueError:
    #     print("Alice can't play her 1st card")

    print ("\nLet's start a new game")
    game = Game(2)
    print ("Here are the hands:")
    print (game.hands)

    game.run()
