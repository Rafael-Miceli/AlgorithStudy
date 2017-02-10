import unittest
import problem

class TestProblem(unittest.TestCase):
    
    def test_rounder_1(self):
        self.assertEqual(problem.rounders(15), 20)
    
    def test_rounder_2(self):
        self.assertEqual(problem.rounders(1234), 1000)

    def test_rounder_3(self):
        self.assertEqual(problem.rounders(1445), 2000)

    def test_rounder_4(self):
        self.assertEqual(problem.rounders(14), 10)

    def test_rounder_5(self):
        self.assertEqual(problem.rounders(10), 10)

    def test_rounder_6(self):
        self.assertEqual(problem.rounders(99), 100)

    def test_rounder_7(self):
        self.assertEqual(problem.rounders(9999), 10000)

    def test_rounder_8(self):
        self.assertEqual(problem.rounders(1), 1)

    def test_rounder_9(self):
        self.assertEqual(problem.rounders(5), 5)

if __name__ == '__main__':
    unittest.main()