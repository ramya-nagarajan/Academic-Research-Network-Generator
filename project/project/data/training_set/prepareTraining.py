import preprocess;
import phraseSelect;
import fileHandle;

def handleCC(tokens):
    if 'and' in tokens:
        ind = tokens.index('and')
        temp1 = tokens[0:ind - 1];
        temp2 = tokens[ind + 2:];
        if ind > 1:
            k = 0;
            #print "temp: ", temp;
            #break;
            #print ind;
            c = len(temp1);
            while k < c:
                tokens.insert(ind + 1 + k, temp1[k]);
                k = k + 1;
                
        if ind + 1 != len(tokens) - 1:
            k = 0;
                
            #print "temp: ", temp2;
            #break;
            c = len(temp2);
            while k < c:
                tokens.insert(ind + k, temp2[k]);
                k = k + 1;
                
    if 'And' in tokens:
        ind = tokens.index('And')
        temp1 = tokens[0:ind - 1];
        temp2 = tokens[ind + 2:];
        if ind > 1:
            k = 0;
            #print "temp: ", temp;
            #break;
            #print ind;
            c = len(temp1);
            while k < c:
                tokens.insert(ind + 1 + k, temp1[k]);
                k = k + 1;
                
        if ind + 1 != len(tokens) - 1:
            k = 0;
                
            #print "temp: ", temp2;
            #break;
            c = len(temp2);
            while k < c:
                tokens.insert(ind + k, temp2[k]);
                k = k + 1;
        
    return tokens;

def main():
    titles = fileHandle.openFile("titles.txt", "r");
    #keys = fileHandle.openFile("keywords.txt", "r");
    
    patterns = phraseSelect.readPatterns("..\\..\\keyphrase_extraction\\freqPatACM.txt");
    
    print patterns;
    
    tags = fileHandle.openFile("tags.txt", "w");
    cand = fileHandle.openFile("candidates.txt", "w");
    
    #title = fileHandle.readLine(titles);
    
    title ="Designing an Interface and Path Translator for a Smartphone Based Indoor Navigation System for Visually Impaired Users";
    
    #print "title = " + title;
    #title = "A Case for World-wide Network Measurement using Smartphones and  Open Marketplaces";
    
    while title != "":
        tokens = preprocess.tokenize(preprocess.removeParenthExp(title));
        
        tokens = handleCC(tokens);
        
        
        
        #print tokens;
        acro = phraseSelect.tagAcronym(tokens);
        
        tagged = preprocess.tagPOS(tokens, acro);
        
        #print tagged;
        
        i = 0;
        count = len(tagged);
        tagStr = "";
        
        while i < count:
            tagStr = tagStr + tagged[i][1] + " ";
                       
            i = i + 1;
            
        print tagStr;
        fileHandle.writeData(tags, tagStr + "\n");
        
        candidates = phraseSelect.posPhrase(tagged, patterns);
        
        print candidates;
        
        fileHandle.writeData(cand, str(candidates) + "\n");
        
        break;
            
        title = fileHandle.readLine(titles);

    titles.close();
    cand.close();
    tags.close();
    
 
main();   
#print toList("['Active disks', 'network-attached storage', 'mobile code', 'distributed applications']");
