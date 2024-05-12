import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as sc
import scipy.fft 

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
        plt.plot(x_axis,y_axis, label="Polynomial function")
        plt.xlabel("x")
        plt.ylabel("P(x)")
        plt.legend()
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

#------------------------------------------------- Lab 5 ------------------------------------------------------------------
    
def best_fit_polynomial(n, points):
    xi= [i[0] for i in points]
    yi= [i[1] for i in points]
    m=len(points)
    list_of_coeff=[]
    for j in range(0,n+1):
        eqn_i=[]
        for k in range(0,n+1):
            sum=0
            for i in range(0,m):
                sum+=(xi[i])**(j+k)
            eqn_i.append(sum)
        list_of_coeff.append(eqn_i)
    print(list_of_coeff)

    list_of_rhs=[]
    for j in range(n+1):
        sum=0
        for i in range(m):
            sum+=yi[i]*(xi[i]**j)
        list_of_rhs.append(sum)
    print(list_of_rhs)

    list_of_coeff= np.array(list_of_coeff)
    list_of_rhs= np.array(list_of_rhs)

    x= Polynomial(list(np.linalg.solve(list_of_coeff,list_of_rhs)))
    print(x)
    plt.scatter(xi,yi)
    x.show(-3,3)

def f(x,j):
    return x**j

def func(x,j):
    return (x**j)*(math.sin(x)+math.cos(x))

def best_approx_function(n):
    a=0
    b=math.pi
    coeff=[]
    for j in range(n+1):
        eq_i=[]
        for k in range(n+1):
            eq_i.append(sc.quad(f,a,b,args=(j+k,))[0])
        coeff.append(eq_i)
    print(coeff)

    rhs=[]
    for j in range(n+1):
        rhs.append(sc.quad(func, a, b, args=(j,))[0])
    print(rhs)
    coeff=np.array(coeff)
    rhs= np.array(rhs)
    x= Polynomial(list(np.linalg.solve(coeff,rhs))) 
    print(x)

    x_axis=np.linspace(a,b,100)

    y_axis= [math.sin(i)+math.cos(i) for i in x_axis]

    plt.plot(x_axis,y_axis, label="Actual function")


    x.show(a,b)

def nth_Legendre_polynomial(n):
    
    p_x= Polynomial([-1,0,1])
    for i in range(n-1):
        p_x= p_x*p_x
    if(n==0): p_x=Polynomial([0])
    # print(p_x)

    for i in range(n):
        p_x= p_x.derivative()
    # print(p_x)

    const=(1/((2**n)*math.factorial(n)))

    p_x= const*p_x
    return p_x


def function(x, p):
    coeff= p.poly()
    sum=0
    for i in range(len(coeff)):
        sum+= coeff[i]*(x**i)
    
    return math.exp(x)-sum

def LSA_using_n_Legendre_polynomials(n):
    phi=[]
    for i in range(1,n+1):
        phi.append(nth_Legendre_polynomial(i))
    c_j=[]
    for poly in phi:
        print(poly)
        new_poly= poly*poly
        c_j.append(new_poly.area(-1,1))
    print(c_j)

    a_j=[]
    for i in range(n):
        a= (1/c_j[i])*(sc.quad(function,))

def nth_Chebyshev_polynomial(n):
    if(n==0):
        return Polynomial([1])
    elif(n==1):
        return Polynomial([0,1])
    else:
        poly_coeff= 2*Polynomial([0,1])
        return poly_coeff*nth_Chebyshev_polynomial(n-1) - nth_Chebyshev_polynomial(n-2)

def first_5_chebyshev_poly():
    result=[]
    for i in range(5):
        result.append(nth_Chebyshev_polynomial(i))
    
    return result

def chebyshev_orthogonality(x,coeff1):
    y=0
    value=0
    for i in range(len(coeff1.poly)):
        value+=(pow(x,i)*coeff1.poly[i])
    y= value*(1/math.sqrt(1-(x**2)))
    return y
    

def orthogonality_test_chebyshev():
    lst=[]
    for p1 in first_5_chebyshev_poly():
        dummy=[]
        for p2 in first_5_chebyshev_poly():
            poly= p1*p2
            value= sc.quad(chebyshev_orthogonality,-1,1, args=(poly,))[0]
            # print(value)
            if(value<1e-11):
                value=0
            dummy.append(value)
        lst.append(dummy)

    print(np.array(lst))

def fcos(x,k):
    return (math.exp(x)*math.cos(k*x))
def fsin(x,k):
    return (math.exp(x)*math.sin(k*x))

def fourier_series_approximation(n):
    ak=[]
    bk=[]
    for k in range(0,n+1):
        ak.append((1/math.pi)*(sc.quad(fcos,-math.pi,math.pi, args=(k,))[0]))
        bk.append((1/math.pi)*(sc.quad(fsin,-math.pi,math.pi, args=(k,))[0]))
    print(ak)
    print(bk)
    ak[0]=ak[0]/2
    x_axis= list(np.linspace(-math.pi+0.5, math.pi-0.5, 1000))
    y_axis=[]
    y_actual=[]
    sn=0
    for x in x_axis:
        for k in range(0,n+1):
            sn+=((ak[k]*(math.cos((k)*x)))+ (bk[k]*(math.sin((k)*x))))
        print(sn, math.exp(x))
        y_axis.append(sn)
        y_actual.append(math.exp(x))
        sn=0
    plt.plot(x_axis,y_axis)
    plt.plot(x_axis,y_actual)
    plt.show()





# points= [ (0,1),(1,4),(-1,0),(2,15)]
# best_fit_polynomial(5, points)

# best_approx_function(4)

# print(nth_Legendre_polynomial(2))
# LSA_using_n_Legendre_polynomials(3)

# print(nth_Chebyshev_polynomial(3))

# fourier_series_approximation(10)

