from tkinter import E
import unittest
from activities import eat, nap


class ActivitiyTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat_healthy: should have positive message"""
        self.assertEqual(
            eat('broccoli', True),
            "I'm eating broccoli, because my body is a temple"
        )

    def test_eat_un_healthy(self):
        """eat_un_healthy: should warn us"""
        self.assertEqual(
            eat('pizza', False),
            "I'm eating pizza, because YOLO"
        )

    def test_short_nap(self):
        """short_nap : is refreshing"""
        self.assertEqual(
            nap(1),
            "You sleft for 1 hours. Short naps are refreshing"
        )

    def test_long_nap(self):
        """long_nap : long nap is NOT refreshing"""
        self.assertEqual(
            nap(5),
            "You sleft for 5 hours. long naps are NOT refreshing"
        )


if __name__ == '__main__':
    unittest.main()
