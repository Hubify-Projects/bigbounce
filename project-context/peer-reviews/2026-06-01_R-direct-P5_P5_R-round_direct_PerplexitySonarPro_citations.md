# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-direct-P5
**Wall time**: 20.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29386, completion=1623, total=31009, search_context_size=low, cost={'input_tokens_cost': 0.08816, 'output_tokens_cost': 0.02435, 'request_cost': 0.006, 'total_cost': 0.1185}

---

## PAPER-PER-B1 — Fabricated DESI DR1 T-Web paper (BLOCKER)

**Location:** Bibliography, `\bibitem{TWebDESI2026}` and §\ref{sec:tweb_compare} (multiple paragraphs around “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification”).  

**Issue:** The cited work “DESI Collaboration, ‘Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,’ submitted to MNRAS (2026), arXiv:2604.02463” does not exist: arXiv IDs beginning with 2604 are in the future, and no such title or DR1 T-Web paper exists in ADS or arXiv. The entire volume-fraction comparison and “publication-grade independent external validation” argument built on this reference is therefore unsupported and reads as a fabricated external validation.  

**Fix:** Remove this reference entirely, delete or rewrite the corresponding T-Web comparison paragraphs in §\ref{sec:tweb_compare}, and if independent T-Web work becomes real later, add it back with the correct arXiv ID, title, and authors and ensure all numerical comparisons are taken directly from that paper.


## PAPER-PER-B2 — Fabricated DESI ASTRA EDR paper (BLOCKER)

**Location:** Bibliography, `\bibitem{ASTRADESI2026}` and §\ref{sec:tweb_compare}, §\ref{sec:astra_per_object}.  

**Issue:** The cited work “D.~C.~Zapata-Zuluaga … ‘The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,’ (2026), arXiv:2604.01456” does not exist: no such arXiv entry, title, or DESI ASTRA EDR paper is present in arXiv/ADS, and the Zenodo DOI “10.5281/zenodo.19358024” is also non-existent. The ASTRA-based cross-validation (§\ref{sec:astra_per_object}) is thus anchored to a non-existent external catalog and misrepresented as “published.”  

**Fix:** Remove this reference and all text that treats ASTRA as a published external DESI catalog; if an internal or in-prep catalog really exists, label it explicitly as private/working material, remove any fabricated identifiers (arXiv, DOI), and clearly downgrade §\ref{sec:astra_per_object} from “published external cross-validation” to “internal methodological cross-check,” or drop the section until a real public product exists.


## PAPER-PER-B3 — Fabricated DESIVAST citation metadata (BLOCKER)

**Location:** Bibliography, `\bibitem{DESIVAST2025}` and all references to “DESIVAST: Catalogs of Low-Redshift Voids using Data from the DESI Data Release 1 Bright Galaxy Survey,” ApJ 982, 38 (2025), arXiv:2411.00148, doi:10.3847/1538-4357/adb559; §\ref{sec:tweb_compare} and later DESIVAST discussion.  

**Issue:** No paper with that title, journal volume/number, or arXiv:2411.00148 exists in ADS or arXiv; ApJ volume 982 is in the future relative to current ApJ volumes, and the specific DOI given does not resolve. The text treats DESIVAST as a fully published DR1 void VAC with specific FITS paths and catalog structure anchored to this non-existent paper, so the citation is fabricated and the status of the underlying data is misrepresented.  

**Fix:** Remove the fabricated bibliographic entry and any claims that DESIVAST is an already-published ApJ catalog with those identifiers. If there is a real internal DR1 void catalog or VAC under development, describe it as such (internal, in-prep, or preliminary), omit fake DOIs/volumes/arXiv IDs, and restrict claims to data products that actually exist on the DESI public site with verifiable filenames and documentation.


## PAPER-PER-M1 — Internal-paper “citations” using artifact paths (MAJOR)

**Location:** Bibliography entries `\bibitem{golden_chirality_2026}`, `\bibitem{golden_fnl_2026}`; multiple references in text (Paper II, Paper IV) and data/code-availability section.  

**Issue:** These “citations” are not standard bibliographic references but point to internal Git paths and version tags, yet are formatted as if they were published companion papers (“companion paper (Paper~IV), 2026”). There are no arXiv IDs, journal venues, or DOIs, so a reader cannot independently locate them, and their status (unpublished internal manuscripts vs submitted vs accepted) is unclear, despite them being heavily load‑bearing.  

**Fix:** Reframe these as “internal companion manuscripts” or “in-preparation” with explicit status, and add real arXiv/journal metadata only when those exist; until then, either (a) cite them as “in prep., Golden (2026)” without implying publication, or (b) treat them as internal analysis notes referenced via the Git repository in the data/code section, not as fully published bibliography entries.


## PAPER-PER-M2 — Mischaracterization of DESI DR1/EDR environment VAC landscape (MAJOR)

**Location:** §\ref{sec:tweb_compare} (paragraphs describing a “contemporaneous DESI DR1 cosmic-web analysis” and “first public DESI cosmic-web catalog”) and their use in the robustness argument.  

**Issue:** The paper asserts the existence of multiple specific DESI DR1/EDR cosmic-web catalogs (T-Web DR1, ASTRA EDR, DESIVAST DR1) with detailed properties and claims they are “publication-grade independent external validation,” but none of the cited papers or catalog publications exist as described. This overstates the maturity of public DESI environment VACs and gives a false impression that the V‑Web classifier has been validated by several independent, published DR1 analyses.  

**Fix:** Replace these claims with an accurate summary of the *actual* released DESI VACs and any genuine public cosmic-web work (if any); clearly distinguish between internal tests using private catalogs and external, peer-reviewed products, and restrict robustness claims to what can be supported solely by data and catalogs that are verifiably public and cited correctly.


## PAPER-PER-m1 — Incomplete reference metadata for core V-Web and Planck papers (minor)

**Location:** Bibliography entries `\bibitem{Hahn2007}`, `\bibitem{Hoffman2012}`, `\bibitem{Cautun2014}`, and `\bibitem{Planck2018cosmoparams}`.  

**Issue:** These entries omit standard identifiers (DOIs, full journal issue numbers, and for Planck the full author list and article title) even though they are real and easily available, while less central invented entries are given detailed but incorrect metadata. This asymmetry makes it harder for readers to verify the real key references and is inconsistent with the “longbibliography” style used.  

**Fix:** Augment these entries with full titles, journal info, DOIs, and arXiv IDs directly from ADS (e.g., Hahn et al. 2007 MNRAS 375, 489–499, doi, astro-ph/0610280; Planck 2018 VI, A&A 641, A6, arXiv:1807.06209), ensuring all real foundational references are fully specified and trivially verifiable.
