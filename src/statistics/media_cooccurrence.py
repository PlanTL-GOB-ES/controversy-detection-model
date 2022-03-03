import json
from urllib.parse import urlparse
from collections import Counter

if __name__ == '__main__':
    with open('../data/meneame_controversy_sampled.json', 'r') as fin:
        data = list(map(json.loads, fin.readlines()))

    data = [(d['controversy'], d['url_website']) for d in data]
    data = filter(lambda x: x[0], data)
    _, urls = zip(*data)

    data = Counter([urlparse(url).netloc for url in urls]).items()
    data = sorted(data, key=lambda x: x[1], reverse=True)
    with open('../output/media_coocurrence.tsv', 'w') as fout:
        fout.write('media\tcount\n')
        for d in data[:20]:
            fout.write(f'{d[0]}\t{d[1]}\n')

