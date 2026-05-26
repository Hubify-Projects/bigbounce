# P5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict_P5_v0_1_31
**Wall time**: 19.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=26599, completion=1437, total=28036

---

## PAPER-PER-B1 — Mis-cited DESIVAST paper metadata (BLOCKER)

**Location:** Bibliography entry `\bibitem{DESIVAST2025}` and related in-text references in §TWeb/ASTRA/DESIVAST discussion.  

**Issue:** The DESIVAST catalog is cited as “S. B. Douglass et al., ApJ 982, 38 (2025), arXiv:2411.00148,” but arXiv:2411.00148 corresponds to “DESIVAST: A Catalog of Low-Redshift Voids using Data from the DESI DR1 Bright Galaxy Survey” with first author Hernan Rincon; the ApJ volume/page and year given in the manuscript (“982, 38 (2025)”) do not match the current arXiv metadata and the author list is incorrect.[2]  

**Fix:** Replace the DESIVAST reference with accurate metadata for arXiv:2411.00148 (correct title, first author Rincon, correct journal info once published) or, if ApJ details are already fixed by the time of submission, update arXiv ID, author list, year, and volume/page consistently; ensure all in-text mentions of “Douglass et al. 2025” are aligned with the actual lead author and publication details.[2]  

---

## PAPER-PER-M1 — Overstated external-validation status for DESI T-Web & ASTRA papers (MAJOR)

**Location:** §“Concurrent-literature DR1/EDR cosmic-web cross-validation” and surrounding text, esp. the phrase “publication-grade independent external validation” and characterization of these works as fully established DESI DR1 catalogs.  

**Issue:** The paper treats arXiv:2604.02463 and arXiv:2604.01456 as publication-grade DESI DR1/EDR environment products providing “independent external validation,” but both are recent arXiv submissions (to JCAP or similar) without final journal acceptance or official DESI VAC status; the manuscript’s language reads as if they are already established, peer-reviewed “public DR1 cosmic-web catalogs,” which is stronger than what the arXiv status supports.[1][0]  

**Fix:** Downgrade the language from “publication-grade independent external validation” / “public DR1 cosmic-web catalog” to “concurrent arXiv analyses we use for consistency checks,” and state explicitly that these are preprint results not yet official DESI value-added catalogs at the time of writing, while still comparing volume fractions and methodology.  

---

## PAPER-PER-M2 — Incomplete metadata for T-Web DESI DR1 preprint (MAJOR)

**Location:** `\bibitem{TWebDESI2026}` and corresponding discussion of the T-Web DR1 analysis.  

**Issue:** The citation lists a DESI Collaboration DR1 T-Web paper as “submitted to MNRAS (2026), arXiv:2604.02463,” but arXiv:2604.02463 is actually “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification” by Ullah et al.; the current manuscript abbreviates authorship to “DESI Collaboration” and omits the actual author names and arXiv title, which is not standard and obscures which work is meant.[1]  

**Fix:** Update the reference to give the correct title and lead-author list for arXiv:2604.02463, and only append “DESI Collaboration” if that is how the paper self-identifies; avoid generic “DESI Collaboration, submitted…” without the real arXiv title and main authors.  

---

## PAPER-PER-M3 — Incomplete metadata for ASTRA DESI EDR preprint (MAJOR)

**Location:** `\bibitem{ASTRADESI2026}` and the paragraph describing the ASTRA EDR probabilistic catalog.  

**Issue:** The citation refers to “Zapata-Zuluaga et al. 2026, the first public DESI cosmic-web catalog” but does not provide the actual title; arXiv:2604.01456 is “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog” by Zapata-Zuluaga et al., and the current shorthand risks confusion and under-specification (it also overstates “first” without acknowledging the EDR scope explicitly).[0]  

**Fix:** Replace the informal description with full bibliographic metadata: correct title and authors for arXiv:2604.01456, and explicitly label it as an EDR probabilistic environment catalog; if you want to call it “first public cosmic-web environment catalog built on DESI EDR,” match that phrasing to the abstract rather than stating it as a broader DR1-wide “first.”[0]  

---

## PAPER-PER-m1 — Planck 2018 cosmological parameters reference underspecified (minor)

**Location:** `\bibitem{Planck2018cosmoparams}`.  

**Issue:** The Planck 2018 parameters paper is cited generically as “Planck Collaboration, ‘Planck 2018 results. VI. Cosmological parameters,’ Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209,” which is correct but omits the lead author and DOI, and uses a slightly abbreviated form of the journal name compared to ADS.[1]  

**Fix:** Optionally enhance to the standard A&A form, e.g. “Planck Collaboration VI, N. Aghanim et al., Astron. Astrophys. 641, A6 (2020), doi:10.1051/0004-6361/201833910, arXiv:1807.06209,” matching ADS metadata; this is polish, not a blocker.[1]  

---

## PAPER-PER-n1 — Internal-artifact reference in main bibliography for Paper IV (nit)

**Location:** `\bibitem{golden_chirality_2026}` and nearby companion-paper references.  

**Issue:** The “Paper IV” chirality catalog is cited with an internal Git/LaTeX artifact path and version tag instead of an arXiv ID, journal, or at least an explicit indication that it is an in-prep companion; this makes the citation non-standard and unverifiable in the literature.  

**Fix:** Replace the artifact path with a real public identifier (arXiv ID, DOI, or journal reference) for Paper IV; if still in preparation, label it explicitly as “in preparation” or “submitted, arXiv:… (to appear)” and remove the internal repository path from the formal bibliography.
