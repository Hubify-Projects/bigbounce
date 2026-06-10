# P4 2026-06-04_1920pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 158.5s

---

## Referee Report: PAPER P4

### ESSENTIAL Revisions

- **P4-E1: Abstract/Conclusions: σ values from different null procedures presented without qualification**  
  - Sec: Abstract, Sec IV C (Table VI), Sec VII  
  - Problem: The abstract reports "−0.12σ" (MASTER-deconvolved) and "+0.43σ" (real-space) as if directly comparable, but they derive from different null procedures (label-shuffle MC for MASTER; per-pixel-shuffle MC for real-space). This implies a false equivalence. Similarly, the canonical-mask "+3.64σ" (binomial monopole-only null) is conflated with other σ values.  
  - Fix: Explicitly qualify all σ values by null procedure (e.g., "−0.12σ under label-shuffle MASTER null") in abstract, figures, and conclusions. Add cautionary language: "σ values from different null procedures are not directly comparable; consult Table II for estimator specifications."

- **P4-E2: Inconsistent decomposition arithmetic in Sec IV D (Table VIII)**  
  - Sec: IV D (Table VIII, pp. 21–26)  
  - Problem: The decomposition "99.3% (pre-MASTER leakage) + 12% (post-MASTER leakage) + 88% (residual) + 25% (leg-proxy)" mixes incompatible quantities: 99.3% is of pre-MASTER *amplitude*; 12%/88% are of post-MASTER *power* (C₁); 25% is of the ℓ=1 *amplitude*. This arithmetic (99.3 + 12 + 88 + 25 ≠ 100%) is misleading.  
  - Fix: Recalculate decomposition using consistent units (power or amplitude) throughout. Clarify that 25% is a partial closure of the 88% residual, not an additive component. Correct Table VIII to avoid implying summation.

- **P4-E3: Lack of provenance for headline scalars in abstract**  
  - Sec: Abstract, IV B–IV D  
  - Problem: Key scalars lack explicit JSON/script provenance: −0.12σ (no artifact for subsample-mask MASTER), 99.3% (monopole leakage; artifact `monopole_mask_null_results.json` exists but not cited in text), 0.75% (injection threshold; artifact `injection_recovery_extended.json` not linked in abstract).  
  - Fix: Embed artifact paths in text for all abstract scalars (e.g., "−0.12σ [pipeline: master_power_spectrum.json]"). Ensure all referenced artifacts are in the immutable release.

---

### MAJOR Revisions

- **P4-M1: Paper length exceeds journal norms without justification**  
  - Sec: Entire document (56 pp)  
  - Problem: At 56 pages, the paper far exceeds PRD's 15–30 pp standard for methods/catalog papers. Peripheral content (e.g., exhaustive null batteries, tangential systematics) dilutes core results.  
  - Fix: Condense to ≤30 pp by:  
    (a) Moving Sec III F (bias tests), IV E–IV K (diagnostics), and VI H (follow-ups) to supplements.  
    (b) Removing redundant tables (e.g., Table IV, Table XI).  
    (c) Simplifying the estimator hierarchy (Sec III A) to one paragraph.

- **P4-M2: Abstract misrepresents "load-bearing" result**  
  - Sec: Abstract, Conclusions  
  - Problem: The abstract positions the canonical-mask residual (+3.64σ) as a "diagnostic" but later calls it "load-bearing" in Sec VI G, creating confusion. The −0.12σ subsample-mask result is claimed as primary but relies on a specific mask choice not defended until Sec VI F.  
  - Fix: Restructure abstract to:  
    (i) Lead with the subsample-mask null (−0.12σ) as the primary cosmological result.  
    (ii) Demote canonical-mask residual to "diagnostic context."  
    (iii) Remove "load-bearing" from descriptions of non-primary results.

- **P4-M3: Version-history artifacts in body text**  
  - Sec: II B (p. 5), IV C (footnotes)  
  - Problem: Phrases like "retained for verification-continuity purposes" (Sec II B) and "retained only as a historical cross-reference" (Sec IV C) are version-history artifacts violating the journal-clean sweep (v1.0.152).  
  - Fix: Delete all version-tracking language (e.g., "superseded," "historical cross-reference"). Report only final canonical results.

---

### MINOR Revisions

- **P4-m1: Duplicate phrases and typos**  
  - Sec: IV D ("canonical canonical-mask" in Table VIII title), Fig. 6 caption ("ordered by decreasing classification confidence confidence").  
  - Fix: Remove duplicates. Proofread for similar errors.

- **P4-m2: Incomplete GZ1 validation provenance**  
  - Sec: II B, III F (T7)  
  - Problem: The 69.91% GZ1 agreement (Sec II B) cites `B20_B21_results.json` but does not specify how it validates Catalog C.  
  - Fix: Add a table cross-tabulating GZ1 vs. Catalog C labels with confusion matrix, hosted in a cited artifact.

- **P4-m3: Undefined "wave 14" nomenclature**  
  - Sec: II B, IV D, VI C  
  - Problem: "wave 14" (e.g., `wave_14_nn_injection_recovery.json`) is undefined and obscures provenance.  
  - Fix: Define "wave" as a pipeline batch ID in a footnote or glossary.

---

### NIT Revisions

- **P4-n1: Overuse of "canonical"**  
  - Sec: Throughout (e.g., "canonical mask," "canonical-N").  
  - Fix: Replace with specific descriptors (e.g., "fiducial mask," "spiral-count-normalized").

- **P4-n2: Redundant confidence-stratification details**  
  - Sec: IV K, Table X  
  - Problem: Table X repeats information from Sec IV E and Fig. 10.  
  - Fix: Keep one concise table; remove the other.

---

## Summary Recommendation  
**MAJOR REVISIONS**  

Justification: The paper reports a significant null dipole result with rigorous systematics tests, but essential issues undermine its conclusions: σ values from incompatible null procedures are presented as equivalent (P4-E1), and the decomposition arithmetic is inconsistent (P4-E2). The length (56 pp) far exceeds PRD standards (P4-M1), and version-history artifacts (P4-M3) contradict the clean sweep claim. While the catalog and methodology are valuable, the presentation must be restructured to qualify statistical claims rigorously, shorten to ≤30 pp, and excise historical baggage. Addressing these will align the paper with PRD's reproducibility and concision standards.