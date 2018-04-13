import urllib;
import urllib2;
import pyPdf;
import bing;
import numpy
from BeautifulSoup import BeautifulSoup;
from collections import defaultdict
#import final
import itertools
import math
import aol_search

def viewSource(url):
    
    req = urllib2.Request(url, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language":"en-us,en;q=0.5", "Connection" : "keep-alive", "User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0" });
        
    conn = urllib2.urlopen(req)
    htmlSource = conn.read()
    conn.close();
    return htmlSource;

def cosine_dist(u,v):
    val = (numpy.dot(u,v))/math.sqrt(numpy.dot(u,u))*math.sqrt(numpy.dot(v,v));
    cos = val*180/math.pi
    return cos
#def dotproduct(v1, v2):
  #return sum((a*b) for a, b in zip(v1, v2))

#def length(v):
  #return math.sqrt(dotproduct(v, v))

#def angle(v1, v2):
  #return math.cos(dotproduct(v1, v2) / (length(v1) * length(v2)))


def bingSearch(phrase1, phrase2):
    #words = {"Robotics","Knowledge retrieval","Knowledge reuse","Evolutionary computing and genetic algorithms","Wearable AI"}
    #try:
        #b = bing.Bing("474A701213035B920005D9DC2D28C3405BC4C766");
        searchStr = '"' + phrase1 + '" "' + phrase2 + '"';
        b = bing.Bing('FFBECD58E6B6F9E9E99BB5539D3D095618B26936');
        response = b.search_web(searchStr);
        print response['SearchResponse']['Web'];
        num = response['SearchResponse']['Web']['Total'];
        
        if num == 0:
            #print "The two keyphrases are orthogonal"
            #declare vectors to be orthogonal and return
            return ([1, 0, -1, 0, 0], [1, 0, 1, 0, 0]);
        results = response['SearchResponse']['Web']['Results'];
        print "Results:",results;
        m = len(results);    
        print "N:",m;
        
        #print results;
        top = [];
        
        i = 0;
        
        p1 = [];
        p2 = [];
        while i < 10:
            #print n;
            if i >= m:
                print "!!", i;
                break;
            print "i: ", i;
            phrase1 = phrase1.lower();
            phrase2 = phrase2.lower();
            freq = {phrase1 : 0, phrase2 : 0};

            print results[i];         
            url = results[i]['Url'];
            
            n = len(url);
            if url[n - 4:] == '.pdf':
                urllib.urlretrieve(url, "try.pdf");
        
                f = open("try.pdf", "rb");
                pdf = pyPdf.PdfFileReader(f);
                #f.close();
                
                pages = pdf.getNumPages();
                text = pdf.read(f);
                j = 0;
                
                ind1 = 0;
                ind2 = 0;
                
                while j < pages:
                    try:
                         text = pdf.getPage(j).extractText();
                         
                         temp = text.lower();
                         phrase1 = phrase1.lower();

                         while phrase1 in temp.lower():
                             
                             ind1 = temp.index(phrase1) + len(phrase1);
                             temp = temp[ind1:];
                             freq[phrase1] += 1;
                        
                         temp = text;
                           
                         while phrase2.lower() in temp.lower():
                             ind2 = temp.lower().index(phrase2.lower()) + len(phrase2);
                             temp = temp[ind2:];
                             freq[phrase2] += 1;
                         
                         j = j + 1;
                    except UnicodeEncodeError as err:
                        j = j + 1;
                
                f.close();
               
            else:
                try:
                    print url;
                    htmlSource = viewSource(url);
                    soup = BeautifulSoup(htmlSource);
                    body = soup.find("body");
                    
                    text = body.text;

                    temp = text.lower();
                    phrase1 = phrase1.lower();
                    
                    while phrase1 in temp:
                        ind1 = temp.index(phrase1) + len(phrase1);
                        temp = temp[ind1:];
                        freq[phrase1] += 1;
                        
                    temp = text.lower();
                    phrase2 = phrase2.lower();
                    while phrase2 in temp:
                             ind2 = temp.index(phrase2) + len(phrase2);
                             temp = temp[ind2:];
                             #print temp;
                             freq[phrase2] += 1;

                except Exception as err:
                    pass;
            p1.append(freq[phrase1]);
            p2.append(freq[phrase2]);
            i = i + 1;

        print "Phrase 1: ", p1;
        print "Phrase 2: ", p2;
        
        value = dot(p1,p2);
        val = (float(mag(p1)) * float(mag(p2)));
        
        if val==0:
           val = 0.0000000001; 
        cos = float(value) / val;
            
        #if cos <= 0.4 or cos==0.00:
        if cos <= 0.86 or cos==0.00:    
            print "Dissimilar words"
            return 0;
        else:
            ret = round(cos, 4);
            print ret;
            return ret;
        
def dot(u, v):
    i = 0;
    n = len(u);
    
    dot = 0;
    
    while i < n:
        dot += u[i] * v[i];
        i += 1;
        
    return dot;    

def main():
    
    #"sentiment analysis", "opinion mining"
    list = {"author1": [['Parallel Computations', 'Computations'],['Scalable Storage', 'Storage Systems', 'Systems'],["Local Features", "Creation", "Image Creation"]], "author2": [["Generative Models", "Models"],["Dynamic Capacity", "Server Farms"],["Machine Learning", "Interactive Machine"],["System-Wide Optimization", "Optimization", "Effective Network"],["Graphical Models", "Molecular Dynamics"]]};
    #list2=  {};
    
    #authors = {"Marc","Jack"};
    #combo = zip(authors,keywords);
    #print combo
    mydict = dict(list);
    #print mydict

    #print mydict
    #keywords = {"marc":["Model Checking", "Statistical Model", "Stateflow Simulink Verification", "Stateflow Simulink","Search Tree Restructuring", "Tree Restructuring","Segment","Qualitative Models", "Computing"],"jack":["Dynamic Logic", "Hybrid Systems","Generative Models","Dynamic Capacity", "Server Farms","Machine Learning","Interactive Machine", "Effective Network","Graphical Models"]};
    for i in range(0,2):
        for j in mydict.keys():
            #print j,":",mydict[j][i]
            for item in mydict[j][i]:
                possible_combos= [];
                #print item;
                possible_combos.append(item);
    
    i = 0;
    l1 = mydict["author1"];
    l2 = mydict["author2"];
    m = len(mydict["author1"]);
    n = len(mydict["author2"]);
    while i < m:
        j = 0;   
        while j < n:
            print l1[i][0],"and",l2[j][0];
            bingSearch(l1[i][0], l2[j][0]);

            j = j + 1;       
        i = i + 1;
        
    
    
        
    
def mag(u):
    i = 0;
    n = len(u);
    val = 0;
    while i < n:
        val += (u[i] * u[i]);
        i = i + 1;
        
    val = math.sqrt(val);
    
    return val;        

#bingSearch('Understanding Route', 'Machine Learning');
main();
#main("http://www1.i2r.a-star.edu.sg/~xlli/publication/ECML_PKDD_Li_2007.pdf")
