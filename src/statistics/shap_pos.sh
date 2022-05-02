#!/bin/bash
##----------------------- Start job description -----------------------
#SBATCH --job-name=shap
#SBATCH --time=72:00:00
#SBATCH --output=./shap_compute_%j.out
#SBATCH --error=./shap_compute_%j.err
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=42G
#SBATCH --partition=standard-gpu
#SBATCH --gres=gpu:a100:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=asierguti96@gmail.com
##------------------------ End job description ------------------------

module purge
module load PyTorch/1.9.0-fosscuda-2020b

/home/t561/t561102/contro/bin/python ./statistics/shap_pos.py
