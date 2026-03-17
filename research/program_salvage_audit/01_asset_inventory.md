# Asset Inventory: Full Repository Scientific Assets

**Date:** 2026-03-16

---

## Classification Key

- **A. STILL_ALIVE_AND_USEFUL** -- asset retains scientific value and can be deployed in a new program
- **B. DEAD_CLAIM_BUT_REUSABLE_INFRASTRUCTURE** -- the scientific claim is dead, but the code/pipeline/methodology is reusable
- **C. DEAD_AND_NOT_WORTH_REUSING** -- neither the claim nor the infrastructure is worth carrying forward

---

## 1. MCMC Pipeline (Cobaya + CAMB on RunPod)

**Location:** `reproducibility/cosmology/` (configs, chains, monitors), `research/paper2/wp4_dneff_microphysics/`

**What exists:**
- 4 Cobaya YAML configs: `cobaya_planck.yaml`, `cobaya_planck_bao.yaml`, `cobaya_planck_bao_sn.yaml`, `cobaya_full_tension.yaml`
- Frozen chain outputs: 176,840 samples (full-tension), 132,949 (Planck+BAO+SN), convergence R-1 < 0.005
- 64 chains across 4 dataset combinations
- Monitor scripts (v2-v5), convergence tracking CSVs, chain diagnostics
- RunPod deployment scripts (`runpod_cloud.py`, `runpod_gpu_session.py`)
- Delta-Neff microphysics scans (24,000 + 32,000 parameter-space rows)

**Classification: A. STILL_ALIVE_AND_USEFUL**

The MCMC infrastructure is the single most valuable reusable asset. It can constrain ANY Lambda-CDM extension with Delta-Neff or similar extra parameters. The configs, monitoring scripts, and RunPod deployment are directly reusable. The existing chains provide baseline Lambda-CDM+Neff posteriors against which any new model can be compared.

---

## 2. Phenomenological Dark Energy Ansatz

**Location:** `submission/paper_1_2/main.tex` Sec. 3 (Phenomenological Dark-Energy Ansatz), `arxiv/main.tex` Secs. 2-4

**What exists:**
- Scaling argument: rho_Lambda = Xi * M_Pl^4, Xi = [(alpha/M) * M_Pl] * D_inf
- Fine-tuning reduction chain: 10^120 -> 10^5 via inflationary dilution
- Monte Carlo sensitivity scan (100,000 samples) confirming N_tot as controlling parameter
- MCMC fits: H0 = 69.2 +/- 0.8, sigma8 = 0.785 +/- 0.016, S8 = 0.80 +/- 0.02

**Classification: B. DEAD_CLAIM_BUT_REUSABLE_INFRASTRUCTURE**

The scaling ansatz is NOT a derivation of w = -1. Paper 1.2 explicitly states this. The fine-tuning reduction depends on the ansatz being correct, and all 7 routes to deriving it from first principles failed. The MCMC fits are real but are driven by the SH0ES prior (verification shows Delta-Neff consistent with zero without it). The sensitivity scan methodology is reusable for any future parametric scaling analysis.

---

## 3. Cosmic Birefringence / Parity Analysis

**Location:** `research/extensions/track_C_parity_cmb/` (scripts, outputs, model-to-observable map), `research/paper2/p6_cmb_eb_pipeline/` (literature registry)

**What exists:**
- Consistency window analysis: f_photon = 1.73 +/- 0.44 (O(1), no fine-tuning needed)
- Combined birefringence posterior: beta = 0.242 +/- 0.061 deg (3.9 sigma from Planck + ACT DR6)
- EB shape comparison (forward model)
- Gaussian posterior sampling scripts
- Literature meta-analysis: beta = 0.358 +/- 0.025 deg (all measurements), forest plot
- 6 publication-quality figures (PDFs + PNGs)

**Classification: A. STILL_ALIVE_AND_USEFUL**

This is the strongest surviving positive asset. The observed cosmic birefringence is REAL data at 3.9 sigma combined significance, independent of the bounce program. The consistency window analysis shows the ECH parity-odd coupling scale is naturally compatible with the data. The key gap (photon-torsion vertex factor f_photon) is an honest open question, not a dead end. The scripts and figures are directly usable. The literature registry is current through early 2026.

---

## 4. Galaxy Spin Chirality Concept

**Location:** `research/paper2/wp5_spin_amplitude/` (Monte Carlo, parity bias model), `research/paper2/p7_cnn_spin_classifier/` (ResNet-18, FAILED), `research/data_build/build_galaxy_spin_dataset.py`

**What exists:**
- Parity-odd tidal torque scaling: A0 = epsilon_PO * 0.015, requiring epsilon_PO ~ 0.2 for A0 ~ 0.003
- Monte Carlo sensitivity: epsilon_PO = 0.244 (68% CI: 0.14-0.38), 100,000 samples
- CNN classifier: FAILED (test_acc = 0.49, random chance) due to RandomHorizontalFlip bug + synthetic data
- Phenomenological model: A(z) = A0(1+z)^{-p} * exp(-qz)

**Classification: B. DEAD_CLAIM_BUT_REUSABLE_INFRASTRUCTURE**

The galaxy spin chirality concept is observationally interesting but the connection to the ECH framework is phenomenological at best (epsilon_PO is a free parameter). The CNN pipeline is broken and needs real SDSS/Galaxy Zoo data. The parity-odd tidal torque model is a generic phenomenological parameterization that does not require spin-torsion cosmology. The Monte Carlo sensitivity methodology is reusable.

---

## 5. Bounce Equations and Perturbation Solvers

**Location:** `research/branch_H_bounce_only/tensor_spectrum/` (6 calculation files + Jupyter solver), `research/branch_K_scalar_perturbations/` (7 calculation files + Jupyter solver)

**What exists:**
- Exact background solution: a(t) = a_b(1 + 4 alpha^2 t^2)^{1/4}
- Tensor mode solver (Bogoliubov coefficients, spectral tilt)
- Results: P_T ~ 2 x 10^{-64}, n_T ~ 0 (flat), Delta-chi = 0 (no chirality)
- Scalar Bardeen equation solver, transfer function T(k) = 1 exactly
- Non-Gaussianity estimate: f_NL^torsion ~ 10^{-56}
- Six parity-odd mechanism assessments (all negative)

**Classification: B. DEAD_CLAIM_BUT_REUSABLE_INFRASTRUCTURE**

The perturbation results are definitive negative results: the bounce is observationally inert. The solvers themselves are well-constructed ODE integrators for bouncing cosmologies and could be reused for any bounce model (not just spin-torsion). But the results they produce are null.

---

## 6. PGT Phenomenology

**Location:** `research/foundation_A_pgt/`, `research/branch_L_uv_ir_bridge/`, `research/branch_M_pgt_bounce_gw/`, `research/branch_P_pgt_bounce_program/`

**What exists:**
- Mass-coupling lock theorem: g_eff ~ m_T / M_Pl^2 (general result)
- Ghost-free parameter space mapping (Sector II, spin-0^- axial torsion)
- PGT bounce GW spectrum: parameter scan table (m_T from 10^{-3} to 10^{18} GeV)
- Vacuum amplification ceiling: Omega_GW proportional to (H/M_Pl)^2, minimum 10^{17} gap
- Torsion relic cosmology (Channels 4+5): gating question on energy fraction
- Z2 parity symmetry blocking torsion relic population at bounce

**Classification: B. DEAD_CLAIM_BUT_REUSABLE_INFRASTRUCTURE**

The mass-coupling lock, vacuum amplification ceiling, and Z2 parity protection are standalone theoretical results with value beyond this program. They constrain ANY attempt to use PGT torsion for late-time phenomenology. The parameter space mapping is reusable. But the PGT bounce program itself is closed -- the Z2 symmetry (Branch P) blocks the last surviving channel.

---

## 7. No-Go Barriers (14 total)

**Location:** `submission/paper_1_2/main.tex` (cataloged in text), `research/branch_NO_joint_summary.md`, individual branch directories

**What exists:**
- 14 structural barriers spanning 5 failure modes
- Organized across Branches A-G (DE derivation) and H-P (bounce observables)
- Each barrier has a clean proof/argument documented in the branch directory
- Paper 1.2 contains the full catalog in publication-ready form

**Classification: A. STILL_ALIVE_AND_USEFUL**

The no-go catalog IS the main positive scientific contribution of the program. It is a publishable comprehensive negative result. Each barrier is a standalone theorem-level result (mass-coupling lock, topological-shift duality, parity-even effective interaction, gravitational democracy, etc.) that constrains future work by others. This has independent value regardless of whether a positive program follows.

---

## 8. Data Visualizations

**Location:** `interactive-data.html`, `interactive-data-simple.html`, `public/images/`, `public/spreadsheets/`

**What exists:**
- Interactive Chart.js visualizations of cosmological parameters
- Scientific figures (PNG, Git LFS tracked)
- Supporting data tables (Excel)
- Web interface with MathJax, lightbox, responsive design

**Classification: B. DEAD_CLAIM_BUT_REUSABLE_INFRASTRUCTURE**

The web infrastructure is well-built but the content it displays is tied to the old Paper 1 claims. The Chart.js visualization framework is reusable for any future data presentation.

---

## 9. Paper 1 (arxiv/main.tex) -- 1680 lines

**Location:** `arxiv/main.tex`

**What exists:**
- Complete Paper 1 manuscript (v1.6.0-preaudit)
- Full theoretical framework, MCMC results, birefringence, galaxy spin, falsification criteria
- 51+ bibliography entries
- Compiled PDF with figures

**Classification: B. DEAD_CLAIM_BUT_REUSABLE_INFRASTRUCTURE**

Paper 1 conflates phenomenological ansatz with derivation. It presents the tension reduction as if the ECH framework is doing the work, when the verification shows Delta-Neff consistent with zero (the SH0ES prior is what pulls H0 up). The bibliography, mathematical exposition, and data compilation remain useful.

---

## 10. Paper 1.2 (submission/paper_1_2/main.tex) -- 2053 lines

**Location:** `submission/paper_1_2/main.tex`

**What exists:**
- Complete Paper 1.2: "Geometric Dark Energy and the Spin-Torsion Bounce: A Complete Theoretical Assessment"
- Three-part structure: phenomenology, DE derivation program, bounce observables
- All 14 barriers documented, 6 structural lessons
- Branches H through P results integrated
- Inline bibliography, 35+ references

**Classification: A. STILL_ALIVE_AND_USEFUL**

Paper 1.2 is honest about what failed and what is phenomenological. It is a legitimate comprehensive negative result paper with substantial positive content (the barrier catalog, the perturbation calculations). It could be submitted essentially as-is once Branches N, O, P results are integrated (they may already be in the latest version).

---

## Summary Table

| Asset | Class | Reuse Value |
|-------|-------|-------------|
| MCMC pipeline (Cobaya/CAMB/RunPod) | A | HIGH -- directly reusable for any cosmological model |
| Phenomenological DE ansatz | B | LOW -- scaling argument dead, sensitivity scan methodology OK |
| Birefringence/parity analysis | A | HIGH -- real data, scripts, figures, open question (f_photon) |
| Galaxy spin chirality | B | MEDIUM -- concept alive, infrastructure needs real data |
| Bounce perturbation solvers | B | MEDIUM -- solvers reusable, results are null |
| PGT phenomenology | B | MEDIUM -- standalone theorems valuable, program closed |
| No-go barrier catalog | A | HIGH -- publishable standalone, constrains future work |
| Data visualizations | B | LOW -- content dead, web framework reusable |
| Paper 1 | B | LOW -- superseded by Paper 1.2 |
| Paper 1.2 | A | HIGH -- publishable comprehensive assessment |
