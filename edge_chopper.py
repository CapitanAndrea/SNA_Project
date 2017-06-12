in_file = open("graph_id","r")
out_file=open('graph6000', 'w')
while True:
	line=in_file.readline()
	if line.startswith('#'): continue
	if line=='': break
	parts=line.split('\t')
	#print str(len(parts)) + '\t' + line
	if int(parts[1])<6001:
		out_file.write(parts[0] + '\t' + parts[1] + '\n')
in_file.close()
out_file.close()