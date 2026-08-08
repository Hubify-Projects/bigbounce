# P1B v1B.0.109 exact-board truth audit

**Audit date:** 2026-07-15

**Disposition:** **MAJOR REVISION — READINESS HOLD 56/100**

**Submission status:** **DO NOT SUBMIT**

**Audit mode:** read-only inspection and independent local numerical checks; no Anthropic or OpenAI API call

## Exact review binding

- Paper: P1B, `arxiv/paper1b_mcmc_companion.tex`, stamped `v1B.0.109` at line 264.
- Review source commit: `54aeaae34614e24ee9d106416b46b7bbb5718128`.
- Exact reviewed PDF SHA-256: `36b8fc984b5be164f5ece1e2f0c3f661dfb49c9f99faa76e2b050e2bd0674a78` (20 pages).
- Review packet: `47eebe6e934ec16a2b4072f83de749b9ceda644550a0f750fa282ae5af0f7d22`.
- Board inputs: `intwave_P1B_codex_0313.md`, `API_P1B_gemini.md`, and `API_P1B_grok.md` in this directory.

The board is validly bound to one exact PDF. Its optimistic Gemini/Grok verdicts do not override the source-level defects below. The Codex physical-spectrum finding is confirmed, and the BBN audit found an additional executed-provenance defect.

## Finding dispositions

### 1. NaMaster input spectrum — confirmed major; production rerun required

`reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py:116-128` constructs an EE array from Gaussian peaks with amplitudes 15, 40, 20, and 8 microkelvin-squared. The script then passes that array directly to `hp.synfast` at lines 209-210. `healpy.synfast` consumes raw angular spectra, `C_ell`, not `D_ell = ell(ell+1)C_ell/(2 pi)`.

At `ell=140`, the executed function gives `C_ell^EE = 39.9030905152 microkelvin^2`. A local independent CAMB calculation with representative Planck-like parameters gives raw `C_140^EE = 3.583361e-4 microkelvin^2`, so the executed value is approximately `1.11357e5` times too large. Even under the charitable interpretation that the peak amplitudes were meant as `D_ell`, the missing conversion factor alone is

`ell(ell+1)/(2 pi) = 3141.72` at `ell=140`.

The additional assignment `cl_bb = 0.05 * cl_ee` at line 133 is not a physical lensed-BB spectrum.

**Scientific impact.** The algebraic window-contraction identity remains a valid linear operator test because both sides use the same input arrays. The physical validation does not survive: the claimed Planck-like EE sky, 10-microkelvin-arcmin signal-to-noise regime, Monte Carlo scatter and standard error, SNR, and numerical bias/systematics checks were evaluated with a radically incorrect signal amplitude and nonphysical BB shape. A prose correction cannot repair these outputs.

**Required closure.** Replace the surrogate spectra with explicitly raw CAMB `C_ell^EE` and physical lensed `C_ell^BB`, record cosmological parameters/CAMB version/units and spectrum hashes, rerun the complete 500-realization production and robustness suite, regenerate every dependent JSON/figure/table/text value, retain the present artifacts as superseded rather than overwriting them, compile a new exact PDF, and send that PDF through a new bound review. Until then the manuscript may claim only an algebraic operator/unit validation, not a physical-noise or physical-scatter validation.

### 2. Executed BBN predictor — confirmed provenance/reproducibility defect

The manuscript says that the frozen runs explicitly used the PArthENoPE predictor (`arxiv/paper1b_mcmc_companion.tex:1778-1787`). The execution record says otherwise:

- `reproducibility/cosmology/frozen/full_tension_20260311_1728/chains/chain_01/spin_torsion.updated.yaml:1-12` records CAMB 1.6.5 and contains no `bbn_predictor` override. The other frozen-chain metadata inspected likewise contain no override.
- The four public reproduction YAMLs later acquired `bbn_predictor: PArthENoPE` (for example, `reproducibility/cosmology/cobaya_full_tension.yaml:41`). Git blame places that addition in commit `6c9fa47f`, after the March frozen runs.
- With the locally installed CAMB API, the literal string `PArthENoPE` is treated as a predictor/table name and raises `FileNotFoundError`; it is not a valid generic alias. A concrete valid table filename or the executed default is required.

Therefore the frozen chains used the CAMB 1.6.5 default BBN-consistency predictor, not the post-hoc YAML setting claimed by the paper. The negative-Delta-N_eff range is not itself evidence of a numerical failure: a valid local PArthENoPE table evaluates smoothly at Delta-N_eff = -1, 0, and +2, and no symmetry assumption is scientifically required. The defect is the false executed-provenance statement and non-runnable reproduction pin.

**Required closure.** Recover and name the exact CAMB 1.6.5 default table from the archived execution environment/package, record its file hash and interpolation domain, change the public YAMLs to the exact executable setting that reproduces the frozen runs, and revise the manuscript to say that the executed chains used the CAMB 1.6.5 default. Compare the executed-default and chosen PArthENoPE helium predictions across the sampled `(ombh2, Delta N_eff)` domain; run a bounded sensitivity chain only if that comparison is scientifically material. Do not add unsupported language about symmetric interpolation.

### 3. Full-EB likelihood — real scope/acceptance gate, already disclosed

The manuscript correctly states that the ALP leg uses the single Gaussian summary `0.342 +/- 0.094 deg`, is not an independent confirmation, and that a full joint-EB refit could shift the posterior (`arxiv/paper1b_mcmc_companion.tex:2402-2426,3276-3299`). The reviewed arithmetic and conditioned/unconditioned counts are internally reproducible.

**Disposition.** This is not a newly discovered arithmetic error. The present method can support narrowly labeled fixed-background accommodation and selection-frequency statements. It cannot support robust JCAP parameter inference for `m`, `C_agamma`, or the spectator subset under the real EB covariance, calibration, foreground, and likelihood structure. A full-EB analysis is required before elevating those quantities to robust parameter measurements; otherwise retain the current explicit surrogate scope and choose a technical-companion/note format.

### 4. S8 overlay burn-in — confirmed bounded numerical inconsistency

`reproducibility/cosmology/c13_s8_desy3_overlay.py:25-40` loads every chain with `ignore_rows: 0`, while the manuscript declares a uniform conservative 30% burn-in (`arxiv/paper1b_mcmc_companion.tex:1812-1841`). The all-row artifact reports overlap integrals 0.0544 and 0.1249 and tensions 2.60 and 2.01 sigma (`reproducibility/cosmology/c13_s8_desy3_overlay.json:28-31`). The committed 30%-burn summaries give:

- Planck+BAO+SN: `S8 = 0.8272911482 +/- 0.0099869531`.
- Full-tension: `S8 = 0.8140908942 +/- 0.0084563771`.

Those values round to the present headline numbers, so no major conclusion change is presently indicated. The KDE overlap values nevertheless have not been computed under the paper's declared cut.

**Required closure.** Set a per-chain 30% burn-in in the overlay loader, regenerate the JSON and PNG, and update every exact overlap/tension value. Preserve raw and post-burn sample counts explicitly.

### 5. ALP mass wording and mixed estimands — confirmed wording correction

The direct weighted `c5_continuous` readout gives full-chain `m/H0` 16/50/84 percentiles `1.70799 / 13.17415 / 196.65465` (`research/branch_R_alp_birefringence/phase2_mcmc/c5_table_iv_recompute.json`, full subset). Direct weighting of the same chain shows only 4.9363% of its weight in the uppermost 0.2 dex of the five-dex mass prior. That does not support the continuous-prior figure caption's statement that the mass marginal “piles toward the upper edge” (`arxiv/paper1b_mcmc_companion.tex:2866-2869`).

The separate `m=37.2 H0` value belongs to the fixed-`C_agamma=8` fit (`arxiv/paper1b_mcmc_companion.tex:1429,2497,3217`), whereas the continuous-prior full-chain median is `13.17 H0`. Passages that place `37.2 H0` beside continuous-prior `C_agamma` or spectator-selection results (`:2412-2421,3293-3297`) risk mixing estimands.

**Required closure.** No rerun is needed. Replace “piles toward the upper edge” and “data-driven pull to the edge” with “broad high-mass tail” or an exact quantile statement. Label `37.2 H0` explicitly as fixed-coupling and `13.17 H0` explicitly as continuous-coupling wherever they coexist. The separate statement that the tiny `theta_i <= 0.1` sliver pushes `C_agamma` high is supported and should not be conflated with the mass-prior claim.

### 6. Standalone venue/cohesion — editorial decision, not a numerical defect

Gemini's request for a connecting paragraph and Codex's standalone-JCAP concern are reasonable editorial judgments, not falsifiable source defects. After the two scientific closures above, choose one format deliberately: technical companion, methods note, supplement/merge with P1A, or a standalone paper with a genuinely unified methods contribution. A connecting paragraph can improve readability but cannot guarantee venue acceptance.

### 7. Immutable release manifest — confirmed release gate

The paper is stamped v1B.0.109 but cites `reproducibility/p1b_analysis_artifact_manifest_v1B.0.108.json` (`arxiv/paper1b_mcmc_companion.tex:2996-3004`). That pre-release manifest cannot bind the new conditioned-ALP artifacts, corrected rerun products, exact reviewed PDF, and final source state.

**Required closure.** After the numerical closures, generate a v1B.0.109-or-later manifest containing the exact source and PDF hashes, all new generator/result/receipt files, load-bearing artifacts, and Git LFS payload OIDs. Freeze source, PDF, manifest, and artifacts under one public commit/tag and persistent archive/DOI. Do not fabricate a DOI or describe a mutable branch as immutable.

### 8. Remaining Gemini/Grok minors

- The c15 chain's `R-1 = 0.0147` limitation is already disclosed as corroborative and non-load-bearing (`arxiv/paper1b_mcmc_companion.tex:2372-2398`). R-hat alone does not imply a defensible maximum posterior-mean shift, so Gemini's suggested “fraction of a percent of sigma” should not be added. Either keep it non-load-bearing or run it to the declared threshold.
- Grok's request to label prior-predictive values as Monte Carlo frequencies is already satisfied repeatedly, including `arxiv/paper1b_mcmc_companion.tex:1352,2402-2426,2964`. No further scientific closure is needed.
- Grok's burn-in-footnote concern is editorial. It can be shortened after the 30%-burn artifact is regenerated, without changing the raw/post-burn/weighted distinctions.

## Readiness hold and bounded closure plan

Readiness is held at **56/100**. This is not an acceptance probability. It is an operational hold reflecting one production-rerun major, one executed-provenance major, one explicit full-EB scope gate, two bounded numerical/wording corrections, and an open immutable-release gate.

Closure sequence:

1. **Correct the NaMaster spectrum contract and add a unit regression** that fails when a D-ell-like spectrum is passed as raw C-ell.
2. **Run the complete physical-spectrum 500-MC and robustness suite**; regenerate all dependent artifacts and scientific prose.
3. **Repair BBN executed provenance** from frozen CAMB 1.6.5 metadata, validate the exact default table/domain/hash, and run only the sensitivity comparison warranted by the table-level difference.
4. **Regenerate the S8 overlay at 30% burn-in** and close exact overlap/tension values.
5. **Correct ALP mass language and estimand labels**; retain the already honest full-EB limitation.
6. **Compile and visually audit a new PDF**, including overflow/reference/URL checks.
7. **Run a new exact-PDF multi-model board**. Acceptance requires no unresolved blocker or major and no invalid/mismatched receipt.
8. **Create the final immutable manifest/archive binding**, then update SSOT/site/Convex in the same release commit.

P1B must remain out of the submission bundle until steps 1-7 pass. Step 8 is required before public submission/release.
