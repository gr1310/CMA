import math
import matplotlib.pyplot as plt
# import decimal
PI= math.pi

# num= int(input("Enter the value of num: "))
num=1000000

x_axis= [i for i in range(1,num,10)]
y_axis=[]
for n in x_axis:
    fact_n= math.log(math.factorial(n))
    if(n==0): log_f=1
    else: log_f= 1/2*(math.log(2*PI*n))+n*(math.log(n)- math.log(math.exp(1)))
    diff= fact_n-log_f
    y_axis.append(diff)
    
plt.ylim(-0.0005, 0.001)

plt.plot(x_axis,y_axis)
plt.show()
