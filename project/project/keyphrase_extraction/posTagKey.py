#tokenize key phrases and tag them
import fileHandle;
import preprocess;

def main(name, out):
    f = fileHandle.openFile(name, "r");
    
    f1 = fileHandle.openFile(out, "w");
    
    phrase = fileHandle.readLine(f);
    
    while phrase != "":
        if '/' not in phrase:
            tokens = preprocess.tokenize(phrase);
                     
            #i = 1;
            #count = len(tokens);
            
            #while i < count:
            #    tokens[i] = tokens[i].lower();
            #    i = i + 1;
               
            tagged = preprocess.tagPOS(tokens, []);
            
            i = 0;
            
            tags = "";
            
            count = len(tagged);
            
            
            while i < count:
                tags = tags + tagged[i][1] + " ";
                i = i + 1;
                
            print tags;
            
            fileHandle.writeData(f1, tags + "\n");
                
        phrase = fileHandle.readLine(f);
    
    f.close();
    f1.close();
            
main("acm.txt", "acmTags1.txt")