#!/bin/bash
#SBATCH --job-name="meneame_controversy"
#SBATCH -D .
#SBATCH --output=slurm_logs/meneame_controversy_%j.out
#SBATCH --error=slurm_logs/meneame_controversy_%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=2-00:00:00
module load gcc
module load python/3.9.1
python controversy_take_sample.py
