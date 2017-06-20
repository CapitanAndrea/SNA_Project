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
			translation_map[line.split(' : ')[0]]=(i, line.split(' : ')[1].split('\n')[0])
			i=i+1
			
out_file=open('pages_translated', 'w')
for entry in translation_map.items():
	out_file.write(str(entry[1][0])+' : '+str(entry[1][1])+'\n')
out_file.close()
out_file=open('graph_translated', 'w')
with open('graph_refined', 'r') as f:
    for line in f:
		parts=line.split('\t')
		id_s=translation_map[parts[0]][0]
		id_d=translation_map[parts[1].split('\n')[0]][0]
		out_file.write(str(id_s)+'\t'+str(id_d)+'\n')
out_file.close()