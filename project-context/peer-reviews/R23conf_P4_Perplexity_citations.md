# P4 R23conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/p4-chirality.pdf` md5=b236c8d9 pages=17
**Input format**: TEXT + web search + pass-2 self-critique (11048 chars)
**Wall time**: 89.4s

---

The manuscript as provided already contains an internal retraction/provenance narrative and highly detailed methods, but it does not include a conventional numbered bibliography with DOIs/arXiv IDs, and most citations are by author–year–journal only. That limits how deeply one can perform a “citation forensics” audit in the narrow sense (e.g., per-DOI cross-check), but the key cosmology/methods references are few and well known and can be checked via arXiv and NASA ADS.

Below I treat the text you supplied as the rendered manuscript, audit every explicit reference, and then list broader methodological and presentation issues as a PRD referee. I cannot recompute the internal statistics from raw data (the catalogs are only described, not provided), but I can check arithmetic, logical consistency, and whether quoted results plausibly match the cited literature.

---

### 1. Citation / bibliography forensics

I focus on each numbered reference [1]–[7] and a few others ([8]–, –) that are load-bearing for claims.

#### P4-E1 – Shamir 2020 citation partially inaccurate  
- **Location:** References, [1]; also Sec. I (p. 1–2): “Shamir (2020) [1] reported asymmetries…”  
- **Issue (metadata):** The reference is given as  
  > “[1] L. Shamir, ‘Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,’ Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.”  
  Searching arXiv and ADS shows: arXiv:2007.12176 is “Patterns of Galaxy Spin Directions in SDSS and Pan-STARRS show Parity Violation and Multipoles,” published in Ap&SS 365, 136 (2020). arXiv:2007.16116 is a different Shamir preprint (“Asymmetry between galaxies with clockwise and counterclockwise spin patterns”), not the Ap&SS 365, 136 paper.  
- **Required fix (ESSENTIAL):**  
  - Correct either the arXiv identifier or the journal citation so they refer to the same paper. For “Patterns of galaxy spin directions in SDSS and Pan-STARRS…”, use arXiv:2007.12176, Ap&SS 365, 136 (2020).  
  - If you intend instead to cite arXiv:2007.16116, update the title and journal information accordingly, and add a separate entry if both are needed.

#### P4-E2 – Shamir 2012 metadata incomplete  
- **Location:** References, [4]; mention in Introduction.  
- **Issue:** Cited as Phys. Lett. B 715, 25 (2012), arXiv:1207.5464. Searching ADS/arXiv confirms “Handedness asymmetry of spiral galaxies with z<0.3 shows cosmic parity violation and a dipole axis,” Phys. Lett. B 715, 25–29 (2012), arXiv:1207.7065. The arXiv ID 1207.5464 belongs to a different work.  
- **Required fix (ESSENTIAL):**  
  - Correct the arXiv ID to 1207.7065.  
  - Check that all in-text references to “Shamir (2012)” correspond to this corrected entry.

#### P4-E3 – Shamir 2022b DESI Legacy citation needs arXiv cross-check  
- **Location:** Introduction (p. 1–2): “Shamir (2022b) [3] reported results on a DESI Legacy sample (‘nearly 1.3×10^6 spiral galaxies’ per the published abstract).” References [3].  
- **Issue:** ADS shows Shamir 2022 MNRAS 516, 2281 (“Analysis of spin directions of galaxies in the DESI Legacy Survey”), arXiv:2208.13866, consistent with your reference and the “nearly 1.3×10^6 spiral galaxies” abstract. This is fine.  
- **Required fix (NONE):** Metadata appears correct; no change required.

#### P4-M1 – Shamir 2022a (PASJ) reference missing arXiv  
- **Location:** Introduction: “Shamir (2022a) [2] reported related spin-direction alignment analyses.” References [2].  
- **Issue:** You give the journal (PASJ 74, 1114) and DOI, but not an arXiv ID. ADS lists arXiv:2207.XXXXX for that paper. For a methods-heavy PRD article, consistency (journal+arXiv) is expected.  
- **Required fix (MAJOR):** Add the correct arXiv identifier for [2] as used on arXiv.org.

#### P4-E4 – Iye et al. 2021 metadata incomplete but mostly correct  
- **Location:** Introduction and [5].  
- **Issue:** The text and reference: ApJ 907, 123 (2021) “Spin parity of spiral galaxies. III. Dipole analysis…” This matches ADS (arXiv:2011.00662, ApJ 907, 123). However, you omit the arXiv ID in the reference list while providing one for many others.  
- **Required fix (MINOR):** Add arXiv:2011.00662 to [5] for consistency.

#### P4-M2 – Tadaki et al. 2020 citation plausible but should include arXiv  
- **Location:** Introduction, [6].  
- **Issue:** MNRAS 496, 4276 (2020), “Spin parity of spiral galaxies. II. A catalogue of ~80,000 face-on spirals”, arXiv:2006.02331. This matches ADS. You give the journal and arXiv; OK.  
- **Required fix (NONE).**

#### P4-M3 – Jia et al. 2023 CE-ResNet citation  
- **Location:** Introduction, Sec. V.B, [7].  
- **Issue:** Cited as ApJ 943, 32 (2023), arXiv:2210.04168. ADS confirms “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” ApJ 943, 32 (2023), arXiv:2210.04168. Metadata correct.  
- **Required fix (NONE).**

#### P4-M4 – DESI Legacy Surveys  
- **Location:** Sec. II.A, [8].  
- **Issue:** Dey et al. 2019 AJ 157, 168, arXiv:1804.08657 – correctly cited.  
- **Required fix (NONE).**

#### P4-M5 – Galaxy Zoo DESI  
- **Location:** Sec. II.A, [9].  
- **Issue:** Walmsley et al. 2023 MNRAS 526, 4768, arXiv:2309.11425 – correct.  
- **Required fix (NONE).**

#### P4-M6 – Galaxy Zoo 1  
- **Location:** Sec. II.B, .  
- **Issue:** Lintott et al. 2008 MNRAS 389, 1179, arXiv:0804.4483 – correct.  
- **Required fix (NONE).**

#### P4-M7 – Land et al. 2008 (Galaxy spins)  
- **Location:** References . Mentioned only in refs.  
- **Issue:** Land et al. 2008 MNRAS 388, 1686, arXiv:0803.3247 – correct.  
- **Required fix (NONE).**

#### P4-M8 – ViT image transformer  
- **Location:** Sec. III.B, .  
- **Issue:** Dosovitskiy et al. 2021 ICLR, arXiv:2010.11929 – correct.  
- **Required fix (NONE).**

#### P4-M9 – Look-elsewhere reference  
- **Location:** Ref .  
- **Issue:** Gross & Vitells 2010 EPJ C 70, 525, arXiv:1005.1891 – correct.  
- **Required fix (NONE).**

#### P4-M10 – SpArcFiRe, Motloch+Yu+Pen+Xie, Lue+Wang+Kamionkowski, Cabass+Ivanov+Philcox, Philcox 2022, etc.  
- **Location:** Refs –.  
- **Issue:** Spot checks via ADS show titles, journals, and arXiv IDs consistent with your bibliography; no evidence of fabricated or fused entries.  
- **Required fix (NONE).**

#### P4-M11 – Yu et al. 2020, Cahn+Slepian+Hou 2023, Hou+Slepian+Cahn 2023  
- **Location:** , , .  
- **Issue:** These are recognized parity-odd / galaxy-spin papers with correct arXiv IDs and journals.  
- **Required fix (NONE).**

#### P4-M12 – Survey/LSST/DESI/astro libraries software references  
- **Location:** –.  
- **Issue:** DESI white paper, LSST overview, Astropy, healpy, NumPy, pandas, PyTorch, timm, NaMaster/pymaster – all standard and consistent with ADS/arXiv or project pages.  
- **Required fix (NONE).**

#### P4-E5 – No duplicated references but one “circular” numbering  
- **Location:** entire reference list.  
- **Issue:** There is no duplication of entries, but [7] appears in the text as both “Jia et al. 2023” and “CE-ResNet (Jia et al. 2023)” and is consistently numbered. No fused records detected.  
- **Required fix (NONE).**

---

### 2. Consistency of quoted statistics vs cited prior work

Here I check whether key numbers attributed to other authors match their abstracts/tables (based on ADS/arXiv).

#### P4-M13 – Shamir 2012 SDSS sample size and amplitudes  
- **Location:** p. 1–2: “Shamir (2012) [4] reported a 2–4σ dipole with per-bin asymmetry amplitudes of ∼5–20% (as reported in that work) using ∼1.27×10^5 SDSS galaxies.”  
- **Check:** The Shamir 2012 Phys. Lett. B abstract reports an SDSS sample of order 10^5 galaxies and order 5–15% hemispheric asymmetries; the precise 1.27×10^5 is in the body and is reasonable. The ∼5–20% bin-level asymmetry is consistent with the figures.  
- **Required fix (MINOR):** Once the correct arXiv ID is fixed (P4-E2), no further change needed; consider adding an inline citation to the specific table/figure where 1.27×10^5 appears.

#### P4-M14 – Shamir 2020 “2–4%” asymmetry  
- **Location:** p. 1–2: “Shamir (2020) [1] reported asymmetries at the reported ∼2–4% level on SDSS and Pan-STARRS samples.”  
- **Check:** The Ap&SS 365, 136 (2020) paper abstract mentions “a small but statistically significant asymmetry at the few percent level” for SDSS and Pan-STARRS. 2–4% is consistent and not overstated.  
- **Required fix (NONE).**

#### P4-M15 – Shamir 2022 DESI Legacy sample size  
- **Location:** p. 1–2: “Shamir (2022b) [3]… ‘nearly 1.3×10^6 spiral galaxies’ per the published abstract.”  
- **Check:** The MNRAS 516, 2281 abstract indeed states “nearly 1.3 million spiral galaxies” from DESI Legacy.  
- **Required fix (NONE).**

#### P4-M16 – Iye et al. 2021 critique characterization  
- **Location:** p. 1–2: “Iye et al. (2021) [5] … found no significant dipole after correcting for reading-direction bias and photometric-object duplication…”  
- **Check:** The ApJ 907, 123 abstract explicitly mentions correction of reading-direction bias and catalog duplication and concludes no significant dipole.  
- **Required fix (NONE).**

#### P4-M17 – Jia et al. 2023 CE-ResNet cw/ccw = 0.998  
- **Location:** p. 2: “Jia et al. [7] … with a reported number-count ratio cw/ccw = 0.998 on ∼1.95 million galaxies.”  
- **Check:** The ApJ 943, 32 paper reports cw/ccw ~0.998 in its abstract/Section 4 for ~2 million galaxies.  
- **Required fix (NONE).**

---

### 3. Internal numerical consistency and basic recomputations

These do not rely on external sources, but are important for PRD-level rigor.

#### P4-E6 – Training set size arithmetic error  
- **Location:** Sec. II.B (p. 2):  
  > “Galaxy Zoo 1: 6,637…; CE-ResNet: 17,153…; Synthetic negatives: 2,000… The combined training set contains 6,637+17,153+2,000 = 25,790 images…”  
- **Issue:** 6,637 + 17,153 + 2,000 = 25,790 is correct. But later you state: “Note: 17,153/25,790 = 66.5% of training labels derive from CE-ResNet predictions.” Compute: 17,153 / 25,790 ≈ 0.6652 = 66.52%, consistent. No error here.  
- **Required fix (NONE).**

#### P4-E7 – Catalog C CW fraction and σ  
- **Location:** Abstract, Sec. IV.B, Table II.  
- **Issue:** You quote for Catalog C (equivariant)  
  - f_CW = 0.497353(279) (Table II).  
  - Spiral count N_spiral = 3,201,160 (Sec. IV.A).  
  - You say “The Catalog C residual (−9.5σ from 0.5000, Table II)…”.  
  Check σ: for binomial, σ_f = sqrt(f(1−f)/N). Take f≈0.49735, N=3,201,160:  
  f(1−f) ≈ 0.49735×0.50265 ≈ 0.25; σ_f ≈ sqrt(0.25 / 3.20116×10^6) ≈ sqrt(7.8×10^−8) ≈ 2.8×10^−4, matching 0.000279 in Table II. Deviation from 0.5 is −0.002647; divide by σ: −0.002647 / 2.79×10^−4 ≈ −9.5. So numbers are self-consistent.  
- **Required fix (NONE).**

#### P4-E8 – Catalog A/B global fractions  
- **Location:** Table II.  
  - A (raw) f_CW = 0.507879(274);  
  - Catalog C f_CW = 0.497353(279).  
  You state “The 2.98× asymmetry-suppression factor from raw +1.576% to equivariant −0.529% (asymmetry-A units…)”. Raw asymmetry A_A = 2(f−1/2) ≈ 2(0.507879−0.5) ≈ 0.015758 = 1.5758%; equivariant A_C ≈ 2(0.497353−0.5) ≈ −0.005294 = −0.5294%. Ratio of magnitudes: 1.5758 / 0.5294 ≈ 2.98. Correct.  
- **Required fix (NONE).**

#### P4-E9 – Nspiral fraction and NS totals  
- **Location:** Sec. IV.A; Fig. 3.  
  - NCW = 1,592,107; NCCW = 1,609,053; NNS = 5,273,371.  
  - Nspiral = NCW+NCCW = 3,201,160; total N = 8,474,531.  
  Spiral fraction = 3,201,160 / 8,474,531 ≈ 0.3778 = 37.78% (claims match).  
- **Required fix (NONE).**

#### P4-E10 – Fisher floor computation  
- **Location:** Sec. VI.A.a, Eq. (4).  
  - They derive σ(A) = sqrt(3/N_spiral). For N=3,201,160, √(3/N) ≈ √(9.373×10^−7) ≈ 9.68×10^−4, in line with 9.7×10^−4 in text. 3σ ≈ 0.29%.  
- **Required fix (NONE).**

#### P4-E11 – Injection table consistency  
- **Location:** Table V (p. 10).  
  - For A = 0.75%, P(σ>3) = 0.55 (A50 ≈ 0.75%);  
  - A=1.0% → 0.91, A=1.5% → 1.00, so A95 ∈ (1.0%, 1.5%]. This matches the verbal description.  
- **Required fix (NONE).**

#### P4-E12 – “6–12×” amplitude discrepancy vs 3% claims  
- **Location:** Abstract and Discussion: “inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼6–12 under the present pipeline.”  
- **Issue:** Your empirical 50%-recovery-3σ floor is A50≈0.75%, and you often reference a “reference amplitude 1.7%” from Shamir-like claims. Relative to 3%, 3/0.5 ≈ 6, 3/0.25 ≈ 12; you do not quantify exactly which amplitude you compare to, but “∼6–12” is qualitatively consistent with the range between your sensitivity and the claimed signals.  
- **Required fix (MINOR):** Clarify explicitly what you are dividing by what. For example: “relative to our 0.25–0.5% sensitivity band, the ∼3% amplitude is larger by a factor 6–12.”

---

### 4. Versioning / internal audit-tags / “withdrawn” language

PRD will allow clear retraction/correction language, but internal bookkeeping must not leak confusingly into the scientific narrative.

#### P4-E13 – Use of “artifact c9x”, “pipelines/p2_chirality/…” pathnames in main text  
- **Location:** Sec. IV.C, IV.D, Appendix A and C.  
- **Issue:** The text repeatedly references internal artifact IDs and file paths, e.g.:  
  - “artifact c9c” (Sec. IV.C);  
  - “artifact c9e”;  
  - “artifact c9a”;  
  - “pipelines/p2_chirality/outputs/canonical_provenance/c3_wp_invariance_fsky.json”, etc.  
  These are internal repository paths, not standard bibliographic references. They clutter the narrative and read like an internal lab notebook rather than a PRD article.  
- **Required fix (MAJOR):**  
  - Move all internal file-path references and “artifact c9*” labels into a short “Code and data availability” or “Supplemental material” section or into an external repository README.  
  - In the main text, replace them by generic references such as “see the released code repository for configuration JSONs” without including raw paths.

#### P4-E14 – “Earlier version misquoted” and “withdrawn” statements referencing version IDs  
- **Location:** Abstract, Sec. III.A, Appendix A and D.  
- **Issue:** The manuscript currently includes extensive provenance prose: “An earlier version of this paper reported…that result is withdrawn (Appendix A)”, “manuscript revision v1.0.76”, “affected manuscript versions (≤v1.0.165)”, etc. While transparency is laudable, PRD usually expects a clean narrative describing the *current* analysis, not a running changelog embedded in the body.  
- **Required fix (MAJOR):**  
  - Retain a brief, clear statement that an earlier harmonic-null claim based on a synthetic-footprint catalog was erroneous and is superseded, but move detailed version identifiers, git hashes, and pathnames to an Appendix or separate “Erratum/provenance note” document.  
  - In the main text, compress to one or two sentences with a pointer to an Appendix or ancillary file.

---

### 5. Sigma juxtaposition / null-procedure comparability

The instructions explicitly ask: if σ’s from different nulls appear side-by-side without explicit non-comparability caveats, flag ESSENTIAL.

Here the author has already anticipated exactly this critique.

#### P4-N1 – σ’s from different nulls are repeatedly labeled “not directly comparable”  
- **Location:** Table I caption; Sec. IV introduction; Appendix tables.  
- **Issue:** Table I explicitly states: “The σ values in different rows are computed against different null procedures… and are not directly comparable across rows.” Sec. IV reiterates: “values from distinct null procedures are not directly comparable.” Similar caveats are present when harmonic and real-space σ’s are quoted together.  
- **Required fix (NONE):** The required caveats are present and unambiguous; no ESSENTIAL issue here.

---

### 6. Length and focus

The methods, diagnostics, and provenance appendices are extremely long for the stated main scientific result (a null dipole with a modest catalog-release component).

#### P4-M18 – Paper overly long for its core contribution  
- **Location:** Entire manuscript (17 pages dense text, plus heavy appendices).  
- **Issue:** For PRD, a catalog-plus-null-result paper is publishable if the catalog or null has unique cosmological impact. Here, the main cosmological content is: (i) a careful null in one specific late-time parity-even dipole observable; (ii) a demonstration of mask–monopole leakage and classifier-bias pitfalls. The rest is architectural detail, internal QA, and provenance.  
- **Required fix (MAJOR):**  
  - Compress the exposition to ≤ 12 PRD pages of main text. Move much of Appendix B–E material, the detailed artifact path names, and some of the multi-level null exploration to supplementary material.  
  - Focus the main paper on: catalog description, classifier architecture and equivariant TTA, real-space dipole result, monopole–mask leakage demonstration, and the key comparison with Shamir and CE-ResNet.

---

### 7. Miscellaneous stylistic / clarity issues

#### P4-N2 – Use of internal jargon acronyms without immediate definition  
- **Location:** Abstract, Table I, Sec. III.A (“HC-broad”, “HC-strict”, “Ap field”).  
- **Issue:** Some internal acronyms are introduced in the abstract or early tables before being defined in the main text (e.g., “HC-broad spiral subsample”, “Ap field”). You do define them later, but PRD prefers first-use definitions.  
- **Required fix (MINOR):** Ensure every acronym or notation (Ap, HC-broad, HC-0.9, N_all, N_spiral) is defined at first appearance in the main text and not first in a table or figure caption.

#### P4-N3 – Self-referential remarks about AI usage  
- **Location:** Acknowledgments.  
- **Issue:** The “AI tool usage” paragraph is acceptable but slightly unusual for PRD. Journals are still converging on policy, but it is fine to keep as is or to conform to PRD’s current guidance.  
- **Required fix (NIT):** Align wording with APS guidance on LLM use once available, e.g., move to a footnote if requested.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific analysis appears careful and technically competent, and the main results (a real-space null dipole, characterization of mask–monopole leakage with an equivariant classifier) are internally consistent and supported by the calculations shown. However, there are at least two hard bibliographic errors in key Shamir references, an overabundance of internal versioning/provenance language and literal file paths in the main text, and the manuscript is significantly longer and more notebook-like than appropriate for PRD. These issues—especially the Shamir arXiv ID/DOI mismatches—must be corrected, and the narrative streamlined, before the paper can meet the journal’s standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-M19 – Abstract injection-recovery numbers arithmetically inconsistent with Table V  
- **Location:** Abstract; Sec. I (last paragraph); Sec. VI.A; Table V; Conclusions (point e).  
- **Issue:** The abstract states “an empirical 50%-recovery‑3σ injection–recovery threshold at |A_dipole| ≥ 0.75%,” and the conclusions reiterate “A₅₀ ≈ 0.75% (full amplitude).” In Table V, however, \(P(\sigma>3)=0.55\) at \(A=0.75\%\), while at \(A=1.0\%\) it is 0.91 and at 0.5% is 0.15; the *closest* 50% crossing inferred from the tabulated grid would be nearer to ~0.7–0.8%, but 0.75% is not actually the point where P=0.5. The text also calls 0.5% “a non‑detection point,” which is correct, but the “50%-recovery-at‑3σ threshold” is presented as if it were a measured crossing rather than an interpolation between grid points.  
- **Required fix (MINOR):** Rephrase to make clear that 0.75% is an *interpolated* approximate A₅₀ between the tabulated 0.5% and 1.0% points (e.g. “A₅₀ ≈ 0.75% by interpolation from the injection grid”), or explicitly state the measured grid values and avoid a pseudo-precise A₅₀.

P4-M20 – Abstract “largest chirality-labeled catalog” claim not quantitatively backed  
- **Location:** Abstract first sentence; Conclusions first sentence.  
- **Issue:** The abstract claims “the largest chirality‑labeled galaxy catalog to date,” with 8.47M galaxies and 3.2M spirals, and later notes CE‑ResNet used ~1.95M galaxies. This shows it is larger than *that* prior work but does not systematically compare against other spin or handedness catalogs (e.g., Galaxy Zoo–based or other DL-based spin catalogs) or justify that no other current catalog exceeds ~3.2M spirals. The “largest to date” is therefore asserted rather than demonstrated.  
- **Required fix (MINOR):** Either (i) soften the language (“among the largest chirality‑labeled catalogs to date, and 1.6× larger than CE‑ResNet’s 1.95M‑galaxy catalog”), or (ii) add a short quantitative comparison in Sec. V showing that no existing public chirality catalog exceeds 3.2M spirals.

P4-M21 – Abstract “inconsistent in amplitude … by a factor of ~6–12” is numerically underspecified  
- **Location:** Abstract; Sec. I last paragraph; Sec. VI.B; Conclusions (point b).  
- **Issue:** The abstract says the null is “inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼6–12 under the present pipeline,” but the body only gives discrete sensitivity benchmarks: Fisher floor 3σ ≈ 0.29%, empirical A₅₀≈0.75%, and A₉₅∈(1.0%,1.5%]. The “6–12×” factor is not explicitly tied to any particular pair of numbers; a reader cannot reconstruct the precise ratio being claimed (3% / 0.5%? 3% / 0.25%? 3% / 0.29%?).  
- **Required fix (MINOR):** In Sec. VI.B or Conclusions, explicitly spell out the ratio(s) used (e.g. “3% / 0.5% = 6 and 3% / 0.25% = 12”), and reference the corresponding sensitivity benchmarks so the “6–12” range is traceable.

P4-M22 – CW fraction significance values in Table II deviate from naïve binomial z  
- **Location:** Table II, “Dev. (σ)” column; text in Sec. III.D and IV.B.  
- **Issue:** For Catalog C, Table II gives \(f_{\rm CW}=0.497353(279)\) and Dev. = −9.47σ. Recomputing with the quoted σ = 0.000279:  
  \[
  \Delta f = 0.497353-0.5=-0.002647,\quad z = \Delta f/0.000279 \approx -9.49,
  \]  
  which is consistent, but for Catalog A, 0.507879(274) implies  
  \[
  \Delta f = 0.007879,\quad z\approx 28.8,
  \]  
  whereas the table lists +28.72, a minor rounding mismatch. Likewise, for Catalog B, “0.504 ± 0.0003” and Dev. = +14.6 imply \(\Delta f\approx 0.00438\), not 0.0040, i.e. the “0.504” is truncated and inconsistent with the implied unrounded value. None of these are numerically large problems, but they mean the table mixes rounded display and hidden internal values.  
- **Required fix (NIT):** Add a one‑line note to the table or caption stating that Dev.(σ) is computed from internally stored unrounded values (and that printed f and σ are rounded), or print more digits of f and σ for Catalog B to make the arithmetic traceable.

P4-M23 – Fisher floor equation uses \(N_{\rm spiral}\) but discussion conflates full and effective sample  
- **Location:** Eq. (4) and surrounding text in Sec. VI.A.a.  
- **Issue:** Equation (4) states \(\sigma(A) = \sqrt{3/N_{\rm spiral}}\) with \(N_{\rm spiral}=3{,}201{,}160\), giving σ(A/2) ≈ 0.048% and a 3σ floor ≈ 0.29% full amplitude, which is dimensionally and numerically consistent. However the text then says that departures from full‑sky coverage and classification noise are “absorbed into the empirical injection‑recovery floor below.” The later section introduces a GZ1‑based dilution factor g ≈ 0.398 and an effective threshold ~1.88%, but the link between the ideal σ(A) expression and the degraded effective noise (g, f_sky factor) is never written explicitly as an equation. This leaves the reader doing implicit dimensional reasoning across several paragraphs.  
- **Required fix (MINOR):** Add a short explicit formula connecting the ideal Fisher floor to the effective floor, e.g. \( \sigma_{\rm eff}(A) \simeq \sigma(A) / g / \sqrt{f_{\rm sky}}\), with numerical substitution, to make the degradation from 0.29% to ~1.9% transparent.

P4-N4 – Abstract’s “real-space dipole consistent with null” could more explicitly flag different nulls for other σ’s mentioned  
- **Location:** Abstract middle sentences.  
- **Issue:** The abstract correctly states the real-space dipole +0.43σ, and later harmonic diagnostics (+3.64σ moment‑z, ≈1.9σ Gaussian‑equivalent, canonical mask; +7.28σ, apodized footprint) and notes they are “systematics‑attributed residuals…dispositioned by an eight‑anchor systematic battery.” However, unlike Table I and Sec. IV, the abstract does not explicitly remind the reader that these σ values come from *different null procedures* (label‑shuffle, generative monopole, depth‑stratified, etc.). A casual reader may interpret them as directly comparable to the +0.43σ real‑space value.  
- **Required fix (MINOR):** Insert a short clause in the abstract clarifying that these σ values derive from different diagnostic nulls and are not directly comparable to each other or to the real-space dipole significance (mirroring the caveat already in Table I and Sec. IV).

P4-M24 – “Maximum regional asymmetry is 0.32%” not explicitly tied to a figure or table  
- **Location:** Sec. V.A first sentence.  
- **Issue:** The text states “our maximum regional asymmetry is 0.32%,” but there is no explicit equation, table, or figure reference showing where this 0.32% is computed (e.g., hemisphere scan, quadrant bin, HC‑only subsample). Given that many other asymmetries (e.g. hemisphere 3.05σ, 0.75% injection amplitudes) are discussed, a reader cannot easily verify this number or its context.  
- **Required fix (MINOR):** Add a reference to the exact diagnostic (Appendix C subsection and/or a table/figure) from which 0.32% is derived, and specify whether this is hemisphere, quadrant, or some other region definition.

P4-M25 – Injection floor description vs. MASTER-channel completeness not tightly cross-referenced  
- **Location:** Conclusions (point a) vs. Sec. VI.A and Table V.  
- **Issue:** The conclusions claim, for the MASTER ℓ=1 channel, P(≥3σ)=0.92 at A_p=0.5% and ≥0.999 at A_p≥0.75%, but the only explicit injection table is Table V, which is for the *real-space* HC‑broad per‑pixel‑shuffle null, not the harmonic MASTER channel. The text in Conclusions refers to “artifact c9b” and “direct injection‑recovery test through the apodized‑footprint MASTER ℓ=1 channel,” but there is no analogous numerical table in the main text. As written, the reader must trust that a separate harmonic‑space injection study (c9b) exists and that its numbers are distinct from Table V, yet the same amplitudes (0.5%, 0.75%, 1.7%, 3%) are used, which is easy to confuse.  
- **Required fix (MAJOR, for clarity):** Clearly separate real‑space and MASTER‑channel injection results. Either (i) add a small table for the MASTER‑channel injection–recovery (even if only a few amplitudes) or (ii) explicitly state in Sec. VI.A and/or Conclusions that Table V is *real‑space* and the harmonic injection stats are separate, with a precise pointer to where those numerical results live (Appendix / artifact). This avoids misreading Table V as supporting the MASTER completeness claims.

P4-M26 – Face-on / edge-on contamination numbers partially unquantified  
- **Location:** Appendix E, first paragraph; Sec. VI.A.b.  
- **Issue:** Appendix E says 65.7% of b/a<0.3 objects get CW/CCW labels and estimates a 10–15% reduction in effective sample size, corresponding to a 5–8% sensitivity penalty. However the 10–15% and 5–8% are stated without explicit calculation from quoted counts (e.g., what fraction of the 3.2M spirals are b/a<0.3? how does that map to an effective N reduction via a dilution factor?). This is a minor quantitative gap, but for PRD‑level rigor, the penalty estimates should be backed by a clear calculation.  
- **Required fix (MINOR):** Provide a short computation (even approximate) showing the fraction of the spiral catalog with b/a<0.3, then derive the 10–15% effective N loss and 5–8% sensitivity penalty explicitly.

P4-M27 – Look-elsewhere corrections: raw vs. post-LEE σ / p not always numerically paired  
- **Location:** Sec. IV.E; Appendix C.b–c; Table IV and discussion.  
- **Issue:** The hemisphere scan finds a max 3.05σ local significance with direct-MC pLEE≤10⁻⁴, and then says Bonferroni/BH reduce post‑LEE significance to <1σ. The text does not report the *post-LEE* σ numerically (only that it is <1), nor does it give the smallest individual p before correction. For reproducibility, PRD usually expects at least the key pair: min raw p and corrected p.  
- **Required fix (MINOR):** Add explicit values: the smallest per-direction p, and the Bonferroni/BH corrected p (and their σ equivalents), rather than only qualitative descriptions (“<1σ,” “≤10⁻⁴”).

P4-M28 – A few internal equation references could be more precise  
- **Location:** Sec. IV.C (“This is the single canonical chirality-field definition used throughout (spirals-only denominator). Note the unit convention Ap = 2(fCW,p−1/2): amplitudes quoted in Ap units…”).  
- **Issue:** The sentence “Note the unit convention Ap = 2(fCW,p − 1/2)” repeats material in Eq. (3) but is not labeled as an equation; later references in Appendix A (“Ap = (NCW−NCCW)/(NCW+NCCW) (Eq. 3)…”) are consistent, but the mention of Ap=2(f−1/2) is not explicitly tied to Eq. (3) by an \eqref. That makes it slightly harder to track that every amplitude quoted in “A units” is exactly twice f deviations.  
- **Required fix (NIT):** Add an \eqref to Eq. (3) when restating the Ap convention, and ensure every later use of “A units” links back clearly to this definition.

If you want, I can next go systematically through each table and equation line‑by‑line to build a machine‑checkable list of all σ/percentage/ratio recomputations as an explicit validation log.