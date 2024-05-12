import numpy as np
class RowVectorFloat:
    def __init__ (self, lst):
        # self.row_vector= np.array(lst)
        self.row_vector=lst

    def __str__(self) -> str:
        # print(self.row_vector)
        output=""
        for i in self.row_vector:
            output=output+str(i)+" "
        return output
    
    def __len__(self):
        return len(self.row_vector)
    
    def __getitem__(self, index):
            return self.row_vector[index]
    def __setitem__(self,key, value):
            self.row_vector[key]=value

    def __rmul__(self, num):
        result=[]
        if((type(num)==int or type(num)==float) and type(self)==RowVectorFloat):
            for i in range(len(self.row_vector)):
                result.append(self.row_vector[i]*num)
            return RowVectorFloat(result)
        else:
            raise Exception("Invalid multiplication")
    
    def __add__(self, a):
        result=[]
        for i in range(len(self.row_vector)):
            result.append(self.row_vector[i]+a.row_vector[i])
        return RowVectorFloat(result)
    
    def __sub__(self, a):
        result=[]
        for i in range(len(self.row_vector)):
            result.append(self.row_vector[i]-a.row_vector[i])
        return RowVectorFloat(result)
    
    
# r = RowVectorFloat([1, 2, 4])
# print(r)
# print(len(r))
# print(r[1])
# r[2] = 5
# print(r)
        
# r1 = RowVectorFloat([1, 2 , 4])
# r2 = RowVectorFloat([1, 1 , 1])

# r3 = 2*r1 + (-3)*r2
# print(r3)


# r = RowVectorFloat([])
# print(len(r))