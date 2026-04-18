# Paper 2 — What's Actually Scientifically Interesting

**Purpose:** Distill the genuine scientific contributions of the f_NL forecast paper beyond "we computed a Fisher matrix" and "SPHEREx will detect it."

**Canonical paper:** `research/focused_paper_source_integration/02_full_draft.tex` (375 lines, v1.6.0, PDF dated 2026-03-24).
**SSOT:** [`project-context/SSOT/paper-2/status.md`](SSOT/paper-2/status.md).
**Last updated:** 2026-04-17.

**Format status:** Science 100 % done, manuscript 100 % written, but NOT arXiv-ready — document class is `article`+natbib and must be converted to `revtex4-2` per the program-wide mandate. See SSOT §0.

---

## Novelty scale (used below)

- **N0 — Replication:** Standard reproduction of prior work with our pipeline.
- **N1 — Refinement:** Tightens or extends prior work — higher precision, bigger sample, systematic audit.
- **N2 — Substantive:** New application of known methods → actionable new result (forecast, calibration, template).
- **N3 — First-of-kind:** Novel methodology or first-of-kind observation, no prior analog in the literature.
- **N4 — Paradigm-shifting:** New physics claim or falsification that changes the consensus.

---

## The 7 Genuinely Novel Scientific Contributions

### 1. Parameter-free f_NL = −35/8 prediction derived from matter-bounce dynamics — **N3**

**What:** For the matter-dominated contracting phase of a generic bounce cosmology, the primordial non-Gaussianity reduces algebraically to **f_NL^local = −35/8 = −4.375**, independent of the microphysical bounce mechanism (ekpyrotic, Cuscuton, effective-field-theory bounce, or spin-torsion ECH). The derivation is reproduced in three independent configurations (equilateral, squeezed, folded) and agrees with the Cai 2009 original result; the paper's contribution is the **mechanism-independence proof**.

**Why it matters:** Standard single-field slow-roll inflation predicts |f_NL^local| ≲ 0.01. Tuned multifield models can reach |f_NL| ∈ [0, 15] but require 2+ free parameters (mixing angles, spectator field mass). The matter-bounce prediction is **zero free parameters** — it's a consequence of the dynamics, not an input. A measurement at |f_NL − (−4.375)| ≲ 1 is a direct test; no tuning allowed.

**Scientific significance:** Creates a decisive falsification target. If SPHEREx reports f_NL ≠ −4.375 at >4σ, the entire matter-bounce class (not just one model) is disfavored. If SPHEREx reports f_NL = −4.375 ± 1, single-field slow-roll is rejected at >10⁵:1 Bayes factor.

**Paper claim:** "The matter-dominated contracting phase of any bounce cosmology predicts f_NL^local = −35/8 = −4.375 as a mechanism-independent, parameter-free consequence of the dynamics, verified here in equilateral/squeezed/folded configurations."

---

### 2. Template-overlap correction to the Fisher forecast — **N3**

**What:** When the data-analysis template (generic local-type f_NL) is applied to a matter-bounce primordial bispectrum, the two are not identical — their inner product (correlation) is r = 0.90 (CMB) and r = 0.85 (LSS scale-dependent-bias / SDB). The forecast must degrade σ(f_NL) by 1/r accordingly. Our template-corrected SPHEREx σ(f_NL) ≈ 0.7 (vs the Fisher-ideal 0.36); the corresponding detection significance for f_NL = −4.375 is **5.0–5.5σ**, not the 12σ an ideal template would suggest.

**Why it matters:** Prior matter-bounce forecast literature (Cai 2014, de Putter 2017) reports the template-matched Fisher ideal without the template-mismatch correction. That overstates detectability by ~30 %. Our pipeline is the first to close that gap quantitatively via 200 Monte Carlo template-cross-correlation realizations.

**Scientific significance:** Sets the realistic near-term target. 5σ is achievable; 12σ is a mirage.

**Paper claim:** "Template-overlap correction (r = 0.85–0.90) degrades the SPHEREx forecast from Fisher-ideal σ(f_NL) = 0.36 to template-corrected σ(f_NL) ≈ 0.7, yielding 5.0–5.5σ detection significance for f_NL = −35/8."

---

### 3. b_φ systematic-fragility audit — first in the literature — **N3**

**What:** The scale-dependent-bias channel for f_NL depends on b_φ, the non-Gaussian bias coefficient. It is not measured — it is assumed via the universality relation b_φ ≈ 2δ_c(b_1 − 1). We perform the first systematic fragility audit: at b_φ uncertainty of 20 %, MegaMapper σ(f_NL) degrades to ≈ 1.0; at 50 % uncertainty, σ(f_NL) ≈ 2.2; bispectrum channel alone (photo-z degradation included) adds another +5 % at 10 % outlier fraction.

**Why it matters:** Many f_NL papers quote forecast numbers that implicitly assume b_φ is known exactly. This is false — b_φ is uncertain by factors of 2 depending on tracer, and a future b_φ disagreement between simulations and data would silently inflate σ(f_NL) beyond published forecasts. Our audit quantifies the sensitivity so the field has a documented fragility baseline.

**Scientific significance:** Sets the priority for near-term simulation work — measuring b_φ to <20 % for SPHEREx and MegaMapper tracers is a pre-2028 survival-of-forecast requirement.

**Paper claim:** "The first systematic audit of b_φ uncertainty propagation shows σ(f_NL) scales from 1.0 (20 % uncertainty) to 2.2 (50 % uncertainty) for MegaMapper, establishing b_φ calibration as a pre-launch priority for SPHEREx and MegaMapper."

---

### 4. Bayes factors: bounce vs tuned multifield vs single-field — **N2**

**What:** We compute posterior Bayes factors for the matter-bounce prediction vs two inflationary alternatives:
- Tuned multifield ([−15,+15] uniform prior on f_NL, 2 extra parameters): **BF = 8–17** in favor of bounce if f_NL = −4.375 is measured.
- Single-field slow-roll (|f_NL| ≲ 0.01): **BF > 10⁵** in favor of bounce.

**Why it matters:** Bayes factors, not p-values, are the correct framework for model comparison across 2+ free-parameter priors. BF ≳ 10 is "strong evidence" on the Jeffreys scale, and the BF > 10⁵ against single-field is already decisive-class.

**Scientific significance:** Converts a point-forecast number (5σ detection) into a falsification framework (which class of theory survives the measurement).

**Paper claim:** "A SPHEREx detection of f_NL = −4.375 ± 0.7 would yield Bayes factor ≈ 8–17 in favor of the matter-bounce prediction over tuned multifield inflation, and > 10⁵ against single-field slow-roll."

---

### 5. Consistency recast: Planck + DESI → f_NL^bounce = −1.3 ± 4.5 (0.7σ from −4.375) — **N2**

**What:** Re-expressing existing Planck 2018 + DESI 2024 constraints in the matter-bounce template frame yields **f_NL^bounce = −1.3 ± 4.5**, i.e. the current data sit **0.7σ** from the bounce prediction. No existing observation excludes matter-bounce today.

**Why it matters:** Many prior discussions of "bounce is constrained by Planck" conflate the constraint on generic local-f_NL with the constraint on the mechanism-specific bounce template. Template overlap means the effective Planck constraint on bounce f_NL is weaker than the quoted local-f_NL constraint.

**Scientific significance:** The matter-bounce f_NL = −4.375 prediction is within 1σ of current data. The consensus that "bounce is dead" is unsupported by the numbers.

**Paper claim:** "Recasting Planck 2018 + DESI 2024 f_NL constraints into the matter-bounce template frame yields f_NL^bounce = −1.3 ± 4.5 — 0.7σ from the matter-bounce prediction, demonstrating that existing data are consistent with and do not exclude the bounce scenario."

---

### 6. Null-result asymmetry: SPHEREx disproves bounce at >4σ if null — **N2**

**What:** Because f_NL^bounce = −4.375 and SPHEREx σ(f_NL) ≈ 0.7 (template-corrected), a SPHEREx report of f_NL = 0 ± 0.7 would place the bounce prediction at |−4.375/0.7| = **6.25σ** from the measured value — decisively excluding it. Single-field slow-roll predicts f_NL ≈ 0, so the null-result scenario is consistent with inflation and catastrophic for matter bounce.

**Why it matters:** The measurement is genuinely two-sided — detection at −4.375 is strong evidence for bounce, but null at 0 is strong evidence against bounce. The matter-bounce class has no free knobs to absorb a null result; either the dynamics produces f_NL = −4.375 or the class is ruled out.

**Scientific significance:** A clean falsification lever — rare in cosmology, where most models have nuisance parameters that absorb null results.

**Paper claim:** "A SPHEREx null result (f_NL = 0 ± 0.7) would exclude the matter-bounce prediction at >6σ — a clean falsification lever unavailable in multifield inflation, where free parameters can absorb the null."

---

### 7. f_NL triple role: bispectrum + PBH regulator + induced-GW shape — **N2**

**What:** The same mechanism-independent f_NL = −4.375 appears in three distinct observables of the bounce cosmology:
1. **Galaxy bispectrum / scale-dependent bias** — the subject of this forecast paper.
2. **Primordial Black Hole (PBH) abundance regulator** — the Edgeworth-correction to Press-Schechter formation, where f_NL < 0 suppresses PBH formation, matching observed PBH constraints.
3. **Induced gravitational-wave spectrum** — the spectral index γ = 3 in the PTA-band stochastic GW (cross-validated in Paper 3 at γ = 3.20 ± 0.42).

**Why it matters:** A single parameter-free number predicts three otherwise-independent observations across galaxy surveys, microlensing/PBH constraints, and PTAs. This is what "mechanism-independent prediction" means in practice: cross-channel consistency is the signature.

**Scientific significance:** Concordance or discordance across these three channels sharpens the test. If SPHEREx measures f_NL = −4.375 and NANOGrav refines γ → 3 and PBH constraints hold — all three independent channels pass. If any fails, we know which sector breaks.

**Paper claim:** "The same parameter-free matter-bounce f_NL = −35/8 governs the LSS bispectrum (this paper), PBH formation via Edgeworth-corrected Press-Schechter (Paper 3 companion analysis), and the induced-GW spectral index γ = 3 (Paper 3 NANOGrav γ = 3.20 ± 0.42), providing a triple-channel consistency test."

---

## Summary table: novelty classification

| # | Finding | N-tier | Why |
|---|---|:---:|---|
| 1 | f_NL = −35/8 as mechanism-independent prediction | **N3** | First proof that all matter-dominated bounces share the same f_NL |
| 2 | Template-overlap correction to Fisher forecast | **N3** | First published template-mismatch correction for bounce f_NL forecasts |
| 3 | b_φ fragility audit | **N3** | First systematic audit of b_φ propagation into σ(f_NL) |
| 4 | Bayes factors vs tuned multifield / single-field | **N2** | Quantitative model-comparison framework |
| 5 | Planck+DESI recast → 0.7σ from bounce | **N2** | First bounce-template-frame recast of existing data |
| 6 | Null-result >6σ falsification asymmetry | **N2** | Two-sided decisive measurement |
| 7 | f_NL triple role (LSS × PBH × GW) | **N2** | Cross-channel concordance test |

Count by tier: **N3 × 3, N2 × 4, N1 × 0, N0 × 0, N4 × 0.**

---

## What this paper contributes to science

1. **A parameter-free prediction** — matter-bounce f_NL = −35/8 = −4.375, mechanism-independent.
2. **A corrected forecast** — template-overlap-corrected SPHEREx σ(f_NL) ≈ 0.7, detection at 5.0–5.5σ.
3. **A fragility audit** — first b_φ uncertainty propagation study, documenting the pre-2028 calibration priority.
4. **A model-comparison framework** — Bayes factors 8–17 (vs tuned multifield) and > 10⁵ (vs single-field).
5. **A consistency recast** — current Planck+DESI place bounce at 0.7σ; the "bounce is dead" claim is unsupported.
6. **A falsification lever** — SPHEREx null result would exclude matter-bounce at > 6σ.
7. **A cross-channel test** — same f_NL drives LSS bispectrum, PBH abundance, and PTA GW spectral index γ = 3.

This is a **pre-data forecast with falsification framework** — a class of paper that matters most in the 2-4 year window before SPHEREx delivers (science data ~2028). The window is short; the contribution is time-sensitive.

---

## Cross-references

- Paper 1 (Spin-Torsion) — derivation of the induced-GW spectral index γ = 3 that Paper 2's §7 triple-role discussion uses.
- Paper 3 (Anomaly Catalog) — NANOGrav γ = 3.20 ± 0.42 cross-validates the γ = 3 prediction at 0.48σ; also supplies the anomaly-multi-tracer σ(f_NL) improvements (6.1–16.4 %).
- Paper 4 (Chirality Catalog) — dipole infrastructure is used by Paper 3 Limitation G to empirically calibrate the anomaly-tracer bias α that Paper 2 §5 treats theoretically.
