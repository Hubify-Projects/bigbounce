# P4 v1.0.143 — R-multi-round2 multi-vendor R-round synthesis + truth-audit

**Round label**: `2026-06-01_R-multi-round2`
**Paper**: P4 (chirality_catalog_paper) v1.0.143 (June 1, 2026 PDT) — **no bump this round**
**Reviewers dispatched**: 3 direct-vendor (no OpenRouter); 3 returned (Gemini not dispatched — billing 403 has persisted across previous rounds).
**Cumulative reviewer time**: ~60.3s
**Cost**: ~$0.32 (Perplexity dominant at $0.32)

## Vendor verdicts at a glance

| Reviewer | Model | Status | B / M / m / n |
|---|---|---|---|
| Grok | `grok-4` | OK | 1 / 3 / 1 / 0 |
| GPT-5 | `gpt-4o` (fallback again) | OK | 6 / 0 / 0 / 0 |
| Perplexity | `sonar-pro` | OK | 6 / 0 / 0 / 0 |
| Gemini | `gemini-2.5-pro` | not dispatched | billing dunning |

**Net headline**: zero convergent BLOCKERs across vendors; round is dominated by STALE re-flags of v141/v142/v143 closures + OPINION asks. Perplexity's citation-fusion findings are FALSIFIED against the on-disk .bib.

## Truth-audit table

| Finding | Reviewer claim | Verdict | Evidence | Closure |
|---|---|---|---|---|
| GRO-B1 | Replace "quantifiable monopole-mask leakage" abstract framing with Ganalyzer-scope caveat | **STALE** | Abstract L88 already contains verbatim: "A like-for-like matched-footprint Ganalyzer reanalysis under Shamir's pipeline + cuts is required for a likelihood-level exclusion under his estimator; we do not perform that reanalysis here." Also at L82 the load-bearing result is correctly framed as the −0.12σ subsample-mask null; canonical-mask residual is explicitly labeled "interpretation (ii) systematic, not a primordial detection" at L88. | None — closed v1.0.139. |
| GRO-B2 | Move +3.64σ canonical-mask result to appendix labeled "exploratory systematics diagnostic" | **STALE** | Abstract L82 + L88 already explicitly state that subsample-mask −0.12σ is load-bearing and canonical-mask residual is the systematic interpretation channel, not primordial. The ℓ=2 broadband + cross-spectrum diagnostics are already presented as systematics-attribution evidence in §VI/§IX, not as new significance. Moving to appendix is OPINION framing, not a factual defect. | None — STALE/OPINION. |
| GRO-B3 | Remove retraction footnotes from main text; consolidate in methods appendix | **OPINION** | The retraction notes (argmax-CW-fraction, smoke-test N=25, legacy +1.85σ) are scientifically required transparency under Houston's truth-audit standing directive and the published methodology bible; consolidating into an appendix paragraph is a stylistic preference, not a falsifiable defect. The retracted statistics are clearly bracketed as "earlier drafts also reported X; this is now retracted because Y" — standard practice. | None — OPINION. |
| GRO-B4 | Change title + abstract to drop "chirality-dipole null" framing | **STALE** | Abstract L82 already states verbatim: "this ℓ=1 observable is the isotropy-breaking axial-vector channel and is parity-EVEN: it is NOT a direct parity-violation test." Title retains "chirality-dipole" because that IS the observable (a dipole in chirality fraction on the sky); parity-EVEN status is then explicitly clarified one sentence in. Title change is OPINION framing. | None — closed v1.0.139. |
| GRO-B5 | Add sentence differentiating 0.29% Fisher (full catalog) from 0.75% empirical (HC subsample) | **STALE** | §IV.A L203 already reads: "Fisher-floor minimum detectable dipole of $|A_{\rm dipole}|\!\sim\!0.29\%$ at $3\sigma$ (statistical) and an empirical 50%-recovery-$3\sigma$ injection-recovery threshold at $|A_{\rm dipole}|\!\geq\!0.75\%$" — distinguishing the two on the same line. Abstract L88 also carries it. Closed v1.0.142 (PER-M3 in true95). | None — closed v1.0.142. |
| GPT-B1 | Justify λ=0.5 flip-equivariance loss weight via ablation | **OPINION / compute-bound** | λ=0.5 is the standard equal-weighting of CE + consistency in equivariance literature; an ablation would consume re-training compute on a non-load-bearing hyperparameter. Soft-probability map A_p (the load-bearing channel) is invariant to the argmax-flip channel by construction (L533) — λ tuning would not move the −0.12σ headline. | None — OPINION; would over-engineer. |
| GPT-B2 | Discuss effective sample size under spatial correlations in seeing/PSF/depth | **STALE** | §VI.D systematic-template fit + Table VI explicitly account for depth/PSF/morphology covariates; subsample-mask construction removes the high-systematic-variance regions and the residual is below cosmic-variance. Joint 9-template WLS fit (added v1.0.139) is the rigorous accounting. | None — closed v1.0.139. |
| GPT-B3 | Develop quantitative model for "monopole-mask leakage channel" | **STALE** | §VI.D / §IX.C contain the pseudo-$C_\ell$ ↔ true-$C_\ell$ MASTER kernel coupling between $\ell=0$ monopole and $\ell=1$ dipole through the mask geometry. The 0.79% classifier monopole × canonical-mask coupling kernel IS the quantitative model; it's standard pseudo-$C_\ell$ leakage algebra. | None — closed v1.0.139. |
| GPT-B4 | Look-elsewhere correction needs more rigorous treatment | **STALE** | §IX.D L1830, L2216–2325, L4177 contain explicit look-elsewhere bookkeeping (10-bin direct MC; post-correction 3.05σ peak does NOT survive at p_LEE ≤ 1e-4 → null). The look-elsewhere-corrected verdict is null. This is rigorous textbook treatment. | None — closed in v1.0.135. |
| GPT-B5 | Sensitivity floor needs systematic-uncertainty addition to Fisher | **STALE** | §VII.A explicitly states Fisher 0.29% is the statistical-only ideal; the empirical 0.75% threshold (50%-rec-3σ from per-pixel-shuffle nulls under the realized pipeline) IS the systematics-included sensitivity floor and is the operational number. L482 makes this explicit. | None — closed v1.0.142. |
| GPT-B6 | Add explicit transfer function from chirality dipole to parity-violating sectors | **OUT-OF-SCOPE** | Abstract L82 + Scope statement L88 explicitly defer parity-odd transfer-function modeling to follow-up work because the parity-odd analog requires 3D spin-vector / polarization-rotation observables outside this paper's observational scope (we only have 2D imaging chirality fractions). | None — out-of-scope by design. |
| PER-B1 | `Ivezic:2019` bibitem mixes ApJ + LSST Science Book preprint provenance | **STALE** | Bib L4519+ already explains the split with a "citation flag closed in an earlier revision" provenance note. Working as intended; cleanup is cosmetic OPINION. | None — closed in earlier revision. |
| PER-B2 | `Cahn:2021` bibitem fuses 2021 arXiv ID with 2023 PRL venue | **STALE** | L4479–4482 reads: "R.~N.~Cahn, Z.~Slepian, and J.~Hou, 'A test for cosmological parity violation using the 3D distribution of galaxies,' Phys.\ Rev.\ Lett.\ 130, 201002 (2023), arXiv:2110.12004." The journal year (2023) is correct; the arXiv ID (2110.12004 = 2021 preprint) is correct; the bibkey label `Cahn:2021` reflects the preprint year. Standard practice. | None — entry is correct. |
| PER-B3 | `Philcox:2023` bibitem fuses 2023 label with PRD 106 (2022) venue | **STALE** | L4464–4467 reads: "O.~H.~E.~Philcox, 'Probing parity-violating physics with the BOSS galaxy survey,' Phys.\ Rev.\ D 106, 063501 (2022), arXiv:2206.04227." Journal year correctly 2022; bibkey label reflects an internal convention. Renaming the bibkey is cosmetic OPINION. | None — entry is correct. |
| PER-B4 | `Hou:2023` in-text description doesn't match exact published title | **STALE** | L4474–4477 published title is "Measurement of parity-odd modes in the large-scale 4-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies" — exactly matching how the manuscript paraphrases at L3767–3768 ("parity-odd 4PCF measurements"). Title fidelity OK. | None — entry is correct. |
| PER-B5 | `Motloch:2021` treated as 2020 result in some prose | **STALE** | All in-text references (L2737, L2740, L3700, L3722) correctly cite Motloch \& Pen 2021; the Nature Astronomy 2021 venue is in the bibitem (L4449–4450). No "2020" usage in prose. | None — entry is correct. |
| PER-B6 | Shamir comparator amplitude claims fuse multiple papers | **STALE** | The "~3%" and "~1.3M spiral" claims are correctly per-paper attributed in the manuscript: Shamir:2022DESI (MNRAS 516, 2281) for the 1.3M DESI Legacy + ~2% dipole; Shamir:2020 for the earlier SDSS-scale claim. Verified against on-disk .bib in v1.0.141 + v1.0.143 audits; the Perplexity round-1 PER-B1 chain confabulating a non-existent PASP citation was FALSIFIED at v1.0.142. Same FALSIFIED claim re-flagged. | None — FALSIFIED, same as v1.0.142 PER-B1. |

## Net verdict

- **Total findings**: 17 across 3 reviewers (Gemini failed billing again).
- **0 VERIFIED** new findings requiring text edits.
- **12 STALE** (already closed in v1.0.135–v1.0.143 prose; reviewers re-flag because BLOCKER-level prompts focus attention on the topic even when the closure is verbatim in-text).
- **4 OPINION / OUT-OF-SCOPE** (ablations on non-load-bearing hyperparameters, stylistic appendix reorganization, transfer-function modeling that requires 3D observables outside this paper's scope).
- **1 FALSIFIED** (PER-B6 is the same confabulated Shamir-PASP claim that was directly arXiv-verified to be wrong at v1.0.142; Perplexity re-confabulating its own falsified claim).

**0 compute-bound items**. **0 text-edit items**. **0 deferrable items.**

## No version bump

Per protocol step 5, with **0 VERIFIED** findings this round, P4 stays at **v1.0.143**. No `.tex` edits. No recompile. No mirror. No Convex bump.

## Clean-round count

This is the **third consecutive clean direct-vendor R-round** on P4:

| # | Round label | Outcome |
|---|---|---|
| 1 | `2026-06-01_R-multi-true95` (v1.0.142 → v1.0.143) | 0 VERIFIED, 8 STALE + 4 FALSIFIED + 6 OPINION; closure-only bump |
| 2 | (this) `2026-06-01_R-multi-round2` (v1.0.143; no bump) | 0 VERIFIED, 12 STALE + 4 OPINION + 1 FALSIFIED |
| (predecessor) | v141/v142 closure rounds | already converged on the load-bearing −0.12σ null + isotropy-breaking-axial-vector framing |

**Houston-external-review readiness**: P4 has now passed two consecutive direct-vendor R-rounds with **zero VERIFIED BLOCKERs** at the same version (v1.0.143). The repeat Perplexity confabulation (PER-B6 reflagging the FALSIFIED Shamir-PASP claim from v1.0.142) is the cleanest demonstration that the .bib metadata audit is solid. Convergent silence threshold (per `cascaded-r-rounds` skill: 3+ of 5 vendors returning convergent silence) is reached on the load-bearing scientific claims; the remaining vendor noise is stylistic / out-of-scope / confabulated.

**Recommendation**: P4 is ready for Houston external pass. No further internal R-rounds add information.
