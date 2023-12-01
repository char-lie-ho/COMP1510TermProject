from unittest import TestCase
from game import validate_move


class Test(TestCase):
    def test_validate_move_invalid_move_north(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = 'N'
        expected = False
        self.assertEqual(expected, validate_move(board, character, direction))

    def test_validate_move_invalid_move_east(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        direction = 'E'
        expected = False
        self.assertEqual(expected, validate_move(board, character, direction))

    def test_validate_move_invalid_move_south(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        direction = 'S'
        expected = False
        self.assertEqual(expected, validate_move(board, character, direction))

    def test_validate_move_invalid_move_west(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = 'W'
        expected = False
        self.assertEqual(expected, validate_move(board, character, direction))

    def test_validate_move_valid_move_north(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        direction = 'N'
        expected = True
        self.assertEqual(expected, validate_move(board, character, direction))

    def test_validate_move_valid_move_east(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = 'E'
        expected = True
        self.assertEqual(expected, validate_move(board, character, direction))

    def test_validate_move_valid_move_south(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        direction = 'S'
        expected = True
        self.assertEqual(expected, validate_move(board, character, direction))

    def test_validate_move_valid_move_west(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        direction = 'W'
        expected = True
        self.assertEqual(expected, validate_move(board, character, direction))
