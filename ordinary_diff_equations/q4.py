# Van der Pol equation

#  x'=y
# y'= mu*(1-x^2)*y-x

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

def func(t, z, mu):
    x,y=z
    return [y, mu*(1-x**2)*y-x]

mu_list=[0,2/3,1,2,3]
for mu in mu_list:
    t=np.linspace(0,10,500)
    solution= solve_ivp(func,(0,10),(1,0),t_eval=t, args=(mu,))
    # print(solution.y[0], solution.y[1])
    plt.plot(solution.y[0], solution.y[1])
    # plt.plot(t, solution.y[0])
plt.show()