# CLAUDE INT — P3 raw referee report (routine re-sweep 2026-07-23)

- **Paper:** P3 — "Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations"
- **Bound PDF:** `pipelines/p3_anomaly_engine/paper3_apjs.pdf`
- **Declared version:** v3.2.0-r12, 17pp, ApJS (AASTeX v7.0.1, twocolumn)
- **Binding SHA-256 (expected):** `d27ce97a42549c6c8b23134c3cc7afbc0232a0a92d0c79b64f37d9d58e2721bc`
- **Computed SHA-256:** `d27ce97a42549c6c8b23134c3cc7afbc0232a0a92d0c79b64f37d9d58e2721bc`
- **Binding:** VERIFIED (exact match). Reviewed all 17 pages of the exact bound bytes.
- **Referee stance:** standard high journal-referee bar, no steering. Scope: confirm the 2026-07-22 confirmation-wave closures landed with no regression/new contradiction; recompute the Poisson-deficit statement; flag anything genuinely new.

## Closure verification (2026-07-22 confirmation-wave)

**C1 — Zenodo tense corrected to the truthful archives-prior-version convention.** LANDED (tense), with a version-number glitch (see N1).
p13: "an immutable versioned archival deposit of the reviewed **v3.2.0-r10** release ... is now published on Zenodo under the minted archival DOI doi:10.5281/zenodo.21461888 (version DOI; the concept DOI doi:10.5281/zenodo.21461887 presently resolves to the latest deposited version (v3.2.0-r10) ...). That deposit archives the reviewed v3.2.0-r10 bytes exactly."
The tense is now truthful: Zenodo archives the *prior reviewed* r10 bytes (done, present tense), while the manuscript is ahead — exactly the archives-prior-version convention requested. Version DOI vs concept DOI usage is internally consistent. The only defect is the accompanying "present manuscript is v3.2.0-r11" self-reference (N1).

**C2 — 0.1–1″ shifted-annulus comparison rewritten as an explicit significant deficit (11 vs 75.56), explained by in-paper core self-recovery slot-consumption.** LANDED and arithmetic verified.
- Abstract: "The corresponding shifted 0.1–1″ annulus contains 75.6 ± 13.0 warning-free-primary associations versus 11 observed, so the tail is not treated as secure candidate-level identity."
- p5: "The observed strict 0.1–1″ annulus contains 11 rows, whereas the shifted annulus mean is 75.56 (13.01; 61–101)."
- p6: "the 11 observed rows fall well below the shifted mean of 75.56 — a deficit, not an excess ... each core cluster's nearest-neighbor slot is consumed by its own seed member inside 0.1″, shielding those clusters from additional matches in the surrounding annulus."
- Figure 1 caption echoes: observed 11 vs shifted mean 75.6, slot consumed by own seed inside 0.1″.
The rewrite explicitly names it a *significant deficit* (not an excess) and gives the correct physical mechanism (self-recovery slot-consumption). Prior ambiguous framing removed. No regression.

**C3 — version-tag key footnote completed.** LANDED.
Footnote 2 (p2) now maps all load-bearing component tags: r2 (audited primary data release), r5 (secondary warned-primary auxiliary table), r7 (checksum-bound submission bundle), **r12 (this manuscript)**, with intermediate checkpoints r1/r3/r4/r6/r10 named as further frozen build/audit/submission checkpoints. The "a later stage does not relabel earlier component versions" convention is stated. The footnote is internally complete and correct — it self-identifies the manuscript as r12, matching the title page.

## Poisson-deficit statement recompute (task-required)

The paper does NOT assert a Poisson significance — it explicitly states the 16 shifted realizations are "correlated local controls rather than an independent Poisson null." That framing is honest and correct. Recomputed the underlying arithmetic for internal consistency:

- Warning-free global-primary within 1″: **181** observed vs shifted mean **76.19** (13.30; 61–103) (p5).
- Warning-free within 0.1″ (core self-recovery): **170** observed vs shifted mean **0.625** (p5).
- Therefore 0.1–1″ annulus, observed: 181 − 170 = **11** ✓ (matches stated 11).
- Annulus shifted mean: 76.19 − 0.625 = **75.565 ≈ 75.56** ✓ (matches stated 75.56).
- Deficit magnitude (informal, shifts correlated so not a clean Poisson z): (75.56 − 11)/13.01 = 4.96 — "large shortfall," consistent with the paper calling it a large deficit while declining a Poisson-null interpretation. ✓
- Physical mechanism check: the 170 core clusters self-recover at <0.1″ (each consumes its single nearest-neighbor slot), so they cannot also match in the 0.1–1″ annulus — depleting the annulus relative to the shifted control where the moved seed frees the slot. Mechanism is sound and matches the counts. ✓

The deficit statement is internally consistent, arithmetically exact, and honestly scoped (deficit corollary of self-recovery, not secure candidate-level identity, not an independent Poisson experiment).

## Independent cross-checks (spot-verified, unchanged science)

- Selection waterfall Table 4: 190,015 → 20,299,155 → 2,468 → (−20 non-ZCAT_PRIMARY) → 2,448 → (−2,267 ZWARN≠0) → 181. Arithmetic exact (2,468−20=2,448; 2,448−2,267=181). ✓
- 170 core + 11 tail = 181 ✓ ; released fraction 181/2,468 = 7.33% ✓.
- Warned auxiliary 2,267 = 2,194 GALAXY + 72 QSO + 1 STAR ✓ ; released 181 = 157 GALAXY + 23 QSO + 1 STAR ✓.
- ZWARN Table 3 rows sum: 787+152+1,294+3+10+2+19 = 2,267 ✓.
- Nearest/all-neighbor: cluster minimum separation 5.02294″; 2,468 parent / 181 strict pairs ✓ (App A step 6, Sec 3.1).
- FITS provenance: 22.37 GB SHA-256 matches DESI official checksum list; 8/8 remote-parity ranges pass; manifest 10 payloads self-excluded (Table 8 all PASS). ✓
- Table 5 twelve illustrative rows internally consistent with the strata description; two negative-z rows P3-DESI-000018/000163 flagged as template artifacts (z = −0.00033819 / −0.00033733), consistent with Sec 4.2. ✓
- Audit Matrix (Table 8, p17): every listed check PASS with cited evidence, characterized as integrity-relative (not an astrophysical-anomaly claim). ✓

All science, selection logic, and provenance are unchanged and internally consistent. No regression from the confirmation-wave.

## Genuinely-new finding

**N1 (MINOR, presentation / internal inconsistency) — stale in-body version self-reference contradicting the footnote and title page.**
Data Availability (p13) states: "the present manuscript is **v3.2.0-r11**, one patch ahead, and will be added to the same Zenodo concept record as a new version on the next re-stage." However the title-page tag (p1), the binding, AND the newly-completed version-tag-key footnote 2 (p2, "v3.2.0-r12 this manuscript") all identify the document as **v3.2.0-r12**. The Data-Availability self-reference is therefore stale by one patch and directly contradicts the paper's own footnote. This is a factual internal inconsistency, not a science/data problem — appears to be version-stamp drift (the C1 Zenodo prose was authored at the r11 stage and not re-synced when the paper bumped to r12 for C2/C3). Closeable by syncing that string: "the present manuscript is v3.2.0-r11, one patch ahead" → "v3.2.0-r12, two patches ahead."

No other new contradictions surfaced across the 17 pages. The three targeted closures landed correctly and the deficit arithmetic recomputes exactly.

## Verdict rationale

All 2026-07-22 confirmation-wave closures landed correctly: Zenodo tense truthful, annulus deficit (11 vs 75.56) explicit and arithmetically exact with a sound self-recovery slot-consumption mechanism, version-tag footnote complete and internally correct. Poisson-deficit statement recomputes exactly and is honestly scoped. One genuinely-new low-severity internal inconsistency (N1: Data-Availability self-reference v3.2.0-r11 contradicting the r12 footnote/title page) prevents a clean ACCEPT under the high referee bar. Severity is copy-edit tier, single string.

VERDICT: MINOR-REVISIONS
