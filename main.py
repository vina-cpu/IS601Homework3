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
        print(f"The result of {a} {operationName} {b} is equal to {operation(mya, myb)}")
    except TypeError:
        print(f"Unknown operation: {operationName}")    
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")        
    except ValueError:
        print("An error occured: Cannot divide by zero")
    except Exception as e: #line missed in cov - don't know how to test this
        print(f"An error occured: {e}") #line missed in cov - don't know how to test this

def main(): # not testing this - missed in cov - don't know how to test for this case
    if len(sys.argv) != 4: #cna't test for this line
        print("Usage: python/python3 main.py <number1> <number2> <operation>")
        sys.exit(1) 
    _, a, b, oper = sys.argv
    useCalculator(a, b, oper)

if __name__ == '__main__':
    main() #line missed in cov - don't know how to test this