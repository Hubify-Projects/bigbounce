# P2 auto-2026-06-08_2353pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11933 chars)
**Wall time**: 85.9s

---

P2-E1  
Section: References (global) — all pages  
Problem: The manuscript contains multiple in-text citation placeholders marked only as “[?]” with no corresponding reference list rendered in the provided text (e.g. “Planck HFI analysis [?]”, “Planck NPIPE [?]”, “ACT DR6 [?]”, “Minami-Komatsu self-calibration method”, “Fujita, Murai, Nakatsuka & Tsujikawa (2021)”, “Namikawa, Murai & Naokawa [?]”, “companion Paper I(a) [?]”, “companion paper [?]”, “14-barrier catalog”). These cannot be verified against arXiv or ADS, and several are clearly incomplete or ambiguous (“Namikawa, Murai & Naokawa” looks like a corrupted author list; “Paper I(a)” is internal bookkeeping).  
Required fix: Provide a complete, properly formatted reference list. Replace every “[?]” with a specific, verifiable citation (correct authors, year, journal or arXiv ID). Fix any fused/garbled author names (e.g. “Namikawa, Murai & Naokawa” to the correct list). Remove internal shorthand like “Paper I(a)” or replace it with the actual published/submitted reference. Until a full bibliography is supplied and can be checked, the paper does not meet PRD standards.

---

P2-E2  
Section: Abstract, p.1  
Problem: The abstract quotes “βobs = 0.342 ± 0.094◦ from the Eskilt et al. joint Planck + ACT analysis” and “3.6σ isotropic birefringence signal” without a corresponding complete citation. “Eskilt et al.” appears to refer to Minami-Komatsu–style analyses or later joint Planck+ACT work, but the exact paper (title, year, arXiv ID, and whether this exact numerical value appears there) cannot be checked because the reference is only “Eskilt et al.” with no bibliographic details in the manuscript.  
Required fix: Provide a full reference (authors, title, journal, year, arXiv ID) for the “Eskilt et al.” joint analysis and verify that βobs = 0.342 ± 0.094° and the stated 3.6σ significance actually match that work’s abstract or tables. If the values differ, update the numbers in the abstract and body or explain clearly how they were derived (e.g. from a different combination or reanalysis).

---

P2-E3  
Section: Abstract & Sec. 3.2, p.1–3  
Problem: The abstract states “We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061◦ (3.9σ from zero) with an effective photon coupling fphoton × C0 = 1.73 ± 0.44,” but the derivation of fphoton × C0 is not defined anywhere in the text, and no explicit formula, units, or connection to gaγ or standard conventions is given. This parameter appears only in Eq. (5) as a number without a definition, and cannot be traced back to any cited work for verification.  
Required fix: Explicitly define fphoton (what combination of fundamental constants and fa it represents, with units) and explain how Eq. (5) is obtained from the data combination in Eq. (3). Provide either a short derivation or a clear reference where this parameterization and numerical value are introduced. Without a precise definition, the numerical result is not scientifically interpretable.

---

P2-E4  
Section: Sec. 3.1 & Sec. 3.2, p.2–3  
Problem: The combined constraint βcombined = 0.242 ± 0.061° is claimed to follow from Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°). Recomputing the inverse-variance weighted average:  

- Weights: w₁ = 1/0.11² ≈ 82.64, w₂ = 1/0.074² ≈ 182.64 ⇒ w₁ + w₂ ≈ 265.28  
- Weighted mean: (0.30×82.64 + 0.215×182.64)/(265.28) ≈ 0.240°  
- Combined σ: 1/√(w₁ + w₂) ≈ 0.061°  

The quoted mean 0.242° differs slightly from the recomputed 0.240°, small but non-zero given the precision claimed (three decimals, and used to argue natural agreement).  
Required fix: Either (a) recompute carefully and update Eq. (4) to βcombined = 0.240 ± 0.061° or (b) explain if slightly different inputs (e.g. more precise underlying numbers or a correlation treatment) were used. Quote all inputs and rounding choices consistently so that the reader can reproduce the combination to the quoted precision.

---

P2-E5  
Section: Sec. 3.2 and Sec. 3.4, p.3  
Problem: The quoted significance “(3.9σ from zero)” and Bayes factor ln B = 5.17 are not reproducible from the displayed numbers and assumptions. For a Gaussian posterior centered at β = 0.242° with σ = 0.061°, the naive z-score is 0.242/0.061 ≈ 3.97, consistent with “3.9σ,” but the Bayes factor value 5.17 for a flat prior β ∈ [0°,1°] via Savage–Dickey is not derivable from any explicit posterior density at β = 0; the posterior density at zero is not given, no normalization constant is shown, and the prior is only loosely specified. Without seeing the actual likelihood evaluated at β = 0 or a numerical check, the reader cannot verify ln B = 5.17 or its prior dependence.  
Required fix: Provide either (a) the explicit formula and numerical inputs used for the Savage–Dickey ratio, including the posterior density at β = 0 and the normalization, or (b) a concise description of the sampling-based procedure and posterior histograms from which ln B is inferred. Alternatively, drop the Bayes factor claim from the main text or weaken it to a qualitative statement unless it can be reproduced from the material given.

---

P2-E6  
Section: Sec. 2.2, p.2  
Problem: Dimensional inconsistency and possible misstatement of Eq. (2). The Lagrangian coupling is \( \mathcal{L} \supset -\frac{1}{4} g_{a\gamma} \phi F\tilde F\), with standard convention \(g_{a\gamma} = \frac{\alpha_{\rm EM} C_{a\gamma}}{2\pi f_a}\). The birefringence rotation is typically \(\beta = \frac{1}{2} g_{a\gamma} \Delta\phi\). The text states:

\[
\beta = \frac{g_{a\gamma}}{2} \Delta\phi = \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi f_a} \Delta\phi
\]

but then uses \(g_{a\gamma} = \alpha_{\rm EM} C_{a\gamma}/(2\pi f_a)\). Combining both, the second equality is missing a factor of 1/2: \(\beta = \frac{g_{a\gamma}}{2}\Delta\phi = \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi f_a} \Delta\phi\) only if \(g_{a\gamma}\) is as stated; otherwise, it becomes \(\frac{\alpha_{\rm EM} C_{a\gamma}}{8\pi f_a}\Delta\phi\). There is an inconsistency between text and standard conventions, which directly affects the numerical prediction β ≈ 0.29°.  
Required fix: Clarify the precise definition of \(g_{a\gamma}\) and check Eq. (2) for the correct numerical factor. Ensure consistency with the standard ALP-photon coupling conventions in the literature (e.g. Fujita et al., Namikawa et al.). Recompute the fiducial β value if the effective factor changes.

---

P2-E7  
Section: Sec. 2.2, p.2  
Problem: Numerical mismatch in the explicit β calculation. Using the expression in the text:  

- α_EM ≈ 1/137 ≈ 0.007299  
- 4π ≈ 12.566, so α_EM × 8 / (4π) ≈ (0.007299×8)/12.566 ≈ 0.00466 (dimensionless radians).  
- Multiply by ∆ϕ/fa ≈ 1.07: β ≈ 0.00499 rad ≈ 0.286°.

However, this assumes the second equality in Eq. (2) is correct; if the factor of 1/2 is misapplied (see P2-E6), β would be ≈0.143°. The paper states β ≈ 0.29° without showing the intermediate steps, and the internal consistency depends sensitively on the factor-of-two convention.  
Required fix: Show the explicit numerical evaluation leading from Eq. (2) to β ≈ 0.29°, including whether β is defined in radians or degrees in that equation, and confirm all factors of 2 and π. If the correct convention yields a different value, update the quoted prediction accordingly.

---

P2-E8  
Section: Sec. 5, Eq. (11), p.4–5  
Problem: The derivation of the energy density and Ωϕ is not shown, and the numbers given are not obviously consistent. Eq. (11) is written as

\[
\rho_\phi(z=0) \approx \frac{1}{2} m^2 f_a^2 \theta_i^2 \Rightarrow \Omega_\phi(z=0) \approx \left(\frac{m}{H_0}\right)^2 \left(\frac{f_a}{M_{\rm Pl}}\right)^2 \theta_i^2,
\]

up to the ambiguous “1/6” and brackets in the text. The following sentence states that for \(f_a \sim M_{\rm Pl}\), \(m \sim H_0\), and \(\theta_i \sim 1\), this gives \(\Omega_\phi \sim 0.17\). Yet, with the schematic scaling just given, \(\Omega_\phi \sim O(1)\) for those parameter values, not 0.17, unless an additional numerical factor (~0.4) is introduced. The text mentions “1/6” but does not derive it, and the final 0.17 value is not traceable.  
Required fix: Provide the full derivation of Eq. (11), including all numerical coefficients and the assumptions about the background critical density. Explicitly show how 0.17 is obtained for the fiducial parameters. This is central to the “spectator vs dark-energy-like” discussion, so hand-waving factors are not acceptable for PRD.

---

P2-E9  
Section: Sec. 5, p.5  
Problem: The “companion Paper I(a) [?]” is cited as the source for characterizing the misalignment tuning as “cosmological-constant-class” and for a “14-barrier catalog” in Sec. 6, yet no bibliographic details are given. The label “Paper I(a)” is an internal version-history tag, not a journal- or arXiv-style reference, and may refer to a manuscript not yet publicly available (“companion paper”). PRD does not usually allow crucial theoretical context or claims about tuning to rest on inaccessible or undefined companion works.  
Required fix: Replace “Paper I(a)” and “companion paper” with full references to publicly accessible documents (arXiv IDs or journal entries). If these works are not yet on arXiv or published, either (a) post them and cite properly, or (b) remove any reliance on them as authority and provide the necessary derivations/arguments within the present paper.

---

P2-E10  
Section: Sec. 6, p.5–6  
Problem: The ECH gravity and “14-barrier catalog” language references a “companion paper [?]” that is crucial for justifying the fa ∼ MPl motivation. No details (title, arXiv ID, journal) are supplied, and “14-barrier catalog” reads like an internal project label rather than a stable literature reference. This is exactly the kind of internal-bookkeeping placeholder the instructions warn against.  
Required fix: Provide a proper citation (or citations) for the ECH framework and “14-barrier catalog”, including author list, title, and arXiv ID or journal reference. If no such paper exists in the public literature, the language “companion paper” and “14-barrier catalog” must be removed or rewritten as speculative motivation, clearly separated from claims based on established literature.

---

P2-E11  
Section: Sec. 1–8, all pages  
Problem: Multiple claims of naturalness and lack of fine-tuning (“no fine-tuning”, “natural prediction”, “no fine-tuning of dimensionless parameters”) rest on comparisons to prior literature (e.g. Fujita et al., Namikawa et al.). However, because the actual references are missing and cannot be checked, it is currently impossible to verify that the claimed novelty and parameter choice (fa ∼ MPl, m ∼ H0, β ≈ 0.27°) is not already explicitly identified in those works or others. Claims of novelty (“Our contribution is not the model itself, but rather the specific parameter identification...”) must be checked against the existing ALP birefringence literature, which cannot be done in the present state.  
Required fix: Supply the full references, and then explicitly demonstrate—by comparing to the cited works—that the specific combination (fa ∼ MPl, m ∼ H0, and the exact β prediction with natural θi, C0) has not already been highlighted elsewhere. If related works already made very similar claims, the novelty must be carefully downgraded and properly attributed.

---

P2-M1  
Section: Abstract & Sec. 1, p.1  
Problem: Incomplete and somewhat misleading summary of existing measurements. The introductory sentence “The Planck HFI analysis [?] reported β = 0.35 ± 0.14◦ (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.” is not accompanied by explicit references or a quantitative combination. Without the reference list, one cannot check if the “combined evidence exceeds 3.5σ” is a re-analysis or simply a heuristic statement.  
Required fix: Once the citations are supplied, verify that the combination of the published Planck and ACT measurements actually exceeds 3.5σ using those works’ quoted values, and indicate precisely which datasets and methods are included. If the 3.5σ claim is based on the Eskilt joint analysis rather than an independent combination, say so clearly.

---

P2-M2  
Section: Sec. 3.3, Table 1, p.3  
Problem: MCMC configuration table lists very small sample sizes (720–6,840 accepted samples) and then claims “The Gelman-Rubin convergence diagnostic R̂ − 1 < 0.01 confirms adequate mixing.” While the authors acknowledge the modest sample sizes, they nevertheless proceed to quote posterior means and errors to three significant figures and use them to argue consistency and to estimate the Bayes factor. These chains are below standard cosmology practice for robust evidence calculations and tail behavior.  
Required fix: Either extend the MCMC analyses to obtain O(50,000) effective samples per run and recompute posteriors and Bayes factors, or scale back the quantitative claims based on these chains (especially about evidence and tail probabilities), explicitly marking them as preliminary. Numerical results quoted to high precision should be supported by adequately converged chains.

---

P2-M3  
Section: Sec. 3.3, Eqs. (6)–(8), p.3  
Problem: The posterior mean and uncertainty for βALP = 0.336 ± 0.107° and βfree = 0.344 ± 0.096° and Caγ × θi = 3.4 ± 1.1 are presented without any display of the posterior histograms or tables from which they are derived. With such small chain lengths and the absence of a reference to a public chain or code, there is no way to confirm that these numbers are not dominated by sampling noise or prior volume effects.  
Required fix: Provide either (a) a figure showing the posterior distributions with overplotted means and standard deviations, or (b) a brief quantitative summary of effective sample sizes, autocorrelation times, and robustness checks (e.g. varying starting points, splitting chains). For PRD, MCMC-inference claims need at least minimal reproducibility and robustness evidence.

---

P2-M4  
Section: Sec. 4, Eq. (10), p.4  
Problem: The forecast significance is quoted as exactly 9σ from β = 0.27° and σ(β) = 0.03°. This is straightforward (0.27/0.03 = 9), but the text elsewhere notes that LiteBIRD’s σ(β) depends on self-calibration and systematics, and the LiteBIRD reference itself is only “[?]”. Without the specific forecast paper, one cannot verify σ(β) = 0.03° is indeed the correct benchmark for isotropic birefringence in the presence of realistic systematics.  
Required fix: Provide the LiteBIRD forecast reference, confirm that σ(β) ≈ 0.03° is quoted there (and under what assumptions), and clarify in the text that 9σ is based on statistical sensitivity only, ignoring systematic floors.

---

P2-M5  
Section: Sec. 7, p.5–6  
Problem: “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [?].” The specific value fNL = −35/8 appears without any derivation in the present paper, and the reference is only “[?]”. For such a precise, load-bearing number (exact fraction), it is essential to verify that it is correctly taken from the cited work and that the conditions (shape, convention, scale) match.  
Required fix: Supply the citation from which fNL = −35/8 is taken, and specify whether this is the local, equilateral, or another shape and under what assumptions. If this value is derived in the companion bounce cosmology paper, then that derivation must be either given here briefly or properly referenced to a publicly accessible document.

---

P2-M6  
Section: Sec. 7, p.5–6  
Problem: The statement “We emphasize that the ALP birefringence model class is well-studied in the literature [?]. Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3◦ , and Namikawa, Murai & Naokawa [?] provide superior ALP mass constraints using the full Planck EB spectrum.” cannot be verified: the Fujita et al. and Namikawa et al. papers are not fully cited. It is impossible to confirm whether they indeed use fa ∼ MPl, whether their β ≈ 0.3° prediction matches the one here, or whether their mass constraints are as described.  
Required fix: Provide full citation details for these papers and ensure that the claims about what they “already demonstrated” are accurate and not overstated. If Fujita et al. already emphasized essentially the same parameter identification, the novelty of the present paper must be reframed.

---

P2-M7  
Section: Abstract & Sec. 7, p.1, 5–6  
Problem: Claim of “no fine-tuning” and “order-unity, no fine-tuning” for C0 and θi is in tension with Sec. 5, which admits a ∼25× tuning of θi (to ~0.22) to maintain Ωϕ ≪ 1 in the “spectator” regime. While the text attempts to classify this as “cosmological-constant-class tuning” and not “ALP-specific”, from the perspective of the model, the initial misalignment is indeed tuned relative to an O(1) prior. The abstract’s unqualified “no fine-tuning” is therefore misleading.  
Required fix: Reconcile the language: either remove “no fine-tuning” from the abstract or explicitly qualify it to say that dimensionless couplings are order unity but the initial misalignment requires a ~25× tuning if one insists on Ωϕ ≪ 1. PRD will expect honest and transparent language about tuning.

---

P2-M8  
Section: Sec. 1 & Sec. 2.1, p.1–2  
Problem: Repetition and redundancy: “For m ∼ H0 and fa ∼ MPl , the field is frozen during radiation and matter domination (Hubble friction exceeds the mass) and begins rolling at z ∼ O(1) when H(z) ∼ m.” appears essentially twice (once in Sec. 2.1 narrative, once just above Eq. (1)), nearly verbatim. While not severe, it suggests the manuscript could be tightened.  
Required fix: Remove redundant sentences and streamline Sec. 2.1 to state the background evolution and onset of rolling once, clearly.

---

P2-M9  
Section: Overall length vs contribution, all pages  
Problem: The paper is 7 pages, focused on a single-parameter minimal ALP birefringence prediction, a two-point summary-likelihood combination, and a fairly minimal MCMC check. Much of the later discussion section is qualitative and could be shorter. Given the modest methodological novelty (once the references are properly accounted for), the paper feels somewhat verbose for its actual technical content.  
Required fix: Consider trimming non-essential motivational prose, especially in Sec. 6–7, and focusing on the concrete calculation, inference, and the spectator-energy-density constraint. A 5-page manuscript should suffice for the claimed contribution once redundancy and speculative ECH discussion are reduced.

---

P2-N1  
Section: Title page, p.1  
Problem: The affiliation is given as “Independent Researcher, Los Angeles, California, USA” and an email address “houston@hubify.com”. While not inherently problematic, PRD typically expects stable institutional affiliations or a clear statement that the author is unaffiliated. This is more editorial than scientific.  
Required fix: Ensure that the contact information matches the submission metadata and that any institutional affiliation (if any) is correctly stated. If “Independent Researcher” is the intended affiliation, this is acceptable but should be consistent across the submission.

---

P2-N2  
Section: Acknowledgments, p.7  
Problem: The author notes “The author acknowledges the use of AI research assistants during the analysis and manuscript preparation.” This is good practice but somewhat vague; PRD may require more detail (e.g. which tools and for which tasks) depending on evolving policies.  
Required fix: If the journal requires it, specify briefly what types of assistance were provided (e.g. code debugging, language editing) and confirm that all scientific judgments and derivations have been checked independently by the author.

---

P2-N3  
Section: Typesetting, throughout  
Problem: Occasional typographical oddities: “mθ ∼ H0” (likely “m ∼ H0”), “14-barrier catalog” (term unexplained), and some spacing issues around parentheses and hyphens. These do not affect scientific content but detract slightly from readability.  
Required fix: Carefully proofread the manuscript for typographical errors, especially around variable names and hyphenation, and correct “mθ ∼ H0” if it is not intentional.

---

## Summary recommendation

REJECT

In its current form, the manuscript lacks a complete and verifiable bibliography, relies on multiple unresolved “[?]” placeholders, contains at least one likely factor-of-two inconsistency in a central formula, and presents key numerical claims (energy density, Bayes factor, effective coupling) without sufficient derivation or reproducibility. The combination of incomplete citation metadata, internal-bookkeeping references to non-public “companion” papers, and underpowered MCMC/evidence calculations falls short of PRD’s standards. Substantial restructuring, full citation repair, and more rigorous numerical support are required; this goes beyond “major revisions” and effectively constitutes a new, more carefully documented submission.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E12  
Section: Abstract & Sec. 2.2 vs Sec. 5, pp.1–2, 4–5  
Problem: The abstract and Sec. 2.2 motivate the prediction β ≈ 0.27° assuming **order‑unity** θi and C0, but Sec. 5 later adopts θi ≈ 0.22 (a ∼25× tuning relative to θi ∼ 1) to satisfy the spectator condition, while simultaneously claiming “the β ∼ 0.27° prediction continues to hold by the cancellation above.” This is not internally consistent: β ∝ θi (for fixed C0 and m/H0), so if θi is reduced by a factor ≈0.22 while keeping C0 and F(m/H0) fixed, β must drop by the same factor unless C0 or m/H0 are changed correspondingly. No such compensating change or recalculation is shown.  
Required fix: Either (a) explicitly recompute β for the spectator choice θi ≈ 0.22, showing the required adjustment of C0 and/or m/H0 to recover β ≈ 0.27°, or (b) clearly state that the “β ≈ 0.27° with θi ∼ 1” prediction corresponds to the dark‑energy‑like regime Ωϕ ∼ 0.17, and that in the strict spectator regime the predicted β is reduced unless parameters are adjusted away from the “order‑unity” benchmark. The abstract’s “order‑unity θi ∼ O(1)” claim must be reconciled quantitatively with the later θi ≈ 0.22 choice.

---

P2-E13  
Section: Abstract & Sec. 3.2, pp.1–3  
Problem: The abstract claims “finding β = 0.242 ± 0.061° (3.9σ from zero) with an effective photon coupling fphoton × C0 = 1.73 ± 0.44,” but the text never defines **fphoton** or shows how this dimensionless number is obtained from βcombined and the ALP parameters. Eq. (5) simply states the result without connecting it to Eq. (2)’s gaγ, Caγ, or to any explicit choice of units. This goes beyond the earlier issue of definition (P2‑E3): it is impossible to recompute 1.73 ± 0.44 from any displayed inputs, so the number is arithmetically opaque as well as conceptually undefined.  
Required fix: Provide the explicit formula for fphoton × C0 in terms of β, θi, m/H0 (via F), and αEM (including units), then show the numerical evaluation that leads to 1.73 ± 0.44 using the βcombined constraint. Make clear whether fphoton has dimensions of energy, inverse energy, or is made dimensionless by factoring out MPl or H0.

---

P2-E14  
Section: Sec. 3.1–3.2 & Abstract, pp.1–3  
Problem: The paper uses three different β values without clearly separating their roles: Planck NPIPE (0.30 ± 0.11°), ACT DR6 (0.215 ± 0.074°), and Eskilt joint (0.342 ± 0.094°). The combined summary‑likelihood result βcombined = 0.242 ± 0.061° is based on NPIPE+ACT, but most qualitative statements about “consistency with the 3.6σ signal” refer to the Eskilt value. The abstract’s opening statement refers directly to the Eskilt 0.342° value as the “3.6σ signal,” whereas the combined summary‑likelihood number 0.242° and the MCMC posteriors (0.336°, 0.344°) are used later. These σ values arise from different likelihood constructions and are implicitly treated as interchangeable.  
Required fix: Clearly state which σ and β values are derived from which null procedures (summary two‑point combination vs full EB spectrum fit), and explicitly warn the reader that the 3.6σ Eskilt result is not directly comparable to the 3.9σ derived here from a different combination and dataset subset. When juxtaposing significances, specify the underlying likelihood and data so that the reader does not interpret them as a single coherent measurement.

---

P2-E15  
Section: Sec. 2.2, Eq. (2), p.2  
Problem: Beyond the factor‑of‑two inconsistency already flagged, there is a **dimension/normalization ambiguity**: Eq. (2) writes β = gaγ/2 ∆ϕ = αEM Caγ/(4π fa) ∆ϕ, but later numerical evaluation uses β = (αEM × 8/4π) × (∆ϕ/fa) without making clear whether β is in radians or degrees in Eq. (2), and whether ∆ϕ is measured in units of fa. The sentence “yielding β = (αEM × 8/4π) × 1.07 ≈ 0.29°” implicitly treats αEM×8/(4π)×1.07 as a pure number in degrees, which is not standard: the formula as written produces β in **radians** if gaγ has its usual mass dimension and ∆ϕ is in field units. The conversion to degrees is not shown, and the text never states the units of β in Eq. (2), only in later prose.  
Required fix: Explicitly specify that Eq. (2) yields β in radians, then show the rad→deg conversion in the worked example, including all intermediate steps. Clearly state whether ∆ϕ in Eq. (2) is dimensional or already rescaled by fa, and ensure that the numerical example uses a consistent convention.

---

P2-E16  
Section: Sec. 2.2, “prediction spans β ≈ 0.17–0.43°”, p.2  
Problem: The quoted range β ≈ 0.17–0.43° is stated for m/H0 ∈ [1,3], θi ∈ [0.5,2], Caγ ∈ [4,12], but no explicit mapping between these ranges and the quoted β interval is given. Because the field response F(m/H0) is not shown and the dependence on θi and Caγ is linear, a wide range of β values is possible; it is unclear whether 0.17–0.43° corresponds to extremal combinations (e.g. Caγ = 4, θi = 0.5, smallest F; Caγ = 12, θi = 2, largest F) or to some more restricted region. Without at least one explicit example or table, the stated “comfortably bracketing” claim cannot be verified.  
Required fix: Provide either a small table or a figure showing β as a function of (m/H0, θi, Caγ), or at minimum give explicit parameter triplets that generate the quoted endpoints 0.17° and 0.43°. Clarify whether these are true extrema over the stated ranges or representative values.

---

P2-E17  
Section: Sec. 3.3–3.4 vs Fig. 1 & Fig. 2 captions, p.3–4  
Problem: The body text references a “triangle plot from the extended ALP MCMC (Run 2, C free)” and “comparison of β posteriors across all three model configurations” with quoted means and uncertainties, but the captions do not specify the chain lengths, burn‑in, or binning used, nor do they indicate whether the posteriors are marginalized over all other parameters. This lack of detail makes it impossible to assess whether the graphical posteriors are consistent with the numerical summaries (Eqs. 6–8 and 9). The captions also do not state whether the plotted β in Fig. 2 is the same β parameter as in the Gaussian summary‑likelihood (Eq. 4), potentially confusing readers about comparability.  
Required fix: Expand the figure captions to state (a) that the posteriors shown are fully marginalized one‑dimensional distributions, (b) that they are derived from the chains described in Table 1 with the indicated sample sizes and priors, and (c) whether β in Fig. 2 corresponds exactly to the β parameter in Eq. (4) or differs (e.g. ALP‑predicted β vs free β). Ensure that the plotted means/intervals match the numerical values quoted in the text.

---

P2-E18  
Section: Abstract vs Sec. 7 & Sec. 8, pp.1, 5–6  
Problem: The abstract describes the Bayes factor ln B = 5.17 as “indicative; prior‑dependent, see Sec. 3.4,” but the Conclusion omits this qualification, stating only that “LiteBIRD will provide a decisive test at ∼ 9σ statistical significance” and summarizing the model as requiring “no fine-tuning of dimensionless parameters” without revisiting the Bayesian evidence’s prior dependence or the misalignment tuning. There is an implicit shift from a nuanced, qualified statement in the main text to a more categorical take‑home message, which overstates the robustness of the evidence and underplays the admitted tuning.  
Required fix: Align the Conclusion’s language with the more cautious statements in Sec. 3.4 and Sec. 5, explicitly noting that the reported ln B values are prior‑dependent and that the spectator‑regime implementation of the model does require a ∼25× tuning of θi if Ωϕ ≪ 1 is enforced. PRD expects the conclusion to reflect the caveats emphasized in the body.

---

P2-M10  
Section: Sec. 1 & Sec. 7, pp.1, 5–6  
Problem: The paper claims “The prediction matches the combined Planck + ACT measurement at 1σ” (Sec. 7), but the only explicit combined constraint shown is βcombined = 0.242 ± 0.061° from Planck NPIPE + ACT DR6. The fiducial prediction β ≈ 0.27° differs from 0.242° by 0.028°, which is ≈0.46σ, consistent with “within 1σ.” However, earlier in the Introduction the observational baseline is described as “the 3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis),” for which the same β ≈ 0.27° prediction is ≈0.77σ below the mean. The text never clearly states which observational reference it is using for the “matches … at 1σ” claim, and by switching between 0.342° and 0.242° without explicit mention, it risks giving the impression that the prediction is simultaneously “1σ‑close” to both.  
Required fix: Specify explicitly which dataset/combination is being used for the “matches at 1σ” statement (e.g. βcombined vs βobs), and provide the numerical offset in σ units. If both the Eskilt joint result and the NPIPE+ACT summary combination are considered, report both residuals (e.g. 0.8σ and 0.5σ) so that “within 1σ” is not used in a way that conflates distinct reference points.

---

P2-M11  
Section: Sec. 3.3, Table 1 & text, p.3  
Problem: The text states “small effective sample sizes (Neff ∼ 1,000)” but does not specify for which runs or parameters this estimate applies, and Table 1 only lists the raw numbers of accepted samples, not Neff. Given that Run 3 has only 720 accepted samples total, an Neff ∼ 1,000 cannot apply uniformly; the wording could be interpreted as implying adequate effective sample sizes across all runs, which is not supported.  
Required fix: Clarify the effective sample size per run and per key parameter (e.g. β, Caγ, θi) and adjust the text to avoid implying Neff ∼ 1,000 where the chain length itself is smaller. If only Runs 1–2 reach Neff ∼ 1,000 for β, state this explicitly and qualify any claims for Run 3.

---

P2-M12  
Section: Sec. 7, p.5–6  
Problem: The statement “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency” is not backed by any explicit, quantitative comparison to prior ALP birefringence works. The text mentions Fujita et al. and Namikawa et al. as having already studied Planck‑scale ALPs and used full Planck EB spectra, and acknowledges that the ALP birefringence model class is well‑studied, but does not show that the particular combination (fa ∼ MPl, m ∼ H0, β ≈ 0.27° with θi, C0 ∼ 1) was *not* previously highlighted. This is a residual novelty‑claim issue beyond the missing references already flagged: even once references are supplied, the manuscript needs to demonstrate that its self‑described contribution is indeed incremental and not redundant.  
Required fix: After adding full citations, include a short subsection or paragraph explicitly comparing the present parameter identification and inference approach with those of Fujita et al., Namikawa et al., and other key works. If those works already discuss fa ∼ MPl and m ∼ H0 leading to β ~ few×0.1°, adjust the claimed novelty accordingly (e.g. emphasize the specific energy‑density discussion or LiteBIRD forecast rather than “the specific parameter identification”).

---

P2-M13  
Section: Acknowledgments, p.7  
Problem: The author notes the “use of AI research assistants during the analysis and manuscript preparation” but does not specify whether any numerical results (e.g. MCMC chains, likelihood codes) were generated or checked using AI‑written code. Given the central role of relatively complex MCMC and Bayesian calculations, this could be relevant for reproducibility and error‑tracing if mistakes are later found.  
Required fix: Briefly clarify whether AI assistance was limited to literature search and language editing, or whether it extended to code generation, data analysis scripts, or figure production. If AI‑generated code was used, state that all scientific results have been independently validated by the author through separate checks.