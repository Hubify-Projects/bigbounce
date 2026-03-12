# P7 CNN Spin Classifier — Run Manifest

## Track
Paper 2, Track C (P7)

## Framing
Pipeline and data product project for galaxy spin classification.
This is NOT a cosmological measurement. The classifier is a technical
demonstration of bias-audited CNN-based morphological classification.

## Run Environment
- Pod: paper2-p7-cnn (RunPod, RTX 3090 community)
- Image: runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04
- Python: 3.10
- Dependencies: torch, torchvision, numpy, scipy, matplotlib, pandas,
  Pillow, requests, scikit-learn (see requirements.txt)

## Datasets Used
| Dataset | Source | Access |
|---------|--------|--------|
| Galaxy Zoo DECaLS | Zenodo: 4573248 | CC-BY-4.0, ~500 MB CSV |
| SDSS DR17 cutouts | skyserver.sdss.org | Public, rate-limited 2 req/s |
| Synthetic fallback | Generated locally | For pipeline testing only |

## Commands
```bash
bash reproduce_training.sh
# Or individually:
python dataset_build_sdss_gz.py --max_galaxies 10000 --output_dir data/
python train_resnet18.py --data_dir data/ --output_dir runs/dev/ --epochs 30
python eval_bias_audits.py --model_path runs/dev/model.pt --data_dir data/ --output_dir runs/dev/audits/
python infer_and_dipole_fit.py --model_path runs/dev/model.pt --data_dir data/ --output_dir runs/dev/dipole/
```

## Outputs
- data/: catalog.csv, images/, manifest.json
- runs/dev/: model.pt, training_curves.json, confusion_matrix.png
- runs/dev/audits/: bias_audit_report.json, mirror/rotation/null plots
- runs/dev/dipole/: dipole_fit.json, sky maps (DISCLAIMER: not cosmological)

## Limitations
- Label noise from crowdsourced Galaxy Zoo votes
- SDSS imaging systematics (PSF, sky background, CCD artifacts)
- Trained at z < 0.3 only; higher-z performance unknown
- The dipole fit is a technical demonstration, NOT a cosmological measurement
- Any scientific dipole claim requires full systematic characterization beyond
  the 4 bias audits implemented here
