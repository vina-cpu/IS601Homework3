'''My Calculator Test'''
import pytest
from calculator.operation import Operation

def test_addition():
    '''Test for working addition function'''
    assert Operation.add(2,2) == 4
    assert Operation.add(2, -3) == -1
    assert Operation.add(-4, 4) == 0
    assert Operation.add(-2, -6) == -8
    assert Operation.add(0, 1) == 1
    assert Operation.add(1, 0) == 1

def test_subtraction():
    '''Test for working subtraction function'''
    assert Operation.subtract(2,2) == 0
    assert Operation.subtract(5, -4) == 9
    assert Operation.subtract(-3, 4) == -7
    assert Operation.subtract(-2, -5) == 3
    assert Operation.subtract(1, 0) == 1
    assert Operation.subtract(0, 1) == -1

def test_multiplication():
    '''Test for working multiplication function'''
    assert Operation.multiply(3,4) == 12
    assert Operation.multiply(2, -6) == -12
    assert Operation.multiply(-4, 2) == -8
    assert Operation.multiply(-3, -5) == 15
    assert Operation.multiply(3,0) == 0

def test_division():
    '''Test for working division function'''
    assert Operation.divide(6, 3) == 2
    assert Operation.divide(2, 1) == 2
    assert Operation.divide(0, 3) == 0
    assert Operation.divide(-5, 2) == -2.5
    assert Operation.divide(2, -1) == -2
    assert Operation.divide(-3, -3) == 1

def test_division_by_zero():
    '''Test for dividing by zero'''
    with pytest.raises(ValueError, match="Division by zero"):
        Operation.divide(3,0)
