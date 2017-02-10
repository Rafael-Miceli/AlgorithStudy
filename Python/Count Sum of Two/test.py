import unittest
from problem import *

class TestProblem(unittest.TestCase):

    #111.804s
    # def test_exemplo_1(self):
    #     self.assertEqual(my_sum(50000, 10000, 40000), 15001)

    #0.001s
    def test_exemplo_2(self):
        self.assertEqual(my_sum_2(50000, 10000, 40000), 15001)

    #0.012s
    def test_exemplo_4(self):
        self.assertEqual(my_sum_3(6, 2, 4), 2)

    def test_exemplo_5(self):
        self.assertEqual(my_sum_2(6, 3, 3), 1)

    def test_exemplo_6(self):
        self.assertEqual(my_sum_2(10, 9, 11), 0)

    def test_exemplo_7(self):
        self.assertEqual(my_sum_2(24, 12, 12), 1)

    def test_exemplo_8(self):
        self.assertEqual(my_sum_2(93, 24, 58), 12)


if __name__ == '__main__':
    unittest.main()