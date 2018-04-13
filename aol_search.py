def aolSearch(searchStr):
    url = 'http://search.aol.com/aol/webhome';
    ret = getFields(url);
    print ret;
    
    names = ret[2].keys();
    
    #print ret;
    
    url = 'http://search.aol.com/' + ret[1] + '?';
    
    i = 0;
    n = len(names);
    
    while i < n:
        url += names[i] + '=' + ret[2][names[i]] + '&';            
        i = i + 1;
        
    searchStr = searchStr.replace(" ", "+")
        
    url += 'query=' + searchStr;
        
    print url;
    
    req = urllib2.Request(url, headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language':'en-us,en;q=0.5', 'Connection' : 'keep-alive', 'Host':'search.aol.com', 'Referer':'http://search.aol.com/aol/webhome', 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0', 'Set-Cookie' : ret[0]});
    
    conn = urllib2.urlopen(req);
    
    html = conn.read();
    
    #print html;
    
    soup = BeautifulSoup(html);
    
    div = soup.find("div", {"class" : "MSR"});
    
    #print div.text;
    if 'About' in div.text:
        num = div.text.split(";")[1].split('&')[0];
        
        num = num.replace(",", "");
    else:
        #print "here";
        num = div.text.split("&")[0];
        #print num;
        num = num.replace(",", "");
    
    return int(num);


def getFields(url):
    param = {};
    
    ret = openURL(url);

    html = ret[1];
    
    #print html;
    
    soup = BeautifulSoup(html);
    
    #print soup;
    
    form = soup.findAll("form", {"name" : "CSBsearchForm1"})[0];
    
    field1 = form.findChild("table").findChild("tbody").findChild("tr").findChild("td").findChild("input");
    param[field1.get("name")] = field1.get("value");
    
    field2 = field1.findNextSibling("input");
    param[field2.get("name")] = field2.get("value");
    
    return (ret[0], form.get("action"), param);

