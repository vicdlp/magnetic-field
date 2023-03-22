import logging
from logging.handlers import RotatingFileHandler
import numpy as np
from time import sleep


# Création du fichier .log d'une capacité maximale de 1 Go puis qui se réécrit à partir du début une fois arrivé à 1 Go

log_formatter = logging.Formatter('%(asctime)s %(message)s')
my_handler = RotatingFileHandler("logtest.log", mode='a', maxBytes=1e9, backupCount=1, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.DEBUG)

logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)
logger.addHandler(my_handler)
logger.setLevel(logging.DEBUG)


while True:
    try:
        data =  np.load("currentfield.npy", allow_pickle=True)
        logger.debug(data)
        sleep(0.125) # 8 points par secondes
    except:
        pass
        
    