#!/bin/bash
#SBATCH --job-name="bne-controversy"
#SBATCH -D .
#SBATCH --output=./slurm_logs/bne-controversy_title_unbalanced-%j.out
#SBATCH --error=./slurm_logs/bne-controversy_title_unbalanced-%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres gpu:4
#SBATCH --cpus-per-task=160
#SBATCH --time=0-6:00:00

module load gcc/8.3.0 cuda/10.2 cudnn/7.6.4 nccl/2.4.8 tensorrt/6.0.1 openmpi/4.0.1 \
			atlas/3.10.3 scalapack/2.0.2 fftw/3.3.8 szip/2.1.1 ffmpeg/4.2.1 opencv/4.1.1 \
			python/3.7.4_ML arrow/3.0.0 text-mining/2.0.0 torch/1.9.0a0 torchvision/0.11.0

source /gpfs/projects/bsc88/projects/bne/eval_cte/venv/bin/activate

SEED=1
NUM_EPOCHS=5
BATCH_SIZE=4
LEARN_RATE=0.00003
WARMUP=0.06
WEIGHT_DECAY=0.01

MODEL='/gpfs/projects/bsc88/projects/bne/eval_cte/models/bne-base'
OUTPUT_DIR='./output'
LOGGING_DIR='./tb'
CACHE_DIR='/gpfs/scratch/bsc88/bsc88882/cache_bne-base'
DIR_NAME='controversy_title_unbalanced'_${BATCH_SIZE}_${WEIGHT_DECAY}_${LEARN_RATE}_$(date +"%m-%d-%y_%H-%M")

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
					  --metric_for_best_model accuracy --evaluation_strategy epoch --load_best_model_at_end
