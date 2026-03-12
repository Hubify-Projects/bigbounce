#!/bin/bash
set -euo pipefail
# BigBounce P7 CNN Spin Classifier — Reproducible Training Pipeline
# Run from: research/paper2/p7_cnn_spin_classifier/

RUN_ID=$(date +%Y%m%d_%H%M)_p7_cnn

echo "=== BigBounce P7 CNN Spin Classifier ==="
echo "=== Run ID: ${RUN_ID} ==="
echo ""

echo "=== Step 1: Build dataset ==="
python dataset_build_sdss_gz.py --max_galaxies 10000 --output_dir data/ --seed 42

echo ""
echo "=== Step 2: Train model ==="
python train_resnet18.py --data_dir data/ --output_dir "runs/${RUN_ID}/" --epochs 30 --seed 42

echo ""
echo "=== Step 3: Bias audits ==="
python eval_bias_audits.py --model_path "runs/${RUN_ID}/model.pt" --data_dir data/ --output_dir "runs/${RUN_ID}/audits/"

echo ""
echo "=== Step 4: Inference + dipole fit ==="
python infer_and_dipole_fit.py --model_path "runs/${RUN_ID}/model.pt" --data_dir data/ --output_dir "runs/${RUN_ID}/dipole/"

echo ""
echo "=== Done: all outputs in runs/${RUN_ID}/ ==="
echo "  model.pt              — best model weights"
echo "  training_curves.json  — loss/accuracy per epoch"
echo "  confusion_matrix.png  — test set confusion matrix"
echo "  audits/               — bias audit report + plots"
echo "  dipole/               — dipole fit + sky map"
