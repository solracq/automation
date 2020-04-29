'''
@author Solracq
'''
import pytest
import math

@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
    num = 7
    assert num * num == 49

@pytest.mark.others
def testquality():
    a = 7
    b = 9
    assert a != b

@pytest.mark.others
def test_module():
    a = 7
    b = 2
    assert a - ( b * ( a // b ) ) == 1
