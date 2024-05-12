import matplotlib.pyplot as plt
import math
import scipy.integrate as integrate
import numpy as np

def y(x):
    return (2*x)*(math.exp(x**2))

f= lambda x: (2*x)*(np.exp(x**2))
# print(integrate.romb(f))
u=[]

quad_integral=[]
fixed_quad_integral=[]
trapz_integral=[]
simps_integral=[]
actual_area=[]
for i in range(1,4):
    u.append(i)
    a=0
    b=i
    actual_area.append(math.exp(b**2)-math.exp(a**2))
    quad_integral.append(integrate.quad(f, a, b)[0])
    fixed_quad_integral.append(integrate.fixed_quad(f,a,b,n=5)[0])
    x= np.linspace(0,b,1000)
    trapz_integral.append(integrate.trapz(f(x),x))
    simps_integral.append(integrate.simps(f(x),x))

plt.plot(u, quad_integral, label="Quad integral",color='y', linewidth=5)
plt.plot(u, fixed_quad_integral, label="Fixed Quad integral")
plt.plot(u, trapz_integral, label="Trapz integral", linewidth= 3)
plt.plot(u, simps_integral, label="Simps integral")
plt.plot(u, actual_area, label="Actual area", color="black")
plt.xlabel("u")
plt.ylabel("integral values")
plt.legend()
plt.grid()
plt.show()

