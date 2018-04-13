import fileHandle;
import urllib2;
import bing;
import urllib;
import preprocess;
import math;
from BeautifulSoup import BeautifulSoup;
import phraseSelect;
import sys;
import re;

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

def bingSearch(searchStr):
    b = bing.Bing('474A701213035B920005D9DC2D28C3405BC4C766');

    response = b.search_web(searchStr);
    print response['SearchResponse']['Web'];    
    num = int(response['SearchResponse']['Web']['Total']);

    return num; 

def readPara(name):
    f = fileHandle.openFile(name + "Para.txt", "r");
        
    line = fileHandle.readLine(f);
    part = line.split(";");
    mean0 = float(part[0]);
    variance0 = float(part[1].split("\n")[0]);
        
    line = fileHandle.readLine(f);
    part = line.split(";");
    before = float(part[1].split("\n")[0]);
        
    line = fileHandle.readLine(f);
    part = line.split(";");
    after = float(part[1].split("\n")[0]);
        
    line = fileHandle.readLine(f);
    part = line.split(";");
    mean3 = float(part[0]);
    variance3 = float(part[1].split("\n")[0]);
        
    n = int(fileHandle.readLine(f));
        
    f.close();
    
    return ((mean0, variance0), before, after, (mean3, variance3), n);

def classify(inp):
    
    inp = inp.split(";");
    length = len(inp);
    inp[length - 1] = inp[length - 1].split("\n")[0];
    
    paraPos = readPara("positive");
    
    paraNeg = readPara("negative");    
        
    length = len(paraPos);
    
    nPos = paraPos[length - 1];
    nNeg = paraNeg[length - 1];
    tot = nPos + nNeg;
    
    #positive
    priorPos = float(nPos)/float(tot);
    
    mean = paraPos[0][0];
    var = paraPos[0][1];
    pos0 = (1 / math.sqrt(2 * math.pi * var)) * math.exp(-math.pow((float(inp[0]) - mean), 2) / (2 * var));
    
    if inp[1] == "1":
        pos1 = paraPos[1] / nPos;
    else:
        pos1 = (nPos - paraPos[1]) / nPos;
        
    if inp[2] == "1":
        pos2 = paraPos[2] / nPos;
    else:
        pos2 = (nPos - paraPos[2]) / nPos;
        
    mean = paraPos[3][0];
    var = paraPos[3][1];
    pos3 = (1 / math.sqrt(2 * math.pi * var)) * math.exp(-math.pow((float(inp[3]) - mean), 2) / (2 * var));
    
    pPos = priorPos * pos0 * pos1 * pos2 * pos3;
    
    #negative
    priorNeg = float(nNeg)/float(tot);
    
    mean = paraNeg[0][0];
    var = paraNeg[0][1];
    neg0 = (1 / math.sqrt(2 * math.pi * var)) * math.exp(-math.pow((float(inp[0]) - mean), 2) / (2 * var));
    
    if inp[1] == "1":
        neg1 = paraNeg[1] / nNeg;
    else:
        neg1 = (nNeg - paraNeg[1]) / nNeg;
        
    if inp[2] == "1":
        neg2 = paraNeg[2] / nNeg;
    else:
        neg2 = (nNeg - paraNeg[2]) / nNeg;
        
    mean = paraNeg[3][0];
    var = paraNeg[3][1];
    neg3 = (1 / math.sqrt(2 * math.pi * var)) * math.exp(-math.pow((float(inp[3]) - mean), 2) / (2 * var));
    
    pNeg = priorNeg * neg0 * neg1 * neg2 * neg3;
    
    return pPos/pNeg;

def constructVector(phrase, key, title, tags, patterns, freq):
    vector = "";
    
    title = preprocess.tokenize(title.lower());
    while '' in title:
        title.remove('');
        
    title = handleCC(title);
    
    print title;   
    
    #tags = preprocess.tokenize(tags); #handle 'and' in tokens
    #while '' in tags:
    #    tags.remove('');
    
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
        print i;
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
    #    logACM = math.log(ret1[0]);
    #    print "ACM: ", logACM;
    #else:
    #    logACM = 0;
    
    ret2 = bingSearch('"' + searchStr + '"');
    #tot = bingSearch("a");
    #if ret2 != 0:
    #    logBing = math.log(ret2);
    #    print "Bing: ", logBing;
    #else:
    #    logBing = 0;
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
        
        freqFeature = math.log(float(ret1) / float(ret2));        
        #freqFeature = round(freqFeature, 4);
    else:
        freqFeature = -sys.maxint - 1;
        #freqFeature = round(freqFeature, 4);
    
    freqFeature = round(freqFeature, 4);
    print freqFeature;
    
    vector += str(freqFeature);# + ";";
    
    #if key:
    #    vector += "1";
    #else:
    #    vector += "0";
    
    return vector;

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
    ret = readPatterns("freqPatACM.txt");
    
    f = fileHandle.openFile("test.txt", "r");
    kf = fileHandle.openFile("testKey.txt", "r");
    
    out = fileHandle.openFile("testOut.txt", "a");
    
    title = fileHandle.readLine(f);
    
    correct = [];
    k = 0;
    
    while k <= 15:
        try:
            correct.append(0);
            outKey = [];
            title = preprocess.removeParenthExp(title);
            
            keys = toList(fileHandle.readLine(kf));
            tokens = preprocess.tokenize(title);
                
            keyWords = phraseSelect.tagAcronym(tokens);
            
            tokens = handleCC(tokens); 
                 
            tagged = preprocess.tagPOS(tokens, keyWords);
                
            #print "\n", tagged, "\n";
                
            candidates = phraseSelect.posPhrase(tagged, ret[0]);
            
            print candidates;
            
            i = 0;
            n = len(candidates);
                    
            while i < n:
                print "candidates[", i, "]: ", candidates[i];
                
                vector = constructVector(candidates[i], True, title, tagged, ret[0], ret[1]);
                category = classify(vector);
                
                if category > 1:
                    print candidates[i], ": positive";
                    outKey.append(candidates[i]);
                    
                    if candidates[i] in keys:
                        correct[k] += 1;
                else:
                    print candidates[i], ": negative";
                    
                    if candidates[i] not in keys:
                        correct[k] += 1;
                    
                #fileHandle.writeData(f1, str(vector) + "\n");
                print vector;
                print "i = ", i;
                i = i + 1;
            
            fileHandle.writeData(out, str(outKey) + "\n");
            
            title = fileHandle.readLine(f);
            
        except Exception as err:
            print err;
            fileHandle.writeData(out, "\n");
            pass;
        
        k = k + 1;
        title = fileHandle.readLine(f);
        
    print correct;
    fileHandle.writeData(out, str(correct) + "\n");
    
    out.close();
    f.close();
    kf.close();
 
bingSearch("Classification algorithm for a small positive training set");       
#main();