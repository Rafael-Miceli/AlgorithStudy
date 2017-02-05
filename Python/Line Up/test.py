import unittest
from problem import *

class TestProblem(unittest.TestCase):

    def test_line_1(self):
        self.assertEqual(line_up("LLARL"), 3)

    def test_line_2(self):
        self.assertEqual(line_up("RLR"), 1)

    def test_line_3(self):
        self.assertEqual(line_up(""), 0)

if __name__ == '__main__':
    unittest.main()