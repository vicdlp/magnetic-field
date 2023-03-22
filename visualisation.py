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