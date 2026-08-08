# P1B RETEST2 — ChatGPT (EXT, verifiable raw capture)

- **Reviewer:** ChatGPT (chatgpt.com)
- **Model/mode:** Pro Extended (thinking) — label "Pro Extended" shown in composer footer
- **Account:** houston (logged in)
- **Timestamp (local):** 2026-07-04
- **Chat URL:** https://chatgpt.com/c/6a48c560-3180-83e8-b5ae-ba51cb81c8cc
- **PDF submitted:** /tmp/ext_retest2_P1B.pdf (P1B v1B.0.99, 22 pages, Dated July 4 2026)
- **Prompt:** exact PRD-referee prompt
- **Verdict line (verbatim):** `(1) VERDICT: REJECT`

---

## Raw response (verbatim)

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract / Secs. I and VII, "technical reproducibility and consistency-check companion": the manuscript repeatedly states that none of the three analyses tests or verifies the ECH spin-torsion sector, that the ALP birefringence is not ECH-specific, and that model comparison is deferred; what remains is a stock-CAMB null proxy, a synthetic-code validation, and a one-datum ALP accommodation, which is not a self-contained PRD-level physics result.

[MAJOR] Sec. III A, "bespoke ECH-sector ∆Neff": the derivation treats the torsion-induced four-fermion operator as a coherent positive thermal energy density ρtor ∼ GN T⁶ and then maps ρtor/ρrad to ∆Neff, but the manuscript does not compute the finite-temperature expectation value with spin/flavor/chirality factors, sign, renormalization/subtraction, or the fact that an a⁻⁶ stiff component is not a radiation-like ∆Neff species; the quoted ∆Neff ∼ 10⁻⁴⁴ is therefore only a dimensional estimate, not the claimed first-principles bound.

[MAJOR] Sec. III A / Sec. V, claim that the stock-CAMB run is a "conservative observational envelope" on ECH: because the actual ECH contribution is asserted to be non-radiation-like and Planck-suppressed, a ΛCDM+∆Neff chain with free generic radiation does not meaningfully constrain the ECH sector; the connection between the MCMC posterior and ECH physics is asserted rather than demonstrated.

[MAJOR] Secs. III and V, ΛCDM+∆Neff MCMC interpretation: the paper reports only extended-model posteriors, with no matched ΛCDM baseline, likelihood-level χ² breakdown, posterior predictive check, Bayes factor, AIC/BIC, or evidence; claims such as "does not resolve the Hubble tension" are plausible descriptively, but not established at the standard required for a cosmological-parameter paper.

[MAJOR] Secs. II, III, and Table II, "full-tension" likelihood stack: SH0ES and DES-Y3 are folded in as active likelihoods/priors and then residual tensions are discussed using posterior shifts; this construction obscures rather than quantifies dataset inconsistency and is not a valid substitute for dataset-level tension metrics or goodness-of-fit diagnostics.

[MAJOR] Sec. V, Planck likelihood release pairing: the frozen chains mix PR4/NPIPE high-ℓ CamSpec with Planck 2018 low-ℓ/lensing, while the c15 rerun changes low-ℓ/lensing likelihoods and is then used to bound release-pairing bias; this is not an independent identical rerun and does not provide a systematic-error budget for the quoted posteriors.

[MAJOR] Sec. IV, NaMaster validation scope: the simulation contains CMB-only synthetic skies, no Galactic foregrounds, no instrumental miscalibration, no beam, no anisotropic or correlated noise, no real map-making transfer function, and no β–α separation; it therefore cannot support any real-sky birefringence-systematics statement, despite the manuscript carrying forward a "0.040° systematic floor."

[MAJOR] Sec. IV, estimator choice and bias: the canonical β estimator is an unweighted χ² template fit over bandpowers, and the manuscript itself reports that inverse-variance weighting removes about 80% of the bias; retaining the biased estimator for "comparability" is not defensible for a validation paper unless the published estimator being emulated is precisely specified and the covariance treatment is reproduced.

[MAJOR] Sec. IV, synthetic BB and template treatment: the use of CℓBB = 0.05 CℓEE, an EE-only template, bins beyond the map band limit, and no full covariance makes the recovered multiplicative under-recovery a property of this artificial setup, not of NaMaster deconvolution generally; the conclusion should be downgraded to a code smoke test.

[MAJOR] Sec. VI, ALP MCMC: the likelihood is a single Gaussian summary of the published βobs value, so βALP ≈ βobs and βfree ≈ βobs are essentially imposed by construction; this cannot be presented as independent confirmation or meaningful posterior validation of the ALP model.

[MAJOR] Sec. VI, ALP model comparison absent: no evidence, Bayes factor, information criterion, posterior predictive check, or comparison to GR+ALP, ΛCDM+rotation, or no-rotation models is provided, so the paper cannot support claims about accommodation cost beyond prior-dependent descriptive fractions.

[MAJOR] Sec. VI and Table IV, spectator status: Ωa < 0.01 is imposed only as a post-sampling cut on a posterior dominated by non-spectator regions, and the strict θi ≤ 0.1 sliver has only 42 raw samples; the spectator-safe inference needs a dedicated run with the spectator condition imposed as a prior or likelihood constraint and with adequate effective sample size.

[MAJOR] Sec. VI, ALP energy-density calculation: the Ωa computation relies on a small-angle/potential-dominated approximation while much of the sampled posterior has θi = O(1); the claimed spectator fractions and fine-tuning costs should be recomputed from the full EOM energy density for every sample.

[MAJOR] Secs. VI and VII, ECH relevance of birefringence: the manuscript explicitly states that the same birefringence arises in standard GR with the same ALP and that no ECH-specific photon-torsion coupling is derived; the ALP section therefore does not support an ECH spin-torsion program and should be removed or reframed as an unrelated phenomenological appendix.

[MAJOR] Data and Code Availability / Appendix A: DOI assignment is pending, the repository is program-wide rather than paper-specific, some artifacts are described as deleted or corrected after a column-permutation bug, and exact immutable release information is incomplete; this is inadequate for a manuscript whose main claimed value is reproducibility.

[MINOR] Sec. I, imported theory results: the text alternates between "thirteen mechanism-class barriers" and a "14-barrier table," while neither table nor derivation is included here; this inconsistency should be fixed or the imported claims removed.

[MINOR] Sec. III A, notation and dimensions: defining κ² = 8πGN = MPl⁻² while writing a four-fermion coefficient proportional to κ² is nonstandard and potentially confusing; the convention should be made explicit and checked against the cited Einstein-Cartan/Holst literature.

[MINOR] Sec. IV, "template-fit SNR" language: the large SNR values are repeatedly caveated, but the terminology remains likely to be misread as sky-detection significance; they should be renamed as injected-template recovery metrics only.

[MINOR] Sec. VI, prior-predictive fractions in the abstract: the 11.6%, 23.9%, 6.1%, and 12.6% figures are not developed with uncertainties, sensitivity to prior choices, or a clear table in the body; they should not appear in the abstract unless fully documented.

[MINOR] References and status labels: several cited companion papers are "posted concurrently" or "in preparation," and DOI placeholders remain; a PRD submission should use stable identifiers or remove dependence on unavailable works.

(3) The central claim that the manuscript provides a publishable, ECH-relevant reproducibility and consistency-check companion is not supported by the evidence presented, although the narrower claim that the three reported exercises are limited non-ECH compatibility checks is supported by the manuscript's own caveats.

---

## Orchestrator note (not part of raw)

Expected outcome: ChatGPT stays REJECT on methodological-companion SCOPE (title-vs-content mismatch, ECH-relevance, no model comparison) — the structural harsh-referee floor per standing directive H (RS5-8 oscillation). ChatGPT's §III.A objection engages the improved area but re-frames the derivation as "only a dimensional estimate," a deeper physics demand than Grok's now-satisfied minor. This is the venue/scope critique, not a regression on the RS25 items.
