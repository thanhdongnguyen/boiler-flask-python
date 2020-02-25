from logging import Logger as Log, FileHandler
from src.helpers.timer import Timer

import logging
import os

class Logger:

    def __init__(self):
        self.name = __name__
        date = Timer.get_current_format()
        self.file_name = "{}/flask_teamate_{}.log".format("/src/logs", date)
        self.format = logging.Formatter("%(levelname)s - %(asctime)s - %(name)s - %(message)s")

    def addHandler(self):
        file_handler = FileHandler(self.file_name, encoding="utf-8")
        return file_handler 

    def info(self, info):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        logger.addHandler(self.addHandler())
        
        return logger.info(info)

    def error(self, error):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.ERROR)
        logger.addHandler(self.addHandler())

        return logger.error(error)

    def exception(self, exception):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.ERROR)
        logger.addHandler(self.addHandler())

        return logger.exception(exception)

