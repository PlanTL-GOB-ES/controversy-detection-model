import json
import random

BALANCED = False
if __name__ == '__main__':
    with open('../../../bsc/meneame_controversy_sampled.json', 'r', encoding='utf-8') as fin:
        data = fin.readlines()
    random.shuffle(data)

    if BALANCED:
        data = list(map(json.loads, data))
        num_controversy = len(list(filter(lambda x: not not x['controversy'], data)))
        data_filtered = []
        counter = 0
        for d in data:
            if d['controversy']:
                data_filtered.append(d)
            elif num_controversy > counter:
                counter = counter + 1
                data_filtered.append(d)
        data = data_filtered
        indices = list(range(len(data)))
        train_indices, indices = indices[:len(indices)//100 * 90], indices[len(indices)//100 * 90:]
        valid_indices, test_indices = indices[:len(indices)//2], indices[len(indices)//2:]
        train = [d for idx, d in enumerate(data) if idx in train_indices]
        valid = [d for idx, d in enumerate(data) if idx in valid_indices]
        test = [d for idx, d in enumerate(data) if idx in test_indices]

        def write(split, data):
            with open(f'{split}.json', 'w', encoding='utf-8') as fout:
                for d in data:
                    fout.write(json.dumps(d))
                    fout.write('\n')

        write('train', train)
        write('valid', valid)
        write('test', test)
    else:
        train = data[0:18_000]
        valid = data[18_000:19_000]
        test = data[19_000:]

        def write(split, data):
            with open(f'{split}.json', 'w', encoding='utf-8') as fout:
                fout.writelines(data)

        write('train', train)
        write('valid', valid)
        write('test', test)

