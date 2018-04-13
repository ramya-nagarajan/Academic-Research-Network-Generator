import pyPdf
import urllib
import urllib2
def getpdfcontent(url):
    #print "Hi"
    try:
     #   print 'hi'
        #content ="";
        
        #print numpages;
        #p = file(path,"rb")
        #pdf = pyPdf.PdfFileReader(p)
        #numpages = pdf.getNumPages();
        #print numpages;
        #for i in range(0, numpages):
            
            #content += pdf.getPage(i).extractText() + "\n"
            #content = " ".join(content.replace(u"\xa0", " ").strip().split())
           # print content
           # return content
           
        f = open(urllib.urlretrieve(url, "try.pdf")[0], "rb");
        
        #f.close();
        
        #f = open("try.pdf", "r");    
        pdf = pyPdf.PdfFileReader(f);
        print pdf.getNumPages();
        #f.close();
        
        
        print pdf.getPage(1);
        print pdf.read('try.pdf')
        
        
    except Exception as err:
            print err;
getpdfcontent('http://www1.i2r.a-star.edu.sg/~xlli/publication/ECML_PKDD_Li_2007.pdf')           
#getpdfcontent("D:\projectwork\Project_8thsem\svd.pdf");