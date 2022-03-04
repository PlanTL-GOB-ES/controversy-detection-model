import json
from urllib.parse import urlparse
from collections import Counter
from itertools import chain

if __name__ == '__main__':
    with open('../data/meneame_controversy_sampled.json', 'r') as fin:
        data_sampled_all = list(map(json.loads, fin.readlines()))

    with open('../data/meneame_controversy.json', 'r') as fin:
        data_all = []
        for line in fin.readlines():
            try:
                data_all.append(json.loads(line)['url_website'])
            except:
                print('Error')

    data = [(d['controversy'], d['tags']) for d in data_sampled_all.copy()]
    data = filter(lambda x: x[0], data)
    data = [d[1] for d in data]
    data = list(chain.from_iterable(data))
    data = Counter(data)
    data = data.items()
    data = sorted(data, key=lambda x: x[1], reverse=True)
    with open('../output/tag_coocurrence.tsv', 'w', encoding='utf-8') as fout:
        fout.write('tag\tcount\n')
        for d in data[:20]:
            fout.write(f'{d[0]}\t{d[1]}\n')