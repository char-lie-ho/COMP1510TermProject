from unittest import TestCase
from unittest.mock import patch
from game import home
import io


class Test(TestCase):
    def test_home_start_from_10_stress(self):
        character = {"Stress": 10, "X-coordinate": 0, "Y-coordinate": 0}
        home(character)
        self.assertEqual(character['Stress'], 7)

    def test_home_start_from_1_stress(self):
        character = {"Stress": 1, "X-coordinate": 0, "Y-coordinate": 0}
        home(character)
        self.assertEqual(character['Stress'], 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_home_start_from_6_stress(self, mock_output):
        character = {"Stress": 6, "X-coordinate": 0, "Y-coordinate": 0}
        home(character)
        printed_cat_and_status = mock_output.getvalue()
        expected_output = ("--------------------------------------------------------------------------------\n"
                           "   |\      _,,,---,,_\n"
                           "   /,`.-'`'    -.  ;-;;,_\n"
                           "  |,4-  ) )-,_..;\ (  `'-'\n"
                           " '---''(_/--'  `-'\_) \n"
                           "Your cat welcomes you home\n"
                           "You have lower your stress [Stress = 3]\n")
        self.assertEqual(expected_output, printed_cat_and_status)
