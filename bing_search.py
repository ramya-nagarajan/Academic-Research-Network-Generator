import bing
def search(str):
    try:
        num =0;
        b = bing.Bing('474A701213035B920005D9DC2D28C3405BC4C766')
        response = b.search_web(str);    
        num = int(response['SearchResponse']['Web']['Total']);
        if num > 0:
    #then search the resultset
                response = b.search_web(str);
                print response['SearchResponse']['Web']['Total']
        results = response['SearchResponse']['Web']['Results']
        print len(results)
    
        for result in results[:5]:
            print repr(result['Title'])
            
    except Exception as err:
            print err;

    