import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
class DirectedGraph():
    def __init__(self,nodes):
        self.adj_lst= dict()
        self.initial_nodes=nodes
        self.edges=0
        if(nodes):
            for i in range(nodes):
                self.adj_lst[i]=[]
        self.nodes= len(self.adj_lst)
    
    def addNode(self, node):
        if(node not in self.adj_lst and node>self.initial_nodes and self.initial_nodes!=0):
            raise Exception("Out of range")
        elif (node not in self.adj_lst):
            self.adj_lst[node]=[]
    
    def addEdge(self, source, sink):
        self.addNode(source)
        self.addNode(sink)

        if(source not in self.adj_lst[sink]):
            # self.adj_lst[sink].append(source)
            self.adj_lst[source].append(sink)
        self.edges+=1

    def incomingEdges(self,node):
        return len(self.adj_lst[node])
    
    def outgoingEdges(self,node):
        count=0
        for i in self.adj_lst:
            # print(self.adj_lst[i])
            if(node in self.adj_lst[i]):
                count+=1
        print(count)
        return count

    def pageRank(self, d):
        n= len(self.adj_lst)
        transition_matrix= np.zeros((n,n))
        for i in range(n):
            outgoing_links= len(self.adj_lst[i])
            if(outgoing_links==0):
                transition_matrix[:,i]= 1/n

            for j in range(n):
                if j in self.adj_lst[i]:
                    transition_matrix[j,i]=  d*(1/outgoing_links)

        e,v = np.linalg.eig(transition_matrix)
        max_e= np.argmax(e)
        pagerank= np.abs(v[:,max_e])
        pagerank/= np.sum(pagerank)
        # print(self.adj_lst.items())
        print(pagerank)

        G= nx.DiGraph()

        for node in self.adj_lst:
            G.add_node(node, size=pagerank[node-1]*1000)

        for s,d in self.adj_lst.items():
            for i in d:
                G.add_edge(s,i)

        node_size= [G.nodes[node]['size'] for node in G.nodes()]

        nx.draw(G, with_labels=True)
        plt.show()
        



p = 0.05; n = 25
g = DirectedGraph(n)
for i in range(n):
    for j in range(n):
        if i != j and random.random() <= p:
            g.addEdge(i+1, j+1)
# print(g.adj_lst)
# g.outgoingEdges(4)
# g.pagerank(0.85) #
g.pageRank(0.85)