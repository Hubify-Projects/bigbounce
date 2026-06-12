# P4 R34conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v176.pdf` md5=baa9467c pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 98.6s

---

**Referee Report (Adversarial Review — PRD Standards)**

**Paper identifier (from rendered PDF):** P4 / R34conf  
**Title (abridged):** Survey-Scale Galaxy Chirality with Equivariant TTA… (8.47M DESI Legacy galaxies)

I have examined every page, figure, table, equation, caption, and the abstract. All quoted \(\sigma\), \(p\)-values, fractions, and amplitudes were recomputed from the displayed numbers where possible. The document contains pervasive internal-audit and version-control language that has no place in a journal submission.

### ESSENTIAL findings (paper cannot be accepted without removal/fix)

**P4-E1** (p. 1, abstract & title block)  
Text: “(Dated: June 11, 2026 — v1.0.176)”, repeated “artifact pipelines/… .json”, “R34conf” context, “earlier version of this paper reported… that result is withdrawn (Appendix A)”, “superseded”, “withdrawn sub-sample-mask null”.  
These are internal review logs and version artifacts. Required fix: complete excision of all such language, dates, commit hashes, and artifact paths from the submitted manuscript.

**P4-E2** (pp. 1, 4, 7–10, 15, 17–20; Tables I, III, IV)  
Multiple \(\sigma\) and \(z\) values from iso-boot, pp-shuffle, label-shuffle, depth-stratified, and generative-monopole nulls are placed side-by-side (e.g., Table I rows (i)–(vi), Table III \(\ell=1\) entries) without the explicit qualifier “not directly comparable” at every juxtaposition. Instruction 7 violation. Required fix: either remove all cross-null numerical comparisons or insert the qualifier in every table cell and every sentence that reports them.

**P4-E3** (abstract, p. 1)  
Claim: “to our knowledge, the largest chirality-labeled galaxy catalog to date: 8,474,531”. Body never demonstrates this is larger than every published catalog after identical quality cuts; the number is simply the post-QA parent sample. Required fix: either delete the superlative or supply a traceable comparison table.

**P4-E4** (abstract + p. 1 headline)  
Abstract states the real-space dipole is “consistent with null (+0.41\(\sigma\), empirical-rank \(p=0.31\))”. Body (p. 7) shows this uses the high-confidence subsample and isotropic-bootstrap null; the same page immediately reports a +7.28\(\sigma\) MASTER result on the identical catalog. The abstract therefore presents only the most favorable null while the body’s primary diagnostic is discrepant. Required fix: abstract must state both the real-space and MASTER results with equal prominence or remove the numerical claim.

**P4-E5** (pp. 2, 15, 16, 20)  
Multiple references to “earlier version”, “R7”, “R8”, “superseded”, “withdrawn”, and “artifact c11_…”, “c12_…”, “c16_…” files. These are review-process bookkeeping. Required fix: total removal.

### MAJOR findings (significant revision required)

**P4-M1** (pp. 1–22, entire document)  
22-page length for a null result whose headline claim is “no detection”. PRD typically expects \(\leq 12–14\) pages for such a focused systematics study. Required fix: condense to \(\leq 14\) pages or justify length.

**P4-M2** (Table I, p. 5; Table III, p. 11)  
Different null procedures (iso-boot vs. pp-shuffle vs. generative monopole) produce \(\sigma\) values that differ by factors of 2–20; the paper never quantifies how much of the spread is statistical versus methodological. Required fix: supply a dedicated section or table that decomposes the variance.

**P4-M3** (Fig. 8, p. 10; Table III)  
Pre-MASTER \(\ell=1\) power is reported as \(+3.64\sigma\) (canonical mask) while post-MASTER is \(+7.28\sigma\) (apodized). The factor-of-two inflation after mode-coupling deconvolution is never explained quantitatively. Required fix: explicit calculation showing how much of the increase is leakage versus signal.

**P4-M4** (p. 4, Eq. 2; p. 6, Fig. 2)  
TTA averaging is presented as the methodological cornerstone, yet the only quantitative validation is a 2,000-galaxy hold-out test showing \(\Delta P_{\rm CW}<0.0016\). No propagation of this uncertainty into the final dipole amplitude is given. Required fix: error budget that includes TTA variance.

**P4-M5** (abstract + p. 12, Sec. V.A)  
Abstract claims the result is inconsistent with Shamir’s 2–4\(\sigma\) detections “by a factor of \(\sim6–12\)”. The comparison uses different samples, different classifiers, and different nulls; no matched-footprint reanalysis is performed. Required fix: either perform the matched reanalysis or remove the quantitative factor.

### MINOR findings

**P4-m1** (p. 3, Fig. 1 caption)  
“\(p_{\rm eq}>0.9\)” cut shown in gallery but never used in any headline statistic. Cosmetic mismatch.

**P4-m2** (p. 5, Table I footnote a)  
\(f_{\rm sky}=0.4801\) vs. 0.49005 discrepancy between rows; explained only in a footnote that itself contains an arithmetic error (23,600 vs. 49,152 pixels). Minor numerical hygiene issue.

**P4-m3** (p. 9, Fig. 5)  
Log-scale spiral density map has no color-bar units or normalization stated in caption. Minor.

### NITs (cosmetic)

- Repeated “canonical canonical-mask” phrasing (pp. 4, 8).  
- Inconsistent use of “\(A_p\)” vs. “\(A\)” for amplitude.  
- Several figure captions truncated mid-sentence in the rendered PDF.

### Abstract-last drift sweep (pattern-045)

Every numerical claim in the abstract was traced:
- “8,474,531” matches body count (ok).  
- “+0.41\(\sigma\), \(p=0.31\)” matches only the HC real-space estimator; MASTER result omitted (ESSENTIAL drift).  
- “1.7% reference amplitude at \(z\approx-18\)” is the WLS template exclusion, not a detection threshold (misleading ordering).

### Provenance / reproducibility audit (patterns 046/047)

- Stale commit hashes and “v1.0.176” predate the stated June 2026 date.  
- Multiple artifact paths reference files whose sample definitions changed between versions (e.g., withdrawn sub-sample mask).  
- No frozen DOI or release tag for the exact catalog version used in the final numbers.

### Summary recommendation

**REJECT**

The manuscript in its present form is an internal working document containing review logs, version-control strings, withdrawn-result discussions, and inconsistent null-procedure comparisons that violate PRD standards for a clean, self-contained submission. Even after removal of those artifacts, the 22-page length, the selective presentation of the most favorable null in the abstract, and the absence of a quantitative error budget for the dominant TTA and leakage systematics would still require major revision. The scientific content may be salvageable, but the current document is not.