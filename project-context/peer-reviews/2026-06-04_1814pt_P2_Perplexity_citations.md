# P2 2026-06-04_1814pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 60.2s

---

I cannot perform the task as requested because the manuscript’s reference list is not included in the text you provided, and the in-text citations are all placeholders (“[?]”, “[??]”) without any identifying information. Without the actual bibliography (authors, titles, arXiv IDs, journal/volume/page, DOIs) or at least explicit in-text citation keys, I cannot cross-check:

- whether each cited work exists and matches the claimed title/venue/authors;  
- whether quoted numerical values (e.g., specific σ(fNL), Bayes factors, etc.) appear in the cited papers;  
- whether arXiv identifiers and DOIs resolve to the intended articles;  
- whether “in preparation” works have since appeared.

All of those require mapping each claim in the text to a specific, identifiable reference.

Given the constraints, I instead audit what *can* be checked from the body of the paper as provided: internal consistency of claims about the literature, obvious citation failures, and any red-flag wording the editor asked to be caught.

Below is a structured referee report under those limitations.

---

PAPER: P2  
ROUND: 2026-06-04_1814pt  
ROLE: Citation / consistency forensics, with limited information (no reference list supplied)

---

### ESSENTIAL Findings

**P2-E1 – Global: Missing and non-functional citations**  
- **Location:** Entire manuscript, especially Introduction, Secs. 2–9, Appendix; also “Data and Code Availability.”  
- **Problem:** All citations in the text are placeholders of the form `[?]` or `[??]`, with no actual reference identifiers (authors, year, journal, arXiv) and no reference list is provided. Examples (non-exhaustive):  
  - “... set by the Maldacena consistency relation [?].”  
  - “... through the growth of the curvature perturbation ζ on superhorizon scales [??].”  
  - “A distinctive prediction of the matter bounce is ... fNL = −35/8 = −4.375 [?].”  
  - “... see the companion paper [?] for the full derivation ...”  
  - “SPHEREx [?] and MegaMapper [?] — ... scale-dependent bias effect [?] and the galaxy bispectrum [?].”  
  - All known-specific references (Cai et al. 2009, Li & Brandenberger, Wilson-Ewing, Heinrich et al. 2023, Planck, DESI, etc.) have only `[?]` or `[??]`.  
- **Required fix:**  
  - Provide a complete, properly formatted PRD-style reference list.  
  - Replace every `[?]` / `[??]` with the correct numbered citation, ensuring one-to-one mapping between statements and references.  
  - After the bibliography is available, a second-pass citation audit is required (to check that numbers match, arXiv IDs and DOIs are correct, and quoted results are faithful). In the current state the paper is not citable or refereable on the literature side.

---

**P2-E2 – Abstract and Sec. 4: SPHEREx bispectrum forecast attribution and value (Heinrich et al. 2023)**  
- **Location:**  
  - Abstract, lines: “The SPHEREx multi-tracer galaxy bispectrum achieves σ(fNL) ≈ 0.7 (Heinrich et al. 2023)…”  
  - Sec. 4: “A dedicated multi-tracer bispectrum analysis [?] forecasts σ(fNL) = 0.7 from the bispectrum alone, with σ(fNL) = 0.5 when combined with the power spectrum.”  
- **Problem:**  
  - You explicitly attribute σ(fNL) ≈ 0.7 to “Heinrich et al. 2023”. However, without the reference list, I cannot check which exact Heinrich et al. paper is meant. Existing SPHEREx PNG forecasts in the literature often report values in the ∼0.7–1.0 range for the bispectrum under specific assumptions, but details vary. It is not possible to verify that:  
    - 0.7 is indeed a *bispectrum-only, multi-tracer* number in the cited work;  
    - 0.5 is indeed the *combined bispectrum+power spectrum* forecast from the same study;  
    - the redshift range, tracer selection, bias model, and GR/systematics assumptions match your usage.  
  - The text also says in the Data and Code section: “No new observational data are introduced; all forecast sensitivities are adopted from published analyses [??].” This again is uncitable without properly specified references and makes it impossible to trace the provenance of σ = 0.7 and σ = 0.5.  
- **Required fix:**  
  - Explicitly identify “Heinrich et al. 2023” with a full reference (arXiv ID, journal, title).  
  - Verify from that paper that the quoted σ(fNL) = 0.7 (bispectrum only) and 0.5 (bispectrum+power) appear there, with the same assumptions (multi-tracer, redshift ranges, etc.). If they differ or correspond to a different setup, adjust the numbers or qualify the statement (e.g., “for the fiducial setup in [Heinrich+ 2023] with … we adopt σ(fNL) ≃ X”).  
  - Make explicit in the text which assumptions from the cited forecasts you are adopting (e.g., photo-z performance, bias parameters, GR treatment), or state that you re-cast their Fisher matrix; then this re-casting becomes a *new* calculation which must be described clearly.

---

**P2-E3 – Sec. 2.3 and Appendix A: Normalization / factor-of-two discrepancy between Cai et al. and Li & Brandenberger**  
- **Location:**  
  - Sec. 2.3, paragraph describing Li et al. “A factor-of-two discrepancy exists in the literature: Li et al. [?] obtain fNL = −35/16 = −2.19 … The factor of two resides in the momentum-dependent polynomial terms …”  
  - Appendix A: “The factor-of-two discrepancy between fNL = −35/8 (Cai et al. [?]) and fNL = −35/16 (Li & Brandenberger [?]) arises from differing bispectrum normalization conventions. … The physical bispectrum amplitude Bζ is identical in both conventions: 2 × (−35/8) = 1 × (−35/4).”  
- **Problem:**  
  - These are quite specific, technical claims about two concrete papers (Cai et al. 2009 and Li & Brandenberger) and their conventions. Without the exact references and arXiv IDs, I cannot verify:  
    - that *Cai et al. 2009* indeed gives the quoted intermediate equations 34–37, with coefficients (3,1,−9,5,−66,9) and final normalization −35/8;  
    - that *Li & Brandenberger* indeed quote −35/16 at cs = 1 and use a different c in the local template definition;  
    - that your explanation of the discrepancy (single-time-ordering vs. full in-in commutator) is correct and not mixing two different conventions (e.g. overall factor vs. different Planck-normalization definition).  
  - The statement “The physical bispectrum amplitude Bζ is identical in both conventions: 2 × (−35/8) = 1 × (−35/4)” is dimensionally and logically inconsistent as written: −35/8 and −35/4 differ by a factor 2, not by 1, and it is unclear which paper is expected to have −35/4. Appendix A currently mixes: fNL = −35/8; fNL = −35/16; and “−35/4” without clearly tracking which is which.  
- **Required fix:**  
  - Provide full references to the two papers (Cai et al., Li & Brandenberger), including arXiv IDs.  
  - Explicitly quote the relevant equations (with equation numbers) from each paper in a way that can be checked against the published versions (e.g., “Eq. (37) of Cai et al. (arXiv:XXXX.YYYY) gives …”).  
  - Check and correct the arithmetic and wording in Appendix A. For example, if:  
    - Planck convention uses c = 6/5 or c = 2 depending on your definition, write this explicitly and show how fNL transforms;  
    - Li & Brandenberger define fNL with c = 1, verify what their quoted number is and write the explicit conversion.  
  - Remove any ambiguous or incorrect numeric statement such as “2 × (−35/8) = 1 × (−35/4)” if it is not a faithful representation of the cited works. Replace with a clear mapping: “Cai et al. quote fNL = X in convention A; Li & Brandenberger quote fNL = Y in convention B; when translated to Planck convention this becomes …”.  
  - Because the normalization is central to your entire forecasting and Bayesian comparison, this is *critical*: the paper cannot be accepted unless this normalization is demonstrably correct relative to the source papers.

---

**P2-E4 – Sec. 2.1, Table 1: “All values match the published results [?] exactly.”**  
- **Location:** Sec. 2.1, text near Table 1.  
- **Problem:**  
  - You claim that the numerical values in Table 1 (squeezed, equilateral, folded) match Cai et al.’s published results *exactly*, but do not provide a specific citation (equation or table) and, because the reference list is missing, I cannot verify which “published results” you are referring to.  
  - Given the sensitivity of normalization issues and the factor-of-two discussion earlier, this is a strong claim that must be traceable to explicit numbers in a paper or to a clear conversion procedure from a known convention.  
- **Required fix:**  
  - Cite the exact equation/table in the paper you are comparing with (e.g., “compare our Table 1 to Table X of Cai et al. (2009)”), and ensure that the conventions (definition of |B|NL, normalization of Pζ, etc.) match.  
  - If the other paper quotes results in a different fNL convention or with different normalization, show the conversion in a short footnote or appendix line so the “exact match” is transparent.  
  - Once the reference list is supplied, check that your Table 1 values correspond numerically to the cited source.

---

**P2-E5 – Sec. 2.3: Statement “Assumption (d) has been verified at linear order [?].”**  
- **Location:** Sec. 2.3, paragraph discussing bounce transmission.  
- **Problem:**  
  - “Assumption (d) has been verified at linear order [?].” refers to transmission of perturbations through the bounce (presumably some LQC or Einstein–Cartan calculation) but gives no identification of the work. This is a strong assertion about linear perturbation evolution through a nonsingular bounce and must be traceable to a specific paper.  
  - Without a reference, it is impossible to check whether the cited work indeed deals with linear perturbations in the same model (Einstein–Cartan-Holst or LQC) and what assumptions it uses.  
- **Required fix:**  
  - Provide a precise citation (author, year, arXiv ID) that deals with linear-order perturbation propagation across the bounce in the model you are considering.  
  - Confirm that that work actually “verifies” assumption (d) in the sense you mean (e.g., shows no large transfer function or instability for the relevant modes). If it does not, rephrase more modestly (e.g., “is consistent with”).  

---

**P2-E6 – Sec. 2.4 and Sec. 8.2: Wilson–Ewing quasi-dust model claims and fNL–ns relation**  
- **Location:**  
  - Sec. 2.4 “The Wilson-Ewing ΛCDM quasi-dust model [?] provides a complete observational package: ns = 0.964 (from w = −0.003, one free parameter; the spectral index formula ns = 1 + 12w for w < 0 follows from the growing-mode solution in quasi-dust contraction [?]), r ≈ 10−4 … and fNL = −35/8 … This model has no current observational tensions.”  
  - Sec. 8.2: explicit formula for ns(ε) and fNL(ε) and the statement that “The Wilson-Ewing quasi-dust model connects the spectral tilt and non-Gaussianity through a single parameter ε ... The consistency relation is nonetheless conceptually significant … Standard multifield inflation has no equivalent.”  
- **Problem:**  
  - These formulas and the assertion that the model has “no current observational tensions” rely on specific results from Wilson–Ewing and related quasi-dust papers. Without the references, I cannot check:  
    - That Wilson–Ewing indeed uses w ≃ −0.003 to achieve ns ≃ 0.964 via ns = 1 + 12w;  
    - That r ≈ 10−4 follows from LQC tensor suppression as stated;  
    - That the model is not constrained by Planck+BICEP constraints on r or other observables.  
  - The explicit fNL(ε) expansion and bounds on the coefficient c1 (c1 ≈ 2 to 18, giving c in [−0.7, −10]) appear to be new derivations by the author. If they are instead drawn from a specific paper, it must be cited. If they are new, then they *cannot* be attributed implicitly to Wilson–Ewing unless checked.  
- **Required fix:**  
  - Provide the explicit Wilson–Ewing reference(s) (arXiv IDs, journal) that define the quasi-dust model and its predictions for ns, r, and fNL.  
  - Check that your quoted values (ns, r) align with those papers and that they indeed claim “no current observational tensions.” If the phrase “no current observational tensions” is your own summary of compatibility with Planck/other data, state this as your own assessment and cite Planck+other data used for that comparison.  
  - Clarify whether the fNL(ε) formula and its linear expansion are *your* calculations or already appear in the literature; in either case, the origin of each term must be explicit.  

---

**P2-E7 – Sec. 6.1: Specific statements about non-attractor inflation, curvaton bounds, and tuning**  
- **Location:** Sec. 6.1 “Can Inflation Reproduce the Signal?”  
- **Problem:**  
  - You make several literature-linked claims:  
    - “Non-attractor single-field inflation naturally gives fNL = +5/2 (wrong sign) [?].”  
    - “The standard quadratic curvaton gives minimum fNL ≈ −1.25 (insufficient). Self-interacting curvatons or curved field-space models can reach −4.375 but require ≥ 2 tuned parameters.”  
  - Without proper citations (e.g., specific non-attractor and curvaton papers), these cannot be checked. Furthermore, the precise bound “minimum fNL ≈ −1.25” and the number of parameters required in self-interacting/curved-field models are not trivial and must be supported by literature.  
- **Required fix:**  
  - Add explicit references to standard non-attractor inflation and curvaton analyses where these numbers are derived (including equations or table references).  
  - Ensure that the numerical values (e.g., fNL = 5/2, fNL ≈ −1.25) are consistent with those sources. If you are re-deriving them under specific assumptions that differ from the literature, state those assumptions and make clear that the results are your own, not directly quoted.

---

**P2-E8 – Sec. 8.1: “Planck + DESI Recast” numerical constraint**  
- **Location:** Sec. 8.1: “The combined constraint on the bounce-template amplitude is fNL^bounce = −1.3 ± 4.5, which is 0.7σ from the bounce prediction and 0.3σ from zero—fully consistent with both.”  
- **Problem:**  
  - You state a very specific combined constraint from “Planck (CMB bispectrum) and DESI DR1 (scale-dependent bias)” but do not specify which Planck release (2018?), which DESI analysis, nor how the recast was performed. There is no citation or methodological description. As a result:  
    - It is impossible to verify that DESI DR1 actually has a scale-dependent-bias fNL analysis with the stated uncertainty;  
    - It is impossible to confirm that the recast to the bounce template was done consistently with the Planck/DESI conventions (including template overlap, covariance, and priors).  
- **Required fix:**  
  - Provide explicit references for the Planck bispectrum analysis and the DESI DR1 SDB analysis used.  
  - Either summarize the method you use to combine and recast them (e.g., via overlap factors r, etc.) with enough detail for reproducibility, or clearly label this as a new analysis to be detailed in the methods.  
  - Check the numbers against the cited analyses to ensure compatibility.

---

**P2-E9 – “Companion paper” references without identification**  
- **Location:**  
  - Introduction: “see the companion paper [?] for the full derivation and structural barrier catalog.”  
  - Sec. 9.4: “An independent observable—cosmic birefringence from a Planck-scale ALP …—is analyzed in the companion paper [?].”  
- **Problem:**  
  - You refer to a “companion paper” at least twice, presumably your own work on Einstein–Cartan-Holst bounce and on cosmic birefringence. This paper is central to the argument (e.g., derivation of perturbation sector, structural barriers, birefringence analysis), but is neither cited nor identified (no title, no arXiv ID, no journal).  
  - If the companion paper is *in preparation* or only on a personal web page, that should be made explicit. If it is on arXiv, it must be cited properly.  
- **Required fix:**  
  - Provide full citation(s) for the companion paper(s), including arXiv ID or journal if available.  
  - If the companion is not yet public, downweight dependence on its results in this PRD paper or, at minimum, clearly mark which statements rely on unpublished work and are therefore less secure. It is generally undesirable to rely heavily on “in preparation” work for key steps (e.g., the full derivation of the perturbation sector).

---

### MAJOR Findings

**P2-M1 – Abstract: Claims about Bayesian model comparison and Bayes-factor ranges**  
- **Location:** Abstract: “... finding that a detection near fNL = −4.375 would favor the bounce over tuned multifield competitors at Bayes factor ∼ 8–17 (depending on prior assumptions) and over standard single-field inflation at Bayes factor ≫ 1; the precise values are prior-dependent (see Sec. 6).”  
- **Problem:**  
  - These Bayes-factor ranges are explicitly linked to Sec. 6 and to prior assumptions on multifield competitors and on the bounce-theory uncertainty. Sec. 6 references prior ranges like [−15,15] or [−5,5], σtheory = 1.0, etc., but none of these choices are justified with literature statements, nor are the competitor models explicitly cited.  
  - Because the Bayes factors themselves are sensitive to the prior widths and model-class definitions, the headline numbers in the abstract need solid methodological and bibliographic grounding. As currently written, there is insufficient citation support to independently verify that these Bayes factors are consistent with the chosen models.  
- **Required fix:**  
  - In Sec. 6, provide citations for the chosen parameter ranges or at least for representative multifield models whose natural fNL ranges you are encoding.  
  - Make clear in the abstract that the quoted numbers are conditional on very specific prior ranges and theory error assumptions; the phrase “depending on prior assumptions” is there but too generic.  
  - Once citations are added, cross-check that the competitor-prior ranges and the delta-function vs. Gaussian bounce prior are reasonable relative to the cited model classes.

---

**P2-M2 – Sec. 7 and Fig. 5: bφ prior assumptions and degradation from forecasts**  
- **Location:** Sec. 7.2 and Fig. 5.  
- **Problem:**  
  - You claim: “Our forecast assumes a 20% Gaussian prior on bφ, which is optimistic. Fig. 5 shows how σ(fNL) degrades as the bφ prior widens: at 20% prior width, MegaMapper SDB gives σ(fNL) ≈ 1.0; at 50%, σ ≈ 2.2; if bφ is completely unconstrained, σ → ∞…”.  
  - There is no citation for the 20% prior assumption or for the behavior of σ(fNL) with bφ prior width. These are stated as if supported by “the literature” but appear to come from your own Fisher calculation. This should be clearly presented as an internal calculation rather than an external result.  
- **Required fix:**  
  - Explicitly state that these numbers are from your own Fisher forecast, not from a specific prior publication, unless there *is* a paper that has exactly these results, in which case cite it.  
  - Clarify what external work, if any, motivates the choice of a 20% bφ prior; if none, state it as a hypothetical optimistic scenario.  
  - Ensure the figure caption explains that this is a new Fisher exercise and not a direct reproduction of any cited reference.

---

**P2-M3 – Sec. 8.2: Bound on coefficient c1 and range for c in fNL(ns) relation**  
- **Location:** Sec. 8.2.  
- **Problem:**  
  - You state: “c1 is bounded: explicit prefactor scaling gives c1 ≈ 2 (lower bound), while including the mode-function amplitude change gives c1 ≈ 18 (upper bound).” and “c ∈ [−0.7, −10]”. These appear to be estimates from your own analytic/numerical work, but no details or references are provided.  
  - Without any methodology presented, these bounds are not verifiable, yet they are used to claim that fNL(ns) is in [−4.35, −4.02] at Planck ns.  
- **Required fix:**  
  - Either:  
    - Provide a methodological sketch and/or a cross-reference to the companion paper where these bounds are derived, or  
    - Downplay them as order-of-magnitude estimates rather than precise bounds.  
  - In either case, the text must clearly identify whether these are new results of this paper and not attributed to existing literature.

---

### MINOR Findings

**P2-m1 – Version-history language in title block**  
- **Location:** Title page: “March 24, 2026 — v1.6.0”  
- **Problem:**  
  - A version tag “v1.6.0” is a clear internal versioning / code-like label. The instructions explicitly ask to flag “version-history language, internal audit tags, or review-log artifacts.”  
- **Required fix:**  
  - Remove “v1.6.0” from the date line for the journal submission. If versioning is helpful for arXiv, it can remain in the arXiv version but is not appropriate in the PRD final manuscript.

---

**P2-m2 – “We assign 92% confidence to this normalization” (Sec. 2.3)**  
- **Location:** Sec. 2.3, last sentence of the normalization discussion.  
- **Problem:**  
  - “We assign 92% confidence to this normalization.” This number appears arbitrary; no method is given for how 92% was computed (is it from a Bayesian model of conventions? some Monte Carlo? subjective assessment?).  
- **Required fix:**  
  - Either remove the numeric “92%” or explain explicitly how it was obtained. If it is purely subjective, it should not be quantified as a percentage in a PRD methods paper.

---

**P2-m3 – Potential ambiguity: “Bayes factor ≫ 1” in abstract vs. specific numbers later**  
- **Location:** Abstract vs. Sec. 6 and Table 3.  
- **Problem:**  
  - The abstract states “over standard single-field inflation at Bayes factor ≫ 1” but later Sec. 7.3 gives specific Bayes factors vs. SSFSR (e.g. 329 with σGR=1 and much larger in ideal case). There is no inconsistency, but the abstract could be more concrete for SSFSR too, in line with the tuned-multifield numbers.  
- **Required fix:**  
  - Not strictly necessary, but consider using a specific representative value or a range for SSFSR in the abstract (e.g., “Bayes factor of order 10^2–10^6 depending on GR treatment”), matching the later tables.

---

**P2-m4 – Abstract accuracy vs. paper content**  
- **Location:** Abstract.  
- **Problem:**  
  - The abstract claims: “We perform a Bayesian model comparison using over 600,000 Monte Carlo realizations across analytic, mock-based, and GR-aware frameworks...” and “A null result from SPHEREx would disfavor the quasi-dust matter bounce benchmark under assumptions (a)–(e) at > 4σ significance.”  
  - The body text qualitatively supports these claims, but the methodological detail for “mock-based” and “GR-aware” realizations and for the “>4σ” null constraint is extremely brief. The abstract slightly overstates the level of methodological detail provided in the current draft.  
- **Required fix:**  
  - Ensure Sec. 6 and Sec. 7 contain sufficient methodological description that a reader can understand the three frameworks and the null-test significance computation. Alternatively, slightly soften the abstract phrasing to reflect that details are given at a schematic rather than fully worked-out level.

---

### NIT-level Findings

**P2-n1 – “SPHEREx (launched 2025; first all-sky survey completed December 2025)”**  
- **Location:** Sec. 9.1.  
- **Problem:**  
  - These are hard factual claims about launch and survey completion dates. They must match the actual mission status at the time of publication; currently they read as predictions.  
- **Required fix:**  
  - Before final publication, update these to the factual mission status (launch date, early operations) or phrase them conditionally (“scheduled to launch in …”).

---

**P2-n2 – Edge-case wording about “no dedicated HPC resources were required”**  
- **Location:** Acknowledgments.  
- **Problem:**  
  - This is cosmetic, but such statements are unusual for PRD and not scientifically relevant.  
- **Required fix:**  
  - Optional: remove or condense if space is an issue.

---

**Checks requested but not applicable with current material**

- **σ-values on incompatible scales (Instruction 7):**  
  All σ(fNL) values are forecasted in “σ(fNL)” units and while you mix results from different surveys and procedures, you generally qualify them (e.g., SPHEREx bispectrum vs. SDB vs. MegaMapper). I do not see an *obvious* case where σ from a completely different null procedure is directly combined without qualification, but a firmer judgment requires seeing which numbers are truly imported from the literature vs. your own Fisher forecasts. Once the reference list is available, this must be re-checked carefully.

- **Duplicate phrases (Instruction 9):**  
  I did not notice obvious duplicated phrases like “canonical canonical-mask” in the provided text.

- **Inflated claims vs. what the paper proves (Instruction 10):**  
  The abstract largely reflects what is in the body: forecasts, overlap computations, and Bayesian comparisons. However, because key citations are missing, claims about “adopted from published analyses” and specific σ-values from named papers cannot yet be independently verified.

---

## Page-length assessment

You state the paper is 12 pages for a methods/catalog-type contribution (PRD typical 15–30 pages). Based on the provided text, the length is not excessive relative to the conceptual and methodological content (bispectrum normalization, template mismatch, Fisher forecasts, Bayesian comparison, GR/systematics). If anything, some methodological details (e.g., in the Monte Carlo Bayes-factor pipeline and in the recast of Planck+DESI constraints) could be expanded slightly once citations are properly given. I see no need to reduce the page count; 12 pages is reasonable.

---

## Summary recommendation

**MAJOR REVISIONS**

The central scientific ideas are coherent, but the manuscript as provided is bibliographically non-functional: all references are placeholders (“[?]”), so no citation can be verified, no quoted numbers can be traced to the literature, and key normalization arguments (Cai vs. Li & Brandenberger, Wilson–Ewing model properties, SPHEREx/MegaMapper forecasts) cannot be independently checked. At a minimum, a complete and accurate reference list with correct mapping of in-text citations must be supplied, and the normalization/convention arguments and key imported σ-values must be explicitly cross-checked against the cited papers. Only then is a proper citation forensics audit possible, and only then can the paper be considered for acceptance.