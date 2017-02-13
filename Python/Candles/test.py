import unittest
import problem

class TestProblem(unittest.TestCase):

    def test_candle_1(self):
        self.assertEqual(problem.candles(5, 2), 9)

    def test_candle_2(self):
        self.assertEqual(problem.candles(1, 2), 1)

    def test_candle_3(self):
        self.assertEqual(problem.candles(3, 3), 4)

    def test_candle_4(self):
        self.assertEqual(problem.candles(11, 3), 16)

    def test_candle_4_2(self):
        self.assertEqual(problem.candles_2(11, 3), 16)

if __name__ == '__main__':
    unittest.main()