# P5 EXT20 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=3e5d3757 pages=32
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 114.4s

---

**REFEREE REPORT — Physical Review D**

**Manuscript:** "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample" (P5)

**Recommendation:** REJECT

The manuscript is not publishable in its current form. It contains pervasive internal-audit artifacts, violates the standalone-reader requirement, is grossly over-length for its actual scientific content, and presents a null result whose statistical framing is not self-contained. The core claim (no environment-dependent chirality signal beyond the Paper IV monopole) is plausible but cannot be evaluated from the submitted document.

### ESSENTIAL findings (paper cannot be accepted without correction)

**P5-E1 (Title page–p. 32, throughout)**  
The manuscript is riddled with internal pipeline paths, JSON artifact filenames, and version-control strings ("pipelines/p5_desi_chirality/outputs/…", "21_r23conf_meta_closures.json", "30_ext4_galzone_complement_contrasts.json", etc.). These appear in the body text, figure captions, and table notes. This is internal bookkeeping, not journal content. Required fix: complete excision of every pipeline/artifact string.

**P5-E2 (Abstract + §I, §II, §VIII–XIII)**  
The paper is not standalone. Every load-bearing claim (monopole offset, \(\Delta f_{\rm CW} = -0.0026\), per-class \(\sigma\) values, DESIVAST vs T-Web comparison) is imported from or cross-referenced to "Paper IV (in preparation)". No arXiv number or published reference is supplied. A PRD reader cannot evaluate the result without the companion. Required fix: either publish Paper IV first or make the present work fully self-contained.

**P5-E3 (Abstract vs body drift)**  
Abstract states "no evidence for environment-dependent chirality beyond the catalog-wide classifier-monopole offset at current sensitivity." The body repeatedly qualifies this with survey-edge artifacts, small-\(n\) void-bin dominance, and the fact that the T-Web void bin (\(n=428\)) is counting-noise limited. The abstract omits these caveats. The stronger phrasing in the abstract is not supported by the final calibrated statements in §§VI–VIII.

**P5-E4 (Non-comparable \(\sigma\) values)**  
Multiple \(\sigma_{\rm from half}\) and \(\sigma_{\rm pred}\) values are presented side-by-side (Tables III, V, VII, X, XII) without an explicit, repeated statement that they are not directly comparable because they use different nulls or different \(N\). This violates the journal's requirement for unambiguous statistical presentation.

**P5-E5 (Length)**  
32 pages for a null result whose headline is "consistent with no environmental signal" is disproportionate. The actual scientific payload (one new cross-match + three-algorithm robustness test) does not justify the length.

### MAJOR findings

**P5-M1 (§III–IV)**  
The T-Web implementation is described via 12 numbered steps that still require the reader to consult external pipelines for the precise Fourier conventions and eigenvalue normalization. The \(\lambda_{\rm th}=0\) choice and \(R_s=25\,h^{-1}\) Mpc scale are presented as canonical without a quantitative justification that other reasonable choices were exhaustively explored before the headline result was fixed.

**P5-M2 (Fig. 8 & Table XI)**  
The "0 maximal voids per pixel" bin is used as a proxy for DESIVAST coverage, yet the paper never quantifies the fraction of that bin that lies inside the BGS footprint but outside any DESIVAST hole. The \(-4.75\sigma\) claim therefore mixes a coverage artifact with a potential chirality signal.

**P5-M3 (§VIII, Table VIII)**  
The DESIVAST void sample (\(n=56{,}981\)) is only 6 galaxies larger than the T-Web void sample after the \(z\le0.24\) cut. The paper treats the two as independent robustness checks when they are almost the same objects. The claimed "three-algorithm" independence is overstated.

**P5-M4 (Abstract scalars)**  
The abstract quotes \(n=56{,}981\) void spirals. This number appears only after the DESIVAST re-projection; the T-Web headline result uses \(n=428\). The abstract therefore advertises a number that does not correspond to the primary statistical test.

### MINOR / NIT findings (representative sample)

**P5-m1** Duplicate phrasing ("canonical canonical-mask") appears in at least two pipeline captions.  
**P5-m2** Several tables report \(\sigma\) to three decimals while the underlying binomial counts yield only two meaningful figures (e.g., Table III, void bin).  
**P5-m3** Citation to "Paper IV v1.0.166" uses an internal version tag rather than a stable identifier.  
**P5-m4** Fig. 6 Mollweide projection lacks an explicit statement that the color scale is truncated at \(\pm4.5\sigma\); the eye is drawn to the high-\(|\sigma|\) pixels that are actually consistent with the label-shuffle null.

### Summary recommendation

**REJECT**

The manuscript cannot be reviewed on its scientific merits until the internal-audit scaffolding is removed, the dependence on an unpublished companion paper is resolved, and the statistical presentation is made unambiguous and self-contained. The present version reads as an internal technical report rather than a finished journal article. A substantially shortened (≤12–14 page), fully standalone resubmission that reports only the DESIVAST-anchored cross-check and its three-algorithm robustness test would be a more appropriate vehicle for this null result.