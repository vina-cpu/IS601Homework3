import os
import logging
#from dotenv import load_dotenv, dotenv_values
from datetime import datetime
from calculator import Calculator
from command import Command, CommandHandler

class Interface:
    def __init__(self):
        self.myEnv = self.loadEnvVar()
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
    
    def loadEnvVar(self):
         myEnv = os.getenv("MYKEY")
         logging.info("Envionment variables loaded into interface")
    
    def getEnvVar(self):
        return self.myEnv.get()
         
    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, type 'menu' for a full list of commands, or type 'exit' to exit!")
        self.commandHandler.loadCommands()
        logging.info("All commands loaded")
        while True:
            self.commandHandler.executeCommand(input(">>> ").strip())     
