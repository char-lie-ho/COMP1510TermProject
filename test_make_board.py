from unittest import TestCase
from unittest.mock import patch
from game import make_board


class Test(TestCase):
    @patch('random.choice', side_effect=['📚library', '🏫classroom'])
    def test_make_board_2by2(self, _):
        actual = make_board(2, 2)
        expected = {(0, 0): '🏠home', (0, 1): '📚library', (1, 0): '🏫classroom', (1, 1): '💼interview'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['📚library', '🏫classroom', '📖study room', '📚library',
                                         '🏫classroom', '💻hackathon', '🚶street'])
    def test_make_board_3by3(self, _):
        actual = make_board(3, 3)
        expected = {(0, 0): '🏠home', (0, 1): '📚library', (0, 2): '🏫classroom', (1, 0): '📖study room',
                    (1, 1): '📚library', (1, 2): '🏫classroom', (2, 0): '💻hackathon', (2, 1): '🚶street',
                    (2, 2): '💼interview'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['📚library', '🏫classroom', '💻hackathon', '🚶street'])
    def test_make_board_2by3(self, _):
        actual = make_board(2, 3)
        expected = {(0, 0): '🏠home', (0, 1): '📚library', (0, 2): '🏫classroom', (1, 0): '💻hackathon',
                    (1, 1): '🚶street', (1, 2): '💼interview'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['🏫classroom', '📚library', '💻hackathon', '🚶street'])
    def test_make_board_3by2(self, _):
        actual = make_board(3, 2)
        expected = {(0, 0): '🏠home', (0, 1): '🏫classroom', (1, 0): '📚library', (1, 1): '💻hackathon',
                    (2, 0): '🚶street', (2, 1): '💼interview'}
        self.assertEqual(expected, actual)
