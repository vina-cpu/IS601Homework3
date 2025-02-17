from decimal import Decimal

class Operation:
    @staticmethod
    def add(a: Decimal,b: Decimal) -> Decimal:
        return a + b

    @staticmethod
    def subtract(a: Decimal,b: Decimal) -> Decimal:
        return a - b

    @staticmethod
    def multiply(a: Decimal,b: Decimal) -> Decimal:
        return a * b

    @staticmethod
    def divide(a: Decimal,b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("Division by zero")
        return a / b;
