import unittest
import calculator


class CalculatorTest(unittest.TestCase):
    def mathing_func_test(self):
        self.assertEqual(calculator.mathing_func(2, 2, "+"), 4)
