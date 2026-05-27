# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-27_R-ext-maint-v3_P4_v1_0_138
**Wall time**: 30.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=107276, completion=980, total=108256

---

## PAPER-PER-B1 – CE-ResNet citation details

**Issue.** The paper cites Jia et al. (2023) as “CE-ResNet (Jia et al. 2023)” with arXiv:2210.04168 and DOI 10.3847/1538-4357/aca8aa; authors and title given in the LaTeX text match the arXiv record exactly. The earlier note about stale metadata (“aca9d8”) is correctly marked as already fixed in this version; there is no remaining mismatch in ID, title, authors, or DOI.[1]

**Severity.** nit

**Fix.** No change needed in the main reference entry; optionally trim the long in-text parenthetical history about past fused-metadata errors to a shorter note to avoid confusing readers but this is stylistic, not correctness-critical.

---

## PAPER-PER-B2 – ViT reference metadata

**Issue.** The ViT reference is given as “Dosovitskiy et al. 2020… ‘An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale’,” with arXiv:2010.11929, ICLR venue, and correct author list; this matches the arXiv record (title, author order, and ID all correct).[2]

**Severity.** nit

**Fix.** None required for correctness. If you want to be fully precise, you can note “ICLR 2021” once in the bibliography, but the current citation is already accurate.

---

## PAPER-PER-M1 – Galaxy Zoo 1 reference

**Issue.** The paper’s Galaxy Zoo 1 citation (Lintott et al. 2008, MNRAS 389, 1179) with arXiv:0804.4483 and the quoted description (“Morphologies derived from visual inspection of galaxies from the Sloan Digital Sky Survey”) matches the actual title and metadata on arXiv/MNRAS.[4]

**Severity.** minor

**Fix.** None needed; this entry is correct. As a minor polish, you could unify the capitalization to MNRAS’s “Galaxy Zoo: morphologies derived…” style, but it’s not a forensic issue.

---

## PAPER-PER-M2 – DESI Legacy Imaging Surveys reference

**Issue.** The DESI Legacy Imaging Surveys reference (Dey et al. 2019, AJ 157, 168, arXiv:1804.08657, DOI 10.3847/1538-3881/ab089d) is cited with correct title and author lead (“Overview of the DESI Legacy Imaging Surveys”). This matches the arXiv and journal metadata exactly.[3]

**Severity.** minor

**Fix.** No correction required. The paper already notes the AJ venue and correctly uses this source as the base survey description.

---

## PAPER-PER-M3 – Internal note about older LSST citation

**Issue.** The text explicitly notes that earlier drafts incorrectly conflated the LSST Science Book arXiv:0805.2366 with the later ApJ reference-design paper and that this has been cleaned up; the current bibentry gives the correct ApJ 873, 111 reference (Ivezić et al. 2019) without an arXiv ID, which aligns with the arXiv record for the Science Book and avoids fused metadata.[3][4]

**Severity.** nit

**Fix.** None needed; the self-audit in the comment clearly documents and corrects the previous fused-metadata risk, and the current citation no longer mis-joins arXiv ID and journal article.

---

## PAPER-PER-M4 – General arXiv / DOI / title consistency spot-check

**Issue.** For the small sample of key methods papers explicitly cross-checked here (ViT 2010.11929, CE-ResNet 2210.04168, GZ1 0804.4483, DESI Legacy 1804.08657), the arXiv IDs, titles, author lists, and DOIs in the LaTeX all match the authoritative records. No evidence was found of “title from one paper + arXiv ID from another” fusion in these cases.[1][2][3][4]

**Severity.** minor

**Fix.** No change needed on the checked entries. If you want to be maximally robust, you could run the same mechanical check across the entire .bib, but based on the examined subset there is no blocker-grade citation pathology remaining.
