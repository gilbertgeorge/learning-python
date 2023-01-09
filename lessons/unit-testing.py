import unittest
import calc_test


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # tests for the add() function
        self.assertEqual(calc_test.add(6, 4), 10)
        self.assertEqual(calc_test.add(6, -4), 2)
        self.assertEqual(calc_test.add(-6, 4), -2)
        self.assertEqual(calc_test.add(-6, -4), -10)

    def test_subtract(self):
        self.assertEqual(calc_test.subtract(7, 5), 2)
        self.assertEqual(calc_test.subtract(7, 10), -3)
        self.assertEqual(calc_test.subtract(7, -3), 10)
        self.assertEqual(calc_test.subtract(-7, 3), -10)
        self.assertEqual(calc_test.subtract(-7, -3), -4)

    def test_multiply(self):
        self.assertEqual(calc_test.multiply(1, 5), 5)
        self.assertEqual(calc_test.multiply(0, 5), 0)
        self.assertEqual(calc_test.multiply(1, -5), -5)
        self.assertEqual(calc_test.multiply(-1, 5), -5)
        self.assertEqual(calc_test.multiply(-1, -5), 5)

    def test_divide(self):
        self.assertEqual(calc_test.divide(10, 5), 2)
        self.assertEqual(calc_test.divide(10, -5), -2)
        self.assertEqual(calc_test.divide(-10, 5), -2)
        self.assertEqual(calc_test.divide(-10, -5), 2)
        self.assertRaises(ValueError, calc_test.divide, 5, 0)


def unit_testing():
    print('unit test')


if __name__ == '__main__':
    unit_testing()
