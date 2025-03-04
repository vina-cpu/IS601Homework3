from calculator import Calculator
from command import Command, CommandHandler

class Interface:
    def __init__(self):
        self.commandHandler = CommandHandler()
    
    @staticmethod
    def newInterface():
        return Interface()
    
    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, type 'menu' for a full list of commands, or type 'exit' to exit!")
        self.commandHandler.loadCommands()
        while True:
            self.commandHandler.executeCommand(input(">>> ").strip())       
