import unittest
from problem import *

class TestProblem(unittest.TestCase):

    #111.804s
    def test_exemplo_1(self):
        self.assertEqual(my_sum(50000, 10000, 40000), 15001)

    #0.001s
    def test_exemplo_2(self):
        self.assertEqual(my_sum_2(50000, 10000, 40000), 15001)

    #0.012s
    def test_exemplo_3(self):
        self.assertEqual(my_sum_3(50000, 10000, 40000), 15001)


if __name__ == '__main__':
    unittest.main()