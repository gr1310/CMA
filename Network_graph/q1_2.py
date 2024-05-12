from q1 import UndirectedGraph
import random
import numpy as np
import matplotlib.pyplot as plt
import math

class ERRandomGraph(UndirectedGraph):
    def __init__(self, n):
        super().__init__(n)
        # self.nodes= n
    def sample(self, p):
        for i in range(1, self.nodes+1):
            for j in range(i+1,self.nodes+1):
                prob= random.random()
                if(prob<=p):
                    self.addEdge(i,j)
                else:
                    pass
    def isSurelyConnected(self):
        threshold= math.log(self.nodes)/self.nodes
        plt.axvline(x= threshold, color='r', linestyle='-', linewidth=2)
        print(threshold)
        x_axis=list(np.linspace(0,0.1,50))
        y_axis=[]
        for x in x_axis:
            runs=0
            num=0
            frac=0
            while(runs<1000):
                self.remove_all_edge()
                self.sample(x)
                if self.isConnected():
                    num+=1
                runs+=1
                frac+= num/runs
            total_frac= frac/1000
            y_axis.append(total_frac)
        # print(x_axis)
        # print(y_axis)
        plt.plot(x_axis, y_axis)
        plt.show()
    def ERoneTwoComp(self):
        threshold= 0.001
        plt.axvline(x= threshold, color='r', linestyle='-', linewidth=2, label='Largest CC size threshold')
        print(threshold)

        connectedness_threshold = math.log(self.nodes)/self.nodes
        plt.axvline(x= connectedness_threshold, color='y', linestyle='-', linewidth=2, label='Connectedness threshold')
        print(connectedness_threshold)

        x_axis=list(np.linspace(0,0.01,50))
        y_largest=[]
        y_second_largest=[]
        
        for x in x_axis:
            runs=1
            total_largest=0
            frac_largest=0

            total_second_largest=0
            frac_second_largest=0
            while(runs<=50):
                self.remove_all_edge()
                self.sample(x)
                total_largest+=self.oneTwoComponentSizes()[0]
                total_second_largest+=self.oneTwoComponentSizes()[1]
                frac_largest+= (total_largest/runs)
                frac_second_largest+= (total_second_largest/runs)
                runs+=1
            
            y_largest.append(frac_largest/50000)
            y_second_largest.append(frac_second_largest/50000)
        # print(y_largest)
        plt.plot(x_axis,y_largest,color='green', label='Largest connected component',linestyle='-', linewidth=2)
        plt.plot(x_axis,y_second_largest, color='blue', label='2nd largest connected component',linestyle='-', linewidth=2)
        plt.legend()
        plt.show()

        


# g1 = ERRandomGraph(100)
# g1.sample(0.4)
# print(g1.adj_lst)
# g1.plotDegDist()
# print(g1.adj_lst)

# g= ERRandomGraph(1000)
# g.ERoneTwoComp()

g=ERRandomGraph(100)
g.isSurelyConnected()

