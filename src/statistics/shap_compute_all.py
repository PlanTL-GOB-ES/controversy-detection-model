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

    with open('../data/meneame_controversy_sampled.json', 'r', encoding='utf-8') as fin:
        texts = list()
        for item in tqdm(fin):
            item = json.loads(item)
            if content:
                text = item['title'] + '--' + item['content']
            else:
                text = item['title']
            texts.append(text)
    shap_values = explainer(texts[0:10])
    # Save computations
    with open(f'../output/shap_results_{"content" if content else "no_content"}.json', 'w', encoding='utf-8') as fout:
        for text, shap_result in zip(texts[0:10], shap_values):
            out = {
                'text': text,
                'shap_values': shap_result.values[:, 0].tolist(),
                'shap_text': shap_result.data
            }
            fout.write(json.dumps(out))
            fout.write('\n')

    """
    # Compute by word
    for words, value in zip(shap_values.data, shap_values.values):
        # words = shap_values.data[0]
        label_0 = value[:, 0]

        for word, value in zip(words, label_0):
            data_0[word] = data_0[word] + value

    with open(f'../output/shap_words_{"content" if content else "no_content"}.json', 'w', encoding='utf-8') as fout:
        json.dump(data_0, fout)
    
    print("Label 0")
    print_stats(data_0)
    """


INPUT_PATH = '../models/title'
if __name__ == '__main__':
    model = AutoModelForSequenceClassification.from_pretrained(INPUT_PATH)
    tokenizer = AutoTokenizer.from_pretrained(INPUT_PATH)
    config = AutoConfig.from_pretrained(INPUT_PATH)
    pipeline = pipeline('text-classification', model=model, tokenizer=tokenizer, config=config, return_all_scores=True)
    explainer = shap.Explainer(pipeline)
    compute_all(explainer, content=False)
