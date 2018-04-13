import preprocess;
import fileHandle;
import phraseSelect;
import rank;
from neo4j import GraphDatabase

def main():
    #title = fileHandle.readLine(f); #if title has something in paranthesis
    
    db = GraphDatabase("D:\\preethi\\data\\graph");
    relationships = db.relationships;
    
    #print str(rel[0].type);
    
    patterns = phraseSelect.readPatterns("..\\freqPat.txt");

    #for rel in relationships:
    i = 0;
    n = len(relationships);
    while i < n:
        try:
            rel = relationships[i];
            if str(rel.type) == 'author_of':
                paper = rel.end;
                title = paper['title'];
                print title;
                #break;
                title = preprocess.removeParenthExp(title);
                #print title;
                tokens = preprocess.tokenize(title);
                #print tokens;
                
                tokens = preprocess.handleCC(tokens);
                
                keyWords = phraseSelect.tagAcronym(tokens);
                
                
                tagged = preprocess.tagPOS(tokens, keyWords);
                #print tagged;
               
                
                candidates = phraseSelect.posPhrase(tagged, patterns);
                
                with db.transaction:
                    paper['candidates'] = candidates;
                print 'Candidates: ', paper['candidates'];
                
                keyphrases = rank.rank(candidates);
                
                with db.transaction:
                    paper['key'] = keyphrases;
                print 'Keyphrases: ', paper['key'];
                
                i += 1;
        except Exception as err:
            print "Here";
            print err;
        
    db.shutdown();
        
main();
#db = GraphDatabase("D:\\preethi\\data\\graph");
#with db.transaction:
    #rel = db.relationships[0];
    #rel.end["key"] = ('a', 'b');
    #print type(rel.end["key"]);
    #del rel.end["key"];

#db.shutdown();