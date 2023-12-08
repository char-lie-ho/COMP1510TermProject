from unittest import TestCase
from move import move_character


class Test(TestCase):
    def test_move_character_north(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        direction = 'N'
        expected = {"X-coordinate": 1, "Y-coordinate": 0}
        self.assertEqual(expected, move_character(character, direction))

    def test_move_character_east(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        direction = 'E'
        expected = {"X-coordinate": 2, "Y-coordinate": 1}
        self.assertEqual(expected, move_character(character, direction))

    def test_move_character_south(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        direction = 'S'
        expected = {"X-coordinate": 1, "Y-coordinate": 2}
        self.assertEqual(expected, move_character(character, direction))

    def test_move_character_west(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        direction = 'W'
        expected = {"X-coordinate": 0, "Y-coordinate": 1}
        self.assertEqual(expected, move_character(character, direction))
