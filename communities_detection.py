import community
import networkx as nx
import Demon as d
import sys
from subprocess import call

"""
args:
	bool - compute louvain community detection
	bool - compute DEMON community detection
	float - custom epsilon for DEMON
	bool - compute Infohiermap community detection
	int - number of tries for IHM
	
"""

g=nx.read_weighted_edgelist('graph_translated', create_using=nx.Graph())

#Louvain algorithm
if int(sys.argv[1])==1:
	partition = community.best_partition(g)
	size = float(len(set(partition.values())))
	pos = nx.spring_layout(g)
	count = 0.
	communities_file= open("louvain_communities","w")
	for com in set(partition.values()) :
		count = count + 1.
		list_nodes = [nodes for nodes in partition.keys()
									if partition[nodes] == com]
		communities_file.write(str(count)+"\t"+str(list_nodes)+"\n")
	communities_file.close()

	print 'Louvain finished!'

#DEMON
if int(sys.argv[2])==1:
	e=float(sys.argv[3])
	dm=d.Demon('graph_translated', epsilon=e, min_community_size=3, file_output=True)
	dm.execute()
	
	print 'DEMON finished'
	
#Infohiermap
if int(sys.argv[4])==1:
	tries=int(sys.argv[5])
	call(['./infohiermap_undir/infohiermap', '42', 'graph_hier.net', str(tries)])
	
	print 'Infohiermap finished'
"""
communities_file=open('kclique_communities', "w")
#k-clique
partition=list(nx.k_clique_communities(g, 3))
for i in range(len(partition)):
	communities_file.write(str(i)+'\t'+str(list(partition[i]))+'\n')
communities_file.close()

print 'kcliques finished!'
"""