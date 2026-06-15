# EXT18 — P4 External Review — Claude_brutal

- **Reviewer:** Claude_brutal (Claude Code sub-agent, Anthropic leg)
- **Note:** Supersedes the failed API leg (413 RequestTooLargeError). Run as a Claude Code sub-agent with full native-PDF read.
- **Paper:** P4 — Survey-Scale Galaxy Chirality (8.47M DESI Legacy galaxies; 3.2M spirals); null real-space chirality dipole
- **Round:** EXT18
- **Version:** v1.0.188 (frozen; 5 prior ACCEPT rounds)
- **Pages read:** 1–23 (full PDF, including all appendices A–E, all figures 1–9, Tables I–XI)

---

## Summary of read

Full read of the abstract verbatim, all figures, all tables, every equation, and the
appendix systematic battery. Arithmetic spot-checked throughout (counts, fractions,
confusion-matrix precision/recall, f_sky ratios). The paper is unusually disciplined
about separating the primary null (HC real-space dipole +0.41σ; block-bootstrap WLS
template exclusion z≈−18) from the systematics-attributed harmonic diagnostics
(+3.64σ / +7.28σ / +7.93σ), and repeatedly states they arise from distinct null
procedures and are not directly comparable as detection significances.

---

## ESSENTIAL findings

None.

---

## MAJOR findings

None.

---

## Targeted check of Grok's EXT18 flag (abstract qualifiers)

Grok's EXT18 report claimed the abstract omits the "not directly comparable /
diagnostic-only" qualifiers. **This flag is INVALID — the qualifiers are present
verbatim in the abstract.** Two explicit `Note:` clauses carry them:

1. After the +0.41σ and z=0.70 numbers: *"Note: the +0.41σ (isotropic-bootstrap
   null) and z=0.70 (per-galaxy label-shuffle null) values arise from distinct null
   procedures and are diagnostic-only, not directly comparable as detection
   significances. This ℓ=1 observable is parity-even ... not a direct
   parity-violation test."*
2. After the +3.64σ / +7.28σ / +7.93σ numbers: *"Note: the σ values quoted in this
   paragraph arise from distinct null procedures — see Sec. III A and Table III —
   and are not directly comparable as detection significances; they are diagnostic
   indicators only."*

The abstract also explicitly labels the MASTER channel "systematics-dominated ...
serves as a diagnostic," states the primary result is "consistent with null," and
gives the ≥5σ falsification criterion with the A_95 ∈ [1.0%, 1.5%] injection bracket.
The prior truth-audit conclusion stands; re-raising this would be a false positive.

---

## MINOR findings

- **M1 (verify, not fix).** Abstract and body both quote the harmonic diagnostics at
  three different σ (+3.64 / +7.28 / +7.93) from three different null-run sizes
  (500-MC / apodized / 10^4-perm). This is correctly disclosed everywhere I checked
  (abstract Note, Sec. IV D, Table III caption, Table IV). No action; flagged only so
  the truth-audit can confirm the three values are never summed or cross-compared as
  a common-axis significance. Body is clean on this.

- **M2 (cosmetic).** Fig. 8 caption quotes σ_{ℓ=1}=+3.63 (200-MC battery) while the
  surrounding text and Table III quote +3.64σ (500-MC) and +7.93σ (10^4). The caption
  states these "arise from distinct null procedures," so it is internally consistent,
  but a reader skimming figure vs. text sees +3.63 vs +3.64 vs +7.93 for nominally
  "the ℓ=1 canonical residual." Already disclosed; optional one-clause reminder in the
  caption that +3.63 is the 200-MC battery value specifically. Not blocking.

- **M3 (cosmetic).** Data Availability fixes the citable commit at 53b41d12 and tags
  the lineage "v1.0.185," while the title-page version/SSOT is v1.0.188. The text
  explains "subsequent same-day metadata and figure commits that do not alter analysis
  artifacts are not reflected in this pin by design," so this is intentional and
  self-documented, not an error. Truth-audit may wish to confirm the v1.0.185→.188
  delta is metadata-only per the stated policy.

---

## Arithmetic / count verification (all PASS)

- Spiral total: 1,592,107 (CW) + 1,609,053 (CCW) = 3,201,160 ✓
- Catalog total: 1,592,107 + 1,609,053 + 5,273,371 = 8,474,531 ✓
- CW fraction: 1,592,107 / 3,201,160 = 0.497353 → abstract "0.4974", Table II "0.497353(279)" ✓
- Training pool: 6,637 + 17,153 + 2,000 = 25,790; +826 flip-aug = 26,616; 21,293 + 5,323 = 26,616 ✓
- 17,153 / 25,790 = 66.5% ✓
- f_sky HC: 23,600 / 49,152 = 0.4801 ✓; canonical 0.49005 (Table VII) ✓
- GZ1 confusion (Table IX): CW precision 39,011/72,444 = 0.539 ✓; CW recall 39,011/71,615 = 0.545 ✓;
  CCW precision 42,928/(18,889+42,928+19,724)=0.527 ✓; chirality acc CW 39,011/57,900 = 67.4% ✓,
  CCW 42,928/59,305 = 72.4% ✓
- HC subsample N=949,584; HC-strict N=624,660; QC-flag rows 59,515 consistently quoted ✓
- Fisher floor Eq. (4): √(3/N_spiral) = √(3/3,201,160) = 9.68×10^-4 → "9.7×10^-4" ✓; = 2√3·σ(f_CW) ✓

No count, fraction, or confusion-matrix arithmetic error found. No leftover audit tags,
TODO markers, duplicated sentences, or broken cross-references detected.

---

## Injection-recovery floor (stated, PASS)

The 50%-recovery-at-3σ floor A_50 ≈ 0.75% is stated in the abstract, Sec. IV A, Sec. VI A,
Table V, and Fig. 9. The 95%-recovery falsification boundary A_95 ∈ [1.0%, 1.5%] is
explicitly "bracketed, not measured" (Table V caption disclaims the two-decimal claim).
The ≥5σ / A ≳ A_95 falsification criterion is in the abstract. Floor is honestly bounded.

---

## "Null dipole" claim is honestly bounded

The primary claim rests on TWO clearly-declared estimators: (i) HC real-space dipole
+0.41σ (p=0.31, isotropic-bootstrap null, N=949,584) and (ii) block-bootstrap WLS
template-fit exclusion of a clean 1.7% dipole at z≈−18. The harmonic +3.64σ/+7.28σ
residuals are consistently labeled non-primary, systematics-attributed, and tied to the
documented monopole-mask leakage channel + 8-anchor systematic battery (Appendix D).
The abstract, body, and conclusions agree. No overclaim of detection; the parity-even
caveat (ℓ=1 axial-vector, not a direct parity-violation test) is stated.

---

## FINAL VERDICT: **ACCEPT**

The abstract already carries every σ-comparability, diagnostic-only, and non-primary
qualifier; Grok's EXT18 flag is a false positive. Arithmetic is clean, the null is
honestly bounded, the injection-recovery floor is stated and disclaimed appropriately,
and abstract/body/conclusions are mutually consistent. The three MINOR items are
cosmetic/optional and none blocks publication.
