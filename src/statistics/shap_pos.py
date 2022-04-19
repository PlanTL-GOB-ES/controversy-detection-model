from transformers import AutoModelForTokenClassification, AutoTokenizer, AutoConfig, pipeline
from collections import defaultdict

def load_pos_pipeline(dir):
    model = AutoModelForTokenClassification.from_pretrained(dir)
    tokenizer = AutoTokenizer.from_pretrained(dir)
    config = AutoConfig.from_pretrained(dir)
    return pipeline('token-classification', model=model, tokenizer=tokenizer, config=config, aggregation_strategy='max')

POS_MODEL = 'PlanTL-GOB-ES/roberta-base-bne-capitel-pos'
if __name__ == '__main__':

    pos_pipeline = load_pos_pipeline(POS_MODEL)

    from transformers import AutoModelForSequenceClassification
    import shap
    INPUT_PATH = '../models/title'
    model = AutoModelForSequenceClassification.from_pretrained(INPUT_PATH)
    tokenizer = AutoTokenizer.from_pretrained(INPUT_PATH)
    config = AutoConfig.from_pretrained(INPUT_PATH)
    pipeline = pipeline('text-classification', model=model, tokenizer=tokenizer, config=config, return_all_scores=True)
    explainer = shap.Explainer(pipeline)

    pos = pos_pipeline(["Meter el título y -- el resumen"])[0]
    contr = explainer(["Meter el título y -- el resumen"])
    contr.values[0, 1:-1]

    pos = [defaultdict(int, element) for element in pos]
    start = 0
    for word, value in zip(contr.data[0], contr.values[0, :, 0]):
        if word:
            end = start + len(word) - 1
            for entity in pos:
                e_start, e_end = entity['start'], entity['end']
                if start >= e_start and start < e_end and end > e_start and end <= e_end:
                    print(word, entity['word'])
                    entity['value'] = entity['value'] + value
            start = end + 1
