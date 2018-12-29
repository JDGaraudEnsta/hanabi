"""
Unitary testin of Deck.
"""

import unittest

from deck import Card, Color


class DeckTest(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        "Card Red1 is good"
        r1 = Card(Color.Red, 1)
        self.assertEqual(str(r1), "R1")

    def test2(self):
        "Test assertions"
        with self.assertRaises(AssertionError):
            print(Card(Color.Red, 0))
        with self.assertRaises(AssertionError):
            print(Card(Color.Red, 6))


if __name__ == '__main__':
    unittest.main()
