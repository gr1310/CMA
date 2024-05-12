import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import scipy.interpolate as sc

def func(x):
    return math.tan(x)* math.sin(30*x)*math.exp(x)

fig, ax = plt.subplots()
xdata, ydata0, ydata1 = [], [], []
ln0, = plt.plot([], [], 'r', animated=True)
ln1, = plt.plot([], [], 'b', animated=True)
f = np.linspace(0, 1, 200)

def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(-4, 4)
    ln0.set_data(xdata,ydata0)
    ln1.set_data(xdata,ydata1)
    return ln0, ln1
func_at_i=[1]
# ydata1=[1]
xdata=[-345678]
def update(frame):
    xdata.append(frame)
    func_at_i.append(func(frame))
    ydata0.append(func(frame))
    ydata1.append(sc.CubicSpline(xdata,func_at_i))
    ln0.set_data(xdata, ydata0)
    ln1.set_data(xdata, ydata1)
    return ln0, ln1,

ani = FuncAnimation(fig, update, frames=f,
                    init_func=init, blit=True, interval=2.5, repeat=False)
# plt.show()

x=[1,2,3,4,5]
print(x[:])