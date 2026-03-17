# Section-by-Section Rebuild Plan

**Date:** 2026-03-17

---

## Paper Structure: Current vs Salvaged

### Current Paper 1 structure (12 sections + 10 appendices, ~1680 lines)

### Salvaged Paper structure (target: ~1200-1400 lines)

---

## Section 1: Introduction

**Action:** KEEP BUT REVISE SUBSTANTIALLY

Current: "dark energy from quantum gravity in rotating BH universe"
New: "spin-torsion bounce cosmology + parity phenomenology"

Specific changes:
- Para 1 (CC problem, tensions): Keep. Standard motivation.
- Para 2 (DESI evidence): Keep. Update with DR2.
- Para 3 ("three pillars" — LQC, EC, BH universe): **Revise.** Keep LQC and EC. Downgrade BH universe from "pillar" to "one possible UV completion." The ALP does not require BH origin.
- Executive summary table (Tab 1): **Rewrite completely.**
  - Remove: H_0 tension row, sigma_8 tension row, "geometric origin" DE row
  - Keep: singularity/bounce row
  - Add: cosmic birefringence prediction row (beta_pred = 0.27 deg vs 0.35 +/- 0.09 obs)
  - Add: structural closure row (13 barriers, all DE routes closed)

### Sec 1.1 (Theoretical Foundations): REVISE
- Keep EC theory paragraph
- Keep LQG/parity paragraph
- Trim BH universe paragraph to 2-3 sentences of motivation
- Add: "The parity-odd sector motivates a Planck-scale ALP..."

### Sec 1.2 (Original Contributions): REWRITE
New contributions list:
1. Complete assessment of ECH bounce cosmology (bounce well-defined, 13 barriers cataloged)
2. Systematic closure of first-principles DE routes (Foundations A-G)
3. Spectator ALP birefringence prediction: beta ~ 0.27 deg from f_a = M_Pl, C = 8
4. MCMC constraints on (theta_i, m_a) from birefringence data
5. Falsification program for LiteBIRD/CMB-S4

### Sec 1.3 (Paper Organization): UPDATE to match new structure

---

## Section 2: Theoretical Framework

**Action:** KEEP CORE, REVISE FRAMING, ADD ALP SECTION

### Sec 2.1 (ECH Action): KEEP AS-IS
- Eq 1 (ECH action), Eq 2 (gamma), Steps 1-2 (torsion, four-fermion): unchanged
- These are well-established physics

### Sec 2.1.2 (Parity-Odd Term): REVISE FRAMING
- Steps 3-4: Keep the math but change the narrative
- Current: "This generates dark energy"
- New: "This generates a parity-odd operator. Whether it persists as a late-time vacuum term is an open question (see Sec X for closure of four attempted derivations). The parity-odd structure motivates an effective ALP sector."
- Eq 6-8 (alpha/M, one-loop): Keep. Explicitly label as "motivation for ALP coupling scale"
- Remove: language about "dark energy scale" being "set" by this operator

### Sec 2.1.3 (Parameter Naturalness): TRIM
- Remove BH mass discussion (specific to BH-universe scenario)
- Keep only: gamma is fixed by LQG, alpha/M has natural O(1) one-loop origin

### Sec 2.2 (Bounce): KEEP AS-IS
- Modified Friedmann, critical density, bounce properties: all clean

### Sec 2.3 (Cosmic Rotation and DE): MAJOR REVISION

**What to do with the failed DE term:**
- Lambda_eff = Xi M_Pl^2 + c_omega omega^2 → REMOVE as a claim
- Replace with: "The inflationary suppression chain (Eq X) illustrates how a Planck-scale parity-odd coefficient could in principle map to late-time scales. However, four explicit routes to deriving w = -1 from the minimal model have been tested and closed (Sec X). We therefore treat dark energy as a separate cosmological constant Lambda."
- Keep the vorticity formalism as background (needed to explain axis)
- Trim: galaxy spin mechanism subsection (Sec 2.3.3) → REMOVE ENTIRELY (9-12 OOM gap)

### NEW Sec 2.4: Effective Spectator ALP Sector
- Add new subsection defining the ALP model cleanly
- Content from 04_effective_sector_spec.md
- Lagrangian, parameters, coupling, birefringence formula
- What is claimed vs what is not claimed

---

## Section 3: Observational Signatures and Evidence

**Action:** RESTRUCTURE

### Sec 3.1 (CMB E-B): KEEP AND EXPAND
- Keep birefringence formula (Eq 14)
- Add: ALP prediction beta = C alpha theta_i eta / (4 pi)
- Add: comparison table (predicted vs observed)
- This becomes the CENTRAL observational section

### Sec 3.2 (Galaxy Spin): REMOVE
- The framework cannot produce A_0 ~ 0.003 (coupling gives A_0 ~ 10^{-12})
- Mention in limitations (1-2 sentences) that galaxy spin asymmetry is phenomenologically interesting but the ECH coupling is orders of magnitude too small

### Sec 3.3 (H_0 and sigma_8 tensions): REFRAME
- Current: "our model reduces tensions"
- New: "The standard LCDM parameters obtained from our MCMC fit are consistent with Planck. The Delta-Neff extension does not by itself resolve cosmological tensions (Sec X verification)."
- Trim to ~1/3 current length

### Sec 3.4 (Verification): KEEP AND MOVE
- Move to an appendix or merge into Sec 6 (MCMC)
- The key finding (Delta-Neff consistent with zero) supports the reframing

---

## Section 4: Data Methods: Galaxy Spin

**Action:** REMOVE ENTIRELY

This entire section supports galaxy spin analysis which the framework cannot source. Move to companion paper or supplementary material if desired.

---

## Section 5: Data Methods: CMB E-B

**Action:** KEEP, EXPAND WITH ALP LIKELIHOOD

- Keep literature birefringence measurements
- Add: description of ALP birefringence likelihood (Gaussian on beta_obs)
- Add: ALP ODE integrator description
- This becomes the data methods section for the ALP MCMC

---

## Section 6: Cosmological Fits and Model Comparison

**Action:** RESTRUCTURE

### Current: LCDM + Delta-Neff fits
### New structure:
- Sec 6.1: Standard LCDM baseline (Planck + BAO)
- Sec 6.2: ALP spectator birefringence MCMC (Run 2 results)
- Sec 6.3: Joint ALP + Planck + BAO constraints (Run 4 results, if available)
- Sec 6.4: Model comparison (ALP vs null, Bayes factor)
- Remove: tension reduction narrative, keep only the honest fit results

---

## Section 7: Systematic Analysis

**Action:** TRIM

- Remove: galaxy spin systematics, galaxy spin null tests
- Keep: CMB E-B systematics (from literature)
- Add: ALP model systematics (prior sensitivity, eta approximation accuracy)

---

## Section 8: Falsification Criteria

**Action:** REWRITE FOR ALP MODEL

New falsification criteria:
1. LiteBIRD measures beta with sigma ~ 0.01 deg. If beta = 0 at > 5 sigma, ALP model is falsified.
2. If beta is confirmed but frequency-dependent, spectator ALP is falsified (ALP gives achromatic rotation).
3. If anisotropic birefringence pattern is inconsistent with monopole-only prediction.
4. CMB-S4 constrains m_a through ISW-like effects for m ~ H_0.

Remove: galaxy spin falsification, rotation bound falsification (rotation is negligible)

---

## Section 9: Related Work

**Action:** KEEP, UPDATE

- Keep: rotating cosmologies, torsion cosmology, parity violation in gravity
- Remove: galaxy spin studies (or trim to 1-2 sentences)
- Update: cosmic birefringence subsection with latest references (Eskilt 2025, SPIDER 2025)
- Add: ALP birefringence literature (Fujita et al., Obata & Fujita, etc.)

---

## Section 10: Discussion

**Action:** MAJOR REVISION

### Sec 10.1 (Inflationary Suppression): DOWNGRADE
- Reframe as "illustrative dimensional chain, not a derivation"
- Trim to half current length

### Sec 10.2 (Limit behavior): KEEP, MINOR EDITS

### Sec 10.3 (Theoretical implications): REWRITE
- Focus on: (1) bounce is viable, (2) DE is separate, (3) ALP is the testable sector
- Add: comparison of spectator ALP to ALP-as-DE (the factor-2 tension from Phase 2 prefit)
- Add: "the ALP is not uniquely derived from ECH; ECH provides one possible UV motivation"

### Sec 10.4 (Birefringence consistency): REWRITE WITH ACTUAL PREDICTION
- Replace the vague f_photon x C_0 = O(1) check with the clean ALP prediction
- Present MCMC posterior

### Sec 10.5 (Distance measures): TRIM OR REMOVE (rotation is negligible)

### NEW Sec 10.X: Structural Closure Summary
- Add subsection summarizing the 13 barriers in compact form
- Reference companion note for full details
- This replaces the scattered closure discussion throughout Paper 1.2

---

## Section 11: Limitations and Future Directions

**Action:** REVISE

### Sec 11.1 (Theoretical limitations): REWRITE
- w = -1 not derived → state clearly, cite closure
- ALP is not uniquely from ECH → state clearly
- m ~ H_0 is the CC problem in disguise → state clearly

### Sec 11.2 (Observational limitations): KEEP, UPDATE

### Sec 11.3 (Galaxy spin null robustness): REMOVE (galaxy spin is removed)

### Sec 11.4 (Future prospects): REWRITE
- LiteBIRD forecast (sigma_beta ~ 0.01 deg)
- CMB-S4 sensitivity
- DESI DR2 w(z) constraints on ALP-as-DE scenario

### Sec 11.5 (Theory program): TRIM HEAVILY
- Remove: higher-loop verification, BH interior NR, bounce-to-inflation dynamics
- Keep: connection to other QG approaches (1 paragraph)
- Add: what would make the ALP uniquely ECH (the one-loop vertex question from salvage audit)

---

## Section 12: Conclusions

**Action:** REWRITE

Three-paragraph structure:
1. The ECH bounce is a well-defined nonsingular cosmology. Thirteen structural barriers close all first-principles routes to dark energy and all distinctive signature channels.
2. A Planck-scale spectator ALP with SM anomaly coupling predicts beta ~ 0.27 deg, consistent with observation. MCMC constraints yield [results]. LiteBIRD will be decisive.
3. Dark energy remains unexplained by the minimal ECH framework. The bounce and DE are independent problems. The ALP birefringence prediction is the single testable output of this program.

---

## Appendices

| Appendix | Action |
|----------|--------|
| A: Notation | KEEP, add ALP symbols |
| B: Parameters | REWRITE with ALP params |
| C: Galaxy spin Bayesian | REMOVE |
| D: Joint likelihood | REMOVE |
| E: Nieh-Yan | KEEP (supports parity-odd derivation) |
| F: Rotation framework | TRIM to 1 page (axis motivation only) |
| G: Error analysis | KEEP, update for ALP MCMC |
| H: Dimensional analysis | KEEP |
| I: Reproducibility | UPDATE for ALP code |
| J: Claims | REWRITE completely |

---

## How to Handle the No-Go/Closure Context

**Problem:** Paper 1.2 has a 14-barrier, 10-branch closure assessment. This is valuable but would overwhelm a paper whose focus is the ALP prediction.

**Solution:**
1. In Paper 1: A compact "Structural Closure Summary" subsection in the Discussion (Sec 10.X), ~1 page, listing all 13 barriers in a single table with 1-line descriptions. Reference the companion technical note for full details.
2. The companion note (Paper 1.2 / supplement) contains the full closure assessment.
3. In the Introduction: "A comprehensive assessment of first-principles routes to dark energy within the ECH framework yields clean negative results (thirteen structural barriers; see Sec X and Ref [companion]). This motivates the phenomenological approach adopted here."

This keeps Paper 1 focused on the positive result (ALP birefringence) while acknowledging the negative results honestly.

---

## How to Mention ECH Motivation Honestly

Standard formulation throughout:
- "The ECH framework motivates a Planck-scale ALP through its parity-odd sector"
- NOT "the ECH framework derives/predicts an ALP"
- "f_a ~ M_Pl is the natural scale in ECH"
- NOT "f_a = M_Pl is predicted by ECH"
- "The birefringence prediction is model-independent (any f_a ~ M_Pl ALP with SM coupling gives beta ~ 0.27 deg); ECH provides one possible UV completion"
- NOT "ECH uniquely predicts cosmic birefringence"
