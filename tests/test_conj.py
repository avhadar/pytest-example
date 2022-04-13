import pytest
from complexnum import ComplexNum

def test_conj_real():
    x = ComplexNum(5)
    assert x.conj() == x

def test_conj_img():
    x = ComplexNum(0, -5)
    exp_res = ComplexNum(0, 5)
    assert x.conj() == exp_res

def test_conj_mixed():
    x = ComplexNum(3, 5)
    exp_res = ComplexNum(3, -5)
    assert x.conj() == exp_res