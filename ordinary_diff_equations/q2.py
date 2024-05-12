# Backward euler

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import interpolate
x_list=[]
h_list= [0.1, 0.5, 1, 2, 3]
t0=0
T=10
t_list=[]
for h in h_list:
    x=[5]
    Nh=int((T-t0)/h)
    for n in range(1,Nh+1):
        x.append(x[n-1]/(1+2*h))
    # print(n)
    t= list(np.linspace(0,10,n+1))
    # print(len(x),len(t))
    x_list.append(x)
    t_list.append(t)
    
for i in range(len(h_list)):
    # print(x_list[i])
    y_pts= x_list[i]
    x_pts= t_list[i]
    y_actual= [5*math.exp(-2*i) for i in x_pts]

    f= interpolate.interp1d(x_pts,y_pts)
    y_new= f(x_pts)
    plt.scatter(x_pts,y_pts, color='yellow')
    plt.plot(x_pts,y_new, color='green', label="Approximated curve")
    plt.plot(x_pts, y_actual, color='orange', label="Actual curve")
    plt.title(f"For h={h_list[i]}")
    plt.legend()
    plt.show()
