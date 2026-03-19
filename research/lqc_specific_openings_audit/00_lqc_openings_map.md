# LQC Openings Map: What Is Settled vs Still Open

**Created:** 2026-03-18
**Status:** ACTIVE
**Mode:** LQC-SPECIFIC OPENINGS (ECH loops closed, no model cataloguing)

---

## DEEPLY_COVERED (settled in our program)

### 1. Generic matter-bounce f_NL = -35/8 benchmark
- Convention resolved: |B|_NL^sq (Cai et al.) = f_NL^Planck. No hidden conversion factor.
- Li-Brandenberger discrepancy diagnosed as systematic factor-of-2 (convention, not physics).
- Quintin value identified as citation artifact, not independent calculation.
- Template projection bounded: cos(theta) ~ 0.95 +/- 0.03.
- **Confidence: 75%.** Remaining 25% risk is the unverified in-in time integral coefficient.

### 2. Wilson-Ewing quasi-dust + LQC viability
- Model B is the sole survivor of the two-pass viability filter (Models A, C eliminated).
- 0 extra fields, 1 fitted parameter (epsilon = 0.003), 1 parameter-free prediction (f_NL).
- n_s = 0.964 from w = -0.003 (Lambda contribution). r ~ 10^-4 from LQC dressed-metric.
- BKL resolution requires ~10 e-folds of ekpyrotic pre-phase (postulated, not derived).
- **Status: ONLY SURVIVING VIABLE MODEL.**

### 3. ECH perturbation transparency
- 14 barriers documented across the full closure argument.
- ECH provides no perturbation-level predictions: perturbations propagate on standard GR background.
- ECH enters only as background cross-check and contrast framework.
- **Status: STRUCTURALLY CLOSED. Do not reopen.**

### 4. Curvaton tilt crisis
- Curvaton in matter contraction produces blue tilt (growing mode dominates).
- Cannot fix n_s -- kills Model A (LQC + Curvaton).
- Standard delta-N fails because zeta grows on superhorizon scales in contraction.
- **Status: MODEL A DEAD.**

### 5. Survey discrimination hierarchy
- SPHEREx: sigma(f_NL) ~ 2.0 -> 2.2 sigma detection of f_NL = -4.375 (marginal).
- MegaMapper: sigma(f_NL) ~ 0.5 -> 8.75 sigma detection (decisive).
- Timeline: SPHEREx data ~2028-2030; MegaMapper ~2032-2035.
- **Status: MAPPED. MegaMapper is the decisive experiment.**

---

## PARTIALLY_COVERED

### 6. LQC perturbation formalisms
We USE dressed-metric results (r ~ 10^-4) but have not audited whether the hybrid formalism gives the same f_NL. The 2024 comparison paper (arXiv:2405.12296) by Agullo, Ashtekar, and Gupt compares perturbation approaches and finds agreement in UV but differences in IR. Nobody has compared them for the bispectrum.

**Gap:** Formalism dependence of f_NL is completely untested. This is the single highest-priority LQC-specific question.

**See:** `01_quantization_ambiguity_formalism_audit.md` for full analysis.

### 7. Matter-ekpyrotic bounce
Mentioned for BKL resolution but not systematically assessed. Haro et al. (arXiv:1703.03710) studied matter-ekpyrotic LQC and found spectrum nearly scale-invariant but n_s inconsistent. A 2025 paper (arXiv:2509.06148) claims two-field quasi-dust ekpyrotic works. Neither paper computes f_NL.

**Gap:** Whether two-field ekpyrotic dynamics preserve, modify, or destroy the f_NL = -35/8 prediction is unknown.

**See:** `02_quasidust_ekpyrotic_lqc_audit.md` for full analysis.

---

## OPEN_AND_HIGH_VALUE

### 8. Dressed-metric vs hybrid for f_NL
**NOBODY** has computed f_NL in both formalisms. This is a genuine gap in the LQC literature.

The two formalisms agree for the power spectrum at observable scales (k << k_LQC). For the bispectrum, the situation is:
- Pre-bounce f_NL is formalism-independent (classical contraction, no quantum corrections).
- Bounce transfer of the bispectrum has not been computed in EITHER formalism at third order.
- If the transfer differs between formalisms, that IS testable quantum-gravity content.
- If the transfer agrees, it raises prediction confidence to ~90%+.

**Estimated probability of a meaningful difference: 10-15%.** But this is where genuine LQC-specific content lives.

**Priority: #1.**

### 9. PBH + induced GW channel
Papanikolaou et al. (arXiv:2404.03779) propose enhancement of scalar perturbations during the bounce-to-expansion transition, producing asteroid-mass PBHs (10^17 - 10^22 g) and an induced stochastic GW background.

Not tested for the Wilson-Ewing model. The key question: is the LQC bounce sharp enough to produce significant enhancement?

This channel is genuinely independent of f_NL:
- Different k-range (k ~ 10^5 - 10^15 Mpc^-1 vs k ~ 0.01 Mpc^-1)
- Different observable (DM fraction + GW spectrum vs bispectrum)
- Different experiments (PTA/LISA/ET vs LSS surveys)

**Estimated viability: 30-50%.** Quick OOM estimate can determine if the channel is alive or dead.

**Priority: #2 (after formalism audit). See `03_second_observable_channel_audit.md`.**

### 10. Third-order perturbation transfer through LQC bounce
Pre-bounce f_NL = -35/8 has never been verified to survive the bounce at bispectrum level. The assumption is that superhorizon modes (k/k_bounce ~ 10^-56) pass through without modification. This is physically reasonable but formally unproven.

Two routes:
- Route A (separate-universe): Quick, expected to confirm faithful transfer.
- Route B (full third-order LQC): Definitive but months of work.

**Priority: #3 (after formalism audit and PBH check).**

---

## LOW_PRIORITY

### 11. Deformed algebra approach (Bojowald, Paily)
Known compatibility issues with general covariance. Not mainstream LQC phenomenology. Technical controversies in the community make results from this approach unreliable for phenomenological predictions.

**Verdict: DEPRIORITIZE. Do not invest time unless dressed-metric vs hybrid comparison produces an unexpected result that motivates checking a third formalism.**

### 12. Separate universe approach
Valid only for superhorizon modes (k << aH). Our modes ARE deeply superhorizon (k/k_bounce ~ 10^-56), so for the power spectrum all approaches agree. For the bispectrum, the separate universe approach may miss mode-coupling effects at the bounce.

**Verdict: USE AS CROSS-CHECK for Route A of Opening 10. Not a standalone calculation.**

### 13. CMB anomaly / low-ell modulation
Evidence is 2-3 sigma anomalies in Planck data (quadrupole suppression, hemispherical asymmetry, cold spot). LQC initial-state effects could modify largest-scale modes (Agullo et al. 2013, 2021). But:
- No quantitative prediction from our specific model (Wilson-Ewing quasi-dust).
- Attribution is ambiguous (cosmic variance, a posteriori statistics).
- Even a positive signal would not uniquely fingerprint LQC.

**Verdict: LOW PRIORITY. Only revisit if the formalism audit (Opening 8) reveals a specific low-ell signature in dressed-metric that hybrid lacks.**

### 14. GFT condensate cosmology
Group Field Theory condensate approach to cosmology (Gielen, Oriti, Sindoni). Derives LQC-like effective equations from full spinfoam/GFT framework. Potentially foundational but:
- Too far from observation for near-term predictions.
- No f_NL calculation exists.
- Multi-year program with qualitative payoff only.

**Verdict: DEPRIORITIZE entirely. Not on our timeline.**

---

## Decision Architecture

```
START
  |
  v
[Opening 8: Formalism audit]
  |
  |---> Formalisms AGREE for f_NL
  |       |
  |       v
  |     Confidence rises to ~90%
  |     Proceed to Opening 10 (third-order transfer)
  |       |
  |       |---> Transfer faithful --> f_NL = -35/8 confirmed
  |       |---> Transfer non-trivial --> MAJOR FINDING
  |
  |---> Formalisms DISAGREE for f_NL
  |       |
  |       v
  |     MAJOR FINDING: formalism-dependent LQC observable
  |     Quantify the difference
  |     Write up as primary LQC-specific result
  |
  v
[Opening 9: PBH + GW channel]
  |
  |---> Enhancement sufficient --> SECOND OBSERVABLE FAMILY
  |---> Enhancement negligible --> Single-observable architecture confirmed
  |
  v
[Opening 7: Ekpyrotic two-field] (only if above paths exhaust)
```

---

## Bottom Line

The program has three genuine LQC-specific openings worth pursuing (8, 9, 10), one partially-covered question worth checking (7), and several low-priority items to deprioritize. The path forward is linear: formalism audit first, then third-order transfer, then PBH channel, then (conditionally) ekpyrotic two-field. Everything else is noise.
