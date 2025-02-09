'''My History Test'''
import pytest
from calculator.calculation import Calculation
from calculator.history import History
from calculator.operation import Operation


@pytest.fixture
def setup_calculations():
    '''clear history and add a couple calculations to set up the history'''
    History.clear_history()
    History.add_calculation(Calculation(2, 3, Operation.add))
    History.add_calculation(Calculation(5, 4, Operation.multiply))

def test_add_calculation(setup_calculations):
    '''test for adding a calculation to History class, and also testing the create Calculation'''
    newcalc = Calculation.create(4, 3, Operation.add)
    History.add_calculation(newcalc)
    assert History.get_last_calc() == newcalc

def test_get_history(setup_calculations):
    '''test for getting history from setup_history'''
    history = History.get_history()
    assert len(history) == 2
