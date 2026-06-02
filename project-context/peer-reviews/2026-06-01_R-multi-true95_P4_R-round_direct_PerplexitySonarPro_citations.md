# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 29.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100585, completion=2149, total=102734, search_context_size=low, cost={'input_tokens_cost': 0.30175, 'output_tokens_cost': 0.03223, 'request_cost': 0.006, 'total_cost': 0.33999}

---

## PAPER-PER-B1 — Mis-citation / wrong bib metadata for Shamir 2022 DESI paper

**Severity:** MAJOR  

**Location:** Bibliography entry `\bibitem{Shamir:2022DESI}` + several in‑text parenthetical descriptions (e.g. Introduction, around “MNRAS 516 2281, DOI 10.1093/mnras/stac2372”).  

**Issue:** The bib entry labeled `Shamir:2022DESI` mixes metadata from *two different* Shamir papers. On arXiv, **arXiv:2208.13866** corresponds to *“Large-scale galaxy spin patterns in DESI legacy imaging data”*, published in **PASP 134, 104501 (2022), DOI 10.1088/1538‑3873/ac9239**, not MNRAS 516 2281.[ ]() By contrast, **MNRAS 516, 2281, doi:10.1093/mnras/stac2372** is Shamir’s SDSS‑based paper *“Distribution of spin directions of spiral galaxies in SDSS”* associated with **arXiv:2207.10634**, not with DESI Legacy imaging.[ ]() The text currently claims “Shamir (2022)… (arXiv:2208.13866, DESI Legacy Survey, … MNRAS 516 2281, DOI 10.1093/mnras/stac2372)”, which is fused/incorrect metadata and misidentifies both the venue and arXiv ID for the DESI paper.  

**Fix (1–2 sentences):**  
Split this into two correctly identified references: one for the DESI Legacy PASP paper (arXiv:2208.13866, PASP 134, 104501, 2022, DOI 10.1088/1538‑3873/ac9239) and one for the SDSS MNRAS 516, 2281 paper (arXiv:2207.10634, DOI 10.1093/mnras/stac2372). Update all in‑text mentions so that when you discuss DESI Legacy sample sizes you cite the PASP/2208.13866 paper, and when you discuss SDSS‑based results you cite the MNRAS/2207.10634 paper, dropping the current fused “MNRAS 516 2281, arXiv:2208.13866” combination.  

---

## PAPER-PER-B2 — Inconsistent and confusing use of “Shamir (2022)” across SDSS vs DESI papers

**Severity:** MAJOR  

**Location:** Introduction (first paragraphs citing Shamir 2012, 2020, 2022), comparison section §\ref{sec:shamir}, and Abstract where “Shamir’s (2020, 2022)” are used as a pair.  

**Issue:** Once the DESI PASP and SDSS MNRAS papers are correctly disentangled (see B1), it becomes clear that the manuscript repeatedly treats “Shamir (2022)” as a single object while actually referring to two distinct 2022 papers: one SDSS MNRAS (MNRAS 516 2281) and one DESI PASP (PASP 134, 104501). Some sentences compress them into a single “Shamir (2022) DESI Legacy” comparator with MNRAS metadata; others talk about “Shamir’s (2020, 2022)” claimed 2–4% asymmetries without being explicit which 2022 paper is meant. That makes it hard to trace which result (SDSS vs DESI) you are comparing against and obscures the citation trail.  

**Fix (1–2 sentences):**  
After correcting the bib, explicitly name and consistently distinguish the **2022 SDSS MNRAS** and **2022 DESI PASP** papers throughout the text—e.g. “Shamir 2022a (SDSS, MNRAS 516, 2281)” vs “Shamir 2022b (DESI Legacy, PASP 134, 104501)”—and adjust all statements summarizing “Shamir (2022)” and “Shamir (2020, 2022)” claims so that it is clear which paper and survey they refer to.  

---

## PAPER-PER-M3 — Overstated description of Shamir 2022 DESI paper’s journal venue early in text

**Severity:** MAJOR  

**Location:** Introduction, paragraph beginning “Shamir~(2022)… (arXiv:2208.13866, DESI Legacy Survey, … MNRAS 516 2281)”.  

**Issue:** Independently of the fused ID in the bibliography, this in‑text sentence asserts that the DESI Legacy analysis appears in “MNRAS 516 2281”. As noted above, the DESI Legacy analysis corresponding to arXiv:2208.13866 is in **PASP, not MNRAS**; the MNRAS 516 2281 paper is the SDSS spin‑direction paper with a different arXiv ID. This is not just a stylistic nit: it misleads a reader trying to locate the DESI paper in the wrong journal and volume.  

**Fix (1–2 sentences):**  
Change this parenthetical to the correct venue and DOI for the DESI paper (PASP 134, 104501, 2022, DOI 10.1088/1538‑3873/ac9239), and if you want to keep the SDSS MNRAS paper in the same sentence, explicitly list it separately with its own arXiv:2207.10634 / MNRAS 516 2281 / DOI 10.1093/mnras/stac2372 metadata.  

---

## PAPER-PER-M4 — Shamir sample-size and catalog-description sentences now ambiguous after correcting refs

**Severity:** MAJOR  

**Location:** Introduction and §\ref{sec:stats} (sentences like “Shamir 2022 DESI Legacy sample as nearly 1.3×10^6 spiral galaxies” and “~1.3×10^6 input galaxies reduced to ~2×10^5 after Ganalyzer cuts”).  

**Issue:** The text currently attributes “nearly 1.3×10^6 spiral galaxies” and the reduction to ~2×10^5 spirals to “Shamir 2022” while also labelling that same paper as DESI Legacy and as MNRAS 516 2281. Once the DESI PASP vs SDSS MNRAS confusion is fixed, at least one of these descriptive sentences will be misaligned: the DESI PASP paper talks about DESI Legacy imaging with its own selection and counts; the MNRAS 516 SDSS paper uses different samples and counts. As written, a reader cannot tell which survey these numbers correspond to.  

**Fix (1–2 sentences):**  
After separating the two 2022 papers, go back to the relevant arXiv/PASP/MNRAS texts and re‑check the exact sample sizes and “spiral vs input galaxy” numbers; then update your sentences so that each numerical description is tied to the correct paper and survey (e.g. “Shamir 2022b (DESI, PASP) analyzes ~X input DESI Legacy galaxies, of which ~Y are classified spirals after Ganalyzer cuts”).  

---

## PAPER-PER-m5 — CE‑ResNet and SpArcFiRe citations look correct but one claim should be tightened

**Severity:** minor  

**Location:** §\ref{sec:ceresnet} and §\ref{sec:sparcfire}.  

**Issue:** The CE‑ResNet citation to Jia et al. (ApJ 943, 32, 2023, arXiv:2210.04168) and SpArcFiRe citation to Davis & Hayes (ApJ 790, 87, 2014, arXiv:1402.1910) are correct. However, the sentence “SpArcFiRe’s deterministic algorithm has near-perfect self-consistency (99.983%) but lower agreement with Galaxy Zoo 1 (85.8% overall, 92.5% at high confidence)” compresses several numbers that are specific to particular tables and confidence cuts in Davis & Hayes; as written it can be read as a general statement about all SpArcFiRe runs.  

**Fix (1–2 sentences):**  
Keep the citation but qualify the claim to match the exact context in Davis & Hayes—for example, specify that the quoted percentages apply to the particular SDSS DR7/DR9 sample and confidence thresholds reported in their Table(s), rather than to SpArcFiRe in general.  

---

## PAPER-PER-n6 — LSST citation note is internally inconsistent about arXiv usage

**Severity:** nit  

**Location:** Bibliography entry `\bibitem{Ivezic:2019}` and surrounding comment block.  

**Issue:** The current note says “The preprint arXiv:0805.2366… is the older LSST Science Book white paper, NOT the preprint of this specific ApJ reference‑design article; the arXiv identifier has been removed…”, but earlier in the comment you still mention “arXiv:0805.2366” as if it were associated. This is confusing for readers inspecting the .bib to see how the ApJ 873, 111 paper relates to preprints.  

**Fix (1–2 sentences):**  
Simplify the LSST entry to just the ApJ 873, 111, 2019 citation (authors, title, DOI) and, if you want to mention the Science Book, add a separate bib entry for arXiv:0805.2366 labeled clearly as “LSST Science Book (white paper)”, avoiding any language that implies a one‑to‑one preprint→journal mapping for the reference‑design article.
