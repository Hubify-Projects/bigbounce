# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v136verify_P4_v1_0_136
**Wall time**: 14.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=104865, completion=630, total=105495

---

## PAPER-PER-B1 — MAJOR
Section: Introduction, Shamir citations.  
`Shamir:2020` / `Shamir:2022DESI` are fine, but the text blurs Shamir 2022 methodology and DESI Legacy results as if they were interchangeable comparators in a few places; keep the catalogs explicitly separate throughout. Fix by consistently pairing the right claim with the right paper: 2020 is SDSS+Pan-STARRS parity/multipoles, 2022DESI is DESI Legacy spin directions. [1][2]

## PAPER-PER-B2 — MAJOR
Section: Introduction / bibliography, `Jia:2023`.  
The citation metadata is correct in the bib entry, but the prose elsewhere says CE-ResNet released “1.95 million galaxy chirality classifications” and “DESI Legacy pre-imaging” in ways that can be read as a single catalog claim, not a model paper result. Fix by stating the model paper separately from the catalog scale derived in this manuscript. [3]

## PAPER-PER-B3 — MAJOR
Section: Comparison with Previous Work, `Iye:2026P6`.  
This is not a verified published paper citation; the manuscript says it is “now public as arXiv:2605.05570,” but no arXiv verification is provided in the reference list, and the citation is not established by the supplied checks. Fix by either removing the citation until verified or adding the exact arXiv record and venue metadata.  

## PAPER-PER-B4 — MAJOR
Section: Comparison with Previous Work, `Walmsley:2023`, `Hart:2016`, `Iye:2021`.  
Several quantitative paraphrases are too aggressive compared with the source abstracts: Walmsley 2023 is a morphology catalog paper, not a chirality catalog; Hart 2016 is about spiral-arm number and redshift bias correction, not handedness; Iye 2021 is about SDSS spiral spin parity and simulations, not “duplication of photometric objects” as a headline claim. Fix by trimming each claim to the exact scope of the cited paper. [3][4]

## PAPER-PER-B5 — minor
Section: Bibliography, `Ivezic:2019`.  
The note about removing the arXiv ID to avoid fused metadata is fine, but the text still mixes “LSST: From science drivers...” with “reference design” wording in a way that can confuse which exact publication is being cited. Fix by keeping only the journal article title and DOI, with no residual preprint framing. [5]

## PAPER-PER-B6 — nit
Section: bibliography / style.  
A few reference entries use inconsistent author-name normalization and venue formatting, but I did not find a blocker-grade metadata error in the checked items. Fix by normalizing initials, journal abbreviations, and DOI punctuation for consistency.
