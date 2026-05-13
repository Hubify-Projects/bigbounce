# P2 v1.7.26 — GPT-5 Adversarial Review (Methodology)
**Date:** 2026-05-13 (13:30 PT)
**Reviewer persona:** OpenAI GPT-5, statistical-methodology lens (Gelman/Vehtari-flavored adversarial)
**Paper:** `research/focused_paper_source_integration/02_full_draft.tex` v1.7.26 / 492 lines / 38 bibitems
**Headline under review:** σ(f_NL)=0.7 (Heinrich+2024) → 5.2–5.5σ optimistic → 3–5σ post-systematic; joint (f_NL, n_fNL) Fisher = 9.9σ idealized.
**Prior rounds closed before this round:** R20, R31–R35, R41, R42 (Waves 11-D, 11-F, 14-K, 14-AA, 14-VV, 14-AAA, 14-FFF). SSOT readiness 84 % (drive-to-99 cap; Houston-only 1 %).

## Summary counts: B/M/m/n

| Severity | Count |
|---|---:|
| BLOCKER | 2 |
| MAJOR | 5 |
| MINOR | 4 |
| NIT | 3 |
| **TOTAL** | **14** |

**Most concerning finding (one sentence):** The joint $(\fnl, n_\fnl)$ Fisher arithmetic in §VIII.D is internally inconsistent — $\sigma_{\rm marg}/\sigma_{\rm unmarg}=1/\sqrt{1-\rho^2}\approx 3.86$ at $\rho=0.966$ implies $\sigma_{\rm unmarg}(\fnl)\approx 0.114$, which is ~6.1× sharper than the bispectrum-only $\sigma(\fnl)=0.7$ baseline, and the paper never tells the reader where that 6× improvement comes from before quoting 9.9σ as a flagship number.

---

## BLOCKERs

### B1: Joint Fisher unmarginalized $\sigma(\fnl)$ is undefined / unjustified (line 369)
**Quote (line 369):** "the marginal/unmarginal ratio $\sigma_{\rm marg}/\sigma_{\rm unmarg} = 1/\sqrt{1-\rho^2} \approx 3.86$ at $\rho = 0.966$ is the multi-bin SDB Fisher-combination ratio after the six-bin information stack, not a direct conversion of the single-bin bispectrum-only $\sigma(\fnl) = 0.7$"

**Issue:** Arithmetic check: $\sigma_{\rm marg}=0.44$ and $\sigma_{\rm marg}/\sigma_{\rm unmarg}=3.8678$ ⇒ $\sigma_{\rm unmarg}(\fnl)=0.1138$. This is 6.15× sharper than the bispectrum-only $\sigma(\fnl)=0.7$ baseline that drives the rest of the paper. The text explicitly says the 9.9σ "is not the same baseline as the bispectrum-only 5.2–5.5σ optimistic figure; the two come from different Fisher matrices and target different observables" — but the paper never identifies WHERE the $\sigma_{\rm unmarg}=0.114$ number originates. It is not in Heinrich 2024 (a bispectrum forecast, not SDB), it is not in Schlegel 2022 (MegaMapper, not SPHEREx), and the "companion artifact" Fisher-input release is explicitly deferred (line 369: "full six-bin Fisher-input release ... deferred to a companion artifact"). A 9.9σ headline that rests on a 6× improvement of an externalized literature number cannot be sourced to a deferred companion — it has to be on disk, with the six-bin Fisher inputs published, before the number is quotable.

For comparison, Münchmeyer+2019 (the canonical SPHEREx SDB-only Fisher this work cites in §IV) gives $\sigma(\fnl) \approx 0.9$–$1.5$ for SPHEREx SDB alone depending on $k_{\min}$ — which is *worse* than the bispectrum, not 6× sharper. The 0.114 unmarginalized SDB number is therefore in tension with every published SPHEREx SDB forecast.

**Fix:** EITHER (a) release the six-bin Fisher inputs (k_min(z), n̄(z), b_1, b_φ, σ_z, V_bin) and the Jacobian of the 9.9σ number in the same commit as v1.7.27, OR (b) demote the 9.9σ from a discussion-section flagship to a single-sentence forward-looking caveat ("a joint SDB analysis could improve the constraint subject to ultra-large-scale modeling; see future work"), OR (c) remove it from the abstract entirely. The current state — abstract-prominent 9.9σ + body "deferred to companion" — is the textbook recipe for a reviewer-rejected forecast.

### B2: Heinrich+2024 σ(f_NL)=0.7 is at the *local-template* fiducial, not at f_NL = -4.375 (line 29, line 152)
**Quote (line 29, abstract):** "The SPHEREx multi-tracer bispectrum achieves $\sigma(\fnl^{\rm local}) \approx 0.7$ (Heinrich \etal~2024~\cite{Heinrich:2023}, Fig.~6 / Table~3, multi-tracer galaxy bispectrum forecast under the local-template normalization)"
**Quote (line 152, §IV):** "forecasts $\sigma(\fnl^{\rm local}) = 0.7$ from the bispectrum alone"

**Issue:** Heinrich+2024 (JCAP 04, 074, arXiv:2311.13082) reports $\sigma(\fnl)$ around fiducial $\fnl=0$, not around $\fnl=-4.375$. For a Gaussian likelihood this distinction usually does not matter — but the matter-bounce forecast in this paper assumes the *fiducial-Fisher* is invariant under the central-value shift to $\fnl=-4.375$, and the matter-bounce bispectrum template is approximately but not exactly local ($r=0.84$). The Heinrich number is the SPHEREx sensitivity to local-template $\fnl$ at zero, *not* the sensitivity to the bounce shape at $\fnl=-4.375$. The paper applies the projection factor $r=0.84$ post-hoc (Eq. 4), which is correct procedurally, but the underlying Fisher matrix $F^{\rm local}_{\fnl\fnl}$ may also shift when re-evaluated at fiducial $\fnl=-4.375$ because the multi-tracer bispectrum estimator covariance has a (weak) $\fnl$-dependence through the scale-dependent bias cross-terms (the same $\Delta b(k) \propto \fnl\,b_\phi/k^2$ terms invoked in §VII.B for the b_φ sensitivity).

The paper acknowledges this *halfway* at line 154 ("the forecast assumes a purely local bispectrum template") and corrects for the shape mismatch, but does not propagate the central-value shift through the Fisher itself. The $5.25\sigma = 0.84 \times 6.25\sigma$ arithmetic assumes $\sigma(\fnl)$ is the same at $\fnl=0$ and $\fnl=-4.375$, which is only true to leading order in the Fisher expansion.

**Fix:** (a) Add one sentence to §IV stating explicitly that the Heinrich $\sigma(\fnl)=0.7$ is the Fisher around $\fnl=0$, that the matter-bounce-shifted Fisher around $\fnl=-4.375$ is approximated as identical to leading order, and that the leading correction is $\mathcal{O}(\fnl \cdot b_\phi / k^2)$ at the scale-dependent-bias cross-term level (sub-percent at SPHEREx scales). (b) OR, if a recomputation is available on Pod 3, redo the Fisher at the bounce fiducial and report the actual $\sigma(\fnl)|_{\fnl=-4.375}$ side-by-side with the $\fnl=0$ baseline. The current treatment lets readers assume Heinrich anchored at $\fnl=-4.375$, which they did not.

---

## MAJORs

### M1: Bayes-factor arithmetic at $\sigma_{\rm theory}=1.0$ vs $[-5,+5]$ does not match analytic formula (line 183, line 217)
**Quote (line 183):** "under the curvaton-natural $[-5, +5]$ prior the headline Bayes factor at the recommended $\sigma_{\rm theory} = 1.0$ bounce prior is $\mathrm{BF} \approx 6$"
**Quote (line 217, table cell):** "$\sigma_{\rm theory} = 1.0$ Gaussian | multifield prior $[-5,+5]$: $\mathrm{BF} \sim 6$"

**Issue:** Direct analytic evaluation of the Bayes factor formula in Eq. (10):
$$B = (\fnl^{\max}-\fnl^{\min}) \cdot \frac{\int \mathcal{N}(\fnl|-4.375, 1.0) \mathcal{L}(\fnl^{\rm obs}|\fnl) d\fnl}{\int_{-5}^{+5} \mathcal{L}(\fnl^{\rm obs}|\fnl) d\fnl}$$
with $\fnl^{\rm obs}=-4.375$, $\sigma=0.7$, $\sigma_{\rm theory}=1.0$, evaluates numerically to **BF ≈ 4.0**, not BF ≈ 6.

For the four-corner table (line 213–217):
| Configuration | Paper's value | Analytic (my recomputation) |
|---|---:|---:|
| Delta vs $[-15,+15]$ | $\sim 17$ | 17.1 ✓ |
| Delta vs $[-5,+5]$ | $\sim 7$ | 7.0 ✓ |
| Gauss $\sigma_{\rm theory}=1.0$ vs $[-15,+15]$ | $\sim 8$ | 9.8 (~22 % low) |
| Gauss $\sigma_{\rm theory}=1.0$ vs $[-5,+5]$ | $\sim 6$ | 4.0 (~50 % HIGH) |
| Gauss $\sigma_{\rm theory}=0.5$ vs $[-15,+15]$ | $\sim 12$ | 13.9 (~14 % low) |
| Gauss $\sigma_{\rm theory}=2.0$ vs $[-15,+15]$ | $\sim 4$ | 5.7 (~30 % low) |

The pattern of discrepancies is not random: the delta-prior rows are exact, but every Gaussian-prior row is off by 20–50 %. This strongly suggests the Gaussian-prior Bayes factors in the paper were computed under a *different* formula (perhaps a saddle-point approximation, or a different definition of the bounce prior normalization) than the literal Eq. (10).

**Fix:** Either (a) recompute the Gaussian-bounce-prior Bayes factors using Eq. (10) literally and update Table II to reflect the actual numbers, OR (b) document the actual formula used (e.g., "we use the saddle-point approximation $B \approx ...$") with a one-paragraph derivation. The current state — quoting BF ~ 8 at $\sigma_{\rm theory}=1.0$ vs $[-15,+15]$ when the formula gives 9.8 — is mid-magnitude consistent, but the BF ~ 6 vs the formula's 4.0 at $\sigma_{\rm theory}=1.0$ vs $[-5,+5]$ is a real arithmetic gap. The curvaton-natural Bayes factor is the *new* abstract headline number after R42 Wave 14-AA — getting that one wrong by 50 % undermines the recommended-baseline framing.

### M2: Higuchi bound is misquoted as $\mu/H = 3/2$ rather than $\mu^2/H^2 = 2$ in dS (line 369, line 246)
**Quote (line 369):** "at $\mu/H = 3/2$ (Higuchi-bound limit) $\Delta = 3/2$ and the exponent vanishes"
**Quote (line 246):** "Across $\mu/H \in [0,\,3/2]$ the QSFI bispectrum interpolates"

**Issue:** The Higuchi bound for massive spin-$s$ fields in de Sitter is $m^2 \geq s(s-1)H^2$. For spin-2 it gives $m^2 \geq 2 H^2$, i.e., $\mu/H \geq \sqrt{2} \approx 1.41$ as a lower bound for unitary spin-2 propagation. For the spin-0 (scalar) QSFI case relevant to this paper (Chen & Wang 2010), the QSFI scalar's mass is not Higuchi-constrained — the Higuchi bound does not apply to scalars at all. What the paper actually means is the *complementary-vs-principal-series transition* at $\mu^2/H^2 = 9/4$, i.e., $\mu/H = 3/2$, where the scaling dimension $\Delta = 3/2 - \sqrt{9/4 - \mu^2/H^2}$ becomes complex (the field transitions from heavy to light in dS representation theory). That transition is well-defined, but calling it the "Higuchi bound" is a category error: Higuchi is about spin, not about light-vs-heavy scalars.

**Fix:** Replace "Higuchi-bound limit" with "complementary-series transition" or "principal-vs-complementary series boundary at $\mu/H = 3/2$" in both line 246 and line 369. Add the standard reference Chen & Wang 2010 / Arkani-Hamed & Maldacena 2015 for the QSFI light-vs-heavy regime if not already in the bib. The Higuchi attribution will be caught by any cosmologist on the QSFI literature in five minutes and is the kind of thing that gets a referee report saying "the authors don't understand the bound they cite."

### M3: $r=0.84$ noise-weighted overlap derivation is reported but never written as an equation (line 137, §III.B)
**Quote (line 137):** "Using the physics-derived polynomial, we computed $r$ under 10 physically motivated weighting schemes ... The result is robust: $r = 0.84 \pm 0.02$"

**Issue:** The paper claims $r$ is a "noise-weighted shape mismatch" (abstract line 29), but the actual definition of $r$ as a weighted inner product over the bispectrum shape function is given only in prose at line 127 ("the Fisher-weighted average of the bounce shape function normalized to the squeezed-limit value $\BNL^{\rm squeeze} = -35/8$") without ever being written down as an equation. The reader is told $r \in [0.821, 0.879]$ across schemes and that "the squeezed-limit cutoff is completely insensitive" — but cannot reproduce the calculation without the explicit weighting kernel $w(k_1,k_2,k_3)$ and the integration measure.

A reproducibility-grade definition would be:
$$r = \frac{\int dV_T \, w(k_1,k_2,k_3) \, B^{\rm bounce}(k_1,k_2,k_3) \, B^{\rm local}(k_1,k_2,k_3) / \sigma^2_B(k_1,k_2,k_3)}{B^{\rm bounce}(k,k,0) \int dV_T \, w(k_1,k_2,k_3) \, [B^{\rm local}]^2 / \sigma^2_B}$$
or whatever the actual definition is.

**Fix:** Add one display equation in §III.B (around line 127) giving the explicit definition of $r$ as a Fisher-weighted shape-cosine, with the weighting kernel for each of the 10 schemes specified in an Appendix or in a supplementary table. Currently the $r=0.84$ derivation is a black box and the reader has to trust the 10-scheme robustness claim without being able to check any single scheme.

### M4: $n_{\fnl}=0$ "testability $\pm 0.09$" conflates marginalized 1σ with detection threshold (line 369)
**Quote (line 369):** "The $n_{\fnl} = 0$ prediction is testable to $\pm 0.09$ at the same idealized-Fisher level."

**Issue:** The $\pm 0.09$ comes from the marginalized $\sigma(n_{\fnl}) = 0.086$ of the joint Fisher. But "testable to $\pm 0.09$" is ambiguous: it conflates the 1σ uncertainty on the *measurement* with the discrimination threshold against alternatives. The bounce predicts $n_{\fnl}=0$ exactly; the relevant question is *how far from zero* a competitor's $n_{\fnl}$ has to be to be distinguishable. The paper then cites "DBI inflation predicts $n_{\fnl} \sim 0.08$, yielding only ${\sim}0.9\sigma$ separation" — which is consistent with $\sigma(n_{\fnl}) = 0.086$ but presents the DBI discrimination as a *weakness* rather than acknowledging that the $\pm 0.09$ "testability" is barely above the DBI prediction itself.

**Fix:** Reframe as: "the marginalized 1σ uncertainty $\sigma(n_{\fnl}) = 0.086$ corresponds to a ${\sim}1\sigma$ discrimination against DBI inflation ($n_{\fnl} \sim 0.08$) but only a $\geq 3\sigma$ discrimination against alternatives with $|n_{\fnl}| \geq 0.26$." This makes the actual discriminating power transparent rather than packaging it as "testable to $\pm 0.09$" — which is technically true but reads as a stronger statement than the data supports.

### M5: Quasi-dust $w = -0.003$ correction propagation is hand-waved at "1–8 %" (line 100, line 327)
**Quote (line 100):** "Explicit cubic-action prefactors give a correction of ${\sim}\,0.6\%$, but the mode-function growth rate also changes with $\epsilon$, potentially amplifying the correction to ${\sim}\,1$--$8\%$."
**Quote (line 327):** "$\kappa_1 \approx 5.6$ (lower bound), while including the mode-function amplitude change gives $\kappa_1 \approx 80$ (upper bound)."

**Issue:** $\kappa_1$ ranges over 14× (5.6 to 80) — a more-than-order-of-magnitude theoretical uncertainty in the leading-order $\epsilon$-correction coefficient. This propagates into the $\fnl$ prediction as: $\fnl(\epsilon=3/2 - \delta) = -35/8 + \kappa_1 \delta$, with $\delta = -0.003 \cdot (3/2)/(1-...) \sim \mathcal{O}(10^{-3})$. So $\Delta \fnl \in [\kappa_1 \cdot 10^{-3}] = [0.006, 0.08]$ in absolute value, i.e., 0.14 %–1.8 % fractional shift in $\fnl$, not 1–8 %. The 1–8 % range in the body text appears to come from a different propagation (perhaps including the shape-distortion correction at $r$-level rather than the value-level correction).

The paper notes (line 100) that there are two channels — "value shift" and "shape shift" — and that "both must be propagated jointly into the forecast." But the joint propagation is never carried out; the 1–8 % is asserted, not derived. For a Bayesian analysis that uses $\sigma_{\rm theory}=1.0$ as the *recommended baseline* (which "encompasses the full $\epsilon$-correction range"), the 1–8 % vs my-arithmetic 0.14–1.8 % is the difference between $\sigma_{\rm theory}=0.4$ (modest broadening) and $\sigma_{\rm theory}=1.0$ (substantial broadening that costs the analysis ~2× in BF).

**Fix:** Either (a) write down the explicit relation between $\delta_w$, $\delta_\epsilon$, $\kappa_1$, and $\Delta \fnl/\fnl$ and propagate it cleanly to derive the 1–8 % range, OR (b) bound $\Delta\fnl$ above by $|\kappa_1^{\max}| \cdot \delta\epsilon = 80 \cdot 4.5 \times 10^{-3} \approx 0.36$, i.e., a $\sim 8$ % multiplicative correction (in line with the upper end of the quoted range), and explicitly justify this as the leading-order bound. The current presentation of "1–8 %" with no derivation is hand-waved.

---

## MINORs

### m1: "Universality assumption $b_\phi = 2\delta_c(b_1-1)$" treated as Heinrich+2024's choice but Heinrich actually uses Barreira's calibration (line 154, line 265)
**Quote (line 265):** "Heinrich \etal~\cite{Heinrich:2023} marginalize over $b_\phi$ for the SPHEREx multi-tracer bispectrum forecast assuming the universal-mass-function relation $b_\phi = 2\delta_c (b_1 - 1)$"

**Issue:** Verify against Heinrich+2024 (arXiv:2311.13082) — the actual treatment of $b_\phi$ in Heinrich is closer to the Barreira+2020/2022 simulation-calibrated bias relations than to the pure-universality $2\delta_c(b_1-1)$ form. The paper's framing implies Heinrich is the "universality" baseline that Barreira improves upon; in fact both are simulation-based and the universality assumption is the *theoretical* prior that pre-dates both. This is a small but important attribution issue.

**Fix:** Re-read §3.2 of Heinrich+2024 and quote the actual $b_\phi$ treatment used. If Heinrich uses Barreira's calibration, restate the §VII.B paragraph: "Heinrich+2024 use the Barreira+2020 simulation-calibrated $b_\phi$ values per tracer bin, which already relaxes the pure-universality $b_\phi = 2\delta_c(b_1-1)$ form." This avoids accidentally implying Heinrich's forecast can be tightened by switching to Barreira — when it already uses Barreira.

### m2: 200 MC injection-recovery test is undersized for $r = 0.90 \pm 0.01$ claim (line 70)
**Quote (line 70):** "An injection/recovery test using 200 Monte Carlo realizations confirms that a local-template estimator applied to a bounce-shaped signal recovers $r_{\rm measured} = 0.90 \pm 0.01$"

**Issue:** 200 MC realizations give a standard error on the mean of $\sigma/\sqrt{200} \approx 0.0\bar{7} \times \sigma$. The reported $\pm 0.01$ on $r$ implies $\sigma_r \approx 0.14$ per realization (which is consistent with the $r=0.85 \pm 0.13$ null-space scatter), and the $\sqrt{200}$ reduction gives SE ≈ 0.010 — which matches. So the arithmetic is internally consistent, but 200 MC is small for a 1 %-precision claim. The $r_{\rm measured}=0.90 \pm 0.01$ also lies *above* the noise-weighted central value $r=0.84 \pm 0.02$ (CMB Fisher gives 0.876, LSS noise weighting gives 0.83), and the paper explains the offset as "the injection-recovery test uses isotropic Gaussian noise (effectively CMB-like weighting)." That is fine, but it means the 200-MC test is a *consistency check on CMB-like weighting*, not on the LSS noise weighting actually relevant to SPHEREx. The body of the paper uses $r=0.84$ for SPHEREx, not $r=0.90$.

**Fix:** Either (a) run the injection-recovery test under realistic SPHEREx-noise weighting (not isotropic Gaussian) so the $r_{\rm measured}$ is a check on the actual $r=0.83$ adopted for SPHEREx, OR (b) explicitly footnote that the 200-MC $r=0.90$ is a CMB-weighting consistency check, not an SPHEREx-noise validation. The current §III.B treatment is slightly misleading because the high-precision $r=0.90$ from MC is reported alongside the LSS noise-weighted $r=0.84$ without making clear they answer different questions.

### m3: $b_\phi$ Gaussian prior with 20 % scatter not specified as "fractional" vs "additive" (line 202)
**Quote (line 202):** "PNG bias parameter $b_\phi$ uncertainty as a Gaussian with 20\% scatter"

**Issue:** 20 % of what? A 20 % fractional scatter ($\sigma(b_\phi) = 0.2 \cdot b_\phi^{\rm fid}$) is very different from a 20 % additive scatter ($\sigma(b_\phi) = 0.2$ regardless of fiducial). For galaxy bias parameters where $b_\phi^{\rm fid}$ can range over $[1, 10]$, this matters by an order of magnitude. Line 263 says "$\sigma(b_\phi)/b_\phi = 0.2$" — fractional — but line 202's MC description is ambiguous and the two should be cross-referenced.

**Fix:** Add "$\sigma(b_\phi)/b_\phi = 0.2$" inline at line 202 to remove the ambiguity.

### m4: "Bayes factor formula in Eq. 10 marginalizes over uniform competitor priors only" — Gaussian-bounce prior case not derived (line 198–200)
**Quote (line 200):** "$B = \frac{(\fnl^{\rm max} - \fnl^{\rm min}) \times \mathcal{L}(\fnl^{\rm obs} \mid \fnl = -35/8)}{\int_{\fnl^{\rm min}}^{\fnl^{\rm max}} \mathcal{L}(\fnl^{\rm obs} \mid \fnl)\, d\fnl}\,.$"

**Issue:** Eq. (10) is the delta-prior Bayes factor formula. The body then quotes Bayes factors at $\sigma_{\rm theory} = 0.5, 1.0, 2.0$ (lines 207–209) — all of which require a *different* formula (numerator integrated against the Gaussian bounce prior). The paper never writes down the Gaussian-prior Bayes factor formula explicitly. Combined with the M1 finding that the numerical values disagree with my analytic recomputation by 20–50 %, the lack of an explicit Gaussian-prior formula in the body makes the discrepancy harder to diagnose.

**Fix:** Add one display equation immediately after Eq. (10) showing $B^{(\sigma_{\rm theory})} = (\fnl^{\max}-\fnl^{\min}) \cdot \int \mathcal{N}(\fnl|-35/8,\sigma_{\rm theory}) \mathcal{L}(\fnl^{\rm obs}|\fnl) d\fnl / \int_{\fnl^{\min}}^{\fnl^{\max}} \mathcal{L}(\fnl^{\rm obs}|\fnl) d\fnl$, so the Gaussian-prior values are traceable to a formula the reader can check.

---

## NITs

### n1: Abstract is one paragraph, ~575 words (line 28–30)
The PRD-style abstract should target ~250 words for a Letter and ~400 words for a Regular Article. The current 575-word single paragraph is hard to parse and re-states the same prior-grid envelope (BF ~ 8–17) three times. Consider breaking into two paragraphs and consolidating the prior sensitivity into one self-contained sentence.

### n2: "M\"unchmeyer" typesetting (line 152)
LaTeX should render this cleanly via `M\"unchmeyer`; verify in the compiled PDF that the umlaut renders correctly under revtex4-2 + UTF-8 input (it can fail silently). Cross-check the bibitem author field.

### n3: "$n_s = 8\epsilon - 11$" (line 323) — sign-of-derivation footnote should be inline rather than in a separate "Linearization note"
The relation is derived from $n_s = 1 + 12w$ via $\epsilon = 3(1+w)/2$, which gives $w = (2\epsilon - 3)/3$ and therefore $n_s = 1 + 12 \cdot (2\epsilon-3)/3 = 1 + 8\epsilon - 12 = 8\epsilon - 11$. Trivial arithmetic but the separation between formula and derivation in the current text reads as if the formula is asserted, then defended in a footnote.

---

## Reviewer disposition

**Recommendation:** REVISE before submission. Two BLOCKERs (B1 joint-Fisher provenance, B2 Heinrich anchor central-value shift) directly affect the abstract's flagship 9.9σ and 5.2–5.5σ numbers. The Bayes-factor arithmetic discrepancy (M1) affects the *recommended-headline* BF ~ 6 number that R42 Wave 14-AA installed as the curvaton-natural baseline.

The paper is otherwise rigorous, transparent, and well-organized — particularly the Appendix A.1 Wick-doubling derivation and the explicit prior-sensitivity ladder in §VI.C are above-peer-review-bar work. The novel content (matter-bounce template-mismatch $r=0.84$ quantification, mechanism-independent $\fnl$ argument via ECH transparency) is real and defensible. The methodological weaknesses are concentrated in the *forecast-arithmetic chain* (Heinrich anchor + Bayes-factor formula consistency + joint-Fisher provenance), which is exactly the part of the paper most exposed to adversarial statistical-methodology review.

**Prior-rounds gap:** R42 Waves 14-AA, 14-VV, and 14-K closed the BF prior-sensitivity framing, the Planck PR4 cite, and the Cai-vs-Li convention. None of those rounds caught the *numerical* mismatch between the analytic Bayes-factor formula (Eq. 10 + Gaussian extension) and the quoted BF values, nor the unsourced 6× improvement implied by the joint-Fisher arithmetic. This is the natural blind spot of cross-vendor reviews that focused on framing and provenance — a methodology lens catches it on first arithmetic recomputation.

**Expected post-revision outcome:** If B1 + B2 are closed (companion-artifact Fisher inputs released OR 9.9σ demoted; Heinrich central-value-shift caveat added) and M1 is closed (BF table regenerated against the literal formula), the paper is at submission-ready status under R45 + cross-vendor close.

---

_Generated by a GPT-5 adversarial-methodology persona running against `02_full_draft.tex` v1.7.26. All numerical recomputations performed independently in Python with scipy.integrate.quad on Eq. (10) and the standard joint-Fisher marginal/unmarginal ratio identity. SSOT status (Paper 2, 2026-05-02 11:30 PDT) reviewed before authoring._
