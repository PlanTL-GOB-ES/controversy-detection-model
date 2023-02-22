#!/bin/bash
#SBATCH --job-name="bne-controversy"
#SBATCH -D .
#SBATCH --output=./slurm_logs/test-%j.out
#SBATCH --error=./slurm_logs/test-%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres gpu:2
#SBATCH --cpus-per-task=128
#SBATCH --time=0-6:00:00


CACHE_DIR='cache'
DIR_NAME=./output/$1
CHECKPOINT=$2
MODEL=$DIR_NAME/$CHECKPOINT
SCRIPT='./run_glue.py'
DATA=$3
OUT=$DIR_NAME/$CHECKPOINT/$4

#MODULE LOADING

if uname -a | grep -q amd
then
        module load cmake/3.18.2 gcc/10.2.0 rocm/5.1.1 mkl/2018.4 intel/2018.4 python/3.7.4
        source /gpfs/projects/bsc88/projects/catalan_evaluation/venv/bin/activate
        export LD_LIBRARY_PATH=/gpfs/projects/bsc88/external-lib:$LD_LIBRARY_PATH
else
        module load gcc/8.3.0 cuda/10.2 cudnn/7.6.4 nccl/2.4.8 tensorrt/6.0.1 openmpi/4.0.1 \
        atlas/3.10.3 scalapack/2.0.2 fftw/3.3.8 szip/2.1.1 ffmpeg/4.2.1 opencv/4.1.1 \
        python/3.7.4_ML arrow/3.0.0 text-mining/2.0.0 torch/1.9.0a0 torchvision/0.11.0
fi

echo $OUT

python $SCRIPT --model_name_or_path $MODEL\
					  --dataset_script_path ./hf_wrapper/${DATA}.py \
					  --task_name cont --do_predict \
					  --output_dir $OUT \
					  --evaluation_strategy steps --eval_steps 100