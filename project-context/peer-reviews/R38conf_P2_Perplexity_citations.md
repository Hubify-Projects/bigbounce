# P2 R38conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.61.pdf` md5=6b413c94 pages=27
**Input format**: TEXT + web search + pass-2 self-critique (14843 chars)
**Wall time**: 86.8s

---

I cannot see or search the actual PDF of this submission; I only have the text block you provided. That means I cannot:  
- verify page numbers or figure/table positions in the rendered PDF,  
- see whether any LaTeX compiled incorrectly,  
- inspect actual reference formatting (journal abbreviations, volume, page) beyond what is explicitly written, or  
- follow links to the claimed GitHub/Zenodo artifacts.

Within those limitations, I will treat the pasted text as if it is the full manuscript content and audit it accordingly. I will *not* judge scientific correctness of the cosmology; I focus on citation forensics, internal numeric consistency, formal issues, and PRD-level standards.

Below I list findings, each tagged with severity and location using the paper’s own sectioning and the implicit page order of the paste (I approximate pages; you will need to map them to actual PDF pages).

---

### P2-E1 — ESSENTIAL  
**Location:** Abstract, first paragraph (top of p.1)  
**Problem:** The Planck slow-roll “benchmark” and ratio are numerically inconsistent with the standard Maldacena relation.  

Text:  
> “the slow-roll value \(f_{\rm NL}^{\rm inf} \approx 0.015\) at \(n_s = 0.9649\) [2,3] gives a contrast \(|f_{\rm NL}^{\rm bounce}|/|f_{\rm NL}^{\rm inf}| \approx 290\).”

From Maldacena for local-type in the CMB gauge frame:  
\(f_{\rm NL}^{\rm local} = \frac{5}{12}(1 - n_s)\). With Planck 2018 \(n_s = 0.9649\),  
\(1 - n_s = 0.0351\),  
\(\frac{5}{12}(1-n_s) \approx 0.014625\).  

So \(f_{\rm NL}^{\rm inf} \approx 0.0146\), not 0.015 exactly, and the ratio  
\(|-35/8| / 0.014625 \approx 4.375 / 0.014625 \approx 299\), not 290.  

This paper elsewhere states 290 again (Sec. X):  
> “the Maldecena consistency relation gives \(f_{\rm NL}^{\rm inf,gauge} = -\frac{5}{12}(n_s -1)\approx 0.015\)… the bounce-vs-inflation gauge-frame amplitude ratio is therefore… \(\approx 290\).”

**Required fix:**  
- Either recompute and state the correct ratio (≈300) or state explicitly which rounded value of \(f_{\rm NL}^{\rm inf}\) is used and adjust the quoted ratio consistently throughout the paper.  
- For PRD, you should show at least one explicit calculation in the main body (perhaps in Sec. I) confirming the numerical relationship, and ensure every occurrence of this ratio is updated (abstract, introduction, conclusion).

---

### P2-E2 — ESSENTIAL  
**Location:** Abstract, first paragraph; repeated later in Sec. X  
**Problem:** Gauge-frame vs physical-frame (CFC) language is muddled at the level of observable vs theoretical discriminator, and risks misleading a PRD reader about what is actually measured.  

Text in abstract:  
> “in the conformal-Fermi physical-observer frame the squeezed-limit consistency relation [4,5] sends \(f_{\rm NL}^{\rm local} \to 0\) for single-field slow-roll, so a non-zero physical-frame local detection … would disfavor the single-field slow-roll attractor. The forecast estimators measure the gauge-frame \(f_{\rm NL}\) directly; the CFC statement is a complementary theoretical discriminator, not the on-sky observable.”

Later in Sec. X:  
> “We retain the gauge-frame ∼ 290× ratio as the bounce-vs-inflation discriminator for the survey forecast, and confine the physical-frame statement to its proper role…”

The text moves back and forth but never gives a clean, explicit, *repeated* caveat at every place where gauge-frame and physical-frame \(f_{\rm NL}\) are juxtaposed (a requirement in your instructions point 7). In several places the two are effectively compared without an immediate “not directly comparable” flag.

**Required fix:**  
- At *every* place where a physical-frame (CFC) statement is put next to gauge-frame forecasts, explicitly declare that the two are not numerically comparable and that only the gauge-frame parameter is forecasted.  
- For PRD, add a short, separate subsection (e.g. “Gauge vs physical frame \(f_{\rm NL}\)”) with clean definitions and a statement that *all numerical* forecasts refer to the Planck/local-template gauge convention. Then cross-reference that subsection in the abstract and conclusion sentences about CFC to avoid any impression that CFC-level statements are being observationally forecast.

---

### P2-E3 — ESSENTIAL  
**Location:** Abstract and Sec. IV/V, all “σ” headline ranges  
**Problem:** Different σ-values from distinct null procedures (Heinrich bispectrum-only Fisher; combined Fisher; additional heuristic “GR budget” σGR; bϕ prior widening) are juxtaposed without an explicit “not directly comparable” caveat at each juxtaposition, contrary to instruction 7.  

Examples:  
- Abstract:  
  > “After template-mismatch correction we obtain bispectrum-only 5.2–5.5σ at \(f_{\rm NL}=-35/8\)… reducing to a realistic ∼ 2.6–5σ after the systematic budget… These systematics are combined additively in quadrature… We adopt the bispectrum-only 5.2–5.5σ optimistic and 2.6–5σ realistic ranges as the headline forecast.”  

- Sec. IV and Table IV mix:  
  - σ(fNL)=0.7 from Heinrich (Fisher),  
  - σGR added “in quadrature” as a free, non-Fisher nuisance,  
  - bϕ priors simply widening σ by ad hoc factors.  

These are heterogeneous procedures; combining them into a single “headline” σ range makes those σ-values appear comparable, which they are not in any single well-defined likelihood. For PRD, you either give one consistent, clearly defined likelihood/Fisher treatment, or you label each σ strictly as arising from separate approximations.

**Required fix:**  
- Recast the systematics section so that:  
  - There is a clearly defined *baseline* σ from the Heinrich Fisher matrix.  
  - Each subsequent σ-degradation (template mismatch, bϕ, GR) is presented as a separate sensitivity study, *not* as a combined, pseudo-Fisher uncertainty unless you actually build a joint Fisher or likelihood.  
- Wherever you quote 2.6–5σ as a “headline” range, qualify that these are approximate, not directly comparable σ-values from different heuristic combinations, and clearly state which combinations are *not* rigorous.  
- Alternatively, perform an explicit joint Fisher marginalization including bϕ and a parametrized GR template. Without that, the paper should *not* present a combined σ or a single “headline” detection band.

---

### P2-E4 — ESSENTIAL  
**Location:** Abstract; Sec. VI; Tables II and III  
**Problem:** Bayes factors and priors are presented as if they constitute robust model-selection evidence, but they are strongly prior-driven, built on a simplified Gaussian likelihood, and several variants are mixed in the abstract without clear caveats.  

Abstract:  
> “a SPHEREx detection near \(f_{\rm NL} = -4.375\) favors the bounce over tuned multifield competitors at Bayes factor \(BF \approx 9\)… up to \(BF \approx 14\)… These Bayes factors should be read as illustrative… — not as definitive model-selection evidence…”

The caveat exists, but the wording “favors the bounce” plus the prominent numeric range in the abstract still oversells what is essentially a 1D Gaussian likelihood with hand-chosen prior widths, not a full survey-level Bayesian model comparison.

Issues:  
- The analytic BF formula (8) is correct *for a simple Gaussian likelihood* with flat competitor prior, but there is no explicit demonstration that such a likelihood is appropriate for the SPHEREx bispectrum estimator near |fNL|~few, especially under the various systematics.  
- The abstract headline BF range (≈9–14) assumes r≈0.84 bookkeeping and σtheory=1.0 for bounce prior, but the text then also explores σtheory=0.5,2.0 and delta priors. The abstract selects a subset of those results without clearly stating which prior choice is being used, or that other “reasonable” choices shift BF appreciably.  
- At PRD standards, any Bayesian claim in the abstract that looks like “BF ≈ 9” must be tied to a unique, clearly-stated prior; here the prior grid and hyperpriors are only fully described deep in Sec. VI, and *multiple* incompatible priors exist.

**Required fix:**  
- In the abstract, either *remove* the explicit numeric BF values, or rephrase to: “A simple 1D Gaussian likelihood with broad, ad hoc priors suggests that a detection at this level would moderately favor the bounce over tuned multifield competitors.”  
- If you keep BF values, specify explicitly in the abstract which single prior choice you are using (e.g., bounce prior Gaussian σtheory=1, multifield prior uniform on [−15,15]), and assert clearly that the numbers are highly prior-sensitive (as the body already shows).    
- Emphasize, in both abstract and conclusion, that these BFs are *illustrative* and *not* data-driven yet.  

---

### P2-E5 — ESSENTIAL  
**Location:** Abstract first line and Sec. II.A  
**Problem:** The claim “minimally parameterized” local non-Gaussianity is inconsistent with the later acknowledgement that there is a wide range in κϵ and c1–c6.  

Abstract:  
> “produces a minimally parameterized local-type non-Gaussianity \(f_{\rm NL}^{\rm local} = -35/8\)… in the scalar-only matter-bounce class defined by assumptions (a)–(f)… and (d) faithful third-order bispectrum transmission…”  

Sec. II:  
- You explicitly state κϵ has range 5.6–80 (order of magnitude, Sec. VIII).  
- You say “the prediction is more precisely described as minimally parameterized rather than strictly parameter-free.”  

But “minimally parameterized” in the abstract reads as if the cubic sector has no relevant unknowns. Given that you then introduce:  
- a wide κϵ range,  
- a 3D null space in c1–c6 giving ±0.13 in r,  
- and the unverified cubic-order bounce transmission,  
this is overstating the level of theoretical control.

**Required fix:**  
- In the abstract, add a qualifying clause such as: “produces a **leading-order** local-type non-Gaussianity \(f_{\rm NL}^{\rm local} = -35/8\), with a 1–8% correction from quasi-dust and polynomial null-space uncertainties discussed in the text.”  
- Remove “minimally parameterized” from the abstract or replace with “tightly constrained at leading order” or similar wording that does not imply a fully parameter-free prediction.

---

### P2-E6 — ESSENTIAL  
**Location:** Abstract, last paragraph of main abstract block  
**Problem:** The phrase “A SPHEREx null would disfavor the quasi-dust matter bounce benchmark at the same ∼ 2.6–5σ post-systematic-budget level as a detection (the exclusion arithmetic is symmetric)” is not backed by an explicit symmetric calculation and uses the same σ-band that is itself heuristic.  

To make such a statement at PRD level, you must:  
- Explicitly write the “null” measurement scenario (e.g., measured fNL=0 ± σeff) and compute the distance to −35/8 with the same σeff used for the detection case.  
- Show that the “realistic” σeff band is indeed symmetric in the mean (which may not hold once some systematics act non-linearly).  

Right now, this claim is asserted but not explicitly recomputed.

**Required fix:**  
- Add a short, explicit calculation in Sec. IV or VII: assume measured \(f_{\rm NL,obs}=0\) with each σeff listed in Table IV, and compute significance \(|f_{\rm NL}^{\rm bounce}|/σ_{\rm eff}\).  
- Confirm that this gives the same 2.6–5σ band; if it does not, state the correct band and update the abstract.  
- Make clear that this is a *forecast* statement only, and that the symmetry relies on linear Gaussian assumptions.

---

### P2-E7 — ESSENTIAL  
**Location:** Data & Code Availability section  
**Problem:** The GitHub path and Zenodo DOI are not checkable from the text as given; more importantly, **no versioning, commit hash, or tagged release IDs** are specified. This violates instruction 16 (provenance surfaces) and PRD’s standard for reproducibility.  

Text:  
> “All analysis code… are available at `https://github.com/Hubify-Projects/bigbounce/tree/main/research/` and archived at Zenodo (DOI inserted at submission).”

Issues:  
- No branch/tag/commit hash is frozen. Using `main` is not reproducible.  
- “DOI inserted at submission” is a placeholder. In a PRD-ready manuscript, the DOI must be actual, and the code version referenced must match the computations.  
- Internal filenames like `c9g bf table recompute.py`, `c9i epsilon ratio check.json` are mentioned, but no guarantee is given that these are unchanged post-submission.

**Required fix:**  
- Replace “tree/main” with a specific commit hash or tagged release name.  
- Insert the actual Zenodo DOI and ensure the Zenodo snapshot corresponds to that commit.  
- Add a sentence explicitly stating: “All figures and numerical results in this paper are generated from code and data in tag vX.Y.Z (Git commit ABCD...) archived under Zenodo DOI …”.  

---

### P2-E8 — ESSENTIAL  
**Location:** References [1]– scattered throughout; entire bibliography  
**Problem:** Citation forensics cannot be fully verified because only minimal metadata are given: no arXiv IDs, no journal volume/pages for most, and some in-text referencing appears inconsistent with the actual arXiv titles (where I can check).  

Given my constraints I can use general knowledge:

- [1] “E. Wilson-Ewing, The matter bounce scenario in loop quantum cosmology, JCAP 1303, 026, arXiv:1211.6269.”  
  This matches the real paper.  

- [10] Cai et al. 2009 “Non-gaussianity in a matter bounce, JCAP 0905, 011, arXiv:0903.0631” — correct.  

- [7] Li et al. 2016 arXiv:1612.02036 — title matches.  

- Heinrich et al. [6] “Measuring fNL with the SPHEREx multi-tracer redshift space bispectrum, Phys. Rev. D 109, 123511 (2024), arXiv:2311.13082” — appears correct.

But the bibliography as pasted omits arXiv IDs for many entries and uses descriptive text (“J. Cosmol. Astropart. Phys. (2024), DESI DR1 LRG combined PNG constraint; arXiv:2411.17623”) rather than standard PRD bibliographic format.

Also, some statistics claimed from references are not clearly traceable:

- For Planck NPIPE , you quote “fNL = −0.1 ± 5.0” and “Jung et al. (2025)”. This may be forward-looking: such a paper appears in 2025; you must ensure it exists and that those numbers are exactly as in its table.

- For DESI DR1 , , you quote specific central values and errors; those must be checked directly, but here I can only infer that you are anticipating DR1 2024–2025 releases.

**Required fix:**  
- For every reference, include full, standard PRD-format metadata: authors, journal, volume, page, year, and arXiv ID when available.  
- Double-check that every quoted number (Planck NPIPE fNL central value and σ, DESI LRG/QSO fNL values) matches exactly the published abstracts/tables. If any are from “accepted but unpublished” or “in prep” sources, clearly label them and avoid using them as foundational quantitative inputs.  
- Remove “future-dated” citations if the papers are not yet accepted or posted on arXiv at the time of submission. PRD will not accept references to hypothetical future works as sources of numerical constraints.

---

### P2-M1 — MAJOR  
**Location:** Repeated internal references to “artifacts” and filenames throughout (e.g., Sec. II footnote; Data & Code Availability)  
**Problem:** Numerous references to internal JSON files and scripts (“artifact c9i epsilon ratio check.json”, “null space analysis.py”, etc.) read like internal bookkeeping rather than publication-quality prose.  

Example:  
> “direct evaluation of those coefficients, or their in-in–doubled values, in our basis does not satisfy the three benchmark constraints; artifact c9i epsilon ratio check.json.”  

These look like internal development notes, not something intended for a PRD article.

**Required fix:**  
- Remove or rephrase all references to “artifact … .json” and internal script filenames from the main text. Such details belong in a README of the code repository, not in the physics narrative.  
- If you want to point to specific files for reproducibility, do so in the Data & Code Availability section only, and with neutral wording (“The coefficient mapping is implemented in file …”) rather than “artifact … .json”.

---

### P2-M2 — MAJOR  
**Location:** Multiple sections (II.B, II.C, VII.C, IX.D)  
**Problem:** Several qualitative claims of robustness (“dominant fragilities”, “suppressed”, “subdominant”) are made without explicit numerical thresholds or inequalities (Instruction 17 on uncomputed quantitative claims).  

Examples:  
- “projection noise is subdominant to the other systematics” with only 1−rcos^2 ~ 0.03–0.06 quoted, but without connecting this to the *total* σ budget.  
- “These effects are expected to degrade the forecast significance by an estimated O(10–30%)…” with no explicit numbers from a joint marginalization.  

**Required fix:**  
- For each such qualitative phrase, either:  
  - Attach a concrete inequality (e.g. “we find that including projection noise changes σ(fNL) by < 5% in all survey scenarios considered”), derived from an explicit computation, or  
  - Rephrase to a speculative statement clearly labeled as such: “we expect, based on order-of-magnitude arguments, that …; we do not include this in our σ budget.”  

---

### P2-M3 — MAJOR  
**Location:** Abstract and Sec. IV/V — “3–7σ envelope” for MegaMapper and “2.6–5σ” for SPHEREx  
**Problem:** For MegaMapper, the σ range is loosely justified and mixes design uncertainty with measurement uncertainty; for SPHEREx, you collapse multiple scenario-specific σ-values into a single “envelope” without clearly separating which are data-limited vs theory-limited vs design-limited.  

Example:  
> “MegaMapper… could reach σ(fNL) ≈ 0.5 ideally, projecting an illustrative 3–7σ envelope that reflects design uncertainty as much as measurement uncertainty.”  

You then reuse “3–7σ” at various points as though it were a meaningful quantitative band, but it’s essentially a guess based on scaling.  

**Required fix:**  
- For MegaMapper, explicitly mark all its forecast numbers as *illustrative* and remove them from any “headline” comparison. PRD will view forecasts for an unfunded, not-yet-designed facility as, at best, a side remark.  
- For SPHEREx, present a single, well-defined “baseline” σ (e.g., bispectrum-only, σ=0.7, with template mismatch applied), and relegate other σ-values to a separate “What-if” subsection clearly demarcated as sensitivity tests.

---

### P2-M4 — MAJOR  
**Location:** Sec. II.C (Assumptions), VIII.B (consistency relation)  
**Problem:** Claims of “UV-completion independence” and “mechanism independence” hinge critically on assumption (d) (faithful cubic-order transfer) and assumption (f) (negligible fermion torsion), which are not quantified.  

You correctly state:  
> “Assumption (d) … verified only at linear order [1] … the weakest link…”  
> “Assumption (f) … would require an explicit bound on ⟨ψ̄γ5γaψ⟩² … not undertaken here.”

Despite that, the abstract and conclusion use phrases like “robust across the bounce class” without repeating these caveats.

**Required fix:**  
- Every time you state anything like “robust across the [Wilson–Ewing] bounce class” (abstract, intro, conclusion), immediately remind the reader “conditional on (d) and (f)”.  
- In Sec. II.C, add a paragraph explicitly quantifying what level of violation of (d) and (f) would be needed to significantly alter fNL (even if only as an order-of-magnitude bound).  

---

### P2-M5 — MAJOR  
**Location:** Sec. II, details of P(k1,k2,k3), and matching to Cai et al.  
**Problem:** The polynomial reconstruction uses three benchmarks for six coefficients, and you assert that your chosen coefficients reproduce Cai’s Table I; however, you rely on internal verification scripts and do not show explicit analytic formulae or numerical values in the paper.  

For PRD, given that you are effectively re-deriving and extending Cai’s bispectrum representation, the reader should be able to verify the key steps without downloading code.

**Required fix:**  
- Provide the explicit expression for P(k1,k2,k3) with your chosen (c1,…,c6) in the main text or an appendix, and show a worked evaluation at the three benchmark triangles yielding the Cai values (numbers already in Table I).  
- Clarify precisely how your monomial basis differs from Cai’s Eq. 37 normalization and provide the mapping matrix explicitly, even if only symbolically.

---

### P2-N1 — NIT  
**Location:** Several places, including Sec. II footnotes and Data Availability  
**Problem:** Use of informal, chatty insertions (“notebook released with the paper’s code”, “artifact …”) makes the manuscript feel like a lab notebook rather than a polished PRD article.

**Required fix:**  
- Replace informal parentheticals with concise, formal sentences or move them to Data & Code Availability.  

---

### P2-N2 — NIT  
**Location:** Sec. X “X. CONCLUSION” and explicit “ACKNOWLEDGMENTS” with tooling mention  
**Problem:** You mention “AI-assisted software tooling (Anthropic Claude)” explicitly. PRD has not yet established a uniform policy, but many journals discourage naming specific LLM tools in Acknowledgments unless they had a major role.

**Required fix:**  
- Check PRD’s current policy; if necessary, remove or neutralize the mention (“we used automated code-generation tools for some scripts; all scientific results were independently checked by the author”).

---

### P2-N3 — NIT  
**Location:** Everywhere “Maldacena” sometimes mis-typed as “Maldecena”  
**Problem:** Typo in a key name.

**Required fix:**  
- Correct all instances of “Maldecena” to “Maldacena.”

---

### Length / scope comment  

The paper is very long and dense for what is fundamentally a *recast* of one SPHEREx forecast plus a prior-known bounce fNL prediction. There is significant space devoted to Bayesian grids and internal basis scans that may be more appropriate for a companion methods paper or an extended appendix. For PRD, I would recommend targeting ~20 pages main text, with the detailed Bayes-factor hyperparameter sweeps and null-space sampling moved to appendices or to the code repository.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The work is ambitious and technically detailed, but as submitted it does not meet PRD standards for clarity and rigor in its treatment of σ-values, Bayes factors, assumptions, and reproducibility metadata. The most serious issues are (i) mixing heterogeneous σ-definitions into single “headline” significance ranges, (ii) prior-sensitive Bayes factors being foregrounded in the abstract without a unique prior choice, and (iii) incomplete reproducibility/provenance details (no frozen code version). Addressing the essential and major points above would require substantial restructuring of the forecast presentation, explicit numerical cross-checks, and a tightened, less self-referential narrative.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E9 — ESSENTIAL  
**Class:** A (arithmetic), E (null‑procedure comparability), J (stale/inconsistent numbers)  
**Location:** Sec. VII.C, paragraph beginning “These effects are expected to degrade…”  

**Problem:** The paper asserts that unmodeled systematics “are expected to degrade the forecast significance by an estimated O(10–30%)” but never recomputes any σ or significance values including these extra effects, nor are these degradations integrated into Table IV’s “all‑combined” σeff. The only quantified degradations in Table IV are template mismatch, ϵ‑correction, bϕ, and GR; photo‑z outliers, integral constraint, magnification bias, nonlinear bias, etc. are only mentioned qualitatively. This creates an inconsistency: the text suggests an additional 10–30% loss beyond the listed budget, but all quoted “2.6–5σ” and “3–7σ” bands implicitly ignore that extra factor.

**Required fix:**  
- Either remove the “O(10–30%)” degradation claim or back it by explicit numbers: apply a 10% and 30% multiplicative degradation to the 2.6–5σ band and state the degraded range explicitly (e.g., 1.8–4.5σ).  
- Clarify in Table IV whether these additional systematics are included; if not included, explicitly say that Table IV is *exclusive* of these effects and that true end‑to‑end significance could be a further 10–30% lower.  
- Ensure the abstract and Sec. IX “2.6–5σ” and “3–7σ” phrases explicitly state whether they include or exclude these additional unmodeled systematics.


P2-E10 — ESSENTIAL  
**Class:** A (arithmetic), J (stale numbers)  
**Location:** Sec. II.B (quasi‑dust correction), Sec. VIII.B (consistency relation)  

**Problem:** The claimed 0.6–8% range for the ϵ‑correction appears inconsistent with the stated κϵ range and the quoted ∆ϵ. In Sec. VIII.B you give κϵ ∈ [5.6, 80] and |∆ϵ| ≈ 0.0045 from Planck ns; the implied shift in fNL is κϵ|∆ϵ| ∈ [0.025, 0.36]. Relative to |fNL| = 4.375 this is ≈ 0.6%–8.2%, in line with the stated 0.6–8%. But earlier in Sec. II you also state “At the Planck best‑fit ns = 0.9649, this gives fNL ∈ [−4.35, −4.02]” — a span ∆fNL ≈ 0.33, i.e. ≈ 7.5%, not obviously consistent with linking the low end to κϵ ≈ 5.6 only from explicit prefactors “giving a correction of ∼ 0.6%.” The derivation path (what exact ∆ϵ range is used for the 0.6% vs 8% endpoints) is never explicitly written and appears internally inconsistent.

**Required fix:**  
- Write the actual numerical steps: specify the ∆ϵ corresponding to ns = 0.9649, compute κϵ|∆ϵ| for the lower and upper κϵ endpoints, and explicitly show how these map to \(|f_{\rm NL}|\times(1\pm \delta)\).  
- Reconcile the “∼0.6% from explicit AT prefactor channel” wording with the lower bound of fNL ∈ [−4.35, −4.02]; if ~0.6% corresponds to κϵ = 5.6, show that explicitly; if not, adjust the text to correct quantitative values.  
- Ensure that every percentage range (0.6–8%, 1–8% elsewhere) and every fNL interval [−4.35, −4.02] is computed from the same ∆ϵ and κϵ numbers and is mutually consistent.


P2-E11 — ESSENTIAL  
**Class:** A (arithmetic), J (stale numbers)  
**Location:** Sec. III.B (projection noise), Sec. VII.A (“Dominant Fragilities”)  

**Problem:** The claim that “projection noise is subdominant to the other systematics” is justified by 1−rcos² ≈ 0.03–0.06, but this is never translated into a concrete impact on σ(fNL) or on the 5.2–5.5σ / 2.6–5σ bands. You state that “either bound confirms the projection noise is subdominant,” but “subdominant” is not quantified relative to, e.g., bϕ or GR. In Table IV, projection noise does not appear at all, so there is an implicit 0% assigned to it, contradicting the O(3–6%) shape mismatch implied by 1−rcos².

**Required fix:**  
- Provide an explicit inequality: for example, approximate how a 1−rcos² fraction of orthogonal‑shape variance would propagate into σ(fNL) (even under simplifying assumptions) and state a bound such as “σ(fNL) changes by < X% (X derived).”  
- Alternatively, explicitly state that projection noise is *not* propagated into Table IV and that the 2.6–5σ range neglects a potential additional O(≤Y%) uncertainty from this source.  
- Replace the qualitative “subdominant” phrasing with a quantitative upper bound tied to the numbers 0.03–0.06.


P2-E12 — ESSENTIAL  
**Class:** D (cross‑references), F (abstract faithfulness), E (null‑procedure comparability)  
**Location:** Abstract Bayes‑factor paragraph vs. Sec. VI and Table II  

**Problem:** The abstract says: “The analytic Bayes factor … is validated across three independent 10⁵‑realization Monte Carlo ensembles (§VI, Table II)…” and gives BF ≈ 9–14 headline numbers. Table II, however, is clearly computed with σeff = 0.7 (r→1 bookkeeping) and then the abstract applies a “noise‑weighted r ≈ 0.84 rebooking σeff = σ/r” to those entries. This means the BF values in the abstract and those in Table II do *not* come from a single, self‑consistent likelihood; they are related by a post‑hoc rescaling of σ. The internal referencing (“Table II reports the r→1 endpoint values while the abstract headline applies… rebooking σeff = σ/r to those entries”) is correct descriptively, but it obscures that two different null procedures (σ=0.7 vs σ=0.83 likelihoods) are being compared as if they were one result.

**Required fix:**  
- In §VI and in the abstract, explicitly label the r→1 and r≈0.84 cases as **separate likelihood assumptions** and state that the tabulated BFs (σ=0.7) and the “headline” BFs (σeff=0.7/0.84) are therefore not directly comparable outcomes of a single inference problem.  
- Either:  
  - Recompute Table II entirely for the σeff=σ/r case and present *those* as the main numbers (dropping the r→1 “endpoint” from the abstract), or  
  - Keep Table II as is, but move all rebooked BF numbers into the main text with a clear warning that they are heuristic rescalings, not distinct Bayesian computations.  
- Make sure the abstract sentence “Table II reports the r→1 endpoint values while the abstract headline applies…” is followed by an explicit “These should not be mixed as though they arose from a single consistent data model.”


P2-E13 — ESSENTIAL  
**Class:** C (dimensional consistency), D (cross‑references)  
**Location:** Eq. (3) and Eq. (4), scale‑dependent bias section  

**Problem:** The units and normalization of Eq. (3–4) are not fully explicit, and there is a mild inconsistency in the verbal description. You write “wavenumbers k are comoving and quoted in h Mpc⁻¹ throughout,” and M(k,z)=2k²T(k)D(z)/(3ΩₘH₀²). In standard conventions, if k is in h Mpc⁻¹ and H₀ in km s⁻¹ Mpc⁻¹, then the combination k²/H₀² requires explicit factors of c to be dimensionless; those are not written. Similarly, P(k) is never explicitly stated to be in comoving h⁻³ Mpc³, which is what makes Δ² dimensionless later in Eq. (7). You then use Δ²ζ(k) ≈ 2.1×10⁻⁹ without stating which k and normalization are assumed.

**Required fix:**  
- Explicitly state the unit system: e.g., “We work in units c=1 and express k and H₀ in the same units so that k²/H₀² is dimensionless,” or else carry the c factors explicitly in Eq. (4).  
- Clarify that Pζ and P(k) are taken in comoving units such that Δ²ζ(k) ≡ k³Pζ(k)/(2π²) is dimensionless, and specify the fiducial scale at which Δ²ζ ≈ 2.1×10⁻⁹ is evaluated.  
- Confirm that all occurrences of M(k,z), Δb, and Eq. (7) are dimensionally consistent under the stated unit conventions; if any hidden c or H₀ factors are required to fix dimensions, write them explicitly.


P2-E14 — ESSENTIAL  
**Class:** F (abstract faithfulness), A (arithmetic/comparability), E (null procedures)  
**Location:** Abstract first paragraph; Sec. I and Sec. II.B/C; Sec. X conclusion  

**Problem:** The abstract’s phrase “minimally parameterized local‑type non‑Gaussianity fNL=−35/8 … conditional on assumptions (a)–(f)” is still too strong relative to the body text: Sec. II and Sec. VIII.B describe a wide κϵ range [5.6,80], a 0.6–8% quasi‑dust correction, a null‑space ±0.13 in r, and an unquantified assumption (d) about cubic‑order transfer. You do improve the caveats in the introduction, but the abstract and conclusion still read as though the prediction is tightly constrained and almost parameter‑free. PRD expects the abstract to echo the real degree of theoretical looseness.

**Required fix:**  
- In the abstract and conclusion, explicitly downgrade the claim to something like “leading‑order prediction fNL=−35/8 with an O(1–8%) theoretical uncertainty from quasi‑dust and polynomial null‑space effects, and additional unquantified uncertainty from cubic‑order bounce transmission (assumption (d)).”  
- Add a pointer such as “(see Sec. II.C for details of theoretical uncertainties)” directly in the abstract sentence that states the prediction.  
- Ensure that every place where you call the prediction “minimally parameterized” or “tightly determined” is immediately followed by a quantitative uncertainty statement (percent level for quasi‑dust, ±0.13 in r, and the fact that assumption (d) is only supported by an order‑of‑magnitude argument).


P2-M6 — MAJOR  
**Class:** D (internal cross‑references), F (abstract faithfulness)  
**Location:** Sec. IX.D (joint (fNL, nfNL) forecast), Sec. IV/V/Abstract  

**Problem:** The paper mixes two distinct Fisher analyses—bispectrum‑only σ(fNL)=0.7 and SDB‑based joint (fNL, nfNL)—in a way that can confuse the reader about what underpins the main “5.2–5.5σ” and “2.6–5σ” claims. In IX.D you state that the (fNL, nfNL) Fisher is SDB‑only and much weaker, but earlier sections talk about “joint” forecasts without always being explicit which Fisher is meant. The abstract does not mention SDB or nfNL at all, yet “staged observational strategy” language in Sec. IX can be read as if the joint Fisher is part of the same core forecast.

**Required fix:**  
- At the start of Sec. IV, add a sentence explicitly stating: “All main σ(fNL) and significance numbers (5.2–5.5σ, 2.6–5σ) come from the Heinrich et al. **bispectrum‑only** Fisher; the SDB‑based (fNL, nfNL) Fisher in Sec. IX.D is a separate, weaker cross‑check, not part of the headline sensitivity.”  
- In Sec. IX.D, add a pointer back to this statement and reiterate that these joint results are *not* used in Table IV or in the abstract.  
- Avoid phrases like “joint forecast” in the abstract or conclusion unless you explicitly specify that “joint” refers only to fNL and nfNL within SDB, not to combining SDB and bispectrum for the main numbers.


P2-M7 — MAJOR  
**Class:** B (figure–body consistency), D (cross‑references)  
**Location:** Fig. 2 and its caption vs. Sec. IV and Table IV  

**Problem:** Fig. 2’s bar labels “naive 6.25σ,” “template‑corrected optimistic 5.2–5.5σ,” “realistic 2.6–5σ,” and “all‑combined conservative 2.6–2.8σ” are not fully synchronized with Table IV’s σeff values and with the narrative in Sec. IV/VII. For example, Table IV’s all‑combined σeff values (1.35 and 1.41) translate to |fNL|r/σeff ≈ 2.7σ and ≈ 2.6σ respectively, but Fig. 2 aggregates these as “2.6–2.8σ,” implicitly combining two different scenarios (bϕ=30% vs 50%) into a single bar. The text says “2.6–5σ post‑systematic‑budget envelope,” whereas Fig. 2 shows “2.6–2.8σ” for “all‑combined conservative,” which is a narrower band and omits the 3.0σ GR‑only floor.

**Required fix:**  
- Make the mapping between Table IV rows and Fig. 2 bars explicit in the caption (e.g., “the rightmost SPHEREx bar shows the two ‘all‑combined’ rows of Table IV, at 2.7σ and 2.6σ”).  
- Either split the “all‑combined” bar into two bars (30% and 50% bϕ) or clearly label the bar as representing the 50% scenario only and state that the 30% case is 2.7σ.  
- Verify all numeric conversions used for the plotted bars from the Table IV σeff values, and adjust the text in Sec. IV and VII so that the numbers quoted there (2.6–5σ, 2.6–2.8σ, 3.0σ GR floor) correspond one‑to‑one with the plotted bars, not to overlapping bands that are visually compressed.


P2-M8 — MAJOR  
**Class:** A (arithmetic), J (stale numbers)  
**Location:** Sec. V (MegaMapper forecast), Fig. 2 MegaMapper bars  

**Problem:** The MegaMapper “3–7σ envelope” is described as spanning from a fully degraded (2.6–5σ after systematics) to an “ideal” 7.4–7.7σ. However, the arithmetic in Sec. V is not fully transparent: for σ=0.5, r∈[0.84,0.88], |fNL|r/σ ≈ 7.35–7.70σ, which matches the stated 7.4–7.7; for σ=0.7 plus 30% or 50% bϕ and GR choices, you give specific illustrative values (e.g., ~3.2σ, ~3.0σ) but never recompute a full “MegaMapper Table IV” analogous to SPHEREx. As a result, the “3–7σ” label in the abstract and in Sec. IX.A is not tied to a clearly defined set of scenarios; it is a hybrid of fundamentally different assumptions.

**Required fix:**  
- Construct an explicit MegaMapper systematic table paralleling SPHEREx’s Table IV (even if coarser), or else remove “3–7σ” as a headline number and refer only to “ideal 7.4–7.7σ” plus a few clearly labelled illustrative degraded cases.  
- In the abstract and Sec. IX, mark MegaMapper forecasts as “illustrative only; no systematic budget is constructed analogous to Table IV” to prevent readers from treating “3–7σ” as a rigorously derived range.  
- Ensure that all MegaMapper σ and significance values appearing in Fig. 2 can be reconstructed from explicit formulae and parameter choices written in Sec. V.


P2-M9 — MAJOR  
**Class:** I (appendix vs. main‑text mismatch), D (cross‑references)  
**Location:** Appendix A.2 (Table V) vs. main‑text treatment of Li vs. Cai normalizations  

**Problem:** Appendix A.2’s Table V presents a “Li single time‑ordering” row with 2.63σ for SPHEREx, but the main text insists that Li’s −35/16 is *not* a physical alternative and should not be used. However, Sec. X and Sec. II.C treat the “Li case” as a “robustness remark” and mention that “every significance halves.” This creates a lingering impression that the 2.6σ number is on the same footing as the main 5.25σ, despite the appendix having argued that it is unphysical.

**Required fix:**  
- In Appendix A.2, add a bold caveat directly under Table V stating that the Li row is *not* a physically allowed prediction once the −2 Im commutator identity is imposed, and is included only to test sensitivity to an algebraic error.  
- In Sec. X, when you briefly mention the “hypothetical reader adopting −35/16,” explicitly cross‑reference Appendix A.2 and reinforce that this is a *stress‑test only*, not an allowed model variant.  
- Consider moving the 2.63σ number out of the main conclusion narrative and confining it to the appendix, to avoid giving it equal rhetorical weight with the physical 5.25σ case.


If you want, I can next go systematically table‑by‑table and compute each quoted σ or significance from the nearest stated inputs to catch any remaining arithmetic mismatches.