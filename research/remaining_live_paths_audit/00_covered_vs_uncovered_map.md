# Covered vs Uncovered Map

**Created:** 2026-03-18
**Status:** COMPLETE
**Purpose:** Honest inventory of what this program has and has not explored.

---

## DEEPLY_COVERED (closed or exhaustive)

These topics have been investigated to the point where further work within the same framing would be redundant.

### 1. ECH Dark Energy Derivation
- **Scope:** All 4 minimal routes to deriving w = -1 from ECH geometry; Foundations A-G (7 structural barriers); IR vacuum program (4 routes closed).
- **Result:** 14 total structural barriers. Bounce and DE are independent problems separated by 60 orders of magnitude in energy. No mechanism connects them.
- **Files:** `research/foundation_A_pgt/` through `research/foundation_G_bounce_vacuum_selection/`, `research/paper2/ir_vacuum_program/`
- **Confidence this is settled:** 95%. Would require a fundamentally new symmetry principle to reopen.

### 2. Minimal ECH Perturbations
- **Scope:** Scalar and tensor perturbation equations through ECH bounce, at all orders in perturbation theory.
- **Result:** ECH is perturbation-transparent. Scalar fields have zero spin current, torsion vanishes identically, Holst term drops out. Barbero-Immirzi parameter disappears completely. Mode equation is unmodified Mukhanov-Sasaki. Tensor spectrum P_T ~ 10^-64 (unobservable). T(k) = 1 for scalar transfer.
- **Files:** `research/branch_Vb_ech_perturbation_gate/`
- **Confidence:** 99%. This is a theorem, not a numerical result.

### 3. Generic Matter Bounce f_NL Benchmark
- **Scope:** Convention resolution (Planck vs Bardeen), literature cross-check (Cai et al. vs Li-Brandenberger vs Quintin), dominant vertex identification, template projection estimate.
- **Result:** f_NL = -35/8 = -4.375 in Planck convention (75% confidence). Convention mapping resolved algebraically. Li-Brandenberger discrepancy diagnosed as systematic factor-of-2, not approximation error. Template projection cos(theta) ~ 0.95.
- **Files:** `research/fnl_derivation_execution/`
- **Remaining gap:** Independent numerical evaluation of the in-in time integral (the 25% uncertainty). This is the single most important open calculation.

### 4. Wilson-Ewing Quasi-Dust + LQC Viability
- **Scope:** Two-pass viability filter across 3 candidate bounce models.
- **Result:** Model B (LCDM quasi-dust bounce) is the ONLY survivor. n_s = 0.964 from w = -0.003 (Lambda contribution). r ~ 10^-4 (LQC dressed-metric). f_NL = -4.375 (parameter-free). Model A (curvaton) killed by blue tilt in matter contraction. Model C (ILS ekpyrotic) failed distinctiveness test.
- **Files:** `research/project_viable_bounce_model_pass2/`
- **Confidence:** 90% for model selection. The 10% uncertainty is entirely in f_NL verification.

### 5. Survey Discrimination Hierarchy
- **Scope:** Detection forecasts for f_NL across SPHEREx, MegaMapper, and Planck.
- **Result:** MegaMapper sigma(f_NL) ~ 0.5 gives 8.75 sigma detection of -4.375. SPHEREx gives ~2.5 sigma. Planck already excludes |f_NL| > 10.3 (current bounds).
- **Files:** Various within `research/branch_V_bounce_evidence/` and `research/next_flagship_program/`

### 6. Inflation Mimicry Assessment
- **Scope:** Can single-field or multi-field inflation produce f_NL^local = -4.375?
- **Result:** NO natural inflationary model produces this. Would require curvaton with r_dec > 1 (unphysical), self-interacting curvaton with lambda < 0 (unstable), or contrived multi-field engineering. Negative local f_NL of O(1) magnitude is hard-to-mimic for inflation.
- **Files:** `research/project_viable_bounce_model_pass2/final_verdict.md`

### 7. Bounce Evidence Audit (16 Claims)
- **Scope:** Systematic assessment of all "bounce explains X" claims in literature and internal results.
- **Result:** No claim reaches STRONG. Three at MODERATE (birefringence is bounce-independent; PTA has trans-Planckian issue; f_NL is testable but unverified). Eight claims overstated and dropped. ECH is perturbation-transparent, so all surviving predictions are bounce-generic.
- **Files:** `research/bounce_evidence_audit/`

### 8. Curvaton Tilt Crisis
- **Scope:** Whether a curvaton can generate red tilt during matter contraction.
- **Result:** NO. Curvaton spectral index is blue in matter contraction. This kills Model A entirely.
- **Files:** `research/project_viable_bounce_model_pass2/`

### 9. Chiral GW Frequency Gate
- **Scope:** Observable frequency of gravitational waves from ECH chiral coupling.
- **Result:** Frequency is in the GHz band (Planck-scale bounce). Permanently inaccessible to all planned detectors. Channel is dead.
- **Files:** `research/branch_M_pgt_bounce_gw/`

### 10. Galaxy Spin Coupling
- **Scope:** Whether ECH torsion coupling can produce detectable galaxy spin correlations.
- **Result:** 9-12 orders of magnitude gap between predicted and detectable coupling strength. Effectively falsified.
- **Files:** `reproducibility/galaxy_spins/`, `research/paper2/wp5_spin_amplitude/`

### 11. ALP Birefringence (Phase 1)
- **Scope:** Consistency of ECH-motivated ALP with cosmic birefringence data (Eskilt 2022, Diego-Palazuelos & Komatsu 2025).
- **Result:** beta = 0.242 +/- 0.061 deg (3.9 sigma combined). Framework requires f_photon = 1.73 +/- 0.44 (O(1), no fine-tuning). Prediction matches data.
- **Files:** `research/extensions/track_C_parity_cmb/`
- **Note:** This is bounce-INDEPENDENT. It uses the ALP from the ECH framework but not the bounce mechanism.

### 12. Hybrid DE Loophole
- **Scope:** Whether adding w0wa freedom to bounce + LCDM could save the DE program.
- **Result:** Exhaustively explored in 7+ disguised forms (Foundations A-G, Branches I/U, salvage audit). Rejected on first principles: improvement comes from w0wa freedom, not from bounce. Never implemented at MCMC level. All 236,622+ chain samples use fixed w = -1.
- **Files:** `research/next_flagship_program/final_verdict.md`

---

## PARTIALLY_COVERED

These have been touched but not exhausted. Specific open questions remain.

### 1. LQC Perturbation Formalisms (Dressed-Metric vs Hybrid)
- **What we did:** Adopted the dressed-metric formalism from Wilson-Ewing (2013) for r suppression. Cited it as giving r ~ 10^-4.
- **What we did NOT do:** Compare dressed-metric to hybrid approach for our specific observables (f_NL, r, n_s). Did not assess whether the formalism choice changes the flagship prediction.
- **Gap significance:** HIGH. If dressed-metric and hybrid give different f_NL, that is a genuine new result. If they agree, it strengthens the prediction.

### 2. Matter-Ekpyrotic Hybrids
- **What we did:** Mentioned ekpyrotic pre-phase as BKL resolution mechanism in Model B. Evaluated ILS ekpyrotic as Model C (failed distinctiveness).
- **What we did NOT do:** Systematically assess two-field ekpyrotic-matter transitions within LQC (the 2025 literature). Did not evaluate whether hybrid models produce different f_NL.
- **Gap significance:** MEDIUM. Could open a second viable model if Model B's f_NL fails.

### 3. ALP Birefringence MCMC (Phase 2)
- **What we did:** Gaussian posterior constraint analysis on g_eff and f_photon. Forward model for EB spectrum shape.
- **What we did NOT do:** Full MCMC with joint cosmological + birefringence likelihood. Did not include scale-dependent birefringence or frequency-dependent effects.
- **Gap significance:** LOW. Current Gaussian analysis is sufficient for the data quality available.

### 4. PBH from Matter Bounce
- **What we did:** Noted the Papanikolaou et al. (2024) mechanism. Classified PBH dark matter as WEAK in evidence audit (2026 dust-radiation calculation shows vanishing fractions).
- **What we did NOT do:** Compute PBH production specifically through the Wilson-Ewing LQC bounce. Did not assess whether the LQC transition dynamics produce the required enhancement.
- **Gap significance:** MEDIUM-HIGH. This is the best candidate second observable channel.

---

## BARELY_TOUCHED

These appear in our notes or literature reviews but have not been systematically investigated.

### 1. PBH + Induced Gravitational Waves in Matter Bounce
- **Status:** We know the mechanism exists (Papanikolaou et al. 2024: short transition enhances small-scale perturbations). We have not computed anything.
- **Why it matters:** Genuinely independent second observable (PTA/LISA/ET bands, not LSS f_NL). Different k-range.

### 2. LQC Low-ell Anomaly / Modulation Program (Agullo et al.)
- **Status:** Cited in bounce evidence audit as WEAK (Durrer challenge, qualitative fits only). Not independently assessed.
- **Why it matters:** If LQC perturbation corrections produce specific, quantitative low-ell predictions, this could strengthen the LQC case even if anomalies are only 2-3 sigma.

### 3. Quantization-Ambiguity Sensitivity
- **Status:** Mentioned in passing. Barbero-Immirzi parameter gamma and holonomy vs inverse-volume corrections noted as open parameters.
- **Why it matters:** If f_NL depends on gamma or quantization scheme, LQC becomes distinguishable from ad hoc bounces. If independent, it strengthens the generic prediction.

### 4. Scale-Dependent Non-Gaussianity f_NL(k)
- **Status:** Not computed. Known that LQC modifies largest scales (k ~ k_LQC) differently from generic bounces.
- **Why it matters:** Would be a genuinely LQC-specific prediction extending the flagship f_NL program.

### 5. Third-Order Perturbation Theory Through LQC Bounce
- **Status:** Identified as critical gap in fnl_derivation_execution. Nobody has computed bispectrum TRANSFER through the LQC bounce. Our f_NL = -35/8 is the pre-bounce value.
- **Why it matters:** If the LQC bounce modifies f_NL (enhances or suppresses), that changes the entire detection forecast. This is the single most important uncomputed quantity in the program.

---

## NOT_REALLY_TESTED

These are entire frameworks or approaches that exist in the literature but were never seriously evaluated in our program.

### 1. GFT Condensate Cosmology
- Entirely different UV completion (group field theory rather than canonical LQG/LQC). Produces bouncing cosmologies from a different starting point. We have not assessed its perturbation predictions or compared to our LQC results. Too far from our current infrastructure to pursue without a major pivot.

### 2. Teleparallel / f(T) / f(Q) Bounce Builders
- Large theory space of modified gravity bounces. Not assessed. These are mostly "bounce exists" papers without sharp observable predictions. Very high sprawl risk.

### 3. Non-Minimal ECH with Genuine Fermionic Torsion Sources
- ECH perturbation transparency is proven for scalar field perturbations. Fermion perturbations couple to torsion and could in principle modify the scalar spectrum at loop level or through backreaction. Not assessed. Expected to be negligible for superhorizon modes, but this is an assumption, not a calculation.

### 4. Quasi-Dust Ekpyrotic Two-Field LQC (arXiv:2509.06148)
- A 2025 paper claiming viable n_s + r from two-field ekpyrotic in LQC. Not evaluated for f_NL predictions. Could either confirm or challenge our single-field architecture.

### 5. Deformed Algebra Approach to LQC Perturbations
- A third formalism (beyond dressed-metric and hybrid) where the constraint algebra itself is deformed. Known to give different results in some regimes. Not assessed for our observables.

---

## Summary Table

| Topic | Coverage | Priority to Fill Gap |
|-------|----------|---------------------|
| ECH DE derivation | EXHAUSTIVE | None (closed) |
| ECH perturbations | EXHAUSTIVE | None (closed) |
| f_NL = -35/8 pre-bounce | 75% confident | HIGHEST (in-in integral) |
| f_NL transfer through LQC bounce | NOT DONE | HIGHEST (critical gap) |
| Model viability filter | COMPLETE | None |
| Dressed-metric vs hybrid for f_NL | NOT DONE | HIGH |
| Quantization-ambiguity sensitivity | NOT DONE | MEDIUM |
| PBH + induced GW | NOT DONE | MEDIUM-HIGH |
| Scale-dependent f_NL(k) | NOT DONE | MEDIUM |
| Low-ell anomaly program | BARELY TOUCHED | LOW |
| Matter-ekpyrotic hybrids | PARTIALLY | MEDIUM |
| GFT condensate | NOT DONE | LOW (too far) |
| Teleparallel bounces | NOT DONE | VERY LOW (sprawl) |
| Non-minimal ECH fermions | NOT DONE | LOW (closed lane) |
