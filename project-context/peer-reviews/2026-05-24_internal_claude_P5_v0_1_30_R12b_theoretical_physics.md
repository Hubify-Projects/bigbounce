# P5 v0.1.30 — R12b theoretical-physics verdict

**Reviewer perspective:** rotating Grok-4.3 + Sonnet-cosmology theoretical-physics
lens. Round 3-of-3 of the AGENT_RULES §4.4.1 cascaded-loop-exit streak on the
same on-disk PDF artifact already cleared by R10 (Gemini-cosmology + GPT-5 +
Grok-brutal) and R11 (Perplexity-citation + DeepSeek-confab).

**Artifact under review:**
`/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
(v0.1.30-2026-05-24, 1518 lines, abstract + 9 sections + 4 figures + 9 tables +
bibliography). Cross-checked JSON artifacts:
`results/analysis_cosmic_web/{p4_monopole_residual_analysis,
filament_within_class_decomposition, cluster_within_class_decomposition,
voids_vs_chirality_robustness_grid}.json`.

## One-line summary

**0 BLOCKER / 0 MAJOR / 0 minor / 0 nit.**

## Per-finding blocks

NO FINDINGS — paper survives theoretical-physics cross-check round 3-of-3.

## Theoretical-physics protocol applied (what was checked and why each cleared)

The instruction specified six failure modes to hunt for. Each was actively
probed; each cleared. Recording the negative results so future R-rounds (and
external referees) can see the cross-check was real, not perfunctory.

### (a) Dimensional / units consistency

- Eq. (1) `σ_pred = Δf_CW / (0.5/√N) = 2 · Δf_CW · √N` is dimensionless on both
  sides (Δf_CW is a probability difference, √N is dimensionless). Bonferroni
  Eq. (2) returns a dimensionless quantile from a dimensionless argument.
  Pearson r and p-value (line 1256) dimensionless by construction. V-Web
  algorithm (§sec:vweb_algo lines 302–332): δ dimensionless, Φ = −δ_k/k² so
  Φ carries units of length² in code; tidal tensor T_ij = k_i k_j Φ(k) is then
  dimensionless (k carries 1/length, so k_i k_j Φ carries 1/length² · length² =
  dimensionless), which is what an eigenvalue threshold λ_th = 0 dimensionless
  comparison requires. **Consistent.**
- RSD displacement σ_v/(aH) in the Limitations block (line 1375) carries units
  of length (km/s ÷ km/s/Mpc = Mpc); the comparison to R_s = 25 Mpc/h is unit-
  matched after the paper's standard h-convention. **Consistent.**

### (b) Bounce-vs-inflation discriminating-power overclaim check

§sec:bounce_inflation_implications (lines 1320–1334) is the load-bearing
theoretical paragraph. Direct quote:
"The present null does not currently discriminate between matter-bounce and
inflation-class models because no published model in either class predicts an
environment-dependent CW signature at DESI DR1 sensitivity; the null instead
establishes an observational upper bound that any future parity-violating model
proposing an environment-dependent chirality signature must respect."

This is the **precise** theoretical statement a strict referee would want: it
(i) does not claim the null *between* bounce and inflation, (ii) correctly
notes neither published model predicts the signal at this sensitivity, and
(iii) reframes the contribution as a forward-looking upper bound on a class of
future models, not a backward-looking discriminator. The Conclusions
recapitulation (lines 1412–1416) is identically phrased. **No overclaim.**

### (c) Theoretical mapping between chirality and V-Web/T-Web tidal eigenvalue structure

The paper does **not** assert that V-Web tidal eigenvalues are predicted by
TTT-class theory to source spiral chirality. V-Web is used strictly as an
environment classifier (lines 296–332): the tidal tensor T_ij = k_i k_j Φ
defines a cell label via eigenvalue counting, not a prediction for spin
direction. The single sentence on theoretical motivation (lines 1322–1325)
correctly says a positive detection "would have been" a discriminator for
"parity-violating scenarios that source coherent angular momentum" — note the
conditional tense and the correct attribution of coherent-AM to *parity-
violating early-universe physics*, not to the V-Web tidal field itself. This
matches the tidal-torque-theory literature (Doroshkevich 1970, White 1984,
Lee–Pen 2000): TTT predicts spin *magnitude* coupling to tidal eigenvalues but
no parity-violating handedness preference in standard ΛCDM + inflation, which
is exactly the null the paper measures. **Mapping is correctly stated.**

### (d) Abstract one-liner vs Discussion theoretical framing consistency

Abstract headline (lines 82–88): "the CW fraction shows no environment
dependence above the sensitivity floor set by the Paper IV catalog-monopole
offset of ~0.2 pp (systematic-dominated for V-Web filament/cluster) and by
counting statistics of ~5 pp (statistical-dominated for V-Web void at n = 428,
~2σ on the binomial null), within DESI DR1 at V-Web resolution."

Discussion framing (lines 1312–1318): "The cosmic-web headline is most cleanly
read as a null: the per-environment CW fractions cluster at the catalog-wide
f_CW ≈ 0.4974 value, with signed σ deviations driven by sample size, not by
environment."

The two framings are mutually consistent and propagate the same caveats. The
abstract is explicit about the underpowered void class ("~2σ on the binomial
null"); the Discussion does not promote the void null beyond what the abstract
already concedes. **Consistent.**

### (e) "Consistent with parity violation" vs "constraint on parity violation" usage

The Intro (lines 178–183) frames a positive detection as "a novel observational
constraint on early-universe parity-violating physics" and the null as
tightening "the limits of correlated handedness." This is the correct
*constraint* phrasing for an upper-bound null.

The Discussion never says "consistent with parity violation" or any cognate. It
says "consistent with the Paper IV global parity-mixture null" (line 1412) —
which means consistent with the *measured CW≈CCW mixture*, not with the
*theoretical prediction* of parity violation. The Intro lines 166–174 set this
up explicitly: parity-conserving leading-order universe → equal-mixture
prediction; Paper IV finds 0.4974 ± 0.000279 "consistent with parity at ~1σ" =
the experimentalist usage "consistent with the parity-preserving null
hypothesis," not the physicist usage "consistent with parity being violated."
**Usage is unambiguous and correct throughout.**

### (f) "Filament sign-flip" vs "environmental dependence" conflation check

The bright-vs-dark sign-flip in the filament class (BGS-bright σ = −2.80 vs
LRG/ELG/QSO-dark σ = +2.85, n_dark = 21,203, joint |z| ≈ 3.4σ on the
difference) is the most theoretically dangerous result in the paper —
naively, an opposite-sign per-tracer signal *within one V-Web class* could be
spun as evidence of environment-conditioned parity violation.

The paper explicitly does not do this. It frames the sign-flip as evidence of
"BGS-selection-function-conditioned imaging-leg systematics" (lines 656–660,
also the abstract at line 156: "consistent with a BGS-selection-function
origin"). The theoretical interpretive logic is correct:
- a genuine environment-dependent astrophysical signal would propagate at
  comparable sign and magnitude across all tracer programs (because the
  environment is the same on the sky);
- a selection-function-conditioned imaging-leg systematic CAN flip sign across
  tracer programs because different programs sample different imaging-leg
  populations.

The cluster-class joint z=−0.5σ is correctly disclosed as sample-size-limited
(n_dark^cluster = 4,234) and *not* independently confirming the bright-origin
interpretation; that hedge — added in R8 per the R11 audit trail — preserves
the right epistemic posture. The filament-class sign-flip is *not* conflated
with "filament environmental dependence." **No conflation.**

## (g) §4.4.1 streak status

| Round | Reviewer panel                                   | BLOCKER | MAJOR | minor | nit |
|-------|--------------------------------------------------|---------|-------|-------|-----|
| R10   | Gemini-cosmology + GPT-5 + Grok-brutal           | 0       | 0     | 0     | 0   |
| R11   | Perplexity-citation + DeepSeek-confab            | 0       | 0     | 0     | 2¹  |
| R12b  | rotating Grok-4.3 + Sonnet theoretical physics   | 0       | 0     | 0     | 0   |

¹ R11's two nits are stylistic/uniformity items (Paper III cite formatting,
0.4974 vs 0.4972 monopole convention), not introduced in v0.1.30 and below the
§4.4.1 (BLOCKER + MAJOR = 0) streak gate.

**Three consecutive clean rounds at 0 BLOCKER + 0 MAJOR on the same PDF artifact
v0.1.30-2026-05-24 → §4.4.1 cascaded-loop-exit gate is SATISFIED for P5.**

The remaining 4% to the 99% AGENT_RULES ceiling is the standing Houston
sign-off + first cross-vendor R-round (currently blocked on the OpenRouter
per-key weekly cap, not on internal closure).

## (h) Closing note — theoretical-physics-specific things this round verified

1. The paper does not claim the V-Web tidal eigenvalues are the predicted
   source of chirality. V-Web is used as a classifier, not as a theoretical
   handle. **Correct restraint.**
2. The bounce-vs-inflation paragraph reframes the null as an upper bound on
   future models, not a discriminator between existing models. **Correct
   restraint and correct theoretical phrasing.**
3. The bright-vs-dark sign-flip in the filament class is explicitly diagnosed
   as a selection-function systematic with the correct logical argument (a
   real environment effect would not flip sign across tracer programs sampling
   the same sky). **Correct interpretive caution.**
4. The paper's "consistent with parity" usage consistently means "consistent
   with the parity-preserving null hypothesis," never the physicist-prediction
   sense. **Correct technical usage.**
5. Dimensional consistency holds in every equation (Eq. 1 σ_pred, Eq. 2
   Bonferroni, V-Web Φ and T_ij), and the RSD-displacement comparison in
   Limitations carries the right h-convention. **Correct units.**

Paper survives the theoretical-physics cross-check.
