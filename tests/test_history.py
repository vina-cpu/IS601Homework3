'''My Tests History Class and Calculator Class With Faker'''
from typing import Callable, List
import pytest
from faker import Faker
from calculator.calculation import Calculation
from calculator.history import History
from calculator.operation import Operation
from calculator import Calculator

fake = Faker()
operationsList: List[Callable[[float, float], float]] = [Operation.add, Operation.subtract, Operation.multiply, Operation.divide]

@pytest.fixture
def setup_history():
    '''clear history and add a couple calculations to set up the history'''
    History.clear_history()
    History.append_calc(Calculation(2, 3, Operation.add))
    History.append_calc(Calculation(5, 4, Operation.multiply))

def test_add_calculation(setup_history):
    '''test for adding a calculation to History class, and also testing the create Calculation'''
    newcalc = Calculation.newCalc(4, 3, Operation.add)
    History.append_calc(newcalc)
    assert History.get_last_calc() == newcalc

def test_random_add_calculation(setup_history):
    '''test for adding fake calculation with any values'''
    newcalc = Calculation.newCalc(fake.random_number(), fake.random_number(), fake.random_element(operationsList))
    History.append_calc(newcalc)
    assert History.get_last_calc() == newcalc

def test_get_history(setup_history):
    '''test for getting history from setup_history'''
    history = History.get_history()
    assert len(history) == 2

def test_set_history(setup_history):
    '''test for setting history'''
    History.set_history([Calculation(1, 1, Operation.multiply)])
    assert len(History.get_history()) == 1
    History.set_history([Calculation(fake.random_number(), fake.random_number(), fake.random_element(operationsList)), Calculation(fake.random_number(), fake.random_number(), fake.random_element(operationsList))])
    assert len(History.get_history()) == 2

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

def test_newcalculation():
    '''test for using newCalculation in Calculator'''
    assert Calculator.newCalculation(4, 3, Operation.add) == 7
    a: float = fake.random_number()
    b: float = fake.random_number() # works with 0 as well as in next test
    oper: Callable[[float, float], float] = fake.random_element(operationsList)
    while b == 0:
        b = fake.random_number()
    assert Calculator.newCalculation(a, b, oper) == oper(a, b)

def test_newcalculation_with_divide_by_zero():
    '''test for using newCalculation with b = 0'''
    a: float = fake.random_number()
    with pytest.raises(ValueError, match = "Division by zero"):
        Calculator.newCalculation(a, 0, Operation.divide)

def test_calculator_add(setup_history):
    '''test for using add method in Calculator'''
    assert Calculator.add(2, 3) == 5
    assert len(History.get_history()) == 3
    a: float = fake.random_number()
    b: float = fake.random_number()
    assert Calculator.add(a, b) == a + b
    assert len(History.get_history()) == 4

def test_calculator_subtract(setup_history):
    '''test for using subtract method in Calculator'''
    assert Calculator.subtract(5, 6) == -1
    assert Calculator.subtract(1, -1) == 2
    assert len(History.get_history()) == 4
    a: float = fake.random_number()
    b: float = fake.random_number()
    assert Calculator.subtract(a, b) == a - b
    assert len(History.get_history()) == 5

def test_calculator_multiply(setup_history):
    '''test for using multiply method in Calculator'''
    assert Calculator.multiply(1, 1) == 1
    assert len(History.get_history()) == 3
    a: float = fake.random_number()
    b: float = fake.random_number()
    assert Calculator.multiply(a, b) == a * b
    assert len(History.get_history()) == 4

def test_calculator_divide(setup_history):
    '''test for using divide method in Calculator'''
    assert Calculator.divide(1, 2) == 0.5
    assert len(History.get_history()) == 3
    a: float = fake.random_number()
    assert Calculator.divide(a, 1) == a
    assert len(History.get_history()) == 4

def test_calculator_divide_by_zero(setup_history):
    '''test for using divide with zero in Calculator'''
    a: float = fake.random_number()
    with pytest.raises(ValueError, match = "Division by zero"):
        Calculator.divide(a, 0)

def test_calculator_redo_last_a(setup_history):
    '''test for changing the last calculation's a and making a new calculation'''
    assert Calculator.redoLastCalcA(1) == 4
    assert len(History.get_history()) == 3
    assert History.get_index_calc(1).getA() == 5
    a: float = fake.random_number()
    assert Calculator.redoLastCalcA(a) == a * 4
    assert History.get_index_calc(1).getA() == 5
    assert History.get_index_calc(2).getA() == 1
    assert History.get_index_calc(3).getA() == a

def test_calculator_redo_last_b(setup_history):
    '''test for changing the last calculation's b and making a new calculation'''
    assert Calculator.redoLastCalcB(1) == 5
    assert len(History.get_history()) == 3
    assert History.get_index_calc(1).getB() == 4
    b: float = fake.random_number()
    assert Calculator.redoLastCalcB(b) == 5 * b
    assert History.get_index_calc(1).getB() == 4
    assert History.get_index_calc(2).getB() == 1
    assert History.get_index_calc(3).getB() == b

def test_calculator_redo_last_operation(setup_history):
    '''test for changing the last calculation's operation and making a new calculation'''
    assert Calculator.redoLastCalcOperation(Operation.add) == 9
    assert len(History.get_history()) == 3
    oper: Callable[[float, float], float] = fake.random_element(operationsList)
    assert Calculator.redoLastCalcOperation(oper) == oper(5,4)
    assert len(History.get_history()) == 4
    assert History.get_index_calc(1).getOperation().__name__ == Operation.multiply.__name__
    assert History.get_index_calc(2).getOperation().__name__ == Operation.add.__name__
    assert History.get_index_calc(3).getOperation().__name__ == oper.__name__

def test_calculator_redo_a(setup_history):
    '''test for changing a calculation's a and making a new calculation'''
    assert Calculator.redoCalcA(History.get_last_calc(), 3) == 12
    assert len(History.get_history()) == 3
    newa: float = fake.random_number()
    assert Calculator.redoCalcA(History.get_last_calc(), newa) == newa * 4
    assert len(History.get_history()) == 4
    assert History.get_index_calc(1).getA() == 5
    assert History.get_index_calc(2).getA() == 3
    assert History.get_index_calc(3).getA() == newa

def test_calculator_redo_b(setup_history):
    '''test for changing a calculation's b and making a new calculation'''
    assert Calculator.redoCalcB(History.get_index_calc(0), 4) == 6
    assert len(History.get_history()) == 3
    newb: float = fake.random_number()
    assert Calculator.redoCalcB(History.get_index_calc(0), newb) == 2 + newb
    assert len(History.get_history()) == 4
    assert History.get_index_calc(0).getB() == 3
    assert History.get_index_calc(2).getB() == 4
    assert History.get_index_calc(3).getB() == newb

def test_calculator_redo_operation(setup_history):
    '''test for changing a calculation's operation and making a new calculation'''
    assert Calculator.redoCalcOperation(History.get_index_calc(0), Operation.subtract) == -1
    assert len(History.get_history()) == 3
    assert History.get_index_calc(0).getOperation().__name__ == Operation.add.__name__
    oper: Callable[[float, float], float] = fake.random_element(operationsList)
    assert Calculator.redoCalcOperation(History.get_index_calc(0), oper) == oper(2, 3)
    assert len(History.get_history()) == 4
    assert History.get_index_calc(0).getOperation().__name__ == Operation.add.__name__
    assert History.get_index_calc(2).getOperation().__name__ == Operation.subtract.__name__
    assert History.get_index_calc(3).getOperation().__name__ == oper.__name__
