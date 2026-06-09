# P4 auto-2026-06-08_1737pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (16928 chars)
**Wall time**: 88.1s

---

P4-E1 (ESSENTIAL)  
Section: Data Availability, page 11  
Problem: The catalog URL is given as “https://huggingface.co/datasets/bamfai/galaxy- chirality- catalog (CC-BY-4.0, Parquet; three tiers A/B/C). Release tag: v2026.04.” The repository “bamfai/galaxy-chirality-catalog” does not exist on HuggingFace as of the current date, and the name with spaces “galaxy- chirality- catalog” is syntactically invalid as written. The Smith42/galaxies dataset referenced earlier also appears not to be a real public DESI-based chirality dataset on HuggingFace under that exact name. Required fix:  
- Provide the **actual, existing** dataset identifier(s) and verify that they resolve on HuggingFace. If the catalog is not yet public, state this explicitly and remove or replace the current broken URLs and version tag.  
- Likewise, verify and correct the “Smith42/galaxies” HuggingFace dataset name in Sec. II A so that it points to an existing dataset, or clearly mark it as a private/internal dataset if so.  

P4-E2 (ESSENTIAL)  
Section: Abstract, page 1; Sec. IV C, Table I / Table III, multiple pages  
Problem: The abstract claims that “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.” However, later sections and the Conclusions repeatedly compare amplitude “disfavor” or “discrepancy factors” across estimators that use different nulls (e.g., comparing the −0.122σ MASTER result to the +0.43σ real-space dipole; comparing the ℓ = 1 pseudo-Cℓ σ values to real-space σ). Even when the non-comparability caveat appears once in the abstract, **whenever σ values from different nulls are juxtaposed for interpretive comparison, PRD requires explicit reminders that they are not directly comparable**, otherwise readers will interpret relative σ as directly meaningful. Required fix:  
- At every place where σ values from different null procedures are put side-by-side in a way that invites comparison (e.g., “−0.122σ (subsample mask, headline) / +0.43σ (real-space cross-check)”), explicitly add language such as “note: these significances are defined with different nulls and are not directly comparable.”  
- Check all sections, tables, and appendices for such juxtapositions and add the qualification in each instance, not only in the abstract.  

P4-E3 (ESSENTIAL)  
Section: Conclusion (d), page 8  
Quoted text: “The empirical 50%-recovery-at-3σ threshold is A ≈ 0.75% (full amplitude) under per-pixel-shuffle nulls; the statistical-only Fisher floor is ∼ 0.29%. The catalog is a community resource: 8.47M galaxies, raw + calibrated + equivariant probabilities, sky coordinates, confidence scores, and quality-control flags, publicly available on HuggingFace (CC-BY-4.0). A future survey detecting a chirality dipole at σ > 5 with amplitude ≳ 0.75% at ≥ 107 galaxies would falsify the present null.”  
Problem: The claimed “falsification criterion” is not rigorously demonstrated. The 0.75% threshold is derived from an injection test on a **much smaller HC subsample** (471,049 spirals) with its own null, yet is applied as a hard falsification criterion for future surveys with ≥ 10⁷ galaxies. That extrapolation ignores differences in systematics, classifier properties, and survey geometry, and is not supported quantitatively. Required fix:  
- Rephrase “would falsify the present null” to a weaker, correctly scoped statement (e.g., “would be in strong tension with the present null under similar analysis assumptions”).  
- Clarify explicitly that the 0.75% threshold is an **empirical sensitivity figure specific to the HC subsample and this pipeline**, not a universal falsification bound for all future surveys.  

P4-E4 (ESSENTIAL)  
Section: I. Introduction, citations [1–7], page 2; Sec. V.A/B, page 6–7; References, pages 11–12  
Problem: Several citations to Shamir, Iye, Tadaki, and Jia must be checked for metadata correctness and for the specific statistics quoted in the text.

Verified items (correct):  
- [1] Shamir (2020), “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116 is accurate in title, journal, year, and arXiv ID.[5]  
- [5] Iye et al. (2021) “Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,” ApJ 907, 123 (2021), arXiv:2011.00662 is correct.[5]  
- [6] Tadaki et al. (2020) “Spin parity of spiral galaxies. II. A catalogue of ∼ 80,000 face-on spirals,” MNRAS 496, 4276 (2020), arXiv:2006.02331 is correct.  
- [7] Jia, Zhu & Pen (2023), “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” ApJ 943, 32 (2023), arXiv:2210.04168 is correct and gives cw/ccw ≈ 0.998 on ~1.95M galaxies in the abstract.[5]  

However:  
- [2] and [3] both list Shamir 2022 papers: [2] PASJ 74, 1114 (2022), arXiv?; [3] MNRAS 516, 2281 (2022), arXiv:2208.13866. Web search shows a Shamir PASJ 2022 paper with that title and DOI 10.1093/pasj/psac058, and a Shamir MNRAS 2022 paper “Analysis of spin directions of galaxies in the DESI Legacy Survey” with DOI 10.1093/mnras/stac2372.[5] The text refers to them as “Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries,” which is broadly consistent with their abstracts, but the **arXiv IDs are missing for [2]** (PASJ paper) and for [3] the arXiv ID 2208.13866 matches the MNRAS article, so metadata are likely correct but must be checked against arXiv directly by the authors (this reviewer cannot see the full arXiv entry text here). Required fix:  
- For [2], add the correct arXiv ID (if one exists; Shamir usually posts to arXiv) and verify the exact title and DOI string from PASJ.  
- Confirm that the quantitative statements in the text (per-bin asymmetries of ~5–20% in [4], global ~2–4% in [1,3]) match **explicit numbers in the abstracts or tables** of those papers; if not word-for-word traceable, either adjust the numbers or add a qualifier (“order-of-magnitude”) with explicit citations to the sections/tables used.  

P4-E5 (ESSENTIAL)  
Section: References ,,, page 12  
Problem: The paper cites three high-profile parity-violation analyses in the large-scale structure/CMB literature:  
-  “Measurement of parity-odd modes in the large-scale 4-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies,” MNRAS 522, 5701 (2023), arXiv:2206.03625, by Hou, Slepian & Cahn.[1][5]  
-  “A test for cosmological parity violation using the 3D distribution of galaxies,” Phys. Rev. Lett. 130, 201002 (2023), arXiv:2110.12004, by Cahn, Slepian & Hou.[3]  
-  Komatsu (2022) review in Nature Rev. Phys. 4, 452 (2022), arXiv:2202.13919.  

In the main text (Sec. VI.B), these works are described qualitatively, but there are **no explicit numbers or σ significances quoted**, which is consistent with not needing detailed forensic verification of stats. However, the **citation strings themselves** must be checked:  
-  should explicitly list “Mon. Not. R. Astron. Soc. 522, 5701 (2023), arXiv:2206.03625” – the current text omits the volume/page and arXiv for .  
-  should list the correct PRL volume and page, “Phys. Rev. Lett. 130, 201002 (2023), arXiv:2110.12004,” which appears correct but should be rendered uniformly with APS style (no abbreviation “Phys. Rev. Lett. 130, 201002 (2023)” is fine, but check formatting).  
-  should give the correct arXiv ID 2202.13919, which is not shown in the supplied snippet. Required fix:  
- Complete and standardize the reference entries for – with volume, page, year, and arXiv ID exactly as in the journal records.  

P4-E6 (ESSENTIAL)  
Section: Data Availability, page 11; Appendix A, Data vector description  
Problem: There is a subtle but critical **notation and consistency issue** between the text description of the NaMaster field and the field actually used. In Appendix A the asymmetry field is defined once as  
- “Ap = (NCW(p) − NCCW(p))/Nspiral(p) (spirals only).”  
Later in the same appendix, the field is described as  
- “Ap = (NCW(p) − NCCW(p))/Ntotal(p), with galaxy-weighted mask-mean subtraction…”  

Using Nspiral vs Ntotal in the denominator **changes the field definition** and can materially affect the amplitude and variance. The text attempts to clarify that “The quantity Nmap,weighted = Σ Wp = 5,547,858 reported in Table I is the sum of these pixel weights; it exceeds Ncatalog,spiral = 3,201,160 because each Wp includes non-spiral objects.” But it leaves ambiguous whether the pseudo-Cℓ field is normalized by spiral counts or all galaxies. Required fix:  
- Explicitly state, in one place, the **exact field definition actually passed to NaMaster (both for the canonical-mask case and the subsample-mask headline run)** and ensure that the notation is consistent throughout Appendix A and the main text.  
- If the headline −0.122σ result uses spiral-only normalization, use that uniformly; if all-galaxy weighting is only in Wp, make this distinction unambiguous and delete the conflicting “Ntotal” definition.  

P4-E7 (ESSENTIAL)  
Section: Appendix A “Monopole subtraction,” pages 9–10; Sec. IV.D, Table IV  
Problem: The monopole-subtraction description and the generative monopole-only null are partly in tension and not fully reproducible from the text. Specifically:  
- Appendix A states: “The monopole subtraction is performed at the data-vector construction step so that the ℓ = 0 mode is removed from the input field, and the MASTER mode-coupling matrix does NOT include ℓ = 0…” But Sec. IV.D says they use a “separate input field constructed WITHOUT monopole subtraction precisely to expose the leakage,” and Table IV reports pre-MASTER pseudo-Cℓ and a 99.3% reproduction by the binomial null.  
- The footnote then acknowledges that the wording “Binomial(ntotal, pglobalCW)” was ambiguous between Nspiral(p) and Nall(p), and that the code uses Nspiral(p), while a rerun with Nall(p) is “in queue” and the impact is “not predictable analytically.” That means **the quoted 99.3% reproduction and +1.68σ residual are tied to a particular, non-final implementation**. Required fix:  
- Remove or clearly demote (e.g. into a “current-status” note) any result that explicitly depends on a **rerun that has not yet been completed**. Either finish the Nall(p) rerun and update the pre-MASTER reproduction figure and σ, or state that all headline monopole-leakage claims are based on the Nspiral(p)-trial generative null and that an alternative weighting remains future work.  
- Ensure that the final published version only presents **completed, stable calculations**, and reconcile the description of monopole subtraction vs. non-subtracted fields so that a reader can reproduce exactly which field is used in which analysis.  

P4-M1 (MAJOR)  
Section: Abstract vs. Sec. VI.A, pages 1 and 7–8  
Problem: The abstract states a “demonstrated empirical 50%-recovery-at-3σ threshold under the adopted per-pixel-shuffle null on the HC pipeline” of A ≈ 0.75%. Sec. VI.A explains that this comes from “N = 471,049 HC-spiral subsample (NMC,null = 1000, NMC,inj = 100 per amplitude),” with P(σ > 3) = 0.55 at A = 0.75% and 0.15 at 0.5%. However, the **statistical uncertainty on the 0.55 estimate is non-negligible**, and the dependence on choice of null (per-pixel shuffle), number of MC trials, and HC selection is substantial. The abstract presents the number as a sharp threshold without error bars or caveats. Required fix:  
- In the abstract, soften the statement to “we empirically find ~50% recovery at 3σ for A ≈ 0.75% in an HC subsample under a per-pixel-shuffle null,” and refer explicitly to Sec. VI.A for methodological details and uncertainties.  
- Add an estimate of the binomial error on P(σ > 3) (from 100 injections) and briefly note the sensitivity of this threshold to sample selection and null choice.  

P4-M2 (MAJOR)  
Section: II.B Training Labels, page 2  
Quoted text: “Note: 67.6% of training labels derive from CE-ResNet predictions; validation metrics against the full training set therefore partially reflect agreement with CE-ResNet rather than independent ground truth. The independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy 69.91% (Cohen’s κ = 0.40). We treat 69.91% as the conservative accuracy floor and propagate it to all downstream isotropy bounds via the sub-percent systematic floor in Sec. IV C.”  
Problem: The text claims to propagate the 69.91% accuracy as a “sub-percent systematic floor” into all isotropy bounds, but the paper does **not provide an explicit mathematical propagation** (e.g., how g = 2a−1 ≈ 0.398 enters the Fisher threshold and null distributions for the pseudo-Cℓ estimators). Only in VI.A does the GZ1 dilution factor appear implicitly. Required fix:  
- Add a concise derivation showing how the measured accuracy a translates into an effective signal dilution factor g and how that alters the effective noise on A and hence the sensitivity floor.  
- Explicitly connect this derivation to the injection-recovery tests and to the quoted “true-underlying threshold ∼ 1.88%,” which is otherwise unexplained in the main text.  

P4-M3 (MAJOR)  
Section: Abstract and Sec. VII(a), pages 1 and 8  
Problem: The phrase “The present null disfavors the Shamir ∼ 2–4% detection class at the amplitude level under our pipeline; a matched-footprint Ganalyzer reanalysis is required for a formal σ-level exclusion” is potentially misleading without quantitative support. The work does not perform a matched-footprint reanalysis, and the sensitivity floor is ≳0.75% under specific assumptions; Shamir’s claimed signal is ~2–4% but in different data and with different systematics. The phrase “disfavors” suggests a statistical tension that is not actually quantified (no Bayesian evidence, no likelihood ratio). Required fix:  
- Either provide a concrete calculation of the **expected σ-level** at which a 2–4% dipole would appear in this catalog given the measured noise and classification systematics, or rephrase to a more agnostic statement (e.g., “our null is in tension with models predicting a ≥2% dipole on the DESI Legacy footprint, but a direct comparison to Shamir’s SDSS-based claims requires a matched analysis, which is beyond the scope of this work”).  

P4-M4 (MAJOR)  
Section: II.A Galaxy Images, page 2  
Problem: The paper states that the parent sample is “the Smith42/galaxies dataset on HuggingFace (https://huggingface.co/datasets/Smith42/galaxies), containing 8,474,688 galaxy images from the DESI Legacy Imaging Surveys DR8.” As of now, a dataset with this exact path does not appear to exist on HuggingFace, and “Smith42” appears to be a placeholder username rather than a recognized DESI or Galaxy Zoo producer. This calls into question the **reproducibility** and identifiers of the primary data. Required fix:  
- Replace “Smith42/galaxies” with the **actual, publicly available** dataset name if it exists.  
- If this is an internal or private dataset, clearly state that it is not yet public and cannot be directly accessed by readers; in that case, provide precise instructions for reconstructing the sample from DESI DR8 and Galaxy Zoo DESI using public data and selection criteria.  

P4-M5 (MAJOR)  
Section: Figures 1–4, captions and internal consistency (pages 5–8)  
Problem: The text frequently references “Figure 1. Test-time D4 equivariant averaging (TTA)” and similar, but the method described in §III C explicitly restricts production TTA to **2-fold (original + horizontal flip)**, with full D4 TTA used only in validation on small subsamples. The caption of Fig. 1 states “For each input image x, the classifier is evaluated on the eight D4 transforms… Output probabilities are averaged… This averaging is the key methodology distinction between Catalog A… and Catalog C.” That implies that **production Catalog C uses full D4 TTA**, which contradicts the Methods section that clearly says they restrict to 2-fold TTA in production. Required fix:  
- Correct the Fig. 1 caption to accurately reflect that **only 2-fold flip TTA is used for the main catalog**, with D4 TTA applicable only to specific validation experiments described in Appendix B.  
- Ensure consistency across text, figure, and appendix on exactly which group of transformations is used in production vs. tests.  

P4-M6 (MAJOR)  
Section: End of main text and Data Availability, pages 10–11  
Problem: The “AI tool usage” statement acknowledges use of LLMs “for code review and manuscript editing.” Given PRD’s standards, this raises two concerns: (1) potential contamination of prose with unvetted claims, and (2) the reproducibility of code that may have been partly generated or altered by an AI system. There is no indication that **all scientific results have been independently verified** beyond reliance on code that may have been LLM-assisted. Required fix:  
- Add a short methodological note (e.g., in Methods or an appendix) clarifying that all numerical results have been independently validated (e.g., via unit tests, sanity checks, cross-check scripts) and that AI-assisted code suggestions were reviewed and tested by the author.  
- Alternatively, if such validation was not done, it must be done and documented before PRD publication.  

P4-M7 (MAJOR)  
Section: Abstract and Sec. VI, overall length and focus  
Problem: The paper runs to 12 pages (plus appendices) and includes extensive detail on classifier architecture, bias tests, and mask diagnostics. For a PRD cosmology methods paper whose **headline result is a null detection at sub-percent level**, the amount of architecture detail and internal diagnostic prose is excessive relative to the actual cosmological inference. This dilutes focus and makes it harder to see the core methodological advance (equivariant TTA + monopole leakage generative null). Required fix:  
- Condense the architecture/training/diagnostic descriptions (e.g., move much of Appendix B and D to a code documentation repository or supplementary material, summarizing in 1–2 paragraphs in the main text).  
- Aim for ≤ 9 main-text pages by tightening redundant explanations of the same bias-hardening logic, while keeping all core equations, the definition of the estimators, and the key null tests.  

P4-m1 (MINOR)  
Section: Title and Abstract, page 1  
Problem: The title is extremely long and uses multiple hyphenated clauses (“A −0.122σ Subsample-Mask ℓ = 1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence…”). This is stylistically non-standard for PRD and makes it difficult for indexing services. Required fix:  
- Shorten the title to one main clause plus a subtitle, e.g. “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null ℓ = 1 Dipole on 3.2M DESI Legacy Spirals,” and move details about the monopole leakage and canonical-mask residual into the abstract.  

P4-m2 (MINOR)  
Section: PACS numbers, page 1  
Problem: PRD is transitioning away from PACS; the current practice is to use **Standard Subject Classification** or none. Required fix:  
- Check the current PRD author guidelines and either replace PACS with the recommended classification or remove them if no longer requested.  

P4-m3 (MINOR)  
Section: Footnote 1 in Sec. IV.D, page 4–5  
Problem: The text: “The per-pixel trial-count inflation factor ⟨Nall /Nspiral ⟩ ≈ 1.49 propagates directly into the binomial variance… the size of the resulting shift in the headline 99.3% reproduction figure… is not predictable analytically…” This is misleading; the effect of changing the binomial trial number on the variance is analytically straightforward, even if the impact on a derived percentage-of-data statistic is not. Required fix:  
- Rephrase to: “the precise impact on the 99.3% reproduction fraction must be evaluated numerically in the full pipeline; while the variance scaling with trial count is analytic, its effect on the end-to-end pseudo-Cℓ statistic is not trivial to obtain in closed form.”  

P4-m4 (MINOR)  
Section: Sec. III B, Model Architecture, page 3  
Problem: The description “LayerNorm → 384→512 (GELU, d=0.3) → 512→256 (GELU, d=0.2) → 256→3 (softmax)” is clear but lacks exact layer names as in the released checkpoint or code. For reproducibility, PRD typically expects exact architecture details. Required fix:  
- Either add a table listing the precise PyTorch module stack (e.g., Linear(384,512), GELU, Dropout(0.3), etc.) or state explicitly that the architecture is identical to a well-known reference implementation (e.g., timm’s ViT-Small) except for this head, which is fully specified in the public code repository.  

P4-n1 (NIT)  
Section: Throughout (e.g., abstract, Sec. IV.D heading)  
Problem: Inconsistent hyphenation and spacing: “subsample mask,” “subsample-mask,” “canonical mask,” “canonical-mask” all appear. This is cosmetic but slightly confusing. Required fix:  
- Standardize terminology: pick either “subsample mask” and “canonical mask” (no hyphen) or consistently use hyphenated forms when used adjectivally (“subsample-mask MASTER result”).  

P4-n2 (NIT)  
Section: Reference list ordering, page 11–12  
Problem: References are not strictly ordered by citation appearance (e.g., [2] and [3] both Shamir 2022 but in slightly odd order relative to citations in text). PRD typically expects references to be ordered by citation order. Required fix:  
- Reorder references to follow the order in which they first appear in the manuscript and adjust numbering accordingly.  

P4-n3 (NIT)  
Section: Typographical consistency, multiple pages  
Problem: Some minor issues:  
- “3D random-walk simulations” vs. “3D random walk simulations” (hyphen usage).  
- “dipole-only explanation is disfavored” vs. “interpretation (i) as a clean dipole-only explanation is disfavored” (slight redundancy).  
- Occasional double spaces and linebreak artifacts due to TeX extraction. Required fix:  
- Run a careful copy-edit sweep to standardize hyphenation and remove redundant wording/spacing.  

## Summary recommendation

MAJOR REVISIONS

The paper presents a technically interesting survey-scale chirality analysis with careful attention to classifier systematics and mask-induced leakage, but it falls short of PRD standards in several key areas: reproducibility (nonexistent or placeholder dataset URLs, ambiguous field and null definitions), over-strong interpretive claims (especially regarding falsification criteria and “disfavoring” prior work), and some internal inconsistencies (D4 vs. 2-fold TTA, apportioning of σ’s across different nulls). These issues require substantial but tractable revisions to the analysis description, citation metadata, and claims in the abstract and conclusions before the work can be considered for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-N1 (NEW ESSENTIAL)  
Class: A (ARITHMETIC) – global CW fraction and “Excess / Dev.(σ)” in Table II, and propagated numbers in text and abstract  
Problem: Several key percentages and σ-values do not match the counts or each other when recomputed. These propagate into the main narrative.  

Specific issues:

1. **Global CW fraction from raw counts vs. quoted value**  
   - Catalog C counts given in text and Fig. 2: NCW = 1,592,107; NCCW = 1,609,053; Nspiral = 3,201,160.[Text/Fig. 2]  
   - Recomputed CW fraction:  
     \( f_{\rm CW} = 1{,}592{,}107 / 3{,}201{,}160 \approx 0.49732 \).  
   - Table II and multiple places in text quote **0.4974**. The difference (~8×10⁻⁵) is small but non‑zero; for a flagship number that appears many times, this should be internally consistent and derived from exactly the same counts. Either the counts or the fraction have been rounded inconsistently, or the counts in the figure are stale relative to the numbers used for the fraction.  

2. **Binomial σ and “Dev.(σ)” in Table II**  
   - The caption says σ = √[p(1−p)/N] with Nspiral = 3,201,160. Using the quoted C‑tier fCW = 0.4974 gives  
     σ ≈ √[0.4974×0.5026 / 3,201,160] ≈ 2.79×10⁻⁴, matching the “±0.000279”.  
   - The “Deviation from 0.5 in σ units” should be  
     \((0.4974 − 0.5)/0.000279 ≈ −9.3σ\), not **−9.5σ** as printed.  
   - For Tier A: 0.5079 → Δ = 0.0079; 0.0079/0.000279 ≈ 28.3, not **28.8**.  
   - For Tier B: 0.504 → Δ = 0.004; 0.004/0.000279 ≈ 14.3, not **14.6**.  
   These sigmas appear to have been computed with a slightly different σ (perhaps using p=0.5 or an older Nspiral) and then not updated when the table was finalized.  

3. **“Global CW-fraction shift from +2.05% (A) to −0.53% (C)” vs. numbers in Table II**  
   - Table II’s “Excess(%)” gives:  
     - Tier A: +0.79%  
     - Tier C: −0.26%  
   - The caption of Fig. 1 and the text state a shift from **+2.05%** (A) to **−0.53%** (C), i.e. a 2.58‑percentage‑point change. That is inconsistent with both the table entries and the raw fractions (0.5079–0.4974 ≈ 1.05 percentage points).  
   - At least one of these sets of numbers is stale. The paper needs to:  
     - Decide what the current, correct A/B/C global fractions are, recompute the “Excess(%)” and “Dev.(σ)” from those, and  
     - Update all prose (including Fig. 1 caption and §IV B, §VI Discussion) to use the same numbers consistently.  

4. **“3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%” (§IV B)**  
   - Using the numbers actually shown in Table II (0.79% → 0.26%) gives a suppression factor of ≈ 0.79/0.26 ≈ 3.0.  
   - Using the prose numbers 2.05% → 0.53% gives ≈ 3.87.  
   - The stated factor **3.86×** matches only the stale pair 2.05%/0.53%, and not the table values. Once the correct raw and equivariant asymmetries are fixed, this factor should be recomputed explicitly and updated.  

Required fix:  
- Recompute all “Excess(%)” and “Dev.(σ)” entries in Table II from the actual current NCW, NCCW, and Nspiral.  
- Ensure the global fractions quoted in the abstract, §IV B, §VI, Fig. 1 caption, and Fig. 2 caption all match those recomputed numbers.  
- Recalculate the “asymmetry-suppression factor” with the final pair of asymmetries and adjust the 3.86× figure accordingly.  
- Explicitly state whether the binomial σ is computed using p = 0.5 or the measured fCW; use that consistently when deriving “Dev.(σ)”.  

---

P4-N2 (NEW ESSENTIAL)  
Class: A (ARITHMETIC) – significance values and signs in Table III  

Problem: Several σ values in Table III are inconsistent with the listed Cℓ and σnull, and one has an inconsistent sign.  

Example checks:

1. **ℓeff = 9 bandpower ([7, 11])**  
   - Cℓ = −0.248×10⁻⁶, σnull = 0.574×10⁻⁶.  
   - Naively (Cℓ − 0)/σnull ≈ −0.432σ. Table reports **+2.232σ**. There is a sign mismatch and a magnitude mismatch. Even if the comparison is to a nonzero null mean, the sign cannot change unless the null mean exceeds Cℓ in magnitude and of opposite sign, which would need to be explicitly shown.  

2. **ℓeff = 14**  
   - Cℓ = −0.387×10⁻⁶, σnull = 0.446×10⁻⁶.  
   - (Cℓ − 0)/σnull ≈ −0.87σ. Table reports **+2.626σ**. Again both sign and magnitude mismatch the obvious computation.  

3. **ℓeff = 19**  
   - Cℓ = −0.576×10⁻⁶, σnull = 0.420×10⁻⁶ → (Cℓ − 0)/σnull ≈ −1.37σ. Table shows **+2.229σ**.  

4. **ℓeff = 24**  
   - Cℓ = −0.648×10⁻⁶, σnull = 0.366×10⁻⁶ → ≈ −1.77σ; table reports **+2.470σ**.  

5. **ℓeff = 4**  
   - Cℓ = 3.210×10⁻⁶, σnull = 0.804×10⁻⁶ → ≈ +3.99σ, but the table lists **+6.097σ**. This could in principle be using (Cℓ−⟨Cℓ,null⟩)/σnull with a negative null mean, but no null mean is shown here, while it is explicitly included in §IV C for ℓ=1.  

The text describes these lines as “Residual mask coupling,” but σ is clearly intended as (data−null mean)/σnull, as in the ℓ = 1 entry just above and in §IV C. As printed, the signs and magnitudes are irreproducible from the numbers shown.  

Required fix:  
- For each bandpower in Table III, explicitly state the null mean ⟨Cℓ,null⟩ if σ is computed relative to a non‑zero mean, or else confirm that the σ column is simply Cℓ/σnull.  
- Recompute the σ values using the actual null means and σnull and update the table so that the σ column matches Cℓ, ⟨Cℓ,null⟩, σnull as printed.  
- Ensure consistency between Table III, any corresponding plot in Fig. 4, and any text references to these σ values (e.g., “ℓ = 2 > ℓ = 1 broadband structure” in Appendix D).  

---

P4-N3 (NEW MAJOR)  
Class: B (FIGURE CAPTION VS BODY CLAIM) – Fig. 2 spiral fraction vs. text  

Problem: Fig. 2 caption describes the Catalog C composition and claims that “The spiral sub-catalog Nspiral = NCW+NCCW = 3,201,160 is the analysis target for all chirality statistics below (Table II et seq.).” Table I and Table II also use Nspiral = 3,201,160 as the base count. The abstract and §II A, however, refer to “3,201,160 DESI Legacy spiral galaxies (8.47 M sources, 471 049 high-confidence per-spiral after peqCW > 0.9).”  

The body further states in §IV A that the spiral fraction is 37.78% and that the spiral fraction is uniform across the footprint at the ≲2% level (§E, Appendix E). There is no explicit cross‑check that the plotted counts in Fig. 2 (log10 N per pixel) are consistent with the total Nspiral, NNS, and Ntotal used elsewhere. While this is mostly a bookkeeping issue, the paper repeatedly uses Nspiral both as an absolute count and as a derived fraction; small inconsistencies (as in P4‑N1) suggest Fig. 2 may be using an older or slightly different cut.  

Required fix:  
- Confirm that the total counts underlying Fig. 2 (summing over all NSIDE=64 pixels) reproduce exactly the quoted global totals NCW, NCCW, NNS, and Nspiral used in Table I and II.  
- If any minor discrepancies exist (e.g., from a slightly different mask or quality cut), state that explicitly in the Fig. 2 caption or in §IV A and give the correct numbers for each figure/dataset.  

---

P4-N4 (NEW MAJOR)  
Class: C (EQUATION DIMENSIONAL CONSISTENCY) – inconsistency of Ap definition between main text and Appendix A  

Problem: You already flagged in P4‑E6 that there is an inconsistency between normalizing Ap by Nspiral vs Ntotal; the fresh pass shows that this is not just a wording glitch but a direct conflict between Eq. (3) and Appendix A’s final configuration, and it propagates into the definition of the generative null.  

- **Eq. (3) in §IV C** defines  
  \( A_p = (N_{\rm CW}(p) - N_{\rm CCW}(p)) / (N_{\rm CW}(p) + N_{\rm CCW}(p))\), i.e. spiral-only normalization.  
- The NaMaster configuration in Appendix A first restates that same definition (“spirals only”) and then later states:  
  “Field: scalar (spin‑0) asymmetry map \(A_p = (N_{\rm CW}(p) − N_{\rm CCW}(p))/N_{\rm total}(p)\), with galaxy-weighted mask-mean subtraction…”  
- The footnote in §IV D clarifies that the generative null uses Nspiral(p) as the trial pool, while the main NaMaster field apparently uses Ntotal(p) in the denominator.  

Dimensional consistency here is not just about units: the statistical meaning of \(A_p\) changes if the denominator includes non-spirals. Equation (3), Appendix A’s first paragraph, the footnote defining the generative null, and the final “Field” definition cannot all be simultaneously true. This affects:  
- The exact variance of Ap and therefore σnull for ℓ = 1.  
- The interpretation of the binomial generative null in Table IV.  

Required fix (stronger than P4‑E6, as a consistency/specification failure):  
- Declare a single, authoritative definition of \(A_p\) for all NaMaster‑based results (both canonical mask and subsample mask), including whether the denominator is Nspiral or Ntotal, and whether any rescaling is applied.  
- Ensure Eq. (3), the generative null footnote, the earlier part of Appendix A, and the final “Field: …” line are all edited to reflect that same definition.  
- If different definitions were indeed used for different analyses (e.g. spiral-only field for one test, all-galaxy normalization for another), specify clearly which one is used where, and recompute any σ and reproduction fractions that depend on the mis‑described configuration.  

---

P4-N5 (NEW ESSENTIAL)  
Class: E (NULL PROCEDURE COMPARABILITY) – unqualified cross‑null σ juxtapositions missed in previous review  

Your earlier P4‑E2 correctly identified the abstract-level caveat vs. later comparisons; a fresh pass reveals **additional** unqualified juxtapositions that were not previously enumerated:

1. **Methods hierarchy (§III A, bullet summary)**  
   - Bullet list presents:  
     - real-space dipole 0.43σ (isotropic bootstrap)  
     - MASTER ℓ = 1 −0.122σ (pp-shuffle)  
     - canonical MASTER +3.64σ (pp-shuffle, different mask and field treatment)  
     - hemisphere LEE statistic with pLEE ≤ 10⁻⁴ (max-stat MC)  
     - monopole+mask null +1.68σ (monopole-only generative)  
   These appear side by side in a ranked list without any per-item reminder that each σ is defined under a different null and, in some cases, a different field definition. This list strongly invites direct comparison of magnitudes.  

2. **Table I**  
   - Summarizes six estimators with σ columns: +0.43, −0.122, +3.64, “pLEE ≤ 10⁻⁴”, +1.68, and “50%-rec-3σ at A=0.75%”. The abstract-level warning is not repeated here. Readers scanning tables will almost certainly treat these σ values as directly comparable unless explicitly reminded otherwise in or under the table.  

3. **Conclusions §VII(b)**  
   - “A direct single-mode NaMaster execution … yields σcanonical = +3.64σ (pMC = 15/500 = 0.030). Two independent wider-coverage estimators … are null: real-space dipole 0.43σ and subsample-mask MASTER −0.122σ…”  
   All three significances are juxtaposed with no explicit “different nulls” qualifier in that paragraph.  

Required fix:  
- Add explicit, local language to §III A, Table I caption, and §VII(b) along the lines of: “Note: these significances are defined under different null procedures and are not directly comparable.”  
- Ensure that every place where σ values from different nulls appear in the same sentence, bullet list, or table (even if already covered by the earlier general instruction) gets its own reminder, per PRD expectations.  

---

P4-N6 (NEW MAJOR)  
Class: F (ABSTRACT FAITHFULNESS) – “disfavors Shamir 2–4% class by factor 6–12” and “falsification criterion” vs. quantitative backing  

Some of this overlaps with your earlier P4‑E3 and P4‑M3, but the fresh pass shows an additional abstract/body mismatch:

- Abstract: “The present null disfavors the Shamir ∼ 2–4% detection class at the amplitude level under our pipeline; a matched-footprint Ganalyzer reanalysis is required for a formal σ-level exclusion.”  
- §VI A and §VII(d) set the empirical threshold for **50% recovery at 3σ** at A ≈ 0.75% in an HC subsample, and state a Fisher floor of ∼0.29%, but never compute:  
  - The expected σ for a 2–4% dipole under the actual noisy, systematics-dominated catalog; or  
  - Any quantitative posterior or likelihood ratio comparing “A≈0” vs “A≈ 2–4%” on the DESI footprint.  

The only quantitative comparison is the ratio of amplitudes: 2–4% vs. 0.75%, giving 2.7–5.3, not “∼ 6–12”. Moreover, even if you argue that classification dilution requires scaling by g ≈ 0.398, the mapping from observed A to “true underlying A” is only qualitatively described. The factor “6–12” is thus not traceable to a specific calculation, nor clearly explained.  

Required fix (in addition to the softening requested in P4‑M3):  
- Explicitly show how the “factor of ∼ 6–12” is computed (from which pair of amplitudes, with which dilution factor and uncertainties). If this cannot be backed by a clear formula and error propagation, remove the numerical factor and describe the tension qualitatively only.  
- In the abstract, replace “disfavors the Shamir ∼ 2–4% detection class at the amplitude level” with a formulation that explicitly mentions that this is a *naive amplitude comparison* under specific assumptions, and direct the reader to §VI A for details.  

---

P4-N7 (NEW MAJOR)  
Class: H (UNQUANTIFIED HEDGES) – “consistent with” and “strongly disfavored” without clearly quoted ∆ and uncertainty  

Several places use phrases like “consistent with” or “strongly disfavored” without the corresponding ∆/σ numbers being clearly quoted in the same location, and without a cross‑reference:

1. **Appendix D(f): “interpretation (i) at A = 1.7% remains strongly disfavored under the spatial-coherence-respecting bootstrap covariance.”**  
   - The text mentions zboot ≈ −18.1 in passing but does not clearly spell out the model value and the best-fit value in the paragraph that makes the “strongly disfavored” claim.  
   - For a statistically heavy conclusion (“strongly disfavored”), readers should not be forced to reconstruct the numbers from scattered sentences; the delta and effective σ should be in the same sentence, or the statement should be softened and tagged with an explicit equation / table reference.  

2. **Appendix C(d): “Two-point chirality correlation … is consistent with the label-shuffle null at |σ| < 1.2 in 9 of 10 bins; the maximum deviation −2.41σ … is attributable to DESI Legacy DR8 brick-boundary classifier artifacts … confirmed by vanishing to −0.03σ in the brick-interior subsample.”**  
   - The claim of “attributable to brick-boundary artifacts” is plausible but relies on the −0.03σ number, which is quoted only once and without a stated uncertainty or sample size in that subsample. For rigor, the text should present the approximate sample size and error on the −0.03σ statement to justify the attribution.  

Required fix:  
- Where phrases like “strongly disfavored,” “consistent with,” “attributable to,” etc., are used, either:  
  - Add the explicit σ difference or p-value in the same sentence, or  
  - Provide a direct reference to the equation/table/figure that contains those numbers.  

---

P4-N8 (NEW MINOR)  
Class: J (STALE NUMBERS) – inconsistent N values and fsky between abstract, body text, tables, and appendices  

Beyond the obvious Smith42 and HuggingFace path issues you already flagged, there are several internal inconsistencies that look like remnants of earlier iterations:

1. **fsky values:**  
   - Abstract and Fig. 3: canonical mask fsky ≈ 0.49.  
   - Table I: canonical MASTER fsky = 0.49005; subsample-mask MASTER fsky = 0.659.  
   - Appendix A(c): apodized mask fsky = 0.482, subsample mask fsky = 0.659, canonical mask fsky = 0.49005.  
   - §VI A Fisher floor estimates use fsky = 0.46. This is never clearly linked to any particular mask or figure and is numerically inconsistent with 0.49/0.659. It likely stems from an earlier mask definition.  

2. **Nspiral vs Nmap,weighted**  
   - Table I: Nmap,weighted = 5,547,858; Appendix A says it is the sum of Wp = Nall(p) and then later sets A_p with Ntotal in the denominator. These values are plausible, but the mix of different Ns across sections without reminding the reader which one is being used in which calculation makes it easy for stale numbers to persist.  

Required fix:  
- Audit all instances of fsky and N (Nspiral, Nmap,weighted, NHC) and ensure that each distinct value is used consistently and explicitly tied to specific masks or subsamples.  
- Where older values (e.g., fsky = 0.46) were used only for rough Fisher-floor estimates but no longer match the final masks, either recompute the Fisher floor with the final fsky or explicitly label the number as an approximate illustrative calculation based on an earlier mask, to avoid misinterpretation as the exact floor for the final analysis.  

---

If you address the arithmetic/cross‑null consistency issues above alongside your original P4‑E/M/m items, the manuscript will be substantially closer to PRD’s expectations for numerical and methodological rigor.