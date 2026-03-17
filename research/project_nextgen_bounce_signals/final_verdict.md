# Final Verdict: Next-Generation Bounce Signal Theory

**Created:** 2026-03-17
**Status:** COMPLETE

---

## 1. What is the best next-generation bounce-signal theory?

**Chiral gravitational waves from a parity-violating torsion bounce.**

The ECH framework contains a natural parity-odd gravitational structure (the Holst term) and a natural pseudoscalar (the Barbero-Immirzi field). When the pseudoscalar is dynamical, its coupling to curvature (Chern-Simons) or torsion (Nieh-Yan) produces differential amplification of left- and right-handed tensor modes. The bounce is the unique moment when this coupling is maximized (Planckian curvature, maximal torsion), producing a chirally asymmetric gravitational wave background.

---

## 2. Why is it the best remaining chance at a genuinely positive result?

Four reasons:

1. **It targets a qualitatively new observable.** Circular polarization of the SGWB is a distinct measurement channel — not a refinement of n_s or a correction to r. A nonzero Δ_h is unambiguous evidence for parity violation in gravity.

2. **The bounce is the active ingredient.** Unlike the transparent bounce (where the spectrum is set by the contraction phase), the chiral signal is generated AT the bounce. The bounce does something that nothing else in the cosmological history does: it provides a moment of Planckian curvature with parity violation.

3. **The ingredients already exist in the ECH framework.** The Holst term is parity-odd. The Barbero-Immirzi pseudoscalar is the natural Chern-Simons coupling. No new fields or symmetries need to be introduced — just promoting γ to a dynamical field, which is a well-studied extension (Taveras & Yunes 2009).

4. **The literature gap is genuine.** Nobody has computed the chiral tensor spectrum from a torsion bounce. Zhu & Cai (2023) showed enhancement is possible. Jiang et al. (2024) used Nieh-Yan in inflation. Neither produces a quantitative Δ_h(f) from a bounce. This is a real first-mover opportunity.

---

## 3. Is it actually novel enough to pursue?

**Yes, with one major caveat.**

**Novel aspects:**
- First computation of circular polarization fraction from a torsion bounce
- First application of Nieh-Yan coupling to chirality generation at a cosmological bounce
- Coupling strength determined by γ = 0.274 (from black hole entropy) — not a free parameter
- Spectral shape of Δ_h(f) from transient parity violation (bounce) differs from quasi-constant parity violation (inflation)

**The caveat — frequency reach:**
If all bounce-scale physics is confined to Planckian frequencies (f ~ 10⁹ GHz), no detector can see it. The chirality must reach frequencies accessible to LISA (mHz), ET (Hz–kHz), or PTA (nHz). This requires either:
- Significant redshifting of the bounce scale (long radiation era or post-bounce inflationary phase)
- The chiral coupling to extend its influence beyond the immediate bounce scale through nonlinear effects
- A different ALP mass/coupling regime that spreads the chirality to lower k

**The frequency-reach question is the single most important quick-kill test.** It must be addressed in Step 1-2 of Phase 1, before any detailed numerical work.

---

## 4. Does the bounce project still have a realistic path to observable support?

**Conditional yes.**

The path is narrow but real:
- IF the chiral coupling sources σ̇ at the bounce (via Nieh-Yan or curvature coupling)
- AND the chirality extends to frequencies below GHz (via redshifting or nonlinear spread)
- AND the amplitude is O(10⁻²) or larger at those frequencies
- THEN the ECH bounce produces a testable prediction for next-generation GW detectors

If any of these conditions fail, the bounce project's observable support reduces to:
- Cosmic birefringence from the ALP (independent of the bounce)
- The structural lesson that minimal ECH resolves the singularity but is observationally silent

The honest assessment: the probability of all conditions being met is perhaps 15–25%. But this is the best shot available, and the quick-kill structure (Step 1 of Phase 1) will determine viability within one session.

---

## 5. Exact recommended immediate next move

### Session N+1: Frequency Reach Gate

Before any detailed computation, answer ONE question:

> **At what frequency does the chiral signal from the ECH bounce appear today?**

This requires:
1. Compute the bounce scale k_b from ρ_c = 0.21 M_Pl⁴
2. Estimate the total expansion factor from bounce to today
3. Map k_b → f_b (frequency today)
4. Determine whether f_b can reach LISA/ET/PTA bands under any reasonable expansion history

**If f_b > 10⁶ Hz for all reasonable expansion histories:** DEAD. Close the program.

**If f_b can reach mHz–kHz:** ALIVE. Proceed to Step 1 (coupling selection) of Phase 1.

**If f_b depends critically on an unknown expansion history:** MARGINAL. Document the assumption needed and decide whether it is motivated.

This is a 1-hour analytic calculation. It should be done before anything else.

### Directory for Phase 1

```
research/project_chiral_bounce_GW/
```

### First file to create

```
research/project_chiral_bounce_GW/00_frequency_reach_gate.md
```

---

## Bottom Line

> The minimal ECH bounce is observationally silent — it resolves the singularity but leaves no perturbation-level fingerprint. The one remaining path to an observable bounce signal is through the parity-odd sector: the Holst term + dynamical Barbero-Immirzi field can source chiral gravitational waves at the bounce. This is the only candidate that uses existing ECH ingredients, targets a qualitatively new observable, and has a genuine literature gap. It lives or dies on one question: can the chiral signal reach detectable frequencies? Answer that first.
