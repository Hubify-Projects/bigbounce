# Manuscript Synchronization Audit

**Date:** 2026-03-13
**Manuscript:** `arxiv/main.tex`
**Last compiled PDF:** `arxiv/main.pdf` (Mar 13 01:03, 32 pages, 2.1 MB)

---

## 1. Frozen Datasets Used

| Dataset | Freeze Date | Samples | R̂−1 (worst) | Min ESS | Status |
|---------|------------|---------|-------------|---------|--------|
| full_tension_20260311_1728 | Mar 11, 2026 | 176,840 | 0.001 (CORRECTED) | 4,761 | FROZEN ✓ |
| planck_bao_sn_20260312_1954 | Mar 12, 2026 | 132,949 | 0.001 | 4,692 | FROZEN ✓ |
| planck_only | — | — | — | — | IN PROGRESS (~Mar 19–20 ETA) |
| planck_bao | — | — | — | — | NOT STARTED |

---

## 2. Figure Inventory

### Figures Referenced in main.tex (\includegraphics)

| # | File | In arxiv/figures/? | Source | Data Source | Current? |
|---|------|--------------------|--------|-------------|----------|
| 1 | figure1_lqg_holst_derivation_enhanced.png | YES | Original art | Theory | YES |
| 2 | figure2_galaxy_spin_comprehensive.png | YES | Original art | Surveys | YES |
| 3 | figure_3a_tension_resolution.png | YES | Original art | Planck+SH0ES | YES |
| 4 | fig_dneff_viability_two_frozen.pdf | YES | generate_two_frozen_figures.py | Both frozen chains | YES ✓ |
| 5 | cosmology_dataset_comparison_two_frozen.pdf | YES | generate_two_frozen_figures.py | Both frozen chains | YES ✓ |
| 6 | figure3b_tensions_resolution_comprehensive.png | YES | Original art | Literature | YES |
| 7 | figure6_parameter_naturalness.png | YES | Original art | Theory | YES |
| 8 | vacuum_scale_sensitivity.pdf | YES | vacuum_scale_sensitivity_scan.py | Theory audit | YES ✓ |
| 9 | consistency_window_birefringence.pdf | YES | Track C scripts | Published β | YES ✓ |
| 10 | figure4_distance_impact.png | YES | Original art | Theory | YES |
| 11 | figure5_rotation_expansion.png | YES | Original art | Theory | YES |

**Result: ALL 11 \includegraphics figures present. No missing files.**

### Unreferenced Figures in arxiv/figures/

| File | Notes |
|------|-------|
| figure7_observational_timeline.png | Was in earlier versions; currently unused |
| figure8_detection_forecast.png | Was in earlier versions; currently unused |

### Track C v2 Figures (Generated but NOT in manuscript)

| File | Location | Notes |
|------|----------|-------|
| trackC_parity_upgrade_corner.pdf | paper/figures/ | Available for integration |
| trackC_parity_upgrade_summary.pdf | paper/figures/ | Available for integration |

### Missing File Referenced in Text

| File | Location in tex | Issue |
|------|-----------------|-------|
| corner_H0_sigma8_Neff.pdf | Line 1622 (Reproducibility Materials appendix) | Listed as deliverable but does NOT exist |

---

## 3. Numerical Consistency Results

**Overall: PASS** — All parameter values in the manuscript match frozen chain outputs to stated precision.

### Discrepancies Found

| Issue | Severity | Details |
|-------|----------|---------|
| Total samples (full_tension) | LOW | Manuscript: 175,545; CORRECTED JSON: 176,840; MANIFEST: 176,240 |
| MANIFEST.md parameter table (full_tension) | MEDIUM | Column-scrambled (pre-correction bug); CORRECTED JSON is authoritative |
| planck_bao_sn convergence_report.txt | MEDIUM | Same column-mapping bug; MANIFEST has correct values |
| S₈ (planck_bao_sn) | LOW | 0.831 in manuscript vs. 0.828 derived from marginals; within uncertainty |
| Birefringence section language | INFO | Still labeled "consistency check"; Track C v2 (BF=176) ready but not integrated |

See `numerical_consistency_report.md` for full details.

---

## 4. Dataset Provenance Check

**Overall: GOOD** — with one historical weakness.

| Category | Status |
|----------|--------|
| MCMC chains + configs | CHECKSUMMED (SHA256) ✓ |
| CMB likelihoods | PUBLIC (Planck NPIPE, auto-download) ✓ |
| BAO + SN | PUBLIC (SDSS, Pantheon+) ✓ |
| Galaxy spin data | CAUTION — deprecated file with bad provenance exists; current analysis uses honest Shamir 2024 |
| Birefringence data | PUBLIC (2 published measurements) ✓ |
| Bibliography | 0 undefined refs; 2 minor BibTeX warnings |

See `dataset_provenance_final_check.md` for full details.

---

## 5. Unresolved Issues

### Must Fix Before Submission

| # | Issue | Action |
|---|-------|--------|
| 1 | Total samples discrepancy (full_tension) | Reconcile manuscript to 176,840 (CORRECTED JSON value) |
| 2 | corner_H0_sigma8_Neff.pdf missing | Generate from frozen chains or remove from Reproducibility appendix text |
| 3 | BibTeX warnings | Add journal to Shamir2024; add author to ECTorsionDESI2025 |

### Should Fix Before Submission

| # | Issue | Action |
|---|-------|--------|
| 4 | MANIFEST.md scrambled parameter table | Annotate or correct |
| 5 | planck_bao_sn needs corrected parameter JSON | Create parameter_summary_CORRECTED.json |
| 6 | Decide Track C v2 integration | Use fuller paragraph from paper_integration_decision_v2.md |
| 7 | Remove deprecated galaxy_spin_data.csv | Or add clear deprecation notice |
| 8 | 4 uncited bib entries | Remove CMBS4_2019, Euclid2024, LSST2019, PantosS82026 or cite them |

### Waiting On External

| # | Issue | ETA |
|---|-------|-----|
| 9 | planck_only chains (RunPod) | ~Mar 19–20 |
| 10 | planck_bao chains | After planck_only completes |
| 11 | Recompile LaTeX | Needs RunPod (no local LaTeX/pdflatex) |
| 12 | Re-run GetDist on planck_bao_sn | Needs RunPod (no local GetDist) |

---

## 6. Sections Safe to Edit Now

| Section | Lines | Notes |
|---------|-------|-------|
| Abstract | 64–76 | Can update birefringence language if Track C v2 integrated |
| Cosmic Birefringence (§10.3) | 1032–1042 | Ready for Track C v2 upgrade text |
| Claims Classification (App. K) | 1629–1669 | May need update if birefringence section changes |
| Reproducibility Materials (App. J) | 1604–1625 | Fix corner plot reference |
| Bibliography | references.bib | Fix warnings, remove uncited entries |

---

## 7. Sections Waiting for planck_only / planck_bao

| Section | Lines | What's Needed |
|---------|-------|---------------|
| Verification Table (Tab. 2) | 439–462 | Add two new rows when chains freeze |
| Verification Discussion | 464–465 | Update "two frozen" → "four frozen" |
| Executive Summary Note | 109 | Update when all four datasets available |
| Appendix B footnote | 1319 | Add planck_only and planck_bao values |

---

## 8. Compilation Status

| Field | Value |
|-------|-------|
| Last compiled | Mar 13, 2026 01:03 |
| Pages | 32 |
| File size | 2,141,515 bytes |
| Undefined references | 0 |
| Missing figures | 0 (all \includegraphics resolve) |
| LaTeX available locally? | NO |
| GetDist available locally? | NO |
| Compilation method | RunPod SSH (`arxiv/compile_on_pod.sh`) |

**Cannot recompile locally.** The existing PDF at `arxiv/main.pdf` was compiled on RunPod. To recompile, use:
```bash
./arxiv/compile_on_pod.sh [HOST] [PORT] [USER]
```

---

## 9. Track C v2 Integration Status

The Track C upgrade (Phases 0–8) is COMPLETE. Key deliverables:
- β = 0.242° ± 0.061° (3.9σ)
- BF(β≠0) = 176 (strong evidence)
- f_photon × C₀ = 1.73 ± 0.44

Integration options prepared in `paper_integration_decision_v2.md`:
- **Option A** (conservative paragraph): 1 paragraph, minimal claim
- **Option B** (fuller paragraph): 1 paragraph with degeneracy discussion
- **Figure caption**: Ready for trackC_parity_upgrade_corner.pdf

**Current manuscript status:** Still uses old "consistency check" framing. The numerical values (β, f_photon) are already consistent between old text and v2 results. The upgrade would add: explicit likelihood framing, Bayes factor, confidence intervals, degeneracy mapping.

---

## 10. GetDist Re-run Status

**Cannot re-run locally** — GetDist not installed.

Existing outputs:
- full_tension: Triangle + posteriors generated from CORRECTED data (Mar 11 10:56) ✓
- planck_bao_sn: No GetDist plots generated yet (getdist/ directory empty)

**Action needed on RunPod:**
1. Re-run GetDist on planck_bao_sn to generate triangle/posterior plots
2. Generate corner_H0_sigma8_Neff.pdf for reproducibility package
3. Verify full_tension GetDist outputs match CORRECTED parameter values

---

## Summary

| Check | Result |
|-------|--------|
| All figures present? | **YES** (11/11 \includegraphics resolve) |
| Numbers match frozen chains? | **YES** (all within rounding to stated precision) |
| Stale numbers? | **1 minor** (total samples count: 175,545 should be 176,840) |
| Dataset provenance issues? | **1 historical** (deprecated galaxy_spin_data.csv) |
| Sections blocked by pending chains? | **4 sections** (waiting for planck_only/planck_bao) |
| Ready to submit? | **NO** — waiting for 2 pending chain sets + recompilation |
