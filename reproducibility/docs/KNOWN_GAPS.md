# Known Reproducibility Gaps

This document honestly discloses what CANNOT currently be reproduced from
the provided materials and how the paper text handles each gap.

## 1. No Bespoke CAMB Modifications

**What the paper describes:** A "modified CAMB v1.5" with a spin-torsion
Λ_eff(z) component and modified perturbation initial conditions.

**What actually exists:** The cosmological model is ΛCDM + ΔN_eff, which
uses standard CAMB parameters. No custom dark energy class was implemented.
The spin-torsion framework provides the *theoretical motivation* for nonzero
ΔN_eff, but the MCMC implementation uses stock CAMB.

**Paper handling:** The text describes the theory module as modifying CAMB
with "an additional early dark energy component" — this is implemented via
the standard N_eff parameter, not a custom code module.

## 2. No MCMC Chains Pre-Computed

**Status:** The Cobaya configurations are provided and can be run with
stock CAMB. Chains take ~4-12 hours per configuration on 4 CPU cores.
Pre-computed chains are not included due to file size (~1 GB per run).

**Workaround:** Run `reproduce_cosmology.sh` to generate chains.

## 3. No Bayes Factor Computation

**What the paper reports:** ln B values from nested sampling (PolyChord).

**What exists:** MCMC configs only. Nested sampling requires changing the
sampler block to PolyChord and is computationally more expensive (~10x).

**Paper handling:** Bayes factors are reported with explicit caveats about
dataset dependence.

## 4. No CNN Galaxy Spin Classifier

**What the paper describes:** A ResNet-18 CNN trained on Galaxy Zoo labels
with parity augmentation.

**What exists:** The hierarchical Bayesian fit code (Stan) + published
CW/CCW count data. No CNN training/inference code.

**Paper handling:** The CNN is described as part of the classification
methodology. The actual fit uses published catalogs, not CNN outputs.

## 5. No CMB EB/TB Analysis from Maps

**What the paper describes:** Power spectrum estimation from Planck HFI
data using SMICA.

**What exists:** No Planck map processing code. All birefringence values
are literature citations.

**Paper handling:** Updated to cite Minami & Komatsu (2020) and Eskilt
(2022) as the source of β values, not original analysis.
