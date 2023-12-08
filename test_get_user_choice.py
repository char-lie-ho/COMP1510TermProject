from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class Test(TestCase):
    @patch('builtins.input', return_value='N')
    def test_get_user_choice_going_north(self, _):
        actual = get_user_choice(_)
        expected = 'N'
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='S')
    def test_get_user_choice_going_south(self, _):
        actual = get_user_choice(_)
        expected = 'S'
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='E')
    def test_get_user_choice_going_east(self, _):
        actual = get_user_choice(_)
        expected = 'E'
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='W')
    def test_get_user_choice_going_west(self, _):
        actual = get_user_choice(_)
        expected = 'W'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['A', 'B', 'C', 'D', 'E'])
    def test_get_user_choice_invalid_inputs_then_valid_input(self, _):
        actual = get_user_choice(_)
        expected = 'E'
        self.assertEqual(expected, actual)
