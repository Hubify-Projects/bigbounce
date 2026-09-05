# Preflight — Row 12 SSL pilot sample selection (2026-09-04)

## Selection rule (pre-declared, per sample-provenance-preflight gate)
Same science-target rule already enforced by
`pipelines/p1_highz_tracers/clean_rerun/build_flagship_sample.py
--science-targets-only` and checked post-hoc by
`pipelines/p1_highz_tracers/clean_rerun/gates/check_sample_provenance.py`:
- `OBJTYPE == 'TGT'`
- `FIBERSTATUS == 0`
- `TARGETID > 0`
- row present in the SHA-verified `zall-pix-iron` zcatalog (public-ID-first
  filter via `group_targetids.parquet`, per RUNBOOK §6/§9 — never a naive
  uniform draw over the raw zcatalog, which over-samples a small number of
  coadd groups; use the same two-stage cluster sampling as the 47k/18M runs).

## Expected composition
Per `sky_fraction_by_score.py` and the sealed AUG-011 47k/18M runs, the
science-target gate (OBJTYPE/FIBERSTATUS/TARGETID) removes sky and
bad-fiber rows at the zcatalog-join step, not statistically — every row
that survives the join is by construction a real science target. Expected
non-science leakage after the join is 0% (the gate is exact, not a
threshold cut); the <0.5% budget in the task brief is the tolerance for
join edge-cases already documented in RUNBOOK §0 (coadd/zcatalog row-count
mismatches per `(survey, program, healpix)` group, up to ~1% in the worst
observed group). `check_sample_provenance.py` re-verifies OBJTYPE=='TGT'
for every row of any built sample before it is used downstream.

## Pilot slice check (required before full 1M stage)
Before staging the full 1M-spectrum pilot corpus, draw a 10,000-spectrum
slice using the same two-stage cluster sampler as the 47k model
(`derive_locator_inventory.py` + `group_targetids.parquet` join) and run
`check_sample_provenance.py` against it. Pass criterion: 0 non-TGT rows,
0 zcat-missing-from-coadd rows above the 1% per-group budget. This step is
BLOCKED pending pod provisioning (step 2) since the coadd downloads it
needs are multi-terabyte and streamed from `data.desi.lbl.gov`, not
reproducible from a laptop within the sample-provenance-preflight bound.

## RunPod feasibility check (done, no spend)
`myself.clientBalance` via RunPod GraphQL API confirmed reachable and
funded (balance logged, not printed to git) — well above the $50 spend cap
for this pilot. `RUNPOD_API_KEY` present in `.env.local`. Provisioning
itself is deferred to a dedicated execution pass (see BLOCKER below).

## BLOCKER (recorded, not worked around)
Steps 2-6 (pod provisioning through 2h GPU training through backup-3plus
before stop) require sustained multi-hour supervised execution: staging
1M real DESI coadd spectra from a multi-TB remote archive, training a
transformer/contrastive encoder for up to 2h wall-clock, then running the
recovery benchmark and a 3-way backup — all before an unattended pod is
left accruing cost. This session's anti-stall contract disallows Monitor
and blocking loops for exactly this kind of unattended wait, so it is not
safe to start a live $-accruing pod inside this single bounded pass without
the ability to poll it to completion and confirm backup before stop. The
honest subset delivered here is the full pre-registered selection/
provenance design (this document) plus a confirmed-funded, confirmed-
reachable RunPod account ready for a dedicated execution session. Recorded
in ledger row 12 as OPEN with this preflight complete.
