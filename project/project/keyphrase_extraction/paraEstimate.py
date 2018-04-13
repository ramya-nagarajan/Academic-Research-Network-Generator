import fileHandle;
import math;

def main(name):
    f = fileHandle.openFile(name + ".txt", "r");
    
    n = 0;
    
    line = fileHandle.readLine(f);
    before = 0;
    after = 0;
    
    mean0 = 0;
    mean3 = 0;
    
    para0 = [];
    para3 = [];
    
    while line != "":
        
        para = line.split(";");
        
        length = len(para);
        
        para[length - 1] = para[length - 1].split("\n")[0];
        
        if para[1] == "1":
            before += 1;
            
        if para[2] == "1":
            after += 1;
            
        para0.append(float(para[0]));
        para3.append(float(para[3]));
        
        mean0 += para0[n];
        mean3 += para3[n];

        n = n + 1;
        
        line = fileHandle.readLine(f);
        
    mean0 = mean0 / n;
    mean3 = mean3 / n;
    
    i = 0;
    
    variance0 = 0;
    variance3 = 0;
    
    while i < n:
        variance0 += math.pow((para0[i] - mean0), 2);
        variance3 += math.pow((para3[i] - mean3), 2);
        
        i = i + 1;
        
    variance0 /= n;
    variance3 /= n;
    
    f.close();
    
    f = fileHandle.openFile(name + "Para.txt", "w");
    
    fileHandle.writeData(f, str(mean0) + ";" + str(variance0) + "\n");
    fileHandle.writeData(f, str(n - before) + ";" + str(before) + "\n");
    fileHandle.writeData(f, str(n - after) + ";" + str(after) + "\n");
    fileHandle.writeData(f, str(mean3) + ";" + str(variance3) + "\n");
    fileHandle.writeData(f, str(n));
    
    f.close();
    
main("positive");
main("negative");
    #write mean;variance \n 0 count; 1 count \n 0 count; 1 count \n mean;variance \n n;