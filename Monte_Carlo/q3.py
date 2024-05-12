import math
from random import random
import matplotlib.pyplot as plt

PI= math.pi

def iterate(n):
    no_in_circle=0
    no_out_circle=n

    x_axis=[]
    actual_pi=[]
    pi=[]
    for i in range(1,n):
        x_cor= random()-0.5
        y_cor= random() -0.5

        x_axis.append(i)
        actual_pi.append(PI)
        lhs= x_cor**2+ y_cor**2
        if(lhs< (0.25)):
            no_in_circle+=1
        pi.append((no_in_circle/i)*4)

    plt.plot(x_axis,pi)
    plt.plot(x_axis, actual_pi)
    plt.ylim(3.1,3.2)
    plt.show()
    # print(no_in_circle, no_out_circle)
    # expected_pi= (no_in_circle/no_out_circle)*4
    # print(expected_pi)
iterate(2000000)