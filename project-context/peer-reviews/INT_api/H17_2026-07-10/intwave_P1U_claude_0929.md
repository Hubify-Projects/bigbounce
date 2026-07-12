# INT Claude-subscription Review — P1U v1U.0.19 — claude-opus-4-8
paper: P1U  version: v1U.0.19  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T16:29:37Z
context-note: v1U.0.19 DP1U presentation overhaul re-test: abstract repetition purge, barrier catalog consolidated to route-mapped list, appendix E/F/G mechanics reframed supplementary; all numbers byte-preserved

======================================================================
RAW RESPONSE (verbatim):
======================================================================

All numeric claims verified against committed artifacts (NJL: 8/8 confirmed via `njl_gap_equation_route1_results.json`; BS running 1.4e-6 reproduced by hand; R4 overshoot 22/36 OOM and ρ_θ≈6ρ_Λ, R2 ~1e-60 confirmed by my own arithmetic). I have read the abstract, intro, all four routes, the barrier catalog, the transparency proof, the structural-tension, R4, NJL/Fierz/dim-4 appendices, limitations, and conclusions.

Here is my referee report.

---

**(1) VERDICT: MAJOR REVISIONS**

The manuscript is numerically clean and unusually honest about its own scope — every number I checked reproduces from committed artifacts, and no mathematical or dimensional error survives. My concerns are not correctness but **significance framing, the "closure" claim word, and presentation**, which for a PRD submission are substantive enough to require another round.

**(2) ISSUES**

1. **[MAJOR] Delivered rigorous content vs. scaffolding.** The paper itself concedes (`arxiv/paper1_unified.tex:3651–3653`) that "the two sharp, first-principles results in the catalog are the Route-1 torsion-elimination derivation and the perturbation-transparency theorem (B14)." The former is the textbook Hehl–Datta result; the latter (§`sec:transp_proof`, L3950–3985) is correct but elementary (zero spin → T=0 → single-curvature Holst dual ε^μνρσR_μνρσ=0 by the first Bianchi identity). Everything else is explicitly labeled ansatz-level (Tier III), naturalness (Tier II), "heuristic" (B9, L3860), or "structural/philosophical" (B13, L3893). A referee must ask whether the genuinely new physics justifies a standalone PRD paper; the significance case needs to be made on the two Tier-I results, not the 13-barrier apparatus.

2. **[MAJOR] "Amplitude closure" overstates R2–R3.** The title (L1250) and abstract (L1267) assert "amplitude closure for R1–R3," yet the text repeatedly concedes the R2/R3 coefficients are *not derived*: R2 is "an illustrative upper-bound amplitude budget … not a result extracted from Mercuri" (L3028–3033) and R3 uses an ansatz "we do not claim … taken verbatim" (L3063–3065). Calling an ansatz-bounded route "closed" in the title/abstract is a stronger word than the delivered content. Recommend the headline claim word for R2/R3 be downgraded to "amplitude-suppressed under stated ansätze" consistently, or the ansatz status be moved into the title.

3. **[MINOR] Internal order-of-magnitude inconsistency in H₀/M_Pl.** Written as "~10⁻⁶⁰" at L2639 but "~10⁻⁶¹" at L2991 and L3808; the true value is 1.2×10⁻⁶¹. Harmless to the ≳60-order margins but a careful referee will flag the mismatch.

4. **[MINOR] Abstract length and repetition.** Despite the stated DP1U repetition purge, the abstract (L1259–1383) still runs ~120 lines and restates the "channel-level, not operator-level" scope at L1281, L1285, L1443-equivalent, and L1478. PRD abstracts are expected to be a single compact paragraph; this remains well over length and self-repeating.

5. **[MINOR] Companion-import verifiability.** Load-bearing-adjacent numbers (e.g. f_NL=−35/16 provenance, L1357–1361) are imported from Papers II/III/IV, "posted concurrently" but not yet public (L1491). The paper correctly flags them non-load-bearing, but a referee cannot audit the −35/16 Cai–Li factor-of-2 resolution from this manuscript alone; a self-contained one-line derivation or an archived artifact reference would close this.

6. **[MINOR] Scope breadth dilutes focus.** A theoretical no-go paper carries galaxy-spin data methods (§`sec:data_galaxy`), a ΛCDM+ΔN_eff MCMC appendix, a NaMaster E→B pipeline appendix, and an ALP-fit appendix (App. F–H). Given a dedicated companion exists, consider relegating these to the companion to sharpen the paper around its two Tier-I results.

**(3)** The central claim is supported *at exactly the strength the paper claims it* — the perturbation-transparency theorem and R1 amplitude/NJL-condensate exclusion are correct and error-free, but the broader "four-route closure" is established only at the explicitly-labeled channel/ansatz level, not as the operator-level no-go the title's "closure" language may suggest to a reader.
