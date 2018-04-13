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
    links = soup.findAll("ul", {"class" : "PeopleIndivPubs"});

    i = 0;
    count = len(links);
    
    for i in range(10, count - 1): 
        location = links[i].text.split(" ")[3];
        names = extractCollegeName(links[i].attrs[2][1]);
        num = len(names);
        
        j = 0;


        while j < num:
            str = names[j].text;
            
            try:
                write(str , location);
            except UnicodeEncodeError:
                err.write(location + " " + names[j].attrs[0][1] + "\n");
                print location;
        

            print j;
            j = j + 1;
        

def write(name , loc):
    file.write("{'name' : '" + name + "' , 'location' : '" + loc + "'}\n");

def extractCollegeName(url):
    city = viewSource("http://www.topengineeringcolleges.co.in/" + url);
    soup = BeautifulSoup(city);
    names = soup.findAll("span", {"class" : "countryname1"});
    return names;

def openFile(name):
    file = open(name , "w");
    return file;

file = openFile("Colleges.json");
err = open("error.txt" , "w");
extract();
file.close();
