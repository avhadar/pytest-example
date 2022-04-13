import pytest
from complexnum import ComplexNum

@pytest.fixture
def my_number():
    '''Returns a complex number'''
    return ComplexNum(2, 3)

def test_subtract_scalar(my_number):
    res = my_number - 5
    exp_res = ComplexNum(-3, -2)
    assert res == exp_res

def test_subtract_cplx(my_number):
    tosub = ComplexNum(1, 4)
    res = my_number - tosub
    exp_res = ComplexNum(1, -1)
    assert res == exp_res