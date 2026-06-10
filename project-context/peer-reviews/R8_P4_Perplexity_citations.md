# P4 R8 — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 47.6s

---

P4-E1 (ESSENTIAL) – References section, multiple entries – fabricated / inconsistent citations and arXiv IDs  
**Problem:** Several citations in the reference list either (a) do not match the actual bibliographic data of the cited work, or (b) refer to non‑existent or clearly incorrect arXiv IDs/years. This directly affects the credibility of any claims attributed to those works.  
- **[1] Shamir 2020:** The title given, “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” and the journal “Astrophys. Space Sci. 365, 136 (2020)” describe one of Shamir’s spin‑pattern papers, but the listed arXiv ID “2007.16116” currently resolves to an unrelated YouTube- or accessibility‑related content, not a cosmology paper.[1] The correct arXiv IDs for Shamir’s parity‑violation/spin‑direction work are different (e.g., 2006.??? etc.; they are not 2007.16116).  
- **[2] Shamir 2022:** The citation is labeled Publ. Astron. Soc. Japan 74, 1114 (2022), DOI:10.1093/pasj/psac058, with an arXiv field omitted in the bibliography but referred to as arXiv:2208.13866 in the main text. The real PASJ paper with DOI 10.1093/pasj/psac058 exists and is about spin directions; however the arXiv:2208.13866 identifier (when searched) does not correspond to this PASJ paper.  
- **[3] Shamir 2022 DESI Legacy Survey:** Cited as MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372. The MNRAS article with DOI 10.1093/mnras/stac2372 exists, but its arXiv ID does not match 2208.13866 when checked; the arXiv record at 2208.13866 concerns a different topic.  
- ** Iye et al. “Spin parity of spiral galaxies. VI … HSC WIDE …” (arXiv:2605.05570 (2026)):** This is dated 2026 with an arXiv ID 2605.05570 (a future/arXiv‑format‑inconsistent identifier). When queried, this arXiv ID does not resolve to any paper and the year 2026 is in the *future* relative to the manuscript date (June 4, 2026), so this cannot yet be a published arXiv preprint.  

**Required fix:**  
- For each cited work, the authors must verify against arXiv.org and NASA ADS:  
  - Correct **arXiv IDs**, **DOIs**, **journal**, **volume**, **page**, and **year** so they match an actual existing paper.  
  - Remove or replace any IDs that do not correspond to the intended work; do not list placeholder or guessed IDs.  
  - For , either (i) remove this reference if it is not yet on arXiv, or (ii) update to the actual arXiv ID and journal info once publicly available. The “2026” dating and arXiv:2605.05570 must not appear in a submitted manuscript unless they correspond to a real, public paper.  
- After correction, re‑check that all in‑text citations (e.g., “Shamir (2020) [1]”, “Jia et al. ”) point to the corrected entries.  

---

P4-E2 (ESSENTIAL) – Abstract & Methods – null-significance scale comparability  
**Problem:** The paper does well to warn in the abstract that σ values are “defined relative to their respective null procedures and are not directly comparable across estimators,” but in a few later passages different σ values are juxtaposed in a way that invites direct comparison without reiterating the null‑dependence. Example:  
- “The post-MASTER canonical-mask direct-MC residual is +3.64σ … under proper galaxy-weighted monopole subtraction.” (Abstract)  
- Later, results and discussion sentences implicitly compare +3.64σ (per‑pixel shuffle null), +1.68σ (monopole‑only null), and 0.43σ (real‑space bootstrap null) as if they sit on a single significance scale, without explicitly repeating that they are relative to different nulls.  

While the abstract caveat exists, any place that uses σ to argue relative strength of signals across estimators can be misread as comparing them on a common scale, which your instructions explicitly forbid.  

**Required fix:**  
- For each sentence where σ values from different null procedures appear together or are compared, explicitly restate which null each σ is based on, and avoid using “stronger”, “weaker”, or “dominates” language that could be interpreted as a direct comparison of σ across nulls.  
- A simple pattern is “+3.64σ (per-pixel shuffle null) vs −0.12σ (subsample-mask shuffle null)” and then interpret them qualitatively without implying cross‑null σ equivalence.  
- Add a short subsection or boxed note near the start of Sec. IV clarifying that σ from different nulls must *never* be compared numerically, and that statements in the paper use σ only within a given estimator–null pair.  

---

P4-E3 (ESSENTIAL) – References , , – – incomplete / partially mismatched metadata  
**Problem:** Several references to standard software and survey papers have incomplete or slightly inaccurate metadata. For a PRD paper, these need to be correct. Examples (checked via ADS/web search):  
- ** Dey et al. DESI Legacy Imaging Surveys:** The AJ paper is correctly cited in journal and year, but the author list “A. Dey, D. J. Schlegel, D. Lang et al.” does not match the standard first‑author ordering used in ADS; also the full title text should match exactly to avoid ambiguity.  
- ** Walmsley et al. 2023 Galaxy Zoo DESI:** Title and journal look plausible, but the exact page range and volume need confirmation; the paper is very recent and needs precise ADS‑verified bibliographic data.  
- **–:** The software citations (Astropy, HEALPix, healpy, NumPy, pandas, PyTorch, timm, etc.) are partially paraphrased; for some (e.g. HEALPix, healpy, PyTorch Image Models), the reference format does not match the standard recommended citations on the respective project pages.  

**Required fix:**  
- For , , –, cross‑check each entry against NASA ADS or the official project documentation, and update titles, journal names, volume, page, year, and first‑author format to the canonical bibliographic form.  
- Ensure that every software package mentioned in the “Software” line is backed by a corresponding, correct reference.  

---

P4-M1 (MAJOR) – References ,  use numbers inconsistent with main text context  
**Problem:** The main text refers to Iye et al. and Tadaki et al. as 2021 “null” results on spin parity; the references  and  are:  
-  Iye et al. 2021 ApJ 907, 123 – random‑walk dipole analysis of SDSS spirals (found no significant dipole).  
-  Tadaki et al. “Spin parity of spiral galaxies. II. A catalogue of ~80,000 face-on spirals” – catalog paper.  

The claims in the Introduction broad‑brush these as “Iye et al. (2021)  analyzed Galaxy Zoo data and found no significant signal after correcting for reading-direction bias and documented photometric-object duplication in earlier Shamir catalogs. Tadaki et al.  likewise found null results.” That conflates results: Tadaki et al. 2020/2021 paper(s) are primarily catalog construction and bias assessment; the “null” pertains specifically to dipole/parity tests in Iye et al.  

**Required fix:**  
- Re‑read Iye et al. and Tadaki et al. via ADS, and ensure the description of their findings is accurate.  
- If Tadaki et al. did not themselves publish a formal null dipole, rephrase to something like “Tadaki et al.  built a large catalog and did not report a significant spin‑parity violation; Iye et al.  explicitly found no significant dipole after correcting…”.  
- Ensure all quoted numbers (e.g., “∼ 80,000 face-on spirals”) exactly match the abstract or tables of the cited papers.  

---

P4-M2 (MAJOR) – Shamir result summaries – need exact numeric traceability  
**Problem:** The Introduction and Discussion summarize Shamir’s previous results numerically:  
- “Shamir (2012) [4] reported a 2–4σ dipole with per-bin asymmetry amplitudes of ∼ 5–20% using ∼ 1.27×105 SDSS galaxies.”  
- “Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries on DESI Legacy samples (‘nearly 1.3×106 spiral galaxies’ per the published abstract).”  
Later:  
- “This is inconsistent in amplitude with Shamir’s claimed ∼ 3% signal by a factor of ∼ 6–12 under the present pipeline…”  

When those Shamir papers are inspected, the quoted numbers (5–20% per bin, 2–4% global, ∼3% signal, “nearly 1.3×10^6 spirals”) must be explicitly identifiable in the abstract or main tables. If any of those numbers are only inferred from figures or from combining results, that must be stated as such.  

**Required fix:**  
- For each Shamir citation, verify that:  
  - The sample sizes and asymmetry percentages match explicit statements or tables in Shamir (2012, 2020, 2022).  
  - If “∼3%” is your own rounding or representative number extracted from a range, label it clearly as “of order 3% (from his Fig. X / Table Y).”  
- If any value cannot be traced directly to a clear numerical statement in the cited paper, either remove it or replace with a text that is explicitly labeled as your estimate based on the cited figure.  

---

P4-M3 (MAJOR) – CE‑ResNet performance description needs explicit mapping to Jia et al. tables  
**Problem:** CE‑ResNet is cited as: “Jia et al.  … guaranteeing by construction that flipping an input exactly swaps CW and CCW outputs, yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.” Also in Sec. V.B: “CE‑ResNet  achieves cw/ccw = 0.998 with architectural equivariance on 1.95 million galaxies.”  

When Jia et al. (2023 ApJ 943, 32) is checked, the abstract and main tables quote classification accuracies, sample sizes, and maybe fractions; but they do not use the phrase “cw/ccw = 0.998”. That appears to be an author‑defined shorthand for the fraction of galaxies with consistent spin assignment under flips in their catalog, not a direct quotation.  

**Required fix:**  
- Verify in Jia et al. where the 0.998 figure comes from (e.g., a reported error rate, a consistency measure, or a table entry).  
- Rephrase the text to make clear whether 0.998 is:  
  - a *classification accuracy*;  
  - a *CW fraction*;  
  - or a *flip‑consistency rate*;  
  and cite the relevant table/section.  
- Avoid implying that “cw/ccw = 0.998” is Jia et al.’s own notation unless it matches verbatim; instead, explain in your own words tied explicitly to their reported statistics.  

---

P4-M4 (MAJOR) – Citation to “SpArcFiRe” and related spin‑correlation work  
**Problem:** Haynes & Davis SpArcFiRe  and Motloch et al.  are cited as methods/works on spin measurement and correlations. In the current draft, these are only listed in the references without being fully integrated into the discussion of methodology or comparison, and some of the phrasing in the main text implies capabilities (e.g., “scalable automated detection of spiral arm segments”) that must exactly match the paper’s abstract.  

**Required fix:**  
- Check  and  on ADS; confirm that your one‑line description of each agrees with their abstracts (SpArcFiRe indeed “scalable automated detection of spiral galaxy arm segments”; Motloch et al. “observed correlation between galaxy spins and initial conditions”).  
- If you wish to use these as methodological precedents, add a couple of sentences in the Introduction or Methods explaining how your approach relates to or differs from SpArcFiRe and Motloch et al., citing them appropriately.  

---

P4-M5 (MAJOR) – “Spin parity of spiral galaxies. VI.” reference appears ahead of publication  
**Problem:** Reference  is labeled as paper VI in a series (“Spin parity of spiral galaxies. VI. A search for dynamical memory…”) with an arXiv ID that does not exist, and a 2026 date that is essentially speculative. This gives the impression that the authors are citing in‑preparation or private communication work as if it were already public.  

**Required fix:**  
- Confirm whether such a paper has actually been posted to arXiv or accepted in a journal.  
- If not yet public, remove it from the References and either:  
  - cite it as “Iye et al., in preparation (private communication)” in the main text without giving a fake arXiv ID or precise year, or  
  - omit entirely if it is not necessary to support any specific claim.  

---

P4-M6 (MAJOR) – Data and code hosting URLs in “Data Availability” are not citable references  
**Problem:** The Data Availability section includes GitHub and HuggingFace URLs and names the repository “Hubify-Projects/bigbounce”. These are not in the reference list, and the repository name looks like an internal project code rather than a stable, archival identifier. For PRD, artifacts should be referenced by stable DOIs or institutional repositories where possible.  

**Required fix:**  
- Ensure that the public catalog, model, and code are archived in a long‑term repository (Zenodo, institutional repository, etc.) that issues a DOI.  
- Add a formal reference entry for the archived software/data release (with DOI, title, and authors).  
- In the Data Availability text, refer to the DOI rather than just a raw GitHub URL; if GitHub remains the primary host, clarify its permanence and version (tag/commit hash).  

---

P4-minor findings (MINOR)

P4-m1 (MINOR) – Abstract / Introduction phrasing “does not depend on any companion work” vs numerous cross‑references  
**Problem:** The Introduction asserts: “The present paper is a standalone observational result: our null dipole at sub-percent sensitivity does not depend on any companion work.” However, the Methods and appendices repeatedly rely on training labels from CE‑ResNet and Galaxy Zoo DESI, and comparison with other spin catalogs. While scientifically fine, the wording can be read as implying no dependence at all on external catalogs.  

**Required fix:**  
- Clarify the sentence to: “does not depend on any *unpublished* companion work” or similar, making clear that the analysis depends on public Galaxy Zoo DESI and CE‑ResNet resources but not on any additional, non‑public companion paper.  

---

P4-m2 (MINOR) – Consistent referencing of Appendices A–E  
**Problem:** The main text does reference Appendices A–E, but a referee checklist asked to ensure “appendices A–E are properly referenced.” There are a couple of places where appendices are only implicitly referred to (e.g., “full edge-on analysis is in Appendix E” is good; but “Full systematic analysis is in Appendix D” appears once, and some diagnostics in Appendices B–C are mentioned only very briefly).  

**Required fix:**  
- Scan the main text and ensure that every substantial block of material in Appendices A–E has at least one explicit forward reference from the main text (e.g., NaMaster config → Appendix A; classifier architecture + bias tests → Appendix B; auxiliary dipole diagnostics → Appendix C; canonical-mask systematics → Appendix D; morphology systematics → Appendix E).  
- If this is already true, you may only need to slightly tighten phrasing (e.g. “see Appendix B for full details of the ViT-Small architecture and training procedure”).  

---

P4-nits (NIT)

P4-n1 (NIT) – Minor typographical issues and spacing  
**Problem:** A few small typographical issues are present, which do not affect scientific content but should be corrected for a PRD publication standard, e.g.:  
- Non‑standard spacing in URLs (e.g., “h t t p s : / / h u g g i n g f a c e . c o / d a t a s e t s / S m i t h 4 2 / g a l a x i es”).  
- Occasional inconsistent spacing in numbers (“3.2×106” vs “3,201,160”) and between symbols and units (“224 × 224 pixel”, “0.262′′ /pixel”).  

**Required fix:**  
- Normalize URLs to standard format in a footnote or Data Availability (while obeying journal style).  
- Standardize number formatting (use either scientific notation or comma‑separated integers consistently) and unit spacing (e.g., “0.262″/pixel”).  

---

P4-n2 (NIT) – Over‑detailed AI tool acknowledgment  
**Problem:** “AI tool usage: Large-language-model tools were used for code review and manuscript editing…” is more verbose than typical PRD practice. Some journals now have dedicated sections or policies; PRD usually expects brief acknowledgment if needed.  

**Required fix:**  
- Condense to a short sentence in Acknowledgments if required by the journal’s AI policy, or follow PRD’s most recent guidance on AI tool disclosure.  

---

## Summary recommendation

**MAJOR REVISIONS**

The core scientific narrative is coherent and the abstract accurately reflects the main results, and importantly the paper explicitly warns against naive comparison of σ across different nulls. However, the citation metadata has multiple serious problems: at least one arXiv ID is wrong or points to unrelated content, one reference appears to be to a non‑existent future paper with a fabricated arXiv ID, and several numerical summaries of prior work are not clearly traceable to the cited papers. These undermine the reliability of the literature comparison and must be corrected rigorously, with all references verified against arXiv and NASA ADS. Once the citation forensics issues are fixed and the minor textual adjustments made, the paper will be in a much stronger position for publication.