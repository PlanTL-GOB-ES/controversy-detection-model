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
    with open('../data/meneame_controversy_sampled.json', 'r', encoding='utf-8') as fin:
        texts = list()
        for item in tqdm(fin):
            item = json.loads(item)
            if content:
                text = item['title'] + '--' + item['content']
            else:
                text = item['title']
            texts.append(text)
    shap_values = explainer(texts)
    # Save computations
    with open(f'../output/shap_results_{"content" if content else "no_content"}.json', 'w', encoding='utf-8') as fout:
        for text, shap_result in zip(texts, shap_values):
            out = {
                'text': text,
                'shap_values': shap_result.values[:, 0].tolist(),
                'shap_text': shap_result.data
            }
            fout.write(json.dumps(out))
            fout.write('\n')


INPUT_PATH = '../models/title'
if __name__ == '__main__':
    model = AutoModelForSequenceClassification.from_pretrained(INPUT_PATH)
    tokenizer = AutoTokenizer.from_pretrained(INPUT_PATH)
    config = AutoConfig.from_pretrained(INPUT_PATH)
    pipeline = pipeline('text-classification', model=model, tokenizer=tokenizer, config=config, return_all_scores=True)
    explainer = shap.Explainer(pipeline)
    compute_all(explainer, content=False)
