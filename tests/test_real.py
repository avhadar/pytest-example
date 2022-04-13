import pytest
from complexnum import ComplexNum

def test_real_real():
    x = ComplexNum(5, 0)
    assert x.real() == 5

def test_real_img():
    x = ComplexNum(0, -1)
    assert x.real() == 0

def test_real_mixed():
    x = ComplexNum(-3, 9)
    assert x.real() == -3
