from BeautifulSoup import BeautifulSoup
import urllib
import fileHandle

def viewSource(url):
    
        sock = urllib.urlopen(url)
        htmlSource = sock.read()
        sock.close();
        return htmlSource
    
def scrape(url):
    
    #base = 'http://www.eecs.berkeley.edu';
    
    f = fileHandle.openFile("..\\..\\keyphrase_extraction\\acm.txt", "w");
    
    main = viewSource(url);
    soup = BeautifulSoup(main);
    lists = soup.findAll('ol', {'type' : 'a'});
    
    count = len(lists);
    i = 0;
    
    while i < count:
        listItems = lists[i].findChildren('li');
        
        j = 0;
        n = len(listItems);
        
        while j < n:
            keyPhrases = listItems[j].text;
            f.write(keyPhrases + "\n");
            
            j = j + 1;
        
        #break;
        
        i = i + 1;
    
      
    
scrape('http://www.computer.org/portal/web/publications/acmtaxonomy');