import unittest
import hanabi



class ColorTest(unittest.TestCase):
    def test_str(self):
        colors = [(31, "Red"), (32, "Green"), (34, "Blue"), (33, "Yellow"), (37, "White")]
        trouve = True
        for (c, color) in colors:
            a = str(hanabi.deck.Color(c))
            self.assertEqual(a, color)
    def test_valid(self):
        for s in (54, 78, 46, 54, -5, 3):
            self.assertRaises(ValueError, hanabi.deck.Color, s)


class CardTest(unittest.TestCase):
    def test_not_equal_cards(self):
        c1 = hanabi.deck.Card('B', 4)
        c2 = hanabi.deck.Card('R', 4)
        self.assertNotEqual(c1, c2)

    def test_equal_cards(self):
        c1 = hanabi.deck.Card('R', 4)
        string_card = "R4"
        self.assertEqual(c1, string_card)

    def test_number(self):
        #self.assertRaises(hanabi.deck.Card('R', 7),  AssertionError)
        with self.assertRaises(AssertionError):
            hanabi.deck.Card('R', 7)
    # TODO: itertools.product to test that all cards are possible

class HandTest(unittest.TestCase):
    # test __special__ functions


    # test normal functions
    def setUp(self):
        self.deck1 = hanabi.deck.Deck()
        self.hand1 = hanabi.deck.Hand(self.deck1)
        self.deck1.shuffle()

        self.deck3 = hanabi.deck.Deck()
        self.hand3 = hanabi.deck.Hand(self.deck3, 1)

    def test_basic_hand(self):
        self.assertEqual(str(self.hand3), hanabi.deck.Card(hanabi.deck.Color.Red, 1).str_color())

    def test_len(self):
        self.assertEqual(5, len(self.hand1))
    
    def test_shuffle(self):
        self.deck1.shuffle()
        mem = str(self.deck1)[0:len(repr(self.hand1))]
        self.hand2 = hanabi.deck.Hand(self.deck1)
        self.assertEqual(str(self.hand2), mem)



class DeckTest(unittest.TestCase):
    # test __special__ functions
    

    # test normal functions
    def setUp(self):
        pass


    def test_shuffle(self):
        pass


    def test_draw(self):
        pass

    def test_deal(self):
        pass


class DeckTest2(unittest.TestCase):
    pass



class GameTest(unittest.TestCase):

    def setUp(self):
        self.unshuffled_game = hanabi.Game()
        self.random_game = hanabi.Game()
        # ... group G here! 
        self.predefined_game = hanabi.Game()
        # ...


    # lines 193, 227
    def test_A1(self):
        game = hanabi.Game(2)
        game.quiet = True
        game.turn('p3')  # check that we can play blindly

    # lines 227, 261
    def test_B1(self):
        pass


    # lines 261, 295
    def test_play_R2_over_R1(self):
        pass


    # lines 295, 329



    # lines 329, 363

    

    # lines 363, 397



    # lines 397, 431

    def test_nb_players(self):
        for i in range (2,6):
            game = hanabi.Game(i)
            game.quiet = True
            ai = hanabi.ai.Cheater(game)
            game.ai = ai
            game.run()





if __name__ == '__main__':
    unittest.main()
