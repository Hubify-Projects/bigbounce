# P2 RA-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=8dabb71b pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (2285 chars)
**Wall time**: 130.1s

---

**Referee Report**

**Paper:** P2 (29 pages)

**Finding P2-E1 (ESSENTIAL, Abstract + Sec. IV p.9–10)**  
Abstract states “the realistic range is ∼2.6–5.5σ” while leading with the 5.2–5.5σ optimistic figure. Body (Sec. IV, Table IV) shows the 5.2–5.5σ value is obtained only before GR marginalization + \(b_\phi\) widening + photo-z degradation; the final all-combined conservative floor is 2.6σ. Abstract ordering and emphasis violate the body’s final calibrated statement.  
**Fix:** Rewrite abstract to lead with the post-systematics envelope and state the optimistic number only as an upper bound.

**Finding P2-E2 (ESSENTIAL, Sec. II p.3–4 + Sec. VII p.16)**  
All headline \(\sigma(f_\text{NL})\) values are derived from the Heinrich et al. (2024) Fisher matrix with a single scalar template-mismatch correction \(r=0.84\). No joint covariance among the six systematics in Table IV is ever computed. Additive quadrature is used without validation against a full marginalization. This is not a self-contained forecast.  
**Fix:** Either perform the joint marginalization or label every quoted significance “heuristic, not joint-covariance.”

**Finding P2-E3 (ESSENTIAL, length + contribution)**  
29-page sensitivity recast of an external baseline. PRD expects concise Letters or short articles for recasts. The novel content (null-space scan, Bayes-factor grid, MegaMapper outlook) occupies <8 pages; the remainder is re-derivation of Cai et al. and Heinrich et al.  
**Fix:** Condense to ≤15 pages or withdraw and resubmit as a focused methods note.

**Finding P2-M1 (MAJOR, Sec. VI p.12–14, Table II)**  
Bayes-factor table reports “BF∼9–14” under the \(r\to1\) endpoint while the abstract and Sec. IV use the noise-weighted \(r=0.84\) value. The two numbers are never reconciled in the same paragraph.  
**Fix:** State a single, consistently rebuked BF value everywhere or flag the \(r\to1\) column as “illustrative only.”

**Finding P2-M2 (MAJOR, Fig. 2 + Table IV p.16)**  
Error bars on the “MegaMapper” bars are labeled “illustrative 3–7σ design-uncertainty envelope.” No calculation or prior width is supplied for the 3–7 range. Caption and body disagree on whether this is a forecast or a stress test.  
**Fix:** Remove or replace with a quantitatively derived band.

**Finding P2-M3 (MAJOR, Sec. IIIB p.8)**  
Template-overlap factor \(r=0.84\pm0.02\) is computed in a 2-D flat-sky CMB-style estimator, then applied to the 3-D galaxy bispectrum Fisher matrix. No validation that the 2-D \(r\) equals the 3-D projection factor is shown.  
**Fix:** Demonstrate equivalence or recompute \(r\) inside the 3-D estimator.

**Finding P2-N1 (MINOR, multiple locations)**  
Repeated phrase “the realistic 2.6–5.5σ range” appears with inconsistent hyphenation and spacing; minor typographic cleanup required.

**Finding P2-N2 (NIT, Sec. I p.2)**  
Footnote “* houston@hubify.com” is split across lines; cosmetic.

**Finding P2-N3 (NIT, Table I caption)**  
“\(^a\)The folded row sits on the degenerate boundary” — the superscript placement is inconsistent with PRD style.

**Abstract drift sweep (after full read)**  
- “5.2–5.5σ optimistic” is traceable only to the pre-systematics Heinrich matrix (p.9).  
- “Bayes factor BF≈9” is traceable only to the \(\sigma_\text{eff}=0.7\) delta-prior cell (Table II). Both claims are weaker once the body’s final caveats are applied.  
**Required:** Abstract must be rewritten to match the body’s last calibrated statements.

**Provenance / reproducibility**  
GitHub link and Zenodo DOI are supplied, but the released scripts contain hard-coded Heinrich et al. Fisher matrices rather than the raw SPHEREx mock catalogs. No frozen commit hash for the exact version used in the paper is given.  
**Fix:** Add explicit commit hash and a one-line statement that the public release reproduces all tabulated numbers.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript is a lengthy sensitivity recast that imports its central Fisher matrix and most numerical results from two external works, applies a single scalar mismatch correction, and then combines systematics by unchecked quadrature. The abstract leads with optimistic figures that the body itself qualifies heavily. These are not cosmetic issues; they affect whether the claimed detection significances and Bayes factors can be trusted as stated. A substantially shortened, fully self-contained version that either performs the joint marginalization or explicitly labels all numbers “heuristic” would be required for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

**P2-E4 (ESSENTIAL, Table IV p.16)**  
The final two rows give explicit quadrature denominators \(\sqrt{0.9^2+1.0^2}=1.345\) and \(\sqrt{1.0^2+1.0^2}=1.41\), yet list detection significances \(\sim2.7\sigma\) and \(\sim2.6\sigma\). Direct division \(4.375/1.345\approx3.25\) and \(4.375/1.41\approx3.10\) do not reproduce the tabulated values (even after the \(r=0.84\) rescaling used elsewhere in the same table). The arithmetic is internally inconsistent.

**P2-E5 (ESSENTIAL, Sec. IV p.9 + Table IV)**  
The 5.2–5.5\(\sigma\) headline interval is obtained only with the noise-weighted central value \(r=0.84\) applied to the pre-systematics Heinrich matrix. The same paragraph then states the “realistic range \(\sim2.6\)–5.5\(\sigma\)” after systematics. These two intervals are generated from numerically incompatible null procedures (different effective \(\sigma_\text{eff}\) and different weighting schemes) yet are presented as a single continuous envelope without an explicit non-comparability qualifier.

**P2-M4 (MAJOR, Sec. II p.4 + Eq. (6))**  
The quoted uncertainty \(r=0.84\pm0.02\) is the standard deviation of the 10 000-sample distribution evaluated at fixed radius 50 in the six-dimensional coefficient ball. The text never shows that this radius corresponds to the physical scale at which the SPHEREx or MegaMapper Fisher matrices are evaluated; the \(\pm0.02\) is therefore an unvalidated extrapolation.

**P2-m1 (MINOR, Abstract + Sec. VI p.12)**  
The abstract states “Bayes factor BF\(\approx9\)” while Table II and the surrounding text give the range 9–14 only under the \(r\to1\) bookkeeping endpoint. The abstract therefore reports a value that the body itself labels illustrative rather than headline.

**P2-N4 (NIT, p.1)**  
The submission date “June 28, 2026” lies in the future; this is a placeholder that should have been updated.

**NO ADDITIONAL FINDINGS** on dimensional consistency, cross-reference accuracy, appendix–main-text mismatch, or unsupported novelty phrasing beyond the issues already catalogued.

The new arithmetic mismatch in Table IV and the unlabelled non-comparability of the two \(\sigma\) intervals are independent of the findings in the first review and directly affect the numerical claims that survive the requested revisions.