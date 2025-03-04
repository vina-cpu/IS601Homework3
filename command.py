import importlib
import pkgutil
import plugins

class Command:
    #@abstractmethod
    def execute(self):
        pass

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
