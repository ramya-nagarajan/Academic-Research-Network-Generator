#!C:/Python27/python.exe
print 'Content-Type:text/plain\n';

from neo4j import GraphDatabase
#import abcd;

#print '<html>'
#print '<head></head><body>'
authors = [];

db = GraphDatabase("D:\\preethi\\data\\graph");
with db.transaction:
	relationships = db.relationships;
	

	i = 0;
	n = len(relationships);
	for rel in relationships:
		start = rel.start;
		if start["name"] not in authors:
			authors.append(start["name"]);
		
print authors;

#print '</body></html>'
#print 'Preethi,Ramya,Lakshitha,Krupesh,Nandindi,Varsha,Jayant,Suharsha';

#Scale-space and edge detection using anisotropic diffusion
#done till 195 nodes