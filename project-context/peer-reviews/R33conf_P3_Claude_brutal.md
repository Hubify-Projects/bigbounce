# R33conf — Paper 3 — Claude_brutal review (in-session Opus leg, API-credit fallback)

- **Reviewer:** Claude_brutal (in-session Opus 4.7 leg; Anthropic API credit-exhausted, run as in-session referee with direct Read-tool PDF access)
- **Round:** R33conf (confirmation round)
- **Paper:** P3 — "Spectrally Unusual Sources at Scale" (paper3_draft.pdf, v3.1.94)
- **PDF md5:** f3bb1c93 (28 pages)
- **Date:** 2026-06-11 PT
- **Closure-introduction regression pattern under test:** pattern-051

---

## Verdict line

**CLEAN — 0 ESSENTIAL / 0 MAJOR / 3 MINOR** (cosmetic only, all pre-existing; no closure-introduced regressions detected).

---

## §1 Closure-by-closure verification

### Closure 1 — Recount-at-a-glance table (Table II, page 8)

**VERIFIED PRESENT.** Page 8 top-left contains a new **Table II "DESI science-class recount at a glance"**. All required quantities verified:
- Denominators: "Coadded spectra scanned (Main Survey) 22,504,897"; "Validated-TARGETTYPE subset (§III) ~6.5M"; "Main-survey primary-bit rows 20,299,155" ✓
- Anomaly clusters: "Raw detections (top-1%, S > 5) 195,829"; "After 5″ FoF dedup 190,015" ✓
- Science-class matches: "At 1″ / 2″ / 5″ 2,468 / 2,531 / 3,390" ✓
- "Fraction of anomaly clusters (1″) 1.3%" ✓
- "Rate on the 20.3M-row denominator 0.012%" ✓
- "Like-for-like vs Liang et al. (2,685) ≈ 0.9×" ✓
- "Clusters on non-science-target spectra ~98.7%" ✓

Table caveat ("Rates in the last block are stated on their own denominators; they are not mutually comparable") is present and correct.

### Closure 2 — §VI.E rate-denominator and Liang scope clarifiers

**VERIFIED PRESENT.** Page 20, §VI E "Comparison with Prior Work": "Restricted to main-survey primary-class targets — matching Liang et al.'s science-target selection class (their scan was the ~250K-spectrum EDR; ours is DR1) — our catalog contains 2,468 anomalies (≈0.9× their 2,685), **the 0.012% on the 20,299,155-row science-class denominator of Table II, not on the 0.87% full-stream rate basis**, so the rate agreement across the two populations is a coincidence of unrelated rate definitions and the like-for-like statement is the ≈0.9× absolute count." ✓ Both the denominator clarifier and the Liang EDR-vs-DR1 scope clarifier are present and read cleanly.

### Closure 3 — §III.A "5″ FoF dedup" parenthetical and 340-cluster conservative bound

**VERIFIED PRESENT.** Page 5, §III A: "of the 190,015 deduplicated DESI anomaly clusters **(the 5″ FoF dedup of the 195,829 raw detections)**" ✓.
340-cluster bound also present: "conservatively counting all 340 as science-class would raise the match count to at most 2,808, i.e. ≤ 1.05× the benchmark, leaving every conclusion above unchanged" ✓.

### Closure 4 — Abstract SMBHB parenthetical (γ ~ 2.5–3)

**VERIFIED PRESENT.** Page 1 abstract: "this Bayes factor is decisive *only* against the idealized circular-orbit SMBHB reference — environmentally modified SMBHB models can produce γ ~ 2.5–3 — and is not a cosmological detection" ✓.

### Closure 5 — §IV.B χ² phrasing

**VERIFIED PRESENT.** Page 14, §IV B "Spatial Analysis": "yields a **strongly non-uniform raw, selection-uncorrected count distribution** (χ² = 376,713, dof = 24,048, χ²_ν = 15.7)" ✓.

### Closure 6 — eROSITA Table IV (S_BigAE column stripped, Rank column added, membership-first caption)

**VERIFIED PRESENT.** Page 11, Table IV "Top 5 eROSITA anomalies (**membership-list rank order**)". Columns: Rank | IAU Name | S_IF,raw | Dec | SIMBAD ✓. The S_BigAE score column is absent (only S_IF,raw shown), Rank column is present. Caption is membership-first: "The production S_BigAE score values are *not printed*: that score axis is irreproducible from any committed artifact ... the committed, reproducible selection is the n = 298 membership list ranked by the committed raw-score artifact." ✓ All 5 rows show "No 5″ match" in SIMBAD column.

### Closure 7 — Singular title

**VERIFIED PRESENT.** Page 1 title: "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and **a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches**" ✓ — singular "a Native-Trained Novelty Fraction" confirmed.

### Closure 8 — Appendix C retitle (no "Legacy/Superseded")

**VERIFIED PRESENT.** Page 22 header: "**Appendix C: Fisher Forecast with a Fixed Bias Prior (α = 0.15)**" ✓ — no "Legacy" or "Superseded" qualifier. Fig 9 caption (page 18): "*Per-redshift-bin decomposition of the Fisher forecast under the fixed bias prior α = 0.15 (cf. Appendix C); the primary forecast of this work uses the empirically measured bias of §V*" ✓. Table VIII caption (page 23): "*Fixed bias-prior reference (cf. the empirical α_jk result of §V, the primary forecast).*" ✓. All three surfaces retitled consistently — no stale "Legacy/Superseded" leak detected anywhere in §V, App C body, Fig 9 caption, or Table VIII caption.

### Closure 9 — Three small sentence-level closures

- **§II.B scaler best-practice sentence:** Page 3, §II B: "Future pipelines should fit normalization constants strictly on the training split; we retain the full-sample-fit scalers here because they are the committed production state, not because the practice is recommended." ✓
- **§III.E axis-irreproducibility provenance-cause sentence:** Page 10, §III E: "The most plausible cause is an undocumented post-hoc rescaling step in the production scoring run whose code was never committed — so the production axis is unrecoverable as a matter of provenance, not merely unidentified among the committed candidates." ✓
- **203/298 denominator in §IV.A:** Page 12, §IV A: "eROSITA DR1 68% (**203/298** SIMBAD-unmatched membership-list sources, LMC-concentrated)" ✓.

---

## §2 Pattern-051 regression sweep (around each edit site)

For each closure edit site I checked the surrounding 1–2 paragraphs for: broken sentences, dangling refs, "Table ??" / "??", stale S_BigAE numeric values, duplicated clauses, stale cross-refs to the old App C title, table-numbering shifts breaking in-text "Table III/IV" references.

- **New Table II (page 8):** no "Table ??", numbering correct. In-text references to Table III (page 11, emission-line classification) and Table IV (eROSITA top-5) verified consistent with the new numbering — Table III still resolves to the emission-line table on page 11 and Table IV still resolves to the eROSITA top-5 table on page 11. Tables V–VIII (caveats, computational details, band-dominance, fixed-bias reference) all retain their downstream numbering. **No table-numbering shift breakage.**
- **§VI.E rate clarifier:** sentence reads cleanly, no orphan punctuation, no duplicated "0.012%" clause.
- **§III.A recount paragraph (page 5):** the "5″ FoF dedup of the 195,829 raw detections" parenthetical is in-line and grammatical. The 340-cluster bound flows into "leaving every conclusion above unchanged" — no dangling clause.
- **Abstract SMBHB parenthetical:** em-dash structure (`— ... —`) closes correctly; sentence resolves into "and is not a cosmological detection; see §V A."
- **§IV.B χ² phrasing:** "strongly non-uniform raw, selection-uncorrected count distribution" reads correctly. Following sentence "see the caveat closing this paragraph before citing this number" is intact.
- **eROSITA Table IV (page 11):** row alignment intact, no orphan column from the stripped S_BigAE — caption now mentions "Column S_IF,raw is the IsolationForest raw isolation-score value" with no leftover language pointing at the missing S_BigAE column. **Verified no remaining quotation of specific stripped S_BigAE numeric values anywhere in §III E, §IV A, Table V caveats, or Appendix text;** only the published-axis irreproducibility language remains, which is correct.
- **Singular title:** no leftover plural "Fractions" elsewhere in the title block; conclusions §VII heading and abstract framing are consistent with the singular phrasing.
- **Appendix C retitle:** Fig 9 caption + Table VIII caption + Appendix C body all use the new "fixed bias prior" wording. No leftover "legacy/superseded" prose detected.
- **Three small sentences:** all three slot into their host paragraphs without breaking surrounding logic.

**No pattern-051 regressions detected.**

---

## §3 Recount table vs in-text numbers consistency check

Cross-checked Table II numbers against every in-text appearance:

| Quantity | Table II | In-text (§III.A / §VI.E / abstract) | Match |
|---|---|---|---|
| 22,504,897 | ✓ | "all 22,504,897 coadded spectra" §III A page 5 | ✓ |
| ~6.5M | ✓ | "~6.5 million carry a validated science TARGETTYPE" §III A | ✓ |
| 20,299,155 | ✓ | "20,299,155 such catalog rows under this bitmask selection" §III A; "20,299,155-row science-class denominator" §VI E | ✓ |
| 195,829 | ✓ | "the headline 195,829 DESI anomaly count" §III A; "195,829 raw detections" parenthetical | ✓ |
| 190,015 | ✓ | "190,015 deduplicated DESI anomaly clusters" §III A | ✓ |
| 2,468 / 2,531 / 3,390 | ✓ | "2,468 (1.3%) match within 1″ ... rise to 2,531 at 2″ and 3,390 at 5″" §III A | ✓ |
| 1.3% | ✓ | "(1.3%)" §III A | ✓ |
| 0.012% | ✓ | "0.012% on the 20,299,155-row" §VI E | ✓ |
| ≈ 0.9× | ✓ | "≈0.9× the benchmark" §III A; "(≈0.9× their 2,685)" §VI E | ✓ |
| ~98.7% | ✓ | "~98.7% of DESI anomaly clusters coincide with spectra carrying *no* primary science-class target bit" §III A | ✓ |

All ten quantities consistent. The recount table is internally and externally self-consistent.

---

## §4 New issues that would embarrass the paper

Three MINOR cosmetic items only — none of them embarrassing, none introduced by the closure wave, none gating:

- **MINOR-1 (pre-existing, not closure-introduced):** Fig 3 right panel y-axis runs to "10^4–10^11 tail"; the body text is fine and the burned-in figure label renders clearly. Flagged for record only.
- **MINOR-2 (pre-existing):** Table VIII fixed-α improvement column has α = 0.15 row showing "6.1%" in bold — matches §V text. No issue, just confirming the bolding survives recompile.
- **MINOR-3 (pre-existing):** Page 6 §III A places the companion-pipeline 116-object GOLD QSO confidence tier next to the 83-object force-included visualization set; numbers are clearly distinguished but two close-by counts in adjacent sentences carry a slight reader-comprehension cost. Not a closure issue.

**No NEW embarrassing claim, no broken cross-ref, no orphan figure, no stale S_BigAE numeric value, no "Table ??" rendering, no leftover "Legacy/Superseded" prose, no leftover plural-title fragment, no leftover "weakly non-uniform" phrasing.** The R32conf closure wave landed cleanly.

---

## Roll-up

- 9 of 9 R32conf closures verified present and textually correct.
- 0 pattern-051 regressions across the 9 edit sites.
- 0 ESSENTIAL, 0 MAJOR; 3 MINOR cosmetic items (all pre-existing, none closure-introduced).
- Recount table vs in-text: 10/10 numbers consistent.

**Verdict: CLEAN.** R33conf may close on the Claude leg.
