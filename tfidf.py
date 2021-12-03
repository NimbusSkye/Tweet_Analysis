import pandas as pd
import sys
import json
import math

def compile_words(csv):
    df=pd.read_csv(csv,usecols=[1,2],dtype=str)
    categories = ['mv','pv','gv','c','pc','cd','cs','h','ot']
    result = {category:{} for category in categories}

    stopwords=[]

    with open('stopwords.txt','r') as f:
        for i in range(6):
            next(f)
        for line in f:
            stopwords.append(line.strip())

    for row in df.itertuples():
        no_punc=row.text.translate({ord(ch):' ' for ch in '()[],-.?!:;#&'})
        list_words=no_punc.split()
        category=row.coding
        for word in list_words:
            word=word.lower()
            if word not in stopwords and word.isalpha():
                if word in result[category]:
                    result[category][word]+=1
                else:
                    result[category][word]=1

    counts={word:0 for category in result for word in result[category]}

    for category in result:
        for word in result[category]:
            counts[word]+=result[category][word]

    bad_words=[word for word in counts if counts[word]<10]

    for char in result:
        for word in bad_words:
            try:
                del result[char][word]
            except KeyError:
                pass

    return result

def compute_lang(counts):

    idf={word:0 for char in counts for word in counts[char]}

    for char in counts:
        for word in counts[char]:
            idf[word]+=1

    for word in idf:
        idf[word]=math.log10(6/idf[word])

    tfidf=counts

    for char in tfidf:
        for word in tfidf[char]:
            tfidf[char][word]*=idf[word]

    return tfidf

def main():
    if len(sys.argv)!=2:
        print('Invalid # arguments. Exiting.')
        quit()

    wcounts=compile_words(sys.argv[1])

    with open('wcounts.json','w') as out:
        json.dump(wcounts,out,indent=4)

    tfidf=compute_lang(wcounts)
    for char in tfidf:
        tfidf[char]=sorted(tfidf[char],key=tfidf[char].get,reverse=True)[:10]
    with open('tfidf.json','w') as f:
        json.dump(tfidf,f,indent=4)

if __name__ == '__main__':
    main()