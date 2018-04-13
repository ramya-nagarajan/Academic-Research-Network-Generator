#file to store frequent POS patterns in descending order
import fileHandle;

def findFreq(name): #in this case whole pattern is important.. not just sub patterns since the sub pattern need not be a keyword and we only want POS patterns of keywords
    f = fileHandle.openFile(name, "r");
    
    freq = {};
    
    line = fileHandle.readLine(f);
    
    pattern = line.split("\n")[0];
    
    while pattern != "":
        if pattern not in freq.keys():
            freq[pattern] = 1;
        else:
            freq[pattern] = freq[pattern] + 1;
            
        line = fileHandle.readLine(f);
    
        pattern = line.split("\n")[0];
        
    f.close();
    
    #invertFreq = dict([[v,k] for k,v in freq.items()]);
    
    keyList = freq.keys();  
    valList = freq.values();
    
    
    f = fileHandle.openFile("freqTags.txt", "w");
    
    
    sortedVal = sorted(valList); 
    sortedVal.reverse();
    fileHandle.writeData(f, str(sortedVal) + "\n");
    
    i = 0;
    count = len(keyList);
    
    print count;
    
    tagFreq = "";
        
    while i < count:
        tagFreq = tagFreq + keyList[i] + "\t" + str(freq[keyList[i]]) + "\n";
        
        print tagFreq;
        
        fileHandle.writeData(f, tagFreq);
        
        i = i + 1;
        tagFreq = "";
        
    f.close();
    
findFreq("tags.txt");        