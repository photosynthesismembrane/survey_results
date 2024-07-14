#!/bin/bash
#SBATCH --time=0-23:59:00
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=v100
#SBATCH --job-name=evaluate
#SBATCH --mem=50G
module purge
module load CUDA/12.1.1
module load Python/3.11.3-GCCcore-12.3.0
module load GCCcore/12.3.0

source ../../venv/bin/activate

export HF_DATASETS_CACHE="/scratch/$USER/.cache/huggingface/datasets"
export HF_HOME="/scratch/$USER/.cache/huggingface/transformers"

pip install --upgrade pip
pip install torch torchvision
pip install diffusers
pip install transformers
pip install accelerate
pip install huggingface_hub

accelerate config default

huggingface-cli login --token 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

# python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_llava_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-llava-composition --model_name llava --task composition --generations_per_prompt 10
# python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_llava_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-llava-contrast --model_name llava --task contrast_elements --generations_per_prompt 10
# python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_llava_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-llava-focus --model_name llava --task focus_point --generations_per_prompt 10

python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_cogvlm_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-cogvlm-composition --model_name cogvlm --task composition --generations_per_prompt 10
python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_cogvlm_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-cogvlm-contrast --model_name cogvlm --task contrast_elements --generations_per_prompt 10
python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_cogvlm_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-cogvlm-focus --model_name cogvlm --task focus_point --generations_per_prompt 10

python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_deepseek_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-deepseek-composition --model_name deepseek --task composition --generations_per_prompt 10
python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_deepseek_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-deepseek-contrast --model_name deepseek --task contrast_elements --generations_per_prompt 10
python generate_images_from_prompts.py --js_file renaissance_evaluation_sample_deepseek_data.js --model_path /scratch/s1889338/diffusers/examples/text_to_image/renaissance-deepseek-focus --model_name deepseek --task focus_point --generations_per_prompt 10

deactivate
