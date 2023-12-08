from unittest import TestCase
from unittest.mock import patch
from initalize_game import game_difficulty
import io


class Test(TestCase):
    @patch('builtins.input', return_value='1')
    def test_game_difficulty_one(self, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                     "Hired": False, "Difficulty": None}
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                    "Hired": False, "Difficulty": 1}
        self.assertEqual(game_difficulty(character), expected)

    @patch('builtins.input', return_value='3')
    def test_game_difficulty_three(self, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                     "Hired": False, "Difficulty": None}
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                    "Hired": False, "Difficulty": 3}
        self.assertEqual(game_difficulty(character), expected)

    @patch('builtins.input', side_effect=['3.5', '3'])
    def test_game_difficulty_incorrect_float_then_three(self, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                     "Hired": False, "Difficulty": None}
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                    "Hired": False, "Difficulty": 3}
        self.assertEqual(game_difficulty(character), expected)

    @patch('builtins.input', side_effect=['one', '1'])
    def test_game_difficulty_incorrect_float_alpha_then_one(self, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                     "Hired": False, "Difficulty": None}
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                    "Hired": False, "Difficulty": 1}
        self.assertEqual(game_difficulty(character), expected)

    @patch('builtins.input', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_difficult_output_one(self, mock_output, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                     "Hired": False, "Difficulty": None}
        game_difficulty(character)
        difficulty_printed_this = mock_output.getvalue()
        expected_output = "Great! I like your choice.\n"
        self.assertEqual(expected_output, difficulty_printed_this)

    @patch('builtins.input', side_effect=['one', 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_difficult_output_incorrect_then_one(self, mock_output, _):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Knowledge": 0, "Term": 1, "Stress": 0, "Name": 'Charlie',
                     "Hired": False, "Difficulty": None}
        game_difficulty(character)
        difficulty_printed_this = mock_output.getvalue()
        expected_output = "Oh, you can't even type numbers?!\nGreat! I like your choice.\n"
        self.assertEqual(expected_output, difficulty_printed_this)
