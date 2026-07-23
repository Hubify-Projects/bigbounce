# TRUTH AUDIT — P4 v1.0.269 confirmation board (ROUND 2026-07-22, EXACTPDF 52985a4f, CLAUDESTACK)

**Paper:** P4 — Galaxy Chirality Catalog, `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Bound PDF sha256:** `52985a4fdde187c8ea874f98b9ba0d459164f3194da337a566aaf88394a13caf` (matches all 3 legs' manifest + Claude's shasum recompute; 32 pp).
**Review commit:** `44b666cb045f405383bf88aa49f8ed0e252f0a67`
**Legs audited:** Claude INT (MINOR-REVISIONS, 4 minors) + Grok grok-4.3 API (MINOR-REVISIONS, 1 MAJOR/2 MINOR) + Gemini gemini-3.1-pro-preview API (MINOR-REVISIONS, 1 MAJOR/3 MINOR).
**Protocol:** every finding → exactly one source-cited verdict ∈ {ALREADY-TRACKED-GATE, DISCLOSED-RE-FLAG, SCOPE-VENUE-OPINION, FALSIFIED, GENUINELY-NEW-REAL}. In doubt → GENUINELY-NEW-REAL.
**Evidence base:** the bound `.tex`; committed retrain artifacts under `pipelines/p2_chirality/outputs/g1_retrain/`; canonical dispositions `project-context/peer-reviews/DISPOSITIONS/P4.md` (DP4-xx ledger); live Zenodo record (as reported by Claude INT, HTTP-200 verified).

---

## KEY FACT ESTABLISHED FROM ARTIFACTS — the epoch story (MINOR-2)

From `pipelines/p2_chirality/outputs/g1_retrain/g1_training_result.json` + `full_run.log.tail` + `PROVENANCE.md`:

- It is **ONE single GZ1-core run**, not two runs. `best_val_acc = 0.9930515344528084`, `best_epoch = 47`; early stop at epoch 62 (best=47). `n_total = 8637` (GZ1 6,637 confident CW/CCW + 2,000 synthetic NS; `ce_resnet_present=false`).
- **Epochs 0–4:** stuck on the 0.66-train / ~0.62-val plateau (val 0.6190 → 0.6572).
- **Epoch 5:** breaks out of the plateau — val jumps 0.6572 → **0.8819** (train 0.759). This is what "broke out of the same 0.66/0.62 plateau by epoch 5" refers to.
- **Epoch 47:** reaches its best **0.9931** three-class val accuracy. This is what Table 13's "epoch 47" refers to.

**Conclusion:** Table 13 ("best-epoch val = 99.31%, epoch 47") is CORRECT. The body phrase "broke out of the same 0.66 plateau **by epoch~5 to 0.9931**" (tex L978 and L1665) telescopes two distinct facts — plateau-breakout AT epoch 5, best 0.9931 AT epoch 47 — into a clause that reads as if 0.9931 was hit by epoch 5. Both numbers are individually true; the phrasing creates the apparent Table-13 tension. This is a **real, genuinely-new clarity defect** with a one-clause fix, not a numeric error and not two conflicting runs.

---

## FINDINGS TABLE (row per finding)

| # | Leg | Finding (verbatim gist) | Verdict | Source-cited basis |
|---|-----|--------------------------|---------|--------------------|
| C1 | Claude | MINOR-1 — Zenodo deposit (DOI 21461899) is v1.0.268 titled "…949,584 High-Confidence…"; live manuscript v1.0.269 titles "…890,069 Quality-Controlled…". DAS discloses it but a reader following the DOI lands on the pre-quarantine title. Recommend depositing v1.0.269. | **GENUINELY-NEW-REAL** | tex L1873 (DAS: "archives the reviewed v1.0.268 PDF…the present manuscript is v1.0.269…subsequent versions added…under the shared concept DOI") + L918 + L1879. In-paper STATEMENT is accurate & the archive-prior-version pattern is the accepted P2/P3 convention (DP4-21). Residual: the Zenodo **landing-page title** itself carries the superseded 949,584 headline. Real, off-paper currency action. See decision note below. |
| C2 | Claude | MINOR-2 — Table 13 "epoch 47" vs text "by epoch 5 to 0.9931" ambiguity. | **GENUINELY-NEW-REAL** | Artifacts `g1_retrain/g1_training_result.json` (breakout epoch 5 val 0.8819; best_epoch 47 val 0.99305) + `full_run.log.tail` ("best 47, val_acc=0.9931"). Same single run; telescoped phrasing at tex L978 + L1665. One-clause fix. |
| C3 | Claude | MINOR-3 — prominence of the non-reproducible-classifier caveat for an ApJS catalog product; surface once in Data-Availability/catalog framing at abstract-level prominence. | **SCOPE-VENUE-OPINION** | Already disclosed at abstract L918 ("composition-faithful CE-included retrain collapses to chance…historical CE-included accuracy is not reproducible…released catalog labels are unchanged"), Sec 2 L978, App B L1665. Claude itself labels it "presentation/prominence recommendation, not a correctness defect." Optional 1-sentence DAS add. |
| C4 | Claude | MINOR-4 — Table 5 "Excluded / valid pixels: 2,597 / 23,633": 2,597 is excluded ROWS (890,069−887,472), not pixels. | **GENUINELY-NEW-REAL** | tex L1257 `Excluded / valid pixels & $2{,}597$ / $23{,}633$`; L1224 confirms 887,472 rows enter the 23,633-pixel support ⇒ 2,597 = excluded rows/galaxies. Trivial real mislabel. |
| G1 | Grok | MAJOR — "the parity-even morphology observable supports no primordial-parity bound" is unsupported and contradicts the paper's own transfer-function caveats. | **FALSIFIED** | Grok misparses "supports **no** …bound" (=yields no bound) as asserting a zero-parity bound. The paper's thesis IS that no physical bound is available pending the open transfer function: L918 ("this is an observed-label sensitivity floor, not a physical parity-amplitude bound, which remains gated on the morphology transfer function"), Sec-6.2 g=0.398 "illustrative", DP4-12 (Chern-Simons/parity bound deliberately NOT claimed). The statement AGREES with the caveats; the alleged contradiction is false. Optional wording hardening below. |
| G2 | Grok | MINOR — text never states whether released Catalog C labels were regenerated after composition adjudication or remain historical outputs. | **FALSIFIED** | Stated explicitly FOUR times: L976 ("does not alter the released Catalog~C labels, which remain the historical production outputs"), L978 ("released Catalog~C labels remain unchanged historical production outputs"), L1665 ("released Catalog~C labels are unchanged"), abstract L918 ("released catalog labels are unchanged"). |
| G3 | Grok | MINOR — a "minted Zenodo DOI" is asserted but never supplied; only the HF revision path is given. | **FALSIFIED** | DOI `10.5281/zenodo.21461899` supplied explicitly THREE times: L1873 (`doi:10.5281/zenodo.21461899`), L1879, and referenced from abstract L918; concept DOI 21461898 at L1873. Claude INT independently curl-verified HTTP-200. Grok's native-PDF pass missed the DAS. |
| M1 | Gemini | MAJOR — forensic training-history accounting reads like a lab notebook/rebuttal; relegate the legacy-run reconstruction + composition conflicts entirely to Appendix B. | **DISCLOSED-RE-FLAG** | Standing presentation disposition **DP4-13** ("presentation/repetition/single-primary-narrative complaint … editorially closed" v1.0.237; re-flagged & re-adjudicated M5/M26/M30/M33/M38/M42). Narrative-placement editorial preference on honestly-disclosed content; the forensic detail is load-bearing transparency the loop chose to keep in-body. |
| M2 | Gemini | MINOR — raw SHA-256 hashes, commit fragments, deep paths embedded in main-text prose disrupt reading flow; move to footnotes/tables/DAS. | **DISCLOSED-RE-FLAG** | Same DP4-13 presentation disposition (hash/artifact-path density, "self-contained" re-flag dispositioned M30/M33/M5-E2). Editorial preference, not a correctness defect. |
| M3 | Gemini | MINOR — Sec 6.2: suggest concrete methodological steps to close the transfer-function gate (e.g. pixel-level CW/CCW injection into raw DESI imaging). | **SCOPE-VENUE-OPINION** | The transfer function is honestly disclosed as an open gate (L918, DP4-12/-15 OPEN-COMPUTE). Constructive future-work suggestion on an acknowledged-open item; not a defect in the reviewed bytes. |
| M4 | Gemini | MINOR — Sec 4.3: add one sentence explaining why the primary real-space dipole estimator is immune to the monopole-mask leakage that afflicts the ℓ=1 harmonic diagnostics. | **SCOPE-VENUE-OPINION** | Pedagogical-clarity suggestion; the paper already frames harmonic analyses as "systematics diagnostics" only and real-space as primary (L918, Sec-notation "block-bootstrap"/"MASTER" convention block). Optional expository add, not a correctness issue. |

---

## DECISION NOTE — MINOR-1 (Zenodo title): defect vs convention, and the correct fix

**Decision: DISCLOSED CONVENTION, not a defect — but with one real, actionable currency item.**

1. The **archive-prior-version pattern** (the minted record deposits the exact reviewed bytes of the immediately-prior version) is the SAME convention already accepted for P2/P3, and the paper's Data-Availability prose discloses it accurately (L1873). That part is correct and needs **no** prose change.
2. The residual is real but narrow: a reader landing on version-DOI 21461899 sees the Zenodo **metadata title** "…949,584 High-Confidence…", the pre-quarantine headline the science itself superseded (949,584 HC − 59,515 unsafe = 890,069). In isolation that landing title is mildly reader-misleading.
3. **The metadata-edit fix is WRONG and is rejected here.** The v1.0.268 Zenodo title matches the v1.0.268 PDF **bytes** it archives (the title change to "890,069 Quality-Controlled" happened at v1.0.269). Editing the record's title to 890,069 would make the metadata **misdescribe its own archived artifact** — a worse integrity state than the current honest one.
4. **Correct fix = deposit v1.0.269 as a NEW version under the existing concept DOI 21461898** (which the paper already commits to: L1873). The concept DOI then resolves to a latest-version landing whose title matches the manuscript; the version DOI 21461899 correctly stays byte-bound to v1.0.268. Optionally lead reader-facing citations with the concept DOI (resolves-to-latest) rather than the pinned version DOI.

---

## GENUINELY-NEW-REAL FIX LIST (concrete edits)

**FIX-1 (C4, real, trivial — .tex L1257).** Table 5 row relabel so the 2,597 numerator is not called "pixels":
`Excluded / valid pixels & $2{,}597$ / $23{,}633$ \\` → `Excluded rows / valid pixels & $2{,}597$ / $23{,}633$ \\`
(2,597 = 890,069 selected − 887,472 supported rows; only 23,633 is a pixel count.)

**FIX-2 (C2, real, clarity — .tex L978 AND L1665, both occurrences).** Disambiguate breakout-epoch from best-epoch on the single GZ1-only run:
`…broke out of the same $0.66$ plateau by epoch~5 to 0.9931.` → `…broke out of the same $0.66$ plateau by epoch~5 and climbed to its best $0.9931$ three-class validation accuracy at epoch~47 (Table~\ref{...}).`
(Grounds the "epoch 5" breakout and the Table-13 "epoch 47" best in one clause; artifact-confirmed as one run.)

**FIX-3 (C1, real, off-paper currency — Zenodo action, NOT a prose edit).** Deposit v1.0.269 as a new version under concept DOI `10.5281/zenodo.21461898`, so the concept-DOI landing headline matches the live manuscript. Do **NOT** edit the v1.0.268 record's metadata title (would misdescribe archived bytes). In-paper DAS prose (L1873) already correct — leave as-is, or optionally foreground the concept DOI as the reader-facing handle.

**FIX-4 (G1, OPTIONAL clarity hardening — .tex L918; finding itself FALSIFIED).** Not required, but since a calibrated referee (Grok) misparsed it into a MAJOR, hardening the abstract's closing sentence removes the ambiguity at zero science cost:
`The parity-even morphology observable supports no primordial-parity bound.` → `The parity-even morphology observable yields no physical primordial-parity bound (that bound remains gated on the unresolved morphology transfer function).`

---

## SUMMARY

- **BLOCKER / MAJOR (real):** none. Both API-leg MAJORs FALSIFIED (Grok G1 misparse) / DISCLOSED-RE-FLAG (Gemini M1 narrative-placement, standing DP4-13). All load-bearing quantities independently reconcile (Claude INT recompute, all ✓).
- **Genuinely-new real items:** 3 — two one-line .tex clarity fixes (Table 5 label; epoch 5-vs-47 phrasing ×2 sites) + one off-paper archival-currency action (deposit v1.0.269). None touches a science number.
- **Convergence read:** consistent with directive-K/L — 0 genuinely-new *scientific* findings; the 3 genuinely-new items are presentation/currency-tier and do not affect the null result or any released number.
