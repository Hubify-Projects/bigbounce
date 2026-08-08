# P5 INT — FINAL pre-sign-off full-source referee review

- **Paper:** P5 v0.1.102-2026-07-06 — `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
- **Reviewer:** Claude Code INT leg (Houston subscription), full source + committed-output access
- **Date:** 2026-07-06
- **Repo HEAD:** 6ab357a75a54f136f13d851368b24704b8a06a53
- **Mode:** read-only; NO .tex edited. Verified headline numbers against committed CSV/JSON.

## VERDICT: ACCEPT — publish-ready confirmed. No genuinely-new real finding.

Compile clean: 37 pages, 0 undefined references (the single log "undefined" hit is a benign
`OMS/cmtt/m/n` font-shape warning, cosmetic auto-substitution — NOT a ref/cite), no overfull
hbox >20pt. `\paperIVarxiv` = `arXiv:XXXX.XXXXX` renders sanely inline on p.1
("...(arXiv:XXXX.XXXXX, posted concurrently under coordinated submission..."). SUBMISSION_NOTE
is coherent and accurate (single-macro swap procedure, P4-first same-day submission).

## Number verification against committed outputs

| Claim (file:line) | Paper value | Committed source | Match |
|---|---|---|---|
| T-Web void bin (L714) | n=428, f_CW=0.4836, −0.68σ | `cw_fraction_by_env__desi_env_vweb.csv` void 428/0.48364/−0.6767 | ✓ |
| wall (L713) | n=6,673, 0.5034, +0.55σ | CSV 6673/0.50337/+0.5509 | ✓ |
| filament (L711) | n=408,187, 0.4980, −2.61σ | CSV 408187/0.49796/−2.606 | ✓ |
| cluster (L712) | n=397,505, 0.4963, −4.66σ | CSV 397505/0.49631/−4.658 | ✓ |
| DESIVAST VoidFinder (L765,L795) | n=56,981; f_void=0.4964; f_nonvoid=0.4971; Δ=+0.0007 | `desivast_three_algorithm_void_chirality.json` n_in_void=56981; 0.49641/0.49709; Δ=0.00068 | ✓ |
| VoidFinder holes (L792) | 101,863 | JSON n_voids_catalog=101863 | ✓ |
| Low-z matched parent (L672) | 678,945 z≤0.24 | JSON matched_spirals_z_leq_0p24=678945 | ✓ |
| Three-algo robustness (L808–817) | \|Δf_CW\|≤0.004 across 5 defs; largest 0.0037, \|z_Δ\|=1.25, p=0.21 | 3 sphere-PIS (JSON) + 2 GALZONE (30_ext4 artifact); largest V2-REVOLVER native 0.0037 | ✓ |

## New macro + GZ1 null (this round's additions) — verified accurate

- `\paperIVarxiv` macro (L24) resolves through every P4 reference (abstract, §Relation-to-P4,
  Data, limitations, App A, bib, arXiv comments) via one line; placeholder renders correctly.
- GZ1-human-null cite (L620): "z=−0.54σ (N=46,017)" — verified against
  `pipelines/p2_chirality/outputs/gz1only_fullN_dipole_result.json`:
  n_matched_to_desi=46017, z_sigma=−0.539, cw_fraction=0.48358, "NO learned model in the
  chirality label chain". Cite is exact and model-independence claim is honest.

## Referee notes (no action required)

- Monopole-shift invariance of the headline Δf_CW is stated correctly and repeatedly; the result
  does not depend on the P4 monopole amplitude. Sound.
- Void bin sample-size limit (n=428 T-Web; controlling constraint from DESIVAST n=56,981
  re-projection) honestly framed as a bounded upper limit, not a precision constraint.
- "Five void definitions" = 3 sphere-PIS + 2 catalog-native GALZONE; explained in text (L808–817),
  internally consistent with the two artifacts.

**No [MAJOR] or [MINOR] findings.** Publish-ready.
