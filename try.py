import urllib;
import urllib2;
import pyPdf;
import bing;

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
                f.close();
                
                top.append(('pdf', pdf));
            
            else:
                htmlSource = viewSource(url);
                
                top.append(('html', htmlSource));
            
            i = i + 1;
        #num = int(response['SearchResponse']['Web']['Total']);
    
        return top;
        #return num;
    except Exception as err:
        print err; 


def main():
    
    print bingSearch('"Classification algorithm for a small positive training set"');
    
    #urllib.urlretrieve(url, "try.pdf");
    
    #f = open("try.pdf", "rb");
    
    #f.close();
    
    #f = open("try.pdf", "r");  
    #f = open('D:\\preethi\\Documents\\8th_sem\\project\\tag cloud\\unsup_ontology.pdf', "rb")  ;
    #pdf = pyPdf.PdfFileReader(f);
    #print pdf.getNumPages();
    #f.close();
    
    
    #print pdf.getPage(1).extractText();
    pass;

main();
#main('http://www1.i2r.a-star.edu.sg/~xlli/publication/ECML_PKDD_Li_2007.pdf')