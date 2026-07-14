# P2 M44 non-Anthropic INT truth audit

**Paper:** P2 `v1.7.116`, `research/focused_paper_source_integration/02_full_draft.tex`
**Raws read verbatim:** `API_P2_openai.md`, `API_P2_grok.md`, `API_P2_gemini.md`
**Verdicts preserved:** OpenAI/gpt-5.5 **REJECT** (15 major, 7 minor); Grok/grok-4.3 **MAJOR REVISIONS** (3 major, 2 minor); Gemini/gemini-3.1-pro-preview **MINOR REVISIONS** (2 major-tagged, 3 minor).
**Policy:** ledger-first against `DISPOSITIONS/P2.md`, but not ledger-deferential when recomputation falsifies a prior disposition. No Anthropic leg used. No source, ledger, version, status, site, or canonical artifact was edited by this audit.

## Truth verdict

This wave contains **one genuinely new reader-visible/logic correction** and **one genuinely new non-reader-visible artifact-hygiene correction**:

1. **Exact-shape uniqueness; prior DP2-15 dismissal superseded.** OpenAI O7/O8 is substantively correct. Re-expanding the committed exact four-vertex sum from `scripts/p2_vertex_check.py` in the paper's own ordered symmetric monomial basis gives the unique coefficient vector

   `c_exact = (3, 1, -9, 5, -33, 9)`.

   The `-33` is required because the ordered `(5,2,2)` orbit contains each distinct monomial twice; it produces the expanded `-66 k_i^5 k_j^2 k_l^2` terms. The existing reference `(2,7,3,-12,-69,19)` is merely one polynomial fitted to three old benchmark values. Sampling its three-dimensional algebraic null space is therefore **not a physical theory uncertainty** once the full vertex expressions are used. The prior DP2-15 disposition calling this only a methodological disagreement is **superseded by this recomputation**, not silently overwritten.
2. **Cited Wick-script status string.** `appendix_A1_wick_doubling.py` correctly verifies `i<[A,B]>=-2 Im<AB>`, six Wick permutations, and four vertices, but its final print string incorrectly calls this the factor between Li and Cai. The paper correctly states that both works use the full commutator and that this identity does not adjudicate their extracted-amplitude discrepancy (`02_full_draft.tex:1638-1692`). This is a genuine cited-artifact PROCESS-NIT, not a reader-visible math error.

The central exact amplitude remains verified: `f_NL^sq=-35/16`, `f_NL^eq=-255/128`, Li Eq. (5.1) at `c_s=1` gives `-35/16`, while the transcribed printed polynomial reduces to `-305/64`. The new exact-shape correction changes the same-grid overlap only from `r=0.8468969` to `r=0.8354229` (shape cosine `0.9849470` to `0.9816783`), which remains inside the published noise-weighted `r=0.84+/-0.02`. Thus the headline amplitude and sensitivity do **not** fail from this correction alone; the null-space uncertainty narrative does.

Standing real limitations remain: third-order bounce transmission is verified only linearly and then bounded by a single-clock/gradient argument (DP2-13); the headline is a heterogeneous sensitivity recast rather than a single joint-covariance forecast (DP2-04/-17/-29); the additive systematics and `b_phi` prior are not a full external-survey joint Fisher (DP2-07/-22/-26/-34); MegaMapper is uncalibrated (DP2-30); and Bayes factors are prior-volume illustrations (DP2-18).

## Matcher triage

`tools/ledger_match.py` parsed 22 OpenAI rows (15 matched, 7 unmatched), 7 Grok rows (5 matched, 2 unmatched), and 7 Gemini rows (4 matched, 3 unmatched). Four unmatched rows were parser scaffolds (`REVISIONS` / `ISSUES`), not findings. The eight real unmatched findings were OpenAI O13, O15-O18, O20-O21 and Gemini Gm1; every one is source-dispositioned below. Low-score false matches were manually corrected, notably OpenAI O4/O5/O10/O12 and the Gemini header-date row.

## Exact recomputation and immutable evidence

Commands run:

```text
python3 research/focused_paper_source_integration/scripts/p2_vertex_check.py
python3 research/focused_paper_source_integration/scripts/caili_certification/{cai_vertices,cai_shape,cai_conv,final_check}.py
python3 research/focused_paper_source_integration/appendix_A1_wick_doubling.py
python3 research/focused_paper_source_integration/scripts/c13_independent_bounce_fisher.py
python3 research/focused_paper_source_integration/scripts/c15_channel_native_fisher.py
```

- Exact-fraction outputs: six-permutation basis gives squeezed `-35/16`, equilateral `-255/128`; Li at `c_s=1` is `-35/16`; `A_total-A_T=(99/128) sum k_i^3`; printed `A_T` gives squeezed `-305/64`.
- Independent symbolic coefficient extraction used `P_exact=(256/3)(k1 k2 k3)^2 A_total` and solved `P_exact=sum c_i M_i`, giving uniquely `(3,1,-9,5,-33,9)`.
- Direct 300x300 triangle-ratio grid (same 23,098-configuration convention): old-shape `(r,r_cos)=(0.8468969,0.9849470)`; exact shape `(0.8354229,0.9816783)`.
- C13 rerun reproduced multi-tracer `sigma_local=0.626/0.687`, `sigma_bounce=0.632/0.689`, `r_eff=0.992/0.998` and `3.46/3.18 sigma` for `-35/16` under its current old-shape normalization.
- C15 rerun reproduced `alpha=0.9916`, native cosine `0.9998`, `rho(f_NL,A_GR)=-0.4246/-0.4944`, 30%-`b_phi`-prior `sigma=0.942`, and `2.32 sigma`.
- C14 was rerun through its first two stages (`sigma_local=0.4487`, `sigma_bounce=0.4493`) but stopped during the expensive primordial-only third stage at the root deadline; no output file was overwritten. This partial rerun is not claimed as a completed certification.

Selected SHA-256 provenance:

- `p2_vertex_check.py`: `6fca53a97c196bc5cf35061cd334e36537c2f1ff0b836f0e8331f008d5ead06c`
- `cai_vertices.py`: `e0d06bd3a195eab6c8c86aaa943e805f59596f28744b4db193cb147984a02849`
- `appendix_A1_wick_doubling.py`: `8e1af53949165a5420639a657bb081ea618d007398b0ae1ec2b96f99cd62d0c7`
- `null_space_analysis.py`: `9c9bef8db1a2dcc3297a3a900d776a6673f22884c08fb49504e1626e5f7ee18d`
- `fig_4vertex_sum.py`: `9c2bcefecb74d089d0430121fc8c49599dd2ac24d6327d813f92f452b1542f92`
- canonical outputs left byte-restored: C13 `f0238cb6252423244f3e555ed9841b3bc47ec7fbf83b7c71a0a70b285a64c06f`; C14 `84ab244e68a66cda3e38f91c42fea4bff7fce6e265bce37173932341381eaee9`; C15 `a34303cc90dc92fc6b9f861697591c2ce9e598c35f768e2f739efae72e7d642c`.

## OpenAI — 22/22 substantive findings preserved

| # | Disposition |
|---|---|
| O1 | **Real standing scope limit, DP2-04/-17/-29.** The source explicitly says the `1.3-2.75 sigma` endpoints are heterogeneous sensitivity envelopes, not one self-consistent forecast (`975,984,1512`). REJECT remains valid as a venue judgment. |
| O2 | **Standing DP2-14/-17/-29.** A scalar template projection cannot replace the unavailable full Heinrich covariance. The paper discloses this and labels the result a recast; the independent Fisher is a validation, not the headline source (`984,1167-1169`). |
| O3 | **Standing DP2-14, affected by the new exact-shape correction.** `r` and `r_eff` are different metrics and are explicitly reconciled (`1167`), but both old-shape calculations should be rerun with `c_exact`; the direct overlap shift is small. |
| O4 | **Real standing DP2-13.** No explicit third-order bounce-mode-function integral exists; the `<=10^-3` bound is a conditional single-clock gradient argument. |
| O5 | **Real standing claim-discipline issue, DP2-13.** The paper says “closed/derived” at cubic order while also saying verified only linearly (`984,990,1512-1515,1527`). Safest wording is conditional until third-order matching is computed. |
| O6 | **Math verified; publication-standard/literature-reconstruction concern DP2-01/-02/-16/-25.** Exact scripts and displayed Appendix A reproduce `-35/16`; Cai's separate `-35/8` remains unreconstructed from his printed coefficients. |
| O7 | **GENUINELY NEW validated correction; supersedes prior DP2-15 dismissal.** The exact vertex sum fixes unique `(3,1,-9,5,-33,9)`; the claimed physical three-dimensional null space is an artifact of discarding the full vertex information and fitting only three benchmarks. |
| O8 | **Same new correction.** Uniform sampling in the artificial coefficient ball is not an invariant or physical theory uncertainty. Remove/reclassify `r=0.85+/-0.13` and its percentiles; retain the exact-shape overlap. |
| O9 | **Standing DP2-18.** Bayes factors are prior-volume illustrations around a mock centered on the bounce; the paper says so (`1512,1529`). They are not real-data model-selection evidence. |
| O10 | **Real standing DP2-04/-07/-26/-34.** Additive quadrature is a labeled scoping heuristic, not a joint covariance (`1332,1434,1512`). |
| O11 | **Standing DP2-07/-34/-35.** The transferred `-0.868`, shape `0.95`, and channel-native `-0.42/-0.49` numbers are different metrics; source labels them as such. No defensible quantitative lower floor exists on the unpublished Heinrich covariance. |
| O12 | **Standing DP2-22/-26/-34.** Hand-widening `0.7` to `0.9/1.0` is not the same as nuisance marginalization. C15 shows the 30% prior result and the free-`b_phi` no-prior limit (`sigma=5.217`); the headline remains prior-conditional. |
| O13 | **Standing DP2-30.** MegaMapper is explicitly “illustrative/uncalibrated/speculative” yet remains in title/abstract/figures. That is a real venue/presentation risk, not a new numerical error. |
| O14 | **Standing DP2-20.** `kappa_epsilon=2.8-40` is a schematic range, not a derived consistency relation. Source discloses its theory uncertainty. |
| O15 | **Real standing DP2-17/-22/-29.** The paper lacks an end-to-end survey bispectrum likelihood with complete bias/RSD/window/non-Gaussian covariance; it is a recast plus leading-order checks. |
| O16 | **DP2-30 venue opinion.** Length/repetition is real and repeatedly flagged. |
| O17 | **DP2-32/-30.** Abstract is now one paragraph but remains dense; editorial, not math. |
| O18 | **DP2-14/-31.4.** Notation is defined once at `984`; residual readability is editorial. |
| O19 | **DP2-21.** Gauge versus conformal-Fermi roles are explicitly separated (`986,1527`); simplification is editorial. |
| O20 | **DP2-04/-15/-30, now affected by the new correction.** Any figure showing null-space percentiles or old-shape “uncertainty” must be corrected; plotted headline significances remain conditional envelopes. |
| O21 | **DP2-16/-27/-30.** Code cannot substitute for equations. Appendix A contains substantial algebra, but DP2-27 reproducibility hygiene remains open and the new Wick-string inconsistency confirms artifact QA is needed. |
| O22 | **PROCESS/venue opinion.** AI disclosure does not validate science; independent derivations and source checks must. No quantitative claim is accepted because an AI checked it. |

## Grok — 5/5 substantive findings preserved

| # | Disposition |
|---|---|
| G1 | **DP2-04/-07/-17/-29.** Mixed null procedures and unavailable external covariance are explicitly disclosed; quoted sensitivity is not a unified forecast. |
| G2 | **Real standing DP2-13.** Cubic transfer remains conditional on the single-clock/gradient argument, without an explicit third-order integral. |
| G3 | **DP2-18.** `BF~9-14` is prior-sensitive and illustrative; any claim beyond qualitative prior-conditional discrimination is unsupported. |
| G4 | **DP2-01/-02/-16/-25 plus DP2-27.** Exact `-35/16` is reproducible, but a self-contained literature-correction presentation and per-vertex script output remain legitimate requests. |
| G5 | **DP2-30.** Length/incremental-content judgment; no new numerical defect. |

## Gemini — 5/5 substantive findings preserved

| # | Disposition |
|---|---|
| Gm1 | **DP2-30 real presentation issue.** Main text contains many internal filenames. Moving most to Data/Code Availability is editorially reasonable. |
| Gm2 | **DP2-04/-07/-22/-26/-34.** Additive quadrature is not statistically equivalent to full nuisance covariance. C15 is an in-house surrogate check, not the external Heinrich joint Fisher. |
| Gm3 | **DP2-18.** Abstract should name the adopted competitor-prior width or reduce the BF to qualitative wording. |
| Gm4 | **DP2-01/-30.** Streamlining the literature-dispute tone is editorial; exact arithmetic remains reproducible. |
| Gm5 | **Not a defect.** `date{July 12, 2026}` matches the `v1.7.116` revision date (`lines 34-35`). A manuscript date need not equal the day a later reviewer reads it. No change warranted solely for “present date.” |

## DP2-27 / DP2-28 hygiene status

- **DP2-27 remains OPEN-COMPUTE and is confirmed.** `p2_vertex_check.py` prints only total squeezed/equilateral values, not the four `tab:vertexwalk` rows. C13/C14 raw stdout is not frozen as a cited third-party verification artifact. This is non-blocking for the already reproducible totals but should be closed in the next hygiene pass.
- **DP2-28 remains OPEN-COMPUTE and is confirmed.** `scripts/fig_4vertex_sum.py` still hard-codes `-35/8` throughout and has no deprecation marker. It is not referenced by any live `includegraphics`, so the rendered PDF is not directly corrupted. The broader exact-shape correction now requires auditing `null_space_analysis.py`, `phase3_bispectrum_shape_overlap.json`, C13-C15 shape metadata, and any generator using `(2,7,3,-12,-69,19)`—not just deprecating this one stale generator.

## Required correction scope (not executed here)

Reader-visible/source locations affected by the exact-shape correction include `02_full_draft.tex:990,1001-1005,1025,1028,1030-1044,1050-1051,1080,1313,1434,1512,1536`, including the coefficient/underdetermination prose, null-space distribution and propagated percentiles, Fig. 1 shape provenance/caption, systematics-table null-space row/caption, BF-table null-space note, caveat summary, and Data/Code Availability. Audit/rebuild any other figure that plots the null-space band or old printed shape, especially the decision-threshold presentation near Fig. 4.

Computational scope: replace benchmark-fitted shape coefficients with `c_exact`; remove the physical-null-space interpretation; rerun template overlaps, C13-C15, derived JSON/figures/tables; correct the Wick artifact status string; close DP2-27 and deprecate DP2-28; then version-bump, recompile, run the mandatory LaTeX/PDF visual audit, mirror PDFs, update SSOT/Convex/site in the same coherent commit, and obtain fresh non-Anthropic review. None of those edits were made in this truth-audit lane.
