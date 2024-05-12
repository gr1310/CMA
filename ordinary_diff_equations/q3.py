# SIMPLE PENDULUM

# x= (theta)'
# (theta) = y
# y' = x
# x'= (-g/L)*sin(y)

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim

h=0.01

g=9.8
L=1
k= (-1*g)/L
Nh= int((10-0)/h)
x=[0]   # omega
y=[math.pi/4]   # theta
t= np.linspace(0,10,Nh+1)
for n in range(1,Nh+1):
    x.append(x[n-1]+k*h*math.sin(y[n-1]))
    y.append(y[n-1]+ h*x[n-1])

theta=y[1:]
def get_coordinates(theta):
    return L*np.sin(theta), -L*np.cos(theta)


fig= plt.figure()
ax= fig.add_subplot(aspect='equal')

x0,y0= get_coordinates(y[0])
line,= ax.plot([0,x0],[0,y0], lw=3, c='k')
bob= 0.08   #bob radius
circle= ax.add_patch(plt.Circle((x0,y0),bob,fc='r',zorder=3))
ax.set_xlim(-L*1.2, L*1.2)
ax.set_ylim(-L*1.2, L*1.2)

def animate(i):
    x,y =get_coordinates(theta[i])
    line.set_data([0,x],[0,y])
    circle.set_center((x,y))

nframes= len(y)
interval= h*0.1
ani= anim(fig, animate, frames=nframes, repeat= True, interval= interval)

plt.show()
