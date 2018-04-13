import re;
import urllib;
import json;
import urllib2;
from BeautifulSoup import BeautifulSoup;
import fileHandle;
import preprocess;
import math;
#import pybing;
import bing;
import sys; 
#from prepareTraining import handleCC

def handleCC(tokens):
    if 'and' in tokens:
        ind = tokens.index('and')
        temp1 = tokens[0:ind - 1];
        temp2 = tokens[ind + 2:];
        if ind > 1:
            k = 0;
            #print "temp: ", temp;
            #break;
            #print ind;
            c = len(temp1);
            while k < c:
                tokens.insert(ind + 1 + k, temp1[k]);
                k = k + 1;
                
        if ind + 1 != len(tokens) - 1:
            k = 0;
                
            #print "temp: ", temp2;
            #break;
            c = len(temp2);
            while k < c:
                tokens.insert(ind + k, temp2[k]);
                k = k + 1;
                
    if 'And' in tokens:
        ind = tokens.index('And')
        temp1 = tokens[0:ind - 1];
        temp2 = tokens[ind + 2:];
        if ind > 1:
            k = 0;
            #print "temp: ", temp;
            #break;
            #print ind;
            c = len(temp1);
            while k < c:
                tokens.insert(ind + 1 + k, temp1[k]);
                k = k + 1;
                
        if ind + 1 != len(tokens) - 1:
            k = 0;
                
            #print "temp: ", temp2;
            #break;
            c = len(temp2);
            while k < c:
                tokens.insert(ind + k, temp2[k]);
                k = k + 1;
        
    return tokens;

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

def bingSearch(searchStr):
    b = bing.Bing('474A701213035B920005D9DC2D28C3405BC4C766');

    response = b.search_web(searchStr);    
    num = int(response['SearchResponse']['Web']['Total']);

    return num;

def google(searchStr):

    query = urllib.urlencode({'q': searchStr})
    
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query;
    
    #url = 'https://www.google.co.in/#hl=en&output=search&sclient=psy-ab&q=google+ajax+api&oq=google+ajax+api&aq=f&aqi=g10&aql=&gs_l=hp.3..0l10.1946l6479l1l6803l15l15l0l6l6l0l294l1866l0j5j4l9l0.frgbld.&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=62189b117f3e72c5&biw=1366&bih=624';
    #print url;
    
    req = urllib2.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0'});
    
    #url = 'http://www.google.com/#hl=en&sclient=psy-ab&%s' % query
    
    #print url;
    
    search_response = urllib2.urlopen(req)
    search_results = search_response.read();
    results = json.loads(search_results)
    
    #print search_results;
    data = results['responseData']
    
    num = data['cursor']['estimatedResultCount']
    
    return int(num);
    #hits = data['results']
        
    #print 'Top %d hits:' % len(hits)
      
    #for h in hits: print ' ', h['url']
    
    #print 'For more results, see %s' % data['cursor']['moreResultsUrl']
    
def acm(searchStr):
    try:
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

def seggregate(cand, keys):
    i = 0;
    n = len(keys);
    
    while i < n:
        if keys[i] in cand:
            #print cand;
            #print keys[i]
            cand.remove(keys[i]);    
        i = i + 1;
        
    return cand;

def readPatterns(name):
    f = fileHandle.openFile(name, "r");
    
    patterns = [];
    freq = [];
    
    pat = fileHandle.readLine(f);
    
    while pat != "":
        if '#' not in pat:
            patList = pat.split(" ");
            freq.append(patList.pop().split("\t")[1].split("\n")[0]);
            
            patterns.append(patList);
        
        pat = fileHandle.readLine(f);
        
    return (patterns, freq);

def constructVector(phrase, key, title, tags, patterns, freq):
    vector = "";
    
    title = preprocess.tokenize(title.lower());
    while '' in title:
        title.remove('');
        
    title = handleCC(title);
    
    print title;   
    
    tags = preprocess.tokenize(tags); #handle 'and' in tokens
    while '' in tags:
        tags.remove('');
    
    searchStr = phrase;
    phrase = preprocess.tokenize(phrase);
    while '' in phrase:
        phrase.remove('');
    
    
    n = len(phrase);
    #vector += str(n) + ";";
    print "phrase: ", phrase;
    print "title", title;
    
    ind = title.index(phrase[0].lower());
    print ind;
    i = 1;
    
    while i < n: #infinite loop when word in title appears more than once
        #print 'In constructVector: i = ', i, "n = ", n;
        #print phrase[i];
        #print title[ind + i];
        #print phrase[i].lower();
        #print title[ind + i].lower();
        if phrase[i].lower() != title[ind + i].lower():
            #print "phrase[0]:", phrase[0];
            #print title[ind + 1:];
            #print "i loop";
            ind = title[ind + 1:].index(phrase[0].lower()) + ind + 1;
            #print "i loop: ", ind;
            #print phrase;
            i = 0; #since incrementing will anyway happen
        
        i = i + 1;
    #print i, "!!";
    
    j = ind;
    pat = [];
    
    while j < ind + n:
        pat.append(tags[j]);
        j = j + 1;
    
    #print "Freq:", freq[ind], "!";
    #print freq[ind];
    #print ind;
    #freq[ind] = freq[ind].split('\t')[1];
    #print "\\t:", freq[ind];
    #freq[ind] = freq[ind].split('\n')[0];#[1].split('\n')[0];
    #print freq[ind];
    
    vector += freq[ind] + ";"; #what if the keyword doesn't even match a pattern?
    
    if ind == 0:
        vector += "1;";
    else:
        if tags[ind - 1] == 'IN':
            vector += "1;";
        else:
            vector += "0;";
            
    if ind+n-1 == len(title)-1:
        vector += "1;";
    else:
        if tags[ind + 1] == 'IN':
            vector += "1;";
        else:
            vector += "0;";
            
    ret1 = acm('"' + searchStr + '"')[0];
    
    #if ret1 != 0:
        #acmVal = float(math.log(ret1[0]))/float(math.log(ret1[1]));
    
        #print "acmVal = ", acmVal;
        #logACM = math.log(ret1[0]);
        #print "ACM: ", logACM;
    #else:
        #logACM = 0;
    
    ret2 = bingSearch('"' + searchStr + '"');
    #tot = bingSearch("a");
    #if ret2 != 0:
        #logBing = math.log(ret2);
        #print "Bing: ", logBing;
    #else:
        #logBing = 0;
    #bingVal = float(ret2)/float(tot);
    
    #print searchStr;
    #print ret;
    print searchStr;
    #print "bingVal = ", bingVal;
    
    #if logBing == 0:
    #    logBing = 0.00000000000000001;
    
    #freqFeature = logACM / logBing;#float(math.log(ret1[0]))/float(math.log(ret2));
    if ret1 != 0:
        if ret2 == 0:
            ret2 = 0.00000000000000001;
        print type(ret1);
        print type(ret2);
        freqFeature = math.log(float(ret1) / float(ret2));        
        freqFeature = round(freqFeature, 4);
    else:
        freqFeature = -sys.maxint - 1;
        freqFeature = round(freqFeature, 4);
        
    print freqFeature;
    
    vector += str(freqFeature) + ";";
    
    if key:
        vector += "1";
    else:
        vector += "0";
    
    return vector;

def main():
    try:
        titles = fileHandle.openFile("titles.txt", "r");
        keys = fileHandle.openFile("keywords.txt", "r");
        tags = fileHandle.openFile("tags.txt", "r");
        cand = fileHandle.openFile("candidates.txt", "r");
        
        f1 = fileHandle.openFile("..\\..\\keyphrase_extraction\\positive.txt", "a");
        f2 = fileHandle.openFile("..\\..\\keyphrase_extraction\\negative.txt", "a");
        
        ret = readPatterns("..\\..\\keyphrase_extraction\\freqPatACM.txt");
        
        title = fileHandle.readLine(titles);
        tag = fileHandle.readLine(tags);
        phrase = toList(fileHandle.readLine(cand));
        keyPhrase = toList(fileHandle.readLine(keys));
        #title = 'Locally Distributed Predicates: A Technique for Distributed Programming';
        j = 1;
        
        while j <= 50:
            
            if j <= 49:
                title = fileHandle.readLine(titles);
                tag = fileHandle.readLine(tags);
                phrase = toList(fileHandle.readLine(cand));
                keyPhrase = toList(fileHandle.readLine(keys));
                j = j + 1;
                continue;
            
            
            #tag = 'RB VBN NNS DT NN IN VBN NN';
            
            #phrase = toList("['Predicates', 'Technique', 'Programming', 'Distributed Predicates']");
            #print "Candidates = ", phrase;
            
            #keyPhrase = toList("['Distributed Programming', 'Predicates']");
            #print "Key = ", keyPhrase;
            nonKey = seggregate(phrase, keyPhrase);
            
            i = 0;
            n = len(keyPhrase);
            
            while i < n:
                vector = constructVector(keyPhrase[i], True, title, tag, ret[0], ret[1]);
                fileHandle.writeData(f1, str(vector) + "\n");
                print vector
                print "i = ", i;
                i = i + 1;
                
            i = 0;
            n = len(nonKey);
            
            while i < n:
                vector = constructVector(nonKey[i], False, title, tag, ret[0], ret[1]);
                
                print vector;
                #break;
            
                fileHandle.writeData(f2, str(vector) + "\n");
                print "i = ", i;
                i = i + 1;
                
            #raise j;
            title = fileHandle.readLine(titles);
            tag = fileHandle.readLine(tags);
            phrase = toList(fileHandle.readLine(cand));
            keyPhrase = toList(fileHandle.readLine(keys));
            print "j = ", j;
            
            #break;
            j = j + 1;
            
        titles.close();
        tags.close();
        keys.close();
        cand.close();
        f1.close();
        f2.close();
        
    except Exception as err:
        print "err: ", err;
        titles.close();
        tags.close();
        keys.close();
        cand.close();
        f1.close();
        f2.close();
 

#print bingSearch('a');
main();    
#474A701213035B920005D9DC2D28C3405BC4C766   
#print acm('"Superhuman Performance"');  
#print google('a');