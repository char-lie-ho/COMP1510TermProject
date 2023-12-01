from unittest import TestCase
from all_events import conduct_interview
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('random.randint', return_value=5)
    @patch('builtins.input', return_value='5')
    def test_conduct_interview_correct_guess_confirm_hired(self, _, __):
        character = {"Knowledge": 22, "Stress": 20, "Hired": False}
        conduct_interview(character)
        self.assertEqual(character["Hired"], True)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', return_value='2')
    def test_conduct_interview_incorrect_guess(self, _, __):
        character = {"Knowledge": 22, "Stress": 20, "Hired": False}
        conduct_interview(character)
        self.assertEqual(character["Hired"], False)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', return_value='a')
    def test_conduct_interview_invalid_input(self, _, __):
        character = {"Knowledge": 22, "Stress": 20, "Hired": False}
        conduct_interview(character)
        self.assertEqual(character["Hired"], False)

    @patch('builtins.input', return_value='one')
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_conduct_interview_invalid_input_test_print(self, mock_output, _, __):
        character = {"Knowledge": 22, "Stress": 20, "Hired": False}
        conduct_interview(character)
        printed_text = mock_output.getvalue()
        expected_output = ("Oh, you can't even type numbers?!\nSorry, your skills and experience do not meet our "
                          "current needs.\nYour current stress is [Stress = 25]\n")
        self.assertEqual(expected_output, printed_text)
