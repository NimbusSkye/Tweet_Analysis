import pandas as pd

annotations_1 = "annotated_800_hamza.csv"
annotations_2 = "annotated_800_himanshu.csv"
annotations_3 = "annotated_800_nimbus.csv"

anno_df_1 = pd.read_csv(annotations_1)
anno_df_2 = pd.read_csv(annotations_2)
anno_df_3 = pd.read_csv(annotations_3)

anno_df_1_count = anno_df_1.groupby("coding").count()
anno_df_2_count = anno_df_2.groupby("coding").count()
anno_df_3_count = anno_df_3.groupby("coding").count()

# print("hamza")
# print(anno_df_1_count)
# print("himanshu")
# print(anno_df_2_count)
# print("nimbus")
# print(anno_df_3_count)

agreement = 0

for i in range(800):
    if i < 10:
        print(anno_df_1["coding"][i])
    if anno_df_1["coding"][i] == anno_df_2["coding"][i] == anno_df_3["coding"][i]:
        agreement += 1

# print(agreement)
pe = 0
tags = ["mv", "gv", "pv", "pc", "cd", "c", "ot", "h", "cs"]

for i in range(9):
    # print(anno_df_1_count["id"][i])
    pe += (anno_df_1_count["id"][i]/2400)*(anno_df_2_count["id"][i]/2400)*(anno_df_1_count["id"][i]/2400)

po = agreement/800

kappa = (po - pe)/(1-pe)

print(f'pe: {pe}')
print(f'po: {po}')
print(f'kappa: {kappa}')