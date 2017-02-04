import unittest
from problem import *

class TestProblem(unittest.TestCase):

    def test_cast_1(self):
        self.assertEqual(castwell(1, 1, 1), 1)
    
    def test_cast_2(self):
        self.assertEqual(castwell(1, 2, 2), 8)

    def test_cast_3(self):
        self.assertEqual(castwell(6, 5, 3), 128)

    #0.010s
    def test_cast_4(self):
        self.assertEqual(castwell(1, 1, 10000), 333383335000)

    #Excede profundidade maxima de recursão
    # def test_cast_5(self):
    #     self.assertEqual(castwell_2(1, 1, 10000), 333383335000)


if __name__ == '__main__':
    unittest.main()