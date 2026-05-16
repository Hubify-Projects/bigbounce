# P4_v1095 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0130pt_P4_v1095_R14_R-round_real
**Wall time**: 24.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=82719, completion=1346, total=84065

---

## PAPER-PER-B1 — Ivezic LSST bibitem

**Location:** Bibliography entry for Ivezić LSST paper (near end: `\bibitem{Ivezic:2019}`).

**Issue:** The paper correctly cites Ivezić et al. 2019, ApJ 873, 111 with DOI 10.3847/1538-4357/ab042c, which is the LSST “From science drivers to reference design” paper, but earlier R-rounds worried about fused metadata with the older LSST Science Book arXiv:0805.2366. The current text explicitly removes that arXiv ID and notes that 0805.2366 is *not* the preprint of this ApJ article, which matches ADS/IOP metadata and resolves the prior fused-metadata concern.[2]

**Fix (classification: minor):** No change needed to the bibitem itself; it is now consistent and non-fused. Optionally tighten wording in the comment above the bibitem to something like: “The LSST Science Book (arXiv:0805.2366) is a related but distinct document; the present citation refers specifically to the ApJ reference-design paper Ivezić et al. 2019, ApJ 873, 111, DOI 10.3847/1538-4357/ab042c.”


## PAPER-PER-B2 — CE-ResNet citation details

**Location:** Sec. Introduction and Methods; bibitem `\bibitem{Jia:2023}`.

**Issue:** The article “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network” is correctly cited as Jia et al., ApJ 943, 32 (2023), with DOI 10.3847/1538-4357/aca8aa, matching the arXiv 2210.04168 metadata (authors, title, journal, volume, page, DOI).[1] There is no fused metadata or incorrect arXiv ID.

**Fix (classification: nit):** None required; the citation is correct and maps cleanly to the actual paper. You might remove the parenthetical “Methodology / Ganalyzer-pipeline reference paper” in the Shamir items and keep a similar neutral parenthetical (“chirality-equivariant classifier”) here for symmetry, but that’s stylistic, not forensic.


## PAPER-PER-B3 — DESI Part I white paper citation

**Location:** Sec. Comparison / Future directions; bibitem `\bibitem{DESI:2016}`.

**Issue:** The DESI Part I paper is correctly cited as the arXiv white paper “The DESI Experiment Part I: Science, Targeting, and Survey Design” (arXiv:1611.00036), with no journal venue claimed.[2] This matches arXiv metadata and avoids any confabulated journal reference.

**Fix (classification: nit):** Optionally add “arXiv preprint” in the bib comment so it’s clear this is intended as a white paper only: e.g. “…arXiv:1611.00036 (white paper; no journal publication at time of writing).”


## PAPER-PER-B4 — Shamir DESI Legacy paper DOI / metadata

**Location:** Bibitems `\bibitem{Shamir:2022}` and `\bibitem{Shamir:2022DESI}` and text mentioning DESI Legacy spin directions.

**Issue:** The 2022 DESI Legacy spin-directions paper is correctly identified as “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022) with DOI 10.1093/mnras/stac2372, which matches the journal entry; no incorrect DOI or arXiv ID is currently attached in the LaTeX.[0] The separate “Shamir:2022” PASJ paper and “Shamir:2022DESI” MNRAS paper are consistently distinguished.

**Fix (classification: minor):** None strictly needed. If you want to be maximally clear, you can add the arXiv ID for the DESI paper (arXiv:2208.13866) in its bibitem and ensure that is not accidentally associated with the PASJ paper, but the current split avoids fused metadata.


## PAPER-PER-B5 — DESI Part I vs DESI imaging (naming nuance)

**Location:** Sec. Data, “Galaxy Images” and “Future Directions” where DESI targeting / surveys are referenced.

**Issue:** The text uses Dey et al. 2019 for DESI Legacy Imaging Surveys and DESI Collaboration 2016 (“DESI Experiment Part I”) for the spectroscopic program, which matches the actual scope of the two references.[2] There is no misattributed title or confabulated arXiv/journal combo.

**Fix (classification: nit):** To avoid any ambiguity for non-specialist readers, you could add a brief clarifier the first time DESI:2016 is cited, e.g. “…DESI spectroscopic survey design (DESI Collaboration 2016, Part I white paper, arXiv:1611.00036)…”, but this is polish only.


## PAPER-PER-B6 — Overall citation forensics status

**Location:** Global (all external cosmology / methods / survey citations).

**Issue:** Spot-checked high-risk items (LSST Ivezić 2019, CE-ResNet 2023, DESI Part I 2016) all map cleanly to real papers with correct titles, authors, venues, and identifiers; the previously flagged LSST fused-metadata issue has been explicitly corrected by removing arXiv:0805.2366 from that ApJ reference.[1][2] I did not find any case where an arXiv ID points to a different paper than the cited title/venue, nor any invented titles.

**Fix (classification: minor):** No blocker- or major-grade citation problems remain. You can add a one-sentence note in the methods or acknowledgments that all external references were cross-checked against arXiv/ADS metadata to preempt referee worries, but that’s optional.
