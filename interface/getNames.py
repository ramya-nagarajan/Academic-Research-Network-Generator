#!C:/Python27/python.exe
print 'Content-Type:text/plain\n';

from neo4j import GraphDatabase
#import abcd;

#print '<html>'
#print '<head></head><body>'
authors = [];
nodes = [];
pairs = [];
strLst = '';
similar = [];
ids = [];

db = GraphDatabase("D:\\preethi\\data\\graph");
with db.transaction:
	relationships = db.relationships;
	
	i = 0;
	n = len(relationships);
	for rel in relationships:
		if str(rel.type) == 'author_of':
			try:
				if rel.end["key"] == None:
					pass;
                    #break;
			except:
				break;
                
			person = rel.start;
			if person['name'] not in authors:
				nodes.append(person);
				ids.append(person.id);
				#print person.id;
				authors.append(person['name']);
				
	i = 0;
	num = len(nodes);
	
	while i < num:
		rels = nodes[i].relationships.outgoing;
		
		for rel in rels:
			if str(rel.type) == 'similar_to':
				similar.append(rel);
		
		#print similar;
		
		for x in similar:
			#print type(x);
			#print x.end;
			#break;
			if nodes[i]['name'] != x.end['name']:
				lst = [nodes[i]['name'], x.end['name']];
				#print lst;
				revList = [lst[1], lst[0]];
				#print revList;
				#revList.reverse();
				#print lst;
				#print revList;
				#print pairs;
			
				if lst not in pairs and revList not in pairs:
					pairs.append(lst);
		#break;
		i = i + 1;
		
	num = len(pairs);
	#print num;
	i = 0;
	while i < num:

		#if i == num - 1:
		strLst += str(pairs[i]);
		if i != num - 1:
			strLst += '|';
			
		i = i + 1;
		
#print authors;		
print authors, ";" + strLst + ";", ids;

#bothe ends of similar_to are same
#print '</body></html>'
#print 'Preethi,Ramya,Lakshitha,Krupesh,Nandindi,Varsha,Jayant,Suharsha';
#multiple nodes called Pieter Abeel ?
#similar to same person multiple times

#Scale-space and edge detection using anisotropic diffusion
#done till 195 nodes

#pass back id of nodes and relationships