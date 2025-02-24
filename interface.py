import importlib
import pkgutil
import plugins
#from abc import ABC, abstractmethod turns out did not end up needing this with plugin architecture, just added a command line at the bottom of each command
from calculator import Calculator
#from command import Command, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, ExitCommand, MenuCommand
class Command:
    #@abstractmethod
    def execute(self):
        pass

class Interface:
    def __init__(self):
        self.commandHandler = CommandHandler()
    
    @staticmethod
    def newInterface():
        return Interface()
    
    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, type 'menu' for a full list of commands, or type 'exit' to exit!")
        
        #self.commandHandler.regCommand("add", AddCommand())
        #self.commandHandler.regCommand("subtract", SubtractCommand())
        #self.commandHandler.regCommand("multiply", MultiplyCommand())
        #self.commandHandler.regCommand("divide", DivideCommand())
        #self.commandHandler.regCommand("menu", MenuCommand())
        #self.commandHandler.regCommand("exit", ExitCommand())
        self.commandHandler.loadCommands()
        
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
    
    def loadCommands(self):
        '''adds all of the plugins in plugins'''
        for _, name, _ in pkgutil.iter_modules(plugins.__path__):
            module = importlib.import_module(f"plugins.{name}.__init__")
            if hasattr(module, "command"):
                self.regCommand(name, module.command)

        
    