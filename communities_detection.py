import community
import networkx as nx

g=nx.read_weighted_edgelist('graph6000', create_using=nx.Graph())

#Louvain algorithm
#partition = community.best_partition(g)
#size = float(len(set(partition.values())))
#pos = nx.spring_layout(g)
#count = 0.
#communities_file= open("louvain_communities","w")
#for com in set(partition.values()) :
#	count = count + 1.
#	list_nodes = [nodes for nodes in partition.keys()
#								if partition[nodes] == com]
#	communities_file.write(str(count)+"\t"+str(list_nodes)+"\n")
#communities_file.close()

print 'Louvain finished!'

communities_file=open('kclique_communities', "w")
#k-clique
partition=list(nx.k_clique_communities(g, 3))
for i in range(len(partition)):
	communities_file.write(str(i)+'\t'+str(list(partition[i]))+'\n')
communities_file.close()

print 'kcliques finished!'