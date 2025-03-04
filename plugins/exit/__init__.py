import sys
import logging
from interface import Command

class ExitCommand(Command):
    def execute(self):
        logging.info("Exiting interface")
        print("Goodbye!")
        
        sys.exit(1)

command = ExitCommand()