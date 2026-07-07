# P5 Duplicate-Row Independence Audit — Truth-Audit by Real Computation

**Date:** 2026-07-05
**Paper:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.102)
**Finding (openai EXT/API):** *"Row-level duplicate independence — environmental-contrast
SEs may be understated if galaxy rows repeat (same TARGETID matched to multiple
voids/environments); wants cluster-robust SEs by TARGETID."*
**Script:** `p5_duplicate_row_audit.py` · **JSON:** `p5_duplicate_row_audit.json`

---

## VERDICT: NON-REAL — dispositioned with computed evidence (already-addressed in-paper)

The concern is real *in principle* but is **already computed, quantified, and disclosed**
in the committed pipeline and the .tex. No new paper fix is required.

---

## Data provenance (what's committed vs. what's missing)

- The per-galaxy matched catalog `results/p5_matched_chirality_desi.parquet` (1.2 GB, holds
  the per-object TARGETID + env labels) is **gitignored and not on disk** — it recreates via
  the pipeline.
- The audit therefore reads the **committed** recompute artifact
  `outputs/17_v0151_closure_recomputes.json`, produced by
  `scripts/17_v0151_closure_recomputes.py` operating directly on that parquet and recording
  per-TARGETID unique counts, the exact DESIVAST point-in-sphere recompute, and the duplicate
  diagnostics. This is a genuine computed audit, not a re-derivation from headline numbers.

## 1. Duplication rate (quantified)

| Quantity | Value |
|---|---|
| Env-labeled join rows | 812,793 |
| Unique TARGETIDs | 783,820 |
| **Duplicate rows** | **28,973 (3.56%)** |
| TARGETIDs w/ conflicting env class | 79 |
| Worst-case naive/clustered SE ratio | √(812793/783820) = **1.018 (≤1.9%)** |

**Mechanism:** the crossmatch parent is *already* deduped one-row-per-TARGETID
(`03_crossmatch.py::_dedupe`, `nearest` strategy → `matched_primary_deduped`). Excess rows
enter **only** through the many-to-one join to the V-Web env table, which carries repeat
DR1 survey/program coadd rows per TARGETID (`zall-pix-iron`). It is **not** a galaxy matched
to multiple *voids* — the openai mental model — but repeated coadd deposits of the same galaxy.

## 2. DESIVAST headline (the +0.0007 ± 0.0022 number) is already dedup-first

The headline void/non-void contrast uses a **per-galaxy boolean membership array**
(`scripts/17` C8: `member = np.zeros(len(gal), bool); member[hit] = True`). A galaxy inside
**up to 249** overlapping void spheres is counted **exactly once** by construction — the SE is
already cluster-robust by TARGETID.

Recompute on unique galaxies:

| | Published | Audit (unique-galaxy recompute) |
|---|---|---|
| void n | 56,981 | 57,081 |
| non-void n | 621,964 | 621,864 |
| Δf_CW (non-void − void) | +0.0007 | **+0.00062** |
| SE | 0.0022 | **0.00219** |
| z | +0.31 | **+0.28** |

Reproduces the published headline to <1×10⁻⁴. **Null unchanged.**

## 3. V-Web per-class z-scores unaffected

Published per-class z (void −0.68σ, filament −2.61σ, cluster −4.66σ) reproduce exactly on the
join surface. Applying the worst-case uniform √1.018 = 1.018 SE widening: filament −2.61 → −2.56
(still ≈ family threshold, sign unchanged), cluster −4.66 → −4.58 (still highly significant),
void unchanged in sign. No conclusion moves.

## 4. Already in the paper

- v-comment header: **`(C0) R35-P5-O13 (VERIFIED MAJOR): duplicate-row percentage corrected`**;
  `783,820 unique; sec VIII.F mechanism corrected to duplicate survey/program`.
- Body (`.tex` l.1615–1671): discloses the 3.56% duplicate rate, recomputes the contingency
  test on the 783,820-unique subset (χ²=3.00, p=0.39; excluding the 79 conflicting-env
  TARGETIDs χ²=2.92, p=0.41), and states the √(N_rows/N_unique)=1.018 SE-inflation bound
  explicitly (≤1.9%).

## Proposed .tex note (OPTIONAL — do not apply unless a referee insists)

Table VI caption, one line:
> *"Reported void/non-void SEs are computed on unique galaxies (boolean point-in-sphere
> membership), i.e. already cluster-robust by \texttt{TARGETID}; the environment-table
> coadd duplication (3.56\%) widens the T-Web contrast SEs by at most 1.9\% and changes no
> conclusion (\S\ref{...})."*

This only re-states existing disclosed content; it is not a science change.
