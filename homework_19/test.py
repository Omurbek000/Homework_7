# test.py
import unittest
from main import Functions

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.functions = Functions()

    def test_add(self):
        self.assertEqual(self.functions.add(2, 3), 5)
        self.assertEqual(self.functions.add(-1, 1), 0)
        self.assertEqual(self.functions.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.functions.subtract(5, 3), 2)
        self.assertEqual(self.functions.subtract(-1, 1), -2)
        self.assertEqual(self.functions.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.functions.multiply(2, 3), 6)
        self.assertEqual(self.functions.multiply(-1, 1), -1)
        self.assertEqual(self.functions.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(self.functions.divide(6, 3), 2)
        self.assertEqual(self.functions.divide(-2, 1), -2)
        self.assertEqual(self.functions.divide(-2, -1), 2)

    def test_is_even(self):
        self.assertTrue(self.functions.is_even(2))
        self.assertFalse(self.functions.is_even(3))
        self.assertTrue(self.functions.is_even(-2))
        self.assertFalse(self.functions.is_even(-3))

    def test_is_odd(self):
        self.assertFalse(self.functions.is_odd(2))
        self.assertTrue(self.functions.is_odd(3))
        self.assertFalse(self.functions.is_odd(-2))
        self.assertTrue(self.functions.is_odd(-3))

    def test_is_positive(self):
        self.assertTrue(self.functions.is_positive(2))
        self.assertFalse(self.functions.is_positive(-2))
        self.assertFalse(self.functions.is_positive(0))

    def test_is_negative(self):
        self.assertFalse(self.functions.is_negative(2))
        self.assertTrue(self.functions.is_negative(-2))
        self.assertFalse(self.functions.is_negative(0))

    def test_is_zero(self):
        self.assertFalse(self.functions.is_zero(2))
        self.assertFalse(self.functions.is_zero(-2))
        self.assertTrue(self.functions.is_zero(0))

    def test_is_positive_or_zero(self):
        self.assertTrue(self.functions.is_positive_or_zero(2))
        self.assertFalse(self.functions.is_positive_or_zero(-2))
        self.assertTrue(self.functions.is_positive_or_zero(0))

