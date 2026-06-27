# R57 P5 — Hardened De-Biased Truth Audit

**Paper:** P5 (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`)
**Round:** R57 hardened de-biased re-review
**PDF:** `/tmp/R57_P5/p5_desi_chirality.pdf` md5=034b7bc0 (pre-fix), 33 pages
**Engine:** `tools/v3_native_pdf_review.py` — 3/4 vendors OK (Gemini 2.5 Pro,
Grok 4.3, GPT-5) + own Opus read. Anthropic not in engine; Perplexity quota-failed.
**Standard:** PRD/MNRAS hardened — internal-inconsistency / self-favoring /
unstated-assumption = MINOR-min; patterns 061-064 + calibration filter for
genuine false-positives only. NEVER fabricate / close-without-verdict.

## Net verdict
Converged with **2 residual VERIFIED MINOR internal-inconsistencies**, both
corroborated by the paper's own body (§X / Paper IV) — no fabrication, both
closed. No BLOCKER/MAJOR survived the hardened audit. Vendor headline-MAJORs
are all venue-norm (DOI, abstract ordering, pre-registration framing,
self-contained-methods) — out-of-scope or opinion, not factual defects.

## VERIFIED findings (closed)

| ID | Vendor | Claim | Verdict | Closure |
|----|--------|-------|---------|---------|
| **R57-1** | Opus (own) | Paper IV real-space dipole = **+0.43σ** at l.703 but **+0.41σ** at l.646 — same quantity | **VERIFIED MINOR** (internal inconsistency + stale-vs-cited-source) | Paper IV canonical is **+0.41σ** and carries an explicit "0.43→0.41 dipole regeneration" correction (`chirality_catalog_paper.tex` l.321); +0.43σ is stale. R56 OAI-E1 closure note itself flagged "two quotes also disagree" but only dropped p-values, leaving the σ mismatch. **CLOSED**: l.703 +0.43σ → +0.41σ. |
| **R57-2** | Gemini P5-M1 + Opus | Internal classifier-monopole offset mislabeled: abstract l.456 "internally verified ≈0.26 pp (f_CW^P5=0.49719)" and §II l.691 "0.49719 … corresponding to Δf_CW = −0.0026" attach the **external Paper IV** value to the **internal** measurement | **VERIFIED MINOR** (internal inconsistency; mildly self-favoring) | Paper's own §X arithmetic reconciliation (l.2551-2567) states f_CW^P5=0.49719 → **Δf_CW^P5 ≈ −0.0028 (0.28 pp), ~8% larger than the P4 catalog-mean −0.0026**. The summary sites understated the internal residual by quoting the smaller P4 number as "internally verified". **CLOSED**: abstract 0.26 pp → 0.28 pp; §II Δf_CW = −0.0026 → Δf_CW^P5 ≈ −0.0028 with the P4 −0.0026 cross-ref retained. σ_pred chain (legitimately uses P4 −0.0026) untouched. |

## Self-favoring item
**Yes — R57-2.** Quoting the internal monopole as the smaller external Paper IV
value (0.26 pp) labeled "internally verified" understated the paper's own larger
internal classifier bias (0.28 pp) by ~8%. The full §X disclosed the true −0.0028;
the abstract/§II summary did not. Corrected.

## FALSE POSITIVES (not actioned — genuine, per patterns 061-064 + calibration)
- **OpenAI P5-E1** "1 − 0.05^{1/6} mis-typeset as 0.05^1/6" — source is correct
  `$1 - 0.05^{1/6} = 39\%$` (l.2135); PDF superscript-render artifact. (Known, R34conf.)
- **OpenAI P5-M2** filament f_CW "0.4980 should be 0.49845" — 203261/408187 = **0.49796 → 0.4980 correct**; vendor arithmetic wrong.
- **OpenAI P5-M7 / Grok** "largest … DESI DR1 superlative unsupported" — already
  hedged "to our knowledge … to date … a null is not positive evidence" (l.2230, GRO-B2).
- **OpenAI P5-n8** Fig "binomial confidence" vs Jeffreys credible — l.2316 is a
  genuine frequentist Wald CI on the two-sample Δf_CW (correct); l.1371 figure
  caption unverifiable without the plotting script (figure may use a plain
  binomial CI). Not closed — cannot verify without fabricating.
- **OpenAI P5-E5** interior-buffer "1,805 vs 1,862 removed" — different builds
  (canonical l.2773 vs selection-corrected l.2792); both individually correct.
- **OpenAI P5-n7** "3,150,086 vs 3,150,089 in-mask cells" — 3-cell drift across
  distinct builds; unverifiable which is canonical without artifact. Noted, not closed.

## OUT-OF-SCOPE / OPINION (per directive: skip DOI + truly-blocked)
DOI/Zenodo (E3/M4), unpublished Paper IV self-contained-methods (E3), version-history
language in body (E2), pre-registration / garden-of-forking-paths (M1), promote
selection-corrected T-Web to mainline (E4), k=20-vs-exact in main table (M6),
TARGETID cluster-robust SE (M5 — design effect 1.018 disclosed, ~2% SE inflation,
changes no verdict), page-length condensation (n6). Abstract-ordering preference
(Gemini E1 / Grok M3): the body's stated DESIVAST-primary hierarchy is intact;
editorial only.

## Prior-fix integrity (R52/R55/R56 — confirmed intact, not re-opened)
- Paper IV reframe (real-space dipole null, harmonic withdrawn): intact l.702-714.
- Table V log10(1+δ) labeling: intact (l.604/1658/3604, col context l.1477-1480).
- Bonferroni |σ|≈4.07 two-sided: intact l.1052.
- −1.38σ / +0.71σ cluster/filament residual disclosure (R56 Gem-M1): intact
  l.1295-1296, honestly framed ("neither residual is negligible at face value").
- R56 OAI-E1 p-value drop: intact (R57-1 closes the *residual* σ mismatch R56 left).

## Compile / overflow audit (post-fix)
4-pass pdflatex (+ bibtex), **0 undefined refs/citations**, **0 Overfull \hbox
(column overflow)**, **0 \mbox{-} artifacts**, 33 pages. (2 benign Overfull \vbox
vertical, pre-existing.) PDF text confirms +0.43σ removed, +0.41σ and 0.28 pp present.

## CONVERGENCE STATEMENT
P5 is **converged** under the hardened de-biased standard. After closing 2 residual
internal-inconsistency MINORs (dipole 0.43→0.41σ; internal monopole 0.26→0.28 pp),
no factual BLOCKER/MAJOR/MINOR remains. All surviving vendor MAJORs are venue-norm
(DOI, abstract presentation, pre-registration framing) — non-substantive to the
science. The DESIVAST three-algorithm void null (Δf_CW=+0.0007), T-Web class
homogeneity (χ²=3.55, p=0.31), and the disclosed bright/dark ~2σ residual stand.
Recommend: address DOI/abstract-ordering at submission packaging; no further
science round required.
