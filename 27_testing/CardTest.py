import unittest
from random import choice

from Card import Card


class CardTest(unittest.TestCase):
    def setUp(self):
        self.suit = choice(Card.suit_allowed)
        self.value = choice(Card.value_allowed)
        self.card = Card(self.suit, self.value)

    def test_init(self):
        print(self.card)

    def test_rept(self):
        self.assertEqual(str(self.card), f"{self.value} of {self.suit}")


if __name__ == '__main__':
    unittest.main()
