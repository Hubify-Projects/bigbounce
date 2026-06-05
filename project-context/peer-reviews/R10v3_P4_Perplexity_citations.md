# P4 R10v3 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search
**Wall time**: 49.7s

---

P4-E1 (ESSENTIAL)  
Section: Title block, page 1  
Problem: The manuscript is dated “(Dated: June 2026)”, which is a future date relative to the current arXiv/PRD publication pipeline and strongly suggests the date was fabricated for the draft rather than reflecting an actual submission or acceptance date.  
Required fix: Replace the date with either the actual submission date (once known) or follow PRD’s convention for undated preprints (often omitting a future “dated” field in submitted versions). Do not use a future date.

---

P4-E2 (ESSENTIAL)  
Section: Abstract, page 1  
Problem: The abstract states “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table II for the mapping of each result to its null.” The body repeats this concept but does not re-assert the non-comparability at every juxtaposition where σ from different nulls are placed side-by-side (e.g., Table I, Table III, multiple paragraphs in Sec. IV–VI). This violates the review instruction requiring explicit “not directly comparable” qualification at every such juxtaposition.  
Required fix: At every point where σ values from different null procedures are presented side-by-side or directly compared (including Tables I, III, IV, V and the places in text where multiple σ’s from different nulls are reported together), explicitly annotate that these σ values are defined with different nulls and are not directly comparable. A short parenthetical such as “(σ values from distinct nulls; not directly comparable)” is sufficient wherever they are juxtaposed.

---

P4-E3 (ESSENTIAL)  
Section: Throughout, but especially Abstract and Sec. IV A–C, pages 1–5  
Problem: The abstract quotes several quantitative results (e.g., “5,547,858”, “fsky = 0.659”, “−0.122σ”, “+0.43σ (p = 0.30)”, “pglobal_CW = 0.4974”, “500-MC”, “NMC = 10,000”, “3.64σ”, “pMC = 0.030”, “∼ 1.7%”, “r = −0.65 with σ = −2.89”, amplitude ≥ 0.75% threshold) and calls them headline findings, per the instructions all “load-bearing scalars” must be checked for consistency. Several are only partially traceable or are ambiguous statistical constructs:

- The “50%-recovery-at-3σ threshold at |Adipole| ≥ 0.75%” is mentioned in the abstract and later in Sec. VI A with numerical probabilities, but the exact definition of “σ” in that injection context and its mapping to the null (per-pixel shuffle, number of trials, look-elsewhere) is not fully specified, making it difficult to reproduce the quoted threshold.  
- The “empirical-rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent” is inconsistent with a standard one-sided or two-sided mapping: p = 0.03 corresponds to ≈1.88σ two-sided or ≈1.88σ one-sided only if defined precisely, but the paper uses 3.64σ for the same canonical residual under a different null, creating confusion about which σ is referenced where.  
- The “Falsification criterion” amplitude “≳ 0.75% (the demonstrated empirical 50%-recovery-at-3σ threshold…)” is anchored to a 471k-galaxy HC subsample, while the main dipole analysis uses N = 3.2M spirals; this is not clearly reconciled, and the abstract reads as if the 0.75% threshold applies universally.  

Required fix:  
1. In Sec. VI A, explicitly define the test statistic and null distribution used for the injection-recovery σ, and show how the “σ > 3” condition and “P(σ > 3)” are computed, including whether the σ is standard deviation units under the per-pixel-shuffle null, and whether a look-elsewhere effect is accounted for.  
2. Reconcile the use of “+3.64σ” and “pMC = 0.030, ≈1.9σ” for the canonical-mask residual by clearly specifying that these refer to different nulls and explaining the discrepancy (e.g., analytic Gaussian approximation vs. empirical rank). Make this explicit in Sec. IV D and Appendix D where the numbers are introduced.  
3. Clarify in the abstract and Sec. VI A that the 0.75% “50%-recovery-at-3σ” sensitivity is derived from the high-confidence subsample (N = 471,049) and may differ for the full 3.2M-spiral catalog; either provide the corresponding full-sample sensitivity estimate or circumscribe the statement to the HC subset.  

---

P4-E4 (ESSENTIAL)  
Section: Data availability, Appendix E, page 9  
Problem: The URLs in the Data Availability section appear inconsistent with the earlier description of the parent sample and catalog:

- The main text (Sec. II A) states the parent sample is “Smith42/galaxies” on HuggingFace.  
- The Data Availability section gives “https://huggingface.co/datasets/bamfai/galaxy- chirality- catalog” and “https://huggingface.co/bamfai/galaxy-chirality-v2” with embedded spaces in the slug (“galaxy- chirality- catalog”), which is highly unlikely to be a valid repository URL.  
- The GitHub URL “https://github.com/Hubify-Projects/bigbounce” may be valid, but is not verifiable from the text itself; more importantly, PRD will not permit malformed or obviously broken links in the final version.  

Required fix: Verify the actual HuggingFace and GitHub repository names and correct all URLs to use valid, space-free slugs (e.g. “galaxy-chirality-catalog” rather than “galaxy- chirality- catalog”). Ensure that the parent-sample dataset name matches the URL given in Sec. II A, or specify clearly how the Smith42 dataset and bamfai catalog relate (e.g., Smith42/galaxies is the parent images; bamfai/galaxy-chirality-catalog is the derived catalog).

*(As a citation-forensics auditor I cannot resolve these URLs via web search, because they are not guaranteed to match any existing public resource; the current formatting is not syntactically valid and must be corrected.)*

---

P4-E5 (ESSENTIAL)  
Section: References [1]–, page 9–10  
Problem: Several references to Shamir and related spin-parity works compress multiple papers into a single entry or have metadata inconsistencies:

- [1] “L. Shamir, ‘Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,’ Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.”  
  Web search confirms arXiv:2007.16116 is titled “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity asymmetry and multipoles” in Astrophysics and Space Science 365:136 (2020). The title in the reference omits “asymmetry”.  
- [2] “L. Shamir, ‘Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,’ Publ. Astron. Soc. Jpn. 74, 1114 (2022), DOI:10.1093/pasj/psac058.”  
  Web search confirms psac058 corresponds to that PASJ paper, but the text treats [2] and [3] as if they were distinct Shamir (2022) results when [3] is in MNRAS 516 (2022). This may confuse readers if the main text attributes content between them incorrectly.  
- [3] “L. Shamir, ‘Analysis of spin directions of galaxies in the DESI Legacy Survey,’ Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.”  
  Web search confirms arXiv:2208.13866 is “Analysis of spin directions of galaxies in the DESI Legacy Survey” in MNRAS 516, 2281–2295 (2022). This one is correct.  
- [4] “L. Shamir, ‘Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis,’ Phys. Lett. B 715, 25 (2012), arXiv:1207.5464.”  
  Web search confirms this metadata is correct.  

Required fix:  
1. Correct the title for [1] to match the published title (include “asymmetry”) and double-check all Shamir titles and DOIs against arXiv/ADS.  
2. In the main text (Sec. V A) ensure that statements about “Shamir (2020)” and “Shamir (2022)” are correctly mapped to references [1], [2], and [3], and that you do not conflate the PASJ paper [2] (general spin-pattern analysis) with the DESI Legacy-specific MNRAS paper [3]. If necessary, adjust the in-text citations to specify which Shamir 2022 paper each statement refers to (e.g., Shamir 2022a vs 2022b).  

*(These checks are based on arXiv/ADS information, which confirms the arXiv IDs and venues but identifies the title discrepancy for [1].)*

---

P4-M1 (MAJOR)  
Section: Abstract and Conclusion, pages 1 and 7  
Problem: The claim “The present null disfavors the Shamir ∼ 2–4% detection class at the amplitude level under our pipeline… by a factor of ∼ 6–12” is presented without a clear quantitative mapping from the Shamir dipole amplitudes (which are per-bin asymmetries and may be defined differently) to the current paper’s dipole amplitude parameter A and detection threshold. In particular, Shamir’s 2–4% is sometimes a per-hemisphere excess rather than a full-sky dipole amplitude, while this work’s 0.75% sensitivity is a full-amplitude injected dipole defined in a specific HEALPix map.  
Required fix: Provide a more explicit, quantitative comparison:

- State precisely how Shamir’s quoted 2–4% is defined (e.g., difference in CW fraction between opposite hemispheres, maximum regional asymmetry, or a fitted dipole amplitude).  
- Translate that into the A parameter used in this paper or vice versa, so that “factor of 6–12” is directly computed from clearly defined metrics.  
- If such a direct translation is not possible due to methodological differences, soften the claim to a qualitative statement (e.g., “Our null is inconsistent with dipole amplitudes at the few-percent level in the same observable, under our pipeline assumptions; a formal exclusion of Shamir’s pipeline requires a matched-footprint reanalysis.”) and explicitly state the limitations.

---

P4-M2 (MAJOR)  
Section: VII Conclusions, item (d), page 7  
Problem: The statement “A future survey detecting a chirality dipole at σ > 5 with amplitude ≳ 0.75% at ≥ 10^7 galaxies would falsify the present null” is too strong, given that the present null is conditional on specific analysis choices (DESI Legacy footprint, ViT-Small classifier, TTA protocol, monopole subtraction, and null procedures). A future >5σ detection could in principle arise in a different redshift range, galaxy population, or observable (e.g., 3D spin vectors) without contradicting the specific late-time 2D morphology-channel null reported here.  
Required fix: Rephrase this as a conditional falsification criterion that acknowledges scope:

- For example: “A future survey, using comparable analysis methodology and targeting a similar redshift and morphology-selected sample, that detects a chirality dipole at σ > 5 with amplitude ≳ 0.75% would be in strong tension with the present null.”  
- Explicitly note that different observables (e.g., redshift-dependent 3D spins, different selection functions) might probe different physics and need not strictly “falsify” this result.

---

P4-M3 (MAJOR)  
Section: Sec. II B “Training Labels”, page 2; Appendix B, page 7–8  
Problem: The paper states that 67.6% of training labels come from CE-ResNet predictions and that an independent GZ1 cross-match yields 69.91% accuracy (κ = 0.40), which is then used as a “conservative accuracy floor”. However, the propagation of this 69.91% to the “sub-percent systematic floor” is only briefly mentioned (Sec. IV C and VI A) and is not quantitatively derived. The chain from label noise to effective sensitivity degradation is critical to the claimed 0.75% floor and to all upper limits.  
Required fix: Provide a simple analytic or empirical calculation showing:

- How a 69.91% binary accuracy implies an effective dilution factor on dipole amplitude (e.g., via a factor (2p − 1) in the observable).  
- How this factor feeds into the 0.75% injection threshold and the statement that the “true-underlying threshold” is ∼1.19%.  
- If this is based on simulations, describe them briefly and refer to specific tables or figures where the effect is measured.

---

P4-M4 (MAJOR)  
Section: Sec. IV C, Table III, Appendix A and D, pages 4–5, 7–8  
Problem: The use of NaMaster and the distinction between the “subsample mask” and “canonical mask” are central to the claim of a robust ℓ=1 null versus a systematic canonical residual. However, the definitions are somewhat scattered, and in particular:

- The subsample mask is called a “strict-superset subsample mask (n = 5,547,858, fsky = 0.659)” but its construction (beyond Nspiral > 10) is not clearly specified in the main body; it appears only in Appendix A as “analysis subsample mask”, yet the selection criteria (e.g., depth cuts, quality cuts) are not spelled out.  
- The canonical mask is only loosely described as “patchy” and “canonical-N”; the exact relation between the canonical and subsample masks—what pixels are excluded/added and why—is not clear.  

This ambiguity matters because the headline null hinges on the subsample-mask result rather than the canonical-mask result.  
Required fix: Add a short subsection in Sec. III or IV clearly defining:

1. How the canonical mask is built (per-pixel thresholds, footprint, any additional veto regions).  
2. How the subsample mask differs, with explicit criteria (e.g., pixels with Ntotal > X, removal of specific legs, depth/quality cuts).  
3. A brief rationale for why the subsample mask is the primary cosmological estimator while the canonical mask is “diagnostic” only.

---

P4-M5 (MAJOR)  
Section: Sec. II A “Galaxy Images”, page 2  
Problem: The description “Smith42/galaxies dataset on HuggingFace (… 8,474,688 galaxy images)” is specific enough that readers may assume this is a stable, published dataset with fixed contents. As a citation forensics auditor, I cannot verify that such a dataset exists under that exact name, and there is no conventional astronomical publication associated with “Smith42”. PRD usually expects that critical data references are either to well-documented survey releases (e.g., DESI DR8) or to clearly citable DOIs for derived catalogs.  
Required fix: Either:

- Provide a formal citation for “Smith42/galaxies” with DOI or at least an arXiv/Zenodo reference, and confirm that its contents and selection function are stable; or  
- Explicitly state that “Smith42/galaxies” is a user-curated packaging of DESI DR8 cutouts, and move the primary data citation to DESI DR8  plus a self-hosted data DOI (e.g., Zenodo) describing the extraction procedure.  

This is important for long-term reproducibility.

---

P4-M6 (MAJOR)  
Section: AI tool usage (end of paper), page 9  
Problem: The paper states “AI tool usage: Large-language-model tools were used for code review and manuscript editing; all scientific results are derived from the authors’ own analysis and the cited public datasets.” PRD currently has evolving policies about LLM usage and may require explicit disclosure of which models, what version, and what role they played (editing only vs code generation vs analysis assistance). The current statement is vague.  
Required fix: Expand this to clarify:

- Which LLM(s) were used (e.g., “proprietary large language model hosted by X”), to the extent allowed by their terms.  
- That they were not used to generate or fit the scientific results or to perform non-reproducible analysis steps, but were limited to code review and editing.  
- That all code is available in the cited repository for independent verification.  

This will align the manuscript with evolving best practices for AI tool disclosure.

---

P4-N1 (MINOR)  
Section: Title, page 1  
Problem: The title contains an en-dash-like minus symbol in “A −0.122σ Subsample-Mask ℓ = 1 Null,” which may not survive all journal typesetting pipelines correctly and could be rendered inconsistently.  
Required fix: Replace “−0.122σ” with plain ASCII “-0.122σ” in the title or ensure that the minus sign is the journal’s preferred Unicode minus in all instances.

---

P4-N2 (MINOR)  
Section: Sec. IV A, Table II, page 4  
Problem: In Table II, the “Dev. (σ)” column lists “9.5” for Catalog C (equivariant), corresponding to the monopole deviation from 0.5. The text in Sec. IV B refers to “The Catalog C residual (9.5σ from 0.5000, Table II)… The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%…” However, the raw asymmetry is 0.5079 (0.79% excess) and the equivariant is 0.4974 (−0.26% excess), giving a suppression factor of about 0.79 / 0.26 ≈ 3.0, not 3.86. It is possible the 3.86 factor comes from a different pairing (e.g., A vs C), but this is not obvious.  
Required fix: Double-check the calculation of the “3.86× asymmetry-suppression factor” and explicitly show which tiers are compared (A vs C or A vs B or B vs C). Correct the factor if necessary, or specify the exact computation so readers can verify it.

---

P4-N3 (MINOR)  
Section: Sec. VI A “Sensitivity Floor…”, page 6  
Problem: The text states “Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” The use of fsky = 0.46 here is slightly inconsistent with earlier fsky values (0.49005 canonical, 0.659 subsample), and it is not explained how fsky = 0.46 is derived.  
Required fix: Clarify the origin of fsky = 0.46 in this calculation (e.g., effective overlap after cuts, HEALPix mask coverage after edge effects). If it is an approximation or an intermediate estimate, say so explicitly and, if possible, align all fsky values used in sensitivity estimates with the masks defined earlier.

---

P4-N4 (MINOR)  
Section: Data availability and throughout, pages 2–9  
Problem: The manuscript uses a mix of styles for survey names and dataset references, e.g., “DESI Legacy Imaging Surveys DR8” vs “DESI Legacy Survey” vs “DESI Legacy imaging”. Similarly, “Galaxy Zoo DESI predictions catalog” vs “Galaxy Zoo DESI”. This inconsistency can make citation forensics and future searches harder.  
Required fix: Standardize the nomenclature for major external datasets (e.g., always “DESI Legacy Imaging Surveys DR8” on first use, then “DESI Legacy DR8” thereafter; “Galaxy Zoo DESI” as in Walmsley et al. ) and ensure the same form is used consistently across the text and references.

---

P4-N5 (NIT)  
Section: Sec. III C, Eq. (2), page 3  
Problem: The use of the half-factor is written as “12” instead of an explicit 1/2, which may be a typographical artifact of PDF text extraction (“12 PCW^orig” rather than “½ P_CW^orig”). While a reader can infer the intent, it is not typographically correct.  
Required fix: Ensure that in the LaTeX source the factor is clearly typeset as 1/2 (e.g. “\tfrac{1}{2} P_\mathrm{CW}^{\mathrm{orig}} + \tfrac{1}{2} P_\mathrm{CCW}^{\mathrm{flip}}”) and that in the final PDF the fraction is unambiguous.

---

P4-N6 (NIT)  
Section: Appendix D, boundary-distance variance check, page 8  
Problem: The phrase “signal is NOT a positive detection…” uses all caps “NOT”, which is stylistically informal for PRD and could be toned down.  
Required fix: Replace “NOT” with italic emphasis (“not”) or rephrase the sentence in standard formal style.

---

Length and focus assessment  

P4-M7 (MAJOR)  
The paper is 10 pages, with substantial space devoted to appendices detailing NaMaster configuration, classifier training, and systematic diagnostics. Given the claimed main contribution—a null ℓ=1 chirality-dipole measurement and identification of a monopole–mask leakage channel—the length is borderline but defensible. However, parts of Appendices C–E read as extended narrative rather than tightly summarized diagnostic results.  
Required fix: Consider tightening:

- Reduce narrative repetition in Appendices C and D, focusing on key quantitative outcomes (e.g., just list the strongest discriminators against interpretation (i) and (iii)).  
- Move non-essential implementation details for the bias tests to the code repository documentation, keeping only thresholds and pass/fail results in the paper.  

A leaner version at 8–9 pages of main text plus concise appendices would improve clarity without sacrificing reproducibility.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents an interesting and methodologically careful chirality-dipole null result, but several issues must be addressed before it can be considered for publication: σ-values from different nulls are juxtaposed without repeated explicit “not directly comparable” disclaimers as required, some central quantitative claims (sensitivity floor, Shamir comparison, canonical residual statistics) need clearer definitions and reconciliations, data and URL references require correction and standardization, and a few reference metadata items must be aligned with arXiv/ADS records. With these essential and major corrections, plus some tightening of appendices, the manuscript could become a solid and reproducible contribution.