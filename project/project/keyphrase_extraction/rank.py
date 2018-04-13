import web;
import urllib2;
import urllib;
from BeautifulSoup import BeautifulSoup;
import math;
import sys;
import httplib;
import json;
from yahoo.search.factory import create_search;
import fileHandle;
import re;


def openURL(url):
    
        req = urllib2.Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language':'en-us,en;q=0.5', 'Connection' : 'keep-alive', 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0', 'Host' : 'search.aol.com' });
        
        conn = urllib2.urlopen(req)
        htmlSource = conn.read()
        conn.close();
        return (conn.headers.getheader("Set-Cookie"), htmlSource);


def scrape(source):
    soup = BeautifulSoup(source);
    table = soup.findAll('table', {"class" : "small-text", "align" : "left", "border" : "0", "width" : "100%"});
    
    i = 0;
    count = len(table);
    #print count;
    
    while i < count:
        tr = table[i].find("tr");
        td = tr.find("td");
        
        if "Results" in td.text:
            listStr = td.text.split(" ") 
            numRes = int(listStr[len(listStr) - 1].replace(",",""));
            break;
        
        i = i + 1;
        
    br = soup.findAll("br");
    i = 0;
    count = len(br);
    
    while i < count:
        if "Found" in br[i].nextSibling:
            break;
        i = i + 1;
        
    if i < count:
        tot = int(br[i].findNextSibling('b').findNextSibling('b').text.replace(",", "")); 
        
    return (numRes, tot);

def acm(searchStr):
    try:
        httplib.HTTPConnection.debuglevel = 1
        
        req = urllib2.Request("http://dl.acm.org", headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0'});#.headers.getheader("Set-Cookie");
        conn = urllib2.urlopen(req);
        
        set_cookie = conn.headers.getheader("Set-Cookie");
        cfid = set_cookie.split(",")[0].split(";")[0].split("=")[1];
        cftok = set_cookie.split(",")[1].split(";")[0].split("=")[1];
        
        #print cfid;
        #print cftok;
        #print set_cookie;
        
        header = { "Host" : "dl.acm.org" , "Accept" : "    text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language" : "en-us,en;q=0.5" , "Accept-Encoding" : "gzip,deflate", "Connection" : "keep-alive" , "Referer" : "http://dl.acm.org" , "Cookie" : set_cookie, 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0'};
        param = urllib.urlencode({"query" : searchStr});
        
        req = urllib2.Request("http://dl.acm.org/results.cfm?h=1&cfid=" + cfid + "&cftoken=" + cftok, data = param , headers = header);
        conn = urllib2.urlopen(req);
        #print conn.read();
        return scrape(conn.read());
        
    except Exception as err:
        print err;

def getFields(url):
    param = {};
    
    ret = openURL(url);

    html = ret[1];
    
    #print html;
    
    soup = BeautifulSoup(html);
    
    #print soup;
    
    form = soup.findAll("form", {"name" : "CSBsearchForm1"})[0];
    
    field1 = form.findChild("table").findChild("tbody").findChild("tr").findChild("td").findChild("input");
    param[field1.get("name")] = field1.get("value");
    
    field2 = field1.findNextSibling("input");
    param[field2.get("name")] = field2.get("value");
    
    return (ret[0], form.get("action"), param);

def aolSearch(searchStr):
    url = 'http://search.aol.com/aol/webhome';
    ret = getFields(url);
    #print ret;
    
    names = ret[2].keys();
    
    #print ret;
    
    url = 'http://search.aol.com/' + ret[1] + '?';
    
    i = 0;
    n = len(names);
    
    while i < n:
        url += names[i] + '=' + ret[2][names[i]] + '&';            
        i = i + 1;
        
    searchStr = searchStr.replace(" ", "+")
        
    url += 'query=' + searchStr;
        
    print url;
    
    req = urllib2.Request(url, headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language':'en-us,en;q=0.5', 'Connection' : 'keep-alive', 'Host':'search.aol.com', 'Referer':'http://search.aol.com/aol/webhome', 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0', 'Set-Cookie' : ret[0]});
    
    conn = urllib2.urlopen(req);
    
    html = conn.read();
    
    #print html;
    
    soup = BeautifulSoup(html);
    
    div = soup.find("div", {"class" : "MSR"});
    
    #print div.text;
    if 'About' in div.text:
        num = div.text.split(";")[1].split('&')[0];
        
        num = num.replace(",", "");
    else:
        #print "here";
        num = div.text.split("&")[0];
        #print num;
        num = num.replace(",", "");
    
    return int(num);

        
def yahooSearch(searchStr):
    app_id = "BI2hVfnV34HAFGH_utNPLvWvwMZi_AHGPCoi0I9jIYFv2nYxcA6iTqYeofBThV8IgPe25A--";
    srch = create_search("Web", app_id, query=searchStr)
    
    if srch is not None:
        print srch.get_results();
        
        # srch object ready to use
    else:
        print "error"

def bingSearch(searchStr):
    print searchStr;
    httplib.HTTPConnection.debuglevel = 1

    #b = bing.Bing('FFBECD58E6B6F9E9E99BB5539D3D095618B26936');
    #b = bing.Bing('474A701213035B920005D9DC2D28C3405BC4C766');
    
    q = web.WebQuery('474A701213035B920005D9DC2D28C3405BC4C766', query=searchStr);
    #q = web.WebQuery('FFBECD58E6B6F9E9E99BB5539D3D095618B26936', query=searchStr);
    results = q.execute();
    
    url = str(results.query).split(" ")[1];
    
    conn = urllib2.urlopen(url);
    
    
    response = json.loads(conn.read());
    print response
    num = response["SearchResponse"]["Web"]["Total"];
    #print type(results.query);
    
    #for result in results:
    #    print result;
    #results = json.loads(q.execute());
    #print results;

    #response = b.search_web(searchStr);
    #print response['SearchResponse']['Web'];    
    #num = int(results['SearchResponse']['Web']['Total']);

    print num;
    
    #num = len(response["SearchResponse"]["Web"]["Results"]);
    #print num;

    #return num; 


def findPop(candidate):
    ret1 = acm('"' + candidate + '"')[0];
    ret2 = aolSearch('"' + candidate + '"');
    
    if ret1 != 0:
        if ret2 == 0:
            ret2 = 0.00000000000000001;
            
        #pop = math.log((float(ret1)/float(1841374)) / (float(ret2)/float(285000000)));
        pop = math.log(float(ret1) / float(ret2));
    
    else:
        pop = -sys.maxint - 1;
        
    pop = round(pop, 4);
    
    return pop;

def rank(candidates):
    n = len(candidates);
    
    #data = str(candidates) + "\n";
    
    #tfidf = fileHandle.openFile("tfidf.txt", "a");
    
    pop = [];
    
    i = 0;
    
    while i < n:
        pop.append(findPop(candidates[i]));
        #data = data + str(candidates[i]) +  "\t" + str(pop[i]) + "\n";
        i = i + 1;
        
    i = 0;
    j = 0;
    
    while i < n - 1:
        j = 0;
        flag = True;
        
        while j < n - i - 1:
            
            if pop[j] < pop[j + 1]:
                temp = pop[j];
                pop[j] = pop[j + 1];
                pop[j + 1] = temp;
                
                temp = candidates[j];
                candidates[j] = candidates[j + 1];
                candidates[j + 1] = temp;
                
                flag = False;
                
            j = j + 1;
            
        if flag:
            break;
        
        i = i + 1;
        
    num = math.ceil(float(n) / 3);
    
    i = 0;
    
    ret = [];
    
    while i < num:
        ret.append(candidates[i]);
        i = i + 1;
            
        
    #key = 0;
    #key2 = 1;
    #key3 = 2;
    
    #if(pop[0] < pop[1]):
    #    if(pop[1] < pop[2]):
    #        key = 2;
    #        key2 = 1;
    #        key3 = 0;
    #    elif(pop[2] > pop[0]):
    #        key = 1;
    #        key2 = 2;
    #         key3 = 0;
    #    else:
    #        key = 1;
    #        key2 = 0;
    #        key3 = 2;
    #else:
    #    if(pop[0] > pop[2]):
    #        key = 0;
    #        if(pop[2] > pop[1]):
    #            key2 = 2;
    #            key3 = 1;
    #        else:
    #            key2 = 1;
    #            key3 = 2;
    #    else:
    #        #2 > 0 > 1
    #        key = 2;
    #        key2 = 0;
    #        key3 = 1;
        
   
    #i = 3;
    
    #while i < n:
    #    try:
    #        if pop[i] > pop[key]:
    #            key3 = key2;
    #            key2 = key;
    #            key = i;
    #        elif pop[i] > pop[key2]:
    #            key3 = key2;
    #            key2 = i;
    #        elif pop[i] > pop[key3]:
    #            key3 = i; 
    #    except Exception as err:
    #        print err;
                
    #    i = i + 1;
    
    #data = data + "\n";
    #print data;
    #fileHandle.writeData(tfidf, data);
    
    #tfidf.close();
       
    #print "key phrase: ", candidates[key];
    #return [candidates[key], candidates[key2], candidates[key3]];

    return ret;

def toList(strList):
    keyList = re.split("[\[\],\n]", strList);
    
    
    #print keyList;
        
    i = 0;
    n = len(keyList);
    
    while i < n:
        #print keyList[i];
        #keyList[i] = str(keyList[i]);
        keyList[i] = keyList[i].strip(" ").strip("'");
        #print keyList[i];
        i = i + 1;
        
    while '' in keyList:
        keyList.remove('');
        
    return keyList;


def main():
    f = fileHandle.openFile("newCand.txt", "r");
    out = fileHandle.openFile("newKey1.txt", "w");
    
    cand = fileHandle.readLine(f);
    
    while cand != "":
        try:
            cand = toList(cand);
            
            ret = rank(cand);
            fileHandle.writeData(out, str(ret) + "\n");
        except Exception as err:
            print err;
        #break;
        cand = fileHandle.readLine(f);
        
    f.close();
    out.close();
    
#main();

#print rank(['Object', 'Recognition', 'Objects', 'Multiple-Cue Object', 'Object Recognition', 'Interactionable Objects', 'Multiple-Cue Object Recognition']);
#print rank(['Principles', 'Provability', 'Logic', 'Constructive Provability', 'Provability Logic', 'Constructive Provability Logic']);
#print rank(['Instrumentation', 'Analysis', 'Method', 'Abstractions', 'Programs', 'Instrumentation Analysis', 'Automated Method', 'Numeric Abstractions', 'Heap-Manipulating Programs']);
#print rank(['Statistical', 'Modeling', 'Activity', 'Scale', 'Networks', 'Statistical Modeling', 'Large Scale', 'Neuronal Networks']);       
#print rank(['Computation', 'Self-Adjusting Computation']);  
#bing gives a new resul each time --- have to look at a fixed corpus? --atleast if relative frequency is same its ok.. but not so
#ok for ramya to use since what existed not likely to change :) but for me.. i rely on the frequency itself!
#but where else to get such a diverse corpus which will indicate which words are common -- google books not diverse


#rank(['Performance', 'Tasks', 'Robots', 'Learning', 'Demonstrations', 'Superhuman Performance', 'Surgical Tasks', 'Iterative Learning', 'Human-Guided Demonstrations']);
#rank(['LQG-MP', 'Path', 'Planning', 'Robots', 'Motion', 'Uncertainty', 'State', 'Information', 'Path Planning', 'Motion Uncertainty', 'Imperfect State', 'State Information', 'Imperfect State Information']);
#rank(['Helicopter', 'Aerobatics', 'Apprenticeship', 'Learning', 'Autonomous Helicopter', 'Helicopter Aerobatics', 'Apprenticeship Learning']);
#rank(['Cloth', 'Grasp', 'Point', 'Detection', 'Cues', 'Application', 'Towel', 'Cloth Grasp', 'Grasp Point', 'Point Detection', 'Geometric Cues', 'Robotic Towel', 'Cloth Grasp Point', 'Grasp Point Detection']);
#rank(['Influence', 'Ship', 'Motion', 'Prediction', 'Accuracy', 'Planning', 'Control', 'Manipulators', 'Platforms', 'Ship Motion', 'Motion Prediction', 'Prediction Accuracy', 'Motion Planning', 'Motion Control', 'Robotic Manipulators', 'Seaborne Platforms', 'Ship Motion Prediction', 'Motion Prediction Accuracy']);
#rank(['GPS', 'Software', 'Receiver', 'GPS Software', 'Software Receiver']);
#print rank(['Source', 'AGPS', 'DGPS', 'Software', 'Receiver', 'Open Source', 'C-coded Software', 'Software Receiver', 'C-coded Software Receiver']);

#print aolSearch('"C-coded Software Receiver"');

#rank(['Low-Depth', 'Cache-Oblivious', 'Algorithms', 'Cache-Oblivious Algorithms']);
#rank(['Pocket', 'ISR', 'Virtual', 'Machines', 'Virtual Machines']);  
#rank(['Multiset', 'Rewriting', 'Specifications', 'Security', 'Protocols', 'Rewriting Specifications', 'Security Protocols']);      
#some phrase may be less popular in bing as well -- eg: rewriting specification -- so somehow incorporate frequency of pos pattern also -- but what weightage to give to each?        
    #findPop();
 
#bingSearch('"Machines"');
#1. 297000000, 2. 89300000


    