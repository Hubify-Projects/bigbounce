# P1B auto-2026-06-09_0025pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 269.9s

---

# Meta-Review: P1B Companion Paper

Five referees have catalogued the paper's well-known problems (future arXiv IDs, scope creep, internal-audit prose, structural confusion, Bayes-factor omissions, Table II error-propagation). My job is to find issues that none of them caught. The list below is restricted to genuinely new findings.

---

## P1B-META-E1 (ESSENTIAL) — Table II footnote b is not merely arithmetically wrong, it is mathematically impossible

**Section/page:** Table II, footnote b, p. 4.
**Why missed:** Gemini correctly flagged "the variance formula is wrong by a factor of ~6," but stopped at the arithmetic. No reviewer worked out what the quoted numbers imply about the underlying covariance matrix.

**Specific problem:** The footnote asserts $a_p = 0.668$, $\sigma_{w_0}=0.0436$, $\sigma_{w_a}=0.1864$, and $\sigma_{w_{\rm pivot}}=0.0301$. The standard pivot relation gives
$$\sigma^2_{w_{\rm pivot}} = \sigma^2_{w_0} - (1-a_p)^2 \sigma^2_{w_a},$$
so for $\sigma^2_{w_{\rm pivot}} \geq 0$ one requires $\sigma_{w_0}/\sigma_{w_a} \geq |1-a_p|$. Plugging in: $0.0436/0.1864 = 0.234 < 0.332 = 1-a_p$. The pivot variance comes out **negative**.

Equivalently, the decorrelation condition forces $\rho \equiv {\rm Cov}(w_0,w_a)/(\sigma_{w_0}\sigma_{w_a}) = -(1-a_p)\sigma_{w_a}/\sigma_{w_0} = -1.42$. A correlation coefficient of magnitude 1.42 is **not a valid covariance matrix**. The triple $(\sigma_{w_0},\sigma_{w_a},a_p) = (0.0436, 0.1864, 0.668)$ cannot coexist.

**Required fix:** Either $\sigma_{w_0}$ is wrong (must be $\geq 0.062$), $\sigma_{w_a}$ is wrong (must be $\leq 0.131$), or $a_p$ is wrong (must be $\geq 0.766$). One of the four headline numbers in Table II is a typo or chain-pull mistake. Identify which one, recompute, and re-derive all marginal-tail σ's that depend on it.

---

## P1B-META-E2 (ESSENTIAL) — 100% of the "spectator-ALP" MCMC samples lie outside the spectator regime

**Section/page:** Sec. VI, Appendix C, fn. 5 and fn. 6, pp. 7, 9–10.
**Why missed:** All five reviewers accepted the framing of footnote 5 (that θ_i ~ 0.1 is required for spectator-consistency) without checking the actual MCMC prior range.

**Specific problem:** Appendix C states the ALP-MCMC prior is $\theta_i \in [0.5, 2]$, uniform. Footnote 5 and the abstract state the spectator regime requires $\theta_i \sim 0.1$, with the dark-energy regime starting at $\theta_i \sim 1$. **Every single one of the 9,720 accepted MCMC samples therefore corresponds to a dark-energy ALP, not a spectator ALP.** The result $\beta_{\rm ALP} = 0.336^\circ \pm 0.107^\circ$ quoted in Sec. VI is a posterior of a DE-ALP, mislabeled as a spectator-ALP result.

**Required fix:** Either (a) re-run the chain with the spectator-consistent prior $\theta_i \in [0.05, 0.3]$ and report what β results from a sample that is *actually* spectator-consistent, or (b) re-label the section as a "dark-energy-ALP consistency check" and explicitly retract the "spectator ALP" framing. The current framing is internally falsified by its own prior choice.

---

## P1B-META-E3 (ESSENTIAL) — The preferred w₀wₐ "quintom" model makes the H₀ tension *worse*, not better, and this is silently omitted

**Section/page:** Sec. III (Table II) vs Sec. II motivation, pp. 2, 4.
**Why missed:** All five reviewers focused on whether the H₀ tension persists under ΛCDM+ΔN_eff; none computed it under the w₀wₐ model the paper actually prefers.

**Specific problem:** Table II reports $H_0 = 67.185 \pm 0.455$ km/s/Mpc under the w₀wₐ extension (no SH0ES). Against Riess $H_0 = 73.04 \pm 1.04$:
$$\sigma_{\rm tension} = \frac{73.04 - 67.185}{\sqrt{1.04^2 + 0.455^2}} = \frac{5.855}{1.135} = 5.16\sigma.$$
The "canonical quintom signature" the paper highlights (Sec. III, "Physics interpretation") thus drives a **larger** H₀ tension than the 3.6σ Hubble tension it cites as motivation. This is *never mentioned*. Sec. III ends by claiming quintom is consistent with bounce/pre-Big-Bang scenarios, while the same chain is silently inconsistent with SH0ES at >5σ.

**Required fix:** Add the H₀-tension calculation for the w₀wₐ-extended posterior to Table II, alongside the ΛCDM+ΔN_eff calculation in Sec. II. Discuss explicitly that the quintom direction the data prefer does not address — and arguably exacerbates — the Hubble tension that motivated the ECH program.

---

## P1B-META-M1 (MAJOR) — Cobaya version is internally inconsistent between abstract and Sec. V

**Section/page:** Abstract, Sec. V.A, pp. 1, 6.
**Why missed:** All five reviewers cited "Cobaya v3.6.1" as the engine. None compared the abstract claim to Sec. V.

**Specific problem:** The abstract states "Cobaya v3.6.1." Sec. V.A states: "Cobaya [20] (v3.5 original; v3.6.1 verification)." Were the headline ΔN_eff posteriors computed in v3.5 and then re-verified in v3.6.1? Were both versions used and the means combined? Or was only v3.6.1 used and v3.5 is legacy? The abstract is misleading either way.

**Required fix:** State unambiguously which engine version produced the published 309,189 frozen samples. If results from two versions are merged, document the version split and demonstrate they are statistically compatible.

---

## P1B-META-M2 (MAJOR) — The actual spin-torsion signature, (ω/H)₀, is fixed to zero — the MCMC tests nothing about torsion

**Section/page:** Sec. II, Sec. V.A, pp. 2, 6.
**Why missed:** Grok argued the paper does not test the torsion module; the other reviewers accepted ΔN_eff as a "proxy." None of them noted that the parameter Paper I(a) identifies as the *distinctive* bounce-class diagnostic, $(\omega/H)_0$, is held fixed at zero — which means the MCMC has no degree of freedom that could even in principle distinguish bounce from non-bounce dynamics.

**Specific problem:** Sec. II: "$(\omega/H)_0$ (angular momentum transfer) and $\Omega_k$ are fixed to zero in the actual sampled MCMC configuration." Then Sec. V.A repeats this. Yet the entire Paper I(a) framing relies on $(\omega/H)_0$ as the bounce-class indicator. The ΔN_eff proxy is at best orthogonal to the bounce mechanism; the paper itself acknowledges this in §III.a, noting that the Hehl–Datta–Mercuri four-fermion contact term "does not produce a ΔN_eff at recombination." So the "verification" sampled a parameter that the ECH framework does not actually predict to be nonzero, while fixing the parameter that *is* the distinctive signature. The exercise is therefore tautological: ΔN_eff = 0 is consistent with ECH because ECH predicts ΔN_eff = 0 by construction.

**Required fix:** Either (a) run a real $(\omega/H)_0$-extended MCMC in modified CAMB (which the paper says it deliberately does *not* do), or (b) drop the "verification" framing entirely. Document the fact that the present MCMC tests no distinguishing prediction of the ECH framework.

---

## P1B-META-M3 (MAJOR) — Likelihood mixing: PR3 low-ℓ with NPIPE high-ℓ is non-standard and not justified

**Section/page:** Table II caption, Sec. III, pp. 3, 4.
**Why missed:** All five reviewers treated "Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing" as a standard stack. It is not. The low-ℓ likelihoods listed (`planck_2018_lowl.EE`, `planck_2018_lowl.TT`) are PR3 products, while CamSpec TTTEEE is NPIPE/PR4.

**Specific problem:** Mixing PR3 lowl (Commander/SimAll) with NPIPE CamSpec highl is not the Planck Collaboration's recommended pipeline; the consistent NPIPE configuration uses either SROLL2 lowl or CamSpec internal lowl, not PR3 Commander+SimAll. The τ posterior (0.054 ± 0.007) depends specifically on which lowl likelihood is used. The paper provides no justification for this mixed stack.

**Required fix:** Either justify the PR3-lowl + NPIPE-highl combination with reference to a published pipeline comparison, or re-run with a consistent stack (full PR3 or full NPIPE) and verify the headline ΔN_eff and H₀ are unchanged.

---

## P1B-META-M4 (MAJOR) — Joint (w₀, wₐ) significance is never computed; marginal-σ quotes are misleading

**Section/page:** Sec. III "Physics interpretation," Table II, pp. 3, 4.
**Why missed:** Gemini and Perplexity noted the absence of Bayes-factor model comparison. None noted that even the most basic joint-frequentist significance — the χ² of (w₀,wₐ) = (−1, 0) under the chain covariance — is also missing.

**Specific problem:** The paper headlines "+4.3σ in w₀" and "−3.6σ in wₐ" as separate marginal-tail departures. The joint significance depends on the off-diagonal correlation. Per META-E1, the chain's correlation coefficient on the (w₀,wₐ) plane is unknown (and inconsistent with the quoted pivot). Without it, the reader cannot infer whether the joint departure is 3σ, 5σ, or unphysical. The single most-cited quantitative result of the paper — that ΛCDM is "disfavored at joint level" — is unsupported.

**Required fix:** Report the full 2×2 covariance for (w₀, wₐ), then compute the joint χ² statistic at the ΛCDM point and translate to a Δχ² → σ. Without this, every statement of the form "phantom-crossing required" in the conclusion is rhetorically asserted, not derived.

---

## P1B-META-m1 (MINOR) — The NaMaster "bias 0.032°" is a 2–3σ detection of a real pipeline calibration offset, not a noise fluctuation

**Section/page:** Sec. IV, Fig. 3 and surrounding text, p. 6.
**Why missed:** All reviewers accepted "0.04° systematic floor" as benign. Nobody computed the standard error on the bias itself.

**Specific problem:** From the SNR ratio in footnote 3, per-realization σ_β̂ ≈ β̂/SNR_real = 0.238°/0.91 ≈ 0.26°. With N = 500 realizations, the standard error of the *mean* bias is $\sigma_{\rm bias} = 0.26^\circ/\sqrt{500} = 0.012^\circ$. The measured bias of 0.032° is therefore a $\approx 2.7\sigma$ detection of a non-zero pipeline calibration offset. This is not a "noise floor" but a real systematic — and the absolute value (0.032° at β=0.27°, 0.040° at β=0.342°) is comparable to the published Planck NPIPE 1σ statistical uncertainty of ±0.11°. A systematic of this size feeding into a sky measurement would shift the inferred β by ~30% of its statistical uncertainty.

**Required fix:** Either re-tune the apodization scale to bring the bias below the SE detection threshold (~0.012°), or quote 0.04° as a confirmed calibration offset that should be subtracted from any downstream β recovery, with appropriate propagated uncertainty.

---

## P1B-META-m2 (MINOR) — ALP-MCMC dataset attribution does not match the "headline" comparison target

**Section/page:** Abstract footnote a, Sec. VI, Appendix C, pp. 1, 7, 9.
**Why missed:** All reviewers noted the PR3-vs-PR4 disambiguation footnote but treated the ALP-MCMC comparison as internally consistent. It is not.

**Specific problem:** The paper compares $\beta_{\rm ALP}^{\rm MCMC} = 0.336^\circ \pm 0.107^\circ$ to the "published joint WMAP+Planck value $\beta = 0.342^\circ \pm 0.094^\circ$" — but the latter (per the abstract footnote) is the **PR3 + WMAP9** analysis, while the ALP-MCMC uses **Planck PR4 + ACT DR6** likelihoods. The two β's are not measurements of the same data combination. The "1σ agreement" claimed in Sec. VI compares posteriors anchored to different sky datasets.

**Required fix:** Either re-anchor the ALP-MCMC to PR3+WMAP9 likelihoods to match the headline comparison number, or re-quote the comparison target as the PR4-derived value (≈0.34° from Eskilt+ PR4-only analysis, differs slightly from PR3+WMAP9 joint).

---

## P1B-META-m3 (MINOR) — Eq. (3) and the fiducial β = 0.27° disagree on Δφ/fₐ

**Section/page:** Sec. VI, Eqs. (2)–(3), p. 7.
**Why missed:** Reviewers accepted the equation but did not cross-check Eq. (2) against Eq. (3) and the fiducial.

**Specific problem:** Eq. (2) gives Δφ/fₐ ≈ 0.65 for (m=H₀, θᵢ=1). Eq. (3) uses Δφ/fₐ = 1.07 (the "× 1.07" factor) for (Caγ=8, θᵢ=1, m≈2H₀), yielding 0.29°. The text then says "the fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H₀, Δφ/fₐ ≈ 1.0." But the same Eq. (3) at Δφ/fₐ = 1.0 gives β = α_EM × 8/(4π) = 0.266°, while at Δφ/fₐ = 1.07 (Eq. 3) it gives 0.285°. There is no internal model that simultaneously gives Δφ/fₐ = 0.65 at m=H₀ (Eq. 2) and Δφ/fₐ = 1.0 at m=1.8H₀ — for the underdamped ALP ODE, Δφ/fₐ should *decrease* with increasing m/H₀ (faster oscillation = more cancellation), not increase from 0.65 to 1.07.

**Required fix:** Provide the actual Δφ/fₐ(m/H₀, θᵢ) numerical table (or trajectory plot) and verify the monotonicity. The current numerical statements are inconsistent with the standard underdamped ALP equation of motion.

---

## P1B-META-N1 (NIT) — Sample-count quartet in Figs/tables/footnotes is irreconcilable

**Section/page:** Table I, Fig. 1, Fig. 2, fn. 1, pp. 3, 5.
**Why missed:** Gemini caught one inconsistency between Fig. 2 (175,545) and Table I (176,240). The full discrepancy set is larger and not all flagged.

**Specific problem:** For the "full-tension" chain alone, the paper quotes: 176,240 (Table I, raw); 175,545 (Fig. 2 caption); 119,617 (Fig. 1 caption, "getdist-thinned"); 123,129 (fn. 1, "post-burnin count"); 123,368 (fn. 1, "exact computation"). Five different sample counts for the same chain. Footnote 1's reconciliation explains 123,129 vs. 123,368 (~1% truncation), but does not explain Fig. 1's 119,617 or Fig. 2's 175,545.

**Required fix:** Provide a single canonical count plus a reproducible recipe (raw → burn-in cut → getdist effective-weight thinning) and apply consistently across all tables and figure captions.

---

## Meta-review recommendation

**REJECT** (consonant with Grok; stronger than Gemini/Perplexity's "Major Revisions").

Across the union of all six reviews, the blocker count is substantial. The genuinely fatal items are: (a) **META-E1** — Table II contains a mathematically impossible covariance specification, undermining the headline w₀wₐ result; (b) **META-E2** — the ALP-MCMC samples are 100% outside the spectator regime the section purports to validate; (c) **META-E3** — the preferred "quintom" model exacerbates the very tension the paper cites as motivation, a fact the paper conceals; (d) **META-M2** — the actual spin-torsion signature $(\omega/H)_0$ is set to zero, making the entire "verification" tautological; (e) **Perplexity-E1** — multiple load-bearing references are future-dated arXiv IDs; (f) **Gemini-E1/META-E1** — the central error-propagation arithmetic in the headline table is internally contradictory; (g) **Grok-E2** — the title-scope mismatch ("Spin-Torsion Program" vs. "carries no torsion modifications") is acknowledged by the authors themselves three times. The paper would not survive non-bigbounce peer review: a competent external referee, even without finding META-E1/E2/E3, would reject on the basis of the future-dated citations alone (Perplexity-E1) — these would fail the editorial-screen stage at PRD before ever reaching peer review. My confidence that the manuscript as submitted would be desk-rejected by PRD's editorial office is ≥ 90%; conditional on reaching peer review, my confidence in acceptance even after revision is ≤ 10%, because the underlying structural problem (the paper claims to verify a theory whose distinguishing parameters it does not sample) is not fixable by text edits.