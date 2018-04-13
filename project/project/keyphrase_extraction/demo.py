import preprocess;
import fileHandle;
import phraseSelect;

def main(title):
    
    #f = fileHandle.openFile("demo.txt", "w");
    
    patterns = phraseSelect.readPatterns("freqPatACM.txt");
    
    title = preprocess.removeParenthExp(title);
    tokens = preprocess.tokenize(title);
    
    print "Tokens: " + str(tokens) + "\n\n";
    #fileHandle.writeData(f, "Tokens: " + str(tokens) + "\n\n");
    
    keyWords = phraseSelect.tagAcronym(tokens);
    
    tagged = preprocess.tagPOS(tokens, keyWords);
    
    print "POS Tagged tokens:" + str(tagged) + "\n\n";
    #fileHandle.writeData(f, "POS Tagged tokens:" + str(tagged) + "\n\n");
    
    candidates = phraseSelect.posPhrase(tagged, patterns);
    
    print "Candidates: " + str(candidates);
    #fileHandle.writeData(f , "Candidates: " + str(candidates));
    
    #f.close();
    
main('Chip Multiprocessors for Server Workloads');