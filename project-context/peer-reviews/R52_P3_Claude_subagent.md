# Referee Report — R52 (Claude/Opus leg)

**Recommendation: MINOR REVISIONS**

Paper: P3 v3.1.112 — "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog
of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from
37.3 Million Sources and Map Patches" (Golden).
Reviewed: full compiled PDF, 30 pages, native render.

## Summary verdict

This is a sound, exhaustively-caveated catalog/data-release paper. I read it
adversarially for an unsupported load-bearing claim, a missing critical control,
or non-reproducibility from committed artifacts. I found none that overturns a
stated result. Every headline number is internally consistent and traceable
(I re-derived the count bookkeeping, the f_NL Fisher arithmetic, the NANOGrav
σ-shifts, the Cramér's V, and the fixed-α grid — all check). The paper
systematically scopes its weak tiers as exploratory and resists the standard
over-claims (SIMBAD-unmatched ≠ novelty; noisy-α improvement ≠ detection;
Bayes factor decisive only vs idealized reference). The remaining items are
analyses a referee would *request added*, not corrections to wrong claims —
hence MINOR REVISIONS rather than MAJOR.

---

## 1. BLOCKERS

None. No claim is contradicted by the committed artifacts, the rendered math is
correct where legible, and the catalog-grade headline (269,317 / 269,117
point-source) and full headline (378,280 = 378,080 + 200) reconcile arithmetically
(388,493 native − 10,213 dedup = 378,280; verified against Table I footnotes).

---

## 2. MAJORS

**M1 — DESI injection-recovery was never executed for the anchor survey (§IID
step 5; §VI D(ii); Fig. 10).** DESI contributes the plurality of the catalog
(195,829 objects, ~52%) and is the scientific core, yet its only validation is
ranking stability (5-fold Jaccard J̄=0.862 and OOD Jaccard 0.732). Injection-
recovery — which tests whether the detector recovers *planted* signal classes,
i.e. sensitivity/completeness — was run for SDSS, LAMOST, eROSITA, Gaia, Planck,
NEOWISE but **not** DESI ("DESI injection-recovery was not executed; its catalog
robustness rests on the two Jaccard metrics"). The infrastructure plainly exists
(it was applied to the six sibling tiers). For a discovery-catalog paper the
sensitivity of the anchor survey is the single most natural validation to
include. *This supports no false claim* (the catalog is candidate-framed and
DESI carries two genuine stability gates), which is why it does not block — but a
DESI continuum-dip + emission-line injection-recovery run on the native
checkpoint, reported on the same axis as Fig. 10, would close the most obvious
gap. **Fix:** execute and tabulate DESI injection-recovery, or state explicitly
in §VID(ii) why DESI sensitivity is intentionally left unquantified while six
other tiers are characterized.

---

## 3. MINORS

**m1 — Full-catalog genuine-novelty is characterized for 0.26% of the catalog
(Abstract; §IV A).** The 17.8% genuine-novelty fraction (178/1000, Wilson 68%
±1.2%) is measured only on the DESI top-1,000 score stratum; the paper correctly
states "no bound exists on the full-catalog extrapolation, which is empirically
untested." This is honest and not an overclaim, but the discovery-engine framing
rests on this single stratum. **Fix:** add even a coarse novelty estimate at a
second, lower score stratum (e.g. ranks 5,000–6,000) to bound the trend, or
state the monotonicity assumption explicitly.

**m2 — Fig. 5 / §III H: the headline NEOWISE anomaly is plausibly instrumental.**
The top NEOWISE source (score 11.5, (α,δ)=(180.59°,0.56°)) is described as "a
bright, saturated source with diffraction spikes." Saturation + diffraction
spikes is a classic photometric-artifact signature; the paper lists
circumstellar-dust/AGN/red-QSO hypotheses but should foreground the
saturation/artifact possibility in the caption, since presenting a likely
saturation artifact as the exemplar infrared anomaly is a candidate-quality
optics issue.

**m3 — §IV D Planck×ACT null is self-disclaimed and adds little.** The null
cross-correlation uses the formally quarantined ACT cross-transfer set and is
then declared "geometry-driven... non-diagnostic" and carrying "essentially no
discriminating power." Presenting a result you immediately neutralize risks
reader confusion. **Fix:** compress to a one-sentence pointer or move entirely to
the ACT appendix (F), where the quarantine rationale already lives.

**m4 — Non-reproducible tiers should surface earlier.** Two tiers are flagged
deep in the text: eROSITA's production threshold 0.259 "could not be reconciled
with any tested score axis" (scores membership-only, §III E / Table IV), and the
Gaia 20-feature preprocessing script "was not recovered from pod backups"
(lineage-inferred, §II B). Both are handled with exemplary transparency and
affect only ~798/378,280 objects (0.2%), both excluded from / down-tiered in the
catalog-grade recommendation. **Fix:** add one clause to the Data-availability
paragraph stating that eROSITA scores are non-reproducible (membership-only) and
the Gaia tier is "best-available reproducible," so a downstream user sees it
without reading §III E.

**m5 — Two improvement figures (9.4% vs 6.1%) use different approximations.** The
empirical primary (§V, α_jk=0.19, quadratic Fisher form 1/σ²=F_0+cα²) gives the
central 9.4% (de-biased to 0); the fixed-prior reference (Appendix C/Table VIII,
α=0.15, *linear* scaling of Δσ/σ) gives 6.1%. Both are internally correct and
labeled, but a reader may conflate them. **Fix:** one cross-reference line noting
the appendix uses linear scaling and is superseded by the empirical de-biased
result.

**m6 — Table V (residual caveat ledger) is excellent but buried.** A one-line
pointer to it from the abstract or conclusions would help readers locate the
honest accounting.

---

## 4. Strengths

- **Provenance discipline is exceptional.** Every count is traceable to a named
  committed artifact (recovered_pod_scripts/, ext3_*.json, r24conf_*.json,
  rescore_summary.json), SHA-256 hashes are promised in DATA_RELEASE_MANIFEST.md,
  and the four DESI rate denominators are explicitly reconciled (Table II) rather
  than silently conflated — this directly defuses the most common catalog-paper
  failure mode (rate confusion).

- **Honest separation of database-coverage from discovery.** The paper refuses to
  quote the 58.8% SIMBAD-unmatched fraction as novelty, instead reporting the
  17.8% CDS-X-Match-against-18-catalogs genuine-novelty fraction and stating the
  SIMBAD figure "substantially overstates true catalog novelty." Fig. 6 makes the
  distinction graphically. This is the correct, conservative framing.

- **The Path-C native-retrain methodology is a real contribution with a
  well-supported lesson.** The LAMOST 98%-blue-excess training-bias result —
  quantified by a 21.5× anomaly-rate compression after native retraining
  (44,075 → 2,054) — is a genuine, transferable methodological finding about
  cross-transfer autoencoder anomaly detection, not a cosmetic caveat.

- **Cosmology sections are presented as no-detections with correct statistics.**
  The f_NL forecast correctly identifies the α̂-squaring noise bias
  (max(0, α²−σ_α²)=0 → returns single-tracer 8.98) and reports σ=8.14 with the
  [3.92, 8.98] envelope as an envelope, not a credible interval; the NANOGrav
  γ=2.567±0.382 result is correctly flagged as decisive only against the
  idealized circular-orbit SMBHB reference, with the environmental-flattening
  caveat. No detection is claimed where none exists.

- **Scale and quarantine handling.** The 37.3M-source / 8-archive sweep is
  credibly the largest reported, and the ACT DR6 quarantine (Appendix F: fails
  both gate criteria, contributes zero objects, retained only as a
  lessons-learned record) is the right call, executed cleanly.

---

*Reviewed by the Claude/Opus external-referee leg, internal round R52,
2026-06-26. Calibration: June-2026 arXiv valid; deliberate placeholders /
scoping labels / transparency notes not penalized; PDF-extraction math artifacts
ignored.*
