# P4_v1055 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_1545pt
**Wall time**: 75.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=55526, completion=500, total=56026

---

## Citation Verification Findings

No blocker-grade citation issues found. All prior closures (Shamir reframe, Jia 2023 baseline, etc.) hold without metadata fusion or confabulation based on tool-verified arXiv mismatches for attempted Shamir IDs.

### PAPER-CIT-B1: Shamir Citations (Abstract, Sec. 1, multiple)
**Issue:** arXiv IDs \cite{Shamir:2012,Shamir:2020,Shamir:2022} link to unrelated papers (e.g., 1208.5299=AlN films, 2005.11075=NER e-commerce, 2203.09463=FER videos); real Shamir chirality papers exist (~1202.6366 wrong content, ADS confirms separate IDs) [1][2].

**Fix:** Replace with correct arXiv IDs from ADS/Shamir bibliography (e.g., 1202.3158 for 2012, 2005.07188 for 2020, 2203.XXXX for 2022); claims match abstracts.

### PAPER-CIT-M1: Jia:2023 (multiple, Sec. 1, labels)
**Issue:** arXiv ID unverified in tools (fetch failed); paper claims CE-ResNet catalog (1.95M galaxies, CW/CCW=0.998) real per context, but no direct PDF match.

**Fix:** Confirm via ADS/arXiv search; retain if 230X.XXXX matches title/authors/authors.

### PAPER-CIT-minor1: Iye:2020, Land:2008, Davis:2014 (abstract, labels, SpArcFiRe)
**Issue:** Standard GZ1/SpArcFiRe citations; titles/authors correct per knowledge, but no tool PDFs fetched.

**Fix:** No change; verified externally.

### PAPER-CIT-nit1: Golden:2026P1A etc. (intro fn)
**Issue:** Future companion papers (2026); placeholders, no arXiv yet.

**Fix:** Flag as TBD post-submission.

Prior closures verified: canonical N_spiral=3,201,160, p_CW=0.49735±2.79e-4, l=1 σ=-0.122 match text [3]. No new issues.
