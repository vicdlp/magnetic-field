import numpy as np
import serial
from pathlib import Path

def init(port): #initialise la comunication avec le port USB
    serialCom = serial.Serial(port, 2000000)
    return serialCom

def end(serialCom): # ferme la connexion avec le port
    serialCom.close()

def querry(serialCom, path): # va chercher une mesure (t, Bx, By, Bz) à l'arduino et la décode
    
    while True:
        
        try:      
            s_bytes = serialCom.readline()
            decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')
            
            break
        except:
            continue
        
    np.save(path, decoded_bytes.split(" ")) # sauvegarde la valeur dans un fichier npy
    
    
def lecture(k, serial, path): # lit k valeurs envoyées par le capteur puis les enregistre en .npy
    
    B = np.empty((k, 3))
    
    for i in range(k):
        try:      
            s_bytes = serial.readline()
            decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')
            B[i,:] = [float(b) for b in decoded_bytes]
            break
        except:
            pass
    
    np.save(path, B)
        
    

ser = init("COM3")
p = "currentfield.npy"

while True:
    querry(ser, p)

end(ser)