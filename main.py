import sys
from typing import Callable, List
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def useCalculator(a: str, b: str, operationName: str):
    oper_map = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide       
    }
    try:
        mya, myb = map(Decimal, [a, b])
        operation = oper_map.get(operationName)
        if operation:
            print(f"The result of {a} {operationName} {b} is equal to {operation(mya, myb)}") 
        else:
            print(f"Unknown operation: {operationName}")    
    # using float so don't know what the error for this would be right now
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")        
    except ValueError:
        print("An error occured: Cannot divide by zero")
    except Exception as e:
        print(f"An error occured: {e}")   

def main():
    _, a, b, oper = sys.argv
    useCalculator(a, b, oper)

if __name__ == '__main__':
    main()