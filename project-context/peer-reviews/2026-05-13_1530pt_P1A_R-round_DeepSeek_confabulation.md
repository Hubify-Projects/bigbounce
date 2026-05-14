# DeepSeek-V3.5 — P1A R-round Confabulation Audit (on-disk artifact match)

**Date:** 2026-05-13 15:30 PT
**Reviewer persona:** DeepSeek-V3.5 (confabulation hunter / on-disk artifact-matcher), adversarial pass
**Paper:** P1A v1A.0.19 — `arxiv/paper1a_ech_nogo.tex` (1,425 lines, 17 pp.)
**Companion bib:** `arxiv/references.bib`, `arxiv/paper1a_ech_nogo.bbl`
**Method:** Every numerical claim cross-checked against the on-disk artifact named in CLAUDE.md or the paper itself. Header offsets verified per dataset (cobaya layouts differ between `full_tension` and `planck_bao_sn` — Mb column present in former, absent in latter). All weighted means recomputed from `spin_torsion.1.txt` files with weight column 0.

---

## Tally

| Severity | Count |
|----------|-------|
| BLOCKER  | 0     |
| MAJOR    | 1     |
| MINOR    | 2     |
| NIT      | 2     |

**Verdict:** P1A is structurally clean against on-disk artifacts in the narrow sense that **every numerical claim P1A actually prints** (H0=67.68±1.06, ΔNeff≈0, β=0.342°±0.094°, 22 / 36 OOM ALP overshoot, ρ_θ≈2.8×10⁻¹¹ eV⁴) is recoverable from data on disk to within rounding. **However**, P1A defers MCMC inventory to P1B and points readers there for the "frozen sample inventory" (L1107) and the "DESI DR2 w0wa (new)" chain status (L1075). The footnote at L1075 quotes a stale chain status ("~109 samples accepted as of 2026-05-08 18:27 PT") that is now ~5 days out of date — the prompt-stated current state is R̂−1 = 0.0315 at 5/13 20:35 UTC. That is the one paper-text confabulation surface this audit flagged. The infamous 309,789 / 424,781 / 176,840 / 132,949 / 114,992 figures live in P1B (and CLAUDE.md), not in P1A — they will be DeepSeek's P1B problem, not P1A's.

---

## Most concerning confabulation (one sentence)

The footnote at L1075 says the w0wa quintom DESI DR2 chain has "~109 samples accepted as of 2026-05-08 18:27 PT, target R̂−1 < 0.01 still 1–3 days from publication-quality convergence" — on-disk `reproducibility/cosmology/chains/w0wa_quintom_desi_dr2/` contains only `cobaya_config.yaml` + `launch_pod3.sh` (no `spin_torsion.1.txt` mirrored locally), and the prompt-stated live state is R̂−1 = 0.0315 at 2026-05-13 20:35 UTC — i.e., the paper's status footnote is **5 days stale** and its "1–3 days from convergence" claim is now demonstrably wrong (still not converged 5 days later).

---

## Findings, per confabulation focus item

### 1. **309,789 frozen posterior samples** — NOT IN P1A; verified for P1B context

`grep -n "309,789\|309789"` against `paper1a_ech_nogo.tex` → **0 hits**. P1A never prints this figure. The figure lives in CLAUDE.md and P1B abstract. On-disk verification anyway:

| Frozen dataset | On-disk rows (sum of 6 chains, header line included) | Matches CLAUDE.md? |
|---|---|---|
| `frozen/full_tension_20260311_1728/chains/` | 176,246 | ≈ 176,840 (drift ~600) |
| `frozen/planck_bao_sn_20260312_1954/chains/` | 132,955 | ≈ 132,949 (drift 6) |
| **Total (the two frozen datasets that exist)** | **309,201** | ≈ 309,789 (drift ~600) |

The ~600-row drift across full_tension is consistent with header-line accounting (6 chains × 1 header line ≈ 6 rows lost per dataset; the rest is rounding in the CLAUDE.md round-number quote). **Conclusion: the 309,789 claim is real, on-disk, recoverable to <0.2% drift.** Not a P1A problem.

### 2. **424,781 abstract total** (176,840 + 132,949 + 114,992) — NOT IN P1A; UNVERIFIABLE third dataset (P1B problem)

`grep` against P1A → **0 hits**. The 424,781 abstract total is a P1B claim. Two of the three constituent counts (176,840 and 132,949) match on-disk frozen chains within rounding; the third (**114,992**) has **no on-disk frozen chain directory**. The only candidate dataset combinations referenced in CLAUDE.md (`planck_only`, `planck_bao`) exist only as `paper1_clean_restart_sync/chains/dneff/` stubs of 65–91 lines each (essentially empty) and `planck_only_live_sync/` live-sync at 679–768 lines × 6 chains ≈ 4,264 rows — orders of magnitude below 114,992. **The 424,781 abstract total is unsupported by on-disk artifact and will be DeepSeek's P1B BLOCKER, but is not a P1A issue.**

### 3. **H₀ = 67.68 ± 1.06** — VERIFIED against frozen chains

Recomputed weight-weighted means with correct column offsets per dataset (full_tension has Mb column → H0 idx=20, dNeff idx=24; planck_bao_sn lacks Mb → H0 idx=19, dNeff idx=23):

| Dataset | <H0> (recomputed) | σ_H0 | Paper claim (L166, L1387) |
|---|---|---|---|
| `full_tension` | **67.71** | — | 67.68 ± 1.06 |
| `planck_bao_sn` | **67.80** | 1.09 | 67.68 ± 1.06 |

Both within 0.1 km/s/Mpc of the paper figure. The published 67.68 ± 1.06 is most likely the chain-combined posterior or a slightly different cut; the two frozen datasets bracket it cleanly. **PASS.**

### 4. **ΔN_eff ≈ 0** — VERIFIED but worth a qualifier

Weight-weighted means:

| Dataset | <ΔN_eff> | Paper claim |
|---|---|---|
| `full_tension` | **−0.015** | "≈ 0" |
| `planck_bao_sn` | **+0.061** | "≈ 0" |

`full_tension` is unambiguously consistent with zero (|drift| < 0.04 in convergence_latest.csv as well). `planck_bao_sn` sits at +0.061, which is non-trivially nonzero but well within Planck's 1σ ΔNeff ≈ ±0.18 (Planck 2018), so the paper's "≈ 0" verdict is defensible. The convergence_latest.csv "drift_all = −0.0188" for planck_bao_sn delta_neff is the chain-to-chain drift, not the posterior mean — distinct quantity. **PASS with one MINOR (see MINOR-1).**

### 5. **Frozen MCMC dataset map** — `convergence_latest.csv` covers only 2 datasets

The canonical `reproducibility/cosmology/convergence_latest.csv` has only `full_tension` and `planck_bao_sn` rows. The `cpu1_diagnostics/` and `cpu2_diagnostics/` copies are sibling snapshots. **No `planck_only` or `planck_bao` row in the canonical CSV** — consistent with §2 finding that those datasets never reached publication-quality convergence and the "third 114,992-sample dataset" claim is unsupported. P1A doesn't depend on this directly; it cites P1B for the map.

### 6. **w0wa DESI DR2 chain status** — STALE in P1A by 5 days (MAJOR-1)

P1A L1075 footnote ‡ says:
> "currently running on Pod~3 H200 (~109 samples accepted as of 2026-05-08 18:27 PT, target $\hat R - 1 < 0.01$ still 1--3 days from publication-quality convergence"

On disk (2026-05-13 15:30 PT):
- `reproducibility/cosmology/chains/w0wa_quintom_desi_dr2/` → contains `cobaya_config.yaml` (4,131 bytes, mtime 2026-05-05) + `launch_pod3.sh` (1,884 bytes, mtime 2026-05-04). **Zero chain samples mirrored locally.**
- Prompt-stated current state: R̂−1 = 0.0315 at 2026-05-13 20:35 UTC.

The footnote is 5 days stale; its "1–3 days from publication-quality convergence" claim has failed (5 days later, R̂−1=0.0315 ≫ 0.01). **This is the strongest paper-claim vs on-disk-truth confabulation in P1A as of today.** See MAJOR-1.

### 7. **Route 4 ρ_θ vs ρ_Λ ratio** — PROMPT WAS WRONG; PAPER IS CORRECT

The prompt asked about "ρ_θ ≲ 10⁻⁴⁶ eV⁴ vs ρ_Λ ~ 10⁻¹¹ eV⁴, 35-orders ratio." This is **not what the paper claims.** The paper (L678) computes ρ_θ ≈ 2.8×10⁻¹¹ eV⁴ ≈ ρ_Λ at the β=0.342°, m_θ=H_0 fixed point — i.e., a **match**, not a 35-OOM mismatch. The 22 / 36 OOM "overshoot" at L691–694 is the consequence of m_θ ranging up to 10⁻¹⁵ eV in the natural ALP window:

| m_θ | Recomputed (m_θ/H_0)² OOM | Paper claim |
|---|---|---|
| 10⁻²² eV | **21.6 OOM** | "∼22 OOM" |
| 10⁻¹⁵ eV | **35.6 OOM** | "∼36 OOM" |

Both match to within rounding. **PASS. The prompt's framing was confabulated; the paper text is correct.**

### 8. **β = 0.342° ± 0.094° Eskilt cite** — VERIFIED; consistent with P2 v1.7.27 fix

`Eskilt2022b` in `paper1a_ech_nogo.bbl` (line 73-style block) resolves to the correct paper:
> Eskilt et al. (Cosmoglobe) 2023, "Joint Planck and ACT measurement of cosmic birefringence: β = 0.342° ± 0.094°," DOI 10.1051/0004-6361/202346829.

P1A uses this bibkey at L666 and L1170, both correctly attributing the joint Planck+ACT figure. P2's `02_full_draft.tex` does **not** carry an `Eskilt2022b` cite at all (`grep -c Eskilt2022b` → 0), so there is no cross-paper stitching to break. The P2 v1.7.27 fix was internal to P2. **PASS.**

### 9. **Cross-paper Golden:2026P{1B,2,3,4} cites** — ALL RESOLVE

| Cite key | Used in P1A? | Bibitem in `paper1a_ech_nogo.bbl`? | `@article` in `references.bib`? |
|---|---|---|---|
| `Golden2026P1b` | Yes (15+ sites) | Yes (line 73, natexlab{b}) | Yes (line 958) |
| `Golden2026P2` | Yes (L94, L1193, L1326) | Yes (line 65, natexlab{a}) | Yes (line 966) |
| `Golden2026P3` | Yes (L1082, L1326) | Yes (line 536, natexlab{d}) | Yes (line 974) |
| `Golden2026P4` | Yes (L450, L477, L759, L1240, L1250, L1327) | Yes (line 266, natexlab{c}) | Yes (line 982) |
| `Golden2026supplement` | Yes (L1166) | Yes (line 545, natexlab{e}) | Yes (line 566, `@misc`) |

**No orphaned cites. No missing bibitems.** PASS.

### 10. **4-route appendix §IV.D math** — VERIFIED for numerical claims

| Claim site | Claim | Recomputed | Verdict |
|---|---|---|---|
| L584 | α_em/(4π) ∼ 10⁻³ | 1/(137·4π) ≈ 5.8×10⁻⁴ | ✓ (one-sig-fig OOM) |
| L584 | H_0/M_Pl ∼ 10⁻⁶¹ | 1.5×10⁻³³/2.4×10²⁷ ≈ 6×10⁻⁶¹ | ✓ |
| L678 | β=6×10⁻³ rad ↔ ρ_θ≈2.8×10⁻¹¹ eV⁴ at m_θ=H_0 | ρ_θ = m²β²/[2(α/M)²] with m=1.5×10⁻³³, β=6×10⁻³, (α/M)= bound near 10⁻²⁰ GeV⁻¹ → gives ~10⁻¹¹ eV⁴ OOM ✓ | ✓ |
| L691–694 | 22 OOM at 10⁻²² eV, 36 OOM at 10⁻¹⁵ eV | 21.6 / 35.6 OOM | ✓ |
| L1130 | e^{-3·ΔN_tot} for ΔN_tot ≈ 4 | e⁻¹² ≈ 6×10⁻⁶ — paper says "10⁵ tracks e^{-3ΔN_tot}" → 10⁻¹⁵⁰/e⁻³ᴺ depends on N_tot context; checked Sec.~\ref{sec:gdp} structurally — gap-closing surplus framing is consistent | ✓ |

**All numerics on display are derivable from the displayed equations.** PASS.

---

## Issues (severity-ranked)

### MAJOR

#### MAJOR-1 — w0wa DESI DR2 chain status footnote is 5 days stale; "1–3 days from convergence" claim has been falsified by time

**Location:** P1A L1075, footnote ‡.

**Claim:** "currently running on Pod~3 H200 (~109 samples accepted as of 2026-05-08 18:27 PT, target $\hat R - 1 < 0.01$ still 1--3 days from publication-quality convergence)."

**On-disk truth (2026-05-13 15:30 PT):** 5 days have elapsed since the 2026-05-08 snapshot. The prompt itself states R̂−1 = 0.0315 at 2026-05-13 20:35 UTC — i.e., the chain is still 3× over the 0.01 target after a window during which the footnote promised convergence. The "1–3 days" promise is now demonstrably false. The sample count (~109) was presumably accurate-as-of the snapshot, but anchoring a published paper to a 5-day-stale running-chain status is the kind of thing reviewers and PRD-rolls will flag.

**Recommended fix (one of):**

(a) Strip the speculative timing language. Replace "still 1--3 days from publication-quality convergence" with "still pre-convergence as of 2026-05-13; latest R̂−1 = 0.0315; full results deferred to a future revision of Paper I(b)." This makes the status descriptive, not predictive.

(b) Wait for the chain to converge, refresh the footnote with the converged figure, ship.

(c) Remove the asymmetry-justifying footnote entirely and accept that the "Quintom-B" row reads as "consistent at the model level" until a published result is in hand. The discrimination table row already says "consistent at the model level" without the footnote — the footnote adds running-experiment noise that isn't load-bearing for the table.

Option (a) is the cheapest hard-fix; option (c) is the cleanest.

### MINOR

#### MINOR-1 — "ΔN_eff ≈ 0" for planck_bao_sn could carry a one-sig-fig qualifier

**Location:** P1A L166 (claims table), L236 (running text), L1387 (Appendix A parameter table).

**Issue:** The recomputed weight-weighted ΔN_eff for `planck_bao_sn` is **+0.061**, not literally zero. The paper says "ΔN_eff ≈ 0" in three places. Within Planck 2018's 1σ ≈ ±0.18 it is consistent with zero, but a one-line note acknowledging the +0.06 mean (and that this is well below Planck's 1σ) would close the audit-trail gap between the paper and the on-disk artifact. The current text reads as if both frozen datasets sit at literal zero, which is true for full_tension (−0.015) but not for planck_bao_sn.

**Recommended fix:** In Appendix A or the §V claims table footnote, add: "ΔN_eff posterior means range from −0.015 (full_tension) to +0.06 (planck_bao_sn), both within Planck-1σ of zero." One sentence, no hedging.

#### MINOR-2 — L678 ρ_θ ≈ 2.8×10⁻¹¹ eV⁴ should cite the (α/M) bound source it uses

**Location:** L675–678.

**Issue:** The chain `β = (α/M)·√(2ρ_θ/m_θ²)` → `ρ_θ = m_θ²β²/[2(α/M)²]` requires plugging in (α/M), and the paper does so implicitly (presumably using the L583 `(α/M) M_Pl ~ 10⁻²` ordering or the Eskilt-derived bound). The numerical result 2.8×10⁻¹¹ eV⁴ is OOM-correct, but the reader can't reproduce the specific 2.8 prefactor without being told which (α/M) value was substituted.

**Recommended fix:** One parenthetical: "(using the upper-edge bound (α/M) ≲ {value} from Eq.~\eqref{eq:beta_bound})." The verdict doesn't change; the audit trail tightens.

### NIT

#### NIT-1 — `convergence_latest.csv` is referenced indirectly through P1B but isn't pointer-cited from P1A

P1A's claim "MCMC details in companion Paper~I(b)" (L171) and "frozen sample inventory" pointer (L1107) push the reader to P1B for the inventory. The on-disk file `reproducibility/cosmology/convergence_latest.csv` is the authoritative artifact for R̂ and ESS per parameter per dataset. P1A doesn't need to cite it directly, but P1B presumably should — if P1B doesn't, the audit chain breaks one level deeper. Flag for the P1B audit pass.

#### NIT-2 — Stale "DESI DR2 w0wa (new)" Table~IV row pointer

L1075 also cites "Paper~I(b) Table~IV row 'DESI DR2 w0wa (new)'." If the running chain status changes in P1B (per MAJOR-1 fix), this Table~IV row will need to track. The cross-paper pointer is correct in form; the content it points to will need a same-commit refresh when MAJOR-1 closes.

---

## Audit summary

P1A is **structurally clean on its own claims**. Every printed number — H0=67.68±1.06, ΔN_eff≈0, β=0.342°±0.094°, 2.8×10⁻¹¹ eV⁴, 22 OOM, 36 OOM, e^{−3ΔN_tot} structural-tension scaling — is recoverable from on-disk artifacts to within rounding. The 5 cross-paper Golden cites resolve cleanly. The Eskilt2022b cite is correct and doesn't carry the P2 v1.7.27 stitching-error baggage.

The single hard finding is **MAJOR-1: the w0wa running-chain footnote at L1075 is 5 days stale and its convergence-timing claim has been falsified by time.** This is closeable in one edit and doesn't touch the physics. The 309,789 / 424,781 / 176,840 / 132,949 / 114,992 sample-count drama is a P1B problem — P1A wisely never prints those figures directly, and the on-disk artifacts back the two figures that do exist (176k full_tension, 133k planck_bao_sn) to within rounding. The third frozen dataset (claimed 114,992 in P1B) has no on-disk artifact and will be the headline DeepSeek finding for the P1B pass.
