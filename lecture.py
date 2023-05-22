import numpy as np
import serial

def init(port): #initialise la comunication avec le port USB
    serialCom = serial.Serial(port, 2000000)
    return serialCom

def end(serialCom): # ferme la connexion avec le port
    serialCom.close()

ser = init("COM4")

def querry(serialCom = ser): # va chercher une mesure (t, Bx, By, Bz) à l'arduino et la décode
    
    np.save("currentfield", ser.readline().decode("utf-8").strip('\r\n').split(" "))
    
    
    
def lecture(k, serial): # lit k valeurs envoyées par le capteur puis les enregistre en .npy
    
    B = np.empty((k, 3))
    
    for i in range(k):
        try:
            B[i,:] = ser.readline().decode("utf-8").strip('\r\n').split(" ")
        except:
            pass
    return B
        
B = lecture(1000, ser)