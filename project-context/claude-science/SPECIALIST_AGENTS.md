# Claude Science specialist agents — BigBounce wrappers (Phase 1)

**Created:** 2026-07-01. Implements INTEGRATION_PLAN.md Phase 1: wrap the three
compute-bound pipelines as specialist-agent definitions. Written
**harness-agnostic** (purpose / wrapped scripts / gates / I-O contract) so each
drops into Claude Science's user-created specialist agents when Houston has a
seat, or runs under Claude Code / any MCP agent today. The adversarial-review
layer stays OUTSIDE these agents (Phase 2 rule): they produce artifacts;
they never adjudicate claims.

Every agent inherits three non-negotiables:
1. `/backup-3plus` at every ~2hr milestone and before any pod stop (local + HuggingFace + B2).
2. Provenance parity: every output JSON carries the script path + git hash + seed + config hash; reconcile with `canonical_provenance/` before any paper touch.
3. Results route through `/peer-review-truth-audit` before entering a `.tex` — an agent result is an artifact, not a claim.

---

## Agent 1 — `namaster-mc` (masked pseudo-Cl Monte Carlo)

**Purpose:** MASTER-corrected pseudo-Cl estimation, MC null batteries, and injection-recovery on HEALPix maps (P4/P5 chirality, P1B fsky sweeps).

**Wrapped scripts (existing, committed):**
- `h200_scripts/experiments/c1_p1b_namaster_fsky_sweep.py` — β-injection recovery at multiple fsky (2×500 MC)
- `h200_scripts/experiments/c2_p4_nall_binomial_null.py` — N_all-trial binomial monopole null (500 MC, seed 42)
- `h200_scripts/experiments/c3_p4_wp_invariance_fsky.py` — Wp invariance (N_all vs N_spiral) + fsky_eff

**Skill dependency:** `hubify skills/astro/cmb-power-spectra` (mask-as-artifact, both-weightings reporting, real-catalog mask only).

**Compute shape:** CPU-bound (12 vCPU / 62 GB class); no GPU needed. Batch + checkpoint; NSIDE=512 full-res unless documented fallback.

**I/O contract:** input = mask artifact + catalog parquet + config (seed, NSIDE, n_MC, weighting); output = one JSON per experiment mirrored to `pipelines/*/outputs/canonical_provenance/` with pre/post-MASTER significances, fsky (binary + effective per weighting), and the launch-time findings block.

**QC gate:** injection-recovery must PASS at claimed amplitude before any null is trusted; provenance findings (like an unreconstructable published mask) are disclosed, never patched.

---

## Agent 2 — `cosmology-mcmc` (Cobaya/CAMB chains)

**Purpose:** parameter-estimation chains and referee-driven control chains (P1B w0waCDM quintom-B; ALP prior-predictive fraction next).

**Wrapped configs (existing, committed):**
- `reproducibility/cosmology/cobaya_control_pantheonplus.yaml` (Control A — done, w0+wa=-1.404±0.190)
- `reproducibility/cosmology/cobaya_control_desy5.yaml` (Control B — done, w0+wa=-1.572±0.206)
- next: ALP prior-predictive fraction config (open queue row)

**Skill dependency:** `skills/astro/cosmology-mcmc` (commit YAML before launch; R-1 gate; per-dataset control chains for shared-object joints; never quote overlapping-dataset sigma-distances as independent).

**Compute shape:** 4+ MPI chains on cheap CPU pods (~$0.17/hr A4000-class); chains on a network volume that survives pod stop; tmux session per chain pair.

**I/O contract:** input = committed Cobaya YAML; output = chains + getdist summary JSON at `reproducibility/cosmology/*_result.json`, R-1 recorded, mirrored to HF.

**QC gate:** R-1 ≤ 0.06 for direction claims (tighter for headline numbers); a joint result is quotable only next to its independent controls.

---

## Agent 3 — `anomaly-retrain` (survey-native classifier retrains + re-scores)

**Purpose:** native-domain retrains and held-out re-scores for the P3 anomaly engine and P4 chirality robustness (GZ1-only full-catalog re-inference; b/a cross-match; ≥200-axis harmonic injection battery).

**Wrapped pipelines (existing):**
- `pipelines/p3_anomaly_engine/` — survey-native retrains (SDSS native histogram done: 77,905 rescores), held-out re-scores (DESI done, Planck pending)
- `pipelines/p2_chirality/` — GZ1-only Z2-flip-equivariant vit_small retrain (done reduced-N: val acc 0.978, dipole z=-0.04σ) → full-catalog re-inference next

**Skill dependencies:** `skills/astro/sdss-lamost-catalogs` (native-over-cross-transfer, injection-recovery gating of catalog-grade totals) + `skills/astro/desi-spectra` (SPARCL re-pull verification) + `skills/astro/gaia-crossmatch` (dedup + novelty gates).

**Compute shape:** the one genuinely GPU-bound agent (retrains + large-batch inference). This is where AI-for-Science credits go first.

**I/O contract:** input = survey catalog + training config (labels provenance explicit: human GZ1 vs pseudo-labels); output = per-survey score histograms + result JSON (like `gz1only_dipole_result.json`) + model weights to HF.

**QC gate:** a survey enters "catalog-grade" totals only after injection-recovery PASS; label-provenance independence must be stated with every null claim.

---

## What Phase 0 still needs (Houston)

Run one of these (recommend Agent 1 on the committed C2 config — cheapest, fully scripted, known-good output to diff against) inside an actual Claude Science seat, and note where its provenance/artifact model and ours disagree. That boundary note completes Phase 0 and de-risks Phase 1 wiring.
