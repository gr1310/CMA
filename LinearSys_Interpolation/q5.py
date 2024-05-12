import matplotlib.pyplot as plt
import math 
import numpy as np
import scipy.interpolate as sc

def f(x):
    return math.tan(x)* math.sin(30*x)*math.exp(x)


def animation():
    n=2
    x_axis= np.linspace(0,1,1000)
    x_axis=list(x_axis)

    true_func= [f(i) for i in x_axis]
    plt.plot(x_axis,true_func)

    while(n<=10):
        x_axis= np.linspace(0,1,n)
        x_axis=list(x_axis)
        func_at_i= [f(i) for i in x_axis]
        cs= sc.CubicSpline(x_axis,func_at_i)
        plt.plot(x_axis, cs(x_axis))
        # print(cs)

        ak= sc.Akima1DInterpolator(x_axis,func_at_i)
        # print(ak)
        plt.plot(x_axis,ak(x_axis))

        x = np.linspace(min(x_axis), max(x_axis), num=100)

        y= sc.barycentric_interpolate(x_axis,func_at_i, x)
        # print(y)
        plt.plot(x, y)
        plt.show()

        n+=1

animation()