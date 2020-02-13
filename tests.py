import unittest
import kata

class KataTests(unittest.TestCase):

    def test_add(self):
        a = 1
        b = 2
        self.assertEqual(a*b, kata.multiply(a, b))

if __name__ == '__main__':
    unittest.main()
    
