import pytest
from complexnum import ComplexNum

def test_zero():
    x = ComplexNum(0, 0)
    assert abs(x) == 0

def test_pos():
    x = ComplexNum(3, 4)
    assert abs(x) == 5

def test_neg():
    x = ComplexNum(-3, -4)
    assert abs(x) == 5

def test_mixed():
    x = ComplexNum(6, -8)
    assert abs(x) == 10