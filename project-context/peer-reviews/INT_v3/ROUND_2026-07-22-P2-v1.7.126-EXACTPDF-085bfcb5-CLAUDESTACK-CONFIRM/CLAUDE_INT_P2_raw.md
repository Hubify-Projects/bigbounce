# Claude INT Referee Report — Paper P2 (EXACT-PDF)

- **Paper:** "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping"
- **Author:** Houston Golden (Independent Researcher)
- **Version:** v1.7.126, Dated July 20, 2026, 13:24 PDT; PDF CreationDate Mon Jul 20 13:32:45 2026 PDT; 11 pp.
- **Target:** Physical Review D
- **PDF path:** research/focused_paper_source_integration/02_full_draft.pdf
- **Recorded sha256:** 085bfcb5bce450423efe8989c621a9b493f8e725bf9330c29e45d7b46a5fd5e7
- **Computed sha256:** 085bfcb5bce450423efe8989c621a9b493f8e725bf9330c29e45d7b46a5fd5e7
- **BINDING:** MATCH (exact-PDF binding confirmed; reviewing the bound bytes)
- **Reviewer:** Claude INT leg (Opus), CLAUDESTACK-CONFIRM round

---

## Summary

This is a careful, heavily caveated derivation paper. Its primary claim — the exact
matter-contraction local amplitude f_NL^local = -35/16 = -2.1875 — is documented with
multiple independent cross-checks and is internally consistent to the level a PRD
referee can audit from the manuscript. The observational SPHEREx mapping is explicitly
framed throughout as illustrative/conditional, not a headline forecast; that framing is
honest and repeated in abstract, body, and conclusion. The archival statement is
transparent (discloses that Zenodo holds v1.7.125 while the manuscript is v1.7.126).
All headline numbers reproduce arithmetically. I found no BLOCKER and no MAJOR error.
A handful of MINOR reproducibility/rounding nits remain.

## Verification performed

**Amplitude lineage (f_NL = -35/16):**
- Eq (2) B_NL = (10/3) A_T / Σk_i^3 → -35/16 in squeezed limit. ✓
- Table I: -35/16 = -2.1875 ✓; -255/128 = -1.9922 ✓; -9/8 = -1.125 ✓. Stated as exactly
  one-half of Cai et al. (-35/8, -255/64, -9/4) — each ratio confirmed ✓.
- Eq (3)/(4) coefficient vector (3,1,-9,5,-33,9): verified against Fig 1 render and Eq (B4).
- Eq (B4) 256 Πk² A = 9Σk⁹ + 3Σk⁷k² - 27Σk⁶k³ + 15Σk⁵k⁴ - 198Σ_dist k⁵k²k² + 27Σk⁴k³k².
  Confirmed = 3·K9 in the distinct-monomial convention: the (5,2,2) ordered coeff -33
  → -66 per distinct monomial × overall 3 = -198. All six coefficients consistent with
  Eq (3). ✓ The (5,2,2) multiplicity bookkeeping (six ordered / three distinct) is
  internally coherent.
- **Eq (B5) ε-order decomposition [visually verified via pdftoppm page 9]:**
  f_NL|ε1 = **-5/2**, f_NL|ε2 = +5/16, f_NL|ε3 = 0. Sum = -40/16 + 5/16 + 0 = **-35/16**. ✓
  (NOTE: pdftotext garbled -5/2 into "-25/16", which would NOT sum correctly; the actual
  rendered PDF prints -5/2 and the arithmetic is correct. No error in the PDF.)
- **Table V column sums [text]:** squeezed -25/16, -5/32, 0, -15/32 → -70/32 = -35/16 ✓;
  equilateral -35/32, -5/32, -5/8, -15/128 → -255/128 ✓.
- -305/64 reduction: -35/16 shifted by -(10/3)(99/128) = -2.578 → -4.766 = -305/64 ✓;
  Eq (B2) spurious -(99/128)Σk_i^3 term consistent throughout Appendix B.
- Li et al. Eq (5.1): f_NL = -165/16 + 65/(8c_s²) → -35/16 at c_s = 1 ✓.

**Observational mapping (transmission, Fisher, transmission coefficients):**
- 2.63σ headline: |f_NL|·r/0.7 with r=0.84 → 2.1875·0.84/0.7 = 2.625 → 2.63σ ✓;
  with r=0.8354 → 2.611 → 2.61σ ✓ (both shown); naive ratio 2.1875/0.7 = 3.125 → 3.13σ ✓.
- r = 0.83542294, rcos = 0.98167825 (body) match abstract 0.8354 / 0.9817 ✓.
- Table III surrogate ladder 3.47/3.14/2.32/0.42σ → f_NL/σ with σ = 0.631/0.697/0.941/5.173:
  2.1875/0.631=3.47 ✓, /0.697=3.14 ✓, /0.941=2.32 ✓, /5.173=0.42 ✓. Abstract/Sec VII
  rounded values 3.5/3.1/2.3/0.4σ all consistent ✓.
- Torsion Eq (5) prefactor (35/16)(3/16)γ²/(1+γ²): γ=0.2375 → 0.022 ✓, γ=1 → 0.21 ✓.
  As fraction of |f_NL|=2.1875: 0.022→1.0%, 0.21→9.6% → "~1-10%" claim CONSISTENT ✓
  (the 0.022–0.21 are absolute δf_NL, not fractions).
- Sec VI: |f_NL^bounce|/0.015 = 2.1875/0.015 = 145.8 → ≈146 ✓ (Table II ✓).
  Slow-roll f_NL = (5/12)(1-ns) with ns≈0.964 → 0.015 ✓.
- Transmission: |δf_NL| ≤ 6.8e-8 at kη_B=1e-2, |T_c-1| = 2.7e-10 to 2.2e-5; internally
  order-consistent with "~4 orders below the earlier 1e-3 residual" ✓ (from cited artifacts).

**Version/date/archival:**
- Version stamp v1.7.126 on page 1 matches binding ✓.
- DOI https://doi.org/10.5281/zenodo.21461881 RESOLVES via curl: 302 → zenodo.org/records/21461881 → 200 OK ✓.
- Concept DOI 10.5281/zenodo.21461880 cited as resolving to latest; primary DOI verified.
- Honest disclosure that archived deposit is v1.7.125 (one patch behind this v1.7.126) ✓.

**LaTeX hygiene:** 0 Overfull hboxes in log; Fig 1 and Fig 2 embedded; no column overflow
observed in page renders (pp 1, 2, 8, 9).

## Findings

### BLOCKER
None.

### MAJOR
None.

### MINOR
1. **reff not reproducible from quoted σ's (Sec IV.B, real-space).** "local-template
   uncertainty 0.626 (bias fixed) ... bounce-template 0.631 ... reff = 0.9929." A direct
   ratio 0.626/0.631 = 0.9921, not 0.9929 (4th-decimal disagreement). Within rounding of
   the 3-decimal displayed σ's, and the paper explicitly states reff uses a different
   inner product than r, so this is not an error — but a reader cannot reproduce reff from
   the printed numbers. Recommend quoting the σ's to 4 decimals or giving reff's defining
   inner-product formula. (Same applies to the 0.687/0.688 → 0.9986 pair.)

2. **Planck consistency "0.37σ" (Sec VIII).** From the quoted bounce-coordinate values
   -0.11 ± 5.71, the deviation from -2.1875 is (2.1875-0.114)/5.708 = 0.363 → 0.36σ, not
   0.37σ. Trivial rounding, but the printed value is one unit off in the 2nd decimal.

3. **"34.7% ... (0.687 → 0.449)" (Sec IV.B).** The 34.7% figure is computed from the
   bounce-template real-space value 0.688 → 0.449 [(0.688-0.449)/0.688 = 34.7%], but the
   parenthetical cites the local real-space value 0.687 [(0.687-0.449)/0.687 = 34.6%].
   Cosmetic baseline-labeling mismatch; align the parenthetical to the bounce value used.

4. **"2.61σ ... rounded to 2.63σ for the adopted r = 0.84" (Sec IV, Sec VII).** 2.63 is a
   recomputation with r=0.84, not a rounding of 2.61; wording "rounded" is imprecise
   (the rounding is in r: 0.8354 → 0.84, which then yields 2.63). Also note the adopted
   rounded r nudges the headline up (2.61 → 2.63); fully disclosed and inside the stated
   ±0.02 envelope, so acceptable, but the "rounded to" phrasing could be tightened.

## Assessment

The core derivation is sound, cross-checked four independent ways (exact four-vertex sum,
Cai ε-order intermediates, Li general-c_s formula, per-vertex Table V column sums), and
every quantitative claim I could audit reproduces. Conditional-claims honesty is a
strength: the paper repeatedly and correctly subordinates the observational numbers to
their assumptions. The remaining items are polish/transparency nits, none affecting any
conclusion. Recommend acceptance after the author addresses the four MINOR items (chiefly:
make reff reproducible from the printed uncertainties, and fix the 0.37σ/0.36σ and
34.7%/34.6% rounding-label nits).

VERDICT: MINOR-REVISIONS
