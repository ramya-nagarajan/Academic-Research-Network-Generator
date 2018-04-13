import string;
import fileHandle;

patterns = [('JJ', 'NN'), ('NN', 'NN'), ('JJ', 'NNS'), ('NN', 'NNS'), ('NN'), ('NN', 'NN', 'NN')]; #make 3 word patters also

#forget noun phrase idea.. find better patterns
#write a learning algorithm to find patterns --- any database of keywords should do to get candidates since POS is being relied on

def tagAcronym(tokens):
    keyPhrase = [];
    
    #caps = string.uppercase;
    small = string.lowercase;
    
    i = 0;
    count = len(tokens);
    
    while i < count:
        j = 0;
        strlen = len(tokens[i]);
        
        if strlen > 1:
            while j < strlen:
                if tokens[i][j] in small:
                    break;
                j = j + 1;
            
        if j == strlen:
            keyPhrase.append(tokens[i]);
        
        i = i + 1;
        
    return keyPhrase;

def readPatterns(name):
    f = fileHandle.openFile(name, "r");
    
    patterns = [];
    
    pat = fileHandle.readLine(f);
    
    while pat != "":
        if '#' not in pat:
            patList = pat.split(" ");
            patList.pop();
            
            patterns.append(patList);
        
        pat = fileHandle.readLine(f);
        
    return patterns;

def posPhrase(tagged, patterns): #acronyms might come twice since they are also part of candidates
    
    
    #print patterns;
    
    candidates = [];
    
    i = 0;
    count = len(tagged);
    posList = [];
    
    while i < count:
        posList. append(tagged[i][1]);
        
        #print "posList = ", posList;
        
        if posList in patterns and tagged[i][0] not in candidates:
            candidates.append(tagged[i][0]);
            
        posList = [];
        
        i = i + 1;
        
    i = 0;
    posList = [];
    #count = len(tagged);
    
    while i < count:
        if i != count - 1:
            posList. append(tagged[i][1]);
            posList. append(tagged[i + 1][1]);
            
            if posList in patterns:
                if tagged[i][0] + " " + tagged[i + 1][0] not in candidates:
                    candidates.append(tagged[i][0] + " " + tagged[i + 1][0]);
                
            posList = [];
        
        i = i + 1;
        
    i = 0;
    posList = [];
    #count = len(tagged);
    
    while i < count:
        if i < count - 2:
            posList. append(tagged[i][1]);
            posList. append(tagged[i + 1][1]);
            posList. append(tagged[i + 2][1]);
            
            if posList in patterns:
                if tagged[i][0] + " " + tagged[i + 1][0] + " " + tagged[i + 2][0] not in candidates:
                    candidates.append(tagged[i][0] + " " + tagged[i + 1][0] + " " + tagged[i + 2][0]);
                
            posList = [];
        
        i = i + 1;
        
        #if tagged[i][1] == 'NN':
        #    candidates.append(tagged[i][0]);
            
        #if i != count - 1:
            
        #    if tagged[i][1] == 'NN' and tagged[i + 1][1] == 'NN':
        #        candidates.append(tagged[i][0] + " " + tagged[i + 1][0]);
                
        #    if tagged[i][1] == 'JJ' and tagged[i + 1][1] == 'NN':
        #        candidates.append(tagged[i][0] + " " + tagged[i + 1][0]);
                
        #    if tagged[i][1] == 'JJ' and tagged[i + 1][1] == 'NNS':
        #        candidates.append(tagged[i][0] + " " + tagged[i + 1][0]);
                
        #    if tagged[i][1] == 'NN' and tagged[i + 1][1] == 'NNS':
        #        candidates.append(tagged[i][0] + " " + tagged[i + 1][0]);
                
        #if i < count - 2: #verify these and see if more to be added
        #    if tagged[i][1] == 'NN' and tagged[i + 1][1] == 'NN' and tagged[i + 2][1] == 'NN':
        #        candidates.append(tagged[i][0] + " " + tagged[i + 1][0] + " " + tagged[i + 2][0]);
                
        #    if tagged[i][1] == 'NN' and tagged[i + 1][1] == 'NN' and tagged[i + 2][1] == 'NNS':
        #        candidates.append(tagged[i][0] + " " + tagged[i + 1][0] + " " + tagged[i + 2][0]);
                
        #    if tagged[i][1] == 'JJ' and tagged[i + 1][1] == 'NN' and tagged[i + 2][1] == 'NNS':
        #        candidates.append(tagged[i][0] + " " + tagged[i + 1][0] + " " + tagged[i + 2][0]);
                
        #    if tagged[i][1] == 'JJ' and tagged[i + 1][1] == 'NN' and tagged[i + 2][1] == 'NN':
        #        candidates.append(tagged[i][0] + " " + tagged[i + 1][0] + " " + tagged[i + 2][0]);
                
        #i = i + 1;   
        
    return candidates;