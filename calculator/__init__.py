from typing import Callable
from calculator.operation import Operation
from calculator.history import History
from calculator.calculation import Calculation

class Calculator:
    
    #merging the calculations with the history, so whenever you call this it does the calculation and adds it to the history too
    @staticmethod
    def newCalculation(a: float, b: float, oper: Callable[[float, float], float]) -> float:
        newCalc = Calculation.newCalc(a, b, oper)
        History.append_calc(newCalc)
        return newCalc.do()
    
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
    
    @staticmethod
    def redoLastCalcA(a: float) -> float:
        lastCalc = History.get_last_calc()
        return Calculator.newCalculation(a , lastCalc.getB(), lastCalc.getOperation())

    @staticmethod
    def redoLastCalcB(b: float) -> float:
        lastCalc = History.get_last_calc()
        return Calculator.newCalculation(lastCalc.getA(), b, lastCalc.getOperation())

    @staticmethod
    def redoLastCalcOperation(oper: Callable[[float, float], float]) -> float:
        lastCalc = History.get_last_calc()
        return Calculator.newCalculation(lastCalc.getA(), lastCalc.getB(), oper)

    @staticmethod
    def redoCalcA(calc: Calculation, a: float) -> float:
        return Calculator.newCalculation(a, calc.getB(), calc.getOperation())
   
    @staticmethod
    def redoCalcB(calc: Calculation, b: float) -> float:
        return Calculator.newCalculation(calc.getA(), b, calc.getOperation())

    @staticmethod
    def redoCalcOperation(calc: Calculation, oper: Callable[[float, float], float]) -> float:
        return Calculator.newCalculation(calc.getA(), calc.getB(), oper)
