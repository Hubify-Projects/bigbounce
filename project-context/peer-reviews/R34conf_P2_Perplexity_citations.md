# P2 R34conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.54.pdf` md5=aae083ab pages=25
**Input format**: TEXT + web search + pass-2 self-critique (14785 chars)
**Wall time**: 85.7s

---

P2-E1 (ESSENTIAL)  
Section: Abstract, p.1  
Problem: The abstract claims “a matter-dominated contracting phase … produces a minimally parameterized local-type non-Gaussianity \(f_{\rm NL}^{\rm local} = -35/8\) (Cai et al. 2009)” and uses this as a hard prior throughout, but the only explicit derivations in this manuscript are verbal, not computational: there is no worked re-derivation of the cubic action, no explicit in-in integrals, and no concrete numerical check beyond quoting Cai et al. and Li et al. The Appendix A description is purely schematic and does not allow an independent reader to verify the factor-of-two resolution or the normalization. Required fix: Either (i) add a complete, explicit derivation of the bispectrum amplitude from the cubic Maldacena action specialized to \(w\simeq 0\), including the full in-in integrals and demonstrating that the numerical coefficient is indeed \(-35/8\) in the Planck convention, or (ii) rephrase the paper to treat \(-35/8\) explicitly as an external assumption from Cai et al., weaken every statement that treats it as “established” by this work, and clearly label all forecasts and Bayes factors as conditional on that external result.

P2-E2 (ESSENTIAL)  
Section: Abstract & Appendix A, p.1 & pp.22–25  
Problem: The “operator-algebra” resolution of the Cai vs Li factor-of-two is asserted but not demonstrated at a level acceptable for PRD. The Appendix provides only schematic expressions for the in-in commutator identity and generic integrals \(I_v\), but does not show any explicit contraction or intermediate step that connects Li et al.’s reported value \(-35/16\) to the claimed “single-time-ordering” intermediate, nor does it reproduce any concrete equation from Li et al. to show the precise mapping. This is a load-bearing point: the entire significance forecast is doubled by this choice. Required fix: Provide an explicit, equation-by-equation comparison with the Li et al. 2016 paper: identify which of their equations correspond to the single time-ordering, show explicitly that summing both orderings plus the exact same normalization conventions leads to \(-35/8\). This should include at least one fully written mode integral, not just a formal commutator identity.

P2-E3 (ESSENTIAL)  
Section: Abstract & §IV, Fig. 2, pp.1, 9–10  
Problem: The headline forecast “bispectrum-only 5.2–5.5σ” at \(f_{\rm NL} = -35/8\) is repeatedly presented as a quantitative result of this paper, but you never recompute a Fisher matrix. You adopt \(\sigma(f_{\rm NL}^{\rm local}) \approx 0.7\) from Heinrich et al. and simply multiply by the shape overlap factor \(r\). This is not an independent forecast and strongly depends on Heinrich et al.’s modeling assumptions, nuisance parameter treatment, and survey implementation. PRD standards require that a “forecast” claimed by a paper be computed within the paper’s own set of assumptions, or be clearly and consistently labeled as an external recast at every occurrence. Required fix: Throughout the paper, including the abstract, title, and all figure captions, clearly label every quoted significance as a recast of Heinrich et al.’s forecast, not a new Fisher computation. Alternatively, perform a full Fisher analysis for SPHEREx with your own covariance, bias parameter model, and survey specification, and re-derive \(\sigma(f_{\rm NL})\) to demonstrate that the numerical values are robust to different analysis choices.

P2-E4 (ESSENTIAL)  
Section: Abstract, §IV, §VII, pp.1, 9–10, 14–16  
Problem: Different sigma ranges are presented in multiple places with partly overlapping but not fully reconciled systematic budgets: abstract “5.2–5.5σ … reducing to ∼2.6–5σ”, Fig. 2 shows a bar labeled “realistic post-systematic-budget envelope 2.6–5σ” and “all-combined conservative endpoint 2.6–2.8σ”, §VII quotes “∼2.6–5σ realistic” and “∼2.6–2.8σ conservative”, while the bϕ discussion gives 3.5–4.2σ ranges. The quadrature combinations that produce these numbers are not systematically tabulated, and a reader cannot verify that the ranges are numerically consistent with the stated inputs. Required fix: Provide one explicit table that lists each systematic (template overlap r, ϵ-correction, bϕ prior, GR projection, photo-z, null-space scatter) with the corresponding effective \(\sigma\) contribution and then shows the actual quadrature combination leading to the 5.2–5.5σ “optimistic”, 2.6–5σ “realistic”, and 2.6–2.8σ “conservative” bands. Make sure that every distinct numerical band in the abstract and captions appears as a row in that table so that the reader can audit the arithmetic.

P2-E5 (ESSENTIAL)  
Section: Abstract; §VI, Table II; §VII, Table III, pp.1, 12–13, 17  
Problem: The Bayes factors quoted in the abstract (“BF ≈ 9–14”, “BF ≈ 4–7”) and body rely on a closed-form expression and Monte Carlo sampling, but the exact likelihood and prior definitions are not fully specified. In particular, it is ambiguous whether the “effective σ” includes the shape-overlap r factor and all systematics, and how the prior widths on \(f_{\rm NL}\) for competitors are chosen. A reader cannot reproduce the exact numbers in Table II or Table III from the prose alone. Required fix: Explicitly write down the likelihood function \(L(f_{\rm NL}^{\rm obs}|f_{\rm NL})\) used; state clearly which \(\sigma\) enters in each entry of Table II and III, including whether r is applied. Provide the exact prior ranges (e.g. \([-15, +15]\), \([-5, +5]\)) and prior shapes (flat, Gaussian) and the mathematical integrals corresponding to each Bayes factor. Add a short appendix with the actual numbers (e.g. for BF=9.80, list the input \(f_{\rm NL}^{\rm obs}\), σ, prior bounds) so that the Bayes factors are reproducible from the manuscript without access to external code.

P2-E6 (ESSENTIAL)  
Section: Abstract, §II.A, Table I, Fig. 1, pp.1–4  
Problem: Table I lists benchmark values for \(B_{\rm NL}\) that are said to “match the published results  exactly”, but there is no explicit citation of the equation or table in Cai et al. where these numbers appear, nor a definition of \(B_{\rm NL}\) that matches their notation. Since this is a central validation step, the reader needs to be able to trace which numbers in Cai et al. you matched. Required fix: Identify explicitly which equations and/or tables in the Cai et al. paper correspond to the squeezed, equilateral, and folded values, and show the mapping between your \(B_{\rm NL}\) and their bispectrum amplitude (including any factors of 2, 5/3, etc.). If the numbers are not literally printed in Cai et al., rephrase “match exactly” to “are consistent with” and state that you computed their integrals numerically.

P2-E7 (ESSENTIAL)  
Section: §III.B, Eq. (5), pp.7–8  
Problem: Equation (5) defines a “canonical inequality” \(0<r\le 1\) for single-field bispectra normalized to their own squeezed limit, and then immediately notes that for the matter-bounce shape \(r\) can exceed unity. However, you continue to use r>1 samples in null-space scans and treat r as an amplitude recovery factor. For a reader, this mixes two different meanings of r (shape-average vs. estimator response) and can be confusing about what is physically allowed. Required fix: Clarify that r>1 here is purely an artifact of your chosen normalization to the squeezed-limit value rather than a true estimator gain >100%, and explicitly separate the definition of r as a shape-weighted inner product from any estimator normalization; emphasize that only the noise-weighted central r≈0.83 is used in forecasts.

P2-E8 (ESSENTIAL)  
Section: §VIII.B, Eq. (9) & (10), p.18  
Problem: The “consistency relation” between ns and fNL is presented as \(f_{\rm NL}(n_s) \approx -35/8 - c'(n_s-1)\) with \(c' \in [0.7,10]\). However, this is based on a very rough order-of-magnitude argument combining a prefactor \(A_T \propto 1/\epsilon^3\) and a mode-function scaling, with no actual calculation. Presenting this as a “consistency relation” risks over-selling a qualitative estimate. Required fix: Either (i) downgrade this to an explicit heuristic scaling relation, clearly labeled as such and not used in any quantitative forecast or Bayes factor, or (ii) provide a concrete calculation of κ_ε (even at leading order) from the cubic action and mode functions so that c′ is a derived parameter rather than a 1–2 order-of-magnitude bound.

P2-E9 (ESSENTIAL – pattern-048, uncomputed quantitative claim)  
Section: §VII.A–D (Systematics), pp.14–16  
Problem: Many robustness statements (photo-z degradation “degrades by only ∼5%”, SDB “>10% at 10% outlier fraction”, “expected to degrade … by an estimated O(10–30%)”) are qualitative and unsupported by explicit numbers or references. According to the instructions, every inequality or robustness assertion where a number is checkable should be quantified. Required fix: For each systematic you discuss (photo-z outliers, nonlinear bias, lensing magnification, integral constraint), either (a) provide an explicit quantitative estimate (formula and numbers) or a traceable literature reference that contains the estimate, or (b) clearly label it as speculative and remove it from the chain of reasoning that leads to your 2.6–5σ headline.

P2-E10 (ESSENTIAL – abstract-last drift)  
Section: Abstract vs. §VII & §X, pp.1, 16, 21  
Problem: The abstract presents the main result as: SPHEREx can achieve “bispectrum-only 5.2–5.5σ … reducing to a realistic ∼2.6–5σ after the systematic budget”. In §VII and the conclusion, you emphasize significant caveats: bϕ prior sensitivity, GR projection modeling, and that the forecast is a recast rather than independent. The abstract does not mention the dependence on Heinrich et al.’s external Fisher analysis, nor the strong prior dependence of Bayes factors. Required fix: Modify the abstract to state explicitly that: (i) all numerical σ values are a recast of Heinrich et al. (2024), (ii) the 2.6–5σ “realistic” range depends on assumptions about bϕ priors and GR modeling, and (iii) Bayes factors are strongly prior-dependent and should be read as illustrative rather than definitive. Ensure that the caveats in §VII and §VI are reflected, even briefly, in the abstract.

P2-E11 (ESSENTIAL – sigma comparability)  
Section: Abstract & Fig. 2, pp.1, 10  
Problem: Multiple σ values from different procedures (ideal bispectrum-only, GR-degraded, bϕ-degraded, MegaMapper SDB) are plotted and discussed side-by-side. Although you mention that some are optimistic vs. conservative, you do not explicitly state at each juxtaposition that they are not directly comparable because they arise from different systematics and even different observables (bispectrum vs. SDB). Required fix: Wherever two σ values from different null procedures appear side by side (especially in Fig. 2 caption and the abstract), add an explicit phrase “these significances are not directly comparable because they rely on different observables and systematic assumptions.”

P2-M1 (MAJOR – citation forensics & metadata)  
Section: References [1]–, throughout  
Problem: Several references appear to be future-dated or hypothetical: e.g. “ M. Zhu and Y.-F. Cai, 2026, arXiv:2603.13924”, “ G. Jung et al., 2025, Planck PR4”, “ Diego-Palazuelos & Komatsu 2025 ACT DR6”, which as of the paper’s date (June 11, 2026) may not exist or may have different arXiv IDs. Also, ref.  is cited in the text as “Zhu & Cai ” for “dark-energy-from-bounce” constructions, which seems very specific. Without verified IDs this is not acceptable for PRD. Required fix: Verify that each of these cited works actually exists on arXiv or in a journal with the stated year, authorship, and title, and correct the IDs and bibliographic information as necessary. If any are speculative future works or private drafts, they must be removed or clearly labeled as “in preparation” and not used as load-bearing support.

P2-M2 (MAJOR – unsupported novelty claims)  
Section: Introduction & Discussion, pp.2, 19–21  
Problem: The paper repeatedly states or implies that fNL = -35/8 is a “minimally parameterized” prediction and that this provides perhaps “the sharpest single observable” to distinguish bounce from inflation. There is no systematic comparison to other potential bounce discriminators (e.g., tensor spectra, specific features in power spectra) nor to other non-Gaussian signatures in multifield inflation. Required fix: Either back these claims with specific references and a comparative discussion (showing why this is sharper than, say, tensor signals or CMB spectral-distortion constraints), or soften the language to “one of the sharpest known observables.”

P2-M3 (MAJOR – internal bookkeeping language)  
Section: Multiple (e.g., “c9g bf table recompute.py”, “artifact … json”), pp.3, 4, 11–13, 16, 21–22  
Problem: The manuscript is riddled with internal artifact names and bookkeeping tags (“null space analysis.py”, “c9i epsilon ratio check.json”, “c9g bf table recompute.py”, “phase3 fisher overlap.json”), which do not belong to a final journal article. PRD expects code to be referenced via DOIs or URLs in a Data Availability statement, not via raw internal filenames sprinkled through the body. Required fix: Remove all such file names and internal audit tags from the main text and either (i) consolidate them in a Data/Code Availability section (already present) with a concise description of what each artifact does, or (ii) replace them with generic references (e.g., “see our public code repository”).

P2-M4 (MAJOR – repetition and length)  
Section: Entire manuscript (25 pages)  
Problem: The manuscript is longer than necessary for the claimed contribution. There is substantial repetition of the same points: template overlap r=0.84±0.02, fNL=-35/8 vs -35/16, “not an independent forecast but a recast”, “σ(fNL)=0.7 from Heinrich et al.”, etc., reappear in many sections and footnotes. This makes the logic harder to follow and obscures the genuinely new parts (null-space analysis, Bayes-factor framing). Required fix: Streamline the text: (i) move technical asides and repetition (e.g., explanation of r, discussion of Li vs Cai) into a single dedicated section or appendix; (ii) cut duplicated paragraphs; (iii) aim for ≤18–20 pages including references for the core content.

P2-M5 (MAJOR – effect sizes per instruction 19)  
Section: Abstract & §IV, VI, VII, pp.1, 9–12, 14–16  
Problem: The instructions require that every χ²/σ/p headline be accompanied by an effect-size or practical-significance statement. Here, 5σ vs 3σ are quoted without giving the actual fractional bias in galaxy clustering or bispectrum amplitude relative to noise. Required fix: For the main SPHEREx bispectrum channel, add a short statement translating 5σ in fNL into a fractional modulation of the galaxy bispectrum or an approximate fractional change in large-scale clustering (e.g. “corresponding to O(10%) modulation of the bispectrum at k ~ …”), with a clear formula and number, so readers can interpret the practical significance.

P2-M6 (MAJOR – τNL and Suyama–Yamaguchi)  
Section: §VIII.D, p.20  
Problem: You mention the Suyama–Yamaguchi inequality and a “local single-source analogy” τNL ≈ (36/25)fNL²≈27.6, and say this is “far below current Planck constraints”, but you do not derive τNL in the bounce model, nor is it clear that the matter-bounce setup is single-source in the sense required by the inequality. Required fix: Either (i) drop this paragraph, or (ii) add a brief derivation showing that the conditions for the SY equality are met in the matter-bounce scenario (single adiabatic source of ζ), and then compute τNL explicitly or show that the local-analogy estimate is justified.

P2-M7 (MAJOR – self-containedness, pattern-046/047)  
Section: §IV, §VII, §VIII, pp.9–10, 14–18  
Problem: Many crucial numerical inputs are imported from “Heinrich et al. [5] Fisher” and “Dore et al.  forecast lineage” without reproducing their key equations or survey parameters. A standalone-reader should be able to see at least the form of the Fisher matrix and the main survey inputs used. Required fix: Add a compact subsection summarizing the Heinrich et al. bispectrum Fisher setup: redshift bins, galaxy number densities, bias model, and the Fisher formula used. This can be schematic but must be detailed enough that a reader can see exactly what σ(fNL)=0.7 means.

P2-M8 (MAJOR – Data Availability & provenance)  
Section: Data and Code Availability, p.21  
Problem: The Data/Code section lists a GitHub path and mentions a Zenodo DOI “inserted at submission” but does not give a concrete DOI or version tag, and the code is tightly coupled to internal filenames. According to the instructions, reproducibility and frozen-release hashes are required. Required fix: Provide an actual Zenodo DOI and a Git commit hash for the version of the code that was used to generate the results. Ensure that the code repository includes a README mapping each figure/table in the paper to a script.

P2-N1 (NIT – duplicate phrase / wording)  
Section: §I, p.2  
Problem: The phrase “mechanism-independent” is used repeatedly with different caveats; this risks confusion. Required fix: Choose a single term (e.g. “UV-completion-independent within the scalar-only matter-bounce class”) and use it consistently, minimizing repetition.

P2-N2 (NIT – minor typos / style)  
Section: Throughout  
Problem: There are scattered minor typographical issues (missing hyphens in “Hehl-Datta–Mercuri”, inconsistent use of “bispectrum-only” vs “bispectrum only”, slightly awkward parenthetical citations). Required fix: Run a careful copy-edit pass, preferably with LaTeX spell-checking, and standardize hyphenation and math formatting.

P2-N3 (NIT – version-history language)  
Section: Several places (e.g. §VI, §VII, tables), pp.12–13, 17  
Problem: There are phrases like “Correction note: an earlier version of this table…” and “an earlier version of this paragraph placed…”. These are version-history artifacts and should not appear in a final PRD manuscript. Required fix: Remove all “earlier version” notes and integrate the corrected content cleanly, perhaps mentioning in a footnote only if the correction addresses a previously published preprint.

P2-N4 (NIT – explicit ns, fNL consistency)  
Section: Abstract & §VIII.B, pp.1, 18  
Problem: The abstract quotes ns=0.9649 and fNLbounce=-35/8 with a “contrast ≈290” but does not give the exact numerical ratio for the Planck best-fit, nor the Planck error on ns. Required fix: Add a short explicit computation in the body (e.g., “At ns=0.9649±0.0042, fNLinf=(5/12)(1-ns)=0.015, so |fNLbounce|/|fNLinf|≈290”) with the Planck reference.

P2-N5 (NIT – figure axis labels)  
Section: Fig. 1, Fig. 2, Fig. 4, Fig. 5, Fig. 6, pp.4–5, 10, 14–15, 19  
Problem: The text describes axes qualitatively, but from the provided captions alone it is not guaranteed that axes in the final figures include units (e.g. k in h Mpc⁻¹) and variable names (e.g. fNL). Required fix: Ensure that all figures have fully labeled axes including symbol, units (where applicable), and that captions specify any normalization used (e.g., “k in h Mpc⁻¹, σ in units of standard deviations”).

## Summary recommendation

MAJOR REVISIONS

The paper tackles a physically interesting question and assembles a substantial amount of technical context, but it relies heavily on external forecasts, contains numerous internal bookkeeping artifacts, and uses heuristic derivations where load-bearing calculations are needed. For PRD, the derivation and normalization of the benchmark fNL, the propagation of systematics into significance, and the Bayes-factor computation must be made fully explicit and reproducible. With a thorough cleanup along the lines above—particularly clarifying what is derived here vs. what is recast, removing internal artifacts, and tightening the technical arguments—the work could become suitable for publication, but in its current form it does not meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E12 (ESSENTIAL – arithmetic and propagation inconsistencies)  
Class: A, J  
Issue: Multiple quoted σ and significance numbers do not consistently follow from the stated inputs, and some internal “sanity checks” embed arithmetic that is either wrong or uninterpretable.

Examples (non‑exhaustive):  
- In §II, the ϵ-correction is described as “0.6–8% uncertainty” around −35/8 and later converted to a shift “κϵ|∆ϵ| ≈ 0.36” with κϵ ∈ [5.6,80] and ∆ϵ ≈ 0.0045 (Sec. VIII.B). But 80×0.0045 ≈ 0.36 corresponds to an 8% shift only if one compares to |−4.375|; the lower end 5.6×0.0045 ≈ 0.025 is ≈0.6% of |−4.375|. This is logically consistent but nowhere explicitly connected; a reader must reverse-engineer that 0.6–8% refers to |δfNL|/|fNL|, not to |δϵ|/ϵ. This should be spelled out and checked step-by-step.  
- In §II, the “null-space” scatter in r is quoted as 0.85±0.13 with range 0.55–1.14, yet earlier the “noise-weighted” r is 0.84±0.02 and the five-set scan is 0.867–0.888. The 16th–84th percentile significance range is given as 4.4–6.2σ “at the pre-systematic baseline (σ(fNL)=0.7)”, but 4.4σ corresponds to r≈0.70 for |fNL|=4.375, and 6.2σ to r≈0.99. This is inconsistent with the stated r-range (0.55–1.14) and implies that in practice low‑r realisations are not being propagated consistently. Either the percentiles are miscomputed or the textual mapping between r and σ is wrong.  
- In §IV, the “all-combined conservative endpoint 2.6–2.8σ” derivation is opaque. For example, using the explicit GR-only example: 4.375×0.83/√(0.7²+1.0²)≈2.98σ, not 2.6–2.8σ, whereas the text later says “σGR=1.0 in quadrature with σ(fNL)=0.7, … ≈3.0σ”. It is claimed that adding the widened bϕ prior pushes this to 2.6–2.8σ, but the actual quadrature arithmetic is never shown and the numbers quoted (e.g. “effective σeff = 0.92⁺¹·⁰²₋¹·⁰²+1.0² = 1.35–1.41” in the Fig. 2 caption) are dimensionally and typographically confusing—it is unclear what 0.92 and 1.0² are supposed to be and how they arise from σ=0.7 and the various systematics. This is an arithmetic‑level issue, not just a presentation issue.  
Required fix:  
- Recompute all quoted σ and significance values from first principles in one place (probably the new table requested in P2‑E4), explicitly showing each quadrature step and the numerical inputs.  
- Recheck the mapping between the null-space r‑distribution, the 4.4–6.2σ percentiles, and the quoted r-range; either the percentiles or the r-ranges need correction, or you must state clearly what subset of the null-space is used for that percentile calculation.  
- Fix the “σeff = 0.92+1.0² – 1.0² + 1.0²” style expressions so they are plain, auditable arithmetic (e.g. σeff² = 0.7² + 0.5² + …) and make sure they numerically reproduce 2.6–2.8σ when inserted into |fNL| r/σeff.

---

P2-E13 (ESSENTIAL – dimensionally and conceptually inconsistent use of the Fisher scaling check)  
Class: C  
Issue: Equation (7) in §IV introduces an “order-of-magnitude” correction to the covariance,  
\[
\delta C/C \sim f_{\rm NL}^2 \Delta_\zeta^2(k) / N_{\rm modes}(k),
\]  
and then translates this into an estimate for δσ/σ ∼ 21 δC/C. However:  
- The factor “21” is unexplained and dimensionally opaque; in a standard Fisher treatment, fractional changes in the covariance do not map to such a simple constant multiple in σ without specifying the full covariance structure and number of bins.  
- The expression mixes primordial-field power (Δζ²(k)) and a shell‑by‑shell mode count without specifying the k at which it is evaluated or the window function; the combination as written has no obvious dimensionless interpretation once one goes beyond hand‑waving.  
- You state that this is “a heuristic primordial-field scaling check rather than a galaxy-covariance derivation,” but then use the resulting ≲5×10⁻⁴ as if it were a quantitative bound ensuring that recasting the Heinrich et al. Fisher matrix around fNL = −4.375 is safe.  
Required fix: Either (i) remove the explicit numbers (21, 5×10⁻⁴) and rephrase Eq. (7) as a purely qualitative statement (“the first corrections scale as fNL² Δζ² and are therefore negligible for |fNL|≈4”), or (ii) provide a short derivation in a toy Fisher model showing how the specific bound δσ/σ≲5×10⁻⁴ arises, including the choice of k, binning, and mode count. In either case, make sure this “check” is not treated as a rigorous justification for extrapolating Heinrich et al.’s Fisher result.

---

P2-E14 (ESSENTIAL – mischaracterization of the Li vs Cai factor-of-two as fully “closed” without a concrete numeric bridge)  
Class: C, I  
Issue: Appendix A.1 now includes formal operator identities (i⟨[ζ³,L]⟩ = −2 Im⟨ζ³L⟩) and schematic Wick expansions, but there is still no explicit, *equation-by-equation* link from any concrete expression in Li et al. to the claimed “single-time-ordering half” of Cai et al.’s full result. You assert that Li compute only one time ordering and then that “after doubling, both papers’ Wick expansions agree with (A7) and reproduce fNL = −35/8,” yet:  
- No actual equation number from Li et al. is written down, no explicit integrand or shape function from Li is reproduced, and no explicit factor of 2 is demonstrated on a concrete integral.  
- The “verification” is described as “symbolic,” but this is not shown; instead the reader is asked to trust an internal script and a high-level operator identity, which is not sufficient to diagnose whether Li’s −35/16 is really exactly half of Cai’s result under Planck conventions, or whether there might be additional normalization differences.  
Required fix: Add a short subsection in Appendix A that:  
- Quotes at least one explicit Li et al. equation (their total bispectrum or cubic action in the cs=1, matter-bounce limit) and the corresponding Cai et al. expression.  
- Shows explicitly, for that example, how the single time-ordered integral in Li matches half of the commutator expression in Cai once the same c=2 normalization is used. This must include at least one explicit mode integral I_v(k₁,k₂,k₃), not only the abstract Iv symbol.  
- States clearly whether Li’s −35/16 was obtained with c=2 or c=1, and demonstrates the mapping numerically, so that a reader can reproduce the factor-of-two resolution without running your code.

---

P2-E15 (ESSENTIAL – abstract and body still implicitly treat fNL = −35/8 as “tightly determined” without a fully quantified theoretical prior)  
Class: F, H  
Issue: Despite some softening, both the abstract and §II still describe fNL = −35/8 as “minimally parameterized” and “tightly determined at leading order” with only “0.6–8%” and “∼13% amplitude scatter” caveats. However:  
- The O(ϵ) coefficient κϵ is only bounded very loosely (5.6–80) by heuristic arguments; this translates into a prior width on fNL of order 0.3–0.4, but you then *choose* σtheory=1.0 in the Bayes-factor analysis “as recommended,” without deriving this from the underlying field theory.  
- Assumption (d) (faithful cubic-order transfer through the bounce) and assumption (f) (negligible fermion torsion) are unquantified and could, in principle, shift fNL by O(1) without any current bound.  
- The Bayes-factor tables and abstract headline rely critically on the bounce prior width; calling the prediction “tightly determined” obscures the fact that σtheory is effectively a free hyperparameter chosen to be of order unity.  
Required fix:  
- In the abstract and early sections, rephrase to “minimally parameterized but currently theory-uncertain at O(1) in fNL once ϵ-corrections and bounce-transfer uncertainties are included.”  
- In §VI, be explicit that σtheory is not derived from a calculation but chosen to span the plausible effect of unknown higher-order and bounce-transfer contributions, and that a shift of order unity in fNL cannot currently be excluded.  
- Make sure the Bayes-factor discussion repeatedly reminds the reader that “tightly determined” here means “relative to the Planck error bar” rather than “derived with rigorously controlled theoretical uncertainty.”

---

P2-M9 (MAJOR – figure/body mismatches and unit ambiguities beyond N5)  
Class: B, C, J  
Issue: Several figures and their textual descriptions are not perfectly aligned, and units/normalizations are still ambiguous:  
- Fig. 2 caption refers to “effective σeff = 0.92+1.0² – 1.0² + 1.0² = 1.35–1.41,” but the body text (§IV and §VII) never defines these 0.92 and 1.0 numbers clearly. They do not map transparently onto σ(fNL)=0.7, σGR, or bϕ contributions. This violates the requirement for caption–body consistency.  
- Fig. 5 (left panel) shows “σ(fNL) vs bϕ prior uncertainty” for both MegaMapper SDB and “SPHEREx bispectrum (σ=0.7)” but the right panel is described as “corresponding detection significance for fNL=-35/8” with “SPHEREx bispectrum (5.2 template-corrected).” Nowhere is it stated clearly whether that 5.2σ includes GR and bϕ systematics or is “pre-budget.” The reader cannot tell whether the SPHEREx point in Fig. 5 should be compared to the 5.2–5.5σ optimistic or to the 2.6–5σ realistic values in Fig. 2.  
- Fig. 6 discusses σ(fNL)=0.7 for SPHEREx and σ=1.5 for MegaMapper “conservative,” but σ=1.5 does not appear in §V, which quotes 0.5 (ideal) and 0.7 (degraded) ranges; the source of σ=1.5 is not explained, and may be a stale number.  
Required fix:  
- For each figure, audit the caption vs. the relevant text section and ensure all σ values and ranges match and are explicitly defined.  
- Replace opaque quantities in captions (like 0.92 and 1.0²) with explicit σ(fNL) components or remove them and defer to the new systematics table requested in P2‑E4.  
- For MegaMapper, either derive σ=1.5 in the body text (with a clear explanation of assumptions) or remove that number from Fig. 6 to avoid confusion.

---

P2-M10 (MAJOR – internal cross-reference and version-history artifacts not fully cleaned)  
Class: D, N3  
Issue: Although you note that some “earlier version” notes are corrections, several still appear in a way that is inappropriate for a final journal article and also create cross-reference confusion:  
- In §VI and §VIII.D you have explicit “Correction note: an earlier version … quoted substantially tighter joint constraints” and similar phrasing. These are more appropriate for an arXiv v2 note than for a PRD paper.  
- References to internal scripts (e.g. “c9k gr continuous marginalization.py,” “appendix A1 wick doubling.py”) remain scattered through the text, not confined to the Data/Code Availability section. This breaks the narrative flow and makes it hard to see what is actually derived in the text vs. what is just “in the repo.”  
Required fix:  
- Move all “earlier version” comments either into a single short footnote (if they correct a previously public arXiv version) or into the cover letter; remove them from the main text.  
- Restrict all file-name references to the Data/Code Availability section, replacing them in the main text with generic phrases (“our public code validates this step; see Data and Code Availability”). Make sure cross-references to tables and equations (e.g. Table III, Eq. (7)) stand on their own without requiring the reader to inspect a script.

---

P2-M11 (MAJOR – remaining unquantified hedges in systematics section)  
Class: H, I  
Issue: Despite some quantitative statements, §VII.D still contains several unquantified or loosely quantified hedges that are then used to support the “2.6–5σ” headline:  
- “Nonlinear bias … introduces additional uncertainty” is not tied to any explicit percentage or reference (beyond b₂ marginalization).  
- “Integral constraint … potentially absorbing part of the fNL signal” is mentioned but neither estimated nor referenced.  
- Lensing magnification bias is called “particularly relevant” for MegaMapper but the actual level of contamination for SPHEREx is not quantified, even though you later say “These effects are expected to degrade the forecast … by an estimated O(10–30%).” The 10–30% is not backed by any equation or citation.  
Required fix: For each bullet in §VII.D, either:  
- Give a simple back-of-the-envelope formula showing how it leads to a 10–30% effect (e.g. reference specific results from Barreira, Addis et al., or other LSS systematics papers with numbers), or  
- Explicitly label that bullet as a qualitative caveat and remove it from any chain of reasoning that underpins the 2.6–5σ range. In particular, the “estimated O(10–30%)” sentence needs either a reference or a calculation.

---

P2-M12 (MAJOR – joint (fNL, n_fNL) forecast still not cleanly separated from main bispectrum result)  
Class: E, F  
Issue: The joint (fNL, nfNL) SDB Fisher forecast in §VIII.D is presented as a “stronger discriminator,” but:  
- It uses a completely different observable (SDB power-spectrum Fisher) from the Heinrich et al. bispectrum Fisher that underpins the main 5.2–5.5σ forecast, yet in several places the text juxtaposes the two in a way that could mislead a reader into thinking they are part of the same forecast pipeline.  
- The joint Fisher is described as “consistent in scaling with, though ≈2.2× weaker than, the bispectrum-only σ(fNL)=0.7 baseline,” but no explicit check is given (e.g. showing how SDB-only σunmarg(fNL)=1.53 arises from the same survey parameters). This is a second Fisher that is effectively black-boxed.  
Required fix:  
- Add an explicit statement near the beginning of §VIII.D that the joint (fNL, nfNL) SDB Fisher is a *separate*, schematic forecast and not directly combined with the Heinrich bispectrum Fisher in any number quoted in the abstract or Fig. 2.  
- Either sketch the SDB Fisher formula and the main survey inputs used to obtain σunmarg(fNL)=1.53 and σ(nfNL)=0.295 (similarly to the Heinrich-summary requested in P2‑M7) or clearly label the SDB joint forecast as a qualitative illustration that is not used in any quantitative decision threshold or Bayes-factor computation.

---

P2-N6 (NIT – explicit arithmetic for the ns–fNL contrast)  
Class: A, N4  
Issue: The abstract states “fNLinf ≈ 0.015 at ns=0.9649 [2] gives a contrast |fNLbounce|/|fNLinf| ≈ 290,” and §VIII.B partially elaborates, but the explicit arithmetic requested in the original nit is not fully written out. The reader has to infer that fNLinf=(5/12)(1−ns)=0.0146.  
Required fix: In §VIII.B, add the explicit step:  
“At ns=0.9649±0.0042 (Planck 2018), fNLinf=(5/12)(1−ns)=0.0146, so |fNLbounce|/|fNLinf|≈4.375/0.0146≈300 (≈290 when rounded to Planck precision).”  
This removes any ambiguity and ensures the contrast can be audited numerically.

---

If you address these new points alongside the earlier ones, the manuscript will be much closer to the level of internal numerical and logical consistency expected for PRD.