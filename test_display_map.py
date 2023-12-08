"""
Add a docstring
"""
from unittest import TestCase
from unittest.mock import patch
from game import display_map
import io


@patch('sys.stdout', new_callable=io.StringIO)
class Test(TestCase):
    def test_display_map_at_top_left_2by2(self, mock_output):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        display_map(0, 0, board)
        printed_map = mock_output.getvalue()
        expected_output = "\t ┍ ⎯ ┬ ⎯ ┑\n\t | x |   |\n\t ├ ⎯ ┼ ⎯ ┤\n\t |   |   |\n\t ┕ ⎯ ┴ ⎯ ┙\n"
        self.assertEqual(expected_output, printed_map)

    def test_display_map_at_top_right_2by2(self, mock_output):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        display_map(1, 0, board)
        printed_map = mock_output.getvalue()
        expected_output = "\t ┍ ⎯ ┬ ⎯ ┑\n\t |   | x |\n\t ├ ⎯ ┼ ⎯ ┤\n\t |   |   |\n\t ┕ ⎯ ┴ ⎯ ┙\n"
        self.assertEqual(expected_output, printed_map)

    def test_display_map_at_bottom_left_2by2(self, mock_output):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        display_map(0, 1, board)
        printed_map = mock_output.getvalue()
        expected_output = "\t ┍ ⎯ ┬ ⎯ ┑\n\t |   |   |\n\t ├ ⎯ ┼ ⎯ ┤\n\t | x |   |\n\t ┕ ⎯ ┴ ⎯ ┙\n"
        self.assertEqual(expected_output, printed_map)

    def test_display_map_at_bottom_right_2by2(self, mock_output):
        board = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        display_map(1, 1, board)
        printed_map = mock_output.getvalue()
        expected_output = "\t ┍ ⎯ ┬ ⎯ ┑\n\t |   |   |\n\t ├ ⎯ ┼ ⎯ ┤\n\t |   | x |\n\t ┕ ⎯ ┴ ⎯ ┙\n"
        self.assertEqual(expected_output, printed_map)
