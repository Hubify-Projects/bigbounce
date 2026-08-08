# EXT Review — P1B × Grok
- paper: P1B
- version: v1B.0.99
- reviewer: Grok
- model: Expert
- timestamp: 2026-07-06T19:13:08Z
- chat_url: https://grok.com/c/75ca4bd1-cdef-4708-b276-bc808e50679f
- pdf: /tmp/round_P1B.pdf

## Raw verbatim response

Thought for 49s

VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] Scope and contribution (Abstract; Sec. I Introduction, paragraphs 2–4 and scope list; Sec. VII Conclusions): The manuscript explicitly and repeatedly states that “none of the three analyses below implements or tests a torsion-modified Boltzmann/theory module, and none verifies the ECH spin-torsion sector,” that each is “an adjacent numerical cross-check,” and that “all three analyses are compatibility checks only; no analysis here constitutes evidence for or against a bounce cosmology.” This framing accurately describes the content but demonstrates that the work is a reproducibility/technical-note companion rather than a standalone advance meeting PRD’s significance threshold; it would be more appropriate as supplementary material or an appendix to Paper I(a).
[MAJOR] Linkage to ECH physics (Sec. III title and scope statement; Sec. III.A, Eq. (3) and following paragraph): The derivation that the torsion-induced four-fermion operator yields ∆N_eff^(ECH) ∼ (T/M_Pl)^2 ≈ 7×10^{-45} at BBN (and 5×10^{-58} at recombination) is order-of-magnitude correct for a dimension-6 Planck-suppressed contact interaction. However, the subsequent claim that the stock-CAMB ΛCDM+∆Neff MCMC therefore supplies a “∼40-orders-of-magnitude-conservative observational envelope on this bespoke ECH result” overstates the connection: the MCMC contains no ECH modification, tests a generic radiation extension, and is insensitive to the actual ECH prediction by construction.
[MINOR] NaMaster pipeline validation (Sec. IV, paragraphs on scope note, estimator, and robustness battery; Eq. (4); Fig. 3 caption): The 500-MC recovery, bias attribution to the unweighted χ² template fit (∼80 % of the −0.032° shift) plus BB-proxy shape, and sky-fraction/robustness battery are technically competent. The decision to carry |∆β̂| = 0.040° forward as the “observed NaMaster pipeline bias” nevertheless requires a still-more-prominent, repeated caveat in the abstract and conclusions that this is an estimator-specific figure on foreground-free synthetic skies only and supplies no bound on real-sky systematics or the β–α degeneracy.
[MINOR] Spectator-ALP consistency check (Sec. VI framing paragraph, prior-predictive Monte Carlo, and spectator-status caveat; Table IV; fn. 6): The Gaussian-summary-likelihood MCMC, prior-predictive fractions (11.6 % within 1σ at fixed C_aγ = 8), disclosure of non-minimal C_aγ ≳ 8–10 and the ∼25× misalignment tuning (θ_i ∼ 0.1) needed for Ω_a < 0.01, and the explicit statement that “the same birefringence arises in standard GR with an identical ALP” are honest. The section nevertheless remains a post-hoc accommodation of already-published Eskilt–Komatsu data rather than an ECH-derived prediction or test; no photon-torsion coupling is derived from the Holst term.
[MINOR] Reproducibility presentation (Sec. V.A and Table III; Appendix A; parameter-summary CORRECTED.json note): The GitHub repository, version-stamp commit, and artifact references are positive. Minor clarity issues remain: the exact likelihood-block YAMLs are only partially reproduced in Table III; the Planck-only chain is reported as unconverged and excluded without a consolidated convergence table for all four configurations; and the earlier off-by-one column bug in parameter_summary.json, while corrected and deleted, should be documented with the column-mapping table in the main text or a dedicated reproducibility subsection rather than solely in the repository.

The central claim—that the three exercises supply technically sound reproducibility and null-consistency checks compatible with the ECH program—is supported by the reported MCMC posteriors (∆N_eff consistent with zero within 1σ), MC pipeline-recovery biases, and ALP posterior readouts (with explicit tuning disclosures), but only at the level of generic consistency rather than ECH-specific validation.
