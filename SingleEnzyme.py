#Griffin Calme
#Python 3.5.0

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Raw Data
s = np.array([1., 3., 5., 10., 20., 50., 100.]) #substrate concentration (micromoles)
v = np.array([.08, .15, .18, .21, .23, .24, .25]) #velocity at corresponding concentration (micromoles/sec)

#take reciprocal of Michaelis-Menten to plot in Lineweaver-Burke
Recip_S = np.reciprocal(s)
Recip_V = np.reciprocal(v)

#Calculate linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(Recip_S, Recip_V)


#Draw linear regression
x = np.linspace(-1., 2., 1000)
for i in x:
    y = (slope * x) + intercept

#Plot 1/Vmax
plt.scatter(0, intercept, color='red')
print("\n1/Vmax = ", intercept)
print("Vmax = ", 1/intercept)


#Plot -1/Km
xintercept = ((0 - intercept)/slope)
plt.scatter(xintercept, 0, color='red')
print("\n-1/Km = ", xintercept)
Km = (-1 / xintercept)
print("Km = ", Km)
print("\nKm/Vmax (slope): ", slope)

#Draw x & y origins
plt.axhline(0, color='black')
plt.axvline(0, color='black')

#Graph scatter points
plt.scatter(Recip_S, Recip_V)

#Graph linear regresison
plt.plot(x, y)

#Titles and labels
plt.xlabel('1/[S] ($\mu$M)')
plt.ylabel('1/v ($\mu$M/s)')
plt.title('Lineweaver-Burk')

plt.show()
