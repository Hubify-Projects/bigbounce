# Model Card: Galaxy Spin ResNet-18 Classifier

## Model Details

- **Name**: BigBounce P7 Galaxy Spin Classifier
- **Architecture**: ResNet-18 (He et al., 2016, arXiv:1512.03385)
- **Pretraining**: ImageNet (torchvision default weights)
- **Final layer**: FC -> 2 classes (CW, CCW)
- **Input**: 128x128 RGB galaxy image (JPEG)
- **Output**: Softmax probabilities [P(CW), P(CCW)]
- **Framework**: PyTorch

## Training Data

- **Source**: Galaxy Zoo DECaLS volunteer classifications (Walmsley et al. 2022)
- **Images**: SDSS DR17 color composite cutouts (128x128 pixels, 0.4 arcsec/pixel scale)
- **Selection**: Spiral galaxies with confident handedness votes
  - Featured/disk fraction > 0.5
  - Has spiral arms fraction > 0.5
  - CW: clockwise fraction > 0.6
  - CCW: anticlockwise fraction > 0.6
- **Balance**: Equal CW and CCW counts
- **Split**: 70% train / 15% val / 15% test (fixed seed=42)

## Classes

| Class | Label | Description |
|-------|-------|-------------|
| 0     | CW    | Clockwise spiral winding |
| 1     | CCW   | Counter-clockwise spiral winding |

## Training Procedure

- **Optimizer**: AdamW (lr=1e-4, weight_decay=1e-4)
- **Scheduler**: CosineAnnealingLR (T_max=epochs)
- **Loss**: CrossEntropyLoss with label smoothing (0.1)
- **Epochs**: 30 (configurable)
- **Batch size**: 64

### Data Augmentation

- Random horizontal flip (p=0.5)
- Random rotation (up to 15 degrees)
- Color jitter (brightness=0.2, contrast=0.2)
- Resize to 144 then random crop to 128
- **Parity augmentation** (p=0.5): Mirror image AND flip label (CW <-> CCW).
  This enforces the physical equivariance that mirror images have opposite chirality.

### Normalization

ImageNet statistics: mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]

## Evaluation Metrics

- Validation accuracy (used for model selection)
- Test accuracy, precision, recall, F1 per class
- Confusion matrix

## Bias Audits

Four mandatory bias tests are run after training:

| Test | Description | Target |
|------|-------------|--------|
| Mirror Test | Predict on L-R mirrored images; should predict opposite class | >90% flip rate |
| Rotation Test | Predict on 180-deg rotated images; chirality should not change | <20% flip rate |
| PSF Proxy Test | Correlate P(CW) with PSF/seeing; should show no correlation | p > 0.05 |
| Balanced Null Test | Predict on elliptical galaxies; should give ~50/50 CW/CCW | 50% within 95% CI |

## Limitations

- **Label noise**: Galaxy Zoo labels are crowdsourced volunteer votes, not ground-truth measurements. Vote fractions represent consensus, not physical certainty.
- **Imaging systematics**: Trained exclusively on SDSS imaging. PSF variations, sky background, and CCD artifacts may introduce systematic biases.
- **Band dependence**: SDSS color composites use g/r/i bands. Morphological features may appear different in other bandpasses.
- **Redshift range**: Galaxy Zoo DECaLS galaxies are predominantly at z < 0.3. Performance at higher redshifts is untested.
- **Angular resolution**: 128x128 pixels at 0.4"/pixel covers ~51" x 51". Very extended or very compact galaxies may be poorly represented.
- **Face-on bias**: Spiral arm winding direction is most visible for face-on galaxies. Edge-on and highly inclined spirals are difficult to classify and may be misrepresented in training data.

## Intended Use

- Pipeline development for galaxy spin asymmetry surveys
- Testing bias audit methodologies for astronomical classifiers
- Educational demonstration of CNN-based morphological classification

## NOT Intended For

- Direct cosmological inference without further systematic characterization
- Replacement of detailed morphological catalogs (e.g., Galaxy Zoo, GalaxyMorphology)
- Classification of non-SDSS imaging without domain adaptation

## Ethical Considerations

- Crowdsourced labels may contain systematic biases related to volunteer demographics or interface design
- The Galaxy Zoo project involved hundreds of thousands of volunteers whose individual contributions are not tracked by this pipeline
- Any cosmological claims derived from this classifier must account for all systematic effects documented in the bias audits

## Citation

If using this model or pipeline, cite:

- Galaxy Zoo DECaLS: Walmsley et al. (2022), MNRAS 509, 3966
- ResNet: He et al. (2016), "Deep Residual Learning for Image Recognition", CVPR
- SDSS DR17: Abdurro'uf et al. (2022), ApJS 259, 35
