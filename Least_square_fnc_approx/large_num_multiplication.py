import scipy.fft
import numpy as np
import matplotlib.pyplot as plt

def traditional_multiplication(num1,num2):
    num1=[int(i) for i in num1][::-1]
    num2=[int(i) for i in num2][::-1]
    sol=0
    for i in range(len(num2)):
        ans=0
        for j in range(len(num1)):
            num= num2[i]*num1[j]
            ans+=(10**j)*num
        sol+=ans*(10**i)
    return (sol)

def fft_multiplication(num1, num2):
    
    num1= [int(i) for i in num1][::-1]
    num2=[int(i) for i in num2[::-1]]
    N= 2*max(len(num1),len(num2))
    while(len(num1)<N):
        num1.append(0)
    while(len(num2)<N):
        num2.append(0)
    
    num1= np.array(num1)
    num2= np.array(num2)
    y=scipy.fft.fft(num1)

    y2= scipy.fft.fft(num2)

    y3= []
    for i in range(len(y)):
        y3.append(y[i]*y2[i])

    y1= scipy.fft.ifft(y3)
    ans=0
    for i in range(len(y1)):
        ans+= (10**i)*(y1[i])
    return (ans)



# num1= input("Enter number 1 ")
# num2= input("Enter number 2 ")
num1="1234"
num2="5678"

print(traditional_multiplication(num1, num2))
print(fft_multiplication(num1,num2))
