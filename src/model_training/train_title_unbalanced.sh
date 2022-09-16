#!/bin/bash
#SBATCH --job-name="bne-controversy"
#SBATCH -D .
#SBATCH --output=./slurm_logs/$2-controversy_title_unbalanced-%j.out
#SBATCH --error=./slurm_logs/$2-controversy_title_unbalanced-%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres gpu:4
#SBATCH --cpus-per-task=160
#SBATCH --time=0-6:00:00

source ../clara/use_env.sh

SEED=1
NUM_EPOCHS=20
BATCH_SIZE=4
LEARN_RATE=0.000008
WARMUP=0.06
WEIGHT_DECAY=0.01

MODEL=$1
OUTPUT_DIR='./output'
LOGGING_DIR='./tb'
CACHE_DIR='/gpfs/projects/bsc88/projects/meneame_controversy/cache'
DIR_NAME=$2_'controversy_title_unbalanced'_${BATCH_SIZE}_${WEIGHT_DECAY}_${LEARN_RATE}_$(date +"%m-%d-%y_%H-%M")

export MPLCONFIGDIR=$CACHE_DIR/$DIR_NAME/matplotlib
export HF_HOME=$CACHE_DIR/$DIR_NAME/huggingface
rm -rf $MPLCONFIGDIR

python ./run_glue.py --model_name_or_path $MODEL --seed $SEED \
					  --dataset_script_path ./hf_wrapper/controversy_title_unbalanced.py \
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
