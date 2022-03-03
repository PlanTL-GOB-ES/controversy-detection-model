import json
from scipy.stats import pointbiserialr

if __name__ == '__main__':
    with open('../data/meneame_controversy_sampled.json', 'r') as fin:
        data = list(map(json.loads, fin.readlines()))

    controversy, comments = zip(*[(d['controversy'], d['number_comments']) for d in data])
    print(pointbiserialr(controversy, comments))

    # Result: PointbiserialrResult(correlation=0.2990078345339685, pvalue=0.0)
