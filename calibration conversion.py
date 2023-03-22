# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:47:56 2023

@author: quantumlab
"""
import numpy as np
from compensation import courant
import lecture as l
from time import sleep
from scipy import stats
from pathlib import Path

def zc():
    for j in range(4):
        courant(0, j)

def response(j, I): # étudie la réponse du capteur à la modification du courant dans une paire de bobine j à une position donnée
    
    com = l.init('COM3') # initialisation du port

    for i in I: # environ 2 secondes pour chaque itération de la boucle
        p = Path(Path.home(), "Documents", "Victor", 'channel1 %5.3f A.npy' %(i))
        courant(i, j) # met le courant à I sur le channel j
        sleep(0.2) # attend que le courant ait atteint sa valeur permanente dans les bobines 
        l.lecture(500, com,  p) # Lecture de 500 points et stockage dans un fichier npy
    
    l.end(com) # fin de la comunication
        
        
def calibrate(Imin, Imax): # calibration en faisant varier le courant dans les bobines entre Imin et Imax
    
    k = 10 # nombre de points
    
    M = np.empty((3,3)) # matrice de passage
    
    Bx_ = np.empty(k) 
    By_ = np.empty(k)
    Bz_ = np.empty(k)
    
    I = np.linspace(Imin, Imax, k) # range de variation de l'intensité
    
    for j in range(3): # j = 0, 1, 2
        
        response(j, I) # mesure de la réponse de la paire de bobine j sur une plage d'intensité I
        
        for i in I: # pour chaque courant appliqué, on calcule la moyenne de Bx, By et Bz 
            data = np.load('channel1 %5.3f A.npy' %(i))
            Bx_[i] = np.mean(data[:,1])
            By_[i] = np.mean(data[:,2])
            Bz_[i] = np.mean(data[:,3])
            
        # régression linéaire pour trouver la pente de la droite
    
        M[0,j] = stats.linregress(I, Bx_).slope 
        M[1,j] = stats.linregress(I, By_).slope
        M[2,j] = stats.linregress(I, Bz_).slope

    return np.linalg.inv(M) # return l'inverse de la matrice car on veut I en foction de B et non l'inverse
        
    
