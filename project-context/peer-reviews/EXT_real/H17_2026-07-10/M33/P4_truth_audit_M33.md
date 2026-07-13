# P4 truth-audit — M33-EXT (2026-07-13, vs byte-unchanged v1.0.239)

**Legs:** Grok EXT (Expert) + ChatGPT EXT (Extended Thinking). Raws: `M33/P4_grok_M33.md`, `M33/P4_chatgpt_M33.md` (both read verbatim). Screenshots present.
Served md5 (v1.0.239) = **15211f0f134095ef153f319931358f0a — byte-unchanged since M30** (no edit M30→M33).

**Grok VERDICT (raw line 1): MINOR REVISIONS** — 5 MINOR.
**ChatGPT VERDICT (raw line 1): MAJOR REVISIONS** — 12 MAJOR + 2 MINOR.

## Pattern-066 walk on byte-identical v1.0.239 (verify 1:1)
Grok has now read this *byte-identical* manuscript as: **M21 ACCEPT → M24 MINOR/FAILED → M30 MAJOR → M33 MINOR**. The M33 minor set is the identical disclosed-content set (p_eq>0.6, 47% residual, Shamir caveat, injection convention, DOI) oscillating in severity — textbook maximal-harsh-referee variance on unchanged content, **NOT new findings** (pattern-066, DP4-18 fingerprint).

## Grok M33 (MINOR) — per-finding disposition
1. [MINOR] p_eq>0.6 (N=949584) a-priori motivation vs post-sweep; state 0.6-vs-0.5/0.7 rationale in main text → **DP4-07** (§prereg L713 declares HC 0.6 a-priori; sweep stable p_eq∈{0.6,0.7,0.8}; GZ1-human null z=-0.54). RE-FLAG-DISCLOSED.
2. [MINOR] Imaging+morphology forward model accounts for only ≈52-54% of ℓ=1 residual; state max cosmological-dipole fraction in remainder → **DP4-17** (47% remainder disclosed, bounded a-fortiori below A50/A95; joint covariance = OPEN-COMPUTE future work) + **DP4-09**.
3. [MINOR] Shamir 1.7-4% amplitude-tension: put matched-Ganalyzer-reanalysis caveat in abstract+conclusions too → **DP4-11** (caveat disclosed §monopole_mask_null L1005; placement/emphasis = presentation, not a defect).
4. [MINOR] Injection-recovery θ-uniform vs area-uniform convention + A95 definition in main text → **DP4-09** (injection convention disclosed §sensitivity L1078; presentation-placement re-flag).
5. [MINOR] Data-availability: give exact commit hash freezing p_eq>0.6 + generator script → **DP4-21** (commit-hash/Zenodo-DOI minted at journal submission, Houston-gated) + **DP4-13** (artifact-paths).

## ChatGPT M33 (MAJOR) — per-finding disposition (1:1 with M26/M30 set)
1. [MAJOR] End-to-end sensitivity not demonstrated; injection bypasses ViT/triage/confidence; g≃0.398 maps 1.7%→0.68% below A50 → **DP4-09** (injection-not-end-to-end / A50-A95 output-floors, disclosed) + **DP4-01** (g-dilution built on the corrected numbers).
2. [MAJOR] z≃-7.6 not a calibrated hypothesis test (bootstrap around observed, positive-definite, direction nuisance) → **DP4-01/-14** (block-bootstrap = template-disfavor statistic not detection significance, disclosed §wls_fit L1410).
3. [MAJOR] p_eq>0.6 cut inseparable from result; not independent preregistration → **DP4-07** (§prereg a-priori; sweep stable; GZ1 null).
4. [MAJOR] Classifier validation insufficient (69.91% acc; 21.4% D4 argmax flips) → **DP4-08** (flip-TTA≠rotation-equivariance, D4 flip = stability check, disclosed) + **DP4-15** (spatial confusion = OPEN-COMPUTE).
5. [MAJOR] Randomization null not a realistic cosmological likelihood (pixel-permutation exchangeability) → **DP4-16** (generative hierarchical null = OPEN-COMPUTE; density-stratified null +3.80σ + block-bootstrap don't assume exchangeability, disclosed).
6. [MAJOR] Non-null harmonic result unresolved; 47% remainder; recovery thresholds ≠ contamination bounds → **DP4-17** (47% disclosed, bounded a-fortiori; joint covariance OPEN-COMPUTE).
7. [MAJOR] "σ" misleading for non-Gaussian nulls (z=7.31 → p=6e-4); use standardized moment ratios → **DP4-10** (moment-z scored vs empirical per-pixel-shuffle null, non-Gaussian declared, disclosed).
8. [MAJOR] Additive/multiplicative bias can rotate/cancel dipole, not only push to null; two estimators not independent → **DP4-09/-16** (toward-null direction argued + GZ1 model-free; joint nuisance = OPEN-COMPUTE).
9. [MAJOR] Missing image-parity / WCS-orientation audit across BASS/MzLS/DECaLS/DES → **DP4-11** (pipeline-specific leakage restricted; parity convention within Smith42 ingestion) + **DP4-08** (ingestion validation). RE-FLAG-DISCLOSED / OPEN-COMPUTE-adjacent (no genuinely-new editable defect; the parity-audit ask is the same image-level-compute class as DP4-15/-16, honestly out-of-scope-for-edit).
10. [MAJOR] Not tied to immutable release (mutable main branch, DOI later, raw/eq mismatch flag, 3,200,420 vs 3,201,160) → **DP4-21** (DOI/hash Houston-gated at submission) + **DP4-13** (bookkeeping-N distinctions tabulated).
11. [MINOR] ECE lower bound not consistent (Jensen on same sample) → **DP4-08 family** (paper L1345 computes Jensen lower bound ECE≥|p̄−acc| on disjoint GZ1 + notes reliability diagram would refine; disclosed).
12. [MINOR] Look-elsewhere: Bonferroni valid under dependence; p_LEE≤1e-4 for local 3.05 needs definition → **DP4-13** (paper L1379 states Bonferroni "formally assumes independence … qualitative cross-check only"; principled control = direct-MC max-statistic; disclosed).

## Verdict
**0 genuinely-new editable findings** across both legs. Every Grok minor + every ChatGPT major/minor fingerprint-matches a standing DP4 D-id (RE-FLAG-DISCLOSED / OPEN-COMPUTE / OPEN-VENUE / definitional-reframe). The Grok ACCEPT→MINOR→MAJOR→MINOR walk on byte-identical content = pattern-066; the ChatGPT MAJOR set is 1:1 with M26/M30. No fabrication; no ACCEPT faked; no finding dismissed without a source-cited D-id; no math fabricated.

**clean-wave streak 11→12** (directive-K; both legs 0-genuinely-new on byte-unchanged v1.0.239; prior 11 from M30). No bump; `directive_g.sh` NOT run; v1.0.239 stands.

**Cap:** Grok flips MAJOR(6)→**MINOR(12)** (restores +6), ChatGPT holds MAJOR(6), Gemini-EXT-latest carry-forward. Formula 50 + Grok-MINOR-latest + ChatGPT-MAJOR-latest + Gemini-EXT-latest — recomputed by `post_verdict.sh` from `_creationTime`-latest legs.

**Integrity:** both raws read verbatim before any disposition; Grok MINOR + ChatGPT MAJOR recorded as-is (verified at raw line 1); no severity steering; no version bumped.
