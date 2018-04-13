import fileHandle;
import preprocess;
import re;

def toList(strList):
    keyList = re.split("[\[\],\n]", strList);
    
    
    #print keyList;
        
    i = 0;
    n = len(keyList);
    
    while i < n:
        #print keyList[i];
        #keyList[i] = str(keyList[i]);
        keyList[i] = keyList[i].strip(" ").strip("'");
        #print keyList[i];
        i = i + 1;
        
    while '' in keyList:
        keyList.remove('');
        
    return keyList;

def main(outName):
    
    f = fileHandle.openFile(".\\..\\data\\training_set\\keywords1.txt", "r");
    
    out = fileHandle.openFile(outName, "a");
    
    line = fileHandle.readLine(f);
    
    while line != "":
        keywords = toList(line);
        print keywords;
        n = len(keywords);
        i = 0;
        
        while i < n:
            phrase = keywords[i];
            
            print phrase;
            
            #while phrase != "":
            if '/' not in phrase:
                tokens = preprocess.tokenize(phrase);
                             
                    #i = 1;
                    #count = len(tokens);
                    
                    #while i < count:
                    #    tokens[i] = tokens[i].lower();
                    #    i = i + 1;
                       
                tagged = preprocess.tagPOS(tokens, []);
                
                print tagged; 
                   
                j = 0;
                    
                tags = "";
                    
                count = len(tagged);
                    
                    
                while j < count:
                    tags = tags + tagged[j][1] + " ";
                    j = j + 1;
                        
                print tags, "\n";
                    
                fileHandle.writeData(out, tags + "\n");
            
            i = i + 1;
            
        line = fileHandle.readLine(f);
        
    f.close();
    out.close();
    
main("tags.txt");   

        
            
        