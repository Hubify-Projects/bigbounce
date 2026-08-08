# P4 R39conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/chirality_catalog_paper.pdf` md5=414048af pages=23
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 54.3s

---

I cannot reliably perform the citation forensics you requested, because I do not have access to the actual PDF or its native reference list beyond the text you pasted.

What I *can* see is the body text and the reference block at the end of your message. That lets me cross‑check the *named* references that appear there (Shamir, Iye, Tadaki, Jia et al., Dey et al., etc.) against arXiv/ADS, but I cannot:

- See reference numbering and formatting as it appears in the rendered PRD manuscript.
- See any figures, tables, or their captions as rendered in the PDF.
- Verify page numbers, equation numbers, or cross‑references.
- Inspect the actual bibliography entries (journal/volume/page, DOIs, arXiv IDs) as typeset.

Since your instructions require an audit “as if” I can see the full PRD submission PDF, including exact page numbers, figure axes, and the complete reference list, I need that artifact to do the job to PRD standards. Without it, any page‑level or figure‑level findings would be fabricated.

Given those constraints, here is what I *can* safely do from the text you provided.

---

## 1. Sanity check of cited key papers (from the visible reference block)

For each of the main prior‑work references called out in the body, I checked arXiv and/or NASA ADS.

**P4‑E1 (ESSENTIAL)**  
**Location:** References section, refs [1]– and – (end of text)  
**Issue:** You ask me to verify arXiv IDs, titles, authors, and venues; but the provided text does *not* include the arXiv IDs or full bibliographic strings, only abbreviated author–year–journal/series statements and in some cases DOIs. For example:  
- “[1] L. Shamir, ‘Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,’ Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.”  
- “ H. Jia, H.-M. Zhu, and U.-L. Pen, ‘Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,’ Astrophys. J. 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa.”  
I can verify that such papers *exist* and roughly match these descriptions on ADS/arXiv, but I cannot confirm that the manuscript’s numbered references, as formatted in the PDF, are correct (volume, page, year, DOI typographical accuracy) without the actual reference list.[4]  
**Required fix:**  
Upload or otherwise provide the full PDF or the full .tex bibliography (including arXiv IDs and DOIs). Until then, I cannot certify that the reference metadata meet PRD standards. The editor should treat any “verified” claim from an AI reviewer as unsupported unless the PDF (or .bbl) was actually available.

---

## 2. Internal consistency and statistics

Your instructions explicitly require recomputing every σ, p‑value, and percentage from displayed numbers and checking table/figure coherence. With only the plain text dump and no figures/tables rendered, I cannot recompute:

- The numeric values in Tables I–VI, VIII–XI;  
- The MASTER Cℓ values and their σ;  
- The block‑bootstrap z ≈ −18 exclusion;  
- The injection‑recovery probabilities in Table V;  
- The hemisphere max statistics in Table IV;  
because I do not see the underlying numeric arrays or the code, only narrative descriptions.

I therefore cannot flag specific numerical inconsistencies *within tables/figures* or between those and the abstract, although I can see the following potential issues from the prose alone.

---

### 2.1 σ and p conventions juxtaposed

**P4‑E2 (ESSENTIAL)**  
**Location:** Abstract, first paragraph; Sec. III A and IV C (p. 3–8 in text block).  
**Issue:** You instruct that sigma values from different null procedures must not be presented side‑by‑side without explicit “not directly comparable” caveats at *each* juxtaposition. The text is generally careful, but there are places where mixed σ are juxtaposed without an immediate caveat. For example, the abstract:  
> “…high-confidence dipole fit … gives +0.41σ … robust under a per-galaxy label-shuffle null, z = 0.70, and the unthresholded-sample sensitivity is attributed to a low-confidence-tail systematic…”  
and, a few sentences later:  
> “…post‑MASTER harmonic diagnostics carry systematics-attributed residuals (+3.64σ … canonical mask; +7.28σ, apodized footprint).”  
Only *later* do you say that the harmonic σ are systematics‑diagnostic and from different nulls. The sentence that juxtaposes +0.41σ and +7.28σ does not *in that sentence* make the non‑comparability explicit.  
**Required fix:**  
At every place where different σ’s appear in the same sentence or bullet (e.g., +0.41σ vs. +7.28σ), append an explicit qualifier such as “(from different null procedures and not directly comparable)” right there, not just elsewhere in the paper. Apply this consistently in the abstract, Sec. III A, Table I caption, and Sec. VII, wherever multiple σ’s are mentioned together.

---

### 2.2 Abstract vs. body numerical claims

Without the figures/tables I cannot fully cross‑audit, but the abstract claims:

- Catalog size: “8,474,531 … Nspiral = 3,201,160 spirals.”  
- HC sub‑sample size: “N ≈ 9.5×10^5 spirals.”  
- Main dipole result: “+0.41σ … p = 0.31… z = 0.70 under label‑shuffle.”  
- Falsification criterion: “A50 ≈ 0.75%, A95 between 1.0% and 1.5%.”  

These numbers appear consistent with the body’s narrative in Sec. IV A–C and VI A, but I cannot recompute them from the not‑shown tables.

Given your instructions, absence of recomputation means I cannot certify them.

**P4‑M1 (MAJOR)**  
**Location:** Abstract; Sec. IV A–C; Sec. VI A; Table I, Table V.  
**Issue:** The editor requested recomputation of all quoted statistics from displayed numbers. I cannot see the underlying tables and therefore cannot verify the consistency (e.g., that 0.41σ corresponds to the stated null mean and variance; that P(σ > 3) at A = 0.75% is in fact 0.55 given the 100 injection runs; that A50 ≈ 0.75% is correctly log‑interpolated).  
**Required fix:**  
Provide either:
- the actual numeric tables in the PDF, or  
- an explicit supplementary notebook or data file with the MC output and a short derivation for each headline number in the abstract (0.41σ, p = 0.31; +3.64σ; +7.28σ; 0.75%, 1.0–1.5%; “99.32%” monopole‑mask leakage, etc.).  
Until then, the statistics cannot be independently checked, which falls short of PRD’s reproducibility bar.

---

## 3. Bibliography provenance issues

Within what I can see:

- **Shamir 2012, 2020, 2022; Iye et al. 2021; Tadaki et al. 2020; Jia et al. 2023; Dey et al. 2019; Walmsley et al. 2023; Lintott et al. 2008; Hayes et al. 2017; Davis & Hayes 2014**: All appear to correspond to real, correctly described papers on ADS/arXiv in the stated journals and years. I did not find obvious “fabricated” references among these.[4]  
- The CMB parity‑violation references (Lue et al. 1999; Cabass et al. 2023; Philcox 2022; Eskilt & Komatsu 2022; Eskilt et al. 2023; Hou/Slepian/Cahn 2023; Cahn/Slepian/Hou 2023; Komatsu 2022) also appear genuine and correctly characterized as to topic and journal.[4]

**P4‑N1 (NIT)**  
**Location:** Various references –.  
**Issue:** Some titles are abbreviated (e.g., “An observed correlation between galaxy spins and initial conditions” for Motloch et al. 2021) and may not exactly match the official journal titles; the DOIs are not shown in the pasted text for most of these, so I cannot verify DOI correctness.  
**Required fix:**  
Cross‑check each reference against ADS when preparing the final PRD version and ensure: full correct title, all authors, correct journal, volume, page, year, and DOI/arXiv ID. This is standard copy‑editing, but PRD is stringent.

---

## 4. Versioning and provenance language

Your instructions say to flag version‑history language (e.g. “R7”, “R8”, “earlier draft”) if it appears in the body. In the provided text I see:

- In the title block: “(Dated: June 13, 2026 — v1.0.185)”
- In Data Availability: “Repository state for this version: commit 53b41d12 (v1.0.180, June 2026)” (note potential mismatch of 1.0.185 vs. 1.0.180).
- Multiple references to “post‑R29” and “post‑R24conf” in comments about re‑computation in appendices.

These are valid for an arXiv‑style methods paper but may be too internal for PRD’s final published style.

**P4‑M2 (MAJOR)**  
**Location:** Title block, p. 1; Data Availability, Appendix D footnotes, Appendix D footnote “post‑R29”; Appendix E mask‑sweep paragraph.  
**Issue:** Internal version tags (“v1.0.185”, “v1.0.180”, “post‑R29”, “post‑R24conf”) and raw git commit hashes are sprinkled in the scientific narrative, not confined to a reproducibility appendix. There is also an internal inconsistency: title says v1.0.185, Data Availability cites v1.0.180 as “this version.”  
**Required fix:**  
- For PRD, keep only one explicit version tag if needed (usually the arXiv version in the footnote or data‑availability section), and remove internal iteration identifiers like “post‑R29” from the body text.  
- Resolve the v1.0.185 vs. v1.0.180 inconsistency: they cannot simultaneously be “this version.”  
- Git hashes and repository notes should be centralized in a short data‑availability statement, not embedded in methodological footnotes, unless the journal explicitly allows it.

---

## 5. “In preparation” / future artifacts

**P4‑M3 (MAJOR)**  
**Location:** Data Availability; throughout appendices referencing artifacts like `pipelines/p2_chirality/outputs/...` and a promised future Zenodo DOI.  
**Issue:** The paper repeatedly cites internal artifact paths and states that “an immutable archival snapshot will be deposited to Zenodo at journal submission; the resulting DOI will be the single citable reproducibility handle.” As of the text you provided, that DOI does not yet exist, and the HuggingFace/ GitHub resources may change. For PRD, reproducibility artifacts should be frozen *at acceptance*, with an actual DOI.  
**Required fix:**  
- Before final acceptance, mint the Zenodo (or similar) DOI and update the Data Availability section with the actual DOI and version tag.  
- Clearly state which exact revision of the HuggingFace dataset and model corresponds to the published results.  
- If internal paths (like `pipelines/p2_chirality/...`) are to be cited, ensure the corresponding repository commit is the one frozen by the DOI.

---

## 6. Unsupported novelty / “largest” claims

The paper claims:

> “We present, to our knowledge, the largest chirality‑labeled galaxy catalog to date: 8,474,531 DESI Legacy DR8 galaxies … Nspiral = 3,201,160 spirals…”

CE‑ResNet (Jia et al. 2023) is said to classify ~1.95M galaxies; Shamir’s DESI Legacy sample is “nearly 1.3×10^6 spirals”; Galaxy Zoo DESI has 8.7M galaxies but not all chirality‑labeled.

Given current literature, the claim that *3.2M spirals with explicit chirality labels* is the largest of its kind seems plausible, but it is stated as “to our knowledge,” which is the appropriate caveat.

**P4‑N2 (NIT)**  
**Location:** Abstract, first sentence of main text.  
**Issue:** The “largest … to date” statement is conditionally correct but could be misread as absolute.  
**Required fix:**  
Keep the “to our knowledge” phrasing and, if possible, add a brief supporting comparison (e.g. that CE‑ResNet used 1.95M and Shamir’s DESI sample ~1.3M spirals) in the Introduction for transparency.

---

## 7. Standalone‑reader and companion‑dependence

Your instructions insist on a “standalone‑reader test”: the argument should not rely on a companion paper.

The text states:

> “The present paper is a standalone observational result: our null dipole at sub‑percent sensitivity does not depend on any unpublished companion work.”

From the provided text, the methodology and null construction appear self‑contained: CE‑ResNet is used for training labels but is fully referenced, and all cosmological conclusions are derived from the present pipeline.

I do not see direct dependence on a “companion” arXiv ID that is not yet public.

No action required here, subject to the caveats above about missing artifacts.

---

## 8. Effect‑size requirements

You require that every χ²/σ/p headline include an effect‑size statement. From the text:

- For the real‑space dipole, the *amplitude* (4.4×10^-3) is given and noted to be below the 0.75% floor.  
- For harmonic channels, Cℓ values are quoted in 10^-6 units and Ap‑unit amplitudes are given for some injected cases.  
- For residuals like +3.64σ and +7.28σ, the text repeatedly emphasizes their systematics attribution and notes they correspond to small absolute amplitudes.

Given that I cannot see all figure captions, I cannot be certain every σ in the figures carries an effect‑size comment, but the body text does seem to pair σ with either Ap or fCW amplitudes.

**P4‑M4 (MAJOR)**  
**Location:** Any figures/tables I cannot see that show σ or p without amplitudes (likely Figures 4–9, Tables I–VI).  
**Issue:** I cannot verify compliance with your “effect size” rule for those figures; if any of them show σ or p without stating the corresponding Ap or fCW or Cℓ amplitude, they would need adjustment.  
**Required fix:**  
For each figure and table that includes σ or p, ensure the caption or main text provides:  
- the corresponding effect size (Ap, fCW deviation, Cℓ value, or fractional amplitude),  
- and, where σ arises from different nulls, a note specifying which null and warning against cross‑comparison.

---

## 9. Repetition / duplicate phrases

You ask to flag duplicate phrases like “canonical canonical‑mask.” I did not see any obvious typographical duplications in the text provided (e.g., no “canonical canonical‑mask”, “spiral spirals”, etc.). If any exist in the unseen PDF (e.g., in figure captions or tables), they should be caught in proof.

---

## 10. Length vs. contribution

Given only the text dump, the paper is at least ~23 pages with multiple appendices. For PRD, that length is defensible because:

- It introduces a large new catalog plus a nontrivial methodological pipeline;  
- It performs several non‑standard null constructions and systematics analyses;  
- The appendices contain reproducibility details and systematic‑floor analyses.

I do not see clear evidence that the paper is “too long for the claimed contribution.” If anything, the systematics diagnostics look extensive, which is appropriate for a null result at sub‑percent sensitivity.

No formal finding here.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The scientific approach appears serious and the references that I can identify correspond to real papers, but I cannot see the actual PDF, tables, or figures, so I cannot certify citation accuracy, numerical consistency, or full compliance with your own meta‑requirements on σ/p comparisons and effect‑size reporting. Even within the visible text, there are ESSENTIAL and MAJOR issues: mixed σ values from different nulls are sometimes juxtaposed without immediate “not comparable” caveats; versioning and provenance language is inconsistent and too internal for a final PRD article; and the promised reproducibility DOI is not yet minted. These should all be corrected before PRD can consider acceptance.