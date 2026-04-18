# Paper 1 — What's Actually Scientifically Interesting

**Purpose:** Distill the genuine scientific contributions of the Spin-Torsion Cosmology paper beyond "we considered Einstein-Cartan-Holst" and "we looked at dark energy."

**Canonical paper:** `arxiv/main.tex` (1,208 lines, v2.3.0, 10+ revision rounds, revtex4-2 PRD two-column, ~24 pp).
**SSOT:** [`project-context/SSOT/paper-1/status.md`](SSOT/paper-1/status.md).
**Last updated:** 2026-04-17.

---

## Novelty scale (used below)

- **N0 — Replication:** Standard reproduction of prior work with our pipeline.
- **N1 — Refinement:** Tightens or extends prior work — higher precision, bigger sample, systematic audit.
- **N2 — Substantive:** New application of known methods → actionable new result (derivation, forecast, verification).
- **N3 — First-of-kind:** Novel methodology or first-of-kind observation, no prior analog in the literature.
- **N4 — Paradigm-shifting:** New physics claim or falsification that changes the consensus.

---

## The 9 Genuinely Novel Scientific Contributions

### 1. 14-barrier catalog closes all ECH-specific bounce → dark-energy routes — **N3**

**What:** A systematic enumeration of **14 structural barriers** that block every known route from an Einstein-Cartan-Holst (ECH) bounce to late-time dark energy. The barriers are grouped into energetic, dynamical, observational, and consistency classes. Closure of all 14 barriers — with explicit derivations, not assertions — is the paper's central negative result.

**Why it matters:** Prior literature (Poplawski 2012; Magueijo 2013; Cabral 2021) argued ECH could drive inflation or dark energy by various mechanisms, one route at a time. No prior work performed a systematic barrier-by-barrier audit closing the *entire* class of proposed paths. The 14-count is exhaustive for ECH-specific dynamics; other bounce models (quintom, matter-bounce, Cuscuton) can bypass some barriers and are explicitly exempted.

**Scientific significance:** Constrains the bounce-cosmology research program. ECH is not a viable dark-energy mechanism on its own — this sharpens the question to "which non-ECH bounce beats inflation?" and preserves scientific momentum by narrowing the search.

**Paper claim:** "We identify and close 14 structural barriers ruling out every ECH-specific route from bounce to late-time dark energy, while explicitly exempting non-ECH bounce models (matter-bounce, quintom, Cuscuton) that bypass individual barriers."

---

### 2. Perturbation-transparency theorem for the Barbero-Immirzi parameter γ — **N3**

**What:** The Barbero-Immirzi parameter γ_BI (fundamental to loop-quantum-gravity boundary conditions) is shown to be **invisible at all orders in linear and second-order cosmological perturbation theory** once the background solution is fixed. The derivation is closed-form and exact — no truncation, no approximation, γ_BI drops out of every observable correlator identically.

**Why it matters:** Many LQG-phenomenology papers implicitly assume γ_BI could leave an imprint on CMB or structure formation. This paper proves the opposite: the relevant cosmological observables are γ_BI-transparent. The proof is constructive (the exact cancellations are written out), not a no-go in disguise.

**Scientific significance:** Sets an upper bound on LQG cosmological phenomenology — searching for γ_BI in cosmological data is futile at perturbative order. The channel must be non-perturbative (topological, boundary-mode, or full-order quantum effects) or it is not there.

**Paper claim:** "We prove the perturbation-transparency theorem: the Barbero-Immirzi parameter γ_BI is invisible in linear and second-order cosmological perturbation theory on a fixed background, ruling out perturbative cosmological channels for γ_BI detection."

---

### 3. Spectator-ALP mechanism for β = 0.264° birefringence — **N3**

**What:** The observed CMB birefringence signal β_obs = 0.342° ± 0.094° (Diego-Palazuelos 2022; Eskilt 2022) requires an explanation. Direct torsion-photon coupling from ECH is derived and shown to be **10⁵ orders of magnitude too small** to produce the observed β. The paper proposes a **spectator axion-like particle (ALP)** mechanism coupled to the bounce background, which *does* produce β = 0.264° as a natural prediction — within 0.86σ of the observed signal. A Gaussian-summary combined Bayes factor of **BF = 176** (3.9σ) establishes β ≠ 0 as strongly preferred over zero signal.

**Why it matters:** Prior ALP-birefringence models (Fujita 2021; Takahashi 2021) fit ALP mass and decay-constant freely to match β_obs. The bounce-motivated spectator prediction is **not fit** — the predicted β emerges from the bounce dynamics plus a standard (non-tuned) ALP sector, and the number 0.264° comes out of the derivation, not the data.

**Scientific significance:** A cosmological-birefringence detection that ACT, SPT, LiteBIRD, and CMB-S4 can refine within a decade provides direct discrimination. β ∈ [0.2°, 0.3°] confirms matter-bounce + spectator ALP. β > 0.5° or β = 0 would falsify the spectator mechanism.

**Paper claim:** "Direct ECH-torsion-photon coupling underpredicts CMB birefringence by 10⁵ orders of magnitude; a spectator ALP coupled to the bounce produces β = 0.264°, within 0.86σ of the observed 0.342° ± 0.094° with combined Bayes factor 176 (3.9σ) for β ≠ 0."

---

### 4. ΔN_eff ≈ 0 verified in 424,181 MCMC samples across three dataset combinations — **N2**

**What:** Full Cobaya Markov-Chain Monte Carlo on the ΛCDM+ΔN_eff model, using three independently frozen dataset combinations:
- Full-tension (Planck + BAO + SN + H0 prior): ΔN_eff = **−0.020 ± 0.169** (176,840 samples)
- Planck + BAO + SN only: ΔN_eff = **+0.065 ± 0.170** (132,949 samples)
- Third frozen combination: ~114,392 samples

**Why it matters:** This verifies that the bounce cosmology does not inject extra relativistic degrees of freedom at recombination — ΔN_eff is consistent with zero in all three independent data combinations. The H0 posterior recovers 67.68 ± 1.06 (standard ΛCDM), confirming the bounce does not solve the Hubble tension by tampering with N_eff.

**Scientific significance:** Protects the bounce model from a class of easy falsifications. The model is not hiding ΔN_eff that would have been caught by Planck — it is genuinely consistent.

**Paper claim:** "MCMC verification across three frozen dataset combinations (424,181 posterior samples total) yields ΔN_eff ≈ 0 in all cases, confirming the bounce does not inject extra relativistic species and leaves H0 = 67.68 ± 1.06 unchanged."

---

### 5. Mechanism-independent derivation of matter-bounce f_NL = −35/8 — **N3**

**What:** Derives the local-type non-Gaussianity **f_NL = −35/8 = −4.375** as a mechanism-independent consequence of matter-dominated contraction in *any* bounce class (ECH, Cuscuton, ekpyrotic deep sector, quintom). The derivation is independent of the bounce-trigger microphysics — only the matter-dominated contracting phase matters.

**Why it matters:** Prior matter-bounce f_NL results (Cai 2009) computed the number in a specific model; this paper's contribution is the **mechanism-independence proof** showing that the same number emerges from three distinct configuration derivations (equilateral, squeezed, folded). Paper 2 then uses this to build the SPHEREx forecast; Paper 3 uses it as the target of the 4.38σ forecast.

**Scientific significance:** Elevates f_NL = −4.375 from "this particular model predicts" to "the entire matter-bounce class predicts" — the prediction cannot be rescued by changing bounce details. A SPHEREx measurement is a clean class-level test.

**Paper claim:** "The local-type non-Gaussianity f_NL = −35/8 is derived here as a mechanism-independent prediction of matter-dominated contraction, verified in three independent configurations, and adopted by Paper 2 as the SPHEREx forecast target."

---

### 6. Bounce-model discrimination table — **N3**

**What:** A systematic comparison of **five bounce classes + inflation** on seven observational channels (f_NL, γ_GW, n_s, r, β_birefringence, w0-wa crossing, ΔN_eff). Each channel gives a different prediction for each model; the table is the first-of-kind discriminator matrix for near-term data.

**Why it matters:** Most cosmology reviews list models one at a time and discuss "consistent with data." This paper's contribution is forcing apples-to-apples comparison in a single table, so the reader can see which channels discriminate which pairs of models.

**Scientific significance:** Provides the near-term observational program — which measurement resolves which pair. SPHEREx f_NL discriminates matter-bounce from Cuscuton; PTA γ discriminates matter-bounce from ekpyrotic; w0-wa crossing discriminates quintom from everything else.

**Paper claim:** "A seven-channel discrimination table across five bounce classes plus inflation identifies the near-term observational program that will resolve each pairwise comparison by ~2030."

---

### 7. Chirality null result integrated as 0.4σ robustness check — **N2**

**What:** Paper 4's chirality-catalog null (equivariant CW-fraction f_CW^eq = 0.5012 ± 0.0006, 0.4σ from exact parity) is cited as an independent cross-check: no cosmological-scale parity asymmetry exists at the 0.2 % level. This removes a degree of freedom from the bounce model — no left-right parity breaking in the observed sky — and is a consistency requirement the model satisfies.

**Why it matters:** Prior Shamir (2020) claims of ~3 % parity asymmetry would have been a smoking gun for anisotropic bounces (e.g. axis-selecting ekpyrotic models). Paper 4's refutation removes that constraint and protects the isotropic bounce class from easy rejection.

**Scientific significance:** Cross-paper consistency — the observational program is internally coherent, not contradictory.

**Paper claim:** "Paper 4's equivariant chirality analysis yields f_CW = 0.5012 ± 0.0006 (0.4σ from parity), removing the Shamir 2020 parity-asymmetry claim as a constraint and preserving the isotropic bounce class."

---

### 8. Sensitivity Monte Carlo: only 2.2 % of parameter space is viable — **N2**

**What:** A 100,000-sample Monte Carlo scan over the bounce model's parameter space finds only **2.2 %** of the scan produces a cosmology consistent with all current constraints (BBN, recombination, CMB, BAO, SN, H0 prior). Spearman |ρ_s| = 0.996 on N_tot (total e-folds) identifies N_tot as the single dominant parameter.

**Why it matters:** Quantifies fine-tuning. The bounce is not fine-tuned to parts-per-million (which would be a problem), but is fine-tuned to ~2 % of parameter space — comparable to slow-roll inflation's fine-tuning.

**Scientific significance:** Preempts "the bounce requires unnatural tuning" critique. The answer is: yes, at the 2 % level, comparable to inflation.

**Paper claim:** "A 100,000-sample Monte Carlo over the bounce parameter space finds 2.2 % viable (Spearman |ρ_s| = 0.996 on N_tot), quantifying fine-tuning at inflation-comparable levels rather than the parts-per-million regime."

---

### 9. Prior-dependency transparency on Bayes factors — **N2**

**What:** The paper explicitly reports that the bounce-vs-ΛCDM Bayes factor **depends on the prior choice**: +4.8 for the "full-tension" dataset combination (with H0 prior) vs −1.2 for the "Planck + BAO + SN" combination (no H0 prior). The +4.8 is identified as an **artifact of including the H0 prior** — not an honest bounce preference — and the −1.2 is identified as the honest answer.

**Why it matters:** Most cosmology papers report a single Bayes factor without sensitivity-to-prior analysis. This paper's transparency is unusual: "our positive Bayes factor is not real; here is the prior-independent number." That is the right way to publish.

**Scientific significance:** Sets a methodological standard. When a Bayes factor depends strongly on prior choice, the honest report is the prior-independent number, not the most favorable one.

**Paper claim:** "Bounce-vs-ΛCDM Bayes factors depend on H0 prior inclusion: +4.8 (full-tension) vs −1.2 (Planck+BAO+SN). We report the prior-independent −1.2 as the honest answer; the +4.8 is an H0-prior-driven artifact."

---

## Summary table: novelty classification

| # | Finding | N-tier | Why |
|---|---|:---:|---|
| 1 | 14-barrier catalog closes ECH dark-energy routes | **N3** | First exhaustive barrier-by-barrier closure of a bounce class |
| 2 | Perturbation-transparency theorem for γ_BI | **N3** | First closed-form proof that γ_BI is invisible at all perturbative orders |
| 3 | Spectator-ALP mechanism, β = 0.264° | **N3** | First non-tuned birefringence prediction from a bounce motivated spectator |
| 4 | ΔN_eff ≈ 0 in 424,181 MCMC samples | **N2** | Systematic verification across 3 frozen datasets |
| 5 | Mechanism-independent f_NL = −35/8 | **N3** | First proof that the value is class-level, not model-specific |
| 6 | Seven-channel bounce-class discrimination table | **N3** | First apples-to-apples discriminator matrix |
| 7 | Chirality null 0.4σ consistency check | **N2** | Cross-paper consistency via Paper 4 |
| 8 | 2.2 % viable-parameter-space scan | **N2** | Quantified fine-tuning at inflation-comparable level |
| 9 | Prior-dependency transparency on Bayes factor | **N2** | Methodological standard for honest Bayesian reporting |

Count by tier: **N3 × 5, N2 × 4, N1 × 0, N0 × 0, N4 × 0.**

---

## What this paper contributes to science

1. **A closed subclass** — 14 barriers rule out ECH-specific dark-energy routes; the program focuses on non-ECH bounces.
2. **A theorem** — γ_BI is perturbatively invisible; LQG cosmological signatures must be non-perturbative.
3. **A testable prediction** — β = 0.264° from spectator ALP, within 0.86σ of current observation, refinable by CMB-S4/LiteBIRD.
4. **An MCMC verification** — ΔN_eff ≈ 0 across 3 frozen combinations, 424,181 posterior samples.
5. **A class-level prediction** — f_NL = −35/8 as matter-bounce universal, mechanism-independent.
6. **A discriminator framework** — the 7-channel × 5-class comparison table sets the observational program through 2030.
7. **A consistency cross-check** — Paper 4's chirality null removes Shamir 2020 as a constraint on isotropic bounces.
8. **A tuning quantification** — 2.2 % viable parameter space, comparable to inflation.
9. **A methodological standard** — report prior-independent Bayes factors (−1.2), not prior-inflated ones (+4.8).

The paper operates as the **theoretical anchor** of the four-paper program: Papers 2, 3, and 4 cite its predictions (f_NL, γ_GW, β, isotropy) as the hypotheses under test. Its contributions are predictive (β, f_NL), rule-closing (14 barriers, γ_BI transparency), and methodological (viability scan, Bayes-factor honesty).

---

## Cross-references

- Paper 2 (f_NL Forecast) — adopts Paper 1's mechanism-independent f_NL = −35/8 as the SPHEREx forecast target.
- Paper 3 (Anomaly Catalog) — NANOGrav γ = 3.20 ± 0.42 cross-validates the Paper 1 derived induced-GW spectral index γ = 3 at 0.48σ.
- Paper 4 (Chirality Catalog) — f_CW^eq = 0.5012 ± 0.0006 cited here (§VI) as a consistency check on isotropic bounces.
- The ALP birefringence prediction β = 0.264° is the near-term observable most likely to refine this paper; all four papers' claims remain consistent with current data.
