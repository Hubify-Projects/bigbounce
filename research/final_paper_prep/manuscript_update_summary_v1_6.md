# Manuscript Update Summary: v1.6.0

**Date:** 2026-03-13
**Version:** v1.5.0 → v1.6.0

---

## What Changed

### 1. New Discussion Subsection: Cosmic Birefringence Consistency Check
- **Location:** Section 10 (Discussion), new subsection between "Theoretical Implications" and "Distance Measures and Rotation"
- **Content:** 2 paragraphs combining published Planck + ACT DR6 birefringence measurements (β = 0.24° ± 0.06°, 3.9σ) and translating to the framework's photon-torsion coupling: f_photon ≈ 1.7 ± 0.4
- **Figure:** New `consistency_window_birefringence.pdf` — f_photon vs β plot
- **Framing:** Explicitly labeled as "consistency check, not statistical inference"

### 2. New Future-Work Bullet: Primordial Power Spectrum Through the Bounce
- **Location:** Section 11.4 (Bounce-to-Inflation Transition Dynamics), new bullet point
- **Content:** States that with N_tot = 92, P(k) features appear at k ~ 10^15 Mpc^-1 (sub-asteroid-mass PBH scales); perturbation calculation needed
- **Framing:** No SMBH/PBH/JWST claims; correctly identifies asteroid-mass window

### 3. Claims Table Update
- New row: f_photon ≈ 1.7 classified as "Consistency check" (algebraic translation)

### 4. Conclusions Update
- Added sentence referencing the consistency check and f_photon ≈ 1.7

### 5. Version Bump
- v1.5.0 → v1.6.0 throughout (version tag, timestamp, Data & Code Availability URLs)

---

## What Remains Pending on planck_only / planck_bao

### planck_only
- **Status:** Running on RunPod (PIDs 8165-8170)
- **ETA:** ~March 19-20 for convergence (R̂-1 < 0.01)
- **Impact on manuscript:** Will fill [PENDING] markers in Table verification and update cross-dataset comparison

### planck_bao
- **Status:** Paused
- **Resume:** After planck_only freezes
- **Impact on manuscript:** Fourth and final dataset column in verification table

### After both freeze:
- Complete verification table with all 4 dataset columns
- Update abstract/conclusions with full quantitative summary
- Final version bump to v1.7.0 or v2.0.0

---

## Compilation Results

- **Pages:** 35
- **PDF size:** 2.1 MB
- **Undefined references:** 0
- **New figure:** 1 (consistency_window_birefringence.pdf)
- **BibTeX warnings:** 2 pre-existing (Shamir2024 missing journal, ECTorsionDESI2025 empty author)
- **Path:** `arxiv/main.pdf`

---

## Is the Paper Ready for External/Referee-Style Review?

**YES, with caveats.**

The paper is ready for a serious external scientific review on its current content. The Track C consistency check and early-structure future-work paragraph are cleanly integrated and properly caveated. The claims alignment audit passes on all 8 checks.

**Caveats:**
1. The verification table has 2 of 4 dataset columns filled (2 [PENDING]). A reviewer will note the incomplete table.
2. The planck_only and planck_bao results may shift some numbers (though the frozen full-tension and Planck+BAO+SN results establish the pattern).
3. A reviewer may ask about the gap between α/M and the galaxy spin amplitude A_0 — this is already disclosed as a known limitation.

**Recommendation:** Send for external review now, noting that the verification table will be completed with the remaining two MCMC datasets by ~March 25. The core theoretical framework, Track C consistency check, and honest limitations are all in final form.
