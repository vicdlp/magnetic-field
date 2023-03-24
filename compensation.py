
from keysightn6700 import outPut, openSocket, closeSockets
from conversion import conversion 
import numpy as np

def courant(I, channel):
    
    outPut('CURR %5.3f,(@%d)' %(I, channel)) # met le courant à I sur la channel choisi

def compensate(B_normal, B_previous):
    
    while True:
        try:
            B = np.array([float(i) for i in np.load("currentfield.npy", allow_pickle=True)]) 
            
            break
        except:
            continue
    
    if B_previous-B)
    
    I = conversion(B, B_normal) # calcul du courant à envoyer
    
    
    if I[0]<0 or I[1]<0 or I[2]<0: # courant négatif
        
        pass
        
    else:
    # set les nouvelles valeurs du courant sur les channels du générateur
        courant(I[0], 4) 
        courant(I[1], 3)
        courant(I[2], 1)
        courant(I[2]*0.37, 2) # ratio actuel

  
openSocket('172.16.9.81',5025) # adresse du port
outPut('FUNC CURR,(@1:4)') # current priority mode



while True:
    try:
        B_normal = np.array([float(i) for i in np.load("currentfield.npy", allow_pickle=True)]) 
        
        break
    except:
        continue
    
print(B_normal)

while True:

    compensate(B_normal)

    
closeSockets()