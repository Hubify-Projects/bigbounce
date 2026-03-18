# 02: Literature Evidence Audit

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Methodology

For each claim from the registry, I assess:
1. What exact model class supports it?
2. Is the evidence robust, suggestive, speculative?
3. Is it a fit to real data, an existence proof, or a toy scenario?
4. Does it depend on extra assumptions beyond "a bounce"?
5. Is it contested or challenged?

Rating scale:
- **STRONG_EVIDENCE:** Real data clearly favors the bounce explanation; robust across reasonable model variations
- **MODERATE_EVIDENCE:** Real data is compatible; bounce provides a plausible explanation but alternatives exist
- **WEAK_EVIDENCE:** Theoretical argument exists but no distinctive data support; or data is marginal
- **SPECULATIVE:** No data contact; theoretical possibility only
- **NOT_RELEVANT_TO_OUR_FRAMEWORK:** Cannot be connected to ECH/spin-torsion

---

## Claim 1: Low-ℓ CMB Power Deficit

**Model class:** LQC bounce + slow-roll inflation (bounce-inflation hybrid)

**Evidence assessment:**

The Agullo, Kranas & Sreenath (2021) paper shows that an LQC bounce preceding standard slow-roll inflation can suppress the primordial power spectrum at the largest scales (smallest k). The suppression arises from LQC quantum-geometry corrections to the perturbation equation during the Planckian bounce phase. Specifically, the dressed-metric approach gives a modified effective potential U(k,η) that acts as a high-pass filter — only modes with k above a critical wavenumber k_LQC receive the full inflationary amplification.

**Strengths:**
- Explains a known ~2–3σ anomaly in Planck data
- The suppression scale is set by LQC (not a free parameter)
- Same model simultaneously addresses claims 2 and 3

**Weaknesses:**
- Requires inflation AFTER the bounce — this is a bounce-inflation hybrid, not a pure bounce alternative
- The low-ℓ deficit itself is only 2–3σ, and could be cosmic variance or a statistical fluke
- Contaldi et al. (2003) showed that ANY finite-duration pre-inflationary phase (not just a bounce) produces similar suppression — the effect is not bounce-specific
- The initial conditions at the bounce (Gaussian vacuum state) are assumed, not derived

**Is it bounce-specific?** Partially. The suppression scale IS set by bounce dynamics, but the qualitative effect occurs in any model with a finite onset of inflation.

**Contested?** Yes. Durrer et al. (2023) computed the CMB bispectrum from LQC bounce models and found "no significant sign of a bispectrum imprint" in Planck data — widely reported as challenging LQC anomaly explanations. Raveendran & Sreenath (2024) rebutted this by arguing the LQC bispectrum is highly oscillatory and essentially indistinguishable from slow-roll — but this means LQC loses its most distinctive signature (the bispectrum becomes a non-test, not a confirmation). Additionally, the Agullo et al. fits are QUALITATIVE only — no formal chi-squared or Bayesian model comparison against Planck data is presented.

**Rating: WEAK_EVIDENCE** (downgraded from MODERATE after literature review: qualitative fits only, bispectrum challenged, cosmic variance alternative)

---

## Claim 2: CMB Parity Asymmetry

**Model class:** LQC bounce + inflation

**Evidence assessment:**

The parity anomaly refers to the observed excess of odd-multipole power over even-multipole power at ℓ < 30, at roughly 2.5–3σ significance. Agullo et al. (2021) show that the LQC bounce-inflation model naturally produces such an asymmetry because the bounce breaks time-reversal symmetry, imprinting a phase coherence between even and odd multipoles that is absent in pure inflation.

**Strengths:**
- Explained by the same model as claim 1 (no additional parameters)
- The parity asymmetry is one of the more robust CMB anomalies

**Weaknesses:**
- Requires the specific LQC dressed-metric perturbation corrections — not present in ECH (we showed ECH perturbations are classical equivalent)
- The anomaly significance is borderline (2.5–3σ)
- The effect depends sensitively on the number of pre-inflationary e-folds
- Alternative explanations exist (e.g., non-trivial topology, hemispherical asymmetry leakage)

**Is it bounce-specific?** Yes, more so than claim 1 — the parity-breaking requires a specific bounce dynamics, not just "finite onset of inflation."

**Contested?** Same Durrer et al. bispectrum challenge applies (the bispectrum was the mechanism for parity preference). Gaztanaga (2025) proposed an alternative "direct-sum inflation" explanation. The anomaly significance is borderline (2.5–3σ). The data comparison is qualitative, not a statistical fit.

**Rating: WEAK_EVIDENCE** (downgraded: qualitative only, bispectrum mechanism challenged, alternatives exist)

---

## Claim 3: Hemispherical Power Asymmetry

**Model class:** LQC bounce + inflation (via non-Gaussianity)

**Evidence assessment:**

The hemispherical power asymmetry (dipolar modulation A ~ 0.06 at ℓ < 64) is one of the more statistically significant CMB anomalies (~3σ). The LQC bounce model produces enhanced non-Gaussianity from the pre-inflationary dynamics, which can generate this asymmetry through a super-horizon modulating mode.

**Strengths:**
- Same model as claims 1 and 2 (impressive multi-anomaly explanation)
- The mechanism (non-Gaussianity + super-horizon mode) is physically clear

**Weaknesses:**
- The connection is qualitative rather than quantitative — the LQC non-Gaussianity amplitude needed to produce A = 0.06 is not uniquely predicted; it depends on initial conditions
- The mechanism requires a specific long-wavelength mode to be present
- Agullo & Morris (2015) showed the mechanism works in LQC but with free parameters
- Similar mechanisms exist in inflationary models (e.g., Erickcek et al. 2008)

**Is it bounce-specific?** Weakly — the same mechanism works with any source of enhanced non-Gaussianity.

**Contested?** The anomaly is established; the explanation via non-Gaussianity is standard; the specific LQC implementation has free parameters.

**Rating: WEAK_EVIDENCE**

---

## Claim 4: Lensing Anomaly (A_L > 1)

**No bounce mechanism identified in the literature.**

**Rating: NOT_RELEVANT_TO_OUR_FRAMEWORK**

---

## Claim 5: PTA / NANOGrav

**Model class:** Matter bounce (dust contraction → radiation expansion)

**Evidence assessment:**

Several papers (Papanikolaou 2025; Lai & Li 2025) have shown that the stochastic gravitational wave background predicted by the matter bounce is compatible with NANOGrav 15yr data and can be Bayesian-favored over conventional astrophysical sources (SMBH binaries).

**Strengths:**
- Real data fit with Bayesian comparison
- The matter bounce GW spectrum has a specific spectral shape (Ω_GW ∝ f^{n_T} with n_T ~ 2 for scale-invariant tensor spectrum) that matches the PTA frequency range
- The amplitude is in the right ballpark without extreme tuning

**Weaknesses:**
- The SMBH binary explanation is the default and is NOT ruled out — it remains the simplest explanation
- The Bayesian preference depends on priors and on what astrophysical models are included in the comparison
- Lai & Li (2025) find that PTA data implies a bounce energy scale **exceeding the Planck mass** (trans-Planckian), undermining EFT validity of the bounce model
- The pre-big-bang (string cosmology) variant is specifically ruled out: arXiv:2411.16505 finds Bayes factor ~468 AGAINST pre-big-bang vs power-law, with dilaton parameter outside allowed range at >5σ
- The matter bounce tensor spectrum has the Quintin et al. (2015) no-go problem: single-field matter bounce cannot have small r at CMB scales AND small f_NL simultaneously. If the tensor amplitude is large enough for PTA, f_NL may be too large for Planck
- Multiple other exotic sources (cosmic strings, phase transitions, domain walls) also fit the PTA signal
- The PTA signal has only recently been confirmed; spectral characterization is still evolving

**Is it bounce-specific?** The spectral shape is matter-bounce-specific, but many other sources produce comparable spectra.

**Contested?** Yes — the conventional SMBH explanation is not ruled out, and the Bayesian preference for exotic sources is sensitive to model assumptions.

**Rating: MODERATE_EVIDENCE** (but with significant caveats about non-uniqueness)

---

## Claim 6: PBH Dark Matter

**Model class:** Matter bounce (enhanced small-scale power from contraction dynamics)

**Evidence assessment:**

The matter bounce can generically amplify perturbations at small scales during the contraction-to-expansion transition. If the amplification is sufficient, PBHs form in the asteroid-mass window (~10¹⁸–10²² g), which is the least constrained mass range for PBH dark matter.

**Strengths:**
- Generic mechanism — doesn't require fine-tuned features in the potential
- The asteroid-mass window remains open (constraints from microlensing, evaporation, dynamical effects are not yet conclusive)
- Less fine-tuned than inflationary PBH production (which requires specific features in V(φ))

**Weaknesses:**
- No PBH detection exists — this is a theoretical window, not observed evidence
- The amplification factor depends on the detailed contraction dynamics and is NOT parameter-free
- **Critical 2026 result:** arXiv:2602.12057 shows that when radiation pressure is properly included in the two-fluid (dust-radiation) system, PBH mass fractions are **vanishingly small** across all benchmark masses. The critical threshold is tiny but the power spectrum amplitude falls orders of magnitude short. Substantial PBH formation requires additional amplification mechanisms beyond the generic bounce.
- The BKL instability problem: if the contraction becomes anisotropic, the perturbation analysis breaks down
- The PBH abundance is exponentially sensitive to the perturbation amplitude at the PBH formation scale — small changes in the model produce huge changes in f_PBH
- Competing inflationary PBH models exist with comparable or better motivated amplification mechanisms
- The asteroid-mass window may close with future microlensing surveys (Roman, Euclid)

**Is it bounce-specific?** The generic production mechanism is bounce-specific, but the quantitative prediction is highly model-dependent.

**Contested?** The mechanism is not contested, but no detection makes this entirely theoretical.

**Rating: WEAK_EVIDENCE** (theoretical plausibility only, no data support)

---

## Claim 7: S₈ Tension Reduction

**Model class:** Bounce-inflation hybrid (bounce modifies early spectrum, inflation provides main amplification)

**Evidence assessment:**

Li et al. (2024) showed that a bounce-inflation model can modify the primordial power spectrum at intermediate scales, reducing the predicted σ₈ and easing the S₈ tension.

**Strengths:**
- Real data contact — addresses a genuine 2–3σ tension
- Provides a physical mechanism (modified transfer function at bounce)

**Weaknesses:**
- Requires BOTH a bounce AND inflation — not a pure bounce model
- The model has additional free parameters beyond standard ΛCDM + inflation
- The S₈ tension may be resolved by astrophysical systematics (baryonic feedback, intrinsic alignments)
- Other BSM solutions exist (interacting dark energy, neutrino masses, modified gravity) that don't require a bounce
- One paper, not yet independently confirmed

**Is it bounce-specific?** Requires a bounce, but also requires inflation. The bounce is one ingredient, not the full explanation.

**Contested?** The S₈ tension itself is debated; the bounce-inflation solution is too new to be widely evaluated.

**Rating: WEAK_EVIDENCE**

---

## Claim 8: Blue Tensor Tilt

**Model class:** Matter bounce

**Evidence assessment:**

The matter bounce generically predicts a blue tensor tilt (n_T > 0), in contrast to inflation's n_T < 0. This would be a smoking-gun discriminator. However:

**Strengths:**
- Qualitative prediction (sign of n_T) is robust and model-independent for matter bounce
- Directly testable if tensor modes are detected

**Weaknesses:**
- The Quintin et al. (2015) no-go: in single-field matter bounce, r and f_NL are correlated. Large r (needed for detection) implies large |f_NL|, which is constrained by Planck
- Wilson-Ewing (2013): LQC suppresses r to ~10⁻⁴, which is below current sensitivity
- If r is undetectably small, the sign of n_T is unmeasurable
- No current or near-future experiment can measure n_T at the precision needed

**Is it bounce-specific?** Yes — the sign of n_T is a genuine bounce discriminator.

**Contested?** The prediction is not contested, but its testability is severely limited.

**Rating: SPECULATIVE** (correct prediction but untestable in the foreseeable future)

---

## Claim 9: r Predictions

**Model class:** LQC/ECH

**Evidence assessment:**

Wilson-Ewing (2013) gives r ~ 10⁻⁴ in LQC. Our ECH classical calculation gives r ~ 10⁻⁵⁵. Neither is testable.

**Rating: SPECULATIVE** (untestable)

---

## Claim 10: f_NL = −35/8

**Model class:** Matter bounce (dust contraction)

**Evidence assessment:**

Cai et al. (2009) showed that the matter bounce produces f_NL^local = −35/8 ≈ −4.375. This is a parameter-free prediction.

**Strengths:**
- Parameter-free — the value is fixed by the contraction dynamics
- The sign is opposite to slow-roll inflation (which gives f_NL ≈ 0 to +O(n_s − 1))
- Compatible with current Planck bounds (f_NL = −0.9 ± 5.1)
- Future surveys: CMB-S4 improves by ~2× over Planck. LSS scale-dependent bias (SPHEREx, DESI) may reach σ(f_NL) ~ 1–2. MegaMapper/SPHEREx multi-tracer could reach σ(f_NL) ~ 0.5, making f_NL = −4.375 an **8σ detection**. This is the most promising near-term test of the matter bounce.

**Weaknesses:**
- Currently only ~0.7σ away from zero — not yet distinguishable from inflation
- The prediction assumes single-field matter contraction — multi-field models or different contraction EOS would change f_NL
- Distinguishing f_NL = −4.4 from f_NL = 0 requires σ(f_NL) ~ 1, which is optimistic for near-term experiments
- The Quintin et al. no-go means single-field matter bounce with this f_NL AND small r may be inconsistent

**Is it bounce-specific?** Yes — the value and sign are specific to matter-dominated contraction.

**Contested?** The calculation is not contested, but the no-go context (Quintin) complicates the full picture.

**Rating: MODERATE_EVIDENCE** (parameter-free, potentially testable in ~10 years)

---

## Claim 11: Galaxy Chirality

**Model class:** No clear bounce mechanism

**Evidence assessment:**

Hou et al. (2023) reported a 7σ parity-odd 4-point signal in BOSS galaxy data. However, **Krolewski et al. (2024), JCAP 08, 044** provided a definitive reanalysis:
- The chi-squared statistic was biased by the parity-even 8-point correlation function (8PCF) differing between real data and mocks
- The 8PCF bias accounts for ~6σ of the original signal
- After correcting: the parity-violation signal drops to **0–2.5σ** depending on analysis choices
- Conclusion: "no compelling evidence for parity violation in BOSS"
- No bounce model has been shown to produce this specific signature

**Rating: NOT_RELEVANT_TO_OUR_FRAMEWORK** (no mechanism, contested data)

---

## Claim 12: Cosmic Birefringence

**Model class:** ALP cosmology (bounce-independent)

**Evidence assessment:**

Combined Planck + ACT data gives β = 0.342° ± 0.094° (3.6σ). Our model predicts β = 0.27–0.35°.

**Strengths:**
- Strongest data contact of any claim — 3.6σ detection
- Our prediction matches within 1σ
- Multiple independent datasets are consistent

**Weaknesses:**
- The prediction is ENTIRELY independent of the bounce
- The ALP mass and coupling are free parameters in our model
- **Miscalibration degeneracy unresolved:** Planck cannot separate instrumental polarization angle miscalibration (α) from true cosmic birefringence (β). The combined α+β is measured at ~7σ (with SPIDER), but β alone remains 2.4–3.6σ depending on analysis. Planck PR4 map-space analysis (Feb 2025): β = 0.46° ± 0.04° (stat) ± 0.28° (syst) — "consistent with no parity violation" when systematics dominate.
- ACT DR6 gives independent β = 0.215° ± 0.074° (2.9σ), but acknowledges "systematics not understood"
- Other ALP models unconnected to ECH/bounce also predict birefringence

**Is it bounce-specific?** **NO.** The birefringence depends on the ALP mass (~10⁻³³ eV) and coupling, not on whether there was a bounce. It works identically in ΛCDM + inflation.

**Contested?** The detection significance is growing but systematic concerns remain.

**Rating: STRONG_EVIDENCE** for the ALP model, but **NOT_RELEVANT** to bounce cosmology specifically

---

## Claim 13: Hubble Tension

No competitive bounce solution exists.

**Rating: NOT_RELEVANT_TO_OUR_FRAMEWORK**

---

## Claim 14: Baryogenesis

**Model class:** ECH/torsion-compatible

**Evidence assessment:**

Alexander, Calcagni & Peskin (2015) proposed that torsion-fermion coupling at the bounce could generate baryon asymmetry. The mechanism requires strong torsion (present at the ECH bounce) and parity violation (from the Holst term).

**Strengths:**
- Uses existing ECH ingredients
- The bounce provides the unique high-energy environment needed

**Weaknesses:**
- Purely theoretical — no quantitative prediction of η_b = n_b/n_γ ~ 6 × 10⁻¹⁰
- The calculation requires knowing the fermion content and coupling at Planckian energies
- Multiple baryogenesis mechanisms exist; torsion baryogenesis is one of many
- No observational test beyond the existence of baryons

**Rating: SPECULATIVE**

---

## Claim 15: BKL Resolution

**Model class:** Slow contraction (Ijjas & Steinhardt) or LQC

**Evidence assessment:**

Not an observational claim — this is an internal consistency requirement. Slow contraction resolves BKL (proven); dust contraction does NOT (anisotropies grow as a⁻⁶ vs ρ_dust as a⁻³).

**Rating: NOT observational — internal consistency question**

---

## Claim 16: GW Echoes from Bounce

**Model class:** Bounce-generic

**Evidence assessment:**

Zhu & Cai (2026) proposed that the bounce leaves periodic modulations (echoes) in the primordial GW spectrum. If the bounce lasts for a finite conformal time Δη, modes with k ~ nπ/Δη experience resonant amplification, creating a comb-like pattern.

**Strengths:**
- Qualitatively distinctive — no other mechanism produces this specific pattern
- Model-independent for any bounce with finite duration

**Weaknesses:**
- Very new paper — not yet peer-reviewed or independently verified
- The echo frequency depends on the bounce scale, which for ECH gives f ~ GHz (from our frequency gate analysis) — inaccessible to all detectors
- Signal amplitude not yet robustly estimated
- Same frequency-amplitude trade-off as chiral GW: Planck-scale bounce → GHz signals

**Rating: SPECULATIVE** (interesting but likely killed by frequency reach for ECH)

---

## Evidence Summary

| Rating | Claims |
|--------|--------|
| STRONG_EVIDENCE | None (birefringence is strong but bounce-independent and miscalibration-degenerate) |
| MODERATE_EVIDENCE | Birefringence (#12, but bounce-independent), PTA/NANOGrav (#5), f_NL (#10) |
| WEAK_EVIDENCE | Low-ℓ deficit (#1), Parity asymmetry (#2), Hemispherical asymmetry (#3), PBH (#6), S₈ (#7) |
| SPECULATIVE | Blue n_T (#8), r predictions (#9), Baryogenesis (#14), GW echoes (#16) |
| NOT_RELEVANT | Lensing (#4), Galaxy chirality (#11, debunked), Hubble tension (#13) |

**Critical observations:**
1. No claim reaches STRONG_EVIDENCE.
2. The best data contact (birefringence) is bounce-independent and has unresolved miscalibration systematics.
3. The CMB anomaly claims (#1-3), which appeared strongest in our initial survey, are downgraded to WEAK after discovering (a) Durrer et al. bispectrum challenge, (b) qualitative-only fits, (c) the mechanism requires LQC + inflation, not ECH.
4. All bounce-dependent claims are MODERATE or below.
