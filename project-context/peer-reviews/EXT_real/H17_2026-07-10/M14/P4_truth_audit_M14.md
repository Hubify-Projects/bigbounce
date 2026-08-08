# P4 — M14-EXT truth-audit (STRICT, ledger-first) — 2026-07-12, vs v1.0.239

Second consecutive ZERO-REJECT harvest for P4+P5 (M9 was the first). Raws read
VERBATIM before any disposition:
- `M14/P4_grok_M14.md` l.1 = `VERDICT: MINOR REVISIONS` (5 MINOR)
- `M14/P4_chatgpt_M14.md` l.1 = `(1) VERDICT: MAJOR REVISIONS` (14 MAJOR + 3 MINOR)
  — **ChatGPT's FOURTH consecutive non-REJECT** on P4 (after M7 floor-crack /
  M9 / M11). Reviewers saw v1.0.239. `tools/ledger_match.py` pre-match + full §3
  Opus truth-audit vs `pipelines/p2_chirality/chirality_catalog_paper.tex` + the
  canonical P4 disposition ledger.

## ChatGPT MAJOR — Q3 again CONCEDES the narrow HC null
Q3 (verbatim, raw l.133): *"No—the manuscript currently supports only a
non-detection in a post-selected observed-label subset, not the broader physical
chirality null or the claimed exclusion of a genuine 1.7% dipole."* — same
framing as M7/M9/M11: the residual dispute is the disclosed classifier-dilution
generalization (OPEN-COMPUTE frontier / post-selection re-flag), not a
genuinely-new reader-visible defect.

### Per-finding disposition (all source-cited RE-FLAG / OPEN-COMPUTE / OPEN-VENUE / OPINION)
- #1 `REVISIONS (2) ISSUES:` = parser-header noise (not a finding).
- #2 p_eq>0.6 not preregistered / post-selection, discards ~70% → **DP4-07** (§prereg tex L713 declares HC 0.6 a-priori; confidence-cut sweep stable; GZ1-human null z=−0.54).
- #3 1.7% physical dipole vs g≃0.398 dilution / observed-label mapping → **DP4-09/-01** (A50/A95 disclosed as observed-f_CW thresholds §sensitivity L1078; g is the disclosed bridge).
- #4 A50/A95 are detection-efficiency thresholds not confidence limits → **DP4-09** (verbatim disclosure §sensitivity L1078: "we do not claim them as physical morphology-dipole thresholds").
- #5 z≃−7.6 block-bootstrap not calibrated under A_ref → **DP4-14** ("not a calibrated frequentist exclusion significance" stated §wls_fit footnote L1410 / abstract).
- #6 primary null exchangeability / heteroscedastic pixels → **DP4-16** (density-stratified null +3.80σ; exchangeability limits disclosed; object-level likelihood = OPEN-COMPUTE).
- #7 classifier validation 66.5% pseudo-labels / 69.91% / 9.5σ offset / global-g inadequate → **DP4-15/-08** (spatially-resolved confusion = OPEN-COMPUTE; GZ1 differential-error disclosed §pseudolabel_independence L1073).
- #8 GZ1-human-only under-powered (A50∼3.4%, A95∼4.5–6.8%) → **DP4-09/-15** (coarse model-free cross-check, explicitly disclosed as corroboration-not-equivalent-sensitivity).
- #9 ~47% ℓ=1 harmonic residual "diagnostic" not statistically irrelevant → **DP4-17** (remainder disclosed + bounded a-fortiori below A50/A95 §monopole_mask_null L1005 / App-D; joint likelihood = OPEN-COMPUTE).
- #10 full-sample z≃4.2–4.4 dipole "circular" to call systematic → **DP4-17/-07** (disappears after the a-priori HC cut; full-sample WLS on unthresholded sample, disclosed).
- #11 image-level "end-to-end injection" only verifies algebraic equivariance → **DP4-15** (e2e mirror-flip closure DP4-15 T_eq=0.9997; sky-dependent physical injection = OPEN-COMPUTE frontier).
- #12 +3.64σ vs +7.93σ "canonical" harmonic non-unique (factor-2 rescale can't change z) → **DP4-01/-16** (different mean-subtraction/field/monopole conventions, disclosed noncomparable; not a defect).
- #13 Shamir 3.7–8.8× tension without matched Ganalyzer → **DP4-11** (explicitly restricted to "our DESI/ViT-Small pipeline; a matched Ganalyzer reanalysis remains required" §monopole_mask_null L1005).
- #14 A95 "f_CW units ≲1.5% ⇒ ≲3×10⁻² A_p" factor-of-2 inconsistency → **DP4-01/-13** — RE-DERIVED **ARITHMETICALLY CORRECT**: A_p=2(f_CW−½) ⇒ 1.5% f_CW-deviation = 3×10⁻² A_p (tex L1104); the "no rescaling" clause (L676/L1471) refers to Shamir's full-count asymmetry which *is* A_p, a distinct object. ChatGPT conflated the two objects — NOT an error (same as M5/M9/M11).
- #15(MIN) birefringence/Chern-Simons interpretation → **DP4-12** (already "in principle … pending a derived transfer function" §parity_translation L1173).
- #16(MIN) survey-selection provenance / parent-catalog distributions → **DP4-07/-08/-13** (documentation-detail request on disclosed provenance §II A + App B; no reset).
- #17(MIN) mutable main branch / DOI / commit hashes → **DP4-21** (OPEN-VENUE, minted at journal submission, Houston-gated).
- #18(MIN) repetitive / repository-paths-in-narrative / shorten → **DP4-13** (directive-M presentation half CLOSED-BY-EDIT v1.0.237; OPINION residual).

## Grok MINOR (5) — AFFIRMS the null
Closing (verbatim, raw l.11): the central real-space HC null "is supported by
the primary estimator, injection-recovery calibration, and extensive systematics
battery." MINOR = presentation polish (pattern-066).
- #1 header noise.
- #2 physical (pre-classifier) amplitude propagation of g / observed-vs-physical → **DP4-09/-01** (g is the disclosed bridge; observed-label limits disclosed).
- #3 47% ℓ=1 residual per-pixel systematics budget → **DP4-17** (bounded a-fortiori below A50/A95, disclosed OPEN-COMPUTE).
- #4 GZ1-human-only "corroboration" vs "equivalent-sensitivity confirmation" separation → **DP4-09/-15** (already framed as coarse cross-check).
- #5 Table I "reader's guide" so +3.64σ/+7.28σ not misread as detections → **DP4-13/-07** (primary/diagnostic split disclosed Table I + σ reader's note).
- (Data-availability #6) full DAS statement (excerpt cut off) → **DP4-21** (DAS present; DOI Houston-gated).

## Outcome
- ledger_match: Grok 4/6 auto-MATCHED; ChatGPT 10/18 auto-MATCHED — every
  UNMATCHED item Opus-adjudicated above to an existing D-id (parser-header noise
  or source-cited re-flag).
- **0 genuinely-new reader-visible editable findings.** All findings are
  RE-FLAG-DISCLOSED / OPEN-COMPUTE / OPEN-VENUE / OPINION / reconciled-convention.
  #14 factor-of-2 re-derived arithmetically CORRECT.
- **clean-wave streak 4→5** (M7/M9/M11/M14 all clean after the M5-INT P4-E7 reset).
- No bump; **v1.0.239 stands**; `directive_g.sh` NOT run (no EXT-triggered edit).
- **Cap HOLDS 74** (Grok MINOR 12 + ChatGPT MAJOR 6 + latest-EXT-Gemini 6 = 50+24).
  No verdict-tier change since M7.
- **Integrity:** both raws read verbatim before disposition (Grok l.1
  `MINOR REVISIONS`, ChatGPT l.1 `MAJOR REVISIONS`); Q3 concession lifted
  verbatim; #14 re-derived correct; no ACCEPT faked; every finding source-cited;
  no math fabricated; no version bumped.
