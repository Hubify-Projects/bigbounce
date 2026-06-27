# R57 P4 — Truth Audit (hardened de-biased re-review)

**Paper:** P4 — Survey-Scale Galaxy Chirality with Equivariant TTA
**Source:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.190)
**Compile:** 0 undef refs, 0 overfull hbox, 23 pages (md5 PDF 5ddefa62)
**Vendors:** Gemini-2.5-pro OK, Grok-4.3 OK, GPT-5 OK; Perplexity FAILED (quota). Anthropic via this Opus read.
**Prior:** 0-new in R55 AND R56 (held ACCEPT).
**Standard:** Hardened PRD/MNRAS; self-favoring / unstated-assumption / internal-inconsistency = real finding (MINOR min).

## Verdicts

### VERIFIED — NEW (closed this round)

- **R57-P4-1 (MINOR, internal inconsistency / overstatement).** §parity_translation (l.755) read
  "The Shamir ~3% amplitude class **is excluded** by a factor of ~5-12 under the present pipeline."
  This contradicts (a) §comparison (l.711) "We do **not** claim a frequentist exclusion of Shamir's
  Ganalyzer estimator," and (b) the abstract/intro (l.366) framing "**inconsistent in amplitude** …
  though a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion."
  The parity section was the lone outlier using the unqualified "excluded."
  Convergently flagged by **Gemini-E1, OpenAI-M5, Grok-M4**.
  **CLOSED:** reworded to "is in tension at the amplitude level by a factor of ~5-12 … not a frequentist
  exclusion of Shamir's Ganalyzer estimator (Sec.~comparison)." Factor 5-12, 0.32%, 1.7-4.0% all
  unchanged. Headline science unchanged. Recompiled clean.

### FALSIFIED / FALSE-POSITIVE (not closed — verified non-issues)

- **OpenAI-E1 / Grok-E1: "+3.64σ vs +7.93σ canonical inconsistency."** Disclosed and litigated across
  EXT5/R34conf with an explicit AUTO-FALSIFY-on-re-raise rule. The two are different estimators
  (500-MC per-pixel direct single-mode vs 10^4 per-galaxy 39-band-decoupled) and the paper states they
  "should not be numerically equated." No new evidence. FALSIFIED.
- **OpenAI-E6 / m6: per-pixel vs per-galaxy null "labeling inconsistency."** Misreading — the +3.64σ
  (canonical, per-pixel) and +7.28σ (apodized, per-galaxy) are different results, each locally tagged
  with its null where reported. FALSE POSITIVE.
- **OpenAI-E2: "broken Data-Availability URL."** `\url{…/datasets/bamfai/galaxy-chirality-catalog}` is
  clean in source; the "dataset s" spacing is an xurl line-break / pdftotext artifact. DOI-not-minted is
  TRULY-BLOCKED (Zenodo at submission). FALSE POSITIVE + TRULY-BLOCKED.
- **OpenAI-E3: "b/a edge-on 65.7% contradiction."** Paper distinguishes the conditional labeling rate
  (65.7%, available) from the deferred catalog fraction f_edge; quantitative reduction = f_edge×65.7%.
  Not contradictory. FALSE POSITIVE.
- **Gemini-M1: "Table X leg z-values misleading."** Already shown as "—" with caption noting collinearity
  (l.950-952). Fix already implemented (raster misread). FALSE POSITIVE.
- **Grok-E3: "99.32% lacks SE/artifact."** SE given (0.40/√500≈0.018 pp) + seed 42 + artifact cited
  (l.695). FALSE POSITIVE.
- **Grok-N1 (157-object diff), Gemini-N1 (δ typo), OpenAI-n1/n2/n3 typos.** Explained in text /
  pdftotext extraction artifacts (\delta in source). FALSE POSITIVE.
- **Grok-M2: D4 21.4% non-equivariance leak.** Quantified: mean p_CW stable <0.0016; QC-flag-excluded
  dipole null-consistent (z=+0.48 vs +0.52). Already addressed. FALSIFIED.

### OPINION / POLISH (not severity-defaulted; genuinely non-load-bearing)

- Length 23pp (Grok-M1, OpenAI, Gemini) — style; already condensed from 54pp per prior mandate.
- σ-juxtaposition "local qualifier at every mention" (Grok-E1, OpenAI-E4) — blanket convention statement
  (l.516) + Sec.~notation + caveats at all load-bearing sites already present; maximalist preference.
- OpenAI-E5 p-convention (15/500 vs (k+1)/(N+1)): two different runs, each labeled; 0.030 vs 0.032
  changes nothing on a non-primary diagnostic. Polish.
- OpenAI-M7 "θ-uniform mildly": area-uniform full re-run reproduces all floors; "mildly" describes the
  (mild) effect on results. Defensible. Polish.

## Integrity fixes — confirmed INTACT (not re-opened)
z=0.58 primary (l.349,606); +3.29σ → -0.03σ on purity ladder (l.702,901,913); Shamir bibchimera /
"comparable pre-MASTER artifact" framing (l.364,711); 37.77% sum-to-one rounding disclosed (l.521).

## Net verdict
**ACCEPT (converged).** 1 NEW VERIFIED MINOR found and closed (Shamir "excluded"→"in tension at the
amplitude level"); all other vendor findings are previously-closed/disclosed, false-positive (extraction
artifacts / misreads), or polish. No self-favoring number-headlining survives audit. After this one-phrase
alignment, P4 has no open DO-NOW items.
