"""
Add a docstring
"""
from unittest import TestCase
from game import end_of_game


class Test(TestCase):
    def test_end_of_game_stressed_out(self):
        character = {"Stress": 53, "Hired": False}
        self.assertEqual(True, end_of_game(character))

    def test_end_of_game_still_surviving(self):
        character = {"Stress": 40, "Hired": False}
        self.assertEqual(False, end_of_game(character))

    def test_end_of_game_got_hired(self):
        character = {"Stress": 10, "Hired": True}
        self.assertEqual(True, end_of_game(character))
