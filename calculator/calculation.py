from typing import Callable
from calculator.operation import Operation

class Calculation:
    def __init__(self, a: float, b: float, operation: Callable[[float, float], float]):
        self.a = a
        self.b = b
        self.operation = operation
        
    def perform(self) -> float:
        return self.operation(self.a, self.b)