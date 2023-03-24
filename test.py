import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


list = []
f = open('test.txt') # ouvre le fichier log
line = f.readline()
while line: # lit toutes les lignes et les met dans une liste
    try:
        list.append(line.split(" "))
    except ValueError:
        print('Error in line :' + line )
    line = f.readline()
    
df = pd.DataFrame([sub for sub in list[:-1]], dtype = 'float') # crée un dataframe pandas à partir de la liste
df.columns = ['Bx', 'By', 'Bz']


plt.figure()
plt.xlabel("temps (s)") 
plt.ylabel("Champ magnétique (μT)")
plt.plot(df['Bx'], label = "Bx")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.xlabel("temps (s)") 
plt.ylabel("Champ magnétique (μT)")
plt.plot(df['By'] , label = "By")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.xlabel("temps (s)") 
plt.ylabel("Champ magnétique (μT)")
plt.plot(df['Bz'], label = "Bz")
plt.legend()
plt.grid()
plt.show()