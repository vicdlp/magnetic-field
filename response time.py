import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_csv('scope_3.csv', sep = ',', skiprows = 200, names = ['Temps (s)', 'Voie 1 (V)', 'Voie 2 (V)'])


def V(t, t0, tau, A, V0):
    r = np.empty(len(t))
    for i in range(len(t)):
        if t[i] < t0:
            r[i] = V0
        else:
            r[i] = V0 + A*(1-np.exp(-(t[i]-t0)/tau))
    return r
    
popt, pcov = curve_fit(V, data['Temps (s)'][:30000], data['Voie 2 (V)'][:30000], p0 = [0.0124, 0.01, 0.05, -0.32] )
fit = V(data['Temps (s)'], popt[0], popt[1], popt[2], popt[3])

plt.figure(figsize =(16, 9))
plt.ylabel('Tension (V)', fontsize = 24)
plt.xlabel("Temps (s)", fontsize = 24)
plt.plot(data['Temps (s)'], data['Voie 2 (V)'], '.', label = "output sources")
# plt.plot(data['Temps (s)'], data['Voie 1 (V)'], '--', label = "GBF")
plt.plot(data['Temps (s)'], fit, label = r'fit : $t_0 = %5.3f$ ms,  $\tau = %5.3f$ ms' %(popt[0]*1000, popt[1]*1000))
plt.legend(fontsize = 24)
plt.show()
