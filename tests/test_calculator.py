'''My Tests for Operation Class and Calculation Class'''
import pytest
from calculator.operation import Operation
from calculator.calculation import Calculation

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

def test_calculation_add():
    '''Test for adding inside of a Calculation instance'''
    assert Calculation(2, 3, Operation.add).do() == 5

def test_calculation_subtract():
    '''Test for subtracting inside of a Calculation instance'''
    assert Calculation(2, 3, Operation.subtract).do() == -1

def test_calculation_multiply():
    '''Test for multiplying inside of a Calculation instance'''
    assert Calculation(4,5, Operation.multiply).do() == 20

def test_calculation_divide():
    '''Test for dividing inside of a Calculation instance'''
    assert Calculation(4 , 2, Operation.divide).do() == 2

def test_calculation_geta():
    '''Test for getting a from a Calculation instance'''
    assert Calculation(3, 1, Operation.add).getA() == 3

def test_calculation_getb():
    '''Test for getting b from a Calculation instance'''
    assert Calculation(3, 1, Operation.subtract).getB() == 1

def test_calculation_getoperation():
    '''Test for getting operation from a Calculation instance'''
    assert Calculation(3,1,Operation.multiply).getOperation().__name__==Operation.multiply.__name__

def test_calculation_seta():
    '''Test for setting a in a Calculation instance'''
    mycalc = Calculation(3, 1, Operation.subtract)
    mycalc.setA(2)
    assert mycalc.getA() == 2

def test_calculation_setb():
    '''Test for setting b in a Calculation instance'''
    mycalc = Calculation(3, 1, Operation.subtract)
    mycalc.setB(2)
    assert mycalc.getB() == 2

def test_calculation_setoperation():
    '''Test for setting a new operation in a Calculation instance'''
    mycalc = Calculation(3, 1, Operation.subtract)
    mycalc.setOperation(Operation.add)
    assert mycalc.getOperation().__name__ == Operation.add.__name__
