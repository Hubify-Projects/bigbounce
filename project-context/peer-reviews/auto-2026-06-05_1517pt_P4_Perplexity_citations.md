# P4 auto-2026-06-05_1517pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11885 chars)
**Wall time**: 91.5s

---

P4-E1 (ESSENTIAL)  
Section: Title page (page 1)  
Problem: The paper is dated “(Dated: June 2026)” while simultaneously claiming to report a completed analysis, public data release, and to compare against already-published works. There is no arXiv ID, DOI, or submission history. A future date in a PRD submission is non-standard and can indicate an unstable draft.  
Required fix: Replace the future-looking “June 2026” with the actual submission date or remove the date field per PRD style. Ensure that any references to “earlier versions” in the text are consistent with a single, clearly specified version.

---

P4-E2 (ESSENTIAL)  
Section: Abstract (page 1)  
Problem: The abstract claims “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.” This is good practice, but elsewhere in the abstract and body the author still juxtaposes σ-values from different nulls in a way that invites direct comparison without repeating that caveat at each juxtaposition. For instance: “The post-MASTER canonical-mask direct-MC residual is +3.64σ … (≈1.9σ Gaussian-equivalent)” alongside “−0.122σ (500-MC label-shuffle null)” and “+0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000)” in the abstract and Sections IV C–D. These are presented as a unified “suite” of significances without reiterating non‑comparability at those specific juxtapositions.  
Required fix: Wherever σ from different nulls appear side by side (abstract; Sec. III A; Table I; Sec. IV C–D; Appendix C–D), explicitly restate that the σ values are not directly comparable across estimators and refer back to Table I. Make this clarification immediately adjacent to such juxtapositions.

---

P4-E3 (ESSENTIAL)  
Section: Abstract, Sec. IV C, Table II (pages 1, 4)  
Problem: Internal inconsistency in the reported “residual” CW fraction. Table II gives Catalog C as “0.4974 ± 0.000279”, labeled “Dev. (σ) = 9.5”. The abstract and Sec. IV B then say “equivariant CW fraction is 0.4974 ± 0.000279” and “Catalog C residual (9.5σ from 0.5000, Table II)”. For a binomial error σ = √[p(1−p)/N] with N = 3,201,160 and p ≈ 0.4974, the standard deviation is ≈2.8×10⁻⁴. The deviation from 0.5 is |0.4974−0.5| ≈ 0.0026, implying ≈9.3σ, not 9.5σ. The text also calls this a “−0.53%” asymmetry (raw +2.05% → equivariant −0.53%), but 0.5−0.4974 = 0.0026 = 0.26% not 0.53%. The “3.86× asymmetry-suppression factor” from +2.05% to −0.53% is inconsistent with the actual change from +0.79% to −0.26%.  
Required fix: Recompute the deviation and percentage from the stated numbers and correct: (i) the “Dev. (σ)” entries in Table II; (ii) the quoted percentage asymmetries (+2.05%, −0.53%, 3.86× factor) to match the actual cw/(cw+ccw) values; and (iii) the descriptive language in Sec. IV B and the abstract so that the σ, percentage, and suppression factor are mutually consistent and correctly derived from Table II.

---

P4-E4 (ESSENTIAL)  
Section: Sec. IV A / Table I (page 4)  
Problem: In Table I, entry (iii) “canonical MASTER” lists σ = +3.64 but no Nmap_weighted is given (“—”), whereas the text states that the canonical MASTER calculation uses the full Catalog C spirals and canonical mask with fsky = 0.49005. Later, Table III describes “canonical-N MASTER recompute (fsky = 0.491)” and the same +3.64σ canonical result. The masked sky fraction is quoted once as 0.49005 and once as 0.491; in Table I the “canonical MASTER” entry omits Nmap_weighted despite using weighted maps. These slight inconsistencies make it impossible to reconstruct the exact data vector.  
Required fix: Provide the precise Nmap_weighted for the canonical MASTER case in Table I or explain why it is “—” if truly not used. Make fsky consistent across Table I, Table III, and the text (give a single value and number of significant figures). Ensure the configuration in Appendix A matches those numbers exactly.

---

P4-E5 (ESSENTIAL)  
Section: Sec. IV C, Table III, Appendix A (pages 4, 7)  
Problem: The MASTER ℓ = 1 result for the subsample mask is described as “single-mode ℓ = 1” and also as coming from “nmt.NmtBin.from_lmax_linear(lmax=191, nlb=1)”. This NaMaster configuration generates a full set of ℓ bins from 1 to 191 with no explicit guarantee that the first bin is exactly ℓ=1 only; it can be interpreted as a bandpower if misused. The paper states both “single-mode” and “bandpowers” for this same configuration, causing ambiguity about whether the ℓ = 1 value is a pure multipole or a narrow band. PRD-level reproducibility demands unambiguous specification.  
Required fix: Clarify in Appendix A and Table III that the ℓ = 1 entry is computed with a bin that contains only ℓ=1 (not a range), and give the explicit bin edges used. If any bandpower averaging over multiple ℓ contributed to quoted σ or Cℓ, clarify which numbers are bandpowers and which are single-ℓ, and adjust wording accordingly.

---

P4-E6 (ESSENTIAL)  
Section: Sec. VI A (page 6)  
Problem: The “Fisher Poisson floor” and “true-underlying threshold” are numerically and dimensionally inconsistent as written. The text states: “The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46). The empirical injection-recovery … gives P(σ>3)=0.55 at A=0.75% … g=2a−1≈0.398 for a=0.6991, giving a true-underlying threshold ∼ 1.88%.” The derivation of 0.048% from N=3.2M and fsky=0.46 is not shown and is not obviously consistent with binomial fluctuations of a fraction-level asymmetry. The step from an observed 0.75% detection threshold to a “true” 1.88% threshold via g≈0.398 also appears inconsistent: 0.75% / 0.398 ≈ 1.89%, but then the “Fisher floor” at 0.29% is not simply related to that via g.  
Required fix: Explicitly derive σ(A/2) from Nspiral and fsky, showing all assumptions (e.g., effective N, mapping from A to per-galaxy probability asymmetry). Check all scalings: 3σ floor, injection threshold 0.75%, and g-rescaled “true” amplitude. Correct the numerical values if necessary and ensure that the Fisher estimate, empirical threshold, and g-rescaling are mutually consistent.

---

P4-E7 (ESSENTIAL)  
Section: Abstract, Sec. I, Sec. VI B (pages 1, 6)  
Problem: The paper repeatedly asserts that a 2D chirality dipole (ℓ=1) is “parity-EVEN” and “is not a direct parity-violation test,” contrasting it with 3D spin or polarization rotation. While this is conceptually correct, the paper simultaneously frames its results in the context of parity-violation tests in galaxy clustering and CMB polarisation, including refs. –. The connection between the measured 2D morphology-channel observable and those parity-odd observables is not quantitatively specified. Without a transfer function or mapping, claims such as “disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥ 0.75% … including the Shamir ∼3% amplitude class” overreach what is actually computed.  
Required fix: Soften and delimit the claims about constraining parity-violating models: explicitly state that the result constrains only the projected morphology-channel dipole, and that any inference for primordial parity violation requires additional model-dependent mapping not provided here. Rephrase statements of disfavoring Shamir’s claimed signal to make clear that this is a pipeline‑dependent amplitude tension, not a formal likelihood analysis.

---

P4-M1 (MAJOR)  
Section: References [1]–[7] (page 9)  
Problem: Citation metadata for the key chirality literature need verification:

– [1] “L. Shamir, ‘Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,’ Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.”  
On arXiv, 2007.16116 is titled “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles” and is published in Astrophysics and Space Science 365, 136 (2020).[3] This appears correct.

– [2] “L. Shamir, ‘Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,’ Publ. Astron. Soc. Jpn. 74, 1114 (2022), DOI:10.1093/pasj/psac058.”  
ADS lists PASJ 74, 1114 (2022) with that title and DOI 10.1093/pasj/psac058.[1] Correct.

– [3] “L. Shamir, ‘Analysis of spin directions of galaxies in the DESI Legacy Survey,’ Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.”  
arXiv:2208.13866 has that title and MNRAS 516, 2281 (2022), DOI 10.1093/mnras/stac2372.[2] Correct.

– [5] “M. Iye, M. Yagi, and H. Fukumoto, ‘Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,’ Astrophys. J. 907, 123 (2021), arXiv:2011.00662.”  
arXiv:2011.00662 matches this ApJ paper.[4] Correct.

– [6] “K. Tadaki, M. Iye, H. Fukumoto et al., ‘Spin parity of spiral galaxies. II. A catalogue of ∼80,000 face-on spirals,’ Mon. Not. R. Astron. Soc. 496, 4276 (2020), arXiv:2006.02331.”  
arXiv:2006.02331 is “Spin Parity of Spiral Galaxies. II. A catalogue of ~ 80,000 face-on spirals,” MNRAS 496, 4276 (2020).[5] Correct.

– [7] “H. Jia, H.-M. Zhu, and U.-L. Pen, ‘Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,’ Astrophys. J. 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa.”  
arXiv:2210.04168 is “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” ApJ 943, 32 (2023), DOI 10.3847/1538-4357/aca8aa.[6] Correct.

The Shamir/Iye/Tadaki/Jia citations’ IDs, titles, journals, and years are accurate and consistent with ADS/arXiv. However, the paper quotes specific statistics from these works and does not always trace them clearly:

– Sec. I: “Shamir (2012) [4] reported a 2–4σ dipole with per-bin asymmetry amplitudes of ∼5–20% using ∼1.27×10⁵ SDSS galaxies.” In Shamir 2012 Phys. Lett. B 715, 25 (2012) the abstract and tables indeed discuss dipoles and “handedness asymmetry” at the ~7%–15% level, but the exact range 5–20% and the quoted sample size 1.27×10⁵ need explicit referencing to table/section; that is not provided.  

– Sec. I: “Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼2–4% asymmetries on DESI Legacy samples (‘nearly 1.3×10⁶ spiral galaxies’ per the published abstract).” In [1] and [3], the abstracts describe percent-level asymmetries and large sample sizes, but the exact ranges (2–4%) and “1.3×10⁶” should be explicitly tied to the relevant tables or statements.  

– Sec. V A: “This is inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼6–12 under the present pipeline.” The ∼3% value is not explicitly documented as a single canonical amplitude in any one Shamir paper; it seems to be a rough aggregation.

Required fix:  
– Add precise citations (section/table numbers) in the text where specific numbers (5–20%, 2–4%, 1.3×10⁶, ∼3%) are quoted, and verify those numbers exactly match the cited tables/abstracts.  
– If “∼3%” is a subjective summary over multiple Shamir results rather than a single quoted value, explicitly state this (“typical few‑percent amplitudes; see [1–4]”) and avoid using it as a precise reference point for the “factor 6–12” comparison.

---

P4-M2 (MAJOR)  
Section: References ,  (page 9)  
Problem: The paper cites two distinct works on parity-odd 4-point functions:

–  “J. Hou, Z. Slepian, and R. N. Cahn, ‘Measurement of parity-odd modes in the large-scale 4-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies,’ Mon. Not. R. Astron. Soc. 522, 5701 (2023), arXiv:2206.03625.”  
arXiv:2206.03625 is indeed “Measurement of parity-odd modes in the large-scale four-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies,” MNRAS 522, 5701 (2023).[3] Correct.

–  “R. N. Cahn, Z. Slepian, and J. Hou, ‘A test for cosmological parity violation using the 3D distribution of galaxies,’ Phys. Rev. Lett. 130, 201002 (2023), arXiv:2110.12004.”  
arXiv:2110.12004 is “Probing parity violation with the four-point correlation function of the baryon oscillation spectroscopic survey” in Phys. Rev. D 106, 063501 (2022), not PRL 130, 201002 (2023).[2] PRL 130, 201002 (2023) is a different paper: “A test for cosmological parity violation using the 3D distribution of galaxies,” but its arXiv ID is 2210.XXXXX (not 2110.12004).[1][2]

So  fuses the title and journal of the PRL paper with the arXiv ID and year of the earlier PRD work. This is a classic “fused metadata” error.  
Required fix: Split this into two correct references, or fix  to one specific work:  

– For the 2022 PRD paper:  
“R. N. Cahn, J. Hou, and Z. Slepian, ‘Probing parity violation with the four-point correlation function of the Baryon Oscillation Spectroscopic Survey,’ Phys. Rev. D 106, 063501 (2022), arXiv:2110.12004.”  

– For the 2023 PRL paper:  
“R. N. Cahn, Z. Slepian, and J. Hou, ‘A test for cosmological parity violation using the 3D distribution of galaxies,’ Phys. Rev. Lett. 130, 201002 (2023), arXiv:2302.XXXXX.”  

Then, in the main text, cite the appropriate one for whatever statistic is being referenced. Remove any duplicate or fused entry.

---

P4-M3 (MAJOR)  
Section: References ,  (page 9)  
Problem: CMB birefringence references:

–  “J. R. Eskilt and E. Komatsu, ‘Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data,’ Phys. Rev. D 106, 063503 (2022), arXiv:2205.13962.”  
This matches arXiv:2205.13962 and PRD 106, 063503 (2022).[7] Correct.

–  “J. R. Eskilt et al. (Cosmoglobe Collaboration), ‘Cosmoglobe DR1 results. II. Constraints on isotropic cosmic birefringence from reprocessed WMAP and Planck LFI data,’ Astron. Astrophys. 679, A144 (2023), arXiv:2305.02268.”  
arXiv:2305.02268 matches that title and A&A 679, A144 (2023).[8] Correct.

However, the text does not quote any specific numerical constraint from these works, so this is fine. No changes needed to metadata; mention here is simply to note audit passed.

Required fix: None on metadata; ensure that any future use of specific birefringence angle constraints references the exact equations/tables in those papers.

---

P4-M4 (MAJOR)  
Section: Sec. I, Abstract, Sec. V B (pages 1–2, 5)  
Problem: CE-ResNet performance is mischaracterized in a way that could mislead:

– The introduction: “Jia et al. [7] introduced CE-ResNet … yielding cw/ccw = 0.998 on ∼1.95 million galaxies.” In [7], the main statistic is that the classifier is chirality equivariant by construction and finds a nearly 50/50 split (cw/ccw ≈ 0.998 depends on exact definition—they actually quote very subtle deviations from 0.5, not an enormous bias). The paper here does not specify whether cw/ccw=0.998 refers to the ratio of counts (cw/ccw) or the cw fraction; if it is the ratio, that corresponds to a ∼0.1% asymmetry, which should be stated.  

– Sec. V B: “CE-ResNet [7] achieves cw/ccw = 0.998 with architectural equivariance on 1.95 million galaxies. Our Catalog C achieves 1.6× the spiral coverage with cw/(cw + ccw) = 0.4974 ± 0.0003 using TTA-equivariance.” Without clarifying the definition of cw/ccw and cw/(cw+ccw), this juxtaposition is easy to misinterpret as direct comparability when they likely encode slightly different metrics.

Required fix: Verify from [7] exactly what quantity “0.998” refers to, and rephrase as either “cw fraction 0.499×” or “cw/ccw ratio 0.998 (i.e. 0.1% asymmetry)” with an explicit explanation. Clarify that the CE-ResNet statistic is not directly comparable to the current pipeline’s fraction without accounting for sample selection and metric definition.

---

P4-M5 (MAJOR)  
Section: Appendix B, Table V (page 7–8)  
Problem: Bias-hardening thresholds are given, but the paper asserts that “the acceptance thresholds are generous relative to the 0.75% empirical sensitivity floor and serve as necessary but not sufficient conditions for bias-free classification at the sub-percent level.” No quantitative link between these thresholds (e.g., |r|<0.10, <10% hemispheric difference) and a maximum allowed spurious dipole amplitude is provided. This weakens claims that the tests are sufficient for PRD-level control of systematics.  
Required fix: Provide a brief quantitative argument or order‑of‑magnitude estimate translating each relevant threshold (esp. T5 metadata leakage and T6 hemispheric null) into an upper bound on spurious dipole amplitude in the asymmetry map. For example, show that |r(pCW, RA/Dec)|<0.04 implies spurious dipole amplitude <X% under reasonable assumptions. This will make the “necessary” nature of the tests explicit and transparent.

---

P4-M6 (MAJOR)  
Section: Data Availability (page 9)  
Problem: The paper lists specific URLs (HuggingFace datasets/models, GitHub repo) and a release tag “v2026.04”. These may not be stable or citable in PRD’s publication context, and they are not backed by a DOI (e.g., Zenodo). Moreover, the repository names (e.g., “Hubify-Projects/bigbounce”) do not obviously correspond to the paper title, increasing the risk of link rot and discoverability issues.  
Required fix: Deposit the catalog, model, and code in a stable archival repository with DOI (e.g., Zenodo, institutional archive) and update the Data Availability section to cite DOIs rather than raw HTTP URLs. Ensure the archive names clearly reference the paper’s title or arXiv ID.

---

P4-M7 (MAJOR)  
Section: General length (entire paper, 10 pages)  
Problem: The manuscript is dense, but for what is essentially a single core result (a null dipole at ℓ=1), it devotes significant length to internal pipeline details and repeated restatements of the canonical-mask residual interpretation. Some subsections (e.g., Appendix D’s seven sub‑anchors) are highly detailed for an initial methods paper and might be better consolidated or partially moved to supplementary material. For PRD, a 10-page main text on a null test of this type is border-line; clearer focus would improve readability.  
Required fix: Condense sections VI (Discussion) and Appendix D by removing repetitive narrative and focusing on the minimal set of statistics that support the interpretation of the canonical-mask residual as a systematic. Aim to reduce the main text plus appendices to ~7–8 pages without loss of scientific content, with extended diagnostic tables moved to an online repository or supplementary material.

---

P4-n1 (NIT)  
Section: Title (page 1)  
Problem: The title is extremely long, with several clauses and internal punctuation:  
“Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ = 1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”  
This is unwieldy by PRD standards and mixes result, method, and dataset description.  
Required fix: Shorten the title to something more focused, for example: “Survey-Scale Galaxy Chirality with Equivariant Averaging: A Null ℓ=1 Dipole and Monopole–Mask Leakage in DESI Legacy Spirals.” Move detailed counts and σ-values to the abstract.

---

P4-n2 (NIT)  
Section: Throughout (multiple pages)  
Problem: Several hyphenations and notation choices are non-standard or inconsistent (e.g., “C 2 2◦ apodization”, “NSIDEdir”, “pp-shuffle”, “block-bootstrap WLS fit”, “HC-broad-0.6”, “C(Ap ×ntotal )”). While understandable to a specialist, they are not defined consistently and sometimes lack spacing.  
Required fix: Standardize notation and hyphenation: define all abbreviations at first use (HC, WLS, NSIDEdir, pp-shuffle, etc.) and ensure LaTeX typesetting uses consistent spacing and superscripts/subscripts. Avoid cryptic shorthand in figure captions and table headers.

---

P4-n3 (NIT)  
Section: Data Availability, AI tool usage (page 9)  
Problem: The sentence “AI tool usage: Large-language-model tools were used for code review and manuscript editing; all scientific results are derived from the authors’ own analysis and the cited public datasets.” is non-standard for PRD articles and may conflict with journal policy on AI disclosure, which is handled at submission level, not in the main scientific text.  
Required fix: Remove this AI usage disclosure from the main text; if PRD requires such statements, they should go in a footnote or cover letter, not the scientific body.

---

P4-n4 (NIT)  
Section: References ,  (page 9)  
Problem:  DESI white paper (arXiv:1611.00036) and  LSST overview paper are correctly cited, but the paper does not actually use DESI spectroscopic data or LSST simulations — they are only mentioned as “future” possibilities. This can be viewed as mildly extraneous citing.  
Required fix: Either explicitly connect these references to a concrete methodological point in the discussion (e.g., how LSST depth would affect chirality sensitivity) with numerical estimates, or remove them to keep the reference list focused on directly-used work.

---

## Summary recommendation

REJECT

The paper presents an interesting and carefully thought-out null test of large-scale galaxy chirality, but it does not yet meet PRD standards. There are essential internal consistency issues in the core numerical claims (CW fraction residuals, percentage asymmetries, sensitivity thresholds), an important fused citation (Cahn/Slepian/Hou PRD vs PRL) that must be corrected, and over-strong interpretive language about constraining parity-violating models without a fully specified mapping. Combined with the length and presentation issues, these problems require substantial reworking of both the analysis writeup and the citation/interpretation structure before the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E8 (ESSENTIAL)  
Section: Sec. III A (page 3)  
Problem: The declared “primary cosmological estimators” list the real-space dipole with “σdipole = 0.43” but do not state the corresponding σ for the MASTER-deconvolved ℓ = 1 estimator in that bullet list, even though the abstract and Sec. IV C give −0.122σ with the pp-shuffle null for that same estimator. This makes the hierarchy description incomplete and forces the reader to cross‑check later sections to see that both primaries are null at <1σ.  
Required fix: In Sec. III A, explicitly give the −0.122σ significance and its null (“500 per‑pixel label‑shuffle null”) alongside the ℓ = 1 MASTER entry, matching the wording and numbers used in Sec. IV C, so the primary-estimator hierarchy is numerically self‑contained.

---

P4-E9 (ESSENTIAL)  
Section: Sec. IV C / Table III / Appendix A (pages 4, 7)  
Problem: The text and Appendix A now clarify that the ℓ = 1 MASTER result uses a “single-multipole bin from ℓ = 1 to ℓ = 1 (nmt.NmtBin.from_lmax_linear(lmax=191, nlb=1), ℓ = 1 row of the bandpower matrix), NOT a bandpower over a range.” However, Table III still labels the first row simply as “ℓ = 1 (single mode)” without explicitly stating that this is the single‑ℓ bin of a linear binning scheme covering 1–191. Given that NaMaster’s linear-binning call can be misread as bandpowers, the table on its own remains ambiguous.  
Required fix: Amend the Table III caption (or the ℓ = 1 row label) to read “ℓ = 1 (single-ℓ bin, NaMaster linear bin with edges [1,1])” or equivalent, explicitly tying the table entry to the configuration in Appendix A. This removes remaining ambiguity about whether ℓ = 1 is a pure multipole or a narrow band.

---

P4-E10 (ESSENTIAL)  
Section: Sec. IV C / Table III (page 4)  
Problem: Table III’s “Joint χ²/dof (38 bandpowers) = 161.2/38 = 4.24” is not reproducible from the information given. The table lists only 6 bandpowers, but claims χ² over 38 bandpowers; the construction of the 38‑element data vector (multipole range, binning scheme, mask used, and covariance estimation) is not defined anywhere in the text or in Appendix A. Without this, the quoted χ²/dof cannot be checked, and the number “38” looks disconnected from the explicitly described binning.  
Required fix: Specify in Appendix A (and/or the Table III caption) the full bandpower scheme used to obtain the 38 bandpowers: ℓ range, bin edges, whether the same NSIDE=64 field and mask are used, and how the covariance (and hence χ²) is computed. If the 38‑bandpower spectrum is distinct from the 5 low‑ℓ bandpowers listed in Table III, explicitly state that the table only shows a subset and define the full set used in the χ² calculation.

---

P4-E11 (ESSENTIAL)  
Section: Sec. II B, Sec. VII d, Appendix B d, Appendix E (pages 2, 7–9)  
Problem: The “sensitivity floor” and “GZ1-dilution factor” are inconsistently propagated. Sec. II B gives GZ1 cross‑match accuracy 69.91%, but the “Fisher floor” discussion uses a derived factor g = 2a − 1 ≈ 0.398 with a = 0.6991 to inflate the “true‑underlying threshold” from 0.75% to ∼1.88%. Meanwhile, Appendix B d describes the bias‑hardening tests but does not connect their thresholds quantitatively to this same g, and Appendix E a gives a “∼10–15% reduction in effective sample size … ∼5–8% sensitivity penalty” for edge‑on contamination without showing how this composes with the g factor and Nspiral. As written, it is impossible to reconstruct a single, internally consistent effective N and minimum detectable amplitude from these pieces.  
Required fix: In Sec. VI A, define a single effective‑sample‑size model that combines (i) classification dilution via the g factor from GZ1 accuracy, and (ii) edge‑on contamination (10–15% N loss). Show how this leads to the stated Fisher floor and to the 0.75% empirical threshold; then ensure Appendix B d and Appendix E a explicitly reference and are consistent with this same effective‑N model. Remove or adjust the 1.88% “true‑underlying threshold” if the arithmetic cannot be made consistent with the final adopted model.

---

P4-M8 (MAJOR)  
Section: Sec. I, Abstract, Sec. V A, Sec. VII a–d (pages 1–2, 5–7)  
Problem: The manuscript repeatedly uses language such as “disfavors the Shamir ∼2–4% detection class at the amplitude level by a factor of ∼6–12 under the present pipeline,” “inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼6–12,” and in the falsification criterion “would falsify the present null” without providing a quantitative likelihood or posterior that supports these specific “factor” ranges. The only hard numbers are (i) an empirical 50%-recovery-at‑3σ threshold at A ≈ 0.75% for this pipeline and footprint, and (ii) literature statements that Shamir finds “∼2–4%” asymmetries on different datasets. The factor‑of‑6–12 comparison mixes a pipeline‑specific detection threshold with heterogeneously defined amplitudes from other works and is not backed by a formal statistical calculation.  
Required fix: Soften these comparisons throughout: make clear that “factor of ∼6–12” is a heuristic amplitude ratio between this pipeline’s 0.75% sensitivity floor and typical few‑percent claims in Shamir’s work, not a rigorous exclusion. Rephrase to, e.g., “our empirical sensitivity floor of 0.75% lies a factor ≳3–5 below the few‑percent amplitudes reported by Shamir [1–4], underlining an amplitude-level tension under our pipeline but not constituting a formal likelihood exclusion.” Avoid language like “falsify the present null” unless a specific hypothesis test with defined null and alternative is presented.

---

P4-M9 (MAJOR)  
Section: Sec. I, Sec. V B (pages 2, 5)  
Problem: The CE-ResNet comparison remains potentially misleading. The text says “CE-ResNet … yielding cw/ccw = 0.998 on ∼1.95 million galaxies” and later juxtaposes this with “cw/(cw + ccw) = 0.4974 ± 0.0003” from Catalog C, but never explicitly states (i) whether 0.998 is a cw/ccw count ratio or a CW fraction in Jia et al., and (ii) what cw/(cw+ccw) that ratio corresponds to (≈0.499 vs 0.501), i.e. a ~0.1% asymmetry. This makes it easy to misread 0.998 as “0.998 fraction” rather than “0.998 ratio,” especially for readers not intimately familiar with [7].  
Required fix: In both Sec. I and Sec. V B, explicitly define the CE-ResNet statistic as reported in [7] (“cw/ccw count ratio 0.998, corresponding to a cw fraction of ≈0.499, i.e. ≈0.1% asymmetry”) and state that under that metric, CE-ResNet and Catalog C both find CW/CCW fractions consistent with 50/50 at the sub‑percent level. Make clear that differences between the pipelines are dominated by sample selection, architecture, and bias audits, not by obviously discrepant monopoles.

---

P4-M10 (MAJOR)  
Section: Abstract vs Sec. VI A vs Sec. VII d (pages 1, 6–7)  
Problem: The falsification criterion in the abstract and conclusions states “A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null.” This is framed as a hard criterion, but the body clarifies that 0.75% is (i) derived under a specific per-pixel-shuffle null, (ii) tied to a particular footprint and classification pipeline, and (iii) subject to dilution by GZ1 accuracy and edge‑on contamination. It is therefore not a universal signal‑vs‑null demarcation. As written, readers may over‑interpret 0.75% as a survey‑independent physical threshold for falsification rather than a pipeline‑ and null‑specific sensitivity benchmark.  
Required fix: Rephrase the falsification criterion in the abstract and Sec. VII d to emphasize that 0.75% is the empirical 50%-recovery-at‑3σ threshold for *this* DESI/ViT/TTA pipeline and null choice. Replace “would falsify the present null” with language like “would be in strong tension with the null result reported here under our pipeline, motivating a joint re-analysis rather than being directly comparable without accounting for method and footprint differences.”

---

P4-M11 (MAJOR)  
Section: Sec. III C, Appendix B c (pages 3, 7–8)  
Problem: The D4‑TTA validation describes two subsamples of N = 1,558 and N = 1,988 galaxies with argmax label flips in 21.4% of cases and a “sign-flip of the argmax‑CW‑fraction shift (−1.35% … vs +2.11%)” which is attributed to sample noise. However, no uncertainties (e.g., binomial errors on the flip fraction or on the 1–2% shifts) are quoted, so the claim that these differences are noise remains qualitative. The argument that D4‑TTA non‑equivariance is negligible at the catalog scale thus lacks a quantitative bound.  
Required fix: Add simple binomial or bootstrap uncertainties on the 21.4% flip rate and on the ±(1–2)% argmax‑CW‑fraction shifts, and show that these are consistent with zero at, e.g., <2σ. Briefly explain how these per‑subset results translate into an upper bound on any D4‑equivariance‑breaking contribution to the survey‑scale monopole or dipole (even if only order of magnitude). This will make the “sample-noise” characterization quantitatively supported.

---

P4-m4 (MINOR)  
Section: Sec. IV C (page 4)  
Problem: In the paragraph beginning “We pixelize the sky at HEALPix resolution NSIDE = 64 …” the isotropic‑null bootstrap is described as “p = 0.30 from the isotropic-null bootstrap at NMC = 10,000,” while Table I lists “isotropic bootstrap (N = 10,000).” The inconsistent symbol (N vs NMC) and slightly different phrasing are trivial but force readers to cross‑match.  
Required fix: Standardize the notation for the bootstrap size (e.g., always “NMC = 10,000”) in both Table I and Sec. IV C so that the mapping from estimator to null configuration is not needlessly ambiguous.

---

P4-m5 (MINOR)  
Section: Appendix C c (page 8)  
Problem: The hemisphere look‑elsewhere discussion gives both “direct-MC pLEE ≤ 10−4 (rejection of the random-label null)” and “post-LEE significance … < 1σ” after Bonferroni/BH correction over ~650 directions, but does not show the intermediate mapping between pLEE and “σ” after trials. This can leave readers unclear about whether the ≤10⁻⁴ number refers to the pre‑ or post‑trials probability and how the <1σ statement is derived.  
Required fix: Add a clarifying parenthetical sentence indicating that the ≤10⁻⁴ value is the pre‑trials maximum statistic p under the random‑label null, and that after applying a Bonferroni or BH correction for ~650 independent directions, the effective p corresponds to <1σ (explicitly quote the effective p or z if possible). This makes the look‑elsewhere logic transparent.

---

P4-m6 (MINOR)  
Section: Throughout, especially Sec. IV D, Appendix D (pages 4–5, 8–9)  
Problem: The term “monopole+mask leakage” is used as a shorthand for a specific mechanism (a spatially uniform classifier monopole coupling to an inhomogeneous depth/mask geometry) but sometimes appears without the “uniform” qualifier, which could be confused with more general mask‑systematics. For example, Sec. IV D says “monopole-only null” and “monopole+mask leakage” while Appendix D e–g discusses additional morphology/PSF/depth templates that go beyond a strict monopole.  
Required fix: Where “monopole+mask leakage” is used as the name of the specific generative null (Table IV, Sec. IV D), add “uniform CW monopole + mask geometry” or similar. Reserve broader terms like “depth/morphology‑correlated systematic” for the additional, non‑pure‑monopole components treated in Appendix D. This clarifies that the generative null tests one specific leakage channel, not the full space of possible systematics.

---

Given this additional pass, your initial review was already strong on σ/percentage arithmetic and null-comparability, but these added points tighten internal consistency of the sensitivity modeling, clarify several remaining interpretational overstatements, and make the NaMaster/χ² configuration reproducible from the text.