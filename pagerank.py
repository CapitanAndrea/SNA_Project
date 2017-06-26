import networkx as nx
import sys

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

damping=0.85
if len(sys.argv)>1:
	damping=float(sys.argv[1])
g=nx.read_edgelist('graph_translated', create_using=nx.DiGraph())

pr=nx.pagerank(g, damping)

out_file = open('pagerank_'+str(damping),'w')
l=pr.items()
l.sort(key=lambda tup: int(tup[0]), reverse=True)
for i in l:
	#out_file.write(str(i[0])+'\t'+str(i[1])+'\n')
	out_file.write(str(truncate(i[1]), 7)+'\n')
out_file.close()

pr_map={}

for i in l:
	key=truncate(i[1], 5)
	if pr_map.has_key(key):
		pr_map[key]=pr_map[key]+1
	else:
		pr_map[key]=1
l=pr_map.items()
l.sort(key=lambda tup: tup[0])
out_file = open('pagerank_distribution_'+str(damping),'w')
for i in l:
	out_file.write(str(i[0])+'\t'+str(i[1])+'\n')
out_file.close()