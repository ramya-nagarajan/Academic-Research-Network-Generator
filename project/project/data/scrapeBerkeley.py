'''
Created on 21-Feb-2012

@author: Prudent
'''
from BeautifulSoup import BeautifulSoup
import urllib
from neo4j import GraphDatabase

def viewSource(url):
    
        sock = urllib.urlopen(url);
        htmlSource = sock.read();
        sock.close();
        return htmlSource;
    
def scrape(url):
    global db;
    
    base = 'http://www.eecs.berkeley.edu';
    
    main = viewSource(url);
    soup = BeautifulSoup(main);
    faculty = soup.findAll('h2', {'class' : 'top'})[1];
    
    members = faculty.findNextSibling('ul');
    
    memberList = members.findChildren('li');
    
    research = {};
    authors = [];
    
    for i in range(0, len(memberList)):
        try:
            member = memberList[i].findChild('a');
            name = member.text;
            home = base + member.attrs[0][1];
            
            homeSource = viewSource(home);
            
            soup = BeautifulSoup(homeSource);
            
            h3 = soup.findAll('h3');
            
            j = len(h3) - 1;
            
            #for j in range(len(h3) - 1, 0):
            while j >= 0:
                #print j;
                if(h3[j].text == 'Selected Publications'):
                    break;
                
                j -=1;
            
            #print j;
            
            if j < 0:
                continue;
            
            #print h3[j];    
            pubs = h3[j].findNextSibling('ul');
            
            pubList = pubs.findChildren('li');
            
            pubMeta = [];
            
            pubs = [];
            
            for j in range(0, len(pubList)):
                #try:
                    #print pubList[j].text;
                    authors = pubList[j].text.split('"')[0].split(",");
                    #print authors;
                    linkToPub = pubList[j].findChild("a");
                    
                    #print linkToPub;
                    
                    if linkToPub != None:
                        title = linkToPub.text;
                    else:
                        #if '"' in pubList[j]:
                        #print "here";
                        try:
                            title = pubList[j].text.split('"')[1].split('"')[0].split(",")[0];
                        except Exception:
                            title = '';
                        #else:
                        #    title = pubList[j].text.split(",")[1];
                    
                    #print title
                    #print linkToPub;
                    #
                    if pubList[j].findChild("em") != None:
                        comm = pubList[j].findChild("em").text;
                    else:
                        comm = '';
                    #break;
                    
                    paperDict = {"authors" : authors, "title" : title, "comm" : comm};
                    pubMeta.append(paperDict);
                    
                    with db.transaction:
                        #print title;
                        if title != '':
                            node = db.node(title=title, conference=comm);
                            #print node.id;
                    
                    pubs.append(node);
                    
                #except Exception as err:
                #    print err;
                
            
                
            research[name] = pubMeta;
            
            with db.transaction:
                node = db.node(name=name, link=home);
                print node.id;
                #print node;
                
                k = 0;
                n = len(pubs);
                
                #print n;
                
                while k < n:
                    #print k;
                    rel = node.author_of(pubs[k]);
                    k += 1;
                
            #print "Here";
            authors.append(node);
            print authors;
            
            print research;
            
            #break;
        except Exception:
            pass;
    
    print "Authors: ", authors;
    
def main():
    global db;
    
    db = GraphDatabase("D:\\preethi\\data\\graph");
    
    #result = db.query("START n=node({'name': 'Pieter Abbeel'}) RETURN n")
 
    #print result;
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/AI/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/BIO/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/COMNET/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/ARC/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/CIR/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/DBMS/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/DES/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/EDUC/'); #--- prob -- list index out of range
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/ENE/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/GR/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/HCI/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/INC/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/MEMS/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/OSNT/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/PHY/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/PS/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/SCI/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/SEC/'); # -- john d. Kubiatowicz splitting on ',' prob as it mite b in title
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/SP/');
    #scrape('http://www.eecs.berkeley.edu/Research/Areas/THY/'); # --- prob -- list index out of range
    
    
    
    db.shutdown();

main();
