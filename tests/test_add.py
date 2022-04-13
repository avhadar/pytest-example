import pytest
from complexnum import ComplexNum

def test_add_scalar():
    mynum = ComplexNum(2, 3)
    res = mynum + 5
    exp_res = ComplexNum(7, 8)
    assert res == exp_res

def test_add_cplx():
    mynum = ComplexNum(2, 3)
    toadd = ComplexNum(1, 4)
    res = mynum + toadd
    exp_res = ComplexNum(3, 7)
    assert res == exp_res

def test_add_zero():
    mynum = ComplexNum(2, 3)
    res = mynum + 0
    assert res == mynum
    # assert res.x == 2
    # assert res.y == 3
