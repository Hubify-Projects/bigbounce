# P1B v1B.0.22 — R25a brutal-honesty-Grok verdict

**Reviewer**: Internal Claude, Grok-4.3 brutal-honesty persona (OpenRouter capped → Anthropic-rotated)
**Round**: R25a (round 1-of-3 of fresh cross-model §4.4.1 verification streak)
**Date**: 2026-05-24
**Protocol**: Read paper top-to-bottom, then for each quantitative headline cross-check on-disk chain / JSON / CSV evidence.
**Persona**: brutal stress-test — assume the 5-vendor R23 wave was too generous on framing and missed a numerical / statistical-framing flaw.

---

**1 BLOCKER / 2 MAJOR / 2 minor / 1 nit**

---

## BLOCKER

### BLK-1 — Two on-disk artifacts disagree on full-tension `total_samples`; paper headlines the LARGER of the two and the discrepancy is unreconciled in the text

**Claim location**:
- Abstract (line 103): "\textbf{309{,}789} frozen samples across two converged dataset combinations"
- Footnote `fn:sample_stratification` (lines 234–253): "\textbf{309{,}789} is the sum of the two frozen combinations ($176{,}840 + 132{,}949$ raw accepted samples)"
- Table I caption / row "Total samples": 176,840 for full-tension
- Conclusions (line 779): "\textbf{309{,}789} frozen samples across two converged dataset combinations"

**On-disk evidence**:
| Source | Reported total | Path |
|---|---|---|
| `freeze_diagnostics_CORRECTED.json` field `total_accepted_samples` | **176,840** | `reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/` |
| `full_tension_physical_parameters.json` field `total_samples` | **176,240** | `research/final_paper_prep/` |
| Raw `wc -l --` of 6 chain files (excluding `#`-prefixed header rows) | **176,240** | `frozen/full_tension_20260311_1728/chains/chain_0*/spin_torsion.1.txt` |
| Working chain dir (`paper1_clean_restart_sync/chains/dneff/full_tension/`) data-row total | **170,878** (sum 14626+14397+14270+14208+14098+99279) | `paper1_clean_restart_sync/chains/dneff/full_tension/chain_0*/spin_torsion.1.txt` |
| Sum of MCMC-step weights (col 1) over working-chain-dir accepted rows | **427,392** | same |

**Defect rationale**: The frozen-snapshot's `freeze_diagnostics_CORRECTED.json` (the file produced by the off-by-one column-mapping fix per its own `bug_fix` field) claims 176,840 accepted samples. But the row-count of the chain files in that same frozen snapshot is 176,240, and `full_tension_physical_parameters.json` — the JSON that gets read by every downstream paper-summary script — agrees at 176,240. The paper anchors its abstract, conclusion, and footnote on the **larger** number with no reconciliation of the 600-sample gap. A brutal reviewer reads this as: the headline is the bigger-feeling number, but the file that produces every parameter mean ± std in Table I (`full_tension_physical_parameters.json`) silently disagrees by 0.34%. Either (a) the 600 difference is the count of pre-burn samples that `freeze_diagnostics` includes but the row-aligned JSON drops, in which case the abstract should say "176,240 post-alignment / 176,840 raw" and explain — or (b) one of the two files is wrong. The R23 wave (5 vendors) all marked the 309,789 headline VERIFIED; none of them checked whether the two on-disk artifacts agree on the addend. This is exactly the kind of headline-vs-file discrepancy the truth-audit protocol exists to catch.

Additionally — **the working chain directory cited in CLAUDE.md as the dneff sync (`paper1_clean_restart_sync/chains/dneff/full_tension/`) contains only 170,878 data rows.** Chain 6 alone has 99,279 rows while chains 1–5 have ~14k each — a 7× imbalance which is itself a yellow flag for an MCMC where rough equality among chains is assumed in the Gelman-Rubin diagnostic. The paper's footnote `fn:rhat_csv` cites `convergence_latest.csv` (the worst-R-hat artifact) which lives at the top-level `reproducibility/cosmology/` path, not under either of the snapshot directories — so the cross-link between the headline 176,840 number and the R-hat CSV the paper cites is not actually traceable to one self-consistent on-disk artifact.

**Severity = BLOCKER**: load-bearing abstract-and-conclusion number (309,789 frozen samples) does not reconcile against the on-disk JSON used for the parameter table; this is the exact failure mode the prior 309,789-vs-309,?? bookkeeping fire (corrected fire #25) was supposed to have eliminated.

---

## MAJOR

### MAJ-1 — "14 sampled parameters" R-hat claim is not verified by the file it cites; the chain header shows ≥17 sampled parameters

**Claim location**: Table I footnote `fn:rhat_csv` (line 294): "all 14 sampled parameters (7 cosmological + 7 Planck likelihood nuisance) across both frozen combinations satisfy $\hat R - 1 < 3\times 10^{-3}$"

**On-disk evidence**:
- `convergence_latest.csv` content (lines 1–15): contains **7 cosmological parameters per dataset only** (`H0, delta_neff, omegam, ombh2, ns, tau, sigma8`); **zero nuisance parameter R-hat rows are present** for either `full_tension` or `planck_bao_sn`.
- Chain header (`spin_torsion.1.txt` line 1): sampled column list is `logA, nnu, ns, ombh2, omch2, tau, theta_MC_100` (7 cosmological) + `A_planck, amp_143, amp_217, amp_143x217, n_143, n_217, n_143x217, calTE, calEE` (**9** Planck nuisance, not 7) + `Mb` (SH0ES nuisance) → **17 sampled parameters total**, not 14.

**Defect rationale**: The paper's footnote makes two related sub-claims: (i) there are 14 sampled parameters (7 cosmo + 7 nuisance), and (ii) **all of them** satisfy $\hat R - 1 < 3\times 10^{-3}$ per `convergence_latest.csv`. Both are problematic. The chain header on disk shows nine Planck-likelihood nuisance amplitudes/indices + one SH0ES $M_B$ nuisance = ten nuisance parameters, not seven. The "14" appears to be a Paper-1A-derived legacy degree-of-freedom count carried into a chain that actually samples a wider nuisance space. More importantly, the cited CSV does **not contain R-hat rows for any nuisance parameter** — so the "all 14 satisfy $\hat R - 1 < 3\times 10^{-3}$" universal claim is at best a 7-of-14 claim (or 7-of-17 if the truthful nuisance count is used). A skeptical reviewer reads this as: the paper claims convergence on a parameter set wider than what the cited convergence file actually reports R-hat for. **This is a Bayesian/frequentist-style "consistent with" overclaim**: the file is consistent with the 7 cosmological parameters converging, not with the full sampled set.

**Severity = MAJOR**: footnote is the only convergence-evidence anchor in the paper for the Table I claim; it needs to either (a) cite a CSV that actually contains nuisance R-hat rows, (b) restate as "7 cosmological parameters" (matching what the cited file proves), or (c) recompile with a full-parameter R-hat table.

### MAJ-2 — Iter2 quintom-B "+4.3σ from LCDM" headline framing is presented as a discovery; in fact LCDM lies in joint marginal tails where the chain has no samples, so the σ value is a marginal extrapolation not a posterior probability

**Claim location**: Multiple — abstract footnote-block (line 75 comment, but ALSO live body lines 314, 343–356, 584, 706 caption, 754 cross-paper anchor); table `tab:iter2_posterior` displays "$w_0 = -0.8122 \pm 0.0436$" with the column header "vs LCDM: $+4.3\sigma$ from $-1$".

**On-disk evidence**: The paper itself (lines 358–374 "Caveats" block, R10 GEM-M1 closure) explicitly admits that "the LCDM point $(w, w_a) = (-1, 0)$ lies at $>4\sigma$ in the joint marginal tails ... and is therefore unsampled by the Metropolis-Hastings chain; any KDE-based Savage-Dickey ratio at an unsampled point yields arbitrary kernel-dependent noise". This is the iron-clad self-falsification.

**Defect rationale**: This is the classic Bayesian/frequentist conflation the persona is paid to flag. The "+4.3σ from LCDM" framing inherits its rhetorical force from frequentist hypothesis-testing intuition — readers parse it as "this chain rules out LCDM at 4.3σ confidence". But the paper's own caveat block admits that LCDM is **unsampled** by the chain: at >4σ in the joint marginal tails the MCMC has effectively zero samples, so the "4.3σ" figure is a marginal-Gaussian-approximation tail extrapolation from the chain mean and 1σ width, **not** a probability statement the chain actually supports. The honest statement is "the LCDM point lies outside the bulk of the Metropolis-Hastings sampling and the chain alone cannot give a robust Bayes factor without a nested-sampling rerun." The paper says this in the caveat but **still uses the "+4.3σ from LCDM" framing as the table headline, the abstract-comment marketing line, the iter2 physics-interpretation paragraph, the cross-paper anchor section, and the Forward section.** A skeptical reviewer reads this as: the discovery framing is in the heading and the disclaimer is buried in §V caveats. Either the σ-from-LCDM column should be removed pending the nested-sampling Bayes factor, or every appearance of "+4.3σ from LCDM" / "phantom-crossing required" should carry the inline qualifier "marginal extrapolation from MCMC bulk; LCDM unsampled by chain; not a Bayes-factor exclusion".

**Severity = MAJOR**: this is the load-bearing scientific claim of the iter2 block. The cross-paper consequence is non-trivial: Paper 1A is queued (per §VII cross-paper anchor, lines 731–767) to import "$w_0 = -0.812 \pm 0.044$ at $+4.3σ$ from LCDM, $w_a = -0.667 \pm 0.186$ at $-3.6σ$ from LCDM, phantom-crossing required" into its Table II $\ddagger$ rows. If P1B propagates the "+4.3σ from LCDM" framing into P1A without the inline unsampled-tail qualifier, the discovery overclaim metastasizes. The fix is to either (a) wait for the nested-sampling rerun (queued v1B.0.15+ but apparently slipped — paper is still v1B.0.22 without nested ln B) before publishing the σ-from-LCDM column, or (b) replace "+4.3σ from LCDM" everywhere with a marginal-tail statement like "$w_0$ posterior median departs from $-1$ by $4.3\,\sigma_{w_0}$ in the marginal" and explicitly disclaim Bayesian interpretation each time.

---

## minor

### MIN-1 — Table I footnote `fn:rhat_csv` says full-tension worst R-1 is $9.74\times 10^{-4}$ at $n_s$; the cited CSV says worst R-1 in full-tension is $9.74\times 10^{-4}$ at `ns` — **but** `tau` is essentially tied at $9.50\times 10^{-4}$, and in `planck_bao_sn` the worst is `delta_neff` at $9.71\times 10^{-4}$, not just "ns"

**Claim location**: Table I, footnote `fn:rhat_csv` line 294.

**On-disk evidence**: `convergence_latest.csv` rows 2–8 (full_tension): worst at `ns` = 0.000974, `tau` = 0.00095 (tied within sampling noise); rows 9–15 (planck_bao_sn): worst at `delta_neff` = 0.000971. Per-dataset worst-R rows differ.

**Defect rationale**: minor cleanup — the footnote attributes the worst R-1 to a single row but the actual worst varies between the two combinations. Easy fix: footnote should say "worst row varies by combination: $n_s$ in full-tension (R-1 = $9.74\times 10^{-4}$), $\Delta\Neff$ in Planck+BAO+SN (R-1 = $9.71\times 10^{-4}$)".

### MIN-2 — "Both frozen datasets find ... $H_0$ consistent with Planck $\Lambda$CDM at $0.3\sigma$" is a "consistent with" used as a discriminator

**Claim location**: Line 439 — "Both frozen datasets find $\Delta\Neff$ consistent with zero and $H_0$ consistent with Planck $\Lambda$CDM at $0.3\sigma$, confirming that the $\Delta\Neff$ extension alone does not resolve the Hubble tension."

**Defect rationale**: minor framing — "consistent with X at 0.3σ" + "confirming Y does not resolve" reads like a discriminator (the test confirmed something) when the actual logical content is null (the test produced no signal in either direction). The honest version: "The posteriors return $H_0$ near Planck $\Lambda$CDM and $\Delta\Neff$ near zero; the data therefore neither prefer nor reject the $\Delta\Neff$ extension, leaving the Hubble tension unresolved by this configuration." The current wording is internally inconsistent with the §III "neither posterior preference nor exclusion" framing the paper itself adopts elsewhere — there it's called null, here it's "confirming". Pick one.

---

## nit

### NIT-1 — Cross-paper table `tab:crosspaper` rows are stale: P1(b) row reads "v1B.0.13 67%" while the paper version on the title page is v1B.0.22; P1(a) reads v1A.0.27 / 74% while CLAUDE.md headline shows v1A.0.35 / 95%; P3 row reads v3.1.45 / 85% while current is v3.1.62 / 95%; P4 v1.0.103 / 95% while current is v1.0.128 / 95%

**Claim location**: Table `tab:crosspaper` lines 685–693.

**Defect rationale**: nit only — the cross-paper status table is the kind of thing that drifts every cron fire. Self-pointing rows in particular ("P1(b) v1B.0.13 67%" inside a v1B.0.22 paper) are an own-goal for a brutal reviewer. Easy bulk sync; doesn't affect any scientific claim.

---

## Summary

**1 BLOCKER / 2 MAJOR / 2 minor / 1 nit**

The R23 5-vendor wave was indeed too generous on **statistical framing**, exactly as the brutal-honesty persona was sent to find:
- **BLK-1** is a numerical-headline inconsistency two file artifacts disagree on, that none of the prior 5-vendor reviewers traced into the JSON tree.
- **MAJ-1** is the classic "all parameters satisfy R-hat" overclaim against a CSV that only contains a 7-parameter subset.
- **MAJ-2** is the load-bearing iter2 "+4.3σ from LCDM" framing presented as discovery while the paper's own caveat block admits LCDM is unsampled by the chain — Bayesian/frequentist conflation, exactly the defect class the persona is paid to flag.

Streak status: round 1-of-3 returns findings; AGENT_RULES §4.4.1 cascaded-loop-exit NOT satisfied yet. Round 2 (different persona) and round 3 (different persona) needed before the v1B.0.22 → v1B.0.23+ closure cycle.

— Internal Claude / Grok-4.3 persona, 2026-05-24
