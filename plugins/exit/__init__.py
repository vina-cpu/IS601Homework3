import sys
from interface import Command

class ExitCommand(Command):
    def execute(self):
        print("Goodbye!")
        sys.exit(1)

command = ExitCommand()