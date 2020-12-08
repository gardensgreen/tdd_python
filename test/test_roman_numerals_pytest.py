from roman_numerals import parse

def test_roman_numeral_parser():
    value = parse("IX")
    assert value == 9
