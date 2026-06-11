---
title: "Paper 5 SSOT — Environmental Dependence of Spiral Chirality Across DESI LSS"
type: ssot
paper: 5
last_updated: 2026-06-10 PDT, late evening (R29 post-EXT1 internal-round closure wave + restamp — v0.1.61 -> v0.1.62-2026-06-10, commit fedad007; 30 pp / 0 errors / 0 undef / md5 1df816c5; Wald-shift bound corrected <=0.01 -> <=0.12 SE with per-class values; void-fraction denominators disambiguated; readiness holds 95. R30conf pending, then EXT2. Prior: EXT1 closure wave + restamp — v0.1.60 -> v0.1.61-2026-06-10, commit a39d98ba; 30 pp / 0 errors / 0 undef / 0 overfull / md5 5eb81cd5; 2 new tables (analysis-tree promoted to table*, DESIVAST program split); phase2_sweep dir links fixed /blob/->/tree/ + 18 metadata files committed; readiness 95 cap. EXT2 confirmation round pending; 95-cap until clean external round + Houston sign-off.)
canonical_source: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
canonical_pdf: pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf (30 pp / 0 errors / 0 undef refs / md5 1df816c5; mirrored to site/public/papers/p5_desi_chirality_v0.1.61.pdf)
version: v0.1.62-2026-06-10 (R29 internal-round closure wave; md5 1df816c5 / 30 pp / 0 errors / 0 undef refs; mirror site/public/papers/p5_desi_chirality_v0.1.62.pdf). Prior: v0.1.61-2026-06-10 (EXT1 closure wave; md5 5eb81cd5 / 30 pp / 0 errors / 0 undef refs; mirror site/public/papers/p5_desi_chirality_v0.1.61.pdf). Prior: v0.1.60-2026-06-11 (R26conf closure wave; md5 642b4807 / 27 pp / 0 errors / 0 undef refs; mirror site/public/papers/p5_desi_chirality_v0.1.60.pdf). Prior: v0.1.56-2026-06-10 (pod-session wave; md5 4061bf5c). Prior: v0.1.55-2026-06-10 (unique-TARGETID parent rebuild wave; md5 d07c14e8). Earlier: v0.1.54-2026-06-10 (R24conf closure wave; md5 1d42599a). Earlier: v0.1.53-2026-06-09 (R23conf closure wave; md5 b86b03f9). Earlier still: v0.1.44-2026-06-03 (R-upgraded-round9 closure bundle: title retitled to lead with DESIVAST primary path; "strongest/largest-sample" wording softened; RSD anisotropic-eigenvalue reframing 3-way; PER-M1 abstract DESIVAST scope tightened; GEM-m1 "any future model" scoped to bounce-chirality coupling class @ 25 Mpc/h; §XI.B retitled; 380-line preamble changelog stripped & archived. Cascaded-exit counter rolled back to 0/3 per synthesis; next round = R-upgraded-round10. Toy EFT appendix RETAINED with v0.1.41 caveat per Houston decision.)
headline_pct: 95
submission_status: PAPER R-ROUND-CLEAN per AGENT_RULES §4.4.1 cascaded-loop-exit criterion (cron fires #25 / #33-#36 / #40-#41 / #43-#45 / #47 / #49 / #51 / #53 / #57 / #60 / #62 / #64-#67, ticks 146-189). Internal Claude R1 review (fire #64) returned 0 BLOCKER / 4 MAJOR / 4 minor / 4 nit; all 12 findings closed across fires #64/#65/#66. Internal Claude R2 verification (fire #67) returned 0 BLOCKER / 0 MAJOR / 3 minor / 3 nit — meets §4.4.1 ≤1-2 polish MAJOR threshold. R2 caught a critical computational error in fire #64's cluster-side joint-z claim (had used full matched-sample bright/dark n instead of cluster-restricted; correct cluster joint z=−0.52σ NULL); paper honestly corrected at v0.1.26 abstract to attribute joint test to filament class only. PRIOR submission_status enumeration: — 27 pp LaTeX. New since v0.1.18: MAXIMAL voids HEALPix sky-position stratification (fire #53) at NSIDE=16 on 3,765 DESIVAST maximal voids, stratifying z≤0.24 matched-spiral subsample (n=678,945) by void count per HEALPix pixel. **CATALOG-LEVEL −5σ HEADLINE IS CONCENTRATED ENTIRELY IN "0 MAXIMAL VOIDS PER PIXEL" BIN (n=378,511 σ=−4.75) — sky regions OUTSIDE DESIVAST coverage**; pixels WITH maximal voids return σ ∈ [−2.04, −0.09] all below Bonferroni-4; cleanest measurement is 3-5-voids/pixel bin at σ=−0.09 NULL on n=23,127. **Signal tracks survey-mask geometry, NOT environment density** — 5th independent positive evidence line for headline environment-independence. The 5 independent positive evidence lines = publication-grade robustness (DESIVAST per-galaxy + within-class density + DESIVAST-anchored clean null + 3-algorithm robustness + catalog-native V2 GALZONE + sky-position maximal voids). Cluster −4.7σ now SIX-decomposed — 26 pp LaTeX. New since v0.1.17: filament-class within-class decomposition (fire #51) mirroring the cluster-class fire #41+#43+#44 analysis on the 2nd-largest V-Web class (n=408,187). Filament z-quartile σ all in [−1.72, −0.55]; density-quartile σ all in [−0.63, −1.97]. **Filament tracer-program REPRODUCES cluster bright-vs-dark sign-flip**: bright (n=416,701) σ=−2.80 vs dark (n=21,203) σ=+2.85, opposite sign with comparable magnitudes — even cleaner sign-flip than the cluster (filament-dark has both larger n AND larger magnitude than cluster-dark). The sign-flip recurrence across the two largest V-Web classes is the strongest sign in the paper that V-Web class-level f_CW deviations are sourced by BGS-selection-function-conditioned imaging-leg systematics, NOT environment-driven astrophysics. PDF 904 KB / 29 pp / 0 overfull / 0 undef refs / 0 undef cites. v0.1.20 additions (fire #57): per-pixel Pearson r(N_voids/pix, σ_chirality/pix) = +0.006 (p=0.88) + new Mollweide sky-map figure. v0.1.21 additions (fire #60): abstract refresh appended Robustness block (~25 lines). v0.1.22 additions (fire #62): **cross-survey P4-monopole-residual analysis** — subtracting the P5 matched-spiral catalog monopole f_CW=0.4972 (= P4 9.5σ catalog monopole propagated into DESI-spectro-confirmed subsample), ALL FOUR V-Web classes fall within |σ_vs_monopole|<1.15 (void −0.56, wall +1.01, filament +0.99, cluster −1.11); per-pixel HEALPix NSIDE=32 residual distribution n=1,821 has mean=+0.020, std=1.184, skew=+0.044 — consistent with pure shot-noise around the catalog monopole. Cleanest single-test publication-grade demonstration that V-Web class σ values are sample-size-weighted projections of the P4 monopole NOT environmental signals. 6th independent positive evidence line. arXiv tarball pre-built + smoke-tested standalone at arxiv/submission_tarballs/p5_v0.1.22_arxiv.tar.gz (577 KB). First R-round blocked on OpenRouter per-key weekly cap. Remaining gates: first R-round + Houston sign-off + arXiv endorsement.
---

# Paper 5 — Environmental Dependence of Spiral Chirality Across DESI Large-Scale Structure — Single Source of Truth

**Canonical status file. When in doubt about Paper 5, read this.**

**🎯 Last authoritative update: 2026-06-11 (PDT) — P5 v0.1.56 → v0.1.60-2026-06-11 — R26conf NOT CLEAN but ZERO ARITHMETIC ERRORS; 9 closures.** R26conf cross-vendor round on v0.1.56: **zero arithmetic errors across the round**; 9 closures landed in v0.1.60, headline item: **code-verified tidal-tensor sign documentation** — the T-Web tidal-tensor sign convention is now documented against the committed code (verified, not asserted). PDF 27 pp / 0 errors / 0 undef refs / md5 642b4807, mirrored to site/public/papers/p5_desi_chirality_v0.1.60.pdf. **Readiness holds 92** (zero-arithmetic-error textual wave; not a clean round). **Close-the-gap: compute-class queue (mask-dilation/randoms rebuilds + footprint re-tabulation, pod-side; #16 completeness-weighted δ still blocked on DESI LSS randoms) → R27conf cross-vendor round clean on v0.1.60 → Houston external round + sign-off → arXiv (last in queue, after P4; tarball rebuilding as paper5_arxiv_v0.1.60.tar.gz — supersedes the v0.1.56 build).**

**🎯 Prior authoritative update: 2026-06-10 (PDT, late night) — P5 v0.1.55 → v0.1.56-2026-06-10 — POD SESSION CLOSED QUEUE #17–19 (stratified Phase-2 LEE + void-membership + z-clamp); #16 randoms-data-missing DOCUMENTED.** Pod-session results: (a) **stratified Phase-2 LEE rerun (#17 CLOSED)** — leg×program-stratified global max-stat p = 0.36 / 0.27, headline null robust under the look-elsewhere stratification; (b) **void membership (#18 CLOSED)** — maximal-sphere vs any-hole membership definitions BOTH null; (c) **z-clamp sensitivity (#19 CLOSED)** — the 1.7<z≤2.0 clamp is a no-op: zero galaxies above z=1.6979 in the matched sample; (d) **#16 (completeness-weighted δ) blocked-and-documented** — DESI LSS randoms not on disk; the data gap is disclosed in-text and the row stays open until the randoms are acquired. PDF 27 pp / 0 errors / 0 undef refs / md5 4061bf5c, mirrored to site/public/papers/p5_desi_chirality_v0.1.56.pdf. **Readiness 91 → 92** (pod queue emptied of runnable substantive items). **Close-the-gap: R26conf cross-vendor round clean on v0.1.56 → Houston external round + sign-off → arXiv (last in queue, after P4; tarball rebuilding as paper5_arxiv_v0.1.56.tar.gz — supersedes the v0.1.55 build).**

**🎯 Prior authoritative update: 2026-06-10 (PDT, evening) — P5 v0.1.54 → v0.1.55-2026-06-10 — UNIQUE-TARGETID PARENT REBUILD CLOSED THE GATING ITEM (R24conf queue #15 CLOSED-LOCAL).** The full T-Web rebuild ran locally in 106 s (no pod needed; zall parquet is local). Row-level rebuild reproduces the published volume fractions to 10⁻⁶ (machinery validated); on the unique-TARGETID parent (14,100,704 of 14,622,283 rows; 3.57% dup), all headline statistics shift by **Δ ≤ 0.70 pp — conclusions unchanged** (environment-independence headline robust to the duplicate-parent axis). Paper text updated + recompiled as v0.1.55. PDF 27 pp / 0 errors / 0 undef refs / md5 d07c14e8, mirrored to site/public/papers/p5_desi_chirality_v0.1.55.pdf. **Readiness 90 → 91** (gating queue item closed; remaining rows pod-only). **Close-the-gap: pod field rebuilds (queue #16–19: completeness-weighted δ, stratified p_LEE rerun, VoidFinder-native membership, z-clamp sensitivity; plus #24 figure regen + #26 ADS pass) → R26conf cross-vendor round clean on v0.1.55 → Houston external round + sign-off → arXiv (last in queue, after P4; tarball rebuilding as paper5_arxiv_v0.1.55.tar.gz).**

**🎯 Prior authoritative update: 2026-06-10 (PDT) — P5 v0.1.53 → v0.1.54-2026-06-10 — R24conf confirmation-round closure wave (full 5-vendor: Claude in-session + OpenAI/Gemini/Grok/Perplexity + meta).** Headline closure: **ZONEVOID zone-offset join bug FOUND + FIXED** (surfaced by queue #23 no-op test) — the published catalog-native GALZONE void counts 86,276/64,514 reproduced exactly only under a zone-offset defect (non-offset NGC+SGC concat; SGC keep-last overwrote NGC); corrected per-cap join gives **104,912 (σ=−0.52) / 74,111 (σ=−1.50)** — **conclusion unchanged** (still null), §VIII.D + abstract corrected with an earlier-draft disclosure. Plus **6 local recomputes closed** (artifact-22 batch, R24conf queue #20/21/22/23/25/27): ASTRA MC variance validation; unique-TARGETID HEALPix σ distribution (mean +0.005 / std 1.015, void correlations all p>0.5); 21-shell N table + cell-level δ stats; EDGE/DEPTH flag shifts ≤0.08 pp all null; boundary-cell fraction 26.6%; NSIDE-64 mask-edge buffer (91.0% quintile-stable, max shift 0.12 pp). PDF 27 pp / 0 errors / 0 undef refs / md5 1d42599a, mirrored to site/public/papers/p5_desi_chirality_v0.1.54.pdf. **Readiness held at 90** — the round found a real (fixed) bug, so it does NOT count as clean.

## Close-the-gap — v0.1.54 (R24conf closure, 2026-06-10)

- **Pod field rebuilds (R24conf queue #15–19)**: unique-TARGETID T-Web density rebuild (#15), randoms/completeness-weighted δ (#16), leg×program-stratified p_LEE rerun + global max-stat (#17), VoidFinder-native membership comparison (#18), 1.7<z≤2.0 clamp sensitivity (#19). Plus #24 figure regen + #26 ADS bib pass.
- **Next cross-vendor round (R25conf wave) must come back clean on v0.1.54** (R24conf found + fixed the ZONEVOID join bug, so it does not count).
- Houston external review round + personal sign-off (final 1%).
- arXiv endorsement + submission (last in queue, after P4; tarball rebuilding as paper5_arxiv_v0.1.54.tar.gz).

**🎯 Prior authoritative update: 2026-06-09 (PDT, evening) — P5 v0.1.52 → v0.1.53-2026-06-09 — R23conf confirmation-round closure wave (full 5-vendor: Claude in-session + OpenAI/Gemini/Grok/Perplexity + GPT-5-Pro meta).** Closures: (a) **Bonferroni misstatement fixed** — the Z3=−3.14 crossing is now disclosed alongside monopole-subtracted residuals; (b) **count ledger unified** — 812,793 rows / 783,820 unique / 7,815 dropouts; (c) **unique-TARGETID omnibus χ²=3.00 (p=0.39)**; (d) **Bonferroni threshold corrected 3.02 → 2.77**. PDF 25 pp / 0 errors / 0 undef refs / md5 b86b03f9, mirrored to site/public/papers/p5_desi_chirality_v0.1.53.pdf. **Readiness held at 90** — R23conf found real findings portfolio-wide, NOT a clean round.

## Close-the-gap — v0.1.53 (R23conf closure, 2026-06-09)

- **R24conf confirmation round on v0.1.53 must come back clean** (next gate; per-portfolio rule, R23conf does not count as clean).
- **P5 Fig 8 generator script missing from repo** — write + commit the producer script so the figure is reproducible (new queue row, agent-local).
- Houston external review round + personal sign-off (final 1%).
- arXiv endorsement + submission (last in queue, after P4).

## Close-the-gap — v0.1.44 (R-upgraded-round9 closure, 2026-06-03)

R-upgraded-round9 (direct-vendor Gemini-2.5-Pro + Grok-4 + GPT-4o + Perplexity Sonar Pro on v0.1.43) returned 7 do-now findings after 5 silent rounds. All 7 closed in this bundle (v0.1.43 → v0.1.44). Cascaded-exit counter rolled back to 0/3; next round = R-upgraded-round10.

| ID | Class | Closure (v0.1.44) |
|----|-------|-------------------|
| GRO-B1 | BLOCKER | Title retitled to lead with DESIVAST primary path: *"Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"* (was V-Web-led). |
| GRO-B2 | BLOCKER | "Largest-sample null confirmation" + "strongest available rejection of the alternative" softened to "largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date" + "controlled-sample non-detection". Abstract "strongest void constraint" → "controlling void constraint". §10.2 "strongest evidence regime" → "extends ... across the void-finding-algorithm axis". |
| GEM-M1 + GPT-M3 + GRO-M1 | MAJOR (3-way) | §Limitations RSD bullet rewritten to lead with anisotropic tidal-tensor eigenvalue deformation (Hahn/Hoffman/Cautun) as the *dominant* effect for a tidal-tensor classifier; scalar σ_v/(aH) demoted to *secondary indicative bound*. |
| PER-M1 | MAJOR | Abstract clarified: "DESIVAST provides the void catalog (three-algorithm: VoidFinder sphere-growing, V2-REVOLVER and V2-VIDE watershed); DESI DR1 redshifts provide the environmental anchor through which we run a V-Web tidal classification on 14,622,283 DR1 spectroscopic galaxies". |
| GEM-m1 | minor | "Any future model" → "any future model in the bounce-chirality coupling class (Sec.~\ref{sec:p4}) ... at the ≳25 Mpc/h V-Web smoothing scale" (intro + conclusions + §XI.B). |
| GEM-n1 | nit | §XI.B title renamed "Bounce vs. inflation discrimination" → "Implications for bounce and inflation models" (the section concludes the test does *not* discriminate the two). |
| GRO-n1 | nit | 380-line preamble changelog (lines 22–404) stripped; archived to `pipelines/p5_desi_chirality/paper/CHANGELOG_pre-v0.1.44.txt`; preamble now ~30 lines of recent history. |

**STALE — not re-applied this bundle** (per synthesis truth audit):
- GEM-B1 + GRO-M2 (toy EFT appendix): retained with v0.1.41 gauge/rotational caveat per Houston decision.
- GPT-M1 (primary-path designation): already at §sec:primary_path since v0.1.39.
- PER-M2 (preprint sweep): already done v0.1.40.

**Recompile**: 4-pass pdflatex, 21 pages / 965,918 bytes / 0 undef refs / 0 overfull boxes. Mirrored to `site/public/papers/p5_desi_chirality.pdf`, `site/public/papers/p5_desi_chirality_v0.1.44.pdf`, `public/papers/p5_desi_chirality.pdf`, paper-local `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf`.

**Convex**: paperVersions.bump returned row `k579j3y8vedj2xgtr3r1rhz3m987zseh`.

---


**Last authoritative update:** 2026-05-26 (PDT) — **🎯 ASTRA-DESI EDR PER-OBJECT CROSS-VALIDATION LANDED + "187-attribute" PHANTOM-FILE WORDING HONESTLY RETIRED IN §Limitations.** Triple-confirmed (2026-05-15, 2026-05-22, 2026-05-26) that no DESI 187-attribute environmental VAC exists in any public release; ASTRA-DESI EDR (Zenodo 10.5281/zenodo.19358024, arXiv:2604.01456) downloaded (4.4 GB Zenodo bundle) + extracted (657,306 ASTRA galaxies with per-class membership probabilities) + per-galaxy cross-matched against P5 deduped-primary spirals × V-Web env labels → **N_overlap = 25,186 spirals with all three labels** (P5 chirality + ASTRA probabilities + V-Web class). Cross-match pipeline: `pipelines/p5_desi_chirality/scripts/15_astra_per_object_crossmatch.py`. Result summary: `pipelines/p5_desi_chirality/results/analysis_astra_per_object/summary.json`. **HEADLINE (n≥100 classes)**: cw_fraction range across env classes is 1.08 pp (V-Web on same overlap), 2.08 pp (ASTRA argmax), 1.17 pp (ASTRA entropy-weighted); max |σ_from_half| is 2.68 (V-Web cluster), 2.25 (ASTRA argmax void), 2.00 (ASTRA entropy-weighted void) — no class clears Bonferroni-corrected α=0.01 K=4 threshold |σ|_Bonf=3.02 under any classifier. **Per-galaxy classifier agreement is poor** (V-Web puts only 3 of 25,186 spirals in void+wall classes, ASTRA argmax puts 10,965 there — survey-shell density-grid systematic at the EDR rosette scale), **yet both classifiers recover the same headline null** despite vastly different per-galaxy class assignments. This is the **7th independent positive evidence line** for headline environment-independence (joins DESIVAST per-galaxy + within-class density + DESIVAST-anchored clean null + 3-algorithm robustness + V2 GALZONE + MAXIMAL voids HEALPix). New §sec:astra_per_object section + cross-references from §sec:tweb_compare + §Limitations wording rewrite to honestly retire "if a 187-attribute VAC becomes available" placeholder. Paper recompiled clean at 16 pp / 920 KB / 0 overfull / 0 undef refs / 0 undef cites. PDF mirrored to `public/papers/`, `site/public/papers/`, `site/out/papers/` byte-identical. **Prior authoritative update:** 2026-05-19 (PDT, tick 116) — **🎯 ENV-VAC BLOCKER CLOSED — V-Web cosmic-web env catalog landed via Phase 1 MVP env_finder, headline analysis ran-not-blocked.** Houston approved Phase 1 MVP at tick 115; this tick implemented + ran end-to-end in 104 seconds wall on laptop ($0 marginal compute, no pod). **Algorithm**: V-Web (Hahn+ 2007 / Cautun+ 2014) on 14,622,283 DESI DR1 spectro galaxies (ZWARN==0 GALAXY 0.01<z<2): comoving Cartesian → CIC onto 256³ grid (cell 25.9 Mpc/h in 6.6 Gpc/h bounding cube) → survey-mask-aware overdensity δ → Gaussian smoothing R_s=25 Mpc/h → tidal tensor T_ij via FFT → eigendecomposition → V-Web class. **Survey-mask fix** added after V0.1 first pass showed void-fraction skew (9.5% vs literature 70%): dilated occupied-cell mask treats outside-footprint cells as mean-density rather than δ=-1, killing the survey-edge artifact. **V0.2 in-footprint volume fractions**: void 24.4% / wall 41.3% / filament 33.3% / cluster 1.0% — still tilted vs Cautun+ 2014 N-body baseline (70/15/12/3) because the DESI footprint is a thin spherical shell not a box, so edge-mode bias remains; relative density-ordering is correct (cluster > filament > wall > void) which is what matters for the analysis. **🎯 HEADLINE COSMIC-WEB RESULT** (`results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv`): **Galaxy chirality is statistically independent of cosmic-web environment within DESI DR1 at V-Web resolution.** Per-env cw_fraction: void (n=428) 0.4836 / −0.68σ; wall (n=6,673) 0.5034 / +0.55σ; filament (n=408,187) 0.4980 / **−2.6σ**; cluster (n=397,505) 0.4963 / **−4.7σ**. The catalog-level P4 monopole (cw_fraction=0.4972, −5σ on 791,635 matched spirals) is uniformly distributed across filament+cluster populations; range of cw_fraction across all 4 env classes is only 0.4836–0.5034 (a 1.7pp spread) and dominated by counting statistics on small subsamples. **Consistent with the P4 uniform classifier-bias interpretation, NOT with an environment-dependent chirality effect.** This is a real positive null finding for P5. **Artifacts**: `data/desi_env/desi_env_vweb.parquet` (230 MB, 14.6M rows, gitignored per policy; provenance sidecar committed), `env_finder/01_compute_vweb.py`, `env_finder/config.yaml`, `env_finder/reports/01_volume_fractions.json`. Readiness P5 **15 → 30** (+15pp): env-VAC blocker closed (the load-bearing P5 blocker); headline analysis runs; null result confirms P5 central scientific question has a defensible answer at MVP resolution. Phase 2 (sensitivity sweep + RSD correction + Tempel cross-validation) and Phase 3 (paper draft + first PDF compile + first R-round) are the next ~3-5 day windows.

**Prior authoritative update:** 2026-05-18 (PDT, tick 114) — **P5 brought onto SSOT radar after being missed across ticks 102-113.** Bootstrap commit `059c3458` (2026-05-15) created the pipeline at `pipelines/p5_desi_chirality/` but P5 was never added to `papers.ts`, `live-status.ts`, `CLAUDE.md`, `queue.md`, or `SSOT/index.md`. The R-round cron loop has never operated on P5. This SSOT file is the first formal acknowledgment that the bigbounce campaign is a **5-paper portfolio**, not 4.

---

## Scientific question

> Is galaxy chirality statistically independent of DESI-derived large-scale-structure environment after controlling for sky position, redshift, imaging systematics, morphology confidence, and selection effects?

Separate from P4 (which is the catalog/null parity paper). P5 inherits P4's chirality labels and asks an environment-dependent question that P4 is not designed to answer.

---

## What's done (all written 2026-05-16)

| Artifact | Path | Size / rows | State |
|---|---|---|---|
| Matched chirality × DESI DR1 catalog | `pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet` | 1.3 GB, **2,232,212** deduped rows | ✅ landed |
| Provenance sidecar | `p5_matched_chirality_desi.parquet.provenance.json` | git_sha 0882fcdcc75e, config_hash 83970171f71bb863 | ✅ |
| Headline binomial | `p5_matched_chirality_desi_summary.json` | cw_fraction=0.4972 on 791,635 spirals; −5.0σ from 0.5 | ✅ |
| Redshift analysis | `results/analysis_redshift/` | permutation null p=0.372; obs max-deviation 3.14% vs null p99 7.75% | ✅ no z-dependence |
| Density analysis (5-NN) | `results/analysis_density/` | max_abs_sigma = 3.94 global; no LEE correction yet | ⚠️ needs LEE |
| HEALPix spatial scan | `results/analysis_healpix/` | nside 16/32/64 p-values 0.607/0.135/0.413 | ✅ no spatial structure |
| Systematics label-shuffle | `results/analysis_systematics/` | null cleanly preserved | ✅ sanity pass |
| Cosmic-web analysis | `results/analysis_cosmic_web/summary.json` | status: **"blocked"** — environmental VAC missing | ❌ BLOCKED |

**Crossmatch geometry**: 1″ primary radius (with 0.5/1.0/2.0/3.0/5.0″ sensitivity sweep showing matched count is insensitive — 2.34M → 2.44M from 1″ → 5″). p50 separation 0.007″, p90 0.030″, p99 0.298″ — sub-arcsecond as expected from shared imaging.

**Imaging-leg breakdown** of matched primary: DECaLS 1,538,880 / BASS+MzLS 688,608 / DES 4,724.

---

## What's blocked

### High-severity: DESI environmental VAC

The cosmic-web/environment headline analysis is blocked on a missing dataset. Schema contract is published in `scripts/08_analysis_cosmic_web.py` and the analysis script writes a `status: "blocked"` summary instead of producing nulls — the pipeline does not silently fail.

**The "187 DESI-derived attributes" catalog** Houston referenced in earlier planning is **confirmed not in repo** (exhaustive subagent search 2026-05-15; reconfirmed tick 114). Two interpretations remain open:
- (a) The file was never committed and lives on an old pod / external Zenodo / separate repo. **Houston-mediated**: needs Houston to point us at its actual location.
- (b) "187 attributes" referred to a count from a planned LSS VAC that doesn't yet exist.

**Three real paths to close this blocker**:

1. **Houston locates the 187-attribute catalog** (if it exists) — fastest path; would unblock analysis C directly.
2. **DESI DR1 LSS VAC official release** (BGS/LRG/ELG/QSO catalogs + random catalogs + filament/void labels) — pending DESI collaboration release. Out of our timeline.
3. **Run our own cosmic-web finder pipeline** on DESI DR1 LSS targets — real new compute work. DBSCAN-style spatial clustering or DisPerSE-style filament tracing on the spectroscopic galaxy sample. Estimated track: a separate sub-project under `pipelines/p5_desi_chirality/env_finder/`. Owner not yet assigned.

### Other open work

| Item | Severity | Resolution |
|---|---|---|
| Paper LaTeX is 9KB scaffold (no compiled PDF) | High for external-review readiness | Requires headline results from analyses A-E in hand; do not draft prose against placeholder numbers per audit's TODO 7. |
| 5-NN density max_abs_sigma=3.94 lacks LEE correction | Medium | Look-elsewhere correction needed before quoting as significant; trial-factor depends on number of density bins × z bins. |
| Cross-survey connections (P2 high-z tracers, P3 anomaly engine) not yet drawn | Low — follow-up | Houston Method completion item per `feedback_houston_method`. |
| Cross-vendor R-round campaign has never operated on P5 | Low — pre-mature | P5 needs paper draft before R-round adversarial review is meaningful. |
| Not in `papers.ts` / `live-status.ts` / `CLAUDE.md` / `queue.md` / `SSOT/index.md` | High — visibility | **Closing in tick-114 bundle.** |

---

## Readiness estimate

**P5 = 15%** — bootstrap with first-pass analyses on hand, no paper draft, headline analysis blocked. The number reflects:
- ✅ Matched catalog landed (2.23M rows) — big load-bearing artifact done (+5pp)
- ✅ 5 of 6 first-pass analyses complete with sensible results (+5pp)
- ✅ Pipeline scaffolding + provenance + audit doc + scripts compile (+3pp)
- ✅ SSOT integration tick 114 (+2pp)
- ❌ Paper draft is scaffold only
- ❌ Cosmic-web headline analysis blocked
- ❌ Never been through R-round campaign
- ❌ No external review yet

For comparison: P2 at 82% has been through 2-3 R-rounds but is also pre-external-review; P1A at 90% has cleared the loop-exit gate. P5's path to ~80% would require: env-VAC blocker resolved (one of 3 paths above), paper draft populated with headline results, at least 1 R-round on the draft.

---

## What changes when you finish a P5 piece of work

Per `project-context/SSOT/README.md` SSOT protocol: when you finish work that changes P5's state (new analysis result, new figure, new compile, env-VAC blocker resolution, paper draft milestone), update **this status.md** AND mark the relevant `queue.md` row AND the `SSOT/index.md` headline IN THE SAME COMMIT. Same protocol as P1-P4.

---

## File pointers

| Resource | Path |
|---|---|
| Pipeline root | `pipelines/p5_desi_chirality/` |
| Audit doc (read FIRST when picking up P5) | `pipelines/p5_desi_chirality/reports/00_audit.md` |
| Pipeline README | `pipelines/p5_desi_chirality/README.md` |
| Paper LaTeX scaffold | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` |
| Config | `pipelines/p5_desi_chirality/config/p5_config.yaml` |
| Scripts (fetch + analysis 01-10) | `pipelines/p5_desi_chirality/scripts/` |
| Matched catalog | `pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet` |
| Cosmic-web blocker contract | `pipelines/p5_desi_chirality/scripts/08_analysis_cosmic_web.py` + `results/analysis_cosmic_web/summary.json` |
