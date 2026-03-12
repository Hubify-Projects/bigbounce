# P7 CNN Spin Classifier

**BigBounce Paper 2 — Track C: Galaxy Spin Classification Pipeline**

## Objective

Build a reproducible ResNet-18 classifier for CW (clockwise) / CCW (counter-clockwise)
galaxy spin from SDSS images, with mandatory bias audits (mirror, rotation, PSF, balanced null).

The classifier is a pipeline development exercise for quantifying galaxy spin asymmetries.
It is NOT intended for direct cosmological inference without further systematic characterization.

## Success Criteria

| Test                | Target                         |
|---------------------|--------------------------------|
| Test set accuracy   | > 60%                          |
| Mirror test         | > 90% flip rate                |
| Rotation test       | < 20% flip rate                |
| Balanced null       | ~50/50 CW/CCW (within 95% CI) |

## Datasets

- **Labels**: Galaxy Zoo DECaLS catalog (public CSV from Zenodo)
- **Images**: SDSS DR17 imaging cutouts (128x128 color composite)
- **Fallback**: Synthetic spiral images for testing pipeline functionality when SDSS
  downloads are slow or blocked (clearly marked SYNTHETIC - NOT FOR SCIENCE)

## Pipeline Overview

```
dataset_build_sdss_gz.py   -->  data/{images/, catalog.csv}
train_resnet18.py          -->  runs/RUN_ID/{model.pt, training_curves.json, ...}
eval_bias_audits.py        -->  runs/RUN_ID/audits/{bias_audit_report.json, ...}
infer_and_dipole_fit.py    -->  runs/RUN_ID/dipole/{dipole_fit.json, skymap.png, ...}
```

## Outputs

- Trained model weights (`model.pt`)
- Confusion matrix and classification report
- Training curves (loss/accuracy per epoch)
- Bias audit report (JSON + human-readable text)
- Bias audit plots (mirror histogram, rotation histogram, null bar chart)
- Calibration plots
- Toy dipole fit results and sky map
- Dataset manifest with SHA256 hash

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run full pipeline (dataset build, training, audits, dipole fit)
bash reproduce_training.sh

# Or run steps individually:
python dataset_build_sdss_gz.py --max_galaxies 10000 --output_dir data/ --seed 42
python train_resnet18.py --data_dir data/ --output_dir runs/dev/ --epochs 30 --seed 42
python eval_bias_audits.py --model_path runs/dev/model.pt --data_dir data/ --output_dir runs/dev/audits/
python infer_and_dipole_fit.py --model_path runs/dev/model.pt --data_dir data/ --output_dir runs/dev/dipole/
```

## File Manifest

| File                         | Purpose                                       |
|------------------------------|-----------------------------------------------|
| `README.md`                  | This file                                     |
| `dataset_build_sdss_gz.py`   | Build training dataset from GZ + SDSS         |
| `train_resnet18.py`          | Train ResNet-18 with parity augmentation      |
| `eval_bias_audits.py`        | 4 mandatory bias audits                       |
| `infer_and_dipole_fit.py`    | Inference + toy dipole fit                    |
| `model_card.md`              | Standard ML model card                        |
| `reproduce_training.sh`      | One-command reproducible pipeline             |
| `requirements.txt`           | Pinned Python dependencies                    |

## References

- Galaxy Zoo DECaLS: Walmsley et al. (2022), MNRAS 509, 3966
- ResNet: He et al. (2016), arXiv:1512.03385
- SDSS DR17: Abdurro'uf et al. (2022), ApJS 259, 35
