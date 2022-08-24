#!/usr/bin/env bash

sbatch train_title_balanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/beto' beto
sbatch train_title_unbalanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/beto' beto

sbatch train_title_summary_balanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/beto' beto
sbatch train_title_summary_unbalanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/beto' beto

sbatch train_title_balanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-large' bne-large
sbatch train_title_unbalanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-large' bne-large

sbatch train_title_summary_balanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-large' bne-large
sbatch train_title_summary_unbalanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-large'  bne-large

sbatch train_title_balanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/mbert' mbert
sbatch train_title_unbalanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/mbert' mbert

sbatch train_title_summary_balanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/mbert' mbert
sbatch train_title_summary_unbalanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/mbert' mbert

sbatch train_title_balanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-base' bne-base
sbatch train_title_unbalanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-base' bne-base

sbatch train_title_summary_balanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-base' bne-base
sbatch train_title_summary_unbalanced.sh '/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-base' bne-base