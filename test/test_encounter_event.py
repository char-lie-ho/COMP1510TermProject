from unittest import TestCase
from unittest.mock import patch
from game import encounter_event


class Test(TestCase):
    @patch('random.random', return_value=0.8001010673223274)
    def test_encounter_event_no_encounter(self, _):
        expected = False
        self.assertEqual(expected, encounter_event())

    @patch('random.random', return_value=0.1297283073654331)
    def test_encounter_event_with_encounter(self, _):
        expected = True
        self.assertEqual(expected, encounter_event())

    @patch('random.random', return_value=0.2499999999999999)
    def test_encounter_event_upper_bound_with_encounter(self, _):
        expected = True
        self.assertEqual(expected, encounter_event())

    @patch('random.random', return_value=0.0000000000000000)
    def test_encounter_event_lower_bound_with_encounter(self, _):
        expected = True
        self.assertEqual(expected, encounter_event())

    @patch('random.random', return_value=0.2500000000000000)
    def test_encounter_event_lower_bound_no_encounter(self, _):
        expected = False
        self.assertEqual(expected, encounter_event())
