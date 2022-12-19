import json
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline
from pprint import pprint
import argparse
import re

def transform_pos(text, model):
    entities = model(text)
    if entities:
        for entity in entities:
            if entity['entity_group'] in ['PROPN']:
                #text = text[:entity['start']] + 'PROPN' + text[entity['end']:]
                text = re.sub(re.escape(entity['word']), ' ' + entity['entity_group'] + ' ', text)
    return text


def main():
    # argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, action="store", help="Input file")
    parser.add_argument("--output", required=True, action="store", help="Output file")
    args = parser.parse_args()

    # import data
    data = []
    with open(args.input, 'r') as file1:
        bal = file1.readlines()
    for line in bal:
        c = json.loads(line)
        data.append(c)

    # create the pipeline
    pos = pipeline("token-classification", model="../../huggingface/models/roberta-base-bne-capitel-pos/", aggregation_strategy='max', device=0)

    for line in data:
        title = line['title']
        content = line['content']
        line['title'] = transform_pos(title, pos)
        line['content'] = transform_pos(content, pos)

    with open(args.output, 'w') as o:
        for line in data:
            o.write(json.dumps(line))
            o.write('\n')

if __name__ == "__main__":
    main()