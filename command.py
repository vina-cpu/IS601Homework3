import sys
from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation
from calculator import Calculator
#abc is abstract base class which allows me to use this pattern thingy 

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
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
            print(result)
        except InvalidOperation:
            print(f"Invalid number input: {num1} or {num2} is not a valid number.")        
        except ValueError:
            print("An error occured: Cannot divide by zero")
        except Exception as e: #line missed in cov - don't know how to test this
            print(f"An error occured: {e}") #line missed in cov - don't know how to test this    

class SubtractCommand(Command):
    def execute(self):
        print("What is your first number:")
        num1str: str = input(">>> ").strip()
        print("What is your second number:")
        num2str: str = input(">>> ").strip()
        print("Calculating ... ")
        try:
            num1, num2 = map(Decimal, [num1str, num2str])
            result = Calculator.subtract(num1, num2)
            print(result)
        except InvalidOperation:
            print(f"Invalid number input: {num1} or {num2} is not a valid number.")        
        except ValueError:
            print("An error occured: Cannot divide by zero")
        except Exception as e: #line missed in cov - don't know how to test this
            print(f"An error occured: {e}") #line missed in cov - don't know how to test this     

class MultiplyCommand(Command):
    def execute(self):
        print("What is your first number:")
        num1str: str = input(">>> ").strip()
        print("What is your second number:")
        num2str: str = input(">>> ").strip()
        print("Calculating ... ")
        try:
            num1, num2 = map(Decimal, [num1str, num2str])
            result = Calculator.multiply(num1, num2)
            print(result)
        except InvalidOperation:
            print(f"Invalid number input: {num1} or {num2} is not a valid number.")        
        except ValueError:
            print("An error occured: Cannot divide by zero")
        except Exception as e: #line missed in cov - don't know how to test this
            print(f"An error occured: {e}") #line missed in cov - don't know how to test this    

class DivideCommand(Command):
    def execute(self):
        print("What is your first number:")
        num1str: str = input(">>> ").strip()
        print("What is your second number:")
        num2str: str = input(">>> ").strip()
        print("Calculating ... ")
        try:
            num1, num2 = map(Decimal, [num1str, num2str])
            result = Calculator.divide(num1, num2)
            print(result)
        except InvalidOperation:
            print(f"Invalid number input: {num1} or {num2} is not a valid number.")        
        except ValueError:
            print("An error occured: Cannot divide by zero")
        except Exception as e: #line missed in cov - don't know how to test this
            print(f"An error occured: {e}") #line missed in cov - don't know how to test this    

class ExitCommand(Command):
    def execute(self):
        print("Goodbye!")
        sys.exit(1)
        