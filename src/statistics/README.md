
### Calculate corpus statistics

```
python comment_correlation.py

python likes_dislikes_correlation.py 

python media_cooccurrence.py

python tag_cooccurrence.py

python topic_cooccurrence.py
```

### Extract SHAP values:

```
python shap_compute_all.py --model output/no_ents_title_summary \
                           --input shap_all/original_balanced.jsonl \
                           --output shap_all/no_ents/shap_values.jsonl
                           
python shap_compute_all.py --model output/title_summary_unbalanced \
                           --input shap_all/original_balanced.jsonl \
                           --output shap_all/ents/shap_values.jsonl
                           
python shap_compute_all.py --model output/no_ents_title_summary \
                           --input shap_all/no_ents_balanced.jsonl \
                           --output shap_all/no_ents/no_ents_test_shap_values.jsonl
```

### Aggregate by POS

```
python src/statistics/shap_pos.py  \
                   --input_path data/shap_all/no_ents/shap_values.jsonl \
                   --output_path data/shap_all/no_ents/
                   
python src/statistics/shap_pos.py \
                   --input_path data/shap_all/no_ents/no_ents_test_shap_values.jsonl \
                   --output_path data/shap_all/no_ents/no_ents_test_

python src/statistics/shap_pos.py \
                   --input_path data/shap_all/ents/shap_values.jsonl \
                   --output_path data/shap_all/ents/
```

### Experiments with no proper nouns

```
python shap_compute_all.py --model output/no_propn_title_summary \
                           --input shap_all/original_balanced.jsonl \
                           --output shap_all/no_propn/shap_values.jsonl
                           
python shap_compute_all.py --model output/no_propn_title_summary \
                           --input shap_all/no_propn_balanced.jsonl \
                           --output shap_all/no_propn/no_propn_test_shap_values.jsonl
                           
python src/statistics/shap_pos.py  \
                   --input_path data/shap_all/no_propn/shap_values.jsonl \
                   --output_path data/shap_all/no_propn/
                   
python src/statistics/shap_pos.py \
                   --input_path data/shap_all/no_propn/no_propn_test_shap_values.jsonl \
                   --output_path data/shap_all/no_propn/no_propn_test_
```

### Compare results: 
```
python src/statistics/analyze_pos.py

python src/statistics/word_analysis.py
```