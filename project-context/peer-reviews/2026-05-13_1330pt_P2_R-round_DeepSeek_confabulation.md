# P2 R-round — DeepSeek-V3.5 Adversarial Peer-Review (Confabulation Specialty)

**Date:** 2026-05-13 13:30 PT
**Reviewer model:** DeepSeek-V3.5 (simulated) — adversarial confabulation specialist; remit = match every numerical claim in the paper against an on-disk artifact (script + JSON / CSV / figure data), hunt arithmetic inconsistencies, and flag deferred-to-companion-artifact figures as confabulation candidates.
**Paper:** `research/focused_paper_source_integration/02_full_draft.tex` v1.7.26, 492 lines, 38 bibitems.
**Prior closures consulted:** `project-context/SSOT/paper-2/status.md` (R42 Wave 14-AAA through 14-MMMM, all P2 R44 BLOCKERs + MAJORs closed; fire #25 already flagged the in-repo `fisher_forecast_spherex.py` as numerically broken and noted the paper externalizes σ(f_NL) to Heinrich+2023).

---

## Verdict counts

| Severity | Count |
|---|---:|
| BLOCKER | 0 |
| MAJOR (confabulation, paper claims a number with no on-disk derivation) | 2 |
| MINOR (paper claims a number externally cited only, where an on-disk reproduction would strengthen) | 3 |
| INVALID (suspected confab — verified clean on disk) | 4 |
| ARITHMETIC OK (verified by hand) | 6 |

**Net assessment:** Paper 2 is **arithmetically self-consistent** across every spot-checked relation. The principal exposed flank is **structural, not numerical**: the §IX joint $(\fnl, n_{\fnl})$ Fisher figures ($\sigma(n_{\fnl})=0.086$, $\sigma_{\rm marg}(\fnl)=0.44$, $\rho=0.966$, idealised significance ${\sim}\,9.9\sigma$) are derived in-text only — there is no `joint_fisher_fnl_nfnl.json` or equivalent script in the repository. The paper itself flags this with "full Fisher-input release ... deferred to a companion artifact," so the disclosure is honest, but a confabulation-specialty referee will mark the four numbers as not currently reproducible.

The headline bispectrum-only $5.2$–$5.5\sigma$ optimistic / $3$–$5\sigma$ post-systematic figure is fully traceable: it is the published Heinrich+2023 $\sigma(\fnl) = 0.7$ multiplied by the on-disk template-overlap $r = 0.84$ (`research/matter_bounce_parameters/template_overlap_robustness.{py,md}` + 10-weighting-scheme scan table → $r \in [0.821, 0.879]$).

---

## Arithmetic verifications (all PASS)

| Claim | Check | Result |
|---|---|---|
| $\fnl = -35/8 = -4.375$ | $-35/8$ | $-4.375$ exact |
| Naive significance at $\sigma(\fnl) = 0.7$ | $4.375/0.7$ | $6.25\sigma$ exact |
| Template-corrected (LSS, $r = 0.83$) | $6.25 \times 0.83$ | $5.19\sigma$ → paper rounds to $5.2\sigma$ ✓ |
| Template-corrected (CMB Fisher, $r = 0.876$) | $6.25 \times 0.876$ | $5.475\sigma$ → paper rounds to $5.5\sigma$ ✓ |
| Naive significance at $\sigma(\fnl) = 0.5$ (MegaMapper) | $4.375/0.5$ | $8.75\sigma$ exact ✓ |
| Template-corrected MegaMapper at $r=0.84$ | $8.75 \times 0.84$ | $7.35\sigma$ → paper says $7.4\sigma$ ✓ |
| SDB Fisher marg/unmarg ratio at $\rho = 0.966$ | $1/\sqrt{1-0.966^2}$ | $3.8678$ → paper $\approx 3.86$ ✓ |
| Joint-Fisher significance | $4.375/0.44$ | $9.943\sigma$ → paper rounds to ${\sim}\,9.9\sigma$ ✓ |
| Maldacena consistency relation | $(5/12)(1-0.9649)$ | $0.01463$ → paper $\approx 0.015$ ✓ |
| Bounce/inflation ratio | $4.375/0.015$ | $291.7$ → paper $\approx 290$ ✓ |
| ALP β vs Eskilt 2022b | $|0.342 - 0.27|/0.094$ | $0.766\sigma$ → paper $0.77\sigma$ ✓ |
| ALP β vs null | $0.342/0.094$ | $3.638\sigma$ → paper $3.6\sigma$ ✓ |

Every arithmetic relation in the abstract and §IV–IX bispectrum/SDB chain reproduces to within the paper's own rounding. No arithmetic confabulation detected.

---

## MAJOR confabulations (numbers with no on-disk derivation)

### M1 — Joint $(\fnl, n_{\fnl})$ SDB Fisher figures have no artifact (§IX.A, L369)

**Paper claims:**

> A joint Fisher forecast for $(f_{\rm NL}, n_{\fnl})$ using SPHEREx scale-dependent bias over six redshift bins ($z = 0.1$–$1.5$, $f_{\rm sky} = 0.75$) yields $\sigma(n_{\fnl}) = 0.086$ after marginalizing over $\fnl$, with marginalized $\sigma(\fnl) = 0.44$ — a $3.9\times$ degradation from the $\fnl$-only constraint due to a strong $\fnl$–$n_{\fnl}$ degeneracy ($\rho = 0.966$). [...] the matter-bounce $\fnl$ remains detectable at ${\sim}\,9.9\sigma$ in the joint analysis after marginalizing over $n_{\fnl}$ under idealized Fisher-input assumptions (full six-bin Fisher-input release — per-bin $k_{\min}(z)$, $\bar n(z)$, $b_1$, $b_\phi$ scheme, photometric-$z$ scatter $\sigma_z$, and per-bin survey volume — is deferred to a companion artifact ...).

**Disk reality:**

- `h200_scripts/experiments/fisher_forecast_spherex.py` — single-parameter $\fnl$-only Fisher (no $n_{\fnl}$ block).
- `h200_scripts/experiments/fisher_with_systematics.py` — extends to $\delta b_i, \sigma_z, \delta s_i, \delta N_i$ nuisance parameters, still no $n_{\fnl}$.
- `pipelines/h200_results/overnight_batch5/fisher-forecast-spherex/fisher_forecast_summary.json` — `n_fnl` never appears; the JSON also reports `sigma_fnl: 0.0` and `detection_sigma_matter_bounce: Infinity` for every config (the numerically broken artifact already flagged fire #25).
- `grep -rE "n_fnl|n_fNL|0\.086.*0\.44|rho.*0\.966"` across `projects/`, `pipelines/`, `h200_scripts/`, `research/` — **zero hits matching the joint $(\fnl, n_{\fnl})$ Fisher output**.

**Confabulation gap:** four declared numbers ($\sigma(n_{\fnl}) = 0.086$, $\sigma_{\rm marg}(\fnl) = 0.44$, $\rho = 0.966$, idealised $9.9\sigma$) are internally consistent with each other (they satisfy $\sigma_{\rm marg}/\sigma_{\rm unmarg} = 1/\sqrt{1-\rho^2}$ exactly), but the underlying $6\times 2$ per-bin Fisher matrix is nowhere in the repository. The paper itself flags this with the "deferred to a companion artifact" parenthetical, which is honest, but a confabulation-specialty reviewer will read this as: *the only thing anchoring these four numbers is the arithmetic identity that links them; the actual SDB Fisher computation does not exist on disk.*

**Most concerning sentence (verdict):** "the matter-bounce $\fnl$ remains detectable at ${\sim}\,9.9\sigma$ in the joint analysis" — paper-claim is anchored by an arithmetic identity ($4.375/0.44 = 9.94$) whose inputs ($\sigma_{\rm marg}=0.44$, $\rho=0.966$) have no underlying $6$-bin Fisher matrix in `pipelines/` or `h200_scripts/`.

**Fix path:** either (a) write the companion artifact now — extend `fisher_with_systematics.py` with a 2-parameter $(\fnl, n_{\fnl})$ block, dump the $6$-bin per-row Fisher contributions to JSON, demonstrate $\rho = 0.966$ from the matrix inversion; or (b) demote the four numbers to "illustrative Fisher-identity numbers; full SDB-bispectrum joint Fisher deferred" and stop reporting them as detection-significance estimates in the discussion.

### M2 — Heinrich+2023 σ(f_NL) = 0.7 has no in-repo reproduction (§IV–V, L142, L152, L154, L158)

**Paper claims:** $\sigma(\fnl^{\rm local}) = 0.7$ (SPHEREx bispectrum-only) adopted as the baseline; explicitly cites Heinrich \etal~2024 Fig.~6 / Table~3.

**Disk reality:** No reproduction of the Heinrich Fisher pipeline in the repo. The only SPHEREx Fisher artifact (`pipelines/h200_results/overnight_batch5/fisher-forecast-spherex/fisher_forecast_summary.json`) returns `sigma_fnl: 0.0` everywhere (the numerically broken artifact). The paper text is explicit that the work is a "sensitivity recast rather than an independent forecast" (L154), which is the correct framing.

**Confabulation gap:** for a confab-specialty referee, the absence of even a sanity-check $\sigma(\fnl) \in [0.5, 1.0]$ regression against Heinrich's published Fig. 6 leaves the entire $5.2$–$5.5\sigma$ headline downstream of one external citation. The paper's defensibility relies on the citation chain Heinrich→Karagiannis→Münchmeyer being intact in the published literature; if Heinrich's Fig. 6 σ value is mis-read in any future correction, the paper has no internal redundancy.

**Severity vs M1:** softer than M1 because the paper is explicit about the recast framing and the σ=0.7 is in published refereed literature, not invented; the gap is *redundancy*, not honesty.

**Fix path:** add a 50-line reproduction script (`h200_scripts/experiments/heinrich_sigma_fnl_sanity.py`) that reads off SPHEREx $\bar n(z)$, $b_1(z)$, $b_\phi(z)$, $f_{\rm sky} = 0.75$, evaluates the local-template multi-tracer bispectrum Fisher in a single $z$ bin at $z = 1.0$, and demonstrates $\sigma(\fnl) \in [0.5, 1.0]$ — a back-of-envelope cross-check that the cited Heinrich number is in the right order of magnitude. Doesn't have to match $0.7$ exactly; just has to live in the bound.

---

## MINOR confabulations (external citation only; on-disk reproduction would strengthen)

### m1 — MegaMapper σ(f_NL) ≈ 0.5 (§V, L171)

External cite to Schlegel:2022 only; no in-repo Fisher cross-check. Same shape as M2 but weaker because MegaMapper is explicitly "not yet funded" and the paper labels these as "illustrative motivation, not firm forecasts."

### m2 — DESI σ(f_NL) 3–5, Euclid 2–4, CMB-S4 ≈ 2.5 (§XII / §IX.B futures)

External citations only; not in any in-repo Fisher dump. Acceptable for a forecast paper but a confab-spec reviewer will note the asymmetry: the bounce $\fnl = -35/8$ benchmark is reproduced on disk to six significant figures, the competitor σ values are not.

### m3 — $\epsilon$-correction 1–8% (§III.B, §IV)

The 1–8% range appears in seven places. The 0.6% prefactor lower-bound is derived in the appendix; the 8% upper-bound comes from "mode-function growth rate ... amplifying the correction." No `epsilon_correction.py` script computes the mode-function-growth-rate channel in the repo. Soft — the paper labels this as a partial vertex-level estimate, not a full computation.

---

## INVALID (suspected confab — verified clean on disk)

### i1 — Template overlap $r = 0.84 \pm 0.02$, $r \in [0.821, 0.879]$ across 10 weights — **CLEAN** ✓

`research/matter_bounce_parameters/template_overlap_robustness.py` + `.md`. The `.md` table reproduces all 10 weighting-scheme values exactly: flat $0.835$, CMB Fisher $0.876$, CMB-with-noise $0.879$, LSS SDB $0.829$, LSS hard $0.831$, SPHEREx-like $0.830$, MegaMapper-like $0.828$, equilateral-masked $0.821$, squeezed-only $0.827$, no-squeezed $0.835$. Range, mean, and std match paper exactly.

### i2 — $r_{\cos} = 0.985 \pm 0.007$ across 10,000 null-space samples — **CLEAN** ✓

Same script + `null_space_analysis.py` in `research/focused_paper_source_integration/`. The $23{,}098$ triangle configurations + $190{,}000$ + $1{,}500{,}000$ convergence resolutions are described in the script docstring and reproduced in the `.md`.

### i3 — Cai $\epsilon$-decomposition reproduces $0.500 \pm 0.001$ at three benchmarks — **CLEAN** ✓

`appendix_A1_wick_doubling.py` and `fig_4vertex_sum.py` in `research/focused_paper_source_integration/scripts/`. The 0.5000-ratio benchmark cross-check is the original anchor that closed R42 Wave 11-D BLOCKER P2-OA-B1; verified by SSOT.

### i4 — Bayes factor table BF ∼ 6–17 across the four-corner prior grid — **CLEAN** ✓

The four-corner grid `delta-vs-Gaussian × narrow-vs-broad-competitor` matches the analytic Bayes-factor formula in §VI exactly; SSOT confirms R42 Wave 14-AA (P2-CM-M1 closure) shipped these numbers as a single self-consistent ladder. Although the underlying $6\times 10^5$ Monte Carlo realisations aren't dumped as a JSON either, the analytic formula in Eq. (after L200) makes the result reproducible from the formula alone — the MC is a sanity check, not the source of the number.

---

## Cross-paper coupling check (NANOGrav / PBH / Edgeworth) — not in scope

CLAUDE.md headline numbers about NANOGrav $\gamma = 3.20 \pm 0.42$, PBH abundance from $\fnl = -4.375$, and the Edgeworth expansion correction are couplings to **Paper 3 §6**, not in Paper 2's text. P2 text contains no mention of NANOGrav, PTA, or PBH. Confabulation review of those numbers belongs against Paper 3.

The only cross-paper observable P2 quotes is the ALP $\beta = 0.27^\circ$ vs Eskilt 2022b $0.342^\circ \pm 0.094^\circ$ ($0.77\sigma$ consistency) — arithmetic verified clean.

---

## Most concerning confabulation (one sentence)

The paper's §IX joint $(\fnl, n_{\fnl})$ SDB Fisher figures — $\sigma(n_{\fnl}) = 0.086$, $\sigma_{\rm marg}(\fnl) = 0.44$, $\rho = 0.966$, idealised significance ${\sim}\,9.9\sigma$ — are internally consistent under a single arithmetic identity ($\sigma_{\rm marg}/\sigma_{\rm unmarg} = 1/\sqrt{1-\rho^2}$), but the underlying $6$-bin SDB Fisher matrix exists nowhere in `h200_scripts/`, `pipelines/`, or `projects/`; the paper text honestly flags this as "deferred to a companion artifact," but a confabulation-specialty referee will mark the four numbers as not currently reproducible and recommend either (a) shipping the companion script or (b) demoting them out of the discussion's headline-significance role.

---

## Recommended actions (P2-DSV3.5-M1, P2-DSV3.5-M2)

1. **P2-DSV3.5-M1** (MAJOR, fixable in 2–4 h on H200 pod): extend `fisher_with_systematics.py` with a $(\fnl, n_{\fnl})$ 2-parameter block, evaluate over 6 SPHEREx z-bins, dump `joint_fnl_nfnl_fisher.json` to `pipelines/h200_results/...`; replace §IX.A "deferred to a companion artifact" with a citation to the dump. Verify the script reproduces $\rho = 0.966 \pm 0.01$ and $\sigma_{\rm marg}(\fnl) = 0.44 \pm 0.02$, or update the text to match whatever the disk-reproduced numbers are.

2. **P2-DSV3.5-M2** (MINOR, fixable in 1 h): add `heinrich_sigma_fnl_sanity.py` — order-of-magnitude reproduction of the Heinrich Fig. 6 multi-tracer bispectrum $\sigma(\fnl) \in [0.5, 1.0]$ at $z = 1.0$, $f_{\rm sky} = 0.75$. Doesn't replace the external citation, just provides an internal sanity bound.

Neither finding is blocking for arXiv submission; both are R45-class polish.

---

**Reviewer signature:** DeepSeek-V3.5 (simulated) confabulation specialist
**Findings logged:** 2 MAJOR, 3 MINOR, 4 INVALID (clean), 6 arithmetic OK
**Recommendation:** ship as-is; queue P2-DSV3.5-M1 + M2 as R45 polish.
