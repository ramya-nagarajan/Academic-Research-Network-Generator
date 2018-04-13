import fileHandle;
from rank import findPop;
import sys;
import re;

def toList(strList):
    strList = strList.lower();
    keyList = re.split("[\[\],\n]", strList);
    
    
    #print keyList;
        
    i = 0;
    n = len(keyList);
    
    while i < n:
        #print keyList[i];
        #keyList[i] = str(keyList[i]);
        keyList[i] = keyList[i].strip(" ").strip("'");
        #keyList[i] = keyList[i].lower();
        #print keyList[i];
        i = i + 1;
        
    while '' in keyList:
        keyList.remove('');
        
    return keyList;


def main(name, actual):
    f1 = fileHandle.openFile(name, "r");
    f2 = fileHandle.openFile(actual, "r");
    #thresh = fileHandle.openFile("thresh1.txt", "w");
    acc = fileHandle.openFile("acc.txt", "w");
    correct = 0;
    wrong = 0;
    threshold = sys.maxint;
    
    
    data = "";
    
    keyList = fileHandle.readLine(f1);
    
    while keyList != "":
        falsePos = [];
        falseNeg = [];
        perKeyCorrect = 0;
        keyData = "";
        
        keyList = toList(keyList);
        
        actualKey = toList(fileHandle.readLine(f2));
        
        i = 0;
        n = len(keyList);
        
        while i < n:
            #data = "";
            
                
            if keyList[i] in actualKey:
                correct += 1;
                perKeyCorrect += 1;
            else:
                wrong += 1;
                falsePos.append(keyList[i]);
                
            i = i + 1;
            
        i = 0;
        m = len(actualKey);
        
        while i < m:
            try:
                #pop = findPop(actualKey[i]);
                
                #data = data +  actualKey[i] + "\t" + str(pop) + "\n";
                
                #if pop < threshold:
                #    threshold = pop;
                    
                if actualKey[i] not in keyList:
                    falseNeg.append(actualKey[i]);
                
                i = i + 1;
                
            except Exception as err:
                print err;
                
            
            
        keyData = "False Positives: " + str(falsePos) + "\nLeft out: " + str(falseNeg) + "\n";
        keyData += "Correct: " + str(perKeyCorrect) + "\n% correct: " + str(100 * float(perKeyCorrect) / n) + "\n\n";
        
        fileHandle.writeData(acc, keyData);
        
        keyList = fileHandle.readLine(f1);
        
    #data += str(threshold);
    #print threshold;
    #fileHandle.writeData(thresh, data);
    
    fileHandle.writeData(acc, "Correct: " + str(correct) + "\n");
    fileHandle.writeData(acc, "Wrong: " + str(wrong) + "\n");
    
    f1.close();
    f2.close();
    #thresh.close();
    acc.close();
    
main("newKey1.txt", "key.txt");