import logging
from logging.handlers import RotatingFileHandler
import numpy as np
from time import sleep
from pathlib import Path

p =  Path(Path.home(), "Documents", "GitHub", "magnetic-field", "log.log")

# Création du fichier .log d'une capacité maximale de 1 Go puis qui se réécrit à partir du début une fois arrivé à 1 Go
def log(path = p):
    
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


        
    