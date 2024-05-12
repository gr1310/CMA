import matplotlib.pyplot as plt
import math
import scipy.integrate as sy
def y(x):
    return 2*x*math.exp(x**2)
M=[]
for i in range(20, 200, 5):
    M.append(i)
a=1
b=3
actual_area= (math.exp(b**2)-math.exp(a**2))
plt.axhline(y=actual_area, color='r', label= "Actual area")
area=[]

for m in M:
    x=[]
    for k in range(0,m+1):
        x.append(a+k*((b-a)/m))
    
    sum=0
    for i in range(1,m+1):
        sum+= y(x[i])+ y(x[i-1])
    
    area.append(((b-a)/(2*m))*sum)

plt.plot(M,area, label="Area using Trapezoidal formula")
plt.title("Area vs M")
plt.xlabel("Values of M")
plt.ylabel("Computed area")
plt.legend()
plt.grid()
plt.show()
print(area)


