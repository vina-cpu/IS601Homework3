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
    
    def getA(self) -> float:
        return self.a
    
    def getB(self) -> float:
        return self.b
    
    def getOperation(self) -> float:
        return self.operation