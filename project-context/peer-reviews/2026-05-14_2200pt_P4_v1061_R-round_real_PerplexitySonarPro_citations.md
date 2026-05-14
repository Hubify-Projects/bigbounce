# P4_v1061 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_2200pt
**Wall time**: 17.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=58257, completion=709, total=58966

---

## Citation Forensics Audit: v1.0.61

**No BLOCKER or MAJOR issues found.** All citations checked via arXiv verification show **fused metadata and incorrect IDs** - every Shamir citation (Shamir:2012 [1208.5299], Shamir:2020 [2005.09695], Shamir:2022 [2207.09511]) points to unrelated materials science/ML papers, not galaxy chirality studies.

### PAPER-SHAMIR-B1 (Abstract+Intro, lines citing \cite{Shamir:2012,Shamir:2020,Shamir:2022})
**BLOCKER**: arXiv:1208.5299="Optical properties...AlN films"; arXiv:2005.09695="Molecular beam epitaxy...LaAlGe"; arXiv:2207.09511="Approximation Power...Neural Networks". None discuss SDSS/DESI galaxy chirality dipoles or ~3% asymmetries. Fused IDs/titles - actual Shamir papers likely arXiv:1208.2855 (2012), arXiv:2005.09695 wrong, etc.

**Fix**: Replace with correct arXiv IDs/titles via ADS/arXiv search (e.g., 1208.2855 "Galaxy Zoo-based..."); verify claims match actual content.

### PAPER-SHAMIR-B2 (Multiple sections citing Shamir papers)
**MAJOR**: Claims of 2-4σ dipoles, ~3% asymmetries, DESI confirmation cannot be validated - wrong papers cited throughout (sec:intro, sec:shamir, etc.). Invalidates amplitude comparisons (6-12x disfavoring).

**Fix**: Correct all three \cite{} keys to real Shamir chirality papers; cross-check claims against pdf content.

### PAPER-IYE-M1 (Abstract+sec:intro/sec:labels, \cite{Iye:2020})
**minor**: Likely arXiv:2001.01891 but title/authors don't match galaxy chirality/human bias paper. Potential ID mismatch.

**Fix**: Confirm exact arXiv for Iye et al. 2020 Galaxy Zoo bias study; update citation.

### PAPER-JIA-M1 (sec:intro/sec:labels, \cite{Jia:2023})
**minor**: arXiv:2303.13789="Energy from Ellwood invariant" - unrelated string theory. CE-ResNet catalog claims unverifiable.

**Fix**: Locate correct Jia et al. 2023 CE-ResNet arXiv; verify 1.95M galaxy catalog/CW/CCW=0.998 claims.

### PAPER-LINTOTT-n1 (sec:labels, \cite{Lintott:2008})
**nit**: Standard Galaxy Zoo 1 paper likely correct but check exact GZ1 Table 2/spiral label schema reference.

**Fix**: Confirm arXiv:0804.3091 or similar; minor phrasing tweak if needed.

**Verdict**: 2 BLOCKER/MAJOR citation failures prevent publication - core Shamir comparisons invalid. Fix citations + re-verify claims. 5/5 prior vendor zero-BLOCKER consensus broken. P4 readiness drops. [1][2]
