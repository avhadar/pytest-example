import pytest
from complexnum import ComplexNum

# data for parametrized tests
scalar_data = [
    ((3, 1),  1, (3, 1)),
    ((2, 5), -2, (-4, -10)),
    ((3, -4), 5, (15, -20)),
]

cplx_data = [
    ((8, -5), (3, -2), (14, -31)),
    ((1, -2), (-2, 1), (0, 5)),
    ((-2, 3), (5, 4),  (-22, 7)),
]

# tests
def test_mult_zero():
    x = ComplexNum(5, 3)
    res = x * 0
    exp_res = ComplexNum(0, 0)
    assert res == exp_res

# parametrized tests
@pytest.mark.parametrize("mynum,scalar,expected", scalar_data)
def test_mult_scalar(mynum, scalar, expected):
    # generate the complex number from input tuple (mynum)
    x = ComplexNum(*mynum) 
    res = x * scalar
    exp_res = ComplexNum(*expected)
    assert res == exp_res

@pytest.mark.parametrize("mynum,other,expected", cplx_data)
def test_mult_cplx(mynum, other, expected):
    # generate the complex number from input tuple (mynum)
    x = ComplexNum(*mynum)
    y = ComplexNum(*other)
    res = x * y
    exp_res = ComplexNum(*expected)
    assert res == exp_res