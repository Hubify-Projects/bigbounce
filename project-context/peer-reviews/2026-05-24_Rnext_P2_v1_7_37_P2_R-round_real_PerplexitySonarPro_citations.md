# P2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-24_Rnext_P2_v1_7_37
**Wall time**: 18.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33357, completion=1145, total=34502

---

## PAPER-PER-B1 — Mis-cited PAPERS for Pajer–Tanaka–Urakawa

The abstract and introduction cite “Pajer-Tanaka-Urakawa” with keys `\cite{Pajer:2013,TanakaUrakawa:2011}`, but arXiv:2013 and 2011 works with those authors are not the sources of the conformal Fermi–frame inflation consistency relation, and the bibkeys as written do not correspond to standard arXiv IDs or titles. [1][2]  
Fix by explicitly citing the correct CFC/physical-frame consistency relation papers with accurate metadata (authors, titles, arXiv IDs) and updating the BibTeX entries and text so the keys match real references.

## PAPER-PER-M1 — Incomplete/ambiguous reference to Cai et al. 2009

The paper repeatedly cites “Cai et al. 2009” / `Cai:2009fn` as the source of the matter-bounce bispectrum and \(f_{\rm NL}^{\rm local}=-35/8\), but the arXiv entry 0903.0631 (“Non-Gaussianity in a Matter Bounce”) does not expose the numerical value or detailed polynomial in the abstract, and no journal reference is given in the draft to disambiguate which published version (if any) is meant. [2]  
Fix by adding the full arXiv ID and journal citation for the exact version where the \(-35/8\) normalization and Eq. (37)-type coefficients are actually written, and ensure the in-text discussion (“their Eqs. 34–36”, “Eq. 37”) matches the numbering in that version.

## PAPER-PER-M2 — Wands & Finelli 1998/2001 references need disambiguation

The introduction attributes the matter-like contracting mechanism for scale-invariant spectra to Wands 1998 and Finelli & Brandenberger 2001 with keys `\cite{Wands:1998yp,Finelli:2001sr}`, but the arXiv stubs implied by those keys (`astro-ph/9805022`, `astro-ph/0101019`) are in fact unrelated observational papers (IRC+10216 imaging and a Chandra lens observation). [3][4]  
Fix by correcting the bib entries so that `Wands:1998yp` points to the actual “Duality invariance of cosmological perturbation spectra” paper and `Finelli:2001sr` to the correct matter-bounce/contracting-phase theory work (with real arXiv IDs and journal references), and updating any hard-coded arXiv numbers.

## PAPER-PER-M3 — Heinrich et al. 2023/2024 SPHEREx bispectrum forecast citation

The paper cites “Heinrich et al. 2024” / `\cite{Heinrich:2023}` as the SPHEREx multi-tracer bispectrum forecast source for \(\sigma(f_{\rm NL}^{\rm local})\approx0.7\), but the arXiv ID suggested by the key and year is not specified and 2023–2024 SPHEREx PNG forecasts need an unambiguous reference (title, arXiv:YYMM.NNNNN). [1]  
Fix by inserting the precise arXiv ID and journal venue for the Heinrich SPHEREx PNG paper, verifying that Fig. 6 / Table 3 indeed give \(\sigma(f_{\rm NL})\approx0.7\) in the stated setup, and aligning the year in the text (2023 vs 2024) with the actual publication.

## PAPER-PER-m1 — Dalal/Slosar scale-dependent bias references mislabeled by arXiv keys

The standard SDB references are cited as `\cite{Dalal:2007cu,Slosar:2008}`, but the internal keys map—by their suffixes—to unrelated 2007–2008 astro-ph entries in the current bib snapshot (lens cluster and IRC+10216 imaging rather than PNG bias). [3][4]  
Fix by ensuring `Dalal:2007cu` points to Dalal et al. 2008 (scale-dependent bias from local PNG) and `Slosar:2008` to the correct Slosar et al. LSS non-Gaussianity paper, with correct titles and arXiv IDs, and regenerate the bibliography so those keys resolve to the right works.

## PAPER-PER-n1 — Mixed “Cai & Brandenberger” vs “Li & Brandenberger” normalization story

In several places the text attributes the \(-35/16\) alternative normalization to “Cai & Brandenberger” while the abstract caveat and later discussion attribute it to “Li & Brandenberger” without giving a precise citation, making it unclear which actual paper carries the \(-35/16\) result. [2]  
Fix by identifying the exact paper (authors, title, arXiv ID) that reports \(-35/16\), using that consistently (either always “Li & Brandenberger” or always “Cai & Brandenberger” as appropriate), and correcting any mismatched author names or fused metadata in the convention-appendix and main text.
