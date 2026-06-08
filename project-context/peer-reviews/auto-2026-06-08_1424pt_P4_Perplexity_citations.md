# P4 auto-2026-06-08_1424pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (16197 chars)
**Wall time**: 88.1s

---

P4-E1 (ESSENTIAL) – Global use of future-dated / nonexistent references  
- **Location:** References [1]–[7], , , –, –; throughout body when these are cited.  
- **Problem:** Many references are dated 2020–2023 and are plausible-sounding, but the paper’s own date is “June 2026” and several citations cannot be confirmed in ADS/arXiv under the given combinations of author list, year, title, and journal. For instance, “Jia et al. (2023) … Astrophys. J. 943, 32, arXiv:2210.04168” is real and matches,[7] but “Cabass, Ivanov & Philcox 2023, Phys. Rev. D 107, 023523, arXiv:2210.16320” and “Cahn, Slepian & Hou 2023, Phys. Rev. Lett. 130, 201002, arXiv:2110.12004” cannot be verified as actually published with these exact metadata at the time of writing. Similarly, “Yu et al. (2020), Phys. Rev. Lett. 124, 101302, arXiv:1904.01029” exists, but other parity‑violation and cosmic‑birefringence references are partially fused or inconsistent in details (journal volume, page, DOI). Without explicit DOIs or correct arXiv IDs, these are not verifiable to PRD standards.  
- **Required fix:** For every reference:  
  - Provide the **correct arXiv ID** and verify that it matches the stated title and author list on arXiv.org and ADS.  
  - Provide **correct journal citation** (journal, volume, page, year, DOI) for all published works.  
  - Remove or clearly mark any **in‑preparation or submitted** works and do not quote firm numerical results from them.  
  - Explicitly check all titles and author lists against ADS; fix any fused or mismatched metadata. The editor should require an itemized list of corrected references.

P4-E2 (ESSENTIAL) – Internal contradiction on parity interpretation of multipoles  
- **Location:**  
  - Abstract, page 1: “this ℓ = 1 observable is … parity‑EVEN … NOT a direct parity‑violation test… parity‑odd analog requires 3D spin‑vector…”  
  - Sec. VI.B, page 6: “The ℓ = 1 dipole observable is parity‑even… the parity‑odd signal lives in the ℓ = 0 monopole and even‑ℓ multipoles.”  
- **Problem:** For a scalar parity transformation on the sphere, even ℓ multipoles are parity even and odd ℓ multipoles are parity odd. The text asserts instead that the *dipole* ℓ=1 is parity‑even while the monopole and even multipoles are parity‑odd, which is backwards. This is not a matter of convention: the spherical‑harmonic parity rule is standard and critical in a paper whose main scientific narrative is about parity and chirality.  
- **Required fix:**  
  - Correct the parity classification of multipoles: explain clearly that the *chirality field itself* may involve an axial quantity, and distinguish this properly from the spherical‑harmonic parity of the 2D scalar field on the sky.  
  - Re‑write Sec. VI.B and the abstract language to avoid incorrect statements such as “parity‑odd signal lives in ℓ = 0 and even‑ℓ multipoles.”  
  - Where the paper connects to parity‑violating models (e.g., –), ensure the mapping between theory’s parity‑odd operators and the observational multipoles is mathematically consistent.

P4-E3 (ESSENTIAL) – σ values from different nulls juxtaposed without sufficient “not comparable” caveats  
- **Location:**  
  - Abstract, page 1: multiple σ values (−0.122σ, +0.43σ, +3.64σ, 3.05σ) appear side‑by‑side. There is one sentence: “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I…”  
  - Table I, page 4: lists σ values from different nulls in one table without repeating the non‑comparability warning.  
  - Main text: Sec. IV, V, VI often juxtapose σ from different nulls (e.g. “+3.64σ residual… +3.3σ in the [0.5,0.6) bin… +2.31σ dipole… +6.48σ pre‑MASTER pseudo‑Cℓ”) without reiterating non‑comparability.  
- **Problem:** The instructions you were given explicitly require that whenever σ values from different null procedures appear side‑by‑side, there must be explicit “not directly comparable” qualification at every juxtaposition. The paper only states this once at the start; thereafter σ are freely compared (“collapsed from 2.31σ to 0.43σ”; “+3.64σ canonical residual is consistent with monopole leakage”) implying cross‑comparison. For PRD, this is misleading and violates the given review requirement.  
- **Required fix:**  
  - Every time σ values from different null constructions appear in the same sentence, table row, or paragraph, explicitly annotate which null is used and state that those σ cannot be directly compared.  
  - Where the text describes reductions in σ (e.g., “collapses from 2.31σ to 0.43σ”), rephrase in terms of the underlying test statistic or amplitude, or explicitly emphasize that σ units differ.

P4-E4 (ESSENTIAL) – Non‑reproducible “99.3%” monopole leakage reproduction claim  
- **Location:**  
  - Abstract, page 1: “pre‑MASTER raw pseudo‑C1 … is reproduced at 99.3% of its observed amplitude by a controlled monopole‑only generative null…”  
  - Table IV, page 5: “monopole‑only null reproduces 99.3% of the observed pre‑MASTER pseudo‑Cℓ(ℓ=1) power (residual +1.68σ).”  
- **Problem:** From Table IV, data pre‑MASTER pseudo‑Cℓ(ℓ=1) = 1.696×10⁻² and null mean = 1.685×10⁻². The ratio is 1.685/1.696 ≈ 0.9935, i.e. 99.35%. The quoted “99.3%” is consistent numerically, but the σ calculation is non‑transparent: σnull is written as “(1.685 ± 0.007)×10⁻²”, which implies σ ≈ 0.007×10⁻² = 7×10⁻⁵, but the difference between data and null is 0.011×10⁻² = 1.1×10⁻⁴. That would correspond to ≈ 1.57σ, not 1.68σ. The 1.68σ is thus inconsistent with the numbers displayed. PRD requires that every quoted σ be recomputable from displayed numbers.  
- **Required fix:**  
  - Recompute σ from the actual Monte Carlo distribution and present σnull consistently.  
  - Ensure that the difference (data − mean)/σnull gives the quoted z. If necessary, adjust either the central value, the quoted σnull, or the z to be internally consistent, and add enough significant figures to avoid rounding artefacts.  
  - Clarify whether “±0.007×10⁻²” is the standard deviation or standard error of the mean; use the appropriate quantity for σnull.

P4-E5 (ESSENTIAL) – Misleading “Fisher floor” and sensitivity scaling formula  
- **Location:** Sec. VI.A, page 6: “The Fisher Poisson floor at 3σ is ∼ 0.29% full‑amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).”  
- **Problem:** For a simple binomial difference in CW/CCW with N≈3.2×10⁶, the standard error in the fraction is ~\(\sqrt{p(1-p)/N} ≈ 0.00028 = 0.028\%\). Three sigma on the *full‐amplitude* A (difference between hemispheres) should therefore be ≲ 0.17% for ideal sampling, not 0.29%, unless a non‑trivial weighting and sky mask scaling are introduced. The text does not provide enough derivation of the factor linking σ(A/2) to A, and “fsky = 0.46” is unexplained here. As written, the “Fisher floor” is not reproducible from the given numbers.  
- **Required fix:**  
  - Provide the explicit analytic expression used to compute σ(A/2) and the 0.048% value, including how fsky is entering.  
  - Show the step from σ(A/2) to 3σ full amplitude.  
  - If masking or weighting explains the larger number, state this explicitly and show the scaling numerically.

P4-E6 (ESSENTIAL) – Mixed, inconsistent treatment of the asymmetry denominator  
- **Location:**  
  - Eq. (3), page 4: \(A_p = (N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})\).  
  - Appendix A, page 7: “Ap = (NCW − NCCW)/(NCW + NCCW)” but then “Field: scalar (spin‑0) asymmetry map Ap = (NCW(p) − NCCW(p))/Ntotal(p)” with Ntotal including NS.  
- **Problem:** The definition of the field used for NaMaster alternates between using only spirals in the denominator and including NS/edge‑on as part of Ntotal. This changes the noise and the physical meaning of A, and directly affects the power spectrum and all quoted Cℓ and σ. As written, the main text and Appendix A disagree on the denominator. This makes the headline results non‑reproducible.  
- **Required fix:**  
  - Choose and state a single, consistent definition of A_p used for all NaMaster analyses (spirals only vs. all galaxies).  
  - Correct the text in Appendix A and earlier sections so that the numerator and denominator match the actual implementation.  
  - If different definitions are used for different diagnostic runs, label them explicitly and ensure tables and σ values reflect the correct choice.

P4-E7 (ESSENTIAL) – Apparent double counting / inconsistency in Nmap,weighted vs. Nspiral  
- **Location:** Table I, page 4; Appendix A, page 7.  
- **Problem:** Table I states Ncatalog,spiral = 3,201,160 and Nmap,weighted = 5,547,858 for the subsample mask, while also stating that Nmap,weighted is the sum of depth weights Wp = Nall(p), including NS. But the full catalog has 8.47M objects; summing Nall over all pixels above the mask threshold should give >8.47M if some pixels contain multiple galaxies. The value 5.55M is < 8.47M, so Nmap,weighted appears to be neither total classified galaxies nor total spirals. The explanation “each galaxy is counted once” conflicts with standard HEALPix counting where multiple galaxies can reside in a pixel. The mapping between these numbers and the weighting used in NaMaster is thus unclear.  
- **Required fix:**  
  - Precisely define Nmap,weighted: is it a sum over pixels of W_p, and is W_p the number of galaxies in that pixel? If so, explain why the number is smaller than the catalog size.  
  - Clarify whether the subsample mask excludes some galaxies, and if so, quantify fractions and show how they yield 5.55M effective weight.  
  - Ensure that the dipole sensitivity estimates and σ values are recomputed using consistent effective N.

P4-E8 (ESSENTIAL) – Internal inconsistency in “global CW fraction” significance  
- **Location:**  
  - Table II, page 4: Catalog C: cw/(cw+ccw) = 0.4974 ± 0.000279, Dev. (σ) = 9.5.  
  - Sec. IV.B, page 4: “The Catalog C residual (9.5σ from 0.5000, Table II)… 3.86× asymmetry‑suppression factor from raw +2.05% to equivariant −0.53%…”  
- **Problem:** A deviation from 0.5 of −0.0026 with σ=0.000279 is ≈ 9.33σ, not 9.5σ, by simple division. The “2.05% to 0.53%” suppression factor is ≈ 3.87, not 3.86; the small mismatch is acceptable, but the σ discrepancy is notable given the paper’s emphasis on precise significance. PRD standards require that headline σ values be exactly reproducible from presented numbers.  
- **Required fix:**  
  - Recompute Dev.(σ) using Dev = (fCW–0.5)/σ and update Table II and text.  
  - Either present σ to fewer significant figures or adjust the quoted 0.000279 uncertainty so that 9.5σ is correct.

P4-E9 (ESSENTIAL) – “Falsification criterion” stated without robust statistical basis  
- **Location:** Abstract, page 1; Sec. VII.d, page 7.  
- **Problem:** The paper claims that “A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75%… would falsify the present null.” However, all σ in the paper are relative to specific null procedures and masks; the 0.75% threshold is itself derived under one particular null and classification pipeline (HC sample, per‑pixel shuffle). It is not demonstrated that this threshold is universal or that a measurement in a different survey with different masks, systematics, and estimator would be “inconsistent” in any rigorous likelihood sense. Presenting this as a “falsification criterion” overstates what the analysis justifies.  
- **Required fix:**  
  - Soften the language to “would be in strong tension with our null under comparable methodology” and specify that a matched estimator, mask, and null would be needed for a quantitative test.  
  - Remove the word “falsify” unless a formal statistical comparison framework is provided.

P4-M1 (MAJOR) – Overclaim of “largest” and “30× extension” without quantitative comparison  
- **Location:**  
  - Sec. VII, page 7: “We have constructed and analyzed the largest galaxy chirality catalog to date: 8,474,531 galaxies…”  
  - Sec. V.A, page 5: “…corroborate and extend the methodological critique of Iye et al. (2021) [5] with 3.2×10⁶ spirals (30× extension).”  
- **Problem:** The “largest” claim must be supported by a systematic comparison to all prior published chirality catalogs. The paper cites Shamir, Tadaki, Jia et al., but does not provide their exact catalog sizes in one place nor verify that none exceeds 8.47M in total or 3.2M spirals. “30× extension” is also approximate: Iye+ 2021 uses ~1.3×10⁶ spirals per its abstract; the present 3.2×10⁶ is between a factor of 2 and 3, not 30. It is unclear what quantity the “30×” refers to, and no calculation is given.  
- **Required fix:**  
  - Provide a table of catalog sizes in main comparable works (Shamir 2012/2020/2022, Tadaki et al., Jia et al., Iye et al.) and show explicitly that 3.2M spirals is indeed the largest chirality‑classified spiral sample.  
  - Correct or remove “30× extension”; if the factor refers to something else (e.g., sky area, volume, number of spirals compared to a specific earlier catalog), specify that explicitly and give the numbers.

P4-M2 (MAJOR) – Ambiguity in treatment of look‑elsewhere correction  
- **Location:** Sec. VI, page 6; Appendix C, page 8.  
- **Problem:** The text states both that a Bonferroni/BH correction across ~650 directions lowers the hemisphere signal below 1σ and that “direct‑MC pLEE ≤ 10⁻⁴” still holds. It is not clearly explained whether the Monte‑Carlo estimation of pLEE already includes the look‑elsewhere effect (it should, if max over directions is computed in each MC realization). The combination of analytic Bonferroni/BH and direct MC pLEE is confusing and may double‑count look‑elsewhere corrections or mislead readers about the effective global significance.  
- **Required fix:**  
  - Clearly define pLEE: is it the probability that the maximum over directions exceeds the observed value under the null? If so, then direct‑MC pLEE already includes look‑elsewhere.  
  - Remove or reframe Bonferroni/BH language so that only one global correction is used, and show consistency between analytic approximations and MC estimates.

P4-M3 (MAJOR) – Confusion between “monopole subtraction” and “monopole‑preserving” analyses  
- **Location:**  
  - Appendix A, page 7: “monopole‑subtracted CW‑deficit map fCW(n)−0.5” for the headline estimator.  
  - Table IV and Sec. IV.D, pages 4–5: discuss “un‑monopole‑subtracted CW‑fraction map” and “proper galaxy‑weighted monopole subtraction” affecting σ.  
- **Problem:** The description of when the monopole is subtracted, and whether it is galaxy‑weighted or unweighted, is scattered and not clearly tied to specific numerical results. Given that the central claim is about monopole‑mask leakage, precise control of monopole treatment is crucial. As written, a reader cannot unambiguously reconstruct which combination (un‑subtracted vs. subtracted; galaxy‑weighted vs. pixel‑weighted) leads to which values in Tables III–IV.  
- **Required fix:**  
  - Provide a concise table or schematic listing each estimator (pre‑MASTER canonical pseudo‑Cℓ, post‑MASTER canonical, subsample mask MASTER, real‑space dipole) with explicit statements: “monopole: subtracted / not; weighting: galaxy‑weighted / pixel‑weighted.”  
  - Make sure every numerical σ and Cℓ quoted in the main text clearly refers back to this table.

P4-M4 (MAJOR) – Use of training metrics partially circular with CE‑ResNet  
- **Location:** Sec. II.B, page 2: “67.6% of training labels derive from CE‑ResNet predictions; validation metrics against the full training set therefore partially reflect agreement with CE‑ResNet rather than independent ground truth.”  
- **Problem:** The quoted “93.7% three‑class accuracy” and “93.2% CW/CCW accuracy” (Appendix B) are measured against a training set largely pseudo‑labeled by CE‑ResNet, not independent human labels. This undermines their value as absolute accuracy estimates, yet the later sensitivity estimates (Sec. VI.A) rely on a separate “69.91%” GZ1 cross‑match to set an accuracy floor. The interplay between these two very different performance measures is not clearly explained; it is unclear how classification noise is actually propagated into the isotropy error budget.  
- **Required fix:**  
  - Explicitly state that the 93% metrics are **pseudo‑label agreement**, and that the only independent accuracy measure is the 69.91% GZ1 cross‑match.  
  - Recompute the classification noise attenuation factor (g=2a−1) only from the independent cross‑match, and explicitly show how it affects the sensitivity floor and the effective N in Fisher estimates.  
  - Clarify whether any of the headline σ values are corrected for classification noise; if not, state this clearly.

P4-M5 (MAJOR) – Overly long and repetitive relative to core contribution  
- **Location:** Entire manuscript (11 pages plus extensive appendices within the same file).  
- **Problem:** For a methods‑driven null‑result paper, the level of narrative repetition and the length of diagnostic appendices embedded in the main file are excessive relative to the single headline conclusion (“no ℓ=1 chirality dipole detectable at ≥0.75%”). Many paragraphs reiterate the same story about monopole leakage and systematic interpretations. PRD typically expects concise presentation, with extended diagnostic detail moved to a separate Supplement.  
- **Required fix:**  
  - Compress the main text to ~7–8 journal pages by moving most of Appendix C–E‑style diagnostic detail to an online Supplement and streamlining sections IV–VI.  
  - Focus the main paper on: data, classifier architecture, main estimators, monopole‑mask leakage demonstration, and the null result.

P4-m1 (MINOR) – Minor numerical rounding inconsistencies  
- **Location:**  
  - Sec. VI.A, page 6: “3.86× asymmetry‑suppression factor from raw +2.05% to equivariant −0.53%” (ratio is 3.87).  
  - Sec. VII.c, page 7: “2.31σ real‑space dipole and a +6.48σ pre‑MASTER pseudo‑Cℓ from a classifier CW excess of only 0.79%” – no explicit demonstration of how 0.79% gives those σ; likely correct but not shown.  
- **Problem:** Numbers are not wrong, but rounding and the lack of explicit formulae make it harder to verify claims.  
- **Required fix:**  
  - Where ratios are emphasized, either round consistently (e.g., 3.9×) or show the exact calculation.  
  - For the 2.31σ and 6.48σ values, provide at least one explicit mapping from the underlying amplitude to σ (or reference a figure/table where the mapping is visible).

P4-m2 (MINOR) – Ambiguous “largest” morphological catalog phrasing  
- **Location:** Sec. VII, page 7.  
- **Problem:** “largest galaxy chirality catalog to date” is ambiguous: is this in terms of total galaxies, spirals, or sky area? For example, Galaxy Zoo DESI has 8.7M galaxies with detailed morphology, so the “largest” should clarify “largest *automatic chirality‑classified spiral* catalog” to avoid overstating scope.  
- **Required fix:**  
  - Specify the quantity in which the catalog is largest (e.g., “largest automated chirality‑classified spiral catalog to date”) and support with explicit numbers versus prior work.

P4-n1 (NIT) – Repeated use of “canonical-mask” terminology  
- **Location:** Throughout (titles, multiple sections).  
- **Problem:** “canonical mask” is used heavily and sometimes appears twice in close proximity (“canonical‑mask Canonical‑N MASTER”) which reads awkwardly.  
- **Required fix:**  
  - Standardize terminology: define “canonical mask” once, then use “canonical mask” or “canonical footprint” consistently without redundancy.

P4-n2 (NIT) – Informal language and overuse of “headline” in scientific prose  
- **Location:** Throughout: e.g., “headline scientific result,” “headline empirical floor,” “headline 93.7%,” etc.  
- **Problem:** This is journal‑style, not press‑release style; repeated “headline” phrasing is informal and distracting.  
- **Required fix:**  
  - Replace with neutral terms such as “primary result,” “main sensitivity estimate,” “principal accuracy metric.”

P4-n3 (NIT) – Footnote 1 wording references “previous wording” and internal script names  
- **Location:** Sec. IV.D, page 4, footnote 1: discussion of “previous wording ‘Binomial(ntotal, pglobal_CW)’ was ambiguous; the code in scripts/monopole_null_generative.py uses Nspiral(p)… rerun is in queue…”  
- **Problem:** This looks like version‑history commentary rather than final‑form exposition. PRD typically discourages references to “previous wording” or “rerun is in queue” in the main paper.  
- **Required fix:**  
  - Rewrite the footnote to simply state the correct definition used in the analysis and remove process history and internal file names.

P4-n4 (NIT) – Minor duplicated hyphenation and spacing typos  
- **Location:** Multiple (e.g., “galaxy- chirality- catalog” in the Data Availability URLs; extra spaces in some composite terms).  
- **Problem:** Cosmetic typographical issues that slightly reduce polish.  
- **Required fix:**  
  - Run a careful copy‑edit pass to fix stray spaces around hyphens and standardize term hyphenation (“chirality catalog,” “spin‑vector,” etc.).  

## Summary recommendation  
**REJECT**

The paper’s core scientific idea and dataset are potentially valuable, but the current manuscript does not meet PRD standards. There are serious internal inconsistencies in key definitions (asymmetry field, parity interpretation, monopole handling), non‑reproducible or mis‑documented σ and “Fisher floor” calculations, and overstrong claims about falsification and catalog scale. The bibliography and citation metadata require a complete forensic cleaning, and the text needs substantial restructuring and clarification. These issues go beyond what can reasonably be addressed in a standard “major revision”; a thorough re‑write with corrected methodology exposition and vetted references would be needed before resubmission.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E10 (ESSENTIAL) – Widespread arithmetic / σ and ratio inconsistencies beyond those already flagged  
- **Location:** Multiple places in abstract, main text, and tables.  
- **Problem:** Several additional σ values and ratios do not match the adjacent numbers from which they are claimed to be derived, beyond the specific cases already identified in P4‑E4 and P4‑E8.  
- **Examples (non‑exhaustive):**  
  - Sec. IV.B: “The 3.86× asymmetry‑suppression factor from raw +2.05% to equivariant −0.53%…” The suppression factor is ambiguous and not reproducible. If one uses absolute amplitudes, \(2.05/0.53 ≈ 3.87\); if interpreting as reduction from +2.05% to −0.53% about zero, the “factor” is ill‑defined. No explicit formula is provided, and the text uses 3.86 in one place and ~3.9 elsewhere.  
  - Sec. VI.A: GZ1 attenuation factor \(g = 2a - 1\) with \(a = 0.6991\) gives \(g = 0.3982\), consistent numerically, but the implied “true‑underlying threshold ∼ 1.88%” from a 0.75% observed threshold is not shown step by step and is not obviously derivable from the numbers given. If the observed amplitude is attenuated by \(g\), one expects \(A_{\rm true} ≈ A_{\rm obs}/g ≈ 0.75\%/0.398 ≈ 1.88\%\), but this mapping is not explicit and mixes “Fisher floor” and injection thresholds in a way that is easy to misinterpret.  
  - Appendix C, per‑imaging‑leg systematics: The family‑wise p‑value 0.0086 is converted to “≈ 2.4σ family‑wise,” but the standard two‑sided Gaussian equivalent of \(p = 0.0086\) is closer to 2.63σ; if one‑sided, it is ≈ 2.39σ. The paper does not state whether σ is one‑ or two‑sided, so the conversion is not reproducible.  
- **Required fix:**  
  - For every σ, p‑value, and ratio in the manuscript, explicitly show (in text or a referenced equation) the calculation used.  
  - State clearly whether σ values derived from p are one‑ or two‑sided throughout and make the conversion consistent.  
  - Where ratios (e.g., “3.86×”) are emphasized, either provide the precise definition and formula or remove the claimed factor and describe the change qualitatively.  
  - Ensure all such quantities can be recomputed directly from displayed numbers to APS standards.

P4-E11 (ESSENTIAL) – Internal inconsistency in the definition and use of the chirality field \(A_p\)  
- **Location:** Eq. (3) Sec. IV.C; Table I caption; Appendix A (data vector and field definitions); footnote in Sec. IV.D; injection‑recovery description (Sec. VI.A).  
- **Problem:** Beyond the denominator inconsistency you already flagged in P4‑E6, there is a deeper, unresolved clash between multiple field definitions:  
  - Eq. (3) defines \(A_p = (N_{\rm CW}(p)-N_{\rm CCW}(p))/(N_{\rm CW}(p)+N_{\rm CCW}(p))\), i.e., spirals‑only numerator and denominator.  
  - Table I caption claims \(N_{\rm map,weighted} = \sum_p W_p\) with \(W_p = N_{\rm all}(p)\), “used as a survey‑depth weight in the NaMaster field object,” and also states that “Nmap,weighted exceeds Ncatalog,spiral because Wp includes non‑spiral galaxies,” which is contradicted by the actual numbers (see P4‑E7 and below).  
  - Appendix A first defines the asymmetry field as Ap = (NCW − NCCW)/(NCW + NCCW) (spirals only), but then says “Field: scalar (spin‑0) asymmetry map \(A_p = (N_{\rm CW}(p) − N_{\rm CCW}(p))/N_{\rm total}(p)\)” with \(N_{\rm total}\) including NS. This “all‑galaxy” denominator directly changes both noise and physical interpretation.  
  - Footnote in Sec. IV.D clarifies that the generative null draws from \(N_{\rm spiral}(p)\) only, to match “the field it is reproducing,” then immediately notes that earlier wording was ambiguous and that the code uses spirals only.  
  - The injection‑recovery sensitivity (Sec. VI.A) is applied to the “HC‑spiral subsample” but does not state whether \(A_p\) is constructed with spirals‑only or all galaxies in that context, nor whether the mapping from injected amplitude to recovered σ uses the same field definition as the NaMaster analysis.  
- **Required fix:**  
  - Choose a single definitive analytical definition of \(A_p\) for each analysis class:  
    - real‑space dipole fits;  
    - NaMaster pseudo‑\(C_\ell\);  
    - generative monopole‑null;  
    - injection‑recovery tests.  
  - Explicitly state in one place (e.g., a dedicated sub‑section) which definition applies where, and ensure Eq. (3), Appendix A, footnote, and Sec. VI.A are all updated to match.  
  - Recompute all affected σ, \(C_\ell\), and sensitivities using the consistent choice and update the tables accordingly.  
  - Any legacy references to “\(N_{\rm total}\)” vs “\(N_{\rm spiral}\)” should be cleaned up to avoid future confusion.

P4-E12 (ESSENTIAL) – Remaining contradictions and missing logic in look‑elsewhere treatment and pLEE  
- **Location:** Sec. IV.C (hemisphere max|A| mention in text vs Table IV); Sec. VI (discussion of Bonferroni/BH and pLEE); Appendix C (hemisphere asymmetry diagnostics, pLEE line).  
- **Problem:** While P4‑M2 flagged conceptual confusion, a second pass shows specific quantitative and logical mismatches:  
  - Table IV lists a “Hemisphere max|A| (NSIDEdir = 8) = 3.48×10⁻³, null mean (1.69±0.41)×10⁻³, z = +4.42,” but Appendix C describes a “maximum asymmetry 3.05σ” over hemispheres. It is not clear whether 3.05σ refers to the same statistic as the 4.42σ in Table IV or to a differently normalized test; this is not specified, yet both are labelled “maximum hemisphere” style tests.  
  - Appendix C states: “direct‑MC look‑elsewhere test (N = 10,000 random‑label shuffles) gives pLEE ≤ 10⁻⁴; the conservative Bonferroni/BH penalty… reduces post‑LEE significance to < 1σ.” If pLEE is defined as the probability that the *maximum* over directions exceeds the observed value, then the direct‑MC pLEE already includes the look‑elsewhere effect. Applying an additional Bonferroni/BH correction to that same maximum is conceptually double‑counting.  
  - Sec. VI uses pLEE ≤ 10⁻⁴ language again and attributes the random‑label rejection to a known systematic, but nowhere states clearly whether all quoted σ for hemisphere tests are before or after look‑elsewhere correction, nor whether p values in Table IV are local or global.  
- **Required fix:**  
  - Introduce a precise, formal definition of pLEE early in the methods: e.g. “pLEE is the probability that the maximum over all scanned directions under the null exceeds the observed maximum.”  
  - For each hemisphere statistic, clearly separate:  
    - the local σ and p at the best‑fit direction;  
    - the global pLEE from Monte‑Carlo;  
    - any analytic Bonferroni/BH approximations.  
  - Use either the MC‑based pLEE *or* an analytic Bonferroni/BH, not both; if both are presented, show explicitly that they refer to different things and do not double‑count.  
  - Clarify the relationship between the 4.42σ (Table IV) and 3.05σ (Appendix C) hemisphere results (same estimator vs different normalization) so the reader can follow the consistency.

P4-M6 (MAJOR) – Abstract and body mismatch on “subsample mask” vs “canonical mask” and which result is “headline”  
- **Location:** Abstract; Sec. III.A (declared analysis hierarchy); Sec. IV.C–D; Table I; Conclusions (VII.a–d); Appendix A.  
- **Problem:** The abstract, methods, and conclusions are not fully aligned about which estimator is the true “headline” and which mask it uses:  
  - Abstract: headline result is “MASTER‑deconvolved single‑mode C1 on the strict‑superset subsample mask (n = 5,547,858, fsky = 0.659) yields −0.122σ” and “real‑space … +0.43σ.” Later the abstract spends more space explaining the canonical‑mask generative null and 3.64σ canonical residual.  
  - Sec. III.A: primary estimators are real‑space dipole and MASTER on the subsample mask; canonical‑mask MASTER and hemisphere maximum are secondary.  
  - Table I, however, labels estimator (iii) “canonical MASTER” as just another row, and (v) “monopole+mask null,” with no clear tie‑back to primary vs secondary status; σ from these different nulls are placed side by side with only a single global disclaimer above the table.  
  - Conclusions VII.b–c again highlight the canonical‑N MASTER ℓ=1 direct compute and the +6.48σ raw pre‑MASTER dipole as central narrative pieces, blurring the emphasis away from the subsample‑mask −0.122σ and +0.43σ as the main scientific outcomes.  
- **Required fix:**  
  - Ensure the abstract, Sec. III.A, Table I, and Conclusions use a *consistent hierarchy* of estimators: clearly mark which ones are “primary cosmological” and which ones are “diagnostic/systematics.”  
  - In Table I, add a column or annotation flagging “primary vs diagnostic” and reiterate that σ from different nulls are not directly comparable (this also helps with P4‑E3/E).  
  - In the abstract and conclusions, reduce narrative emphasis on the canonical‑mask 3.64σ and 6.48σ values, explicitly labelling them as systematics‑diagnostic, not scientific detections, and keep the −0.122σ and +0.43σ subsample‑mask results as the clear focal point.

P4-M7 (MAJOR) – Abstract and body mismatch on “interpretation (ii) is attributed to…” vs demonstrated evidence  
- **Location:** Abstract (second paragraph, “Interpretation (ii) is attributed to a coherent depth/sampling‑correlated systematic…”); Sec. IV.D–E; Appendix D (systematic analysis).  
- **Problem:** The abstract states as a firm conclusion that interpretation (ii) (a coherent depth/sampling‑correlated systematic) is the explanation of the canonical‑mask residual, but the body shows only partial, suggestive diagnostics:  
  - Appendix D finds leg‑proxy ℓ=1 partial closure of only ~25% of the observed amplitude, and the density‑stratified null reduces but does not remove the excess.  
  - The WLS plus block‑bootstrap template analysis disfavors a pure primordial dipole but does not produce a unique best‑fit systematic model; instead, multiple templates (depth, PSF, morphology) are degenerate, and the fit is described qualitatively.  
  - Thus, the body supports “strong evidence for systematics” and “primordial dipole disfavored,” but not a fully quantified identification of a specific depth/morphology systematic with known amplitude and uncertainty.  
- **Required fix:**  
  - Soften the abstract sentence to reflect what is actually shown: e.g., “Interpretation (ii), a coherent depth/morphology‑correlated systematic, is favored by multiple diagnostics but not fully modeled.”  
  - In Sec. IV.D–E and Appendix D, add one explicit statement summarizing that the analysis does *not* uniquely decompose the residual into specific physical systematics; it only shows that a purely primordial dipole is incompatible with the joint diagnostics.  
  - Avoid language that treats interpretation (ii) as definitively established unless a quantitative model fit (with parameter estimates and uncertainties) is provided.

P4-M8 (MAJOR) – Sensitivity floor and Fisher limit derivation still under‑specified and dimensionally opaque  
- **Location:** Sec. VI.A; Appendix A (effective N and fsky); Sec. IV.A (catalog statistics); Table I.  
- **Problem:** Beyond P4‑E5, a second pass shows that the sensitivity statements blend Fisher limits, classification noise, edge‑on contamination, and masking without a fully explicit formula that can be verified:  
  - Sec. VI.A states: “The Fisher Poisson floor at 3σ is ∼ 0.29% full‑amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” No explicit expression is given for σ(A/2) in terms of Nspiral and fsky, nor for how fsky = 0.46 is obtained (Table I lists fsky = 0.659 and 0.49005, not 0.46).  
  - The step “σ(A/2) ≈ 0.048% ⇒ 3σ full amplitude ≈ 0.29%” is not derived. For a simple binomial difference one expects 3σ on A to be smaller (~0.17%) for the stated N, so the extra factor presumably comes from masking/weighting, but the factor is not spelled out.  
  - The subsequent mapping from the empirical 0.75% injection‑recovery threshold to a “true underlying threshold ∼ 1.88%” via g ≈ 0.398 again mixes Poisson and classification‑noise effects without a fully explicit, dimensionally consistent chain of equations.  
- **Required fix:**  
  - Provide a clear analytic derivation of σ(A/2), including the role of fsky and Nmap,weighted, with units (fractions vs percentages) explicitly indicated.  
  - Show the exact algebra from σ(A/2) to “3σ full amplitude,” including any factors of 2 from amplitude definitions.  
  - Present a compact expression for the impact of classification accuracy \(a\) on the effective amplitude and noise (e.g., using the standard \(g = 2a-1\) attenuation), and propagate it consistently into the Fisher floor and injection‑recovery thresholds.  
  - Reconcile the stated fsky = 0.46 value with Table I (0.659, 0.49005) or correct the number.

P4-m3 (MINOR) – Abstract/body mismatch on “survey‑scale” and “multi‑survey” phrasing  
- **Location:** Title; abstract first sentence; Sec. II (Data); Sec. VI (discussion and future directions).  
- **Problem:** The title and abstract use “Survey‑Scale Galaxy Chirality with Equivariant TTA” and “We report a multi‑survey, equivariance‑corrected angular dipole analysis…” The data, however, are drawn from the DESI Legacy Imaging Surveys DR8 via a single curated HuggingFace dataset (Smith42/galaxies), with cross‑matches to Galaxy Zoo DESI and GZ1; there is no independent second imaging survey in the analysis. “Multi‑survey” seems to be referring to DECaLS, BASS+MzLS, and DES sub‑components of DESI Legacy, which are different imaging campaigns but part of one overall survey product; this could mislead readers into thinking multiple independent surveys were combined.  
- **Required fix:**  
  - Clarify in the abstract and introduction that “multi‑survey” refers to the three imaging legs within DESI Legacy (DECaLS, BASS+MzLS, DES) rather than multiple independent surveys, or replace with “multi‑leg” / “multi‑imaging‑campaign.”  
  - Ensure “survey‑scale” is used in the sense of “full DESI‑Legacy‑footprint‑scale” and not implying cross‑survey combinations that are not actually performed.

P4-m4 (MINOR) – Small but systematic inconsistencies in hemisphere/dipole terminology  
- **Location:** Abstract; Sec. IV.C–D; Appendix C.  
- **Problem:** The manuscript alternates between “hemisphere maximum asymmetry,” “hemisphere LEE (MC),” “3.05σ local maximum,” and “Hemisphere max|A| (NSIDEdir = 8)” without clearly defining whether these refer to the same statistic (fraction difference, dipole amplitude, or a specific estimator) and whether they are evaluated on the same mask and catalog tier. This makes it unnecessarily hard to cross‑check the numbers and interpret the results.  
- **Required fix:**  
  - Introduce one canonical definition of the hemisphere statistic (e.g., “max over directions of |fCW,N – fCW,S| normalized by its null σ”) and stick to a single name for it in text, tables, and appendices.  
  - When a variant is used (different NSIDEdir, different catalog tier, different mask), label it explicitly each time.

P4-N3 (NIT) – Inconsistent capitalization and hyphenation of technical terms  
- **Location:** Throughout, e.g., “per-pixel shuffle” vs “pp-shuffle,” “pre‑MASTER” vs “pre-MASTER,” “NaMaster” vs “NaMaster/pymaster,” “D4 -TTA” vs “D4‑TTA.”  
- **Problem:** These inconsistencies do not affect the science but reduce clarity and make it harder to follow which procedures are identical and which are variants. In a methods‑heavy paper, consistent naming is important for reproducibility.  
- **Required fix:**  
  - Standardize each key term (e.g., “pre‑MASTER,” “post‑MASTER,” “per‑pixel shuffle (pp‑shuffle),” “NaMaster/pymaster,” “D4‑TTA”) and use the same spelling and hyphenation throughout.  
  - Where an abbreviation is introduced (e.g., pp‑shuffle), define it once and then use it consistently.

Given these additional issues, your initial review did not fully cover arithmetic consistency, internal logic of nulls and sensitivity, and the precise alignment of abstract claims with the demonstrated body of work. The paper will need another careful consistency pass (especially around field definitions, σ calculations, and pLEE) before it is ready for PRD.