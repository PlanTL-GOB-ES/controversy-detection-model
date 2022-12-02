

sbatch train_models.sh 'bne-base' 'controversy_title_balanced' 0.00001 5
sbatch train_models.sh 'bne-base' 'controversy_title_summary_balanced' 0.00001 5
sbatch train_models.sh 'bne-base' 'or_controversy_title_summary_unbalanced' 0.00001 5
sbatch train_models.sh 'bne-base' 'or_controversy_title_unbalanced' 0.00001 5

sbatch train_models.sh 'bne-base' 'no_ents_title' 0.00001 5
sbatch train_models.sh 'bne-base' 'no_ents_title_summary' 0.00001 5

sbatch train_models.sh 'mbert' 'or_controversy_title_summary_unbalanced' 0.00001 5
sbatch train_models.sh 'mbert' 'or_controversy_title_unbalanced' 0.00001 5

sbatch train_models.sh 'beto' 'or_controversy_title_summary_unbalanced' 0.00001 5
sbatch train_models.sh 'beto' 'or_controversy_title_unbalanced' 0.00001 5