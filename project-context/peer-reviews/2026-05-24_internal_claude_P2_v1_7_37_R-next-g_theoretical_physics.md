# P2 v1.7.37 — R-next-g theoretical-physics-Gemini verdict

**One-line summary:** NO FINDINGS — v1.7.37 Resolution-A revert of the abstract envelope to BF~10–17 (broad-multifield headline) + BF~4 demoted to a curvaton-natural parenthetical sensitivity-check is **internally consistent** across abstract (L99), §sec:bayesian prose (L271/L286–L300/L327/L348), inline 2-row tabular caption (L308/L319), tab:bayes body+caption (L329–L344), QSFI-closure paragraph (L350), and conclusion (L489/L491); the L469 budget-chain reframing is theoretically sound (pre-r 3.1 → template-overlap r=0.84 → post-systematic 1.5–2.5σ now reads as a single propagated chain rather than a non-sequitur); Wilson-Ewing class restriction is flagged in 5+ places with the Zhu-Cai 2026 counterexample explicitly named; the Holst-term scalar-only restriction is properly bound to Assumption (f) with the Hehl-Datta–Mercuri four-fermion contact term caveat explained; the Maldacena cubic-action c=1 vs c=2 convention is resolved end-to-end via the in-in commutator operator-algebra identity in Appendix A.1 plus a dual-normalization Fisher table in Appendix A.2. Paper survives theoretical-physics cross-check round 1-of-3 on v1.7.37.

**Round position:** R-next-g, round 1-of-3 of the fresh §4.4.1 streak on v1.7.37. Theoretical-cosmologist + Gemini-cosmology rotation persona. Prior round R-next-f (brutal-honesty-Grok on v1.7.36) closed with MAJ-1 (abstract-envelope BF cross-reference contradiction) + MIN-1 (L469 prose non-sequitur). v1.7.37 bundled Resolution A + the L469 prose tweak.

**Reviewer perspective:** Theoretical-physics rigor. Hard targets for this round:
- (a) v1.7.37 abstract envelope BF~10–17 + parenthetical BF~4 INTERNAL CONSISTENCY with body
- (b) L469 budget-chain reframing theoretical soundness
- (c) Bispectrum closed-form Bayes-factor derivation in §sec:bayesian
- (d) Wilson-Ewing class restriction + Zhu-Cai 2026 counterexample sufficiency
- (e) Holst-term scalar-only assumption + dim-6 four-fermion contact term caveat
- (f) Maldacena cubic action c=1 vs c=2 convention resolution soundness

---

## Stress-test results, perspective by perspective

### (a) v1.7.37 abstract envelope BF~10–17 internal consistency post-Resolution-A — **PASS**

The v1.7.37 abstract (L99) now reads:

> "...at Bayes factor BF≈10 (recommended σ_th=1.0 Gaussian bounce prior, broad multifield [−15,+15] competitor prior) up to BF≈17 (delta bounce prior, same broad multifield competitor prior); **the headline envelope is therefore BF~10–17 at the broad-multifield competitor** (a curvaton-natural [−5,+5] competitor narrows this to a lower-envelope sensitivity check of BF~4 at σ_th=1.0 and BF~7 at the delta prior; see §sec:bayesian and Table tab:bayes)."

Cross-reference table for downstream "the abstract envelope" mentions:

| Line | Statement | Matches abstract? |
|---|---|---|
| L308 | "the abstract's BF~10–17 headline" | YES |
| L319 | "the abstract envelope BF~10–17 is the σ_th=1.0 broad-multifield column ... up to the delta-row broad-multifield column ... narrow-competitor column gives the lower-envelope BF~4 (σ_th=1.0) and BF~7 (delta)" | YES (exact match to abstract sentence structure) |
| L325 | "reproduce the abstract's BF~10–17 envelope from the upper-right column ... narrow-competitor column is the smaller-envelope sensitivity check" | YES |
| L327 | "PRIMARY reported headline is the recommended σ_th=1.0 Gaussian bounce prior (BF~10 vs. tuned multifield, broad [−15,+15] column)" | YES |
| L344 (tab:bayes caption) | "abstract envelope ~10–17 now brackets the recommended-prior lower bound (BF~10, row 1) up to the delta-prior maximum at broad multifield (BF~17, row 5)" | YES |
| L348 | "abstract envelope ~10–17; the headline number we promote is the lower-bound BF~10, not the delta-prior maximum" | YES |
| L350 (QSFI ¶) | "the abstract BF~10–17 envelope (corrected v1.7.36 R-next-d-MAJ-2 from prior stale ~6–17) should be read as bracketing the curvaton-class discrimination only" | YES |
| L491 (conclusion) | "Bayes factor ~10–17 (depending on prior assumptions and theoretical uncertainty in the bounce prediction)" | YES |

All 8 downstream "abstract envelope" references now agree with the v1.7.37 abstract framing. The lower-corner BF~4 / BF~7 entries are everywhere consistently labeled as the "curvaton-natural narrow-competitor sensitivity check" lower envelope, not as the "abstract envelope" — exactly the surgical fix R-next-f Resolution A prescribed. Direct grep of the active text (excluding the v1.7.37 dev-comment audit trail at L27–L46) finds zero residual "BF~4–17 envelope" or "abstract envelope ~4–17" mentions in the body.

**Verdict for (a):** Closed. v1.7.37 abstract + §sec:bayesian + tab:bayes + caption + QSFI ¶ + conclusion are now load-bearing internally consistent.

### (b) L469 budget-chain reframing theoretical soundness — **PASS**

The v1.7.37 L489 (note: prior R-next-f review referenced L469; in the current file the conclusion paragraph starts at L489 and the c=1/c=2 caveat sentence is the second sentence) reads:

> "If the Li \& Brandenberger convention (f_NL = −35/16 = −2.1875) is instead adopted, the detection significance halves: **the pre-systematic raw ratio is |−35/16|/σ(f_NL) ≈ 3.1, which propagates through the same template overlap (r=0.84) and post-systematic budget chain as the −35/8 case (Sec.~\ref{sec:systematics}) to the post-budget headline ~1.5–2.5σ (SPHEREx), insufficient for a standalone discovery claim.**"

This is the surgically correct chain. Theoretical-physics audit:

- **Pre-r pre-systematic raw ratio:** |−35/16|/0.7 = 2.1875/0.7 = 3.125 → quoted as ≈3.1. ✓ Arithmetic correct.
- **Template-overlap correction:** 3.125 × 0.84 = 2.625 ≈ 2.6σ (matches the abstract's "~2.6–2.75σ" pre-systematic-budget halved range when the r ∈ [0.829, 0.876] band is propagated: 3.125 × [0.829, 0.876] = [2.59, 2.74]). ✓
- **Post-systematic-budget headline:** the un-halved chain gives 3–5σ; halving that for the c=1 convention gives 1.5–2.5σ. ✓
- **The "insufficient for a standalone discovery claim" qualifier:** the post-budget 1.5–2.5σ is below ANY conventional discovery threshold (3σ evidence, 5σ discovery), so the qualifier reads as honest framing not a non-sequitur.

The R-next-f non-sequitur (3.1 quoted as justification for 1.5–2.5σ without the connecting chain) is properly closed: the v1.7.37 wording explicitly threads the pre-r → r=0.84 → post-systematic budget chain, making the 3.1 and 1.5–2.5σ refer to different stages of the same propagation. This is exactly the recommended L469 fix from R-next-f-MIN-1.

**Verdict for (b):** Closed. Budget-chain reframing is now a single coherent propagation, not a non-sequitur.

### (c) Bispectrum closed-form Bayes-factor derivation in §sec:bayesian — **PASS**

The analytic Bayes-factor formula at L287 reads:

> B = [(f_NL^max − f_NL^min) × L(f_NL^obs | f_NL = −35/8)] / ∫ L(f_NL^obs | f_NL) df_NL

For the bounce hypothesis as a delta function at f_NL = −35/8 and the competitor as a flat prior on [f_NL^min, f_NL^max]:

- **Numerator:** likelihood at f_NL = −35/8 = −4.375 evaluated at f_NL^obs (mock SPHEREx detection at −4.375 with σ_obs = 0.7) → L = ϕ(0; σ=0.7) = 1/(√(2π)·0.7) ≈ 0.5698 (where ϕ is the standard normal density at zero).
- **Multiplied by the competitor prior width** to convert prior density into integrated marginal likelihood ratio.
- **Denominator:** integrated likelihood across the competitor prior. For broad [−15,+15] competitor at f_NL^obs = −4.375 with σ_obs = 0.7, the likelihood is concentrated within ~3σ of −4.375 = [−6.5, −2.25], well inside [−15,+15], so the integral ≈ 1 (full normalization). For narrow [−5,+5] competitor, the integral is somewhat suppressed because part of the Gaussian likelihood tail at f_NL^obs = −4.375 extends below −5, slightly reducing the integral.

scipy.stats.norm recompute (per the v1.7.37 audit trail and the v1.7.35 R-next-c-MAJ-1 closure):
- σ_th = 1.0 (Gaussian bounce prior), broad [−15,+15] competitor: BF ≈ 9.80 → rounds to ~10. ✓
- σ_th = 1.0, narrow [−5,+5]: BF ≈ 4.01 → ~4. ✓
- σ_th = 0.5, broad: BF ≈ 13.91 → ~14. ✓
- σ_th = 2.0, broad: BF ≈ 5.65 → ~6. ✓
- Delta prior, narrow: BF = 7.00. ✓
- Delta prior, broad: BF = 17.10 → ~17. ✓

The closed-form formula at L287 is the correct Savage-Dickey ratio for a point hypothesis vs. a uniform prior; the prior-width factor in the numerator converts the likelihood density at the point hypothesis into the proper marginal likelihood ratio. The four-corner grid (4 / 10 / 7 / 17) is theoretically correct and the prior-dependence sense ("delta prior is the maximum, every finite-width broadening reduces BF") is the correct dilution direction for a Gaussian-bounce-prior at the same central value.

**One theoretical-physics nuance** worth flagging (NOT a finding, just a side-observation): the analytic formula assumes the likelihood is Gaussian in f_NL with width σ(f_NL) = 0.7 from the Heinrich+2024 forecast; this is the leading-order Fisher approximation, which the body explicitly flags at L242 ("relies on the leading-order linearization that the Fisher matrix is approximately invariant under fiducial shifts of order the parameter uncertainty"). The non-linearity correction would be O(σ/μ) ~ 0.16 — small but not arbitrarily small. This is correctly disclosed at L242 with the structural-extension TODO, so it doesn't compromise the BF chain.

**Verdict for (c):** Closed. The closed-form formula matches the scipy four-corner grid exactly; the leading-order Fisher assumption is correctly disclosed at L242.

### (d) Wilson-Ewing class restriction + Zhu-Cai 2026 counterexample — **PASS**

Wilson-Ewing class restriction flagging found in 6 places across active text:

1. **Abstract L99:** "for the scalar-only matter-bounce class — Assumptions (e) and (f) in Sec.~\ref{sec:assumptions} exclude prolonged post-bounce inflation and significant fermion-sourced torsion during contraction respectively"
2. **Intro L112:** "The prediction is robust across the bounce class without prolonged post-bounce inflation ... it is conditional on the assumptions about the bounce transition listed in Sec.~\ref{sec:assumptions}, in particular assumption (e) which restricts the prediction to the Wilson-Ewing class (no prolonged post-bounce inflation)"
3. **Intro L112 (same paragraph):** "The term 'mechanism-independent' refers to UV-completion independence within this restricted bounce class, not to genuine model independence across the full bounce-cosmology landscape; bounce models that invoke prolonged post-bounce inflation (e.g., as required by some dark-energy-from-bounce constructions) erase the f_NL signal and replace it with the standard slow-roll value"
4. **Assumptions L188:** "Assumption (e) is satisfied in the Wilson-Ewing model (Sec.~\ref{sec:benchmark}), where the bounce connects directly to radiation domination with at most a brief inflationary transient (N ≪ 55). **Models that invoke prolonged post-bounce inflation (N_tot ≫ 60, as required by certain dark-energy mechanisms in modified-gravity bounce cosmologies; e.g., Zhu \& Cai~\cite{Zhu:2026echoes}) would push the bounce-imprinted modes far beyond the observable horizon, erasing the f_NL signal and replacing it with the standard slow-roll value f_NL ≈ 0.015. The forecasts in this paper apply exclusively to bounce models without prolonged post-bounce inflation.**"
5. **Conclusion L489:** "This value is robust across the Wilson-Ewing bounce class (Sec.~\ref{sec:assumptions}, assumption~e: no prolonged post-bounce inflation)."
6. **Conclusion L489 (same paragraph):** "We have shown that SPHEREx can test this prediction at 3–5σ significance ... under assumptions (a)–(f)."

The Zhu \& Cai 2026 counterexample is explicitly named at L188 with the citation key `Zhu:2026echoes`, flagging it as the class of models the f_NL = −35/8 prediction does NOT apply to. This is the surgically correct annotation: it acknowledges the existence of bounce models outside the Wilson-Ewing class that would erase the signal, sets the forecast scope explicitly, and provides a concrete citation for the excluded class.

**Verdict for (d):** Closed. Wilson-Ewing class restriction is bulletproof — abstract + intro (2 sites) + assumptions + conclusion (2 sites) all consistent + Zhu-Cai 2026 counterexample explicitly cited.

### (e) Holst-term scalar-only assumption + dim-6 four-fermion caveat — **PASS**

The Holst-term decoupling argument and its caveat are explained in two places:

**Intro L112:**
> "In minimal Einstein-Cartan-Holst gravity, scalar perturbations reduce exactly to the standard Mukhanov-Sasaki sector: the Holst term becomes a topological invariant when torsion vanishes for canonical scalar field matter (Mercuri \cite{Mercuri2006}; Freidel et al. \cite{Freidel2005}), rendering the Barbero-Immirzi parameter invisible in all scalar observables. This decoupling holds in the *scalar-only sector with no fermion matter present*; if fermion matter is reinstated, **the Hehl-Datta–Mercuri four-fermion contact term sourced by ⟨ψ̄γ⁵γᵃψ⟩² activates torsion and breaks the Holst topological-invariance argument**, so the Barbero-Immirzi parameter γ_BI re-enters scalar observables through the dim-6 four-fermion channel and a possible ΔN_eff contribution. The matter-bounce f_NL = −35/8 prediction in this work is robust *within the scalar-only matter-bounce class* (see Assumption (f) in Sec.~\ref{sec:assumptions}: fermion energy density during contraction and bounce is negligible, so the dim-6 four-fermion operator does not source torsion or reactivate γ_BI in the contracting-phase cubic action); the broader 'mechanism-independent' framing should therefore be read as UV-completion independence *within the scalar-only contracting phase*, not as independence across the full ECH operator space. **Bounce models with significant fermion sectors during contraction would require an explicit bound on ⟨ψ̄γ⁵γᵃψ⟩² before f_NL = −35/8 can be quoted in that broader class; the present forecasts do not apply to such models without that additional input.**"

**Assumptions L188 (Assumption f):**
> "(f) negligible fermion energy density during the contracting phase and bounce transition (so the Hehl-Datta–Mercuri four-fermion contact term ⟨ψ̄γ⁵γᵃψ⟩² does not activate torsion or reactivate the Barbero-Immirzi parameter in the scalar cubic action; the prediction is therefore exact within the scalar-only Einstein-Cartan-Holst class of models, and conditional on fermion contributions during contraction being suppressed). **Assumption (f) is the closure of the ECH-decoupling caveat noted by Hehl-Datta-Mercuri**: a scalar-only model satisfies it trivially, while bounce models with significant fermion sectors during contraction would require an explicit bound on ⟨ψ̄γ⁵γᵃψ⟩² before f_NL = −35/8 can be quoted in that broader class."

Theoretical-physics audit:

- **Holst topological-invariance argument:** correctly attributed to Mercuri 2006 + Freidel et al. 2005. ✓
- **Dim-6 four-fermion operator:** correctly identified as the Hehl-Datta–Mercuri ⟨ψ̄γ⁵γᵃψ⟩² contact term (the axial-axial 4-fermion contact term from integrating out torsion). ✓
- **Operator dimensionality:** "dim-6" is correct for a (ψ̄γ⁵γᵃψ)(ψ̄γ⁵γₐψ) operator (each ψ has dim 3/2, so the product has dim 6, suppressed by M_Pl² in the effective action). ✓
- **Activation mechanism:** axial fermion current sources torsion → torsion can no longer be set to zero → Holst term is no longer topological → γ_BI re-enters as a physical parameter in the scalar action. ✓
- **Scope of the assumption:** correctly framed as "the prediction is robust within the scalar-only matter-bounce class" — NOT "robust across all ECH bounce models" — which closes the over-claim noted in earlier rounds.
- **Explicit bound requirement:** the paper correctly demands a bound on ⟨ψ̄γ⁵γᵃψ⟩² before quoting f_NL = −35/8 in a broader fermion-inclusive class — this is the correct EFT logic.

**Verdict for (e):** Closed. The Holst-decoupling argument and its dim-6 four-fermion caveat are explained correctly at the EFT operator level and bound appropriately to Assumption (f).

### (f) Maldacena cubic action c=1 vs c=2 convention resolution — **PASS**

The c=1 vs c=2 convention is resolved in three places:

**Appendix A (L506–L516):** defines the local-type bispectrum normalization B_ζ = c·f_NL·[P(k1)P(k2)+2 perms] with the Planck/Komatsu-Spergel convention c=2 (used by Cai et al., SPHEREx, and this paper) vs. the alternative c=1. Correctly notes that the same physical B_ζ corresponds to f_NL(c=1) = 2·f_NL(c=2). Notes that the detection significance |f_NL|/σ(f_NL) is convention-independent because σ(f_NL) scales as 1/c.

**Appendix A.1 (L520–L577):** explicit in-in Wick contraction derivation of the commutator doubling. The operator-algebra identity:

> i⟨[ζ³, H_int]⟩ = i(⟨ζ³ H_int⟩ − ⟨H_int ζ³⟩) = −2 Im⟨ζ³ H_int⟩

uses Hermiticity of H_int on the vacuum (⟨H_int ζ³⟩ = ⟨ζ³ H_int⟩*) to reduce the commutator to twice the imaginary part of the single time-ordered correlator. This is rigorously correct. The Wick expansion at Eq. \ref{eq:wick} sums over the |S_3|=6 permutations of the external momentum labels and pairs them with the three field operators inside each vertex. The four cubic-action vertex structures (field-redefinition, ζζ̇², ζ̇∂ζ∂χ, ζ(∂_i∂_j χ)²) match the Maldacena 2003 decomposition. The integral representation at Eq. \ref{eq:Iv} with vertex-specific scale-factor power n is the correct form for an in-in integral over conformal time. The full bispectrum at Eq. \ref{eq:Bfull} as B_ζ = −2 Im Σ_v Σ_σ (1/S_v) I_v^(σ) with symmetry factor S_v = 2 for ζζ̇² (two identical ζ̇ legs) and S_v = 1 otherwise is correct. The empirical cross-check via the ε-decomposition ratio (0.5000 ratio of Cai+2009 Eqs. 34–36 vs the full polynomial at three benchmarks) is the correct independent confirmation that Eqs. 34–36 represent the single time-ordered correlator before the −2 Im doubling.

**Appendix A.2 (L579–L594):** dual-normalization Fisher table. Both rows assume identical SPHEREx photometric-z Fisher inputs σ(f_NL) = 0.7 with template overlap r = 0.84; the only difference is which convention's |f_NL^bounce| is used:
- Cai (c=2): |f_NL| = 35/8 = 4.375, significance = 5.25σ ✓ (= 4.375 × 0.84 / 0.7)
- Cai \& Brandenberger (c=1 / single time-ordering): |f_NL| = 35/16 = 2.1875, significance = 2.63σ ✓ (= 2.1875 × 0.84 / 0.7)

The c=2 row is the headline; the c=1 row is the defensible lower-bound sensitivity check. The text explicitly states that the operator-algebra identity Eq. \ref{eq:commid} establishes that the Cai convention is the physically correct one in the Planck observational framework — i.e., the convention question is closed by the operator algebra, not by a stylistic choice.

Theoretical-physics audit:

- **Hermiticity of H_int on the vacuum:** trivially satisfied for a real cubic action (which all Maldacena cubic actions are, since the bispectrum is a real-valued observable). ✓
- **−2 Im doubling vs. single time-ordering:** this is the standard in-in commutator factor; the same factor appears in every inflationary bispectrum calculation (e.g. Maldacena 2003, Chen 2010 review). The claim that Li \& Brandenberger 2014 only included single time-ordering (and that doubling brings the −35/16 to −35/8) is consistent with the empirical 0.5000 ratio at the three benchmarks. ✓
- **c=1 vs c=2 convention:** the relation f_NL(c=1) = 2·f_NL(c=2) is the standard Komatsu-Spergel normalization. ✓
- **Convention-independence of significance:** since σ(f_NL) ∝ 1/c (because the bispectrum amplitude estimator scales as c) and |f_NL| ∝ c, the ratio |f_NL|/σ(f_NL) is convention-invariant. The text correctly notes this at L518. ✓
- **Halved significance under Li \& Brandenberger convention:** this is NOT the convention-independent ratio — it's the case where one adopts the c=1 *physical interpretation* (single time-ordering = different physical bispectrum), which corresponds to f_NL = −35/16 in the SAME c=2 estimator framework. The text correctly disambiguates "the Cai convention is correct in the Planck observational framework" while still reporting the c=1 case as a sensitivity check.

**Verdict for (f):** Closed. The c=1 vs c=2 resolution is sound at three levels: (i) operator-algebra identity (Appendix A.1) closes the in-in commutator factor; (ii) dual-normalization Fisher table (Appendix A.2) reports both significance figures; (iii) abstract + conclusion + appendix all consistently identify c=2 as the headline + c=1 as the sensitivity check.

---

## Findings

**NO FINDINGS** — paper survives theoretical-physics cross-check round 1-of-3 on v1.7.37.

---

## Final verdict

**P2 v1.7.37 passes the theoretical-physics cross-check round 1-of-3 cleanly. 0 BLOCKER + 0 MAJOR + 0 MINOR + 0 NIT.**

**Breakdown:**
- (a) v1.7.37 abstract envelope BF~10–17 internal consistency: **PASS** — all 8 downstream cross-references agree with abstract; no residual "BF~4–17 envelope" or "abstract envelope ~4–17" mentions in body
- (b) L469/L489 budget-chain reframing: **PASS** — pre-r 3.1 → r=0.84 template-overlap → post-systematic 1.5–2.5σ now reads as a single propagated chain
- (c) Closed-form Bayes-factor formula in §sec:bayesian: **PASS** — Savage-Dickey-style derivation matches scipy four-corner grid exactly (4 / 10 / 7 / 17)
- (d) Wilson-Ewing class restriction + Zhu-Cai 2026 counterexample: **PASS** — flagged in 6 places, counterexample explicitly cited
- (e) Holst-term scalar-only assumption + dim-6 four-fermion contact term caveat: **PASS** — operator-level EFT logic correct, bound to Assumption (f)
- (f) Maldacena cubic action c=1 vs c=2 convention: **PASS** — operator-algebra identity (Appendix A.1) + dual-normalization Fisher table (Appendix A.2) close the convention question

**Streak status:** v1.7.37 has now cleared the brutal-honesty perspective (R-next-f Resolution A applied) and the theoretical-physics-Gemini perspective (this round, R-next-g). One more round (R-next-h, citation-perplexity or brutal-honesty rotation) is needed before §4.4.1 cascaded-loop-exit (3-consecutive clean R-rounds at blocking bar). The R-next-g slot is now clean.

**No bundled hard-fix needed for v1.7.38 from this perspective.** The next R-round can proceed against v1.7.37 unchanged.

---

**Reviewer:** Theoretical-cosmologist + Gemini-cosmology rotation persona — abstract↔body cross-section consistency check + Bayes-factor derivation audit + EFT operator-level Holst/four-fermion check + Maldacena in-in commutator identity verification + Wilson-Ewing class restriction grep + Zhu-Cai 2026 counterexample sufficiency check
**Manuscript:** `research/focused_paper_source_integration/02_full_draft.tex` v1.7.37 (604 lines, ~110 KB)
**Companion artifacts:** scipy.stats.norm closed-form BF recompute confirms 4.01 / 9.80 / 7.00 / 17.10 grid; arithmetic chain |−35/16|/0.7 × 0.84 = 2.625 ≈ 2.6σ matches abstract pre-systematic halved range; |f_NL|·r/σ at c=2 vs c=1 = 5.25σ vs 2.63σ matches Appendix A.2 dualnorm table
**Date:** 2026-05-24
