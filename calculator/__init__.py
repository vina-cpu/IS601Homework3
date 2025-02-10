from typing import Callable
from calculator.operation import Operation
from calculator.history import History
from calculator.calculation import Calculation

class Calculator:
    
    #merging the calculations with the history, so whenever you call this it does the calculation and adds it to the history too
    @staticmethod
    def newCalculation(a: float, b: float, oper: Callable[[float, float], float]) -> float:
        newCalc = Calculation.newCalc(a, b, oper)
        History.add_calculation(newCalc)
        return newCalc.perform()
    
    @staticmethod
    def add(a: float, b: float):
        return Calculator.newCalculation(a, b, Operation.add)
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        return Calculator.newCalculation(a, b, Operation.subtract)
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return Calculator.newCalculation(a, b, Operation.multiply)
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        return Calculator.newCalculation(a, b, Operation.divide)