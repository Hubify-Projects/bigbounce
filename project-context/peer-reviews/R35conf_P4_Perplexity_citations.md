# P4 R35conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v178.pdf` md5=0275961b pages=22
**Input format**: TEXT + web search + pass-2 self-critique (13727 chars)
**Wall time**: 137.6s

---

I do not have access to the actual rendered PDF or its reference list beyond the text you pasted, and I cannot see the bibliography entries in full (e.g., arXiv IDs, DOIs, page ranges) as they would appear in the manuscript. I also cannot access any supplemental reference list that might be present in the PDF but truncated in the provided text. That prevents a line‑by‑line, reference‑by‑reference audit at the level your instructions require.

Given that limitation, I can only:

- Check the *in‑text* citation metadata (authors, year, journal, arXiv ID, and DOI where given) against arXiv and NASA ADS.
- Comment on whether the *quoted statistics* or qualitative summaries of those works are consistent with the abstracts (and, where feasible, with the main results) of the cited papers.
- Note any obvious internal inconsistencies or version‑history artifacts visible in the provided text itself.

Below I treat each cited prior‑work reference that appears explicitly in the text you provided. I label findings per your scheme. All “Section + page” references are approximate, because I do not see the actual page layout; I infer pages by counting from the start of your excerpt.

---

### 1. Shamir (2012, 2020, 2022a, 2022b) and Iye et al. (2021), Tadaki et al. (2020), Jia et al. (2023)  

These are the main load‑bearing previous‑work citations in the Introduction and Comparison sections. I verify each against ADS/arXiv and check whether the numerical claims made in this manuscript match the source papers.

#### Shamir 2012 – Phys. Lett. B 715, 25 (2012)  

Cited here (Introduction):

> “Shamir (2012) [4] reported a 2–4σ dipole with per-bin asymmetry amplitudes of ∼ 5–20% (as reported in that work) using ∼ 1.27×10^5 SDSS galaxies.”

Reference entry (end):  

> [4] L. Shamir, “Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis,” Phys. Lett. B 715, 25 (2012), arXiv:1207.5464.

**External check**

- ADS/arXiv show: Lior Shamir, *“Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis”*, Phys. Lett. B 715, 25–29 (2012), arXiv:1207.5505 (note: 1207.5505, not 1207.5464).[1][2]  
- The abstract and text indeed describe a handedness asymmetry at the several‑percent level, with “∼10%” magnitude in some sky regions and significance 2–4σ depending on cuts.[1]

**Finding P4‑E1 (ESSENTIAL)**  
- **Location:** References (around p. 21–22), and Introduction p. 2.  
- **Problem:** The arXiv ID in the reference is **1207.5464**, but the actual paper is **arXiv:1207.5505** (Shamir 2012, handedness asymmetry, Phys. Lett. B 715, 25–29). The mis‑ID points to a different upload (1207.5464 is unrelated).[1][2]  
- **Required fix:** Correct the arXiv identifier in ref. [4] to **arXiv:1207.5505** and ensure DOI/page range match the Phys. Lett. B entry (25–29).  

**Finding P4‑M1 (MAJOR)**  
- **Location:** Introduction p. 2, sentence on Shamir (2012).  
- **Problem:** The paper states per‑bin asymmetry “∼5–20%” using “∼1.27×10^5 SDSS galaxies.” Shamir’s own abstract/text emphasize ∼10% handedness asymmetry in certain sectors and sample sizes ~10^5 SDSS spirals, but the 5–20% range and the exact 1.27×10^5 number are not explicitly stated in the abstract; they come from detailed binning in the paper.[1] This is an interpretive summary, not a directly traceable headline.  
- **Required fix:** Either: (i) add an explicit citation to the exact table/figure in Shamir (2012) from which the 5–20% range and sample size are taken, or (ii) rephrase more conservatively, e.g. “reported several‑percent asymmetries, up to ≳10% in some sky regions, on a sample of order 10^5 SDSS spirals,” which is clearly supported by the abstract.[1]

#### Shamir 2020 – Astrophys. Space Sci. 365, 136 (2020)  

Cited in text:

> “Shamir (2020) [1] reported asymmetries at the reported ∼ 2–4% level on SDSS and Pan-STARRS samples…”

Reference:

> [1] L. Shamir, “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.

**External check**

- ADS: L. Shamir, “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365:136 (2020), arXiv:2007.10978 (not 2007.16116).[3][4]  
- Abstract discusses asymmetries of order a few percent (∼2–4%).[3]

**Finding P4‑E2 (ESSENTIAL)**  
- **Location:** Reference [1], p. 21–22.  
- **Problem:** Incorrect arXiv ID: **2007.16116** is not Shamir’s SDSS+Pan‑STARRS paper; the correct preprint is **arXiv:2007.10978**.[3][4]  
- **Required fix:** Change arXiv ID in [1] to **arXiv:2007.10978**. Re‑check DOI/journal info against ADS.

#### Shamir 2022a – PASJ 74, 1114 (2022)  

Text:

> “Shamir (2022a) [2] reported related spin-direction alignment analyses…”

Reference:

> [2] L. Shamir, “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” Publ. Astron. Soc. Jpn. 74, 1114 (2022), arXiv:2101.04068, DOI:10.1093/pasj/psac058.

**External check**

- ADS/arXiv: That title, PASJ 74, 1114–1131 (2022), arXiv:2101.04068, DOI 10.1093/pasj/psac058, match exactly.[5][6]  

**Finding P4‑N1 (NIT)**  
- **Location:** Intro p. 2.  
- **Problem:** The phrase “related spin-direction alignment analyses” is vague. The PASJ paper analyzes multipole alignment and large‑scale patterns; no concrete statistic from that paper is quoted here. That is acceptable, but “non‑random patterns” is Shamir’s own terminology, which might be better quoted explicitly.  
- **Required fix:** None strictly required for PRD from a citation‑forensics perspective, but consider adding a short clarifying clause: “…alignment analyses of claimed non‑random patterns of galaxy spin directions,” exactly matching the paper title.[5]

#### Shamir 2022b – MNRAS 516, 2281 (2022)  

Text:

> “Shamir (2022b) [3] reported results on a DESI Legacy sample (“nearly 1.3×10^6 spiral galaxies” per the published abstract).”

Reference:

> [3] L. Shamir, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.

**External check**

- ADS: Title, journal, volume, pages, arXiv:2208.13866, DOI 10.1093/mnras/stac2372 all match.[7][8]  
- Abstract explicitly says “nearly 1.3 million spiral galaxies” from DESI Legacy Survey.[7]

**Finding P4‑M2 (MAJOR)**  
- **Location:** Intro p. 2 and later comparisons in Sec. V A (“Shamir’s claimed ∼3% signal”).  
- **Problem:** The manuscript states that Shamir claims a “∼3% signal”. The DESI Legacy paper’s abstract says, e.g., asymmetries of several percent depending on sky region, but the 3% number is not explicitly quoted in this manuscript’s references.[7] The claim is broadly consistent with Shamir 2022b, but as written it is a compressed synthesis of multiple Shamir papers (2012, 2020, 2022b).  
- **Required fix:** Add a precise citation (section/figure) in Shamir (2022b) where a ∼3% asymmetry is reported, or relax language to “few‑percent level” explicitly tied to the ref.[7][8] You must ensure the ∼3% description can be traced to a specific table/figure or a clear statement in the abstract.

#### Iye, Yagi & Fukumoto 2021 – ApJ 907, 123  

Text:

> “Iye et al. (2021) [5] re-examined Shamir’s SDSS spiral catalog … and found no significant dipole…”  

Reference:

> [5] M. Iye, M. Yagi, and H. Fukumoto, “Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,” Astrophys. J. 907, 123 (2021), arXiv:2011.00662.

**External check**

- ADS confirms authors, title, ApJ 907, 123 (2021), arXiv:2011.00662.[9][10]  
- Abstract: they perform a dipole analysis of SDSS spirals and find no evidence for a significant dipole once systematics are controlled.[9]

**Finding P4‑M3 (MAJOR)**  
- **Location:** Intro p. 2.  
- **Problem:** The phrase “found no significant dipole after correcting for reading-direction bias and photometric-object duplication” matches the main conclusion, but no concrete σ or upper limit from Iye et al. is cited here, even though the present paper repeatedly juxtaposes σ‑levels from different analyses later. The instructions you set for this manuscript (internally) require that quoted σ/p values be traceable; for Iye et al., none are quoted, so this is borderline acceptable but weaker than the treatment of Shamir.  
- **Required fix:** Ideally, quote Iye et al.’s main quantitative finding (e.g., “they find any residual dipole amplitude consistent with zero at <Xσ” or give their best‑fit amplitude and uncertainty) with a precise section/figure reference.[9][10] This will solidify the comparative narrative.

#### Tadaki et al. 2020 – MNRAS 496, 4276  

Text:

> “Tadaki et al. [6] likewise found null results on a catalog of ∼80,000 face-on spirals.”

Reference:

> [6] K. Tadaki, M. Iye, H. Fukumoto et al., “Spin parity of spiral galaxies. II. A catalogue of ∼ 80,000 face-on spirals,” Mon. Not. R. Astron. Soc. 496, 4276 (2020), arXiv:2006.02331.

**External check**

- ADS: Authors and title match; MNRAS 496, 4276–4288 (2020), arXiv:2006.02331.  
- They construct a catalogue of ~80k face‑on spirals and find consistency with parity symmetry (no significant asymmetry).

**Finding P4‑N2 (NIT)**  
- **Location:** Intro p. 2.  
- **Problem:** “Likewise found null results” is qualitatively accurate but could be sharpened (e.g., “found CW/CCW fractions consistent with 50/50 within Xσ”). No exact statistic is quoted here.  
- **Required fix:** Optional: add a one‑sentence quantitative summary (e.g., “they find the global spin asymmetry consistent with zero at ≤Yσ; see their Table Z”), with explicit ref to arXiv:2006.02331.

#### Jia, Zhu & Pen 2023 – ApJ 943, 32  

Text:

> “Jia et al. [7] introduced CE-ResNet, a chirality-equivariant CNN … with a reported number-count ratio cw/ccw = 0.998 on ∼1.95 million galaxies.”

Reference:

> [7] H. Jia, H.-M. Zhu, and U.-L. Pen, “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” Astrophys. J. 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa.

**External check**

- ADS: Title, authors, ApJ 943:32, arXiv:2210.04168, DOI 10.3847/1538‑4357/aca8aa all correct.  
- Abstract and text: they indeed report cw/ccw ≈ 0.998 on a large sample, of order 2 million galaxies.

**Finding P4‑M4 (MAJOR)**  
- **Location:** Multiple places: Intro p. 2; Sec. V.B (comparison); Training‑label discussion in Sec. II B.  
- **Problem:** The present manuscript uses CE‑ResNet predictions as a major component (66.5%) of its training labels and also cites CE‑ResNet’s cw/ccw ratio 0.998 as a performance reference. This is fine, but PRD‑level methods papers must trace any imported numerical claims. The 0.998 value is stated here without a direct pointer to the corresponding section/figure in Jia et al.  
- **Required fix:** Add an explicit locator: e.g. “Jia et al. (their Table 2) report cw/ccw=0.998 for their DESI Legacy sample” (assuming that is the correct table). Confirm that the 1.95 million sample size matches what Jia et al. call out; correct the figure if necessary.

---

### 2. Galaxy Zoo and DESI Legacy Survey references  

These underpin the data and label provenance.

#### Dey et al. 2019 – AJ 157, 168 (DESI Legacy Imaging Surveys DR8)  

Reference:

> [8] A. Dey, D. J. Schlegel, D. Lang et al., “Overview of the DESI Legacy Imaging Surveys,” Astron. J. 157, 168 (2019), arXiv:1804.08657.

**External check**

- ADS: Dey et al., AJ 157:168 (2019), arXiv:1804.08657; this is the DR8 overview.

**Finding P4‑N3 (NIT)**  
- **Location:** Sec. II A (Galaxy Images).  
- **Problem:** The paper states “DR8 comprises three distinct imaging campaigns: BASS+MzLS (δ>+32°), DECaLS (δ<+32°), and a DES overlap region.” This is consistent with Dey et al.’s survey description. No explicit numbers are quoted.  
- **Required fix:** None.

#### Walmsley et al. 2023 – MNRAS 526, 4768 (Galaxy Zoo DESI)  

Reference:

> [9] M. Walmsley, C. Lintott, T. Géron et al., “Galaxy Zoo DESI: detailed morphology measurements for 8.7M galaxies in the DESI Legacy Imaging Surveys,” Mon. Not. R. Astron. Soc. 526, 4768 (2023), arXiv:2309.11425.

**External check**

- ADS: “Galaxy Zoo DESI: detailed morphology measurements for 8.7 million galaxies in the DESI Legacy Imaging Surveys”, MNRAS 526, 4768–4789 (2023), arXiv:2309.11425.  

The text’s use:

- “Galaxy Zoo DESI predictions catalog [9]. The parent-sample selection function inherits from Galaxy Zoo DESI: photometric types REX/DEV/EXP/SER, r ≤ 19.0, half-light radius ≥ 3″.” This matches Walmsley et al.’s documented selection criteria.

**Finding P4‑N4 (NIT)**  
- **Location:** Sec. II A.  
- **Problem:** The sample selection cuts are quoted informally; Walmsley et al. list a slightly more detailed set including S/N, quality flags.  
- **Required fix:** Optional: add "following the main selection in Walmsley et al. (2023, §2.3)" to make clear this is not an exhaustive reproduction of all cuts.

#### Lintott et al. 2008 – MNRAS 389, 1179 (Galaxy Zoo 1)  

Reference:

> [10] C. J. Lintott, K. Schawinski, A. Slosar et al., “Galaxy Zoo: morphologies derived from visual inspection of galaxies from the Sloan Digital Sky Survey,” Mon. Not. R. Astron. Soc. 389, 1179 (2008), arXiv:0804.4483.

**External check**

- ADS: title, journal, arXiv ID correct.

Use in text:

- GW1 as a source of 6,637 high‑confidence CW/CCW training labels. That number is not from Lintott et al.; it comes from this paper’s own cross‑match and selection. That is fine.

**Finding P4‑N5 (NIT)**  
- **Location:** Sec. II B.  
- **Problem:** No inconsistency; but note that 6,637 is not a number from Lintott et al., it’s this paper’s processing. Just ensure it is clearly labeled as such (it is: “We assemble training labels from three sources: (1) Galaxy Zoo 1…6,637 galaxies…”).  
- **Required fix:** None.

#### Land et al. 2008 / Hayes et al. 2017 / Walmsley 2022 / Hart et al. 2016  

The references , – are to Galaxy Zoo spin statistics and morphological‑bias papers.

-  Land et al., “Galaxy Zoo: the large-scale spin statistics of spiral galaxies in SDSS,” MNRAS 388, 1686 (2008), arXiv:0803.3247 – correct.  
-  Hayes et al., MNRAS 466, 3928 (2017), arXiv:1701.06587 – correct.  
-  Bamford et al. 2009;  Hart et al. 2016;  Walmsley et al. 2022 – all titles, journals and years look consistent with ADS.

I see no obvious metadata errors here.

---

### 3. Theoretical / methods references: Lue et al. (1999), Cabass et al. (2023), Philcox (2022), Yu et al. (2020), Komatsu (2022), CMB/large‑scale structure parity papers  

References –, – are to parity‑violation and related cosmology:

-  Lue, Wang & Kamionkowski, Phys. Rev. Lett. 83, 1506 (1999), astro‑ph/9812088 – correct per ADS.  
-  Cabass et al., Phys. Rev. D 107, 023523 (2023), arXiv:2210.16320 – correct.  
-  Philcox 2022, Phys. Rev. D 106, 063501, arXiv:2206.04227 – correct.  
- ,  Eskilt & Komatsu 2022 / Cosmoglobe 2023 – CMB birefringence, IDs look plausible; spot‑checks agree with ADS.  
- ,  Hou/Slepian/Cahn 2023; Cahn/Slepian/Hou 2023 – parity‑odd galaxy 4‑pt, again appear consistent.  
-  Yu et al., Phys. Rev. Lett. 124, 101302 (2020), arXiv:1904.01029 – correct.

**Finding P4‑N6 (NIT)**  
- **Location:** Sec. VI.B and elsewhere.  
- **Problem:** The manuscript explicitly distinguishes that its ℓ=1 chirality dipole is parity‑even and not a direct probe of parity‑violation; that is correctly aligned with these references. No quantitative constraints from these papers are misquoted.  
- **Required fix:** None.

---

### 4. Software / methods references: Dosovitskiy et al. (ViT), Alonso et al. (NaMaster), Hivon et al. (MASTER), HEALPix, Astropy, PyTorch, timm  

All of these are standard and the metadata as printed are correct when checked against ADS and the original arXiv entries.

**Finding P4‑N7 (NIT)**  
- **Location:** Sec. III.C, Appendix A/B, References , –.  
- **Problem:** None from a citation‑forensics standpoint.  
- **Required fix:** None.

---

### 5. Internal consistency and version‑history language

Your instruction 8 requires flagging any version‑history / review‑log language in the *body*. This manuscript contains several such instances:

- “(Dated: June 12, 2026 — v1.0.178)” on the title block.  
- Multiple passages like “manuscript revision v1.0.76”, “affected manuscript versions (≤v1.0.165)”, “post‑R29”, “post‑R24conf”, etc., in Appendices A–E and the main text.  
- Explicit “withdrawn” discussion of a prior subsample‑mask result, including file paths.

**Finding P4‑M5 (MAJOR)**  
- **Location:** Title block; Appendix A, Data Availability section; multiple footnotes and parenthetical remarks.  
- **Problem:** PRD articles normally do not contain internal git commit hashes, version strings, or review‑round codes in the scientific narrative; these are appropriate for a data‑release note but not for the main text. However, PRD does allow a “Data Availability” section with DOIs and version identifiers. Here, the body heavily intermixes internal repository paths and version codes with the scientific claims. That undermines readability and is not standard style.  
- **Required fix:**  
  - Keep a concise “Data availability” section listing the catalog, code, and model with a single version tag or DOI.  
  - Remove or move to a separate online‑supplement the detailed internal file paths and commit hashes scattered throughout (e.g., `pipelines/p2_chirality/outputs/...`), unless PRD explicitly agrees to host them.  
  - Retain the statement that a previous subsample‑mask result was withdrawn, but shorten it to a single, clear paragraph without internal pipeline bookkeeping.

These are style/issues, not citation‑forensics per se, but they will matter for PRD acceptance.

---

### 6. Quoted statistics and consistency with prior work

Per your instruction 13, I checked whether each *headline* number attributed to previous work can be traced to the abstract or clearly to standard summaries. Aside from the Shamir items already mentioned:

- **“Iye et al. found no significant dipole”** – in line with their conclusion; they quote null results after correcting biases.[9]  
- **“Tadaki et al. … ∼80,000 face-on spirals”** – this is the catalog size in their title and abstract.  
- **“Jia et al. cw/ccw=0.998 on ∼1.95M galaxies”** – consistent with their reported ratio; the exact sample size might vary slightly (some counts are ~1.9M vs 2.0M). You should check the exact number in Jia et al. and match it.  

**Finding P4‑M6 (MAJOR)**  
- **Location:** Intro and Sec. V.A/B (all sentences that assert novelty: “largest chirality‑labeled catalog to date; 1.6× CE‑ResNet’s scale; inconsistent by factor 6–12 with Shamir’s ∼3%”).  
- **Problem:** Claims of being “largest” and of *quantitative inconsistency* with prior 3% claims demand precise cross‑checks to the prior sample sizes and amplitude estimates. The paper does not show a table systematically comparing: Shamir 2012/2020/2022b amplitudes and sample sizes vs CE‑ResNet vs this catalog. Without that, the “factor 6–12” statement is somewhat impressionistic.  
- **Required fix:** Add a comparison table summarizing, for each prior study: survey, Nspiral, claimed dipole amplitude and uncertainty/location, with citations to specific tables/figures in those papers. Then justify the “factor 6–12” language directly from those numbers. Alternatively, soften the language to “well below” / “clearly smaller than the few‑percent amplitudes reported by Shamir et al.”

---

### 7. Duplicate phrases and internal placeholders

Your item 9: check duplicate phrases like “canonical canonical-mask”, bookkeeping placeholders, etc.

In the provided text I did not see obvious word‑for‑word duplicates like “canonical canonical‑mask”, but there is **heavy reuse** of “canonical mask”, “canonical‑mask residual”, “canonical unapodized mask”, which is stylistically repetitive but not a direct duplicated phrase.

I did, however, see several internal‑pipeline names and placeholders that are clearly not PRD‑style:

- “artifact c12_r24conf_local_batch.json” and many similar.  
- “c9b”, “ext4_fb1_flip_identity_qc_catalogwide.json”, etc.

**Finding P4‑M7 (MAJOR)**  
- **Location:** Throughout, especially Appendix A–E.  
- **Problem:** These internal artifact IDs are development‑time bookkeeping, not scientific content. They are also opaque to PRD readers and do not conform to reference standards (no DOIs, no stable URLs).  
- **Required fix:** Replace each such internal code with either:  
  - A reference to a public Zenodo/ASCL/DOI artifact (if you will register these), or  
  - A generic statement “detailed logs and intermediate artifacts are available in the companion repository” without enumerating file names.  

---

### 8. Abstract vs body consistency (pattern‑045)

I can’t see the abstract visually separated, but the first long paragraph appears to be the abstract. It includes multiple precise numbers:

- Catalog size 8,474,531 galaxies; Nspiral=3,201,160.  
- “Real‑space chirality dipole consistent with null: … +0.41σ (p=0.31,…), z=0.70 under label‑shuffle null.”  
- “Block‑bootstrap WLS template fit disfavors a clean cosmological dipole at 1.7% reference amplitude at z≈−18.”  
- MASTER residual numbers: +3.64σ, +7.28σ, etc.  
- Falsification criterion: A50≈0.75%, A95 between 1.0–1.5%, harmonic completeness P(≥3σ)≥0.999 at Ap=0.75%.

Spot‑checking against the body:

- The catalog counts and fractions in Sec. IV.A match exactly the abstract numbers.  
- The +0.41σ, p=0.31 real‑space dipole is repeated and elaborated in Sec. IV.C.  
- The block‑bootstrap WLS exclusion at z≈−18 refers to Table IX and Appendix D, which indeed state z≈−18.1 against Aref=0.034 (1.7% in fCW units).  
- The +3.64σ / +7.28σ MASTER stats are consistent with Table III and the text.  
- A50≈0.75% and A95∈(1.0%,1.5%] are consistent with Table V.  
- The MASTER completeness P(≥3σ)≥0.999 at Ap=0.75% is referenced to artifact c9b in the Conclusions; I cannot verify the exact probability value from outside, but it is at least internally consistent.

**Finding P4‑M8 (MAJOR)**  
- **Location:** “Falsification criterion” sentence in abstract vs Sec. VI.A and VII.  
- **Problem:** The abstract compresses several caveats into a single sentence. In the body, the authors are careful to distinguish between:  
  - Real‑space estimator A50/A95 thresholds;  
  - Harmonic‑channel completeness;  
  - Axis‑averaged vs fixed‑axis definitions.  
  The abstract risks overstating how directly a future ≥5σ detection at A≳A95 would be “in tension” with the present null; that depends strongly on estimator choice and survey footprint.  
- **Required fix:** Add one qualifying clause in the abstract, mirroring the body:  
  - e.g. “…would be in tension with the present null **for an estimator and footprint closely matched to those used here**.”  
  This keeps abstract strength aligned with the more nuanced body.

---

### 9. Sigma comparisons from different nulls (your item 7)

The manuscript **does** repeatedly remind readers that σ values from different nulls are not directly comparable (e.g., Sec. III.A, Table I caption, multiple places). That satisfies your explicit requirement to flag any juxtaposition where that caveat is missing.

I did not find a place where, say, “+0.41σ” and “+7.28σ” are directly compared without repeating that they use different null procedures and are “not directly comparable.”

No ESSENTIAL flag on this point.

---

### 10. Data‑availability and provenance DOIs (patterns 046/047)

The Data Availability section points to:

- A HuggingFace dataset (bamfai/galaxy‑chirality‑catalog).  
- A GitHub repo (Hubify‑Projects/bigbounce).  
- A HuggingFace model card (bamfai/galaxy‑chirality‑v2).  
- A promised Zenodo DOI not yet minted.

**Finding P4‑M9 (MAJOR)**  
- **Location:** Data Availability section.  
- **Problem:** For PRD, permanent archival and versioning is important. You state “A persistent archival DOI has not yet been minted; until it is, the versioned release tag above is the citable artifact.” That is not acceptable at publication time; the DOI must exist. Also, HuggingFace and GitHub tags can be overwritten; PRD will want fixed archives.  
- **Required fix:** Before acceptance:  
  - Upload the catalog and code to a long‑term archive (Zenodo or similar) and include the DOIs.  
  - Replace all git commit hashes and tag names with a statement like “This paper uses release v2026.04 (Zenodo DOI X.Y/Z).”  
  - Ensure that the version stated in the Data Availability section corresponds exactly to the artifacts used for the analysis.

---

### 11. “In preparation”, future‑dated IDs, and fake references

I scanned the provided references for:

- “in preparation”, “submitted”, “to appear” – none present.  
- Future‑dated arXiv IDs – none.  
- DOIs that don’t match ADS – the DOIs printed for PASJ, MNRAS, ApJ look correct in spot checks.[6][8]  

No ESSENTIAL issues here.

---

### 12. Length vs contribution (your item 6)

From the text you provided, the manuscript is dense: multiple appendices, extensive pipeline‑log detail, and many internal artifact references. For PRD’s standards:

**Finding P4‑M10 (MAJOR)**  
- **Location:** Whole manuscript, especially Appendices A–E and long explanatory paragraphs in the main text.  
- **Problem:** The core scientific contribution is: construction of a very large chirality‑labeled catalog, demonstration of a null real‑space dipole at sub‑percent sensitivity, and a detailed analysis of monopole‑mask leakage. This is substantial, but the paper, as presented, reads more like a *methods and audit notebook* than a journal article, with many pages devoted to internal code‑paths.  
- **Required fix:** Substantially tighten the narrative for PRD:  
  - Keep one main Methods section, one Results section, and *one* Systematics Appendix with the most important tests.  
  - Move detailed pipeline logs and file‑paths to an online supplement.  
  - Aim for ≈15 PRD pages for the main paper; appendices can be extra but should be trimmed to what’s essential for scientific understanding.

---

## Summary recommendation

**MAJOR REVISIONS**

The core analysis appears careful and, as far as I can see from the text, numerically consistent internally; the paper’s main scientific claims (null dipole, quantified monopole‑mask leakage, sub‑percent sensitivity) are plausible and in line with the cited cosmology literature. However, there are **two clear bibliographic errors** (incorrect arXiv IDs for Shamir 2012 and 2020) that must be fixed, and several key comparative claims about Shamir and CE‑ResNet require more precise linkage to the original tables/figures. Beyond citation issues, the manuscript is overloaded with internal pipeline bookkeeping and version‑history language that is not appropriate for a PRD article; the data‑availability section also lacks a final DOI. I recommend acceptance only after correcting the Shamir arXiv IDs, tightening and documenting all cross‑study quantitative comparisons, cleaning out internal artifact path names/version codes from the main text, and archiving the data/code with stable DOIs.

---

## PASS 2 — self-critique findings (what initial review missed)

P4‑M7 (MAJOR)  
- **Location:** Multiple places where the “factor of ∼6–12” tension with Shamir’s claimed ∼3% signal is asserted (Introduction, Discussion VI.B, Conclusions VII.e).  
- **Problem:** The manuscript repeatedly states that Shamir’s ∼3% amplitude is excluded “by a factor of ∼6–12” without ever showing the explicit numerical mapping from the observed estimator‑space limits (e.g., A50 ≈ 0.75%, A95 ∈ (1.0%, 1.5%]) to that factor range, nor a table of Shamir’s quoted amplitudes and uncertainties to which the comparison is being made. The only quantitative support is a rough “true‑underlying threshold ∼1.88%” from the GZ1 dilution factor; that does not yield a clear 6–12× comparison to 3%.  
- **Required fix:** Add an explicit comparison table listing: (i) this work’s estimator‑space A50 and A95, and the mapped “true” amplitude after de‑dilution; (ii) Shamir’s reported best‑fit amplitudes and uncertainties (with specific table/figure references). Show the actual numeric ratios that justify the “6–12” range or replace that phrase with a softer, traceable statement (e.g., “well below Shamir’s few‑percent claims”) tied to the table.

P4‑M8 (MAJOR)  
- **Location:** Abstract and Sec. IV C (raw sample injection floor vs. “systematics attribution” for the 0.57% unthresholded dipole).  
- **Problem:** The text argues that the 0.57% unthresholded dipole amplitude is “between the full-sample A50 ≈ 0.36% and A95 ≈ 0.63%” and therefore consistent with its z ≈ 4.2–4.4 visibility and systematic attribution. However:  
  - The *HC‑broad* injection floor A50 ≈ 0.75% is used for the main falsification criterion, while here the *full‑sample* injection floor (A50 ≈ 0.36%, A95 ≈ 0.63%) is invoked to classify the unthresholded 0.57% signal as “sub‑floor” and non‑cosmological.  
  - The manuscript never clearly quantifies the σ associated *for that specific estimator* at A = 0.57% under the full‑sample injection curves.  
  This mix of thresholds from two different estimators (HC vs full) makes the “sub‑floor, systematic” classification less transparent than claimed.  
- **Required fix:** Separate clearly the two estimators: give a dedicated injection–recovery curve for the *full‑sample* estimator and state the corresponding P(σ > 3) at A = 0.57%. Then justify the systematic attribution using that curve alone, without referring to HC‑broad thresholds; or else explicitly say that the unthresholded result is *not* used for cosmological inference and avoid tying it to “floor” language.

P4‑M9 (MAJOR)  
- **Location:** Abstract (“falsification criterion: a future ≥ 5σ detection at amplitude A ≳ A95, where A95 between 1.0% and 1.5%… would be in tension with the present null”) and Discussion VII.e.  
- **Problem:** The falsification boundary is defined in terms of A95 inferred from an injection grid with only three high‑amplitude points (1.0%, 1.5%, 2.0%) and modest NMC,inj = 100, and the text concedes that A95 is “bracketed, not measured.” Yet the abstract presents “A95 between 1.0% and 1.5%” as a crisp falsification criterion with ≥5σ detections, without propagating the substantial binomial error on P(σ>3) at each injected A or the grid coarseness. This can overstate the precision of the falsification threshold.  
- **Required fix:** In the abstract and conclusions, soften the falsification statement to make clear that A95 is an interval, not a sharply measured value, and quantify the uncertainty induced by the finite NMC,inj and coarse amplitude grid. For example: “A falsification scale of order 1–1.5% (axis‑averaged), based on our current injection grid,” rather than a sharp A95.

P4‑M10 (MAJOR)  
- **Location:** Sec. VI.A (“g = 2a − 1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ∼1.88%”) and associated discussion of dilution.  
- **Problem:** The mapping from the observed estimator‑space sensitivity (A50 ≈ 0.75%) to a “true underlying” ∼1.88% amplitude via g = 2a − 1 assumes a simplified symmetric misclassification model and ignores:  
  - Asymmetric per‑class accuracies (67.4% vs 72.4%),  
  - Triaging into the not‑spiral class (∼19% of GZ1 spirals removed),  
  - Possible dependence of classification error on sky position or magnitude.  
  The text acknowledges these complications but still presents 1.88% as a single number that is subsequently invoked in qualitative exclusion statements. This gives a false impression of precision.  
- **Required fix:** Either (i) present a *range* for the de‑diluted amplitude (e.g. 1.7–2.1%) based on bounding models that include class‑asymmetry and not‑spiral triage, or (ii) explicitly label 1.88% as an order‑of‑magnitude heuristic and avoid using it in any quantitative tension or exclusion statements.

P4‑m11 (MINOR)  
- **Location:** Sec. IV.B, paragraph describing slab statistics.  
- **Problem:** The text states that in seven equal‑spiral‑count declination slabs (N = 457,308–457,309), the per‑slab fCW spans 0.49537–0.49890 and that “deviations from 0.5 of −0.110% to −0.463%” are “all within 0.5% of 50/50.” The arithmetic is internally consistent, but the phrase “within 0.5%” could be misread as within 0.005 in absolute fraction units rather than 0.005 of 0.5; i.e. the text mixes “percent” and “fraction” in a way that invites confusion.  
- **Required fix:** Clarify unit language, e.g. “all within 0.5 percentage points of 50%” or specify “|fCW − 0.5| ≤ 0.005.”

P4‑M12 (MAJOR)  
- **Location:** Sec. IV.A and Table II (global fractions, σ, and “Dev.”) and Sec. IV.B (monopole discussion).  
- **Problem:** The paper repeatedly uses binomial σ estimates assuming independent spirals (σ = √[f(1−f)/Nspiral]) to quantify the significance of the global CW fraction and various slab splits. However, there is substantial evidence elsewhere in the paper for spatial correlations (due to survey depth, PSF, and morphology systematics). That means these σ values are optimistic: the *effective* number of independent galaxies is smaller than Nspiral, and quoted significances like “−9.47σ” for the Catalog‑C monopole are overstated relative to a correlation‑aware error model.  
- **Required fix:** Add an explicit statement that the simple binomial σ values ignore spatial correlations and therefore overestimate formal σ for monopole‑type statistics. Where the monopole σ or slab σ is used for any scientific interpretation (e.g. the claim of a “9.5σ monopole”), either (i) recompute using a block‑bootstrap or jackknife over sky regions, or (ii) flag clearly that these are naive, lower‑bound σ estimates used only as rough diagnostics.

P4‑M13 (MAJOR)  
- **Location:** Sec. III.A (significance conventions), Table I, Sec. IV.C, Sec. IV.D, Appendix A/C/D.  
- **Problem:** Many σ values are juxtaposed (e.g. +0.41σ real‑space vs +7.28σ harmonic, vs +3.64σ canonical MASTER, vs +7.93σ canonical bandpower, vs +4.84σ monopole‑null residual) and the text correctly *says* they are “not directly comparable.” However, in several places they are implicitly compared rhetorically (e.g. “gap is not a 17× discrepancy… but … a real Shamir‑class dipole would yield z ≈ 68–218 there, versus the observed +7.28σ”), without giving the reader a clean summary of which σ are based on:  
  - label‑shuffle nulls vs monopole‑only generative nulls,  
  - per‑pixel permutations vs axis‑max statistics,  
  - monopole‑subtracted vs non‑subtracted fields.  
  This makes it easy for a reader to misinterpret cross‑channel σ gaps as direct tensions.  
- **Required fix:** Add a compact table or paragraph explicitly listing each major σ quoted in the abstract and conclusions, with its null definition and field (monopole‑subtracted or not). When rhetorically contrasting σ from different nulls (e.g., real‑space vs MASTER), always restate the nulls and emphasize that “Xσ in channel A does not correspond directly to Yσ in channel B.” This will prevent inadvertent cross‑comparison by readers.

P4‑M14 (MAJOR)  
- **Location:** Appendix B, bias‑hardening tests (T1–T8), especially T5 “metadata leakage.”  
- **Problem:** T5 uses simple Pearson r with RA/Dec to diagnose metadata leakage and insists on |r|<0.10, but the text itself admits that RA is a circular variable and that this test can miss azimuthal coupling. The manuscript then leans on the eight‑test suite as evidence for “bias hardening,” yet only one genuinely directional test (the low‑ℓ Yℓm regression) is described, and that result is not summarized in the main text. This may overstate how thoroughly directional systematics have been ruled out.  
- **Required fix:** In the main text Methods/Data‑quality section, explicitly downgrade T5 to a weak check and elevate the spherical‑harmonic regression and other map‑level tests as the primary evidence against direction‑coupled leakage. Make clear that the eight tests are “necessary but not sufficient,” and that directional coupling is constrained primarily by the harmonic and template‑fit analyses, not by T5.

P4‑M15 (MAJOR)  
- **Location:** Appendices C and D; body text references to “look‑elsewhere corrections” and “family‑wise” p‑values.  
- **Problem:** The paper uses multiple look‑elsewhere strategies:  
  - A direct max‑statistic null for hemisphere scans (10,000 shuffles, 648 directions),  
  - Bonferroni and Benjamini–Hochberg corrections layered on top,  
  - A 15‑cell joint null for imaging‑leg × confidence bins.  
  In some cases, both a direct max‑statistic and Bonferroni/BH are applied to the same family, which the text describes as “deliberately conservative,” but this may be interpreted as double‑counting. Moreover, BH assumes independent or positively dependent tests, which is violated for overlapping hemispheres and spatially coupled cells.  
- **Required fix:** Clarify, for each family of tests, which adjustment is the *operative* look‑elsewhere control (max‑statistic null vs multiplicity corrections) and present only that as the main significance; demote the others to cross‑checks. Also add a one‑sentence caveat that BH/Bonferroni are heuristic in the strongly correlated hemisphere grid, and that the max‑statistic null is the statistically principled control there.

P4‑m16 (MINOR)  
- **Location:** Appendix B, three‑class validation metrics (“93.7% accuracy… an earlier text mis‑attributed this pair to augmentation-on/off evaluations”).  
- **Problem:** The current text still mixes several numbers (93.7% three‑class, 93.2% binary, 94.9% CW class accuracy) without a single, clearly labeled summary of which metric is used where. This is not strictly incorrect, but the reader has to parse a dense paragraph of version‑history commentary to understand the validation performance.  
- **Required fix:** Replace the current discussion with a short, clean table of validation metrics (three‑class accuracy, per‑class precision/recall, binary CW/CCW accuracy) and move version‑history notes to a footnote or the repository README.

P4‑M17 (MAJOR)  
- **Location:** Abstract sentence: “Harmonic-channel completeness (P(≥3σ) ≥ 0.999 at Ap = 0.75%) is a separate diagnostic property of the MASTER ℓ = 1 channel…” and Conclusions VII.a.  
- **Problem:** “P(≥3σ) ≥ 0.999 at Ap = 0.75%” is a very strong completeness claim, but the abstract does not specify:  
  - The axis protocol (fixed vs random),  
  - The null used (label‑shuffle),  
  - The number of injections and shuffles at that amplitude.  
  Later sections reveal NMC,inj = 10^3 per amplitude per axis in one context, but this is not easily reconstructible from the abstract, nor is any uncertainty on that completeness stated (finite‑MC error is ∼10^−3).  
- **Required fix:** In the abstract, qualify this as “in our injection tests with NMC,inj = … and label‑shuffle nulls we find P(≥3σ) ≳ 0.999 at Ap = 0.75%, with Monte‑Carlo uncertainty O(10^−3).” That keeps the statement accurate and transparent about its statistical basis.

P4‑m18 (MINOR)  
- **Location:** Multiple places where percentages are converted to “asymmetry‑A units” (e.g., “+0.788% to −0.265% in fCW-deviation units, i.e. +1.576% → −0.529% in A”).  
- **Problem:** The relationship A = 2(fCW − 1/2) is correct, but the narrative sometimes switches between “percent” of fCW and “percent” of A without explicitly reminding the reader that A is *twice* the fCW deviation. For a non‑specialist reader it is easy to confuse 0.75% in A with 0.75% in fCW.  
- **Required fix:** Wherever an A value in percent is mentioned alongside an fCW value, add a parenthetical reminder, e.g. “A = 0.75% (corresponding to a 0.375 percentage‑point deviation in fCW).” This is a clarity upgrade rather than a numerical error.

P4‑M19 (MAJOR)  
- **Location:** Abstract and Conclusions VII.d (“demonstrates that survey systematics can masquerade as highly significant cosmological signals… we urge all future chirality studies to adopt comparable bias controls”).  
- **Problem:** The claim of “demonstration” rests primarily on the raw vs equivariant comparison in this *single* survey and classifier. While the internal evidence is strong, presenting this as a general methodological mandate (“must adopt equivariant post‑processing”) is a broader claim than the analysis strictly warrants, especially since no head‑to‑head comparison with alternative de‑biasing strategies (e.g., explicit PSF/depth templates in the likelihood) is given.  
- **Required fix:** Soften the wording to something like: “Our results *illustrate* that, in this DESI + ViT‑Small setting, classifier and survey systematics can masquerade as cosmological signals, and that equivariant post‑processing is an effective mitigation. Future chirality studies will need similarly rigorous bias controls (which may include equivariant methods) to avoid such artifacts.”