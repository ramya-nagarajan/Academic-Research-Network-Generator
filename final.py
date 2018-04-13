import pdfreader
from BeautifulSoup import BeautifulSoup
import google_search
import numpy
import nltk.stem.lancaster;
#import lsa
import semantic_comp
import bing_search
import urllib
from urllib2 import HTTPError
import sys
import urllib2

def bingKeyphrases(): 
    
    for i in semantic_comp.a:
        j = 1;
        k=1;
        for j in range(k,5):
            if semantic_comp.a[j] and k != j:
                srchStr = i+"+"+semantic_comp.a[j];
                print srchStr
                
                res = str(bing_search.search(srchStr));
                print res
                print "\n"
            
def findpdfs(url):
        try:
            
            url = "https://www.google.co.in/search?rlz=1C1CHMZ_enIN461IN461&ix=sea&sourceid=chrome&ie=UTF-8&q=AI+pdf"
            
            pdfreader.getpdfcontent(path);
            #print urllib.urlretrieve(path, "D:\\projectwork\\Project_8thsem")
            #req = mechanize.Request(url);
            #res = mechanize.urlopen(req);
            #print res.read();
            #localFile = open(url.split('/')[-1], 'w')
            
            #print webFile.read();
            
            #localFile.write(webFile.read())
            #print localFile.name
            #webFile.close()
            #print 'hi'
            #localFile.close()
            #pdfreader.getpdfcontent('D:\projectwork\Project_8thsem\svd.pdf');
           # sock = urllib.urlopen(url)
            #htmlSource = sock.read()
            #sock.close();
            #soup= BeautifulSoup(htmlSource);
            
            
            #embed = soup.findAll('embed');
            
            #print embed;
            
            #print embed[0].get("src");
            
            #print htmlSource
            #return localFile
        
        except Exception as err:
            print err
            

def cosine_dist(u,v):
    return (numpy.dot(u,v))/math.sqrt(numpy.dot(u,u))*math.sqrt(numpy.dot(v,v));

bingKeyphrases();
#findpdfs('D:\projectwork\Project_8thsem\svd.pdf');
    