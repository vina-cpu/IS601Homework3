'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test for working addition function'''
    assert add(2,2) == 4

def test_subtraction():
    '''Test for working subtraction function'''
    assert subtract(2,2) == 0
    