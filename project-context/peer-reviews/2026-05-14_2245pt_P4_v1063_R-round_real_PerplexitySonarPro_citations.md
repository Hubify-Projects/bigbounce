# P4_v1063 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_2245pt
**Wall time**: 15.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=60407, completion=241, total=60648

---

## PAPER-PER-B1 — MAJOR
**Section:** Bibliography, `\bibitem{Shamir:2022}` and multiple in-text claims.  
The paper says the prior arXiv ID `2207.11885` was wrong and that the canonical record is PASJ 74, 1114 (2022), but the source does not verify the actual arXiv preprint or title match for Shamir 2022. This is still a citation-gap issue: either cite the journal record only, or supply a verified arXiv ID/title pair; do not imply a confirmed arXiv reference where none is established [2].

## PAPER-PER-B2 — MAJOR
**Section:** Bibliography, `\bibitem{Iye:2020}`.  
The year/title pair is fused incorrectly: the cited arXiv record `2011.00662` corresponds to the paper “Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,” with journal placement on the arXiv page, but the manuscript’s surrounding prose treats it as
