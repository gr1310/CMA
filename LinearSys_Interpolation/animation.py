import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline, Akima1DInterpolator, BarycentricInterpolator
from matplotlib.animation import FuncAnimation

def f(x):
    return np.tan(x)*np.sin(30*x)*np.exp(x)

xlim=(0,1)
ylim=(-4,4)

fig,ax= plt.subplots()
ax.set_xlim(*xlim)
ax.set_ylim(*ylim)
n= 5
x_values= np.linspace(xlim[0],xlim[1],1000)
y_values= f(x_values)
ax.plot(x_values,y_values, c='purple', label="True")

line_spline, = ax.plot([],[], c='blue', label="CubicSpline")
line_akima, = ax.plot([],[],c='green', label="Akima")
line_bary,= ax.plot([],[],c='red',label="BaryCentric")

def animate(i):
    n=i+2
    new_x_values= np.linspace(xlim[0],xlim[1],n)
    new_y_values= f(new_x_values)

    ax.set_title(f"Different Interpolations of $tan(x) \cdot sin(30*x)\cdot e^x$ for {n} samples")

    cs= CubicSpline(new_x_values, new_y_values)
    ak= Akima1DInterpolator(new_x_values,new_y_values)
    br= BarycentricInterpolator(new_x_values,new_y_values)

    line_spline.set_data(x_values, cs(x_values))
    line_akima.set_data(x_values, ak(x_values))
    line_bary.set_data(x_values, br(x_values))

anim= FuncAnimation(fig, animate, frames= 35, interval= 500)
plt.legend(loc='upper left')
plt.grid()
plt.show()
