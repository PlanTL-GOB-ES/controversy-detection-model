import json
import csv
from collections import Counter


if __name__ == '__main__':
    with open('../data/meneame_controversy_sampled.json', 'r') as fin:
        data = list(map(json.loads, fin.readlines()))

    with open('../data/meneame_controversy.json', 'r') as fin:
        category_all = []
        for line in fin.readlines():
            try:
                d = json.loads(line)
                category_all.append(d['category'])
            except:
                print('Error')
        category_all = Counter(category_all)

    data = [(d['controversy'], d['category']) for d in data]
    data = filter(lambda x: x[0], data)
    data = [d[1] for d in data]
    data = Counter(data)
    data = data.items()
    data = sorted(data, key=lambda x: x[1], reverse=True)

    category_all = [category_all[d[0]] for d in data]
    with open('../output/topic_coocurrence.csv', 'w', encoding='utf-8') as fout:

        csv_writer = csv.writer(fout, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(['topic', 'occurrences controversy sampled', 'total occurrences'])
        for (tag, count), count_all in zip(data, category_all):
            csv_writer.writerow([tag, count, count_all])