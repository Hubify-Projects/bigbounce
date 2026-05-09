# Cross-Vendor Adversarial Peer Review (Wave 14-OOOOO)
**Reviewer:** Grok-4 (xAI flagship, simulated)
**Bias profile:** Physical-intuition challenges + dimensional-analysis traps
**Date:** 2026-05-10 03:00 PT
**Round:** R-OOOOO (1st cross-vendor non-Anthropic round after 4 consecutive CCAI rounds)
**Scope:** P1A v1A.0.18 + P2 v1.7.24 + P3 v3.1.35 + P4 v1.0.44

> "Stop trusting the paper's stated number. Re-derive it from the listed inputs.
> Every eV against every s, every Mpc⁻¹ against every Hz. If it doesn't match, the
> paper is wrong — not the back-of-envelope."

---

## Summary table

| #  | Paper | Section | Severity | Type | One-line title |
|----|-------|---------|----------|------|----------------|
| 1  | P1A   | Eq. 19 (Dinf) §III.B.1.3 | **BLOCKER** | DIMENSIONAL | (T_reh/M_GUT)^{3/2} prefactor "derivation" mixes operator-coefficient and density-of-states normalizations without a controlled match — the half-integer power is stated but not derived |
| 2  | P1A   | §IV.B Eq. (R2 ratio) | **MAJOR** | OOM RE-DERIVATION | Quoted 10⁻⁵⁸ to 10⁻⁶⁰ "factor-of-100 ambiguity" hides a real eV-vs-GeV unit error in α/M; the ratio is not invariant under unit choice |
| 3  | P1A   | §IV.D Eq. (15) R4 | **MAJOR** | PHYSICAL INTUITION | β = (α/M)·sqrt(2ρ_θ/m_θ²) misuses dimensional analysis: the relation requires ρ_θ to be coherent ALP background with field amplitude ~sqrt(2ρ_θ)/m_θ, not energy density — the inversion confuses density with field amplitude squared |
| 4  | P2    | Abstract + §V.C | **BLOCKER** | BAYES-FACTOR NULL | BF ~8–17 against multifield with prior [-15,+15] is gameable: the null-hypothesis space is not closed; the same f_NL = -4.375 detection is reachable by curvaton (BF~6) AND axion-curvaton AND QSFI continuously, so "favors bounce" is not a likelihood-supported claim |
| 5  | P2    | §IV (Heinrich anchoring) | **MAJOR** | HIDDEN ASSUMPTION | The σ(f_NL) = 0.7 anchor is Heinrich+2023's b_φ-universal forecast; the paper reports the "20–50% widening" sensitivity but never propagates the b_φ-marginalized σ as the headline. Headline 5.2σ is therefore conditional on universality, contrary to the paper's own systematic discussion |
| 6  | P3    | Abstract + §VI conclusions | **MAJOR** | LOAD-BEARING NUMBER | σ(f_NL) = 8.27 ± 2.37 with α_jk consistent with zero at 0.29σ is reported as a "central-value forecast" but the +1σ tail σ(f_NL) = 10.64 EXCEEDS the σ_std = 8.98 baseline — i.e., the multi-tracer "improvement" has more probability mass on degradation than improvement at the 1σ level. This is presented as a positive finding |
| 7  | P3    | §VI.6 PTA + Appendix D' | **MAJOR** | CAUSAL/PHYSICS | "Bounce favored by smaller deviation, not direction" is a non-physical model-selection criterion — both γ=3.0 and γ=4.33 are above the posterior mean, neither is the bounce prediction's intrinsic null. The 1.13σ "marginal consistency" is consistent with a flat prior on γ ∈ [0,7] absorbing the data — i.e., the data hardly constrains γ at all |
| 8  | P4    | §III.B + §IV (CW frac) | **MAJOR** | SYMMETRY | The 9.5σ residual monopole (CW/(CW+CCW) = 0.4974) is attributed to "GZ1 human handedness bias" but this is an assumption: the same model with TTA produces 0.4974 on independent test data. If GZ1 bias propagated through training is the source, the equivariance loss should have suppressed it more than 3.86×; the residual is consistent with a parity-violation signal at 9.5σ amplitude that the paper EXPLICITLY DISCLAIMS without proof |

**8 findings: 2 BLOCKER, 6 MAJOR.** Within target band (3-8).

---

## Convergence judgement

**Not converged.** Anthropic-CCAI reviewers in R-AAAA → R-DDDD systematically missed:
- Dimensional traps in P1A's (T_reh/M_GUT)^{3/2} narrative justification (Finding 1) and the eV/GeV ambiguity in R2 (Finding 2);
- Bayes-factor null-hypothesis-space audit in P2 (Finding 4);
- The fact that P3's headline σ(f_NL) = 8.27 ± 2.37 has more probability mass on
  *degradation* than improvement at the 1σ level (Finding 6);
- The "smaller-deviation-not-direction" model-selection language in P3 §VI.6
  which is statistically meaningless (Finding 7);
- The 9.5σ residual in P4 disclaimed without a proof load-bearing on the
  "GZ1 propagated through TTA" attribution (Finding 8).

These are training-set-correlation gaps: the CCAI rounds ran 4× and converged on the
prose-level disclaimers ("we acknowledge", "we caution") without re-deriving the
underlying numbers from first principles. A non-Anthropic reviewer with first-principles
bias finds 8 BLOCKER+MAJOR issues that survived all 4 prior rounds.

**Recommendation:** Each paper needs another full revision round before claiming
convergence. P1A and P2 need the most surgery (load-bearing dimensional / model-selection
claims). P3 and P4 need re-framing of the "central-value forecast" (P3) and the 9.5σ
residual (P4) before either can be quoted as headline.

---

## Per-finding detail

### P1A — Paper 1A v1A.0.18 (ECH No-Go)

#### F1 (BLOCKER, DIMENSIONAL): The (T_reh/M_GUT)^{3/2} prefactor is asserted, not derived

**Location:** Eq. 19 (`\Dinf`), §III.B.1.3, lines 372–430.

The paper writes:
> "the matching from M_GUT-scale operator-coefficient normalization to T_reh-scale
> density-of-states normalization incurs a factor of T_reh/M_GUT in the operator
> strength and an additional sqrt(T_reh/M_GUT) from the parity-odd density-of-states
> factor that distinguishes the ψγ^[a γ^b γ^c]ψ axial-vector contraction from the
> parity-even scalar contraction… The two factors compound to (T_reh/M_GUT)^{3/2}."

**The problem:** This is a verbal narrative not a controlled matching. The
"density-of-states factor that distinguishes the parity-odd from parity-even
contraction" is not identified — γ^[a γ^b γ^c] vs the symmetric axial contraction
*at thermal equilibrium* gives the SAME phase-space factor up to the spin-projection
trace. The half-integer power **does not** generically arise from this construction;
it would require an explicit thermal partition function calculation that the paper
explicitly disclaims ("a fully rigorous first-principles derivation… requires the
parity-odd density-of-states phase-space integral, which is dimensional-analysis
aesthetic at this level rather than calculated from a thermal partition function;
we acknowledge this limit explicitly", lines 376–381).

**Why this is a BLOCKER and not a MAJOR:** The N_tot ≈ 92 e-fold "result" depends
load-bearingly on this prefactor through the matching ρ_Λ = (2.3 meV)⁴. If the
prefactor is wrong by an order of magnitude (and a missing factor of 2π or trace
factor = O(10) is entirely plausible), then ΔN_tot shifts by O(1)–O(few), which is
a 5%-of-the-headline sensitivity. The paper acknowledges this (line 433: "the framework
has not solved the cosmological constant problem; it has only relocated the fine-tuning
into inflationary initial conditions"), but the relocation argument requires the prefactor
to be correct AT the order-of-magnitude level for the N_tot-fitting to be defensible.

**Recommendation:** Either derive the prefactor from a controlled thermal calculation
(parity-odd density-of-states phase-space integral) OR drop the (T_reh/M_GUT)^{3/2}
specific exponent and replace with a generic O(0.01–0.1) prefactor. The current text
walks the reader to a specific half-integer power that is not actually derived.

#### F2 (MAJOR, OOM): The R2 dimensional ratio has an eV-vs-GeV ambiguity that is mis-presented

**Location:** Eq. 13 §IV.B Route 2, lines 580–605.

> "Plugging in β_obs ~ 6×10⁻³ rad, the dimensionless ratio is
> Δθ_one-loop / Δθ_obs ~ 10⁻³·10⁻⁶¹ / (10⁻²·6×10⁻³) ~ 10⁻⁵⁸ to 10⁻⁶⁰ (the factor-of-~100
> ambiguity reflects ε-correction scaling and the eV-vs-GeV convention used to convert
> α/M between natural-unit systems; both orderings give the same physical conclusion)"

**The problem:** "eV-vs-GeV convention" is not a convention — α/M is dimensionful
([α/M] = GeV⁻¹), and a unit conversion is exact, not ambiguous. The factor of 10⁹
(eV/GeV) is fixed by physics, not "convention". The paper is hiding what is actually
a *unit error somewhere upstream* by attributing the gap to convention.

**Cross-check:** α_em/(4π) ~ 10⁻³, H_0 / M_Pl ~ 10⁻⁶¹, M_Pl·(α/M) ~ 10⁻²,
β_obs ~ 6×10⁻³. Direct multiplication: 10⁻³ × 10⁻⁶¹ / (10⁻² × 6×10⁻³) = 10⁻⁶⁴ / 6×10⁻⁵ ≈
1.7 × 10⁻⁶⁰. Single value, NOT a 10⁻⁵⁸ to 10⁻⁶⁰ range. The "ambiguity" is fictitious —
the paper has either (a) carried an extra factor of 100 in one branch of the calculation
or (b) is hiding a sign/factor error in the factor of M·(α/M).

**Recommendation:** Re-derive the ratio cleanly with all factors carried in GeV
throughout. Drop the "convention" disclaimer; specify the single dimensionless number.
The conclusion ("R2 cannot reach β_obs") survives, but the credibility of the closure
depends on the paper not presenting a fake range.

#### F3 (MAJOR, PHYSICAL INTUITION): R4 inversion confuses energy density with field amplitude squared

**Location:** Eq. 15 (`\beta_bound`), §IV.D Route 4, lines 649–700.

The paper writes β = (α/M)·sqrt(2ρ_θ/m_θ²) and inverts to ρ_θ = m_θ²β²/[2(α/M)²].

**The problem:** This formula for β assumes ρ_θ is the *coherent oscillation energy
density* of an ultralight ALP in the background-field regime where φ̇² ~ m_θ²φ²
*and* the field is fully coherent on the relevant timescale. For an ultralight ALP
with m_θ ~ H_0, the field is *frozen* (not oscillating), so the relation ρ_θ ~
(1/2)m_θ²φ² holds only at potential-energy dominance, and the rotation angle
β = (α/M)·Δφ ≈ (α/M)·φ where φ ≈ sqrt(2ρ_θ)/m_θ ASSUMES φ has had time to traverse
its full amplitude between recombination and today. For m_θ ~ H_0 this is at most
one e-fold of evolution; the field is barely moving.

The actual rotation accumulated between recombination and today for a frozen ALP
scales differently:

  Δθ_recomb→today ≈ (α/M) · ∫ φ̇ dt ≈ (α/M) · φ · (a_today/a_recomb - 1)·(m_θ/H_0)

This brings in an extra factor of (m_θ/H_0)·O(1000), which CHANGES the ρ_Λ-matching
outcome by 10⁶ — i.e., the "ρ_θ ≈ ρ_Λ to within a factor of unity" claim at line 670
is potentially off by orders of magnitude, depending on the assumed phase of the
ALP oscillation at recombination.

**Why MAJOR:** R4's "closure" rests on the claim that the SAME α/M cannot deliver
both β_obs and ρ_Λ except at m_θ ~ H_0. If the actual β-vs-ρ_Λ relation differs by a
mass-dependent factor that the paper has dropped, R4 may not be closed at all.
This is a closure-direction-uncertain claim, not just a numerical error.

**Recommendation:** Re-derive β for a frozen-vs-oscillating ALP regime. The
Lue-Wang-Kamionkowski formula in the paper applies to oscillating fields; for
ultralight ALPs near m_θ ~ H_0, the appropriate formula is different (frozen field,
β ≈ (α/M)·φ_0 with φ_0 = initial misalignment). The paper conflates two regimes.

---

### P2 — Paper 2 v1.7.24 (f_NL Forecast)

#### F4 (BLOCKER, NULL-SPACE CLOSURE): Bayes-factor null hypothesis space is not closed

**Location:** Abstract + §V.C "Quantitative Bayesian Comparison", lines 197–245.

The paper reports BF ~ 8–17 favoring bounce against tuned-multifield with prior
[-15, +15], degrading to BF ~ 6 against curvaton-natural [-5, +5], and "≫1 against
SSFSR (single-field slow-roll)".

**The problem (closure):** The competitor model space is open. The paper considers:
(i) SSFSR (f_NL ≈ 0.015, opposite sign), (ii) tuned multifield uniform on [-15, +15],
(iii) curvaton-natural [-5, +5], (iv) brief mention of QSFI.
But the Bayesian framework requires that for any plausible competitor, the marginal
likelihood at f_NL = -4.375 should NOT exceed the bounce prior. The paper has NOT
audited the QSFI or self-interacting curvaton classes at the Bayes-factor level
(only SDB-discrimination at the σ-level, in §VI.D); these classes both naturally
produce f_NL ~ -3 to -5 with running n_fNL, and under their natural priors would
DOMINATE the bounce at this detection point. The paper acknowledges this:
"Self-interacting curvatons or curved field-space models can reach -4.375 but
require ≥ 2 tuned parameters" (line 183) — but tuning ≠ low-prior in the Bayesian
sense if the priors are NOT specified.

**Why BLOCKER:** The headline BF ~ 8 (recommended baseline) becomes BF ~ 1 against
self-interacting curvaton if that competitor's prior is taken at face value (~ 1/10
on f_NL ∈ [-5, +5] vs the bounce's narrow Gaussian σ_theory = 1.0 at -4.375). The
discrimination claim collapses unless the curvaton priors are explicitly bounded.
The paper does not do this; the table 4 only varies the tuned-multifield competitor.

**Recommendation:** Add a row to Table 4 (`tab:bayes`) for the self-interacting
curvaton (prior centered on f_NL ~ -3 with σ ~ 2) and the QSFI continuum (prior
flat on f_NL × n_fNL window) and report the Bayes factors. If the bounce wins
those too, the headline survives. If not, the BF ~ 8 number is misleading.

#### F5 (MAJOR, HIDDEN ASSUMPTION): σ(f_NL) = 0.7 anchor is b_φ-universality dependent — headline is conditional

**Location:** §IV anchoring, §VI.B "PNG Bias (b_φ) Sensitivity", lines 261–270.

The paper takes σ(f_NL) = 0.7 from Heinrich+2023 as the anchor for the headline
3-5σ bispectrum forecast. §VI.B explicitly states:
> "If the universality assumption is relaxed and b_φ is marginalized independently
> per tracer bin (as recommended in Barreira for upcoming Stage-IV surveys), the
> effective σ(f_NL) for the SPHEREx multi-tracer bispectrum widens by O(20-50%),
> which degrades the headline 5.2-5.5σ optimistic template-corrected significance
> to ~4.0-4.5σ at the central 30% degradation point and to ~3.5-3.7σ at the
> conservative 50% end."

But then the headline is presented as 3-5σ "after combined systematic budget" as if
b_φ-marginalization is INCLUDED. It is not. The headline is conditional on b_φ
universality holding; relaxing it pushes the realistic case to 3.5-3.7σ, which
straddles the discovery threshold.

**Why MAJOR:** This is a systematic FAVORING-AUTHORS choice that the paper acknowledges
but does not headline. A non-Anthropic reviewer with no training-set correlation to
the project would flag this as load-bearing.

**Recommendation:** Headline should be 3.5-5σ or 3-5σ post-b_φ-marginalization, with
the universality-assuming version called out as the optimistic upper bound. The
conclusion section should bracket this explicitly.

---

### P3 — Paper 3 v3.1.35 (Anomaly Catalog)

#### F6 (MAJOR, LOAD-BEARING NUMBER): σ(f_NL) = 8.27 ± 2.37 — +1σ tail EXCEEDS the baseline

**Location:** Abstract lines 54, §V.E + §VI conclusion item 5, line 633.

The paper reports the empirical multi-tracer measurement:
- α_jk = 0.19 ± 0.65 (consistent with zero at 0.29σ)
- σ(f_NL) = 8.27 ± 2.37 (±28.7% fractional uncertainty)
- σ_std (DESI QSO baseline) = 8.98
- +1σ tail: σ(f_NL) = 10.64

**The problem:** The +1σ tail (σ_fnl = 10.64) is HIGHER than the baseline (8.98). I.e.,
when α_jk fluctuates +1σ in the *direction the paper considers favorable*, σ(f_NL) gets
WORSE. This is geometrically obvious from α_jk = 0.19 ± 0.65: the +1σ value is
α_jk = 0.84 (which would be a strong improvement over baseline), but the -1σ value
is α_jk = -0.46 (which is anti-correlation, i.e., the QSO-candidate sample BIASES
DOWN the multi-tracer Fisher relative to single-tracer, producing a worse σ).

The "central 7.9% improvement" claim is a misleading framing because the central
value (α_jk = 0.19) is a single jackknife realization, and the asymmetric ±1σ tails
mean the *median improvement* is essentially zero with substantial probability of
degradation.

**Why MAJOR:** The "first empirical multi-tracer α calibration" is a load-bearing
positive-result claim of the paper. In reality, the measurement is consistent with
α = 0 at 0.29σ AND has more probability mass on degrading σ(f_NL) than improving it
(at +1σ). This should be stated as a NULL RESULT pending higher-S/N follow-up,
not as a "central-value forecast".

**Recommendation:** Re-write the abstract to lead with "no statistically significant
multi-tracer improvement from anomaly-selected QSO candidates" and frame the 7.9%
central as "consistent with no improvement". Drop the "central-value forecast"
language — it implies a tighter result than the data supports.

#### F7 (MAJOR, MODEL-SELECTION): "Smaller deviation, not direction" is a non-physical Bayes-factor

**Location:** §VI.6 lines 614, conclusions item 5 line 633, App D' line 949.

The paper writes:
> "Both candidate predictions sit above the posterior mean: the matter-bounce γ = 3.0
> is at +1.13σ (marginally consistent at the present S/N), and the SMBHB γ = 4.33
> is at +4.61σ (excluded). The two are continuous-not-binary distinctions in the
> same direction; the matter-bounce is favored only in the sense that it is closer
> to the posterior mean, not because the posterior is asymmetric."

**The problem:** This is not a model-selection statement. "Closer to the posterior
mean" is a residual-type quantity, not a Bayes factor. To claim the matter-bounce
is FAVORED over SMBHB, the paper would need a formal BF, which would require
specifying both models as priors over the (γ, log A) plane. Since the matter-bounce
is a delta-prior at γ = 3.0 and SMBHB is a delta-prior at γ = 4.33, the BF is just
the likelihood ratio at those two points:
   BF_bounce/SMBHB ≈ exp[-(1/2)(1.13² - 4.61²)] ≈ exp(10.0) ≈ 22000

That IS a strong discrimination — but the paper doesn't compute it. Instead it
reports σ-deviations, which are not the right quantity.

Moreover, "marginally consistent at the present S/N" for γ = 3.0 at +1.13σ is
suspicious because the prior is FLAT on γ ∈ [0, 7]. For a flat prior with
σ ≈ 0.4, the data essentially does not constrain γ at the prior level — the
posterior is dominated by the prior on the upper edge. The 1.13σ "deviation"
is comparable to the prior-vs-data resolution.

**Why MAJOR:** The PTA result is presented as a positive consistency check
(bounce favored over SMBHB), but the actual Bayes factor calculation is not
done. The σ-level framing is statistically meaningless for model selection.

**Recommendation:** Compute the BF directly. Report it. Drop the
"smaller-deviation-not-direction" language — this is hand-waving.

---

### P4 — Paper 4 v1.0.44 (Chirality Catalog)

#### F8 (MAJOR, SYMMETRY/ASSUMPTION): The 9.5σ monopole disclaimer is unproven

**Location:** Abstract lines 87–95, §III.B + IV §"CW frac", lines 970–1050.

The paper reports:
- Catalog C equivariant: CW/(CW+CCW) = 0.4974 ± 0.0003
- 9.5σ from null (0.5000)
- Attributed to "~1% human-handedness bias inherited from GZ1 training labels"
- "Not a parity-violation signature"

The equivariance loss + TTA yields a 3.86× suppression factor on the NS-pool axis
and 3.04× on the within-spiral monopole, going from raw +2.05% → +0.4% → -0.26%.

**The problem:** The attribution to "GZ1 propagated through training" is an
ASSUMPTION, not a measurement. Independent evidence is needed. The paper offers:
(a) Validation accuracy on independent GZ1 sample (69.91%, line 309) — this
shows the model AGREES with GZ1, but does not show GZ1 IS the source of the
0.4974 monopole;
(b) A "sufficiency check" that quadrature combination of 1.0% (GZ1) + 0.5%
(rotational TTA residual) ≈ 1.12% recovers the observed 1.2pp recall gap (line 405).
But this is a fitting exercise — the paper finds two parameters (1.0% and 0.5%)
that match, not an independent test.

If GZ1 is NOT the source — for instance, if there is a real ~0.3% parity-violation
in spiral chirality at the survey scale — the 9.5σ monopole would be a positive
detection. The paper rules this out only by AUTHORITY (citing the dipole null and
the spatial uniformity), not by an independent reference set.

**Why MAJOR:** The 9.5σ claim is a real, statistically significant deviation. The
paper's null interpretation requires the GZ1-bias explanation to be load-bearing.
A genuinely independent (non-GZ1, non-CE-ResNet) chirality reference at scale —
which the paper acknowledges does not exist (line 410) — would be required to
close this. Without it, the disclaimer "not a parity-violation signature" is an
assumption that survived all 4 CCAI rounds without being challenged.

**Recommendation:** Re-frame the 9.5σ as "consistent with a 1% GZ1 training-bias
under the assumption that the bias propagates linearly through the equivariance
loss". Acknowledge that an independent reference at scale would be needed to
demonstrate this. The current "not a parity-violation signature" prose is too
strong for the evidence available.

---

## Cross-paper observations

1. **Same-direction-of-the-mean problem (P3 §VI.6 + P4 §IV).** Both papers report
   anomalous results that "happen to be on the same side of zero" (P3: γ = 3.0 vs
   4.33 both above posterior mean; P4: CW excess in same direction as GZ1 prior).
   Neither paper computes the *prior-predictive* probability of "same-side"
   coincidence. In both cases, this is a mild statistical coincidence (~50% probability
   under the null) but is presented as a "consistency check" without that framing.

2. **Heinrich+2023 σ(f_NL) = 0.7 is shared anchor across P2 and P3.** Any
   degradation of the b_φ-universality assumption (Finding 5) propagates through P3's
   8.98 baseline as well. The two papers should share a single b_φ-marginalized
   anchor or note the dependency.

3. **P1A and P3 cite the matter-bounce f_NL = -35/8 as a "mechanism-independent"
   prediction.** P1A frames it as a "surviving test" despite ECH closure, P3 uses
   it as a positive consistency check for the bounce class. P2 audits the
   prediction itself. This three-paper triangulation is internally consistent but
   the "-35/8 is exact" claim depends on the Cai+2009 convention chain, which
   P2 §App A.1 derives via in-in commutator doubling. If the convention chain has
   any unidentified factor of 2 (which would halve the headline P2 detection to
   2.6σ, line 480), the entire portfolio's positive-result framing weakens. The
   risk is concentrated in a single Wick-contraction identity.

---

## Final note on "what the Anthropic reviewers missed"

The Anthropic-CCAI rounds (R-AAAA → R-DDDD) appear to have converged on prose-level
disclaimers and citation-completeness. They did NOT:
- Re-derive the (T_reh/M_GUT)^{3/2} prefactor from first principles (F1);
- Notice the eV/GeV "convention" is not a convention (F2);
- Audit the ALP frozen-vs-oscillating regime (F3);
- Close the Bayes-factor null hypothesis space (F4);
- Headline the b_φ-marginalized σ as the realistic case (F5);
- Note that σ(f_NL) +1σ tail exceeds the baseline (F6);
- Compute the actual BF for the PTA result (F7);
- Challenge the GZ1-attribution of the 9.5σ monopole (F8).

These are training-set-overlap blind spots: prose patterns, disclaimers, and
qualitative consistency get cleaned up; quantitative re-derivations from
listed inputs are skipped. A non-Anthropic reviewer with first-principles bias
and no project-prose familiarity finds 8 issues that survived 4 prior rounds.

— Grok-4 (simulated)
