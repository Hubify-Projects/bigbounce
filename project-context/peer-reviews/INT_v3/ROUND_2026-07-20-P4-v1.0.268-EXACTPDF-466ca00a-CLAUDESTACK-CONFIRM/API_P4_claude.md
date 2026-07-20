# INT v3 Referee Report — P4 (Chirality Catalog + Methods)

- **Model:** claude-opus-4-8 (subagent)
- **Date:** 2026-07-20 PT
- **Paper:** P4 v1.0.268 (An Observed-Label Chirality-Dipole Null in 890,069 QC High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog)
- **pdf_sha256:** 466ca00a63b2219293acd5de1528be713fb28dfd289a20aa8f731f8557e0298f
- **Venue:** ApJS (The Astrophysical Journal Supplement Series)
- **Profile:** APJS-CATALOG-METHODS
- **PARSED VERDICT:** MAJOR REVISIONS

---

## RAW VERBATIM REPORT

You are an expert referee for The Astrophysical Journal Supplement Series. I have reviewed this Catalog + methods manuscript under profile APJS-CATALOG-METHODS to the standard of a real submission.

### (1) VERDICT: MAJOR REVISIONS

### (2) ISSUES

**[MAJOR] 1 — Released Catalog C labels have an unreproducible generation provenance (Sec. 2; Table 13).**
The primary deliverable of an ApJS catalog is the labels themselves. Here the released Catalog C chirality labels were produced by a classifier whose exact historical training realization is, by the authors' own statement, "not fully recoverable": three conflicting committed records exist (826 vs. 846 vs. 819 CE non-spirals; 92.10% vs. 93.6878% validation accuracy; no retained object/split manifest or random-state receipt). The from-scratch, manifest-retained retrain that the authors add regenerates only the GZ1-core component (`ce_resnet_present=false`) and explicitly does *not* re-provision the ~67.5% CE-derived pool, so the released labels remain unreproducible. Disclosing the gap thoroughly (which the authors do, admirably) does not close it. For an ApJS catalog release the authors must either (a) demonstrate a pipeline that regenerates the *released* labels to within a stated tolerance, or (b) far more sharply quantify and bound the fraction of released labels whose values could differ under the conflicting historical accounts, so downstream users know the label-level reproducibility floor.

**[MAJOR] 2 — Composition-faithful CE-included retrain collapses to chance on chirality (Sec. 2; Table 13, val acc 0.5617).**
The authors report that a composition-faithful retrain of the identical 26,609-object realization reaches only 0.5617 three-class validation accuracy and is "at chance on chirality," with per-source held-out GZ1 CW/CCW agreement 0.517. This is presented as an "honest negative" that "strengthens the disclosure," but it raises a first-order scientific question the paper does not fully resolve: to what extent is the released Catalog C chirality signal driven by the GZ1 training-label distribution rather than by robust, transferable image morphology? If a faithful re-ingestion of the same composition cannot learn chirality above chance, a skeptical reader must worry that the released chirality assignments encode a training prior as much as a physical handedness. The authors need to demonstrate more directly — e.g., via a clean, training-disjoint, image-only test on the *released* classifier (not only the regenerable GZ1-core checkpoint) — that Catalog C chirality reflects genuine morphological handedness. The κ=0.9733 training-disjoint result (Sec. B) is on a *different* checkpoint and a high-confidence clean subset and does not speak to the released classifier.

**[MAJOR] 3 — Presentation/legibility: the load-bearing result is buried under non-commensurable significance conventions (Secs. 3.1, 4; Tables 1–3, 6–9).**
The manuscript reports significance in at least four mutually non-comparable conventions (moment-z, empirical rank-p, block-bootstrap z, MASTER moment-ratio z) and displays numerous large values (+6.923, +7.033, +6.983, −7.6, −9.47σ, +6.48σ, +3.29σ) each footnoted as "not a Gaussian significance / not directly comparable." Tables 1–3 are a genuine effort to disambiguate, but the net effect is that a reader cannot easily separate the single load-bearing null (z_mom=+0.635, p=0.23768) from a dense thicket of diagnostics that individually look like >5σ detections. For an ApJS methods paper this needs substantial tightening: state the one primary result and its convention plainly and early; demote the diagnostic z-values to a clearly-labeled appendix; and provide (and use consistently) a single crosswalk that tells the reader how to read each convention. As written, the paper is very hard to referee and will be harder for a typical catalog user to use correctly.

**[MAJOR] 4 — "Systematics" functions as an under-modeled catch-all for multiple >5σ residuals (Secs. 4.2, 4.4; Tables 6–8).**
The +9.5σ global monopole (CW-fraction offset) and +6.48σ pre-MASTER ℓ=1 pseudo-power, plus elevated ℓ=1–3 harmonic power (z up to +7.2), are all attributed to systematics. The classifier-injection forward model is a real strength — it excludes classifier confusion (0.0% of the observed monopole) and sign-excludes the GZ1 training-prior candidate. But the paper explicitly leaves the true-sky-vs-DESI-imaging origin *unresolved*, and no forward model actually reproduces the observed monopole/harmonic amplitudes from a named systematic. Repeatedly labeling >5σ deviations "systematics-attributed" without a model that predicts their magnitude weakens the claim that the primary null is protected from the same systematics. The authors should either exhibit a systematics model that quantitatively reproduces the monopole/low-ℓ amplitudes, or explicitly propagate the unmodeled-systematic risk into a stated uncertainty on the primary null.

**[MINOR] 5 — Edge-on contamination in the spiral catalog (Sec. 6.2 / App. E; Table not numbered).**
15.80% (505,889 of 3,201,160) classified spirals are edge-on (b/a<0.30), where projected arm-winding chirality is ill-defined. The edge-on-isolated tie-break test is null-consistent but "does not exclude every spatially varying hard-label bias." A catalog user needs a clear per-object purity flag and an explicit recommendation for chirality studies (e.g., a suggested b/a cut) rather than a footnote.

**[MINOR] 6 — Modest released-classifier vs. human agreement should not be conflated with the clean-subset value (Table 15; Sec. B).**
The released classifier's three-class agreement with GZ1 is Cohen's κ=0.40 (69.91% chirality agreement) on the overlap. The much stronger κ=0.9733 is from a different checkpoint on a clean, high-confidence, training-disjoint subset. The abstract/body should make unmistakable that the *released* catalog's descriptive human-agreement figure is the κ=0.40 / 69.91% number, and that κ=0.9733 is not the released product's reliability.

**[MINOR] 7 — Bias-hardening thresholds are too loose for the sub-percent science regime (Table 14).**
T8 "CW/CCW balance 50±10%" is reported as passing at 49.7%, yet the scientifically relevant deviation (f_CW≈0.4974, the −0.53%/−9.5σ monopole) lives at the 0.5% level. A ±10% acceptance window cannot certify anything at the scale at which the paper's science operates; several thresholds should be re-justified against the sub-percent bias budget or explicitly described as coarse sanity checks only.

**[MINOR] 8 — Thin literature context for a parity/isotropy methods paper (18 references).**
The manuscript invokes primordial parity violation, isotropy-breaking axial-vector sectors, Chern–Simons gravity, and cosmic birefringence, but cites essentially only the Shamir series, Iye, Tadaki, the CE-ResNet paper, and tooling/data references. Broader context — other spin/parity-alignment searches, imaging-systematics studies on SDSS/DESI, and prior catalog-classifier reliability work — would substantially strengthen the framing and the "comparison with previous work" section.

**[MINOR] 9 — Catalog score calibration is entirely deferred to the user (Secs. 4.1, 6.4).**
p_eq is stated to be an uncalibrated ranking score with no ECE claim, and probabilistic users are told to apply their own temperature/Platt scaling. This is honest, but the catalog would be materially more useful with at least one calibration reference curve provided on a clean held-out set, even if flagged as approximate.

### (3) One sentence — is the central claim supported?
Yes: the primary claim that the observed-label chirality dipole on the quality-controlled HC sample is consistent with zero (z_mom=+0.635, p=0.23768) with a coverage-calibrated ~0.98% observed-label sensitivity ceiling is statistically well-supported and carefully bounded as a sensitivity floor rather than a physical parity limit — but the catalog's value as a chirality *product* is undercut by an unreproducible label-generation provenance and a composition-faithful retrain that cannot recover chirality above chance, both of which must be more sharply addressed before publication.
