# P4 R9 — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 58.5s

---

P4-E1 (ESSENTIAL) – References section, page 9–10  
**Problem:** Reference [1] is cited as “L. Shamir, ‘Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,’ Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.” The arXiv record 2007.16116 and the published Astrophysics and Space Science article list the title as “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles of the large-scale structure.” The trailing phrase “of the large-scale structure” is missing.  
**Required fix:** Update the title in ref. [1] to match the published title exactly, including “of the large-scale structure,” or clearly state that a shortened title is being used.

---

P4-E2 (ESSENTIAL) – References section, page 9–10  
**Problem:** Reference [2] is listed as “L. Shamir, ‘Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,’ Publ. Astron. Soc. Jpn. 74, 1114 (2022), DOI:10.1093/pasj/psac058.” NASA ADS and the PASJ publication record for this DOI show the article is by Shamir in PASJ 74, 1114 (2022), but the official title is “Analysis of the alignment of non-random patterns in populations of spiral galaxies” (no “of spin directions”). The in‑paper title appears to be a hybrid of the older arXiv phrasing and the journal version.  
**Required fix:** Harmonize ref. [2] with the published PASJ title exactly, or explicitly state that the arXiv title is being quoted if that is intended and correct (and then ensure it matches the arXiv record).

---

P4-E3 (ESSENTIAL) – References section, page 9–10  
**Problem:** Reference [3] is given as “L. Shamir, ‘Analysis of spin directions of galaxies in the DESI Legacy Survey,’ Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.” The MNRAS 516, 2281 (2022) paper with DOI 10.1093/mnras/stac2372 has the title “Analysis of spin directions of galaxies in the DESI Legacy Survey” and is indeed arXiv:2208.13866; this looks consistent. However, the paper text cites this as “Shamir (2022) [3] reported results with ∼ 2–4% asymmetries on DESI Legacy samples” (Introduction, page 2). Reading the abstract and main results, Shamir (2022) quotes a global spin asymmetry at the few-percent level but not as “2–4% asymmetries” on “nearly 1.3×10^6 spiral galaxies” in exactly the way phrased here. The “nearly 1.3×10^6 spiral galaxies” wording is from Shamir’s abstract, but you should ensure the ∼2–4% range and the exact sample description match his quoted statistics (he reports specific asymmetry values and subsamples).  
**Required fix:**  
- Verify directly from Shamir (2022) the precise asymmetry percentages and sample sizes reported in his abstract and tables.  
- Replace “∼ 2–4% asymmetries on DESI Legacy samples (“nearly 1.3×10^6 spiral galaxies” per the published abstract)” with a quantitatively accurate statement that matches his reported amplitudes and sample size wording (e.g., quote his main asymmetry value and the exact sample size he states).  

---

P4-E4 (ESSENTIAL) – Introduction, page 2; Discussion / Conclusions, multiple pages  
**Problem:** The paper repeatedly compares its null to “Shamir’s claimed ∼ 3% signal” and states that the present pipeline disfavors “the Shamir ∼ 2–4% detection class by a factor of ∼ 6–12” and “disfavors … any model predicting … dipole ≥ 0.75%, including the Shamir ∼ 3% amplitude class.” However, none of the Shamir papers [1–4] are explicitly documented here with a single canonical 3% dipole amplitude on a survey matching this footprint; the numbers are amalgams (2–4% range from various works). The paper presents these as if they were a single well‑defined “3% amplitude” benchmark. That is a fused/averaged characterization, not a directly quoted result.  
**Required fix:**  
- For each Shamir paper you use as a benchmark (2012, 2020, 2022), state the exact reported asymmetry/dipole amplitude with citation, as given in that paper (e.g., “Shamir (2012) finds X%, Shamir (2020) finds Y% ...”).  
- Replace phrases like “the Shamir ∼ 3% amplitude class” and “2–4% detection class” with language that clearly attributes the specific numbers to specific papers, or explicitly label “∼3%” as a rough representative value. Do not present “3%” as a single measured quantity if it is a heuristic average.  

---

P4-E5 (ESSENTIAL) – Reference [5], page 9–10  
**Problem:** The paper cites Iye et al. (2021) [5] as “M. Iye, M. Yagi, and H. Fukumoto, ‘Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,’ Astrophys. J. 907, 123 (2021), arXiv:2011.00662.” The arXiv entry 2011.00662 and ApJ 907, 123 do indeed correspond to this title and author list; metadata is correct. However, in the main text you say “Iye et al. (2021) [5] analyzed Galaxy Zoo data and found no significant signal after correcting for reading-direction bias and documented photometric-object duplication in earlier Shamir catalogs.” Iye et al. explicitly reanalyze Shamir’s SDSS spin catalog, but they do not “analyze Galaxy Zoo data” in the sense of using Galaxy Zoo spirals as their primary sample; they use a carefully re‑curated SDSS sample and random‑walk simulations.  
**Required fix:**  
- Re‑read Iye et al. (2021) and correct the description. For example, say that they re-examined Shamir’s SDSS spin sample, employing 3D random walk simulations and checking for duplication/systematics, and obtained a null result, if that matches their abstract and conclusions.  
- Remove or correct the claim that they “analyzed Galaxy Zoo data” if that is not literally what their sample is.  

---

P4-E6 (ESSENTIAL) – Reference [6], page 9–10  
**Problem:** Tadaki et al. [6] is given as “K. Tadaki, M. Iye, H. Fukumoto et al., ‘Spin parity of spiral galaxies. II. A catalogue of ∼ 80,000 face-on spirals,’ Mon. Not. R. Astron. Soc. 496, 4276 (2020), arXiv:2006.02331.” This matches the arXiv entry 2006.02331 and its MNRAS publication. In the Introduction you state “Tadaki et al. [6] likewise found null results.” Tadaki et al. compile a catalog and discuss spin parity; you must ensure that they in fact report a null, in the sense you mean (no statistically significant global spin parity asymmetry). If their abstract and results present upper limits or mixed findings, “null results” may be an over‑simplification.  
**Required fix:**  
- Verify from Tadaki et al. (2020) whether they explicitly conclude that spin parity is consistent with isotropy (null).  
- If they instead provide, for example, upper limits or constraints, rephrase your summary to match their conclusions precisely (e.g., “they found spin parity consistent with random at Xσ, placing an upper limit of Y%”).  

---

P4-E7 (ESSENTIAL) – Reference , page 9–10; Section V.B, page 5  
**Problem:** Reference  is “H. Jia, H.-M. Zhu, and U.-L. Pen, ‘Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,’ Astrophys. J. 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa.” This matches arXiv and ApJ. The main text states “Jia et al.  introduced CE-ResNet, a chirality-equivariant CNN guaranteeing by construction that flipping an input exactly swaps CW and CCW outputs, yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.” You must verify that Jia et al. explicitly claim exactly‐equivariant behavior under flip and that they state a cw/ccw ratio of 0.998 on a 1.95M‑galaxy sample. If those exact numbers are not literally in their paper (e.g., if they quote a slightly different ratio or a different sample size), this is an over-precise paraphrase.  
**Required fix:**  
- Check Jia et al. (2023) for: (a) the explicit equivariance condition they prove/implement; (b) the exact cw/ccw fraction and galaxy count reported.  
- Replace “yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies” with the exact numbers they provide (or a clearly approximate statement like “about 0.998” and “about 1.95 million” if that is consistent). Ensure the claim “exactly swaps CW and CCW outputs” uses their own terminology (e.g., “equivariant to reflection”) or is otherwise fully supported.  

---

P4-E8 (ESSENTIAL) – Reference , page 9–10  
**Problem:** Dey et al. (2019)  is cited for DESI Legacy Imaging Surveys. The metadata (authors, journal, volume, arXiv:1804.08657) matches ADS. No issue there. However, in the Data section you state “DR8 comprises three distinct imaging campaigns: BASS+MzLS (δ > +32◦), DECaLS (δ < +32◦), and a DES overlap region.” Dey et al. indeed describe BASS+MzLS and DECaLS, but the exact declination boundary and description of the DES overlap need to be consistent with DESI Legacy documentation. If any of the numerical declination cuts or campaign boundaries differ from Dey et al.’s text, this is a misstatement.  
**Required fix:**  
- Cross‑check Dey et al. (2019) and the DESI Legacy DR8 documentation for the precise definition of the imaging regions, especially the declination boundary and the nature of the DES overlap.  
- Correct the wording and boundary values if they are not faithful to the cited source (or add a clarification if the δ = +32° split is specific to your selection, not the survey definition itself).  

---

P4-E9 (ESSENTIAL) – References , , , [34–39], page 9–10  
**Problem:** The methods rely on HEALPix, NaMaster, PyTorch, timm, and other software libraries. The references  (NaMaster),  (MASTER), [34,35] (HEALPix/healpy), [36,37] (NumPy, pandas),  (PyTorch),  (timm) appear to correspond to standard citations and look consistent with ADS and software documentation. However, you use specific configuration statements in the text (e.g., “pymaster 2.6”, “nmt.NmtBin.from lmax linear(lmax=191, nlb=1)”) that are not backed by explicit citations to the NaMaster documentation. This is borderline for forensics but relevant for reproducibility.  
**Required fix:**  
- Add a brief footnote or clarifying sentence citing the specific NaMaster documentation or version notes (beyond just ) if any behavior (e.g., single‑ℓ bins) relies on version‑specific features. This is not about metadata correctness but ensuring that all technical behavior you attribute to NaMaster is clearly tied to the referenced version.  

---

P4-M1 (MAJOR) – Multiple sections, σ comparisons; Abstract, Section III.A, Table I  
**Problem:** You follow the instruction to state that “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table II for the mapping of each result to its null.” However, in several places you nevertheless compare amplitudes and quote “disfavors” in a way that a casual reader will interpret as comparing significances on the same footing. Examples:  
- Abstract: “This is inconsistent in amplitude with Shamir’s claimed ∼ 3% signal by a factor of ∼ 6–12 under the present pipeline…” but Shamir’s quoted σ significances are computed against different nulls, with very different survey systematics.  
- Conclusions: “The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥ 0.75% … including the Shamir ∼ 3% amplitude class by a factor of ∼ 6–12.”  
Even though you label this “in amplitude,” the mapping from your injection‑recovery threshold (defined under a particular per-pixel shuffle null and classifier noise model) to Shamir’s effective sensitivity is nontrivial and not quantitatively justified.  
**Required fix:**  
- Add an explicit caveat wherever you compare your amplitude threshold to Shamir’s claimed amplitudes, reminding readers that the noise models, footprints, and systematics differ, so direct σ comparison is not valid and the “factor of 6–12” is heuristic.  
- Replace strong language like “disfavors … by a factor of ∼ 6–12” with more careful phrasing: e.g., “Under our pipeline, a 3% dipole would be detected at high significance (given our injection‑recovery study); our null thus strongly suggests that any true dipole on the DESI Legacy footprint is below this level, but a matched‑footprint reanalysis with Shamir’s pipeline is required for a formal statistical exclusion.”  

*(This is flagged MAJOR rather than ESSENTIAL because you do state non‑comparability of σ; but the rhetoric still risks misinterpretation and should be toned down for PRD.)*

---

P4-M2 (MAJOR) – Abstract accuracy vs body, page 1 vs Sections IV & VI  
**Problem:** The abstract says “The measured dipole is consistent with null: the equivariant CW fraction is 0.4974 ± 0.000279 and the post-MASTER dipole significance is −0.122σ (subsample mask, headline) / +0.43σ (real-space cross-check).” This is aligned with the body. However, the abstract also foregrounds the canonical-mask residual (+3.64σ) in a way that could be read as quasi‑detection: “a quantifiable monopole-mask leakage channel, and diagnostic evidence for a depth/morphology-correlated canonical-mask residual…” without immediately emphasizing that this is *not* treated as a cosmological detection. Only later in the introduction is this clarified. For a forensics context, the abstract should clearly and succinctly say “no cosmological detection; residual is interpreted as systematic” to prevent misinterpretation.  
**Required fix:**  
- Add one explicit clause in the abstract that the +3.64σ canonical-mask signal is fully attributed to survey/systematic effects and not interpreted as a cosmological parity violation or dipole detection. This aligns the abstract more transparently with the later “not interpreted as cosmological signal” statements.  

---

P4-M3 (MAJOR) – Length vs contribution  
**Problem:** The paper devotes extensive space (multiple appendices plus long in‑text descriptions) to internal diagnostic machinery (TTA, bias tests T1–T8, morphological systematics, WLS template fits, etc.) relative to the core cosmological result (a null ℓ = 1 dipole). For a PRD methods paper this may still be acceptable, but as currently written, the manuscript reads closer to 10 pages full‑text with dense appendices for a single null measurement and one new catalog. Many derivations are essentially implementation details of a survey‑specific pipeline rather than general methodology.  
**Required fix:**  
- Condense the internal audit/bias‑hardening descriptions in the main text, moving as much as possible into appendices or a companion data‑release paper. Aim for a main‑text length of ≲ 7 journal pages for the core cosmological analysis, leaving technical training/architecture details to supplementary material. Focus the main narrative on: data description, estimator definitions, null construction, main dipole constraints, and a short comparison to prior work.  

---

P4-M4 (MAJOR) – Informal or ambiguous attributions, multiple locations  
**Problem:** Several phrases attribute interpretation to “the present ViT/TTA pipeline” or “our DESI/ViT-Small pipeline” when discussing prior works’ results (e.g., “The prior literature’s pre-MASTER dipole-detection claims are therefore explained at the percent level by this leakage channel under our DESI/ViT-Small pipeline.”) This could be read as claiming that you have definitively explained Shamir’s SDSS signals and other past claims, whereas you have analyzed a different footprint and catalog. The methodology you develop shows the *possibility* of such leakage, but not that it *did* cause those specific published results.  
**Required fix:**  
- Rephrase such claims to be clearly conditional or illustrative: e.g., “We demonstrate that in our DESI/ViT-Small pipeline, a small monopole can generate a spurious pre‑MASTER ℓ=1 signal at the percent level; this provides a plausible mechanism for similar pre‑MASTER signals in earlier work, though a direct reanalysis of those surveys would be needed to confirm.”  

---

P4-M5 (MAJOR) – “Null procedures” and σ scale, global clarity (connects to instruction #7)  
**Problem:** The paper does state early: “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table II for the mapping of each result to its null.” However, there are many σ values quoted in quick succession (e.g., +3.64σ, +3.05σ, −0.122σ, +0.43σ, +6.48σ, etc.) with various nulls (label shuffle, isotropic bootstrap, monopole-only MC, etc.), and Table I puts them all into a single column labeled “σ.” Even with the textual caveat, the layout encourages cross‑comparison. This is very close to violating the instruction that no σ from different nulls be presented “as if on the same scale.”  
**Required fix:**  
- In Table I, explicitly label the σ column as “σ (null‑specific; not comparable across rows)” and add a footnote reiterating that each σ uses a different null and variance model.  
- Within the main text, whenever two σ from different nulls are mentioned together, explicitly state the null types again (e.g., “+3.64σ under a label-permutation null vs −0.122σ under a monopole‑subtracted MASTER null”).  

---

P4-M6 (MAJOR) – Data availability URLs in text, page 9  
**Problem:** The Data Availability section includes full URLs to HuggingFace and GitHub. PRD generally allows URLs but prefers them in footnotes or references. More importantly for the forensics role: one of the dataset URLs is written as “https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog” with an apparent space in “datasets” and in “galaxy- chirality- catalog” that would break the link. The HuggingFace search confirms the correct dataset path is “datasets/bamfai/galaxy-chirality-catalog.”[4]  
**Required fix:**  
- Fix the broken URL by removing spurious spaces so that the dataset path “datasets/bamfai/galaxy-chirality-catalog” is correct.  
- Optionally, move URLs to footnotes or a short “External resources” paragraph in line with PRD style, but the critical fix is the typo.  

---

P4-M7 (MAJOR) – “Standalone observational result” wording, Introduction, page 2  
**Problem:** The Introduction says “The present paper is a standalone observational result: our null dipole at sub-percent sensitivity does not depend on any unpublished companion work.” You then rely heavily on the external Smith42/galaxies HuggingFace dataset, Galaxy Zoo DESI predictions, and CE-ResNet labels, as well as a public model release “v2026.04.” None of these is unpublished, but to avoid any ambiguity about dependence on prior analysis, you should clarify the role of these external resources.  
**Required fix:**  
- Clarify that while the catalog construction uses publicly released external datasets and models, the analysis and conclusions in this paper do not rely on any *unpublished* companion manuscripts. For example: “This paper is a standalone analysis in the sense that all inputs (DESI Legacy DR8, Galaxy Zoo catalogs, CE-ResNet labels, and our own released model) are publicly available and no results depend on unpublished companion studies.”  

---

P4-m1 (MINOR) – “cw/ccw = 0.998” vs “cw/(cw + ccw)” notation, Section V.B, page 5  
**Problem:** You describe CE-ResNet as “yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies,” whereas everywhere else you use cw/(cw + ccw) to describe fractions. Jia et al. (2023) likely report the fraction of Z‑wise vs S‑wise galaxies; using the ratio cw/ccw is potentially ambiguous (is it f_cw/f_ccw or f_cw?).  
**Required fix:**  
- Harmonize notation; e.g., if Jia et al. report f_cw ≈ 0.499 and f_ccw ≈ 0.501, then express it as “cw/(cw+ccw) = 0.498–0.502 (approximately 0.998 balance)” or similar, consistent with how you define your own cw fraction.  

---

P4-m2 (MINOR) – Potential fused phrase “nearly 1.3×10^6 spiral galaxies,” Introduction, page 2  
**Problem:** You attribute to Shamir (2022) the phrase “nearly 1.3×10^6 spiral galaxies” in quotes. This must match his abstract wording exactly if quoted. If he instead writes “approximately 1.3 million galaxies” or similar, your quotation marks are misleading.  
**Required fix:**  
- Verify Shamir (2022) abstract wording. If not exact, either rephrase without quotes (“about 1.3×10^6 spiral galaxies”) or quote precisely.  

---

P4-m3 (MINOR) – Reference  vs  scope, page 9–10  
**Problem:** You cite Lintott et al. (2008)  for Galaxy Zoo 1 and Land et al. (2008)  for Galaxy Zoo spin statistics. In the text, you use GZ1 labels and mention GZ spin bias work. Ensure that whenever you discuss Galaxy Zoo spin bias (e.g., reading-direction bias), you cite the correct paper (Hayes et al. 2017 ) rather than overloading /.  
**Required fix:**  
- Review the Galaxy Zoo–related citations and ensure that claims about spin bias and its correction are attributed to Hayes et al. (2017) , not just to the original Galaxy Zoo description papers.  

---

P4-m4 (MINOR) – “LSST extrapolations and spectroscopic-redshift upgrade paths are deferred to a future matched-footprint analysis,” Section VI.A, page 6  
**Problem:** This statement implicitly suggests a planned future paper but gives no citation (“in preparation”). For a forensics context, you must avoid implying an existing companion work if it is not yet available.  
**Required fix:**  
- Either remove any implication of a specific future paper (“deferred to future work”) or make it generic (“deferred to future studies”) so as not to imply a concrete in‑prep manuscript.  

---

P4-n1 (NIT) – Minor spacing / hyphenation artifacts, various locations  
**Problem:** There are small typesetting artifacts, likely from PDF->text conversion, e.g.:  
- “galaxy- chirality- catalog” with stray spaces around hyphens.  
- “galax- ies” split across lines, “gala xy-chirality-v2” with added spaces.  
These are cosmetic but should be fixed in the final typeset version.  
**Required fix:**  
- Clean up all instances of broken words and spurious spaces around hyphens in URLs and dataset/model names.  

---

P4-n2 (NIT) – Repeated “canonical-mask” phrasing  
**Problem:** Phrases like “canonical-mask residual,” “canonical-mask direct-MC,” “canonical-mask post-MASTER residual” are used very frequently. This is not an exact duplicate phrase artifact like “canonical canonical-mask,” but the repetition is stylistically heavy.  
**Required fix:**  
- Where possible, vary phrasing or define “canonical mask” once and then refer briefly to “the canonical residual,” etc., to improve readability. No change in scientific content is required.  

---

## Summary recommendation

**MAJOR REVISIONS**

The core citations (arXiv IDs, journals, DOIs) are largely correct, but several descriptions of prior work are either too loose (Shamir amplitude claims, Iye/Tadaki characterization, CE-ResNet performance) or risk over‑interpreting your results as explaining earlier detections. There is also a near‑miss on cross‑comparing σ from heterogeneous nulls, and the manuscript is longer and more discursive than necessary for its main null result. These issues require careful textual revision and modest structural tightening before the paper can meet PRD’s standards.