import json
import pandas as pd
from collections import defaultdict


if __name__ == '__main__':
    words = True
    results = ['ents/', 'no_propn/no_propn_test_'] # 'ents/', 'no_ents/','no_propn/no_propn_test_'
    for res in results:
        print(res)
        with open('data/shap_all/'+res+'pos_all.json', 'r', encoding='utf-8') as fin:
            raw = json.loads(json.loads(fin.readlines()[0]))
        df = pd.DataFrame(raw)
        unique_entities = df['entity_group'].unique()
        df_group = df.groupby(by=['entity_group', 'word'])
        df_sum = df_group['value'].mean()
        #df_group_pos = df.groupby(by=['entity'])
        #df_sum_pos = df_group_pos['value'].mean() # or mean()?

        #print(df)

        data = df.values.tolist()
        entity_dict = {}
        for i in unique_entities:
            entity_dict[i] = [[],[]]
        for line in data:
            if line[5] >= 0:
                entity_dict[line[0]][0].append(line[5])
            else:
                entity_dict[line[0]][1].append(line[5])

        for key,value in entity_dict.items():
            if key in ['VERB', 'PROPN', 'ADV', 'NOUN', 'ADJ']:
                try:
                    print(key, sum(value[0])/len(value[0]), sum(value[1])/len(value[1]), len(value[0])+len(value[1]))
                except ZeroDivisionError:
                    print(key, 0, 0)

        propn_values = [[],[]]
        if res == 'no_propn/no_propn_test_':
            for line in raw:
                if line['word'] == 'PROPN':
                    if line['value'] >= 0:
                        propn_values[0].append(line['value'])
                    else:
                        propn_values[1].append(line['value'])
            print('PROPN-token', sum(propn_values[0])/len(propn_values[0]), sum(propn_values[1])/len(propn_values[1]), len(propn_values[0])+len(propn_values[1]))

        if words:
            for unique_entity in ['ADV']: # 'PROPN', 'VERB', 'ADV', 'NOUN', 'ADJ'
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
