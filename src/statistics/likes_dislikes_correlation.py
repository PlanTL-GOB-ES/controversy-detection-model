import json
from scipy.stats import pointbiserialr

if __name__ == '__main__':
    with open('../data/meneame_controversy_sampled.json', 'r') as fin:
        data = list(map(json.loads, fin.readlines()))

    controversy, positives, negatives = zip(*[(d['controversy'], d['positive_votes'], d['negative_votes']) for d in data])
    positives_negatives = list(map(lambda x: x[0] - x[1], zip(positives, negatives)))
    print(pointbiserialr(controversy, positives))
    print(pointbiserialr(controversy, negatives))
    print(pointbiserialr(controversy, positives_negatives))

    # PointbiserialrResult(correlation=0.03867201670720913, pvalue=3.326899106764101e-08)
    # PointbiserialrResult(correlation=0.8097246068445221, pvalue=0.0)
    # PointbiserialrResult(correlation=-0.10512477418228533, pvalue=3.428207741214995e-51)
