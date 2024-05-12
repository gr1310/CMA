def handleException(method):
    def decorator(ref, *args, **kwargs):
        try:
            method(ref, *args, **kwargs)
        except Exception as err:
            print(type(err))
            print(err)
        return decorator

import networkx as nx
import matplotlib.pyplot as plt
G= nx.Graph()
for i in range(5):
    for j in range(5):
        G.add_node((i,j))
print(G.nodes())
G.add_edge((1,2),(3,2),color='red')

edge_colors=[G[u][v]['color'] for u,v in G.edges()]
pos={(x,y):(-y,x) for x,y in G.nodes()}

plt.figure()
nx.draw(G, pos=pos, node_size=1,edge_color=edge_colors)
plt.show()