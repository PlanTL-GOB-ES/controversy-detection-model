import json
import pandas as pd
from collections import defaultdict


if __name__ == '__main__':
    with open('output/all_data/pos_all.json', 'r', encoding='utf-8') as fin:
        data = json.loads(json.loads(fin.readlines()[0]))
    df = pd.DataFrame(data)
    unique_entities = df['entity'].unique()
    df_group = df.groupby(by=['entity', 'word'])
    df_sum = df_group['value'].sum()
    df_group_pos = df.groupby(by=['entity'])
    df_sum_pos = df_group_pos['value'].sum() # or mean()?

    print(df_sum_pos)

    for unique_entity in unique_entities:
        print("\hline")
        pos_selection = df_sum[unique_entity].nlargest(25)
        neg_selection = df_sum[unique_entity].nsmallest(25)
        pos = list(zip(pos_selection.index, pos_selection))
        neg = list(zip(neg_selection.index, neg_selection))
        for i, w in enumerate(pos):
            if i == 4:
                print(unique_entity, " & ", w[0], " & & ", f'{w[1]:.2f}', " & ", neg[i][0], " & & ", f'{neg[i][1]:.2f}', " \\\ ")
            else:
                print( " & ", w[0], " & & ", f'{w[1]:.2f}', " & ", neg[i][0], " & & ", f'{neg[i][1]:.2f}',
                      " \\\ ")
