# P4 RP4-INT-v200 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=a644743f pages=25
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 92.7s

---

**Referee Report**

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA… (P4)

**Journal:** Physical Review D

**Finding P4-E1 (ESSENTIAL)**  
Section: Abstract (p. 1) and Sec. IV.C (p. 8–9)  
Problem: Abstract states the primary real-space dipole is “consistent with null” at \(z = +0.41\sigma\) while simultaneously quoting the MASTER \(\ell=1\) value \(+3.64\sigma\) without repeating the explicit qualifier “these \(\sigma\) values … are not directly comparable as detection significances” at the juxtaposition. The same side-by-side presentation occurs in Table II (p. 5) and the text on p. 10.  
Required fix: Insert the qualifier sentence immediately after every numerical comparison of distinct-null \(\sigma\) values in the abstract, main text, and all tables/figures that contain them.

**Finding P4-E2 (ESSENTIAL)**  
Section: Abstract (p. 1)  
Problem: The sentence “the low-confidence tail (\(p_\text{eq}\le0.5\)) shows a systematics-attributed excess (\(z\approx4.0{-}4.3\))” is stronger than the body’s final calibrated statement (p. 9), which attributes the excess to the low-confidence tail of a depth/morphology-correlated classifier bias and never claims a physical signal.  
Required fix: Rewrite the abstract sentence to match the body’s final wording exactly, including the explicit “systematics-attributed” and “not a cosmological signal” clauses.

**Finding P4-M1 (MAJOR)**  
Section: Entire manuscript (25 pages)  
Problem: The paper is far too long for a null-result methods paper. Core scientific claim (null dipole at the survey scale) plus the necessary null tests can be presented in \(\le12\) pages; the remaining 13 pages consist of internal diagnostic tables, eight-anchor systematic batteries, and per-null recomputations that belong in Supplemental Material.  
Required fix: Reduce main text to \(\le12\) pages; move Tables IV–XII, Figs. 8–9, and Appendices C–E to Supplemental Material.

**Finding P4-M2 (MAJOR)**  
Section: Sec. IV.D and Appendix D (p. 11–13, 21–22)  
Problem: The \(+3.64\sigma\) canonical-mask residual is presented as a “diagnostic” yet is used to argue that the harmonic-channel leakage is “non-primary.” No quantitative statement of the practical effect size (fraction of pre-MASTER power reproduced by the generative monopole-only null = 99.32 %) is given in the main text; only the \(\sigma\) value appears.  
Required fix: Add an explicit effect-size sentence in Sec. IV.D: “The generative monopole-only null reproduces 99.32 % of the observed pre-MASTER \(\ell=1\) power (residual \(+1.69\sigma\)).”

**Finding P4-M3 (MAJOR)**  
Section: Data Availability (p. 23)  
Problem: The release tag “v2026.04” and the statement that a “frozen release tag and a Zenodo DOI will be deposited at journal submission” are inconsistent with a finished manuscript. No commit hash or immutable archive snapshot is supplied.  
Required fix: Provide the actual immutable Zenodo DOI and the exact git commit hash used for all quoted numbers.

**Finding P4-N1 (MINOR)**  
Section: p. 1 (author affiliation line)  
Problem: “(Dated: June 30, 2026)” is a future date appearing in the published PDF.  
Required fix: Remove or correct the date string.

**Finding P4-N2 (MINOR)**  
Section: Table I caption (p. 5)  
Problem: Minor typographic inconsistency: “\(N=10^4\)” vs. “\(10^4\)-permutation” in adjacent rows.  
Required fix: Standardize notation.

**Finding P4-NIT1 (NIT)**  
Multiple figure captions repeat the phrase “not directly comparable as detection significances.” While correct, the repetition is cosmetic.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a technically thorough null result. However, it violates PRD standards on length, on the requirement that every juxtaposition of distinct-null significances carry an explicit comparability warning, and on the requirement that the abstract never exceed the final calibrated claim in the body. These are not cosmetic issues; they affect readability, statistical interpretation, and reproducibility. A substantially shortened version that moves the internal diagnostic machinery to Supplemental Material, together with the two ESSENTIAL textual fixes, would be required before the paper could be reconsidered.