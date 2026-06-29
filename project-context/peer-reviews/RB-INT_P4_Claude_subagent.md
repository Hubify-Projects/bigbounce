# RB-INT Referee Report — P4 (Chirality Catalog)

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA (v1.0.196, 24pp)
**Reviewer role:** Neutral journal referee (PRD/ApJ bar), null-result catalog class
**Date:** 2026-06-29

---

## VERDICT: minor-revisions

The science is sound and the manuscript is unusually self-consistent for a null-result catalog — every arithmetic chain I could check holds, often to surprising precision — but the abstract gives a physically incorrect reason for the largest internal σ gap, and one headline tension factor is built on the most favorable of several disclosed amplitudes. Both are quick, bounded fixes; no blocker or major-class defect.

---

## Findings

### 1. [MINOR] Abstract attributes the +3.64σ vs +7.93σ canonical gap to "different null-run sizes" — but run size cannot produce a 2× z shift.
**Abstract** (parenthetical after the harmonic diagnostics) and **§notation (Sec III.A)**: the +3.64σ (500-MC direct) and +7.93σ (10⁴-perm, Table III canonical-unapod row) values are described in the abstract as "from different null-run sizes, not two independent detection claims." For a fixed estimator, the moment-z `(C₁−⟨C₁⟩_null)/σ_null` has an expectation independent of the number of null draws; 500 vs 10⁴ realizations changes the MC estimate of `σ_null` by only a few percent, not a factor of ~2 in z. The actual driver is stated correctly in §notation and Appendix A: the two rows use **different monopole-subtraction weight conventions** (+3.64 = A_p field with galaxy-weighted W_p=N_all mean subtraction, ⟨A⟩_mask,gw=−0.005294; +7.93 = (A_p/2) field with N_spiral-weighted subtraction). The abstract should name the weight/field-convention difference (as §notation does), not "null-run sizes," which is the one cause that demonstrably cannot account for the gap. Impact is low because both numbers are explicitly non-primary/systematics-attributed, but the abstract's stated explanation is simply wrong as written.

### 2. [MINOR] The "factor of ~5–12" Shamir tension headlines the smallest of several disclosed amplitudes (0.32% regional max), not the global dipole best-fit.
**Intro, §comparison (Sec V.A), §parity_translation (Sec VI.C):** the ~5–12× tension is computed as Shamir's 1.7%–4.0% ÷ **0.32%** (the maximum WLS template amplitude restricted to "the cleanest equal-area partition," A_p units). But the paper's own global block-bootstrap dipole best-fit is A_dipole=4.55×10⁻³ = **0.455%** A_p (Table X), and the real-space healpy dipole amplitude is 4.4×10⁻³ = 0.44% A_p (Sec III.C). Using the global dipole amplitude gives ~4–9×, not 5–12×; the chosen 0.32% inflates the headline factor by ~30–40%. The larger amplitudes are disclosed in the same sentence ("equal-area slab maxima reach 0.46–0.56%"), so this is not concealment, but headlining the single most-favorable number to maximize the stated discrepancy is exactly the value-selection pattern a skeptical referee flags. Recommend leading with the global dipole-amplitude comparison (~4–9×) and quoting the regional 0.32% as a secondary, clearly-scoped statistic. (Note: the *conservative* choice of Shamir's 1.7% lower end for the z≈−18 **exclusion** is correct and appropriate — this finding is only about the amplitude-ratio framing.)

### 3. [MINOR/OPINION] The primary HC cut p_eq>0.6 sits exactly on the systematic-transition boundary.
**§dipole (Sec III.C):** the confidence-cut sweep collapses from z=+4.3,+4.1,+4.0 at cuts {0,0.4,0.5} to z=+0.41,+1.14,+0.51 at {0.6,0.7,0.8}. The primary threshold (0.6) is the first cut on the null side of a sharp transition. The paper defends this well — 0.6 is the generator's standing operational threshold, pre-specified, robust across the {0.6,0.7,0.8} sub-sweep (all |z|<1.2), and the physical argument (a real diluted dipole would *strengthen* with confidence, whereas this excess *weakens*) is genuinely sound. No change to the verdict required, but one explicit sentence acknowledging that the primary cut coincides with the systematic boundary (rather than leaving the reader to notice) would close the appearance gap.

### 4. [OPINION] Hedging density occasionally works against the reader.
The notation section plus ~6 repeated figure/table-caption caveats ("σ values arise from distinct null procedures; not directly comparable") are individually correct and the discipline is admirable for a multi-null paper. But the abstract alone carries three nested "Note: … diagnostic-only, not directly comparable" clauses, and a first-time reader must work hard to extract the one-line result (HC real-space dipole +0.41σ, null). Consider consolidating the repeated caption caveats into a single forward-reference to §notation and tightening the abstract so the primary null is not buried under diagnostic disclaimers. This is a presentation preference, not a defect — the hedging is substantively justified.

### 5. [MINOR] Table III canonical-unapod row does not recompute to its stated z from the displayed cells (disclosed).
**Table III:** the canonical-unapod ℓ=1 row shows C=7.27, ⟨C⟩=0.57, σ=0.84 (×10⁻⁶), which recompute to z=(7.27−0.57)/0.84=**+7.98**, while the row states **+7.93**. The caption explicitly flags that "tabulated values are rounded for display — the full-precision arrays live in the committed artifacts," and the residual is consistent with σ≈0.845 rounding to 0.84, so this is properly disclosed and harmless. Flagged only for completeness; optionally add one more displayed digit to σ to remove the apparent mismatch.

---

## Numbers verified clean (no action)

- Catalog totals and fractions: 8,474,688−157=8,474,531; CW+CCW=3,201,160; +5,273,371=8,474,531. ✓
- f_CW(C)=1,592,107/3,201,160=0.497353; dev −0.002647/2.795e−4=−9.47σ. ✓
- Catalog A: 0.507879, +28.72σ; A=1.576%; 2.98× suppression to −0.529%. ✓
- Slab 2.7σ (Round-A fix): (0.49735−0.49537)/7.4e−4=2.68; per-slab σ=√(0.25/457,308)=7.39e−4. ✓
- Fisher floor √(3/3,201,160)=9.7e−4=2√3·σ(f_CW); 3σ=0.29%; HC √(3/949,584)=1.78e−3→0.53%. ✓
- GZ1 confusion: CW 67.4% / CCW 72.4% → pooled 69.91%; diagonal 141,438/240,919=58.7%; 240,919−6,637=234,282; triage 27,435/144,640=19% (dual denominators 144,640 = all GZ1-spiral rows vs 117,205 = also-predicted-spiral reconcile correctly). ✓
- WLS: (4.55e−3−0.034)/1.63e−3=−18.1; naive /1.11e−4=−264.5; inflation 14.7×. ✓
- Monopole-mask: 1.6846/1.6961=99.32%; residual (1.6961−1.6846)/0.0068=+1.69σ; hemisphere (3.484−1.693)/0.405=+4.42σ. ✓
- MASTER apodized: (2.348e−5−1.71e−6)/2.99e−6=+7.28σ; 10⁴-perm (24.74−1.93)/3.12=+7.31σ. ✓
- Iye extension 3.2e6/1.27e5≈25; CE-ResNet 3.2M/1.95M≈1.6×. ✓

## Calibration items (not raised, per instructions)
June-2026 date current; arXiv refs valid; \artifact{}/blob/main links current; pseudo-label circularity bounded in §pseudolabel_independence with GZ1-only retrain deferred as a structural GPU follow-up; DOI deferred; 24pp length acceptable. The parity-even (not parity-violation) framing is handled honestly, and the title's "diagnostic evidence for a … canonical-mask residual" is an accurate, non-overclaiming description of the systematics-attributed +3.64σ.
