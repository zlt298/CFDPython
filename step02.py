import numpy as np                 #here we load numpy, calling it 'np' from now on
import matplotlib.pyplot as plt    #here we load matplotlib, calling it 'plt'
import time, sys

"""
linear convection , inviscid burgers' u = u0 = 2 for interval 0.5<=x<=1 and 1 everywhere else
"""

nx = 21
nt = 20

dx = 2./(nx-1) #dx = 0.05
dt = 0.025

u = np.ones(nx)
u[.5/dx : 1/dx + 1] = 2
print u

plt.plot(np.linspace(0,2,nx), u)
plt.show()

"""
implement discretization of convection equation

Find next time step:
u_(i,n+1) = 
"""

un = np.ones(nx) #initialize a temporary array

for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy() ##copy the existing values of u into un
    for i in range(1,nx): ## iterate through x position...
        u[i] = un[i]-un[i]*dt/dx*(un[i]-un[i-1])
plt.plot(np.linspace(0,2,nx), u)
plt.show()
print u
