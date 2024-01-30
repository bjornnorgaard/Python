import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
