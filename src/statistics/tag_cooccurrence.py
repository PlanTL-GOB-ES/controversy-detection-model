import json
import csv
from collections import Counter
from itertools import chain

if __name__ == '__main__':
    with open('../data/meneame_controversy_sampled.json', 'r') as fin:
        data_sampled_all = list(map(json.loads, fin))

    with open('../data/meneame_controversy.json', 'r', encoding='utf-8') as fin:
        tags_all = []
        for line in fin:
            try:
                d = json.loads(line)
                tags_all.extend(d['tags'])
            except:
                pass
        tags_all = Counter(tags_all)

    data = [(d['controversy'], d['tags']) for d in data_sampled_all.copy()]
    data = filter(lambda x: x[0], data)
    data = [d[1] for d in data]
    data = list(chain.from_iterable(data))
    data = Counter(data)
    data = data.items()
    data = sorted(data, key=lambda x: x[1], reverse=True)

    tags_all = [tags_all[d[0]] for d in data]
    with open('../output/tag_coocurrence.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(['tag', 'occurrences controversy sampled', 'total occurrences'])
        for (tag, count), count_all in zip(data, tags_all):
            csv_writer.writerow([tag, count, count_all])
