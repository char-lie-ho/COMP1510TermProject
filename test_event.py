from unittest import TestCase
from unittest.mock import patch
from game import event
import io


class Test(TestCase):
    @patch('builtins.input', side_effect=['A', 'B', 'C'])
    @patch('random.randint', side_effect=[40, 38, 40])
    def test_event_4_correct_input(self, _, __):
        character = {'Difficulty': 1, 'Knowledge': 5, 'Name': 'Charlie', 'Stress': 10}
        expected = {'Difficulty': 1, 'Knowledge': 8, 'Name': 'Charlie', 'Stress': 13}
        self.assertEqual(expected, event(character))

    @patch('builtins.input', side_effect=['', '', 'hi', 'i', 'like', 'cats'])
    @patch('random.randint', side_effect=[40, 38, 20, 10])
    def test_event_4_incorrect_correct_input(self, _, __):
        character = {'Difficulty': 2, 'Knowledge': 1, 'Name': 'Charlie', 'Stress': 10}
        expected = {'Difficulty': 2, 'Knowledge': 3, 'Name': 'Charlie', 'Stress': 14}
        self.assertEqual(expected, event(character))

    @patch('builtins.input', side_effect=['what', 'should', 'i', 'type?'])
    @patch('random.randint', side_effect=[23, 51, 27, 34])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_event_print(self, mock_output, _, __):
        character = {'Difficulty': 1, 'Knowledge': 1, 'Name': 'Charlie', 'Stress': 10}
        event(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = ("You discover an interesting Leetcode Question.🤔\n"
                           "(Hint: You can type anything to try to solve.)\n"
                           "You have finished 23%\nYou have finished 74%\n"
                           "You have finished 100%\nGreat job, Charlie!\n"
                           "You have learned from this. [Knowledge = 4]\n"
                           "However, you are more stressed now. [Stress = 13]\n")
        self.assertEqual(expected_output, the_game_printed_this)
