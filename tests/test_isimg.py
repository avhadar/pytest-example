import pytest
from complexnum import ComplexNum

# data for parametrized tests
testdata = [
    ((5, 0), False),
    ((0, 4), True),
    ((5, 6), False),
]

@pytest.mark.parametrize("mynum,expected", testdata)
def test_is_img(mynum, expected):
    # generate the complex number from input tuple (mynum)
    x = ComplexNum(*mynum)
    assert x.is_img() == expected