import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_csv('scope_1.csv', sep = ',', skiprows = 2, names = ['Temps (s)', 'Voie 1 (V)', 'Voie 2 (V)', 'Voie 3 (V)'])


def V(t, t0, tau, A, V0):
    r = np.empty(len(t))
    for i in range(len(t)):
        if t[i] < t0:
            r[i] = V0
        else:
            r[i] = V0 + A*(1-np.exp(-(t[i]-t0)/tau))
    return r
    
popt, pcov = curve_fit(V, data['Temps (s)'], data['Voie 1 (V)'], p0 = [0.02, 0.001, 0.6, 0.2] )
fit = V(data['Temps (s)'], popt[0], popt[1], popt[2], popt[3])

plt.figure()
plt.ylabel('Tension (V)')
plt.xlabel("Temps (s)")
plt.plot(data['Temps (s)'], data['Voie 1 (V)'], '.', label = "output sources")
# plt.plot(data['Temps (s)'], data['Voie 3 (V)'], '--', label = "GBF")
plt.plot(data['Temps (s)'], fit, label = r'fit : $t_0 = %5.3f$ ms,  $\tau = %5.3f$ ms' %(popt[0]*1000, popt[1]*1000))
plt.legend(loc = 'upper left')
plt.show()
