import unittest
from app.roman_numerals import parse


class TestRomanNumerals(unittest.TestCase):
    def test_i(self):
        value = parse("I")

        self.assertEqual(value, 1)
