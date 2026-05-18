# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1640pt_P3_v3154_R16
**Wall time**: 28.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=65386, completion=1183, total=66569

---

## PAPER-PER-B1 — Liang et al. scaling, survey description

**Severity:** MAJOR  

The paper repeatedly cites “Liang et al. (2023)” as working on “approximately 250,000 DESI Early Data Release spectra, finding 2,685 anomalies at a 1.07% rate,” and as “the largest prior single-survey spectroscopic anomaly catalog.” (abstract, Introduction). In reality, Liang et al. 2023 analyze the DESI **Bright Galaxy Survey (BGS) subset** of EDR with  **∼270k** BGS galaxy spectra and 3,275 outliers (most prominent set is 400 objects) and do not quote a simple “2,685 at 1.07%” headline nor position themselves as a generic “largest spectroscopic anomaly catalog” in that way. [1]  

**Fix:** Recheck Liang et al. and replace all numerical claims and “largest prior single-survey spectroscopic anomaly catalog” language with values and wording that match their BGS-only scope and quoted counts, clearly flagging that their sample is BGS galaxies, not “DESI EDR spectra” in general.  


## PAPER-PER-M1 — Nicolaou et al. 2026 reference

**Severity:** MAJOR  

The paper cites “Nicolaou et al. 2026 ... on 208,000 EDR spectra” as a published extension using a VAE and Astronomaly (Introduction). No such 2026 paper is currently indexed under Nicolaou with DESI EDR anomaly detection or Astronomaly; “Nicolaou et al. 2026” appears to be either unpublished, misdated, or conflated with other anomaly work. [2]  

**Fix:** Verify whether this is an accepted but not-yet-published manuscript, a different first author, or a mis-citation; either (a) replace with a real, citable arXiv/journal reference, (b) clearly label it as “in preparation / private communication” without year and arXiv ID, or (c) delete the reference.  


## PAPER-PER-M2 — UMAP / HDBSCAN citations and parameter discussion

**Severity:** minor  

UMAP is correctly cited to McInnes et al. 2018, arXiv:1802.03426, but the text calls it “UMAP~[McInnes2018]” and describes configuration details; there is no ADS or arXiv ID printed in the current excerpt, and HDBSCAN is cited only as “McInnes et al. 2017” without full metadata. The UMAP arXiv entry has full title and details that should be reflected. [2]  

**Fix:** Ensure the bibliography entry for UMAP includes full title, arXiv ID 1802.03426, and correct venue, and that HDBSCAN has its JOSS citation; check that the text’s claims about UMAP’s properties (global-structure preservation, etc.) align with the abstract of McInnes et al. rather than paraphrasing beyond it. [2]  


## PAPER-PER-M3 — NANOGrav / EPTA / new-physics references

**Severity:** minor  

The paper references the NANOGrav 15-year new-physics paper “Afzal et al. 2023 NewPhys” and the EPTA DR2 GWB detection as context for its PTA analysis. The arXiv entries confirm: Antoniadis et al. 2023, arXiv:2306.16214 (EPTA DR2 GWB) and Afzal et al. 2023, arXiv:2306.16219 (NANOGrav 15-year new-physics analysis). [3]  

**Fix:** Make sure the bib entries match these exact author lists, titles, and arXiv IDs (including journal references A&A 678 A50 and ApJL “Search for Signals from New Physics”), and that no older preprint IDs or provisional titles are still present in the .bib file. [3]  


## PAPER-PER-n1 — ADS / arXiv cross-check on Liang metadata

**Severity:** nit  

Your text implies Liang et al. is “Liang et al. 2023, MNRAS 525, 1078” with arXiv:2307.07664, which matches the ADS entry “Outlier Detection in the DESI Bright Galaxy Survey” and author list (Liang, Melchior, Hahn, Shen, Goulding, Ward). [1]  

**Fix:** Just verify the journal volume/page (MNRAS 525, 1078–1092) and ensure the year is 2023 consistently throughout (no “2024” slips). [1]  


## PAPER-PER-n2 — Cross-field arXiv collision (1711.00525)

**Severity:** nit  

If 1711.00525 is used anywhere in your unseen .bib as a placeholder for a clustering or anomaly paper, note that arXiv:1711.00525 is actually “Internet of Cloud: Security and Privacy issues” (Cook et al.), a CS security chapter unrelated to cosmology or ML anomaly detection. [2]  

**Fix:** Grep your .bib / source for “1711.00525”; if it was meant to be an anomaly/ML reference, replace with the correct arXiv ID, otherwise remove the entry to avoid accidental, irrelevant citation.
