from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig, pipeline
import shap

INPUT_PATH = '../models/title'
if __name__ == '__main__':
    model = AutoModelForSequenceClassification.from_pretrained(INPUT_PATH)
    tokenizer = AutoTokenizer.from_pretrained(INPUT_PATH)
    config = AutoConfig.from_pretrained(INPUT_PATH)
    pipeline = pipeline('text-classification', model=model, tokenizer=tokenizer, config=config, return_all_scores=True)
    explainer = shap.Explainer(pipeline)
    shap_values = explainer(["Esto es una prueba"])
