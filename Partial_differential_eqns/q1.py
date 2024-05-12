import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def u_x(x):
    return np.exp(-x)

mu= 5e-5
a=0
b=1
L= b-a
h=0.01
Nx= int(L//h)+1
x=np.linspace(0,L,Nx+1)

T=2000
dt= 0.5
Nt= int(T//dt)+1
t=np.linspace(0,T,Nt+1)

u_initial= np.array(u_x(x))
# print(u_initial)

u_a= 0
u_b= 0
f= np.array([0 for i in x])
res= [u_initial]
A= np.eye(Nx+1, k=-1)*1+ np.eye(Nx+1,k=0)*-2+np.eye(Nx+1, k=1)*1

for i in t[1:]:
    du= ((mu/(h**2))*(A @ u_initial))+f
    u_initial= u_initial+ dt*du
    u_initial[0]=u_a
    u_initial[-1]=u_b
    res.append(u_initial)


fig,ax= plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(0, 1.1*np.max(res))
# ax.plot(x, res[0], label="initial")
line,= ax.plot([],[], label="animate")
def animate(i):
    line.set_data(x, res[i])
    return line,

anim= FuncAnimation(fig, animate, frames=len(res), interval= 50)
plt.legend(loc='upper left')
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.title('Heat Conduction in a Rod')
plt.grid()
plt.show()