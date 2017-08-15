"""
Eric Smith
Southern Methodist University
CSE3365
February 8th, 2017
"""

from math import sin, fabs, pi
from numpy import zeros
import matplotlib.pyplot as plt
x = pi/4
nmax = 65
h = zeros((65, 1), 'float')
errorForward = zeros((nmax, 1), 'float')
errorCentral = zeros((nmax, 1), 'float')
exact_value = sin(x)

for j in range(nmax):
    h[j] = (1 / 2.0) ** j

    # forward difference
    computed_value = (sin(x + h[j]) - sin(x)) / h[j]
    errorForward[j] = fabs(computed_value - exact_value)

    # central difference
    computed_value = (sin(x + h[j]) - sin(x - h[j])) / (2*h[j])
    errorCentral[j] = fabs(computed_value - exact_value)

plt.loglog(h, errorForward, h, errorForward, '-ro')
plt.loglog(h, errorCentral, h, errorCentral, '-bs')

plt.xlabel('h')
plt.ylabel('error')
plt.legend(('Central Difference', 'Forward Difference'), loc = 0)
plt.savefig('ForwardvsCentralDifference.png', format='png')
plt.show()


