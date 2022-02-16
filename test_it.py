from pytest import raises
from .convert_roman_arabic import *

def test_string_input():
    """Test with a string as input, should raise ValueError"""
    with raises(ValueError):
        convert_arabic_to_roman_number(number="a")

def test_high_number():
    """Test with a number higher then 3000, should raise NotInRangeError"""
    with raises(NotInRangeError):
        convert_arabic_to_roman_number(number=3001)

def test_null():
    """Test with a number lower then 1, should raise NotInRangeError"""
    with raises(NotInRangeError):
        convert_arabic_to_roman_number(number=0)

def test_correct_numbers():
    """Test with numbers in range from 1 to 3000 should give a correct return 
    value"""
    assert convert_arabic_to_roman_number(2444) == 'MMCDXLIV'
    assert convert_arabic_to_roman_number(1845) == 'MDCCCXLV'
