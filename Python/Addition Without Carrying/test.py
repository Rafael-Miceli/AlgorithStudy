import unittest
from problem import *


class TestProblem(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(add_without_care_2(456, 1734), 1180)
    
    def test_add_2(self):
        self.assertEqual(add_without_care_2(999, 999), 888)

    def test_add_3(self):
        self.assertEqual(add_without_care_2(0, 0), 0)

    def test_add_4(self):
        self.assertEqual(add_without_care_2(99999, 0), 99999)

if __name__ == '__main__':
    unittest.main()