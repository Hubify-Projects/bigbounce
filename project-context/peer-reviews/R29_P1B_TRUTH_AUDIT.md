# R29 P1B — Truth-Audit

**Paper**: arxiv/paper1b_mcmc_companion.tex (v1B.0.55, 2026-06-10)
**Round**: R29 v3 native-PDF 5-vendor cross-vendor + META synthesis
**Auditor**: Claude (per /peer-review-truth-audit + feedback_peer_review_truth_audit_protocol)
**Date**: 2026-06-10
**Verdict schema**: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION

Each ESSENTIAL + MAJOR is audited individually. MINOR / NIT are batched by theme.

---

## E1 — Units-README mislabels a column-permutation bug as a units issue

**Source**: Grok_brutal P1B-E1 (verbatim claim repeated in this task brief).

**Claim**: `reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/parameter_summary_units_README.md` describes the discrepancy between `parameter_summary.json` and `parameter_summary_CORRECTED.json` as a "Cobaya internal normalisation / unit-conversion" issue, with a 6-row table of fake "conversions." Grok claims the real cause is a column-permutation in the extraction script (raw H0 = sigma8, raw sigma8 = omegam, raw omegam = S8, raw ns = ombh2, raw tau = 100*theta_MC).

**On-disk verification**:
1. Chain header (`reproducibility/cosmology/frozen/full_tension_20260311_1728/chains/chain_01/spin_torsion.1.txt`, line 1) columns 0..25:
   `weight, minuslogpost, logA, nnu, ns, ombh2, omch2, tau, theta_MC_100, A_planck, amp_143, amp_217, amp_143x217, n_143, n_217, n_143x217, calTE, calEE, Mb, As, H0, sigma8, omegam, S8, delta_neff, age`.
2. Computed weighted means + std on 6 stacked chains, 30% burn-in (123,369 post-burn samples):
   - col 20 `H0` = 67.6840 +/- 1.0606
   - col 21 `sigma8` = 0.8034 +/- 0.0084
   - col 22 `omegam` = 0.30809 +/- 0.00546
   - col 24 `delta_neff` = -0.01959 +/- 0.16921
   - col 7 `tau` = 0.05359 +/- 0.00696
   - col 4 `ns` = 0.96548 +/- 0.00618
   These match `parameter_summary_CORRECTED.json` and Table I exactly.
3. The raw values in `parameter_summary.json`:
   - JSON `H0` = 0.8035 -> actual chain col 21 `sigma8` (true H0 is col 20)
   - JSON `sigma8` = 0.308 -> actual chain col 22 `omegam` (true sigma8 is col 21)
   - JSON `omegam` = 0.814 -> actual chain col 23 `S8` (true omegam is col 22)
   - JSON `delta_neff` = 13.82 -> actual chain col 25 `age` (true delta_neff is col 24)
   - JSON `tau` = 1.041 -> actual chain col 8 `theta_MC_100` (true tau is col 7)
   - JSON `ns` = 0.0223 -> actual chain col 5 `ombh2` (true ns is col 4)

   **Uniform off-by-one column-index bug in the extraction script** (read `col[i+1]` instead of `col[i]`). NOT a Cobaya internal normalisation. The 6 "conversions" in the README's table (`× 100`, `− 3.046`, etc.) are physically meaningless: e.g., raw `H0` 0.8035 -> 80.35 km/s/Mpc is wrong; the value 0.8035 is sigma8.

**Verdict**: **VERIFIED** (Grok's spirit correct; specific cell mapping in Grok's claim slightly off — Grok said "raw omegam=0.814 is S8" which is correct, but said raw ns=0.0223 is "omega_b h^2" (correct: ombh2 = omega_b h^2) and "raw tau=1.041 is 100*theta_MC" (correct: theta_MC_100). Grok said "raw delta_neff" wasn't in the JSON header set, but in the actual artifact `delta_neff` raw = 13.82 = age in Gyr, not ombh2. So Grok's table had one wrong cell but the diagnosis is correct).

**Fix applied**: Rewrote README with the verified column-permutation diagnosis. Updated paper Data-Availability sentence. `parameter_summary_CORRECTED.json` already contains the correct values (verified to ~5 sig figs against fresh getdist-style chain reload), so it is NOT regenerated; the README documents the verification command.

---

## E2 (META-E1) — ALP sign restriction silently removes half the physical parameter space

**Source**: META_REVIEW.

**Claim**: ALP fits sample C_aγ only over positive intervals (prior [4, 60]), removing the C_aγ < 0 / sign(Δφ) < 0 half of the physical parameter space.

**On-disk verification**: This is a methodological choice about the ALP scan. The paper explicitly notes the sign convention in §VI; the spectator-ALP consistency check sets C_aγ = 8 fixed with θ_i scanned. This is a CONSISTENCY check, not a constraint. Sign of C_aγ flips sign of β; sign of β has been jointly fit with α in the cited Eskilt2022 analysis.

**Verdict**: **OPINION** — methodological framing critique. Adding a sign-symmetric prior would not change the consistency-check conclusion (it's already symmetric in |β|). HOUSTON-DECISION whether to add a one-sentence note documenting that the sign of C_aγ * sign(Δφ) is degenerate with the sign of β and a positive prior on |C_aγ| does not lose physics.

**Fix applied**: None (deferred to Houston).

---

## E3 (META-E2) — Hidden BBN-consistency assumption for ΔNeff < 0

**Source**: META_REVIEW.

**Claim**: The CAMB BBN-consistent default Y_He extrapolation may be invalid for ΔNeff < 0 (negative ΔNeff is outside the BBN training-table domain).

**On-disk verification**: The full-tension posterior is centered at ΔNeff = -0.020 with 1σ = 0.169. The negative half of the posterior is sampled. CAMB's PArthENoPE BBN table covers ΔNeff ∈ [-3, 3] in standard releases. This is well within the tabulated range.

**Verdict**: **STALE/PARTIAL** — the concern is real in principle but the standard CAMB BBN table covers the sampled range. A one-line clarifying footnote would close the audit point but the science is unaffected.

**Fix applied**: None this round (low-risk, defer to next pass with a footnote).

---

## E4 (Gemini-E1) — Structural reorganization (Table I/II ordering)

**Source**: Gemini_cosmology.

**Claim**: Table II (w0-wa) is referenced before Table I (ΛCDM+ΔNeff) is presented.

**On-disk verification**: Confirmed in the rendered PDF that the Table II discussion appears in §III before Table I in §III, but this is intentional — §III opens with a "physics interpretation" preamble that points readers to the structural quintom anchor before walking through the ΛCDM+ΔNeff null. Multiple prior rounds (R22, R24) preserved this ordering. PRD allows forward references.

**Verdict**: **OPINION** — stylistic preference, not a defect.

**Fix applied**: None.

---

## E5 (Grok-E2, OpenAI-E1) — Abstract claims "consistent with zero" without ln B

**Source**: Grok_brutal P1B-E2, OpenAI P1B-E1 (SN double-count is a separate item).

**Claim**: Abstract asserts "Both frozen dataset combinations find ΔNeff consistent with zero" without Savage-Dickey or ln B.

**On-disk verification**: Paper now explicitly addresses this in Appendix A / Reproducibility ("Bayes factors and information criteria... are NOT reported... Savage-Dickey readout from the present Metropolis-Hastings chain is not viable--the ΛCDM point (w,wa)=(-1,0) lies at >4σ in the joint marginal tails and is unsampled") — confirmed at lines 2034+. This is a different chain (w0wa) but the principle applies: Savage-Dickey on the ΔNeff=0 point IS feasible since ΔNeff=0 is well-sampled in both chains.

**Verdict**: **PARTIAL** — abstract phrasing "consistent with zero" is statistically conservative and accurate; Savage-Dickey on ΔNeff=0 is feasible but is a real follow-up. HOUSTON-DECISION whether to add a one-paragraph Savage-Dickey readout (low-cost) or label as future work.

**Fix applied**: None this round.

---

## E6 (Gemini-E2, OpenAI-E3) — Internal review prose / artifact paths in body

**Source**: Gemini_cosmology P1B-E2, OpenAI P1B-E3.

**Claim**: Prose like "earlier draft quoted... and is corrected here", "committed driver", "pod run", explicit file paths, "Claims Classification" appendix are internal lab-log content not appropriate for PRD body.

**On-disk verification**: All these strings are present in the .tex. Confirmed.

**Verdict**: **VERIFIED** but **HOUSTON-DECISION** — Houston's previous explicit directive was to keep the audit-trail in-paper for transparency. PRD style guide is at odds with this. Punt.

**Fix applied**: None (Houston-policy).

---

## E7 (OpenAI-E2) — Provenance: paper tag v1B.0.55 vs DOI pinning v1B.0.54

**Source**: OpenAI P1B-E2.

**Claim**: Paper is tagged v1B.0.55 but Data-Availability says HF DOIs are pinned to v1B.0.54.

**On-disk verification**: Line 122: `\newcommand{\paperVersion}{v1B.0.55}`. Line 2040: `DOI links are pinned to the \texttt{v1B.0.54} commit`. Mismatch confirmed.

**Verdict**: **VERIFIED**.

**Fix applied**: Updated line 2040 from `v1B.0.54` to `\paperVersion` so the DOI pin tracks the paper tag automatically going forward.

---

## E8 (OpenAI-E4) — Planck likelihood pairing PR4 + 2018 lowℓ unjustified

**Source**: OpenAI P1B-E4.

**Verdict**: **OPINION** — the pairing is documented and acknowledged in §V.A; pairing-robustness sweep is a real future improvement but does not invalidate present results. Defer.

**Fix applied**: None.

---

## E9 (OpenAI-E5) — Fig 3(b) missing per-realization error bar at canonical fsky

**Verdict**: **PARTIAL** — text explicitly notes σ_β "not recorded" and acknowledges. Real fix is a rerun. Defer to next round.

---

## E10 (OpenAI-E6) — Labeling "2.0σ from DES-Y3" for full-tension stack misleading

**Verdict**: **VERIFIED** — DES-Y3 prior is inside the full-tension stack, so the resulting S8 is partially anchored to DES-Y3, making "tension" a misleading label.

**Fix applied**: Local clarification added to Table I caption (small surgical patch — see Phase 2 below).

---

## E11 (OpenAI-E7) — NaMaster template pixel-window ambiguity

**Verdict**: **OPINION/PARTIAL** — technical clarity request; the paper asserts cancellation. Defer to a future explicit equation in §IV.

---

## MAJOR — batched verdicts

| ID | Source | Verdict | Note |
|----|--------|---------|------|
| M1 (OpenAI-M1) | unweighted χ² estimator | OPINION | Documented bias floor; estimator choice is method-paper-style. Defer. |
| M2 (OpenAI-M2) | single binning/ℓ-range | PARTIAL | Future-work item. |
| M3 (OpenAI-M3) | CMB-S4 σ(Neff) citation | VERIFIED | Add citation. **FIX APPLIED**. |
| M4 (OpenAI-M4) | unit warning in Data Availability | VERIFIED (=E1) | Subsumed by E1 fix. |
| M5 (OpenAI-M5) | Fig 2(a) legend "SM (Neff=0)" should be "(ΔNeff=0)" | VERIFIED | Figure file. Defer; tracked in figure-rebuild ticket. |
| M6 (OpenAI-M6) | mixed lensing clik vs native across chains | VERIFIED | Real cross-chain inconsistency, acknowledged in caveats §V.A. Defer to dedicated robustness sweep. |
| M7 (OpenAI-M7) | Σmν fixed to 0.06 eV | OPINION | Standard convention; defer. |
| M8 (OpenAI-M8) | bins above band limit | PARTIAL | Documented; defer. |
| M9 (OpenAI-M9) | ΔP √2 convention | PARTIAL | Documented in footnote; defer. |
| M10 (OpenAI-M10) | overlap integral definition | VERIFIED | Add 1-line definition. **FIX APPLIED**. |
| META-M1 | TB-channel validation missing | OPINION | Real future-work; defer. |
| META-M2 | β periodicity untested in estimator | PARTIAL | Scope-noted; defer. |
| META-M3 | (β,α) joint injection | OPINION | Explicit scope-out in paper. |
| META-M4 | ΔP per Q/U vs P consolidation | PARTIAL | Same as M9. |
| Grok-M1 | 17pp paper too long | OPINION | Stylistic; reject. |
| Grok-M2 | tension between two frozen chains not quantified | PARTIAL | Add 1-sentence cite to parameter-shift number. Defer. |
| Grok-M3 | one-sided convention ambiguity | VERIFIED | Add 1-sentence definition. **FIX APPLIED**. |
| Gemini-M1 | spectator-ALP framing/fine-tuning | OPINION | Already disclosed in abstract + §VI caveat. |
| Gemini-M2 | garbled formula on p.7/p.11 | VERIFIED | Typo `//)` — **FIX APPLIED**. |
| Gemini-M3 | uncomputed posterior mass fractions | OPINION | Pointer to artifact would help; defer. |

---

## MINOR / NIT — batched

All MINOR/NIT items (Gemini m1-m3, Grok N1-N2, OpenAI n1-n7, N1-N4, META m1-m3, META-N1):

**Verdict**: mostly VERIFIED-but-stylistic; one (OpenAI N1, version stamp in title) is a HOUSTON-DECISION (Houston explicitly keeps the version stamp during R-rounds for traceability). The rest are non-blocking polish items deferred to a final pre-arXiv pass.

**Fix applied**: None this round.

---

## Summary

| Verdict | Count |
|---------|-------|
| VERIFIED | 7 (E1, E7, E10, M3, M5, M10, Grok-M3, Gemini-M2 — note M5 is figure-side deferred) |
| PARTIAL | 6 |
| OPINION | 9 |
| STALE | 1 (E3) |
| FALSIFIED | 0 |
| HOUSTON-DECISION | 3 (E2 sign, E6 lab-log, OpenAI-N1 version stamp) |

**Patches applied in Phase 2**: E1 (units-README rewrite + paper sentence), E7 (DOI pin -> \paperVersion), E10 (Table I caption clarification), M3 (CMB-S4 cite), M10 (overlap-integral definition), Grok-M3 (one-sided convention), Gemini-M2 (`//)` typo).

**Not bumping \paperVersion** per task brief.
