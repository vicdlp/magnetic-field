import logging
from logging.handlers import RotatingFileHandler
import numpy as np
from time import sleep
from pathlib import Path
import os
import datetime


def logdata(data):
    
    path = Path(Path.home(), "Documents", "GitHub", "magnetic-field", "log")
    
    now = datetime.datetime.now()
        
    folder = Path(path, str(now.year), str(now.month), str(now.day))
    isExist = os.path.exists(folder)
    
    if not isExist:
        os.makedirs(folder)
        
    file = Path(folder, 'log.txt')
    log = open(file, 'a')
    string = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "," + str(now.microsecond) + " " + str(data) + '\n'
    log.write(string)
    log.close()
    

# Création du fichier .log d'une capacité maximale de 1 Go puis qui se réécrit à partir du début une fois arrivé à 1 Go
def log(path = Path(Path.home(), "Documents", "GitHub", "magnetic-field", "log.log")):
    
    log_formatter = logging.Formatter('%(asctime)s %(message)s')
    my_handler = RotatingFileHandler(path, mode='a', maxBytes=1e9, backupCount=1, encoding=None, delay=0)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.DEBUG)
    
    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(my_handler)
    logger.setLevel(logging.DEBUG)
    
    return logger

def debug(log, data):
    log.debug(data)


        
    