'''
Created on Feb 21, 2012

@author: Ramya
'''
from BeautifulSoup import BeautifulSoup
import urllib

def viewSource(url):
        sock = urllib.urlopen(url)
        htmlSource = sock.read()
        sock.close();
        return htmlSource

def extract():
    global err;

    main = viewSource("http://www.cs.duke.edu/research/artificial/");
    soup = BeautifulSoup(main);
    #furl = htmlSource + 
    faculty_1 = soup.findAll("ul", {"class" : "ResearchFaculty MarginTopZero MarginBottomZero"});
    faculty_2 = soup.findAll("ul", {"class" : "ResearchFaculty MarginBottomZero"});
    faculty = faculty_1 + faculty_2;
    #print faculty; 
    print "------------------------------------------------------------"
    #print len(publ);
    list_fac_1 = faculty[0].findChildren("li");
    list_fac_2 = faculty[1].findChildren("li");
    list_fac = list_fac_1 + list_fac_2;
    print  list_fac;
    print"==========================================================="
    
    links = [];
    
    for i in range(0, len(list_fac) - 1):
        links.append(list_fac[i].findChild('a'));
        url = "http://www.cs.duke.edu" + links[i].attrs[0][1];
       # print url;
        page = viewSource(url);
        soup1 = BeautifulSoup(page);
        pubs = soup1.findAll("ul",{"class" : "PeopleIndivPubs"});
        if(pubs != []):     
            print "Publications are >>> ", pubs; 
            
    
        
    
    #links_1 = list_fac[0].find("a");
    #links_2 = list_fac[1].find("a");
    
    #i = 0;
    #count = len(faculty);
    #for i in range(0, count-1):
    #    links = links_1.attrs[0][1];
    #    print links;
    #    links = links_1.attrs[0][1];
    #    print links;
    #    links = links_2.attrs[0][1];
    #    print links;

    
    #for i in range(10, count - 1): 
    #    location = faculty[i].text.split(" ")[3];
    #    names = extractCollegeName(faculty[i].attrs[2][1]);
    #    num = len(names);
        
    #    j = 0;


    #    while j < num:
    #        str = names[j].text;
    #        
    #        try:
    #            write(str , location);
    #        except UnicodeEncodeError:
    #            err.write(location + " " + names[j].attrs[0][1] + "\n");
    #            print location;
    #    

    #        print j;
    #        j = j + 1;
        

def write(name , loc):
    file.write("{'name' : '" + name + "' , 'location' : '" + loc + "'}\n");

def extractCollegeName(url):
    city = viewSource("http://www.topengineeringcolleges.co.in/" + url);
    soup = BeautifulSoup(city);
    names = soup.findAll("span", {"class" : "countryname1"});
    return names;

#def openFile(name):
 #   file = open(name , "w");
  #  return file;

#file = openFile("Colleges.json");
#err = open("error.txt" , "w");
extract();
#file.close();
