import os
import logging
from datetime import datetime
from calculator import Calculator
from command import Command, CommandHandler

class Interface:
    def __init__(self):
        self.configLogging()
        self.commandHandler = CommandHandler()
    
    @staticmethod
    def newInterface():
        return Interface()
    
    def configLogging(self):
        logDir = "logs"
        os.makedirs(logDir, exist_ok = True)
        logFile = os.path.join(logDir, datetime.now().strftime("%m.%d.%H.%M.log"))
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt="%m-%d-%Y %H:%M:%S",
            filename=logFile
        )
        logging.info("Logging configured")
    
    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, type 'menu' for a full list of commands, or type 'exit' to exit!")
        self.commandHandler.loadCommands()
        logging.info("All commands loaded")
        while True:
            self.commandHandler.executeCommand(input(">>> ").strip())     
