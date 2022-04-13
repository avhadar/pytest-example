import pytest
from complexnum import ComplexNum

# data for parametrized tests
testdata = [
    ((5, 0), True),
    ((0, 4), False),
    ((5, 6), False),
]

@pytest.mark.parametrize("mynum,expected", testdata)
def test_is_real(mynum, expected):
    # generate the complex number from input tuple (mynum)
    x = ComplexNum(*mynum) # alternative to: x = ComplexNum(mynum[0], mynum[1])
    assert x.is_real() == expected