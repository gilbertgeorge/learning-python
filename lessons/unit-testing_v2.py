import unittest
from calc_test import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(5, 1)
        print('setUp method')

    def tearDown(self):
        print('tearDown method')

    def test_add(self):
        self.assertEqual(self.calc.add(), 6)
        self.calc.first = 8
        self.calc.second = 2
        self.assertEqual(self.calc.add(), 10)
        print('test_add method')

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 4)
        self.calc.first = 8
        self.calc.second = 2
        self.assertEqual(self.calc.subtract(), 6)
        print('test_subtract method')
