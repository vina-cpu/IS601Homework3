class Operation:
    @staticmethod
    def add(a: float,b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float,b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float,b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float,b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero")
        return a / b;