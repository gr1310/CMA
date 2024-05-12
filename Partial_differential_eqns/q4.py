import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-4

def f_(x):
    return 2*x

def newton_raphson():
    y=[]
    i=[]
    x= -10
    y.append(x)
    delta=1e10
    iterations=1
    i.append(iterations)
    while(delta>1e-10):
        x_new= x- (f(x)/f_(x))
        delta= abs(x_new-x)
        x=x_new
        y.append(x)
        iterations+=1
        i.append(iterations)
    return i,y

def secant():
    y=[]
    i=[]
    x_prev=-100
    x=-10
    y.append(x)
    delta= 1e10
    iterations=1
    i.append(iterations)
    while(delta>1e-10):
        x_new= x- f(x)*((x-x_prev)/(f(x)-f(x_prev)))
        delta= abs(x_new-x)
        x_prev= x
        x= x_new
        y.append(x)
        iterations+=1
        i.append(iterations)
    return i,y
def comparing_two():
    i_n, y_n= newton_raphson()
    i_s, y_s= secant()
    i= max(i_n,i_s)
    while(len(i_n)>len(i_s)):
        i_s.append(0)
        y_s.append(y_s[-1])
    while(len(i_s)>len(i_n)):
        i_n.append(0)
        y_n.append(y_n[-1])
    plt.plot(i,y_n, label="newton raphson")
    plt.plot(i,y_s, label= "Secant method")
    plt.legend()
    plt.show()

comparing_two()