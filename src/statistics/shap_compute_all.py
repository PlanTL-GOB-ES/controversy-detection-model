from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline, AutoConfig
import shap
import json
from collections import defaultdict
from tqdm import tqdm


def print_stats(data):
    data = sorted(data.items(), key=lambda x: x[1])
    print("Positive")
    print(data[:-20:-1])
    print("Negative")
    print(data[:20])


def compute_all(explainer, content):
    data_0 = defaultdict(int)
    data_1 = defaultdict(int)

    with open('../data/meneame_controversy_sampled.json', 'r', encoding='utf-8') as fin:
        for item in tqdm(fin):
            item = json.loads(item)
            if content:
                text = item['title'] + '--' + item['content']
            else:
                text = item['title']
            shap_values = explainer([text])
            words = shap_values.data[0]
            label_0 = shap_values.values[0][:, 0]
            label_1 = shap_values.values[0][:, 1]

            for word, value in zip(words, label_0):
                data_0[word] = data_0[word] + value
            for word, value in zip(words, label_1):
                data_1[word] = data_1[word] + value

    with open(f'../output/data_0_{"content" if content else "no_content"}.json', 'w', encoding='utf-8') as fout:
        json.dump(data_0, fout)

    with open(f'../output/data_1_{"content" if content else "no_content"}.json', 'w', encoding='utf-8') as fout:
        json.dump(data_1, fout)

    print("Data 0")
    print_stats(data_0)
    print("Data 1")
    print_stats(data_1)


INPUT_PATH = '../models/title'
if __name__ == '__main__':
    model = AutoModelForSequenceClassification.from_pretrained(INPUT_PATH)
    tokenizer = AutoTokenizer.from_pretrained(INPUT_PATH)
    config = AutoConfig.from_pretrained(INPUT_PATH)
    pipeline = pipeline('text-classification', model=model, tokenizer=tokenizer, config=config, return_all_scores=True)
    explainer = shap.Explainer(pipeline)
    compute_all(explainer, content=False)
