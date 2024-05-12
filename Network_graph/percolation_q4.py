import networkx as nx 
import matplotlib.pyplot as plt
import random
import numpy as np

class Lattice:
    def __init__(self,n):
        self.dim= n
        self.graph= nx.Graph()
        self.dir= [-1,1]
        self.allPaths=[]
        for i in range(self.dim):
            for j in range(self.dim):
                self.graph.add_node((i,j))
    
    def show(self):
        """Plotting the graph created"""

        # assigning colors
        edges= self.graph.edges()
        colors = [self.graph[u][v]['color'] for u,v in edges]
        weights = [self.graph[u][v]['weight'] for u,v in edges]

        # positions of nodes
        pos = {(x,y):(y,-x) for x,y in self.graph.nodes()}

        # plotting
        plt.figure(figsize=(6,6))
        nx.draw(self.graph, pos=pos,edge_color=colors,width= weights, node_size= 1)
        plt.show()
    

    def percolate(self, prob):
        """Function to perform perculation"""

        for i in range(self.dim):
            for j in range(self.dim):
                if(random.random()<=prob):
                    # boundary conditions
                    if(i==0):
                        self.graph.add_edge((i,j),(i + 1, j), color='r', weight=1)
                    elif(i==self.dim-1):
                        self.graph.add_edge((i,j),(i - 1, j), color='r', weight=1)

                    # random addition of edge either up or down
                    else:
                        self.graph.add_edge((i,j),(i + random.choice(self.dir), j), color='r', weight=1)

        for i in range(self.dim):
            for j in range(self.dim):
                if(random.random()<=prob):

                    # boundary conditions
                    if(j==0 ):
                        if(not self.graph.has_edge((i,j),(i , j+1))): 
                            self.graph.add_edge((i,j),(i , j+1), color='r', weight=1)
                    elif (j==self.dim-1):
                        if(not self.graph.has_edge((i,j),(i , j-1))): 
                            self.graph.add_edge((i,j), (i, j - 1), color='r', weight=1)

                    #  random addition of edge either right or left
                    else:
                        val=random.choice(self.dir)
                        if(not self.graph.has_edge((i,j),(i , j+val))):
                            self.graph.add_edge((i,j),(i , j+val), color='r', weight=1)


    def existsTopDownPath(self):
        """If there exists a path from top layer nodes to the bottom layer nodes"""

        top_layer=[]
        bottom_layer=[]
        for i in range(self.dim):
            top_layer.append((0,i))
            bottom_layer.append((self.dim-1,i))
        
        for top in top_layer:
            for bottom in bottom_layer:
                if(nx.has_path(self.graph,top, bottom)):
                    return True
        return False
    

    def showPaths(self):
        top_layer=[]
        bottom_layer=[]
        for i in range(self.dim):
            top_layer.append((0,i))
            bottom_layer.append((self.dim-1,i))

        top_vis=[]
        for top in top_layer:
            top_paths=[]
            for bottom in bottom_layer:
                if(nx.has_path(self.graph,top, bottom)):
                    # Find shortest weighted paths and lengths from a source node to a target node
                    paths= nx.single_source_dijkstra(self.graph, top, bottom)
                    top_paths.append(paths)
            if(len(top_paths)):
                self.allPaths.append(sorted(top_paths)[0])
                top_vis.append(top)
                    
        for top in top_layer:
            if(top in top_vis):
                for paths in self.allPaths:
                    for t in range(1,len(paths[1])):
                        self.graph.add_edge(paths[1][t-1], paths[1][t], color='b', weight= 2)
                self.allPaths=[]
            else:
                diff_paths=[]
                prev=top
                # print(top)
                for i in range(top[0],self.dim):
                    for j in range(top[1],self.dim):
                        bottom=(i,j)
                        # print(nx.has_path(self.graph,top, bottom))
                        if(not nx.has_path(self.graph,top, bottom)):
                            diff_paths.append(nx.single_source_dijkstra(self.graph, top, prev))
                            break
                        prev=bottom
                for i in diff_paths:
                    for t in range(1,len(i[1])):
                        self.graph.add_edge(i[1][t-1],i[1][t], color='b',weight= 2)
            


def path_exists():
        x_axis= list(np.linspace(0,1,50))
        y_axis=[]
        runs=50
        for p in x_axis:
            num=0
            for i in range(1,runs+1):
                l= Lattice(25)
                l.percolate(p)
                if l.existsTopDownPath():
                    num+=1
            frac= num/runs
            y_axis.append(frac)
        plt.plot(x_axis,y_axis)
        plt.show()



    

        

l = Lattice(100)
print(l.graph)
# l.show()
l.percolate(0.7)
print(l.existsTopDownPath())
l.showPaths()
l.show()
        
# path_exists()


