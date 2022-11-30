#!/bin/bash
#SBATCH --job-name="bne-controversy"
#SBATCH -D .
#SBATCH --output=./slurm_logs/controversy-%j.out
#SBATCH --error=./slurm_logs/controversy-%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres gpu:2
#SBATCH --cpus-per-task=128
#SBATCH --time=0-6:00:00

source ../clara/use_env.sh

SEED=1
NUM_EPOCHS=5
BATCH_SIZE=4
LEARN_RATE=0.00005
WARMUP=0.06
WEIGHT_DECAY=0.01

MODEL=$1
DATA=$2
OUTPUT_DIR='./output'
LOGGING_DIR='./tb'
CACHE_DIR='/gpfs/projects/bsc88/projects/meneame_controversy/cache'
DIR_NAME=${MODEL}_${DATA}_${BATCH_SIZE}_${WEIGHT_DECAY}_${LEARN_RATE}_$(date +"%m-%d-%y_%H-%M")
SCRIPT='./run_glue.py'

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

python $SCRIPT --model_name_or_path '/gpfs/projects/bsc88/projects/bne/eval_cte/models/'${MODEL} --seed $SEED \
					  --dataset_script_path ./hf_wrapper/${DATA}.py \
					  --task_name cont --do_train --do_eval --do_predict \
					  --num_train_epochs $NUM_EPOCHS --per_device_train_batch_size $BATCH_SIZE \
					  --learning_rate $LEARN_RATE --warmup_ratio $WARMUP --weight_decay $WEIGHT_DECAY \
					  --output_dir $OUTPUT_DIR/$DIR_NAME --overwrite_output_dir \
					  --logging_dir $LOGGING_DIR/$DIR_NAME --logging_strategy epoch \
					  --cache_dir $CACHE_DIR/$DIR_NAME --overwrite_cache \
					  --save_strategy steps --save_steps 100 \
					  --evaluation_strategy steps --eval_steps 100 \
					  --logging_strategy steps --logging_steps 100 \
					  --metric_for_best_model f1 --load_best_model_at_end
