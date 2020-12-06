from app.roman_numerals import parse
from pytest import mark


@mark.parametrize("s,expected", [("IX", 9), ("X", 10)])
def test_roman_numeral_parser(s, expected):
    value = parse(s)
    assert value == expected
