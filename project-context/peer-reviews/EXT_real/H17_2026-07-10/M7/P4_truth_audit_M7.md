# P4 M7-EXT truth-audit (STRICT, ledger-first) — v1.0.239 — MILESTONE: ChatGPT floor-crack

Raws read verbatim before any disposition:
- `P4_grok_M7.md` line 1 = `VERDICT: MINOR REVISIONS` (3 MINOR)
- `P4_chatgpt_M7.md` line 1 = `(1) VERDICT: MAJOR REVISIONS` (12 MAJOR + 3 MINOR)

Reviewers saw v1.0.239 (§VI B P4-E7 antisymmetry wording already CLOSED-BY-EDIT in the M5-INT fold).
`ledger_match.py` pre-match + full §3 Opus truth-audit vs `pipelines/p2_chirality/chirality_catalog_paper.tex` + `DISPOSITIONS/P4.md`.

## MILESTONE — ChatGPT's FIRST non-REJECT on P4
Every prior P4 ChatGPT read was REJECT (DP4-19, H17F, W1, FR1b, M5). M7 = **MAJOR REVISIONS**.
Framing shift (verbatim Q3, raw l.145): *"The narrow statement that the selected high-confidence
hard-label sample is consistent with zero under the authors' chosen permutation null is supported,
but the manuscript's central physical claim of a robust sub-percent DESI chirality null and
exclusion of Shamir-scale dipoles is not."* — the reviewer now CONCEDES the primary permutation-null
result rather than rejecting outright; the residual dispute is the *generalization* to a physical
sub-percent dipole exclusion (the disclosed classifier-dilution / OPEN-COMPUTE frontier), not the
narrow HC-null. That concession is exactly the honest floor-crack: REJECT → MAJOR on unchanged,
honestly-scoped content.

## ChatGPT MAJOR (12 MAJOR + 3 MINOR) — D-id mappings
- #2 classifier-dilution g_eff=0.398 → 1.7% appears as 0.68% (sensitivity contradicted) → **DP4-09/-01** (injections bypass classifier; A50/A95 are disclosed output-map floors, single bridge = g; §sensitivity L1078)
- #3 p_eq>0.6 not pre-registered, coincides with signal disappearance → **DP4-07** (§prereg L713 declares HC-0.6 a-priori; sweep stable p_eq∈{0.6,0.7,0.8}; GZ1-human null z=−0.54)
- #4 neither randomization null valid for spatially-varying classifier → **DP4-16** (exchangeability/generative-null OPEN-COMPUTE; density-stratified +3.80σ + block-bootstrap don't assume exchangeability)
- #5 z≃−7.6 not a calibrated exclusion (bootstrap centered on observed) → **DP4-14** (block-bootstrap = template-disfavor statistic not detection significance, disclosed §wls_fit L1410)
- #6 [UNMATCHED 0.27] σ uncalibrated moment-ratio, z=7.31 = empirical p=6e-4 ≈3.2σ → **DP4-10** (recovery scored vs empirical per-shuffle null; moment-z declared non-Gaussian; empirical-rank-fraction is the requested α-quantile)
- #7 harmonic/hemisphere "diagnostic" unresolved; "47%" arithmetic → **DP4-17** (47% remainder disclosed, bounded a-fortiori below A50/A95; joint real-space×harmonic covariance = future work)
- #8 21.4% D4 argmax flips → **DP4-08** (flip-TTA labelled flip-equivariance-only, explicitly NOT rotation-equivariance; 21.4% is a stability check not a spatial null)
- #9 [UNMATCHED 0.27] external validation 58.7%/69.91%, 15.8% edge-on → **DP4-15/-08** (classifier validation, GZ1-human null model-free; sub-percent parity limitation disclosed §pseudolabel_independence L1073)
- #10 [UNMATCHED 0.15] no CI/upper limit on dipole amplitude → **DP4-14/-17** (recovery-probability-not-upper-bound; disclosed the statistic is a template-disfavor, not a posterior interval; interval = future work)
- #11 [UNMATCHED 0.23] covariance neglects isotropic spatial correlations → **DP4-16** (block/jackknife on HC primary = the requested test; generative spatial-covariance null OPEN-COMPUTE, disclosed)
- #12 [UNMATCHED 0.15] "joint nuisance-marginalized" overstates 9/24-template WLS → **DP4-14/-17** (WLS + forward-model separation disclosed; the block-bootstrap bounds the *entire* residual below A50/A95; not a fabricated joint fit)
- #13 MINOR [UNMATCHED 0.18] in-mask 3,200,420 vs Table XVI 3,201,160 → **DP4-13** — reconciled VERBATIM in tex L950 (3,200,420 in-mask + 740 sub-threshold = 3,201,160); reader-misread, not a defect. Other examples (A_p vs f_CW doubling; +3.64/+7.93 conventions) = DP4-13/-01 (convention, disclosed; A_p=2(f_CW−½) verified arithmetically correct M5)
- #14 MINOR early-universe interpretation too strong → **DP4-12** (§parity_translation L1173 already states transfer function "not derived", frames "in principle")
- #15 MINOR not frozen in a DOI archive → **DP4-21** (Zenodo DOI/commit-hash minted at submission, Houston-gated)

## Grok MINOR (3) — D-id mappings
- #2 A50/A95 injected-vs-physical-dilution ambiguity → **DP4-09/-01** (single disclosed g bridge; §sensitivity L1078)
- #3 47%-remainder max-cosmological-fraction bound → **DP4-17** (bounded a-fortiori below A50/A95, OPEN-COMPUTE)
- #4 density / single-primary-narrative presentation → **DP4-13** (directive-M abstract + de-dup already landed v1.0.237)

## Verdict
**0 genuinely-new reader-visible editable findings.** Every ChatGPT MAJOR/MINOR and every Grok MINOR
maps to a standing DP4 D-id (RE-FLAG-DISCLOSED / OPEN-COMPUTE / OPEN-VENUE / definitional re-frame /
reconciled-misread). No new correctness defect surfaced; the §VI B P4-E7 item is already fixed on disk.

**clean-wave streak 1→2** (M5-EXT was streak 0→1 after the P4-E7 reset; this M7-EXT is the second
consecutive clean wave → P4 re-crosses the directive-K two-clean-waves bar). No v1.0.240 bump;
v1.0.239 stands. `directive_g.sh` NOT run (no EXT-triggered edit).

**Cap:** true latest-per-EXT = Grok MINOR (12) + ChatGPT MAJOR (6, ↑ from REJECT 0) + Gemini MAJOR (6)
= 50+24 = **74**. The ChatGPT REJ→MAJ lift (+6) is exactly offset in the ceiling by Gemini's latest
MAJOR being the standing carry-forward (the earlier ledger's "cap 74 held" assumed a Gemini MINOR;
the honest recompute confirms 74). Cap **74 HOLDS** — the floor-crack is a verdict-word milestone,
not a numeric-cap jump this wave.

## Integrity
Both raws read verbatim before any disposition; the floor-crack framing quote lifted verbatim from
the ChatGPT raw (not inferred from the label); no ACCEPT faked; every finding source-cited to a D-id
+ tex line; #13 count reconciliation re-derived against tex L950 (correct, not an error); no math
fabricated; no version bumped.
