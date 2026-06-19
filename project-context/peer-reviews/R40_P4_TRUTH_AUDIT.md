# R40 P4 — Truth Audit (Survey-Scale Galaxy Chirality, v1.0.188, FROZEN)

**Audit lead**: Opus truth-audit + synthesis leg
**Date**: 2026-06-18 (America/Los_Angeles)
**Paper**: `pipelines/p2_chirality/chirality_catalog_paper.tex` (1231 lines), PDF md5=c47abc18, 23 pp
**Protocol**: `feedback_peer_review_truth_audit_protocol` — every finding grounded against on-disk artifact before any VERIFIED-OPEN.

**Vendor inputs**:
- OpenAI `gpt-5` methodology — MAJOR REVISIONS (E1–E12, M1–M10, N/Ni items)
- Gemini `2.5-pro` cosmology — MAJOR REVISIONS (E1, M1–M2, m1–m2, T1–T2)
- Grok `4.3` brutal (image-rasterized) — MAJOR REVISIONS (E1–E4, M1–M4, N1–N3)
- Perplexity citations — **CALL FAILED** (400: content > 100KB; no findings returned)
- Claude Opus 5th leg — **ACCEPT, frozen status confirmed**

**Prior**: Paper is FROZEN at 5+ rounds of universal ACCEPT. By protocol the strong prior is that vendor findings are stale / already-closed in prior rounds (notably R39conf/EXT5). Demand on-disk proof before any VERIFIED-OPEN.

---

## Per-finding verdicts

### The "reproducibility / Data Availability" cluster (OpenAI E4/E5/M6, Gemini E1)
**Claim**: Body text contains ephemeral artifact paths, internal version lineage ("v1.0.185"), future date ("June 2026"), "DOI not yet minted", commit `53b41d12`, mutable HF tag `v2026.04`. Must be replaced with archival Zenodo DOI before publication.
**On-disk**: CONFIRMED PRESENT. `chirality_catalog_paper.tex:1005` ("commit 53b41d12 (v1.0.185 lineage, June 2026)... DOI will be deposited at journal submission"); `:1010` ("persistent archival DOI ... has not yet been minted"); `\artifact{}` paths throughout (`:938`, `:858`, `:1000`, etc.).
**Verdict**: **OUT-OF-SCOPE (pre-submission deferral, by design).** The text is real, but it is the *deliberate* pre-arXiv state: the Zenodo DOI is minted AT submission, not before — that is the standing workflow. The `\artifact{}` macro renders as a stable GitHub blob hyperlink (`:36`, pinned to commit `53b41d12`), not a bare filesystem path, so the OpenAI/Grok "unciteable path" framing is MISLABELED. The future-date / version-lineage prose is cosmetic submission-time hygiene, already tracked. No frozen-paper closure: these resolve mechanically at the submission step (DOI mint + date stamp), which is downstream of arXiv freeze. **Not a blocker, not a content defect.**

### Abstract σ-juxtaposition (Grok E1/E4, OpenAI E8/E11/E12)
**Claim**: Abstract juxtaposes +0.41σ (isotropic-bootstrap) with z=0.70 (label-shuffle) and +3.64σ vs +7.93σ without a local "not directly comparable" qualifier.
**On-disk**: `:348` abstract carries TWO explicit local qualifiers verbatim: *"Note: the +0.41σ ... and z=0.70 ... arise from distinct null procedures and are diagnostic-only, not directly comparable as detection significances"* AND *"Note: the σ values quoted in this paragraph arise from distinct null procedures ... not directly comparable ... diagnostic indicators only."* Table I caption (`:444`), notation §(`:515`), and every figure caption (`:547`,`:573`,`:626`,`:788`) repeat the qualifier.
**Verdict**: **STALE.** The exact fix the reviewers demand is already in the abstract — this was the R39conf σ-mixing closure (`:67` changelog: "σ-mixing caveats abstract+4 captions"). Grok's image-rasterized read missed the inline italic notes.

### Look-elsewhere inconsistency (OpenAI E1)
**Claim**: §III.B "<1σ after look-elsewhere" contradicts Appendix C / Table I row (v) "p_LEE≤10⁻⁴".
**On-disk**: Table I caption `:444` and `:680`,`:721`,`:906` fully reconcile this: the **principled** correction is the direct-MC max-statistic null (p_LEE≤10⁻⁴, rejecting random-label noise → systematics-attributed), and the Gaussian Bonferroni "<1σ" is explicitly labeled a **heuristic cross-check** ("noted here only as a qualitative cross-check ... Bonferroni formally assumes independence which the overlapping-hemisphere grid does not guarantee"). Row (v) reports the LEE-corrected significance with the raw direct-MC value stated alongside. Changelog `:72` records this exact EXT5/R39 closure: "Bonferroni/BH layer dropped to heuristic cross-check only."
**Verdict**: **STALE / MISLABELED.** Already a closed finding; the two numbers measure different things and the text says so explicitly.

### Split/augmentation arithmetic (OpenAI E9/M8/N6)
**Claim**: 80/20 of 25,790 should give n_val=5,158 not 5,323; +826 aug should give n_train=21,458 not 21,293 → "not truly 80/20."
**On-disk**: `:409` states the split is on the **augmented combined pool of 26,616**, with the validation split never augmented. Arithmetic: 0.20 × 26,616 = **5,323.2** (n_val=5,323 exact); 0.80 × 26,616 = **21,292.8** (n_train=21,293 exact); 21,293+5,323 = 26,616. The 826 = horizontal-flip augmentation applied to training split only. Provenance: `c17_item13_training_semantics.json`.
**Verdict**: **MISLABELED (reviewer arithmetic error).** OpenAI assumed split-before-augment on 25,790; the paper explicitly splits the 26,616 pool. It IS exactly 80/20. No defect.

### Fig sky_map ("Fig 4") colorbar A_p vs (N_CW−N_CCW)/N (Grok M2)
**Claim**: Color bar labeled per-pixel asymmetry but caption claims A_p; mislabeled by factor 2.
**On-disk**: `:538` caption explicitly defines the field; `:613` states the partner map is in f_CW units "not the A_p units of Fig.~\ref{fig:sky_map}: the two..." — the convention difference is documented, not an error. A_p = (N_CW−N_CCW)/N_spiral is the stated definition (`:680` fn).
**Verdict**: **OPINION / STALE.** Caption is internally consistent and the f_CW/A_p convention is explicitly disclosed.

### Label-noise / monopole-leakage budgets (Grok M3/M4, OpenAI M4)
**Claim**: GZ1 69.91% κ=0.40 noise not propagated; 0.68% residual-monopole-after-MASTER leakage tolerance not computed.
**On-disk**: `:409` "We treat 69.91% as the conservative accuracy floor and propagate it to all downstream isotropy bounds via the sub-percent systematic floor." Monopole-after-MASTER: `:683`,`:994` quantify post-MASTER monopole-only null reproduces only ~12% of C₁ (+4.84σ residual), i.e. the leakage tolerance IS computed.
**Verdict**: **STALE.** Both budgets are present.

### Structural / length / placement (Gemini M1, OpenAI M7) — move appendix results to body, trim to ≲18pp
**Verdict**: **OPINION.** Editorial preference, not a correctness defect. WLS z≈−18 exclusion and eight-anchor summary are referenced in the abstract and §IV; relegating granular derivation to appendices is a legitimate authorial choice. No on-disk error.

### Remaining MAJOR/MINOR/NIT (OpenAI M1/M2/M3/M5/M9/M10, N1–N9, Ni1–5; Gemini M2/m1/m2/T1/T2; Grok E2/E3/M1/N1/N2/N3)
- **Gemini M2 / Grok E3** (+3.64σ vs +7.93σ "cherry-pick"): `:633` Table III caption explicitly explains 500-MC vs 10⁴-perm run sizes, "retained in text for continuity with the leakage analysis." **STALE.**
- **Grok E2** ("largest catalog" superlative): hedged as "to our knowledge" `:348`. **OPINION.**
- **Future date June 13 2026** (Gemini m2, Grok N1, OpenAI E5): submission-time stamp, resolves at submission. **OUT-OF-SCOPE.**
- All other MINOR/NIT items (unit-vector typography, colorbar unit labels, "pp" definition, Spearman supplement, reliability ECE, ref [39] software-citation style, table mini-tables): **OPINION / polish-tier**, none load-bearing, all on a FROZEN universally-accepted paper.
- **Perplexity**: no findings (API failure). **N/A.**

### Claude 5th leg ACCEPT — corroboration
All quantitative spot-checks independently reproduce: CW frac 0.4974±0.000279 (−9.47σ), Fisher floor √(3/N)=9.68e-4, 99.32% monopole reproduction, all multipole/monopole z-values, GZ1 0.6991, dilution g, 23pp/0 overfull/0 undef, N3 novelty. OpenAI's own "Arithmetic spot-checks (passed)" block (`:148`–`:156`) corroborates every headline number. **Confirmed.**

---

## Merged verdict

| Cluster | Vendors | Verdict |
|---|---|---|
| Data-availability / DOI / artifact paths | OpenAI E4/E5/M6, Gemini E1 | OUT-OF-SCOPE (mints at submission, by design) |
| Abstract σ-juxtaposition qualifiers | Grok E1/E4, OpenAI E8/E11/E12 | STALE (already in abstract `:348`) |
| Look-elsewhere "inconsistency" | OpenAI E1 | STALE/MISLABELED (reconciled `:444`,`:906`) |
| Split/augmentation arithmetic | OpenAI E9/M8 | MISLABELED (reviewer math error; exact 80/20) |
| Fig colorbar A_p mismatch | Grok M2 | OPINION/STALE (convention disclosed) |
| Label-noise / leakage budgets | Grok M3/M4, OpenAI M4 | STALE (both present) |
| Structure / length / placement | Gemini M1, OpenAI M7 | OPINION |
| All MINOR / NIT / typography | all | OPINION / polish-tier |
| Perplexity | — | N/A (API failure) |

**VERIFIED-OPEN findings: 0.**

Every essential/major vendor finding is stale (already closed in R39conf/EXT5), mislabeled (reviewer arithmetic/rasterization error), out-of-scope (submission-time DOI/date hygiene that resolves downstream of arXiv freeze), or opinion (editorial structure/polish). The Claude 5th leg ACCEPT and OpenAI's own passed-arithmetic block corroborate every headline number. The paper's FROZEN, universally-accepted status holds.

**Recommendation: ACCEPT — frozen, no closures.** The only non-content action is the standing submission-time step (mint Zenodo DOI, stamp submission date), which is performed at arXiv/journal submission, not as an R40 closure.
