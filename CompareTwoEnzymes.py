#Griffin Calme
#Python 3.5.0

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Raw Data
s = np.array([1., 3., 5., 10., 20., 50., 100.]) #substrate concentration (micromoles)
vA = np.array([0.67, 1.20, 1.43, 1.67, 1.82, 1.92, 1.96]) #velocity of enzyme A at corresponding concentration (micromoles/sec)
vB = np.array([0.40, 0.86, 1.11, 1.43, 1.67, 1.85, 1.92]) #velocity of enzyme Bat corresponding concentration (micromoles/sec)

#take reciprocal of Michaelis-Menten to plot in Lineweaver-Burke
Recip_s = np.reciprocal(s)
Recip_vA = np.reciprocal(vA)
Recip_vB = np.reciprocal(vB)

#Calculate linear regression
slopeA, interceptA, r_valueA, p_valueA, std_errA = stats.linregress(Recip_s, Recip_vA)
slopeB, interceptB, r_valueB, p_valueB, std_errB = stats.linregress(Recip_s, Recip_vB)

#Draw linear regression A
xA = np.linspace(-1., 2., 1000)
for iA in xA:
    yA = (slopeA * xA) + interceptA

#Draw linear regression B
xB = np.linspace(-1., 2., 1000)
for iB in xB:
    yB = (slopeB * xB) + interceptB


#Plot 1/Vmax A
plt.scatter(0, interceptA, color='red')
print("\n----Values for vA----")
print("1/Vmax A = ", interceptA)
print("Vmax A = ", 1/interceptA)

#Plot -1/Km A
xinterceptA = ((0 - interceptA)/slopeA)
plt.scatter(xinterceptA, 0, color='red')
print("\n-1/Km A = ", xinterceptA)
KmA = (-1 / xinterceptA)
print("Km A = ", KmA)
print("\nKm/Vmax A (slope A): ", slopeA)


#Plot 1/Vmax B
plt.scatter(0, interceptB, color='green')
print("\n\n----Values for vB----")
print("1/Vmax B = ", interceptB)
print("Vmax B = ", 1/interceptB)

#Plot -1/Km B
xinterceptB = ((0 - interceptB)/slopeB)
plt.scatter(xinterceptB, 0, color='green')
print("\n-1/Km B = ", xinterceptB)
KmB = (-1 / xinterceptB)
print("Km B = ", KmB)
print("\nKm/Vmax B (slope B): ", slopeB)


#Draw x & y origins
plt.axhline(0, color='black')
plt.axvline(0, color='black')

#Graph scatter points
plt.scatter(Recip_s, Recip_vA, color='blue')
plt.scatter(Recip_s, Recip_vB, color='purple')
#Graph linear regression
plt.plot(xA, yA, label='A', color='blue', linestyle='--')
plt.plot(xB, yB, label='B', color='purple', linestyle=':')

#Titles and labels
plt.xlabel('1/[S] ($\mu$M)')
plt.ylabel('1/v ($\mu$M/s)')
plt.title('Lineweaver-Burk')
plt.legend()
plt.show()
