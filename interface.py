from abc import ABC, abstractmethod
from calculator import Calculator
from command import Command, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, ExitCommand

class Interface:
    def __init__(self):
        self.commandHandler = CommandHandler()
    
    @staticmethod
    def newInterface():
        return Interface()
    
    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, or type 'exit' to exit!")
        
        self.commandHandler.regCommand("add", AddCommand())
        self.commandHandler.regCommand("subtract", SubtractCommand())
        self.commandHandler.regCommand("multiply", MultiplyCommand())
        self.commandHandler.regCommand("divide", DivideCommand())
        self.commandHandler.regCommand("exit", ExitCommand())
        
        print("Type 'exit' to exit")
        while True:
            self.commandHandler.executeCommand(input(">>> ").strip())

class CommandHandler():
    def __init__(self):
        self.commands = {}
    
    def regCommand(self, commandName: str, command: Command):
        self.commands[commandName] = command
    
    def executeCommand(self, commandName: str):
        try:
            self.commands[commandName].execute()
        except KeyError:
            print(f"No such command: {commandName}")
        
        
    