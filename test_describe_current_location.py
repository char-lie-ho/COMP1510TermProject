from unittest import TestCase
from game import describe_current_location


class Test(TestCase):
    def test_describe_current_location_0by0(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = '🏠home'
        self.assertEqual(expected, describe_current_location(board, character))

    def test_describe_current_location_1by1(self):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        expected = '💼interview'
        self.assertEqual(expected, describe_current_location(board, character))

