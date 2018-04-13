import fileHandle;
import re;

def toList(strList): #lower case
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
    can = fileHandle.openFile("newCand.txt", "r");
    acc = fileHandle.openFile("acc1.txt", "w");
    
    tp = 0;
    fp = 0;
    tn = 0;
    fn = 0;
    
    candList = fileHandle.readLine(can);
    
    while candList != "":
        fPos = [];
        tPos = [];
        fNeg = [];
        tNeg = [];
        
        candList = toList(candList);
        
        keyList = toList(fileHandle.readLine(f1));
        actualKey = toList(fileHandle.readLine(f2));
        
        i = 0;
        n = len(candList);
        
        while i < n:
            if candList[i] in actualKey:
                if candList[i] in keyList:
                    tPos.append(candList[i]);
                    tp = tp + 1;
                else:
                    fNeg.append(candList[i]);
                    fn = fn + 1;
            else:
                if candList[i] in keyList:
                    fPos.append(candList[i]);
                    fp += 1;
                else:
                    tNeg.append(candList[i]);
                    tn = tn + 1;
            i = i + 1;
            
        data = "True Pos: " + str(tPos) + "\n";
        data += "False Neg: " + str(fNeg) + "\n";
        data += "False Pos: " + str(fPos) + "\n";
        data += "True Neg: " + str(tNeg) + "\n\n";
        
        fileHandle.writeData(acc, data);
        
        candList = fileHandle.readLine(can);
    
    data = "tot true pos: " + str(tp) + "\n";
    data += "tot false Neg: " + str(fn) + "\n";
    data += "tot false Pos: " + str(fp) + "\n";
    data += "tot true Neg: " + str(tn);
    
    fileHandle.writeData(acc, data);
    
    f1.close();
    f2.close();
    can.close();
    acc.close();
    
main("newKey1.txt", "key.txt");