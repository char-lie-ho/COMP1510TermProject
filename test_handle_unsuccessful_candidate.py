from unittest import TestCase
from game import handle_unsuccessful_candidate
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_unsuccessful_candidate_print_stress_5(self, mock_output):
        character = {"Knowledge": 5, "Stress": 5}
        handle_unsuccessful_candidate(character)
        printed_text = mock_output.getvalue()
        expected_output = ('Sorry, your skills and experience do not meet our current needs.\n'
                           'Please try to study more and come back.\n'
                           'You are exhausted from this interview. [Stress = 15]\n'
                           'However, you also learn from this. [Knowledge = 6]\n')
        self.assertEqual(expected_output, printed_text)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_unsuccessful_candidate_print_stress_22(self, mock_output):
        character = {"Knowledge": 9, "Stress": 22}
        handle_unsuccessful_candidate(character)
        printed_text = mock_output.getvalue()
        expected_output = ('Sorry, your skills and experience do not meet our current needs.\n'
                           'Please try to study more and come back.\n'
                           'You are exhausted from this interview. [Stress = 32]\n'
                           'However, you also learn from this. [Knowledge = 10]\n')
        self.assertEqual(expected_output, printed_text)
