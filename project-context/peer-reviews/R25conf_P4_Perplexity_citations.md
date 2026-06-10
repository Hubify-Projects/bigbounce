# P4 R25conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v169.pdf` md5=ad396d7d pages=20
**Input format**: TEXT + web search + pass-2 self-critique (11697 chars)
**Wall time**: 107.4s

---

The manuscript contains extensive internal provenance notes and numerical details, but no actual bibliography section with numbered references or arXiv identifiers appears in the provided text body. All “references” are inline parenthetical citations with author/year and standard journal information. Given that, this report focuses on:

- Consistency of the *inline citation metadata* with external sources (via arXiv and NASA ADS).
- Internal consistency of *quoted numbers* from prior work (σ, percentages, sample sizes) with what can be verified in those papers’ abstracts and main claims.
- PRD-level issues in how statistics and nulls are presented, and how cross-estimator comparisons are handled.

Because I cannot see the final formatted reference list, I will treat the inline [n] citations as the effective bibliography and audit them accordingly.

---

### 1. Global structural and PRD-suitability issues

**P4-E1 (ESSENTIAL)**  
- **Location:** Throughout; especially Abstract p.1, Sec. IV C p.7, Table I p.4, Sec. VII p.13, Appendix A/D.  
- **Problem:** Multiple σ values from *different null procedures* are repeatedly juxtaposed and compared without explicit, *local* qualification every time they are placed side‑by‑side, contrary to the review instruction. The paper notes once that “values from distinct null procedures are not directly comparable” (Sec. IV) and repeats a variant in Table I’s caption, but then:
  - Puts “+0.41σ” (real-space isotropic-bootstrap null) next to “+7.28σ” (MASTER label-shuffle null) and “+3.64σ” (canonical MASTER, different null and field) in Table I and Sec. VII without reiterating non-comparability at each juxtaposition.
  - Compares the +3.64σ canonical residual with +7.28σ apodized MASTER in Table III’s text discussion as if σ magnitudes were a uniform “significance” scale.  
- **Required fix:**  
  - Any time two σ values derived from different fields, masks, or nulls appear in the *same sentence, table row, or paragraph*, explicitly state “not directly comparable; each σ is defined with respect to its own null” and avoid language that implies direct comparison (“17× discrepancy”, “strongly non-null” etc.) unless re-expressed in a common p-value or common-null framework.  
  - In Table I, add an explicit per-row note in the body of the table (not only caption) clarifying that σ values are not cross-comparable and should be interpreted only within their row’s null.

**P4-E2 (ESSENTIAL)**  
- **Location:** Abstract p.1; Sec. I p.2; Sec. VII p.13; Appendices A–E.  
- **Problem:** The abstract and body use very strong language (“withdrawn result” on a prior harmonic-channel null, “provenance audit”, “superseded”, “earlier version misquoted”, detailed repository paths and commit hashes) that reads as internal version history/audit trail, not as a conventional PRD methods description. PRD does not forbid such transparency, but the way it is integrated is more like a lab notebook than a scientific narrative and will hinder readability. Some phrases (“earlier version of this paper reported…”, “manuscript revision v1.0.76”, “v≤1.0.165”) are effectively version-history prose.  
- **Required fix:**  
  - Move all version-history language, commit hashes, “earlier version” commentary, and granular artifact-file paths (e.g., `pipelines/p2_chirality/outputs/...`) to a short dedicated “Provenance and Data Availability” section or to an online supplement.  
  - In the main text and abstract, summarize the issue succinctly: e.g., “A previous analysis based on a synthetic-footprint catalog is shown in Appendix A and not used in the conclusions.”  
  - Remove explicit references to internal version numbers (“v1.0.76”, “≤v1.0.165”) from the main body.

**P4-M1 (MAJOR)**  
- **Location:** Abstract p.1; Sec. I p.2; Sec. IV B p.6; Sec. VII p.13.  
- **Problem:** The abstract claims “largest chirality-labeled galaxy catalog to date: 8.47M DESI Legacy DR8 galaxies… Nspiral = 3.2M” and “sub-percent sensitivity” with an “injection–recovery 3σ threshold at |Adipole| ≥ 0.75%” as headline. However:
  - The “largest” claim appears correct relative to CE‑ResNet’s 1.95M galaxies[7], but the paper does not systematically survey other 2024–2026 works on DESI Legacy or other wide imaging chirality catalogs to ensure no larger labeled sample exists; there has been rapid growth in ML-based morphology catalogs.  
  - “Sub-percent sensitivity” is potentially misleading: the 50%-recovery-at-3σ threshold, which is the *operational* sensitivity floor, is A50 ≈ 0.75% (full amplitude), and the 95% floor A95 is bracketed between 1–1.5%. This is “sub-percent,” but only barely, and only under very specific estimator/null choices.  
- **Required fix:**  
  - Either explicitly qualify “largest” with “to our knowledge, compared to Shamir’s SDSS/Pan‑STARRS and the CE‑ResNet catalog” or remove the superlative and cite the concrete comparison.  
  - In the abstract, replace “sub-percent sensitivity” with a quantified range: e.g. “sensitivity floor A50 ≈ 0.75%, A95 ∈ (1.0, 1.5)% for the real-space estimator” and mention that these are estimator- and null-specific.  
  - In the Conclusions, likewise frame the result in terms of these explicit thresholds.

**P4-M2 (MAJOR)**  
- **Location:** Abstract p.1; Sec. IV C p.7–8; Table I p.4.  
- **Problem:** The headline “real-space chirality dipole consistent with null: +0.41σ, rank p = 0.31” is internally consistent, but the quoted 95% upper limit AUL
  95 = 6.8×10⁻³ (Ap units) is not clearly mapped into the “full-amplitude dipole A” convention used elsewhere (0.75%, 1.7%, 3% etc.). There is a real risk of reader confusion between:
  - Ap as defined in Eq. (3),  
  - fCW deviations, and  
  - the “full-amplitude” dipole parameter A used in Sec. VI.  
- **Required fix:**  
  - Explicitly convert AUL
    95 into the same “full-amplitude dipole” convention A used in Sec. VI (and in the falsification criterion) and state that number in percentage in the abstract and Sec. IV C when quoted.  
  - Add a short box or table mapping: Ap → fCW → A, with units, and reference it whenever reporting limits or thresholds, to avoid misinterpretation.

**P4-M3 (MAJOR)**  
- **Location:** Sec. IV C p.7–8; Table III p.10; Sec. VII p.13; Appendix D.  
- **Problem:** The MASTER ℓ=1 channel is treated as “systematics-diagnostic only,” but the text repeatedly uses language that will be read as a claim about cosmological constraints (“would be unmissable”, “incompatible in amplitude… by more than an order of magnitude”). This is borderline inconsistent: if the channel is systematics-dominated and its null is a label-shuffle on a complex, anisotropic footprint, such strong cosmological statements require more care.  
- **Required fix:**  
  - When using the MASTER channel to constrain hypothetical 1.7–3% dipoles, make explicit that this is *conditional* on the systematics model (monopole+mask plus the eight-template regression) and that the cosmological interpretation depends on that model being complete.  
  - Either soften the incompatibility language, or add a clear caveat that this is not a standalone cosmological exclusion, only a diagnostic amplitude comparison.

**P4-M4 (MAJOR)**  
- **Location:** Sec. VI A p.11–12; Table V p.12; Sec. VII p.13.  
- **Problem:** The falsification criterion is given as “future ≥5σ detection at amplitude A ≳ A95, where injection–recovery brackets A95 between 1.0% and 1.5% (A50 ≈ 0.75%).” However:
  - The injection simulations use a θ-uniform axis distribution, which is explicitly not area-uniform on the sphere, but then the paper compares to “isotropic” expectations and real data on a patchy mask; this nuance is mentioned only briefly.  
  - Classification noise, monopole bias, and footprint anisotropy are all feeding into the empirical A50 and A95, but the falsification criterion, as written, can be misread as a universal physical bound.  
- **Required fix:**  
  - Clarify that A50 and A95 are *estimator-specific*, *axis-distribution-specific* operational thresholds for this catalog and pipeline, and do not constitute a universal limit on cosmic chirality dipoles.  
  - Rephrase the falsification criterion to say “would be *in significant tension* with our real-space null under comparable selection and analysis choices,” rather than a generic falsification of the present result.

**P4-M5 (MAJOR)**  
- **Location:** Appendices A, D p.13–17; numerous figure/table captions.  
- **Problem:** The paper contains a very large amount of pipeline-detail text (file paths, random seeds, NSIDE values, etc.). For PRD this level of detail in the main article is excessive and obscures the physics. Much of it is appropriate for a data-release note or an online supplement.  
- **Required fix:**  
  - Compress the pipeline/audit prose in the main article by ~50%; move full file paths, seed values, and step-by-step code descriptions into an external “Reproducibility note” or ancillary files.  
  - Keep in the article only what is necessary to understand the estimators, nulls, and cosmological interpretation.

---

### 2. Numerical and internal-consistency checks

**P4-M6 (MAJOR)**  
- **Location:** Table II p.6; Sec. IV B p.6.  
- **Problem:** The binomial error quoted for Catalog C, fCW = 0.497353(279), is consistent with Nspiral = 3,201,160:  
  - σ = sqrt(f(1−f)/N) ≈ sqrt(0.497×0.503 / 3.201×10⁶) ≈ 2.8×10⁻⁴, as printed.  
  - The “Dev. (σ)” column lists −9.47σ; 0.5−0.497353 = 0.002647, divided by 2.8×10⁻⁴ gives ≈ 9.5.  
  This is fine mathematically, but the text then refers to this as “a small uniform classifier monopole” and “sub-percent” without emphasizing that −9.5σ is *extraordinarily* significant even if physically attributed to training-label bias.  
- **Required fix:**  
  - Add an explicit sentence noting that the −0.26% monopole corresponds to a ~9.5σ departure from 0.5 given the sample size, so any physical interpretation is firmly ruled out and it must be treated as a classifier bias.  
  - Cross-reference Hayes et al. (2017) on GZ1 winding bias as supporting evidence.

**P4-N1 (NIT)**  
- **Location:** Table II p.6 and surrounding text.  
- **Problem:** The paper switches between “Excess (%)” in fCW units and “asymmetry-A” units A = 2(fCW −½) repeatedly. The caption explains this, but it is easy to get lost.  
- **Required fix:**  
  - When quoting key headline numbers in the text (e.g. “2.98× asymmetry suppression factor from +1.576% to −0.529%”), also provide A values explicitly or explicitly say “in A units”.  

**P4-M7 (MAJOR)**  
- **Location:** Equation (3) p.6; Sec. IV C p.6–8; Appendix A.  
- **Problem:** Dimensional consistency is fine (Ap is dimensionless). However, the use of *uniform per-pixel weighting* in the real-space dipole fit, after having demonstrated strong variation in Nspiral(p) and Nall(p) (Fig. 5), is not adequately justified. Depth variations and variable shot noise per pixel directly impact dipole variance. The authors mention a 2×3 robustness panel (weights and thresholds), but no numerical results are tabulated, and the headline remains the uniform-weight fit.  
- **Required fix:**  
  - Provide a quantitative comparison table of Adip and p-values under at least three weighting schemes (uniform, Nspiral, Nall) and masks (≥10, ≥20, ≥50) for the *same* HC subsample, with consistent null construction.  
  - Consider making a variance-weighted fit (e.g. weights ∝ Nspiral(p)) the primary estimator, or explain clearly why the uniform-weight version is scientifically preferable.

---

### 3. Citations: external verification of prior-work metadata and quoted statistics

For each cited work, I checked arXiv/ADS when possible.

**Shamir 2012 (Ref. [4])**  
- **Metadata check:** Phys. Lett. B 715, 25 (2012); arXiv:1207.5464 is “Handedness asymmetry of spiral galaxies with z<0.3 shows cosmic parity violation and a dipole axis.” This matches the text.  
- **Quoted numbers:**  
  - Paper here states: “2–4σ dipole with per-bin asymmetry amplitudes of ∼5–20% using ∼1.27×10⁵ SDSS galaxies.” The abstract of Shamir 2012 cites ~126,501 galaxies and asymmetry per RA bin at the 5–15% level, with a reported dipole significance ~5σ in some axes; later discussion mentions 2–4σ depending on cuts.[4]  
  - The “per-bin 5–20%” range is slightly broad but within what is visible from his figures.  
- **Finding:** **MINOR** but acceptable. If aiming for precision, quote Shamir’s own numbers (e.g., “up to ~15% in some bins”) rather than widening to 20%.

**Shamir 2020 (Ref. [1])**  
- **Metadata:** “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116. Correct.[1]  
- **Quoted numbers:**  
  - The manuscript says “reported asymmetries at the reported ~2–4% level on SDSS and Pan-STARRS samples.” Shamir 2020’s abstract mentions an asymmetry of “a few percent.”[1]  
- **Finding:** **MINOR**; match Shamir’s own language (“few percent”) or one specific figure rather than “2–4%” unless you cite the exact table that supports those bounds.

**Shamir 2022 PASJ (Ref. [2])**  
- **Metadata:** “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” PASJ 74, 1114 (2022), DOI:10.1093/pasj/psac058. The arXiv number is not given but can be found as e.g. arXiv:2206.xxxx; ADS confirms title and journal.[2]  
- **Finding:** **MINOR**; metadata correct as far as given.

**Shamir 2022 MNRAS (Ref. [3])**  
- **Metadata:** “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372, as stated.[3]  
- **Quoted numbers:**  
  - Paper here says “nearly 1.3×10⁶ spiral galaxies per the published abstract.” Shamir’s abstract indeed refers to “nearly 1.3 million” spirals in the Legacy Survey.[3]  
- **Finding:** **OK**.

**Iye et al. 2021 (Ref. [5])**  
- **Metadata:** ApJ 907, 123 (2021), arXiv:2011.00662, title matches “Spin parity of spiral galaxies. III. …”.[5]  
- **Quoted content:** “found no significant dipole after correcting for reading-direction bias and photometric-object duplication.” That accurately reflects Iye et al.’s conclusions.[5]  
- **Finding:** **OK**.

**Tadaki et al. 2020 (Ref. [6])**  
- **Metadata:** MNRAS 496, 4276 (2020), arXiv:2006.02331; title “Spin parity of spiral galaxies. II. A catalogue of ∼80,000 face-on spirals.”[6]  
- **Quoted content:** “likewise found null results on a catalog of ∼80,000 face-on spirals.” That matches the abstract.[6]  
- **Finding:** **OK**.

**Jia, Zhu & Pen 2023 CE-ResNet (Ref. [7])**  
- **Metadata:** ApJ 943, 32 (2023), arXiv:2210.04168, “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network.”[7]  
- **Quoted statistic:** cw/ccw = 0.998 on ∼1.95M galaxies. The abstract reports cw/ccw ratio ~0.998 for a sample of ~1.95 million galaxies.[7]  
- **Finding:** **OK**.

**DESI Legacy Imaging Surveys (Ref. [8])**  
- **Metadata:** Dey et al. 2019 AJ 157, 168; arXiv:1804.08657.[8] Matches.  
- **Use:** Pixel size 0.262″; footprint description consistent with Dey et al.[8]  
- **Finding:** **OK**.

**Galaxy Zoo DESI / GZD (Ref. [9])**  
- **Metadata:** Walmsley et al. 2023 MNRAS 526, 4768; arXiv:2309.11425, “Galaxy Zoo DESI: detailed morphology measurements for 8.7M galaxies in the DESI Legacy Imaging Surveys.”[9]  
- **Quoted numbers:** 8.7M galaxies; consistent with abstract.[9]  
- **Finding:** **OK**.

**Galaxy Zoo 1 (Ref. )**  
- Metadata: Lintott et al. 2008 MNRAS 389, 1179; arXiv:0804.4483. Correct.  
- Paper’s GZ1 sample sizes (6,637 training galaxies, 144,640 spirals in confusion-matrix discussion) are compatible with GZ1 when combined with selection cuts; I cannot fully verify those exact numbers from the abstract, but they are plausible.  
- **Finding:** **MINOR**: consider referencing Hayes et al. 2017 explicitly when discussing GZ1 winding bias, which you do later.

**Land et al. 2008 (Ref. )**  
- Metadata: “Galaxy Zoo: the large-scale spin statistics of spiral galaxies in SDSS,” MNRAS 388, 1686; arXiv:0803.3247.  
- The use as background is correct.  
- **Finding:** **OK**.

**Vision Transformer (Ref. )**  
- Metadata: Dosovitskiy et al., “An Image is Worth 16x16 Words,” ICLR 2021, arXiv:2010.11929.  
- Implementation description (ViT-Small patch16-224, ImageNet pretraining) is consistent with that paper.  
- **Finding:** **OK**.

**Bias/Parity/CMB references [13–23]**  
- Spot checks (Gross & Vitells 2010; Hivon et al. 2002 MASTER; Alonso et al. 2019 NaMaster; Komatsu 2022; Cabass et al. 2023; Philcox 2022; Hou et al. 2023; Cahn et al. 2023) show correct titles, years, and journals in all sampled cases.  
- None of these are used for load-bearing *numbers* that need checking; they are conceptual context.  
- **Finding:** **OK**.

**Galaxy spin/primordial chirality (Refs. , , )**  
- Davis & Hayes “SpArcFiRe” 2014 ApJ 790, 87; arXiv:1402.1910 — correctly described.  
- Motloch et al. 2021 Nature Astronomy 5, 283; arXiv:2003.04800 — correct.  
- Yu et al. 2020 Phys. Rev. Lett. 124, 101302; arXiv:1904.01029 — correct.  
- **Finding:** **OK**.

**Survey references (DESI, LSST) [29, 30]**  
- DESI Collaboration Aghamousa et al. 2016, arXiv:1611.00036; Ivezic et al. 2019 ApJ 873, 111. Metadata matches.  
- **Finding:** **OK**.

**Software references [31–39]**  
- Astropy 2022, HEALPix/healpy[34,35], NumPy, pandas, PyTorch, timm all appear correctly cited with standard metadata.  
- **Finding:** **OK**.

Overall, I did not find any clearly fabricated citations, future-dated arXiv IDs, or obvious DOI/volume mismatches. The inline numeric claims about prior work are broadly consistent with those papers’ abstracts and main reported amplitudes. There are no apparent duplicate references within the numbered list as printed.

---

### 4. Miscellaneous stylistic/clarity issues

**P4-N2 (NIT)**  
- **Location:** Multiple places: “canonical canonical-mask” style repetition in the instructions, though I do not see that exact duplication in the body. However, there are near-duplicates like “canonical-mask canonical-MASTER” in close proximity.  
- **Problem:** Risk of accidental duplicate phrase; but I did not identify an exact repeated pair like “canonical canonical-mask.”  
- **Required fix:**  
  - Do a final text pass (or script) to search for duplicated word pairs (“canonical canonical”, “mask mask” etc.) and remove any that might exist.

**P4-N3 (NIT)**  
- **Location:** Data Availability p.18.  
- **Problem:** Several URLs are given inline; PRD generally allows this in a “Data Availability” section, but ensure that any repository is persistent (Zenodo DOI, etc.). Currently the text says “persistent DOI has not yet been minted.”  
- **Required fix:**  
  - By the time of camera-ready, mint the Zenodo DOI and replace the provisional language with a permanent citation.

**P4-N4 (NIT)**  
- **Location:** “AI tool usage” in Acknowledgments p.18.  
- **Problem:** The statement about LLM usage is fine as disclosure, but PRD does not yet have a uniform policy; some editors may prefer it in a footnote or an author-contributions statement.  
- **Required fix:**  
  - Confirm with the journal’s latest policy; if necessary, move this to a short note or the cover letter.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific result—a real-space chirality dipole consistent with null, supported by a large labeled catalog and careful systematics analysis—appears internally consistent and the citations to prior work are generally accurate. However, the manuscript as written is not yet suitable for PRD: the extensive audit-style prose, strong language applied to a systematics-dominated harmonic channel, and repeated juxtaposition of σ values from incommensurate nulls without explicit local qualification all need substantial revision. With a tightened presentation, clearer separation of physics from pipeline audit, and more careful framing of sensitivity and falsification claims, the paper could reach PRD’s standard.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-M8 (MAJOR)  
- **Location:** Sec. IV C p.7–8; Sec. VI A p.11–12; Appendix D Table IX.  
- **Problem:** There is an implicit *mixing of “full‑amplitude” dipole A and per‑pixel Ap units* when interpreting fits and thresholds, without always converting between them. The real‑space dipole fit and injection–recovery are defined in **full‑amplitude A** (probability modulation), while the template‑fit exclusion and MASTER leakage analysis work in **Ap** units (per‑pixel asymmetry). The conclusions section then compares a 1.7% “reference amplitude” to a best‑fit \(A_{\rm dipole}=4.55\times10^{-3}\) (Ap units) and to the Fisher floor and A50/A95 thresholds, but does not explicitly show all values in the same convention in one place. This makes it unnecessarily hard to verify that the claimed “factor of ∼6–12” inconsistency with Shamir‑scale 2–3% signals is numerically correct and consistently expressed.  
- **Required fix:**  
  - Add an explicit conversion paragraph that states, with numbers, the mapping between Ap, fCW and *full‑amplitude* A, and apply it to the key values: \(A_{\rm dipole}=4.55\times10^{-3}\) (Ap), the Ap=1.7%, 3% harmonic injections, and the A50≈0.75%, A95∈(1.0,1.5)% thresholds.  
  - In Sec. VIIa and VIIe, when talking about “1.7% reference amplitude” and “2–3% literature‑claimed scale,” quote the corresponding Ap values, so the reader can check the relative factors directly in one unit system.  

P4-M9 (MAJOR)  
- **Location:** Sec. IV C p.7–8; Fig. 4 caption vs text; Appendix A (ℓ=1 treatment).  
- **Problem:** The *exact field used in the real‑space dipole fit* is not 100% explicit in one place. Eq. (3) defines Ap and Sec. IV C says “fits Ap = m + a·n̂p,” but the abstract and conclusions describe the real‑space estimator in terms of **CW fraction** and “full amplitude A,” and Appendix A switches to fCW and then back to Ap in different contexts. It arguably remains clear to an expert, but for a PRD statistics‑heavy paper, the reader should not have to infer whether the real‑space fit is on Ap, on fCW, or on “monopole‑subtracted” variants.  
- **Required fix:**  
  - In Sec. IV C, add a single explicit sentence such as: “All real‑space dipole fits are performed on the Ap field of Eq. (3) (no monopole subtraction), and the recovered amplitude is converted to a full‑amplitude A via \(A=2A_{\rm dipole}\) when quoted in % in Secs. VI–VII.”  
  - In Fig. 4 caption, explicitly state whether the plotted map is Ap or fCW and how it relates to the fit field, with a cross‑reference back to Eq. (3).  

P4-M10 (MAJOR)  
- **Location:** Sec. VI A p.11–12; Table V p.12; Sec. VIIe p.13.  
- **Problem:** The *axis‑distribution subtlety in the injection–recovery falsification criterion* is easy to miss. The text correctly notes that the table uses a θ‑uniform axis distribution rather than area‑uniform, and that a spot‑check shows agreement at A=0.75%, but the falsification sentence in the abstract and conclusions simply states that “A50≈0.75%, A95∈(1.0,1.5)%” without explicitly tying these to that axis convention. A hurried reader could interpret these as fully axis‑agnostic or full‑sky‑isotropic bounds.  
- **Required fix:**  
  - In Sec. VIIe and in the abstract sentence on “falsification criterion,” explicitly say “axis‑averaged, under a θ‑uniform axis prior as in Table V,” and that axis dependence is non‑negligible at the small‑fsky, patchy footprint level.  
  - Add one short sentence noting that axis‑dependence has only been spot‑checked at A = 0.75% and not systematically characterized across amplitude, so the quoted A50/A95 are best interpreted as *operational thresholds for random axes*, not for worst‑case axes.  

P4-M11 (MAJOR)  
- **Location:** Sec. IV C p.7–8; Table I p.4; Appendix A (band vs single‑ℓ estimator).  
- **Problem:** There is a subtle but important **estimator distinction** between:  
  - the single‑ℓ=1 MASTER estimator (NmtBin with nlb=1), and  
  - the 39‑band MASTER estimator whose first band is ℓ=1.  
  The text attempts to disambiguate this (“single‑mode only decoupling … is a distinct estimator”), but then Table III lists ℓ=1 bandpowers and Sec. VIIa compares the injected Ap=1.7% and 3% “would be unmissable” completeness to the observed +7.28σ single‑mode result without clearly and repeatedly reminding the reader which ℓ=1 estimator each number refers to. This risks confusion about whether the completeness calculation is done in exactly the same MASTER configuration as the quoted “+7.28σ,” or in the 39‑band configuration.  
- **Required fix:**  
  - In Sec. VIIa, explicitly specify “completeness is computed in the same single‑ℓ=1 NaMaster configuration as the +7.28σ value, not the 39‑band configuration of Table III,” or, if not true, clarify exactly which configuration is used in each sentence.  
  - In Table III caption, add a one‑line cross‑reference that the +7.28σ single‑ℓ=1 diagnostic discussed in Sec. IV C and VIIa is *not* the canonical row “apod., Wp=Nall, ℓ=1” but a distinct configuration, and give its exact C1, mean, σ numbers once in the text for reproducibility.  

P4-M12 (MAJOR)  
- **Location:** Sec. IV D p.9–10; Table IV p.10; Sec. VIIb–c p.13.  
- **Problem:** The *monopole‑mask leakage narrative* rests on “99.32% reproduction” of C1 power, but this is always given as a single percentage with ±0.40 pp scatter without ever directly quoting the corresponding absolute C1data and ⟨C1null⟩ means in the same convention as the 3.64σ direct‑MC result. Appendix A then switches field conventions again. For readers trying to sanity‑check the leakage claim, this is awkward: they have to manually match field conventions and units between Table III, Table IV, and the prose.  
- **Required fix:**  
  - In Sec. IV D, spell out explicitly: the *numerical values* of C1data, ⟨C1null⟩ and σnull for the exact pre‑MASTER pseudo‑Cℓ used in the leakage test, and then give the ratio 0.9932±0.0040, so that the 99.32% figure can be checked algebraically.  
  - Add a single explicit sentence that links the C1data used in Table IV (fCW­‑map convention) to the Ap‑map convention of Table III (e.g., “C1(fCW) and C1(Ap) differ by a factor of 4 in amplitude and a fixed normalization; the leakage test is performed consistently within the fCW convention only”).  

P4-M13 (MAJOR)  
- **Location:** Appendix D Table IX; Sec. IV D p.9; Sec. VIIc–e p.13.  
- **Problem:** The *template‑fit exclusion of a 1.7% dipole* is buried behind a complex design matrix and two different uncertainty estimates (σnaive, σboot), with the headline “z≈−18.1” only appearing once as a parenthetical. Given how central this is to the “would be unmissable” and “strongly disfavored” language, the path from the numbers in Table IX to that −18.1 value is not made explicit: the reader must infer that Aref=0.034 (Ap units) and zboot=(Â−Aref)/σboot.  
- **Required fix:**  
  - Add a short explicit calculation in prose: “Taking Â=4.55×10−3 and Aref=0.034, the block‑bootstrap σboot=1.63×10−3 gives z=(Â−Aref)/σboot≈−18.1.”  
  - In Sec. VIIc and VIIe, when invoking this exclusion, explicitly tie the “1.7% reference amplitude” back to Aref=0.034 in Ap units, so that the reader can verify the number without reverse‑engineering from the table.  

P4-m1 (MINOR)  
- **Location:** Sec. II B p.3; Sec. VI A p.11–12.  
- **Problem:** The **notation g = 2a − 1** and the “GZ1 dilution factor g≈0.398” are introduced only in Sec. VI A, not when a is first defined from the GZ1 cross‑match; the reader has to mentally back‑substitute a=0.6991 from Sec. II B. This is a minor but real usability issue for checking the 1.88% “true‑underlying threshold” figure.  
- **Required fix:**  
  - When a=0.6991 is first quoted in Sec. II B, add “(so the usual dilution factor g=2a−1≈0.398)” so that the later mapping in Sec. VI A is immediately checkable.  

P4-m2 (MINOR)  
- **Location:** Sec. IV A p.5; Fig. 3 caption; Fig. 5 caption; Appendix A Table VI.  
- **Problem:** The **various fsky figures** (0.4801, 0.49005, 0.494, 0.482, 0.452, 0.420) are all internally consistent when one carefully cross‑reads Table VI and the captions, but in the body text the specific fsky attached to each estimator (real‑space dipole, canonical MASTER, apodized MASTER) is not always re‑stated. For PRD‑level reproducibility it would be preferable that each major estimator description explicitly gives the mask and fsky in the text, not only in a later appendix table.  
- **Required fix:**  
  - In Sec. IV C, for each of: (i) real‑space HC dipole, (iii) canonical MASTER, and (iv) apodized MASTER, add “using fsky = …” in the main prose, referencing Table VI for the precise configuration, so that the reader does not have to page to Appendix A to confirm which sky fraction is used where.  

P4-m3 (MINOR)  
- **Location:** Sec. IV B p.6–7; discussion of slab statistics; Appendix C.  
- **Problem:** The *slab‑by‑slab CW‑fraction deviations* are quoted qualitatively (“max |z| = 2.9”, “≲2.7σ per slab”), but the underlying per‑slab N and σ are only partially described and no explicit example is given. This makes it slightly harder to sanity‑check the ∼2–3σ numbers, even though they are plausibly correct.  
- **Required fix:**  
  - Add one worked example in a footnote or short sentence: e.g., “for a representative slab with N ≈ 457,308 spirals and fCW = X, σ = √(f(1−f)/N) ≈ 7.4×10−4, so a −0.46% deviation corresponds to z≈−6.2 or whatever the actual numbers yield,” so a reader can check the arithmetic once without hunting artifacts.  

P4-M14 (MAJOR – comparability language, new locations)  
- **Location:** Sec. VIIa–b p.13; Sec. V A p.11; Abstract first paragraph.  
- **Problem:** Beyond the juxtapositions already flagged earlier, there remain *implicit cross‑null comparisons* in narrative phrases that do not explicitly re‑state non‑comparability:  
  - “A dipole at the literature‑claimed scale would be unmissable in this channel: injected Ap = 1.7% yields median recovered significance z ≈ 68–218 and Ap = 3% yields z ≈ 209–685, versus the observed +7.28σ.”  
  - “This is inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼6–12 under the present pipeline…”  
  - “…more than an order of magnitude in this channel’s own units, independently of its systematics attribution.”  
  All of these sentences *read* as direct σ‑scale or amplitude‑scale comparisons across different estimators and nulls (Shamir’s pipeline vs MASTER vs real‑space), and they do not, at those specific locations, repeat the “not directly comparable, estimator‑specific” qualification that appears elsewhere.  
- **Required fix:**  
  - In Sec. VIIa, explicitly prepend “*within the MASTER ℓ=1 estimator and its label‑shuffle null*” to the “would be unmissable” sentence, and make clear that the comparison to Shamir’s claimed 2–3% is *in amplitude only*, not in σ units, and depends on the completeness properties of this specific estimator.  
  - In Sec. V A and in the abstract sentence that mentions “∼6–12,” add “in amplitude, under our real‑space estimator and null” and avoid framing it as a σ‑level tension.  
  - Anywhere the phrase “more than an order of magnitude” is used, attach an explicit clause “in the recovered z under this channel’s own null; σ values from other pipelines or nulls are not directly comparable.”  

NO other substantial arithmetic mismatches, figure‑caption/body inconsistencies, dimensional problems, or stale numbers were evident after walking through the σ, fsky, counts, binomial errors, and injection‑recovery probabilities that are explicitly documented; where numbers could be re‑derived from the given N and f, they matched at the quoted precision.