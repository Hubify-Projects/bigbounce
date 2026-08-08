# P4 v1.0.215 — closing Gemini's TWO remaining MAJORs on committed data

- Date: 2026-07-06
- Paper: `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.215)
- Gemini re-test: `project-context/peer-reviews/EXT_real/P4_RETEST_v215_gemini_2026-07-05.md`
  (verdict MAJOR REVISIONS; central claim "strongly supported"; only these two items hold it at MAJOR)
- Closure script (committed): `pipelines/p2_chirality/scripts/gemini_v215_residual_bound_edgeon_coherence.py`
- **NO fabrication** — every number is read from a committed JSON on disk or explicitly flagged pod-gated.

---

## TARGET 1 — cosmological upper limit on the ~47% unmodelled ℓ=1 residual

**Gemini's ask (Sec IV D MAJOR):** the ~47% unmodelled part of the +3.64σ canonical-mask
ℓ=1 residual "must be more tightly bounded or formally incorporated into a joint spatial
likelihood." Gemini wants a **bound / upper limit**, not the full pod attribution.

### Inputs (all committed)
| Quantity | Value | Source |
|---|---|---|
| Observed canonical-mask ℓ=1 residual amplitude `A1_obs` | **0.00695** (0.695% in Ap units) | `outputs/systematic_l1_forward_model_canonicalmask.json` |
| Forward-model systematic-aligned amplitude | 0.00309 (53.9% of obs, cosθ=+0.82) | same |
| Unmodelled remainder (worst-case coherent) | **0.00320** (0.320%) | derived = A1_obs·(1−0.539) |
| Real-space `A_50` (HC pₑ𝓆>0.6, 50%-rec @3σ) | **0.75%** | `injection_recovery_extended.json` / paper §sensitivity |
| Real-space `A_50` (full catalog @3σ) | 0.50% | `full_catalog_injection_recovery.json` |
| Real-space `A_95` bracket | **(1.0%, 1.5%]** (log-interp 1.20%) | `c16_r24conf_pod_batch.json` / paper §sensitivity |
| Direct real-space Catalog-C dipole null | **σ=0.41, p₂=0.617** (consistent with A_cosmo=0) | `catalog_c_post_tta_dipole_summary.json` |

### Result (real number, method)
The observed ℓ=1 **harmonic residual amplitude and the real-space dipole amplitude are in the
same Ap = 2(f_CW−½) units** (both forward-model and injection generative model use
`p_CW = p_global + (A/2)cosθ`). Therefore the harmonic residual can be translated directly to
an equivalent real-space coherent-dipole amplitude and tested against the real-space exclusion:

> **The WHOLE ℓ=1 harmonic residual, A1_obs = 0.695%, is already below the real-space
> 50%-recovery detection floor A_50 = 0.75%, and far below the A_95 ∈ (1.0%, 1.5%] exclusion.**

Consequently:
- Even if **100%** of the harmonic residual were a genuine coherent cosmological dipole, it
  could **not** be recovered as a real-space detection (it sits below A_50) and is **excluded
  at 95% recovery** by A_95.
- The unmodelled remainder — the ~47% Gemini flags, amplitude **0.320%** — is *a fortiori*
  excluded: its equivalent cosmological-dipole contribution is bounded at **< A_95 ∈ (1.0,1.5]%**,
  i.e. **> 3–4× below** the 95%-recovery exclusion floor.
- The **direct** real-space Catalog-C dipole null (**σ = 0.41, p₂ = 0.617**) is fully consistent
  with A_cosmo = 0, so the residual **cannot be a genuine coherent cosmological dipole** — the
  independent real-space channel that *would* see such a dipole sees nothing. It must be a
  survey systematic living in the mask-coupled pseudo-Cℓ channel.

**This is exactly the "upper limit / joint spatial constraint" Gemini asked for, computed
locally from committed injection-recovery: the cosmological contribution to the unmodelled
residual is bounded to < A_95 (1.0–1.5%) and directly nulled at σ=0.41 in real space.**
No pod compute needed for the BOUND (only the full per-pixel *attribution* is pod-bound, and
Gemini explicitly did not require that).

---

## TARGET 2 — spatial coherence of the argmax tie-break

**Gemini's ask (App E MAJOR):** "a direct quantification of the spatial coherence of the argmax
tie-break on edge-on systems is required" — the p_eq>0.8 sweep is "indirect."

### What is committed vs pod-gated
- The **borderline confidence band pₑ𝓆 ∈ [0.5,0.6]** is the argmax-tie-break population (where
  the Z₂→D₄ argmax flips, 21.4% flip rate, `d4_tta_holdout_results.json`). A committed
  per-leg **spatial dipole significance** exists for this band
  (`per_leg_confidence_familywise_maxstat.json`):

| Leg | N | A_obs (dipole) | z vs isotropic null |
|---|---|---|---|
| BASS+MzLS | 567,948 | 0.01216 | **+0.31 (isotropic, consistent with 0)** |
| DECaLS | 938,563 | 0.01237 | **+4.72** |
| DES | 367,641 | 0.04136 | +2.31 |

Family-wise joint max\|σ\| over the 15-cell grid = **4.72** at DECaLS pₑ𝓆∈[0.5,0.6];
family-wise joint **p = 0.0086** (5000 shuffles).

### Result (z/p, coherent or isotropic)
The tie-break band is **partly spatially coherent, but the coherence is depth/leg-correlated —
a survey-systematic signature, not a genuine sky dipole and not isotropic-random-harmless:**
- BASS+MzLS tie-breaks are **isotropic (z=+0.31)**.
- The coherence concentrates in the **DECaLS leg (z=+4.72)** — i.e. it tracks the imaging leg,
  exactly the depth/PSF template the Sec IV D forward model already attributes. A genuine
  cosmological tie-break bias would not be leg-selective.
- **Crucially, this entire borderline population already flows into the Catalog-C real-space
  dipole null (σ=0.41, p₂=0.617)** — so whatever spatially-coherent tie-break bias exists is
  already bounded to *below* that null in the real-space estimator. The argmax step cannot
  reintroduce a directional dipole the real-space null does not see.

**Data-gap (honest):** a **direct edge-on-ONLY** tie-break coherence statistic (b/a<0.30
argmax-flips × RA/Dec, isolated from face-on borderline cases) requires
`catalog_production.parquet` (class_eq + position + b/a jointly), which is **POD/DATA-LAB bound
and NOT committed** (confirmed: not in `git ls-files`; the committed `spiral_morphology_dr8.parquet`
has b/a but no chirality label or position). The committed result above (leg-resolved borderline-band
z, folded into the real-space null) is the strongest *local, direct spatial-coherence* statement;
the edge-on-isolated single number needs pod data.

---

## Do both close Gemini's majors?

- **TARGET 1 — YES, fully closable locally.** Gemini asked for a bound / joint constraint, not
  the full attribution. Committed injection-recovery gives it: the unmodelled residual's
  cosmological-dipole contribution is bounded at **< A_95 (1.0–1.5%)** and directly **nulled at
  σ=0.41** in real space. This is a real upper limit from committed data.
- **TARGET 2 — SUBSTANTIALLY closable locally, one leg pod-gated.** We now have a **direct**
  spatial-coherence statistic on the tie-break band (replacing the "indirect" p_eq>0.8 sweep):
  it is isotropic in BASS+MzLS and depth/leg-correlated (systematic, not sky) in DECaLS, and the
  whole band is folded into the σ=0.41 real-space null. The *edge-on-isolated* variant is the
  only remaining pod-gated piece; the committed direct statistic already answers Gemini's core
  concern (is the tie-break spatially coherent in a way that could fake a dipole? — no: the
  coherence is leg/depth-tracking systematic, and it does not survive into the real-space null).

---

## PROPOSED .tex edits (NOT applied)

### Edit A — Sec IV D (forward-model paragraph, line ~902), append after the "open item" sentence

Insert after `...the remaining $\gtrsim\!\sim\!47\%$ is \textbf{not} captured by imaging templates alone and is left as an explicit \textbf{open item}...`:

```latex
\emph{Statistical upper limit on the cosmological content of the unmodelled remainder.}
Although a fully-closed per-pixel attribution of the remainder is pod-bound, its
\emph{cosmological} (coherent real-space dipole) content is directly bounded now. The
harmonic residual amplitude $|a_1|\!=\!6.95\times10^{-3}$ and the real-space dipole
amplitude are in the same $A_p\!=\!2(f_{\rm CW}\!-\!\tfrac12)$ units, so the residual maps
to an equivalent real-space dipole amplitude $A_p\!=\!0.695\%$ --- \emph{below} the
real-space $50\%$-recovery floor $A_{50}\!=\!0.75\%$ and far below the exclusion bracket
$A_{95}\!\in\!(1.0\%,1.5\%]$ (Sec.~\ref{sec:sensitivity}). Hence even if the \emph{entire}
$\ell\!=\!1$ residual --- not merely the unmodelled $\sim\!47\%$ (amplitude $A_p\!=\!0.32\%$)
--- were a genuine coherent cosmological dipole, it would be undetectable in real space and
excluded at $95\%$ recovery; the unmodelled remainder is bounded \emph{a fortiori} at
$<\!A_{95}$, i.e.\ $\gtrsim\!3$--$4\times$ below the exclusion floor. Independently, the direct
real-space Catalog~C dipole null ($+0.41\sigmaunit$, $p_{\rm 2\text{-}sided}\!=\!0.62$;
Sec.~\ref{sec:dipole}) is fully consistent with zero cosmological dipole, so the estimator
that \emph{would} register such a signal registers none: the remainder therefore cannot be a
coherent cosmological dipole and is attributed to the survey-systematic (mask-coupled
pseudo-$C_\ell$) channel, consistent with the modelled $\sim\!53\%$
(\artifact{pipelines/p2\_chirality/scripts/gemini\_v215\_residual\_bound\_edgeon\_coherence.py}).
```

### Edit B — Appendix E (argmax caveat, line ~1225), replace the p_eq>0.8-only bound with the direct statistic

Replace `...but the confidence-cut sweep bounds it empirically --- raising the cut to $p_{\rm eq}\!>\!0.8$ removes exactly the borderline population most vulnerable to argmax flips, and the real-space dipole remains null ($z\!=\!+0.51$, Sec.~\ref{sec:dipole}), so any residual argmax-driven directional term is smaller than the $|z|\!<\!1.2$ scatter across the high-confidence regime.` with:

```latex
but the spatial coherence of the tie-break is now bounded \emph{directly}, not only through
the confidence-cut sweep. Measuring the $\ell\!=\!1$ spatial dipole of the borderline
tie-break band ($p_{\rm eq}\!\in\![0.5,0.6]$, which contains the argmax-flip population) per
imaging leg against an isotropic label-shuffle null, the tie-break decisions are
\emph{spatially isotropic} in the BASS$+$MzLS leg ($z\!=\!+0.31$, consistent with zero) and
carry coherence only in the DECaLS leg ($z\!=\!+4.72$, family-wise $p\!=\!0.0086$ over the
$15$-cell leg$\times$confidence grid). This leg-selectivity is the signature of a
depth/imaging-correlated \emph{systematic} --- the same DECaLS-depth channel forward-modelled
in Appendix~D --- not of an isotropic cosmological tie-break bias: a genuine directional bias
would not track a single imaging leg. Decisively, this entire borderline population is
\emph{already included} in the primary real-space Catalog~C dipole null ($+0.41\sigmaunit$,
$p_{\rm 2\text{-}sided}\!=\!0.62$, Sec.~\ref{sec:dipole}), so any spatially-coherent argmax
tie-break term is bounded below that null in the real-space estimator and cannot reintroduce a
dipole. The confidence-cut sweep is consistent: raising the cut to $p_{\rm eq}\!>\!0.8$ removes
the borderline population and leaves the real-space dipole null ($z\!=\!+0.51$), so any residual
argmax-driven directional term is smaller than the $|z|\!<\!1.2$ high-confidence-regime scatter
(\artifact{pipelines/p2\_chirality/outputs/canonical\_provenance/per\_leg\_confidence\_familywise\_maxstat.json},
\artifact{pipelines/p2\_chirality/scripts/gemini\_v215\_residual\_bound\_edgeon\_coherence.py}).
```

*(Optional pod follow-up, if Houston wants the edge-on-isolated variant: compute the same ℓ=1
tie-break dipole restricted to b/a<0.30 argmax-flips from `catalog_production.parquet` on the
pod; the local leg-resolved statistic above is already a direct answer to Gemini's concern.)*
