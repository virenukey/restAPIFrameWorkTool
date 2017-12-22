import logging
import setupTest
from os import path, remove

_logloc = setupTest.logLoc

logLocation = _logloc['location']+'\\'+_logloc['fileName'] 

if path.isfile(logLocation):
    remove(logLocation)
 
class Log(object):
    def __init__(self):
        self.current_number = 0
        self.logger = logging.getLogger(__name__)
 
        # Create the Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
 
        # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler(logLocation)
        logger_handler.setLevel(logging.DEBUG)
 
        # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
 
        # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)
 
        # Add the Handler to the Logger
        self.logger.addHandler(logger_handler)
        #self.logger.info('Completed configuring logger()!')
 
   