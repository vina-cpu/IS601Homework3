from interface import Command

class MenuCommand(Command):
    def execute(self):
        print("Here is a list of commands:")
        print("Type 'add' to add two numbers")
        print("Type 'subtract' to subtract two numbers")
        print("Type 'multiply' to multiply two numbers")
        print("Type 'divide' to divide two numbers")
        print("Type 'exit' to exit")

command = MenuCommand()