# INT v3 Referee Report — Paper P4 (Chirality Catalog + Methods)

- **Model:** claude-opus-4-8 (subagent)
- **Date:** 2026-07-16 (PT)
- **Paper:** P4 — "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog" v1.0.263
- **pdf_sha256:** de12ac783b0581f35ad024b2314283726a123b3c5a83db5dd1c833021aa9da10
- **Venue:** ApJS (The Astrophysical Journal Supplement Series)
- **Profile:** APJS-CATALOG-METHODS
- **Exactness gate:** PASS (on-disk shasum -a 256 == de12ac78…9da10)

**PARSED VERDICT: MAJOR REVISIONS**

---

## Referee report (verbatim)

You are an expert referee for The Astrophysical Journal Supplement Series. I have reviewed this Catalog + methods article under profile APJS-CATALOG-METHODS to the standard of a real submission.

### (1) VERDICT: MAJOR REVISIONS

### (2) ISSUES

**[MAJOR] 1 — The catalog's core deliverable (the machine-generated labels) is not reproducible, and the committed training records mutually conflict.**
Section 2.2 and Table 12 concede that "the exact historical training realization is not fully recoverable," that no object/split manifest or run receipt ties named objects to the checkpoint, and that the committed provenance records disagree on first-order facts: 26,616 vs 26,626 total rows, 826 vs 846 CE-selected non-spirals, a 21,293/5,323 split vs none, and 93.6878% vs 92.10% validation accuracy. For an ApJS catalog whose primary product *is* a set of classifier labels, the inability to regenerate the label-producing model — and the presence of two conflicting committed accounts of how it was trained — is a first-order reproducibility deficiency. Honest disclosure (which the paper provides in full) is necessary but does not substitute for a regenerable pipeline or a single reconciled training record. The authors should either (a) reconstruct and checksum a single canonical training realization with a stable object/split manifest, or (b) state explicitly in the abstract and the data-availability section that the released labels are a non-regenerable historical artifact, and quantify the resulting uncertainty on all downstream catalog statistics.

**[MAJOR] 2 — The headline null depends on a non-preregistered, post-hoc sample-selection predicate.**
Section 4.3 (and Appendix B) states that the `raw_flip_qc_unsafe` quarantine "was introduced and finalized during post-review closure after inspection of the earlier unsafe-inclusive result; it was not preregistered." The primary claim ($N_{\rm selected}=890{,}069$, $z_{\rm mom}=+0.635$, $p=0.23768$) is computed on the sample *after* this cut. The paper argues the numerical effect is small ($z=+0.48$ excluded vs $+0.52$ baseline), which is welcome, but a null result whose defining sample was selected after looking at the data carries a look-elsewhere/garden-of-forking-paths liability that a single sensitivity number does not fully discharge. Please (a) report the primary estimator on the pre-quarantine sample as the co-equal headline (not only in an appendix), (b) state the quarantine predicate's definition and thresholds as fixed *before* it is applied, and (c) show that no other plausible unsafe-row definition materially changes the conclusion.

**[MAJOR] 3 — The primary external validation of label quality is overlap-contaminated; there is no independent held-out validation.**
The Galaxy Zoo 1 cross-match (Tables 14–15, Appendix) cannot be anti-joined against the 6,637 GZ1 rows used in training because stable training IDs were not retained; the paper itself flags the comparison as "overlap-contaminated rather than independent." The reported quality figures — three-class accuracy 58.7%, CW/CCW agreement 69.91% ($\kappa=0.40$) — are therefore upper-biased and cannot serve as an independent characterization of catalog reliability. An ApJS catalog release should demonstrate label fidelity on a genuinely held-out human-labeled set with training objects removed. If that is infeasible with the retained records (per Issue 1), this limitation must be stated as a hard caveat wherever accuracy/agreement numbers appear, not only in the appendix.

**[MAJOR] 4 — The "all residuals are systematics" synthesis is asserted without a joint statistical framework.**
The manuscript reports numerous highly significant residuals — raw real-space $+2.31\sigma$, MASTER $\ell=1$ moment ratio $+6.923$/$+7.033$, monopole $-9.47\sigma$ (Catalog C) / $+28.72\sigma$ (Catalog A), hemisphere $3.05\sigma$ — and attributes every one to survey/classifier systematics. Yet Section 3.2 and 4.5 concede that the estimators are "not commensurable," "no joint likelihood is defined," and "the missing joint covariance remains an open methodological gate." The systematics interpretation may well be correct, but as presented it is a qualitative narrative rather than a demonstrated result: without a joint covariance the paper cannot show that these residuals are mutually consistent with a single systematics model, nor exclude a sub-dominant physical component. Please either construct the joint nuisance covariance / likelihood needed to support the synthesis, or soften the claim to state that the systematics attribution is a plausibility argument pending a joint analysis.

**[MAJOR] 5 — The released catalog carries a large, highly significant CW-fraction monopole and coherent low-$\ell$ structure that limit its fitness for parity science, and no causal mechanism is isolated.**
Catalog C exhibits a $-9.5\sigma$ monopole offset from $f_{\rm CW}=0.5$ and coherent $\ell=1$–$3$ MASTER structure ($+6.923,+2.931,+3.089$). The paper candidly lists three candidate mechanisms (GZ1 training-label excess, residual orientation-dependent bias, DESI photometric asymmetry) but isolates none, and recommends users locally re-normalize the per-region monopole before any $\ell=0$ statistic. For a supplement catalog whose advertised novelty includes parity applications, a $\sim0.26\%$ ($9.5\sigma$) uncorrected handedness monopole is a material fitness-for-use limitation. The abstract and the catalog documentation should state prominently that the released fractions are systematics-biased at this level and are not usable for $\ell=0$ parity detection without the shipped correction map; the current abstract phrasing ("supports no primordial-parity bound") understates that the catalog itself carries a $9.5\sigma$ handedness monopole.

**[MINOR] 6 — Overloaded $z$/$\sigma$ notation.** The symbols $z$ and $\sigma$ are used throughout for quantities the text repeatedly clarifies are *not* Gaussian tail significances but null moment ratios (e.g. $z_{\rm mom}=+6.923$ at $p=0.002$). Despite the repeated disclaimers, reusing detection-significance notation for non-Gaussian moment ratios is a persistent misreading hazard; adopt a distinct symbol (e.g. $R_{\rm mom}$) for moment ratios and reserve $\sigma$/$z$ for calibrated significances.

**[MINOR] 7 — Appendix bulk of explicitly-excluded diagnostics.** Sections/Appendix C–E and Tables 8, 16 carry many "historical provenance" diagnostics that the paper then excludes from the strict FS-C synthesis (different support, uncomputed covariance, unrecorded mask). This is honest but dilutes the main line; consider moving pure-provenance material to a supplementary data note or a repository README and keeping the appendix to diagnostics that bear on the primary result.

**[MINOR] 8 — Literature framing is thin.** With 18 references, the parity/handedness context is under-cited relative to the claims made (e.g. earlier reports of large-scale spin/handedness asymmetry, independent parity-violation searches in galaxy 4-point statistics, and prior GZ handedness-bias studies). A catalog paper positioned against the Shamir/CE-ResNet literature should more completely situate the observed-label-bias question.

**[MINOR] 9 — Reproducibility handles are promised but not yet minted.** The Zenodo DOI and the frozen release-tag commit hash are stated as "inserted at submission time" (Data Availability). ApJS will require the archival DOI and the exact tag to be live and resolvable at acceptance; the current placeholders should be resolved and the artifact-link set re-verified before the paper is considered complete.

### (3) One sentence on the central claim
The narrow central claim — that the strict quality-controlled HC observed-label real-space dipole is statistically consistent with zero ($p=0.238$) — is supported *within its own honestly-scoped definition*, but its standing as a scientific result is materially weakened by a non-preregistered post-hoc sample cut, non-reproducible labels, overlap-contaminated validation, and a $9.5\sigma$ systematics-attributed monopole whose causal origin is not isolated.
