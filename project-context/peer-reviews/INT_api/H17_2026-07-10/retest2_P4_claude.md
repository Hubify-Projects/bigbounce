I have verified the new content thoroughly. The stratified-confusion table matches the committed JSON on every cell, internal arithmetic is consistent (14,093+26,894 = 32,550+8,437 = 40,987; +5,030 NS = 46,017 matched), the generator script is methodologically sound and honest (independent GZ1 human labels, Wilson/two-proportion CIs, DATA-UNAVAILABLE rather than fabricated void stratum), and the Shamir factor-of-2 correction (A_ref=0.017, z=−7.6, verified: (0.00455−0.017)/0.00163 = −7.64) is complete and consistent across abstract, intro, notation, the Appendix-D WLS table, and the bootstrap figure caption.

---

## Referee Report — P4 (chirality_catalog_paper.tex, v1.0.233)

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR]** *Sensitivity §, L1143–1146 / abstract L628.* The new stratified analysis's operative bound is the CI half-width — science-cut asymmetry CI ≈ ±0.42 pp (extent ≲0.6 pp), BASS+MzLS ≲1.4 pp (`tab:gz1_stratified`, verified against `outputs/gz1_stratified_confusion.json` `error_asymmetry_ci95`). A residual differential asymmetry of order ~0.6 pp maps to an A_p contribution comparable to A_50≈0.75% and the WLS best-fit 0.455%. The phrase "a leg-symmetric, parity-symmetric error *cannot manufacture a dipole at the A_p scale of the null*" (L1144–1146) is therefore slightly stronger than the CIs support and sits in mild tension with the authors' own correct qualifier "do not exclude a sub-percent differential asymmetry" (L1361). Recommend softening to "corroborates but does not fully close the differential-error channel at the sub-percent level."

2. **[MINOR]** *Appendix-B §, L1343–1361.* The test is a 2-bin dec-split (dec ≷ +32°) + confidence projection measured on the ~41k GZ1-overlap sample, which is not spatially uniform over the 8.5M-galaxy DESI footprint. A differential-error dipole *not* aligned with the leg-split axis (e.g. RA-varying error within a leg) is not directly bounded. The authors' argument that the imaging legs are "the dominant axis of spatial variation" is physically defensible (depth/PSF systematics track imaging campaigns) and the per-pixel gap is honestly disclosed — but the coarseness of a 2-cell projection as a *dipole* bound should be stated explicitly (one clause) rather than implied.

3. **[MINOR]** *Appendix-B §, L1352 / L1355 vs Training-Labels §, L691.* The stratified subsample accuracy (overall 0.912, science-cut 0.961) is far above the paper's headline conservative GZ1 chirality-accuracy floor (0.6991, κ=0.40) that feeds the dilution factor g. Both are correct (different subsample: confident spirals with NS triaged out vs the full disjoint match), but a reader can conflate them. Add a one-line note that 0.912 is the confident-spiral ∩ classifier-CW/CCW accuracy, not a revision of the 0.6991 floor used for g.

*No MAJOR issues.* The new analysis is correct, artifact-backed, and non-fabricated; the Shamir factor-of-2 correction is mathematically right (A_p = 2(f_CW−½) = (N_CW−N_CCW)/(N_CW+N_CCW) = Shamir's asymmetry exactly, so 1.7%→A_ref=0.017 with no rescaling) and fully propagated; the direction of the correction (z −18 → −7.6) honestly *weakens* the headline.

**(3)** Yes — the central claim (a null large-scale chirality dipole, +0.41σ / p=0.31 real-space primary) is supported, and the new leg/confidence-stratified confusion analysis materially strengthens the systematics-control argument by showing the only dipole-biasing channel (CW↔CCW error asymmetry) is consistent with zero in every stratum, with the three minor items above being precision/scoping tightenings rather than threats to the result.
