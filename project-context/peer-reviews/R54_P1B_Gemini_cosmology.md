# P1B R54 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R54_P1B/paper1b_mcmc_companion.pdf` md5=0b4a8768 pages=21
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 176.1s

---

## Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Manuscript ID:** [Internal ID]
**Author:** Houston Golden
**Journal:** Physical Review D

### Summary recommendation
**ACCEPT WITH MINOR CORRECTIONS**

This paper presents three technical analyses that serve as verification and contextualization for a separate program on Einstein-Cartan-Holst (ECH) cosmology. The analyses themselves—a standard ΛCDM+ΔNeff MCMC run, a NaMaster pipeline validation for cosmic birefringence, and a spectator-ALP consistency check—are presented not as new discoveries but as carefully executed null tests and compatibility checks.

The manuscript is exceptionally well-written, rigorous, and transparent. The scope of each analysis is clearly defined, and the authors are meticulous in stating the limitations of their results, avoiding over-interpretation. The commitment to reproducibility, with detailed appendices, public code/data repositories, and explicit versioning, is exemplary and meets the highest standards of the field. The paper successfully achieves its stated goal of providing a solid technical foundation for its companion work.

The few required corrections are minor and relate to numerical precision and clarity. The paper is a model of good scientific practice and is suitable for publication in Physical Review D after these minor points are addressed.

---
### Detailed Findings

#### MAJOR Revisions

**ID: P1B-M1**
*   **Location:** Section IV, Page 8, "Noise model and injections" paragraph.
*   **Problem:** The paper states the HEALPix pixel area for Nside=512 is `Ω_pix = 47.21 arcmin²`. The standard calculation for the area of a HEALPix pixel is `Ω_pix = 4π / (12 * Nside²)`, which for Nside=512 yields approximately 41.8 arcmin². This is a significant discrepancy (~13%) in a fundamental quantity. While the subsequent calculation of the per-pixel noise RMS (`σ_pix = 1.455 μK`) is internally consistent with the quoted (but incorrect) `Ω_pix`, the pixel area itself is wrong.
*   **Required Fix:** Correct the value of `Ω_pix` to the standard value of ~41.8 arcmin². Recompute the corresponding `σ_pix` (`10 / sqrt(41.8) ≈ 1.545 μK`) and verify if this change has any downstream effect on the pipeline validation results. If the value 47.21 arcmin² arises from a non-standard definition (e.g., related to the specific footprint mask), this must be explicitly defined and justified.

#### MINOR Revisions

**ID: P1B-N1**
*   **Location:** Section V.B, Page 11, "Independent re-run cross-check" paragraph.
*   **Problem:** The text states that the re-run gives `ΔNeff = +0.0514 ± 0.171`, which is in "0.04σ agreement with the frozen +0.058 ± 0.179 quote above." The calculation is `|0.058 - 0.0514| / sqrt(0.179^2 + 0.171^2) = 0.0066 / 0.2475 ≈ 0.027σ`. The quoted `0.04σ` appears to be a slight overestimation or based on a different calculation (e.g., using only one of the uncertainties).
*   **Required Fix:** Please verify the calculation for the agreement significance. The difference appears to be at the ~0.03σ level. Adjust the text to reflect the precise value.

**ID: P1B-N2**
*   **Location:** Section II, Page 5, paragraph starting "in Table I, which carries the H0.riess2020Mb likelihood...".
*   **Problem:** The text describes a 3.2σ tension manifesting in the `M_B` axis. The calculation is based on an offset of 0.156 mag along the Pantheon+ constraint axis, divided by the marginal uncertainty `σ_MB = 0.049`. While the text correctly qualifies this as a "descriptive offset measure" and not a formal tension, the presentation could be misinterpreted.
*   **Required Fix:** To enhance clarity and prevent misinterpretation, please briefly rephrase to make it even more explicit that this is an internal consistency check of the joint posterior against one of its inputs along a specific degeneracy direction, rather than a standard tension between two independent posteriors. For example: "...This offset, when projected onto the `M_B` axis and normalized by the marginal posterior width `σ_MB`, corresponds to ~3.2σ. We emphasize this is a descriptive measure of the model's internal strain, not a formal tension statistic."

**ID: P1B-N3**
*   **Location:** Section III, Page 3, Footnote 1.
*   **Problem:** The footnote provides a detailed and transparent reconciliation of sample counts, but the discussion of the 20% vs. 30% burn-in is slightly convoluted. A reader may be confused about which value is used where.
*   **Required Fix:** Streamline the explanation for clarity. Suggestion: "The 30% burn-in figure used throughout this paper is a conservative choice matching the original chain configuration's documentation. Standard GetDist analysis reports diagnostics using a 20% burn-in by default, which accounts for minor differences in sample counts (e.g., 106,361 vs. 93,066) reported by automated tools for the same chain."

#### NIT (Cosmetic)

**ID: P1B-T1**
*   **Location:** Section VI, Page 12, paragraph starting "The DESI DR2 w0wa chain...".
*   **Problem:** The text refers to `χ²_BAO`, `χ²_CMB`, and `χ²_SN`. The table and subsequent text use `X_BAO`, `X_CMB`, `X_SN`.
*   **Required Fix:** For consistency, use either `χ²` or `X` notation throughout. Using `χ²` is more standard.

**ID: P1B-T2**
*   **Location:** Section VI, Page 14, paragraph starting "MCMC parameter estimation."
*   **Problem:** The sentence "...settles at `θ_i = 1.32 ± 0.41` and `m = 10-10^2 H_0` (posterior median `m ≈ 36 H_0`) — i.e. outside the natural envelope box `θ_i ∈ [0.5, 2]`, `m/H_0 ∈ [1, 3]` in mass — where the data-preferred joint product is..." is very long and contains multiple nested clauses, slightly hindering readability.
*   **Required Fix:** Consider breaking this into two sentences for improved clarity.