import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lg

def f1(x1,x2,x3):
    return 3*x1-np.cos(x2*x3)-3/2

def f2(x1,x2,x3):
    return 4*(x1**2)-625*(x2**2)+2*x3-1

def f3(x1,x2,x3):
    return 20*x3+np.exp(-x1*x2)+9

def func(x):
    x1,x2,x3=x
    return [f1(x1,x2,x3), f2(x1,x2,x3), f3(x1,x2,x3)]
def Jacobian_matrix(x):
    x1,x2,x3=x
    j1= [3, x3*np.sin(x2*x3), x2*np.sin(x2*x3)]
    j2=[8*x1, -1250*x2, 2]
    j3=[-x2*np.exp(-x1*x2), -x1*np.exp(-x1*x2), 20]

    return [j1,j2,j3]

def solve():
    x1=1
    x2=2
    x3=3
    x= [x1,x2,x3]
    J_1= lg.inv(Jacobian_matrix(x))
    delta= 1e10
    f= func(x)
    y=[lg.norm(func(x))]
    it=1
    iterations=[it]
    while(delta>1e-6):
        x_new= x- lg.inv(Jacobian_matrix(x)) @ func(x)
        delta= np.sum(abs(x_new-x))
        x=x_new
        y.append(lg.norm(func(x)))
        it+=1
        iterations.append(it)
    print("Roots are ",x)
    plt.plot(iterations,y)
    plt.show()
solve()