#!/bin/bash
# Launch DESI DR1 Full-Scale GPU Inference
#
# Pod requirements:
#   GPU: A100 or H100 (40GB+ VRAM)
#   CPU: 16+ cores (for data loading)
#   RAM: 64+ GB (for large coadd files)
#   Disk: 200 GB (for temp files + outputs)
#   Network: Fast (downloading ~TB of data)
#
# Estimated runtime: 3-5 days
# Estimated cost: $200-350 ($3-4/hr for A100)

echo "=== DESI DR1 GPU Inference Setup ==="

# 1. Install dependencies
pip install torch torchvision healpy astropy scipy scikit-learn requests

# 2. Download the trained model from HuggingFace
mkdir -p /workspace/desi_dr1/{outputs,temp,model}
cd /workspace/desi_dr1
wget -q https://huggingface.co/bamfai/desi-spectral-anomaly-detector/resolve/main/best_model_47k.pt -O model/best_model_47k.pt
echo "Model downloaded"

# 3. Copy the inference script
# (copy 13_desi_dr1_gpu_inference.py to /workspace/desi_dr1/)

# 4. Run inference
python -u 13_desi_dr1_gpu_inference.py \
    --model-path model/best_model_47k.pt \
    --output-dir outputs \
    --temp-dir temp \
    --threshold 5.0 \
    --batch-size 8192

# 5. After completion, backup results
echo "Results saved to outputs/dr1_full_anomaly_catalog.json"
echo "Upload to HuggingFace:"
echo "  huggingface-cli upload bamfai/desi-spectral-anomaly-detector outputs/dr1_full_anomaly_catalog.json"
