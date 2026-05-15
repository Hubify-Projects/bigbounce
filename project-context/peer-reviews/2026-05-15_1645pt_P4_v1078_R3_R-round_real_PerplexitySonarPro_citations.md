# P4_v1078_R3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_1645pt
**Wall time**: 15.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=72334, completion=687, total=73021

---

## PAPER-PER-B1 — Mischaracterization of Ivezic LSST paper status (MAJOR)

**Location:** Bibliography entry for Ivezić et al. 2019 / arXiv:0805.2366 and discussion around it in Sec. \ref{sec:comparison}, \ref{sec:future}.

**Issue:** The text states that a previous AI review “false‑positively” flagged 0805.2366 as fused/incorrect metadata and asserts that the arXiv preprint “corresponds to the published ApJ paper,” implying a single paper with a single DOI. In reality, arXiv:0805.2366 is “LSST: from Science Drivers to Reference Design and Anticipated Data Products” with its own ApJ‑style DOI 10.3847/1538‑4357/ab042c, while the later, shorter ApJ article Ivezić et al. 2019 cited in the main text has DOI 10.3847/1538‑4357/ab042c and is not simply “v6 of the same arXiv preprint” but a distinct, curated journal version with a different abstract and length. The current wording suggests that an AI criticism about fused IDs was simply wrong, when in fact the situation is that the same collaboration has multiple closely related LSST design papers and a long preprint that feeds into a journal article, so metadata confusion is plausible rather than a pure hallucination.[2]

**Fix:** Rephrase the note to acknowledge that 0805.2366 is the long LSST design preprint whose content underlies the later ApJ article, and that earlier tool flags about possible metadata fusion were reasonable given the overlapping titles and authorship, instead of calling them flatly “false positives.” Explicitly list the correct title and DOI for the cited LSST reference and remove the implication that the arXiv ID–journal DOI mapping can never be fused or confusing.


## PAPER-PER-M2 — Overconfident claim that Shamir 2022 DESI spiral count is “per the published abstract” (minor)

**Location:** Sec. \ref{sec:comparison}, discussion of Shamir (2022 DESI) sample size.

**Issue:** The text states that Shamir (2022 DESI) uses “nearly 1.3×10^6 spiral galaxies … per the published abstract,” but the arXiv record and journal version distinguish between the total Legacy objects and the subset that are classified spirals; not all “nearly 1.3 million galaxies” in the footprint are spirals in every version of that paper. The current phrasing subtly conflates “galaxies in DESI Legacy Survey data” with “spirals,” overstating the precision of what the abstract itself claims.[1]

**Fix:** Soften and clarify the wording to: “Shamir (2022) reports nearly 1.3×10^6 DESI Legacy galaxies in his sample (not all classified as spirals); our canonical spiral subsample 3.20×10^6 is ≳2.5× larger, but selection and classifier differences mean this is a catalog‑scale context comparison rather than a like‑for‑like sensitivity ratio.”
