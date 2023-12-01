from unittest import TestCase
from game import character_advance


class Test(TestCase):
    def test_character_advance_False(self):
        character = {"Knowledge": 2, "Term": 1}
        expected = False
        self.assertEqual(expected, character_advance(character))

    def test_character_advance_True_to_term2(self):
        character = {"Knowledge": 5, "Term": 1}
        expected = True
        self.assertEqual(expected, character_advance(character))

    def test_character_advance_True_to_term3(self):
        character = {"Knowledge": 10, "Term": 2}
        expected = True
        self.assertEqual(expected, character_advance(character))

    def test_character_advance_True_to_term4(self):
        character = {"Knowledge": 15, "Term": 3}
        expected = True
        self.assertEqual(expected, character_advance(character))

    def test_character_advance_False_reached_max(self):
        character = {"Knowledge": 20, "Term": 4}
        expected = False
        self.assertEqual(expected, character_advance(character))
