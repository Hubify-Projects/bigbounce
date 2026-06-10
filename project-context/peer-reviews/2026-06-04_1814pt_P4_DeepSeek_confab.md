# P4 2026-06-04_1814pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 217.5s

---

## Referee Report for P4: Confabulation-Hunter Review (Reasoning Mode)

### ESSENTIAL Findings

- **P4-E1: Abstract, Page 1**  
  **Problem:** Headline figure "−0.12σ" (subsample-mask ℓ=1 null) lacks immediate provenance in the abstract. While Table II in the body links it to a JSON artifact (`master_power_spectrum.json`), the abstract itself does not cite this traceable source.  
  **Fix:** Add a footnote in the abstract: "JSON provenance: `pipelines/p2_chirality/master_results/master_power_spectrum.json`".

- **P4-E2: Abstract, Page 1**  
  **Problem:** "99.3%" (monopole-only leakage amplitude) is presented without explicit traceability. The value derives from Table VII (Sec. IV D) but is not directly linked to its generative null JSON (`monopole_mask_null_results.json`) in the abstract.  
  **Fix:** Reference Table VII and its companion artifact in the abstract: "99.3% (Table VII; artifact: `monopole_mask_null_results.json`)".

- **P4-E3: Sec. IV C, Page 18 (Table VI)**  
  **Problem:** The decomposition "99.3%/12%/88%/25%" (Table VIII) is inconsistent: 12% + 88% = 100%, but 25% is a subset of 88% without clarifying if it is additive or overlapping. The narrative implies 25% is part of the 88% residual, but the abstract presents them as sequential components.  
  **Fix:** Revise Table VIII to explicitly state: "25% of the 88% residual" and update the abstract to: "99.3% leakage (pre-MASTER), 12% residual leakage (post-MASTER), and 88% systematic residual (of which 25% is morphology-proxy-bound)".

- **P4-E4: Sec. VI C, Page 36**  
  **Problem:** The falsification criterion "σ > 5 with full amplitude ≳ 0.75%" uses σ from a per-pixel-shuffle null, but Table XVI (injection-recovery) shows σ values are not comparable across null procedures (e.g., bootstrap vs. binomial). This violates the paper’s own qualification (Sec. I: "σ values [...] are not directly comparable").  
  **Fix:** Specify the null procedure in the falsification criterion: "σ > 5 under a per-pixel-shuffle null with amplitude ≳ 0.75%".

- **P4-E5: Throughout**  
  **Problem:** Version-history artifacts appear in prose: e.g., "v1.0.153" (title), "older snapshot value 2.75σ" (Table VI), "v1.0.76" (Sec. III A). These are internal tags violating journal standards.  
  **Fix:** Remove all version numbers from body text. Use immutable dataset DOIs/URLs for reproducibility instead.

---

### MAJOR Findings

- **P4-M1: Entire Paper**  
  **Problem:** Paper length (56 pages) exceeds PRD norms (15–30 pp) for methods/catalog papers. The systems diagnostics (Sec. IV E–K) and bias audits (Sec. III F) are overdetailed.  
  **Fix:** Condense to 30 pages by:  
  (1) Moving training/architecture details (Sec. III B–D) to supplementary material.  
  (2) Reducing redundant diagnostics (e.g., hemisphere asymmetry vs. sky quadrants).  
  (3) Trimming Table VI (bandpowers) to ℓ = 1–3.

- **P4-M2: Sec. IV D, Page 21**  
  **Problem:** "99.3%" and "12%" are used interchangeably for pre-/post-MASTER leakage (Table VII vs. Table VIII), causing narrative conflict. Table VII reports 99.3% pre-MASTER leakage, while Table VIII claims 12% post-MASTER leakage without reconciling the drop.  
  **Fix:** Clarify in Sec. IV D: "MASTER reduces monopole leakage from 99.3% (pre-) to 12% (post-) of the signal, leaving 88% unresolved systematics".

- **P4-M3: Sec. VI C, Page 36**  
  **Problem:** The "0.75% empirical 50%-recovery-at-3σ threshold" is cited as the falsification floor, but Table IX lists four sensitivity values (0.29%, 0.50%, ≥0.75%, ∼1.19%) without justifying why 0.75% is headline.  
  **Fix:** Justify the choice in Sec. VI C: "0.75% is adopted as the fiducial threshold due to its empirical robustness across pipeline variants (Table XVI)".

- **P4-M4: Sec. III E, Page 10**  
  **Problem:** The 21.4% per-galaxy argmax flip rate (D4-TTA hold-out) is not propagated to dipole uncertainties. The real-space dipole σ = 0.43 (Table II) assumes Poisson noise but ignores flip-induced variance widening.  
  **Fix:** Recalculate dipole σ with flip-noise inflation (∼1.21×; Sec. III E) and report updated significance.

---

### MINOR Findings

- **P4-m1: Abstract, Page 1**  
  **Problem:** "3.2 Million Spirals" in the title contradicts the canonical count "N = 3,201,160" (Sec. IV A), which is 3.20 million (rounded).  
  **Fix:** Update title to: "3.20 Million Spirals".

- **P4-m2: Sec. IV B, Page 15**  
  **Problem:** The residual monopole offset (cw fraction = 0.4974) is called "9.5σ" but uses binomial σ. A spatial-correlation Neff correction is noted as needed but not applied.  
  **Fix:** Add a caveat: "Formal significance may be overestimated if spatial correlations reduce Neff".

- **P4-m3: Sec. V A, Page 32**  
  **Problem:** Shamir’s spiral counts are inconsistently summarized: "∼1.3×10^6" (abstract) vs. "nearly 1.3×10^6" (Sec. V A).  
  **Fix:** Standardize to "∼1.3×10^6" throughout.

---

### NIT Findings

- **P4-n1: Sec. I, Page 3**  
  **Problem:** Duplicate phrase: "canonical canonical-mask" (e.g., "canonical-mask diagnostic" and "canonical mask" used interchangeably).  
  **Fix:** Standardize to "canonical mask" (without hyphen).

- **P4-n2: Sec. IV G, Page 27**  
  **Problem:** "3.05σ" hemisphere asymmetry is reported but downplayed post-LEE. This minor result could be removed to shorten the paper.  
  **Fix:** Delete or move to supplementary material.

- **P4-n3: Table II, Page 9**  
  **Problem:** Footnotes use non-standard abbreviations (e.g., "pp" for percentage points).  
  **Fix:** Replace "pp" with "percentage points".

---

## Summary Recommendation  
**MAJOR REVISIONS**  

Justification: The paper reports a null chirality dipole with rigorous methods and public data, contributing significantly to cosmology. However, it has essential flaws: (1) key scalars in the abstract (e.g., −0.12σ, 99.3%) lack immediate provenance; (2) the leakage decomposition (99.3%/12%/88%/25%) is inconsistently presented; (3) version-history tags (v1.0.153) pollute the body text; and (4) the length (56 pages) far exceeds PRD standards. Major revisions must address traceability, reconcile statistical contradictions, and condense the paper to 30 pages. Minor issues (e.g., terminology standardization) should also be fixed. When revised, this work will meet PRD's reproducibility and concision standards.