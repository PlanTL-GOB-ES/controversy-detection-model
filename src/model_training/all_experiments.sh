

sbatch train_models.sh 'bne-base' 'controversy_title_balanced'
sbatch train_models.sh 'bne-base' 'controversy_title_summary_balanced'
sbatch train_models.sh 'bne-base' 'or_controversy_title_summary_unbalanced'
sbatch train_models.sh 'bne-base' 'or_controversy_title_unbalanced'

sbatch train_models.sh 'bne-base' 'no_ents_title'
sbatch train_models.sh 'bne-base' 'no_ents_title_summary'

sbatch train_models.sh 'mbert' 'or_controversy_title_summary_unbalanced'
sbatch train_models.sh 'mbert' 'or_controversy_title_unbalanced'

sbatch train_models.sh 'beto' 'or_controversy_title_summary_unbalanced'
sbatch train_models.sh 'beto' 'or_controversy_title_unbalanced'