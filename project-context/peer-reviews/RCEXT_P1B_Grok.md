# RCEXT P1B Grok — chat: https://grok.com/c/cf97118d-6bc1-4c2a-977b-c2901bf88794
VERDICT: MINOR REVISIONS

---

Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program (P1B)

Recommendation: MINOR REVISIONS

This is a solid, technically careful companion paper whose core value lies in its explicit scoping, reproducibility documentation, and refusal to overclaim. It provides three self-contained verification analyses (stock-CAMB ΔN_eff proxy, NaMaster MC pipeline validation on synthetic skies, and spectator-ALP consistency check) that contextualize the structural no-go results of the concurrently submitted Paper I(a). All quantitative claims are appropriately caveated as compatibility checks only; model-preference statistics (Bayes factors, ΔAIC/BIC, nested-sampling evidence) are explicitly deferred. No fatal flaws, uncontrolled systematics that invalidate the stated conclusions, or internal numerical contradictions were identified. The paper meets the technical standard for PRD/JCAP/MNRAS but requires modest polishing for clarity, narrative framing, and prior motivation to reach the highest tier.

BLOCKERS

None.

MAJORS (presentation/narrative framing that affects readability and perceived strength at top-journal level)

Justification of the "natural parameter box" for the ALP scan (Sec. VI and Appendix C): The scan range m/H_0 ∈ [1, 3], θ_i ∈ [0.5, 2] is repeatedly described as the "natural-parameter box" or "scan-prior envelope," yet the physical motivation for these specific bounds is light. The posterior-supported fixed-C_aγ = 8 solution shifts to median m ≃ 36 H_0 (well outside the box) with required C_aγ ≳ 8–10 (outside minimal KSVZ/DFSZ benchmarks) and a ~25× misalignment tuning (θ_i ~ 0.1) to satisfy the spectator-safe Ω_a < 0.01 cut (only 13% of posterior mass). This is reported honestly, but the box itself needs stronger a-priori justification (e.g., why m ~ few × H_0 is theoretically privileged for a birefringence-capable spectator ALP with f_a ~ M_Pl, or reference to UV-completion or misalignment priors that would naturally populate this window). Without it, the "accommodates but near the edge / requires tuning" verdict reads as post-hoc rather than as a controlled exploration of a motivated prior volume. This is the single largest presentational weakness.

Narrative integration with the ECH program (Introduction and Conclusions): The paper correctly positions itself as the "technical verification layer" for Paper I(a)'s 13-barrier structural closure and perturbation-transparency theorem. However, the link remains somewhat loose: the three analyses are standard (or standard + heuristic f_a ~ M_Pl motivation) tools whose results are consistent with the scoping but do not directly test ECH-specific dynamics (explicitly stated for the ΔN_eff proxy and ALP birefringence). A short, explicit paragraph early in the Introduction (or a boxed "Role of this companion within the ECH program" statement) would clarify how these particular checks were chosen to support/contextualize the no-go (e.g., "we verify that the obvious phenomenological proxies and consistency tests do not resurrect closed channels or produce unaccounted signatures"). This would prevent the impression that the companion is mostly "standard checks we ran anyway."

MINORS (clarity, readability, and minor robustness points)

Heavy caveat density and visual hierarchy: The abstract, Sec. IV scope note, and ALP subsection are exemplary in their explicit limitations ("MC pipeline-recovery figures, not sky-measurement systematics"; "not a distinctive ECH prediction"; "spectator-safe verdict rests on the broader Ω_a < 0.01 subset (13% mass), not the extreme θ_i ≤ 0.1 sliver"). However, the density of footnotes and parenthetical qualifications makes it easy for a skimming reader to miss the load-bearing numbers or to misread the NaMaster SNR = 20.32 / 25.71 figures as sky significances despite the warnings. Consider a short "Key limitations at a glance" box near the end of the Introduction or a clearer visual separation (e.g., italicized or boxed scope statements) in Sec. IV and VI.

NaMaster robustness battery attribution (Sec. IV): The battery cleanly pins the ~12% multiplicative under-recovery primarily to the unweighted χ² template fit (equal weighting of noise-dominated high-ℓ bins) with a secondary contribution from the proxy C_ℓ^BB = 0.05 C_ℓ^EE shape. This is good, but the paper could briefly note whether published Planck/ACT analyses use the same unweighted estimator or an inverse-variance-weighted variant (the latter reduces bias to –0.006° in the battery). This would help readers assess how directly the reported 0.032°–0.040° floor propagates to real-sky results.

ALP Ω_a computation and prior dependence (Sec. VI and dedicated subsection): The Ω_a definition, onset-of-oscillations solver, and potential-dominated approximation (verified against full EOM) are clearly documented. The 44%/13% mass fractions for Ω_a < 0.1 / 0.01 are correctly flagged as prior-dependent (flat θ_i). A one-sentence reminder that the spectator-sliver mass would drop further under a cos θ_i-flat (vacuum-manifold-uniform) prior is already present; keep it.

Minor editorial/readability items:
- Some long compound sentences in Sec. III (physics interpretation of w_0wa) and Sec. VI (ALP caveats) could be split for flow.
- The SN-overlap systematic (caveat (e)) is stated repeatedly and correctly; a short dedicated "Systematic uncertainty from SN catalog overlap" paragraph or table footnote would reduce repetition.
- Table II footnote (a) on overlap-narrowed widths is excellent; ensure it is cross-referenced from the abstract-level w_0wa discussion if any summary numbers migrate there.
- Reproducibility appendix is exemplary (honest "what is committed vs. regenerable," pending Zenodo/Hugging Face DOIs are normal at submission stage).

STRENGTHS (at least three, listed without ranking)

Exemplary intellectual honesty and scoping discipline: Every major claim is immediately qualified with what it does not demonstrate (ΔN_eff proxy is not a spin-torsion Boltzmann test; NaMaster recovery is not a sky detection; ALP birefringence is not an ECH-specific prediction and requires documented tuning). This is rare and valuable in a field where bounce vs. ΛCDM interpretations can be overstated. The "compatibility check only; model-preference deferred" framing is maintained consistently from abstract through conclusions.

Strong reproducibility and diagnostics culture: 309k+ frozen samples with explicit burn-in/ESS/R̂ tables, independent c15 release-pairing re-run (0.04σ agreement on ΔN_eff), full robustness battery for NaMaster bias sources, committed chains + YAMLs + scripts, and honest disclosure of what must be regenerated locally. Appendix A and the Hugging Face dataset plan set a high standard.

Clear separation of the three analyses and their distinct limitations: The paper never blurs the MC pipeline-validation SNR figures with published sky significances, never presents the ALP posterior shift to m ≫ H_0 as a "natural" success, and correctly notes that the same birefringence arises in standard GR. The spectator-status caveat (main-text disclosure of ~25× misalignment tuning, Ω_a < 0.01 subset at 13% mass) is load-bearing and properly foregrounded.

Technical depth without hidden assumptions: NaMaster configuration (apodization, binning, unweighted estimator choice justified by public-script comparability), ALP EOM integration + Runge–Kutta cross-check, Ω_a derivation with anharmonic-correction estimate, and MB–H_0 joint-posterior offset check are all executed and documented at a level that allows independent reproduction and auditing.

Overall Assessment

This companion does exactly what a technical verification paper should: it stress-tests the obvious phenomenological channels that could have weakened the structural no-go of Paper I(a) and reports that the data remain compatible with the scoping (ΔN_eff consistent with zero; pipeline recovers injected signals with characterized bias; ALP accommodates the birefringence signal but only with documented tuning and outside minimal benchmarks). The science is sound. The revisions requested above are matters of motivation, narrative signposting, and visual clarity that will make the paper's already-high integrity more immediately accessible to readers and referees. With those addressed, the paper should be suitable for publication in PRD/JCAP (or MNRAS with appropriate cosmology scope). I am happy to re-review a revised version focused on the two MAJOR points.
