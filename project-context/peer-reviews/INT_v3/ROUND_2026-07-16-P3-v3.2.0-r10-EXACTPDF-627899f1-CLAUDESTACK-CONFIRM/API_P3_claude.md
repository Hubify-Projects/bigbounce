# INT v3 Referee Report — P3 (Claude subagent leg)

- **Model:** claude-opus-4-8 (subagent)
- **Date:** 2026-07-16 (PT)
- **Paper:** P3 — "Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations" — v3.2.0-r10
- **pdf_sha256:** 627899f1bfa030b56502150224b174b66186b3d0beb3e608a68b2aab68ae0cd6
- **File reviewed:** pipelines/p3_anomaly_engine/paper3_apjs.pdf (17 pages)
- **Venue:** The Astrophysical Journal Supplement Series (ApJS) — profile APJS-CATALOG
- **Referee prompt:** "You are an expert referee for The Astrophysical Journal Supplement Series. Review this Catalog article manuscript under profile APJS-CATALOG to the standard of a real submission. Respond with exactly: (1) VERDICT; (2) ISSUES numbered, each prefixed [MAJOR] or [MINOR]; (3) One sentence: is the central claim supported?"
- **PARSED VERDICT:** MAJOR REVISIONS

---

## (1) VERDICT: MAJOR REVISIONS

## (2) ISSUES

**[MAJOR] 1 — Central deliverable (general, reusable machinery) is demonstrated on only a single instance.**
The abstract and Introduction (contributions list; §1 "The primary, reusable deliverable is this machinery itself") make the headline claim that the reusable, memory-bounded join + provenance/validation *machinery* is the primary contribution, and that it "is designed to be re-run on any future frozen anomaly or coordinate list" (§1, end of Introduction). But the manuscript exercises the machinery exactly once, on the author's own historical anomaly list. Generality is asserted by design, not evidenced: there is no second input list, no demonstration on a distinct catalog, and no packaged/installable general tool — only repository script paths specific to this pipeline (pipelines/p3_anomaly_engine/scripts/). For an ApJS article whose stated primary deliverable is reusable machinery, the reusability/generality claim must be substantiated (a second worked instance on an unrelated input, or a documented general interface), or the abstract/§1 framing must be softened to "a reproducible recovery pipeline for this list" rather than general machinery.

**[MAJOR] 2 — Community utility / significance for an ApJS Catalog is only partially established.**
The delivered product is 181 rows (170 sub-0.1" core + 11 in the 0.1–1" tail) recovering public IDs for the author's own prior anomaly catalog (ref [5]), and the paper explicitly disclaims essentially every scientific interpretation: it is "not validated detections or unbiased samples for anomaly-rate inference" (abstract), "not a purity claim" (§3.4), "no secure object-identity" (§5), and the 170-row core is "the expected self-recovery of the seed DESI members whose own coordinates define the cluster centroids" (abstract; §3.5) — i.e. the majority of the catalog is a tautological recovery of the seeds that defined the centroids. The stated recommended uses (§5.2) reduce to deterministic retrieval of 181 public spectra by TARGETID plus reproducibility exercises. This is scientifically honest, and the reproducibility engineering is genuinely strong, but the manuscript does not make the affirmative case that a 181-row, interpretation-disclaimed, self-referential product clears the ApJS Catalog bar for broad community utility. The revision should either strengthen this case (e.g. concrete downstream science the list enables that could not be done from the public DESI archive directly) or position the contribution explicitly around the reusable pipeline once MAJOR-1 is addressed.

## MINOR ISSUES

**[MINOR] 3 — Non-reproducible score/residual columns not flagged in-table.**
§2.1/§2.2 and Limitation 1 disclose that the released per-object S and residual metadata "cannot be numerically reproduced from the currently public spectra." Because these are catalog columns (Table 7: original_score, original_residual_b/r/z), the machine-readable table and DATA_DICTIONARY should carry an explicit "frozen / not reproducible from public data" flag so downstream users do not treat S as a recomputable quantity. Table 6/7 note it in prose only.

**[MINOR] 4 — Version-tag proliferation is confusing.**
The manuscript is v3.2.0-r10, the submission bundle is r7, the primary data release is r2, and the warned auxiliary is r5 (footnote 2; §6.4; Data Availability). A reader/user cannot easily tell which artifact version is authoritative for the submitted table. Provide a single up-front component→version→DOI/SHA-256 mapping table and one clear "this is what is being submitted" statement.

**[MINOR] 5 — Title leads with a number the abstract itself deflates.**
The title headlines "170 High-Coordinate-Consistency Core ... Positional Associations," while the abstract and §3.5 establish those 170 are tautological seed self-recoveries, not independent associations. Recommend adjusting the title to signal the self-recovery nature (e.g. "seed-recovery core"), consistent with the paper's own framing.

**[MINOR] 6 — Local-shift null rests on 16 correlated realizations, and the annulus deficit is argued qualitatively.**
§3.5 reports the observed 0.1–1" warning-free-primary annulus (11 rows) sits well *below* the shifted mean (75.56 ± 13.0), and explains this as core self-recovery consuming each cluster's nearest slot. This corollary is plausible but is only argued qualitatively; a direct quantitative check (predicted annulus suppression given 170 consumed slots) would substantiate it. Also state clearly that with 16 correlated shifts the quoted standard deviations are not an independent Poisson error (the text notes this in passing).

**[MINOR] 7 — Thin methodological/cross-match literature.**
For a paper whose claimed contribution is positional-join machinery, the reference list (12 entries, mostly DESI + software) omits standard positional cross-matching / false-match-rate statistical frameworks. Situate the nearest-neighbor + local-shift approach against established cross-identification literature.

**[MINOR] 8 — Negative-redshift rows retained without an in-table flag.**
Two released rows (P3-DESI-000018, P3-DESI-000163) carry unphysical z < 0 (§4.2; Table 5), retained under ZWARN=0. This is disclosed and defensible, but a machine-readable flag would prevent downstream surprise.

**[MINOR] 9 — AAS machine-readable asset / DOI pending.**
The 43-column tab3.tsv, column dictionary, and SHA-256 manifest are described as the AAS digital asset with DOI "pending" (§4.4, §6.4, Data Availability). This is normal at submission, but confirm the submitted table's version matches the r7 bundle and that the dictionary/manifest travel with it.

## (3) Central-claim assessment

The instance-level reproducibility claim — that this specific 181-row recovery is exactly reconstructable from a frozen input with full provenance — is rigorously and convincingly supported (exact row counts, checksums, and the Table 8 audit matrix); however, the paper's *headline* claim of general reusable machinery rests on a single demonstration, and the ApJS-Catalog-level scientific/community value of the product is not yet affirmatively established, so the central claim is only partially supported.
