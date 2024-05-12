import numpy as np
import random
import math

class Matrix:
    def __init__(self, rows,cols) -> None:
        self.rows= rows
        self.cols= cols
        self.matrix= np.zeros([rows,cols])
        self.test= np.around(self.matrix[0], decimals=8)
    def __setitem__(self, index, val):

        i,j= index
        self.matrix[i,j]= val

    def __getitem__(self, index):
        return self.matrix[index[0],index[1]]
    
    def __str__(self):
        # print(self.matrix)
        # print(self.cols, self.rows)
        mat=""
        for i in range(self.rows):
            for j in range(self.cols):
                mat+=str(self.matrix[i][j])+" "
            mat+="\n"
        # return f"A {self.rows} x {self.cols} matrix with entries\n{self.matrix}"
        return f"A {self.rows} x {self.cols} matrix with entries\n{mat}"
    
    def __add__(self, matrix2):
        if(self.rows==matrix2.rows):
            if(self.cols== matrix2.cols):
                output= Matrix(self.rows, self.cols)
                for i in range(self.rows):
                    for j in range(self.cols):
                        output.matrix[i][j]= self.matrix[i][j]+matrix2.matrix[i][j]
                return output
            else:
                raise Exception("Matrix dimension mismatch")
        else:
            raise Exception("Matrix dimension mismatch")
    
    def __sub__(self, matrix2):
        if(self.rows==matrix2.rows):
            if(self.cols== matrix2.cols):
                output= Matrix(self.rows, self.cols)
                for i in range(self.rows):
                    for j in range(self.cols):
                        output.matrix[i][j]= self.matrix[i][j]-matrix2.matrix[i][j]
                return output
            else:
                raise Exception("Matrix dimension mismatch")
        else:
            raise Exception("Matrix dimension mismatch")

    def __mul__(self, matrix2):
        if(type(self)==Matrix):
            if(type(matrix2)==Matrix):
                if(self.cols== matrix2.rows):
                    output= Matrix(self.rows, matrix2.cols)

                    for i in range(self.rows):
                        for j in range(matrix2.cols):
                            for k in range(matrix2.rows):
                                output.matrix[i][j]+= self.matrix[i][k]+ matrix2.matrix[k][j]
                    return output
                else:
                    raise Exception("Matrix dimension mismatch")
            else:
                for i in range(self.rows):
                    for j in range(self.cols):
                        self.matrix[i][j]*=matrix2
                return self
    
    def __rmul__(self,num):
        if(type(num)==float or type(num)==int):
            if(type(self)==Matrix):
                for i in range(self.rows):
                    for j in range(self.cols):
                        self.matrix[i][j]*=num
            return self

    def toEye(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if(i==j):
                    self.matrix[i][j]=1
                else:
                    self.matrix[i][j]=0

    def toOne(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j]=1

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j]= random.uniform(0,1)
    def t(self):
        new_matrix=np.zeros([self.cols,self.rows])
        
        for i in range(self.cols):
            for j in range(self.rows):
                new_matrix[i][j]=self.matrix[j][i]
        output= Matrix(self.cols, self.rows)
        output.matrix= new_matrix
        return output

    def norm(self,p,q):
        ans=0
        for j in range(0,self.cols):
            inside_term=0
            for i in range(0, self.rows):
                inside_term+=(abs(self.matrix[i][j]))**p
            ans+=(inside_term)**(q/p)
        
        return (ans)**(1/q)
    

    def solvezero(self):
        A= self.matrix
        ans= Matrix(A.shape[1],1)
        if(A.shape[0]==A.shape[1]): return ans
        b= np.zeros(shape=(A.shape[0],1))
        Q, R = np.linalg.qr(A)
        ans.matrix[-1][0]= 1
        for i in range(len(ans.matrix)-2,-1,-1):
            ans.matrix[i] = (b[i] - np.dot(R[i, i+1:], ans.matrix[i+1:])) / R[i, i]
        return ans


    def dominantEigen(self, tol=0.00001):
        A=(self.matrix)
        ans= Matrix(A.shape[1],1)
        v = np.random.normal(size=A.shape[1])
        v = v / np.linalg.norm(v)
        previous = np.empty(shape=A.shape[1])
        iter=0
        while True:
            previous[:] = v
            v = A @ v
            v = v / np.linalg.norm(v)
            iter+=1
            if np.allclose(v, previous, atol=tol) or iter==100000:
                break
        lam= (np.transpose(v) @ A @ v)/ (np.transpose(v) @ v)
        for i in range(len(v)):
            ans.matrix[i][0]=v[i]
        return lam, ans
    
    def deflate(self):
        A= self.matrix
        e= Matrix(A.shape[0],1)
        v= Matrix(A.shape[0], A.shape[1])

        e1,v1= self.dominantEigen()

        for i in range(len(A)):
            e.matrix[i][0]=e1
            v.matrix[i]= v1.matrix.reshape(1,v1.matrix.shape[0])
            v1= v1.matrix
            B= A- (e1*(v1 @ np.transpose(v1)))
            B_mat= Matrix(B.shape[0], B.shape[1])
            B_mat.matrix= B
            e1, v1= B_mat.dominantEigen()
            A=B
        return e,v.t()
    
    def unshifted_qr(self):
        A= self.matrix
        Q,R= np.linalg.qr(A)

        while True:
            A= R @ Q
            Q, R= np.linalg.qr(A)

            if(np.sum(np.abs(A- np.diag(np.diag(A))))<1e-6):
                break

        eigen_values= np.diag(A)
        return eigen_values
    
    def eigen_vector(self):
        lambda_values= self.unshifted_qr()
        A= self.matrix
        v= []
        for e in lambda_values:
            # print(e)
            mat= A- e * np.eye(A.shape[0])
            # print(mat)
            try:
                ans= np.linalg.solve(mat, np.zeros(A.shape[0]))
            except np.linalg.LinAlgError:
                print("Singular matrix for eigenvalue:", e)
                ans= np.zeros(A.shape[0])
            print(ans.reshape(-1,1))
            v.append(ans)
        return v
    
    def svd(self):
        M= self.matrix
        MMT= M @ np.transpose(M)
        MTM= np.transpose(M) @ M

        # e_mmt= 

  


# m = Matrix(3, 4)
# print(m.matrix)
# print(m.test)
# m[1, 1] = 2
# print(m.matrix)
# m[2, 3] = 4
# print(m[2, 3])
# m.toOne()
# print(m)

# print(m.matrix)
# print(m)

# m = Matrix(4, 3)
# m.toEye()
# print(m)
# m.randomize()
# print(m)
# # m.t()
# print(m.t())

# m1 = Matrix(2, 3); m1.randomize(); print(m1)
# m2 = Matrix(3, 2); m2.randomize(); print(m2)
# print(m1+m2.t())
# print(m2.t()- m1)
# print(m1 * m2)
# print(m1 * m2.t())
# m1 = 2 * m1; print(m1)

# m = Matrix(2, 3); m.randomize(); print(m)
# print(m.norm(1,1))
# print(m.norm(2,2))
# print(m.norm(math.inf, math.inf))

# --------------------to be done-------------------

# m = Matrix(3, 3)
# for i in range(3):
#     for j in range(3):
#         m[i, j] = (i+1) ** (j+1)
# print(m)
# print(m.solvezero())

# m = Matrix(2, 3)
# for i in range(2):
#     for j in range(3):
#         m[i, j] = (i+1) + (j+1)
# print(m); print(m.solvezero())

# ---------------------------------------------------

# m = Matrix(3, 3)
# for i in range(3):
#     for j in range(3):
#         m[i, j] = (i+1) ** (j+1)
# print(m)

# e,v = m.dominantEigen()
# print(e)
# print(v)

# m = Matrix(4, 4)
# m.randomize()
# m = m + m.t()
# e, v = m.deflate()
# print(e)
# print(v) # v[:,i] is the eigenvector for eigenvalue e[i,0]
# print(np.linalg.eig(m.matrix))

m = Matrix(5, 5)
m[0,0] = 2; m[1,1] = 3; m[2,2] = 2
print(m)
print(m.eigen_vector())
# e, v = m.deflate()
# print(e)
# print(v) # v[:,i] is the eigenvector for eigenvalue e[i,0]
print(np.linalg.eig(m.matrix))

# m = Matrix(4, 4); m.randomize(); m = m + m.t()
# print(m.unshifted_qr())
# print(m.eigen_vector())
# # e, v = m.qreig()
# # print(e)
# # print(v) # v[:,i] is the eigenvector for eigenvalue e[i,0]
# print(np.linalg.eig(m.matrix))

# m = Matrix(3, 4); m.randomize(); u, s, v = m.svd()
# print(u * u.t())
# print(s)
# print(v * v.t())
# print(m)
# print(u * s * v.t())
