from typing import Callable
from calculator.operation import Operation

class Calculation:
    def __init__(self, a: float, b: float, operation: Callable[[float, float], float]):
        self.a = a
        self.b = b
        self.operation = operation
        
    def do(self) -> float:
        return self.operation(self.a, self.b)
    
    @staticmethod
    def newCalc(a: float, b: float, oper: Callable[[float, float], float]):
        return Calculation(a, b, oper)
    
    #can't make any of these staticmethods because they all use self, and
    #can't make any of these classmethods because i want this to be for
    #each instance only
    def getA(self) -> float:
        return self.a
    
    def getB(self) -> float:
        return self.b
    
    def getOperation(self) -> float:
        return self.operation
    
    def setA(self, newa: float):
        self.a = newa
    
    def setB(self, newb: float):
        self.b = newb
    
    def setOperation(self, newOperation: Callable[[float, float], float]):
        self.operation = newOperation