import pytest

def test_divisible_by_15(input_value3):
    assert input_value3 % 15 == 0

def test_divisible_by_mult_15(input_value2, input_value3):
    assert ((input_value2 // input_value3) + 4) % 15 == 0