import sys
from typing import Callable, List
from calculator import Calculator

def useCalculator(a, b, operationName):
    oper_map = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide       
    }
    try:
        mya, myb = map(float, [a, b])
        operation = oper_map.get(operationName)
        if operation:
            print(f"The result of {a} {operationName} {b} is equal to {operation(mya, myb)}") 
        else:
            print(f"Unknown operation: {operationName}")    
    # using float so don't know what the error for this would be right now               
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occured: {e}")   

def main():
    if len(sys.argv) != 4:
        print("Invalid number of arguments, call by: python/python3 main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, oper = sys.argv
    useCalculator(a, b, oper)

if __name__ == '__main__':
    main()