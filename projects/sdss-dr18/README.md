# SDSS DR18 Cross-Survey Validation

**Status:** Running (H200) | **Paper:** TBD | **Target:** ApJS

## Overview
Apply BigAE autoencoder (trained on DESI) to 5M SDSS DR18 spectra. Proves methodology is survey-independent. First cross-survey anomaly comparison.

## Goals
1. Score all 5M SDSS spectra with BigAE
2. Compare anomaly rate with DESI (1.10%)
3. Cross-match SDSS anomalies with DESI anomalies (overlapping sky)
4. Validate that same object types are flagged across surveys

## Status
- [x] Model uploaded to H200
- [x] SDSS spAll catalog downloaded (11.2GB)
- [ ] Spectrum processing in progress
- [ ] Anomaly catalog generation
- [ ] Cross-survey comparison
- [ ] Cross-match with DESI catalog

## Files
- Script: On H200 at `/workspace/bigbounce/sdss_dr18_scan.py`
- Model: `/workspace/bigbounce/best_model_47k.pt`
- Pod: `7zong4jdj46yjp` (H200 SXM, <pod-ip>:<port>)

## Cost
~$50 estimated
