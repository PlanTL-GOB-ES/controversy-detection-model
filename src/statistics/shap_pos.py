from transformers import AutoModelForTokenClassification, AutoTokenizer, AutoConfig, pipeline

POS_MODEL = 'PlanTL-GOB-ES/roberta-base-bne-capitel-pos'
if __name__ == '__main__':
    model = AutoModelForTokenClassification.from_pretrained(POS_MODEL)
    tokenizer = AutoTokenizer.from_pretrained(POS_MODEL)
    config = AutoConfig.from_pretrained(POS_MODEL)
    pipeline = pipeline('token-classification', model=model, tokenizer=tokenizer, config=config)
    pass