import urllib2
import ssl
import time
import json
import Queue

#indent a json string to be more human readable
def beautify(json_string):
	return json.dumps(json.loads(json_string), sort_keys=True, indent=2, separators=(',', ': '))

#send a request to obtain all routes from a given departure airport
def req_flights(iata):
	#wait enough time to get the request accepted
	time.sleep(1.5)
	#send the request
	gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	routes=urllib2.urlopen('https://iatacodes.org/api/v6/routes?departure='+iata+'&api_key=7a6ff549-3dcc-45ad-9c10-37bd07b0b411', context=gcontext).read()
	#store the result in a file
	out_file = open("pages/"+iata,"w")
	out_file.write(beautify(routes))
	out_file.close()
	#return the string itself
	return routes

#parse the route response from the web service, eliminating duplicates
def parse_routes(routes_json):
	flights={}
	edges={}
	#transform the json into a python object
	jdata=json.loads(routes_json)
	response=jdata['response']
	#retrieve all the routes
	for i in range(len(response)):
		flight=response[i]
		if not flights.has_key(flight["flight_number"]):
			flights[flight["flight_number"]]=1
			destination=flight["arrival"]
			count=edges.get(destination, 0)
			edges[destination]=(count+1)
	return edges	

#starting seed is PSA (Pisa international airport)
airports_map={}
airports_map['PSA']=0
airports_queue=Queue.Queue()
airports_queue.put('PSA')
#for each of the airports, find the routes starting from the airport
out_file = open("graph","w")
out_file_id=open("graph_id", "w")
out_file_id.write("# source_id destination_id weight\n")
num=0
#while the queue is not empty
while not airports_queue.full():
	num=num+1
	#get the next airport id, and ask for its routes
	airport_code=airports_queue.get()
	routes=req_flights(airport_code)
	edges=parse_routes(routes)
	#write all the newly found routes
	for j in edges.items():
		out_file.write(airport_code+"\t"+j[0]+"\t"+str(j[1])+"\n")
		#if a new airport is found, assign it a new private id number and put it in the queue
		if not airports_map.has_key(j[0]):
			airports_map[j[0]]=len(airports_map)
			airports_queue.put(j[0])
		out_file_id.write(str(airports_map[airport_code])+"\t"+str(airports_map[j[0]])+"\t"+str(j[1])+"\n")
	print(str(num))
out_file.close()
out_file_id.close()

#also write to file the dictionary with iata code-private id association
out_file = open("pages/airports","w")
out_file.write(str(airports_map))
out_file.close()