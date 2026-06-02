# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 9.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=76932, completion=1124, total=78056, search_context_size=low, cost={'input_tokens_cost': 0.2308, 'output_tokens_cost': 0.01686, 'request_cost': 0.006, 'total_cost': 0.25366}

---

## PAPER-PER-B1

**BLOCKER** — Section 5 / Appendix PTA / bib items `Heinrich2023`, `Quintin2014`, `Cai2014`, `Wands2010`, `WilsonEwing2012`, `NANOGrav2023`, `Sesana2016`, `Burke-Spolaor2019`, `Heinrich2023`, `Munchmeyer2019` need a hard citation audit. Several claims are over-specific or fused across papers: the paper asserts `Quintin2014` + `Cai2014` establish a matter-bounce \( \gamma=3.0 \) prediction, but the cited bounce papers are about matter creation / bounce cosmology, not the PTA spectral-index result; `Cai2014` title is likely wrong or at least nonstandard; `Heinrich2023` is cited as the SPHEREx multi-tracer bispectrum paper but the bib says 2024 JCAP 074 with arXiv:2311.13082.  
**Fix:** Verify every cosmology citation against arXiv/ADS and split claims to the exact paper that makes them. If a claim comes from a review or secondary derivation, cite that explicitly instead of fusing titles/authors/years from multiple sources.

## PAPER-PER-B2

**MAJOR** — Intro / Sec. `\ref{sec:fnl}` claims an “internal Fisher diagnostic computation gives \( \sigma(f_{\rm NL}) \approx 0.07\)–0.12” and later a full 5-block Fisher yields \( \sigma(f_{\rm NL}) = 0.0667\)–0.115 with “\(38\sigma\) to \(66\sigma\)” detection significance for matter bounce. This is a huge theoretical overclaim on a non-public, internally tuned pipeline, and it is not anchored to any external validated forecast. The text also mixes “headline forecast” anchors with a separate idealized result and then downgrades/rewrites the canonical envelope multiple times.  
**Fix:** Remove the internal-number layering or clearly label it as an unvalidated toy calculation. Present one forecast family, one error model, and one caveat statement; do not convert the same Fisher pipeline into both a headline prediction and a post-hoc consistency check.

## PAPER-PER-B3

**MAJOR** — `\S\ref{sec:method}` / Table `\ref{tab:survey_summary}` / Sec. `\ref{sec:crossmatches}` contain arithmetic and definitional instability around counts: 37.3M sources vs. 37,272,042 in the “Path-C unique” row, 388,493 detections collapsing to 378,280 unique, and a three-layer stratification into point-source tier + Planck patches + ACT-quarantined artifacts. The narrative repeatedly changes whether ACT is included, whether Planck patches count as objects, and whether the headline should be 378,280 or 378,080.  
**Fix:** Freeze one counting convention and enforce it everywhere: define the population universe, the survey-level totals, the deduped unique-object total, and the non-object patch tier once; then make every table and abstract sentence use exactly the same accounting.

## PAPER-PER-M1

**MAJOR** — Sec. `\ref{sec:nanograv}` and bib item `NANOGrav2023` are citation-forensics risky. The paper cites “The NANOGrav 15 yr Data Set: Evidence for a Gravitational-wave Background” as the source for a free-spectrum KDE likelihood and then builds a Savage-Dickey calculation on a companion chain, but the paper does not show that the cited NANOGrav paper provides the exact KDE product, nor that the quoted arXiv/paper metadata are correct for the free-spectrum release being used.  
**Fix:** Cite the exact data-release / likelihood-product paper or archive record that corresponds to the KDE free-spectrum package, not just the headline evidence paper. Separate the dataset citation from the inference method citation.

## PAPER-PER-B4

**minor** — Sec. `\ref{sec:crosssurvey}` and Table `\ref{tab:survey_summary}` mix SIMBAD-unmatched fractions with “genuine novelty fraction” and then backtrack in prose. The paper says 58.8% is not novelty, but still uses novelty-like phrasing in multiple captions and conclusion bullets.  
**Fix:** Standardize terminology: “SIMBAD-unmatched fraction” for SIMBAD-only misses, and a distinct “archival novelty fraction” only for the 20-catalog cross-match result.

## PAPER-PER-N1

**nit** — Bib metadata likely stale or inconsistent for multiple entries: `SDSS_DR18` says 2023 ApJS 267, 44; `eROSITA_DR1` and `ACT_DR6` titles/venues look plausible but need title-level verification; `Nicolaou2026` is “in press” with no arXiv or DOI; `DESI2025DR1` is a documentation URL, not a normal bibliography item.  
**Fix:** Normalize the bibliography: include arXiv IDs/DOIs where available, remove placeholder “in press” entries if not needed, and verify venue/year/title strings against ADS or publisher metadata.
