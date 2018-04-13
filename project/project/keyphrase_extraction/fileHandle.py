def openFile(name, mode):
    f = open(name, mode);
    return f;

def readLine(f):
    return f.readline();

def writeData(f, data):
    f.write(data);