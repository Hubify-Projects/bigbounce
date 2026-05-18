# P1A v1A.0.20 — DeepSeek-V3.5 Confab-Hunter Adversarial Review

**Date:** 2026-05-14 10:00 PT
**Reviewer persona:** DeepSeek-V3.5 (simulated) — confabulation hunter
**Target:** `arxiv/paper1a_ech_nogo.tex` (1457 lines, v1A.0.20)
**Scope:** Numbers without on-disk source; 4th adversarial pass after tick #3 rewrote the L1075 footnote.
**Time-boxed:** 5 minutes.

---

## Verdict

Tick #3 footnote rewrite (L1095–1096) is now outcome-agnostic and the dominant load-bearing numbers (γ=0.274, ρ_c=0.27ρ_Pl, β_obs=0.342°±0.094°, 424,781 samples, H₀=67.68±1.06, γ_PTA=2.567±0.382) trace cleanly to either the SSOT, the on-disk frozen chains, or cited literature. Remaining findings are **mid-severity at worst** — provenance gaps and one narrative inconsistency, not numerical confabs.

---

## Findings

### P1A-DS-B1 (MAJOR) — β ≈ 0.27° "spectator-ALP prediction" has no on-disk derivation script

**Where:** L95–96 abstract, L469 ("0.27°–0.30°"), L1192 ("β ≈ 0.27° prediction arises in"), L1216 ("β ≈ 0.27°"), L1346 conclusion, L1425 Table II ("0.27° (midpoint)").

**Issue:** The bounce-side prediction β ≈ 0.27° is cited in 6+ places as a load-bearing model-discrimination number, but I found NO on-disk script, JSON, or fit file that derives 0.27° from spectator-ALP parameters (f_a ~ M_Pl, m_θ ~ H_0). The table labels it "midpoint" with no anchor to a calculation. The closest companion derivation lives in Paper I(b) per the prose, but **L1425 already lives in the standalone P1A**, so any P1A-only reader sees a number with no in-paper derivation and no citation.

**Fix:** Add a one-line in-text formula or cite the specific Paper I(b) equation/section that produces 0.27° from the spectator-ALP parameters. Alternatively cite an external derivation (e.g., Carroll Field Jackiw-style with f_a ~ M_Pl, m_θ ~ H_0 yields β ~ α_em / 4π ~ rad-scale, then numerical reduction). Right now the number is asserted, not produced.

---

### P1A-DS-B2 (MAJOR) — "0.27°–0.30°" range vs. "0.27° midpoint" internal inconsistency

**Where:** L469 says "β ≈ 0.27°–0.30°". L1425 Table II row labels 0.27° the "midpoint". L1216, L1346 use bare "0.27°". L1192 uses "≈ 0.27°".

**Issue:** If 0.27° is a midpoint of a 0.27°–0.30° range, the midpoint is 0.285°, not 0.27°. Either 0.27° is the **lower edge** (mislabeled as midpoint), or the range is wrong, or the midpoint is wrong. The L1346 falsification discussion uses |0.342 − 0.27|/0.03 = 2.4σ — if the "real" prediction is actually 0.285° this becomes |0.342 − 0.285|/0.03 = 1.9σ, which materially changes the discrimination claim.

**Fix:** Pick one. Either commit to a point prediction 0.27° (no range) or a range and re-derive the 2.4σ LiteBIRD distinguishability number from the chosen central value.

---

### P1A-DS-B3 (MINOR) — "14 mechanism-class constraints via 7 foundations + 6 branches" off-by-one bookkeeping

**Where:** L67, L195, L1333: "Through 7 foundation studies (Foundations A–G) and 6 observational research branches (Branches H, J, L, M, N, O) we catalog 14 mechanism-class constraints."

**Issue:** Table I (L866 onward) shows B1–B7 sourced from Foundations A–G (7 barriers), B8–B13 sourced from Branches H/J/L/L-M/M/N-O (6 barriers), and **B14 sourced from "ECH Gates"** — a separate category that is neither a foundation nor a branch. So the narrative "7 + 6 = 14" is structurally 7 + 6 + 1 = 14, with B14 produced by the perturbation-transparency theorem (an ECH-gates result, not a foundation or branch). The text already flags B14 as the theorem that subsumes B8 (L194–197), so the framing is honest about the structure — but the phrase "7 foundations and 6 branches yield 14 constraints" overcounts by one without acknowledging the ECH-Gates row.

**Fix:** Tweak to "7 foundations (A–G), 6 branches (H, J, L, M, N, O), and the ECH-Gates perturbation-transparency theorem (B14) give 14 mechanism-class constraints" or equivalent. Cosmetic but it's been called out before by other reviewers and the easy fix didn't propagate.

---

### P1A-DS-B4 (MINOR) — "424,781 samples" cited as Paper I(a) abstract figure but the **frozen chains directory** holds 4 datasets, not the 3 enumerated in the companion footnote

**Where:** L232: "Cobaya v3.6.1, 424,781 samples". CLAUDE.md canonical: 176,840 + 132,949 + 114,992 = 424,781 across **three** frozen dataset combinations. On-disk: `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/` contains **four** subdirectories: `full_tension`, `planck_bao`, `planck_bao_sn`, `planck_only`.

**Issue:** The 424,781 total reconciles three datasets; the directory has four. Either (a) `planck_only` was excluded from the 424,781 count (in which case the paper is silent about why), or (b) the count is mis-summed. Per L1096 the companion's "three completed dataset combinations" framing matches the 3-not-4 narrative, but P1A doesn't tell the reader which three. Standalone-readable P1A loses this provenance.

**Fix:** Add a one-clause aside at L232: "424,781 accepted samples across {Planck-only, Planck+BAO, Planck+BAO+SN | OR | the three dataset combinations enumerated in companion Paper I(b) Table IV}". Standalone readability + audit trail.

---

### P1A-DS-B5 (MINOR) — γ_PTA = 2.567 ± 0.382 quoted in P1A but the script/posterior file is in a companion/pod artifact, not in-repo at an obvious path

**Where:** L1102: "NANOGrav model comparison: γ = 2.567 ± 0.382 from real-KDE reanalysis". L1107: "supersedes the synthetic γ = 3.20 ± 0.42 used in pre-real-KDE drafts". L1427 Table II row.

**Issue:** The number is correct per SSOT/index.md (canonical post-tick #2 of the drive-to-100 loop) but I could not find an in-repo JSON, NPY, or log file at a `pipelines/...` / `projects/.../real_kde*` path that produces γ=2.567±0.382 in <60s of search. The SSOT entry references a P3 paper-side update; P1A re-quotes the number without a citation to the producing artifact. For a P1A standalone reader (P1A is being submitted standalone per v1A.0.20 framing) this is an unanchored number.

**Fix:** Either cite the producing pipeline path (`pipelines/p3_anomaly_engine/pta_real_kde/...` or whatever the canonical path is) in a footnote, or defer to companion Paper III with an explicit `\cite{}` and section reference. Right now it's a bare number in a discriminator table.

---

### P1A-DS-B6 (MINOR) — Route 1–4 amplitude bounds are dimensional / order-of-magnitude, not numerical posterior bounds

**Where:** L605–611 (Route 2): "α_em/(4π) ~ 10^{-3}, H_0/M_Pl ~ 10^{-61}, (α/M)M_Pl ~ 10^{-2}, β_obs ~ 6 × 10^{-3} rad → dimensionless ratio ~ 10^{-58} to 10^{-60}". L595: ∂θ ~ H ~ 10^{-33} eV. L562: ρ_Λ ~ (10^{-3} eV)^4.

**Issue:** These are dimensional-analysis bounds, not posterior-inferred bounds, and the paper occasionally describes them as "amplitude-level closure" (L518, L539). That's fair, but a confab-hunting reviewer will note there's no fit / no data product / no MCMC run producing these ratios. The text DOES acknowledge "factor-of-~100 ambiguity" (L612) and "qualitative R2 closure" (L624) — so the honesty flag is already on. But a stricter referee might ask whether the 10^{-58}–10^{-60} ratio depends on which way you order the (α_em / 4π) vs (H_0/M_Pl) hierarchy — and the paper itself flags this at L619–622.

**Fix:** No new derivation needed; the text already self-flags. Optionally add a sentence at the start of §V.B: "Route closures R1–R4 are dimensional / amplitude-level rather than posterior-inferred, by design — see also §V.A on the level of the argument." Helps preempt the referee question.

---

## Numbers I checked and traced cleanly (no findings)

| Number | Source on disk |
|---|---|
| γ = 0.274 ± 0.020 (Barbero–Immirzi) | L269 cite ABCK1998; references.bib L699 |
| ρ_c ≈ 0.27ρ_Pl (LQC) | L342 formula, self-contained derivation |
| β_obs = 0.342° ± 0.094° | L1191 cite Eskilt2022b (Eskilt+Komatsu PRD 106 063503); references.bib L1040 |
| 3.6σ ALP detection significance | L96, L1190 cite Eskilt2022b — matches published number |
| 14 barriers full list | Table I L866–887 enumerates all 14, source columns consistent |
| H₀ = 67.68 ± 1.06 | L166, L236, L1419 — matches CLAUDE.md canonical full-tension value |
| ΔN_eff = -0.020 ± 0.169 | L1420 (full-tension) — matches `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/full_tension/` |
| 309,789 frozen posterior samples | Referenced via Paper I(b) footnote; matches CLAUDE.md and `reproducibility/docs/KNOWN_GAPS.md` L103 |
| R̂−1 progress wording (L1096) | Tick #3 rewrite is outcome-agnostic ("descending monotonically toward < 10^{-2}", no calendar date) — CONFIRMED |
| Route 1 (NJL): closed by M_Pl^{-2} suppression | L562 dimensional argument self-contained |
| Route 2 (one-loop): 10^{-58}–10^{-60} | L605–611 dimensional, with stated ambiguity |
| Route 3 (Immirzi running): mass-dimension lock | §V.D self-contained algebra |
| Route 4 (parity-CMB / spectator ALP): see DS-B1 above | β=0.27° prediction is the only confab candidate |

---

## Summary line for SSOT

P1A v1A.0.20 confab-hunter R-round: **2 MAJOR + 4 MINOR**. The two MAJORs are about the β=0.27° spectator-ALP prediction — it appears in 6 places without an in-paper derivation OR a clean external cite, and its "0.27° midpoint of 0.27°–0.30°" labeling is arithmetically inconsistent. Tick #3 footnote rewrite is solid and outcome-agnostic. No new fabrication detected beyond what prior rounds flagged.

— DeepSeek-V3.5 (simulated), 2026-05-14 10:05 PT
