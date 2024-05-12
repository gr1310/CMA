from q1 import RowVectorFloat 
import random
import math
import matplotlib.pyplot as plt

def handleException(method):
    def decorator(ref, *args, **kwargs):
        try:
            method(ref, *args, **kwargs)
        except Exception as err:
            print(type(err))
            print(err)
            return None
    return decorator

class SquareMatrixFloat():
    def __init__(self, dim):
        self.matrix=[]
        for i in range(dim):
            self.matrix.append(RowVectorFloat([0]*dim))
        self.dim= dim
        self.size=dim
    
    def __str__(self) -> str:
        result="The matrix is\n"
        for i in self.matrix:
            for j in i:
                # print(j, end=" ")
                result= result+str(j)+" "
            result+="\n"
        return result
    
    def sampleSymmetric(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if(i==j):
                    # random.seed(10)
                    self.matrix[i][j]= random.uniform(0,self.dim)
                    # print((i,j),self.matrix[i][j])
                else:
                    # random.seed(10)
                    self.matrix[i][j]= random.uniform(0,1)
    
                    
    def toRowEchelonForm(self):
        pivot=0
        vis=[]
        start=0

        while (start<self.dim):
            for i in range(self.dim):
                if(self.matrix[i][start]!=0 and i not in vis):
                    pivot=self.matrix[i][start]
                    temp= self.matrix[start]
                    self.matrix[start]= self.matrix[i]
                    self.matrix[i]= temp
                    vis.append(i)
                    break
                    # start+=1
            for i in range(self.dim):
                self.matrix[start][i]/=pivot

            start_mat= self.matrix[start]
            for i in range(start+1, self.dim):
                val= self.matrix[i][start]
                self.matrix[i]= self.matrix[i]-val*start_mat
            start+=1
    
    def isDRDominant(self):
        diagnol_ele=[]
        for i in range(self.dim):
            diagnol_ele.append(self.matrix[i][i])
        for i in range(self.dim):
            for j in range(self.dim):
                if(i!=j and self.matrix[i][j]>diagnol_ele[i]):
                    return False
        return True
    # @handleException
    def jSolve(self,b, it) -> tuple:
        if(type(b)==list and type(it)==int):
            if(self.isDRDominant()):
                x=[0]*self.dim
                A=self.matrix
                rows=[]
                while it:
                    e=[]
                    row=0
                    m_sum=0
                    for i in range(self.dim):
                        k= 1/A[i][i]
                        bi= b[i]
                        sum=0
                        for j in range(self.dim):
                            m_sum+=(A[i][j]*x[j])
                            if(j==i):
                                pass
                            else:
                                sum+=(A[i][j]*x[j])
                        x[i]= k*(bi-sum)
                        e.append(m_sum-bi)
                    for xi in e:
                        row+=pow(xi,2)
                    rows.append(math.sqrt(row))
                    it-=1
                return((rows,x)) 
            else:
                raise Exception("Not solving because convergence is not guranteed.")
        else:
            raise Exception("Invalid types passed")
   
    def jVisualize(self,b):
        if(type(b)==list):
            # if(self.isDRDominant()):
                x=[0]*self.dim
                A=self.matrix
                rows=[]
                old_error=0
                error= 100
                y_axis=[]
                while abs(error-old_error)>0.00001:
                    e=[]
                    row=0
                    m_sum=0
                    for i in range(self.dim):
                        k= 1/A[i][i]
                        bi= b[i]
                        sum=0
                        for j in range(self.dim):
                            m_sum+=(A[i][j]*x[j])
                            if(j==i):
                                pass
                            else:
                                sum+=(A[i][j]*x[j])
                        x[i]= k*(bi-sum)
                        e.append(m_sum-bi)
                    for xi in e:
                        row+=pow(xi,2)
                    rows.append(math.sqrt(row))
                    error= math.sqrt(row)
                    if(len(rows)>2): 
                        old_error= rows[-2]
                        y_axis.append(abs(error-old_error))
                    print(error)
                    
                print((error,x)) 
                x_axis= [i for i in range(len(y_axis))]
                # plt.plot(x_axis,y_axis)
                # plt.show()
                return [x_axis, y_axis]
            # else:
            #     raise Exception("Not solving because convergence is not guranteed.")
        else:
            raise Exception("Invalid types passed")
    
    
    def gsSolve(self,b, it) -> tuple:
        if(type(b)==list and type(it)==int):
            if(self.isDRDominant()):
                x=[0]*self.dim
                A=self.matrix
                rows=[]
                while it:
                    e=[]
                    row=0
                    m_sum=0
                    # x_new=[0]*self.dim
                    for i in range(self.dim):
                        x_new=[0]*self.dim
                        k= 1/A[i][i]
                        bi= b[i]
                        l_sum=0
                        r_sum=0
                        for j in range(self.dim):
                            m_sum+=(A[i][j]*x[j])
                            if(j==i):
                                pass
                            elif(j<i):
                                l_sum+=(A[i][j]*x_new[j])
                            else:
                                r_sum+=(A[i][j]*x[j])
                        x_new[i]= k*(bi-l_sum-r_sum)
                        x[i]=x_new[i]
                        e.append(m_sum-bi)
                    for xi in e:
                        row+=pow(xi,2)
                    rows.append(math.sqrt(row))
                    it-=1
                return((rows,x)) 
            else:
                raise Exception("Not solving because convergence is not guranteed.")
        else:
            raise Exception("Invalid types passed")
    
    def gsVisualize(self,b):
        if(type(b)==list):
            # if(self.isDRDominant()):
                x=[0]*self.dim
                A=self.matrix
                # rows=[]
                old_error=0
                error= 100
                rows=[]
                y_axis=[]
                while abs(error-old_error)>0.00001:
                    e=[]
                    row=0
                    m_sum=0
                    
                    for i in range(self.dim):
                        x_new=[0]*self.dim
                        k= 1/A[i][i]
                        bi= b[i]
                        l_sum=0
                        r_sum=0
                        for j in range(self.dim):
                            m_sum+=(A[i][j]*x[j])
                            if(j==i):
                                pass
                            elif(j<i):
                                l_sum+=(A[i][j]*x_new[j])
                            else:
                                r_sum+=(A[i][j]*x[j])
                        x_new[i]= k*(bi-l_sum-r_sum)
                        x[i]=x_new[i]
                        e.append(m_sum-bi)
                    for xi in e:
                        row+=pow(xi,2)
                    rows.append(math.sqrt(row))
                    error= math.sqrt(row)
                    if(len(rows)>2): 
                        old_error= rows[-2]
                        y_axis.append(abs(error-old_error))
                    print(error)
                    
                print((error,x)) 
                x_axis= [i for i in range(len(y_axis))]
                # plt.plot(x_axis,y_axis)
                # plt.show()
                return [x_axis, y_axis]
            # else:
            #     raise Exception("Not solving because convergence is not guranteed.")
        else:
            raise Exception("Invalid types passed")
        
    def visualize(self,b):
        if(self.isDRDominant()):
            gsPlot= self.gsVisualize(b)
            jPlot= self.jVisualize(b)
            print(gsPlot)
            print(jPlot)

            plt.plot(gsPlot[0][1:],gsPlot[1][1:],"r", label="Gauss- Siedel")
            plt.plot(jPlot[0][1:],jPlot[1][1:],"b",label= "Jacobi")
            plt.xlabel("Number of iterations")
            plt.ylabel("Error")
            plt.legend()
            plt.show()
        else:
            raise Exception("Not solving because convergence is not guranteed.")



    
s = SquareMatrixFloat(4)
s.sampleSymmetric()
print(s)


# s.toRowEchelonForm()
# print("\nAfter echlon form: \n")
# print(s)

# q=([RowVectorFloat([0.20,0.31,0.41,0.47]), RowVectorFloat([0.31, 1.53, 0.42, 0.28]), RowVectorFloat([0.41, 0.42, 2.48, 0.91]),RowVectorFloat([0.47, 0.28, 0.91, 1.07])])
# q.toRowEchelonForm()
# print(q)

# print(s.isDRDominant())
(e,x)=s.jSolve([1, 2, 3, 4], 10)

# print(e)
# print(x)

# (err, x) = s.gsSolve([1, 2, 3, 4], 10)
# print(x)
# print(err)

# s.visualize([1,2,3,4])