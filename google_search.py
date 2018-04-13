import urllib
import json
import pdfreader
def google(searchStr):

    query = urllib.urlencode({'q': searchStr})
    
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    
    #url = 'http://www.google.com/#hl=en&sclient=psy-ab&%s' % query
    
    print url;
    
    search_response = urllib.urlopen(url)
    search_results = search_response.read();
    results = json.loads(search_results)
    
    #return results;
    data = results['responseData']
    
    num = data['cursor']['estimatedResultCount']
    
    return int(num);
    #hits = data['results']
        
    #print 'Top %d hits:' % len(hits)
      
    #for h in hits: print ' ', h['url']
    
    #print 'For more results, see %s' % data['cursor']['moreResultsUrl']