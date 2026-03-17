# Final Verdict

**Date:** 2026-03-16

---

## 1. What from Paper 1 is still alive

Three things survive from Paper 1:

**A. The observed cosmic birefringence consistency.** The ECH parity-odd coupling scale (alpha/M ~ 10^{-21} GeV^{-1}) requires f_photon ~ 1.7 (O(1)) for consistency with the 3.9-sigma combined Planck + ACT DR6 birefringence measurement. This is a genuine positive result: the framework's natural scale is compatible with data without fine-tuning. The open question is whether f_photon can be computed from first principles.

**B. The MCMC pipeline.** The Cobaya + CAMB infrastructure (configs, chains, RunPod deployment, monitoring scripts) is a reusable asset for any cosmological model testing. It is not ECH-specific.

**C. The ECH theoretical framework.** The action, reduced action, four-fermion structure, modified Friedmann equation, and perturbation equations are all mathematically correct. The framework is a valid starting point for any future work on ECH gravity, even if the dark energy and bounce programs are closed.

Everything else from Paper 1 -- the H0 tension reduction, the S8 tension reduction, the dark-energy origin claim, the galaxy spin connection, the observable GW spectrum -- is dead or requires such heavy reframing that the original claim is unrecognizable.

---

## 2. What from Paper 1.2 / Branches A-P is dead

**All direct routes from spin-torsion geometry to dark energy are dead.** Seven structural barriers (A-G) close four minimal routes and three extended foundations. The barriers are:
- Mass-coupling lock
- Topological-shift duality
- Scalar-tensor universality
- Planck suppression
- Scale separation
- Attractor-sensitivity dilemma
- Parameter immunity

**All distinctive bounce observables are dead.** Seven additional barriers (H, J, K, L, M, N, O, P) close:
- Tensor spectrum: P_T ~ 10^{-64} (undetectable)
- Tensor chirality: Delta-chi = 0 exactly
- Scalar transfer: T(k) = 1 (transparent)
- Non-Gaussianity: f_NL ~ 10^{-56} (undetectable)
- State selection: Liouville's theorem prevents it
- UV-IR bridge: specificity dilemma
- GW background: 10^{17} gap at all frequencies
- Baryogenesis/relics: gravitational democracy
- Hidden-sector vacuum: bounce-vacuum decoupling
- Torsion relic: Z2 parity protection

**The PGT lower-scale bounce is dead as a source of observable consequences.** The mass-coupling lock, vacuum amplification ceiling, and Z2 parity protection collectively close all channels.

**The tension reduction claims are dead.** The independent MCMC verification shows Delta-Neff consistent with zero. The apparent H0 and S8 reductions were artifacts of including SH0ES and DES priors in the fit.

---

## 3. Does the project have a plausible positive path?

**Yes, but it is narrow.**

The one surviving positive path is: compute the one-loop photon-torsion vertex in ECH gravity and determine whether it gives a first-principles prediction for cosmic birefringence.

This path is plausible because:
- The observed birefringence is real (3.9 sigma, two independent experiments)
- The ECH coupling scale is naturally compatible (f_photon ~ O(1) required)
- The calculation is well-defined (one-loop QFT in curved spacetime with torsion)
- The result is testable (LiteBIRD, CMB-S4)

This path is narrow because:
- The vertex might vanish at one loop (the most likely outcome, given Branch G v1)
- Even if nonzero, the prediction might be indistinguishable from a generic ALP
- Route S1 already noted the absence of photon coupling in the minimal model

The expected value is still positive because the closure paper exists as a guaranteed output regardless of the vertex result.

---

## 4. Single best next program

**Hybrid: finalize and submit the closure paper (Paper 1.2) while simultaneously computing the photon-torsion vertex.**

- Paper 1.2 is submitted within 2-3 weeks (near-certain publication)
- The vertex calculation takes 1-3 weeks in parallel
- If the vertex is nonzero and O(1): write and submit a short letter (PRL/JCAP Letters) with the birefringence prediction
- If the vertex is zero: add it as Barrier 15 to Paper 1.2 and submit the enhanced closure

This maximizes expected output (1.4-1.5 papers) while minimizing risk (the closure paper hedges the vertex calculation).

---

## 5. Theory vs data vs hybrid

**Theory-first, then data comparison.**

The immediate next step is a theoretical calculation (one-loop vertex), not a data analysis. The MCMC pipeline is not needed now. No new data products are needed. The Track C scripts and consistency window are already in place for the data comparison step, which happens only if the vertex is nonzero.

If the vertex succeeds, the follow-up is a data comparison: use the predicted f_photon to compute beta and compare with current and future birefringence measurements. This is a simple forward model (already implemented in Track C scripts), not a full MCMC.

If the vertex fails, no data analysis is needed. Submit the closure paper.

---

## 6. Whether MCMC is needed now

**No.**

The existing MCMC chains (300,000+ samples, R-1 < 0.005) are sufficient for the closure paper. No new cosmological parameter estimation is needed. The birefringence program, if it proceeds, uses a Gaussian forward model (Track C scripts), not MCMC. Updated MCMC with DESI DR2 or other new datasets is not justified because:

- Delta-Neff is consistent with zero in all existing dataset combinations
- The ECH framework provides no mechanism to predict a specific Delta-Neff value
- Running Lambda-CDM + Delta-Neff with updated data is routine parameter estimation that any group can do and many already have

The RunPod infrastructure should remain available but inactive. It can be reactivated if a future calculation produces a specific prediction that requires MCMC testing.

---

## Summary

| Question | Answer |
|----------|--------|
| What is alive from Paper 1? | Birefringence consistency, MCMC pipeline, ECH framework |
| What is dead from A-P? | All DE derivation routes, all distinctive bounce observables, tension reduction claims |
| Positive path exists? | Yes, narrow: photon-torsion vertex calculation |
| Single best program? | Hybrid: closure paper + vertex calculation |
| Theory/data/hybrid? | Theory-first (vertex), then data comparison if positive |
| MCMC needed now? | No |
