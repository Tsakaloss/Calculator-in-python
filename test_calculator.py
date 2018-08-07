import unittest
import calculator


class CalculatorTest(unittest.TestCase):
    def test_mathing_func(self):
        self.assertEqual(calculator.mathing_func(2, 2, "+"), 4)
