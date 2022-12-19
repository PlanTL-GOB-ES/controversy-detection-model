import os
import json
import random


def split(data):
    indices = list(range(len(data)))
    train_indices, indices = indices[:len(indices) // 100 * 90], indices[len(indices) // 100 * 90:]
    valid_indices, test_indices = indices[:len(indices) // 2], indices[len(indices) // 2:]
    train = [d for idx, d in enumerate(data) if idx in train_indices]
    valid = [d for idx, d in enumerate(data) if idx in valid_indices]
    test = [d for idx, d in enumerate(data) if idx in test_indices]
    return train, valid, test


def write(collection, split, data):
    with open(os.path.join(PATH, collection, f'{split}.json'), 'w', encoding='utf-8') as fout:
        for d in data:
            fout.write(json.dumps(d))
            fout.write('\n')


PATH = 'data/'
if __name__ == '__main__':
    with open(os.path.join(PATH, 'meneame_controversy_sampled.json'), 'r', encoding='utf-8') as fin:
        data = fin.readlines()
    data = list(map(json.loads, data))

    cont_count = 0
    cont = []
    no_cont = []
    for line in data:
        if line['controversy']:
            cont_count += 1
            cont.append(line)
        else:
            no_cont.append(line)

    new_data = cont + no_cont[:cont_count]

    random.shuffle(new_data)
    print(cont_count, len(new_data))

    with open(os.path.join(PATH+'shap_eval.json'), 'w', encoding='utf-8') as fout:
        for d in new_data:
            fout.write(json.dumps(d))
            fout.write('\n')