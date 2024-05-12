import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sy
class Integration:
    def __init__(self):
        pass

    def f(self,x):
        return 2*x*math.exp(pow(x,2))
        
    
    def plot(self):
        x_axis= list(np.linspace(1,3,10))
        y_axis=[]
        for x in x_axis:
            y_axis.append(self.f(x))
        
        plt.plot(x_axis,y_axis)
        plt.show()
    
    def computed_area(self):
        M=10
        a=1
        b=3
        x_axis= [0]*(M+1)
        for k in range(M+1):
            x_axis[k]=a+k*((b-a)/M)
        
        # print(x_axis)
        m=[]
        im=[]
        for j in range(1,M+1):
            m.append(j)
            const= (b-a)/(2*j)
            sum=0
            for k in range(1,j+1):
                sum+=(self.f(x_axis[k])+self.f(x_axis[k-1]))
            im.append(const*sum)
        
        # print(m, im)
        print(im[-1])
        plt.plot(m, im)
        plt.show()

        # print(len(x_axis))
        # h_2= (b-a)/(2*M)
        # sum=0
        # for k in range(1,M+1):
        #     sum+=(self.f(x_axis[k])-self.f(x_axis[k-1]))
        # sum= h_2*sum
        # print(sum)

        print(sy.quad(self.f, a,b ))



i= Integration()
# i.plot()
i.computed_area()