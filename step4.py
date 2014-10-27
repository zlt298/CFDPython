import numpy as np                 #here we load numpy, calling it 'np' from now on
import matplotlib.pyplot as plt    #here we load matplotlib, calling it 'plt'
import time, sys
import sympy

from sympy import init_printing
init_printing(use_latex=True)
from sympy.utilities.lambdify import lambdify

"""
1D: Burgers' Equation
pu/pt + u*pu/px = nu*(p^2u/px^2)
IC: u = -2*nu*(phiprime/phi)+4
BC: u(0) = u(2*pi) - condition of periodicity

"""

x, nu, t = sympy.symbols('x nu t')
phi = sympy.exp(-(x-4*t)**2/(4*nu*(t+1))) + sympy.exp(-(x-4*t-2*np.pi)**2/(4*nu*(t+1)))
phiprime = phi.diff(x)

u = -2*nu*(phiprime/phi)+4
ufunc = lambdify((t, x, nu), u)
print ufunc(1,4,3)

nx = 1001
nt = 100

dx = 2*np.pi/(nx-1)
nu = 0.07
sigma = .08
dt = sigma*dx**2/nu


x = np.linspace(0,2*np.pi,nx)
u = np.empty(nx)
un = np.empty(nx)
t = 0

u = np.asarray([ufunc(t, x0, nu) for x0 in x])

plt.figure(figsize=(11,7), dpi=100)
plt.plot(x,u, marker='o', lw=2)
plt.xlim([0,2*np.pi])
plt.ylim([0,10])
plt.show()

"""
implement discretization of convection equation

Find next time step:
u_(i,n+1) = 
"""

for n in xrange(nt):
    un = u.copy()
    for i in xrange(nx-1):
        u[i] = un[i] - un[i] * dt/dx *(un[i] - un[i-1]) + nu*dt/dx**2*\
                (un[i+1]-2*un[i]+un[i-1])
    u[-1] = un[-1] - un[-1] * dt/dx * (un[-1] - un[-2]) + nu*dt/dx**2*\
                (un[0]-2*un[-1]+un[-2])
        
u_analytical = np.asarray([ufunc(nt*dt, xi, nu) for xi in x])

plt.figure(figsize=(11,7), dpi=100)
plt.plot(x,u, marker='o', lw=2, label='Computational')
plt.plot(x, u_analytical, label='Analytical')
plt.xlim([0,2*np.pi])
plt.ylim([0,10])
plt.legend()
plt.show()
