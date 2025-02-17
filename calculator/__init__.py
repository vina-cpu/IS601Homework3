from typing import Callable
from decimal import Decimal
from calculator.operation import Operation
from calculator.history import History
from calculator.calculation import Calculation

class Calculator:
    
    #merging the calculations with the history, so whenever you call this it does the calculation and adds it to the history too
    @staticmethod
    def newCalculation(a: Decimal, b: Decimal, oper: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        newCalc = Calculation.newCalc(a, b, oper)
        History.append_calc(newCalc)
        return newCalc.do()
    
    @staticmethod
    def add(a: Decimal, b: Decimal):
        return Calculator.newCalculation(a, b, Operation.add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.newCalculation(a, b, Operation.subtract)
   
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.newCalculation(a, b, Operation.multiply)
   
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.newCalculation(a, b, Operation.divide)
    
    @staticmethod
    def redoLastCalcA(a: Decimal) -> Decimal:
        lastCalc = History.get_last_calc()
        return Calculator.newCalculation(a , lastCalc.getB(), lastCalc.getOperation())

    @staticmethod
    def redoLastCalcB(b: Decimal) -> Decimal:
        lastCalc = History.get_last_calc()
        return Calculator.newCalculation(lastCalc.getA(), b, lastCalc.getOperation())

    @staticmethod
    def redoLastCalcOperation(oper: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        lastCalc = History.get_last_calc()
        return Calculator.newCalculation(lastCalc.getA(), lastCalc.getB(), oper)

    @staticmethod
    def redoCalcA(calc: Calculation, a: Decimal) -> Decimal:
        return Calculator.newCalculation(a, calc.getB(), calc.getOperation())
   
    @staticmethod
    def redoCalcB(calc: Calculation, b: Decimal) -> Decimal:
        return Calculator.newCalculation(calc.getA(), b, calc.getOperation())

    @staticmethod
    def redoCalcOperation(calc: Calculation, oper: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        return Calculator.newCalculation(calc.getA(), calc.getB(), oper)
