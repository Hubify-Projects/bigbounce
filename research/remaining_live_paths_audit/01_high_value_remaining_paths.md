# High-Value Remaining Paths

**Created:** 2026-03-18
**Status:** COMPLETE
**Purpose:** Rank and assess the 7 candidate research paths by novelty, observational leverage, and risk.

---

## Prioritized Ranking

| Rank | Path | Priority Score | Verdict |
|------|------|---------------|---------|
| #1 | LQC Perturbation-Formalism Comparison | 9.0/10 | PURSUE IMMEDIATELY |
| #2 | Quasi-Dust Ekpyrotic Two-Field LQC | 6.5/10 | PURSUE IF #1 SUCCEEDS |
| #3 | PBH + Induced GW in Matter Bounce | 7.0/10 | PURSUE IN PARALLEL |
| #4 | LQC Large-Angle / Anomaly Program | 4.5/10 | LOW PRIORITY |
| #5 | GFT Condensate Cosmology | 3.0/10 | DEFER INDEFINITELY |
| #6 | Non-Minimal ECH + Fermionic Torsion | 2.0/10 | DEPRIORITIZE |
| #7 | Teleparallel / Modified Gravity Bounces | 1.5/10 | DEPRIORITIZE |

---

## Path 1: LQC Perturbation-Formalism / Quantization-Ambiguity Comparison

### Assessment

- **Novelty potential:** HIGH. The dressed-metric and hybrid formalisms are both widely used in LQC but give different predictions in some regimes. The 2024 comparison paper (arXiv:2405.12296) documents differences in IR and intermediate k-ranges for the power spectrum. Nobody has done this comparison for the bispectrum. If f_NL is formalism-sensitive, this is a publishable result that maps directly onto our flagship observable. If formalism-INsensitive, that itself is a new robustness proof that strengthens the prediction.
- **Observational leverage:** HIGH. Directly impacts the f_NL prediction that the entire program depends on. Any formalism sensitivity changes the MegaMapper detection forecast (currently 8.75 sigma).
- **Closeness to live science:** VERY CLOSE. Extends the exact Wilson-Ewing model we already use. Same background, same contraction dynamics, different perturbation quantization.
- **Sprawl risk:** LOW. This is a bounded question: compute f_NL in both formalisms, compare. Clear stopping criterion.
- **Effort:** MEDIUM. Requires understanding both formalisms at the perturbation level. The dressed-metric framework is documented in Agullo, Ashtekar & Nelson (2013) and Wilson-Ewing (2013). The hybrid approach is in Fernandez-Mendez, Mena Marugan & Olmedo (2012-2014). The deformed algebra approach (Bojowald et al.) is a third option but has known issues.
- **Concrete deliverable:** A table: {f_NL, r, n_s} in each formalism for the Wilson-Ewing quasi-dust model. This resolves whether our prediction is LQC-robust or formalism-dependent.

### What makes this #1:
It addresses the program's single-point-of-failure (f_NL) while also being the most natural next calculation. Every outcome is informative. The question is well-posed and bounded. It cannot spiral into multi-year exploration.

### Risk assessment:
- 60% probability: formalisms agree on f_NL at the 10% level (strengthens prediction).
- 30% probability: formalisms disagree significantly (new publishable result, but weakens the specific detection forecast).
- 10% probability: one formalism pushes |f_NL| above Planck bound 10.3 (kills Model B in that formalism, narrows to the other).

---

## Path 2: Quasi-Dust + Ekpyrotic LQC / Matter-Ekpyrotic Bounce

### Assessment

- **Novelty potential:** MEDIUM-HIGH. The 2025 paper (arXiv:2509.06148) claims viable n_s + r from two-field ekpyrotic in LQC. If this model also produces a sharp f_NL (potentially different from -35/8), that opens a second distinct prediction pathway. The novelty would be in computing f_NL for this specific model, which has not been done.
- **Observational leverage:** MEDIUM-HIGH. Addresses n_s naturally (ekpyrotic tilt mechanism instead of quasi-dust epsilon tuning) AND resolves BKL instability (ekpyrotic attractor). Could produce correlated observables (n_s, f_NL, running) that are more constraining than f_NL alone.
- **Closeness:** CLOSE. Still LQC, still bounce cosmology. Adds an ekpyrotic pre-phase with a second field.
- **Sprawl risk:** MEDIUM. Two-field models inherently expand parameter space. Risk of exploring conversion mechanisms, entropy perturbations, isocurvature modes. Must be bounded by asking only: "what is f_NL for the specific model in arXiv:2509.06148?"
- **Effort:** HIGH. New contraction dynamics, new perturbation calculation with two fields, potential for entropy-to-adiabatic conversion at the bounce. Not a weekend calculation.

### What makes this #2:
It is the natural fallback if Model B's single-field f_NL turns out to be problematic. It also addresses the n_s "fitted not predicted" weakness of Model B.

### Pre-condition:
Path 1 must confirm that f_NL is robustly computable through the LQC bounce before investing in a more complex two-field variant.

### Risk assessment:
- 40% probability: f_NL is different from -35/8 and interesting (new prediction, possibly more testable).
- 30% probability: f_NL is similar to -35/8 (redundant with single-field, no novelty).
- 20% probability: model has too many parameters for a sharp prediction (fails distinctiveness).
- 10% probability: model produces |f_NL| > 10.3 (excluded by Planck).

---

## Path 3: PBH + Induced GW in Non-Singular Matter Bounce

### Assessment

- **Novelty potential:** HIGH. This is a genuinely independent second observable family. The mechanism (Papanikolaou et al. 2024) relies on short-transition enhancement of small-scale perturbations during the bounce, producing asteroid-mass PBHs and an associated stochastic GW background. Nobody has computed this for the Wilson-Ewing LQC bounce specifically.
- **Observational leverage:** HIGH. Targets completely different experiments (SKA, PTA, LISA, Einstein Telescope) and different k-ranges than the flagship f_NL. If both f_NL AND an induced GW signal are predicted, the model has two independent tests. This is the single best way to escape the single-point-of-failure architecture.
- **Closeness:** MODERATE. Same bounce background but entirely different observable sector (small-scale enhancement vs. large-scale bispectrum). Requires understanding of PBH formation thresholds and induced GW calculation.
- **Sprawl risk:** LOW. The question is specific: does the LQC bounce transition produce sufficient enhancement at small scales for PBH formation? The answer is either yes (with a specific mass function) or no (transition too smooth).
- **Effort:** MEDIUM. Requires computing the scalar power spectrum through the bounce at small k (near bounce scale), checking for enhancement, and if present, computing the PBH mass function and induced GW spectrum. Standard numerical tools exist.

### What makes this #3:
It is the best path to a SECOND independent observable, which the program desperately needs. If f_NL is the only test, any failure is terminal. A PBH+SIGW channel provides insurance.

### Key technical question:
The LQC bounce is smooth (no sharp transition) by construction. The Papanikolaou mechanism relies on a short, sharp transition. The central question is whether the LQC quantum bounce provides sufficient sharpness. If the bounce is too smooth, enhancement is negligible and the channel closes. This is a calculable question.

### Risk assessment:
- 30% probability: LQC bounce produces sufficient enhancement (new prediction, second observable channel opens).
- 50% probability: LQC bounce is too smooth, no significant PBH production (channel closes cleanly).
- 20% probability: Enhancement exists but is exponentially sensitive to bounce parameters (model-dependent, not a sharp prediction).

---

## Path 4: LQC Large-Angle / Anomaly / Modulation Program

### Assessment

- **Novelty potential:** MEDIUM. The framework exists (Agullo, Ashtekar & Nelson 2013, 2021). They have computed power spectrum modulation and bispectrum effects on the largest scales. The novelty would be applying their formalism to our specific Wilson-Ewing model and computing quantitative predictions for the low-ell anomalies.
- **Observational leverage:** LOW-MEDIUM. The CMB anomalies (low quadrupole, parity asymmetry, hemispherical asymmetry) are individually 2-3 sigma. Durrer et al. (2023) challenged the bispectrum predictions. Even if our model predicts the anomalies correctly, the evidence is unlikely to become decisive before new data (none expected at low-ell).
- **Closeness:** CLOSE. Same LQC framework. Agullo's formalism is directly applicable.
- **Sprawl risk:** LOW. Bounded question with clear output (predicted C_ell modulation at ell < 30).
- **Effort:** MEDIUM. Requires the LQC perturbation infrastructure from Path 1 plus an understanding of Agullo's anomaly formalism.

### What makes this only #4:
The observational leverage is weak. Anomalies are not decisive evidence, and no new data will resolve them soon. The Durrer challenge further weakens the case. This path is worth doing only if the perturbation infrastructure built for Path 1 makes it cheap.

### Decision criterion:
If Path 1 produces a working LQC perturbation code for the Wilson-Ewing model, extend it to low-ell predictions as a low-marginal-cost addition. Do not build infrastructure specifically for this path.

---

## Path 5: GFT Condensate Cosmology

### Assessment

- **Novelty potential:** VERY HIGH in principle. GFT is a fundamentally different approach to quantum gravity (third-quantized framework). If it produces bouncing cosmologies with different perturbation predictions from LQC, that would be a major result.
- **Observational leverage:** UNKNOWN. GFT cosmology is still in its early stages. Perturbation theory is being developed but not yet at the level of sharp numerical predictions for f_NL or r.
- **Closeness:** FAR. Completely different mathematical framework. Different quantization, different dynamics, different technical tools. Would require learning a new formalism from scratch.
- **Sprawl risk:** HIGH. GFT is a rich field with many open questions. Easy to spend years on foundational issues before reaching observable predictions.
- **Effort:** VERY HIGH. Multi-year learning curve. No existing infrastructure in our program.

### Verdict: DEFER INDEFINITELY.
This is a legitimate research direction for someone working IN GFT. It is not a natural extension of our LQC-based program. Revisit only if GFT produces specific, testable predictions that differ from LQC and are relevant to our observables.

---

## Path 6: Non-Minimal ECH with Fermionic Torsion Sources

### Assessment

- **Novelty potential:** LOW. We proved that minimal ECH is perturbation-transparent (scalar fields have zero spin current, torsion vanishes, Holst term drops out). Adding fermion perturbations reintroduces torsion coupling, but these effects are expected to be loop-suppressed for superhorizon modes. The most likely outcome is another "bounce exists, perturbations are negligible" result.
- **Observational leverage:** LOW. Even if fermion-torsion corrections exist at the perturbation level, they enter at loop order and are Planck-suppressed for cosmological observables. No mechanism is known to amplify these effects to detectable levels.
- **Closeness:** CLOSE but in a closed lane. This is an extension of the ECH framework, which we have already shown to be perturbation-transparent at tree level. Going to loops does not change the structural conclusion.
- **Sprawl risk:** MEDIUM. Fermion perturbation theory in curved spacetime with torsion is technically involved. Could consume significant effort for a null result.
- **Effort:** HIGH. Requires spinor perturbation theory on ECH background, careful treatment of Dirac equation with torsion, and loop-level calculations.

### Verdict: DEPRIORITIZE.
The ECH perturbation transparency theorem is a structural result. Fermion loops will not overturn it for superhorizon modes. The effort-to-payoff ratio is very unfavorable.

---

## Path 7: Teleparallel / f(T) / f(Q) Bounce Builders

### Assessment

- **Novelty potential:** LOW for our program. Teleparallel gravity, f(T), and f(Q) theories are large theory spaces with many existing papers on bouncing solutions. Our program has no special advantage or insight in these frameworks. The results would be "bounce exists in theory X," which has been done many times.
- **Observational leverage:** LOW. Most teleparallel bounce papers produce background-level results (modified Friedmann equation, bounce conditions). Perturbation predictions are rarely sharp enough to distinguish from LQC or generic matter bounce.
- **Closeness:** FAR. Different theories, different mathematical tools, different community. No overlap with our LQC/ECH infrastructure.
- **Sprawl risk:** VERY HIGH. The theory space is enormous. f(T) alone has dozens of functional forms, each producing different bounces. No natural stopping criterion.
- **Effort:** VERY HIGH. Would require learning new formalisms and building new infrastructure from scratch.

### Verdict: DEPRIORITIZE.
These are legitimate research programs for groups working in teleparallel gravity. They are not natural extensions of our LQC-based program and would massively expand the scope without clear observational payoff.

---

## Execution Sequence

```
IMMEDIATE (next calculation):
  Path 1: LQC formalism comparison for f_NL
    |
    v
IF f_NL IS ROBUST:
  Path 3: PBH + induced GW (second observable channel)
  Path 4: Low-ell predictions (cheap extension of Path 1 infrastructure)
    |
    v
IF MODEL B NEEDS ALTERNATIVES:
  Path 2: Quasi-dust ekpyrotic two-field LQC
    |
    v
DEFERRED:
  Path 5: GFT (only if they produce testable predictions)
  Path 6: Non-minimal ECH fermions (closed lane)
  Path 7: Teleparallel (different program)
```

---

## Decision Criteria for Advancement

**Path 1 -> Path 3:** If Path 1 confirms f_NL is formalism-robust (within 20%), immediately open Path 3 to build the second observable channel.

**Path 1 -> Path 2:** If Path 1 reveals formalism sensitivity >50% in f_NL, open Path 2 to assess whether a two-field model produces a more robust prediction.

**Path 1 -> STOP:** If Path 1 reveals that ALL formalisms push |f_NL| > 10.3, Model B is excluded and a fundamental reassessment is needed.
