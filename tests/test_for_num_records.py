'''My Tests for conftest.py and generating an amount of records via input with Calculator and Calculation'''
from typing import Callable, List
import pytest
from faker import Faker
from calculator.operation import Operation
from calculator.calculation import Calculation
from calculator import Calculator
from calculator.history import History

fake = Faker()
operationsList: List[Callable[[float, float], float]] = [Operation.add, Operation.subtract, Operation.multiply, Operation.divide]

def test_num_records_calculation(a, b, oper, expected):
    '''Testing all types of Calculation via faker'''
    newcalc = Calculation.newCalc(a, b, oper)
    if b != 0:
        assert newcalc.do() == expected
    else:
        if oper.__name__ == Operation.divide.__name__:
            with pytest.raises(ValueError, match="Division by zero"):
                newcalc.do()

def test_num_records_calculation_divide_by_zero(a, b, oper, expected):
    '''Testing division by zero operation via conftest.py to show it works'''
    b = 0
    oper = Operation.divide
    newcalc = Calculation.newCalc(a, b, oper)
    with pytest.raises(ValueError, match="Division by zero"):
        newcalc.do()

def test_num_records_calculator(a, b, oper, expected):
    '''Testing all types of Calculator methods given data from faker'''
    History.clear_history()
    if b == 0:
        if oper.__name__ == Operation.divide.__name__:
            with pytest.raises(ValueError, match="Division by zero"):
                Calculator.newCalculation(a,b,oper)
        else:
            assert Calculator.newCalculation(a,b,oper) == expected
            assert len(History.get_history()) == 1
    else:
        assert Calculator.newCalculation(a,b,oper) == expected
        assert len(History.get_history()) == 1

def test_num_records_calculator_division_by_zero(a, b, oper, expected):
    '''Testing division by zero with Calculator methods given data from faker'''
    History.clear_history()
    b = 0
    oper = Operation.divide
    with pytest.raises(ValueError, match="Division by zero"):
        Calculator.newCalculation(a,b,oper)

def test_num_records_calculator_redo_last(a, b, oper, expected):
    '''Testing all redo calc functions with faker data'''
    History.clear_history()
    b = 1
    Calculator.newCalculation(a, b, oper)
    new = fake.random_number()
    while new == 0:
        new = fake.random_number()
    newoper = fake.random_element(operationsList)
    assert Calculator.redoLastCalcA(new) == oper(new, b)
    assert Calculator.redoLastCalcB(new) == oper(new, new)
    assert Calculator.redoLastCalcOperation(newoper) == newoper(new, new)
    newoper = Operation.divide
    assert Calculator.redoLastCalcOperation(newoper) == newoper(new, new)
    new2 = 0
    with pytest.raises(ValueError, match="Division by zero"):
        Calculator.redoLastCalcB(new2)

def test_num_records_calculator_redo(a, b, oper, expected):
    '''Testing redo calc functions with faker data'''
    History.clear_history()
    b = 1
    Calculator.newCalculation(a, b, oper)
    new = fake.random_number()
    while new == 0:
        new = fake.random_number()
    newoper = fake.random_element(operationsList)
    assert Calculator.redoCalcA(History.get_last_calc(), new)
    assert Calculator.redoCalcB(History.get_index_calc(0), new)
    assert Calculator.redoCalcOperation(History.get_index_calc(0), newoper)
    newoper = Operation.divide
    assert Calculator.redoCalcOperation(History.get_index_calc(0), newoper)
    new2 = 0
    with pytest.raises(ValueError, match="Division by zero"):
        Calculator.redoCalcB(History.get_last_calc(), new2)
