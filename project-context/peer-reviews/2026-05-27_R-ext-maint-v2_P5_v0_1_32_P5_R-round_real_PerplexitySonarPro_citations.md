# P5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-27_R-ext-maint-v2_P5_v0_1_32
**Wall time**: 23.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29379, completion=1377, total=30756

---

## PAPER-PER-B1 — Self-cites used as external references (BLOCKER)

The “concurrent-literature DR1/EDR cosmic-web cross-validation” section repeatedly treats the DESI T-Web, DESIVAST, and ASTRA catalogs as independent external works, but then cites them as \bibitem{TWebDESI2026}, \bibitem{ASTRADESI2026}, and \bibitem{DESIVAST2025} with author lists and titles that do not match the actual arXiv metadata and appear to be placeholders or fused from internal VAC nicknames plus the first author only.[3] In reality, the DESI void catalog is Douglass et al. 2025 (ApJ 982, 38), and the ASTRA/EDR paper is Zapata-Zuluaga et al. 2026 (arXiv:2604.01456), with very specific titles different from those in the bibliography.[3]  
**Fix:** Replace all placeholder-style citations with the real bibliographic entries (full author list as per journal style, exact titles, correct arXiv IDs and DOIs), and make crystal clear in the text which external paper is DESI collaboration vs independent, using the actual author order and names.

---

## PAPER-PER-M1 — Mislabeling DESI T-Web paper as “DESI Collaboration” (MAJOR)

The text describes \cite{TWebDESI2026} as “DESI Collaboration, ‘Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,’ submitted to MNRAS (2026), arXiv:2604.02463.”[3] The actual arXiv entry 2604.02463 is authored by Ullah, Awais, Matos, and Suárez-Pérez, with no DESI Collaboration designation and the same title, in the astro-ph.GA category.[3]  
**Fix:** Change the reference label and in-text description to match the real authorship (Ullah et al., not “DESI Collaboration”), keep the correct title and arXiv:2604.02463, and avoid implying that this is an official DESI-collaboration data release unless that is explicitly stated in the paper itself.

---

## PAPER-PER-M2 — ASTRA citation metadata incomplete / partly confabulated (MAJOR)

\bibitem{ASTRADESI2026} is described in the text as “Zapata-Zuluaga et al. 2026, the first public DESI cosmic-web catalog” with a parenthetical “Zenodo 10.5281/zenodo.19358024,” but the bibliography entry only gives an informal title and year, and omits the arXiv identifier 2604.01456 and the real abstracted title text (“The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog”).[3] The current mixture of label, description, and venue is under-specified and looks like stitched metadata.  
**Fix:** Replace this with a proper citation to Zapata-Zuluaga et al., “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” arXiv:2604.01456 (astro-ph.CO), adding the Zenodo DOI only if actually present in that paper, and ensure the year and subject tags match the arXiv record.

---

## PAPER-PER-m1 — Tempel+2014 reference is correct but minimally formatted (minor)

The Tempel et al. 2014 group catalog is correctly identified by author list, title (“Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation”), journal (A&A 566, A1), and arXiv:1402.1350.[2] However, the in-text phrase “Tempel+2014 SDSS DR10 FoF catalog INGESTED from CDS VizieR J/A+A/566/A1” is informal and not obviously tied to the formal reference entry.  
**Fix:** Keep the existing correct bibitem, but add an explicit “see Tempel et al. (2014, A&A 566, A1, arXiv:1402.1350)” at first use, and consider clarifying “Tempel+2014 FoF” as the short-name mapping to that citation.

---

## PAPER-PER-m2 — Cautun et al. 2014 used as “V‑Web” authority (minor)

\bibitem{Cautun2014} correctly cites Cautun et al., “Evolution of the cosmic web,” MNRAS 441, 2923, arXiv:1401.7866.[2] The text sometimes calls the classifier “V-Web tidal-tensor classifier (Hahn et al. 2007; Hoffman et al. 2012; Cautun et al. 2014) … Cautun et al. geometric default \(\lambda_{\rm th}=0\),” which is broadly consistent with usage but slightly overstates Cautun et al. as defining a unique “geometric default” for this exact implementation.[2]  
**Fix:** Slightly rephrase to “following the commonly used choice \(\lambda_{\rm th}=0\) (e.g. Cautun et al. 2014)” to avoid implying that Cautun et al. uniquely define the specific V‑Web implementation used here.

---

## PAPER-PER-n1 — Alexander & Yunes and Lue–Wang–Kamionkowski citations (nit)

The Alexander & Yunes review and the Lue–Wang–Kamionkowski PRL are cited with accurate titles, journal info, DOIs and arXiv IDs: “Chern–Simons modified general relativity,” Phys. Rep. 480, 1 (2009), arXiv:0907.2562, and “Cosmological signature of new parity-violating interactions,” Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088.[1] The text’s discussion of these works as examples of parity-violating gravity / cosmology is consistent with their abstracts.[1]  
**Fix:** None required for correctness; optionally add subject tags (hep-th / astro-ph.CO) in the bibitem to ease discoverability.
