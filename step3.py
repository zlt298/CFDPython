import numpy as np                 #here we load numpy, calling it 'np' from now on
import matplotlib.pyplot as plt    #here we load matplotlib, calling it 'plt'
import time, sys

"""
linear Diffusion u = u0 = 2 for interval 0.5<=x<=1 and 1 everywhere else
"""

nx = 41
nt = 20

dx = 2./(nx-1) #dx = 0.05

nu = 0.3
sigma = 0.2 #Courant number 
dt = sigma*(dx**2)/nu #dt is defined using sigma ... more later!

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
    for i in range(1,nx-1): ## iterate through x position...
        u[i] = un[i]+(nu*dt/(dx**2))*(un[i+1]-2*un[i]+un[i-1])
plt.plot(np.linspace(0,2,nx), u)
plt.show()
print u
