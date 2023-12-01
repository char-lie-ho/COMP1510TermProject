from unittest import TestCase
from game import advance
from unittest.mock import patch
import io


class Test(TestCase):
    def test_advance_to_term2(self):
        character = {"Term": 1, "Stress": 20}
        advance(character)
        self.assertEqual(character["Term"], 2)
        self.assertEqual(character["Stress"], 15)

    def test_advance_to_term3(self):
        character = {"Term": 2, "Stress": 14}
        advance(character)
        self.assertEqual(character["Term"], 3)
        self.assertEqual(character["Stress"], 9)

    def test_advance_to_term3_0stress(self):
        character = {"Term": 2, "Stress": 2}
        advance(character)
        self.assertEqual(character["Term"], 3)
        self.assertEqual(character["Stress"], 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_advance_print(self, mock_output):
        character = {"Term": 1, "Stress": 17}
        advance(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = ('  ______              _ _            _     _ \n' 
                           ' |  ____|            | | |          | |   | |\n'
                           ' | |__  __  _____ ___| | | ___ _ __ | |_  | |\n'
                           ' |  __| \ \/ / __/ _ \ | |/ _ \ |_ \| __| | |\n'
                           ' | |____ >  < (_|  __/ | |  __/ | | | |_  |_|\n'
                           ' |______/_/\_\___\___|_|_|\___|_| |_|\__| (_)\n\n'
                           'You are now in Term 2\n'
                           'After the term break, you are more refreshed! [Stress: 12]\n')
        self.assertEqual(expected_output, the_game_printed_this)
