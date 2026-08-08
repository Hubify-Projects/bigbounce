# R52 — P4 Peer-Review Truth-Audit (Opus judgment leg)

**Paper:** P4 — "Survey-Scale Galaxy Chirality with Equivariant TTA…" v1.0.188
**Canonical PDF:** `pipelines/p2_chirality/chirality_catalog_paper.pdf` (md5 `c47abc18…`, 23 pp)
**Source verified:** `pipelines/p2_chirality/chirality_catalog_paper.tex` — `\paperVersion{v1.0.188}`, `\date{June 13, 2026}`; md5 + version match the canonical PDF. (`arxiv/paper4_chirality_catalog.tex` is a 1.8 KB stub — NOT the canonical source.)
**Auditor:** Opus director, extra-rigor anti-fabrication gate.

---

## 0. NET VERDICT

**P4 HOLDS at ACCEPT.** The science does not regress. Both harsh verdicts are
**FALSE POSITIVES** at the recommendation level, but each surfaced a handful of
**genuine MINOR presentation/consistency defects** worth a polish pass.

- **OpenAI `gpt-5-2025-08-07`** — the report's actual summary recommendation is
  **"MAJOR REVISIONS,"** *not* REJECT. (The dispatch tag that reached the
  orchestrator as "REJECT" is harsher than the report text. Flagging the
  dispatch-vs-report mismatch.) Its verdict rests on **zero** load-bearing
  problems: every "ESSENTIAL/MAJOR" is a presentation inconsistency on a
  *secondary diagnostic*, an editorial house-style item, or a submission-logistics
  item. **Decisive evidence it is a false positive:** o3's own
  "Arithmetic and dimensional checks" section (report lines 95–106) independently
  recomputed *every* load-bearing scalar — catalog counts, real-space dipole,
  MASTER ℓ=1 z, block-bootstrap WLS z, Fisher floor, monopole leakage — and
  confirmed each "correct" / "matches." o3 itself verified the science holds; its
  downgrade is built entirely on editorial/logistics nits tiered too high.

- **Grok `grok-4.3`** (77 s, rasterized images) — **MAJOR**, false positive. Both
  its "ESSENTIAL" findings are **FALSIFIED against the abstract text**.
  **Decisive evidence:** Grok-E2 claims the abstract juxtaposes +0.41σ and z=0.70
  "without repeating the [comparability] warning," but abstract line 348 contains
  it verbatim: *"Note: the +0.41σ (isotropic-bootstrap null) and z=0.70 (per-galaxy
  label-shuffle null) … are not directly comparable as detection significances."*

- **Claude ACCEPT** and **Gemini ACCEPT-with-minors** are well-calibrated and
  consistent with this audit.

**KEY QUESTION (does any REJECT reason rest on a VERIFIED load-bearing problem —
unsupported central claim / missing critical control / non-reproducibility?):
NO.** All three primary claims survive truth-audit against committed artifacts:
1. Primary null real-space dipole **+0.41σ** (HC, N=949,584) — 4 independent
   nulls/implementations + 2×3 robustness panel; reproducible from
   `run_dipole_catalog_c.py` + `c11b/c12` artifacts (tex line 605). o3 recomputed,
   confirmed (report line 100).
2. **WLS exclusion of a clean 1.7% dipole at z≈−18** — naive z=−264 explicitly
   superseded by NSIDE=8 block-bootstrap (σ×14.7), block-scale sweep
   {4,8,16}→z=−16.9/−18.4/−19.4 (tex line 938). o3 confirmed (report line 104).
3. **+3.64σ/+7.28σ MASTER residual** — explicitly declared NON-primary,
   systematics-attributed, backed by the eight-anchor Appendix-D battery
   (tex lines 694–696).

---

## 1. FINDINGS LEDGER (deduped across o3 / Grok / Claude / Gemini)

Tiers below are the **audited** tiers, not the reviewer's claimed tier.

### VERIFIED — real text defects, all MINOR, none load-bearing, all DO-NOW

| # | Source | Finding | Evidence | Tier | Disposition |
|---|--------|---------|----------|------|-------------|
| V1 | o3-E1 | Hemisphere LEE prose contradicts Table I + App C. Body §III.B bullet (v) (tex **436**) says "3.05σ … **<1σ after look-elsewhere correction**"; but Table I caption (**444**) + row (**453**) report the *principled* control as **p_LEE≤10⁻⁴**, and App C (**906**) explicitly **demotes the Bonferroni <1σ to "qualitative cross-check only."** Line 436 quotes the demoted heuristic as THE corrected significance. | tex 436 vs 444/453/906 | MINOR (consistency) | **DO-NOW** — secondary diagnostic; systematics-attributed under *both* readings; primary result untouched. |
| V2 | o3-M1 | Table II row B `0.504±0.0003` cannot reproduce the listed `Dev +14.6σ` (naive 0.004/0.0003=13.3σ). The Dev is **correct** for the true σ≈2.74×10⁻⁴ (0.004/2.74e-4=14.6σ); the *displayed* σ is rounded to 1 sig-fig. Rows A & C use trailing-digit form `0.507879(274)`; row B uniquely uses the coarse form. | tex 580 (caption: "Dev from unrounded fraction"), 585–587 | MINOR (display/reproducibility) | **DO-NOW** — render B as `0.50400(27)`. Not a numerical error; monopole is a declared classifier artifact. |
| V3 | o3-M8 | "isotropic-**bootstrap** null" is a misnomer (it's a per-pixel **permutation**, tex 605) and is internally inconsistent ("isotropic **permutation** null," tex 721; "pixel-permutation"). | tex 348/Table I vs 605/721 | MINOR (terminology) | **DO-NOW** — rename to "isotropic (pixel-)permutation null" in abstract + Table I. |
| V4 | o3-E2/M5 | Version/review-process narration in body: "was declared in **early versions** … predates the provenance audit" (**433**); "computed **post-R29**" (**938** fn); "An **earlier version** of this paragraph overstated…" (**1000**); "Repository state for this version: commit `53b41d12` (**v1.0.185 lineage**)" (**1005**). 25 `\artifact{…json}` path macros + inline `\texttt{…json}`. | tex 433, 938, 1000, 1005; grep | MINOR (editorial house-style) | **DO-NOW** for the process/version prose (neutralize). Artifact paths are reproducibility-positive (lab convention) — *optional* consolidation, not required. |
| V5 | o3-M2 | Training accounting: "80/20 split: ntrain=21,293, nval=5,323" implies 79.4/20.6, and "826-image difference … from flip augmentation" is unexplained (why only 826 of ~20k augmented?). | tex §II.B | MINOR (clarity) | **DO-NOW** — state actual split fraction + augmentation policy. Classifier validated independently via GZ1 cross-match; not load-bearing. |
| V6 | o3-M9 | Catalog-A "+6.48σ pre-MASTER" lacks the estimator/null provenance (type, N_real, seed) that every other ℓ=1 number carries. | tex 605/619/721/798 | MINOR (provenance) | **DO-NOW** — one footnote pinning the null. It's a *spurious* artifact that collapses; not load-bearing. |
| V7 | o3-E4 | Fig 8 caption (tex **661–674**) labels a **pre-MASTER** pseudo-Cℓ panel (annotated σ_{ℓ=1}=+3.63, 200-MC) then states "the **post-MASTER** canonical-mask residual is +3.64σ." Near-identical numbers, different estimators, one caption → conflation risk. | tex 661–674 | MINOR (caption clarity; o3 over-tiered as ESSENTIAL) | **DO-NOW** — add "(distinct estimator from the panel)" to the post-MASTER sentence. |
| V8 | o3-M7 | App-E edge-on claim "Neff reduction ∼10–15%" not derivable from the supplied numbers (gives 65.7% label rate for b/a<0.3 but not the b/a<0.3 *fraction* of the catalog). | report line 141–143 (App E) | MINOR (support gap) | **DO-NOW** — give the b/a<0.3 fraction or soften to qualitative. Non-load-bearing sensitivity aside. |

### OUT-OF-SCOPE / TRULY-BLOCKED

| # | Source | Finding | Disposition |
|---|--------|---------|-------------|
| B1 | o3-E3 | "A persistent archival DOI … has **not yet been minted**" (tex 1010). | **OUT-OF-SCOPE / TRULY-BLOCKED** — submission logistics. PRD requires the DOI at *acceptance*, not at referee stage; paper honestly states the release tag is the current citable handle and Zenodo deposit happens at journal submission (tex 1005). Mint at arXiv/journal submission. Not a scientific defect. |

### FALSIFIED / OPINION — no action required

| Source | Finding | Verdict & evidence |
|--------|---------|--------------------|
| Grok-E1 | Abstract catalog size 8,474,531 is "post-QA without qualifier." | **FALSIFIED-as-defect** — 8,474,531 *is* the actual released catalog size; the 157-galaxy QA cut (0.0019% of 8,474,688) is disclosed in body (tex 520). The number is correct. Optional nitpick only. |
| Grok-E2 | Abstract juxtaposes +0.41σ & z=0.70 without the comparability warning. | **FALSIFIED** — warning present verbatim, tex 348. |
| Grok-M2 | No effect-size next to +3.64σ. | **FALSIFIED/largely-addressed** — abstract gives "+3.64σ, ≈1.9σ Gaussian-equiv" + 99.32% reproduction; headline σ's carry amplitudes. |
| Grok-M3 | A50≈0.75% threshold validity under the actual depth mask. | **FALSIFIED/addressed** — injection-recovery runs on the canonical mask with per-pixel binomial nulls reflecting actual depth (tex 605, 801). Optional cross-ref. |
| Grok-M1 / o3-M6 | 23 pp too long for a null result. | **OPINION** — catalog-class extensiveness + 8-anchor battery; explicitly not-a-defect. Claude & Gemini call the thoroughness a strength. |
| o3-M3 | Null-procedure glossary. | **OPINION/editorial** — paper already labels each null per-row. Optional. |
| o3-M4 | One canonical post-MASTER number. | **OPINION/addressed** — primary estimators declared (real-space +0.41σ + WLS z≈−18); notation §(tex 426) + Table III caption (633) already state harmonic numbers are "not mutually comparable." |
| o3-N1…N10, Grok-N1/N2, Gemini-N1…N5, Claude-3.1…3.5 | Polish nits. | **MINOR/OPINION** — several already handled (sigma-comparability caveats, (k+1)/(N+1) for Table III at tex 633). Gemini-N2 (placeholder future "Dated: June 13, 2026") and Gemini-N1 ("sensitivity"→"excess" in abstract) are cheap real polish; fold into the same pass. |

---

## 2. CLOSURE PLAN

**Net: P4 stays ACCEPT. No BLOCKER, no science-MAJOR, no regression.** A single
optional **polish wave** closes 8 VERIFIED MINOR text fixes + a few free Gemini/Claude
nits. None touches a result, an artifact, or a number's *value* (V2 changes only the
*displayed precision*). All DO-NOW; one TRULY-BLOCKED logistics item (DOI) deferred to
submission.

Exact edits (all in `pipelines/p2_chirality/chirality_catalog_paper.tex`):

1. **V1 (line 436):** replace "`<1σ after look-elsewhere correction`" with
   "`p_LEE≤10⁻⁴ direct-MC max-statistic, systematics-attributed (the Gaussian-Bonferroni <1σ heuristic is a non-principled cross-check); App. C`" — matches Table I row (v) + App C.
2. **V2 (line 586):** `B (calibrated) & 0.50400(27) & +0.4 & +14.6` (match A/C trailing-digit form).
3. **V3 (lines 348, 451/Table I, any "isotropic-bootstrap"):** → "isotropic (pixel-)permutation null" (4 occurrences).
4. **V4 (lines 433, 938 fn, 1000, 1005):** neutralize "early versions / predates the provenance audit / post-R29 / earlier version overstated / v1.0.185 lineage" to result-only phrasing. (Artifact `\artifact{}` paths: leave — lab reproducibility convention.)
5. **V5 (§II.B):** state actual split fraction (≈79.4/20.6) + which subset was flip-augmented and why.
6. **V6 (footnote near line 605/619):** pin the +6.48σ pre-MASTER null (type, N, seed).
7. **V7 (lines 669–671):** append "(distinct estimator from the panel's pre-MASTER pseudo-Cℓ)".
8. **V8 (App E):** give the b/a<0.3 catalog fraction or recast 10–15% Neff as qualitative.
9. **Free nits:** Gemini-N1 abstract "sensitivity"→"excess"; Gemini-N2 fix the future placeholder date at restamp; Gemini-N4 put "—" in blank Table X z-cells.
10. **B1 (DOI):** TRULY-BLOCKED — mint Zenodo DOI at journal submission; update tex 1005/1010 then.

**Recommended routing:** this is a well-specified checklist → Sonnet closure pass +
`/latex-audit` + `/bigbounce-version-bump` (patch). Opus not required for execution.
Add the R52 timeline entry per the standing site-sync directive in the same bundle.
