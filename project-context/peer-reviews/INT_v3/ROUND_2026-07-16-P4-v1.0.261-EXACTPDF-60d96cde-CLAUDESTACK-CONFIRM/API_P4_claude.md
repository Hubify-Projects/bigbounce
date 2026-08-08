# INT leg — Claude (Anthropic subscription, Claude Code subagent)
- model: claude-opus-4-8 (Opus-tier subagent)
- date: 2026-07-16 (PT)
- paper: P4 v1.0.261
- pdf_sha256: 60d96cde47cee1475d58273a4e14fc41046abebf03d89fd50cb03bf10f6f0a64
- venue: The Astrophysical Journal Supplement Series (APJS-CATALOG-METHODS, Catalog + methods article)
- PARSED VERDICT: MAJOR REVISIONS

---

Referee report — The Astrophysical Journal Supplement Series
Profile: APJS-CATALOG-METHODS
Manuscript: "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled
High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog" (H. Golden)

## (1) VERDICT: MAJOR REVISIONS

## (2) ISSUES

[MAJOR] 1 — Core data product (labels) is not reproducible and the internal
training records conflict (§2.2, Table 12).
The catalog's primary deliverable is the CW/CCW/NS labels, yet §2.2 states "The
exact historical training realization is not fully recoverable," no object/split
manifest was retained, and the committed repository records disagree with each
other: 26,616 vs 26,626 total rows, 826 vs 846 CE non-spirals, 21,293/5,323 split
vs benchmark totals, and 93.6878% (model-repo audit) vs 92.10% (README) validation
accuracy (Table 12). For an ApJS catalog paper the provenance of the primary
product cannot rest on mutually inconsistent internal records. The frozen,
checksummed model checkpoint and the frozen catalog make *inference* reproducible,
but the label-generating pipeline is not, and a repository whose own records
contradict one another needs reconciliation, not merely a "conflict disclosure"
table. At minimum: reconcile the conflicting counts to a single authoritative
manifest, or re-train with a retained seed/split/object manifest.

[MAJOR] 2 — No overlap-free, independent characterization of label reliability
(§4.4, §6.1, Tables 14–15).
The only external validation is against Galaxy Zoo 1 (Table 14, N=240,919), but it
is explicitly overlap-contaminated: the 6,637 GZ1 rows used in training cannot be
removed because object IDs were not retained, so the reported 69.91% three-class /
CW/CCW agreement (κ=0.40) and the per-class precision/recall cannot be read as
independent purity or completeness. A chirality-label catalog's central usability
claim is the reliability of its labels; the manuscript currently provides no clean,
training-disjoint purity/completeness measurement. Table 15's declination-stratified
confusion is likewise built on the same overlap-contaminated GZ1 match and does not
close this. The paper must deliver an independent (training-disjoint) label-quality
assessment before catalog users can trust the labels.

[MAJOR] 3 — The scientific null is estimator-conditional and the systematics story
is not quantitatively closed (§4.1–4.4, §5, Tables 1–2, 6–7).
The single primary result (z_mom = +0.635, one-sided p = 0.23768) holds only under
one estimator+null (fixed-occupancy label randomization on the QC HC real-space
dipole). Nearly every other estimator the paper itself runs is large and is labeled
"systematics": WLS template z ≈ −7.6; binary/apodized FS-C MASTER ℓ=1 z_mom =
+6.923/+7.033; monopole-only null +6.983/+7.207; multipole vector +6.923, +2.931,
+3.089, −0.317, +1.606 for ℓ=1–5; hemisphere 3.05σ post-LEE; and the released
Catalog C class-fraction deviation from 0.5 at −9.47σ (raw Catalog A at +28.72σ).
The paper repeatedly states that the joint covariance needed to separate systematics
from signal across these estimators "remains open." As written, the null is a
property of one privileged estimator rather than a demonstrated physical null. The
authors must either (a) compute the joint real-space/harmonic/nuisance covariance or
a matched-footprint independent-estimator comparison that actually closes the
systematics interpretation, or (b) present a rigorous, quantitative justification for
why the fixed-occupancy QC HC estimator is uniquely privileged over the others.
Asserting privilege by declaration (§3.2 "Declared Analysis Hierarchy") is not
sufficient for a methods paper at this bar.

[MAJOR] 4 — The released catalog carries an uncorrected >9σ systematic floor in its
class fractions, delivered as a user responsibility rather than a product (§4.1–4.2,
Fig. 3, Table 4).
Catalog C — the science-facing released product — has a documented f_CW − 0.5 =
−0.265% deviation (−9.47σ) plus ~0.5% per-slab and up to ~0.56% per-band scatter,
which the paper says users "must" locally monopole-renormalize before any ℓ=0 parity
search. A catalog whose released spiral class fractions carry a known >9σ artifact
should ship the correction/characterization as part of the data product (e.g. a
per-region CW-fraction correction map with an uncertainty), not defer it to the user
and to "Open Follow-up." This is central to the catalog's fitness for its stated
purpose (parity/isotropy searches).

[MINOR] 5 — Post-hoc, non-preregistered primary sample-defining cut (§4.3, Table 3).
The raw_flip_qc_unsafe quarantine that defines the primary 890,069-row sample was
"introduced and finalized during post-review closure after inspection of the earlier
unsafe-inclusive result... not preregistered" (a "transparent corrective action, not
a blinded confirmatory test"). The null conclusion is robust to it (z: +0.48
unsafe-inclusive → +0.52 baseline), but a post-hoc cut that defines the primary
estimator's sample should be foregrounded in §4.1/Abstract and both pre- and
post-cut primary numbers reported side by side, not relegated.

[MINOR] 6 — Spurious numerical precision inconsistent with the underlying
uncertainty (Tables 4–5). z_mom = +0.6346509 (7 sig figs, Table 5), p = 0.23768
from an integer rank (2376+1)/(10000+1), and f_CW to six decimals (Table 4) overstate
precision given the 10^4-draw null and the acknowledged systematic budget. Quote
values at a precision consistent with the null resolution and stated systematics.

[MINOR] 7 — Moment-ratio "z"/σ notation invites detection misreading (§3.1, §4,
Tables 6–7). The manuscript correctly and repeatedly warns that the MASTER/monopole
"z_mom" and the reported σ are moment ratios, "not Gaussian tail significances," yet
still tabulates +6.9σ/+7.0σ/−9.47σ throughout. A distinct symbol (or explicit
non-σ units) for moment ratios versus rank-based/Gaussian significances would remove
a real risk that readers cite these as detections.

[MINOR] 8 — Persistent DOI archive not yet secured (Abstract, §7). A DOI-backed
paper/source archive is described as "a separate submission gate" that "remains open."
ApJS catalog papers normally require the catalog in a citable persistent archive
(e.g. Zenodo DOI) at acceptance; the immutable HuggingFace dataset revision is good
provenance but a DOI should be in place, not deferred.

[MINOR] 9 — No calibration statement for the released scores (§4.1, §6.1). The p_eq
values are explicitly uncalibrated ranking scores, no same-object reliability artifact
was retained, and no ECE/reliability curve is provided. Even an approximate
calibration (or reliability curve) on a clean, training-disjoint subset would
substantially improve downstream usability of the released confidences.

## (3) Is the central claim supported?
The narrow central claim — that the observed-label chirality dipole is consistent
with zero within the declared quality-controlled HC real-space estimator — is
internally supported and unusually honestly caveated, but its robustness is
undercut because nearly every alternative estimator the paper runs yields high
significance attributed to systematics without a closed joint-covariance analysis,
so the reported null is estimator-conditional rather than a demonstrated physical
null.
