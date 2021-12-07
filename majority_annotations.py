import pandas as pd

annotations_1 = "annotated_800_hamza.csv"
annotations_2 = "annotated_800_himanshu.csv"
annotations_3 = "annotated_800_nimbus.csv"

anno_df_1 = pd.read_csv(annotations_1)
anno_df_2 = pd.read_csv(annotations_2)
anno_df_3 = pd.read_csv(annotations_3)

anno_final = anno_df_1.copy()

c=0
s=0

for i in range(803):

    coding1 = anno_df_1['coding'][i]
    coding2 = anno_df_2['coding'][i]
    coding3 = anno_df_3['coding'][i]
    maj = 'UNK'

    if(coding1 == coding2 ):
        maj =coding1
        c=c+1
    
    elif(coding1 == coding3):
        maj=coding1
        c=c+1

    elif(coding2 == coding3):
        maj=coding2
        c=c+1

    anno_final['coding'][i]=maj

    #print(f'{coding1} {coding2} {coding3} \n')

for i in range(803):

    sent1 = anno_df_1['sentiment'][i]
    sent2 = anno_df_2['sentiment'][i]
    sent3 = anno_df_3['sentiment'][i]
    maj = 'UNK'

    if(sent1 == sent2 ):
        maj =sent1
        s=s+1

    elif(sent1 == sent3):
        maj=sent1
        s=s+1

    elif(sent2 == sent3):
        maj=sent2
        s=s+1

    anno_final['sentiment'][i]=maj

#    if(maj == 'UNK'):
#        print(f'{sent1} {sent2} {sent3} \n')


print(f'the number of cases in coding where UNK wasnt needed = {c}\n')
print(f'the number of cases in sentiment where UNK wasnt needed = {s}\n')

#print(f'{anno_df_1}')
#print(f'{anno_final}')
anno_final.to_csv('annotated_800_combined.csv', encoding='utf-8', index=False)
