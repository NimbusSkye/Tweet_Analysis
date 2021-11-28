import sys
import pandas as pd
import json

if len(sys.argv)!=3:
    print('Incorrect # arguments. Exiting.')
    quit()

out=sys.argv[2]
jsonf=sys.argv[1]

with open(jsonf,'r') as f:
    tweets=json.load(f)

posts={col:[] for col in ['id','text']}
posts['coding']=''*len(tweets)

for tweet in tweets:
    posts['id'].append('"'+tweet['data']['id']+'"')
    format_text=tweet['data']['text'].translate({ord('"'):"'",ord('\n'):''})
    posts['text'].append(format_text)
        
df=pd.DataFrame(posts)

df.to_csv(out,index=False)