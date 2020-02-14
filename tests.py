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


    def test_clock_output(self):
        pass


if __name__ == '__main__':
    unittest.main()
