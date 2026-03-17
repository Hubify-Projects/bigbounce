# Positive Program Candidates: Ranked Assessment

**Date:** 2026-03-16

---

## Candidate A: Phenomenological ECH Dark Energy (Paper 1 Ansatz)

**Description:** Reframe the ECH scaling ansatz as a generic effective model. Update MCMC with DESI DR2, Planck PR4. Fit Lambda-CDM + Delta-Neff + possibly w0-wa.

**Existing repo support:**
- Cobaya configs (4 dataset combinations), RunPod deployment scripts
- 300,000+ existing chain samples as baseline
- Paper 1 manuscript with full methodology

**New ingredient needed:**
- Updated likelihoods (DESI DR2, possibly Planck PR4 if available)
- Honest reframing: the model is Lambda-CDM + Delta-Neff, not "ECH dark energy"
- Possibly w0-wa extension (motivated by DESI preference for dynamical DE)

**First decisive test:** Run Lambda-CDM + Delta-Neff with DESI DR2 BAO. If Delta-Neff is still consistent with zero AND the DESI dynamical-DE preference persists, the ECH motivation adds nothing -- the model is just standard Lambda-CDM with an unused extra parameter.

**Biggest risk:** The model IS Lambda-CDM + Delta-Neff. There is nothing ECH-specific about it. The "geometric" framing is window dressing. The MCMC verification already showed this. Updating the data does not fix the conceptual problem.

**Theory vs data:** Pure data fitting exercise. No theory content.

**Verdict: WEAK.** This is not a research program; it is routine parameter estimation on a standard extension. Hundreds of groups do this. There is no competitive advantage from the ECH framing.

---

## Candidate B: Parity/CMB Birefringence Observational Program

**Description:** Develop the cosmic birefringence connection. Compute the photon-torsion vertex (f_photon) from the ECH one-loop effective action. Make a genuine prediction for beta. Compare with LiteBIRD, CMB-S4.

**Existing repo support:**
- Track C scripts: consistency_window.py, gaussian_posterior.py, eb_shape_comparison.py
- 6 publication-quality figures
- Literature registry with current measurements (beta = 0.242 +/- 0.061 deg)
- Model-to-observable map with explicit equation chain and gap identification
- Combined Planck + ACT DR6 constraint

**New ingredient needed:**
- ONE CALCULATION: the one-loop photon-torsion vertex in ECH gravity. This determines f_photon from first principles. If f_photon comes out O(1), the framework makes a genuine prediction.
- This calculation is well-defined: integrate out torsion + fermion loops with an external photon leg. The technology exists (heat kernel methods, documented in Vassilevich 2003 and Shapiro & Teixeira 2014).

**First decisive test:** Compute f_photon at one loop. If it is zero (no vertex), the program is dead. If it is O(1), the framework predicts beta ~ 0.2-0.4 deg. If it is very small or very large, the consistency window closes.

**Biggest risk:** The photon-torsion vertex might vanish at one loop due to gauge invariance or the algebraic structure of the Holst term. The minimal coupling does not include a direct A-mu-torsion term, so the vertex must be generated radiatively.

**Theory vs data:** Theory-first (one calculation), then data comparison. This is the right structure for a physics program.

**Verdict: STRONG.** This is the best candidate. Real data exists (3.9 sigma). A specific, tractable calculation (one-loop vertex) determines whether the program lives or dies. The existing infrastructure directly supports it. LiteBIRD (launch ~2028) and CMB-S4 will reach sigma(beta) ~ 0.01 deg, making this a decisive near-term test.

---

## Candidate C: Galaxy Spin Chirality Observational Program

**Description:** Build a real galaxy spin classification pipeline with SDSS/Galaxy Zoo data. Measure the dipole asymmetry. Compare with the parity-odd tidal torque model.

**Existing repo support:**
- wp5 Monte Carlo sensitivity (epsilon_PO posterior)
- Parity bias model (ttt_baseline.py, parity_bias_model.py)
- CNN architecture (ResNet-18, needs fix + real data)
- Dataset builder (build_galaxy_spin_dataset.py)

**New ingredient needed:**
- Real galaxy images from SDSS DR17 or Galaxy Zoo DECaLS (minimum 50,000)
- Fix the RandomHorizontalFlip bug in the CNN training pipeline
- Independent verification of Shamir (2024) dipole claims (controversial in the literature)
- Statistical framework for dipole detection with systematic error control

**First decisive test:** Reproduce the Shamir A0 ~ 0.003 dipole with an independent pipeline on Galaxy Zoo DECaLS data. If the dipole is not reproduced, the entire observational basis evaporates.

**Biggest risk:** Shamir's results are controversial. Multiple groups have found null results. The signal may be a systematic artifact of the CNN classification (mirror-image asymmetry in training data, telescope-specific PSF effects). The ECH framework provides no prediction for epsilon_PO, so even a confirmed dipole would not test the theory.

**Theory vs data:** Pure data/pipeline engineering. No ECH-specific theory content.

**Verdict: MEDIUM-WEAK.** The observational question (does a galaxy spin dipole exist?) is real and interesting. But it is an observational astronomy project, not a theoretical physics program. The ECH connection is cosmetic. The Shamir results are controversial and may not survive independent replication. High effort, uncertain payoff, and no theory advancement.

---

## Candidate D: Comprehensive Negative Result Paper (No-Go Catalog)

**Description:** Publish the 14-barrier no-go catalog as a standalone paper or as Paper 1.2. This is the "closure document" -- a comprehensive assessment of why the spin-torsion bounce cannot produce observable consequences.

**Existing repo support:**
- Paper 1.2 manuscript (2053 lines, nearly complete)
- All branch directories with detailed derivations
- 14 barriers documented across 10 branches
- Structural lessons (DR1-DR5, Lesson 6)

**New ingredient needed:**
- Final integration of Branches N, O, P results (may already be done)
- Possibly one more pass on exposition and bibliography
- Comparison with related recent literature (Liu et al. 2025, Legner et al. 2025, Fabbri 2025)

**First decisive test:** Not applicable -- this is a write-up of completed work.

**Biggest risk:** Negative result papers are harder to publish. However, the scope (14 barriers, 10 branches, covering all perturbation channels, DE derivation routes, and early-universe mechanisms) is unprecedented for this topic. PRD publishes comprehensive negative results when they are thorough and close a question definitively.

**Theory vs data:** Pure theory.

**Verdict: STRONG.** This has the highest certainty of producing a publishable output. The work is done. The question is framing and submission strategy, not research. Can be pursued in parallel with any positive program.

---

## Candidate E: ECH-Inspired Modified Gravity Phenomenology

**Description:** Strip the bounce connection entirely. Treat the ECH effective action as a modified gravity model with parity-violating structure. Constrain its parameters from CMB, GW, and structure formation data. Compare with Chern-Simons gravity, dynamical Chern-Simons, and generic ALP models.

**Existing repo support:**
- ECH action and reduced action derivations
- Four-fermion coupling structure (Paper 1.2 Secs. 2-3)
- Birefringence consistency window (Track C)

**New ingredient needed:**
- Systematic comparison with Chern-Simons gravity (which IS a competitive, well-studied alternative)
- Clear statement of what ECH adds beyond generic parity-violating gravity
- Possibly Boltzmann code modifications (CAMB/CLASS) for parity-violating perturbation theory

**First decisive test:** Can the ECH effective action be distinguished from Chern-Simons gravity or a generic ALP at the level of CMB/GW observables? Route S1 already showed the answer is NO for birefringence. The question is whether other observables fare better.

**Biggest risk:** Route S1 already established that the ECH parity phenomenology is identical to generic ALP phenomenology once f_photon is a free parameter. Without the bounce connection, ECH is just one more modified gravity model in a crowded field. The specific structural lessons (algebraic torsion, fixed Immirzi = no IR fingerprint) argue AGAINST distinctive ECH phenomenology.

**Theory vs data:** Phenomenology (effective theory approach).

**Verdict: WEAK.** The structural lessons from the no-go program themselves argue that ECH phenomenology reduces to generic scalar-tensor or ALP phenomenology on FRW backgrounds. Pursuing this would be knowingly entering a field where the framework has no competitive advantage.

---

## Candidate F: Hybrid -- Birefringence Vertex + Closure Paper

**Description:** Combine Candidates B and D. Publish Paper 1.2 as the comprehensive closure. Simultaneously compute the photon-torsion vertex as the "single surviving open question" identified by the closure. If the vertex calculation succeeds, publish a short follow-up paper with the birefringence prediction.

**Existing repo support:** All of B and D combined.

**New ingredient needed:** Only the one-loop vertex calculation.

**First decisive test:** The vertex calculation.

**Biggest risk:** The vertex vanishes, leaving only the closure paper (which is still publishable).

**Verdict: STRONGEST.** This combines the highest-certainty output (closure paper) with the highest-potential positive result (birefringence prediction). The closure paper is ready now. The vertex calculation is a well-defined next move. If the vertex works, you have two papers. If it fails, you have one paper plus a clean additional no-go result (Barrier 15: no radiative photon-torsion vertex).

---

## Ranking

| Rank | Candidate | Verdict | Certainty | Upside |
|------|-----------|---------|-----------|--------|
| 1 | F: Hybrid (birefringence + closure) | STRONGEST | HIGH | TWO papers |
| 2 | B: Birefringence vertex calculation | STRONG | MEDIUM | Genuine prediction |
| 3 | D: Closure paper alone | STRONG | VERY HIGH | One solid paper |
| 4 | C: Galaxy spin pipeline | MEDIUM-WEAK | LOW | Data product |
| 5 | A: Updated MCMC | WEAK | HIGH | Routine result |
| 6 | E: Modified gravity phenomenology | WEAK | MEDIUM | Crowded field |
