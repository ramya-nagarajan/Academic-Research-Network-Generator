import urllib;
import urllib2;
import pyPdf;
from BeautifulSoup import BeautifulSoup;
import math;
def viewSource(url):
    
    req = urllib2.Request(url, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language":"en-us,en;q=0.5", "Connection" : "keep-alive", "User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0" });
        
    conn = urllib2.urlopen(req)
    htmlSource = conn.read()
    conn.close();
    return htmlSource;

def cosine_sim():        

        p1 = [];
        p2 = [];
    #i=0;
    #while i < 10:
            #print n;
        #if i >= 10:
            #print "!!", i;
            #break;
        #print "i: ", i;
        phrase1 = "Scalable Storage";
        phrase2 = "Internet Worms";
        
        phrase1 = phrase1.lower();
        phrase2 = phrase2.lower();
        freq = {phrase1 : 0, phrase2 : 0};

            #print results[i];         
            #url = results[i]['Url'];
        url = ["http://www.cs.odu.edu/~mukka/cs775s11/Presentations/papers/lee.pdf","http://www.pdl.cmu.edu/PDL-FTP/Storage/CMU-PDL-12-103.pdf","http://www.techrepublic.com/topics/internet+and+viruses++and++worms+and+web+browser?s=20","http://www.billdoll.com/dir/ci/q/emerging_opps.html","http://www.shopwiki.co.uk/l/worms-data?page=3","http://www.cisco.com/application/pdf/en/us/guest/netsol/ns304/c654/cdccont_0900aecd80096182.pdf","http://www.dtic.mil/cgi-bin/GetTRDoc?AD=ADA465393","http://www.zdnet.com.au/whitepapers/network-wide-deployment-of-intrusion-detection-and-prevention-systems-22541867/","http://www.zdnet.com.au/whitepapers/a-flexible-approach-to-embedded-network-multicast-authentication-22531966/","http://www.zdnet.com.au/whitepapers/reusing-migration-to-simply-and-efficiently-implement-multi-server-operations-in-transparently-scalable-storage-systems-22541863/"];
        
        #n = len(url);
        k=0;
        while k<10:
            u = url[k];
            print u;
            n = len(u);
            
            if u[n - 4:] == '.pdf':
                urllib.urlretrieve(u, "try.pdf");
                try:
                    f = open("try.pdf", "rb");
                    pdf = pyPdf.PdfFileReader(f);
                    #print pdf;
                    #f.close();
                    
                    pages = pdf.getNumPages();
                    #print pages;
                    text = pdf.read(f);
                    #f.close();
                    j = 0;
                    
                    ind1 = 0;
                    ind2 = 0;
                    
                    while j < pages:
                        try:
                            text = pdf.getPage(j).extractText();
							#print j;
                            #print j;
							#print j;
                            #print j;                               
                            temp = text.lower();
                            phrase1 = phrase1.lower();
    
                            while phrase1 in temp:
                                #print "HIIIIII!"
                                ind1 = temp.index(phrase1) + len(phrase1);
                                temp = temp[ind1:];
                                freq[phrase1] += 1;
                            
                                #temp = text;
                               
                            while phrase2.lower() in temp.lower():
                                ind2 = temp.lower().index(phrase2.lower()) + len(phrase2);
                                temp = temp[ind2:];
                                freq[phrase2] += 1;
                             
                            j = j + 1;
                        except (UnicodeEncodeError,Exception) as err:
							print err;
							if 'unicode' in str(err).lower() or 'decrypted' in str(err).lower():
								j = j + 1;
                    
                
                except Exception as err:
                    print "error";
                f.close();       
            else:
                try:
                    u = url[k];
                    #print url;
                    htmlSource = viewSource(u);
                    soup = BeautifulSoup(htmlSource);
                    body = soup.find("body");
                        
                    text = body.text;
    
                    temp = text.lower();
                    print temp;
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
					print err;
					pass;
            p1.append(freq[phrase1]);
            p2.append(freq[phrase2]);
                #i = i + 1;
            k=k+1;
            print k;
        print "Phrase 1: ", p1;
        print "Phrase 2: ", p2;
            
        value = dot(p1,p2);
        val = (float(mag(p1)) * float(mag(p2)));
            
        if val==0:
            val = 0.0000000001; 
        cos = float(value) / val;
                
            #if cos <= 0.4 or cos==0.00:
        if cos <= 0.81:    
            print "Dissimilar words";
            #return 0;
        else:
            ret = round(cos, 4);
            print ret;
            #return ret;
    

def dot(u, v):
    i = 0;
    n = len(u);
    
    dot = 0;
    
    while i < n:
        dot += u[i] * v[i];
        i += 1;
        
    return dot;

def mag(u):
    i = 0;
    n = len(u);
    val = 0;
    while i < n:
        val += (u[i] * u[i]);
        i = i + 1;
        
    val = math.sqrt(val);
    
    return val;
      
def main():
    cosine_sim();
main();