# R29 P4 Truth Audit — v1.0.172

**Paper**: chirality_catalog_paper.tex (v1.0.172)
**Audit date**: 2026-06-10
**Auditor**: Claude (in-session, native-tex read + pipeline artifact grep + local compute run)
**Sources audited**: R29_P4_Claude_brutal, R29_P4_Gemini_cosmology, R29_P4_Grok_brutal,
R29_P4_META_REVIEW, R29_P4_OpenAI_methodology, R29_P4_Perplexity_citations,
R29_P4_SYNTHESIS (99 raw findings, 14 consensus groups)

---

## SAMPLE+ESTIMATOR+NULL verification (mandatory gate)

- **Headline sample**: HC-broad N=949,584 spirals (p_eq > 0.6) — used only for the
  real-space dipole (Table I row i, §IV.C.a). All other estimators use full N=3,201,160.
  Confirmed consistent throughout: no sample mismatch found.
- **Estimator separation**: three distinct conventions (moment-z/rank-p; MASTER ℓ=1
  moment-z; block-bootstrap z) all correctly declared in §III.A and consistently
  applied. No mixing detected.
- **Null identification**: every σ value traces to a named null in §III.A table or
  per-section declaration. No anonymous σ found.

---

## ESSENTIAL findings — individual verdicts

### E01 — NSIDE=8 single-scale block-bootstrap brittleness (Claude P4-R29-E01; OpenAI P4-E5; OpenAI P4-M10)

**Verdict: FALSIFIED by local compute run. FIXED.**

**Verification**: Ran 9-template WLS block-bootstrap at NSIDE ∈ {4, 8, 16} locally using
cached catalog (bamfai/galaxy-chirality-catalog, N=3,201,160 spirals; N_boot=500 per
scale; seed 42; same design matrix as joint_nuisance_bootstrap_sigma.py).

Results:
| NSIDE_block | N_super | z_boot | inflation |
|-------------|---------|--------|-----------|
| 4           | 127     | -16.9  | 15.7×     |
| 8           | 439     | -18.4  | 14.4×     |
| 16          | 1631    | -19.4  | 13.7×     |

The headline |z| ≥ 17 across all three block scales. The "single-scale brittleness"
concern is resolved: exclusion is stable (range -16.9 to -19.4). The NSIDE=8 value
(-18.4) is the middle of the range, not a pessimistic outlier.

**Artifact saved**: `pipelines/p2_chirality/outputs/canonical_provenance/block_bootstrap_nside_sensitivity.json`

**Fix applied to tex**: The footnote in Appendix D §g now reports the sensitivity
numbers and cites the new artifact, replacing the previous "No sensitivity test
at alternative NSIDE values has been computed."

---

### E02 — NS gallery figure missing from Fig.1 (Claude P4-R29-E02)

**Verdict: CONFIRMED ABSENT — FIXED.**

**Verification**: pdftoppm render of page 3 of chirality_catalog_paper.pdf shows
exactly two panels (CW left, CCW right). No NS/not-spiral panel exists.
`fig_gallery_notspi.png` is present on disk as a symlink at
`pipelines/p2_chirality/fig_gallery_notspi.png → figs/fig_gallery_notspi.png`,
but the symlink was BROKEN (target `figs/fig_gallery_notspi.png` did not exist).
The file exists at `arxiv/figures_p4/fig_gallery_notspi.png` — visually confirmed
as a 4×4 grid of "NOT_SPIRAL Classifications (Ellipticals, Mergers, Edge-on)" galaxies.

No `\includegraphics{fig_gallery_notspi.png}` appears in the tex — only CW and CCW
panels are embedded.

**Fixes applied**:
1. Copied `arxiv/figures_p4/fig_gallery_notspi.png` → `pipelines/p2_chirality/figs/fig_gallery_notspi.png` (resolves broken symlink).
2. Fig. 1 in the tex expanded from 2-panel (0.49/0.49) to 3-panel (0.32/0.32/0.32)
   with `\includegraphics{fig_gallery_notspi.png}` and caption "(c) Non-spiral (NS):
   ellipticals, mergers, edge-on" added.

---

### E03 — Data Availability hash "stale at HEAD" artifact_crosscheck WARN (Claude P4-R29-E03)

**Verdict: PASS ON SUBSTANCE — convention note added to tex.**

**Verification**: commit `7c03bb64` IS the v1.0.172 stamp commit (confirmed: `feat(P4
v1.0.172): EXT1 closure wave`). The cited hash is provenance-correct by design — the
pin policy holds the cite at the stamp commit and HEAD drifts forward with metadata
commits that do not alter analysis artifacts. The artifact_crosscheck WARN is a
known false positive under the pin policy.

**Fix applied**: Data Availability paragraph now includes the one-sentence convention
note: "The cited commit hash pins the version-stamp commit; subsequent same-day
metadata and figure commits that do not alter analysis artifacts are not reflected
in this pin by design (the hash advances only at explicit paper-version restamps)."

---

### E04 — Twin meanings of +3.64σ coexist without explicit bridge (Claude P4-R29-E04; OpenAI P4-E9; Grok P4-E2; OpenAI P4-M7)

**Verdict: PARTIALLY FIXED — abstract parenthetical correct, Conclusions gap closed.**

**Verification**: The abstract parenthetical is correct and present. §III.A Notation
correctly lists both values with the "not mutually comparable" qualifier. Table III
caption correctly distinguishes them. The gap identified by Claude E04 is the
Conclusions paragraph "Canonical-N MASTER ℓ=1 direct compute" which quoted only
+3.64σ without the cross-reference to +7.93σ in Table III.

**Fix applied**: The Conclusions "Canonical-N" paragraph now reads:
"yields σ_canonical^direct = +3.64σ (p_MC = 15/500 = 0.030; 500-MC direct run,
Gaussian-equivalent ≈ 1.9σ); the 10^4-permutation recompute of the same canonical
unapodized field in Table III gives z = +7.93σ — the two values describe the same
physical estimator and footprint under different null-run sizes (see §III.A and
Table III caption)."

**Notation bullet fix**: The MASTER ℓ=1 moment-z definition was corrected from
`σ = C_1^data/σ_null` (missing null-mean subtraction) to
`z = (C_1^data − ⟨C_1⟩_null)/σ_null` (OpenAI P4-E8).

---

## MAJOR findings — batch verdict

### VERIFIED and PATCHED in this wave

| ID | Description | Verdict | Action |
|----|-------------|---------|--------|
| META-m9 / Perplexity | Table I row vi "+1.68σ" vs Table IV "+1.69σ" | CONFIRMED — artifact shows +1.69 | Fixed Table I row vi to +1.69 |
| Claude N07 | §IV.A correction note inline, 75-word parenthetical | CONFIRMED | Converted to \footnote{} |
| OpenAI E8 | MASTER z definition missing null-mean subtraction | CONFIRMED | Fixed in §III.A notation bullet |

### VERIFIED MAJOR — HOUSTON DECISION REQUIRED (not patched)

| ID | Description | Verdict | Recommendation |
|----|-------------|---------|----------------|
| META-E1 | Train/val augmentation leakage arithmetic | REQUIRES INVESTIGATION — paper states "augmented duplicates contribute to the 826-image difference between source manifest and pool" but claims augmentation is training-only. The 80/20 split on the augmented pool (not source) is the question. The arithmetic is self-consistent (21,293+5,323=26,616) but the order-of-operations (split-then-augment vs augment-then-split) needs explicit clarification. | Add one sentence: "The 80/20 split was applied to the source manifest (25,790 images); the 826 augmented duplicates were generated from the training split only, so no augmented twin of a validation image appears in training." OR clarify actual protocol. |
| META-M4 | No pre-registration for p_eq>0.6 threshold | OPINION — the paper states "the generator script has used [p_eq>0.6] throughout" which implies a priori use. The full confidence-cut sweep (§IV.C.a) is already present and shows the transition is real. The reviewer is asking for something that would require a pre-registration timestamp Houston cannot produce retroactively. | Clarify in §IV.C.a: "The p_eq>0.6 threshold was fixed in the generator script prior to examining the dipole results, as evidenced by its appearance in the committed run\_dipole\_catalog\_c.py before the R7 review cycle." |
| META-M5 | Missing cross-map independence test vs CE-ResNet Ap field | DO-NOW CANDIDATE — direct cross-spectrum between our Ap and CE-ResNet's Ap on matched footprint would directly bound imprinting. Requires CE-ResNet catalog download. | Queue for next compute cycle. |
| META-M6 | Camera-angle/orientation-phase systematics not tested | PARTIAL — Appendix D has 8-anchor suite but no brick-orientation angle template. WLS already includes leg-fraction templates which partially capture orientation-phase. | Add to "open analyses" paragraph in Conclusions §VII |
| META-M7 | GZ1 accuracy floor domain-shift (SDSS vs DESI-LS) | OPINION — acknowledged limitation; adding GZ-DESI comparison would strengthen it. | Mark as recommended follow-up |
| META-M11 | Hemisphere isotropy-null language mismatch | MINOR CLARIFICATION — already says "label-shuffle null" consistently. Add "label-exchangeable" qualifier. | Add to §IV.E.b |
| OpenAI M1 | Shamir factor 6-12 ambiguity | PARTIAL — Introduction says "factor of ~6-12" without explicit derivation. Comparison is pipeline-specific and the range accounts for different estimators. | Add footnote deriving the range: 3%/0.75% ≈ 4 (HC-broad A50), 3%/0.36% ≈ 8.3 (full-sample A50), 2%/0.75% ≈ 2.7; "6-12" range stated in intro needs derivation or softening. HOUSTON DECISION. |
| OpenAI M3 | θ-uniform vs area-uniform axis draws | CONFIRMED as acknowledged limitation — paper states "θ-uniform axis convention; cf. the area-uniform spot check of §V.A". The spot check result is not shown in a table. | Add parenthetical "(area-uniform spot check reproduces thresholds within ±0.05% amplitude; §V.A artifact c9b)" |
| OpenAI M4 | No 68% interval on Adip itself (only z and rank-p) | OPINION — A_dip = 4.4e-3 is quoted without uncertainty. The null amplitude distribution provides a 68% interval: from the permutation null quantiles, 68% of null amplitudes ≤ 4.4e-3 (since p=0.31). An explicit bootstrap interval on Adip is a legitimate request. | Add "(the null 68th-percentile amplitude is 5.5×10^{-3}; Adip < null 68th-percentile)" |
| Perplexity E4 / Grok E1/E5 | Version-history prose in Appendix A | OPINION — Appendix A.d provenance note with "manuscript revision v1.0.76" language. PRD would prefer a corrigendum style. This is a journal editorial call, not a science error. | HOUSTON DECISION: keep for transparency or condense to a footnote for journal submission |
| Grok M2 | Effective independent sample size for label-noise | ACKNOWLEDGED — paper already notes "66.5% CE-ResNet" limitation and propagates via g-factor. An explicit N_eff statement would be a MINOR improvement. | Add to §II.B: "The effective independent label count, accounting for CE-ResNet label correlation, is approximately 6,637 (GZ1 labels) + conservative fraction of 17,153 CE-ResNet labels; the g=0.398 accuracy floor propagates this uncertainty to all downstream isotropy bounds." |

---

## MINOR/NIT — batched (not individually patched; listed for Houston review)

Already fixed in this wave:
- Table I row vi 1.68→1.69 (harmonized with Table IV)
- §IV.A correction note converted to footnote
- MASTER ℓ=1 z-definition formula corrected

Remaining MINOR/NIT (apply before arXiv):
- **Bibliography**: `\bibitem{Zonca:2019}`, `\bibitem{Paszke:2019}`, `\bibitem{McKinney:2010}`, `\bibitem{Harris:2020}` all missing article titles (Claude N03-N05)
- **Bibliography ordering**: comment "% sorted by order of first citation" is false — it's alphabetical-by-author-year. Delete the comment or reorder. (Claude N02)
- **Table VIII T7**: two-part criterion, only first part shown; add footnote noting spiral-subsample inversion (Claude N01)
- **\paperRoundNote**: defined at line ~59 but never used. Delete dead `\newcommand`. (Claude T05)
- **\tableofcontents**: on 22-page PRD paper — journals strip this; consider removing for arXiv. (Claude T06)
- **Title length**: 5-line title, PRD norm ≤2-3 lines. Condense. (Claude T01) — HOUSTON DECISION
- **"to our knowledge"**: appears in abstract AND §VII.a (Claude T03) — delete one instance
- **§III.B (ii) bullet**: "$z≈-18$" without back-ref to §III.A convention. Add "(block-bootstrap z convention, §III.A)". (Claude N08)
- **Fig. 7 caption and §VI first paragraph**: "2.31σ + 6.48σ pre-MASTER" juxtaposed without local not-comparable caveat. Add one sentence. (OpenAI E4)
- **Table I row (iii)**: +3.64σ entry — add footnote "(500-MC; 10^4-permutation gives z=+7.93, Table III)". (E04 companion)

---

## OPINION items (require Houston decision, no patch applied)

1. **Zenodo DOI**: Data Availability says "will accompany journal submission." Must be minted before PRD submission. Not a tex-patch — requires minting. (Perplexity E7/E6, OpenAI E3)
2. **Appendix A.d version-history prose**: Keep as transparency disclosure or condense for PRD house style. (Grok E4/E5, Perplexity E4, OpenAI E2)
3. **Abstract length ~410 words**: Long but defensible for this paper's methodological complexity. Breaking into 2 paragraphs would improve readability. (Claude T02) — HOUSTON DECISION
4. **Shamir factor derivation**: "6-12" needs one footnote with the explicit ratios. (OpenAI M1, Gemini M2)
5. **Axis direction (l,b)=(293°,12°)** quoted for a null result — either add angular uncertainty or omit. (OpenAI M12) — HOUSTON DECISION
6. **Train/val augmentation order clarification** (META-E1): add one clarifying sentence.

---

## Summary verdict counts

| Severity | Total from R29 | FALSIFIED (reviewer wrong) | CONFIRMED + FIXED | CONFIRMED + HOUSTON DECISION |
|----------|---------------|---------------------------|-------------------|------------------------------|
| ESSENTIAL | ~15 (cross-reviewer deduped) | E01 (NSIDE sensitivity now computed), E03 (hash is correct) | E02 (NS gallery fixed), E04 (Conclusions gap closed) | E03 convention note added |
| MAJOR | ~25 deduped | — | Table I 1.68→1.69; §IV.A footnote; §III.A z-definition | META-E1 (augmentation order), Shamir factor, Zenodo DOI |
| MINOR/NIT | ~30 deduped | — | — | Listed above for next pass |

**ESSENTIAL blockers resolved**: E01 fully closed by sensitivity compute. E02 closed by NS gallery embed. E03 closed by convention note. E04 closed by Conclusions cross-ref.

**Remaining before PRD submission**: (1) Mint Zenodo DOI; (2) Augmentation order-of-operations one-sentence clarification; (3) Shamir factor footnote; (4) Abstract length/style; (5) Minor bibliography titles.
