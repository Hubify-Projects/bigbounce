# EXT1 P4 — ChatGPT Pro Extended referee report
**Provider**: chatgpt.com web app (Big Bounce Book project) · intelligence **Pro Extended** (GPT-5.5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37
**PDF**: chirality_catalog_paper_v171.pdf (md5 2f0317c4) · **Harvested**: 2026-06-10T17:05 PDT

---

Show more
Thought for 9m 13s
Referee report on Paper 4 v1.0.171

Recommendation: MAJOR REVISIONS

I read the full 21-page PDF and spot-checked the public source/artifact paths at the commit stated in the paper. The core result may be publishable: a large chirality-labelled catalogue with a high-confidence real-space null, a useful demonstration of monopole-mask leakage, and a serious attempt to separate cosmological and survey-systematics channels. However, I cannot recommend acceptance in the present form. Several load-bearing claims are undermined by reproducibility/version mismatches and by inconsistent treatment of the post-MASTER harmonic diagnostics. The paper is fixable, but only after the authors freeze an exact source/artifact release and rewrite the harmonic-systematics interpretation around what the released artifacts actually show. 

chirality_catalog_paper_v171

PDF line numbers were not available, so I cite page/section/table/figure locations. Where I inspected the public .tex or JSON artifacts, I cite the public source lines.

Summary assessment

The paper’s most defensible scientific statement is the high-confidence real-space chirality dipole null: Catalog C with p
eq
	​

>0.6, N≃9.5×10
5
, gives +0.41σ, with a per-galaxy label-shuffle check remaining null. The paper also persuasively shows that a small global classifier monopole can leak into low-ℓ pseudo-C
ℓ
	​

 on a patchy mask.

The weakest part is the harmonic-channel story. The manuscript repeatedly foregrounds the canonical +3.64σ result, while Table III reports a later 10
4
-permutation canonical row at +7.93σ, and the public MASTER-decoupled monopole-only artifacts show that pure monopole leakage explains only about 12% of the decoupled post-MASTER C
1
	​

, not the post-MASTER residual. The source/artifact versioning problem is severe enough that the paper is not reproducible as submitted.

BLOCKERS — must fix before publication
#	Location	Finding	Proposed fix
B1	Data Availability, p.19; public source at stated commit	The paper states “Repository state for this version: commit 2a2939b2” and says a Zenodo DOI is not yet minted. But the public .tex at that commit declares \paperVersion{v1.0.166} and contains materially different headline values: +0.43σ, p=0.30, p
eq
	​

>0.9 high-confidence count 471,049, and A
95
	​

≈1.5−2%. The PDF says +0.41σ, p=0.31, p
eq
	​

>0.6, N=949,584, and A
95
	​

∈(1.0,1.5]. The source-to-PDF chain is therefore not auditable. 

chirality_catalog_paper_v171

 
GitHub
	Freeze a single immutable release: exact .tex, exact PDF, exact scripts, exact JSON/NPY artifacts, catalog/model hashes, and a build script. Mint the DOI before acceptance. The paper must cite the exact tag/commit that rebuilds the submitted PDF byte-for-byte or at least reproduces all tables.
B2	Sec. III A/Table I; Sec. IV D; Conclusions VII.b	The manuscript says the N=500 monopole-only null demonstrates that the +3.64σ canonical value is consistent with monopole-mask leakage. But the released monopole_mask_null_results.json explicitly says both observables are mask-coupled and neither is MASTER-deconvolved; it supports only the pre-MASTER 99.32% statement. The released MASTER-decoupled monopole-only null gives C
1
data
	​

=6.55×10
−6
, monopole-only mean 7.59×10
−7
, and z=5.14. Thus pure monopole leakage explains only ∼0.759/6.555≃11.6% of the decoupled post-MASTER C
1
	​

; roughly 88% is beyond monopole-only leakage. 

chirality_catalog_paper_v171

 

chirality_catalog_paper_v171

 
GitHub
 
GitHub
	Rewrite the leakage conclusion: “pre-MASTER pseudo-C
1
	​

 is almost entirely monopole-mask leakage; post-MASTER residual is not explained by monopole-only leakage and requires additional depth/PSF/morphology-correlated structure.” Add the MASTER-decoupled monopole-only null as a table in the paper. Remove or qualify every sentence saying the +3.64σ post-MASTER residual is “consistent with monopole-mask leakage.”
B3	Abstract; Sec. IV C–D; Table III; Fig. 8; Conclusions VII.b–c	The canonical harmonic significance is internally inconsistent. The abstract and conclusions foreground +3.64σ, p
MC
	​

=0.030, “≈1.9σ Gaussian-equivalent,” while Table III reports the canonical unapodized 10
4
-permutation row as +7.93σ, rank p=3×10
−4
. The Table III caption says the older +3.64σ value is “superseded as a table entry” but the abstract and conclusions still use it as a headline diagnostic. 

chirality_catalog_paper_v171

 

chirality_catalog_paper_v171

 

chirality_catalog_paper_v171

	Define one canonical harmonic diagnostic, or give distinct names to the old direct-MC single-mode estimator and the new 39-band decoupled estimator. A superseded number should not appear in the abstract as the canonical result. Update all abstract/conclusion wording and p-value interpretations.
B4	Sec. II B, p.2 vs Appendix B, p.15	Training-set accounting is inconsistent. Sec. II says 6,637+17,153+2,000=25,790 images and 66.5% CE-ResNet-derived labels. Appendix B says the validation split is n
val
	​

=5,323 of 26,616. This is not a harmless rounding issue; it changes the training/validation manifest and pseudo-label fraction. 

chirality_catalog_paper_v171

 

chirality_catalog_paper_v171

	Add a definitive training-label accounting table: source, raw count, deduplicated count, train/validation split, overlap removals, augmentations, and final manifest hash. Recompute CE-ResNet fraction and all validation metrics from that manifest.
B5	Appendix D/Table IX; public WLS artifacts	The WLS/template-fit exclusion is one of two primary results, but the public artifacts do not consistently describe the mask. The paper says “canonical-mask A
p
	​

 field,” f
sky
	​

=0.49005. The public joint_nuisance_model_fit.json reports f_sky_canonical = 0.740926, n
pix
	​

=36418, while the bootstrap artifact reports mask `(	b_gal
MAJORS — should fix

High-confidence null depends on a confidence cut that removes the non-null full-sample signal.
Location: Sec. IV C, pp.7–8; Fig. 6. The paper reports a clean +0.41σ null at p
eq
	​

>0.6, but the unthresholded sample has a 0.57% A
p
	​

-unit dipole at z≃4.2−4.4. The paper attributes this to a low-confidence-tail systematic, plausibly, but the headline should be framed as “HC-selected real-space null,” not as a full-catalog null. Add a pre-specified threshold history or a hierarchical model in which confidence, morphology, and depth are nuisance variables. 

chirality_catalog_paper_v171

The “three-interpretation closure” language remains stronger than the evidence.
Location: Sec. IV D; Appendix D. The evidence favors interpretation (ii), a coherent depth/morphology systematic, but many anchors are correlated: density-stratified null, pixel-density cross-spectrum, imaging-leg fractions, and footprint/depth weighting are not independent tests. Replace “closure” and “confirmed” language with “favoured/supported,” unless a formal model comparison is added. The paper already has the right ingredients; it needs a clean statistical synthesis.

The ℓ=2 cross-spectrum is useful but underpowered as a formal discriminator.
Location: Appendix D.h. The paper quotes r
ℓ=2
	​

=−0.65, z=−2.89, using a 200-realization permutation null. That is good diagnostic evidence, but not strong enough to carry “confirmed” systematic language. The public artifact also states the test is against n
total
	​

, a depth/sampling proxy, not a physical depth/PSF/morphology basis. 

chirality_catalog_paper_v171

 
GitHub

Fix: increase to at least N
MC
	​

=5000−10000, include DR8 depth, PSF FWHM, extinction, seeing, b/a, fracdev, size, and magnitude templates, and report covariance among ℓ=1,2.

The WLS z=−18 is correctly downscoped from the naive z=−264, but the interpretation still needs tightening.
Location: Appendix D.g/Table IX. The block bootstrap inflation from σ
A
	​

=1.11×10
−4
 to 1.63×10
−3
 is appropriate and the paper correctly avoids using the naive 264σ as the exclusion. But this is an exclusion of a clean template with A
ref
	​

=0.034 in A
p
	​

 units on this catalog, not a likelihood-level exclusion of Shamir’s Ganalyzer pipeline. The text mostly says this, but any remaining “Shamir excluded” implication should be removed. 

chirality_catalog_paper_v171

 
GitHub

Classifier calibration is too weak for the strength of the catalogue claims.
Location: Sec. IV A; Appendix B. The paper responsibly states that max-class probabilities are not calibrated: mean confidence is 0.951 while independent GZ1 three-class accuracy is 58.7% and spiral-chirality accuracy is 69.91%. That should be elevated from a caveat to a methodological limitation in the abstract or conclusions. Any released “confidence” column must be described as a ranking score, not a probability. 

chirality_catalog_paper_v171

 

chirality_catalog_paper_v171

D4-TTA validation is not enough to dismiss rotation-related systematics.
Location: Sec. III C; Appendix B.c. The mean P
CW
	​

 stability under Z2 vs D4 is reassuring, but a 21.4% argmax-label flip rate on borderline galaxies is large. Since the full-sample signal is low-confidence-tail dominated, the paper should show a spatially stratified Z2-vs-D4 comparison in the same low-confidence tail and for the same real-space estimator. 

chirality_catalog_paper_v171

The previous-work comparison overreaches in one sentence.
Location: Sec. V A. “The monopole-mask leakage channel ... can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples” is too broad: the demonstrated leakage is under this DESI/ViT-Small catalog and mask. Reword to “demonstrates a mechanism by which a comparable pre-MASTER dipole-class signal can arise under this pipeline; a matched Ganalyzer reanalysis is required.” 

chirality_catalog_paper_v171

The “largest chirality-labelled catalogue” claim should be made precise.
Location: Abstract; Conclusions. The catalogue has 8.47M galaxies but only 3.20M are CW/CCW spirals; 5.27M are non-spiral/ambiguous. Use “largest released catalogue with chirality probabilities and a 3.20M spiral chirality sub-catalogue,” unless the authors document a complete literature census.

MINORS — polish

Add arXiv ID for Shamir 2022a/PASJ.
The paper correctly separates Shamir 2020 arXiv:2007.16116 and Shamir 2022 DESI arXiv:2208.13866. The PASJ 2022 alignment paper appears to correspond to arXiv:2101.04068; add this to reference [2]. 

chirality_catalog_paper_v171

 
arXiv
 
arXiv
 
arXiv

Title is far too long.
Suggested title: “Survey-scale galaxy chirality with equivariant test-time averaging: a DESI Legacy null dipole and low-ℓ mask-systematics diagnostic.”

Add line numbers for review.
This paper is complex enough that line-numbered PDFs are essential.

Figure 3/caption wording: “non-spiral / face-on / morphologically indeterminate” appears wrong; face-on spirals are exactly the desired chirality class. Use “non-spiral / edge-on / morphologically indeterminate.”

Move long provenance/correction notes out of the main flow.
The transparency is commendable, but the main text is hard to read. Put the audit trail in a reproducibility appendix or changelog table.

Unify “confidence” notation.
The paper alternates max-class confidence, p
eq
	​

, p
CW
eq
	​

, and per-spiral confidence. Define once and use consistently.

Use a single p-value convention table.
The manuscript mixes moment z, empirical rank p, Gaussian-equivalent σ, one-sided p, two-sided p, and positive-definite amplitude p. Add a compact table mapping each result to its exact p-value convention.

Journal formatting: for MNRAS, remove PACS and use the MNRAS bibliography/style; for PRD, keep REVTeX but shorten the title and abstract.

Local artifact paths should be replaced by stable links.
The paper repeatedly cites paths such as c12_r24conf_local_batch.json. These should be DOI-backed or exact release-tag links.

State coordinate conventions in every quoted axis.
The real-space dipole axis is given in (l,b), while many figures are equatorial. Add a short note that axes are Galactic unless stated otherwise.

Specific requested scrutiny
1. Subsample-mask −0.12σ MASTER-deconvolved load-bearing null

In the PDF, this is correctly withdrawn and not used as a conclusion: Appendix A says the −0.122σ value came from a synthetic-footprint catalogue and that a faithful real-catalog rerun gives +7.28σ / +9.78σ, systematics-attributed. That handling is acceptable in the PDF. 

chirality_catalog_paper_v171

However, the public source at the paper’s stated commit still contains stale/deprecated −0.122σ-as-headline language in places. This is part of B1 and must be fixed before publication. 
GitHub

2. v1.0.139 joint nuisance-marginalized fit, 1.7% f
CW
	​

 reference, naive WLS 264σ, block bootstrap ∼18σ

The statistical instinct is right: the naive WLS z≃−264 is not credible because the residuals are spatially coherent, and the block-bootstrap z≃−18 is the only number that should appear. The paper mostly handles this properly. The blocker is reproducibility: the released artifacts disagree about the mask used for the fit, while the paper presents it as a canonical-mask primary estimator. Fix the mask/artifact mismatch and state that this excludes only a clean dipole template in this catalogue, not Shamir’s pipeline. 

chirality_catalog_paper_v171

 
GitHub
 
GitHub

3. Canonical-mask +3.64σ three-interpretation closure

The evidence favors interpretation (ii), but the paper should not call it closure. More importantly, the paper cannot keep +3.64σ as the canonical headline while Table III reports a later canonical +7.93σ row. Define the estimators distinctly or remove the superseded number from the abstract and conclusions. 

chirality_catalog_paper_v171

4. ℓ=2 cross-spectrum r=−0.65, σ=−2.89 vs pixel-density proxy

This is one of the best pieces of evidence for depth/sampling correlation. It is not by itself decisive. With only 200 null realizations and only a pixel-density proxy, it supports the systematic interpretation but does not close it. Increase the null ensemble and use physical depth/PSF/morphology templates. 

chirality_catalog_paper_v171

 
GitHub

5. MASTER-decoupled monopole-only null ×500: 88% unexplained by monopole-only leakage

This is the most important correction. The pre-MASTER 99.32% leakage result is valid for the un-deconvolved pseudo-C
1
	​

. The public MASTER-decoupled monopole-only null shows the post-MASTER data are still z≃4.84 for N=500, and z≃5.14 for N=10
4
. Therefore pure monopole-mask leakage does not explain the post-MASTER residual; the text should say the residual requires additional coherent low-ℓ systematics beyond the monopole-only channel. 
GitHub
 
GitHub

6. Shamir 2020 vs 2022 split with arXiv IDs

The split is mostly correct in the PDF: Shamir 2020 is arXiv:2007.16116, and Shamir 2022 DESI is arXiv:2208.13866. Add the missing arXiv ID for the PASJ 2022 alignment paper, likely arXiv:2101.04068, and keep the paper’s existing caveat that a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion. 

chirality_catalog_paper_v171

 
arXiv
 
arXiv
 
arXiv

Strengths

The catalogue scale is genuinely valuable: 8.47M galaxies and 3.20M CW/CCW spirals, with public probabilities, coordinates, confidence scores, and model outputs.

The flip-equivariant TTA design is a strong methodological improvement over naive chirality classifiers, and Fig. 7 clearly shows why raw classifiers can create spurious dipole-like maps.

The paper is unusually transparent about failures, provenance audits, withdrawn results, null definitions, and estimator hierarchy.

The pre-MASTER monopole-mask leakage demonstration is important and likely useful beyond this paper.

The injection-recovery/falsification framing is better than simply quoting a null p-value.

The authors correctly distinguish the ℓ=1 projected chirality dipole from a direct parity-violation observable, which prevents an otherwise common overinterpretation.

Sources

Pro Extended

