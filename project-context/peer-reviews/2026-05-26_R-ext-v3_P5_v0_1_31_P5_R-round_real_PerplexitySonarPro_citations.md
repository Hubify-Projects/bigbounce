# P5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v3_P5_v0_1_31
**Wall time**: 13.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=27794, completion=1097, total=28891

---

## PAPER-PER-B1 — Nonexistent Paper II citation

Paper II is cited as “$f_{NL} = -35/8$ Forecast: SPHEREx Discrimination of Bounce vs. Inflation,” 2026, with an internal artifact path instead of a journal/arXiv reference. A search shows no such paper on arXiv, ADS, or publisher sites, and the quoted title/contents appear to be internal-only and not yet publicly published.  

**Fix:** Clearly mark Paper II as “in preparation” or “internal companion manuscript” and remove any implication it is a published or arXiv-indexed paper; do not treat it as an external, citable reference until actually released with a DOI or arXiv ID.

---

## PAPER-PER-B2 — Misrepresented status of Paper IV

Paper IV is cited as “companion paper (Paper IV), 2026” with only an internal GitHub/HuggingFace artifact and no journal or arXiv reference. A search finds no public paper with this title or arXiv record, so referring to it as an established published result (e.g., “Paper IV establishes…,” “reported in Paper IV”) overstates its external status.  

**Fix:** Explicitly label Paper IV as an internal companion analysis / in-prep manuscript and avoid language that treats its results as peer-reviewed external literature; optionally add “Golden, in preparation” or supply an arXiv ID once posted.

---

## PAPER-PER-M1 — Shorthand citation “Paper III” missing from bibliography

The text refers to “Paper III provide[s] independent discriminators (primordial \(f_{\rm NL}\) and multi-survey anomaly statistics)” with no bibliographic entry or identifying information. This is effectively an uncited, opaque reference and prevents readers from locating the work.  

**Fix:** Either add a full bibliographic entry for Paper III (author, title, year, venue/arXiv ID) or explicitly state that “Paper III (in preparation)” is not yet public and remove claims that rely on it as established literature.

---

## PAPER-PER-M2 — DESI T-Web paper metadata inaccuracies

The reference labeled \cite{TWebDESI2026} is described as a DESI Collaboration paper titled “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” with arXiv:2604.02463 and DESI Collaboration authorship. The actual arXiv:2604.02463 paper is titled “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification” but lists authors Hafiz Inam Ullah et al. (not the DESI Collaboration), and does not present itself as a DESI-collaboration-branded DR1 cosmic-web catalog.  

**Fix:** Correct the citation metadata to match arXiv:2604.02463 exactly (author list beginning with Ullah, H., appropriate author group, and “submitted to JCAP”) and adjust prose so it is cited as an independent T-Web analysis using DESI DR1, not as a DESI Collaboration DR1 catalog paper.

---

## PAPER-PER-M3 — ASTRA DESI EDR citation metadata mismatch

The paper cites \cite{ASTRADESI2026} as “Zapata-Zuluaga et al. 2026, the first public DESI cosmic-web catalog,” with a Zenodo DOI 10.5281/zenodo.19358024 implied. ArXiv:2604.01456 exists with the exact title “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog” and authors Diana C. Zapata-Zuluaga et al., but the current citation does not include the arXiv ID, and wording should match the actual arXiv record rather than only a Zenodo entry.[0]  

**Fix:** Update the bibliography entry to include arXiv:2604.01456, correct the author list and title formatting to match arXiv, and phrase it as the first public DESI EDR cosmic-web environment catalog built with ASTRA, explicitly tying the citation to the arXiv record.[0]

---

## PAPER-PER-nit1 — DESIVAST catalog citation formatting

The DESIVAST reference \cite{DESIVAST2025} corresponds to “DESIVAST: Catalogs of Low-Redshift Voids using Data from the DESI Data Release 1 Bright Galaxy Survey,” ApJ 982, 38 (2025), arXiv:2411.00148. The arXiv ID and DOI match the actual paper, but the text sometimes treats DESIVAST as a “DR1 VAC” generically rather than explicitly as the BGS-based DR1 void catalog, which could be tightened for clarity.[1]  

**Fix:** Keep the existing bibliographic metadata but clarify in the text that DESIVAST is the DR1 BGS-based void catalog (VoidFinder + ZOBOV implementations) rather than a generic DR1 cosmic-web VAC, to avoid overgeneralization of its scope.[1]

---


