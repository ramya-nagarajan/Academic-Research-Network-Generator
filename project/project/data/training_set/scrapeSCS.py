from BeautifulSoup import BeautifulSoup
import urllib
import fileHandle
import re

def viewSource(url):
    
        sock = urllib.urlopen(url)
        htmlSource = sock.read()
        sock.close();
        return htmlSource
    
def scrape(url):
    
    base = 'http://reports-archive.adm.cs.cmu.edu/';
        
    main = viewSource(url);
    soup = BeautifulSoup(main);
    lists = soup.findAll('a');
    
    #titleList = soup.findAll('b');
    
    titles = []; #check for the words "keywords", then '.'
    keyList = [];
    
    print lists;
    #count = len(lists);
    i = 0;
    globTit = 0;
    globAbs = 0;
    
    while i < 19:
        try:
            href = lists[i].get("href");
            
            print href;
            
            html = viewSource(base + href);
            soup = BeautifulSoup(html);
            
            #print titleList[i + 1];
            
            links = soup.findAll('a');
            possTitles = soup.findAll('b');
            #print titles;
                    
            count = len(possTitles);
            j = 1;
            
            while j < count:
                #print j;
                if possTitles[j].findNextSibling('a') != None:
                    titles.append(str(possTitles[j].text).replace("\n", " "));
                    #print possTitles[j].findNextSibling('a');
                    #print titles[globTit];
                    globTit = globTit + 1;
                    #print title;
            
                j = j + 1;
            
            count = len(links);
            j = 0;
            
            while j < count:
                #print j;
                try:
                    abstract = links[j].text;
                                            
                    if 'Abstract' in abstract:
                        #title = links[j].previous;
                        
                        #print title;
                        
                        #print links[j].get('href');
                        
                        paper = viewSource(base + links[j].get('href'));
                        soup1 = BeautifulSoup(paper);
                        
                        bold = soup1.findAll('b');
                        
                        k = 0;
                        n = len(bold);
                        
                        while k < n:
                            if 'Keywords:' in bold[k].text:
                                break;
                            k = k + 1;
                            
                        if k == n:
                            titles.pop(globAbs); #no keywords for that paper
                            globTit = globTit - 1;
                            j = j + 1;
                            #print "!!";
                            continue;
                        #print type(bold[0]);
                        
                        #break;
                        
                        keyStr = bold[k].nextSibling;
                        #print "#", keyStr;
                        keyStr = str(keyStr);
                        
                        print "#", keyStr, "#";
                        if keyStr == ' ' or 'NA' in keyStr or keyStr == '':
                            print 'here';
                            titles.pop(globAbs);
                            globTit = globTit - 1;
                            j = j + 1;
                            continue;
                        
                        keyStr = keyStr.replace('\n', ' ')
                        
                        keywords = re.split(",", str(keyStr));
                                       
                        
                        while '' in keywords:
                            keywords.remove('');
                        
                        
                        k = 0;
                        n = len(keywords);
                        while k < n:
                            keywords[k] = keywords[k].strip(' ');
                            k = k + 1;
                            
                        keyList.append(keywords);   
                        #print keyList[globAbs];       
                        globAbs = globAbs + 1;
                        #print outer.find('b').findNextSibling();
                        #title = soup1.findAll('b')[2].text;
                        #print title;
                        
                        #break;
                except Exception as err:
                    print err;
                    
                j = j + 1;
                
            #break;
        except Exception as error:
            print error;
        
        i = i + 1;
    
    titl = fileHandle.openFile("titles.txt", "w");
    
    tCount = len(titles);
    
    fileHandle.writeData(titl, str(tCount) + "\n");
    fileHandle.writeData(titl, str(globTit) + "\n");
    
    i = 0;
    while i < tCount:
        fileHandle.writeData(titl, str(titles[i]) + "\n");
        i = i + 1;
        
    titl.close();    
        
    keys = fileHandle.openFile("keywords.txt", "w");
    
    kCount = len(keyList);
    
    fileHandle.writeData(keys, str(kCount) + "\n");
    fileHandle.writeData(keys, str(globAbs) + "\n");
    
    i = 0;
    while i < kCount:
        fileHandle.writeData(keys, str(keyList[i]) + "\n");
        i = i + 1;
        
    keys.close();
    
    #print len(keyList);
     
scrape('http://reports-archive.adm.cs.cmu.edu/cs.html');