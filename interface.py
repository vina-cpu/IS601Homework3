import os
import logging
from dotenv import load_dotenv
from datetime import datetime
from calculator import Calculator
from command import Command, CommandHandler

class Interface:
    def __init__(self):
        self.configLogging()
        load_dotenv()
        self.myEnvironment: str = "default"
        self.myEnvironment: str = self.loadEnv()
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
        
    def loadEnv(self):
        logging.info("Environment variable loaded")
        key: str = os.getenv("MYKEY")
        return key
    
    def getEnv(self):
        return self.myEnvironment

    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, type 'menu' for a full list of commands, or type 'exit' to exit!")
        self.commandHandler.loadCommands()
        logging.info("All commands loaded")
        while True:
            self.commandHandler.executeCommand(input(">>> ").strip())     
