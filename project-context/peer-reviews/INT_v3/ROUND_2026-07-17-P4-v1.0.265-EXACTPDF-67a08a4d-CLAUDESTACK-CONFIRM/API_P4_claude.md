# INT v3 — Independent Referee Report (Claude subagent leg)

- **Model:** claude-opus-4-8 (subagent)
- **Date:** 2026-07-17 (PT)
- **Paper:** P4 — "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog" — v1.0.265
- **pdf_sha256:** 67a08a4d3255a6fab0eadacd96580491ac20ae77abda50c55847506f49c16fc5
- **Venue:** The Astrophysical Journal Supplement Series (ApJS)
- **Profile:** APJS-CATALOG-METHODS
- **PARSED VERDICT:** MAJOR REVISIONS

---

## RAW VERBATIM REPORT

**(1) VERDICT: MAJOR REVISIONS**

**(2) ISSUES:**

**1. [MAJOR] Reproducibility of the primary data product (Sec. 2.2; Appendix B; Table 13).** For an ApJS catalog paper the released labels are the deliverable, yet the manuscript states the "exact historical training realization is not fully recoverable." Table 13 documents conflicting committed records for the very run that produced the catalog: 26,616 vs 26,626 training rows, 826 vs 846 CE-ResNet-selected non-spirals, a 93.6878% audit accuracy vs a 92.10% README accuracy, and no retained object/split manifest or random-state receipt. The output is content-addressed and checksummed, but it cannot be regenerated. A supplement/catalog paper should either (a) supply a re-training run with fully retained split IDs, seeds, and object manifest that reproduces the released labels, or (b) foreground far more prominently that the released 8.47M labels are a frozen, non-replayable artifact and quantify the downstream trust cost. As written, the candor is commendable but the reproducibility standard for a released ApJS data product is not met.

**2. [MAJOR] A 9.47σ handedness monopole lives in the released catalog labels (Sec. 4.2; Table 4; Fig. 3).** The global CW fraction of the science-facing Catalog C deviates from 0.5 at −9.47σ (raw Catalog A at +28.7σ; a ~0.79% classifier CW excess). This is a very large, statistically dominant label asymmetry in a chirality catalog, attributed to classifier/imaging/training systematics. Two problems must be closed more rigorously: (i) demonstrate, not assert, that a monopole of this size does not leak into the ℓ=1 (dipole) and low-ℓ channels that carry the primary null and the harmonic diagnostics — the joint-covariance argument (Table 9, ρ≈−0.037) is a bootstrap-correlation statement, not a proof of zero mean leakage; and (ii) quantify the fitness of the released labels for any third-party chirality science given a ~0.26%–0.79% handedness bias of unresolved origin. The monopole-correction map is a useful mitigation but is offered as a convenience product that "changes no science number," which does not resolve the underlying label-bias concern.

**3. [MAJOR] Classifier–human agreement is only moderate and overlap-contaminated (Sec. 4.1; Tables 15–16).** The entire scientific value of the catalog rests on label quality, yet agreement with Galaxy Zoo 1 human chirality labels is 69.91% (Cohen's κ=0.40) — moderate at best — and the comparison is explicitly overlap-contaminated because the 6,637 GZ1 training rows were not removed from the agreement calculation, and no object-level training anti-join was retained. A training-disjoint, independent human-label validation (or a matched external catalog comparison, e.g. a matched-footprint Ganalyzer run, which the paper itself repeatedly flags as necessary but not performed) is required to establish that the released labels are reliable enough for the advertised use.

**4. [MAJOR] Presentation density defeats the catalog+methods purpose (whole manuscript).** The paper carries an unusually large number of supports (HC-RI, FS-C, MASTER-AGF, MASTER-ALL-GALAXY-FOOTPRINT, latitude-cut variants), three non-commensurable significance conventions, and roughly a dozen diagnostics repeatedly labeled "historical," "provenance-only," or "out of scope" (Tables 8, 12, 13, 17; Sec. 4.4–4.5; Appendices B–E). The reader must continuously separate load-bearing numbers from retained provenance to know what the paper actually claims. For an ApJS catalog+methods article the core result (the HC observed-label null) and the catalog characterization should be cleanly and briefly stated, with the extensive systematics forensics condensed and relegated to clearly-marked appendices/supplementary. Substantial restructuring is warranted before acceptance.

**5. [MINOR] Proliferation of non-comparable z conventions (Sec. 3.1; Sec. 4).** Three distinct significance conventions are defined and the text repeatedly warns that the many z values are moment-ratios, not Gaussian tail probabilities, and "must not be converted through a Gaussian z→p map." This is careful, but presenting so many z-like numbers of different provenance invites exactly the misreading being warned against. Consider a single summary table binding each estimator to its null family and reporting a uniform empirical rank-p, with the moment-ratio z's demoted.

**6. [MINOR] Catalog A vs Catalog C comparison confound (Fig. 7; Sec. 4.2).** The raw-vs-equivariant sky-map comparison is presented as evidence that equivariant post-processing mitigates directional bias, while the caption concedes the two products "have different inference-pass provenance, memberships, and quoted null conventions, [so] the comparison does not by itself isolate TTA." Given this confound the didactic value of the figure should be clarified or the comparison controlled.

**7. [MINOR] Deferred archival DOI (Sec. 7; Data Availability).** The Zenodo DOI and pinned commit hashes are marked "inserted here in place of this sentence at submission time." ApJS review normally expects a resolvable archival DOI for the data product at submission; the placeholder should be resolved so the referee can verify the deposited snapshot.

**8. [MINOR] Retained rank-deficient fits (Tables 8, 17).** Table 17's 9-template WLS fit has condition number 4.5×10^16 with collinear imaging-leg templates whose coefficients are "not meaningful," retained "for provenance." Carrying a numerically singular fit in the main body, even as provenance, adds noise; move fully to supplementary or drop.

**9. [MINOR] Figure legibility at print size.** Verify the Mollweide asymmetry map (Fig. 4), the log-scale confidence distribution (Fig. 6), and the dense multi-panel diagnostics render with legible colorbars, tick labels, and per-panel captions at journal column width.

**10. [MINOR] AI-pipeline provenance of quantitative claims (Acknowledgments).** The AI-assisted methodology disclosure is welcome. Given the volume of machine-generated diagnostics, itemize which released quantitative claims were independently human-verified vs pipeline-generated, so a referee can trace the load-bearing numbers.

**(3) Is the central claim supported?** Yes, narrowly: the observed-label chirality-dipole null on the declared QC HC sample (z_mom=+0.635, one-sided rank p=0.23768) supports "consistent with zero," and the paper is scrupulous in not overclaiming a physical parity bound (A_95^obs≈0.98% is explicitly an observed-label sensitivity floor, not a physical limit) — but the released catalog's non-reproducible generation, a 9.5σ label monopole, and only-moderate human agreement materially temper the catalog's stated utility and must be addressed before publication.
