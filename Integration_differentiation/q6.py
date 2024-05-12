import numpy as np
import matplotlib.pyplot as plt
import math

class Polynomial:
    def __init__(self, lst):
        self.poly=lst

    def __str__(self):
        result="Coefficients of the polynomial are:\n"
        for i in self.poly:
            result+=str(i)+" "
        return result
    
    def __add__(self, other):
        result=[]
        n= len(self.poly)
        m= len(other.poly)
        if(m==n):
            for i in range(m):
                result.append(self.poly[i]+other.poly[i])
        elif(m>n):
            for i in range(n):
                result.append(self.poly[i]+other.poly[i])
            for i in range(n,m):
                result.append(other.poly[i])
        else:
            for i in range(m):
                result.append(self.poly[i]+other.poly[i])
            for i in range(m,n):
                result.append(self.poly[i])
        return Polynomial(result)
    
    def __sub__(self, other):
        result=[]
        n= len(self.poly)
        m= len(other.poly)
        if(m==n):
            for i in range(m):
                result.append(self.poly[i]-other.poly[i])
        elif(m>n):
            for i in range(n):
                result.append(self.poly[i]-other.poly[i])
            for i in range(n,m):
                result.append(-1*other.poly[i])
        else:
            for i in range(m):
                result.append(self.poly[i]-other.poly[i])
            for i in range(m,n):
                result.append(self.poly[i])
        return Polynomial(result)
    
    def __rmul__(self, num):
        result=[]
        if((type(num)==float or type(num)==int) and type(self)==Polynomial):
            for i in range(len(self.poly)):
                result.append(num*self.poly[i])

        return Polynomial(result)
    
    def __mul__(self, num):
        max_degree= len(self.poly)+len(num.poly)-1
        # print(max_degree)
        result= [0]*max_degree
        if (type(self)==Polynomial and type(num)==Polynomial):
            
            for i in range(len(self.poly)):
                for j in range(len(num.poly)):
                    result[i+j]+=(self.poly[i]*num.poly[j])

        return Polynomial(result)

    def __getitem__(self,x):
        result=0
        for i in range(len(self.poly)):
            result+=self.poly[i]*pow(x,i)
        return result
    
    def show(self,a,b):
        x_axis= list(np.linspace(a,b,50))
        y_axis=[]
        for x in x_axis:
            y_axis.append(self[x])
        # print(y_axis)
        exp=""
        for i in range(len(self.poly)):
            if(i==0): 
                exp+= f"{self.poly[i]}"
            else:
                if(self.poly[i]>=0):
                    exp+=f"+{self.poly[i]}x^{i}"
                else:
                    exp+=f"{self.poly[i]}x^{i}"
        # exp=exp[:-1]
        print(exp)
        plt.title(f"${exp}$")
        plt.plot(x_axis,y_axis)
        plt.xlabel("x")
        plt.ylabel("P(x)")
        plt.grid()
        plt.show()
    def fitViaMatrixMethod(self,points):
        size= len(points)
        lst= [1]*size
        # print(lst)
        dummy= Polynomial(lst)
        # print(dummy)
        b=[]
        for _,y in points:
            b.append(y)
        b= np.array(b)
        # print("Matrix b is \n",b)

        a=[]
        x_pts=[]
        for x,_ in points:
            x_pts.append(x)
        # print(x_pts)

        for i in range(len(x_pts)):
            x_pt= x_pts[i]
            lst=[]
            for j in range(len(dummy.poly)):
                lst.append(pow(x_pt,j)*dummy.poly[j])
            a.append(lst)

        a= np.array(a)
        # print("Matrix A is \n",a)

        # a_1= np.linalg.inv(a)
        # print("Matrix A-1 is \n", a_1)

        coeff= np.linalg.solve(a,b)
        # print(coeff)

        self.poly= coeff

        x_axis= np.linspace(-1,3,50)
        y_axis=[]
        for x in x_axis:
            value=0
            for i in range(len(coeff)):
                value+=(pow(x,i)*coeff[i])
            y_axis.append(value)

        plt.scatter(x_pts,b, c="red")
        plt.title("Polynomial interpolation using matrix method")
        plt.ylabel("f(x)")
        plt.xlabel("x")
        # plt.plot(x_axis,y_axis)
        plt.grid()
        # plt.show()

    def fitViaLagrangePoly(self, points):
        y_pts=[]
        for _,y in points:
            y_pts.append(y)
        y_pts= np.array(y_pts)

        # print(y_pts)

        x_pts=[]
        for x,_ in points:
            x_pts.append(x)

        # print(x_pts)

        sol=[]

        for i in range(len(x_pts)):
            value=Polynomial([1])
            const=1
            for j in range(len(x_pts)):
                if(i!=j):
                    const=float(-1/(x_pts[j]-x_pts[i]))
                    key= const*Polynomial([-1*x_pts[j],1])
                    value*=key
            # print(value)
            sol.append(value)
        # print(sol)
        coeff=Polynomial([])
        for i in range(len(y_pts)):
            coeff+= (y_pts[i]*sol[i])
        print(coeff.poly)

        x_axis= np.linspace(-1,3,50)
        y_axis=[]
        for x in x_axis:
            value=0
            for i in range(len(coeff.poly)):
                value+=(pow(x,i)*coeff.poly[i])
            # print(value)
            y_axis.append(value)

        plt.scatter(x_pts,y_pts, c="red")
        plt.title("Polynomial interpolation using Lang. method")
        plt.ylabel("f(x)")
        plt.xlabel("x")
        plt.plot(x_axis,y_axis)
        plt.grid()
        plt.show()
    
    def derivative(self):
        result=[]
        for i in range(1,len(self.poly)):
            result.append(i*self.poly[i])
        return Polynomial(result)

    def area(self, a, b):
        b_area= 0
        a_area=0
        for i in range(len(self.poly)):
            coeff= self.poly[i]
            b_area+= (((b**(i+1))*coeff)/(i+1))
            a_area+= (((a**(i+1))*coeff)/(i+1))
        area_cal= b_area-a_area
        # return f"Area in the interval [{a}, {b}] is: {area_cal}"
        return area_cal



# p = Polynomial([1, 2, 3])
# pd = p.derivative()
# print(pd)

# print(p.area(1,2))

def fact(n):
    if(n==0 or n==1): return 1
    return n*fact(n-1)
# print(fact(5))




def visualize_using_taylor():
    inital_error= 100
    n=1
    final_area=0
    actual_area= (1/2)*(math.exp(1/2)*(math.sin(1/2)-math.cos(1/2))+1)
    while (inital_error> 0.0001):
        e_x=[]
        sin_x=[]
        for i in range(n):
            e_x.append(1/math.factorial(i))

            if(i%2!=0):
                sin_x.append(1/math.factorial(i))
            else:
                sin_x.append(0)
        poly_e_x= Polynomial(e_x)
        poly_sin_x= Polynomial(sin_x)
        final_poly= poly_e_x*poly_sin_x
        new_area=final_poly.area(0,1/2)
        final_area= new_area
        inital_error= abs(actual_area- new_area)
        print("error",inital_error)
        n+=1

    print(actual_area)
    print(final_area)

# visualize_using_taylor()
    
def visualize_poly_fitting():
    error= 0.1
    actual_area= (1/2)*(math.exp(1/2)*(math.sin(1/2)-math.cos(1/2))+1)
    final_area=0
    n=1
    while(error>pow(10,-10)):
        e_x=[]
        e_x_poly= Polynomial([])
        sin_x=[]
        sinx_poly= Polynomial([])
        for i in range(n):
            f= math.exp(i/(2*n))
            g= math.sin(i/(2*n))
            e_x.append((i/(2*n),f))
            sin_x.append((i/(2*n),g))
        # print(e_x)
        e_x_poly.fitViaMatrixMethod(e_x)
        # print(e_x_poly)
        sinx_poly.fitViaMatrixMethod(sin_x)
        # print(sinx_poly)

        ex_sinx= e_x_poly*sinx_poly
        # print(ex_sinx)

        area= ex_sinx.area(0,1/2)
        final_area=area
        error= abs(final_area- actual_area)
        print(error)
        n+=1
    
    print(final_area, actual_area)


visualize_poly_fitting()