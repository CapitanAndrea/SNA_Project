nodes_map={}
translation_map={}

with open('graph_refined', 'r') as f:
    for line in f:
		parts=line.split('\t')
		nodes_map[parts[0]]=1;
		nodes_map[parts[1].split('\n')[0]]=1;

i=1
with open('pages', 'r') as f:
    for line in f:
		if nodes_map.has_key(line.split(' : ')[0]):
			translation_map[line.split(' : ')[0]]=(i, line.split(' : ')[1].strip())
			i=i+1
			
out_file=open('idlist', 'w')
l=translation_map.items()
l.sort(key=lambda tup: int(tup[1][0]), reverse=True)
for entry in l:
	out_file.write(str(entry[1][1])+'\n')
out_file.close()