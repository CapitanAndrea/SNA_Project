import networkx as nx
import sys

damping=0.85
if len(sys.argv)>1:
	damping=float(sys.argv[1])
g=nx.read_edgelist('graph_translated', create_using=nx.DiGraph())

pr=nx.pagerank(g, damping)

out_file = open('pagerank_'+str(damping),'w')
l=pr.items()
l.sort(key=lambda tup: tup[1], reverse=True)
for i in l:
	out_file.write(str(i)+'\n')
out_file.close()