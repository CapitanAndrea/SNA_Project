import networkx as nx
import operator


g=nx.barabasi_albert_graph(5717, 16) # n.archi/n.nodi = 16
ung=nx.Graph(g)
print'Barabasi graph loaded!111!'

#base stats
print 'there are '+str(len(g.nodes()))+' nodes'
print 'there are '+str(len(g.edges()))+' edges'

#degree distribution
degree_distribution=sorted(g.degree().values())
degree = open("degree_barabasi","w")
degree_map={}
for i in range(degree_distribution[len(degree_distribution)-1]+1):
	degree_map[i]=0;
for i in range(len(degree_distribution)):
	degree_map[degree_distribution[i]]=degree_map[degree_distribution[i]]+1;
for i in range(degree_distribution[len(degree_distribution)-1]+1):
	degree.write(str(i)+'\t'+str(degree_map[i])+'\n')
degree.close()

#connected components
print 'there are ' + str(nx.number_connected_components(g)) + ' connected components'
connected_components=sorted(nx.connected_components(g))
connected_components=sorted(list(map(lambda x: len(x), nx.connected_components(g))))
print connected_components
connected_components_file= open("connected_components_barabasi","w")
connected_map={}
for i in range(connected_components[len(connected_components)-1]+1):
	connected_map[i]=0;
for i in range(len(connected_components)):
	connected_map[connected_components[i]]=connected_map[connected_components[i]]+1;
for i in range(connected_components[len(connected_components)-1]+1):
	connected_components_file.write(str(i)+'\t'+str(connected_map[i])+'\n')
connected_components_file.close()
print 'there are ' + str(nx.number_connected_components(g)) + ' connected components'

	
#path analysis
print 'the diameter is ' + str(nx.diameter(ung))
print 'the average shortest path is ' + str(nx.average_shortest_path_length(ung))

#clustering coefficient, density analysis
print 'the density is ' + str(nx.density(g))
print 'the average clustering is ' + str(nx.average_clustering(ung))

#centrality analysis
centrality=nx.betweenness_centrality(g, normalized=True)
sorted_centrality=sorted(centrality.items(), key=operator.itemgetter(1))
print 'top betweenness centrality: ' + str(sorted_centrality[len(sorted_centrality)-1])

centrality=nx.closeness_centrality(g, normalized=True)
sorted_centrality=sorted(centrality.items(), key=operator.itemgetter(1))
print 'top closeness centrality: ' + str(sorted_centrality[len(sorted_centrality)-1])






g=nx.erdos_renyi_graph(5717, 0.0028, directed=True) # num.archi/(num.nodi * num.nodi-1) = 0,0028
ung=nx.Graph(g)
print'Random graph loaded!111!'

#base stats
print 'there are '+str(len(g.nodes()))+' nodes'
print 'there are '+str(len(g.edges()))+' edges'

#degree distribution
indegree_distribution=sorted(g.in_degree().values())
outdegree_distribution=sorted(g.out_degree().values())
indegree = open("indegree_random","w")
outdegree = open("outdegree_random","w")
indegree_map={}
outdegree_map={}
for i in range(indegree_distribution[len(indegree_distribution)-1]+1):
	indegree_map[i]=0;
for i in range(outdegree_distribution[len(outdegree_distribution)-1]+1):
	outdegree_map[i]=0;
for i in range(len(indegree_distribution)):
	indegree_map[indegree_distribution[i]]=indegree_map[indegree_distribution[i]]+1;
for i in range(len(outdegree_distribution)):
	outdegree_map[outdegree_distribution[i]]=outdegree_map[outdegree_distribution[i]]+1;
for i in range(indegree_distribution[len(indegree_distribution)-1]+1):
	indegree.write(str(i)+'\t'+str(indegree_map[i])+'\n')
for i in range(outdegree_distribution[len(outdegree_distribution)-1]+1):
	outdegree.write(str(i)+'\t'+str(outdegree_map[i])+'\n')
indegree.close()
outdegree.close()

#connected components
print 'there are ' + str(nx.number_strongly_connected_components(g)) + ' strongly connected components'
#strongly_connected_components=sorted(nx.strongly_connected_components(g))
strongly_connected_components=sorted(list(map(lambda x: len(x), nx.strongly_connected_components(g))))
#print strongly_connected_components
strongly_connected_components_file= open("strongly_connected_components_random","w")
connected_map={}
for i in range(strongly_connected_components[len(strongly_connected_components)-1]+1):
	connected_map[i]=0;
for i in range(len(strongly_connected_components)):
	connected_map[strongly_connected_components[i]]=connected_map[strongly_connected_components[i]]+1;
for i in range(strongly_connected_components[len(strongly_connected_components)-1]+1):
	strongly_connected_components_file.write(str(i)+'\t'+str(connected_map[i])+'\n')
strongly_connected_components_file.close()
print 'there are ' + str(nx.number_weakly_connected_components(g)) + ' weakly connected components'
#for i in nx.weakly_connected_components(g):
#	print str(len(i))
	
#path analysis
print 'the diameter is ' + str(nx.diameter(ung))
print 'the average shortest path is ' + str(nx.average_shortest_path_length(ung))

#clustering coefficient, density analysis
print 'the density is ' + str(nx.density(g))
print 'the average clustering is ' + str(nx.average_clustering(ung))

#centrality analysis
centrality=nx.betweenness_centrality(g, normalized=True)
sorted_centrality=sorted(centrality.items(), key=operator.itemgetter(1))
print 'top betweenness centrality: ' + str(sorted_centrality[len(sorted_centrality)-1])

centrality=nx.closeness_centrality(g, normalized=True)
sorted_centrality=sorted(centrality.items(), key=operator.itemgetter(1))
print 'top closeness centrality: ' + str(sorted_centrality[len(sorted_centrality)-1])

