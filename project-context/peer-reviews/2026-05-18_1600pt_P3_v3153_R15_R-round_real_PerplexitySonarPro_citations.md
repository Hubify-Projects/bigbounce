# P3_v3153_R15 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1600pt
**Wall time**: 29.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=65307, completion=1292, total=66599

---

## PAPER-PER-B1 — Wrong reference for “Baron & Poznanski 2017”

**Location:** Introduction, paragraph 2: “Baron & Poznanski~\cite{Baron2017} demonstrated the approach on SDSS spectra, identifying unusual white dwarfs, cataclysmic variables, and previously unclassified objects.”  

**Issue:** The cited paper 2017MNRAS.465.4530 (“The weirdest SDSS galaxies: results from an outlier detection algorithm”) is about galaxy spectra and does not focus on unusual white dwarfs or cataclysmic variables as headline results; it describes a galaxy outlier search in SDSS, not the stellar classes claimed here.  

**Fix (MAJOR):** Rephrase the sentence to match the paper’s actual content, e.g. “demonstrated the approach on SDSS galaxy spectra, identifying extreme-emission-line and unusual-continuum galaxies, gravitational lenses, and other peculiar systems,” or replace the citation with a stellar-focused anomaly paper that really highlights white dwarfs and cataclysmic variables.

---

## PAPER-PER-B2 — Liang et al. metadata and rate consistency

**Location:** Introduction, paragraph 2: “Liang \etal~\cite{Liang2023} applied an autoencoder coupled with a normalizing flow to approximately 250{,}000 DESI Early Data Release (EDR) spectra, finding 2{,}685 anomalies at a 1.07\% rate.”  

**Issue:** The cited paper “Outlier Detection in the DESI Bright Galaxy Survey” (Liang et al. 2023, arXiv:2307.07664) does use an autoencoder plus normalizing flow on DESI BGS EDR, but the abstract describes the outliers qualitatively and does not front‑page a “2,685 anomalies at 1.07%” figure.[1] That specific count and rate look like numbers from the current paper, not from Liang’s, so attributing them directly to Liang et al. is likely inaccurate.  

**Fix (MAJOR):** Either (a) explicitly say these numbers are from your own reproduction on a Liang-style setup and not from their paper, or (b) check Liang et al.’s text/tables and adjust the quoted anomaly count and percentage to exactly match what they actually report, clarifying that the “~250,000 BGS EDR” dataset is their Bright Galaxy Survey sample.

---

## PAPER-PER-M1 — UMAP citation is correct but incomplete

**Location:** Sec. 3, SDSS DR18 clustering (UMAP + HDBSCAN): text cites “UMAP~\cite{McInnes2018}.”  

**Issue:** The UMAP paper is correctly cited as McInnes, Healy & Melville, arXiv:1802.03426, but the description “UMAP… (McInnes et al. 2018)” is generic and omits that this is the canonical “UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction” paper; there is no outright error, but given heavy methodological reliance, it’s easy for readers to mis-track which dimensionality-reduction variant is used.[2]  

**Fix (nit):** Expand the first mention to “UMAP (Uniform Manifold Approximation and Projection for Dimension Reduction; McInnes, Healy & Melville 2018)” so the title and authors match the arXiv record unambiguously.

---

## PAPER-PER-M2 — NANOGrav “new physics” paper is fine but role should be clearer

**Location:** Sec. 5 / Sec. 6.2 and Appendix PTA MCMC: citing “NANOGrav new-physics companion paper~\cite{Afzal2023NewPhys}” and describing cosmological interpretations.  

**Issue:** The citation maps correctly to “The NANOGrav 15-year Data Set: Search for Signals from New Physics” (Afzal et al. 2023, arXiv:2306.16219; ApJL 951 L11).[3] However, your text could be read as if that paper itself endorses bounce cosmology over SMBHBs, whereas Afzal et al. emphasize Bayes factors depend strongly on SMBHB modeling and caution against interpreting them as evidence for new physics.[3]  

**Fix (minor):** Add one clarifying clause when you reference Afzal et al., e.g. “Afzal et al. (2023) show that several cosmological models can fit the data, but explicitly caution that Bayes factors favoring cosmological sources depend strongly on SMBHB modeling and should not be taken as evidence for new physics.”

---

## PAPER-PER-M3 — UMAP ADS/arXiv metadata (authors / venue) are correct

**Location:** Bibliography entry for McInnes et al. 2018.  

**Issue:** Cross‑checking against arXiv:1802.03426 confirms title, authors (Leland McInnes, John Healy, James Melville), and venue status (arXiv preprint, no journal specified) are consistent.[2] This is not an error but is a verified check.  

**Fix (nit):** None required; entry is fine. Optionally note it as an arXiv preprint in the bib entry if your style wants explicit designation.

---

## PAPER-PER-M4 — Liang et al. bibliographic metadata are correct

**Location:** Bibliography entry for \cite{Liang2023}.  

**Issue:** The paper “Outlier Detection in the DESI Bright Galaxy Survey” is correctly listed as Yan Liang et al., arXiv:2307.07664, with the Bright Galaxy Survey / DESI EDR context matching your description.[1] I found no fused title/arXiv-ID mismatch and no author/venue conflicts.  

**Fix (nit):** None needed; citation metadata and arXiv ID are consistent with the source.
