# P4_v1_0_111_R_INTERNAL R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1745pt
**Wall time**: 32.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=90392, completion=1650, total=92042

---

## PAPER-PER-B1 — CE-ResNet citation package

**Issue (MAJOR)**  
Jia et al. CE‑ResNet is cited with arXiv:2210.04168, ApJ 943, 32, and DOI 10.3847/1538‑4357/aca8aa; those metadata are correct and consistent with arXiv/ADS. [0]  
However, the manuscript also states “$1.95$ million galaxies, all classified as CW or CCW since CE‑ResNet lacks a not‑spiral class” and “their catalog of 1.95 million galaxies from DESI Legacy pre‑imaging yields CW/CCW = 0.998,” which is an extrapolation beyond the arXiv abstract: the abstract mentions a classifier and that DESI images increase spiral counts, but does not itself assert a public 1.95M‑object catalog, that all objects are CW/CCW (no non‑spiral class), or that the CW/CCW ratio is exactly 0.998. [0]

**Fix**  
Keep the bibliographic metadata as is, but rephrase all CE‑ResNet catalog statements to what is actually documented in Jia et al.: describe CE‑ResNet as a chirality‑equivariant classifier trained on SDSS GZ1, note that DESI imaging improves counts, and drop or explicitly flag as “from the CE‑ResNet public tables / code” any specific DESI‑footprint object count or CW/CCW ratio unless you can point to the exact table, figure, or data release in Jia et al. that gives 1.95M and 0.998. [0]


## PAPER-PER-B2 — Shamir 2020 reference

**Issue (nit)**  
Shamir (2020) is cited as “Shamir (2020)~\cite{Shamir:2020} extended this to $\sim10^5$ galaxies from multiple surveys, reporting asymmetries of $\sim3\%$ with a consistent dipole axis,” which matches the qualitative claims in the arXiv:2007.16116 abstract: it analyses $\sim6.4\times10^4$ SDSS and $\sim3.3\times10^4$ Pan‑STARRS galaxies and reports statistically significant asymmetries and significant quadrupole alignments. [1]  
However, the text says “multiple surveys” and “$\sim10^5$ galaxies” whereas the abstract explicitly mentions SDSS and Pan‑STARRS totaling $\sim9.7\times10^4$ galaxies; the rounding and “multiple surveys” wording are slightly loose but not misleading.

**Fix**  
Tighten the wording to “$\sim10^5$ galaxies from SDSS and Pan‑STARRS” and, if you want to emphasize the value, cite the actual SDSS and Pan‑STARRS counts from the abstract. [1]


## PAPER-PER-B3 — Galaxy Zoo 1 (Lintott et al. 2008)

**Issue (nit)**  
Galaxy Zoo 1 is cited with Lintott et al. (2008), arXiv:0804.4483, MNRAS 389, 1179–1189, which matches arXiv and journal metadata. [3]  
The text claims “original GZ1 catalog: $\sim14{,}000$ objects with spiral classifications,” while Lintott et al. describe a sample of nearly 1 million galaxies, with morphology classes, not a specific 14k‑spiral subsample in the paper itself; that 14k number is presumably an internal cut for this work, but it is easy for a reader to misread it as a GZ1 catalog property.

**Fix**  
Clarify this as your derived subset: e.g., “from the public GZ1 catalog of nearly one million galaxies, we select $\sim14{,}000$ with spiral classifications under our cuts,” making clear that 14k is not a property stated in Lintott et al. [3]


## PAPER-PER-B4 — DESI Legacy overview (Dey et al. 2019)

**Issue (nit)**  
Dey et al. are cited as “Overview of the DESI Legacy Imaging Surveys DR8” with arXiv:1804.08657, AJ, which matches the arXiv record “Overview of the DESI Legacy Imaging Surveys” and its journal reference AJ 157, 168 (2019). [2]  
Your text states DR8 specifically; the paper itself describes the combined Legacy Surveys program (DECaLS, BASS, MzLS) and later data releases, not “DR8” in the title, though DR8‑based catalogs are indeed part of the project.

**Fix**  
Change the citation text to the exact paper title (“Overview of the DESI Legacy Imaging Surveys”) and, when you need to say DR8, phrase it as “we use DR8 imaging from the DESI Legacy Imaging Surveys described in Dey et al. (2019)” rather than implying that Dey et al.’s title is DR8‑specific. [2]


## PAPER-PER-B5 — Ivezic LSST citation

**Issue (MAJOR for citation-chain precision)**  
You cite LSST as “Ivezić et al. (2019), ApJ 873, 111, arXiv:0805.2366,” i.e. linking the 2019 ApJ reference‑design paper to the 2008 “LSST Science Book” arXiv ID. [4]  
arXiv:0805.2366 is the older LSST science book submission and not simply the preprint of ApJ 873, 111, which has its own DOI (10.3847/1538‑4357/ab042c) and is not associated with that arXiv ID; combining the 2019 journal reference with the 2008 arXiv ID is a fused‑metadata error. [4]

**Fix**  
Either (a) cite the ApJ design paper alone with its DOI and no arXiv ID, or (b) cite both resources separately: LSST Science Book as arXiv:0805.2366, and the 2019 ApJ paper with its proper citation (no arXiv). Do not attribute arXiv:0805.2366 as the preprint of ApJ 873, 111. [4]


## PAPER-PER-B6 — Shamir 2022 DESI Legacy paper DOI

**Issue (minor)**  
You note in a comment that a previous DOI suffix `stac2342` actually corresponds to an unrelated MNRAS paper, and correct Shamir (2022) DESI Legacy to MNRAS 516, 2281 with DOI 10.1093/mnras/stac2372, which matches the MNRAS record. [1]  
This is correct now, but the surrounding prose still references “earlier drafts” using the wrong DOI in a way that is easy to miss, and there is no single clean bibliographic entry in the main bibliography for the DESI‑specific Shamir paper distinct from the 2022 PASJ paper.

**Fix**  
Ensure the bibliography has a single, clean entry for Shamir’s DESI Legacy paper with MNRAS 516, 2281 and DOI 10.1093/mnras/stac2372, and remove residual in‑text DOI suffixes or comments that mention the older `stac2342` to avoid any confusion in reference parsers. [1]
