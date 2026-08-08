# INT leg — Claude (Anthropic subscription, Claude Code subagent)
- model: claude-opus-4-8 (Opus-tier subagent)
- date: 2026-07-16 (PT)
- paper: P4 v1.0.262
- pdf_sha256: f59fc937597efe749894eca426e623b21b918bd8e977c9edd85a75732b494cb2
- venue: The Astrophysical Journal Supplement Series (APJS-CATALOG-METHODS, Catalog + methods article)
- PARSED VERDICT: MAJOR REVISIONS

---

## Referee report — The Astrophysical Journal Supplement Series
### Profile: APJS-CATALOG-METHODS (Catalog + methods article)

**(1) VERDICT: MAJOR REVISIONS**

This is a careful, unusually honest catalog-and-methods manuscript releasing observed
chirality labels for 8,474,531 DESI Legacy DR8 galaxies and testing a single primary
chirality-dipole null. The equivariant test-time-averaging design, the explicit estimator
decision tree, and the frank separation of one primary estimator from a battery of
systematics diagnostics are genuine strengths and above the honesty bar of most
morphology-catalog releases. The primary null is internally defensible. However, at a
strict ApJS bar the paper has several substantive gaps — centered on the reproducibility
of the label-generating model, the unmodeled coexistence of multiple ~7σ estimator
channels, a post-hoc sample-defining cut, and a large unexplained monopole in the
released product — that in my judgment require another substantive round before
acceptance. None are fatal; the science is not wrong; but disclosure alone does not
discharge them for a catalog that is the deliverable.

---

**(2) ISSUES**

**[MAJOR] 1 — Label-generating model is not reproducible; committed training records
conflict (§2.2, §B, Table 12, Table 4 caption).** For a catalog+methods paper the
generating classifier is part of the product, yet the manuscript repeatedly concedes
"the exact historical training realization is not fully recoverable." The committed
records disagree: 26,616 vs 26,626 total rows; 826 vs 846 CE non-spirals; 93.6878% vs
92.10% validation accuracy; no retained object/split manifest or random-state receipt.
ApJS catalog releases are held to a reproducibility contract; here the released labels are
frozen and checksummed (good), but the process that produced them cannot be replayed and
its own committed audit trail is internally inconsistent. The paper should either
reconcile these records to a single realization or state precisely and prominently what a
catalog user can and cannot reproduce, and how the conflict bounds label provenance.

**[MAJOR] 2 — No joint covariance / joint likelihood while several estimators show ~7σ
"signals" that are asserted, not demonstrated, to be systematics (§3.2, §4.4, Tables 2,
6, 7).** The WLS template fit (z ≈ −7.6), the exact-support MASTER ℓ=1 (z = +6.923 binary,
+7.033 apodized), and the binomial-monopole null (z = +6.983 / +7.207) all sit alongside
the p=0.238 primary. The paper attributes every one of these to systematics via
different-support / different-null arguments and explicitly leaves "the missing joint
covariance … an open methodological gate." That is honest, but a referee needs positive
evidence that the primary HC real-space channel is not contaminated by whatever produces
the 7σ harmonic/WLS excursions — at minimum a cross-consistency demonstration on a shared
support, or an explicit argument (beyond "different support") for statistical
independence. As written, the systematics interpretation of the load-bearing null-vs-signal
contrast is a declaration, not a result.

**[MAJOR] 3 — The primary sample is defined by a post-hoc, post-unblinding cut (§4.1,
lines 481–485; App B).** The `raw_flip_qc_unsafe` quarantine that yields the headline
N_selected = 890,069 was "introduced and finalized during post-review closure … not
preregistered or fixed before unblinding." The stability check (+0.48 excluded vs +0.52
baseline, line ~998) is reassuring and should be promoted from Appendix B into the main
Results, together with the full unsafe-inclusive real-space primary value, so the reader
can judge the cut's effect on the headline channel directly rather than inferring it from
a WLS number. A transparent corrective analysis is acceptable, but the primary-sample
definition depending on an after-the-fact predicate must be foregrounded, not tucked into
an appendix sentence.

**[MAJOR] 4 — The released Catalog C carries a 9.5σ monopole that is systematics-attributed
but mechanistically unexplained, and the mitigation is buried (Table 4; §4.2; Data
Availability).** f_CW = 0.4974 (−0.265%, −9.47σ) after equivariant TTA; the raw product is
+28.72σ. For a catalog explicitly offered to ℓ=0 parity users, a 9.5σ residual
handedness monopole with three candidate-but-unresolved mechanisms is a first-order
usability caveat. The per-region monopole-correction map and the "must locally
renormalize before any parity statistic" guidance are the right response but appear only
in Data Availability; they belong in the abstract/Results and in the catalog column
documentation.

**[MAJOR] 5 — The only external label validation is overlap-contaminated and only
moderate (§B, Table 14, Table 15).** The GZ1 human-vote comparison (69.91% agreement,
Cohen's κ = 0.40) cannot serve as independent validation because the 6,637 GZ1 training
rows were not anti-joined (no stable training IDs retained), so the benchmark is
"overlap-contaminated." The catalog therefore ships without a clean independent accuracy
figure, and κ = 0.40 is only moderate agreement for a handedness label. The manuscript
should provide (or clearly flag the absence of) a training-disjoint human-label validation
and state the resulting bound on catalog label reliability for downstream users.

**[MINOR] 6 — Confidence outputs are uncalibrated ranking scores (§4.1 calibration
caveat, §B).** p_eq is a monotone ranking score with no ECE/reliability claim; "high
confidence" is a selection threshold, not a per-object correctness probability. This is
disclosed in text but should be stated explicitly in the released catalog schema / column
descriptions so users do not treat the score as a probability.

**[MINOR] 7 — Confusion/transfer resolved only at two declination strata (§B, Table 15).**
The "CW→CCW error asymmetry consistent with zero" conclusion is bounded only at
two-declination-stratum resolution; DES is not separately validated and RA variation
within a stratum is unresolved. Every place this null is cited should carry that
resolution caveat, and the abstract's transfer-function language should reflect it.

**[MINOR] 8 — Proliferation of non-commensurable significance conventions (Tables 2, 6, 7;
§3.1, §4).** The paper juggles moment-z, empirical rank-p, block-bootstrap-z, and
binomial-z, and repeatedly warns they are not comparable across rows. A single
consolidated table mapping each reported z/p to its null, its support, and its
interpretation would materially reduce the risk of a reader over-reading (e.g.) the +6.9
moment-z as a Gaussian detection.

**[MINOR] 9 — Inline artifact filenames/paths in prose (§4.2, §B, Data Availability).**
Long provenance filenames embedded mid-sentence (e.g. `c12_r24conf_local_batch.json`,
`monopole_correction_map_v1_0_262.json`) are hard to use and risk column overflow;
a single machine-readable artifact/provenance index would serve reproducibility better.

**[MINOR] 10 — Abstract's closing sentence is easy to misread.** "The parity-even
morphology observable supports no primordial-parity bound" should be reworded to make
unambiguous that the work places *no constraint* on primordial parity (the galaxy-formation
transfer function is absent), rather than that it disfavors parity violation.

---

**(3) Is the central claim supported?** Yes, narrowly: the strict HC real-space
observed-label dipole is null-consistent (z_mom = +0.635, p = 0.23768) under its stated
estimator, but that single-channel null is not yet shown to be robust against the
coexisting ~7σ WLS/harmonic/monopole channels (no joint covariance), rests on a
post-hoc-defined sample, and is paired with a large unexplained monopole in the released
catalog — so the primary null holds as stated while the paper's broader systematics
attribution remains asserted rather than demonstrated.
