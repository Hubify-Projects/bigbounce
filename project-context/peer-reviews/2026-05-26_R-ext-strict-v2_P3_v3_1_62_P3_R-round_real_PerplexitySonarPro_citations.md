# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict-v2_P3_v3_1_62
**Wall time**: 21.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=68030, completion=1319, total=69349

---

## PAPER-PER-B1 – Mis-cited Liang et al. (dataset and rate)

**Grade:** MAJOR  

**Location:** Intro, para 2: “Liang et al. (2023)… approximately 250,000 DESI EDR spectra, finding 2,685 anomalies at a 1.07% rate.”  

**Issue:** Liang et al. analyze DESI BGS galaxies in EDR and present 2,685 outliers, but they do not quote a 1.07% rate nor a “250,000 EDR spectra” phrasing; the paper describes “Bright Galaxy Survey (BGS) dataset from the DESI Early Data Release” without that specific sample size or percentage. [1]  

**Fix:** Rephrase to something directly supported, e.g. “Liang et al. (2023) analyzed DESI BGS galaxies in EDR with an autoencoder+normalizing-flow pipeline and identified 2,685 outliers,” dropping the specific 250k/1.07% claims or adding an explicit note that those figures are derived from their public catalog, not quoted in the paper.


## PAPER-PER-M2 – Mis-description of Baron & Poznanski 2017 scope

**Grade:** minor  

**Location:** Intro, para 2: “Baron & Poznanski demonstrated the approach on SDSS spectra, identifying unusual white dwarfs, cataclysmic variables, and previously unclassified objects.”  

**Issue:** Baron & Poznanski (2017) develop an outlier algorithm and apply it to >2M SDSS galaxy spectra, highlighting extreme emission-line galaxies, lenses, galaxies with unusual continua, etc.; the abstract does not emphasize white dwarfs or cataclysmic variables, and focuses on galaxies. [2]  

**Fix:** Align the description with their own wording, e.g. “Baron & Poznanski (2017) applied an outlier-detection algorithm to over two million SDSS galaxy spectra, finding objects with extreme emission lines, unusual continua, galaxy–galaxy lenses, and other peculiar galaxies.”


## PAPER-PER-m3 – SPHEREx citation fine but wording drifts

**Grade:** minor  

**Location:** Intro, para 2 and §5 (SPHEREx description and capabilities).  

**Issue:** The citation to Doré et al. 2014/2015 and the basic description of SPHEREx as an all-sky spectroscopic mission are correct, but the text attributes fairly specific “3–5σ” detectability ranges for a particular \(\fnl\) value without those exact numbers appearing in the SPHEREx paper itself (which focuses on broader forecasts rather than this exact scenario). [3]  

**Fix:** Soften to “SPHEREx forecasts suggest \(\sigma_{f_{\rm NL}}\lesssim 1\) for local-type non-Gaussianity in optimistic scenarios,” and clearly attribute the 3–5σ for the particular bounce model as this paper’s own Fisher estimate anchored to SPHEREx survey parameters, not as a direct SPHEREx-team claim.


## PAPER-PER-m4 – Munchmeyer et al. forecast range slightly off

**Grade:** minor  

**Location:** Intro, para 2: “Münchmeyer et al. consensus \(\sigma_{f_{\rm NL}} \approx 0.4–0.9\) for SPHEREx-class surveys.”  

**Issue:** Münchmeyer et al. (2019) forecast \(\sigma_{f_{\rm NL}}\sim 0.5\) for CMB-S4×LSST kSZ tomography, not a 0.4–0.9 “consensus” range for SPHEREx-class galaxy surveys; the mapping to “SPHEREx-class” is your extrapolation, not their claim. [4]  

**Fix:** Reword as “Münchmeyer et al. (2019) find \(\sigma_{f_{\rm NL}}\sim 0.5\) for CMB-S4×LSST kSZ tomography; our internal Fisher tests are tighter than this by a factor of a few under optimistic assumptions,” and drop “SPHEREx-class” from the attribution to them.


## PAPER-PER-m5 – Nicolaou et al. (2026) status and details

**Grade:** minor  

**Location:** Intro, para 2: “Nicolaou et al. (2026)… extended this with a variational autoencoder and Astronomaly on 208,000 EDR spectra.”  

**Issue:** As of now there is no publicly indexed “Nicolaou et al. 2026” DESI anomaly paper with those exact numbers in ADS/astro‑ph; the project (Astronomaly + DESI) has been discussed but the specific year, sample size and method combination look forward‑projected rather than tied to a citable publication. (No matching arXiv entry appears under the authors + DESI anomaly detection.)  

**Fix:** Either update to a real arXiv/ADS reference with correct year/title/sample size once it exists, or relabel this as “in prep.” without concrete numbers, e.g. “Nicolaou et al., in preparation, apply a variational autoencoder with Astronomaly to DESI EDR spectra,” and remove the 208,000 and detailed method claim until it is formally published.


## PAPER-PER-n6 – “Nicolaou et al. 2026” in bibliography

**Grade:** nit  

**Location:** Bibliography entry “Nicolaou et al. 2026” (no arXiv/journal details).  

**Issue:** The bib item has no arXiv ID, journal, or clear title, which makes it non-resolvable and reinforces the impression that it is a projected reference rather than a published work.  

**Fix:** Either (a) replace with an arXiv/journal entry once available, or (b) mark it explicitly as “in preparation” or “private communication” and remove the year “2026” from the citation key so it is not misread as a published 2026 paper.
