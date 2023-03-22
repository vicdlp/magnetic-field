import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

list = []
f = open('logtest.log') # ouvre le fichier log
line = f.readline()
while line: # lit toutes les lignes et les met dans une liste
    try:
        list.append(line.replace("[", '').replace("]", '').replace("\n", '').replace("'", '').split(" "))
    except ValueError:
        print('Error in line :' + line )
    line = f.readline()
    
df = pd.DataFrame([sub for sub in list[:-1]]) # crée un dataframe pandas à partir de la liste
df.columns = ['Date', 'Time', 'Bx', 'By', 'Bz']

T = pd.to_datetime(pd.Series(df['Date'] + ' ' + df['Time'], dtype = "datetime64")) # date au bon format pour l'affichage
Bx = pd.Series(df["Bx"], dtype = 'float') # champ magnétique au format float
By = pd.Series(df["By"], dtype = 'float')
Bz = pd.Series(df["Bz"], dtype = 'float')
B_norm = np.sqrt(Bx**2 + By**2 + Bz**2) # calcul de la norme de B

Bxc = Bx - np.mean(Bx) # champ magnétique centré sur sa valeur moyenne
Byc = By - np.mean(By)
Bzc = Bz - np.mean(Bz)
Bc = B_norm - np.mean(B_norm)

# Affichage des données du log

plt.figure(figsize = (16, 9))
plt.xlabel("temps (s)") 
plt.ylabel("Champ magnétique (μT)")
plt.plot(T, Bx, label = "Bx")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize = (16, 9))
plt.xlabel("temps (s)") 
plt.ylabel("Champ magnétique (μT)")
plt.plot(T, By , label = "By")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize = (16, 9))
plt.xlabel("temps (s)") 
plt.ylabel("Champ magnétique (μT)")
plt.plot(T, Bz, label = "Bz")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize = (16, 9))
plt.xlabel("temps (s)") 
plt.ylabel("Champ magnétique (μT)")
plt.plot(T, B_norm, label = "Norme")
plt.legend()
plt.grid()
plt.show()

# Calcul du spectre du signal

X1 = fft(Bxc)
X2 = fft(Byc)
X3 = fft(Bzc)
N = len(T)
n = np.arange(N)
# get the sampling rate
sr = 8 # Hz
tau = N/sr
freq = n/tau 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside] # 

plt.figure()
plt.plot(f_oneside, np.abs(X1)[:n_oneside], label = "Bx")
plt.xlabel('Freq (Hz)')
plt.legend()
plt.ylabel('FFT Amplitude |X(freq)|')
plt.show()

plt.figure()
plt.plot(f_oneside, np.abs(X2)[:n_oneside], label = "By")
plt.xlabel('Freq (Hz)')
plt.legend()
plt.ylabel('FFT Amplitude |X(freq)|')
plt.show()

plt.figure()
plt.plot(f_oneside, np.abs(X3)[:n_oneside], label = 'Bz')
plt.xlabel('Freq (Hz)')
plt.legend()
plt.ylabel('FFT Amplitude |X(freq)|')
plt.show()
