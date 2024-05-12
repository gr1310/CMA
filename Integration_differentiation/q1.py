
import math
import matplotlib.pyplot as plt
import numpy as np

class Visualize:
    def __init__(self):
        # self.function= math.sin(pow(x,2))
        self.actual_derivative= []
        pass
    
    def f(self,x):
        return math.sin(pow(x,2))
    def derivativeVisualize(self):
        x_axis= list(np.linspace(0,1,50))

        for x in x_axis:
            self.actual_derivative.append(2*x*math.cos(pow(x,2)))

        h= 0.01

        error_fd=[]
        self.forward_difference(error_fd,x_axis, h)

        error_bd=[]
        self.backward_difference(error_bd, x_axis, h)
        
        error_cd=[]
        self.centered_difference(error_cd, x_axis, h)

        plt.plot(x_axis,error_fd,'r', label="Forward difference")
        plt.plot(x_axis,error_bd, label="Backward difference")
        plt.plot(x_axis,error_cd, label="Centered difference")
        plt.legend()
        plt.show()

    def backward_difference(self, error, x_axis,h):
        computed_backward_derivative=[]
        for x in x_axis:
            b_d= (self.f(x)-self.f(x-h))/h
            computed_backward_derivative.append(b_d)
        for i in range(len(x_axis)):
            error.append(abs(self.actual_derivative[i]-computed_backward_derivative[i]))

    def forward_difference(self, error, x_axis,h):
        computed_forward_derivative=[]
        for x in x_axis:
            f_d= (self.f(x+h)-self.f(x))/h
            computed_forward_derivative.append(f_d)
        for i in range(len(x_axis)):
            error.append(abs(self.actual_derivative[i]-computed_forward_derivative[i]))
    
    def centered_difference(self, error, x_axis,h):
        computed_centered_derivative=[]
        for x in x_axis:
            c_d= (self.f(x+h)-self.f(x-h))/(2*h)
            computed_centered_derivative.append(c_d)

        for i in range(len(x_axis)):
            error.append(abs(self.actual_derivative[i]-computed_centered_derivative[i]))

    def forward_difference_approximation(self, error, x_axis,h):
        for x_ in x_axis:
            x=x_+h
            f__= 2*math.cos(x**2)- 4*(x**2)*math.sin(x**2)
            error.append(abs((h/2)*f__))
        # print(error)
    
    def centered_difference_approximation(self, error, x_axis,h):
        for x_ in x_axis:
            x=x_+h
            f_3= -12*x*math.sin(x**2)+ 8*(x**3)*math.cos(x**2)
            error.append(abs(((h**2)/6)*f_3))
        # print(error)

    def max_abs_error(self):
        x_axis= list(np.linspace(0,1,10))

        self.actual_derivative=[]
        for x in x_axis:
            self.actual_derivative.append(2*x*math.cos(pow(x,2)))

        h_list= list(np.linspace(0.01, 0.1, 100))

        # using formula
        max_approx_error_fd=[]
        for h in h_list:
            error= []
            self.forward_difference_approximation(error, x_axis, h)
            max_approx_error_fd.append(max(error))
        

        # theoritical
        max_abs_error_fd=[]
        for h in h_list:
            error_fd=[]
            self.forward_difference(error_fd, x_axis, h)
            max_abs_error_fd.append(max((error_fd)))
            # max_abs_error_fd.append(mean_error)

        # using formula
        max_abs_error_cd=[]
        for h in h_list:
            error_cd=[]
            self.centered_difference(error_cd, x_axis, h)
            max_abs_error_cd.append(max((error_cd)))
       
        # theoritical
        max_approx_error_cd=[]
        for h in h_list:
            error_cd=[]
            self.centered_difference_approximation(error_cd, x_axis, h)
            max_approx_error_cd.append(max((error_cd)))
        
        plt.plot(h_list,max_abs_error_fd, label="Absolute maximum error in forward difference")
        plt.plot(h_list,max_approx_error_fd, label="Absolute maximum approximate error in forward difference")
        plt.plot(h_list,max_abs_error_cd, label="Absolute maximum error in centered difference")
        plt.plot(h_list,max_approx_error_cd, label="Absolute maximum approximate error in center difference")
        
        plt.legend()
        plt.show()
    




der= Visualize()
# der.derivativeVisualize()
der.max_abs_error()