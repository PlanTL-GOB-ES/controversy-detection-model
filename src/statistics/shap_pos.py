import json
from collections import defaultdict
from transformers import AutoModelForTokenClassification, AutoTokenizer, AutoConfig, pipeline


def load_pos_pipeline(dir):
    model = AutoModelForTokenClassification.from_pretrained(dir)
    tokenizer = AutoTokenizer.from_pretrained(dir)
    config = AutoConfig.from_pretrained(dir)
    return pipeline('token-classification', model=model, tokenizer=tokenizer, config=config, aggregation_strategy='max')


POS_MODEL = 'PlanTL-GOB-ES/roberta-base-bne-capitel-pos'
INPUT_SHAP_RESULTS = '../output/shap_results_no_content.json'
if __name__ == '__main__':
    pos_pipeline = load_pos_pipeline(POS_MODEL)
    with open(INPUT_SHAP_RESULTS, 'r', encoding='utf-8') as fin:
        texts = list()
        values = list()
        words = list()
        for line in fin:
            line = json.loads(line)
            text = line['text']
            shap_values = line['shap_values']
            shap_text = line['shap_text']
            texts.append(text)
            values.append(shap_values)
            words.append(shap_text)

        pos = pos_pipeline(texts)
        pos = [[defaultdict(int, element) for element in _pos] for _pos in pos]
        for _pos, _words, _values in zip(pos, words, values):
            start = 0
            for word, value in zip(_words, _values):
                if word:
                    end = start + len(word) - 1
                    for entity in _pos:
                        e_start, e_end = entity['start'], entity['end']
                        if start >= e_start and start < e_end and end > e_start and end <= e_end:
                            print(word, entity['word'])
                            entity['value'] = entity['value'] + value
                    start = end + 1
        pos_tags_values = defaultdict(int)
        for _pos in pos:
            for __pos in _pos:
                tag = __pos['entity_group']
                pos_tags_values[tag] = + __pos['value']
        pos_tags_values = sorted(pos_tags_values.items(), key=lambda x: x[1])
        for ptv in pos_tags_values:
            print(ptv[0] + '\t' + str(ptv[1]))
