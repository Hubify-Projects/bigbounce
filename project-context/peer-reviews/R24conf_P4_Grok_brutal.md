# P4 R24conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v168.pdf` md5=90c4a8a3 pages=19
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 168.7s

---

**P4-E1 (ESSENTIAL)**  
Section: Abstract + p.1 (headline result)  
Problem: Abstract states “equivariant-catalog high-confidence dipole fit … gives +0.41σ (empirical-rank p = 0.31, 10^4 isotropic-null realizations)”. The body (Table I row i, p.4) shows this number is obtained only after an ad-hoc p_eq > 0.6 cut on a post-hoc “high-confidence” subsample; the full Catalog C real-space dipole is −0.265 % (Table II). The abstract therefore reports a secondary, threshold-dependent statistic as the headline result without stating the selection.  
Required fix: Remove the 0.41σ claim from the abstract or qualify it explicitly as a post-selection diagnostic on a 30 % subsample.

**P4-E2 (ESSENTIAL)**  
Section: p.1 (main text)  
Problem: “An earlier version of this paper reported a MASTER ℓ = 1 null on a subsample mask that a provenance audit traced to a synthetic-footprint catalog; that result is withdrawn (Appendix A)”. Explicit withdrawn-result language and “provenance audit” phrasing appear in the body.  
Required fix: Delete all such sentences; any correction history belongs in an unnumbered footnote or cover letter only.

**P4-E3 (ESSENTIAL)**  
Section: p.1, 4, 8–10 (multiple locations)  
Problem: σ values obtained from qualitatively different nulls (isotropic MC, block-bootstrap WLS, label-shuffle, depth-stratified, generative monopole-only) are placed in the same tables and paragraphs without the mandatory qualifier “not directly comparable” at every juxtaposition. Instruction 7 is violated.  
Required fix: Insert the qualifier in every table caption and every paragraph that mixes null families, or move all cross-null comparisons to a single dedicated subsection.

**P4-E4 (ESSENTIAL)**  
Section: p.2 (Introduction) + p.10 (Comparison)  
Problem: Paper repeatedly cites Shamir (2012, 2020, 2022) 2–4σ dipoles and claims the present 0.41σ result is inconsistent “by a factor of ∼6–12”. No matched-footprint reanalysis of Shamir’s catalog with the ViT+TTA pipeline is performed; the factor is therefore an apples-to-oranges comparison.  
Required fix: Either perform the matched reanalysis or remove all quantitative “factor of 6–12” statements.

**P4-M1 (MAJOR)**  
Section: p.19 (19 pages total)  
Problem: A null result whose dominant signal is a systematics floor is presented in a 19-page article. PRD norms for incremental null results with heavy diagnostic appendices are 8–12 pages.  
Required fix: Condense to ≤12 pages or justify length in cover letter.

**P4-M2 (MAJOR)**  
Section: Table I (p.4) and Table IV (p.10)  
Problem: The generative monopole-only null reproduces 99.32 % of the observed pre-MASTER C_ℓ power, yet the paper still quotes a “+3.64σ canonical-mask residual” as a headline diagnostic. The residual is therefore almost entirely the monopole leakage the authors themselves have quantified.  
Required fix: Relegate the +3.64σ number to a systematics budget table and state explicitly that it is not a cosmological detection.

**P4-M3 (MAJOR)**  
Section: Fig. 4 caption + p.6–7  
Problem: The color scale of the all-sky map is labeled in raw (N_CW − N_CCW)/(N_CW + N_CCW) units while the text repeatedly quotes amplitudes in the doubled A_p convention. Axis-label mismatch.  
Required fix: Unify convention in every figure and caption.

**P4-N1 (MINOR)**  
Section: p.1 (author affiliation)  
Problem: “Independent Researcher, Los Angeles, California, USA” with email houston@hubify.com. No institutional endorsement or conflict-of-interest statement.  
Required fix: Add standard COI paragraph.

**P4-N2 (MINOR)**  
Section: Multiple figure captions (Figs. 1–8)  
Problem: Captions contain internal file names (“c11_meta_e1_e2_realspace_nulls.json”, “artifact c9b”) and commit hashes.  
Required fix: Remove all repository-internal strings from captions.

**P4-NIT1 (NIT)**  
Duplicate phrasing on p.8: “canonical canonical-mask”. Typo only.

**Summary recommendation**  
REJECT

The manuscript contains multiple instances of withdrawn-result language, internal-audit phrasing, and inconsistent null-procedure comparisons that violate PRD presentation standards. The headline 0.41σ number in the abstract is a post-selection statistic whose relation to the primary full-catalog estimator is not disclosed. The paper is also substantially over-length for a systematics-dominated null result. These are not cosmetic issues; they are first-read rejection criteria.