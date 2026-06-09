# P4 auto-2026-06-09_1042pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (16378 chars)
**Wall time**: 75.3s

---

P4-E1 (ESSENTIAL) – Global σ-definition vs. per-result qualification  
Section: Abstract & throughout; Page 1 and multiple  
Problem: The abstract states “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators,” but in the body several σ-values from different nulls are juxtaposed without always re-stating this non-comparability at the point of comparison (e.g. abstract: “−0.122σ … The real-space post‑TTA Catalog C dipole is +0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000).”).  
Required fix: At every place where σ values from different null procedures appear side-by-side (abstract and main text, including Table I and the conclusions), explicitly state “not directly comparable” or equivalent in the immediate sentence or caption, not only via a global note.  

P4-E2 (ESSENTIAL) – Missing references [24–27, 31–39]  
Section: References; Page 13–14  
Problem: The in-text citations , , , , – appear in the manuscript, but the provided reference list only includes [1]–. For instance, Hayes et al. is referred to as , Bamford et al. as , Hart et al. as , Walmsley et al. (DECaLS) as , Astropy as , HEALPix/healpy as [34–35], NumPy as , pandas as , PyTorch as , timm as , but their bibliographic entries are missing in the excerpt.  
Required fix: Ensure that all cited works [24–27,31–39] appear in the reference list with correct authors, title, journal, year, and (where relevant) arXiv ID and DOI, consistent with NASA ADS/arXiv records. Cross-check all citation numbers in the body to match the final reference ordering.  

P4-E3 (ESSENTIAL) – Incorrect or inconsistent citation metadata for Shamir 2020 and 2022  
Section: References; Page 13–14  
Problem: The Shamir references are internally inconsistent and partially wrong:

- [1] is “Patterns of galaxy spin directions in SDSS and Pan‑STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116. According to ADS/arXiv, arXiv:2007.16116 is indeed “Patterns of galaxy spin directions in SDSS and Pan‑STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020). This is correct.  
- [2] is given as a PASJ 74, 1114 (2022) paper titled “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” DOI:10.1093/pasj/psac058. According to ADS, PASJ 74, 1114 (2022), DOI psac058, by Shamir has that approximate title; the metadata look plausible but must be checked carefully against ADS to ensure exact title wording and page numbers.  
- [3] is “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372. ADS confirms that arXiv:2208.13866 is “A large-scale cosmic anomaly from galaxy spin patterns in the DESI Legacy Survey” (title slightly different) published in MNRAS 516, 2281–2292 (2022).[1] The manuscript’s title does not match the published title.  

Required fix:  
- For [3], update the title and page range to match the published MNRAS article for arXiv:2208.13866 exactly (check ADS for final published title and pagination).[1]  
- For [2], verify the exact title/pagination/DOI against PASJ/ADS and correct any deviations.  
- Re-check all three Shamir entries ([1]–[3]) against NASA ADS to ensure author lists, titles, journal, volume, pages, year, arXiv ID, and DOI are all accurate and consistent.  

P4-E4 (ESSENTIAL) – Mischaracterization of CE‑ResNet result  
Section: Introduction; Page 2  
Quoted text: “Jia et al. [7] introduced CE‑ResNet, a chirality‑equivariant CNN … yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.”  
Problem: In Jia et al. (ApJ 943, 32 (2023), arXiv:2210.04168), the key metric reported in the abstract is that the *ratio* of clockwise to counter‑clockwise counts is 0.998 ± 0.005 (i.e. *near unity*, not 0.998 in the sense of a fraction of one class).[2] The manuscript’s phrasing “yielding cw/ccw = 0.998” is ambiguous and, as written, looks like the CW fraction, which would be inconsistent with the cited work.  
Required fix: Rephrase this sentence to match the actual statistic reported by Jia et al., e.g. “yielding a CW/CCW *number ratio* of 0.998 on ∼ 1.95 million galaxies,” and cite where in Jia et al. this comes from (abstract / specific table). Verify that the sample size (“∼1.95 million galaxies”) matches the number in the Jia paper.  

P4-E5 (ESSENTIAL) – Mis-stated Shamir DESI Legacy sample size  
Section: Introduction; Page 2  
Quoted text: “Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries on DESI Legacy samples (‘nearly 1.3 × 106 spiral galaxies’ per the published abstract).”  
Problem: The “nearly 1.3×10^6 spiral galaxies” wording refers to the DESI Legacy analysis in Shamir’s 2022 MNRAS paper (arXiv:2208.13866), not to the 2020 SDSS+Pan‑STARRS paper.[1] The sentence collapses the 2020 and 2022 results and attributes the DESI sample size to both. Moreover, the exact phrase in the MNRAS abstract is different (ADS gives a specific number of galaxies; the “nearly 1.3×10^6” paraphrase may be slightly off).  
Required fix:  
- Separate the SDSS/Pan‑STARRS and DESI Legacy samples and attribute the “nearly 1.3×10^6 spiral galaxies” explicitly to the 2022 DESI Legacy analysis only, with a precise galaxy count as stated in that abstract.[1]  
- Make clear which paper reports “2–4% asymmetries” and on which survey. Re-derive those quoted asymmetry amplitudes from the cited paper’s abstract or tables and state them accurately (with ranges if needed) instead of the vague “∼2–4%”.  

P4-E6 (ESSENTIAL) – Misstated “null” in Tadaki et al.  
Section: Introduction; Page 2  
Quoted text: “Tadaki et al. [6] likewise found null results.”  
Problem: Tadaki et al. (MNRAS 496, 4276 (2020), arXiv:2006.02331) present a catalogue of ∼80,000 face-on spirals and discuss spin-parity tests.[3] Whether they present a “null” in exactly the sense implied here (no evidence of parity violation at the quoted levels) must be backed explicitly by an abstract or table statement. Without quoting their actual constraints (e.g., their measured asymmetry and uncertainty), calling this simply “null results” is too imprecise and potentially misleading.  
Required fix: Re-check Tadaki et al.’s conclusions. Either (a) quote their measured asymmetry and uncertainty and then state “consistent with zero within Xσ,” or (b) cite their explicit conclusion phrase that no significant asymmetry was found. Avoid generic “null results” without a quantitative support.  

P4-E7 (ESSENTIAL) – Falsification criterion vs. injection-recovery numbers  
Section: Abstract & Sec. VI A; Pages 1 & 8–9  
Problem: The abstract defines a falsification criterion using A50 ≈ 0.75% and A95 ≈ 1.5–2% “above the demonstrated empirical 50%-recovery-at-3σ threshold of A50 ≈ 0.75%,” and Sec. VI A quotes “P(σ > 3) = 0.55 at A = 0.75% and P(σ > 3) = 0.15 at A = 0.5%.” These numbers are consistent internally, but the mapping from these injection-recovery fractions (on N = 471,049 HC spirals) to a falsification criterion for the *full survey* (3.2M spirals) is not fully justified. The abstract’s “A95 ≈ 1.5–2%” is not backed by any explicit simulation results in the text or tables.  
Required fix:  
- Provide explicit injection-recovery results at amplitude(s) yielding ≈95% recovery at ≥3σ and quote those instead of the ad-hoc “1.5–2%” range, or clearly label A95 as an extrapolation with a brief justification.  
- Clarify how the HC-subset simulations are extrapolated to the full Catalog C, or repeat injection-recovery on a sample representative of the full catalog if the falsification criterion is to be applied at that level.  

P4-E8 (ESSENTIAL) – Use of “disfavors” / “strongly disfavored” without quantitative mapping  
Section: Abstract; Sec. IV D, V A, D, VI B; multiple pages  
Problem: Statements such as “Interpretation (i)… is disfavored by three independent lines of evidence,” “strongly disfavored under the spatial-coherence-respecting bootstrap covariance,” and “disfavors the Shamir ∼ 3% amplitude class by a factor of ∼ 6–12” are used without a clear statistical mapping from the quoted z-scores/χ² to model odds or Bayes factors. The null vs. “dipole only” comparison is qualitative rather than a formulated hypothesis test.  
Required fix: When claiming that a hypothesis is “disfavored” or “strongly disfavored,” give the explicit test statistic (e.g., Δχ², z, or a p-value) and state what threshold you consider as “strong.” For example: “interpretation (i) at A = 1.7% yields z ≈ −18 in the bootstrap covariance (p ≪ 10−5), so we regard it as strongly ruled out.” Likewise, when saying “disfavors Shamir’s ∼3%”, specify the amplitude ratio and the recovered σ-level for that amplitude from injection tests or a simple Fisher estimate.  

P4-E9 (ESSENTIAL) – Ambiguous use of σ for positive vs. negative “significance”  
Section: Whole paper; e.g., Abstract, Sec. IV C/D, Table III  
Problem: The paper uses both positive and negative σ values, e.g. “−0.122σ,” “+3.64σ,” “σ = −2.89,” often describing them as “significance,” but the sign convention is not always clear (is it based on (C_meas−⟨C_null⟩)/σ_null with sign inherited from the numerator, or something else?). For instance, Table III lists some bandpowers with Cℓ < 0 but positive “significance,” which is confusing.  
Required fix: Explicitly define what “σ” means in each context (e.g., “significance is defined as (Cℓ,meas − ⟨Cℓ,null⟩)/σnull; this may be negative when the measured value is below the null mean,” and similarly for correlation coefficients r). Ensure Table III and the text consistently report sign and magnitude; if Cℓ is negative while significance is given as +2.232σ, clarify that this is |z|.  

P4-M1 (MAJOR) – Length vs. scope  
Section: Whole paper; 14 pages plus appendices  
Problem: The claimed main scientific result is a null ℓ=1 dipole at the sub-percent level on a single catalog, with a substantial portion of the paper devoted to internal systematics diagnostics and methodology. For PRD, which expects strong conceptual or methodological advances, the current manuscript is arguably over-long for the net contribution (especially given that the central cosmological statement is a null and much of the methodology is survey/ML-specific rather than general cosmological theory).  
Required fix: Condense the manuscript by removing or relegating to supplementary material some of the more descriptive parts of the bias-hardening suite, morphology systematics, and implementation details that do not change the cosmological conclusions. A reasonable target is ≤10 journal pages (main text), keeping only the most essential diagnostics.  

P4-M2 (MAJOR) – Ambiguity in “largest” / “survey-scale” claims  
Section: Introduction & Conclusions; Pages 2 & 10  
Problem: The paper states “the largest galaxy chirality catalog to date: 8,474,531 galaxies … 3,201,160 equivariant-classified spirals, 1.6× CE-ResNet’s scale.” Jia et al. report ~1.95 million galaxies used for their chirality analysis.[2] The “1.6×” factor is numerically consistent with 3.2M vs 1.95M, but “largest to date” should be established explicitly against all relevant prior spin-catalogue efforts, including Shamir’s claimed ~1.3M DESI spirals and other SDSS-based catalogues.  
Required fix:  
- Explicitly list the sizes of the main previous chirality/spin catalogs (Shamir DESI, Shamir SDSS/Pan‑STARRS, CE‑ResNet) with numbers taken from their abstracts or tables and show that 3.2M spirals is indeed larger than each.  
- Replace or qualify blanket statements like “largest to date” with “to our knowledge, larger than [X] and [Y], which contain N1 and N2 spirals respectively,” unless a comprehensive literature check justifies the absolute claim.  

P4-M3 (MAJOR) – Use of “null” for 9.5σ monopole  
Section: Sec. IV B and elsewhere; Pages 4–5  
Problem: The global CW fraction in Catalog C is 0.4974 ± 0.000279, which is a 9.5σ deviation from 0.5, yet the text repeatedly refers to this as a “monopole offset” and essentially lumps it under “null dipole” in rhetoric. Strictly, for any model in which the prior expectation is 0.5, this is a highly significant systematic effect. While the authors are careful to call it a classifier artifact, the severity is not fully confronted.  
Required fix:  
- Explicitly refer to this as a “high-significance (9.5σ) classifier monopole bias” and quantify its potential impact on dipole observables in more detail.  
- Quantitatively show (e.g., via simulations or analytic considerations) that after TTA and MASTER deconvolution, a 9.5σ monopole cannot leak into an ℓ = 1 dipole larger than the quoted sensitivity. Link this explicitly to the monopole+mask generative null.  

P4-M4 (MAJOR) – Footnote and text suggesting “earlier paper versions”  
Section: Sec. IV D, footnote; Page 6  
Problem: The footnote in Sec. IV D references “earlier paper versions” and “a parallel rerun … is in queue,” which is version-history language inappropriate for a final PRD submission.  
Required fix: Remove mention of earlier versions and queued reruns. Replace with a neutral description: what was done for the final analysis, and what limitations remain. If the N_all vs N_spiral choice is uncertain, either (a) re-run the analysis now and present final numbers, or (b) explicitly bracket the impact with a completed sensitivity study included in the paper.  

P4-M5 (MAJOR) – Ambiguity in definition of the field A_p across sections  
Section: Sec. IV C, Appendix A; Pages 5 & 10–11  
Problem: There are at least two definitions of Ap:  
- Sec. IV C: \(A_p = (N^{(p)}_{CW} - N^{(p)}_{CCW}) / (N^{(p)}_{CW} + N^{(p)}_{CCW})\).  
- Appendix A: “The asymmetry field is \(A_p = (N_{CW}^{(p)} - N_{CCW}^{(p)}) / N^{(p)}_\text{spiral}\).” This is equivalent in spirals-only pixels but later another definition \(A_p=(N_{CW}-N_{CCW})/N_{total}\) (with N_total including non‑spirals) is used. The generative null footnote also discusses N_spiral vs N_all confusion.  
Required fix: Provide a single, unambiguous definition of Ap used for the headline dipole measurement (including whether non‑spirals contribute to the denominator), and ensure all formulae and footnotes align with that definition. If different fields are used for different diagnostics, label them distinctly (e.g., A_spiral, A_all) and specify clearly which is used for which figure/table.  

P4-M6 (MAJOR) – Lack of explicit recomputation of quoted Shamir asymmetries  
Section: Sec. V A; Page 7  
Problem: The paper states “our maximum regional asymmetry is 0.32% and the 0.43σ simple dipole is well below the 2–4σ dipoles reported by Shamir [1,3,4]” and “discrepancy most likely reflects two factors…”. However, the 2–4σ values and associated asymmetry amplitudes are cited as broad ranges and are not traced explicitly to specific tables/figures in Shamir’s papers.  
Required fix: For each Shamir paper where a 2–4σ signal is claimed, explicitly identify the relevant statistic (e.g., the dipole amplitude and uncertainty from a specified table/section) and show numerically how 2–4σ is obtained. Then, compare directly to your sensitivity estimates.  

P4-M7 (MAJOR) – Cosmology framing vs. metric used  
Section: Abstract, Introduction, Discussion; multiple  
Problem: The paper is framed for a cosmology journal (PRD) but the core observable is a single ℓ = 1 angular dipole in galaxy chirality, interpreted in terms of isotropy-breaking axial-vector sectors. However, there is no explicit mapping to underlying cosmological parameters (e.g., constraints on a parity-violating tensor amplitude, or a specific model’s parameter), nor a clear forecast of how this constraint compares with other cosmological parity tests.  
Required fix: Add a quantitative discussion connecting the measured upper bound on chirality dipole amplitude to constraints on a class of cosmological models (even if approximate), or explicitly reframe the work as an observational-methods paper with limited direct cosmological parameter inference. For PRD, some quantitative tie to theory is expected.  

P4-N1 (MINOR) – Dimension / notation checks in equations  
Section: Sec. III C & Appendix A/B; Pages 3, 10–11  
Problem: The definitions in Eq. (2) for equivariant probabilities are dimensionless and consistent, but some notation is overloaded (e.g., “orig, flip, eq” superscripts vs. the use of angled brackets for averages). Also, in Table III, Cℓ values are given in “Cℓ × 10^6 (sr)” without explicitly stating that the plotted quantity is \(C_\ell\) in units of steradians (dimensionless power spectrum multiplied by sr).  
Required fix: Clarify notation: define all superscripts and symbols when first introduced; in Table III and the text, explicitly state that \(C_\ell\) is dimensionless and that the “(sr)” refers to the usual pseudo-Cℓ convention.  

P4-N2 (MINOR) – Duplicate/malformed phrases  
Section: Multiple; e.g. Fig. 1 caption; Page 4  
Problem: There are a few awkward phrases that look like editing artefacts, e.g. “V iT − Small-Small classifier” in Fig. 1 caption (likely intended “ViT-Small classifier”), “canonical-N” vs. “canonical mask” terminology inconsistently used, and “bigbounce” in the Data Availability section that looks like an internal codename rather than a descriptive label.  
Required fix:  
- Correct “V iT − Small-Small” to “ViT-Small”.  
- Standardize terminology for the canonical mask / canonical sample (do not mix “canonical-N” with “canonical mask” unless precisely defined).  
- Replace “bigbounce” with a descriptive repository or package name if this is internal jargon.  

P4-N3 (MINOR) – Internal-tool acknowledgment  
Section: Acknowledgments; Page 13  
Problem: “AI tool usage: Large-language-model tools were used for code review and manuscript editing” is acceptable, but PRD may have specific policies or preferred phrasing for AI assistance.  
Required fix: Check PRD’s current guidelines on AI-assisted writing and adjust the acknowledgment language to comply, if needed.  

P4-N4 (NIT) – Minor formatting inconsistencies  
Section: Whole paper  
Problem: There are occasional inconsistencies in spacing and typography (e.g., fsky vs fsky with different spacing; “C 2 2◦” vs “C2 2°”; arrows and en-dashes around ViT‑Small notation, etc.).  
Required fix: Run a careful typesetting/formatting pass to standardize LaTeX macros for f_sky, degrees symbol, and model names, and ensure consistent use throughout.  

P4-N5 (NIT) – Slightly telegraphic footnotes  
Section: Footnotes in Sec. IV D and Appendix E; Pages 6 & 12  
Problem: Some footnotes contain dense internal discussion (e.g., about N_all vs N_spiral, “in queue for recompute”) that are hard to follow.  
Required fix: Either integrate essential content into the main text or streamline the footnotes to clearly state only the final analysis choices and their impact on results.  

---

## Summary recommendation

REJECT

The manuscript shows serious effort and includes a sophisticated analysis pipeline, but for PRD standards it falls short on multiple fronts: citation metadata errors, incomplete reference list, some mischaracterizations of previous work, unclear statistical framing of key “disfavored” claims, unresolved analysis-version language, and an overall scope that is heavy on survey/machine-learning details with relatively modest direct cosmological constraining power. Addressing the essential and major issues would require a substantial reworking of both the technical presentation and the positioning of the results, amounting to more than a “major revision” in PRD practice.

---

## PASS 2 — self-critique findings (what initial review missed)

[P4-N6] **Equation and table-definition mismatch for \(A_p\), \(N_{\text{all}}\), and the NaMaster field object**  
Section: Appendix A vs. Table I vs. Sec. IV C/D; Pages 5, 10–11  
Problem: Appendix A says the reported NaMaster field uses the *monopole-subtracted* CW-deficit map, but it also states that the field is defined as \(A_p=(N_{CW}^{(p)}-N_{CCW}^{(p)})/N_{\text{total}}^{(p)}\) with galaxy-weighted mask-mean subtraction, while Table I and Sec. IV C treat \(A_p\) as the *spirals-only* asymmetry \((N_{CW}-N_{CCW})/(N_{CW}+N_{CCW})\). The appendix then says the monopole-subtraction step is applied “so that the \(\ell=0\) mode is removed from the input field,” but the field object in the main text is introduced as a scalar asymmetry map without specifying which denominator is actually used for the headline \(C_1\).  
Required fix: State, in one place, the exact field used for the headline MASTER analysis:
- numerator,
- denominator,
- whether the mask-weight \(W_p=N_{\text{all}}^{(p)}\) enters only as a weight or also in the field definition,
- and whether the field is built from \(N_{\text{spiral}}^{(p)}\) or \(N_{\text{all}}^{(p)}\).  
Then make Appendix A, Table I, Eq. (3), and the footnote all use that same definition or explicitly distinguish the alternate diagnostic field.

[P4-N7] **Arithmetic inconsistency in Table II, raw/Catalog A percentage shift**  
Section: Table II; Page 5  
Problem: Table II gives Catalog A as \(0.5079 \pm 0.000279\) with “Excess (%) = +0.79” and “Dev. = 28.8.” Recomputing from the displayed numbers:  
- Excess relative to 0.5 is \(0.5079-0.5=0.0079\), i.e. **0.79%**, which matches.  
- The z-score is \(0.0079 / 0.000279 \approx 28.32\), not 28.8.  
The quoted deviation is therefore not consistent with the displayed mean and uncertainty.  
Required fix: Recompute the deviation using the exact underlying \(N\) or update the quoted \(f_{CW}\), uncertainty, or z-value so the three numbers agree.

[P4-N8] **Arithmetic inconsistency in Table II, Catalog C deviation**  
Section: Table II; Page 5  
Problem: Table II gives Catalog C as \(0.4974 \pm 0.000279\) with “Dev. = 9.5.” From the displayed numbers,  
\[
(0.4974-0.5)/0.000279 \approx -9.32,
\]
so the deviation is about **9.3σ**, not 9.5σ.  
Required fix: Either quote the exact \(f_{CW}\) to more digits, quote the exact binomial uncertainty from the true \(N\), or change the deviation to match the displayed values.

[P4-N9] **Arithmetic inconsistency in the “3.86× asymmetry-suppression factor”**  
Section: Sec. IV B; Page 5  
Problem: The text says the raw +2.05% catalog shift to equivariant −0.53% “demonstrates the dominance of the equivariant TTA process” and implies a 3.86× suppression factor. Recomputing the ratio from the displayed percentages gives  
\[
2.05/0.53 \approx 3.87,
\]
which is close, but the sign convention is not explained and the factor is sensitive to rounding of the input percentages. If the intended factor is exactly 3.86×, the displayed percentages should be quoted more precisely or the factor should be stated as approximate.  
Required fix: Either present the exact pre/post percentages to enough significant figures or soften the claim to “about 3.9×.”

[P4-N10] **Arithmetic inconsistency in Table III: \(C_\ell\), \(\sigma_{\text{null}}\), and quoted significance**  
Section: Table III; Page 7  
Problem: Several rows in Table III do not reproduce their listed significance when using the displayed \(C_\ell\) and \(\sigma_{\text{null}}\) values.  
- For \(\ell_{\rm eff}=4\): \(3.210/0.804 = 3.99\), not **6.097**.  
- For \(\ell_{\rm eff}=9\): \((-0.248)/0.574 = -0.43\), not **+2.232**.  
- For \(\ell_{\rm eff}=14\): \((-0.387)/0.446 = -0.87\), not **+2.626**.  
- For \(\ell_{\rm eff}=19\): \((-0.576)/0.420 = -1.37\), not **+2.229**.  
- For \(\ell_{\rm eff}=24\): \((-0.648)/0.366 = -1.77\), not **+2.470**.  
These are not small rounding differences; the significance column is not the simple \(C_\ell/\sigma_{\text{null}}\) implied by the header.  
Required fix: Explicitly define the statistic used for “Significance (σ)” in Table III and recompute each entry accordingly, or relabel the column if it is not a direct z-score.

[P4-N11] **Arithmetic inconsistency in Table IV, monopole-only reproduction percentage**  
Section: Table IV and surrounding text; Page 8  
Problem: Table IV reports pre-MASTER pseudo-\(C_\ell^{(\ell=1)}\) data \(=1.696\times10^{-2}\) and null \(=(1.685\pm0.007)\times10^{-2}\), then the prose says the null reproduces **99.3%** of the observed power. But \(1.685/1.696 = 0.99352\), i.e. **99.35%**, which is fine as an approximation. However, the same table also gives a \(z=+1.68\), and from the displayed values  
\[
(1.696-1.685)/0.007 \approx 1.57,
\]
not 1.68, unless the uncertainty is actually about \(0.00655\).  
Required fix: Recompute the \(z\) from the exact Monte Carlo standard deviation, not from the rounded \(\pm0.007\), or display the full precision needed to support the quoted \(z\).

[P4-N12] **Arithmetic inconsistency in Table I, injection floor and sample-size linkage**  
Section: Table I vs. Sec. VI A; Pages 1 and 8  
Problem: Table I lists the injection floor as “50%-rec-3σ at \(A=0.75\%\)” for \(N=471{,}049\) HC spirals, while Sec. VI A states \(P(\sigma>3)=0.55\) at \(A=0.75\%\) and \(P(\sigma>3)=0.15\) at \(A=0.5\%\). These numbers do not directly imply a 50% recovery threshold without interpolation, yet the paper presents the threshold as if it were directly measured.  
Required fix: State whether \(A=0.75\%\) is an exact simulation point, an interpolated 50% threshold, or a rounded summary of a curve fit. If it is interpolated, show the interpolation method and uncertainty.

[P4-N13] **Figure-caption/body mismatch for Fig. 1 label wording**  
Section: Fig. 1 caption vs. body; Page 4  
Problem: The caption says the example galaxies are from the “classified spiral sub-catalog (peq > 0.9),” while the body immediately preceding it says the production catalog uses “Catalog C (equivariant)” and later refers to high-confidence spirals via \(p_{\rm eq}>0.9\). The caption omits the fact that these examples are *selected from the same tier used for the headline analysis* and may therefore be read as illustrative only.  
Required fix: Add one sentence to the caption or adjacent text clarifying whether Fig. 1 examples are drawn from the same analysis tier as Catalog C or from a separate visualization-only subset.

[P4-N14] **Figure-caption/body mismatch for Fig. 2 D4-TTA description**  
Section: Fig. 2 caption vs. Sec. III C; Pages 4–5  
Problem: Fig. 2 caption says the classifier is evaluated on the “eight D4 transforms (four rotations × two reflections),” but Sec. III C says the production inference uses only **2-fold TTA** (original + horizontal flip) and explicitly rejects full D4 for the main pipeline. This makes the figure-caption description look like it depicts the production procedure, when the body says it is only a diagnostic validation.  
Required fix: Mark Fig. 2 explicitly as a diagnostic hold-out illustration, not the production TTA used in Catalog C, or revise the caption to note that D4 is *not* the production inference protocol.

[P4-N15] **Figure-caption/body mismatch for Fig. 3 sample counts and analysis target**  
Section: Fig. 3 caption vs. Table I / Sec. IV A; Pages 5–6  
Problem: Fig. 3 caption states that the spiral sub-catalog \(N_{\text{spiral}}=3{,}201{,}160\) is “the analysis target for all chirality statistics below,” but Table I and Appendix A show that the headline MASTER estimator uses a *subsample mask* with \(N=5{,}547{,}858\) weighted pixels and \(f_{\rm sky}=0.659\), not the same object as the spiral count. The caption therefore conflates the chirality sample count with the field-pixel count.  
Required fix: Distinguish between galaxy counts and pixelized-field counts in the caption, so readers do not infer that the reported \(N=3.2\)M is the direct input to the MASTER estimator.

[P4-N16] **Figure-caption/body mismatch for Fig. 5 threshold condition**  
Section: Fig. 5 caption vs. Appendix A; Pages 7 and 10  
Problem: Fig. 5 caption says the canonical mask “requires \(N_{\text{spiral}}(p)\ge 5\) per pixel,” which matches Appendix A in spirit, but Appendix A also mentions that the pixel-count threshold sweep varies this threshold from 5 to 50 with <0.5σ change in the headline result. The figure caption presents the \(N\ge 5\) cut as fixed and foundational, while the appendix indicates it is a tunable robustness parameter.  
Required fix: Clarify in the caption that \(N\ge 5\) is the default threshold, not a uniquely justified physical choice.

[P4-N17] **Figure-caption/body mismatch for Fig. 8 null amplitude**  
Section: Fig. 8 caption vs. Table IV; Page 9  
Problem: The Fig. 8 caption says the pre-MASTER \(\ell=1\) power is reproduced at **99.3%** by the monopole-only null, while Table IV gives a data value of \(1.696\times10^{-2}\) and a null mean of \((1.685\pm0.007)\times10^{-2}\). That ratio is consistent with 99.3%, but the same figure caption also says the post-MASTER residual is \(+3.64\sigma\), whereas the headline MASTER result in the abstract is \(-0.122\sigma\). The caption does not distinguish that these are *different estimators with different nulls*.  
Required fix: Explicitly add “not directly comparable” language in the caption itself, not just elsewhere in the paper, when juxtaposing the \(+3.64\sigma\) canonical-mask statistic and the \(-0.122\sigma\) subsample-mask statistic.

[P4-N18] **Equation-dimension issue for Eq. (2): normalization and probability-sum conservation**  
Section: Eq. (2); Page 3  
Problem: The TTA equations average probabilities from the original and flipped images, but the displayed formula is line-broken in a way that obscures whether the \(1/2\) factor applies to *each* class channel or to the vector as a whole. The surrounding text says the method “enforces flip-equivariance of the output protocol,” but the equation as typeset can be read as two separate definitions rather than a normalized probability-preserving average.  
Required fix: Rewrite Eq. (2) in vector form, e.g. \( \mathbf p_{\rm eq} = \frac12(\mathbf p_{\rm orig} + S \mathbf p_{\rm flip})\), and explicitly note that the components still sum to 1.

[P4-N19] **Equation-dimension issue for Eq. (3): asymmetry map denominator changes units of the mask weight**  
Section: Eq. (3), Appendix A; Pages 5 and 10  
Problem: Eq. (3) defines \(A_p\) using only spiral counts in the denominator, but Appendix A later uses \(N_{\text{total}}^{(p)}\) when defining the field for the mask-weighted MASTER analysis. These two choices produce different numerical fields even though both are called the “asymmetry map.”  
Required fix: Distinguish the two fields by notation, since the denominator choice changes the field amplitude and therefore the units/normalization of the spectrum input. If both are used, assign separate symbols and state which one is fed to each estimator.

[P4-N20] **Internal cross-reference mismatch: “Sec. IV D” vs. Appendix D claims about recovery percentage**  
Section: Sec. IV D, Appendix D, and abstract; Pages 1, 6, 12  
Problem: The abstract says the monopole+mask leakage null “reproduces 99.3%” of the observed pre-MASTER pseudo-\(C_\ell\), and Sec. IV D repeats that the monopole-only null explains the leakage. Appendix D then reframes the same channel as a **“non-headline, systematics-attributed canonical-mask excess”** and explicitly says the quantitative 99.3% figure is specific to the spiral-trial draw, with an all-galaxy rerun “in queue.” This means the abstract is summarizing a result that Appendix D itself treats as provisional and estimator-specific.  
Required fix: Mark the 99.3% reproduction statement as conditional on the spiral-trial null and remove it from the abstract unless the all-galaxy rerun is completed.

[P4-N21] **Unsupported novelty claim: “largest galaxy chirality catalog to date” lacks explicit comparison set**  
Section: Conclusions; Page 10  
Problem: The conclusion states the paper has constructed “the largest galaxy chirality catalog to date,” but the body only compares directly against CE-ResNet and mentions Shamir’s catalog sizes qualitatively. There is no explicit comparison against all extant chirality/spin catalogs in the literature, nor a compact table showing the previous largest catalog sizes.  
Required fix: Either add a comparison table with the major prior chirality catalogs and their sample sizes, or weaken the claim to “larger than the specific prior catalogs compared here.”

[P4-N22] **Unsupported novelty claim: “survey-scale coverage” is numerically true but not benchmarked consistently**  
Section: Abstract, Introduction, Conclusions; multiple pages  
Problem: The manuscript repeatedly claims “survey-scale coverage” and “3.2 million spirals,” but the comparison benchmark varies between CE-ResNet’s 1.95M galaxies and Shamir’s nearly 1.3M spirals, and sometimes the paper compares 3.2M spirals to 8.47M total galaxies. Because the benchmark set changes across sections, the “survey-scale” claim is not consistently tied to one denominator.  
Required fix: State one benchmark definition—spirals only, all classified galaxies, or total survey sample—and use it consistently wherever “survey-scale” is invoked.

[P4-N23] **Abstract faithfulness issue: “primary scientific result” vs. body’s split result structure**  
Section: Abstract vs. main text; Page 1 and whole paper  
Problem: The abstract presents the headline as a single null \(\ell=1\) result, but the body devotes substantial space to the \(+3.64\sigma\) canonical-mask excess and classifies it as a systematic. This is scientifically reasonable, but the abstract does not warn the reader that a strong positive signal exists in one estimator and is then argued away by a leakage model and auxiliary tests.  
Required fix: Add one sentence in the abstract stating that a separate canonical-mask estimator gives a \(+3.64\sigma\) excess, which the paper attributes to mask-leakage/systematics rather than a cosmological signal.

[P4-N24] **Abstract faithfulness issue: “not directly parity-violation test” is too compressed for the body’s theory discussion**  
Section: Abstract vs. Sec. VI B; Page 1 and 9  
Problem: The abstract correctly says the observable is parity-even and not a direct parity-violation test, but the body later discusses parity-violating tensor amplitudes and transfer functions. The abstract does not indicate that this mapping is deferred to follow-up theory work, which is important for understanding the scope of the claim.  
Required fix: Add a brief qualifier in the abstract that the connection to primordial parity-violating models is not derived here and remains model-dependent.

[P4-N25] **Internal cross-reference issue: “Appendix D” cited before its contents are fully defined**  
Section: Sec. IV D and Sec. V A; Pages 6–7  
Problem: The main text references Appendix D as containing the “five-anchor systematic analysis” and the “direct cross-spectrum verdict,” but the appendix contains multiple statistics with different nulls and even a note about an in-queue rerun. The citation implies a single resolved result, when the appendix actually contains provisional and estimator-specific quantities.  
Required fix: When citing Appendix D, specify which sub-result is meant (e.g. apodized-mask robustness, density-stratified null, leg-proxy cross-spectrum), rather than referring to the appendix as if it contained one unified conclusion.

[P4-N26] **Null-procedure comparability issue in Table III and Sec. IV D**  
Section: Table III, Sec. IV D, Appendix D; Pages 7, 12  
Problem: Table III’s \(-0.122\sigma\) headline result comes from a 500-MC label-shuffle null on the subsample mask, while the canonical-mask \(+3.64\sigma\) result is from a 500-MC per-pixel random-label permutation null, and the real-space \(+0.43\sigma\) result uses a 10,000-sample isotropic bootstrap. The paper already notes global non-comparability, but Table III and Sec. IV D place these values side-by-side without an immediate local qualifier in the relevant paragraph.  
Required fix: Add “not directly comparable across nulls” in the paragraph where the three values are first juxtaposed, not just in the abstract or Table I.

