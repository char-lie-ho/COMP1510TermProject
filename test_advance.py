from unittest import TestCase
from game import advance
from unittest.mock import patch
import io


class Test(TestCase):
    def test_advance_to_term2(self):
        character = {"Term": 1, "Stress": 20}
        expected = {"Term": 2, "Stress": 15}
        self.assertEqual(expected, advance(character))

    def test_advance_to_term3(self):
        character = {"Term": 2, "Stress": 14}
        expected = {"Term": 3, "Stress": 9}
        self.assertEqual(expected, advance(character))

    def test_advance_to_term3_0stress(self):
        character = {"Term": 2, "Stress": 0}
        expected = {"Term": 3, "Stress": 0}
        self.assertEqual(expected, advance(character))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_advance_print(self, mock_output):
        character = {"Term": 1, "Stress": 17}
        advance(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = ('Excellent!\nYou are now in Term 2\n'
                           'After the term break, you are more refreshed! [Stress: 12]\n')
        self.assertEqual(expected_output, the_game_printed_this)
