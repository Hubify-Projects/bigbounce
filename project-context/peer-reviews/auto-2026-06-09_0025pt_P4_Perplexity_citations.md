# P4 auto-2026-06-09_0025pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 80.1s

---

P4-E1  
Section: Title / Header (page 1)  
Problem: The title claims a **“Galaxy chirality catalog v1.0.159”** context in the reviewer metadata, but the rendered paper’s title and body do not specify any version tag for the released catalog, while the Data Availability section refers instead to a HuggingFace release “v2026.04” and a GitHub repo “bigbounce” with no explicit semantic link to “v1.0.159.” This is an internal inconsistency between the stated catalog identity and the actually citable released artifact.  
Required fix: Explicitly state in the main text which catalog version (including exact tag/commit/hash) underlies all reported numbers, and ensure this identifier is consistent between title/abstract/body/Data Availability. If the “Galaxy chirality catalog v1.0.159” designation is obsolete or internal, remove it from all public-facing text and align the paper with the publicly released tag (or vice versa).  

P4-E2  
Section: Abstract (page 1), sentence “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.”  
Problem: Despite this caveat in the abstract, later sections juxtapose σ-values from different null procedures directly as if they were comparable (e.g., +3.64σ canonical-mask residual vs −0.122σ subsample ℓ=1 null; +4.31σ “monopole-preserving” pseudo‑Cℓ vs 0.43σ real‑space dipole) without reiterating non‑comparability at each juxtaposition. The instructions for this review explicitly require that any side‑by‑side presentation of σ from different nulls must locally re‑state non‑comparability.  
Required fix: Every time σ values from different null procedures are compared or listed together (e.g. in Sec. IV D, Sec. VI, Appendix D, Appendix E), explicitly remind the reader that these are defined under different nulls and are not directly comparable. Alternatively, convert all significance discussions into p‑values or z‑scores after mapping them to a single, clearly specified common null, and explain that mapping.  

P4-E3  
Section: Abstract (page 1) & Sec. IV C / Table III (page 6)  
Problem: The abstract quotes the “post‑MASTER dipole significance is −0.122σ (subsample mask, headline)” and a “real‑space post‑TTA Catalog C dipole is +0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000).” In Sec. IV C, the ℓ=1 MASTER measurement is C1meas = 1.494×10⁻⁶, ⟨C1null⟩=1.546×10⁻⁶, σnull=4.29×10⁻⁷, which indeed gives (1.494−1.546)/4.29×10⁻⁷ ≃ −0.12σ, so this is numerically consistent. However, the abstract also states: “A canonical-mask diagnostic… raw pseudo-C₁ … is reproduced at 99.3% of its observed amplitude by a controlled monopole-only generative null (N = 500… )” and Table IV claims the pre‑MASTER pseudo‑Cℓ is 1.696×10⁻² vs (1.685±0.007)×10⁻², which is only ~0.65σ away, not “99.3% of its observed amplitude” in any clearly defined sense:  
1. 1.685/1.696 ≈ 0.9945, so the null mean is ≈99.45% of “data,” inconsistent with “99.3%” at the precision implied.  
2. The ratio “reproduces 99.3%” does not match the z‑score in Table IV (+1.68σ).  
Required fix: Recompute and report the exact ratio used to define “99.3%,” state explicitly whether this refers to the mean null amplitude divided by the data amplitude, and ensure all quoted percentages and σ correspond numerically to the values in Table IV. If rounding changes the central figure (e.g. to 99.4%), update abstract and body consistently. Alternatively, drop the “99.3%” claim and express only the quantitative difference as a z‑score.  

P4-E4  
Section: Abstract (page 1) – Falsification criterion paragraph  
Problem: The abstract states A₉₅ ≈ 1.5–2% with “empirical 50%-recovery-at-3σ threshold of A₅₀ ≈ 0.75%” and claims that a future detection at A≈0.75% and 5σ would be “entirely consistent with the present non-detection.” In Sec. VI A, the Fisher 3σ floor is 0.29% and the empirical injection‑recovery gives P(σ>3)=0.55 at A=0.75% and 0.15 at A=0.5%; the mapping from these points to A₉₅ ≈ 1.5–2% is asserted but not actually demonstrated, and 0.75% is repeatedly used both as an “empirical sensitivity floor” and as a threshold for future consistency without a formal statistical definition.  
Required fix: Provide a clear, quantitative definition of A₅₀ and A₉₅ and show how A₉₅ ≈ 1.5–2% is obtained from the injection‑recovery curves (e.g. by fitting a detection‑probability vs amplitude curve and quoting the amplitude where P≥0.95). Clarify in the abstract that the 0.75% figure corresponds to 50% detection probability at 3σ, not a sharp limit, and adjust the falsification criterion language accordingly (e.g. “would be in tension with, but not formally excluded by, the present analysis”).  

P4-E5  
Section: Abstract, first paragraph (page 1) and Table I (page 4)  
Problem: The abstract states: “8.47 M sources, 471 049 high-confidence per-spiral after peq_CW > 0.9,” while Table I’s entry (vi) injection floor states “A = 0.75%” threshold on “471,049 HC.” However, Sec. VI A defines the injection‑recovery using “HC-spiral subsample (N = 471,049, N_MC,null = 1000, N_MC,inj = 100 per amplitude)” but never explicitly links this to “peq_CW > 0.9” or to a particular Catalog tier. The abstract’s “peq_CW > 0.9” is a load‑bearing scalar but is nowhere precisely defined in the methods (e.g., whether this is max softmax, calibrated, equivariant probability, or only CW class).  
Required fix: In Sec. III–IV, define unambiguously what “peq_CW” is (tier, calibration, exact threshold, whether NS class is allowed) and explicitly state that the HC-spiral subsample used in injection‑recovery corresponds to the 471,049 galaxies satisfying peq_CW > 0.9. Ensure consistent notation and thresholds between abstract, Table I, Sec. IV, and Sec. VI A.  

P4-E6  
Section: Sec. II B “Training Labels” (page 2) and Sec. III C (page 3) vs. Figure 1 (page 5)  
Problem: The main text clearly states that production uses **2‑fold** TTA (original + horizontal flip), with rotations used only for diagnostics: “We restrict to 2-fold TTA… A direct D₄‑TTA hold-out… confirms… Full details in Appendix B.” However, Figure 1 depicts “Test-time D4 equivariant averaging (TTA)… eight D4 transforms” and describes the output as a “strictly flip-equivariant classifier” under averaging over all eight transforms. This is inconsistent with the stated production protocol and may mislead readers about the estimator used to produce Catalog C.  
Required fix: Clarify explicitly in the Figure 1 caption and surrounding text that the production Catalog C uses 2-fold TTA, while full D₄‑TTA is a diagnostic experiment only. Either (a) replace Figure 1 with a schematic matching the actual 2-fold TTA pipeline, or (b) clearly label Figure 1 as “diagnostic D₄‑TTA (not used in production catalog)” and add a separate schematic for the production 2‑fold TTA.  

P4-E7  
Section: Data / Galaxy Images (page 2)  
Problem: The paper cites “Smith42/galaxies dataset on HuggingFace (… 8,474,688 galaxy images)” but provides no formal citation (author, year, persistent identifier) in the References list, despite this dataset being the foundational data source. This is a serious citation omission by PRD standards, where all external data products must be referenced with as much bibliographic information as possible.  
Required fix: Add a formal reference for the “Smith42/galaxies” dataset to the bibliography, including creator(s), year, dataset title, platform (HuggingFace), and version/tag used. Make sure the in‑text citation matches the reference and that the Data Availability section uses the same canonical name.  

P4-E8  
Section: Sec. I Introduction (page 2), paragraph summarizing Jia et al. [7]  
Problem: The text claims: “Jia et al. [7] introduced CE-ResNet… yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.” In the cited paper [7] (Jia, Zhu & Pen 2023, ApJ 943, 32, arXiv:2210.04168), the main reported outcome is that the CW and CCW counts are consistent with parity (cw/ccw ratio close to 1) but the specific **0.998** ratio and the **1.95 million** galaxy count need to be traceable to that paper’s abstract or tables. A check of the abstract and main tables shows that while they do quote a nearly equal CW/CCW distribution, the exact cw/ccw = 0.998 and “∼1.95 million” figures are not explicitly presented in that precise form (they are inferred from downstream selection; e.g., the full catalog contains 1.95M labelled galaxies, but the cw/ccw ratio is given in terms of fractions with uncertainties).  
Required fix: Either (a) quote directly the statistics as they appear in Jia et al. (e.g. “the CW fraction is X±Y, consistent with unity ratio within Zσ”) with precise numbers matching their text/tables, or (b) explicitly state that 0.998 and 1.95M are derived from their published counts by straightforward division and cite the specific table or section used. Avoid using a cw/ccw ratio with three significant figures unless that exact ratio is explicitly given in the cited work.  

P4-E9  
Section: Sec. I Introduction (page 2) – Shamir citations [1–4]  
Problem: The text states “Shamir (2012) [4] reported a 2–4σ dipole with per-bin asymmetry amplitudes of ∼5–20% using ∼1.27×10⁵ SDSS galaxies. Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼2–4% asymmetries on DESI Legacy samples (‘nearly 1.3×10⁶ spiral galaxies’ per the published abstract).” In [4] (Phys. Lett. B 715, 25, arXiv:1207.5464), the sample size and asymmetry amplitudes are indeed large, but the quoted “∼1.27×10⁵” and “5–20%” must match the paper’s abstract and main tables; similarly, [3] (MNRAS 516, 2281, arXiv:2208.13866) must actually use the phrasing “nearly 1.3×10⁶ spiral galaxies” in the abstract. A check confirms that [3] does state “nearly 1.3×10⁶” in the abstract, but [4] does not give “5–20%” in that exact form; those values are aggregated from multiple figures/tables.  
Required fix: Tighten the wording so that any numerically specific claim (e.g. “5–20% per bin,” “1.27×10⁵ galaxies”) is either directly quoted from the abstract or explicitly sourced to a table/figure. If the numbers are synthesized across multiple bins or subsamples, state this clearly (“combining the binned asymmetries reported in Figures X–Y gives typical per-bin asymmetries in the range 5–20%”).  

P4-E10  
Section: Sec. I Introduction (page 2), “Jia et al. [7] … cw/ccw = 0.998 on ∼ 1.95 million galaxies” vs Sec. V B (page 7)  
Problem: Sec. V B states: “CE-ResNet [7] achieves cw/ccw = 0.998 with architectural equivariance on 1.95 million galaxies. Our Catalog C achieves 1.6× the spiral coverage…” implying CE-ResNet’s spiral sample is 1.95M and this is *directly comparable* to the 3.2M spirals here. In [7], the 1.95M number refers to galaxies with reliable chirality classification, but there are subtleties (e.g. quality cuts, morphological selection) and the cw/ccw ratio is only “consistent with 1” within errors. The “1.6×” factor is therefore based on approximate numbers and may give an exaggerated sense of precision.  
Required fix: Downgrade this to an approximate comparison and explicitly note the selection differences (“roughly 1.6× larger, though selection functions differ”; “CE-ResNet reports ~2M spirals with cw and ccw counts consistent with parity”). Provide an explicit citation to the section or table in [7] that specifies the sample size and cw/ccw balance.  

P4-E11  
Section: Sec. II A “Galaxy Images” (page 2)  
Problem: The paper states: “Each image is a 224×224 pixel cutout in grz bands at 0.262″/pixel.” DESI Legacy DR8 has a nominal pixel scale of 0.262 arcsec/pixel, but “Smith42/galaxies” as a derived dataset may have resampled or cropped images. This exact pixel scale and size is not supported by a citation to DR8  or to the dataset description.  
Required fix: Either (a) cite the DR8 technical reference  where the 0.262″/pixel scale is specified and state that the Smith42 dataset preserves this native scale, or (b) explicitly note if the dataset creator resampled to 224×224 at 0.262″ and provide a citation or documentation link for that dataset.  

P4-E12  
Section: Sec. III A Declared Analysis Hierarchy (page 3) & Table I (page 4)  
Problem: Table I defines N_map^weighted = Σ_p W_p where W_p = N_all^(p), and claims “N_map^weighted exceeds N_catalog,spiral because W_p includes non-spiral galaxies (~62% of the catalog); each galaxy is counted once.” However, with NSIDE=64 pixels of area ~0.84 deg², many galaxies will fall in the same pixel, so Σ_p N_all^(p) should equal the total number of galaxies (i.e. 8.47M), whereas Table I lists N_map^weighted = 5,547,858; this is *less* than the total number of galaxies and also < N_catalog,total, contradicting the “each galaxy is counted once” description. It is unclear whether W_p is count or weight, and how 5.55M is obtained.  
Required fix: Clarify the precise definition of W_p:  
– Is it the number of galaxies in pixel p, or a normalized weight (e.g. N_all^(p)/N_ref)?  
– Why does Σ_p W_p = 5.55M when there are 8.47M galaxies?  
Correct the text to accurately describe the weighting scheme (possibly “each pixel contributes a weight proportional to its galaxy count; Σ_p W_p is 5.55M but this is not a galaxy count”). Ensure consistent units and remove the claim “each galaxy is counted once” if not strictly true.  

P4-E13  
Section: Sec. IV B “Global CW fraction” (page 4) vs. Table II (page 4)  
Problem: Table II lists Catalog C cw/(cw+ccw) = 0.4974 ± 0.000279 with “Dev.(σ) = 9.5,” but (0.4974−0.5)/0.000279 ≈ −9.3σ, not −9.5σ (depending on rounding). Additionally, the text describes the “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%,” implying that Catalog A is +0.79% (0.5079) and Catalog C is −0.26% (0.4974). The wording “+2.05% to −0.53%” is unclear: 0.5079–0.5 = +0.79%, not +2.05%; 0.4974–0.5 = −0.26%, not −0.53%. There is an unexplained factor-of-two.  
Required fix: Recompute and clearly present:  
– The global CW–CCW excess in percentage points for each tier (A, B, C).  
– The corresponding Gaussian σ using binomial variance.  
Correct any mis‑stated percentage values (e.g. change “+2.05%” to “+0.79%” if that is what is actually observed, or explain the 2× factor if it refers to half‑amplitude vs full amplitude). Update the “3.86× suppression factor” wording and number to reflect these corrected values.  

P4-E14  
Section: Sec. IV C “Dipole Analysis” (page 4–5) – simple dipole 0.43σ, p=0.30  
Problem: The simple dipole significance is reported as 0.43σ with p = 0.30 from 10,000 bootstrap realizations. A one-sided Gaussian mapping from 0.43σ gives p ≈ 0.33, and two-sided p ≈ 0.67. It is unclear which convention is used and how p=0.30 is derived; this misalignment may confuse readers and slightly misrepresents the significance.  
Required fix: State explicitly whether p-values are one‑sided or two‑sided, and recompute p for 0.43σ under that convention, or else report σ and p from the empirical bootstrap directly (e.g. “29.6% of nulls exceed the observed amplitude”). Ensure that all σ ↔ p mappings in the paper are internally consistent.  

P4-E15  
Section: Sec. IV D “Monopole+mask leakage generative null” (page 4–5), footnote 1  
Problem: Footnote 1 acknowledges that an earlier version used ambiguous wording “Binomial(n_total, p_global_CW)” and that a rerun with N_all(p) is “in queue” and may change the quantitative “99.3%” reproduction figure. However, the main text still bases key conclusions (e.g. that prior literature’s pre‑MASTER dipole‑detection claims are explained “at the percent level variance”) on the current N_spiral(p)‑based simulation. This leaves a methodologically important result contingent on an unfinished rerun.  
Required fix: Complete the N_all(p) rerun and update all relevant numbers before publication. If this is not feasible, remove or down‑weight any claims that depend sensitively on the exact reproduction percentage (e.g. “99.3%”) and instead present a qualitative statement that the monopole‑only null reproduces the bulk of the pre‑MASTER pseudo‑Cℓ power. Explicitly state that the main no‑dipole conclusion does not depend on whether N_spiral or N_all is used.  

P4-E16  
Section: Sec. V A “Shamir (2012, 2020, 2022)” (page 6–7)  
Problem: The text asserts: “These conclusions corroborate and extend the methodological critique of Iye et al. (2021) [5] with 3.2×10⁶ spirals (30× extension).” The claim of a “30× extension” in sample size relative to Iye et al. [5] must be numerically correct and sourced. Iye et al. (ApJ 907, 123, arXiv:2011.00662) use 80,000 galaxies (or another reported number); the factor of 30 is approximate and not explicitly given in [5].  
Required fix: Quote the exact spiral sample size in Iye et al. [5] from their paper and compute the ratio precisely. If the factor is approximate (e.g. 26× or 32×), state it as “~30×” and briefly show the numbers underlying the comparison.  

P4-E17  
Section: Sec. VI A “Sensitivity floor” (page 8)  
Problem: The Fisher Poisson 3σ floor is quoted as ~0.29% (from σ(A/2) ≈ 0.048% at N_spiral = 3,201,160, f_sky = 0.46). Recomputing: for a binomial proportion p≈0.5 and N≈3.2×10⁶, σ(p) ≈ sqrt(0.25/N) ≈ 0.00028 (0.028%); a 3σ excess in p is ~0.084% in the half‑amplitude A/2, so A ≈ 0.17%, not 0.29%, unless additional factors (e.g. f_sky, pixelization) are included. The derivation of 0.29% is not shown.  
Required fix: Provide an explicit derivation for the 0.29% Fisher floor, including all factors (f_sky, effective number of modes, pixel threshold). Recompute the value and update if necessary. If additional noise sources beyond simple counting statistics are included, state them clearly.  

P4-M1  
Section: Sec. III B “Model Architecture” (page 3) and Appendix B (page 9–10)  
Problem: The architecture and training details are described, but there is no quantitative uncertainty propagation from classifier misclassification (69.91% agreement with GZ1; Cohen’s κ=0.40) into the cosmological dipole constraints beyond a brief mention of a “GZ1-dilution factor g ≈ 0.398.” The paper claims to propagate this to “all downstream isotropy bounds via the subpercent systematic floor,” but the exact procedure is not given, making it impossible to reconstruct the claimed sensitivity floor and falsification thresholds from first principles.  
Required fix: Provide an explicit formula and workflow for how classifier accuracy (and g) is folded into the error budget for the dipole amplitude and A₅₀/A₉₅ thresholds. Ideally, include a toy calculation or reference a table that shows the resulting effective N_eff and amplitude sensitivity after misclassification dilution.  

P4-M2  
Section: Equations (2) and (3) (page 3–4)  
Problem: Equation (2) defines equivariant probabilities as arithmetic averages of original and flipped outputs, but does not explicitly state that the same input image is used for both passes, nor how stochastic augmentations (e.g. random crops, noise) during inference are controlled. This affects reproducibility of the catalog and the derived statistics, especially if dropout or randomness is involved. Equation (3) defines A_p but uses N_CW^(p) + N_CCW^(p) in denominator, which is later reinterpreted with N_total^(p) (including NS) in the field definition in Appendix A, causing confusion.  
Required fix: Explicitly state whether inference is deterministic (no stochastic augmentations, dropout disabled) and that the two passes in Eq. (2) see identically preprocessed images except for the deterministic horizontal flip. Align the definitions of A_p across the main text and Appendix A: make it clear when non‑spirals are included or excluded from the denominator and update notation accordingly to avoid ambiguity.  

P4-M3  
Section: Figures 3 and 4 (pages 7–8) and Table III (page 6)  
Problem: Figure 4 shows pseudo‑Cℓ curves and an orange band from the monopole-only null, while Table III presents bandpowers and a joint χ²/dof = 161.2/38≈4.24, interpreted as “dominated by mask-coupled monopole.” This interpretation is plausible but no quantitative comparison of χ² with and without a monopole-leakage template is shown, nor is a goodness‑of‑fit p‑value quoted; the conclusion that the excess is “dominated” by monopole leakage is more qualitative assertion than statistically demonstrated.  
Required fix: Provide a quantitative test: for example, fit a simple mask‑coupled monopole template to the bandpowers and show that including that template reduces χ²/dof substantially. Quote the resulting p‑values with and without the template. This will substantiate the statement that the canonical pseudo‑Cℓ excess is “dominated by mask‑coupled monopole leakage.”  

P4-M4  
Section: Data Availability (page 11–12)  
Problem: Data and code availability URLs are given in prose but not as formal references, and there is no explicit statement that the archived artifacts correspond exactly to the version used in the paper (e.g., no Git commit hash, no DOIs, and no specification that the models and scripts can reproduce all tables within numerical tolerances). PRD standards for methods papers increasingly require stable archival (e.g., Zenodo DOIs) and explicit reproducibility statements.  
Required fix: Assign or reference archival DOIs (e.g., via Zenodo or similar) for the dataset, model weights, and code snapshots used for this paper; include them in the reference list. Add a short statement clarifying that running the provided scripts on the referenced catalog reproduces all main tables and figures within specified tolerances, or else note any known differences (e.g., due to random seeds).  

P4-M5  
Section: References [1]–[7], – (pages 12–13)  
Problem: Several references are incomplete or inconsistent in style for PRD:  
– [1], [3], [7] mix arXiv and DOI but do not include volume/page for all.  
– Some multi-author lists have “et al.” but the in‑text citations sometimes rely on exact author combinations (e.g. “Jia et al. (2023)” vs “H. Jia, H.-M. Zhu, and U.-L. Pen”).  
– The dataset “Smith42/galaxies” is not cited at all (see P4-E7).  
Required fix: Bring all references into a consistent PRD format: include full journal name, volume, page, year, and DOI (when available) for all published works; ensure arXiv identifiers match title/authors/venue. Add missing dataset references.  

P4-m6  
Section: Throughout (all pages) – novelty claims  
Problem: The paper repeatedly claims “largest galaxy chirality catalog to date: 8,474,531 galaxies” and “survey-scale coverage of 8.47 million galaxies (3.2M spirals, 1.6× CE-ResNet’s scale)” as key novelties. While 3.2M spirals is indeed larger than the ∼1.95M in Jia et al. [7], no systematic survey of prior catalogs is provided (e.g. potential larger but noisier spiral samples, or catalogs with different selection criteria).  
Required fix: Either (a) add a short subsection explicitly reviewing the sizes of previous chirality‑classified spiral catalogs and demonstrate that none exceed 3.2M spirals, or (b) soften the claim to “to our knowledge, this is among the largest chirality catalogs to date” and include Jia et al. and Shamir’s catalogs for comparison.  

P4-m7  
Section: Length and structure (entire manuscript)  
Problem: The paper runs 13 pages with a heavy emphasis on internal diagnostics, appendices, and qualitative interpretation of systematics. For the claimed primary scientific result (“a null ℓ=1 subsample-mask dipole”), the length appears excessive: multiple pages repeat the same qualitative statement that the canonical-mask residual is not cosmological. Many details (e.g. full bias‑hardening suite, morphology systematics) are appropriate as supplemental material but could be condensed for PRD.  
Required fix: Condense and reorganize:  
– Move most of Appendices C–E and detailed diagnostic text into an online Supplemental Material file.  
– Target a main‑text length of ≤9–10 pages focused on data, methods, primary estimators, and key systematics.  
– Keep only the most essential diagnostics in the main text and limit repetition of the “null” conclusion.  

P4-N1  
Section: Minor wording / typos (multiple pages)  
Problem: Various small issues:  
– “NaMaster low-ℓ deconvolution artifact. Interpretation (iii) sharp-edge variant” (missing hyphen and commas).  
– “cw/ccw = 0.998” vs “CW/CCW” inconsistent capitalization.  
– “probes classifier non-equivariance” should be “non‑equivariance”.  
– Some sentences run long and would benefit from restructuring for clarity.  
Required fix: Perform a careful language edit to correct typos, hyphenation, and capitalization, and to simplify overly long sentences, without changing technical content.  

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper presents an interesting and potentially important null result with extensive systematic checks, but several load‑bearing numerical claims (e.g., “99.3%” monopole reproduction, sensitivity floors, suppression factors) are not fully consistent or transparently derived, the TTA protocol is described inconsistently between text and figures, and key dataset and method references are incomplete. These issues must be resolved, and the statistical treatment made more explicit, before the paper can meet PRD’s standards for a rigorous cosmology methods publication.