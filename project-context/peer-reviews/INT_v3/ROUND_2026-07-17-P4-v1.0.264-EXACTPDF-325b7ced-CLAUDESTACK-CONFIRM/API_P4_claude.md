# INT v3 Referee Report — P4 (Chirality Catalog + Methods)

- **Model:** claude-opus-4-8 (subagent)
- **Date:** 2026-07-17 PT
- **Paper:** P4 v1.0.264 — "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog"
- **pdf_sha256:** 325b7ced736081a201fb5f1bc9c6283760c1296b5adcb1baf7cb503ce98cb862
- **Venue:** The Astrophysical Journal Supplement Series (APJS-CATALOG-METHODS)
- **Exactness gate:** PASS (on-disk shasum -a 256 == expected)
- **PARSED VERDICT:** MAJOR REVISIONS

---

## Referee prompt (as executed)

"You are an expert referee for The Astrophysical Journal Supplement Series. Review this
Catalog + methods article manuscript under profile APJS-CATALOG-METHODS to the standard of a
real submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR
REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the
specific section/claim and concrete problem. (3) One sentence: is the central claim
supported?"

---

## (1) VERDICT: MAJOR REVISIONS

## (2) ISSUES

**[MAJOR] 1 — The catalog-generating classifier is not exactly reproducible (Sec 2.2, Appendix B, Table 13).**
For a catalog paper the single most important deliverable is that the released catalog can be
regenerated. Here the manuscript states plainly that "the exact historical training
realization is not fully recoverable" and documents three mutually conflicting committed
records: the model-repository audit (26,616 rows / 826 CE non-spirals / 93.6878% val
accuracy), BENCHMARK_REPORT.md (26,626 rows / 846 CE non-spirals / 92.10%), and the model
README (92.10%). No object/split manifest and no random-state record were retained (Table 13:
"Exact object/split manifest — not retained"). The paper is admirably transparent about this,
but transparency does not repair the defect: the primary science-facing product (Catalog C)
was produced by a model whose training data membership, split, and stochastic realization
cannot be reconstructed. ApJS should not publish a catalog whose generating pipeline is
irreproducible without, at minimum, a clearly foregrounded statement in the abstract and a
committed frozen inference environment that reproduces the *labels* bit-for-bit from the
frozen checkpoint (even if the training cannot be replayed).

**[MAJOR] 2 — The sole independent cross-check of the null is overlap-contaminated (Sec 6.1, Sec 4.1 "GZ1 confusion", Tables 15–16, Appendix B).**
The null's only claimed corroboration from a non-machine-learned source is the Galaxy Zoo 1
human-vote dipole (z = −0.54, p = 0.67). But the classifier was trained on 6,637 GZ1
high-confidence CW/CCW rows and "no object-level anti-join against the 6,637 GZ1 training rows"
was retained, so the 69.91% agreement (Cohen's κ = 0.40) is explicitly "descriptive, not an
independent validation metric." The human votes are partly independent of the softmax, but the
*matched inputs* overlap the training set, so the paper's one independence argument is
weakened by its own disclosure. The claim in the abstract/Sec 6.1 that GZ1 "corroborates the
null independently" overstates what an overlap-contaminated cross-match can support; this
should be softened and the retained-overlap fraction quantified, or a genuine held-out GZ1
subset (training objects removed) reported.

**[MAJOR] 3 — A null result with no calibrated sensitivity floor / upper limit (Sec 4.2, Sec 6.2, Tables 1, 10, 11, Fig 8).**
The central result is a null, yet the manuscript repeatedly and explicitly declines to state
what amplitude it could have detected: the finite-injection grids "do not establish a
calibrated physical sensitivity floor"; the pilot rows are "not calibrated coverage or an
upper limit" (Table 1 row vii); the Fisher scale σ(A) ≈ 9.7×10⁻⁴ is "not a calibrated
detection threshold" (Sec 6.2); the injection scores are "descriptive tested-grid evidence"
only. A methods paper whose stated purpose is a null-search pipeline has therefore not
demonstrated that the pipeline can detect a dipole of any stated amplitude at stated coverage.
Without a quantified upper bound the null has limited standalone scientific weight and cannot
be cited as a constraint. At minimum the paper needs a defensible, coverage-calibrated upper
limit on A_dip (or an explicit, prominent statement in the abstract that no upper limit is
claimed and the result must not be read as a parity constraint).

**[MAJOR] 4 — Primary sample definition (unsafe-row quarantine) was fixed post-unblinding (Sec 4.3).**
The manuscript states the raw_flip_qc_unsafe quarantine predicate "was introduced and
finalized during post-review closure after inspection of the earlier unsafe-inclusive result;
it was not preregistered or fixed before unblinding," so the strict rerun "is a transparent
confirmatory analysis, not a blinded confirmatory test." Post-hoc definition of the primary
estimator's sample after seeing the data is a genuine statistical concern even when honestly
disclosed. The effect on the null is shown to be small (z = +0.48 excluded vs +0.52
inclusive), which mitigates the stakes, but the primary-result framing should present the
pre-specified (inclusive) number as the primary and the quarantined number as the robustness
variant — not the reverse — or explicitly justify why the post-hoc sample is the headline.

**[MAJOR] 5 — Presentation: the single load-bearing result is buried under a thicket of mutually non-comparable statistics (Secs 3–4; Tables 2, 4, 5, 6, 7, 8, 9).**
The paper correctly insists that z-values from distinct null families "must not be converted
through a Gaussian z→p map" and are "not directly comparable." The consequence is that the
reader is presented with a large set of large-magnitude, non-comparable z's (+6.923, +7.033,
+7.207, +9.47, +6.48, −7.6, +3.80, +2.931, +3.089, ...) most of which are systematics
diagnostics, while the one primary number (z_mom = +0.635) is easy to lose. For an ApJS
article the organization needs restructuring so that the primary HC real-space null is
unambiguously foregrounded (ideally its own short results subsection and a single summary
sentence), with the diagnostic z-zoo clearly demoted to appendices. As written, the
signal-to-noise of the *exposition* is low and invites misquotation of a diagnostic z as "the
result."

**[MAJOR] 6 — The released science catalog still carries a −9.47σ CW-fraction monopole; TTA's causal role is not established (Table 4, Sec 4.2, Fig 2/7 captions, Data Availability).**
After equivariant averaging the released Catalog C has f_CW − 0.5 = −0.265% (−9.47σ, Table 4).
This is a highly significant residual monopole in the delivered product; users doing any ℓ=0
parity work must apply the supplied per-region correction map or be misled. Compounding this,
the paper repeatedly concedes that raw (A) and equivariant (C) products "came from different
inference passes, memberships, and quoted null conventions," so the comparison "does not by
itself isolate TTA as the unique causal explanation" for the asymmetry suppression. Since the
methods contribution is precisely that equivariant post-processing mitigates directional bias,
the causal claim should either be supported by a matched-membership A-vs-C comparison on
identical objects, or the language downgraded throughout to a purely associational statement,
and the −9.47σ residual flagged as a first-order fitness-for-use caveat in the abstract.

**[MAJOR] 7 — Fitness-for-use of the full 8.47M labels vs the HC science sample is under-characterized (Sec 4.1, Table 15).**
The catalog releases labels for all 8,474,531 objects, but the chirality reliability of the
full sample is marginal: on the GZ1 1″ cross-match (Table 15), GZ1-CW spirals are labeled CCW
in ~33% of cases and GZ1-CCW labeled CW in ~28% (off the confidence cut). The clean ~4%
CW↔CCW error appears only on the science cut (p_eq > 0.6, Table 16). A catalog user pulling
the full-sample labels inherits ~1/3 chirality error. The paper should carry a prominent,
early fitness-for-use table/paragraph stating the per-confidence-bin chirality error so the
8.47M product is not mis-used at low confidence.

**[MINOR] 8 — No minted Zenodo DOI or commit hashes at review time (Data Availability).**
"The DOI and commit hashes will be inserted here in place of this sentence at submission
time." An ApJS catalog paper requires a resolvable DOI-backed archival snapshot and frozen
git commit hash of the analysis code before acceptance; these must be present (not promised)
for the referee to verify the availability claims.

**[MINOR] 9 — 35 catalog rows unexplained (Sec 4.1).**
The catalog is 8,474,531 rows, 35 fewer than the 8,474,566-row training split, and "the
historical inference runner retained neither a per-object failure ledger nor reason codes, so
the identities of those absent rows and their exact failure reasons are unavailable." Small,
but another provenance gap in a catalog deliverable; list the missing dr8_ids even if the
reason is unknown.

**[MINOR] 10 — Unresolved D₄ rotational-equivariance instability (Appendix B).**
The classifier is only 2-fold flip-equivariant; the D₄-TTA holdout finds per-galaxy argmax
labels flip in 21.4% of borderline cases between Z₂ and D₄, and the CW-fraction shift even
reverses sign (−1.35% at N=1558 vs +2.11% at N=1988). The paper concedes this "does not
exclude a D₄-dependent systematic." A ~21% borderline instability is relevant to label
reliability and should be propagated into a per-object confidence caveat.

**[MINOR] 11 — False precision on a null (Table 5).**
z_mom is quoted as +0.6346509 (7 significant figures) and p as 0.23768 for a result
consistent with zero. Report to a precision commensurate with the null (e.g. z = +0.63,
p = 0.24).

**[MINOR] 12 — Abstract phrasing and hedging.**
"The parity-even morphology observable supports no primordial-parity bound" is syntactically
ambiguous (reads either as "provides no bound" or "supports a no-parity bound"); rephrase to
state explicitly that the ℓ=1 morphology dipole is parity-even and therefore cannot constrain
primordial parity violation. Relatedly the abstract's closing list of five items that "remain
open" (spatial transfer calibration, joint likelihood, matched-footprint estimator,
systematics-metadata sidecar, DOI archive) reads as heavily hedged; consider consolidating.

## (3) Is the central claim supported?

Yes — the specific central claim, that the observed-label chirality dipole on the
quality-controlled HC sample is statistically consistent with zero (z_mom = +0.635, one-sided
rank p = 0.238), is supported by the presented data and is not over-interpreted, but its
scientific weight is materially limited by the absence of any calibrated upper limit and by
the catalog-generation reproducibility and independence gaps enumerated above.
