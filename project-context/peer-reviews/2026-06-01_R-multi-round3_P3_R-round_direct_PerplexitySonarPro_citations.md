# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round3
**Wall time**: 17.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79820, completion=1345, total=81165, search_context_size=low, cost={'input_tokens_cost': 0.23946, 'output_tokens_cost': 0.02018, 'request_cost': 0.006, 'total_cost': 0.26564}

---

## PAPER-PER-B1 — Mis-cited Planck 2018 non‑Gaussianity paper

**Issue (MAJOR):**  
Several places cite “Planck 2018 results. IX. Constraints on primordial non-Gaussianity” as Astron. Astrophys. **641, A9 (2020)** under the key `Planck2018IX`.[Planck 2018 IX is indeed A9, 2020.] However, in the bibliography the generic `Planck2018` key is used for “Planck 2018 results. I. Overview and the cosmological legacy of Planck”, A&A 641, A1 (2020), and there is no separate entry for the IX non‑Gaussianity paper.[Planck 2018 I is A1, 2020.] The text clearly attributes non‑Gaussianity constraints to IX but only cites I.

**Fix:**  
Add a separate bib entry for “Planck 2018 results. IX. Constraints on primordial non-Gaussianity”, Astron. Astrophys. 641, A9 (2020), and change non‑Gaussianity‑related in‑text citations to `Planck2018IX` (leaving `Planck2018`/A1 for overview/cosmology‑legacy context).

---

## PAPER-PER-M1 — DESI DR1 reference incomplete / slightly inaccurate

**Issue (minor):**  
The `DESI2025DR1` bib entry is described only as “DESI Data Release 1 documentation” without author list or year details, yet the text treats it as a formal DR1 release paper.[DESI DR1 is normally cited as DESI Collaboration, “The DESI Data Release 1”, arXiv:2404.03002 / ApJS 2024.] The citation as “2025” also does not match the 2024 publication year.

**Fix:**  
Update the DESI DR1 reference to a standard form (e.g. DESI Collaboration, “The DESI Data Release 1”, ApJS, 2024, arXiv:2404.03002) and align the year used in the text (2024 not 2025), or clearly label it as “online documentation” if you intentionally cite the docs site rather than the paper.

---

## PAPER-PER-M2 — eROSITA DR1 reference underspecified

**Issue (minor):**  
The `eROSITA_DR1` bib entry is “A. Merloni et al., The SRG/eROSITA All-Sky Survey: The first X-ray all-sky survey in the 21st century, A&A 682, A34 (2024)”.[This is a specific DR1 survey paper.] In the text it is used as the **catalog/documentation** citation for the DR1 source catalog.[The official DR1 catalog paper is comparably titled but there is also a separate description of catalogs and selection functions; e.g., Predehl et al. 2021 for eRASS1, with Merloni et al. 2024 as overview.] This is defensible but a bit fused between “all-sky survey overview” and “DR1 catalog” roles.

**Fix:**  
Either (a) clarify in the text that Merloni et al. (2024) is used as the *survey overview* citation and that the DR1 catalog details follow that paper, or (b) add the dedicated DR1 catalog/selection-function reference if you intend to refer to the catalog specifically.

---

## PAPER-PER-M3 — Gaia DR3 reference missing main DR3 paper

**Issue (minor):**  
`GaiaDR3` is given simply as “Gaia Collaboration, Gaia Data Release 3, A&A 674, A1 (2023)”.[This is correct for the DR3 summary.] However, parts of the text use Gaia as a **variable-star / time‑domain** catalog with variability parameters.[There are dedicated DR3 variability/astrophysical-parameter papers.] Strictly, the variability content is documented in separate DR3 papers (e.g. DR3 variability or astrometric solutions), not in the generic A1 overview alone.

**Fix:**  
If you rely on specific DR3 variability content (time‑domain features), add the appropriate DR3 variability paper to the bibliography and cite it where you describe Gaia DR3 as a “variable-star” survey.

---

## PAPER-PER-N1 — NANOGrav free‑spectrum KDE dataset citation could be more precise

**Issue (nit):**  
The text correctly cites the NANOGrav 15‑yr detection paper as ApJL 951, L8 (2023) and references the free‑spectrum KDE release via Zenodo DOI 10.5281/zenodo.8060824, but the bib entry `NANOGrav2023` appears to refer only to the ApJL paper.[The Zenodo record is a separate dataset citation with its own authorship string.]

**Fix:**  
Add a separate bib entry for the Zenodo KDE dataset (with its dedicated title and DOI) and use that key wherever the “Ceffyl-compatible free-spectrum KDE likelihood” is described, keeping `NANOGrav2023` for the ApJL evidence paper itself.

---

## PAPER-PER-N2 — Minor mismatch in SPHEREx citation vintage

**Issue (nit):**  
The paper cites SPHEREx as Doré et al. 2014, arXiv:1412.4872 (“Cosmology with the SPHEREx All-Sky Spectral Survey”), which is correct for the early concept study.[Later SPHEREx papers (e.g. Doré et al. 2016, 2018) refine the mission design and forecasts.] Some of the \(\sigma_{f_{\rm NL}}\) benchmark language (especially the 3–5σ “realistic” range) aligns better with later SPHEREx forecast work than with the original 2014 concept.

**Fix:**  
Optionally add a later SPHEREx forecast reference (e.g. Doré et al. 2016/2018) and cite it alongside the 2014 white paper wherever you quote specific \(\sigma_{f_{\rm NL}}\) forecast numbers, to avoid over‑loading the 2014 arXiv paper.
