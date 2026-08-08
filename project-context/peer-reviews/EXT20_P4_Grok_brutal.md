# P4 EXT20 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 106.8s

---

**REFEREE REPORT — Physical Review D**

**Manuscript:** Survey-Scale Galaxy Chirality with Equivariant TTA… (P4)  
**Round:** First submission (external)  
**Reviewer:** Adversarial

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P4-E1** Abstract (p. 1) & Sec. IV C (p. 7)  
The abstract states the primary result as “a real-space chirality dipole consistent with null: … +0.41σ”. Table I and the surrounding text present +0.41σ (isotropic-bootstrap), +0.70 (label-shuffle), and +3.64σ (MASTER) side-by-side without the explicit qualifier “not directly comparable as detection significances” at every juxtaposition. Per instruction 7 this is ESSENTIAL.  
*Fix:* Insert the qualifier in the abstract and in every table/figure caption that reports multiple null procedures.

**P4-E2** Abstract (p. 1) vs. body (pp. 4–5, 9–11)  
Abstract claims “diagnostic evidence for a Depth/Morphology-Correlated Canonical-Mask Residual”. The body (Sec. IV D, Appendix D) shows this residual is systematics-attributed and is *not* interpreted as a cosmological signal. The abstract sentence is therefore stronger than the final calibrated body statement.  
*Fix:* Rewrite abstract sentence to match the body’s explicit “systematics-attributed, not cosmological” language.

**P4-E3** Throughout (especially pp. 2, 9, 15–16, 19)  
Dozens of internal artifact strings (“artifact c11…”, “pipelines/p2_chirality/…”, “c12_r24conf…”, commit hashes, “R7/R8” style tags) appear in the main text and figure captions. These are internal bookkeeping and violate the standalone-reader test.  
*Fix:* Remove all such strings from the body; move only essential reproducibility information to a clean Data Availability section.

**P4-E4** Length (23 pages)  
A null result whose central claim is “consistent with null at sub-percent level after exhaustive systematics audit” does not justify 23 journal pages. PRD norm for such a systematics-limited null is a Letter (≈4–6 pages) or a concise methods paper.  
*Fix:* Reduce to ≤8 pages or re-submit as a methods-focused article.

**P4-E5** Abstract load-bearing scalars (p. 1)  
“8.47 million DESI Legacy galaxies (3.2 million spirals)” and “+0.41σ” cannot be recomputed from the displayed numbers without external artifacts. The 3.2 M spiral count is stated only after quality cuts whose exact definition is referenced to non-public scripts.  
*Fix:* Provide a self-contained one-paragraph derivation of every abstract number in the body.

### MAJOR findings

**P4-M1** Sec. I & V (pp. 2, 12)  
Claims of “largest chirality-labeled catalog to date” and “inconsistent with Shamir’s ~3 % signal by a factor of ~6–12” rest on a single pipeline. No matched-footprint reanalysis of Shamir’s catalog is performed. The factor 6–12 is therefore not independently verified.

**P4-M2** Fig. 4 & Sec. IV C (p. 8)  
The canonical-mask ℓ=1 residual is reported as +3.64σ (label-shuffle) yet is interpreted as “not a cosmological null”. The figure caption and text never state the effect size in fractional amplitude (Aₚ units) alongside the σ value, violating instruction 19.

**P4-M3** Table III (p. 11)  
Multiple C_ℓ bands are shown with z and rank-p values derived from different null procedures. No effect-size column (e.g., fractional power excess) is supplied.

**P4-M4** Data Availability (p. 21)  
Commit hash 53b41d12 is dated June 2026 (future date relative to submission). The DOI is listed as “not yet minted”. This violates provenance audit requirements.

### MINOR findings

**P4-m1** Sec. II B (p. 2)  
Training-label provenance mixes GZ1 human labels, CE-ResNet pseudo-labels, and synthetic negatives without a single consolidated table of label-source fractions.

**P4-m2** Fig. 2 caption (p. 6)  
States “flip-swap correlation = 1.000 by construction” but the accompanying text (p. 4) shows per-galaxy flips of 21.4 % on borderline objects. Caption is therefore imprecise.

**P4-m3** References  
Several arXiv IDs are given without journal updates (e.g., ref. 5, 6). Minor but required for PRD.

### NITs

- Duplicate phrasing “canonical canonical-mask” appears once (p. 9).  
- Axis labels on Fig. 8 use “C_ℓ × 10^{-6}” without explicit units.  
- Page numbers in the table of contents are off by one for Sec. VII.

## Summary recommendation

**REJECT**

The manuscript presents a technically elaborate null result whose central scientific claim is already known to be systematics-limited. The 23-page length, pervasive internal artifact language, repeated juxtaposition of non-comparable significance numbers, and abstract–body drift on the interpretation of the mask residual constitute multiple independent grounds for rejection on first read. A drastically shortened (≤8 page) version that removes all internal bookkeeping, supplies a single consistent null convention, and matches abstract wording exactly to the body’s final calibrated statements could be reconsidered as a Methods or Instrument paper, but the present submission does not meet PRD standards.