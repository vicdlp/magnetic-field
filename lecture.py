import numpy as np
import serial

def init(port): #initialise la comunication avec le port USB
    serialCom = serial.Serial(port, 2000000)
    return serialCom

def end(serialCom): # ferme la connexion avec le port
    serialCom.close()

ser = init("COM3")

def querry(serialCom = ser): # va chercher une mesure (t, Bx, By, Bz) à l'arduino et la décode
    
    np.save("currentfield", ser.readline().decode("utf-8").strip('\r\n').split(" "))
    
    
while True:
    querry()

end(ser)
    
    
def lecture(k, serial, name): # lit k valeurs envoyées par le capteur puis les enregistre en .npy
    
    B = np.empty((k, 3))
    
    for i in range(k):
        B[i,:] = [float(b) for b in ser.readline().decode("utf-8").strip('\r\n').split(" ")]

    np.save(name, B)
        
    