# P4 auto-2026-06-05_1817pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13389 chars)
**Wall time**: 92.9s

---

P4-E1 (ESSENTIAL)  
Section: References, page 9–10  
Problem: Reference [2] is cited in the text as “Shamir (2022)” in PASJ with the title “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” but the bibliographic metadata given in the reference list is incorrect.  
– The PASJ 74, 1114 (2022) paper arXiv:2208.04143 is titled “Asymmetry between clockwise and counterclockwise galaxies in the Sloan Digital Sky Survey” and does not use the “alignment of non-random patterns” title.[1]  
– The supplied DOI `10.1093/pasj/psac058` and journal/volume/page match this “Asymmetry…” paper, not the stated title.  
Required fix: Correct [2] to match the actual PASJ article metadata (title and, if desired, add the arXiv ID). If “Analysis of the alignment of non-random patterns…” is intended, supply the correct journal/volume/DOI or correct arXiv ID; do not fuse distinct papers’ titles and DOIs.

P4-E2 (ESSENTIAL)  
Section: References, page 9–10  
Problem: Reference [1] (Shamir 2020) is given as:  
“Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.  
The arXiv entry 2007.16116 is titled “Patterns of Galaxy Spin Directions in SDSS and Pan-STARRS” and the published journal version in Ap&SS 365:136 carries essentially that title without the phrase “show parity violation and multipoles.”[2] Adding “show parity violation and multipoles” is not part of the official title.  
Required fix: Change the reference title to the actual journal (or arXiv) title, without the added clause, or clearly indicate if that longer phrase is a section subtitle that appears in the journal record.

P4-E3 (ESSENTIAL)  
Section: References, page 9–10  
Problem: Reference [3] (Shamir 2022, MNRAS 516, 2281) is written as:  
“Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.  
The MNRAS paper with DOI 10.1093/mnras/stac2372 and arXiv:2208.13866 is titled “Analysis of spin directions of spiral galaxies in the DESI Legacy Survey.”[3] The word “spiral” is missing in the manuscript’s title.  
Required fix: Correct the title in [3] to “Analysis of spin directions of spiral galaxies in the DESI Legacy Survey” to match the journal record.

P4-E4 (ESSENTIAL)  
Section: Abstract, page 1; Methods §III.A, page 3; Results §IV, Table I, Table II, page 4  
Problem: The manuscript states that “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.” However, multiple juxtapositions of σ from distinct null procedures occur without repeating the “not directly comparable” caveat “at every juxtaposition,” as required by the review instructions. Examples:  
– Abstract: “The MASTER-deconvolved single-mode pseudo-C1 … yields −0.122σ… The real-space post-TTA Catalog C dipole is +0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000).” These two σ values use different nulls but are placed side-by-side without a local reminder.  
– §III.A: “(i) … real-space CW-fraction dipole fit… (σdipole = 0.43, p = 0.30); and (ii) MASTER-deconvolved Cℓ at ℓ = 1 … −0.122σ.” Again, no explicit local “not comparable across estimators.”  
– Table I lists σ from at least four different nulls in a single column, but the caption does not reiterate their non-comparability.  
Required fix: At every place where σ from different null procedures are presented in direct proximity (same sentence, adjacent clauses, or same table row/column), explicitly state that these σ are defined with distinct nulls and are not directly comparable; e.g. “…0.43σ (bootstrap null; not directly comparable to the −0.122σ MASTER value, which uses a different null).” Include a brief disclaimer in the Table I caption as well.

P4-E5 (ESSENTIAL)  
Section: Abstract, pages 1–2; Main text §IV.C, §VI.A, page 4 & 6  
Problem: The abstract’s load‑bearing scalars must be consistent with the body and recomputable from displayed inputs. There is a significant inconsistency in the **global CW fraction** and its inferred significance:  
– Abstract and §II.B/§IV.B: Catalog C global CW fraction is given as 0.4974 ± 0.000279, where the ± presumably comes from binomial σ = √p(1 − p)/N with Nspiral = 3,201,160.  
– Using p = 0.4974, N = 3,201,160: σbin ≈ √[0.4974×0.5026/3,201,160] ≈ √(0.24999/3,201,160) ≈ √7.81×10⁻⁸ ≈ 2.80×10⁻⁴, consistent with 0.000279. Deviation from 0.5 is Δp = −0.0026, so Δp/σ ≈ −9.3, matching the quoted 9.5σ to order unity.  
– However, Table II reports “Dev. (σ)” for Catalog C as **9.5σ**, while earlier in §IV.B the same residual is described as “9.5σ from 0.5000.” This is consistent internally.  
The problem is that this “9.5σ” is repeatedly described as a “monopole” and then used to motivate a “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%,” but the raw fraction 0.5079 and the equivariant 0.4974 differ by 1.05 percentage points, not a factor 3.86 in amplitude relative to 0.5. The factor 3.86 seems to compare +0.79% to −0.26% in units of |excess|, but the text calls it “asymmetry-suppression factor” without stating clearly that the sign flips, not just the magnitude. This risks misinterpretation of how much of the bias is removed.  
Required fix:  
– Explicitly define what “asymmetry-suppression factor 3.86×” means and show the calculation (e.g. 0.79% / 0.26% ≈ 3.0, not 3.86). Recompute and correct the factor numerically; from Table II, |0.5079 − 0.5| / |0.4974 − 0.5| = 0.0079 / 0.0026 ≈ 3.04, not 3.86. There is a genuine numerical error.  
– Ensure that the same corrected factor is stated consistently in the abstract (if mentioned), main text, and any appendices.

P4-E6 (ESSENTIAL)  
Section: References, page 9–10  
Problem: Reference  is given as “J. Hou, Z. Slepian, and R. N. Cahn, ‘Measurement of parity-odd modes in the large-scale 4-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies,’ MNRAS 522, 5701 (2023), arXiv:2206.03625.” The MNRAS article 522, 5701 (2023) and arXiv:2206.03625 indeed correspond to that title.[3][4] However, in the main text this paper is not cited at all (no  in the text). Uncited references are not acceptable for PRD.  
Required fix: Either (a) cite  explicitly where parity-odd 4PCF galaxy constraints are discussed (e.g. in §I/§VI.B for context alongside [17,18]), or (b) remove  from the bibliography if truly unused.

P4-E7 (ESSENTIAL)  
Section: References, page 9–10  
Problem: Reference  is given as “R. N. Cahn, Z. Slepian, and J. Hou, ‘A test for cosmological parity violation using the 3D distribution of galaxies,’ Phys. Rev. Lett. 130, 201002 (2023), arXiv:2110.12004.” This matches the APS record and arXiv.[2] However, similar to , there is no in‑text citation of .  
Required fix: Either add a proper citation in the discussion of parity-violating sectors (§VI.B) or primordial tests, or remove  if not used.

P4-E8 (ESSENTIAL)  
Section: Data Availability, page 9; Appendix A, page 7  
Problem: The Data Availability section gives explicit URLs for catalog, model, and code on HuggingFace and GitHub. PRD normally allows URLs, but the journal requires that data/code be citable and stable; currently, these repositories are personal (Hubify-Projects, bamfai) and may not be archival. Also, there is an inconsistency with the dataset name: in §II.A the “Smith42/galaxies” dataset on HuggingFace is cited, whereas Data Availability lists “bamfai/galaxy-chirality-catalog.” These are distinct datasets and both need proper citation.  
Required fix:  
– Explicitly cite the Smith42/galaxies dataset in the reference list (with author/maintainer and year) if it is a primary data product.  
– Clarify the distinction between the parent DESI image dataset and the derived chirality catalog; both should have consistent names and, ideally, DOIs (e.g. via Zenodo).  
– Ensure the code/data locations are final, stable, and described in a way acceptable to PRD (no reliance on personal accounts without archival backup).

P4-E9 (ESSENTIAL)  
Section: Any place with today’s date in metadata: title page “(Dated: June 2026)”  
Problem: PRD requires that the date reflect the submission or revision date managed by the journal, not an arbitrary month/year supplied by the author. “(Dated: June 2026)” is non‑standard.  
Required fix: Replace the manual date with the standard PRD style (the journal will insert its own date), or remove it in the preprint version submitted to PRD.

P4-E10 (ESSENTIAL)  
Section: Global comparison to Shamir, Abstract and §VI.B, page 1 & 6  
Problem: The manuscript states that the present null “disfavors the Shamir ∼2–4% detection class at the amplitude level under our pipeline; a matched-footprint Ganalyzer reanalysis is required for a formal σ-level exclusion.” This claim of disfavouring prior results at the amplitude level is not quantitatively backed by a likelihood analysis or by a clear mapping from their estimator to the present one. Given that Shamir’s works use different selection functions, classifiers (Ganalyzer), and footprints, an amplitude‑only argument is not sufficient for a strong statement about their results. For PRD, such a statement of tension must be supported by a careful matched-sample analysis or be clearly softened.  
Required fix: Either (a) perform and report a matched-footprint reanalysis (or at least a controlled subset comparison) showing the quantitative inconsistency, or (b) weaken the language to something like “in tension at the level of simple amplitude comparison but not formally excluded, as a matched-footprint analysis is not yet performed.”

P4-M1 (MAJOR)  
Section: Abstract, pages 1–2; §IV.D, Table IV, page 4  
Problem: The abstract claims: “pre-MASTER raw pseudo-C₁ in the un-monopole-subtracted CW-fraction map … is reproduced at 99.3% of its observed amplitude by a controlled monopole-only generative null (N = 500, binomial realizations at p_global_CW = 0.4974…).” Table IV shows pre-MASTER pseudo-C₁(data) = 1.696×10⁻² and null mean = (1.685 ± 0.007)×10⁻². The ratio 1.685/1.696 ≈ 0.9935, consistent with 99.35%. However, the z value is quoted as +1.68σ. A 1.68σ deviation is not “explained at the percent level”; it corresponds to a p‑value ≈ 0.09, which is only marginal consistency. The text “explained at the percent level” is aggressive; for PRD, this must be quantitatively precise.  
Required fix:  
– Clarify that the monopole-only null recovers 99.3% of the *mean amplitude*, but that the actual data point is at +1.68σ relative to that mean; rephrase to “can account for nearly all (≈99%) of the observed amplitude, with the measured value lying 1.7σ above the monopole-only mean.”  
– Do not present this as a fully closed channel; emphasize residual uncertainty quantitatively.

P4-M2 (MAJOR)  
Section: §IV.C–D, Table I, Table III–IV, page 4–5  
Problem: Dimensional consistency and units in the angular power spectrum tables are unclear. Table III lists “Cℓ × 10⁶ (sr)” and σ_null × 10⁶ (sr). For a dimensionless asymmetry field A_p (difference divided by sum of counts), Cℓ should be dimensionless; if a factor of steradians enters due to normalization convention, it must be explained. Table IV reports pre-MASTER pseudo‑Cℓ(ℓ=1) = 1.696×10⁻² (no units indicated), while Table III’s ℓ=1 entry is 1.494×10⁻⁶ (sr). The relationship between pseudo‑Cℓ and MASTER‑deconvolved Cℓ, including units, is not spelled out. This makes it impossible to recompute significances purely from the presented numbers.  
Required fix:  
– Explicitly state the normalization convention for A_p and Cℓ (e.g. Cℓ dimensionless, but multiplied by 10⁶ for readability; “(sr)” is then misleading).  
– Add a bridge sentence explaining how 1.696×10⁻² pseudo‑Cℓ becomes 1.494×10⁻⁶ MASTER‑deconvolved C₁ (e.g. via mode‑coupling matrix inversion).  
– Ensure units are consistent across tables; if Cℓ is dimensionless, drop “(sr)” in the headers.

P4-M3 (MAJOR)  
Section: §III.C and Appendix B, page 3 & 7–8  
Problem: The classifier architecture and training description is generally detailed, but the paper states “Headline 93.7% three-class accuracy (with augmentation active); post-hoc evaluation without augmentation yields 94.9%. For binary CW/CCW discrimination: 93.2% accuracy,” and then uses a GZ1 cross‑match (69.91% accuracy, κ=0.40) as “conservative accuracy floor” for isotropy bounds. However, there is no explicit mapping or derivation showing how this 69.91% is propagated to the dipole sensitivity floor (other than invoking g = 2a − 1 ≈ 0.398 in §VI.A). While the formula g = 2a − 1 for dilution is standard, a PRD cosmology methods paper should show the intermediate steps (e.g. effective noise on A and on C₁).  
Required fix: Add a short derivation or appendix paragraph explicitly showing how classification noise with accuracy a results in an effective suppression g of the true dipole amplitude and how this modifies the Fisher floor and injection‑recovery results. This will make the sensitivity claims fully reproducible from the paper alone.

P4-M4 (MAJOR)  
Section: §VI.A, page 6  
Problem: The “Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” This is only sketched, not derived. Given that this 0.29% floor is central to the claimed sensitivity, PRD standards require that the formula for σ(A) be explicitly provided (including f_sky dependence and any weighting) and that the numerical value be recomputable.  
Required fix: Provide the explicit expression used for σ(A/2) in terms of N_spiral and f_sky (and any weighting), then show the numerical calculation that leads to 0.048% and 0.29%. Check and correct the value if any approximation was misapplied.

P4-M5 (MAJOR)  
Section: Overall length (10 pages including appendices)  
Problem: The paper attempts to present: a new catalog, classifier architecture, bias auditing suite, a full harmonic analysis with generative nulls, and an extensive canonical‑mask systematic analysis. For the modest headline physics result (essentially a null at ℓ=1 with a relatively simple statistic), the manuscript is somewhat long and diffuse for PRD. Several appendices (C–E) read like extensive technical notes that could be moved to a data‑release companion or arXiv‑only material.  
Required fix: Condense the main text to emphasize (i) definition of the estimator, (ii) null‑test framework, and (iii) core results. Consider moving the long bias-test table, much of the classifier training detail, and the extended canonical‑mask systematics narrative to supplemental material. A target length of 7–8 journal pages (main text) is more appropriate for the level of methodological innovation and the essentially null result.

P4-M6 (MAJOR)  
Section: Use of AI tools, Acknowledgments, page 9  
Problem: The paper states “AI tool usage: Large-language-model tools were used for code review and manuscript editing; all scientific results are derived from the authors’ own analysis and the cited public datasets.” PRD currently expects any AI‑assistance to be transparent but not to obscure authorship responsibility. The sentence is acceptable in spirit but vague (no indication of which tools or scope).  
Required fix: Clarify the extent of AI usage more concretely (e.g. “LLM tools were used for language polishing only; all code and analysis pipelines were written and validated by the author”). Ensure that this phrasing complies with APS’s latest AI‑usage policy.

P4-m1 (MINOR)  
Section: §II.A, page 2  
Problem: The URL “https://huggingface.co/datasets/Smith42/galaxies” appears inline. PRD generally discourages raw URLs in the body; they should be moved to a footnote or reference.  
Required fix: Move the dataset URL into a formal reference or footnote, and refer to it in text as “the Smith42/galaxies dataset.”

P4-m2 (MINOR)  
Section: Equations (2) and (3), pages 3–4  
Problem: Equation (2) uses the symbol “” (likely a corrupted plus sign or similar) in the expression for the equivariant probabilities:  
“PCW^eq = 1/2 P_CW^orig + P_CCW^flip ” etc. This appears to be a typesetting artifact. Equation (3) similarly has minor spacing issues.  
Required fix: Clean the LaTeX so that the equations render without stray glyphs; e.g.  
\(P_{\rm CW}^{\rm eq} = \tfrac12 (P_{\rm CW}^{\rm orig} + P_{\rm CCW}^{\rm flip})\), etc.

P4-m3 (MINOR)  
Section: §IV.A, Table I note, page 4  
Problem: The note below Table I explains N_map^weighted but uses inconsistent notation: N_all^(p) vs N_total^(p) in different locations, and “P” sometimes appears as a summation index placeholder without definition.  
Required fix: Standardize the notation, define the summation index clearly (e.g. “sum over pixels p”), and use a single symbol (e.g. N_total^(p)) throughout for consistency.

P4-m4 (MINOR)  
Section: Appendix A, page 7  
Problem: The NaMaster binning configuration line “(nmt.NmtBin.from lmax linear(lmax=191, nlb=1))” is nearly literal Python, but with a space in “from lmax” likely due to typesetting. This is confusing as pseudo‑code.  
Required fix: Either provide valid pseudo‑code in a code block or describe it in words (e.g. “a single‑ℓ binning from ℓ=1 to ℓ=191 with Δℓ = 1”). Avoid half‑broken API calls in the text.

P4-m5 (MINOR)  
Section: §II.B, page 2  
Problem: The sentence “Note: 67.6% of training labels derive from CE-ResNet predictions; validation metrics against the full training set therefore partially reflect agreement with CE-ResNet rather than independent ground truth.” is important, but could be misread as implying circularity in the isotropy result.  
Required fix: Add one clarifying sentence that the isotropy tests are run on DESI galaxies not used in the CE-ResNet training and that the CE-ResNet‑derived labels serve only as an initial training signal.

P4-m6 (MINOR)  
Section: §V.A, page 5  
Problem: The phrase “these conclusions corroborate and extend the methodological critique of Iye et al. (2021) [5] with 3.2×10⁶ spirals (30× extension)” is imprecise: Iye et al. do not present their work as a “methodological critique” per se but as an empirical re‑examination.  
Required fix: Soften and accurately attribute: e.g. “These conclusions are consistent with and extend the empirical re‑examination of Shamir’s claims by Iye et al. (2021) with an enlarged sample of 3.2×10⁶ spirals (≈30× more galaxies).”

P4-m7 (MINOR)  
Section: §VII, conclusion bullet (d), page 7  
Problem: “A future survey detecting a chirality dipole at σ > 5 with amplitude ≳ 0.75% at ≥ 10⁷ galaxies would falsify the present null.” The usage of “falsify” is strong; in a strict statistical sense, this would show inconsistency with this dataset or its systematics model, but not necessarily “falsify” the analysis.  
Required fix: Replace “falsify” with “be in significant tension with” or similar more precise wording.

P4-n1 (NIT)  
Section: Title, page 1  
Problem: Title is extremely long and multi‑clausal: “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ = 1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals).” PRD typically prefers concise titles; the current title reads like an abstract.  
Required fix: Strongly consider shortening to something like: “Survey-scale galaxy chirality with equivariant averaging: an ℓ=1 dipole null and monopole–mask leakage in DESI Legacy spirals.” Keep specifics (−0.122σ, 8.47M) in the abstract.

P4-n2 (NIT)  
Section: Text duplications and phrasing, multiple pages  
Problem: Several phrases are repeated verbatim or nearly so (e.g. “canonical-mask leakage channel,” “headline null,” “strict-superset subsample mask”). While not technically incorrect, this repetition slightly detracts from readability.  
Required fix: Light editing to reduce repeated phrases where not necessary.

P4-n3 (NIT)  
Section: PACS numbers, page 1  
Problem: PACS is deprecated; APS now uses PhySH.  
Required fix: Replace PACS with appropriate PhySH keywords as per PRD guidelines.

P4-n4 (NIT)  
Section: Minor typography, various pages  
Problem: Occasional mismatched hyphens/en‑dashes (e.g. “3.2×106” vs “3.2× 10^6”, “per-pixel” vs “per pixel”) and spacing anomalies around symbols.  
Required fix: Run a careful typographical pass to standardize scientific notation and hyphenation.

## Summary recommendation

MAJOR REVISIONS

The core scientific analysis appears plausible and the main numerical claims are broadly self‑consistent, but there are multiple issues that do not meet PRD standards: fused and slightly incorrect reference metadata, over‑strong interpretation of the monopole‑mask leakage closure, some ambiguous units and missing derivations in key sensitivity estimates, uncited references, and an overlong, somewhat diffuse presentation for the level of novelty. These problems are fixable, but require a careful revision to tighten the statistical and methodological exposition, correct and clarify the bibliography, and sharpen the connection between classifier systematics and cosmological conclusions.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E11 (ESSENTIAL)  
Section: Abstract, §IV.B, §VII.A (multiple locations)  
Problem: The **“3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%”** is arithmetically inconsistent with the numbers actually used and displayed. The paper’s own catalog fractions give:  
- Catalog A (raw): \(f_{\rm CW} = 0.5079\Rightarrow\) excess \(= +0.79\%\).[2]  
- Catalog C (equivariant): \(f_{\rm CW} = 0.4974\Rightarrow\) excess \(= -0.26\%\).[2]  
The ratio of magnitudes of excess about 0.5 is \(|0.5079-0.5|/|0.4974-0.5|=0.0079/0.0026\approx 3.04\), not 3.86, and neither 2.05% nor 0.53% appears anywhere in the actual tables.[2] The text appears to use stale numbers from a previous version.  
Required fix:  
- Replace 3.86× by the correct suppression factor computed from the *current* raw and equivariant fractions (≈3.0× if using 0.5079 and 0.4974).  
- Remove or correct the “+2.05%” and “−0.53%” values so they match the catalog tiers or explicitly mark them as obsolete and not used in any inference.  
- Ensure all places that reference this factor (abstract, §IV.B, and any discussion sections) are updated consistently.

P4-E12 (ESSENTIAL)  
Section: §IV.B, Table II  
Problem: The **“Dev. (σ)” values in Table II** do not match the stated binomial uncertainties. The table reports for each tier an uncertainty of ±0.000279, with Dev defined in text as \((f_{\rm CW} - 0.5)/\sigma\) and \(N_{\rm spiral}=3{,}201{,}160\).[2] Using \(\sigma = 0.000279\):  
- Tier A: \(f=0.5079\Rightarrow \Delta=0.0079\Rightarrow \Delta/\sigma \approx 28.3σ\), close to the tabulated 28.8σ.[2]  
- Tier C: \(f=0.4974\Rightarrow \Delta=-0.0026\Rightarrow \Delta/\sigma \approx -9.3σ\), while the table gives −9.5σ.[2]  
Minor rounding aside, the much larger issue is that the *same* σ=0.000279 is used for all tiers even though tiers A,B,C do not necessarily share the same effective N (e.g. if any filtering differs). The text never states that \(N_{\rm spiral}\) is identical across tiers, and Catalog A/B may have subtly different usable spiral counts than Catalog C.  
Required fix:  
- Explicitly state that all three tiers share the exact same \(N_{\rm spiral}\) if this is true, or provide the tier-specific N used to compute σ.  
- Recompute Dev(σ) with the correct N for each tier and update the table to the exact rounded values; if a single N is used deliberately for comparability, say so explicitly and explain the choice.

P4-E13 (ESSENTIAL)  
Section: §VI.A (Sensitivity Floor and Minimum Detectable Signal)  
Problem: The **Fisher floor** numbers are non‑reproducible and dimensionally opaque. The text states: “The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).”[2] No explicit formula is given, and with the displayed quantities the numbers cannot be uniquely reproduced:  
- If \(A\) is the full dipole amplitude and \(A/2\) is the fractional hemispheric difference, a Poisson-limited variance should scale roughly as \(\sigma(A/2)\sim 1/\sqrt{N_{\rm eff}}\), possibly modulated by \(f_{\rm sky}\). Plugging \(N=3.2\times 10^6\) gives \(\sigma\sim 0.056\%\), not 0.048%, before any sky‑fraction corrections.  
- The way \(f_{\rm sky}=0.46\) enters is not described; depending on convention, it could either increase or decrease σ, but the text gives no normalization or derivation.  
Required fix:  
- Provide the exact analytic expression for \(\sigma(A/2)\) used, including all factors of \(f_{\rm sky}\), solid angle, and any weighting.  
- Show the explicit numerical calculation step‑by‑step leading to 0.048% and 0.29%, or correct these numbers if they came from an earlier N or mask.  
- Ensure that the stated “3σ floor” (0.29%) is traceable from the given N and fsky; otherwise, update it to the recomputed value.

P4-M7 (MAJOR)  
Section: Abstract vs. §IV.D, Appendix D (canonical-mask residual interpretation)  
Problem: The **abstract’s narrative on the canonical-mask residual** is stronger than the body’s more nuanced treatment. The abstract says: “The +3.64σ canonical-mask residual is consistent with monopole leakage through survey geometry … and is not interpreted as a cosmological signal.”[abstract] In the body, Appendix D emphasizes only that interpretation (i) (a clean ∼1.7% dipole) is disfavored and that the residual is “most likely” due to depth/morphology‑correlated systematics, not that monopole leakage alone is sufficient to explain it.[2] The generative null in Table IV reproduces 99.3% of the *pre-MASTER* pseudo‑\(C_1\) but still leaves the *post-MASTER* residual at +3.64σ.[2] Thus “consistent with monopole leakage” is an overstatement; the leakage model explains the pre-MASTER amplitude, but only partially constrains the remaining residual.  
Required fix:  
- Rephrase the abstract to match the body’s more careful language, e.g. “consistent with a combination of monopole–mask leakage and depth/morphology‑correlated systematics” rather than attributing it solely to monopole leakage.  
- Explicitly distinguish in the abstract between (a) pre‑MASTER pseudo‑\(C_1\), which is reproduced at ≈99% by the monopole-only null, and (b) the post‑MASTER +3.64σ canonical residual, which is *interpreted* as systematic but not fully modeled by monopole leakage alone.

P4-M8 (MAJOR)  
Section: Abstract; §IV.C–D; Table I, Table III–IV  
Problem: **Null-procedure comparability is not consistently stated** wherever σ values are juxtaposed. While you already flagged some cases, additional proximity issues remain:  
- Abstract: “The MASTER-deconvolved single-mode pseudo-C1 … yields −0.122σ… The real-space post-TTA Catalog C dipole is +0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000).”[abstract] No local reminder appears that these σ values come from different nulls and are not comparable.  
- §IV.C first paragraph: contrasts the 0.43σ simple dipole with “2.31σ real-space dipole and a +6.48σ pre-MASTER pseudo‑Cℓ in the lowest bandpower” from Catalog A in the same sentence without restating that the σ definitions differ between the isotropic bootstrap and the pseudo‑Cℓ MC null.[2]  
- Table III caption: it mixes the subsample-mask single‑mode ℓ=1 result (−0.122σ) with canonical‑N bandpowers, but the caption does not reiterate that the σ in row 1 comes from a different null than the σ in rows 2–5.  
Required fix:  
- Wherever σ from different nulls are placed in the same sentence, clause, or table, add an explicit parenthetical qualifier, e.g. “(σ defined relative to [null X]; not directly comparable to the [null Y] σ values below).”  
- In Table III’s caption, explicitly state the null procedure associated with each set of σ and repeat the “not directly comparable” caveat.

P4-M9 (MAJOR)  
Section: §V.A, §VII.a; Abstract and Discussion (Shamir comparison)  
Problem: The **“factor of ∼6–12” suppression/tension with Shamir** is not numerically justified anywhere in the body and appears stale. The text claims: “This is inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼ 6–12 under the present pipeline” in §V.A, and again in §VI.B: “disfavors … by a factor of ∼ 6–12.”[2] However:  
- Your own sensitivity floor says 50%-recovery-at-3σ at A ≈ 0.75% full amplitude.[2] A Shamir-like 3% amplitude is therefore ≈ 4× this threshold, not 6–12×.  
- Under a simple amplitude comparison, the equivariant Catalog C monopole deviation |0.4974−0.5|=0.26% is ≈11.5× smaller than a 3% monopole, but this is not clearly what is meant by “factor 6–12,” and no calculation is shown.  
- There is no explicit mapping from Shamir’s reported 2–4% per-bin asymmetries and dipole formats to the A used here.  
Required fix:  
- Either remove the “6–12×” factor or provide a precise definition (e.g. ratio of Shamir’s amplitude to your 0.26% residual, or to your 0.75% detection threshold) and show the arithmetic.  
- Align abstract, §V.A, §VI.B, and conclusions so they use the *same* quantitative comparison, and soften language as already requested unless a matched-footprint analysis is performed.

P4-M10 (MAJOR)  
Section: §III.C; Appendix B; §VI.A  
Problem: The **propagation of classifier accuracy into dipole sensitivity** is still under‑specified quantitatively. You now state: “we treat 69.91% as the conservative accuracy floor and propagate it to all downstream isotropy bounds via the sub-percent systematic floor in Sec. IV C,”[2] and in §VI.A give “GZ1-dilution factor \(g = 2a − 1 ≈ 0.398\) for a = 0.6991, giving a true-underlying threshold ∼ 1.88%.”[2] But:  
- There is no explicit derivation linking the three‑class accuracy and κ to an effective multiplicative dilution of the dipole amplitude in A, nor to the 3σ detection threshold.  
- It is not clear whether the Poisson Fisher floor already includes this dilution or whether you apply g as a separate factor; the relationship between 0.29% Fisher floor, 0.75% empirical threshold, and 1.88% “true underlying threshold” is never written as an explicit formula.  
Required fix:  
- Add a short derivation showing (i) how classification accuracy a leads to a fraction of effective random labels, (ii) how that converts into a multiplicative factor g on the underlying dipole amplitude, and (iii) how this produces the 0.75% and 1.88% thresholds.  
- Check the arithmetic and ensure that 0.29%, 0.75%, and 1.88% are mutually consistent under the stated model; update any values that are using outdated N or g.

P4-M11 (MAJOR)  
Section: §IV.C, Appendix A; Equation (3)  
Problem: There is a **subtle but important inconsistency between the definition of the asymmetry field \(A_p\)** in the main text and in Appendix A.  
- §IV.C defines \(A_p = (N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)})/(N_{\rm CW}^{(p)} + N_{\rm CCW}^{(p)})\), i.e. denominator is spirals only.[2]  
- Appendix A defines the NaMaster field as \(A_p = (N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)})/N_{\rm total}^{(p)}\), where \(N_{\rm total}\) includes NS galaxies as well.[appendix A]  
This change of denominator alters the effective variance and normalization of Cℓ. It is not described as a deliberate redefinition, and no scaling relationship is given to allow recomputation of Cℓ from the counts.  
Required fix:  
- Make clear in the main text that there are *two* conventions for \(A_p\) (spiral‑only and total‑galaxy‑weighted), or unify them to a single definition throughout.  
- If both are kept, explicitly state which one is used for each estimator (real-space dipole vs. harmonic analysis), and provide the mapping between them so a reader can recompute C1 and its σ from the count statistics.

P4-m8 (MINOR)  
Section: §II.B; §E (Morphology Systematics)  
Problem: The **description of edge-on contamination and its impact on sensitivity** is vague and not arithmetically linked to the final floor. You state “Edge-on galaxy contamination … reduces effective sample size by ∼ 10–15%, corresponding to a ∼ 5–8% sensitivity penalty,” but no calculation is provided to connect the fraction of edge-ons, their misclassification rate, and the quoted 5–8% penalty.[2]  
Required fix:  
- Provide a one‑line calculation: e.g. “If f of galaxies are effectively random labels, the variance increases by 1/(1−f), so a 10–15% loss in effective N implies a √(1/(1−f)) ≈ 1.05–1.08 penalty in σ.”  
- Confirm that this correction has been incorporated (or not) into the quoted 0.29% Fisher floor and the 0.75% empirical threshold.

P4-m9 (MINOR)  
Section: §III.A (Declared analysis hierarchy), Table I, §IV.C  
Problem: The **definition of the “hemisphere LEE (MC)” estimator** in Table I is not cleanly cross‑referenced. Table I lists estimator (iv) as “hemisphere LEE (MC)… pLEE ≤ 10⁻⁴,”[2] but the main text reference to this result appears only in Appendix C, and §IV.C mentions a “3.05σ local maximum; Appendix C” in the bullet list, without explicitly linking to Table I’s pLEE or clarifying that the pLEE quoted there is the pre‑correction value before Bonferroni/BH.  
Required fix:  
- In §IV.C or §IV.E, add a sentence explicitly connecting estimator (iv) in Table I to the Appendix C hemisphere analysis, clarifying that pLEE ≤ 10⁻⁴ is the raw MC probability before multiple‑testing correction, and that the post‑LEE adjusted significance is <1σ.  
- This makes the numerical values in Table I fully traceable from the body text.

P4-n3 (NIT)  
Section: Abstract; §I; §VII  
Problem: Several **novelty/scale phrases** are still not explicitly supported: e.g. “survey-scale coverage of 8.47 million galaxies (3.2M spirals, 1.6× CE-ResNet’s scale)” and “largest galaxy chirality catalog to date.”[2] The 1.6× factor is correct given CE‑ResNet’s quoted 1.95M galaxies vs. your 3.2M spirals, but “largest to date” is not justified against other possible catalogs (e.g. Tadaki et al., Walmsley et al.).  
Required fix:  
- Keep the quantitative, demonstrable claims (e.g. “1.6× CE-ResNet’s spiral count”) and either (a) remove “largest” or (b) explicitly note the basis, e.g. “to our knowledge, this is the largest *publicly documented* chirality catalog, exceeding CE‑ResNet’s 1.95M spirals by a factor 1.6.”  

Because the supplied text does not include the figures themselves, I could not systematically check figure–caption numerical consistency (point B), but within the tables, equations, and text, the items above are additional issues that were not flagged in your initial review.