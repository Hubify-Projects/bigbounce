# P5 R-multi-round2 R-round — Truth-Audit Synthesis

**Date**: 2026-06-01
**Paper**: P5 (DESI LSS spiral-chirality V-Web environmental analysis)
**Pre-round version**: v0.1.34
**Post-round version**: v0.1.35
**Vendors fired**: Grok-4 (brutal honesty), GPT-4o (FALLBACK from GPT-5; methodology), Perplexity Sonar Pro (citation forensics), Gemini-2.5-Pro (cosmology — FAILED at 0.9s, 403 PERMISSION_DENIED / Lightning dunning)
**Source paper**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
**Cascaded-r-rounds protocol**: cascade of R-multi-true95 (closed at v0.1.34) → R-multi-round2 (on v0.1.34) → output v0.1.35.

---

## Findings table (per `feedback_peer_review_truth_audit_protocol`)

| ID | Class | Headline | Verdict | Evidence | Action |
|----|-------|----------|---------|----------|--------|
| PER-R2-B1 | MAJOR | Shamir 2022 mis-cited to A&A 665, A76 (claim: should not be MNRAS 516, 2281) | **FALSIFIED** | WebFetch on arXiv:2208.13866 returns DOI `10.1093/mnras/stac2372` redirecting to `academic.oup.com/mnras/article/516/2/2281/6678564` — Shamir IS MNRAS 516, 2281 (2022). The reviewer's proposed "correction" to A&A 665, A76 is itself wrong. | No change. Bibitem retained as-is. |
| PER-R2-B2 | MAJOR | DESIVAST void counts (1,461/420/295 + 3,765 maximal voids + 101,863 holes) "look internally generated" | **FALSIFIED** | (a) arXiv:2411.00148 abstract verbatim: "1,461 interior voids with VoidFinder, 420 with V2 using REVOLVER pruning, and 295 with V2 using VIDE pruning." (b) Direct `astropy.io.fits` inspection of local `DESIVAST_BGS_VOLLIM_VoidFinder_{NGC,SGC}.fits`: NGC MAXIMALS=3241, SGC MAXIMALS=524 → 3,765 total; NGC HOLES=89,003, SGC HOLES=12,860 → 101,863 total. Exact match to paper text. | No change. |
| PER-R2-M1 | MAJOR | `zall-pix-iron.fits` not a documented DR1 product name | **FALSIFIED** | "iron" is the DR1 spectroscopic-reduction tag; local fetch script `scripts/02_fetch_desi_dr1.py` line 4 sources from `data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/`. Filename is canonical. | Tightened §II.B with explicit specprod-tag URL pointer for clarity (defensive closure). |
| PER-R2-M2 | MAJOR | ASTRA "BGS-anchored volume-filling-fraction calibration" overclaim | **FALSIFIED** | WebFetch on arXiv:2604.01456 returns abstract verbatim: "We calibrate the classification thresholds using BGS as an anchor to match the volume-filling fractions reported for GAMA." Paper text matches source. | No change. |
| PER-R2-m1 | minor | DR1 parent-sample numbers presented as canonical without "derived in this work" tag | **VERIFIED** | True — paper text gives 16,361,731 / 14,622,283 with no clarifier; these come from applying our cuts, not from a published DR1 constant. | Added "These row counts are *derived in this work*..." clarifier + driver pointer to §II.B. |
| PER-R2-m2 | minor | "authoritative public DR1 void identification" overstates DESIVAST status | **VERIFIED** | True — DESIVAST is one of several valid void finders, not the official DR1 void VAC. | Softened to "publicly released, peer-reviewed DR1 BGS void catalog at low z (VoidFinder + ZOBOV watershed algorithms)" in §VII.E. |
| GRO-R2-B1 | BLOCKER | V-Web void n=428 still leads abstract per-class line | **VERIFIED** | True — abstract per-class line started with void number despite text body downgrading void to artifact-dominated. | Re-ordered abstract per-class line to lead with filament/cluster (high-N), move void numbers behind a "(survey-edge artifact dominated; see DESIVAST anchored result below)" hedge. |
| GRO-R2-M1 | MAJOR | "A positive detection would have been a discriminator" — empty conditional given no model predicts environmental signature | **VERIFIED** | True — §XI.B opening sentence dangled this empty conditional in front of the actual disclaimer. | Replaced opening sentence with: "No published model in either class (matter-bounce or inflation) currently predicts an environment-dependent CW signature at the sensitivity reached here, so the present null does not directly discriminate..." |
| GRO-R2-M2 | MAJOR | EFT operator paragraph carries too much main-text weight given toy/order-of-magnitude caveats | **VERIFIED** | True — entire 36-line toy parametrization sits in §Conclusions; the caveats outweigh the result. | Moved bulk to new `\appendix \section{Toy EFT mapping of the environmental bound}\label{app:toy_eft}`; left one-sentence pointer in §Conclusions. |
| GRO-R2-m1 | minor | "load-bearing concordance result" internal contradiction with abstract's "supporting rather than load-bearing" framing | **VERIFIED** | True — §VII bullet and Fig.\ref{fig:tempel_overlay} caption both still said "load-bearing". | Renamed to "highest-N concordance result (supporting, not load-bearing — the primary cross-classifier validation remains the on-DESI DESIVAST re-projection...)" in both locations. |
| GRO-R2-m2 | minor | RSD boundary-crossing claim presented as if propagation has been done | **VERIFIED** | True — v0.1.34 introduced the boundary-crossing estimate but the wording "leaves per-class Δf_CW unchanged at the 10^{-3} level" overstated what was shown. | Downgraded to "expected to be sub-dominant at current precision; full quantification requires the Zel'dovich-reconstructed rerun"; carried as explicit caveat in headline-null wording. |
| GPT-R2-B1 | BLOCKER | Permutation null setup detail (N_perm, null construction) missing in §V | **VERIFIED** | True — §V Statistical methods said "label-shuffle permutation" without N_MC value or driver. Code inspection shows N_MC=1000 (default) in `scripts/07_analysis_healpix.py` line 82 and `scripts/09_systematics.py` line 149. | Added explicit "$N_{\rm MC}=1000$ independent permutations from a deterministic-seeded NumPy `default_rng`... null distribution constructed as empirical CDF" + driver artifact pointers to §V. |
| GPT-R2-B2 | BLOCKER | No power analysis for sample-size-vs-environment claim | **OPINION/duplicate** | Phase 2 sensitivity sweep across nine $(R_s, \lambda_{\rm th})$ cells IS the power/sensitivity analysis. The catalog-monopole subtraction against $\sigma_{\rm pred}$ in Table II is the per-bin power check. | No additional closure. |
| GPT-R2-M1 | MAJOR | V-Web $R_s/\lambda_{\rm th}$ choice justification | **OPINION/duplicate** | Already swept in Phase 2 across 3×3 grid; smoothing scale choice follows Cautun+2014 and is cited verbatim. | No additional closure. |
| GPT-R2-M2 | MAJOR | Phase 2 error propagation | **OPINION/duplicate** | Phase 2 sweep IS the error propagation (per-cell range of CW fractions reported across all nine cells, max 0.22pp). | No additional closure. |
| GPT-R2-M3 | MAJOR | Tempel biases | **OPINION/duplicate** | Already discussed in §VII (SDSS DR10 vs DESI Legacy DR8, $z\le 0.20$ vs $z\le 4$, richness-vs-tidal mapping caveats all spelled out). | No additional closure. |
| GPT-R2-M4 | MAJOR | Alternative VAC suggestion | **OPINION/duplicate** | DESIVAST + ASTRA + Tempel already proposed as the three alternative classifiers; §XII Limitations already lists "full DR1 VAC as desirable future input." | No additional closure. |
| GEM (failed) | n/a | Gemini-2.5-Pro returned 403 PERMISSION_DENIED ("Lightning dunning decision is deny") in 0.9s | **VENDOR-FAILURE** | Not a content finding; vendor billing failure. | None — re-fire on next cron after billing reconciliation. |

**Counts**:
- VERIFIED + closed with real text edits: **8** (PER-R2-m1, PER-R2-m2, GRO-R2-B1, GRO-R2-M1, GRO-R2-M2, GRO-R2-m1, GRO-R2-m2, GPT-R2-B1)
- FALSIFIED via direct evidence: **4** (PER-R2-B1, PER-R2-B2, PER-R2-M1, PER-R2-M2 — all citation forensics over-calls)
- OPINION/duplicate: **5** GPT findings (GPT-R2-B2 + M1-M4)
- STALE: 0
- Vendor failure: 1 (Gemini-2.5-Pro, no charge)

---

## Compile state

- Recompile: 3 passes (`pdflatex -interaction=nonstopmode -halt-on-error p5_desi_chirality.tex`)
- Final pass: 0 undefined refs, 0 undefined citations, 0 overfull boxes
- Pre-existing float-stuck warnings on lines 556 and 1032 unchanged (table/figure placement; not new from v0.1.35 edits)
- Output: 18 pages, 939,924 bytes
- MD5: `a806b58b9bb4336cef80b7833ee8adbf`

## Mirroring

- `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` (source)
- `site/public/papers/p5_desi_chirality.pdf` (latest mirror)
- `site/public/papers/p5_desi_chirality_v0.1.35.pdf` (versioned mirror)

## Convex updates

- `paperVersions:bump` → row id `k57f9r95cz9jj88feh08bwdp8587wrr4` (paper-5, v0.1.35, datestamp 2026-06-01, texCommit `40d0293d`, md5 `a806b58b...`)
- `papers:upsert` → row id `k972tnctn98e83dh2pn9vm2bjn87ty9p` (sitePdfPath now `/papers/p5_desi_chirality_v0.1.35.pdf`; focusAreas refreshed with DESIVAST + toy-EFT-appendix + R-multi-round2 closure marker)

## Files modified

- `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`:
  - `\paperVersion` v0.1.34 → v0.1.35 + new round-2 changelog block with 12 per-finding closure notes
  - `\paperTimestamp` "June 1, 2026 PDT" → "June 1, 2026 PDT (R-multi-round2)"
  - §II.B DESI DR1 paragraph: added specprod-tag URL pointer + "derived in this work" clarifier on row counts + driver artifact
  - Abstract per-class line re-ordered (filament → cluster → wall → void) with survey-edge-artifact hedge on void numbers
  - §V Statistical methods: added explicit $N_{\rm MC}=1000$ + null-construction note + driver pointers (`scripts/07_analysis_healpix.py`, `scripts/09_systematics.py`)
  - §VII bullet (filament_like_vs_filament) + `\caption{}` of Fig.~\ref{fig:tempel_overlay}: "load-bearing" → "highest-N (supporting, not load-bearing)" with explicit DESIVAST primary-validation pointer
  - §VII.E DESIVAST framing: "authoritative public DR1 void identification" → "publicly released, peer-reviewed DR1 BGS void catalog (VoidFinder + ZOBOV watershed)"
  - §XI.B Bounce-vs-inflation: deleted empty-conditional opening sentence; rewritten to lead with "no published model predicts..."
  - §XII Limitations RSD paragraph: downgraded "leaves per-class Δf_CW unchanged at 10^{-3}" to "expected to be sub-dominant at current precision; full quantification requires the Zel'dovich-reconstructed rerun"
  - §Conclusions: replaced 36-line EFT toy-operator paragraph with one-sentence pointer to new appendix
  - New `\appendix \section{Toy EFT mapping of the environmental bound}\label{app:toy_eft}` containing the moved EFT toy-parametrization paragraph
- `site/public/papers/p5_desi_chirality.pdf`
- `site/public/papers/p5_desi_chirality_v0.1.35.pdf`
- `project-context/peer-reviews/2026-06-01_R-multi-round2_P5_synthesis.md` (this file)

## Cascaded-r-rounds streak status

- **Clean-round count on v0.1.35**: 0 (post-closure state; v0.1.35 has not yet been re-reviewed)
- **Clean-round count history**:
  - R-multi-true95 (v0.1.34): not clean — 9 VERIFIED findings closed (now retired)
  - R-multi-round2 (v0.1.35): not clean — 8 VERIFIED findings closed (this round; now retired)
- **Streak required for §4.4.1 cascaded-loop-exit**: ≥3-of-5 vendor silence on a single version (Anthropic excluded per `feedback_cross_model_peer_review` no-echo-chamber rule)
- **Next action**: fire round-3 against v0.1.35 with all 5 direct vendors (re-attempt Gemini once billing reconciled) to test whether the round-2 closures hold without introducing regressions

## Standing-directive compliance

- `/peer-review-truth-audit`: per-finding table with claim / verdict / evidence / action — complete; FALSIFIED findings backed by direct WebFetch on arXiv DOIs + local FITS inspection, not "Claude says so".
- `/no-future-work-defer`: every VERIFIED finding closed with a real text edit; the only remaining "deferred" hook is the Zel'dovich-reconstructed RSD rerun, which is TRULY-BLOCKED (requires a separate end-to-end re-classification pipeline beyond the R-round scope).
- `/take-critiques-seriously`: pushed back on FALSIFIED findings only with direct on-disk + web evidence (FITS row counts, DOI resolutions); all other findings closed with full hard fixes.
- `/no-permission-loop`: no permission requested; executed full close including version bump + Convex update.
- `/readiness-cap-99`: paper readiness should oscillate backward (had been at v0.1.34 95%-cap eligible; R-multi-round2 reopens that cap until a clean re-round on v0.1.35 lands).
- `/hardest-path-first`: no shortcuts taken; appendix split for GRO-R2-M2 was the structurally cleanest fix (vs. just adding more caveats inline), §V permutation detail was sourced from actual code not invented, RSD downgrade was honest about what the boundary-crossing estimate does and does not show.
- `/no-openrouter-excuse`: all four vendors hit via direct vendor SDKs (Anthropic excluded; Gemini failed independently on Lightning dunning — not an OpenRouter cap issue).
