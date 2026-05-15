# P4_v1070_R R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_0735pt
**Wall time**: 12.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=63638, completion=886, total=64524

---

## PAPER-PER-B1 — MAJOR
**Section:** References / in-text citation to `Walmsley:2023GZDESI` and `Walmsley:2023`.

The paper cites the same Galaxy Zoo DESI work under two labels, but both references point to arXiv **2309.11425**, whose real title is **“Galaxy Zoo DESI: Detailed Morphology Measurements for 8.7M Galaxies in the DESI Legacy Imaging Surveys”** and whose first author list begins with **Mike Walmsley**. The in-text claim about a separate “GZ DESI detailed-morphology measurements” source is fine, but the bib split is metadata duplication that will confuse citation chains. Consolidate to one canonical entry and make every mention point to it. 

## PAPER-PER-B2 — MAJOR
**Section:** Bibliography entry `Jia:2023`.

The citation text says **“CE-ResNet: A chirality-equivariant ResNet for spiral-galaxy classification”** with **ApJ 943, 154 (2023)**, but the actual arXiv title is **“Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network”** and the arXiv ID is **2210.04168**. This is fused metadata: title from a different paper/working name plus the correct journal venue and DOI. Replace the title with the real published/arXiv title and keep the DOI/venue only if they match the journal record. 

## PAPER-PER-B3 — MAJOR
**Section:** Bibliography entry `Iye:2020`.

The paper cites **“Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations”** and labels it **Astrophys. J. 907, 123 (2021)** with **arXiv:2011.00662**. The arXiv record confirms the ID and title, but the in-text year-to-work framing is sloppy: the claim is about a 2020 preprint while the journal venue is 2021, so the citation should be normalized consistently to one form. Use either the arXiv version or the journal version throughout, not a hybrid. 

## PAPER-PER-B4 — MAJOR
**Section:** Bibliography entry `Ivezic:2019`.

The reference lists **“LSST: From science drivers to reference design and anticipated data products”** as **Astrophys. J. 873, 111 (2019)** but gives **arXiv:0805.2366**, which is an obviously different-era identifier and does not match the 2019 LSST review. This is a fused/incorrect arXiv ID and must be fixed before submission. Keep the title and venue if they are correct, but replace the arXiv identifier with the actual one. 

## PAPER-PER-B5 — minor
**Section:** Bibliography entry `Dosovitskiy:2020`.

The paper cites the ViT work with the correct arXiv ID **2010.11929**, but the bib line omits the real title **“An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale”** in favor of a short descriptor. That is not fatal, but it weakens provenance and makes automated citation matching less reliable. Replace the shorthand with the actual paper title. 

## PAPER-PER-B6 — BLOCKER
**Section:** Overall bibliography / submission readiness.

There are multiple metadata defects that are not isolated typos: at least one duplicate source entry (`Walmsley:2023` vs `Walmsley:2023GZDESI`), one fused title/venue citation (`Jia:2023`), and at least one wrong arXiv ID (`Ivezic:2019`). That is enough to break citation-chain forensics and makes the manuscript **not publishable to arXiv yet** in its current bibliographic state. Fix the reference list first, then rerun a complete citation audit against arXiv/publisher records. 
