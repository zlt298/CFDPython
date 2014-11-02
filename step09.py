from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

###variable declarations
nx = 31
ny = 31
nt = 40

dx = 2.0/(nx-1)
dy = 2.0/(ny-1)

x = np.linspace(0,2,nx)
y = np.linspace(0,1,ny)

p = np.zeros((ny,nx)) ##create a 1xn vector of 0's
pn = np.zeros((ny,nx)) ##

p[:,0]=0
p[:,-1]=y

def plot2D(x, y, p):
    fig = plt.figure(figsize=(11,7), dpi=100)
    ax = fig.gca(projection='3d')
    X,Y = np.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,p[:], rstride=1, cstride=1, cmap=cm.coolwarm,
            linewidth=0, antialiased=False)
    ax.set_xlim(0,2)
    ax.set_ylim(0,1)
    ax.view_init(30,225)
    plt.show()

plot2D(x, y, p)
    
#====================================================
#My Approach
#====================================================
for n in range(nt+1): ##loop across number of time steps
    pn = p.copy()
    dxsq,dysq = dx**2,dy**2
    p[1:-1,1:-1]=(dysq*(pn[2:,1:-1]+pn[0:-2,1:-1])+dxsq*(pn[1:-1,2:]+pn[1:-1,0:-2]))/(2.*(dxsq+dysq))
    
    p[:,0]=0
    p[:,-1]=y
    p[0,:]= p[1,:]
    p[-1,:]= p[-2,:]
    #print n

plot2D(x,y,p)
