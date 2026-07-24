# Manuscript Update Plan: v1.5.0 → v1.6.0

**Date:** 2026-03-13
**Purpose:** Integrate audited Track C and early-structure results into the manuscript

---

## 1. Early-Structure Future-Work Paragraph

### Location
Insert at **end of Section 11.4 "Bounce-to-Inflation Transition Dynamics"** (after line ~1132), as a new paragraph within the existing subsubsection. This is the natural home because the subsubsection already discusses the bounce-to-inflation transition and N_tot determination.

### Content
3 sentences: state that the bounce-to-inflation transition may imprint P(k) features, that N_tot = 92 places them at k ~ 10^15 Mpc^-1 (asteroid-mass PBH scales), and that a full perturbation calculation is needed.

### Wording to AVOID
- "SMBH seed formation" — framework does not predict features at those scales
- "early structure" — overly suggestive
- "implications for JWST" — no connection exists
- "allowed window" — refers to phenomenological analysis not in the paper

---

## 2. Track C Consistency Check

### Location
Insert as a **new subsection within Section 10 (Discussion)**, after the existing "Theoretical Implications" subsection (after line ~1031) and before "Distance Measures and Rotation." Title: "Cosmic Birefringence Consistency Check"

### Content
2 paragraphs: (1) state the combined published birefringence measurements and the framework's parity-odd coupling; (2) translate to f_photon and note O(1) naturalness. Use the conservative draft from the paper integration recommendation.

### Wording to AVOID
- "constraint" — no likelihood evaluated
- "posterior" — no Bayesian inference performed
- "our analysis finds" — we combine published numbers
- "we measure f_photon" — algebraic parameter translation
- "predicts" — the framework does not predict β

### Wording to USE
- "consistency check"
- "combining published measurements"
- "requires f_photon ≈ 1.7"
- "compatible with"
- "does not uniquely select"

---

## 3. Figure Inclusion

### Track C: Include ONE figure
- **consistency_window.pdf** — Shows f_photon vs β with observational bands
- Copy to `arxiv/figures/consistency_window_birefringence.pdf`
- Caption must call this a "consistency check" and state data are from published measurements

### Do NOT include
- beta_posterior.pdf — labeled "posterior" but no inference was performed
- geff_posterior.pdf — same issue
- eb_shape_comparison.pdf — forward model without data comparison, misleading
- pk_feature_window_analysis.pdf — not relevant to current paper

---

## 4. Claims Table Update

Add one row to the Claims Classification table (Appendix K):

| Claim | Status | Where | Notes |
|-------|--------|-------|-------|
| f_photon ≈ 1.7 from birefringence | Consistency check | Sec. 10.X | Algebraic translation of published β using framework α/M |

---

## 5. Version Updates

- `\paperVersion` → v1.6.0
- Date → March 13, 2026
- Data and Code Availability URL tag → v1.6.0

---

## 6. Revision Tracker Update

Log as Round 7:
- Early-structure future-work paragraph (3 sentences)
- Track C consistency check subsection (2 paragraphs + 1 figure)
- Claims table updated
- Version bump

---

## 7. Compilation

Compile on RunPod pod (<pod-ip>:<port>) using existing compile_on_pod.sh script.
Verify: 0 undefined references, no overfull hboxes affecting readability.
