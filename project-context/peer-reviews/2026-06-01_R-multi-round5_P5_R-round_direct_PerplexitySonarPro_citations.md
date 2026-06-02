# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round5
**Wall time**: 16.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34823, completion=1439, total=36262, search_context_size=low, cost={'input_tokens_cost': 0.10447, 'output_tokens_cost': 0.02159, 'request_cost': 0.006, 'total_cost': 0.13205}

---

## PAPER-PER-B1 — Shamir 2022 journal metadata and DOI

**Severity:** MAJOR  

**Location:** Bibliography entry `\bibitem{Shamir2022DESI}`  

**Issue:** The paper correctly cites Shamir (2022) as “Analysis of spin directions of galaxies in the DESI Legacy Survey” in MNRAS 516, 2281 (2022) with DOI `10.1093/mnras/stac2372`. That is an actual paper and DOI on arXiv:2208.13866, but the in-text discussion repeatedly frames Shamir 2022 as the prior “large-scale asymmetry” detection at the few‑percent level, whereas the cited MNRAS paper is focused on DESI Legacy Survey morphology/spin analysis and does not present the same specific cosmological‑parity claim as Shamir’s earlier SDSS‑based works. The paper is using the correct citation metadata for a different Shamir paper than the one historically associated with the claimed anomaly.  

**Fix:** Explicitly verify, from the MNRAS article text, what amplitude and type of asymmetry it reports; if it does not match the 2–4% large‑scale parity violation claim being contrasted to Paper IV, either (a) replace this citation with the correct Shamir paper that actually makes that claim, with its proper journal/DOI/arXiv metadata, or (b) narrow the comparison text in §XIII.C to match what Shamir 2022 MNRAS actually states and add an additional, correctly cited reference for the older SDSS‑based anomaly if needed.


## PAPER-PER-M1 — DESIVAST author list and collaboration tag

**Severity:** MAJOR  

**Location:** Bibliography `\bibitem{DESIVAST2025}` and multiple mentions in §X, §XII  

**Issue:** The DESIVAST void catalog is correctly identified as arXiv:2411.00148, ApJ 982, 38 (2025) with first author Hernán Rincon and title “DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey.” However, the bib item and prose intermittently refer to “DESIVAST (DESI Collaboration)” and treat it as a DESI‑collaboration product; the arXiv and ApJ versions list Rincon et al. without “DESI Collaboration” in the author line and describe it as a DESI‑based project, not a collaboration‑branded paper.  

**Fix:** Remove “(DESI Collaboration)” from the DESIVAST reference and from any prose that implies formal DESI‑collab authorship; keep the correct Rincon‑et‑al. author list and describe DESIVAST as a DR1 BGS void catalog built on DESI data, not an official DESI‑Collaboration paper, unless the published version explicitly includes the collaboration tag.


## PAPER-PER-M2 — ASTRA DESI EDR catalog description

**Severity:** MAJOR  

**Location:** §“Concurrent-literature DR1/EDR cosmic-web cross-validation”, citation `\bibitem{ASTRADESI2026}`  

**Issue:** The paper cites arXiv:2604.01456 as “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog” by Zapata‑Zuluaga et al., which matches the real arXiv title and author list. But the text further claims that “ASTRA is published only on EDR while our V-Web run is on DR1; the ∼175 deg² EDR rosettes are contained within the DR1 footprint” and that ASTRA is “the first public DESI cosmic-web catalog,” implicitly treating it as a finalized public VAC. In the actual preprint, ASTRA is an EDR analysis still at pre‑DR1 scope and, as of now, is not released as a DR1‑wide value‑added catalog in the DESI public data system in the way vacuum terminology “first public DESI cosmic-web catalog” suggests.  

**Fix:** Rephrase to describe ASTRA strictly as an EDR‑based probabilistic environment catalog from Zapata‑Zuluaga et al. on the EDR rosettes, avoiding “first public DESI cosmic-web catalog” language and any implication that it is a DR1‑wide official VAC; clearly distinguish EDR‑scale preprint products from DR1-level public value‑added catalogs.


## PAPER-PER-M3 — T-Web DESI DR1 volume-fraction comparison

**Severity:** minor  

**Location:** §“Concurrent-literature DR1/EDR cosmic-web cross-validation”, `\bibitem{TWebDESI2026}`  

**Issue:** arXiv:2604.02463 by Ullah, Awais, Matos & Suárez‑Pérez is correctly cited in metadata (title, ID, author list). The text, however, quotes T‑Web DR1 in‑footprint volume fractions as “{0.06–0.16, 0.45–0.48, 0.37–0.40, 0.04–0.06} (ranges across the three BGS/LRG/ELG tracer samples)” without a direct reference to the exact table/figure, and the numeric ranges do not obviously match a single table’s quoted values in the current preprint. This is likely an approximate blend of several numbers.  

**Fix:** Check the latest arXiv version of Ullah et al.; if those ranges are not explicitly present, either (a) replace them with the exact fractions as given in a specified table/figure (with an explicit citation to that table), or (b) mark them clearly as approximate values computed “in this work” from the authors’ public catalog, rather than as direct textual quotes from the paper.


## PAPER-PER-m1 — DESI DR1 zall-pix-iron path formatting

**Severity:** nit  

**Location:** §II.B (“DESI Data Release 1”)  

**Issue:** The path `https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/` is a real DR1 location, but `zall-pix-iron.fits` is not literally present at that top-level URL; the actual DR1 layout nests zcatalogs under subdirectories per healpix or tile, so the naked URL in the text is slightly misleading as a direct file location.  

**Fix:** Clarify the description to say that `zall-pix-iron.fits` is fetched from the DR1 spectro/redux/iron zcatalog tree (with subdirectories) rather than implying that the file itself lives exactly at the shown URL; optionally give the precise relative path used by the script, as documented in the repository.
