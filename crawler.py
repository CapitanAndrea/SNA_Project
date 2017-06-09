import urllib2
import re
import ssl
import time
import json
import Queue
import os

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
	jdata=json.loads(routes)
	if jdata.has_key('error'):
		time.sleep(60)
		return req_flights(iata)
	#store the result in a file
	out_file = open("pages/"+iata,"w")
	out_file.write(beautify(routes))
	out_file.close()
	#return the string itself
	return jdata

#parse the route response from the web service, eliminating duplicates
def parse_routes(routes_object):
	flights={}
	edges={}
	#transform the json into a python object
	response=routes_object['response']
	#retrieve all the routes
	for i in range(len(response)):
		flight=response[i]
		if not flights.has_key(flight["flight_number"]):
			flights[flight["flight_number"]]=1
			destination=flight["arrival"]
			count=edges.get(destination, 0)
			edges[destination]=(count+1)
	return edges	

def req_page(page_name):
	#wait enough time to get the request accepted
	time.sleep(1)
	#send the request
	
	#gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

	#error for # in page_name -- example: John_Henry_Patterson_(NCR_owner)#Pioneering_business_practices		
	if page_name.find('#') != -1 : 
		page_name=page_name.replace('#','&')

	page_utf=page_name.encode('utf-8', 'replace')
	print page_utf
	
	page=urllib2.urlopen('https://en.wikipedia.org/w/api.php?action=query&titles='+page_utf+'&prop=revisions&rvprop=content&format=json').read()
	#page=urllib2.urlopen('https://en.wikipedia.org/w/api.php?action=query&titles='+page_utf+'&prop=revisions&rvprop=content&format=json', context=gcontext).read()
	
	jdata=json.loads(page)
	
	try:
		response=jdata['query']['pages']
	except BaseException as e:
		#ignore unparsable pages
		return {}

	page_id=response.keys()[0]
	
	#page content not exist	
	if response[page_id].has_key('missing'): return {}	
	
	#page content exist	
	page_content=response[page_id]['revisions'][0]['*']
	#redirect case	
	if page_content.startswith('#'):
		regex = ur"\[\[(.+?)\]\]+?"
		page_id = re.findall(regex, page_content)[0]
		#redirect returns the value equals to page_utf
		if page_id.replace(' ', '_') == page_utf: return {}
		return req_page(page_id.replace(' ', '_'))
	
	#store the result in a file

	#check if page_name contains / => searched directory
	if page_name.find('/')!=-1:
		page_name=page_name.replace('/','_')

	out_file = open("pages/"+page_name,"w")
	out_file.write(beautify(page))
	out_file.close()
	#return the string itself
	return jdata

def parse_page(page_object):
	flights={}
	edges={}
	#transform the json into a python object
	response=page_object['query']['pages']
	page_id=response.keys()[0]
	page_content=response[page_id]['revisions'][0]['*']
	#find string into [[ ]]	
	regex = ur"\[\[(.+?)\]\]+?"
	linked_pages = re.findall(regex, page_content)

	#retrieve all the pages
	for i in range(len(linked_pages)):
		linked_page=linked_pages[i]
		if not linked_page.find('|')==-1:
			linked_page=linked_page.split('|')[0]
		linked_page=linked_page.replace(' ', '_')
		count=edges.get(linked_page, 0)
		edges[linked_page]=(count+1)
	return edges

#create new directory
if not os.path.exists('pages'):
    os.makedirs('pages')

page_map={}
page_map['barabasi']=0
page_queue=Queue.Queue()
page_queue.put('barabasi')

out_file = open("graph","w")
out_file_id=open("graph_id", "w")
out_file_id.write("# source_id destination_id weight\n")
num=0

#while the queue is not empty
while not page_queue.empty():
	num=num+1
	page_name=page_queue.get()
	#request page	
	page_obj=req_page(page_name)
	if(page_obj=={}): continue
	edges=parse_page(page_obj)
	#write all the newly found edges
	for j in edges.items():
		out_file.write(page_name.encode('ascii', 'replace')+"\t"+j[0].encode('ascii', 'replace')+"\t"+str(j[1])+"\n")
		#if a new page is found, assign it a new private id number and put it in the queue
		if not page_map.has_key(j[0]):
			page_map[j[0]]=len(page_map)
			page_queue.put(j[0])
		out_file_id.write(str(page_map[page_name])+"\t"+str(page_map[j[0]])+"\t"+str(j[1])+"\n")
	print(str(num))
	if num>5000: break
out_file.close()
out_file_id.close()

#also write to file the dictionary
out_file = open("pages/pages","w")
out_file.write(str(page_map))
out_file.close()
