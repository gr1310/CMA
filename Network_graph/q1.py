import matplotlib.pyplot as plt

class UndirectedGraph:
    def __init__(self, nodes=0):
        self.adj_lst=dict()
        self.edges=0
        self.initial_nodes= nodes
        
        if(nodes):
            for i in range(nodes):
                self.adj_lst[i+1]=[]
        self.nodes= len(self.adj_lst)

    def addNode(self, node):
        if(node not in self.adj_lst and node>self.initial_nodes and self.initial_nodes!=0):
            raise Exception("Node index cannot exceed number of nodes")
        elif(node not in self.adj_lst):
            self.adj_lst[node]=[]
        self.nodes= len(self.adj_lst)
    
    def addEdge(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        if node2 not in self.adj_lst[node1]:
            self.adj_lst[node1].append(node2)
        if node1 not in self.adj_lst[node2]:
            self.adj_lst[node2].append(node1)
        self.edges+=1
    
    def remove_all_edge(self):
        for i in self.adj_lst:
            self.adj_lst[i].clear()

    # operator overloading
    def __add__(self, temp):
        
        if(type(temp)==int):
            self.addNode(temp)
            return self
        elif(type(temp)==tuple):
            self.addEdge(temp[0],temp[1])
            return self
        
    # printing graph
    def __str__(self):
        string= f"Graph with {len(self.adj_lst)} nodes and {self.edges} edges. Neighburs of nodes are below:\n "
        neighbours= ""
        
        for x in self.adj_lst:
            values=""
            for i in self.adj_lst[x]:
                values+= str(i)+","
            values= values[:-1]
            txt= f"Node {x} : {{{values}}} \n"
            neighbours+=txt
        string+= neighbours
        return string
    
    def bfs(self, i, vis, queue, sz):
        temp=0
        if(i and (i not in vis)):
            vis.append(i)
            queue.append(i)
            while(len(queue)>0):
                # print([i for i in queue])
                i_node= queue.pop(0)
                if(i_node): temp+=1
                # print(i_node)
                for j in self.adj_lst[i_node]:
                    if(j and (j not in vis)):
                        queue.append(j)
                        vis.append(j)
                    else:
                        pass
                # print(len(queue))
            sz.append(temp)

    def isConnected(self):
        vis=[]
        queue=[]
        sz=[]
        for i in self.adj_lst:
            if(i not in vis):
                self.bfs(i,vis, queue,sz)
                break
        for i in self.adj_lst:
            if(i not in vis):
                return False
            
        return True
    
    def oneTwoComponentSizes(self):
        vis=[]
        queue=[]
        comp_size=[]
        for i in self.adj_lst:
            # print(i)
            if(i not in vis):
                self.bfs(i,vis, queue,comp_size)
                # for x in vis:
                    # print(x, end=" ")
        comp_size=sorted(comp_size)
        if(len(comp_size)==1):
            comp_size.append(0)
            return comp_size
        return [comp_size[-1], comp_size[-2]]

    def plotDegDist(self):
        node_degree=[i for i in range(len(self.adj_lst))]
        degree_freedom=[0]*(len(node_degree))

        for x in self.adj_lst:
            degree_freedom[len(self.adj_lst[x])]+=1
        print(node_degree)
        print(degree_freedom)
        
        sum=0
        for i in range(len(degree_freedom)):
            sum+= i*degree_freedom[i]
        average= sum/ len(self.adj_lst)

        degree_freedom= [i/len(self.adj_lst) for i in degree_freedom]
        plt.axvline(x= average, color='r', linestyle='-', linewidth=2)
        plt.scatter(node_degree,degree_freedom)
        plt.xlabel("Node Degree")
        plt.ylabel("Fraction of nodes")
        plt.grid()
        plt.show()



# g = UndirectedGraph()
# g.addNode(1)
# g.addNode(11)
# g.addEdge(10, 25)
# print(g.adj_lst)
# g=g+30
# print(g.adj_lst)
# g = g + (12, 15)
# print(g.adj_lst)
# print(g)

# g = UndirectedGraph(5)
# g = g + (1, 2)
# g = g + (3, 4)
# g = g + (1, 4)
# print(g)
# g.plotDegDist()
        
# g = UndirectedGraph()
# g = g + 100
# g = g + (1, 2)
# g = g + (1, 100)
# g = g + (100, 3)
# print(g.nodes)
# g = g + 20
# g.plotDegDist()
        
# g = UndirectedGraph(5)
# g = g + (1, 2)
# g = g + (2, 3)
# g = g + (3, 4)
# g = g + (3, 5)
# print(g.adj_lst)
# print(g.isConnected())
        
# g = UndirectedGraph(5)
# g = g + (1, 2)
# g = g + (2, 3)
# g = g + (3, 5)
# print(g.isConnected())
# print(g.adj_lst)

# g = UndirectedGraph(6)
# g = g + (1, 2)
# g = g + (3, 4)
# g = g + (6, 4)
# print(g.oneTwoComponentSizes())
