# Independent Referee Report — Paper 3 (P3)

- **Model:** claude-opus-4-8 (Claude Code subagent, independent INT referee leg)
- **Date:** 2026-07-16 (PT)
- **Paper:** P3 — "Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations"
- **Version:** v3.2.0-r9
- **PDF SHA-256:** `7526e6859cf4544f0b835f1f7b2d8bd990314c3879fc5ed9eae4e743f3274d36`
- **PDF path:** `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_apjs.pdf`
- **Venue:** The Astrophysical Journal Supplement Series (ApJS)
- **Review profile:** APJS-CATALOG
- **Exactness gate:** PASS (on-disk SHA-256 equals the declared hash)
- **PARSED VERDICT:** MAJOR REVISIONS

---

## Referee statement

I reviewed all 16 pages of this manuscript as an expert ApJS referee under the
Catalog profile, to the standard of a genuine submission. The paper is
unusually honest, technically clean, and exceptionally well documented on the
provenance/checksum axis. My concerns are not about integrity or execution of
the join; they are about the scientific value and interpretation of the
deliverable at the level a Catalog article in ApJS is held to.

### (1) VERDICT

**MAJOR REVISIONS**

### (2) ISSUES

**[MAJOR] 1 — The sub-0.1″ "association excess" (Section 3.5, Figure 1) is
largely circular / self-recovery, and is over-interpreted.**
The released cohort is drawn from 190,015 historical clusters that *contain a
DESI member by construction* ("survey-membership string containing `desi_dr1`",
Section 2.1), and the cluster coordinate used for the re-match is the ICRS
*mean of the member coordinates*, which includes that DESI member's
`TARGET_RA/TARGET_DEC` (Sections 2.1, 3.1). Consequently, re-matching the
cluster mean against the same public DESI catalog is expected to recover the
seed DESI member at ≪0.1″ — this is re-identification of the object the cluster
was partly built from, not an independent positional association. The 60–120″
shift controls necessarily lose that self-recovery, so the reported "170
observed vs shifted mean 0.625 within 0.1″" and the statement that "the sub-0.1″
core has strong aggregate association evidence" overstate what the experiment
shows. The paper gestures at recovery language elsewhere but Section 3.5 and
Figure 1 present this as a nontrivial excess. The core result must be reframed
explicitly as seed-member self-recovery, and the shift-control comparison
either removed for the core or accompanied by a control that breaks the
member-coordinate dependence (e.g., using an independent cluster centroid that
excludes the DESI member's own coordinate).

**[MAJOR] 2 — Scientific value/motivation of the deliverable is not
established, because the upstream is admittedly irreproducible and
uncalibrated.**
The recovered catalog inherits its selection from a frozen BigAE anomaly stream
whose per-object scores "cannot be numerically reproduced from the currently
public spectra" and carry "no physical feature or detection efficiency"
(Section 2.1), with an unrecoverable production selection function (Sections 5,
7). The concrete reusable content is therefore 181 already-public DESI
TARGETIDs flagged by a black-box, uncalibrated process, with the ranking metadata
(`S`) explicitly meaningless as a physical quantity. For a Catalog article the
manuscript needs a much stronger, honest argument for why this set is a useful
reusable resource given that its provenance selection function cannot be
reconstructed — otherwise the product is a list of public spectra of uncertain
scientific pedigree.

**[MAJOR] 3 — Scope/size relative to the ApJS Catalog bar.**
The deliverable is 181 rows (170 core + 11 tail), none presented as a validated
detection, and the manuscript is dominated by release-engineering, provenance,
and checksum machinery rather than astrophysical content (Sections 3.4, 6.1–6.4,
Appendix, Tables 6–8). The authors should justify that a 181-row recovery of
public IDs — with no calibrated scores, no purity claim, and no validated
identities — meets the threshold and expected scientific utility of an ApJS
Catalog article, versus a shorter data-note/RNAAS-style contribution.

### (2b) MINOR issues

**[MINOR] 4 — Reproducibility framing conflates the join with the science.**
The headline reproducibility (Sections 3.1, 6, abstract) applies to the
positional join and provenance replay only; the underlying scores and selection
function are irreproducible. The abstract should state this distinction plainly
so a reader does not read "reproducible recovery" as scientific reproducibility
of the anomaly selection.

**[MINOR] 5 — Internal release-engineering version tags leak into the prose.**
The manuscript repeatedly cites internal component tags (v3.2.0-r2 / r5 / r7 /
r9, "submission bundle", checkpoint-part counts) in the body text (Sections 2.1,
4.1, 6.3–6.4, footnote 2). This is non-standard for a journal article and
distracting; consolidate into a single data-availability/provenance statement.

**[MINOR] 6 — Thin anomaly/outlier-detection literature.**
Only three domain references (Baron & Poznanski 2017; Liang 2023; Nicolaou 2026)
situate the anomaly-detection context. Broaden the discussion of prior spectral
outlier/anomaly work and its catalog conventions.

**[MINOR] 7 — Table 5 "z = −0.000" display is confusing.**
Two rows print `z = −0.000` for z = −0.00033819 and −0.00033733; even with the
footnote this reads as an error. Show the sign/precision inline or use a clearer
format.

**[MINOR] 8 — Primary Catalog deliverable is not yet deposited.**
The AAS machine-readable table (`tab3.tsv`, 181×43) — the actual reusable
product for a Catalog article — is described as "prepared for submission" with
DOI "pending" (Sections 6.4, Software, Data Availability). Acceptance for a
Catalog article normally requires the machine-readable table deposited as the
AAS digital asset; a HuggingFace snapshot is supplementary, not a substitute.

**[MINOR] 9 — Retained but unused cross-survey provenance (SDSS/LAMOST).**
Historical cross-survey labels are carried as provenance (Section 2.1) but play
no role in the DR1-only recovery. State this explicitly to avoid any impression
of cross-survey validation of identity.

**[MINOR] 10 — Title length/awkwardness.**
The two-clause title embedding exact row counts is unwieldy; consider a more
compact form.

### (3) Is the central claim supported?

The narrow literal claim — that public DESI DR1 identifiers were recovered for
181 objects and partitioned into a 170-row ≤0.1″ core and an 11-row 0.1″–1″
tail by a fully checksum-audited, reproducible join — is supported by the
machinery, but the paper's implied value as a reusable anomaly catalog is not
yet established, because the sub-0.1″ core excess is largely seed-member
self-recovery and the upstream scores/selection are admittedly irreproducible
and uncalibrated.
