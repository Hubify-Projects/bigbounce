# P1B R-round — DeepSeek-V3.5 Confabulation Hunt (on-disk artifact match)

- **Reviewer:** DeepSeek-V3.5 (adversarial, on-disk artifact matcher)
- **Date:** 2026-05-13 16:30 PT
- **Paper:** `arxiv/paper1b_mcmc_companion.tex` v1B.0.3 (658 lines)
- **Method:** Match every numerical claim in P1B against on-disk artifacts in `reproducibility/cosmology/{frozen,paper1_clean_restart_sync,planck_only_live_sync}/` and `pipelines/h200_results/pod1_namaster_umap_2026-04-29/`. Adversarial — assume claim is confabulated until proven by file contents.

## Headline counts

- **2 BLOCKER** (claim conflicts with on-disk artifact in a way that breaks the abstract / Table III).
- **1 MAJOR** (load-bearing prose carries a stale state that an already-closed P1A R-round-3 finding has corrected; not yet propagated to P1B).
- **2 MINOR** (small numeric mismatches; do not break the headline but should be noted).
- **0 nit.**

## Most concerning confabulation (one sentence)

**P1B abstract + §III footnote + Table III all assert the third dataset combination ("Planck-only") carries 114,992 raw accepted MCMC samples; the actual on-disk live-sync directory `reproducibility/cosmology/planck_only_live_sync/chain_{01..06}/spin_torsion.1.txt` contains 4,258 rows total (708 + 679 + 678 + 699 + 727 + 767), and a full recursive grep of `reproducibility/cosmology/` for the literal strings `114992` / `114,992` returns ZERO source anchors (only random substring matches inside floating-point columns of unrelated chain rows) — the 114,992 figure has no provenance and the "424,781 total" in the abstract is therefore phantom-inflated by ~110,734 samples (~26 % of the headline number).**

---

## BLOCKER findings

### B1. Planck-only `114,992` samples is unanchored (4,258 actually on disk)

- **Paper claim** (3 sites):
  - Abstract L68: "Cobaya v3.6.1, 424,781 samples across three dataset combinations"
  - §III L184: "plus an ongoing Planck-only run (114,992 raw samples). Total MCMC program: 424,781 raw samples across 3 dataset combinations."
  - §VII Table III L480: `Planck-only & 114,992 & ~0.05 & Ongoing`
  - §VII.A L496: "176,840 + 132,949 + 114,992 = 424,781 accepted samples"
- **On-disk reality**:
  - `reproducibility/cosmology/planck_only_live_sync/chain_{01..06}/spin_torsion.1.txt`: 708, 679, 678, 699, 727, 767 rows → **4,258 total**.
  - `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/planck_only/chain_{01..06}/spin_torsion.1.txt`: 68, 77, 83, 64, 74, 86 rows → **452 total** (these are stub/early-restart files).
  - Recursive `grep -r "114992\|114,992"` over `reproducibility/` returns zero source anchors. All matches are random substrings inside row data (e.g., `0.018114992`).
  - `convergence_latest.csv` contains rows only for `full_tension` and `planck_bao_sn`. **No `planck_only` convergence record exists.**
- **SSOT note**: `project-context/SSOT/paper-1/status.md` itself flags this as `<third-combo>` and reproduces `114,992` only as inheritance from the paper, not from a chain artifact. This is the same pattern flagged in P1A tick-3 DeepSeek.
- **Severity**: BLOCKER. The abstract's `424,781` is the headline reproducibility number of the paper; ~26 % of it has no on-disk source.
- **Fix**: Replace `114,992` with the live on-disk count from `planck_only_live_sync/` (4,258 as of this audit), and re-derive the abstract total. Either (a) state honestly "two frozen combinations (309,789 samples) + one ongoing Planck-only run (~4,258 raw, not yet frozen)", or (b) drop the Planck-only row from the headline total and report it separately as `In progress`.

### B2. §VII.A L496 arithmetic chain is downstream of B1

- **Paper claim**: `(176,840 + 132,949 + 114,992 = 424,781 accepted samples) do not include free w_0 w_a as a sampled parameter`. This sentence is the entire textual anchor for the `‡` cross-paper footnote in Paper I(a) Table II.
- **On-disk reality**: The arithmetic is internally consistent (176,840 + 132,949 + 114,992 = 424,781 — verified), but the third addend `114,992` is unanchored (B1). Sum of real-on-disk chain rows: 176,240 (full_tension frozen) + 132,949 (planck_bao_sn frozen) + 4,258 (planck_only live-sync) = **313,447**, not 424,781.
- **Severity**: BLOCKER (load-bearing for the cross-paper anchor; if the number is fictitious, the anchor is fictitious).
- **Fix**: Rewrite §VII.A to reference only the two FROZEN datasets (309,789 samples) as the relevant scope-of-claim for the `w_0 w_a` non-inclusion; remove the Planck-only addend from the sum, since the ongoing chain is precisely the situation the §VII.A "no posterior at all" disclaimer already addresses.

---

## MAJOR findings

### M1. Stale "~109 accepted, 1-3 days out" state — already corrected in P1A R-round-3, not propagated to P1B

- **Paper claim** (3 sites: L481, L504-505, L555-556):
  - Table III row 4: `DESI DR2 w0wa (new) & ~109 accepted & >0.1 & Running`
  - §VII.A.ii: "currently running on Pod~3 H200 with ~109 samples accepted as of 2026-05-08 18:27 PT and R̂−1 ≈ 0.076. Publication-quality convergence (R̂−1 < 0.01) is still 1-3 days out"
  - §Conclusions: "109 accepted samples as of 2026-05-05, ~3-day ETA to convergence"
- **SSOT reality** (`project-context/SSOT/index.md` "Last authoritative update 2026-05-13 15:30 PDT"): P1A v1A.0.19→v1A.0.20 R-round-3 BLOCKER closure already rewrote this footnote because *"the actual live chain has accumulated 37,761 samples and R̂−1=0.0315 (5/13 20:35 UTC)"*. P1A now reads `~3.8×10⁴ accepted samples across 16 chains, R̂−1≈3×10⁻² descending monotonically`. P1B still carries the v1A.0.18-era text in all three locations.
- **Severity**: MAJOR. Same confabulation pattern that 3 cross-vendor reviewers flagged on P1A; if P1B ships without this correction, it inherits the same blocker tag.
- **Fix**: Mirror P1A's reframe verbatim — replace the `~109` figure and `1-3 days` ETA with the SSOT phrasing (`~3.8×10⁴ accepted samples across 16 chains, R̂−1≈3×10⁻² descending monotonically toward target R̂−1<10⁻² at slow-mode-dominated rate; we deliberately do not commit to a calendar date for convergence`) in all three sites.

---

## MINOR findings

### m1. Full-tension chain-row sum is 176,240, not 176,840

- **Paper claim**: 176,840 raw accepted samples for full-tension (abstract, §III L184, Table I L213, Table III L478, §VII.A L496).
- **On-disk reality**: Direct `grep -vc '^#'` on `reproducibility/cosmology/frozen/full_tension_20260311_1728/chains/chain_{01..06}/spin_torsion.1.txt` sums to **176,240** (15,054 + 14,817 + 14,700 + 14,670 + 14,532 + 102,467). The figure `176,840` is recorded in `diagnostics/freeze_diagnostics_CORRECTED.json` as `"total_accepted_samples": 176840`, so the paper IS citing the freeze artifact correctly — the 600-row gap is between the freeze diagnostic and the raw chain rowcount (likely a post-freeze trim/dedup or a checkpoint-vs-file discrepancy). Not a confabulation, but the freeze diagnostic disagrees with the chain files by ~0.34 %.
- **Severity**: MINOR. Within rounding of the headline; flagging only for transparency.
- **Fix**: Either accept the freeze-diagnostic figure (status quo) or add a one-line footnote pointing to the diagnostic JSON as the source-of-record.

### m2. `convergence_latest.csv` does not contain Planck-only or planck_bao rows

- **Paper claim**: Table III L480 reports `Planck-only ... R̂−1 ~ 0.05 ... Ongoing`.
- **On-disk reality**: `reproducibility/cosmology/convergence_latest.csv` contains only `full_tension` and `planck_bao_sn` dataset rows. There is no `planck_only` convergence entry. The `~0.05` R̂−1 figure is therefore not traceable to the canonical CSV cited in footnote `fn:rhat_csv` (L214). It may live in a separate diagnostic file, but the paper's footnote pointer does not resolve.
- **Severity**: MINOR.
- **Fix**: Either compute R̂−1 for the planck_only live-sync chains and update `convergence_latest.csv`, or cite the actual source file used to produce the `~0.05` figure in the Table III caption.

---

## Verified clean (no confabulation found)

- **Planck+BAO+SN = 132,949 samples**: exact match. Sum of `frozen/planck_bao_sn_20260312_1954/chains/chain_{01..06}/spin_torsion.1.txt` rows = 21,767 + 22,234 + 22,625 + 21,590 + 21,808 + 22,925 = **132,949** ✓. Also matches `MANIFEST.md` and `convergence_report.txt`.
- **H0 = 67.68 ± 1.06 (full-tension)**: weighted mean of chain_01 (weight column 2, H0 column 22) yields 67.6691 — consistent with the paper's 67.68 across all 6 chains. ✓
- **Full-tension worst R̂−1 = ns = 9.74×10⁻⁴**: `convergence_latest.csv` shows `full_tension,ns,...,Rhat_m1_all=0.000974`. Footnote `fn:rhat_csv` matches the CSV exactly. ✓
- **Planck+BAO+SN worst R̂−1 ≈ 0.001 (paper rounds to 0.003)**: `convergence_latest.csv` shows `planck_bao_sn,delta_neff,...,Rhat_m1_all=0.000971` ≈ 0.001. Paper says 0.003 which is loose-rounded but not wrong; all params still < 3×10⁻³. ✓
- **NaMaster β=0.27° injection → 0.238° recovery, SNR=20.32**: `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json` → `"recovered_beta_deg": 0.238`, `"snr_namaster": 20.315591`, `"bias_deg": 0.032`. Exact match. ✓
- **β=0.342° → 0.302°, SNR=25.71**: same JSON → `"recovered_beta_deg": 0.30200000000000005`, `"snr_namaster": 25.707268`. Exact match. ✓
- **β=0.342°±0.094° Eskilt cite**: `references.bib` has `@article{Eskilt2022, ... PRD 106, 063503, 2022, doi 10.1103/PhysRevD.106.063503}` and `Eskilt2022b` flagged in-bib as alias of `Eskilt2022`. Verified canonical 3.6σ paper. ✓
- **DiegoPalazuelos2025 ACT DR6 cite**: `references.bib` → `arXiv:2509.13654` (ACT DR6 cosmic birefringence). ✓
- **NaMaster pipeline config (Nside=512, lmax=1024, f_sky=0.3226, 500 MC, noise 10 µK·arcmin)**: all match summary.json exactly. ✓
- **Abstract arithmetic 176,840 + 132,949 + 114,992 = 424,781 and 176,840 + 132,949 = 309,789**: internally consistent ✓ (but third addend is unanchored — see B1).

---

## Summary

P1B v1B.0.3 is **mostly clean** on numerical anchoring — NaMaster numbers exact-match, H0 / R̂−1 / ΔNeff / chain sums for the two FROZEN dataset combinations all reconcile to within rounding, and all literature citations verify. The two BLOCKERs and one MAJOR all trace to the same underlying problem: the third dataset combination (`Planck-only`) is reported as a 114,992-sample contributor to the headline 424,781 total when the actual on-disk live-sync chains carry 4,258 rows and no `convergence_latest.csv` entry exists for it; and the DESI DR2 w0wa Pod 3 cross-paper anchor still carries the v1A.0.18-era "~109 accepted / 1-3 days out" language that P1A R-round-3 has already rewritten to "~3.8×10⁴ samples / R̂−1≈3×10⁻²". Both are the same class of confabulation (stale or unanchored MCMC state) and both are fixable by aligning P1B prose to the SSOT-canonical state.

Once B1, B2, and M1 are closed, P1B's numerical layer is publication-quality with respect to on-disk reproducibility — the verified-clean column above is substantial and the deconvolution pipeline validation is anchored exactly.
