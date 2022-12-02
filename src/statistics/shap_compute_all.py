import os
import argparse
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline, AutoConfig
import shap
import json
from collections import defaultdict
from tqdm import tqdm
import glob


def print_stats(data):
    data = sorted(data.items(), key=lambda x: x[1])
    print("Positive")
    print(data[:-20:-1])
    print("Negative")
    print(data[:20])


def compute_all(explainer, content, path, output):
    with open(path, 'r', encoding='utf-8') as fin:
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
    with open(output, 'w', encoding='utf-8') as fout:#f'output/{os.path.basename(path)}_{"content" if content else "no_content"}.jsonl', 'w', encoding='utf-8') as fout:
        for text, shap_result in zip(texts, shap_values):
            out = {
                    'text': text,
                    'shap_values': shap_result.values[:, 0].tolist(),
                    'shap_text': shap_result.data.tolist()
                }
            print(out)
            fout.write(json.dumps(out))
            fout.write('\n')


#INPUT_PATH = '../models/no_ents_sum'
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('--idx', type=int)
    parser.add_argument('--model', type=str)
    parser.add_argument('--input', type=str)
    parser.add_argument('--output', type=str)
    args = parser.parse_args()
    INPUT_PATH=args.model
    model = AutoModelForSequenceClassification.from_pretrained(INPUT_PATH)
    tokenizer = AutoTokenizer.from_pretrained(INPUT_PATH)
    config = AutoConfig.from_pretrained(INPUT_PATH)
    pipeline = pipeline('text-classification', model=model, tokenizer=tokenizer, config=config, return_all_scores=True, device=0)
    explainer = shap.Explainer(pipeline)
    compute_all(explainer, content=True, path=args.input, output=args.output) # glob.glob('../data/x*')[args.idx])
