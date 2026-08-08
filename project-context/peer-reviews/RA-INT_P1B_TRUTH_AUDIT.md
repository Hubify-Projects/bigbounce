# RA-INT P1B — Truth Audit (Round A, neutral, verdict-first)

Paper: `arxiv/paper1b_mcmc_companion.tex` (v1B.0.82 → v1B.0.83 after close)
PDF audited: md5 `f2838e5b`, 22 pp. Compile: clean, 0 undef-refs.
Vendors (native-PDF): Gemini 2.5 Pro, OpenAI gpt-5 (high+pass2), Grok 4.3 (rasterized).
Perplexity FAILED (API quota 401). Anthropic leg absent (cost-conservation failover; 3 PDF vendors cover).

Vendor recommendations:
- Gemini: **ACCEPT WITH MINOR CORRECTIONS** ("model of careful scientific work").
- OpenAI: **MAJOR REVISIONS** (mostly structural/presentational + a few real spot-checks).
- Grok: **REJECT** (scope/self-containment/length — all pre-empted by deliberate companion structure).

## Verdicts

### VERIFIED + CLOSED (real, in-scope, non-fabricating)

1. **SH0ES provenance mislabel (OpenAI E3, ESSENTIAL).** Prose said "Riess+2020"
   for the anchor while the values ($M_B=-19.253\pm0.027$, $h=0.7304$ i.e.
   $H_0=73.04\pm1.04$) and the citation are Riess et al. 2022 (`\cite{Riess2022}`,
   used everywhere else). Author's own comment (L819-820) confirms `H0.riess2020Mb`
   is only the Cobaya alias, actual cite is Riess2022. **Fix:** two prose
   "Riess+2020" → "SH0ES~\cite{Riess2022}" (L1669, L1722); Cobaya alias
   `H0.riess2020Mb` left unchanged (literal software name). Internal-consistency fix.

2. **R-hat boundary inequality (OpenAI M13, MAJOR).** Footnote (L1525) claimed
   "all ... satisfy $\hat R-1 < 3\times10^{-3}$" while Table I lists the
   Planck+BAO+SN worst as exactly 0.003 = $3\times10^{-3}$. Strict `<` contradicted
   by the boundary table value. **Fix:** `<` → `\le` (L1525). Inconsistency fix.

### VERIFIED but NOT closed (flagged; closure would require author-intended derivation — no fabrication)

3. **"$\gtrsim100\times$ fine-tuning" (OpenAI M11).** Only the companion
   "$\sim25\times$" energy-density tuning (Ωa∝θ², (0.5/0.1)²=25) is derived; the
   "$\gtrsim100\times$ under cosθ-flat prior" is asserted, not shown. Genuine
   unbacked-number, BUT the cosθ rerun (θ≤0.1 mass 0.33%→0.068%) does not obviously
   reconstruct 100×. Not closed in Round A: deriving it would risk fabrication;
   removing it would discard a claim the author may have basis for. Carry to author/Round B.

### FALSIFIED (source contradicts the finding)

- Grok E1/E2/E4 (abstract omits scope qualifiers): abstract is extensively
  caveated ("no torsion modifications... null-consistency test... not evidence
  for/against ECH"; "not a distinctive ECH prediction"). Grok 150-DPI raster
  missed dense caveats.
- OpenAI E5 (LiteBIRD "0.032" denominator typo): source L2771 is `\sqrt{0.03^2+0.094^2}`
  → 0.73σ, correct. GPT misread the rendered superscript.
- OpenAI N5/N6 (inverse-variance 0.241; M_B–H0 constant −18.571): both recompute
  correct to quoted precision (0.2415→0.241; −18.5706→−18.571).
- OpenAI M10 (Age 0.019 Gyr "too small"): Planck-2018 age σ≈0.020 Gyr; 0.019 is
  consistent for a well-constrained chain. Reviewer "expectation" hand-wavy.
- Grok N2 ("canonical canonical-mask" doubled word): not present in source.
- Gemini N4 ("planck_2018_lensing.k_2018_lensing.clik"): not in source; PDF
  line-wrap render artifact.

### OUT-OF-SCOPE / submission-time / OPINION (calibration: leave)

- Grok M1 (self-containment), M2 (length/negative-results), Grok REJECT framing:
  companion-to-P1a is a deliberate coordinated submission; negative-results framing
  protected. Imported P1(a) results are summarized for standalone readability.
- Grok M4 / OpenAI M5 (w0wa overlap σ-distance): calibration — overlap caveat +
  removed σ-distances are INTENTIONAL (DES-Y5×Pantheon+ shared SNe); do NOT re-add.
  Table II already bears the bold "no σ-distance / not for model comparison" label.
- OpenAI M6 (DOI minting): DOI deferred-to-submission is NOT a defect (calibration).
- OpenAI M7/N2/n2 (move pathnames to appendix, 22→14pp, AI-ack placement):
  deliberate reproducibility style + PRD editor-discretion; OPINION.
- OpenAI E1/E2/M1/M2/M3/M8/M14, Gemini M1/M2/N1/N2/N3 (robustness tables, promote
  IVW estimator, beam-mismatch test, fsky-after-apodization def, 3.6σ abstract
  citation, "load-bearing" jargon): polish/enhancement; the prose already discloses
  the numbers/choices. The unweighted estimator is deliberately retained to match
  published driver scripts and is fully disclosed. No defect.
- 3.6σ abstract attribution (Gemini M1, OpenAI M9): the abstract's H0-tension 3.6σ
  IS the full-tension value (67.68±1.06 → 3.61σ), quoted in place and tied in body
  (L1671). Distinct from the coincidental birefringence 3.6σ (Eskilt, attributed).
  No defect; optional citation polish only.

## Outcome
2 VERIFIED items closed (provenance + R-hat boundary). Version v1B.0.82 → v1B.0.83,
date June 29, 2026. 1 unbacked-number flagged for author (no fabrication). All other
findings FALSIFIED / OUT-OF-SCOPE / OPINION.
