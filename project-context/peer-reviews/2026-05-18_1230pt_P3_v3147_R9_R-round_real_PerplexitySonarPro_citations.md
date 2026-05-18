# P3_v3147_R9 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1230pt
**Wall time**: 21.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=62449, completion=590, total=63039

---

## PAPER-PER-B1 — Liang et al. 2023 citation

**Issue.** In the abstract and elsewhere, the paper cites “Liang et al. (2023)” as an autoencoder+normalizing-flow anomaly search on DESI EDR that finds 2,685 anomalies from ≈250,000 spectra at a 1.07% rate.[1] The arXiv paper actually titled *“Outlier Detection in the DESI Bright Galaxy Survey”* uses DESI BGS EDR galaxies and finds 641 outliers at a 0.26% rate; the sample size, anomaly count, and fraction do not match the numbers quoted here.[1]  

**Fix.** Either (a) correct the description to match Liang et al. (*Bright Galaxy Survey*, 641 outliers, 0.26%) and adjust all scale-ratio statements, or (b) explicitly state that the 2,685 / 1.07% figures come from a different internal DESI anomaly run and not from Liang et al., and remove the implication that those numbers are taken from Liang+2023.

---

## PAPER-PER-M1 — Liang et al. 2023 scope / terminology

**Issue.** The text calls Liang’s work “the largest prior single-survey spectroscopic anomaly catalog” and refers to “DESI EDR” generally, whereas the cited paper is specifically the DESI **Bright Galaxy Survey** subset of EDR, not the full spectroscopic EDR, and it is framed as a BGS outlier search rather than a general “spectroscopic anomaly catalog.”[1]  

**Fix.** Rephrase to: “Liang et al. (2023) performed an outlier search in the DESI Bright Galaxy Survey (BGS) Early Data Release, identifying 641 outliers out of ≈250,000 BGS spectra (0.26%); our catalog exceeds that sample in scale by …”, and avoid presenting their result as the global “largest spectroscopic anomaly catalog” without checking more recent literature.

---

## PAPER-PER-M2 — SPHEREx citation details

**Issue.** The SPHEREx reference is cited as “SPHEREx 2014” with shorthand “SPHEREx satellite,” but the actual arXiv entry is *“Cosmology with the SPHEREX All-Sky Spectral Survey”* (Doré et al. 2014, arXiv:1412.4872) and describes a proposed NASA MIDEX mission; the text does not give the correct title or authorship and may be read as referring to an already-launched satellite.[0]  

**Fix.** Update the citation to “Doré et al. 2014, *Cosmology
