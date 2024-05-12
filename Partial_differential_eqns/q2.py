# 2D heat equation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x,y, xc, yc):
    return np.exp(-np.sqrt((x-xc)**2+(y-yc)**2))
xc=0.5
yc=0.5

mu=5 * (10 ** (-5))
h=0.01
a=0
b=1

Lx=b-a
Ly= b-a

Nx= int(Lx/h)+1
x= np.linspace(0,Lx,Nx+1)
Ny= int(Ly/h)+1
y= np.linspace(0,Ly,Ny+1)

T= 2000
dt= 0.5
Nt= int(T/dt)+1
t= np.linspace(0,T, Nt+1)


fmat= [[f(i,j, xc, yc) for j in y] for i in x]

A= np.eye(Nx+1, k=-1)*1+np.eye(Nx+1,k=0)*-2+np.eye(Nx+1,k=1)*1

u_initial= np.array([[0 for j in y] for i in x])

res=[u_initial]
for i in t[1:]:
    du= ((mu/(h**2))*(A@u_initial+ u_initial@A))+fmat

    u_initial= u_initial+du*dt

    for i in range(len(x)):
        u_initial[i][0]=0
        u_initial[i][-1]=0
    for j in range(len(y)):
        u_initial[0][j]=0
        u_initial[-1][j]=0
    
    res.append(u_initial)

# print(res)

# 3d animation
# fig= plt.figure()
# ax=plt.axes(projection= "3d")

# X, Y= np.meshgrid(x,y)
# ax.plot_surface(X, Y, res[0], cmap="hot",antialiased= False,linewidth=0)

# def animate(i):
#     ax.plot_surface(X,Y, res[i],cmap="hot",antialiased= False,linewidth=0)

# using imshow
fig, ax= plt.subplots()
plt1= plt.imshow(res[-1],cmap="hot",origin="lower", extent=[0,1,0,1], aspect=1, animated=True)
cb = fig.colorbar(plt1) 
cb.set_label("Temperature")  
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

def animate(i):
    plt1.set_array(res[i])
    return plt1

numFrames = len(res)  
interval = 1 

    # Setting up the animation
anim = FuncAnimation(
        fig,
        func=animate,
        frames=numFrames,
        repeat=False,
        interval=interval,
    )
plt.show()




