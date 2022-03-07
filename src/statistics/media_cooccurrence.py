import csv
import json
from urllib.parse import urlparse
from collections import Counter

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

    data = [(d['controversy'], d['url_website']) for d in data_sampled_all.copy()]
    data = filter(lambda x: x[0], data)
    _, urls = zip(*data)

    data = Counter([urlparse(url).netloc for url in urls]).items()
    data = sorted(data, key=lambda x: x[1], reverse=True)

    data_sampled_all = [d['url_website'] for d in data_sampled_all]
    data_sampled_all = Counter([urlparse(url).netloc for url in data_sampled_all])
    sampled_all_counts = [data_sampled_all[url[0]] for url in data]
    data_all = Counter([urlparse(url).netloc for url in data_all])
    data_all_counts = [data_all[url[0]] for url in data]
    with open('../output/media_coocurrence.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(['Source', 'Controversy Occurrences', 'Total Occurrences Sampled', 'Total Occurrences'])
        for (media, count), sampled_count, all_count in zip(data, sampled_all_counts, data_all_counts):
            csv_writer.writerow([media, count, sampled_count, all_count])



