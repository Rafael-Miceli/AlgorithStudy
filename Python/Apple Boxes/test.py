import unittest
from problem import *

class TestProblem(unittest.TestCase):

    def test_box_1(self):
        self.assertEqual(apple_boxes(5), -15)


if __name__ == '__main__':
    unittest.main()