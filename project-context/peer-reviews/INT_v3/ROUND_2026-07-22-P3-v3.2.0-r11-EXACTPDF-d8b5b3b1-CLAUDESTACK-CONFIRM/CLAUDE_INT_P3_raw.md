# Claude INT Referee Report — Paper 3 (P3)

- **Paper:** "Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations" (Houston Golden)
- **Target journal:** ApJS (catalog paper)
- **Version:** v3.2.0-r11
- **PDF:** `pipelines/p3_anomaly_engine/paper3_apjs.pdf` (17 pp)
- **Round:** ROUND_2026-07-22-P3-v3.2.0-r11-EXACTPDF-d8b5b3b1-CLAUDESTACK-CONFIRM
- **Reviewer leg:** Claude INT (independent journal referee)
- **Date:** 2026-07-22

## Exact-PDF binding verification (fail-closed)

- Binding file `intwave_bindings.json` P3 record: pdf `pipelines/p3_anomaly_engine/paper3_apjs.pdf`, version `v3.2.0-r11`, sha256 `d8b5b3b1e7cb802a2661f9e800b2b7a5fc4c09dcda7771ae731771afdb6f297a`.
- `shasum -a 256` of on-disk PDF: `d8b5b3b1e7cb802a2661f9e800b2b7a5fc4c09dcda7771ae731771afdb6f297a`.
- **RESULT: MATCH.** Proceeded with review of the bound exact PDF.

## DOI resolution verification

- `curl -sIL https://doi.org/10.5281/zenodo.21461888` → HTTP/2 302 → `zenodo.org/doi/10.5281/zenodo.21461888` → 302 → `zenodo.org/records/21461888` → **200 OK**. Version DOI resolves.
- Zenodo API `records/21461888`: title matches paper; **version = `3.2.0-r10`**; `doi = 10.5281/zenodo.21461888`; `conceptdoi = 10.5281/zenodo.21461887`; publication_date 2026-07-20. Consistent with the paper's statement that the deposit "archives the reviewed v3.2.0-r10 bytes."
- Concept DOI `curl -sIL https://doi.org/10.5281/zenodo.21461887` → resolves to `zenodo.org/records/21461888` (i.e., latest deposited version = **r10**). API `records/21461887` also returns the same r10 record. **No r11 version record is discoverable on the Zenodo concept.** (Basis for MAJOR-1.)

---

## Findings

### MAJOR-1 — Zenodo "r11 added as a new version" claim is not reflected on Zenodo (release/DOI accuracy)
**Evidence:** p. 13, DATA AVAILABILITY, lines ~825–837: "an immutable versioned archival deposit of the reviewed v3.2.0-r10 release … is now published on Zenodo under the minted archival DOI doi:10.5281/zenodo.21461888 (version DOI; the concept DOI doi:10.5281/zenodo.21461887 resolves to the latest deposited version …). That deposit archives the reviewed v3.2.0-r10 bytes; **the present manuscript is v3.2.0-r11, added to the same Zenodo record as a new version.**"

The version-DOI half is accurate: 21461888 = r10 bytes, honestly disclosed. However the asserted-as-completed clause that this r11 manuscript is "added to the same Zenodo record as a new version" is **not** verifiable and is currently contradicted by Zenodo state: the concept DOI 21461887 still resolves to record 21461888 (version 3.2.0-r10), and no newer (r11) version record exists under the concept. Because the paper is itself v3.2.0-r11, this is a self-referential archival claim that must be exactly true. Either (a) actually deposit the r11 bytes as a new Zenodo version (so the concept DOI resolves to r11), or (b) soften the tense to future/conditional ("r11 will be deposited as a new version on finalization; the archived version DOI presently pins the r10 bytes"). This is a discrete factual correction — it does not touch the catalog science and needs no re-review of substance.

### MINOR-1 — "Version-tag key" footnote is incomplete
**Evidence:** p. 2–3, footnote 2 ("Version-tag key"): defines only r2 (primary release), r5 (warned auxiliary), r7 (submission bundle), and r11 (this manuscript). The body additionally uses r1 (p. 13, "historical p3-v3.2.0 and p3-v3.2.0-r1 tags"), r3 (p. 10, "r3 audit artifacts" / public_viewer_audit.json), r4 (p. 15, "aas submission v3.2.0-r4/"), r6 (pp. 3, 12, "r6 machine-readable sensitivity sidecar," "r6 controls," `p3_apjs_r6_science_controls.py`), and r10 (p. 13, Zenodo "reviewed v3.2.0-r10 release"). The footnote presents itself as *the* key but does not enumerate r1/r3/r4/r6/r10, so a reader cannot map every RC tag encountered. Add the missing tags (or state the key is illustrative).

---

## Consistency and integrity checks that PASSED (verified against the exact PDF)

**Catalog counts / waterfall (all reconcile):**
- 170 core + 11 tail = 181 (title, abstract, §3.4, §6.4, Conclusions). ✓
- SPECTYPE composition 157 GALAXY + 23 QSO + 1 STAR = 181 (abstract, §4.2, Table 5 strata). ✓
- Waterfall (Table 4 / Fig. 2 / §4.1): 2,468 parent − 20 non-primary = 2,448 global-primary; 2,448 − 2,267 warned = 181. ✓
- 181/2468 = 7.33% (Table 4 note, §5.1). ✓ ; ZWARN removes 2,267/2,448 = 92.6% (§7). ✓
- "2,287 exclusions" (Conclusions, p. 13) = 2,468 − 181 = 20 + 2,267. ✓
- Warned auxiliary 2,267 rows; IDs P3-DESI-WARNED-000001…002267; composition 2,194 GALAXY + 72 QSO + 1 STAR = 2,267. ✓
- Redshift bins (§4.2): 2(z<0)+36+36+76+8+13+10 = 181. ✓ ; positive-z subset = 179. ✓
- North/south 134+47 = 181 (§4.3); dark/bright 162+19 = 181 (§4.2). ✓

**ZWARN distribution (Table 3, p. 7):** seven masks sum to 2,267 (787+152+1,294+3+10+2+19). ✓ Non-exclusive bit totals: LITTLE_COVERAGE 2,110 (787+1,294+10+19), SMALL_DELTA_CHI2 1,467 (152+1,294+2+19), POORDATA 34 (3+10+2+19) — all reproduce from the mask table. ✓

**Local-shift control (abstract ↔ §3.5) all match:** parent 2,468 obs vs 86.69±14.42 (66–109); strict 181 obs vs 76.19±13.30 (61–103) within 1″; 0.1–1″ annulus 11 obs vs 75.56±13.01 (61–101); core 170 obs vs 0.625 at ≤0.1″; parent 0.1″ 2,456 vs 0.75. ✓

**Separation tails:** Table 2 lists exactly 11 rows, all in (0.1″,1″], max 0.990574 (= abstract's 0.9906″); 8 above 0.5″, 5 above 0.75″. ✓ Target-to-original-member (§3.4): 11 exceed 0.1″, one exceeds 1″ (P3-DESI-000030 at 1.979009″), none exceed 2″; max 1.979 = §2.1 counterfactual value. ✓ Median target-to-cluster 0.00127″ (§3.5 ↔ §4.3). ✓

**Sub-0.1″ circularity reframe (central honesty check) — HANDLED WITH STRONG INTEGRITY.** Abstract (lines 42–45), §3.5 (pp. 5–6), Fig. 1 caption, §6.4/§7 all consistently state the sub-0.1″ 170-vs-0.625 excess is the *expected seed self-recovery* of single-member clusters whose centroid is the seed's own TARGET_RA/TARGET_DEC (which the matched catalog still contains), that it "verifies the recovery end to end rather than providing independent association evidence," and that the local-shift control "is informative only for the 0.1–1″ tail." The 170 core = single-member clusters is internally consistent: only P3-DESI-000030 (n_detections=2) has >1 member and it falls in the 11-tail, so all 170 core are single-member. No overclaim of association from the core. This is exemplary disclosure.

**Table 5 (p. 9) 12-row strata:** six top scores + highest-score QSO (000020) + sole STAR (000039) + max-z (000047, z=6.088) + two negative-z (000018, 000163) + max-separation slot. The max-separation row (target-to-cluster max = P3-DESI-000005, 0.991″) overlaps the top-six set, so per the stated "overlaps filled by next highest-score unused row" rule the slot is filled by P3-DESI-000007 (S=6.76, the 7th-highest score). Internally consistent once the overlap-fill rule is applied. ✓

**Other:** 18 fields read = count of Table 1 (3+2+4+4+1+4); "read 18 columns" (abstract) ✓. Union mask 0x3000000000000007 = bits 0,1,2,60,61 ✓. FITS SHA-256 `2d95ad99…b128b49b` identical in §2.2 and the p. 13 build command ✓. 143 checkpoint parts consistent across §3.1/§6.1/§6.4 ✓. AAS table 181×43 consistent (Table 5 note, §DATA AVAILABILITY, Table 8) ✓. Reference numbering [1]–[12] consistent with in-text and SOFTWARE section ✓. AAS journal digital-asset DOI consistently disclosed as "pending / not yet assigned" (pp. 12,13,15, Table 8) — honest open gate ✓.

**Presentation / LaTeX visual audit (pdftoppm @110 dpi):** pp. 1, 4, 8, 9, 17 rendered. No column overflow, no multi-column escape, no right-margin path bleed. Superscripts in Eq. 2 (2⁰|2¹|2²|2⁶⁰|2⁶¹) and Table 3 binary components render correctly (the "20|21|22|260|261" seen in pdftotext is an extraction artifact, not a PDF defect). Full-width tables (Table 5 8-col, Tables 6–8) and Figures 1–3 sit within margins. Version stamp "v3.2.0-r11" on the p. 1 dateline matches the binding. Clean.

---

## Assessment

The catalog science, internal numeric consistency, and honest-disclosure integrity are excellent — the sub-0.1″ circularity reframe and the "not an anomaly rate / not a purity estimate / not a detection" boundary-setting are handled with rigor rare in catalog papers. The only substantive defect is a single verifiably-premature archival claim (the r11 Zenodo version is not yet on the concept DOI, which still resolves to r10), plus an incomplete version-tag key. Both are discrete factual corrections requiring no re-review of the science. Recommend MINOR-REVISIONS: resolve MAJOR-1 (deposit r11 or soften the tense) and MINOR-1 (complete the version key).

VERDICT: MINOR-REVISIONS
