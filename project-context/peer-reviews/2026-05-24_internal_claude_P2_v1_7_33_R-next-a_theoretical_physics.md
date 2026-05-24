# P2 v1.7.33 — R-next-a theoretical-physics verdict

**Reviewer perspective:** rotating Gemini-cosmology + Sonnet theoretical-physics rigor
**Round:** 1-of-3 fresh Anthropic-rotated cross-model verification streak (post v1.7.29/v1.7.30/v1.7.33)
**Artifacts read:** `research/focused_paper_source_integration/02_full_draft.tex` (534 lines), `focused_paper_refs.bib` (Heinrich:2023 entry), `pipelines/p1_highz_tracers/outputs/step4_bias_validation/bias_validation.json`, `SSOT/paper-2/status.md`
**Date:** 2026-05-24
**OR cap:** still blocking external 5-vendor wave; this is internal-Anthropic R-next.

---

## One-line summary

Paper survives a theoretical-physics cross-check at the headline-claim level — `f_NL=-35/8` derivation is well-audited (3 benchmark match + Wick-doubling appendix), Heinrich+2023 sensitivity number is correctly cited and degraded — but **two MAJOR theoretical-rigor issues remain** (an internal contradiction between "parameter-free / tightly determined" and the κ₁∈[5.6, 80] order-of-magnitude range, and a possibly-overstated "categorically larger discriminator" claim against the physical-frame f_NL_inf→0 limit) plus three minors.

---

## Per-finding blocks

### MAJOR-1 — "Tightly determined" vs. κ₁ ∈ [5.6, 80] is an internal contradiction

**Location:** L29 abstract ("minimally parameterized local-type non-Gaussianity f_NL = -35/8"), L42 intro ("the value is tightly determined at leading order but the first correction carries substantial theoretical uncertainty"), L361 §sec:currentdata ("κ₁ ≈ 5.6 (lower bound), while including the mode-function amplitude change gives κ₁ ≈ 80 (upper bound)").

**Issue:** The paper simultaneously claims (a) the prediction is "tightly determined at leading order" with $1$–$8\%$ ε-correction uncertainty, **and** (b) the first-order coefficient κ₁ has an **order-of-magnitude** range $[5.6, 80]$ — a factor of $\sim 14$. Eq.\ \ref{eq:consistency} converts this into $c' \in [0.7, 10]$, also order-of-magnitude. The text at L367 reports "fnl ∈ [-4.35, -4.02] (a $1$–$8\%$ correction, within σ≈0.7)" using only the **lower** end of the κ₁ range; if κ₁ ≈ 80 is taken at face value at the Planck-best-fit deviation $\Delta n_s = -0.035$, the consistency-relation correction is

$$\Delta f_{\rm NL} = -\kappa_1 \cdot \Delta n_s/8 \approx -80 \cdot (-0.0044) = +0.35\text{ to } +1.4,$$

which moves f_NL from $-4.375$ up to as much as $\sim -3.0$ — a **30%+ correction**, not $1$–$8\%$. Either the κ₁ upper bound is grossly overstated and should be tightened, or the "$1$–$8\%$ ε-correction" headline is grossly understated. The two cannot both be right. The Bayes-factor analysis at §sec:bayesian §bayesian assumes the σ_theory=$0.5$–$2.0$ envelope encompasses this, but σ_theory=$1.0$ (the "recommended baseline") does **not** encompass a $\Delta f_{\rm NL} \sim +1.4$ shift — at that point the bounce prior should be widened well beyond σ_theory=$2.0$ and the BF~$\sim 4$ floor would erode further.

**Hard-fix:** Either (a) explicitly retire the κ₁=$80$ upper bound with a justification (e.g., "the mode-function-amplitude-change estimate is a heuristic that overestimates the true coefficient by an order of magnitude; numerical evaluation of the full cubic-action integrals would give κ₁ closer to the explicit-prefactor estimate κ₁≈$5.6$"), OR (b) propagate κ₁=$80$ into §sec:currentdata to give a wider $f_{\rm NL}$ range (something like $[-4.4, -3.0]$), recompute σ_theory accordingly, and revise the abstract's "tightly determined at leading order" framing. Path (a) is preferred and is consistent with the paper's existing description elsewhere of the upper bound as a "potentially amplifying" estimate.

### MAJOR-2 — "Categorically larger discriminator" overstates the physical-frame Pajer-Tanaka-Urakawa claim

**Location:** L29 abstract, L199 §sec:bayesian, L419 §sec:conclusion ("inflation predicts strictly $0$ in this observable frame; matter bounce predicts $-4.375$, a categorically larger discriminator").

**Issue:** The Pajer-Schmidt-Zaldarriaga 2013 / Tanaka-Urakawa 2011 result is that the **observable** local-template f_NL after CFC projection is parametrically smaller than the gauge-frame Maldacena value, **not** that it is exactly zero. The paper itself acknowledges this at L29: "within the gradient / projection / finite-squeezed-corrections caveats of the CFC expansion". The conclusion section's framing — "inflation predicts strictly 0 in this observable frame" — drops those caveats and is therefore strictly stronger than the cited literature supports. There are residual finite-squeezed corrections at $\mathcal{O}((k_3/k_1)^2)$ and gradient-expansion corrections; CFC projection takes you from $\mathcal{O}(1-n_s)\approx 0.015$ down to something like $\mathcal{O}((k_3/k_1)^2 \cdot \text{slow-roll})$, **not** identically zero. Furthermore — and this is the load-bearing point — the **survey estimators** (SPHEREx and BOSS local-template), as the paper itself notes at L29, **measure the gauge-frame quantity, not the CFC physical-frame quantity**. So the "categorically larger discriminator" framing in the Conclusion is rhetorically pointing at a quantity that the observations cannot access. Either downgrade the rhetorical contrast or be explicit that this is a theoretical observation about the *underlying* physics that the SPHEREx local-template forecast cannot directly verify.

**Hard-fix:** Replace "inflation predicts strictly 0 in this observable frame; matter bounce predicts $-4.375$, a categorically larger discriminator" with something like "inflation predicts a CFC-frame value parametrically smaller than the already-small gauge-frame $\mathcal{O}(0.015)$ — but since the SPHEREx and BOSS estimators measure the gauge-frame local template, this physical-frame statement is a theoretical complement rather than an additional on-sky discriminator beyond the gauge-frame $\sim 290\times$ ratio already quoted."

### minor-1 — Bispectrum normalization constant `c` chain partially obscured

**Location:** App.\ \ref{app:convention}, L437–443.

**Issue:** The appendix says "Planck/Komatsu-Spergel convention: $c = 2$" but the abstract (L29) and Sec.\ \ref{sec:spherex} (L170) both quote the bispectrum normalization as $B^{\rm local} = (6 f_{\rm NL}/5)[P P + \text{perms}]$. The factor "6/5" already absorbs the convention into a single coefficient; a reader matching against Komatsu-Spergel will know the $6/5 \equiv 2 \cdot 3/5$ comes from $c=2$ times the $\zeta = \zeta_g + \tfrac{3}{5} f_{\rm NL}\zeta_g^2$ field definition, but a quick-read reviewer (or external referee) could conflate the two factors. One short sentence in App.\ A would close this: "the $6 f_{\rm NL}/5$ prefactor used in Sec.\ \ref{sec:spherex} comes from $c=2$ times the $3/5$ field-definition prefactor; this is the Planck observational convention."

### minor-2 — "n_s is a fit, not a prediction" deserves a more prominent flag

**Location:** L122 §sec:benchmark "$n_s = 0.964$ (from $w = -0.003$, one free parameter tuned to the Planck observed $n_s = 0.9649 \pm 0.0042$; the spectral index formula $n_s = 1 + 12w$ follows from the growing-mode solution...so $n_s$ is a fit to the data rather than a prediction)".

**Issue:** This is a clear-eyed disclosure but is buried deep in the text and is **not** signaled at the abstract or intro. A theoretical-cosmologist reading the paper without skimming §sec:benchmark would assume the matter-bounce "complete observational package" includes a genuine n_s prediction; what the paper is actually doing is **fitting** $w$ to the Planck $n_s$ and then **predicting** $f_{\rm NL}$ from $w$. That is fine — but the framing should be unambiguous. A one-clause flag in the abstract or §sec:intro ("the equation-of-state parameter $w \approx -0.003$ is fixed by the observed Planck spectral tilt $n_s = 0.9649$ via $n_s = 1 + 12w$; the matter-bounce f_NL prediction at the resulting $\epsilon$ is then a downstream consequence") would prevent reviewers from over-claiming what the bounce "predicts".

### minor-3 — Joint-Fisher $9.9\sigma$ caveat is honest but the abstract framing is still slightly ambiguous

**Location:** L29 abstract ("A separate joint $(f_{\rm NL}, n_{f_{\rm NL}})$ scale-dependent-bias Fisher analysis is discussed... as an idealized-Fisher self-consistency check... the specific numerical significance is not quoted here in the abstract until that release lands"), L403 §sec:discussion ("the matter-bounce $f_{\rm NL}$ remains detectable at ~9.9σ in the joint analysis...$\sigma_{\rm unmarg}(f_{\rm NL}) \approx 0.114$ from this joint analysis would be 6.1× sharper than the bispectrum-only $\sigma(f_{\rm NL})=0.7$ baseline, which is sharper than any published SPHEREx SDB forecast known to us").

**Issue:** The abstract correctly defers the $9.9\sigma$ number, and §sec:discussion correctly flags that the implied $\sigma_{\rm unmarg}=0.114$ is **sharper than any published SPHEREx forecast**. The honest framing is appreciated. But the very fact that the implied sensitivity is 6× tighter than anything in the public literature is itself a red flag that the joint-Fisher arithmetic has an upstream input error — most likely in the assumed $f_{\rm sky}$, the 6-bin information stacking, or the $b_\phi$ prior. The paper should add one explicit sentence: "the implied 6× sharpening **likely reflects an unphysical Fisher input** (overly optimistic $k_{\min}$, $f_{\rm sky}=0.75$, or $b_\phi$ universality assumption) rather than a real survey-design discovery; the companion artifact will diagnose the offending input." Without that, an external referee will read the $9.9\sigma$ as a positive forecast and ask for the Fisher inputs — which the SSOT confirms are not on disk.

### nit-1 — Abstract single-sentence length

**Location:** L29.

**Issue:** The abstract is a single 67-line paragraph. RevTeX renders fine, but readability is poor for a forecast paper that already has post-systematic, optimistic, pre-systematic, convention-reversal, and Bayes-factor-grid numbers competing for attention. Splitting into 2–3 sentences (results / systematic budget / convention sensitivity) would lift readability without changing any number.

---

## What survived cleanly (cross-check confirmations)

- **f_NL = −35/8 derivation:** Three-benchmark match (Table~\ref{tab:benchmarks}) is exact to published Cai+2009 values; Appendix A.1 Wick-expansion of the −2 Im commutator identity is a clean operator-algebra derivation; the 0.5000 ε-decomposition ratio is an independent empirical signature. No hidden tuning detected in the cubic sector at zeroth ε-order.
- **Heinrich+2023 σ(f_NL) = 0.7:** Citation is correct (`Heinrich:2023`, PRD 109 123511, arXiv:2311.13082 — author list Heinrich-Doré-Krause matches). Bispectrum normalization $B^{\rm local} = (6 f_{\rm NL}/5)[P P + \text{perms}]$ is correctly stated. Three caveats (b_φ universality, local-template assumption, full-survey-depth assumption) are explicitly flagged at L172. The shape-mismatch r=0.84 ± 0.02, the ε-correction propagation, b_φ marginalization $\mathcal{O}(20-50\%)$ widening, and relativistic-projection $\sigma_{\rm GR}$ envelope are all consistently propagated through to the final 3–5σ post-systematic significance.
- **Bispectrum vs power-spectrum scope:** Cleanly separated. The bispectrum forecast (σ=0.7) is the headline; the scale-dependent-bias channel is presented as the complementary SDB observable; cross-channel contamination (b_φ cross-terms in the bispectrum) is explicitly noted at L299.
- **Post-systematic vs optimistic distinction:** 5.2–5.5σ optimistic is anchored in $|f_{\rm NL}| \cdot r / \sigma = 4.375 \cdot 0.83$–$0.876 / 0.7$; 3–5σ post-systematic follows from the GR+b_φ degradation in Table~\ref{tab:gr} and the b_φ universality-relaxation widening. The arithmetic is internally consistent.
- **Bounce-vs-inflation discriminator:** The sign is unambiguously opposite (matter bounce −4.375, single-field slow-roll +0.015 in the gauge frame); equilateral-shape DBI is excluded at the shape level; non-attractor inflation gives +5/2 (wrong sign); curvaton class requires ≥2 tuned parameters to reach −4.375. The discrimination claim is defensible **within the curvaton-class framing** explicitly noted at the QSFI-closure paragraph (L280).
- **Units/dimensions on bispectrum:** $\zeta$ is dimensionless, $P_\zeta$ has the usual $k^{-3}$ dimensions, the bispectrum normalization $(6 f_{\rm NL}/5)[P_1 P_2 + \text{perms}]$ is dimensionally consistent, the shape function $A_T = (3/256\,k_1^2 k_2^2 k_3^2) P(k_1,k_2,k_3)$ with degree-9 polynomial $P$ gives $A_T \sim 1/k^6 \cdot k^9 = k^3$, and $B_{\rm NL} = (10/3)\,A_T/\sum k_i^3$ is dimensionless — all clean.
- **Suyama-Yamaguchi inequality:** Correctly framed as $\tau_{\rm NL} \geq (6 f_{\rm NL}/5)^2$ (inequality, not saturation), with the explicit caveat that bounce is not exactly local (L405). This was a real fix from R-round-3.

---

## Verdict

**Status:** NOT clean (2 MAJOR + 3 minor + 1 nit). Per §4.4.1 cascaded-loop-exit, a clean round requires 0 BLOCKER + 0 MAJOR. R-next-a does **not** satisfy that bar; v1.7.33 → v1.7.34 closure of MAJOR-1 (κ₁ contradiction) and MAJOR-2 (physical-frame discriminator overstatement) is mandatory before R-next-b/c can deliver a clean streak.

**Readiness impact:** 95% cap holds. Honest mid-streak rollback to ~88% is appropriate while MAJOR-1 and MAJOR-2 are open. Forward step to 92% after closure of both MAJORs in v1.7.34. The 95% ceiling stays gated on a clean R-next-c PLUS the still-blocked external 5-vendor wave PLUS Houston sign-off.

**Recommended next action:** v1.7.34 bundled closure of MAJOR-1 (retire κ₁=80 with explicit justification) + MAJOR-2 (tone down "categorically larger discriminator" in Conclusion) + minor-1 (one-sentence c=2 chain note in App. A) + minor-2 (abstract-level n_s-is-fit flag) + minor-3 (one-sentence likely-Fisher-input-error caveat on the 9.9σ). All five are text-only edits; no recompile-blocking changes; PDF impact <500 bytes. Then R-next-b should land clean.
