import math
import re

def stop(f):
    words=[]
    with open(f,'r') as file:
        for line in file:
            for w in line.split():
                words.append(w)
    file.close()
    return words
def remove(f):
    stopwords=stop('stopwords.txt')
    words=[]
    with open(f,'r') as file:
        for line in file:
            line = line.split()
            for w in line:
                w = w.lower()
                if w in stopwords or 'http://' in w or 'https://' in w or w=='':
                    continue
                else:
                    w=w.lower()
                    for c in w:
                        if c != ' ' and c != '(' and c != ')' and  c != '{' and c != '}' and c != ',' and c != '.' and c != '*' and c != '-' and c != '\"':
                            re.sub('[^A-Za-z0-9_]+', ' ', c)  
                    if w [-3:]=='ing':
                        w = w[:-3]
                    if w [-2:]=='ly':
                        w = w[:-2]
                    if w [-4:]=='ment':
                        w = w[:-4]
                    if w [-2] == '\'':
                        w = w[:-2] + w[-1]
                    if w [-1:] == ',':
                        w = w[:-1]    
                    word = ''

                    if word not in stopwords:
                        words.append(word.lower())
    file.close()
    s = 'preproc_'+f
    with open(s,'w')as file:
        for w in words:
            file.write(w)
            file.write(' ')
def tf(f):
    words=dict()
    total = 0
    with open(f,'r')as file:        
        for line in file:
            line=line.split()
            for w in line:
                if w in words:
                    words[w]+=1
                else:
                    words[w]=1
                total+=1
    for w in words.keys():
        words [w]/=total
    return words

d = []
with open ('tfidf_docs.txt','r')as file:
    for line in file:
        line=line.split()

        remove('tfidf_docs.txt')
        s='preproc_'+ 'tfidf_docs.txt'
        tfidff = 'tfidf_'+ 'tfidf_docs.txt'
        d.append(tf(s))


        idf=dict()
        for doc in d:
            for w in doc:
                if w not in idf:
                    count=0
                    for doc in d:
                        if w in doc:
                            count+=1
                    score=math.log(len(d)/count)
                    idf [w]=round(score,2)+1

        tfidf=dict()
        for doc in d:
            for w in doc:
                if w not in tfidf:
                    tfidf[w]=doc[w]*idf[w]

        tfidf = {k: v for k, v in sorted(tfidf.items(), key=lambda item: item[1], reverse = True)}
        i = 0
        with open (tfidff, 'w') as file:
            for k in tfidf.keys():
                if i >= 5:
                    break
                file.write(k)
                file.write(' ')
                file.write(str(round(tfidf[k], 2)))
                file.write(' ')
                i += 1
