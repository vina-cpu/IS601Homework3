from decimal import Decimal, InvalidOperation
from calculator import Calculator
from interface import Command

class AddCommand(Command):
    def execute(self):
        print("What is your first number:")
        num1str: str = input(">>> ").strip()
        print("What is your second number:")
        num2str: str = input(">>> ").strip()
        print("Calculating ... ")
        try:
            num1, num2 = map(Decimal, [num1str, num2str])
            result = Calculator.add(num1, num2)
            print(f"The result of {num1} add {num2} is equal to {result}")
        except InvalidOperation:
            print(f"Invalid number input: {num1str} or {num2str} is not a valid number.")        
        except ValueError:
            print("An error occured: Cannot divide by zero")
        except Exception as e: #line missed in cov - don't know how to test this
            print(f"An error occured: {e}") #line missed in cov - don't know how to test this

command = AddCommand()