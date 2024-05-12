import numpy as np
import math
import matplotlib.pyplot as plt

h=0.01
a=0
b=1
# mu= 5e-5
N= int(((b-a)/h)+1)
# print(N)
x= np.linspace(0,1,N)
u= np.zeros(N)
u[N//2]= math.exp(-1*N//2)
d2u_d2t=np.zeros(N)
u[0]=0
u[N-1]=0
for t in range(100):
    for i in range(1,N-1):
        u[i]+= (u[i-1]-2*u[i]+u[i+1])/4
    plt.clf()
    plt.plot(x,u)
    plt.ylim(0, 4.25*1e-23)
    plt.pause(0.001)
    

print(u)

# plt.plot(x,u)

plt.show()