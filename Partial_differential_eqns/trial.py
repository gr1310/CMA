# import numpy as np

# print(np.eye(3,k=-1))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define parameters
L = 1  # length of the rod
T = 1  # total time
Nx = 100  # number of spatial grid points
Nt = 200  # number of time steps
dx = L / Nx
dt = T / Nt
x = np.linspace(0, L, Nx+1)
t = np.linspace(0, T, Nt+1)

# Initial condition
def initial_condition(x):
    return np.exp(-x)

u = initial_condition(x)

# Finite difference method to solve the PDE
def heat_conduction(u):
    u_new = np.copy(u)
    for i in range(1, Nx):
        u_new[i] = u[i] + dt * (u[i-1] - 2*u[i] + u[i+1]) / dx**2
    return u_new

# Create figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, u, color='red')

# Animation function
def animate(frame):
    global u
    u = heat_conduction(u)
    line.set_ydata(u)
    return line,

# Set up animation
ani = FuncAnimation(fig, animate, frames=Nt, interval=50, blit=True)

# Set plot labels and title
ax.set_xlabel('Position')
ax.set_ylabel('Temperature')
ax.set_title('Heat Conduction in a Rod')

# Show plot
plt.show()
