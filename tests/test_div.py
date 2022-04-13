import pytest
import math
from complexnum import ComplexNum

# data for parametrized tests
scalar_data = [
    ((3, 1),  1, (3, 1)),
    ((2, 5), -2, (-1, -2.5)),
    ((12, -8), 4, (3, -2)),
]

cplx_data = [
    ((4, 6), (3, 2), (1.8462, 0.7692)),
    ((2, 1), (1, 1), (1.5, -0.5)),
    ((-2.5, 4), (0, -5), (-0.8, -0.5)),
]

# tests
def test_div_scalar_zero():
    # try to divide by zero and generate error
    with pytest.raises(ZeroDivisionError):
        x = ComplexNum(5, 3)
        res = x / 0

# parametrized tests
@pytest.mark.parametrize("mynum,scalar,expected", scalar_data)
def test_div_scalar(mynum, scalar, expected):
    # generate the complex number from input tuple (mynum)
    x = ComplexNum(*mynum)
    res = x / scalar
    exp_res = ComplexNum(*expected)
    assert res == exp_res

@pytest.mark.parametrize("mynum,other,expected", cplx_data)
def test_div_cplx(mynum, other, expected):
    # generate the complex number from input tuple (mynum)
    x = ComplexNum(*mynum)
    y = ComplexNum(*other)
    res = x / y
    exp_res = ComplexNum(*expected)
    # comparison of real and imaginary parts as floating point numbers is tricky 
    # -> use rounding or difference with tolerance
    assert round(res.real(), 4) == round(exp_res.real(), 4)
    assert round(res.img(), 4) == round(exp_res.img(), 4)