#!/usr/bin/env bash

sbatch train_title_balanced.sh
sbatch train_title_unbalanced.sh

sbatch train_title_summary_balanced.sh
sbatch train_title_summary_unbalanced.sh