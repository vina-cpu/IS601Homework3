'''My History and Calculator Test'''
import pytest
from calculator.calculation import Calculation
from calculator.history import History
from calculator.operation import Operation
from calculator import Calculator


@pytest.fixture
def setup_history():
    '''clear history and add a couple calculations to set up the history'''
    History.clear_history()
    History.add_calculation(Calculation(2, 3, Operation.add))
    History.add_calculation(Calculation(5, 4, Operation.multiply))

def test_add_calculation(setup_history):
    '''test for adding a calculation to History class, and also testing the create Calculation'''
    newcalc = Calculation.create(4, 3, Operation.add)
    History.add_calculation(newcalc)
    assert History.get_last_calc() == newcalc

def test_get_history(setup_history):
    '''test for getting history from setup_history'''
    history = History.get_history()
    assert len(history) == 2

def test_set_history(setup_history):
    '''test for setting history'''
    History.set_history([Calculation(1, 1, Operation.multiply)])
    assert len(History.get_history()) == 1

def test_clear_history(setup_history):
    '''test for clearing history'''
    History.clear_history()
    assert len(History.get_history()) == 0

def test_get_last_calc(setup_history):
    '''test for getting last calculation'''
    recent = History.get_last_calc()
    assert recent.getA() == 5
    assert recent.getB() == 4
    assert recent.getOperation().__name__ == Operation.multiply.__name__

def test_get_last_calc_with_no_history(setup_history):
    '''test for getting the last calculation when there is no history'''
    History.clear_history()
    assert History.get_last_calc() is None

def test_get_index_calc(setup_history):
    '''test for getting a calculation at an index'''
    indexcalc = History.get_index_calc(0)
    assert indexcalc.getA() == 2
    assert indexcalc.getB() == 3
    assert indexcalc.getOperation().__name__ == Operation.add.__name__

def test_get_index_calc_with_no_history(setup_history):
    '''test for getting a calculation at an index outside of length of hist'''
    assert History.get_index_calc(4) is None

def test_find_operations(setup_history):
    '''test for finding all the operations of a certain type'''
    didfind = History.find_operations(Operation.add)
    assert len(didfind) == 1

def test_newcalculation():
    '''test for using newCalculation in Calculator'''
    assert Calculator.newCalculation(4, 3, Operation.add) == 7

def test_calculator_add(setup_history):
    '''test for using add method in Calculator'''
    assert Calculator.add(2, 3) == 5
    assert len(History.get_history()) == 3

def test_calculator_subtract(setup_history):
    '''test for using subtract method in Calculator'''
    assert Calculator.subtract(5, 6) == -1
    assert Calculator.subtract(1, -1) == 2
    assert len(History.get_history()) == 4

def test_calculator_multiply(setup_history):
    '''test for using multiply method in Calculator'''
    assert Calculator.multiply(1, 1) == 1
    assert len(History.get_history()) == 3

def test_calculator_divide(setup_history):
    '''test for using divide method in Calculator'''
    assert Calculator.divide(1, 2) == 0.5
    assert len(History.get_history()) == 3
