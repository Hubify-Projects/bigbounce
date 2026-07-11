I've now read the full manuscript (abstract, all body sections, systematics tables, and Appendix A with the Cai–Li resolution). Here is my referee report to PRD standard.

---

**(1) VERDICT: MAJOR REVISIONS**

To be explicit up front: I found **no computational error and no fabrication**. Every significance and Bayes-factor number I could check by hand reconciles (see below), and the headline theory value −35/16 is independently corroborated. The "major" designation is driven by **presentation/format non-compliance and one load-bearing methodological disclosure**, not by a wrong result. A strict PRD editor would return this for substantial condensation before acceptance; the science itself is close to sound.

**Arithmetic I verified independently (all consistent):**
- Li et al. Eq. 5.1: −165/16 + 65/(8c_s²) → −165/16 + 130/16 = **−35/16** at c_s=1 ✓ (decisive independent check of the central value)
- ε-order grouping: −5/2 + 5/16 + 0 = −35/16 ✓; L_ζζ̇² squeezed = (10/3)(−3/64) = −5/32 ✓; vertexwalk column sum −35/16 ✓
- Spurious-term shift: (10/3)(−99/128) = −2.578; −35/16 − 2.578 = −305/64 ✓
- 3.13σ, 2.63σ (r=0.84), 2.74σ (r=0.876), 1.5σ GR-floor ✓
- BF vs SSFSR exp[(35/16)²/(2σ_eff²)]: 1.4×10² at σ_eff=0.7, ~5 at σ_eff=1.22 ✓
- n_s = 8ε−11 from n_s=1+12w, ε=3(1+w)/2 ✓; w=−0.003 ↔ n_s=0.9649 ✓

I did **not** re-run the sympy certifications (`p2_vertex_check.py`, `cai_vertices.py`) or verify the Table VIII (`tab:vertices`) transcription against arXiv:0903.0631 — those I take on the paper's representation. The downstream algebra built on them is internally consistent.

**(2) ISSUES**

1. **[MAJOR] Abstract violates PRD format norms** (lines 900–911). The abstract is five dense paragraphs with inline displayed equations, embedded caveats, and multiple overlapping σ ranges. PRD abstracts are a single ~150-word paragraph. This requires a genuine rewrite, not a trim, and combined with heavy body redundancy (the r vs r_cos vs r_eff vs r=0.85±0.13 disambiguation is repeated ~6×) is the single largest obstacle to acceptance.

2. **[MAJOR] The conservative endpoint of the headline significance rests on a proxy correlation, not a channel-native marginalization** (line 1266; `tab:systematics` rows at lines 1364–1365). The 1.3σ floor (and 0.8σ lower edge) use ρ=−0.868 transferred from a *power-spectrum* SDB Fisher (`c8`) and an in-repo |ρ|≈0.95 *shape overlap*, because Heinrich's per-triangle bispectrum covariance Cov_B is not public (lines 1266, 1472). This is disclosed thoroughly and the whole budget is labeled a "scoping envelope," but the lower bound the abstract headlines is not derived from a self-consistent bispectrum-channel Fisher. Either (a) compute the channel-native σ_marg once a covariance surrogate is adopted, or (b) state in the abstract that the 1.3σ floor is proxy-based.

3. **[MINOR] The "resolution" of Cai's −35/8 is incomplete (and disclosed as such)** (lines 901, 1489–1492, 1554). The transcribed printed polynomial reduces to −305/64, **not** to Cai's stated −35/8, so the paper establishes the *correct value* robustly but does not reconstruct Cai's specific error. The intro/abstract framing ("resolve the long-standing factor-of-two discrepancy") slightly outruns what is shown; the honest claim is "we certify −35/16 four ways; −35/8 is an unreproduced erroneous literature value." Tighten the framing accordingly.

4. **[MINOR] Citation author-name inconsistency** — `\cite{Jolicoeur:2025}` is attributed to "**Addis et al.**" at line 1294 but cited unnamed at lines 1122 and 1326. Verify the first author against `focused_paper_refs.bib`; one form is wrong.

5. **[MINOR] Reference-year inconsistency** — prose says "Heinrich et al. **2024**" (lines 1158, 1393) while the bibkey and all `\cite` calls are `Heinrich:2023`. Reconcile.

6. **[MINOR] Assumption-(d) "closure" is asserted, not derived, in the deformed-algebra scheme** (lines 1010, 1449). The single-clock/all-orders ζ-conservation argument is sound in the dressed-metric scheme, but the claim that the effect is "(kη_bounce)²-suppressed" through the deformed-algebra signature-change window (c_s²=1−2ρ/ρ_c<0), precisely where the gradient expansion is questionable, is stated rather than shown. Present it as conditional on the dressed-metric quantization (which the text mostly does); soften "derived/closed."

7. **[MINOR] Abstract oversells the Monte Carlo** — "validated across three independent 10⁵-realization Monte Carlo ensembles" (line 909) reads as three physical ensembles, but the body (line 1158) correctly clarifies they are cross-checks of a closed-form integral. Align the abstract wording.

8. **[MINOR / unverifiable from source] Figure content** — `fig1_shape_function.png` and `fig2_survey_comparison.png` must render the corrected −35/16 values (per the paper's own figure-propagation discipline). I cannot verify PNG contents from the .tex; this needs a compiled-PDF check on the figure pages.

**(3) Is the central claim supported?** Yes — the theory value f_NL^local = −35/16 is decisively corroborated by Li et al.'s independent general-c_s formula (Eq. 5.1 → −35/16 at c_s=1) in addition to the vertex re-summation, and the SPHEREx forecast is an honestly conservative recast whose significance arithmetic I re-derived and confirmed; the only genuinely soft link is that the abstract-headlined *lower* significance bound rests on a disclosed proxy correlation (Issue 2).
