import numpy as np
import matplotlib.pyplot as plt

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
        print("Matrix b is \n",b)

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
        print("Matrix A is \n",a)

        # a_1= np.linalg.inv(a)
        # print("Matrix A-1 is \n", a_1)

        coeff= np.linalg.solve(a,b)
        print(coeff)

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
        plt.plot(x_axis,y_axis)
        plt.grid()
        plt.show()

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






# p = Polynomial([1, 2, 3])
# print(type(p))

# p1 = Polynomial([1, 2, 3])
# p2 = Polynomial([3, 2, 1])
# p3 = p1 + p2
# print(p3)

# p4 = p1 - p2
# print(p4)

# p1 = Polynomial([1, 2, 3])
# p2 = (-0.5)*p1
# print(p2)

# p1 = Polynomial([-1, 1])
# p2 = Polynomial([1, 1, 1])
# p3 = p1 * p2
# print(p3)

# p = Polynomial([1, 2, 3])
# print(p[2])

# p = Polynomial([1, -1, 1, -1])
# p.show(-1, 2)

# p = Polynomial([])
# p.fitViaMatrixMethod([(1,4), (0,1), (-1, 0), (2, 15), (3,12)])

# p = Polynomial([])
# # p.fitViaLagrangePoly([(0, 1), (1, 4), (-1, 0),(2, 15)])
# p.fitViaLagrangePoly([(1,-4), (0,1), (-1, 4), (2, 4), (3,1)])


