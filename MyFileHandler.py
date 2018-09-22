import logging
from datetime import datetime
import os, os.path


class CustomFileHandler(logging.FileHandler):
    def __init__(self, filename, mode):
        self.filename = datetime.now().strftime(filename + '%H_%M_%d_%m_%Y.log')
        logDir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../Logs/')
        super(CustomFileHandler, self).__init__(logDir + self.filename, mode)

