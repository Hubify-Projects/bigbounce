# P2 R24conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.46.pdf` md5=45ee3af4 pages=23
**Input format**: TEXT + web search + pass-2 self-critique (14033 chars)
**Wall time**: 116.3s

---

The manuscript as provided is already typeset and includes equations, figures, tables, and a full reference list, but I only see the LaTeX/PDF content you pasted, not the actual rendered PDF. I therefore cannot:  
- see page breaks or exact page numbers,  
- visually inspect figures, axes, or tables, or  
- recompute numerics from plotted curves.  

I will nonetheless audit: (i) the logical and numerical consistency of the text and equations, (ii) the internal consistency of quoted σ / significance / ratios, and (iii) the bibliography metadata and claims about prior work that can be checked via arXiv/ADS. Where a page number is needed I approximate by section location.

Below I list findings with IDs and severities.

---

### ESSENTIAL ISSUES

**P2-E1 – Multi-σ values from heterogeneous σ(fNL) without explicit non-comparability disclaimer**

- **Location:** Abstract and throughout (e.g., opening paragraph; IV, V, VII, X).  
- **Problem:** Different quoted “σ” significances mix:  
  - σ(fNL) = 0.7 SPHEREx bispectrum forecast (Heinrich et al. 2024).  
  - σeff after template mismatch (σ/r).  
  - “Before GR and bϕ degradation” vs “after full systematic budget” ranges.  
  - Even different experiments (SPHEREx vs MegaMapper) and channels (SDB vs bispectrum).  
  These are put side-by-side as “5.2–5.5σ”, “3–5σ”, “3–7σ” without **at every juxtaposition** a statement that these σ values are not directly comparable in a likelihood sense—different systematics, channels, priors, and weighting assumptions. This violates the instruction in the prompt and would be confusing for PRD readers.
- **Required fix:**  
  - At each place where σ values from different null procedures or channels are juxtaposed (e.g., abstract, Fig. 2 caption, Secs. IV, V, VII, X), add explicit phrases such as: “These significances are not directly comparable across channels/surveys; each is defined with its own Fisher setup and systematic budget.”  
  - In the abstract, replace “3–5σ” and “5.2–5.5σ” language with “corresponding to ≈3–5σ under our internal Fisher definition; this is not directly comparable to other σ values in the literature” or equivalent.  
  - Clearly distinguish between *statistical* σ (pure Fisher) and *effective* σ after heuristic systematic reweighting.

---

**P2-E2 – Unverifiable and likely incorrect citation to “Cai & Brandenberger (2014)”**

- **Location:** Sec. II C, paragraph beginning “A factor-of-two discrepancy exists in the literature: Cai & Brandenberger  obtain fNL = −35/16…”.  
- **Problem:** Reference  is given as “Y.-F. Cai and R. Brandenberger, Non-Gaussianity in a matter bounce, Phys. Rev. D 90, 023534 (2014).” The well-known 2014 Cai–Brandenberger PRD 90, 023528/023534 series concerns non-singular bounces but, as far as ADS/arXiv indicate, the canonical “Non-Gaussianity in a matter bounce” local-shape calculation is Cai et al. JCAP 0905:011 (already cited as [7]). The text claims Cai & Brandenberger obtain fNL = −35/16 at cs = 1 and then discusses a normalization audit. I cannot find an arXiv or ADS entry matching the precise phrasing and result ascribed to ; the 2014 PRD papers with Cai/Brandenberger concern ekpyrosis and other scenarios, and the earlier detailed matter-bounce fNL calculation is [7] (Cai–Xue–Brandenberger–Zhang 2009).  
- **Required fix:**  
  - Re-verify  against arXiv/ADS: check title, journal, arXiv ID, and whether it actually contains the −35/16 statement with cs = 1. If it does not, then either:  
    - Correct the citation to the actual paper that contains the −35/16 value, or  
    - If no such published paper exists, clearly state that the −35/16 value comes from unpublished notes / a private communication, **not** from a PRD paper, and remove or rephrase “Cai & Brandenberger  obtain …”.  
  - Ensure that the DOI, volume, and page numbers for  match the corrected article.  
  - PRD will not accept fused or misattributed citations for a central normalization argument; this must be nailed down.

---

**P2-E3 – Bayes factor numbers and σtheory priors rely on opaque “scipy.stats.norm” recomputes with no reproducible numerical inputs**

- **Location:** Sec. VI C and Table II, Table III, Appendix A.2.  
- **Problem:** The text contains many precise Bayes factors (e.g., 13.91, 9.80, 5.65, 7.0, 4.01) supposedly from closed-form Gaussian integrals implemented in scripts. These are used to support BF ∼ 10–17 headlines. However:
  - The actual numerical inputs (σeff, prior widths, central values) are scattered and not presented in a clean, reproducible form in the text.  
  - Two different bookkeeping conventions (r=1 vs σeff = σ/r vs “bounce-amplitude space”) are mixed, with nontrivial rescalings.  
  - Although you state a correction from earlier irreproducible BF values, PRD cannot rely on external GitHub scripts for core quantitative claims.
- **Required fix:**  
  - For each headline BF (the ∼10 and ∼17 values used in the abstract), explicitly show the analytic formula and the numerical inputs *in the paper*: prior width Δf, σeff, and the Gaussian central values. Provide a short table listing, for example, Δf = 30, σeff = 0.7, ftrue = −4.375, fcomp uniform in [−15, 15], and the resulting BF computed analytically.  
  - Remove references like “scipy.stats.norm recompute” from the main text. Replace with a symbolic expression plus one or two explicit numerical evaluations that a referee can check with a one-line calculator.  
  - Clarify in one subsection which convention is used for the actual BF values quoted in Table II (is r absorbed into σeff or into the effective fNL?) and stick to that consistently.

---

**P2-E4 – Ambiguous/incorrect claim that Cai & Brandenberger  and Cai et al. [7] “describe the same physical bispectrum” but differ only by conventions**

- **Location:** Sec. II C and Appendix A.  
- **Problem:** The manuscript asserts that the −35/8 vs −35/16 discrepancy is entirely a matter of normalization conventions (c = 1 vs c = 2 and missing time ordering) and that “the physical bispectrum is identical” once this is corrected. This is a strong claim: that all four vertex contributions, mode functions, and overall normalization match across two different computations to six significant figures. You then assert that the operator identity i⟨[ζ^3, L]⟩ = −2Im⟨ζ^3 L⟩ guarantees the factor of two.  
  This goes beyond what can be verified by the current citations. Without giving explicit integral expressions, there is no way for a referee to confirm that Cai & Brandenberger really computed only one time ordering (as opposed to having genuinely different conventions). This creates a risk of misrepresenting prior work.
- **Required fix:**  
  - Either:  
    - Provide explicit citations to equations in [7] and  that show *exactly* that one uses the commutator form and the other uses a single time-ordered correlator, and include at least one explicit vertex integral in the appendix to justify your matching; or  
    - Downgrade the statement to a hypothesis: e.g. “We **interpret** the −35/16 value of  as arising from a single-time-ordering normalization; if both time orderings are included, the Planck normalization yields −35/8. A full cross-derivation is beyond the scope of this work.”  
  - Remove unqualified statements that “the physical bispectrum is identical” unless you either explicitly perform the integrals or show detailed symbolic agreement. PRD standards require that you not overstate what is proven.

---

**P2-E5 – Excessive length and scope relative to claimed contribution**

- **Location:** Entire manuscript (~23 pages).  
- **Problem:** For a methods/forecast paper, the main new, checkable contributions appear to be:  
  - A careful template-overlap calculation (r ≈ 0.84) and its impact on Heinrich et al. SPHEREx σ(fNL).  
  - A Bayesian model comparison framework based on that forecast.  
  - A qualitative audit of the Cai et al. normalization.  
  Much of the rest (long exposition on ECH gravity, torsion, birefringence, anomaly-tracer autoencoders, QSFI asymptotics, etc.) is tangential to the central forecast and makes the paper unfocused. PRD expectations for a cosmology methods paper favor sharper focus.
- **Required fix:**  
  - Tighten the paper to ≈ 15 pages (PRD style) by:  
    - Moving the ECH torsion/γBI and birefringence material to a separate paper or a brief appendix.  
    - Condensing Sec. VI (Bayes factors) to core formulas and one small table; move the lengthy prior grid discussion and Monte Carlo ensembles to an appendix.  
    - Shortening the extensive narrative on anomaly-detected tracers and curvaton/QSFI parameter spaces to concise paragraphs with references.  
  - Make the main text center on: bispectrum shape mapping, template overlap, the σ(fNL) recast, and a conservative model-comparison statement.

---

### MAJOR ISSUES

**P2-M1 – Multiple “correction notes” and internal-audit prose in the body**

- **Location:** Sec. VII (Table III caption), Sec. VII D; Appendix A.2; Data and Code Availability.  
- **Problem:** The text contains editorial/debug language such as:  
  - “Correction note: an earlier version of this table quoted BF values… that could not be reproduced…”  
  - “committed recompute,” “artifact … check.json,” “per-sample propagation artifact released with the paper’s code.”  
  This is essentially version-history and internal QA log content, which does not belong in a PRD article. It suggests that central numbers *changed* mid-stream and undermines confidence.
- **Required fix:**  
  - Remove all “Correction note:” paragraphs and references to earlier inconsistent values. Simply present the final, verified numbers.  
  - Remove references to internal filenames (e.g. “c9g bf table recompute.py”, “artifact … epsilon ratio check.json”) from the main text; they may appear in a separate “code release” note or in supplemental material, but not as narrative in the main article.  
  - Replace such phrases with a concise statement like: “We verified these numbers by independent checks; code is available in the supplemental repository.”

---

**P2-M2 – Use of informal, non-technical language in a PRD manuscript**

- **Location:** Throughout, e.g.:  
  - “This is the headline forecast of this paper.”  
  - “kills live lane” in Fig. 6 caption.  
  - “Anomaly-detected QSO candidates…”  
  - “not firm forecasts” / “speculative motivation.”  
- **Problem:** The tone is occasionally informal and journalistic rather than PRD-style scientific prose. This undercuts clarity and professionalism.
- **Required fix:**  
  - Replace colloquial phrases with neutral scientific language. For example:  
    - “headline forecast” → “principal forecast result.”  
    - “kills live lane” → “excludes the quasi-dust matter bounce parameter point at comparable significance.”  
    - “speculative motivation, not firm forecasts” is fine in content but should be phrased more crisply.  
  - Ensure figure captions are purely descriptive and technical.

---

**P2-M3 – Overly strong novelty claims**

- **Location:** Abstract (“for the first time to our knowledge, the template mismatch… quantified”); Sec. III B (“no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024)”).  
- **Problem:** Claims of “for the first time” require comprehensive literature coverage. The overlap between bounce templates and local estimators in the context of SPHEREx-like forecasts is indeed not widely covered, but similar template mismatch analyses exist for other non-local templates (equilateral, QSFI, etc.), and the general method is standard. Without an explicit search restricted to matter-bounce, these claims are too strong.  
- **Required fix:**  
  - Soften to: “To our knowledge, no prior work has quantified this particular matter-bounce vs local-template overlap, though analogous analyses exist for other non-local shapes.”  
  - Remove any unqualified “first” or “unprecedented” language.

---

**P2-M4 – Claims about SPHEREx launch and survey schedule inconsistent with current status**

- **Location:** Abstract (“SPHEREx (launched March 2025; survey data collection through ∼2027)”); Sec. IV; Sec. IX A; X.  
- **Problem:** SPHEREx is a NASA MIDEX mission with a projected launch window but, as of mid-2026, the exact launch date is not a published, immutable fact. Phrasing “launched March 2025” reads as if the mission is already in orbit and collecting data, which is not correct in a forward-looking PRD submission drafted June 2026.  
- **Required fix:**  
  - Rephrase to future- or conditional tense with citation to the mission description (Dore et al. 2014): e.g., “SPHEREx is planned for launch in the mid-2020s, with a nominal 2-year survey.”  
  - Remove any specific past-tense dates unless you can cite an official post-launch status report.

---

**P2-M5 – Internal cross-checks (“rederivation” language) without real derivation**

- **Location:** Sec. II C (“We performed a source-to-source normalization audit and established…”); Appendix A.1 (“we replace it with an explicit operator-algebra identity”); Sec. II C (“our forecasts therefore rely on the Cai et al. value… validated through these cross-checks rather than through a fully independent derivation.”).  
- **Problem:** The text oscillates between suggesting a full independent derivation and admitting that only limited cross-checks (benchmark configurations, symbolic doubling) were done. This is potentially misleading.  
- **Required fix:**  
  - Clarify explicitly: “We do not perform an independent vertex-level in-in evaluation. Instead, we numerically confirm that the Cai et al. shape function reproduces their published values at the three benchmark configurations and we check consistency of normalization conventions. Our work therefore assumes Cai et al. (2009) is correct.”  
  - Remove phrases like “explicit in-in Wick contraction derivation” unless the appendix actually steps through one full vertex integral with all factors.

---

### MINOR ISSUES

**P2-m1 – Some dimensionful/dimensionless checks are asserted but not clear**

- **Location:** Eq. (1)-(2) and surrounding text.  
- **Problem:** You explain the degree counting for P and BNL. While the overall statement seems dimensionally consistent (BNL dimensionless), the notation “P has degree 9” and “prefactor removes degree 6” is a bit opaque without defining precisely the monomials (k_i^m k_j^n etc.).  
- **Required fix:**  
  - Add one explicit line defining P(k1,k2,k3) = Σ cα k1^pα k2^qα k3^rα, with pα+qα+rα=9, to make the degree counting transparent.  

---

**P2-m2 – Minor numerical consistency checks**

I can recompute a few key scalars:

- Maldacena fNL for ns=0.9649: (5/12)(1−ns) = (5/12)(0.0351) ≈ 0.014625 ≈ 0.015 – consistent.  
- Ratio |fNL^bounce|/|fNL^inf| = 4.375 / 0.015 ≈ 291.7, quoted ≈ 290 – consistent.  
- Shape variation between −4.375 (squeezed) and −2.25 (folded): |Δ|/|squeezed| = 2.125 / 4.375 ≈ 0.486 ≈ 49% – consistent.  
- Template-corrected significance for SPHEREx: |−4.375| × r / 0.7 with r=0.84 → 4.375×0.84/0.7 ≈ 5.25σ, in line with the 5.2–5.5σ range – consistent.  

These are all fine and do not need changing.

---

**P2-m3 – Bibliography metadata**

Spot checks via ADS/arXiv for a few central references:

- [1] Maldacena 2003 JHEP 0305:013, astro-ph/0210603 – correct.  
- [2] Pajer, Schmidt, Zaldarriaga 2013 Phys. Rev. D 88, 083502, arXiv:1305.0824 – correct.  
- [4] Heinrich, Dore, Krause 2024 Phys. Rev. D 109, 123511, arXiv:2311.13082 – correct.  
-  Wilson-Ewing 2013 JCAP 1303:026, arXiv:1211.6269 – correct.  
-  Dore et al. 2014 SPHEREx white paper, arXiv:1412.4872 – correct.  
-  Schlegel et al. 2022 MegaMapper concept, arXiv:2209.04322 – correct.  
-  Barreira 2022 arXiv:2205.05673 – correct.  
-  Jung et al. 2025 A&A 702 A204, arXiv:2504.00884 – looks plausible (future-dated but within the “it is June 2026” context; treat as in-press / preprint).  

I do not see obvious fused citations or impossible arXiv IDs (no “26xx” IDs used here). However, because I don’t have the full ADS list for each minor reference, you should still run your own ADS check for all 38 references, especially , , [33–35] which refer to future/forthcoming works.

- **Required fix:**  
  - Verify  as noted above.  
  - For any references that are still “arXiv e-prints (2026)” without accepted journal info, adjust formatting to PRD style (“arXiv:2603.13924 [astro-ph.CO]”) and do not imply journal acceptance.  

---

**P2-m4 – Data and code availability section format**

- **Location:** “DATA AND CODE AVAILABILITY”.  
- **Problem:** PRD allows data/code statements but typically they should not include URLs; the journal will convert DOIs or links. Your text includes a GitHub URL directly and a long list of internal filenames.  
- **Required fix:**  
  - Replace the raw URL with a brief statement: “All analysis code and configuration files are available in a public Git repository; a persistent DOI and link will be provided in the published version.”  
  - Move detailed file names to supplemental material or a README in the repository.

---

**P2-m5 – Cosmic birefringence digression**

- **Location:** Sec. IX E.  
- **Problem:** The cosmic birefringence discussion and bounce-motivated ALP angle β ≈ 0.27° is peripheral to the main non-Gaussianity/bounce forecast and is not tightly integrated into the rest of the paper. It risks making the narrative diffuse.  
- **Required fix:**  
  - Either substantially shorten this to a single paragraph noting that other observables may probe related physics, or move it to an appendix.  

---

### NITS

**P2-N1 – Minor repetition and small phrasing issues**

- “mechanism-independent” vs “UV-completion-independent” is explained at length twice (Sec. I and II B). This could be tightened.  
- Some sentences are extremely long and nested; PRD prefers clearer, shorter sentences.  

**Required fix:**  
- Light copy-editing for repetition and sentence length.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core idea—recasting SPHEREx and MegaMapper local-fNL forecasts for the matter-bounce bispectrum and quantifying template mismatch—is interesting and potentially suitable for PRD. However, the manuscript in its current form is too long and diffuse, contains at least one problematic key citation (Cai & Brandenberger ), overstates what is actually derived versus assumed for the bispectrum normalization, and uses Bayes factors in a way that is not sufficiently transparent for an article of this rigor. Addressing the essential issues (especially E2, E3, and E4), tightening the scope to a focused methods paper, and cleaning out internal “correction note” language and informal prose are necessary before the work can meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E6 – Several Bayes-factor and “σeff” numbers are arithmetically inconsistent or undefined as written
- **Location:** Sec. VI C (Bayes factors 13.91, 9.80, 5.65, 7.0, 4.01, “17.1→14.4”, “7.0→6.2”, “4.0→4.0”), Table II, surrounding prose on σeff and r.
- **Problem:**  
  - The core BF formula (Eq. 7) is given, but for many quoted BF values there is no unambiguous specification of the numerical inputs (σ, prior width, central value), and the text’s verbal description is internally inconsistent. For example, the paragraph “Gaussian prior, σtheory = 1.0 … ∼10 (BF=9.80, broad [−15,+15])” gives only the *posterior* number 9.80, with no consistent back-substitution that reproduces 9.80 from Δf=30, σeff, and a central value −4.375 using Eq. (7). Similar issues hold for “13.91”, “5.65”, “4.01”, and the rescaled values “17.1→14.4”, “7.0→6.2”, “4.0→4.0”: the paper mixes r=1 vs σeff=σ/r vs “bounce-amplitude space” conventions without giving a single closed numerical example that both a reader and the author’s own text satisfy simultaneously.
  - The “σeff = 0.83” used in the template-rescaling paragraph conflicts with the earlier statement that σ(fNL)=0.7 and r=0.84; 0.7/0.84 ≈ 0.83, but later the text also says σeff=0.72+σGR² under GR-marginalization, which cannot simultaneously represent the same effective width as the r-rescaled value.  
- **Required fix:**  
  - For each specific BF quoted with two significant figures, provide in one place the explicit inputs (σ, σeff if rescaled, prior bounds, central value) and show that Eq. (7) reproduces the number. If any quoted numbers cannot be reproduced, correct them and explicitly remove the old values.  
  - Clearly distinguish three cases in the text: (i) “raw σ=0.7, r=1”; (ii) “bounce-amplitude bookkeeping σeff=0.7/r”; (iii) “σeff including GR and other systematics”. State explicitly which σeff is used in Table II and Table III. Remove any BF value that relies on mixing these schemes.  

---

P2-E7 – Abstract’s “3–5σ after the combined systematic budget” is not supported by a single, coherent budget calculation
- **Location:** Abstract (“template-corrected significance ∼3–5σ after the combined systematic budget … with 5.2–5.5σ as the optimistic case before GR and bϕ degradation”), Sec. IV, Sec. VII A–C.
- **Problem:** The body discusses many degradations—template overlap, ϵ-correction, null-space scatter, bϕ priors, GR projection, photo‑z, etc.—but these are never propagated in one consistent, quantitative chain starting from σ=0.7 to yield a concrete “3σ floor” and “5σ ceiling.” Different sections quote different partial degradations (e.g., 20–50% from bϕ, 10–30% from GR, 5% from photo‑z, 15–30% from anomaly-shot-noise), but the abstract’s “3–5σ” appears to be a qualitative envelope rather than a documented calculation.  
- **Required fix:**  
  - Build one explicit error budget table: start from σ=0.7, show multiplicative or additive factors for each systematic (with central and extreme assumptions), and show how this yields the “optimistic” and “conservative” significances.  
  - Either justify the “3–5σ” range numerically or soften the abstract to “∼few-σ” with explicit pointer to where the detailed budget is constructed.  

---

P2-E8 – Claims of having “established” the Cai vs. Cai & Brandenberger factor-of-two as purely conventional are stronger than the actual derivation supports
- **Location:** Abstract; Sec. II C (“We performed a source-to-source normalization audit and established that this is a convention difference, not a physical one… The physical bispectrum is identical.”); Appendix A and A.1.
- **Problem:**  
  - The appendix presents an operator-identity derivation of the in‑in commutator doubling and a careful discussion of c=1 vs c=2 conventions, but it does **not** actually show, vertex by vertex, that Cai & Brandenberger  dropped exactly one time ordering rather than, e.g., using different mode functions, different gauge, or a different definition of the curvature variable. It also does not display any explicit equation from  demonstrating that their “−35/16” corresponds precisely to a single-ordering version of the Cai et al. shape.  
  - Nonetheless, the main text repeatedly asserts as fact that “all four individual vertex contributions … agree between the two papers … the physical bispectrum is identical,” which is more than the appendix actually proves with explicit formulas.  
- **Required fix:**  
  - Either include explicit references to the precise equations in  and  that show equality of the four vertex contributions and their mode functions, or downgrade the language to a well-motivated interpretation (“we interpret the −35/16 value as arising from a single-time-ordering normalization; a full cross-derivation is beyond our scope”).  
  - Remove unqualified phrases like “established that this is a convention difference” unless the paper truly shows symbolic equality beyond doubt.  

---

P2-M6 – Inconsistent treatment of r and σ(fNL) across sections leaves the effective significance under-defined
- **Location:** Abstract; Sec. III B, IV, VI C, VII D; Table II; Fig. 2 caption.
- **Problem:** The paper uses at least three different ways of implementing the template overlap r:  
  - In places, the detection significance is written as |fNL| r / σ(fNL), using σ=0.7 and r≈0.84.  
  - Elsewhere (Sec. VI C) σeff is defined as σ/r and then Bayes factors and significance are computed in “bounce-amplitude space”.  
  - In Sec. VII C and Table III, σeff is instead defined via GR-degradation (σeff² = 0.72² + σGR²).  
  These definitions are not clearly reconciled: it is never stated whether the GR-degraded σeff includes the r factor or not, nor is it clear which σeff is used in the Bayes-factor tables. As written, a reader cannot reconstruct a single, consistent “effective σ” that underlies all quoted significances.  
- **Required fix:**  
  - Introduce a single notation: e.g., σ0=0.7 (Heinrich), r for template overlap, and σGR for GR broadening. Give explicit formulas such as σeff² = (σ0/r)² + σGR² and stick to them everywhere.  
  - Recompute all advertised significances (Fig. 2, the “3–5σ” band, the null exclusion) using that single scheme and correct any numbers that change appreciably.  

---

P2-M7 – Some abstract sentences are not fully backed by quantitative results in the body
- **Location:** Abstract sentences on (i) “validated via ℓ-space Fisher overlap, 200 injection–recovery realizations, and a 10,000-sample null-space scan,” (ii) “3–7σ realistic MegaMapper range,” (iii) “Bayes factor BF ≈ 10–17” envelope.
- **Problem:**  
  - The ℓ-space Fisher and injection–recovery checks are described, but the statistical power of those tests (e.g., uncertainties on r from 200 realizations, treatment of cosmic variance, mask, etc.) is not quantified beyond quoting means ± very small errors; it is not demonstrated that these are sufficient to “validate” the 84% overlap to the 2–3% level claimed.  
  - The MegaMapper “3–7σ” range is a fairly broad, headline-level claim, yet there is no detailed Fisher calculation in Sec. V showing how specific assumptions on kmin, bϕ priors, GR projections, and survey design map into that range. The text characterizes the numbers as “speculative motivation” but the abstract still presents “3–7σ realistic” as if based on a rigorous forecast.  
  - The BF≈10–17 envelope is sensitive to both σtheory and competitor priors, but only a subset of combinations are actually shown numerically, and no single table gives BF for all combinations of (σ, r, σGR, σtheory, prior width).  
- **Required fix:**  
  - For each of the three headline claims, add an explicit pointer to the concrete calculation that supports it, plus enough numbers that a referee can reconstruct the quoted range, or soften the abstract language to clearly indicate they are qualitative or design-level estimates.  

---

P2-M8 – Several dimensional-analysis explanations are only qualitative and could hide normalization mistakes
- **Location:** Eq. (1)–(4) and surrounding explanations; Sec. III A.
- **Problem:**  
  - For AT and BNL, the argument that “P has degree 9, the prefactor removes degree 6, and the denominator removes degree 3, so BNL is dimensionless” is *qualitative* and relies on implicit assumptions about how the monomials are constructed and how factors of a, H, and Mpl have been absorbed.  
  - Similarly, in Eq. (4), M(k,z) is said to be \(2 k^2 T(k) D(z)/(3 \Omega_m H_0^2)\) with no explicit statement of units (c=1 vs not, whether T and D are dimensionless, whether k is comoving, etc.). A sloppy dimensional mismatch (e.g., missing factors of c or a) would be hard to catch from the current prose.  
- **Required fix:**  
  - Add an explicit line defining P(k1,k2,k3) as a sum of monomials with exponents that sum to 9 so that one can literally see degree counting.  
  - For M(k,z), state the units and conventions (e.g., c=1, k in h Mpc⁻¹, H0 in km s⁻¹ Mpc⁻¹, T and D dimensionless), and check in-text that ∆b(k,z) is dimensionless.  

---

P2-M9 – Abstract and Sec. X still mix gauge-frame and CFC-frame statements in a way that may confuse readers
- **Location:** Abstract opening, and last paragraph of Sec. X.
- **Problem:** The abstract and conclusion jump back and forth between the gauge-frame fNL measured by SPHEREx and the conformal-Fermi (physical) fNL that obeys a different consistency relation. While the text eventually clarifies that SPHEREx measures the gauge-frame quantity and the CFC statement is “a complementary theoretical discriminator,” the transitions are abrupt and could easily be misunderstood as implying that the survey tests the CFC relation directly.  
- **Required fix:**  
  - In the abstract and conclusion, explicitly label which quantities are *observables* and which are *frame-dependent theoretical constructs*, and keep survey forecasts strictly in the observable (gauge-frame) language. Relegate the CFC statement to a clearly marked theoretical aside.  

---

P2-m6 – Some percentages and factors quoted verbally are not explicitly recomputed in the text
- **Location:** Sec. II B/C, III B, VII B–D, VIII A/B, IX D, X (various “∼10–20%”, “∼15–30%”, “∼19%”).
- **Problem:** Many percentage degradations are given as “∼X%” without showing the actual numerical ratios from which they are derived. For example, in Sec. III B the mask degradation “1/√0.7 ≈ 1.19, a ∼19% degradation” is consistent, but other quoted ranges (e.g., 10–20% improvement from anomaly tracers, 15–30% degradation from shot noise, 20–50% from bϕ) do not show the underlying arithmetic or assumptions. This makes it hard to verify which of these are back-of-envelope and which are calculated.  
- **Required fix:**  
  - For each instance where a percentage or ratio is used to support an argument (especially if it feeds into the σ range), either add a brief parenthetical computation or explicitly label it as an order-of-magnitude estimate not used directly in the main forecast numbers.  

---

P2-m7 – Internal cross-reference “Sec. VIII” for κϵ range and impact is thinly quantified
- **Location:** Sec. II A (“κϵ has an order-of-magnitude range 5.6–80, Sec. VIII.”), Sec. VIII B.
- **Problem:** The text cites Sec. VIII as giving a detailed basis for κϵ ∈ [5.6, 80] and the resulting 0.6–8% correction, but the actual derivation is semi-qualitative: it sketches contributions from prefactor scaling and mode-function scaling without performing a full numerical integral or giving an explicit expression for κϵ. The range is plausible, but calling it a “correction window” and using it in the σtheory argument in Sec. VI gives it more quantitative authority than is explicitly demonstrated.  
- **Required fix:**  
  - Clarify in Sec. II and VIII that κϵ ∈ [5.6, 80] is a schematic bound, not a computed likelihood range, and that σtheory = 1.0 is chosen to comfortably cover this plus the convention ambiguity.  

---

P2-m8 – Some figure-caption vs. body-text phrasings are not perfectly aligned
- **Location:** Fig. 2 caption vs. Sec. IV; Fig. 4 & 5 captions vs. VII A–C; Fig. 6 caption vs. Sec. IX C.
- **Problem:**  
  - Fig. 2 caption says “error bars span the optimistic endpoint (published ideal σ(fNL) with template-overlap correction only) to the conservative endpoint (full §VII budget…)” but Sec. IV’s narrative primarily discusses point values (5.5σ, 5.2σ, ∼3–5σ) without explicitly stating these as the same endpoints plotted in Fig. 2.  
  - Fig. 6 labels the dark-red region “kills live lane”, which the body explains as a null disfavoring the quasi-dust bounce at the same 3–5σ level as a detection, but the figure caption does not restate that symmetry or the dependence on assumptions (a)–(f).  
- **Required fix:**  
  - Make sure that for each figure the body explicitly restates the *same* quantitative ranges and the main assumptions underlying them, so a reader can cross-check caption and text numerically. Replace “kills live lane” with neutral language as already noted in P2-M2.  

---

P2-N2 – A few lingering tense and date inconsistencies around SPHEREx status
- **Location:** Abstract; Sec. IX A; Sec. X.
- **Problem:** P2-M4 already flagged “launched March 2025” as incorrect for a forward-looking 2026 manuscript. There are multiple occurrences (“launched March 2025; first all-sky survey completed December 2025; science data release expected ∼2028”) that mix past tense (“launched”, “completed”) with future/conditional context (“expected”), which would not be appropriate if the paper is submitted before launch.  
- **Required fix:**  
  - Uniformly adopt future or conditional language for SPHEREx status (e.g., “planned launch in the mid-2020s, nominal 2-year survey”), and remove any past-tense mission milestones unless you can cite an official post-launch document.  

If you address these new issues in addition to the earlier list, the manuscript will be substantially more internally consistent and quantitatively transparent at PRD standards.