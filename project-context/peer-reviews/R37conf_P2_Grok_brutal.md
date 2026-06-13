# P2 R37conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.60.pdf` md5=a961bf1c pages=27
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 80.3s

---

**Referee Report**

**Paper:** P2  
**Journal target:** Phys. Rev. D  
**Round context:** First read (adversarial)

### ESSENTIAL findings

**P2-E1**  
**Section:** Abstract (p. 1) + §IV (p. 9)  
**Problem:** Abstract states “realistic range is ∼2.6–5σ” while the body headline (and Fig. 2) foregrounds the 5.2–5.5σ optimistic window before GR + b_φ systematics. The 2.6σ conservative floor is only reached after adding four systematics in quadrature; the abstract ordering therefore presents the most favorable number first.  
**Required fix:** Rewrite abstract sentence to lead with the post-systematic range (2.6–5σ) and state the optimistic ceiling only as an upper bound. Add explicit qualifier “under the full systematic budget of Table IV.”

**P2-E2**  
**Section:** Abstract (p. 1) + §II (p. 4)  
**Problem:** Abstract claims “a local estimator recovers 84%–88% of the bounce signal.” The quoted interval is the range of the 10 000-sample null-space scan at radius 50; the headline noise-weighted central value used everywhere else is r = 0.84 ± 0.02. The abstract therefore reports an internal diagnostic rather than the number propagated into all σ forecasts.  
**Required fix:** Replace the interval with the single central value and uncertainty that actually enters Eqs. (5)–(6) and Table IV.

**P2-E3**  
**Section:** §IV (p. 9) + Table IV (p. 19)  
**Problem:** The 2.6–5σ “realistic range” is obtained by adding four systematics in quadrature after the fact. No joint multi-parameter Fisher matrix or Monte-Carlo marginalization over the full set {r, b_φ, σ_GR, photo-z outlier fraction} is shown. The quoted interval is therefore an approximate envelope, not a statistically rigorous posterior width.  
**Required fix:** Either (a) publish the full 4-parameter Fisher matrix and its eigenvalues or (b) replace the interval with the single conservative number obtained from the joint analysis.

**P2-E4**  
**Section:** §VI (p. 11–12) + Table II (p. 14)  
**Problem:** Bayes-factor headline BF ≈ 9–14 is obtained only after the r → 1 “bookkeeping” rescaling that forces the local-template estimator to recover the full amplitude. The raw (un-rescaled) BF values are 4–7. The abstract and §VI present the rescaled numbers as the primary result.  
**Required fix:** Report both raw and rescaled BF side-by-side in the abstract and Table II, with an explicit statement that the rescaling is an interpretive choice, not a data-driven correction.

### MAJOR findings

**P2-M1**  
**Section:** Entire manuscript (27 pages)  
**Problem:** The paper is a sensitivity recast of existing SPHEREx/MegaMapper forecasts plus one new local-template overlap calculation. PRD page limits for incremental forecast papers are typically 12–15 pages. The present length is driven by extensive internal cross-checks and null-space scans that belong in appendices or a companion methods paper.  
**Required fix:** Reduce main text to ≤ 16 pages; move §§II, VI, and the four-corner Bayes-factor grids to appendices.

**P2-M2**  
**Section:** §II.C (p. 6) + assumption (d)  
**Problem:** The claim that f_NL = −35/8 is “robust within the scalar-only Einstein-Cartan-Holst class” rests on the unverified statement that the cubic-order bispectrum transmission holds at linear order only. No explicit numerical check of the four cubic integrals at next-to-leading order in the bounce is provided.  
**Required fix:** Either perform the four-integral evaluation or downgrade the claim to “conditional on assumption (d) verified only at linear order.”

**P2-M3**  
**Section:** §VII.B (p. 16) + Fig. 5  
**Problem:** The b_φ degradation curves assume a universal 20% prior width per redshift bin. No justification is given for this number beyond “optimistic.” When the prior is relaxed to 50%, the significance drops below 4σ even before GR marginalization.  
**Required fix:** Replace the single 20% curve with a shaded band spanning the range of published b_φ calibration uncertainties (Barreira et al. 2023 and references therein).

**P2-M4**  
**Section:** §III.B (p. 8)  
**Problem:** The injection-recovery test uses only 200 realizations and a flat-sky CMB-style estimator, not the full 3-D SPHEREx window and mask. The quoted r_meas = 0.90 ± 0.01 is therefore an upper bound on performance.  
**Required fix:** Either increase the Monte-Carlo suite to ≥ 1000 realizations with the actual SPHEREx mask or qualify the result as “optimistic flat-sky test.”

### MINOR findings

**P2-m1**  
**Section:** Table I caption (p. 5)  
**Problem:** Footnote “a” states the folded configuration is evaluated “as the limit of the sequence k1 = 2k, k2 = k3 = k,” but the numerical value −2.250 is taken directly from the squeezed-limit formula. The two limits are not identical; a 0.3% difference appears when the exact folded kinematics are used.  
**Required fix:** Recompute the folded entry with the exact triangle and update the table.

**P2-m2**  
**Section:** §VIII.A (p. 18)  
**Problem:** Recast of Planck PR4 + DESI numbers uses the older Chaussidon et al. (2024) LRG bound; the newer Fondi et al. (2025) QSO assembly-bias result is cited only in passing.  
**Required fix:** Update the combined constraint with the most recent DESI QSO number.

**P2-m3**  
**Section:** Data Availability statement (p. 23)  
**Problem:** The GitHub link is given without a frozen commit hash or Zenodo DOI. The statement “all forecast sensitivities are adopted from published analyses” is therefore not reproducible from the repository alone.  
**Required fix:** Add commit hash and Zenodo DOI for the exact version used to generate every number in Tables II–IV.

### NIT findings

**P2-n1**  
**Section:** Abstract (p. 1)  
**Problem:** “Dated: June 13, 2026” appears in the author block. This is future-dated relative to any realistic submission.  
**Required fix:** Remove or correct.

**P2-n2**  
**Section:** Fig. 3 caption (p. 11)  
**Problem:** The vertical error bar on the bounce point is labeled “SPHEREx 1σ” but the plotted value is the pre-systematic 0.7; the post-systematic 1σ is never shown on the same figure.  
**Required fix:** Add a second error bar or remove the label.

**P2-n3**  
**Section:** Multiple locations  
**Problem:** Inconsistent use of “bounce” vs. “matter bounce” in section headings; the title uses the latter.  
**Required fix:** Standardize terminology.

## Summary recommendation

**MAJOR REVISIONS**

The manuscript contains a technically competent local-template overlap calculation and a thorough (if lengthy) enumeration of systematics. However, the headline detection significance and Bayes-factor claims are presented in their most optimistic form, the statistical treatment of the joint systematic budget is approximate rather than joint, and the paper is substantially over-length for its incremental contribution. These issues are correctable but require a major rewrite and re-computation before the paper meets PRD standards for a forecast methods article.