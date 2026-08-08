# INT v3 Referee Report — P4 (Chirality Catalog)

- **Model:** claude-opus-4-8 (subagent, independent referee leg)
- **Date:** 2026-07-18 PT
- **Paper:** P4 v1.0.267 (`pipelines/p2_chirality/chirality_catalog_paper.pdf`)
- **pdf_sha256:** eaa9a5a6d1985a2411f68946ee27647ec2b5023b1609af07e24ffaf3e30ed6cd
- **Exactness check:** PASS (on-disk SHA-256 equals the bound target hash)
- **Venue:** ApJS — profile APJS-CATALOG-METHODS
- **PARSED VERDICT:** MAJOR REVISIONS

---

## Referee prompt (as issued)

> You are an expert referee for The Astrophysical Journal Supplement Series. Review this Catalog + methods article manuscript under profile APJS-CATALOG-METHODS to the standard of a real submission. Respond with exactly: (1) VERDICT: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT. (2) ISSUES: numbered, each prefixed [MAJOR] or [MINOR], naming the specific section/claim and concrete problem. (3) One sentence: is the central claim supported?

---

## (1) VERDICT: MAJOR REVISIONS

## (2) ISSUES

**[MAJOR] 1 — The released data product is not reproducible (Sec. 2.2, Appendix B, Table 13).**
For an ApJS *catalog* paper the reproducibility of the primary data product is a central acceptance criterion, and here it is only partially met. The released 8,474,531-row Catalog C was produced by a historical pipeline whose exact training realization "is not fully recoverable" (no retained object/split manifest, random-state record, or run receipt). The from-scratch manifest-retained retrain (κ = 0.9733) explicitly "does not re-provision the CE-ResNet component (~67.5% of the historical composition), does not resolve the 826-vs-846 conflict, and does not change the released Catalog C labels." So the labels users will cite cannot be regenerated end-to-end; only a GZ1-core sub-component (~32.5%) is now regenerable. The author must either (a) regenerate the *released* labels reproducibly, or (b) give a far more prominent, editor-facing justification for why a byte-frozen-but-non-regenerable catalog meets ApJS reproducibility standards.

**[MAJOR] 2 — Unresolved internal training-record conflicts (Sec. 2.2, Table 13).**
The committed records disagree on fundamental training-set quantities: 826 vs 846 CE-selected NOT_SPIRAL rows; 26,616 vs 26,626 total labeled rows; 93.6878% (audit) vs 92.10% (README) validation accuracy. The paper reclassifies this as a "conflict disclosure" rather than resolving it. Transparent, but for a published catalog an unresolved discrepancy in the training composition of the released classifier is a substantive deficiency; it should be reconciled, or the exact provenance of each committed number stated so a reader can determine which is authoritative.

**[MAJOR] 3 — The *released* labels lack a clean independent validation (Sec. 6.3, Appendix B, Tables 15–16).**
The only clean, provably training-disjoint validation (κ = 0.9733 on 3,000 held-out GZ1 spirals) is of the *regenerated* retrain checkpoint, not of the released Catalog C classifier. The released classifier's human-agreement figure (69.91%, Cohen's κ = 0.40, Table 15) is explicitly overlap-contaminated (training rows not anti-joined; no stable training IDs). The manuscript is candid that these "measure fundamentally different quantities," but the net effect is that the shipped labels have no clean, independent human-agreement benchmark — a gap an ApJS catalog referee will want closed with an object-level anti-join on the released realization, or an explicit boxed statement that no such validation exists for the released product.

**[MAJOR] 4 — Uncharacterized ~9.5σ parity-even monopole of unresolved physical-vs-imaging origin (Sec. 4.2, Fig. 3, Sec. 5, Sec. 6.2).**
The equivariant Catalog C carries a −9.47σ CW-fraction monopole (−0.529% deviation). The paper convincingly shows (i) it is a monopole, not a dipole; (ii) it does not bias the fitted real-space dipole (constant template absorbed into the fitted monopole; 500-realization generative test); and (iii) the classifier-injection forward model excludes classifier confusion as its source (0.0% of the observed value) and sign-excludes the GZ1 training-prior candidate. But the residual attribution — true-sky parity asymmetry vs. parity-odd DESI imaging/photometric systematic — "remains open." A released chirality catalog thus ships a 9.5σ systematic whose origin is uncharacterized; the paper itself instructs future ℓ=0 users to locally renormalize. This limitation is honestly disclosed and a correction map is provided, but its prominence and the openness of the attribution warrant elevation and, ideally, further diagnostic narrowing before publication.

**[MINOR] 5 — Statistics presentation is hard to follow and invites misreading (Tables 1–3, Sec. 3.1, 4.x).**
The paper juggles multiple non-commensurable nulls, supports, and conventions (moment-ratio z_mom, empirical rank-p, block-bootstrap z, binomial σ, MASTER z_ℓ), repeatedly and correctly warning that z_mom values are *not* Gaussian significances and must not be mapped through z→p. The care is commendable, but the sheer proliferation raises reader-misinterpretation risk. A single consolidated "estimator/null/convention" table with an explicit "how to read each number" legend would materially improve usability for catalog users.

**[MINOR] 6 — NOT_SPIRAL completeness / edge-on selection channel is unquantified (Sec. 4.1, Sec. C, Table 16).**
5,030 GZ1-confirmed spirals are assigned to NOT_SPIRAL with "no chirality-neutral assumption," and 15.80% (505,889) of classified spirals are edge-on (b/a < 0.30). These are labeled "unquantified completeness/selection channels." A catalog paper should quantify the resulting spiral-selection completeness (even approximately) so downstream users can model the selection function.

**[MINOR] 7 — Missing per-object failure ledger for dropped rows (Sec. 4.1).**
35 galaxies are absent from the final catalog (8,474,566 → 8,474,531) with "identities and exact failure reasons unavailable." Small in number, but a catalog release should list which object IDs were dropped and why; "unavailable" is not acceptable provenance for a supplement data product.

**[MINOR] 8 — Archival/DOI gate still open (Data Availability).**
The Zenodo DOI and the frozen commit hashes are placeholders ("will be inserted here ... at submission time"). Standard, but the paper cannot receive a final positive recommendation until the DOI, frozen release tag, and canonical-provenance commit hashes are populated and independently resolvable.

**[MINOR] 9 — Retention of superseded "provenance-only" diagnostics bloats the manuscript (Table 8, Appendix D, Table 17, Fig. 9).**
Numerous historical calculations (WLS 9-template fit, density-stratified null, boundary-distance variance, leg-proxy cross-power, direct cross-spectrum) are carried in the paper solely as "different-support provenance ... excluded from the strict synthesis." At 31 pages this is a heavy load for a reader/referee. Most of this belongs in the data-release documentation, with only the support-bound rows (apodization robustness, multipole spectrum) retained in the article.

**[MINOR] 10 — AI-assisted methodology disclosure (Acknowledgments).**
The work discloses an "agentic multi-model pipeline for literature review, code development, analysis, and adversarial internal peer review." The disclosure and author accountability statement are appropriate; flagging only so the editor can confirm conformance with current ApJS policy on AI-assisted preparation.

**[MINOR] 11 — Sensitivity floor should be foregrounded next to the abstract upper limit.**
The observed-label 95% sensitivity floor A_95^obs ≃ 0.98% means the null only excludes observed-label dipoles above ~1%; the observed A_dip = 0.467% simply lies below the floor. The abstract states the value but a reader can over-read the "null" as a strong exclusion. One clause at the abstract-level upper-limit sentence ("sensitivity floor, not an exclusion of sub-1% dipoles") would prevent this.

### Internal-consistency spot checks (all PASS — noted as a positive)
- 949,584 − 59,515 = 890,069 ✓; CW 1,592,107 + CCW 1,609,053 = 3,201,160 ✓; +NS 5,273,371 = 8,474,531 ✓
- f_CW = 1,592,107 / 3,201,160 = 0.49735 ✓; Catalog C dev −0.265% → −9.5σ (σ ≈ 2.79×10⁻⁴) ✓; Catalog A +0.788% → +28.7σ ✓
- rank p = 2377 / 10001 = 0.237676 ≈ 0.23768 ✓; A_dip = 0.00466520 < A_95^obs = 0.98% ✓
No arithmetic inconsistencies detected across abstract, tables, and body.

## (3) Is the central claim supported?

Yes — the primary claim, a null observed-label chirality dipole in the quality-controlled HC sample (z_mom = +0.635, rank p = 0.23768) explicitly framed as an observed-label sensitivity floor rather than a physical parity bound, is internally consistent and scrupulously caveated; the MAJOR revisions concern reproducibility, validation, and characterization of the *released catalog data product* rather than the narrow statistical null itself.
