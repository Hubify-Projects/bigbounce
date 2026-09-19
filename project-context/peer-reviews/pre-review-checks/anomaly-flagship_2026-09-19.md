# /paper-pre-review-check report — anomaly-flagship @ vAF.0.2

**Run:** 2026-09-19 · **Lane:** LA-anomaly-draft (campaign 2026-09-18)
**Paper:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.tex`
**PDF:** 15 pp · sha256 `b972d890cf5b907eec0a7bf614dac5ba5647502efe3ee907533e4b3f96dd4cba`
**Status:** FIRST FULL DRAFT. **No review board has been run on this paper at any
version** — the director decides the first R-round. This report is prevention-layer
prep, not a convergence claim.

**Scope note.** The portfolio executable gate
(`project-context/pre-review-rules.json`) declares six other papers as its sources and
runs portfolio validators that belong to other lanes. This lane did **not** mutate that
shared config (concurrent-lane rule); the applicable mechanical patterns were run
directly against this paper's `.tex` and compiled PDF and are recorded below. Adding
`AF` to the shared rules catalog is a director-level decision and is listed as a
follow-up.

## Checks run and outcomes

| Pattern | Check | Result |
|---|---|---|
| 003 | stale title/version comments in `head -50` | **ACCEPTED** — the head block is the paper's artifact-provenance map (which `%`-shorthand maps to which committed file), not review-log content. Intentional and load-bearing for auditability. |
| 005 | overclaim vocabulary (`first`, `novel`, `unprecedented`, `definitive`, …) | **PASS** — 10 hits, all ordinary English ("the first thing to rule out", "First, the catalogue is infrastructure"). Zero novelty self-claims. |
| 011/001 | bibliography verification | **PARTIAL — carried as an in-paper `\TODO`.** Five recovery-class citations are verbatim from the committed benchmark artifact; the journal/volume/page of Ritter & Kolb and the three software citations (scikit-learn, Matplotlib, astroquery) are not in any committed artifact and need an ADS pass before submission. Recorded in Appendix A of the paper itself rather than silently accepted. |
| 014 | review-log keywords in `^%` comments | **PASS** — 0 hits |
| 017 | review-log artifacts in body prose | **PASS** — 0 hits |
| 019 | title overclaim vs body null | **ACCEPTED, flagged for the board.** The body carries a negative result (recovery benchmark unmet). The title carries no "bound/no-go/null" token but does carry two honest qualifiers — *candidate* catalogue and *descriptive* taxonomy — and the abstract states the negative outcome explicitly ("recovers no class at the pre-declared bar, so this work is reported as a validated data release and not as a discovery"). Recommend the first board be asked directly whether the title should carry the null more overtly. |
| 023 | future-work-defer / trivial-fix-refused | **PASS** — 0 hits. Stronger than pass: the cheapest named follow-up test (the FT-A Lyman-break check) was *executed* in this draft rather than deferred, and it changed the result (one candidate refuted). The five open tests OT-1…OT-5 each name their real cost; OT-1 is genuinely GPU-scale and is stated as a gate, not an excuse. |
| 027 | headline claim → on-disk artifact | **PASS** — every quantitative statement in `main.tex` carries a trailing `%` comment naming its committed artifact; derived quantities are emitted by `make_draft_figures.py` into `outputs/draft_numbers.json`. |
| 029 | estimator multiplicity / pre-registration | **PASS** — the selection threshold rule, the recovery-benchmark bar, and the V12 null are all pre-declared and quoted from their artifacts; the paper reports the *less* favourable reading of V12 and the *lower* of the two defensible enrichment denominators. |
| 033/022/025 | prefactor / attribution without derivation | **PASS** — see the `/never-fabricate-derivation` report. One equation, transcribed from `calibration.json`; one prose relation, stamped. |
| 036 | closure fabricates math justification | **CLEAN** — `project-context/peer-reviews/never-fabricate-derivation/anomaly-flagship_2026-09-19.md` |
| 037 | future-dated `\date{}` | **PASS** — `\paperTimestamp` = September 19, 2026 = today |
| 037b | page-count gate | **PASS** — 15 pp (PRD norm 15–30; ApJS catalogue papers run longer) |
| 038 | version-history artifacts in compiled PDF text | **PASS** — 0 hits |
| 040 | duplicate adjacent words in PDF | **PASS** — 1 apparent hit (`rather / rather`) confirmed a `pdftotext -layout` two-column extraction artifact (left-column line 96 vs right-column line 95), not a source defect |
| 041 | raw file paths in body prose | **PASS with note** — all path-like hits are inside Table I (the provenance chain), Fig. 1's caption, or §IX Data Availability, all exempt. The single body-prose hit is `zall-pix-iron.fits` in §II A, which is the public DESI product's own name, not an internal provenance tag. |
| 046 | artifact/paper cross-check | **PASS** — all 7 `\artifactlink`/`\artifactdirlink` targets resolve on disk with the correct blob/tree kind |
| 053 | companion "in preparation" leak | **PASS** — 0 hits; this paper cites no lab companion |
| 054/038(σ) | σ-value mixing | **N/A** — the paper reports no significance-σ values; the only σ is $\sigma_{\rm MSE}$, a calibration constant |
| N4 | novelty self-claim over-reach | **PASS** — no novelty claim of any grade is made. The paper's own framing is "reproducible data infrastructure with a validated selection", and §X enumerates six things the catalogue is not. |
| latex-audit | full 7-step visual audit | **PASS** — 0 errors, 0 undefined refs, 0 overfull hboxes, all 15 pages rendered at 110 dpi and inspected, 0 broken artifact URLs |

## Open `\TODO`s in the manuscript (4, all honest gaps — nothing invented)

1. §VII C OT-1 — per-class injection recovery (the selection function). GPU-scale; gates every population-level claim.
2. §IX — Zenodo DOI for the public deposit (deposit not yet made).
3. Acknowledgments — DESI/SIMBAD/NED/VizieR/compute acknowledgements.
4. Appendix A — final ADS verification of four bibliography entries (above).

## Release defects the paper carries openly (by design, not omissions)

DEFECT-1 (enriched table's zcatalog columns unpopulated; repair CSV committed),
DEFECT-2 (`residual_kurtosis` empty), plus two schema gaps this draft newly
records: **no `FLUX_IVAR_*` columns** (which is why two of the four FT-A
candidates are undecidable from the release) and **no `OBJTYPE` /
`COADD_FIBERSTATUS` columns** (so the provenance gate cannot re-verify its own
first two conditions from the published file alone). All four must be closed in
the public deposit.

## Verdict

- **BLOCK review:** no. Nothing found blocks a first internal round.
- **Three-stage status for vAF.0.2:** Stage 1 (mechanical sweep) **PASSED**;
  Stage 2 (cross-vendor R-round) **NOT RUN**; Stage 3 (external) **NOT RUN**.
  Readiness must not be lifted on the strength of this report alone.
- **Pre-audit notes for the first board** (please do not re-flag):
  the recovery benchmark's failure to meet its bar is the paper's own reported
  result, not an oversight; the taxonomy's negative silhouette is reported at
  its weaker reading deliberately; the BAL enrichment is quoted at the *lower*
  of two defensible denominators; and the FT-A tier is presented with one
  candidate already refuted by the authors.
