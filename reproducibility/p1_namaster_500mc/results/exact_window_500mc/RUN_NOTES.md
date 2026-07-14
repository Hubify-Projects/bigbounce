# Exact-window production notes — 2026-07-14

Status: production in progress. Quantitative claims belong in the generated
JSON artifacts, not in this narrative file.

## Correctness change

- The recovery model contracts the full rotated `[EE, EB, BE, BB]` theory
  through `NmtWorkspace.get_bandpower_windows()`.
- Every workspace checks that this contraction matches
  `decouple_cell(couple_cell(theory))` to a maximum absolute tolerance of
  `1e-10` before an ensemble starts.
- Historical effective-ell-template outputs remain at the top-level `results/`
  directory and are explicitly marked superseded.

## Verified accelerations

- Uniform Q/U rotation commutes with a scalar mask. The canonical three-beta
  ensemble therefore performs one spherical-harmonic transform per seed,
  rotates the coupled `[EE, EB, BE, BB]` spectra algebraically, then decouples
  each beta. A deterministic regression against direct rotated Q/U fields
  passed at maximum absolute error `8.67e-19`.
- The c10 canonical-refit row reuses the saved canonical 500-MC bandpowers;
  only the five genuinely distinct mask/BB/purification configurations are
  re-simulated. This removes 500 duplicate sky simulations without reducing
  any declared sample count.
- Disjoint robustness configurations are production-sharded and merged only
  after exact name/completeness validation.

## Compute routing

- The authenticated RunPod API reported all retained pods stopped and zero
  active spend.
- Restarting the purpose-built `bigbounce-p1b-snctrl` pod failed with the
  provider response: account balance too low to rent a pod.
- Production therefore runs locally with the isolated PyMaster 2.6 / healpy
  environment. Generated JSON records exact package versions and runtimes.

## Interrupted-process evidence and recovery

- The first local robustness launch used parent PID `93816` with workers
  `93945`, `93946`, and `93947`; the first declared-sweep launch used parent
  PID `65370` with workers `65945`, `65961`, and `65969`.
- At recovery inspection none of those processes remained. The robustness run
  had left only a non-atomic canonical partial, and the declared run had not
  published an output. There was no retained exit status, so the cause is
  unknown; the record does not label the loss as an OOM event.
- The host later showed extreme scheduler contention while replacement jobs
  were active. That observation explains degraded wall-clock throughput but
  does not establish why the earlier processes disappeared.
- Recovery changed execution topology, not science: one named configuration
  per shard, exact `N=500`, seeds 42--541 for every configuration, a two-job
  ceiling, atomic result+receipt publication, and strict validated skip on
  restart.

## Declared checks

- canonical beta injections: `0`, `+0.27`, `+0.342` degrees, 500 realizations;
- c10 robustness: canonical refit, CAMB lensing BB, 0.5/3.0-degree
  apodization, `|b|>30` mask, and B purification, 500 realizations each;
- f-sky/sign extensions: f-sky 0.85 and 0.65 at `+0.27` degrees and f-sky
  0.32 at `-0.27` degrees, 500 realizations each.
