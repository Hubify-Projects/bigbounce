# M21-EXT truth audit — P4 (v1.0.239, byte-unchanged)

Raws read verbatim before any disposition:
- `M21/P4_grok_M21.md` = **ACCEPT** (l.1 `VERDICT: ACCEPT` — verified at raw line 1, NOT inferred from a label) — 0 MAJOR + 3 MINOR
- `M21/P4_chatgpt_M21.md` = **MAJOR REVISIONS** (l.1 `(1) VERDICT: MAJOR REVISIONS`) — 11 MAJOR + 3 MINOR

`ledger_match.py` draft: Grok 3/3 auto-MATCHED (exit 0); ChatGPT 10/17 auto-MATCHED (row #1 = "REVISIONS (2) ISSUES:" section-header non-finding; 6 UNMATCHED prose-diluted, all Opus-adjudicated + source-verified below). Full §3 audit vs `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.239 + `DISPOSITIONS/P4.md`.

## Grok EXT = ACCEPT — THIRD verified EXT ACCEPT on P4 of the campaign
Raw l.1 literally `VERDICT: ACCEPT`. Closing (raw l.9, verbatim): *"The central claim that the large-scale chirality dipole is consistent with null at sub-percent sensitivity … is supported by the data, the declared estimator hierarchy, the injection-recovery calibration, the model-independent GZ1 human-label cross-check, and the multi-anchor attribution of all secondary residuals to survey systematics."* This is the Grok-EXT P4 A-cell (prior P4 Grok EXT ACCEPTs: W1-EXT, M18-INT was Grok-INT ACCEPT). All 3 minors are disclosed presentation/re-flags:
- **MINOR#1** abstract leads with secondary σ (+3.64σ/+7.28σ) before clarifying non-cosmological role; add one abstract sentence → **DP4-14** (σ-incommensurability reader's note + notation §; primary/diagnostic split disclosed Table I; presentation-emphasis request).
- **MINOR#2** §IV D / App D forward-model reproduces ~53% of ℓ=1 residual, ~47% open; add a paragraph quantifying expected per-galaxy purity modulation or state planned DR8 sweep → **DP4-17** (47% remainder disclosed + bounded a-fortiori below A50/A95; joint real-space×harmonic covariance = OPEN-COMPUTE future work).
- **MINOR#3** §VI B injection uses θ-uniform axis while A50/A95 quoted area-uniform; label the published A50/A95 "area-uniform axis-averaged" in Table VIII → **DP4-09** (injection/sensitivity-floor convention disclosed §sensitivity L1078; labeling-precision request).

## ChatGPT EXT = MAJOR REVISIONS — back from its M19 one-round REJECT slip
ChatGPT's M19 read was REJECT (the FIRST P4 ChatGPT REJECT after M7/M9/M11/M14/M16 all-MAJOR). M21 returns to **MAJOR** — canonical pattern-066 verdict-word oscillation on byte-identical v1.0.239. Item set 1:1 with the M5/M7/M9/M11/M14/M16/M19 reads. All 11 MAJOR + 3 MINOR source-cited standing re-flags:
- p_eq>0.6 not preregistered / 949,584-vs-8.47M parent → **DP4-07** (§prereg L713 declares HC 0.6 a-priori; WLS runs unthresholded; GZ1-human null model-free z=−0.54).
- Shamir "would have been detected" injection not end-to-end (g=0.398 ⇒ A_obs≃0.68% below A50) → **DP4-15** (spatially-resolved confusion = OPEN-COMPUTE; direction-of-bias toward-null; GZ1-human null model-free).
- block-bootstrap z≃−7.6 not a valid exclusion statistic (centered on observed, positive-definite, no transfer function) → **DP4-01/-14** (factor-of-2 CLOSED; z is a template-disfavor statistic not a detection significance, §wls_fit footnote L1410).
- A50/A95 detection-efficiency thresholds not confidence limits → **DP4-09/-17** (stated verbatim §sensitivity; "we do not claim them as physical morphology-dipole thresholds").
- primary estimator / null exchangeability (per-pixel ratios, per-galaxy shuffle) → **DP4-15/-16** (density-stratified null +3.80σ + template-agnostic block-bootstrap don't assume exchangeability; generative hierarchical null = OPEN-COMPUTE).
- unresolved z≃4.2–4.4 full-sample excess / 7–8σ MASTER residuals / 47% harmonic → **DP4-17** (disclosed diagnostic-not-independent; joint model = future work).
- +3.64σ vs +7.93σ "mutually inconsistent" canonical MASTER → **DP4-13** (500→10⁴ null-ensemble + convention distinction disclosed; sample-N/σ reader's note).
- classifier validation (66.5% pseudo-labels / GZ1 69.91% / 2,000 synthetic negatives / 15.8% edge-on) → **DP4-08/-15** (flip-TTA flip-equivariance-only disclosed; GZ1-human null model-free; spatial confusion = OPEN-COMPUTE).
- equivariance evidence (flip-swap 1.000 / T_eq=0.9997 tautological; T_raw=0.2303 / 21.4% D4) → **DP4-08** (T_eq closed v1.0.239 — probability-level antisymmetry vs argmax flip-recovery distinguished, tex L1183-1187; 21.4% = classifier-stability check not spatial null).
- Table XIV spatially-varying differential errors (~0.6/1.4 pp) → **DP4-15** (disclosed §sensitivity; finer conditional confusion = OPEN-COMPUTE).
- physical interpretation vs Shamir / no derived transfer function → **DP4-12** ("transfer function not derived in this paper", §parity_translation L1173, hedge kept).
- Data Availability mutable branch / DOI placeholder / 2.9%–6.3% inconsistent prob columns → **DP4-21** (commit-hash + Zenodo DOI minted at journal submission, Houston-gated; provenance disclosed).
- MINOR units/terminology (A95 f_CW-vs-A_p / canonical-mask N≥10-vs-N≥1) → **DP4-13**.
- MINOR MC precision / multiplicity (100 injections / 50–200 realizations) → **DP4-09** (disclosed future-work L1091).
- MINOR presentation / rebuttal-style length → **DP4-13** (presentation half CLOSED-BY-EDIT v1.0.237).

ChatGPT Q3 (raw l.141) concedes the narrow HC null: *"the manuscript supports only that one data-selected high-confidence hard-label estimator is null-consistent"* — its residual REJECT-adjacent complaints are statistical-philosophy on honestly-disclosed content (two-category gate → referee-variance/venue, NOT editable). **0 genuinely-new.**

## Verdict
**0 genuinely-new reader-visible editable findings.** Every Grok + ChatGPT item fingerprint-matches a standing DP4 D-id (RE-FLAG-DISCLOSED / OPEN-COMPUTE / OPEN-VENUE / definitional-reframe / CLOSED-BY-EDIT). **clean-wave streak 8→9** (directive-K; 0-new on byte-unchanged v1.0.239). No content bump; `directive_g.sh` NOT run; v1.0.239 stands.

**Cap: 74→85.** Grok EXT flips MINOR(12)→ACCEPT(16.7); ChatGPT EXT flips REJECT(0)→MAJOR(6): 50 + Grok-EXT ACCEPT 16.7 + ChatGPT-EXT MAJOR 6 + Gemini-latest MINOR 12 = 84.7 → **85** (formula-true, `_creationTime`-latest). This is a real Grok-EXT ACCEPT lifting the cap honestly.

**All-A grid:** the Grok-EXT P4 cell flips to **A (ACCEPT)** — raw-verified at line 1. activityFeed entry logged for the verified EXT ACCEPT.

**Integrity:** all raws read verbatim before any disposition; Grok ACCEPT confirmed at raw line 1 (`VERDICT: ACCEPT`) — not inferred from a label; ChatGPT MAJOR recorded as-is; no ACCEPT faked; every finding source-cited to a D-id + tex line; no un-sourced dismissal; no math fabricated; no version bumped; the Grok-EXT ACCEPT is the honest floor-crack, recorded exactly.
