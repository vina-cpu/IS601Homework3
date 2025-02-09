'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test for working addition function'''
    assert add(2,2) == 4

def test_subtraction():
    '''Test for working subtraction function'''
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test for working multiplication function'''
    assert multiply(3,4) == 12

def test_division():
    '''Test for working division function'''
    assert divide(6,3) == 2
    assert divide(2,1) == 2

def test_division_by_zero():
    '''Test for dividing by zero'''
    assert divide(3,1) == 3
