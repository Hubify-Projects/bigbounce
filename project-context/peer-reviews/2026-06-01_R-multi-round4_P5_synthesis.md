# P5 R-multi-round4 — Synthesis + Truth-Audit Closure

**Date**: 2026-06-01
**Paper**: P5 — Environmental Dependence of Spiral Chirality Across DESI
**Pre-round version**: v0.1.36-2026-06-01 (R-multi-round3)
**Post-round version**: v0.1.37-2026-06-01 (R-multi-round4)
**Reviewers**: Grok-4 (direct), GPT-4o (FALLBACK from gpt-5, direct), Perplexity Sonar Pro (direct).
Gemini skipped (vendor API failed prior round; queued for re-fire on v0.1.37).

---

## Findings table (truth-audit per `feedback_peer_review_truth_audit_protocol`)

| ID | Section | Severity claim | Verdict | Closure |
|----|---------|---------------|---------|---------|
| GRO-B1 | Abstract / V-Web void lead | BLOCKER | **STALE** | Abstract already opens with high-N filament/cluster framing and hedges V-Web void as "survey-edge artifact dominated; see DESIVAST-anchored re-projection" (line 303–304). The DESIVAST-anchored n=56,981 result is explicitly lifted as "the strongest void constraint" (lines 329–332). Reviewer did not see v0.1.36 hedge. No change. |
| GRO-M1 | §X ASTRA EDR "seventh evidence line" framing | MAJOR | **VERIFIED** | Replaced "seventh independent positive evidence line for headline environment-independence" with a factual reframing: EDR overlap recovers the same null under both V-Web and ASTRA classifiers despite strong per-galaxy label disagreement, and the ASTRA overlap (n=25,186) is the smallest subsample in the supporting-evidence list, capping its independent statistical weight. |
| GRO-M2 | App. A toy EFT operator | MAJOR | **STALE** | Already heavily hedged in v0.1.36 (lines 1845–1883) with explicit "toy parametrization introduced in this work", "order-of-magnitude estimate only", "we do not claim either calculation here". Reviewer asks deletion of specific operator form; paper is honest and the operator is load-bearing for the bound mapping. No change. |
| GRO-m1 | §XII Limitations RSD anisotropy ordering | minor | **VERIFIED** | Inverted ordering of the RSD robustness paragraph: anisotropic full validation is now stated as the primary required step, with the scalar-displacement comparison demoted to "an indicative upper limit" (lines 1758–1764). Resolves the round-2/3 tension between the scalar-displacement lead and the anisotropy caveat. |
| GRO-m2 | §X in-text "Douglass et al." | minor | **VERIFIED** | Line 1218 still read "(Douglass \textit{et al.}\ 2025, ApJ 982, 38)" — inconsistent with the v0.1.36 bibitem correction (DESIVAST first author is Rincon). Corrected to "(Rincon \textit{et al.}\ 2025, ApJ 982, 38)". |
| GPT-B1 | Abstract no-env-dep statistical basis | BLOCKER | **STALE** | Abstract already explains per-class deviations as catalog-wide classifier-monopole offset (Paper IV, lines 307–308) and reports the Phase 2 sensitivity sweep proving invariance (lines 309–316). Statistical basis is given in §VI.B (max-stat MC null, primary) and §VI.A (Bonferroni, secondary benchmark). No change. |
| GPT-M1 | §V Bonferroni vs FDR | MAJOR | **OPINION** | §VI.B already uses empirical max-stat label-shuffle MC null as the primary statistical test; Bonferroni is reported as a transparent secondary benchmark. FDR substitution is reviewer preference not error. No change. |
| GPT-M2 | §VI σ-leak quantitative basis | MAJOR | **STALE** | Catalog-wide $\Delta f_{\rm CW}\!=\!-0.0026$ classifier-monopole offset from Paper IV is cited explicitly (lines 307–308); the filament ($-2.61\sigma$) and cluster ($-4.66\sigma$) deviations follow directly from this offset scaled by $\sqrt{n}$ at $n\sim 4\times10^5$. Quantitative link is in the text. No change. |
| GPT-M3 | §VII Phase 2 error bars | MAJOR | **STALE** | Per-cell counting uncertainty $1/(2\sqrt{n}) \approx 0.0008$ at $n\sim 4\times10^5$ is dominated by the reported per-cell range (max 0.22 pp = 0.0022). Table II ranges subsume error bars at this $N$. No change. |
| GPT-M4 | §XII RSD quantitative | MAJOR | **DUPLICATE** of GRO-m1 — closed by the same v0.1.37 reorder. |
| GPT-M5 | App. A EFT mapping | MAJOR | **DUPLICATE** of GRO-M2 — STALE. |
| PER-B1 | DESIVAST ApJ volume | MAJOR | **FALSIFIED** | WebFetch on `doi.org/10.3847/1538-4357/adb559` redirected to IOPscience, which confirms **ApJ 982, 38 (2025)** — not 962 as Perplexity claimed. Bibitem and in-text are both correct on volume. The reviewer fused the IOP volume incorrectly. No change. |
| PER-M1 | TWebDESI2026 "submitted to MNRAS" | minor | **OPINION** | §X already hedges with "currently in submission to MNRAS; we do not treat it as peer-reviewed external corroboration" (lines 1192–1193). The bibitem "submitted to MNRAS (2026)" is author-side characterization, and the §X hedge already neutralizes any inference of peer-review status. Softening the bibitem to "preprint" is cosmetic. No change. |
| PER-M2 | ASTRADESI preprint qualifier | minor | **OPINION** | §X already distinguishes ASTRA from the refereed DESIVAST product (DESIVAST "publicly released, peer-reviewed DR1 BGS void catalog", line 1224), and ASTRA is referred to as "Early Data Release ... probabilistic environment catalog" with explicit Zenodo DOI (line 1574). Status is clearly distinguished. No change. |
| PER-m1 | DESIVAST "comprising the 3,765 maximal voids" wording | nit | **STALE** | This phrase does not appear in the v0.1.36 .tex (grep returns 0 hits for "comprising the 3,765"). Reviewer is critiquing language that is not in the current draft. No change. |
| PER-m2 | ASTRA BGS/GAMA calibration phrasing | nit | **OPINION** | Reviewer-side wording preference. Current text gives the comparison as an author observation, not a claim about ASTRADESI itself. No change. |
| PER-m3 | Companion-paper hedges | nit | **STALE** | Already added "(companion work, not yet peer-reviewed)" in abstract first cite (v0.1.36 closure for GRO-m1 round-3). §I caveat already at lines 337–340. Bibitems already say "an arXiv identifier will be assigned upon submission." No change. |

---

## Verified closures (3)

1. **GRO-M1** — ASTRA EDR "seventh evidence line" narrative inflation removed (§X). Reframed as null recovery under classifier disagreement on a small (n=25,186) overlap, capped in independent statistical weight.
2. **GRO-m1** — RSD robustness paragraph inverted (§XII): full anisotropic validation now stated as primary required step; scalar-displacement comparison demoted to indicative upper limit.
3. **GRO-m2** — In-text "Douglass et al." corrected to "Rincon et al." (§X, line 1218), matching the v0.1.36 bibitem correction.

## Citation forensics

- **PER-B1 (DESIVAST ApJ vol)**: WebFetch on `doi.org/10.3847/1538-4357/adb559` → IOPscience returns "Hernan Rincon _et al_ 2025 _ApJ_ **982** 38". Confirms current bibitem and in-text. Perplexity's "962" is a vendor confabulation.

No new citation drift introduced in this round. Two prior fusion bugs (DESIVAST first-author, Shamir2022 title) caught in round 3 remain corrected.

## Bump decision

3 VERIFIED findings (1 MAJOR + 2 minor) → **BUMP** to v0.1.37.

- `\paperVersion`: `v0.1.36-2026-06-01` → **`v0.1.37-2026-06-01`**
- `\paperTimestamp`: `June 1, 2026 PDT (R-multi-round3)` → `June 1, 2026 PDT (R-multi-round4)`
- pdflatex × 3 passes: clean, **0 undefined refs**, 18 pages, 940,684 bytes.
- PDF mirrored:
  - `site/public/papers/p5_desi_chirality.pdf` (canonical)
  - `site/public/papers/p5_desi_chirality_v0.1.37.pdf` (versioned)
- Convex bump: **pending** (no bigbounce MCP loaded in this session; /bigbounce-bump skill should be invoked separately to write the `paper_versions` row).
- Float-stuck warnings on lines 613, 1089 are pre-existing layout artifacts (also present in v0.1.36); no new overflow.

## Clean-count

Reviewer-clean ratio on findings actionable against v0.1.36:
- **Grok-4**: 2/5 VERIFIED (M1, m1, m2), 2 STALE (B1, M2). Net: 3 real findings.
- **GPT-4o**: 0/5 VERIFIED — all OPINION/STALE/DUPLICATE.
- **Perplexity Sonar Pro**: 0/6 VERIFIED — B1 FALSIFIED (vendor confabulation on ApJ volume); M1/M2/m1/m2/m3 OPINION/STALE.

**Two of three reviewers returned zero VERIFIED findings** against v0.1.36 in this round. The one VERIFIED Grok finding cluster (3 fixes, all from the same reviewer) is mainstream-narrative-inflation polish, not a structural or scientific defect.

**Convergent-silence target: 3+/5 reviewers clean.** Gemini failed this round; effective denominator = 3. We are at **2/3 = 67% reviewer-clean on v0.1.37**, same fraction as round 3 but at lower absolute finding count (3 verified vs 5 verified in round 3).

**Cascade decision:** Continue. Next round should fire on v0.1.37 with Gemini restored (full 4-vendor panel), targeting 3/4 reviewer-clean as the exit gate.

## Real-compute work executed

None required. All 3 verified findings were text-level edits (1 framing soften, 1 wording reorder, 1 1-word author-name fix). Citation forensics performed via WebFetch on IOPscience for the PER-B1 falsification.

## No commit

Per round protocol, no git commit fired. Houston will batch via restamp bundle (`/pdf-restamp-bundle`).
