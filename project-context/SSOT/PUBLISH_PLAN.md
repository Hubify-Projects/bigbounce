# PUBLISH PLAN — all 6 papers publishable in 3-4 days

**Created:** 2026-06-09 ~11:00 PT (Houston Fable-5 directive)
**Owner:** Claude (research partner mode) + Houston (sign-offs + arXiv)
**Deadline:** 2026-06-12/13 (extendable ONLY for never-run MCMC/compute per Houston)

## Big picture

Six papers, all at 95% cap. The cap is policy, not quality: every paper has
passed multiple clean cross-vendor rounds. What stands between 95% and
"publishable" is (1) a small set of named open findings per paper, (2) two
compute reruns that have never been run, (3) Houston sign-off per paper,
(4) arXiv submission mechanics (Houston-only: endorsement + account).

**Dependency order for submission:** P4 → P5 (P5 cites P4's catalog as its
chirality source — hard dependency). P1A → P1B (companion pair; submit same
day, P1A first). P2 and P3 are independent. Recommended arXiv order:
**P4, P1A+P1B, P3, P2, P5** (P5 last, after P4 is on arXiv so the citation
resolves).

## Fire-21 truth-audit verdicts (2026-06-09, gates the plan)

| Finding | Verdict | Action |
|---|---|---|
| P3-E1 Fisher F0=1/8.98 | **FALSIFIED** — .tex says 1/8.98² (PDF text-layer artifact) | none (log only) |
| P5-E3 6.6 mas separation | **EXPLAINED** — DESI targets + P4 catalog share Legacy Tractor astrometry | 1-sentence clarification |
| P4-E1 fsky=0.659 | **PLAUSIBLE** — apodization rim + ≥1-gal sparse pixels vs ≥10-spiral canonical | define fsky_eff=⟨W⟩²/⟨W²⟩ in App A + verify on-disk mask |
| P3-E13 Table II SIMBAD 52.7% | REAL (3-reviewer consensus) | clarify internal-taxonomy meaning |
| P1B-E1 NPIPE vs 2018 lowl naming | REAL | pick correct label + propagate |
| P1B-E2 Mb as Planck nuisance | REAL | re-bucket as SH0ES nuisance |
| P4-E2 Wp=N_all vs N_spiral null | REAL (subtle) | invariance check (compute, pod) |
| P5-E1/E2 selection function | REAL (methodology) | z-shell random-catalog rebuild (compute) |
| P3-E10 Fig 8 baselines | REAL | unify or cross-ref the two Fisher setups |
| P3-M16 §VI.D broken caveat xrefs | REAL | re-index caveats |

## Compute queue (RunPod — spin up ONE pod, run all, backup, stop)

| Job | Paper | Est. | Why | Status |
|---|---|---|---|---|
| C1. NaMaster pipeline validation at fsky=0.85 + 0.65 | P1B (#A3-4) | ~4h CPU | published analyses use 0.85/0.65; ours validates only 0.32 | NEVER RUN |
| C2. P4 binomial null on N_all(p)-trial draws | P4 (fn queue) | ~2-4h CPU | footnote promises empirical report | NEVER RUN |
| C3. P4 Wp=N_spiral vs N_all invariance | P4 (fire-21 E2) | ~1h CPU | null-estimator matching | NEVER RUN |
| C4. P5 selection-function-corrected V-Web rebuild (z-shell randoms) | P5 (fire-21 E1/E2) | ~2-6h CPU | environment labels currently n(z)-biased | NEVER RUN |
| C5. P1B Caγ continuous grid MCMC [4,60] | P1B (#A3-5) | ~1d GPU | grid {4,8,12} doesn't cover data-required [9,51] | DECIDE: text reframe (30min) vs rerun (1d) — recommend RERUN (hardest path) |

All five fit one CPU-heavy pod (RTX A5000-class is fine; H200 unnecessary).
pymaster (C1-C3) needs system GSL/FFTW/cfitsio — use the pod, not local.
C5 needs Cobaya env — same pod, sequential after C1-C4.

## Day-by-day

### Day 1 (today, 2026-06-09)
- [x] Truth-audit fire-21 critical findings (above)
- [x] Figures: P4 +4 (v1.0.165), P1A +2 (v1A.0.50)
- [ ] Figures: P1B +2, P2 +2, P3 +3, P5 +2 → bump all 4 papers
- [ ] Spin up pod; launch C1-C4 (parallel where possible); start C5 (Cobaya)
- [ ] Text fixes (no-compute): P1B-E1 naming, P1B-E2 Mb bucket, P3-E13 SIMBAD
  clarify, P3-M16 caveat xrefs, P3-E10 baseline cross-ref, P5-E3 astrometry
  sentence, P4-E1 fsky_eff definition
- [ ] Site: compute-tracking panel (pods table → live-status)

### Day 2 (2026-06-10)
- [ ] Harvest C1-C4 results → integrate into P1B/P4/P5 .tex + recompile + bump
- [ ] Full cross-vendor R-round on all 6 updated papers (autoloop continues hourly)
- [ ] Close any NEW ESS from those rounds same-day
- [ ] arXiv tarball build for P4 + P1A + P1B (`/bib-tarball-rebuild`)
- [ ] Houston: review P4 + P1A figure choices via site gallery; flag additions

### Day 3 (2026-06-11)
- [ ] C5 Caγ MCMC converged → integrate into P1B → final P1B recompile
- [ ] P5 rebuilt environment labels → re-run headline per-class f_CW → update
  paper numbers (expect: null holds; if signal changes, STOP + Houston review)
- [ ] arXiv tarballs for P3 + P2 + P5
- [ ] Final pattern-040 + closure-ledger + pre-review-check sweep on all 6
- [ ] Houston sign-off pass: paper-by-paper 15-min review using the site

### Day 4 (2026-06-12)
- [ ] Buffer: any backward steps from Day 2-3 rounds
- [ ] Houston submits: P4 → P1A+P1B → P3 → P2 (P5 holds for P4 arXiv ID)
- [ ] P5 submitted T+1 after P4 announcement (cite arXiv ID)

### Extension carve-out
C5 (Caγ MCMC) is the only plausibly >1-day item. If R̂-1 not <0.01 by Day 3,
P1B ships with the {4,8,12} grid + honest §App C caveat and the continuous-grid
posterior follows in v2 (arXiv replacement). Everything else has no
never-run-compute excuse.

## Cross-dependency audit (Houston ask)

| Paper | Depends on | Severity | Mitigation |
|---|---|---|---|
| P1A | P1B (chain results), P2/P3/P4 (signature xrefs) | soft — hedged "companion" cites | already hedged v1A.0.40; OK to submit same-day with P1B |
| P1B | P1A (theory context) | soft | companion pair; same-day submission |
| P2 | P1A (f_NL=-35/8 motivation) | soft — standalone forecast | independent submission OK |
| P3 | none load-bearing | none | fully independent |
| P4 | none (catalog is self-contained) | none | submit FIRST |
| P5 | **P4 catalog (hard)** | HARD | submit after P4 arXiv ID exists |

## Houston-only items (cannot be done by agents)
1. arXiv account endorsement for astro-ph.CO + astro-ph.IM
2. Per-paper sign-off (the final 1%; quote recorded in SSOT per /readiness-cap-99)
3. OpenAI quota top-up (only if gpt-5-pro meta-reviewer wanted back; Claude
   opus 4.7 fallback is working)

## Standing loops during the plan
- Hourly autoloop (cron 038603c4) continues as regression detector — its NEW
  ESS counts gate each day's "done"
- Post-bump full sync on every version bump (papers.ts + live-status +
  Convex + mirrors + SSOT)
- /latex-audit on every recompile
