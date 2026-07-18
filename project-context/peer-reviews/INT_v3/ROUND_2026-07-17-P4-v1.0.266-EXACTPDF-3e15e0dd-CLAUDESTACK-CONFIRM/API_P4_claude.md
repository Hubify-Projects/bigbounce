# Independent Referee Report — P4 (Chirality Catalog + Methods)

- **Model:** claude-opus-4-8 (subagent, independent referee leg)
- **Date:** 2026-07-17 (PT)
- **Paper:** P4 — "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog"
- **Version:** v1.0.266
- **PDF SHA-256:** `3e15e0dd6200855a3866b13b010836b380ac72ae5e5ea1d4f3a5600e9e674a6e`
- **Venue:** The Astrophysical Journal Supplement Series (ApJS)
- **Referee profile:** APJS-CATALOG-METHODS
- **Exactness gate:** PASSED (on-disk SHA-256 == required digest)

**PARSED VERDICT: MAJOR REVISIONS**

---

## Referee Review (verbatim)

You are an expert referee for The Astrophysical Journal Supplement Series. The manuscript
was reviewed in full (29 pages, all tables/figures/appendices) under profile
APJS-CATALOG-METHODS to the standard of a real submission.

### (1) VERDICT: MAJOR REVISIONS

### (2) ISSUES

**[MAJOR] 1 — The released catalog (Catalog C), the paper's principal ApJS deliverable, is not reproducible, and the committed provenance records conflict.**
Section 2.2 and Appendix B state the "exact historical training realization is not fully
recoverable"; no retained object/split manifest, random-state record, or run receipt ties the
released labels to the historical checkpoint. Worse, two committed records that are supposed to
describe the *same* production run disagree: the production-script/model-audit account gives
26,616 rows / 826 CE-selected non-spirals / 93.6878% validation accuracy, while the committed
`BENCHMARK_REPORT.md` gives 26,626 rows / 846 non-spirals and the HF README reports 92.10%
(Table 13). The paper explicitly cannot resolve the 826-vs-846 conflict. For a catalog/methods
venue whose core product is the released label set, an irreproducible catalog with unresolved
internal provenance inconsistencies is a substantive concern, not merely a documentation gap. The
from-scratch manifest-retained retrain (κ = 0.9733) regenerates only the GZ1-core component
(`ce_resnet_present = false`, ~67.5% of the historical composition absent) and, by the authors'
own statement, "does not re-provision the CE-ResNet component, resolve the composition conflict,
or alter the released catalog labels." The manuscript must either (a) reconstruct a byte-exact
regeneration path for the released labels, or (b) if that is genuinely impossible, foreground this
limitation in the abstract and Section 1 (currently it surfaces only in §2.2/App. B) and justify
why an irreproducible label set meets ApJS's data-release reproducibility expectations.

**[MAJOR] 2 — The primary science sample was defined post-hoc, after inspection of the unblinded result.**
Section 4.1 (and §3.2) discloses that "the unsafe-row quarantine predicate was introduced and
finalized during post-review closure after inspection of the earlier unsafe-inclusive result; it
was not preregistered or fixed before unblinding." The single PRIMARY scientific result
(N_selected = 890,069; z_mom = +0.635; p = 0.23768) is therefore a corrective, not a blinded
confirmatory, analysis. The authors argue the impact on the dipole is small (z = +0.48 excluded
vs. +0.52 baseline), which is reassuring for a null, but the post-hoc construction of the primary
selection after seeing results is a methodological red flag that a rigorous reader must be able to
evaluate. This disclosure is currently buried mid-Results; it belongs in the abstract-level framing
and warrants an explicit statement that the *identical* qualitative conclusion (null) holds under
the pre-quarantine selection, so the reader can confirm the choice does not manufacture the null.

**[MAJOR] 3 — The headline A_95 ≈ 0.98% "sensitivity upper limit" has narrow interpretive value and its scope should be stated where the number first appears.**
The abstract leads with A_95^obs ≈ 0.98%. The paper is admirably careful and repetitive that this
is an *observed-label* floor and "not a physical parity-amplitude bound," and §6.2 (p. 830–844)
correctly enumerates that the injection-recovery chain injects a dipole only in the observed
hard-label CW/CCW field at fixed per-pixel occupancy and "does not traverse the ViT, NOT_SPIRAL
triage, confidence cut, or spatially varying confusion." The consequence is that the quoted 95%
coverage is conditional on a chain beginning *after* the classifier and holding pixel occupancy
fixed — i.e., it bounds observed-label dipoles under near-tautological conditions and does not
constrain any astrophysical or primordial amplitude. Given how prominently 0.98% is featured
(abstract, Table 1 row viii, Eq. 7, §6.2), the "not a physical bound / fixed-occupancy /
post-classifier" scope must accompany the number at the abstract level, not only deep in §6.2, to
avoid over-reading in citation.

**[MINOR] 4 — Significance-convention proliferation burdens interpretability.**
The paper quotes many non-commensurable z/p values against distinct nulls: moment-z, rank-p,
MASTER moment-z (binary and apodized), binomial-monopole, block-bootstrap, and the −9.47σ /
−9.5σ monopole (z = +6.923, +6.983, +7.033, +7.207, −7.6, −9.47, +3.80, +2.31σ, +3.29σ,
+3.05σ, ...). While Table 2/3 and repeated caveats ("not directly comparable," "not Gaussian tail
significances") are honest, the reader must continually re-anchor which null each z references. A
single consolidated "estimator → sample → null → statistic → role" table exists (Table 1/2), but a
compact notation/glossary box (HC-RI, FS-C, MASTER-AGF, moment-z vs. rank-p, A_p vs. f_CW
conventions) would materially reduce the cognitive load and lower the risk of cross-null
misreading.

**[MINOR] 5 — The released catalog carries an undisclosed-at-abstract-level −9.5σ handedness monopole.**
Catalog C has a global CW fraction 0.497353 (−9.47σ from 0.5; Table 4, Fig. 3). The paper
correctly treats this as classifier/imaging systematics, ships a per-region monopole correction map
(§4.2, App. A), and shows it does not bias the real-space dipole. This handling is reasonable, but a
9.5σ monopole is a defining property of the released labels; a one-line abstract/Section-1 note that
the catalog labels are locally monopole-biased and require per-region renormalization before any
ℓ=0 parity use would appropriately calibrate downstream expectations.

**[MINOR] 6 — Comparison with prior contested literature (Shamir 2012/2020/2022) is qualitative only.**
The stated motivation is the intermittent Shamir dipole claims, yet §5.1 declines any frequentist or
physical exclusion and states a "matched-footprint independent-estimator (Ganalyzer) analysis is
required," deferring it to future work. For a catalog/methods paper positioned against a specific
contested detection, the absence of a matched-footprint reanalysis limits the ability to directly
adjudicate the prior claims. This is honestly scoped as open, but it caps the paper's contribution to
the parity debate and should be acknowledged as such in the Discussion.

**[MINOR] 7 — Submission-readiness: no minted DOI / archival snapshot.**
The Data Availability section states the Zenodo archive "will be deposited at journal submission" and
that the "DOI and commit hashes will be inserted here in place of this sentence." ApJS expects a
DOI-backed archival snapshot for a data release. The manuscript should not be considered
publication-complete until the DOI, frozen commit hash, and exact commit hashes for all
canonical-provenance artifacts are inserted. (Placeholder is acceptable for review but must close
before acceptance.)

**[MINOR] 8 — Reference list is thin (18 entries) relative to the contested literature engaged.**
The parity-violation / spin-alignment debate is only partially cited (Shamir, Iye, Tadaki, Jia). A
data-release paper making claims about isotropy tests and systematics would benefit from broader
citation of the methodological and null-result literature (e.g., prior handedness-systematics and
look-elsewhere-in-cosmology treatments) so the systematics-attribution conclusions are anchored to
independent precedent rather than internal argument alone.

### (3) Is the central claim supported?

Yes — the primary claim that the quality-controlled high-confidence observed-label real-space
chirality dipole is null-consistent (z_mom = +0.635, p = 0.23768) is well-supported by the primary
estimator and is appropriately, even scrupulously, hedged; the principal reservations concern the
released catalog's non-reproducibility, the post-hoc definition of the primary sample, and
abstract-level framing of the A_95 sensitivity floor, none of which overturn the null but all of which
must be addressed for a catalog/methods venue.

---

*End verbatim referee report.*
