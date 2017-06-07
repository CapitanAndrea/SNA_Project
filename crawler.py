import urllib2
import ssl
import time
import json

def req_flights(iata):
	time.sleep(1.5)
	gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	routes=urllib2.urlopen('https://iatacodes.org/api/v6/routes?departure='+iata+'&api_key=7a6ff549-3dcc-45ad-9c10-37bd07b0b411', context=gcontext).read()
	out_file = open("pages/"+iata,"w")
	out_file.write(json.dumps(routes, sort_keys=True, indent=2, separators=(',', ': ')))
	out_file.close()
	return routes

def parse_airports(airports_json):
	airports_array=[]
	jdata=json.loads(airports_json)
	response=jdata['response']
	for i in range(0, 10050):
		airports_array.append(response[i]['code'])
	return airports_array

gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
airports=urllib2.urlopen('https://iatacodes.org/api/v6/airports?api_key=7a6ff549-3dcc-45ad-9c10-37bd07b0b411', context=gcontext).read()
out_file = open("pages/airports","w")
#print json.dumps(airports, indent=2, separators=(',', ': '))
out_file.write(json.dumps(airports, sort_keys=True, indent=2, separators=(',', ': ')))
out_file.close()
airports_array=parse_airports(airports)
for i in range(0, 10050):
	print(airports_array[i])