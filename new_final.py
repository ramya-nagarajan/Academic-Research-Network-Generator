import urllib;
import urllib2;
import pyPdf;
import bing;
import numpy
from BeautifulSoup import BeautifulSoup;
from collections import defaultdict
#import final
import math
def viewSource(url):
    
    req = urllib2.Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language':'en-us,en;q=0.5', 'Connection' : 'keep-alive', 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0' });
        
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
        #b = bing.Bing('474A701213035B920005D9DC2D28C3405BC4C766');
        searchStr = '"' + phrase1 + '" "' + phrase2 + '"';
        b = bing.Bing('FFBECD58E6B6F9E9E99BB5539D3D095618B26936');
        response = b.search_web(searchStr);
        print response['SearchResponse']['Web'];
        num = response['SearchResponse']['Web']['Total'];
        
        if num == 0:
            #print 'The two keyphrases are orthogonal'
            #declare vectors to be orthogonal and return
            return ([1, 0, -1, 0, 0], [1, 0, 1, 0, 0]);
        results = response['SearchResponse']['Web']['Results'];    
        #print results;
        top = [];
        
        i = 0;
        
        #phrases = searchStr.split("+");
        p1 = [];
        p2 = [];
        #http://www.schools.ash.org.au/mcpcompdept/ppts/Robotics.pdf
        while i < 10:
            freq = {phrase1 : 0, phrase2 : 0};            
            url = results[i]['Url'];
            #print url
            n = len(url);
            if url[n - 4:] == '.pdf':
                urllib.urlretrieve(url, "try.pdf");
        
                f = open("try.pdf", "rb");
                pdf = pyPdf.PdfFileReader(f);
                #f.close();
                
                pages = pdf.getNumPages();
                text = pdf.read(f);
                #print text;
                #print pages;
                j = 0;
                #http://virtualastronaut.tietronix.com/teacherportal/pdfs/Humans.and.Robots.pdf
            
                ind1 = 0;
                ind2 = 0;
                
                while j < pages:
                     #find frequency of the phrases in the page
                    try:
                         text = pdf.getPage(j).extractText();
                         #print text
                         temp = text.lower();
                         phrase1 = phrase1.lower();
                         #print "j = ", j
                         while phrase1 in temp.lower():
                             #print ind1;
                             #print text[ind1 : ]
                             #print "hi";
                             #print phrase1 + " " + str(ind1);
                             #print ind1
                             ind1 = temp.index(phrase1) + len(phrase1);
                             temp = temp[ind1:];
                             #print temp;
                             freq[phrase1] += 1;
                             #break;
                         #break;
                        
                         temp = text;
                           
                         while phrase2.lower() in temp.lower():
                             ind2 = temp.lower().index(phrase2.lower()) + len(phrase2);
                             temp = temp[ind2:];
                             #print temp;
                             freq[phrase2] += 1;
                             
                         #k = 0;
                         #for k in range(0,4):
                         #    if words[k] in text:
                         #        freq = freq +1;
                         
                         j = j + 1;
                    except UnicodeEncodeError as err:
                        j = j + 1;
                
                    #text = f.read();
                f.close();
                #print freq;
                    #word_list = text.lower.split(None)
                #j = j + 1;
                #print text
                
                    
                    
                
                #top.append(('pdf', pdf));
                    #print freq
            else:
                try:
                    #continue;
                    print url;
                    htmlSource = viewSource(url);
                    soup = BeautifulSoup(htmlSource);
                    body = soup.find('body');
                    
                    text = body.text;
                    #print htmlSource;
                    #break;
                    temp = text.lower();
                    phrase1 = phrase1.lower();
                    
                    while phrase1 in temp:
                             #print ind1;
                             #print text[ind1 : ]
                             #print "hi";
                             #print phrase1 + " " + str(ind1);
                             #print ind1
                        ind1 = temp.index(phrase1) + len(phrase1);
                        temp = temp[ind1:];
                        #print temp;
                        freq[phrase1] += 1;
                             #break;
                         #break;
                        
                    temp = text.lower();
                    phrase2 = phrase2.lower();
                    while phrase2 in temp:
                             ind2 = temp.index(phrase2) + len(phrase2);
                             temp = temp[ind2:];
                             #print temp;
                             freq[phrase2] += 1;
                    
                    #print body;
                except Exception as err:
                    pass;
                    #print err;
                #find frequencies of phrases in body.text 
            #break;
            if phrase1 not in freq.keys():
            
                print freq;
                p1.append(freq[phrase1]);
                p2.append(freq[phrase2]);
            #print i;
                i = i + 1;
        #num = int(response['SearchResponse']['Web']['Total']);
    
        #return frequency of each phrse in top 5 results --- maybe like a tuple of two lists, each list containing op 5 freq eg: ([2,3,4,5], [2,3,4,5])
        #return num;
    #except Exception as err:
    #    print err; 
        print "Phrase 1: ", p1;
        print "Phrase 2: ", p2;
        
        value = dot(p1,p2);
        cos = float(value) / (float(mag(p1)) * float(mag(p2)));
        #cos = math.cos(value)
        if cos <= 0.4:
            print 'Dissimilar words'
        else:
            print round(cos, 4);
        #return (p1,p2);
    
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
    
    bingSearch("networking","internet");
    
def mag(u):
    i = 0;
    n = len(u);
    val = 0;
    while i < n:
        val += (u[i] * u[i]);
        i = i + 1;
        
    val = math.sqrt(val);
    
    return val;        

main();
#main('http://www1.i2r.a-star.edu.sg/~xlli/publication/ECML_PKDD_Li_2007.pdf')
