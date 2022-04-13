import pytest
from complexnum import ComplexNum

def test_img_real():
    x = ComplexNum(5, 0)
    assert x.img() == 0

def test_img_img():
    x = ComplexNum(0, -1)
    assert x.img() == -1

def test_img_mixed():
    x = ComplexNum(-3, 9)
    assert x.img() == 9
