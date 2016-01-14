import networkx as nx 
import re

G=nx.Graph() 
for i in range(0, 14): 
    file = open('part-000%02d' % i, 'r') 
    for line in file: 
        line = line.strip() 
        if len(line) > 0: 
            node1, node2, weight = re.split('\|', line)
            G.add_edge(node1, node2, weight=int(weight))
file.close()
nx.write_gexf(G, 'graph.gexf')
