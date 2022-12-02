import json
from transformers import AutoModelForTokenClassification, AutoTokenizer
from custom_ner import CustomNerPipeline
from pprint import pprint
import argparse
import re

def transform_ner(text, model):
    entities = model(text)
    if entities:
        for entity in entities:
            if entity['entity'] in ['LOC', 'PER', 'ORG']:
                text = re.sub(re.escape(entity['word']), ' '+entity['entity'], text)
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

    # import model and tokenizer
    model = AutoModelForTokenClassification.from_pretrained(
        "PlanTL-GOB-ES/roberta-base-bne-capitel-ner-plus")
    tokenizer = AutoTokenizer.from_pretrained("PlanTL-GOB-ES/roberta-base-bne-capitel-ner-plus")

    # create the pipeline
    ner = CustomNerPipeline(model, tokenizer)  #, device=0)

    for line in data:
        title = line['title']
        content = line['content']
        line['title'] = transform_ner(title, ner)
        line['content'] = transform_ner(content, ner)

    with open(args.output, 'w') as o:
        for line in data:
            o.write(json.dumps(line))
            o.write('\n')

if __name__ == "__main__":
    main()