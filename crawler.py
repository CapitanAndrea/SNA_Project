import urllib2
import ssl
import time
import json

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
		if flights.has_key(flight["flight_number"]):
			continue
		else:
			flights[flight["flight_number"]]=1
			destination=flight["arrival"]
			count=edges.get(destination, 0)
			edges[destination]=(count+1)
	return edges	

#parse the airport response from the web service
def parse_airports(airports_json):
	airports_array={}
	#transform the json into a python object
	jdata=json.loads(airports_json)
	response=jdata['response']
	#retrieve all the iata codes of the airports
	for i in range(10051):
		airports_array[response[i]['code']]=i
	return airports_array

#request info of all the available airports
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
airports=urllib2.urlopen('https://iatacodes.org/api/v6/airports?api_key=7a6ff549-3dcc-45ad-9c10-37bd07b0b411', context=gcontext).read()
#store the json in a file
out_file = open("pages/airports","w")
out_file.write(beautify(airports))
out_file.close()
#retrieve all the airports iata codes
airports_array=parse_airports(airports)
"""
for i in range(10053):
	print(airports_array[i])
"""
#for each of the airports, find the routes starting from the airport
out_file = open("graph","w")
out_file_id=open("graph_id", "w")
for airport_code in airports_array.keys():
	#routes=req_flights(airport_code)
	routes=req_flights("MLC")
	edges=parse_routes(routes)
	for j in edges.items():
		out_file.write(airport_code+"\t"+j[0]+"\t"+str(j[1])+"\n")
		out_file_id.write(str(airports_array[airport_code])+"\t"+str(airports_array[j[0]])+"\t"+str(j[1])+"\n")
		
	break
	
out_file.close()
out_file_id.close()