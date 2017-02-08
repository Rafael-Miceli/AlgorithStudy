import unittest
from problem import *

class TestProblem(unittest.TestCase):

    def test_box_1(self):
        self.assertEqual(apple_boxes(5), -15)

    def test_box_2(self):
        self.assertEqual(apple_boxes(15), -120)

    def test_box_3(self):
        self.assertEqual(apple_boxes(36), 666)

    def test_box_4(self):
        self.assertEqual(apple_boxes(1), -1)

    def test_box_5(self):
        self.assertEqual(apple_boxes(100000), 5000050000)



    def test_box_1_2(self):
        self.assertEqual(apple_boxes_deterministically(5), -15)

    def test_box_2_2(self):
        self.assertEqual(apple_boxes_deterministically(15), -120)

    def test_box_3_2(self):
        self.assertEqual(apple_boxes_deterministically(36), 666)

    def test_box_4_2(self):
        self.assertEqual(apple_boxes_deterministically(1), -1)

    def test_box_5_2(self):
        self.assertEqual(apple_boxes_deterministically(100000), 5000050000.0)


if __name__ == '__main__':
    unittest.main()