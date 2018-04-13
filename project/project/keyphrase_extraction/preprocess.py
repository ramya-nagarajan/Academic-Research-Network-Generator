import re
from nltk.tag import stanford
from nltk.internals import config_java

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
            ret = tagPOS([tokens[ind - 1]], []);
            
            if 'JJ' in ret[0][1]:
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
            ret = tagPOS([tokens[ind - 1]], []);
            
            if 'JJ' in ret[0][1]:              
                k = 0;
                    
                #print "temp: ", temp2;
                #break;
                c = len(temp2);
                while k < c:
                    tokens.insert(ind + k, temp2[k]);
                    k = k + 1;
        
    return tokens;


def removeParenthExp(title): #keywords are not likely to be in parenthesized expressions --- but wat if its some explanation and would help in semantic comparison?
    while '(' in title:
        print "hi!";
        title = re.sub('\(.*\)', '', title);
        #title.replace(str[str.find('(') : str.find(')')], "")
    
    return title;


def tokenize(title): #how to treat '/'?
    try:
        tokens = re.split("[ :\n/,]", title);
        
        while "" in tokens:
            tokens.remove("");
    
        return tokens;
    except Exception as e:
        print "In pre-process -> tokenize : ", e;

            
def tagPOS(tokens, acro): 
    try:
        small = [];
        #print "Tokens : ", tokens;
        
        i = 1;    
        count = len(tokens);
        
        small.append(tokens[0]);
        
        while i < count:
            if tokens[i] not in acro:
                small.append(tokens[i].lower());
            else:
                small.append(tokens[i]);
                
            i = i + 1;
        
        #print tokens;
        #print small;
            
        #print tokens;
        #tagger = nltk.DefaultTagger();
        #print nltk.pos_tag(tokens); 
        #print os.environ;
        #
        #print os.path.isfile("C:\\Program Files\\Java\\jdk1.6.0_23\\bin\\java.exe");
        
        config_java(bin = "C:\\Program Files\\Java\\jdk1.6.0_31\\bin\\java.exe");
        
        stan = stanford.StanfordTagger(path_to_model='C:\\stanford-postagger-2011-09-14\\models\\bidirectional-distsim-wsj-0-18.tagger', path_to_jar='C:\\Program Files\\Java\\jdk1.6.0_31\\bin\\stanford-postagger.jar');
        tagged =  stan.tag(small);
        
        i = 1;
        
        #print tagged;
        
        while i < count:
            try:
                #print tagged[i][1];
                #print i;
                tagged[i] = (tokens[i], tagged[i][1]);
                #print tokens[i];
                i = i + 1;
            except:
                #print i;
                #print tagged[i - 1];
                i = i + 1;
                
        return tagged;
    
    except Exception as e:
        print "In pre-process -> tagPos : ", e;

#print tagPOS(['parsing'], []);