#run this code and print tokens, POS tagged tokens and the candidate phrases --- first cache in file

import preprocess;
import fileHandle;
import phraseSelect;
import rank;

def main():
    f = fileHandle.openFile("titles2.txt", "r");
    
    out = fileHandle.openFile("newCand.txt", "a");
    key = fileHandle.openFile("newKey.txt", "a");
    
    title = fileHandle.readLine(f); #if title has something in paranthesis
    
    patterns = phraseSelect.readPatterns("freqPat.txt");
    #patterns = phraseSelect.readPatterns("freqPatACM.txt");
    
    while title != "":
        try:
            title = preprocess.removeParenthExp(title);
            #print title;
            tokens = preprocess.tokenize(title);
            #print tokens;
            
            tokens = preprocess.handleCC(tokens);
            
            keyWords = phraseSelect.tagAcronym(tokens);
            #print keyWords;
            
            #taggedTok = [];
            
            #i = 0;
            #count = len(tokens);
            
            
            #while i < count:
            #    if tokens[i] in candidates:
            #        taggedTok.append((tokens[i],'NNP'));
            #    else:
            #        taggedTok.append((tokens[i],'')); 
            #        
            #    i = i + 1;   
            
            #print taggedTok;
            
            tagged = preprocess.tagPOS(tokens, keyWords);
            
            print "\n", tagged, "\n";
            
            candidates = phraseSelect.posPhrase(tagged, patterns);
            
            print "Candidates = ", candidates; #problem
            #print tagged;
            
            #fileHandle.writeData(out, str(candidates) + "\n");
            
            keyphrases = rank.rank(candidates);
            
            print "Keyphrases = ", keyphrases;
            
            fileHandle.writeData(key, str(keyphrases) + "\n");
        
        except Exception as err:
            print err;
        
        title = fileHandle.readLine(f);
        
    out.close();
    key.close();
    f.close();
        
        
main();
