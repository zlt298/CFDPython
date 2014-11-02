from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots

import numpy as np
import matplotlib.pyplot as plt

###variable declarations
nx = 101
ny = 101
nt = 80
c = 1.
dx = 2.0/(nx-1)
dy = 2.0/(ny-1)
sigma = 0.2
dt = sigma*dx/c

x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)

u = np.ones((ny,nx)) ##create a 1xn vector of 1's
un = np.ones((ny,nx)) ##
v = np.ones((ny,nx)) ##create a 1xn vector of 1's
vn = np.ones((ny,nx)) ##

###Assign initial conditions

u[.5/dy:1/dy+1,.5/dx:1/dx+1]=2 ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
v[.5/dy:1/dy+1,.5/dx:1/dx+1]=2 ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2

for n in range(nt+1): ##loop across number of time steps
    un = u.copy()
    vn = v.copy()
    
    u[1:,1:] = un[1:,1:] - (un[1:,1:]*dt/dx*(un[1:,1:] - un[0:-1,1:]))-(vn[1:,1:]*dt/dy*(un[1:,1:]-un[1:,0:-1]))
    v[1:,1:] = vn[1:,1:] - (un[1:,1:]*dt/dx*(vn[1:,1:] - vn[0:-1,1:]))-(vn[1:,1:]*dt/dy*(vn[1:,1:]-vn[1:,0:-1]))

    u[0,:] = 1
    u[-1,:] = 1
    u[:,0] = 1
    u[:,-1] = 1
    
    v[0,:] = 1
    v[-1,:] = 1
    v[:,0] = 1
    v[:,-1] = 1

##for n in range(nt+1): ##loop across number of time steps
##    un = u.copy()
##    for i in range(1, len(u)):
##        for j in range(1, len(u)):
##            u[i,j] = un[i, j] - (c*dt/dx*(un[i,j] - un[i-1,j]))-(c*dt/dy*(un[i,j]-un[i,j-1]))
##            u[0,:] = 1
##            u[-1,:] = 1
##            u[:,0] = 1
##            u[:,-1] = 1



from matplotlib import cm ##cm = "colormap" for changing the 3d plot color palette
fig = plt.figure(figsize=(11,7), dpi=100)
ax = fig.gca(projection='3d')
X,Y = np.meshgrid(x,y)
ax.plot_surface(X,Y,u, cmap=cm.coolwarm)
plt.show()

fig = plt.figure(figsize=(11,7), dpi=100)
ax = fig.gca(projection='3d')
X,Y = np.meshgrid(x,y)
ax.plot_surface(X,Y,v, cmap=cm.coolwarm)
plt.show()
