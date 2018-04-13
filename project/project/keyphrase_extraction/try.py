import urllib;
import urllib2;
import pyPdf;
import bing;
from BeautifulSoup import BeautifulSoup;

def viewSource(url):
    
    sock = urllib.urlopen(url)
    htmlSource = sock.read()
    sock.close();
    return htmlSource

def bingSearch(searchStr):
    try:
        #b = bing.Bing('474A701213035B920005D9DC2D28C3405BC4C766');
        b = bing.Bing('FFBECD58E6B6F9E9E99BB5539D3D095618B26936');
        response = b.search_web(searchStr);
        print response['SearchResponse']['Web'];
        num = int(response['SearchResponse']['Web']['Total']);
        
        if num == 0:
            #declare vectors to be orthogonal and return
            return;
        results = response['SearchResponse']['Web']['Results'];    
        
        top = [];
        
        i = 0;
        
        while i < 5:
            url = results[i]['Url'];
            
            n = len(url);
            if url[n - 4:] == '.pdf':
                urllib.urlretrieve(url, "try.pdf");
        
                f = open("try.pdf", "rb");
                pdf = pdf = pyPdf.PdfFileReader(f);
                
                pages = pdf.getNumPages();
            
                j = 0;
            
                while j < pages:
                    #find frequency of the phraeses in the page
                    j = j + 1;
                
            
            else:
                htmlSource = viewSource(url);
                soup = BeautifulSoup(htmlSource);
                body = soup.find('body');
                print body.text;
                #find frequencies of phrases in body.text 
            
            i = i + 1;
        
    
        f.close();
        #return frequency of each phrse in top 5 results --- maybe like a tuple of two lists, each list containing op 5 freq eg: ([2,3,4,5], [2,3,4,5])
        
    except Exception as err:
        print err; 


def main():
    
    ret = bingSearch('Classification algorithm for a small positive training set');
    
    
            

main();