import unittest
import problem

class TestProblem(unittest.TestCase):
    
    def test_roundness_1(self):
        self.assertEqual(problem.increaseNumberRoundness(902200100), True)

    def test_roundness_2(self):
        self.assertEqual(problem.increaseNumberRoundness(11000), False)

    def test_roundness_3(self):
        self.assertEqual(problem.increaseNumberRoundness(888), False)
    
    def test_roundness_4(self):
        self.assertEqual(problem.increaseNumberRoundness(106611), True)

if __name__ == '__main__':
    unittest.main()

