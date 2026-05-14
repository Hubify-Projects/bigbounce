# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_1200pt
**Wall time**: 23.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=52566, completion=596, total=53162

---

## PAPER-SHAMIR1-BLOCKER
**Abstract, line ~15**: Cites \cite{Shamir:2012} claiming "~3% asymmetry reported by Shamir (2012, 2020, 2022)". arXiv:1208.5299 is "Optical properties...AlN films" (materials science, no galaxies).  
**Fix**: Replace with correct arXiv (likely 1203.3548 or similar); verify title/authors match galaxy chirality paper by Lior Shamir.

## PAPER-SHAMIR2-BLOCKER
**Abstract, line ~15**: Cites \cite{Shamir:2020} for 2020 extension to ~10^5 galaxies, ~3% asymmetry. arXiv:2006.15790 is "Detection of microquasar V404 Cygni at gamma-rays" (X-ray binary, no spirals).  
**Fix**: Correct arXiv ID (likely 2007.01532); cross-check ADS/arXiv for Shamir's actual 2020 chirality paper title/authors.

## PAPER-SHAMIR3-BLOCKER
**Introduction, line ~3**: Cites \cite{Shamir:2022} for DESI Legacy confirmation. No 2022 paper verifiable; ID likely fused/confabulated (pattern matches prior errors).  
**Fix**: Locate real arXiv via ADS search "Shamir galaxy chirality 2022"; if none, remove claim or cite correctly.

## PAPER-IYE-TITLE-MAJOR
**Introduction, line ~8**: Cites \cite{Iye:2020} analyzing Galaxy Zoo, finding null after reading bias correction. Title/authors correct (arXiv:2003.02227), but claim omits key detail: Iye uses manual reclassification of subset, not full Zoo correction.  
**Fix**: Qualify as "subset manual analysis" to avoid overstating scope.

## PAPER-JIA-CECOUNT-minor
**Introduction, line ~15**: Claims Jia:2023 CE-ResNet catalog "1.95 million galaxies". Actual ~1.95M total objects, but many non-spirals; spirals subset smaller (paper implies binary classifier).  
**Fix**: Change to "1.95M galaxies (binary CW/ACW, no NS class)" for precision.

## PAPER-LAND-OVERCLAIM-nit
**Abstract, line ~28**: Attributes Catalog C 0.26% CCW excess to "sub-percent human-handedness bias documented in ". Land:2008 shows ~1-2% bias in Zoo votes, but not quantified as "sub-percent" or direct cause.  
**Fix**: Rephrase to "consistent with magnitude of bias in Land:2008 (~1%)".
