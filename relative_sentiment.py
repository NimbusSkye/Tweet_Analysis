import pandas as pd
import json
import pprint
import sys

def main():
    if len(sys.argv)!=2:
        print('Invalid # arguments. Exiting.')
        quit()

    annotations = sys.argv[1]

   # annotations = "annotated_800_hamza.csv"
    anno_df_1 = pd.read_csv(annotations)

    tags = ["mv", "gv", "pv", "pc", "cd", "cs", "cs","ot"]
    sent = ["p","n","x"]
    dict ={}

    for t in tags:
        total = (len(anno_df_1[anno_df_1["coding"] == t]))
        dict[t]={}

        for s in sent:
            dict[t][s]=(len(anno_df_1[(anno_df_1["coding"] == t) & (anno_df_1["sentiment"] == s)]))/total
            
    pprint.pprint(dict)

    with open('relative_sentiment.json','w') as f:
        json.dump(dict,f)


if __name__ == "__main__":
        main()
