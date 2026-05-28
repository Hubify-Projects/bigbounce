# P5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-27_R-ext-maint-v3_P5_v0_1_32
**Wall time**: 16.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29353, completion=978, total=30331

---

## PAPER-PER-B1 – Self-citations to unpublished companion papers

The references to “Paper IV” and “Paper II” use internal artifact paths and version tags instead of standard bibliographic metadata and do not correspond to any arXiv/ADS/public DOI entries under those titles as of now (e.g. the Shamir 2022 DESI spin paper is the only obvious match in this topic space, and the claimed 8.47M-galaxy chirality catalog paper is not indexed).[3][5]  
Fix: Replace these with proper external references once the companion papers are on arXiv/journal (with arXiv IDs, journal info, year), and in the meantime clearly mark them as “in preparation / in review, internal dataset description” rather than giving them the appearance of already-published literature.

## PAPER-PER-M1 – Alexander & Yunes citation formatting

The Alexander & Yunes review is correctly identified by title, journal (Phys. Rep. 480, 1, 2009), DOI and arXiv:0907.2562, but the bibliography line drops the journal page-range “1–102” and uses “1” as if it were a page number, which is not the usual Phys. Rep. citation format.[0]  
Fix: Update the entry to standard form, e.g. “Phys. Rept. 480, 1–102 (2009)” or the journal’s preferred style, while keeping the DOI and arXiv ID unchanged.

## PAPER-PER-M2 – Lue–Wang–Kamionkowski metadata

The Lue, Wang & Kamionkowski paper is real and correctly matched to arXiv:astro-ph/9812088 and Phys. Rev. Lett. 83, 1506–1509 (1999), but the citation omits the page range and slightly compresses the title (missing “Interactions” plural) compared to the journal version.[1]  
Fix: Change the title to exactly “Cosmological Signature of New Parity-Violating Interactions” and give the full page range “1506–1509” in the Phys. Rev. Lett. citation.

## PAPER-PER-min1 – DESIVAST reference details

The DESIVAST void catalog is correctly cited as Douglass et al. (DESI Collaboration), ApJ 982, 38 (2025) with arXiv:2411.00148 and DOI 10.3847/1538‑4357/adb559, but the paper text and bibliography conflate “DESIVAST: Catalogs of Low-Redshift Voids…” with “DESIVAST: A Catalog…” (singular/plural mismatch vs. the arXiv/journal title).[5]  
Fix: Align the bibliography entry and in-text mentions to the exact published title string from ApJ/arXiv; if the authors or journal adjusted it during review, follow the final ApJ version.

## PAPER-PER-min2 – T-Web DESI DR1 citation

The T-Web DESI DR1 paper is real and correctly matched to arXiv:2604.02463 with the title “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” but in the prose you describe it generically as “Cosmic-web quenching with DESI DR1: T-Web environments…” and as “submitted to MNRAS,” whereas the arXiv record notes submission to JCAP and includes the full title.[2]  
Fix: Update the in-text description to use the exact title string and correct target journal (JCAP) from the arXiv record, or leave the journal unspecified (“submitted”) if you want to avoid future drift.

## PAPER-PER-nit1 – ASTRA DESI EDR catalog wording

The ASTRA paper is correctly cited as Zapata-Zuluaga et al. (2026), “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” arXiv:2604.01456, but you describe it as “the first public DESI cosmic-web catalog” without qualifying that it is EDR‑only, while the arXiv abstract is careful to say “first public cosmic-web environment catalog built on any DESI data release” and to limit scope to DESI EDR rosettes.[4]  
Fix: Slightly tighten the wording to “the first public DESI EDR cosmic-web environment catalog” or similar, explicitly tying the “first” claim to EDR and not implying DR1-wide coverage.
