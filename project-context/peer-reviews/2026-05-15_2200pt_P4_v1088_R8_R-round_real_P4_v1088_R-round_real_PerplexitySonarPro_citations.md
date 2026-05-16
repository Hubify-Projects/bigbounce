# P4_v1088 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_2200pt_P4_v1088_R8_R-round_real
**Wall time**: 23.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79651, completion=1366, total=81017

---

## PAPER-PER-B1 – Shamir 2022 DESI paper metadata

**Issue (MAJOR)**  
The bib entry `Shamir:2022DESI` is described as “Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372,” which correctly corresponds to Shamir’s DESI Legacy spin-directions paper, but the body text elsewhere conflates “nearly 1.3×10^6 spiral galaxies” (spiral subsample) with “nearly 1.3×10^6 galaxies” (full sample) in a way that is ambiguous and partially inconsistent with the abstract of that paper (which emphasizes the full galaxy count; the spiral-only number is smaller and context-dependent). [1]  

**Fix (1–2 sentences)**  
Tighten the wording to: “Shamir (2022) analyzes nearly 1.3×10^6 DESI Legacy galaxies, of which a smaller subset are classified as spirals by Ganalyzer (see his paper for the exact spiral-count definition).” This preserves the correct paper metadata while avoiding over-specific claims about the spiral-only count that are not explicitly fixed in Shamir’s abstract.  

---

## PAPER-PER-B2 – CE-ResNet (Jia et al. 2023) citation content

**Issue (minor)**  
The citation to Jia et al. 2023 (CE-ResNet) is accurate in arXiv ID, authors, title, journal (ApJ), and DOI, but the manuscript paraphrases their numerical Z-wise/S-wise imbalance reduction as “the discrepancy drops to <1.8σ” without clearly emphasizing that this is a catalog-wide asymmetry significance in their specific SDSS+DESI setup, not a general bound that can be applied directly to the present DESI-only chirality catalog. [0]  

**Fix (1–2 sentences)**  
Add a short qualifier, e.g.: “CE-ResNet reduces the GZ1-trained Z/S imbalance to <1.8σ in their SDSS+DESI configuration; this value is specific to their training set and footprint and is cited here only as a qualitative benchmark, not as a bound on our catalog.”  

---

## PAPER-PER-B3 – DESI Legacy overview paper metadata

**Issue (nit)**  
The Dey et al. 2019 DESI Legacy Imaging Surveys reference is essentially correct in title, venue (AJ), and arXiv ID, but the inline description repeatedly refers to “DR8” as if it were part of the original survey-design paper’s nomenclature, whereas the Dey et al. paper is an overview of the Legacy Surveys project and predates the specific DR8 data release naming that later appears on the project’s website. [1]  

**Fix (1–2 sentences)**  
Slightly rephrase to: “We use the DESI Legacy Imaging Surveys Data Release 8 (DR8; see survey overview in Dey et al. 2019)…” to make clear that DR8 is the data product used here rather than a label defined in that specific paper.  

---

## PAPER-PER-B4 – ArXiv/DOI fusion risk for LSST reference

**Issue (minor)**  
The LSST reference is given as Ivezić et al. 2019 ApJ 873, 111 with arXiv:0805.2366, which corresponds to the older LSST Science Book preprint; this is a standard but slightly fused citation in the literature (the long arXiv white paper vs the shorter ApJ design paper). ADS confirms both are commonly linked, but strictly speaking they are not the same document. [1]  

**Fix (1–2 sentences)**  
Clarify the dual nature explicitly, e.g.: “We refer to the LSST reference design paper (Ivezić et al. 2019, ApJ 873, 111) and its longer precursor white paper (arXiv:0805.2366) collectively as ‘LSST’; our citation uses the ApJ article for journal reference and the arXiv preprint for technical background.”  

---

## PAPER-PER-B5 – Explicitness of CE-ResNet catalog size comparison

**Issue (nit)**  
The comparison “this spiral count alone is 1.6× larger than the state-of-the-art prior chirality catalog of CE-ResNet (Jia et al. 2023, 1.95 million galaxies, all classified as CW or CCW since CE-ResNet lacks a not-spiral class)” is directionally correct, but it doesn’t explicitly note that CE-ResNet’s catalog is over DESI pre-imaging with a different parent selection and that their 1.95M is not a spiral-only subset in the same sense as the present catalog’s 3.20M spirals. [0]  

**Fix (1–2 sentences)**  
Clarify the comparison scope: “Jia et al. (2023) provide 1.95 million DESI pre-imaging galaxies all assigned CW/CCW labels (no explicit non-spiral class); our 3.20 million spirals are selected from a larger parent sample with a separate NS class, so the 1.6× ratio is a catalog-scale, not like-for-like, comparison.”  

---

## PAPER-PER-B6 – Status of Iye & Yagi 2026 citation

**Issue (MAJOR)**  
The manuscript cites “Iye & Yagi (2026)… in preparation (arXiv ID pending; cited per private communication)” and then uses this as one of “four independent lines of evidence consistent with the present null.” This is correctly flagged as “in preparation” but is treated in the narrative almost on par with refereed results (Iye 2020, Tadaki 2020), which is too strong for a non-public, non-archived source. [1]  

**Fix (1–2 sentences)**  
Downgrade its evidentiary weight and be explicit, e.g.: “Iye & Yagi (2026, in preparation; private communication) report a similar null in HSC WIDE regions; we mention this only as indicative ongoing work, not as an independent, citable constraint.”
