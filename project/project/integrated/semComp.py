from neo4j import GraphDatabase;

def getAuthors(name): #for generating pairs(name is None)  or finding people compatible with name
    db = GraphDatabase("D:\\projectwork\\graph");
    relationships = db.relationships;
    
    authors = [];
    
    if name != None:
        name = name.lower();
    
        for rel in relationships:
            if str(rel.type) == 'author_of':
                person = rel.start;
                
                if person['name'].lower() != name:
                    authors.append(person);
    else:
        for rel in relationships:
            if str(rel.type) == 'author_of':
                person = rel.start;
                
                authors.append(person);
                
    
    return authors;

def buildKey(a1, a2): #build a dictionary consisting the two authors' keyphrases
    papers1 = a1.author_of.outgoing;
    key1 = [];
    for paper in papers1:
        key1.append(paper["key"]);
        
    papers2 = a2.author_of.outgoing;
    key2 = [];
    for paper in papers2:
        key2.append(paper["key"]);  
        
    return {a1["name"] : key1, a2["name"] : key2};