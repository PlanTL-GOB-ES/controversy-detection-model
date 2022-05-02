import json
import pandas as pd

if __name__ == '__main__':
    with open('../output/pos_all.json', 'r', encoding='utf-8') as fin:
        data = json.loads(json.loads(fin.readlines()[0]))
    df = pd.DataFrame(data)
    unique_entities = df['entity_group'].unique()
    df_group = df.groupby(by=['entity_group', 'word'])
    df_sum = df_group['value'].sum()

    for unique_entity in unique_entities:
        print(unique_entity)
        print("TOP 10")
        print(df_sum[unique_entity].nlargest(10))
        print("LAST 10")
        print(df_sum[unique_entity].nsmallest(10))
