pajek_file=open('graph.net', "w")
pajek_file.write('*Vertices  5717\n')

with open('pages_translated', 'r') as f:
    for line in f:
		parts=line.split(' : ')
		pajek_file.write(str(parts[0]) + ' \"'+str(parts[1]).split('\n')[0]+'\"\n')
	
pajek_file.write('*Edges\n')
with open('graph_translated', 'r') as f:
    for line in f:
		pajek_file.write(str(line))
pajek_file.close()

