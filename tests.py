import unittest
import kata


class KataTests(unittest.TestCase):

    def test_update_lights_in_row(self):
        top_row = ['O', 'O', 'O', 'O']
        number_lights_on_top_row = 2
        colour = 'R'

        updated_top_row = kata.update_lights_in_row(number_lights_on_top_row, top_row, colour)

        expected_updated_top_row = ['R', 'R', 'O', 'O']
        self.assertEqual(expected_updated_top_row, updated_top_row)


    def test_berlin_clock(self):
        input = '12:56:01'
        expected_output = ['O', ['R', 'R', 'O', 'O'], ['R', 'R', 'O', 'O'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'O', 'O', 'O']]
        self.assertEqual(expected_output, kata.berlin_clock(input))

    def test_get_top_light_state(self):
        seconds = 1
        expected_output = 0
        self.assertEqual(expected_output, kata.get_number_lights_on_top_light(seconds))

    def test_get_number_lights_on_top_row(self):
        hours = 12
        expected_output = 2
        self.assertEqual(expected_output, kata.get_number_lights_on_top_row(hours))

    def test_get_number_lights_on_second_row(self):
        hours = 12
        expected_output = 2
        self.assertEqual(expected_output, kata.get_number_lights_on_second_row(hours))

    def test_get_number_lights_on_third_row(self):
        minutes = 56
        expected_output = 11
        self.assertEqual(expected_output, kata.get_number_lights_on_third_row(minutes))

    def test_get_number_lights_on_fourth_row(self):
        minutes = 56
        expected_output = 1
        self.assertEqual(expected_output, kata.get_number_lights_on_fourth_row(minutes))

    def test_parse_hours_from_time(self):
        input = '12:56:01'
        expected_output = 12
        self.assertEqual(expected_output, kata.parse_hours_from_time(input))

    def test_parse_minutes_from_time(self):
        input = '12:56:01'
        expected_output = 56

    def test_parse_seconds_from_time(self):
        input = '12:56:01'
        expected_output = 1

    def test_parse_time(self):
        expected_output =
if __name__ == '__main__':
    unittest.main()
