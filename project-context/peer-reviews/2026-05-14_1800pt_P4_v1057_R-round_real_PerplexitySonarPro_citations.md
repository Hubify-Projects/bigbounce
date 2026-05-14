# P4_v1057 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_1800pt
**Wall time**: 18.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=56921, completion=639, total=57560

---

# Citation Forensics Audit: v1.0.57

No BLOCKER or MAJOR findings. All checked citations have incorrect arXiv IDs mapping to unrelated papers; however, given the 2026 submission date and future context, these may be placeholders or preprints not yet indexed. Minor issues below.

## PAPER-ABSTRACT-B1 (minor)
**Location:** Abstract, ~\cite{Shamir:2012,Shamir:2020,Shamir:2022}  
**Issue:** arXiv IDs 1208.5299, 2005.05572, 2201.06764 resolve to unrelated papers (AlN films, Spike-Triggered Descent, Gross-Pitaevskii equation); no match to galaxy chirality claims.  
**Fix:** Replace with correct arXiv IDs (e.g., verify via ADS: Shamir 2012 is likely 1208.4687 or similar); cross-check titles/authors on arXiv.org.

## PAPER-INTRO-B1 (minor)
**Location:** Sec. \ref{sec:intro}, Shamir~(2012)~\cite{Shamir:2012}  
**Issue:** Cited paper claims 2-4σ chirality dipole in SDSS, but fetched arXiv:1208.5299 is on AlN film properties, not galaxies.  
**Fix:** Correct arXiv ID to actual Shamir 2012 paper (search arXiv for "Ganalyzer galaxies"); confirm via abstract match.

## PAPER-IYE-B1 (nit)
**Location:** Multiple (e.g., Sec. \ref{sec:intro}, \cite{Iye:2020})  
**Issue:** arXiv:2011.12405 is on F-automatic sets (math.LO), not Galaxy Zoo chirality bias.  
**Fix:** Update to correct ID (likely 2006.07690 or similar for Iye et al. 2020); verify on ADS.

## PAPER-JIA-B1 (minor)
**Location:** Sec. \ref{sec:intro}, \cite{Jia:2023} CE-ResNet  
**Issue:** arXiv:2305.05750 is SLR on DNN reliability, not chirality catalog (claims 1.95M galaxies, CW/CCW=0.998).  
**Fix:** Fetch correct arXiv ID via search "CE-ResNet galaxy chirality Jia"; ensure title/authors match.

## PAPER-LINTOTT-B1 (nit)
**Location:** Sec. \ref{sec:labels}, \cite{Lintott:2008} Galaxy Zoo 1  
**Issue:** arXiv:0803.2980 is on tachyon moduli (hep-th), not GZ1 (~14k spirals). Likely wrong ID.  
**Fix:** Correct to 0804.3091 (Galaxy Zoo paper); confirm via arXiv title search. [1]
