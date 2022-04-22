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


PATH = '../data/'
if __name__ == '__main__':
    with open(os.path.join(PATH, 'meneame_controversy_sampled.json'), 'r', encoding='utf-8') as fin:
        data = fin.readlines()
    data = list(map(json.loads, data))

    controversy = list(filter(lambda x: not not x['controversy'], data))
    no_controversy = list(filter(lambda x: not x['controversy'], data))

    random.shuffle(controversy)
    random.shuffle(no_controversy)

    num_controversy = len(controversy)

    # split controversy first
    train_controversy, valid_controversy, test_controversy = split(controversy)

    # unbalanced
    train, valid, test = split(no_controversy)
    train_unbalanced = train_controversy + train
    valid_unbalanced = valid_controversy + valid
    test_unbalanced = test_controversy + test

    # balanced
    train, valid, test = split(no_controversy[:num_controversy])
    train_balanced = train_controversy + train
    valid_balanced = valid_controversy + valid
    test_balanced = test_unbalanced  # test_controversy + test

    # write all
    write('split_20k', 'train', train_unbalanced)
    write('split_20k', 'valid', valid_unbalanced)
    write('split_20k', 'test', test_unbalanced)

    write('split_balanced', 'train', train_balanced)
    write('split_balanced', 'valid', valid_balanced)
    write('split_balanced', 'test', test_balanced)

