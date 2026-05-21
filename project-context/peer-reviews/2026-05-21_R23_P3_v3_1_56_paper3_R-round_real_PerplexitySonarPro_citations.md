# paper3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R23_P3_v3_1_56
**Wall time**: 24.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=66764, completion=1282, total=68046

---

## PAPER-PER-B1 – Mis-cited Nicolaou et al.

**Grade:** MAJOR  

**Location:** Introduction, para 2 (“Nicolaou et al. [Nicolaou2026] … on 208,000 EDR spectra.”)  

**Issue:** There is currently no arXiv or journal paper matching “Nicolaou et al. 2026” on DESI EDR spectra with Astronomaly; the bibliography entry is also missing in the provided reference list, and web search finds no such work. This looks like a forward‑dated or confabulated citation.  

**Fix (1–2 sentences):** Either (a) remove this citation and sentence entirely, or (b) replace it with a confirmed, published Nicolaou/Astronomaly reference that actually exists, including correct authors, year, title, and arXiv ID, and adjust the text so it accurately describes that paper’s sample and method.  


## PAPER-PER-M1 – Liang et al. citation underspecified / slightly off

**Grade:** minor  

**Location:** Introduction, para 2 (“Liang et al. [Liang2023] … approximately 250,000 DESI Early Data Release (EDR) spectra, finding 2,685 anomalies at a 1.07% rate.”)  

**Issue:** The paper being referenced is clearly arXiv:2307.07664, “Outlier Detection in the DESI Bright Galaxy Survey,” which does analyze DESI BGS EDR and finds 2,685 outliers, but the text does not give the arXiv ID and the current reference list gives only a generic “Liang et al. (2023)” entry without title or e-print. The numerical description is broadly consistent but not explicitly tied to the correct BGS‑EDR sample as described by the authors.[1]  

**Fix (1–2 sentences):** Update the bibliography entry for Liang et al. to include the full title “Outlier Detection in the DESI Bright Galaxy Survey,” arXiv:2307.07664, and explicitly mention in the main text that this is a BGS EDR sample so that the scope and citation unambiguously match the actual paper.[1]  


## PAPER-PER-M2 – SPHEREx reference outdated / incomplete

**Grade:** minor  

**Location:** Introduction, para 2 (“SPHEREx satellite [SPHEREx2014] …”)  

**Issue:** The cited SPHEREx reference is clearly arXiv:1412.4872, “Cosmology with the SPHEREX All-Sky Spectral Survey,” which is correctly described as an all‑sky spectroscopic mission, but the bibliography lacks the explicit arXiv identifier and DOI, and the text calls it a “proposed” satellite even though the mission has since been formally adopted and the 2014 paper is a concept/forecast document.[2]  

**Fix (1–2 sentences):** In the references, give the full citation including arXiv:1412.4872 and its title; in the text, clarify that you are using the 2014 SPHEREx cosmology forecast paper and, if desired, update the wording from “proposed” to “mission concept paper (2014)” to match the cited document’s status.[2]  


## PAPER-PER-M3 – UMAP citation slightly malformed

**Grade:** nit  

**Location:** SDSS section and Appendix galleries (“UMAP [McInnes2018] …”)  

**Issue:** The method clearly corresponds to arXiv:1802.03426, “UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction,” but the cited year “2018” without arXiv ID or full title is ambiguous; UMAP is primarily known via that arXiv preprint, and the reference list omits the explicit identifier.[4]  

**Fix (1–2 sentences):** Amend the UMAP reference to give the full title and arXiv:1802.03426, and ensure the in‑text citation matches (e.g., “McInnes et al. (2018, arXiv:1802.03426)”).[4]  


## PAPER-PER-M4 – ADS/arXiv linkage missing for SPHEREx & Liang anchors

**Grade:** nit  

**Location:** References section, entries “Liang et al. (2023)” and “SPHEREx2014”  

**Issue:** Both the Liang DESI outlier paper and the SPHEREx cosmology paper are primary quantitative anchors in the abstract and conclusions, but their references currently omit arXiv identifiers and DOIs; for arXiv:2307.07664 and arXiv:1412.4872 these are standard and should be present for reproducibility.[1][2]  

**Fix (1–2 sentences):** Add the arXiv IDs and DOIs for both Liang et al. (arXiv:2307.07664) and SPHEREx (arXiv:1412.4872) in the bibliography so readers can verify the numerical comparisons and forecasts directly.[1][2]  


## PAPER-PER-M5 – “Nicolaou2026” label should be clearly marked as in‑prep or removed

**Grade:** nit  

**Location:** Introduction, para 2; references list (absence of a matching entry)  

**Issue:** Beyond being currently unresolvable as a published paper, the “Nicolaou2026” label is formatted like a standard literature citation, which will mislead readers into thinking there is an accessible arXiv or journal article when there is not.[3]  

**Fix (1–2 sentences):** If this refers to ongoing work, relabel it explicitly as “Nicolaou et al., in preparation” (without a numeric year tag that suggests publication) and remove it from the numbered/bibkey list used for published papers; otherwise, delete the citation until the work is publicly available.[3]
