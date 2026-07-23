# Claude INT Referee Report — P4 (Galaxy Chirality Catalog)

**Paper:** "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog"
**Author:** Houston Golden (Independent Researcher)
**Version:** v1.0.269 (Dated July 20, 2026), 32 pp, AASTeX7 twocolumn, ApJS-venue catalog/methods paper
**Bound PDF:** `pipelines/p2_chirality/chirality_catalog_paper.pdf`
**Leg:** Claude INT (independent journal referee), ROUND 2026-07-22, EXACTPDF binding.

## EXACT-PDF BINDING VERIFICATION — PASS

- Recorded sha256 (intwave_bindings.json, P4): `52985a4fdde187c8ea874f98b9ba0d459164f3194da337a566aaf88394a13caf`
- Computed `shasum -a 256` on the bound path: `52985a4fdde187c8ea874f98b9ba0d459164f3194da337a566aaf88394a13caf`
- **MATCH.** Reviewed the exact bound bytes. 32 pages confirmed via pdfinfo.

## METHOD
Full pdftotext read of all 32 pages; pdftoppm visual renders of pp. 1, 6, 22, 28; log scan for overfull hboxes; live curl verification of all archival handles (Zenodo version/concept DOIs, CE-ResNet Zenodo, arXiv, HF provider-overlay revision tree). Every quantitative claim below was recomputed from the paper's own reported integers.

---

## INTERNAL CONSISTENCY — EXTENSIVELY VERIFIED, ALL TIES OUT

Every cross-checked number is self-consistent to the reported digit:

- **Catalog composition:** CW 1,592,107 + CCW 1,609,053 = Nspiral 3,201,160 (✓); + NS 5,273,371 = 8,474,531 released rows (✓); parent 8,474,566 − 35 = 8,474,531 (✓, Sec 4.1).
- **Primary selection:** 949,584 HC − 59,515 unsafe = 890,069 Nselected (✓); Nsupport 887,472; excluded-from-support = 2,597 (✓).
- **Global CW fractions (Table 4):** C = 1,592,107/3,201,160 = 0.497353 → excess −0.265%, Dev −9.47σ (✓); A = 0.507879 → +0.788% (✓). A=2(fCW−½): −0.529%↔−0.265%, +1.576%↔+0.788% (✓).
- **Primary dipole (Table 5):** z=(0.00466520−0.00362029)/0.00164643=+0.6346 (✓); rank p=(2376+1)/10001=0.237676 (✓); observed Adip=0.467% below A95≈0.98% floor (✓).
- **MASTER ℓ=1 (Tables 6/7):** z=(7.0113−0.585)e-6/9.2823e-7=+6.923 (✓); binomial 500-draw +6.983, 1e4-draw +7.207 (✓).
- **Joint covariance (Table 9):** monopole −0.003949/0.000601=−6.57 (✓); real-space +2.21, WLS +0.81, C1master −0.61 all reproduce (✓).
- **GZ1 confusion (Table 15, N=240,919):** row/col sums reconcile to 240,919; 3-class acc 141,438/240,919=58.7% (✓); chirality subset 117,205, agreement 81,939/117,205=69.91% (✓); all six precision/recall values reproduce (✓).
- **geff:** sCW=39,011/57,900=0.674, sCCW=42,928/59,305=0.724 → geff=sCW+sCCW−1=0.398 (✓); pooled 2a−1=0.398217 (✓). The sensitivities are correctly conditioned on chirality-classified predictions and derive from Table 15 as claimed.
- **Disjoint validation:** confusion [[1460,10],[30,1500]] sums to 3,000; acc 0.98667; κ recomputed = 0.9733 (✓).
- **CE-composition arithmetic:** 6,637+17,153+819+2,000 counts → class 11,904/11,886/2,819 = 26,609; train/val 21,288/5,321 (✓). Audit identity 6,637+17,153+826+2,000=26,616 (✓).
- **Banked passes:** 8,474,531×2 = 16,949,062 = 1.69e7 ≈ "1.7×10⁷" (✓).

The 826-vs-846 disclosure, A95^obs≈0.98%, retrain 99.31%, disjoint κ=0.9733, and the honest-negative CE section (val 0.5617, chance-on-chirality with the 0.106+0.894×0.5=0.553 arithmetic) are all present, internally consistent, and — notably — the honest-negative is framed as strengthening rather than undermining the null. This is exemplary disclosure.

## ARCHIVAL / EXTERNAL CLAIMS — VERIFIED LIVE

- `https://doi.org/10.5281/zenodo.21461899` → HTTP 200, resolves to zenodo.org/records/21461899 (✓). API metadata: version **1.0.268**, pub_date 2026-07-20, files = {chirality_catalog_paper.tex, paper4_arxiv_v1.0.268.tar.gz, SHA256SUMS, manifest.json, chirality_catalog_paper.pdf, P4_v1.0.252_tracked_provenance.tar.gz}. This exactly matches the paper's disclosure that the deposit archives the **v1.0.268** reviewed bytes.
- Concept DOI `10.5281/zenodo.21461898` → 200, redirects to the latest version record (✓, correct concept-DOI behavior; matches paper).
- CE-ResNet `10.5281/zenodo.7167388` → 200 (✓); arXiv:2210.04168 → 200 (✓).
- HF provider overlay revision `911316f31c21f2c4b933a2f3a761274cfe85c6d6`, path `apjs-release/v1.0.259-strict-primary/` → tree returns **exactly seven files** (MANIFEST.json, PRIMARY_REPRODUCTION.json, README.md, SCHEMA.json, SHA256SUMS, primary_strict_fixed_occupancy_amps_10000.npy, reproduce_p4_primary_null_v1_0_259.py); MANIFEST.json resolves HTTP 200. This corroborates the paper's "all seven overlay files were re-downloaded ... and byte-verified" claim.

## PRESENTATION — CLEAN
- LaTeX log: **0 Overfull \hbox**.
- Visual renders (pp. 1, 6, 22, 28): clean two-column layout, no column overflow, no margin escapes; Tables 1, 13 and Figure 9 well-formed; monospace artifact paths wrap correctly. Title/date stamps ("July 20, 2026; Version v1.0.269") consistent on p.1.

---

## FINDINGS

### BLOCKER — none.

### MAJOR — none.
The paper's headline is a null with an explicitly-labeled observed-label sensitivity floor (not a physical parity bound), stated repeatedly and correctly; the load-bearing numbers all verify; archival handles resolve. No finding rises to MAJOR.

### MINOR

**MINOR-1 — Archival deposit carries the pre-quarantine title/headline.**
The minted Zenodo deposit (DOI 21461899) is version 1.0.268 and its title is *"...949,584 High-Confidence DESI Spirals..."*, whereas the live manuscript (v1.0.269) titles *"...890,069 Quality-Controlled High-Confidence DESI Spirals..."*. The Data Availability paragraph **accurately discloses** this ("That record archives the reviewed v1.0.268 PDF and source ... the present manuscript is v1.0.269"), so the archival *statement* is correct — but a reader following the DOI lands on a paper whose title/headline sample number differs from the cited version. The paper already commits to adding subsequent versions under the concept DOI; recommend depositing v1.0.269 as a new version so the citable landing page matches the manuscript being reviewed. Evidence: p.1 title vs. Zenodo API `metadata.version=1.0.268`, `metadata.title`; Data Availability p.30 (lines ~4311–4314 of extract).

**MINOR-2 — Epoch-of-best ambiguity for the GZ1-core retrain.**
Table 13 records "Retrain: best-epoch val. accuracy = 99.31% (epoch 47)", while the honest-negative discussion (Sec 2 / App B) states "an identical-optimizer GZ1-only run broke out of the same 0.66/0.62 plateau **by epoch 5** to 0.9931." If these describe the same regenerable GZ1-core realization, "epoch 5" and "epoch 47" read as inconsistent; if they are two separate runs (manifest retrain vs. an honest-negative control), one clause disambiguating them would remove the tension. Evidence: Table 13 bottom block (p.22) vs. Sec 2 CE-included-negative paragraph (p.3–4, "broke out ... by epoch 5 to 0.9931").

**MINOR-3 — Prominence of the non-reproducible-classifier caveat for a catalog paper.**
The released Catalog C labels rest on a historical CE-included training realization whose headline accuracy (93.69%/92.10%) is **not reproducible** — the composition-faithful honest retrain collapses to chance on chirality (val 0.5617). The author discloses this thoroughly, retains the checkpoint, and supplies a regenerable GZ1-core with a provably training-disjoint κ=0.9733. This does not threaten the *primary null* (hard-argmax counts; a degraded classifier dilutes toward null; human-vote GZ1 corroborates). For an ApJS **catalog** product, however, this is the single most consequential limitation of the released resource; recommend surfacing it once in the catalog/Data-Availability framing at the same prominence it currently has in the abstract, so downstream catalog users cannot miss it. This is a presentation/prominence recommendation, not a correctness defect. Evidence: Abstract; Sec 2 honest-negative; App B Table 13; DIAGNOSIS_ce_included_retrain.json reference.

**MINOR-4 — Table 5 column label.**
Table 5 row "Excluded / valid pixels: 2,597 / 23,633" — 2,597 is the count of excluded **rows/galaxies** (890,069 − 887,472), not pixels; the shared "pixels" label is mildly ambiguous. Trivial wording fix. Evidence: Table 5 (p.11).

---

## ASSESSMENT
This is an unusually rigorous, self-auditing manuscript. Every load-bearing quantity I recomputed reconciles exactly; every archival handle resolves and matches its disclosed version/revision; the honest-negative CE section and the observed-label-vs-physical distinction are handled with exemplary care and are consistently caveated; presentation is clean (0 overfull hboxes). The remaining items are small clarity/archival-currency points, all either already disclosed or trivially fixable, none affecting the science. A version-1.0.269 Zenodo deposit (MINOR-1) and the two one-line clarifications (MINOR-2, MINOR-4) plus the prominence tweak (MINOR-3) would fully close the round.

VERDICT: MINOR-REVISIONS
