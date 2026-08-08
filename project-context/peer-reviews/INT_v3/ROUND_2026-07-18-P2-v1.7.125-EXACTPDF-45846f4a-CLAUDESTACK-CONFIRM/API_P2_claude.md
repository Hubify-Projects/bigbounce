# INT Referee Report — Paper P2

- **Model:** claude-opus-4-8 (subagent, independent referee leg)
- **Date:** 2026-07-18 (PT)
- **Paper:** P2 v1.7.125 — "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping"
- **pdf_sha256:** `45846f4ac780ac4663ef24a6e5d48c4924e4691b057a0cf7683399f48d534490`
- **Venue:** Physical Review D (profile PRD-RESEARCH)
- **PARSED VERDICT:** MAJOR REVISIONS

---

## Referee Report (raw, verbatim)

You are an expert referee for Physical Review D. Review this Research Article manuscript under profile PRD-RESEARCH to the standard of a real submission.

### (1) VERDICT: MAJOR REVISIONS

### (2) ISSUES

1. **[MAJOR] Provenance of the "correction" — factor-of-2 vs additive-term inconsistency (Sec. II A/B, Appendix B, Table I).** Table I's caption states the corrected benchmarks are *exactly one-half* of Cai et al.'s published amplitudes across all three configurations (squeezed −35/16 = ½·(−35/8), equilateral −255/128 = ½·(−255/64), folded −9/8 = ½·(−9/4)). A uniform factor of exactly 1/2 across squeezed/equilateral/folded is the signature of a global normalization or symmetry-factor difference (e.g. a factor of 2 in the definition of f_NL, the bispectrum normalization, or the number of Wick/leg permutations). Yet the paper simultaneously attributes the discrepancy to an additive shape-function term −(99/128)Σk_i³, which contributes a *constant* B_NL shift of (10/3)(−99/128) = −165/64 independent of configuration. These two mechanisms are mutually incompatible: an additive constant B_NL shift cannot reproduce a uniform multiplicative factor of 2 across three distinct shapes. The paper juxtaposes both facts in the Table I caption and Appendix B without reconciling them, leaving open the alternative that −35/8 is simply Cai et al.'s value in a self-consistent convention rather than an error. Since "corrects the unreproduced printed −35/8 literature value" is the abstract's headline, this tension must be resolved: either demonstrate the factor of 2 is not a convention (e.g. by fixing the bispectrum/f_NL normalization identically to Cai's and re-deriving), or soften the correction claim.

2. **[MAJOR] Independence of the cross-checks is overstated (Appendix B, "four independent ways").** The vertex-sum polynomial, Cai's ε-order-grouped intermediates (A^ε, A^{ε²}, A^{ε³}), and the per-vertex Table V column sums are all the *same* computation performed on Cai et al.'s four transcribed vertex expressions, merely re-grouped; they cannot independently validate those inputs. The single genuinely independent anchor is Li et al.'s general-c_s formula (their Eq. 5.1) evaluated at c_s = 1. One independent formula is thin support for overturning a published value. Moreover the claim that Li et al.'s "generalized single field with an extended no-go theorem" construction reduces *exactly* to Cai et al.'s standard matter bounce at c_s = 1 (same operator content, same background) is asserted but not demonstrated; the agreement could be coincidental to the squeezed local coefficient. The paper's own framing ("trusted-expression provenance… deliberately bounded… Cai's four source-level vertex expressions are trusted inputs") concedes the entire chain is conditional on the correctness of the transcribed inputs.

3. **[MAJOR] The observational half yields no defensible number (Sec. III–VIII; Tables II–III; Fig. 2).** The reported significance spans 0.42σ → 3.5σ across nuisance treatments (Table III) — more than an order of magnitude — so the SPHEREx mapping constrains nothing. This is compounded by the acknowledged unavailability of the true per-triangle SPHEREx covariance (only the scalar σ(f_NL^local) ≈ 0.7 from Heinrich et al. is used, wrapped in an in-house squeezed-dominated surrogate that the text repeatedly says "does not replace" the real covariance), and by current data (Planck PR4 → 0.37σ) being consistent with both −35/16 and zero. The section is honest but presents a ladder of explicitly non-headline σ values with no takeaway a reader can use; it should be substantially trimmed or reduced to a single clearly-bounded statement rather than four competing significances.

4. **[MAJOR] Load-bearing assumption (d) undercuts the entire mapping (Sec. II C, III, IX).** Every observational statement is conditional on faithful *third-order* cubic transmission through the nonsingular bounce. The paper concedes this is established only at *linear* order, in a *single* scheme (dressed-metric / Wilson–Ewing), and "a fully nonlinear third-order branch calculation remains open," with explicit scheme dependence (dressed-metric vs deformed-algebra carry different subleading structure). The chain from the −35/16 contraction-phase amplitude to any late-time observable therefore rests on an unproven, scheme-dependent assumption. Given the paper markets the amplitude as testable via SPHEREx, this limitation should be foregrounded in the abstract/intro, not deferred to Sec. II C.

5. **[MINOR] Torsion "bound" Eq. (5) is a heuristic estimate, not a bound (Sec. II C).** It is built on an "asserted energy-density transfer proxy" |δf_NL^tor| ≲ f_NL · ρ_tor/ρ (explicitly "not derived in in-in propagation") and a spin-coherent proxy ⟨J_5²⟩ ≲ n²_ψ. The word "bound" overstates what is an order-of-magnitude parametric estimate; relabel as an estimate.

6. **[MINOR] Abstract "local-type … f_NL^local = −35/16" vs. the demonstrably non-local full shape.** Fig. 1 / Table I show the shape is configuration-dependent (equilateral −255/128, folded −9/8); the −35/16 is the squeezed limit only. This is correct in the standard f_NL^local convention and disclosed in Sec. III B, but the abstract should note the amplitude is the squeezed limit of a shape that is not purely local, to prevent over-reading.

7. **[MINOR] Three inconsistent numerical objects coexist without a reconciling summary (Appendix B).** The exact vertex sum (−35/16), Cai's printed-polynomial squeezed limit (−305/64), and Cai's separately-stated value (−35/8) all differ from one another. The paper openly declines to reconstruct how −35/8 arose, but the reader is left to track three numbers across several paragraphs; a small reconciliation table (object → squeezed value → relationship) would materially improve auditability.

8. **[MINOR] Certification is entirely symbolic on transcribed inputs (Data & Code Availability).** The load-bearing artifact (scripts/p2_vertex_check.py and companions) re-sums Cai's transcribed vertex expressions in SymPy; there is no independent re-derivation of the cubic action or the in-in integral from the matter-bounce Lagrangian. A transcription error in the trusted inputs would propagate undetected. An independent from-Lagrangian check (even partial) would substantiate the "exact" claim beyond re-summation.

### (3) Is the central claim supported?

The narrow algebraic claim — that the exact four-vertex-sum squeezed limit is f_NL^local = −35/16 at c_s = 1 — is internally consistent (Table V column sums, the ε-decomposition −5/2 + 5/16 + 0, and the (5,2,2) ordered-vs-distinct bookkeeping all check out) and is corroborated by Li et al.'s independent c_s formula; but the stronger headline that this *corrects* Cai et al.'s published −35/8 is only partially supported, because the uniform factor-of-2 pattern is left unreconciled with the additive −(99/128)Σk_i³ diagnosis and the correction rests on a single genuinely-independent cross-check.

---

*End of report.*
