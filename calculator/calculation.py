from typing import Callable
from decimal import Decimal
from calculator.operation import Operation

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
        
    def do(self) -> Decimal:
        return self.operation(self.a, self.b)
    
    @staticmethod
    def newCalc(a: Decimal, b: Decimal, oper: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a, b, oper)
    
    #can't make any of these staticmethods because they all use self, and
    #can't make any of these classmethods because i want this to be for
    #each instance only
    def getA(self) -> Decimal:
        return self.a
    
    def getB(self) -> Decimal:
        return self.b
    
    def getOperation(self) -> Decimal:
        return self.operation
    
    def setA(self, newa: Decimal):
        self.a = newa
    
    def setB(self, newb: Decimal):
        self.b = newb
    
    def setOperation(self, newOperation: Callable[[Decimal, Decimal], Decimal]):
        self.operation = newOperation
