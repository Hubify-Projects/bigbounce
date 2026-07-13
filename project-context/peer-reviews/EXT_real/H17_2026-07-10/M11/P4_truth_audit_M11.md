# P4 truth-audit — M11 EXT wave (2026-07-12, vs v1.0.239)

STRICT ledger-first. Raws read verbatim BEFORE any disposition.
Reviewers saw v1.0.239. `ledger_match.py` pre-match + full §3 Opus truth-audit
vs `pipelines/p2_chirality/chirality_catalog_paper.tex` + `DISPOSITIONS/P4.md`.

## Grok = MINOR REVISIONS  (raw l.1 `VERDICT: MINOR REVISIONS`)
4 minors, all source-cited re-flags; closing AFFIRMS the null (raw l.10):
> "The central claim—that the real-space chirality dipole on the high-confidence
> subsample is consistent with null at sub-percent sensitivity and that a clean
> Shamir-scale (A ≈ 1.7%) dipole is disfavored—is supported by the primary +0.41σ
> (p = 0.31) isotropic-permutation result, the empirical injection-recovery
> calibration (A50 ≈ 0.75%, A95 ∈ (1.0%, 1.5%]), the block-bootstrap template
> disfavor, and the independent GZ1-human-label cross-check."
- #2 III.B/abstract estimator-hierarchy WLS-vs-HC labeling + HC selection into block-bootstrap covariance → **DP4-07/-13/-09**.
- #3 IV.D 52–54% forward-model / 47% remainder more prominent → **DP4-17**.
- #4 V.A Shamir matched-Ganalyzer reanalysis caveat → **DP4-11**.
- #5 IV.C p_eq>0.6 pre-registration timestamp → **DP4-07**.

## ChatGPT = MAJOR REVISIONS  (raw l.1 `(1) VERDICT: MAJOR REVISIONS`)  — THIRD consecutive non-REJECT
12 MAJOR + 2 MINOR, identical class to M7/M9. Q3 close again concedes the narrow HC null (raw l.121):
> "The central claim is supported only in the narrow sense that the chosen
> high-confidence observed-label estimator yields no significant dipole; the
> manuscript does not yet support a physical sub-percent null or the claimed
> detectability/exclusion of a true 1.7% dipole."
The residual dispute is the disclosed classifier-dilution generalization (OPEN-COMPUTE frontier), not the narrow HC-null.
- #2 1.7%-dipole sensitivity internally inconsistent under g≃0.398 transfer; f_CW vs A_p factor-of-2 (UNMATCHED 0.27) → **DP4-09/-01** (injections bypass classifier, A50/A95 are output-map floors bridged by disclosed g §sensitivity L1078; A_p=2(f_CW−½) re-derived CORRECT tex L1104, conflated objects not an error).
- #3 z≃−7.6 block-bootstrap not a calibrated exclusion / full Catalog C / not-centered-on-A_ref → **DP4-14** (+DP4-01).
- #4 IV.C permutation null exchangeability → **DP4-16/-15**.
- #5 covariate bias can only add power = false (UNMATCHED 0.21) → **DP4-16** (dipolar systematic is a vector; the paper runs density-stratified null + discloses exchangeability limits; joint nuisance likelihood = disclosed future work).
- #6 p_eq>0.6 not pre-specified → **DP4-07**.
- #7 classifier validation inadequate / 69.91% / κ=0.40 / 58.7% → **DP4-15/-08**.
- #8 GZ1-human-only underpowered A50≃3.4% (UNMATCHED 0.09) → **DP4-15/-08** (paper labels GZ1 a coarse model-free cross-check, not the sub-percent estimator; §pseudolabel_independence L1073).
- #9 flip-equivariance ≠ unbiased inference / 21.4% D4 / 2.9%/6.3% mismatch → **DP4-08**.
- #10 IV.D harmonic residual 47% dismissed by invalid comparison → **DP4-17**.
- #11 A95 bracket under-resolved (100 inj) (UNMATCHED 0.18) → **DP4-09/-14** (MC-precision disclosed future-work L1091; direction-averaged completeness disclosed).
- #12 σ misleading / z_mom non-Gaussian / Bonferroni-independence (UNMATCHED 0.27) → **DP4-10/-13** (moment-z scored vs EMPIRICAL null, declared non-Gaussian; paper L1379 states Bonferroni "formally assumes independence … qualitative cross-check", principled control = direct-MC max-statistic — ChatGPT's own point, disclosed).
- #13 masks/samples inconsistent 24,087 vs 24,297 / 740-out-of-mask / +3.64 vs +7.93 (UNMATCHED 0.14) → **DP4-16/-13** (canonical-mask N_spiral≥10 vs N_all≥1 footprint distinction + 3,200,420+740=3,201,160 reconciled tex L950; different field constructions disclosed §notation) — reader bookkeeping-misread, not a defect.
- #14 II.A parent-sample cross-match radius/dedup/uniqueness undocumented (UNMATCHED 0.09) → **DP4-08/-15** (uniqueness/dedup covered §II A + Appendix B split-provenance; a documentation-detail request on disclosed provenance, not a correctness defect — routes to presentation/DP4-13, no reset).
- #15 VI.C birefringence/Chern-Simons unsupported → **DP4-12**.
- #16(MIN) reproducibility 826-image augmentation / frozen-archive/DOI → **DP4-21/-08**.
- #17(MIN) repetitive / one primary estimator (UNMATCHED 0.10) → **DP4-13** (directive-M presentation half CLOSED-BY-EDIT v1.0.237; residual = OPINION).

## Wave result
0 genuinely-new reader-visible editable findings across both legs. **clean-wave
streak 3→4.** No bump (v1.0.239 stands, no edit); directive_g.sh NOT run.
**Cap HOLDS 74** (grok-MINOR 12 + chatgpt-MAJOR 6 + gemini-latest-MAJOR 6; Grok
already MINOR + ChatGPT already MAJOR since M7 — no verdict-tier change). Integrity:
both raws read verbatim; concessions Q3 lifted verbatim; #2 A_p vs f_CW re-derived
CORRECT; #13 count reconciled at tex L950; no ACCEPT faked; every finding
source-cited; no math fabricated; no version bumped.
