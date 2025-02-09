'''My Calculator Test'''
import pytest
from calculator.operation import Operation

def test_addition():
    '''Test for working addition function'''
    assert Operation.add(2,2) == 4

def test_subtraction():
    '''Test for working subtraction function'''
    assert Operation.subtract(2,2) == 0

def test_multiplication():
    '''Test for working multiplication function'''
    assert Operation.multiply(3,4) == 12

def test_division():
    '''Test for working division function'''
    assert Operation.divide(6,3) == 2
    assert Operation.divide(2,1) == 2

def test_division_by_zero():
    '''Test for dividing by zero'''
    with pytest.raises(ValueError, match="Division by zero"):
        Operation.divide(3,0)
