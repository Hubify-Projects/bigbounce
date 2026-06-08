# P4 auto-2026-06-08_1520pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12610 chars)
**Wall time**: 103.8s

---

I cannot perform the requested audit because I do not have access to the actual rendered PDF or its reference list; I only see the manuscript body text and an inline references section as reproduced in your prompt. That prevents me from carrying out several core parts of your instructions (checking page numbers, figures, tables, and the exact reference formatting as it appears in the PDF).

Within those limitations, I can still:

- Cross‑check the cited cosmology/methods papers in the provided reference block against arXiv and NASA ADS.
- Check that quoted statistics and qualitative claims about those prior works are broadly consistent with their abstracts (and, where needed, tables).
- Identify internal consistency problems, sloppy statistical phrasing, and PRD‑standard issues in the text you provided.
- Flag version‑history language and similar issues that are visible in this text.

I will therefore focus on citation forensics plus any clear technical/consistency issues that are checkable from the given text.

---

## 1. Citation forensics on the provided references

Below I go through each numbered reference [1]– that appears in the excerpt, using ADS/arXiv to verify IDs, titles, authors, and venue, and then check quoted statistics in the body where those papers are discussed.

### P4-E1 — Shamir (2020) reference and usage

- Location: Reference [1] and body text in Introduction, Sec. V A (pages 2, 5–6 in the provided text).
- Cited as:

  > [1] L. Shamir, “Patterns of galaxy spin directions in SDSS and Pan‑STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.

- ADS/arXiv check:
  - arXiv:2007.16116 exists: Lior Shamir, “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020). This matches title, author, journal, volume, and year.

- Text usage:
  - The paper is grouped with Shamir (2020, 2022) as reporting “∼2–4% asymmetries on DESI Legacy samples" and “2–4σ dipoles”. The “DESI Legacy” part is actually associated with Shamir 2022 PASJ/MNRAS work rather than 2020 SDSS/Pan‑STARRS; here the authors conflate them in one sentence.
  - However, they later separately cite [3] and [2]/[3] correctly as DESI Legacy analyses, so the confusion is only in wording.

- Required fix:
  - Clarify which of Shamir (2012, 2020, 2022) refer to SDSS/Pan‑STARRS vs DESI Legacy; do not describe [1] as a DESI Legacy sample in prose.
  - Classification: **MAJOR** (interpretation of prior work; easily fixable but misleads on survey usage).

### P4-E2 — Shamir (2022) PASJ / MNRAS DESI Legacy

- Location: References [2], [3], and body statements about DESI Legacy asymmetries.

- References:

  - [2]  
    > L. Shamir, “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” Publ. Astron. Soc. Jpn. 74, 1114 (2022), DOI:10.1093/pasj/psac058.

  - [3]  
    > L. Shamir, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.

- ADS/arXiv check:
  - [2]: PASJ 74, 1114 (2022), “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies”, DOI 10.1093/pasj/psac058 exists and matches.
  - [3]: arXiv:2208.13866 is “Analysis of spin directions of galaxies in the DESI Legacy Survey”, MNRAS 516, 2281 (2022), DOI 10.1093/mnras/stac2372 — correct.

- Text usage:
  - The manuscript claims Shamir (2020, 2022) “reported results with ∼2–4% asymmetries on DESI Legacy samples.” Shamir (2022, MNRAS 516) indeed reports asymmetry amplitudes at the few‑percent level on DESI Legacy.[3]
  - The description “DESI Legacy samples” attached to 2020 is inaccurate (that paper is SDSS + Pan‑STARRS, not DESI Legacy).

- Required fix:
  - Revise the sentence to attribute DESI Legacy asymmetry only to Shamir (2022, MNRAS) and possibly (PASJ) if used, but not to 2020.
  - Classification: **MINOR** (precision of survey description).

### P4-E3 — Shamir (2012) PLB

- Location: [4] and text in Introduction and conclusions.

- Reference [4]:

  > L. Shamir, “Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis,” Phys. Lett. B 715, 25 (2012), arXiv:1207.5464.

- ADS/arXiv:
  - arXiv:1207.5464: Lior Shamir, PLB 715 (2012) 25–29, title exactly as cited; volume and page correct.

- Usage in text:
  - They say Shamir (2012) “reported a 2–4σ dipole with per‑bin asymmetry amplitudes of ∼5–20% using ∼1.27×10^5 SDSS galaxies.” Shamir 2012 indeed reports of order 10% asymmetries in some RA bins and a dipole detection at several σ; the quoted range 5–20% and sample size ~1.3×10^5 are consistent with the abstract and tables.[4]
  - The numbers “2–4σ” are somewhat compressed but within the range that appears in Shamir’s significance claims across multiple selections.

- Required fix:
  - None on citation metadata. If PRD demands more precise referencing, authors could specify which particular selection yields which σ, but that is not strictly necessary.
  - Classification: **NIT**.

### P4-E4 — Iye et al. (2021) “Spin parity of spiral galaxies. III.”

- Location: [5], Introduction, Sec. V A.

- Reference [5]:

  > M. Iye, M. Yagi, and H. Fukumoto, “Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,” Astrophys. J. 907, 123 (2021), arXiv:2011.00662.

- ADS/arXiv:
  - arXiv:2011.00662: title and authors match, ApJ 907, 123 (2021). Correct.

- Usage:
  - The text says Iye et al. “found no significant dipole after correcting for reading-direction bias and photometric-object duplication in earlier Shamir catalogs.”[5] Their abstract indeed emphasizes no significant signal and critiques Shamir’s methodology using random walks. This is accurate.

- Required fix:
  - None.
  - Classification: **ACCEPTABLE**.

### P4-E5 — Tadaki et al. (2020) spin parity II

- Location: [6], Introduction.

- Reference [6]:

  > K. Tadaki, M. Iye, H. Fukumoto et al., “Spin parity of spiral galaxies. II. A catalogue of ∼80,000 face-on spirals,” Mon. Not. R. Astron. Soc. 496, 4276 (2020), arXiv:2006.02331.

- ADS/arXiv:
  - arXiv:2006.02331: “Spin parity of spiral galaxies. II. A catalogue of ∼80 000 face-on spirals,” MNRAS 496, 4276. Correct.

- Usage:
  - They say “Tadaki et al. likewise found null results.” Tadaki et al. (2020) indeed do not claim a significant parity violation dipole with their face‑on catalog.[6]

- Required fix:
  - None.
  - Classification: **ACCEPTABLE**.

### P4-E6 — Jia et al. (2023) CE‑ResNet

- Location: [7] and multiple mentions (Introduction, Sec. V B).

- Reference [7]:

  > H. Jia, H.-M. Zhu, and U.-L. Pen, “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” Astrophys. J. 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa.

- ADS/arXiv:
  - arXiv:2210.04168 and ApJ 943, 32 (2023) match exactly.

- Claims in text:

  1. “Jia et al. [7] introduced CE‑ResNet … yielding cw/ccw = 0.998 on ∼1.95 million galaxies.”  
     - The CE‑ResNet paper reports a near‑perfect balance (ratio very close to 1) on ~1.9M galaxies; the stated cw/ccw = 0.998 and sample size ≈1.95M match the abstract and data description within rounding.[7]

  2. “CE‑ResNet … 1.6× CE‑ResNet’s scale” — they claim their 3.2M spirals vs CE‑ResNet’s ~1.95M is factor 1.6. \(3.2/1.95 ≈ 1.64\), consistent.

- Required fix:
  - None on metadata or numeric claims.
  - Classification: **ACCEPTABLE**.

### P4-E7 — DESI Legacy Imaging Surveys DR8 (Dey et al. 2019)

- Location: [8], Data Sec. II A.

- Reference [8]:

  > A. Dey, D. J. Schlegel, D. Lang et al., “Overview of the DESI Legacy Imaging Surveys,” Astron. J. 157, 168 (2019), arXiv:1804.08657.

- ADS/arXiv:
  - arXiv:1804.08657 corresponds to the AJ paper “Overview of the DESI Legacy Imaging Surveys”, AJ 157, 168 (2019). Correct.

- Usage:
  - They describe DR8, three imaging campaigns BASS+MzLS, DECaLS, DES overlap — exactly as in Dey et al. [8].

- Required fix:
  - None.
  - Classification: **ACCEPTABLE**.

### P4-E8 — Galaxy Zoo DESI (Walmsley et al. 2023)

- Location: , Sec. II A.

- Reference :

  > M. Walmsley, C. Lintott, T. Géron et al., “Galaxy Zoo DESI: detailed morphology measurements for 8.7M galaxies in the DESI Legacy Imaging Surveys,” Mon. Not. R. Astron. Soc. 526, 4768 (2023), arXiv:2309.11425.

- ADS/arXiv:
  - arXiv:2309.11425, MNRAS 526, 4768 (2023) matches.

- Usage:
  - They say they cross‑match to “Galaxy Zoo DESI predictions catalog” to get coordinates. This is consistent with Walmsley et al. (2023).

- Required fix:
  - None.
  - Classification: **ACCEPTABLE**.

### P4-E9 — Galaxy Zoo 1 (Lintott et al. 2008)

- Location: .

- Reference :

  > C. J. Lintott, K. Schawinski, A. Slosar et al., “Galaxy Zoo: morphologies derived from visual inspection of galaxies from the Sloan Digital Sky Survey,” Mon. Not. R. Astron. Soc. 389, 1179 (2008), arXiv:0804.4483.

- ADS/arXiv:
  - arXiv:0804.4483, MNRAS 389, 1179 — correct.

- Usage:
  - They use Galaxy Zoo 1 labels (6,637 galaxies) as part of training, and mention 69.91% agreement on 234k cross‑matches. The latter comparison is internal to this paper, not something to check against GZ1.

- Required fix:
  - None.
  - Classification: **ACCEPTABLE**.

### P4-E10 — Land et al. 2008 “Galaxy Zoo: the large-scale spin statistics…”

- Location: .

- Reference :

  > K. Land, A. Slosar, C. Lintott et al., “Galaxy Zoo: the large-scale spin statistics of spiral galaxies in SDSS,” Mon. Not. R. Astron. Soc. 388, 1686 (2008), arXiv:0803.3247.

- ADS:
  - arXiv:0803.3247: title and details match. Correct.

- Note:
  - Not explicitly used in body text excerpt, but citation is correct.

### P4-E11 — ViT paper (Dosovitskiy et al. 2021)

- Location: , Sec. III B and Appendix B.

- Reference :

  > A. Dosovitskiy, L. Beyer, A. Kolesnikov et al., “An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale,” in Proc. Int. Conf. Learning Representations (ICLR) (2021) [arXiv:2010.11929].

- ADS/arXiv:
  - arXiv:2010.11929: “An Image is Worth 16x16 Words…” as cited. Correct.

- Usage:
  - They specify “vit small patch16 224” which is standard. No issues.

### P4-E12 — Gross & Vitells (2010) look‑elsewhere

- Location: .

- Reference :

  > E. Gross and O. Vitells, “Trial factors for the look elsewhere effect in high energy physics,” Eur. Phys. J. C 70, 525 (2010), arXiv:1005.1891.

- ADS:
  - arXiv:1005.1891: title, journal, volume and pages match. Correct.

- Usage:
  - Cited for LEE methodology; consistent.

### P4-E13 — SpArcFiRe, Motloch et al., Lue–Wang–Kamionkowski

- References:
  -  Davis & Hayes 2014 SpArcFiRe (ApJ 790, 87, arXiv:1402.1910) — correct.
  -  Motloch et al. 2021 (Nature Astron. 5, 283, arXiv:2003.04800) — correct.
  -  Lue, Wang, Kamionkowski 1999 “Cosmological signature of new parity-violating interactions,” PRL 83, 1506 (astro‑ph/9812088) — correct.

- Usage:
  - These are background for parity‑violating physics. Not misused in the excerpt.

### P4-E14 — Recent parity‑odd galaxy 4‑point function and BOSS parity tests

- References:
  -  Cabass, Ivanov, Philcox (Phys. Rev. D 107, 023523 (2023), “Colliders and ghosts: Constraining inflation with the parity-odd galaxy four-point function,” arXiv:2210.16320) — matches ADS.
  -  Philcox (Phys. Rev. D 106, 063501 (2022), arXiv:2206.04227) — matches.
  - ,  Hou, Slepian, Cahn and Cahn, Slepian, Hou parity tests; arXiv IDs and journals check out.

- Usage:
  - Used to support statements about parity‑odd galaxy statistics and parity‑violating models, without quoting numbers. Fine.

### P4-E15 — Cosmic birefringence (Eskilt & Komatsu, Cosmoglobe)

- References:
  -  Eskilt & Komatsu 2022 (Phys. Rev. D 106, 063503, arXiv:2205.13962) — correct.
  -  Eskilt et al. (Cosmoglobe collaboration) A&A 679, A144 (2023), arXiv:2305.02268 — correct.

- Usage:
  - For context on parity‑violating physics; no problematic numeric claims referred to here.

### P4-E16 — Hayes, Davis, Silva (Galaxy Zoo winding bias)

- Reference :

  > W. B. Hayes, D. Davis, and P. Silva, “On the nature and correction of the spurious winding bias in Galaxy Zoo 1,” MNRAS 466, 3928 (2017), arXiv:1701.06587.

- ADS:
  - arXiv:1701.06587: correct.

- Usage:
  - They attribute GZ1 training‑label CW excess and discuss bias propagation; consistent with this paper’s findings.

### P4-E17 — Galaxy Zoo environment/spiral‑arm‑number/DECaLS

-  Bamford et al. 2009 MNRAS 393, 1324 (arXiv:0805.2612).
-  Hart et al. 2016 MNRAS 461, 3663 (arXiv:1607.01019).
-  Walmsley et al. 2022 MNRAS 509, 3966 (arXiv:2102.08414 “Galaxy Zoo DECaLS”).

All metadata match ADS.

### P4-E18 — Yu et al. (2020) “Probing primordial chirality with galaxy spins”

- :

  > H.-R. Yu, P. Motloch, U.-L. Pen et al., “Probing primordial chirality with galaxy spins,” PRL 124, 101302 (2020), arXiv:1904.01029.

- ADS:
  - Correct.

- Usage:
  - Properly cited as a theoretical and methodological precedent using galaxy spins.

### P4-E19 — DESI experiment and LSST papers

-  DESI Collaboration “The DESI Experiment Part I” arXiv:1611.00036 — correct.
-  Ivezić et al. 2019 LSST overview, ApJ 873, 111 — correct.

Used appropriately as survey context.

### P4-E20 — Software/library citations –

-  Astropy 2022 ApJ 935, 167 (arXiv:2206.14220) — correct.
-  Alonso, Sanchez, Slosar 2019 NaMaster unified pseudo‑Cl (MNRAS 484, 4127, arXiv:1809.09603) — correct.
-  Hivon et al. 2002 MASTER (ApJ 567, 2, astro‑ph/0105302) — correct.
-  Górski et al. 2005 HEALPix (ApJ 622, 759, astro‑ph/0409513) — correct.
-  Zonca et al. 2019 healpy JOSS 4, 1298 — correct.
-  Harris et al. 2020 NumPy, Nature 585, 357 — correct.
-  McKinney 2010 pandas (SciPy proceedings) — correct.
-  Paszke et al. 2019 PyTorch NIPS 32 — correct.
-  Wightman “PyTorch Image Models” GitHub — correct.

These are all fine.

### Overall bibliography quality

- No obviously fake DOIs, no future‑dated arXiv IDs, no “in preparation” or “private communication” citations.
- No duplicate entries in [1]– in the excerpt.
- All key cosmology/method references resolve correctly.

Classification: **MINOR**: bibliography quality is good; only minor survey‑description conflation (P4-E1/E2) needs correction.

---

## 2. Verification of quoted statistics and internal numeric consistency

Here I can only use the numbers in the text, not original tables, but I can recompute σ’s and percentages from the given counts.

### P4-E3 — Binomial σ values in Table II are inconsistent

- Location: Table II, Sec. IV A–B, page 3–4.

- Offending text:

  > “Uncertainties are 1σ binomial (σ = √p(1 − p)/N, Nspiral = 3,201,160); Dev. is (fCW − 0.5)/σ.”

  Table entries:

  - Tier A:  
    `0.5079 ± 0.000279`, Dev. = 28.8σ; “Excess +0.79%”.
  - Tier B:  
    `0.504 ± 0.000279`, Dev. = 14.6σ; “Excess +0.4%”.
  - Tier C:  
    `0.4974 ± 0.000279`, Dev. = 9.5σ; “Excess −0.26%”.

- Check with N = 3,201,160 and p close to 0.5:

  - Binomial σ ≈ \(\sqrt{0.5·0.5/N} = 0.5/\sqrt{3,201,160}\).

    \(\sqrt{3.20116×10^6} ≈ 1.789×10^3\), so  
    σ ≈ 0.5 / 1789 ≈ 2.80×10^-4 = 0.000280.

    The quoted 0.000279 is fine.

  - Deviations in σ:

    - Tier A: fCW − 0.5 = 0.0079.  
      Dev. = 0.0079 / 0.000279 ≈ 28.3σ, close to 28.8; the small discrepancy can be from rounding of σ.

    - Tier B: fCW − 0.5 = 0.004.  
      Dev. = 0.004 / 0.000279 ≈ 14.3σ, close to 14.6.

    - Tier C: fCW − 0.5 = −0.0026.  
      Dev. = −0.0026 / 0.000279 ≈ −9.33σ, close to −9.5.

- These are internally consistent.

- Required fix:
  - None; numbers are consistent.
  - Classification: **OK**.

### P4-E4 — Misstated asymmetry suppression factor

- Location: Sec. IV B, page 4.

- Offending text:

  > “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates the dominance of the equivariant TTA processing.”

- From Table II and earlier:

  - Catalog A excess: +0.79%.  
  - Catalog C excess: −0.26%.
  - In Discussion: they also mention “a classifier CW excess of only 0.79%” as raw Catalog A monopole.

- Now they claim “raw +2.05% to equivariant −0.53%”. Neither of these values appear elsewhere in the text, and they do not match the table. If I try to interpret “2.05% → 0.53%”:

  - Suppression factor = 2.05 / 0.53 ≈ 3.87 → matches the quoted 3.86×.
  - But the actual data in Table II show 0.79% vs 0.26%, giving 0.79 / 0.26 ≈ 3.0, not 3.86.

- This indicates the 2.05% and 0.53% numbers are from some earlier version of the catalog or an internal run and have not been updated when finalizing Table II.

- Required fix:
  - Replace “+2.05% to equivariant −0.53%” and “3.86×” with values derived from the final catalog, e.g. raw +0.79% to equivariant −0.26%, suppression factor ≈3.0.
  - Make sure all stated suppression factors are recomputed from the *published* catalog tiers (A/B/C).
  - Classification: **ESSENTIAL** — they explicitly quantify a key “asymmetry suppression factor” that is numerically inconsistent with their own Table II; this undermines the claimed bias‑reduction scale.

### P4-E5 — Headline σ values consistent but p‑value mapping under‑explained

- Location: Abstract, Sec. IV C, Table I, Table III.

- Claims:

  - “MASTER-deconvolved single-mode pseudo‑C1 on the strict-superset subsample mask (…) yields −0.122σ (500-MC label-shuffle null).”
  - “The real-space post-TTA Catalog C dipole is +0.43σ (p = 0.30, isotropic-null bootstrap, \(N_{\rm MC} = 10,000\)).”
  - Table III first row: C1 = 1.494×10^-6, σnull = 0.429×10^-6, significance −0.122σ.

- Consistency:

  - For −0.122σ: \( (C_{1,\rm meas}-\langle C_{1,\rm null} \rangle)/σ_{\rm null} = (1.494−1.546)/0.429 ≈ −0.052 / 0.429 ≈ −0.121\). That matches −0.122σ.
  - For the real-space dipole, they do not show the bootstrap distribution, but p = 0.30 corresponds to ≈0.52σ in a Gaussian; 0.43σ is reasonable given finite bootstrap noise.

- Required fix:
  - The abstract includes the warning “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I…”. This good practice satisfies your “not directly comparable” requirement.
  - No numerical inconsistency found.
  - Classification: **OK**.

### P4-E6 — Monopole+mask leakage “99.3%” reproduction

- Location: Abstract; Sec. IV D; Table IV.

- Claims:

  - “pre-MASTER raw pseudo‑C1 in the un-monopole-subtracted CW-fraction map … is reproduced at 99.3% of its observed amplitude by a controlled monopole-only generative null (N=500…).”
  - Table IV: pre‑MASTER pseudo‑Cℓ^(ℓ=1) data = 1.696×10^-2; null mean (1.685±0.007)×10^-2.

- Check:

  - Ratio: 1.685 / 1.696 ≈ 0.9945 → 99.45%.
  - They say “99.3%”, which is consistent within stated rounding.

- Required fix:
  - None; the figure is consistent.
  - Classification: **OK**.

### P4-E7 — “+3.64σ (z = Δ/σnull moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent)”

- Location: Abstract; Sec. IV D; Table III/IV; Appendix D.

- Internal consistency:

  - They use two “σ” notions: a z‑score from moment ratio (+3.64σ), and a Gaussian equivalent for the MC rank (pMC = 0.030 ↔ 1.88σ).
  - They explicitly mark pMC as ≈1.9σ Gaussian‑equivalent. That is correct: a one‑sided Gaussian tail of 0.03 corresponds to 1.88σ.

- Conceptual clarity:

  - They should explicitly state in the main text that the +3.64σ is “σnull from the fitted moment ratio, not implied detection significance; the MC rank corresponds to ~1.9σ”.
  - As written, an inattentive reader might confuse +3.64σ with a ≈3.6σ detection, although they later emphasize this is non‑headline and systematics‑attributed.

- Required fix:
  - Add one explicit sentence in Sec. IV D clarifying that +3.64σ is a *z‑score defined from the null variance* and that the *detection significance* against the permutation null is given by pMC (≈1.9σ equivalent).
  - Classification: **MINOR** (clarity, but not a correctness issue).

### P4-E8 — “Fisher Poisson floor at 3σ is ∼0.29% full‑amplitude”

- Location: Sec. VI A.

- They write:

  > “The Fisher Poisson floor at 3σ is ∼0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).”

- Check:

  - For Nspiral = 3.2×10^6, 1σ uncertainty on a *half*-amplitude (A/2) is ≈0.048%; then 3σ on A/2 is 0.144%; so 3σ on *full amplitude A* is ≈0.288% → 0.29% as quoted. The math is consistent.

- Required fix:
  - None.
  - Classification: **OK**.

### P4-E9 — “Disfavors Shamir ∼3% by factor 6–12”

- Location: Abstract, Sec. VI B, Conclusions.

- They claim:

  - Their empirical 50%-recovery-at-3σ threshold is 0.75% amplitude, and they say:
    > “This is inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼ 6–12 under the present pipeline…”
  - Later: 
    > “The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥0.75%… including the Shamir ∼3% amplitude class by a factor of ∼ 6–12.”

- Check:
  - The ratio 3% / 0.75% = 4, not 6–12.
  - To get a factor of 6–12, they might be combining classification dilution factor g ≈ 0.398 (from 69.91% accuracy) so that an underlying 3% signal appears shrunk by g, or vice versa; but they do not show the algebra that yields 6–12.
  - As written, 6–12 is not supported by the numbers:

    - Lower bound: 3% / 0.75% = 4.
    - If they consider 2–4% Shamir range, 2%/0.75% ≈ 2.7, 4%/0.75% ≈ 5.3. Still 2.7–5.3, not 6–12.
    - If they take effective threshold on *true underlying* signal ∼1.88% (after dividing by g), 3%/1.88% ≈ 1.6, still not 6–12.

- Required fix:
  - Either:
    - Remove “by a factor of ∼6–12” entirely, or
    - Provide a clear calculation showing how 6–12 is derived from specific Shamir amplitudes and the classification dilution factor; as it stands, no obvious combination of the stated numbers leads to 6–12.
  - Classification: **ESSENTIAL** — this is a prominent comparative claim about ruling out prior work; the factor is numerically unsupported.

---

## 3. Structural / methodological and wording issues relevant to PRD standards

Even though full figure/table audit is impossible without the actual PDF, the text reveals several issues.

### P4-E10 — Overuse of internal version-history language

- Location: Sec. IV D, Appendix D.

- Offending phrases:

  - “were interpreted in earlier paper versions as mask-geometric leakage…”
  - “A parallel rerun … is in queue for the canonical-mask sensitivity-budget recompute…”
  - “the canonical-mask number” (referring to a particular run with seed 42).
  - “Release tag: v2026.04.” in Data Availability.

- PRD standards:
  - The body of a published paper should not contain references to “earlier paper versions”, “rerun in queue”, or software release tags as if this is a living report.
  - Versioning and pipelines belong in a code/citation, not as forward‑looking comment inside the methods text.

- Required fix:
  - Remove or rewrite all version‑history/log‑like language:
    - Replace “earlier paper versions” by a neutral description of what was once interpreted that way, if truly necessary.
    - Delete “parallel rerun … is in queue”; only describe analyses that have actually been performed.
    - In Data Availability, keep a generic reference to the repository; do not hard‑wire a particular tag unless the intent is that this tag is frozen and archived, in which case frame it as a permanent DOI/archive rather than “v2026.04”.
  - Classification: **MAJOR** — PRD will not accept text that reads like internal development notes in the body.

### P4-E11 — Ambiguous “σ” across different nulls is mostly addressed, but needs stronger signposting at every juxtaposition

- Location: Abstract, Sec. III A, IV, Table I, Appendices.

- Positive:
  - The abstract explicitly states:
    > “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.”
  - Sec. IV begins with:
    > “Significance conventions. This paper reports significance in standard-deviation units (σ) throughout, but values from distinct null procedures are not directly comparable. Section identifiers specify the null for each result.”

  This is a good safeguard.

- However:

  - There are several *juxtapositions* where different σ’s are discussed side‑by‑side without restating non‑comparability, e.g.:

    - Table I lists +0.43, −0.122, +3.64, +1.68, etc., in one row of σ without reminding that they refer to different nulls.

    - Sec. VI “The raw Catalog A dipole (2.31σ real-space; +6.48σ pre-MASTER)… Equivariant averaging collapses the real-space dipole from 2.31σ to 0.43σ; MASTER deconvolution independently collapses the pseudo‑Cℓ to −0.122σ.”  
      This invites the reader to compare the magnitudes of σ across these nulls.

  - Your instruction 7 is strict: if sigma values from different null procedures appear side‑by‑side without explicit “not directly comparable” qualification at *every juxtaposition*, flag ESSENTIAL.

- Required fix:
  - At every place where two or more σ’s from different null procedures are written in the same sentence/table row, add a short parenthetical reminder, e.g.:

    - In Table I caption: “σ values refer to different null procedures and are not directly comparable across rows.”
    - In Sec. VI: “… 2.31σ (real-space null) vs 0.43σ (bootstrap null; not directly comparable) vs −0.122σ (MASTER null; not directly comparable) …”

  - Classification: **ESSENTIAL** — current text warns once, but PRD‑level clarity (and your explicit instruction) requires redundant reminders at every juxtaposition.

### P4-E12 — Abstract over‑promises “quantifiable” monopole-mask leakage explaining prior literature

- Location: Abstract; Sec. VII Conclusions.

- Claims:

  - “A canonical-mask diagnostic … shows … reproduced at 99.3% of its observed amplitude … The post-MASTER canonical-mask direct-MC residual is +3.64σ… The +3.64σ canonical-mask residual is consistent with monopole leakage through survey geometry and is not interpreted as a cosmological signal.”
  - “The prior literature’s pre-MASTER dipole-detection claims are therefore explained at the percent level by this leakage channel under our DESI/ViT-Small pipeline.”

- Problem:

  - Their generative null uses *their own classifier’s* monopole plus *their own canonical mask*. Claiming that this “explains prior literature’s dipole-detection claims” requires:
    - A demonstration that the same mechanism at similar amplitude is present in SDSS/DECaLS/Galaxy Zoo data and in Shamir’s estimator pipeline, not just in DR8+ViT.
  - They do not perform a matched-footprint reanalysis of Shamir’s sample with his pipeline; they even admit in Sec. V A that a likelihood-level exclusion “requires a matched-footprint Ganalyzer reanalysis … not performed here.”

- Required fix:
  - Tone down the conclusion; instead of “are therefore explained,” say something like:
    - “… shows that an analogous monopole+mask leakage mechanism can reproduce pre-MASTER pseudo‑dipole power at the percent level under our pipeline. This suggests that similar leakage could contribute to earlier dipole claims, but a matched-footprint reanalysis would be required to demonstrate this directly.”
  - Classification: **MAJOR** — overstatement of what has been *proved* vs what is *suggested*.

### P4-E13 — Falsification criterion wording

- Location: Abstract, Sec. VII conclusions.

- Claim:

  > “A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null.”

- Problem:

  - This is not strictly correct: a new detection could be due to selection effects, redshift dependence, different galaxy population, or systematic differences in the estimator. “Falsify” is too strong; at best it would be *in tension with* or *inconsistent with* this null under shared assumptions.
  - PRD typically expects careful language around falsification.

- Required fix:
  - Replace “would falsify the present null” by “would be inconsistent with the present null under similar selection and analysis assumptions” or “would put the present null in significant tension”.
  - Classification: **MINOR** (wording, but easy to fix).

### P4-E14 — Data availability links and tags

- Location: Data Availability section.

- Offending text:

  - Explicit URLs (HuggingFace, GitHub) and a moving‑target GitHub repo are cited.
  - “Release tag: v2026.04.”

- PRD practice:
  - Direct URLs are acceptable if stable; but for a permanent record, a DOI and a clearly archived version are preferred.
  - “v2026.04” looks like an internal version. For a journal article, the authors should ensure that the exact version used for the analysis is permanently archived (e.g. Zenodo DOI).

- Required fix:
  - Replace raw URLs and version tags with a statement that the catalog, model weights, and code have been deposited in a long‑term archive with a DOI and that the version used in this paper is the DOI version.
  - Classification: **MINOR** (presentation/archival robustness).

### P4-E15 — Slightly casual or colloquial phrases

- Examples:

  - “signal-hunt diagnostics”, “mask-geometry leakage channel”, “we urge all future chirality studies to adopt comparable bias controls.”
  - For PRD, tone is generally fine but could be made more formal.

- Required fix:
  - Optional stylistic polishing; not required for correctness.
  - Classification: **NIT**.

---

## 4. Length vs claimed contribution

The paper, as presented, is 11 pages including appendices and references. For a methods/data‑analysis paper presenting:

- A new 3.2M spiral chirality catalog on 8.47M galaxies;
- A null dipole result with careful null simulations and MASTER deconvolution;
- A multi‑null diagnostic of a canonical mask residual;

11 pages is entirely reasonable for PRD, not obviously too long.

No reduction in page count is necessary; if anything, clarity about statistical conventions and removal of version‑history language will slightly shorten the text.

---

## Summary recommendation

**MAJOR REVISIONS**

The bibliography and citation metadata are in very good shape, and the core statistical pipeline appears conceptually sound. However, there are several issues that fall short of PRD standards: (1) numerically inconsistent “asymmetry suppression” factors (P4-E4) and unsupported “factor 6–12” exclusion claims (P4-E9) that must be corrected; (2) σ values from distinct null procedures are juxtaposed without local reminders of non‑comparability, contrary to the stated convention and your explicit requirements (P4-E11); and (3) over‑strong claims about explaining prior literature and “falsification” that are not strictly justified by the presented analysis (P4-E12, P4-E13). In addition, version‑history/internal‑log language needs to be removed from the body (P4-E10). Once these essential and major issues are resolved, the manuscript could be suitable for PRD, but not before.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E21 — Arithmetic inconsistency in Fisher-floor sensitivity estimate (MAJOR)

- Location: Sec. VI A, first paragraph.
- Text:  
  “The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at \(N_{\rm spiral} = 3,201,160, f_{\rm sky} = 0.46\)).”
- Check:
  - For a *dipole* estimated from \(N\) independent spirals with an effective sky fraction \(f_{\rm sky}\), the binomial RMS on the *half-amplitude* \(A/2\) is roughly
    \[
    \sigma(A/2) \simeq \sqrt{\frac{0.5 \cdot 0.5}{N_{\rm eff}}} = \frac{0.5}{\sqrt{N_{\rm eff}}}, \quad N_{\rm eff} \sim N_{\rm spiral} f_{\rm sky}.
    \]
  - Using the paper’s own numbers, \(N_{\rm spiral} = 3{,}201{,}160\) and \(f_{\rm sky} = 0.46\):
    \[
    N_{\rm eff} \approx 3.20116\times 10^6 \times 0.46 \approx 1.47\times 10^6,
    \]
    so
    \[
    \sigma(A/2) \approx \frac{0.5}{\sqrt{1.47\times 10^6}} \approx \frac{0.5}{1212} \approx 4.1\times 10^{-4} = 0.041\%.
    \]
  - A 3σ *full* amplitude threshold is \(A_{3\sigma} \approx 3 \times 2 \times \sigma(A/2) \approx 6 \times 0.041\% \approx 0.25\%\), not 0.29%.
  - Conversely, starting from σ(A/2) = 0.048% implies
    \[
    N_{\rm eff} = \left(\frac{0.5}{0.00048}\right)^2 \approx 1.08\times 10^6,
    \]
    which is inconsistent with the simultaneous statement \(N_{\rm spiral} = 3{,}201{,}160, f_{\rm sky} = 0.46\) (that product is ≈1.47×10^6, not 1.08×10^6).
- Diagnosis:
  - The quoted σ(A/2) = 0.048% and the resulting 3σ amplitude 0.29% do not match the stated \(N_{\rm spiral}\) and \(f_{\rm sky}\); they appear to come from an earlier \(N\) or different \(f_{\rm sky}\).
- Required fix:
  - Recompute σ(A/2) and the 3σ full-amplitude floor directly from the *final* \(N_{\rm spiral}\) and \(f_{\rm sky}\), and update both 0.048% and 0.29% accordingly.
  - Alternatively, if 0.048% and 0.29% are kept, explicitly state the effective \(N_{\rm eff}\) they are based on and ensure consistency with the numbers in the same sentence.
  - Classification: **MAJOR** (headline sensitivity calibration; affects all “Fisher floor” comparisons).

---

P4-E22 — Arithmetic inconsistency in GZ1-dilution “true-underlying threshold ∼1.88%” (MAJOR)

- Location: Sec. VI A, last sentence of first paragraph.
- Text:  
  “The empirical injection-recovery sweep … gives \(P(\sigma > 3) = 0.55\) at \(A = 0.75\%\)… The headline empirical 50%-recovery-3σ threshold is therefore \(A \approx 0.75\%\), above the Fisher floor due to classification noise (GZ1-dilution factor \(g = 2a − 1 ≈ 0.398\) for \(a = 0.6991\), giving a true-underlying threshold ∼ 1.88%).”
- Check:
  - They define \(g = 2a−1\) with a = 0.6991, so
    \[
    g = 2\times 0.6991 - 1 = 1.3982 - 1 = 0.3982 \ (\text{≈ 0.398, consistent}).
    \]
  - If the *observed* amplitude is diluted by \(g\), then the *true* underlying amplitude is \(A_{\rm true} = A_{\rm obs}/g\).
  - With \(A_{\rm obs} = 0.75\%\) and \(g \approx 0.398\):
    \[
    A_{\rm true} \approx \frac{0.75\%}{0.398} \approx 1.885\%,
    \]
    matching the stated “∼1.88%.”
  - However, this logically contradicts the earlier framing of 0.75% as a *full-amplitude* threshold on the *underlying* dipole used in injections. If the injected signal in the HC-spiral sample is implemented at catalog level (after classification), then 0.75% is already the *true* dipole amplitude in the field actually analyzed; applying an additional factor of 1/g double-counts the dilution.
- Diagnosis:
  - The arithmetic A_true ≈ 0.75% / 0.398 ≈ 1.88% is correct, but the conceptual mapping between “injected amplitude” and “underlying physical amplitude” is not clearly defined. As written, the text can be read as:
    - 0.75% is both the injected, catalog-level amplitude and the “headline empirical threshold”; and
    - 1.88% is a second, larger “true-underlying threshold.”
  - Without an explicit statement that the injections are at *catalog* level and that 0.75% therefore does *not* require further scaling by g, readers will misinterpret 1.88% as the correct minimum detectable physical amplitude, overstating the required true signal by ≈2.5×.
- Required fix:
  - Explicitly specify whether the injection amplitude A is defined:
    - (a) at the *catalog field* level (i.e., after classification noise), in which case 0.75% is already the physical threshold and 1.88% should be removed, or
    - (b) at the *true spin* level before classification noise, in which case the MC injection procedure must be clearly described as applying a reduced amplitude A·g at catalog level.
  - Align all occurrences of “threshold” to a single, consistently defined quantity; avoid presenting both 0.75% and 1.88% as thresholds without a clear hierarchy.
  - Classification: **MAJOR** (affects interpretation of empirical sensitivity and comparison to prior claimed amplitudes).

---

P4-E23 — Arithmetic and interpretation ambiguity in “factor of ∼6–12” discrepancy with Shamir (MAJOR)

- Locations:
  - Abstract, end of first paragraph of Discussion (embedded):  
    “This is inconsistent in amplitude with Shamir’s claimed ∼ 3% signal by a factor of ∼ 6–12 under the present pipeline…”
  - Sec. VI B, last sentence:  
    “The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥ 0.75%… including the Shamir ∼ 3% amplitude class by a factor of ∼ 6–12.”
- Check:
  - The paper adopts an empirical 50%-recovery 3σ *observed* threshold A_obs ≈ 0.75%.
  - Shamir’s per-bin asymmetries are quoted as ∼3% (middle of the 2–4% or 5–20% ranges elsewhere).
  - Straightforward amplitude ratios:
    - \(3\% / 0.75\% = 4\),
    - \(2\% / 0.75\% \approx 2.67\),
    - \(4\% / 0.75\% \approx 5.33\).
  - None of these yield a factor in the range 6–12.
  - If the authors combine the 1.88% “true-underlying threshold” with Shamir’s 2–4%:
    - \(2\% / 1.88\% \approx 1.06\),
    - \(3\% / 1.88\% \approx 1.6\),
    - \(4\% / 1.88\% \approx 2.1\),
    again not 6–12.
- Diagnosis:
  - The “6–12” factor does not follow from any straightforward combination of:
    - the stated sensitivity floor 0.75%,
    - the back-calculated 1.88%,
    - Shamir’s 2–4% asymmetries.
  - This suggests that “6–12” is a stale number from an earlier draft with different thresholds or Shamir amplitude interpretation, not updated when the injection study and 0.75% threshold were finalized.
- Required fix:
  - Recompute the discrepancy factor using the final, clearly defined amplitude threshold and the actual amplitude range of Shamir’s claims cited in this paper.
  - Either:
    - replace “∼6–12” with a correctly calculated factor (likely ∼3–5, depending on which threshold is adopted), or
    - remove the factor entirely and simply state the numerical comparison (e.g., “our 0.75% sensitivity is below Shamir’s ∼2–4% class”).
  - Classification: **MAJOR** (misstates the strength of the constraint on prior claimed signals).

---

P4-E24 — Catalog-tier asymmetry example uses stale “2.05% → −0.53%” numbers (ESSENTIAL — arithmetic + narrative)

- Location: Sec. IV B, middle paragraph; also in your earlier review but with an additional nuance here.
- Text:  
  “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates the dominance of the equivariant TTA processing.”
- Newly emphasized issues:
  - From Table II (final catalog):
    - Catalog A excess: +0.79%.
    - Catalog C excess: −0.26%.
    - Suppression factor based on those: \(0.79 / 0.26 ≈ 3.0\), not 3.86.
  - The signs and magnitudes quoted (+2.05% to −0.53%) are not present anywhere else; they are incompatible with the table and with the headline claim that the *equivariant* catalog monopole is −0.26%.
  - Using +2.05% and −0.53% implies a raw excess of 2.05% and a residual of 0.53%, a much stronger bias and a somewhat weaker suppression relative to the actual catalog.
- Required fix (expanded):
  - Replace both amplitudes and suppression factor with values derived strictly from the finalized Table II numbers.
  - Align the sign convention (whether “Excess” is CW–CCW or |CW–CCW|) consistently with Table II.
  - Ensure no other section (e.g., Discussion, Appendix B) uses these earlier 2.05%/0.53% values.
  - Classification: **ESSENTIAL** (internal numerical contradiction in the key narrative about bias reduction).

---

P4-E25 — Incomplete specification of z-score definitions in Table III (MINOR but clarity-critical for σ comparability)

- Location: Table III caption and Sec. IV C–D.
- Issue:
  - Table III lists “Significance (σ)” values for each bandpower, e.g. +6.097, +2.232, etc., but the caption only says “Significance (σ)” with no explicit reminder that σ is computed as \((C_{\ell,\rm meas} - \langle C_{\ell,\rm null}\rangle)/\sigma_{\rm null}\) from the *bandpower-specific* null.
  - In the text they are careful elsewhere: the abstract and Sec. IV state that σ values are null-specific and not directly comparable. However, the table itself is where a reader most easily forgets this and treat σ as a detection significance.
- Required fix:
  - Add a one‑line note in the Table III caption such as: “Significance (σ) is defined as \((C_{\ell,\rm meas} - \langle C_{\ell,\rm null}\rangle)/\sigma_{\rm null}\) for each row’s null; these σ values are not directly comparable to σ from other estimators in this paper.”
  - This change directly enforces the “σ non-comparability” caveat at the point of use.
  - Classification: **MINOR** (clarity; reduces risk of misinterpretation).

---

P4-E26 — Dimensional consistency ambiguity in definition of Ap and subsequent use (NIT, but worth tightening)

- Locations:
  - Eq. (3) defining \(A_p\).
  - Appendix A, “Field: scalar (spin-0) asymmetry map.”
- Issue:
  - Eq. (3) defines \(A_p\) as
    \[
    A_p = \frac{N^{(p)}_{\rm CW} - N^{(p)}_{\rm CCW}}{N^{(p)}_{\rm CW} + N^{(p)}_{\rm CCW}},
    \]
    a dimensionless fraction.
  - Appendix A then describes the field used in NaMaster as
    \[
    A_p = \frac{N^{(p)}_{\rm CW} - N^{(p)}_{\rm CCW}}{N^{(p)}_{\rm CW} + N^{(p)}_{\rm CCW}},
    \]
    but also introduces a galaxy-weighted mask mean subtraction \(\langle A \rangle_{\rm mask,gw}\) and Wp = N_all as the weight. The notation Ap and the use of pglobal_CW later in the monopole-only null description blur the distinction between:
    - the *local asymmetry* field Ap; and
    - the *global monopole* pglobal_CW.
  - Dimensional units are consistent (all are pure numbers), but the semantics are easy to confuse in the generative null paragraph (the earlier “Binomial(ntotal, pglobal_CW)” vs “Binomial(Nspiral(p), pglobal_CW)”) where “total” could mean different N’s.
- Required fix:
  - Introduce distinct symbols for:
    - the global CW fraction \(p_{\rm CW}^{\rm global}\), and
    - the local asymmetry field \(A_p\).
  - In the generative null description, explicitly write “Binomial(N_spiral(p), p_CW^global)” and avoid “ntotal” language.
  - Classification: **NIT** (no numerical error, but avoids dimensional/semantic confusion between different uses of “p” and “A”).

---

P4-E27 — Abstract claim “factor of ∼6–12” not clearly supported in body (ABSTRACT FAITHFULNESS, MAJOR overlap with P4-E23)

- Location: Abstract, final sentences of the introduction-like paragraph in the abstract section.
- Issue:
  - The abstract states that the null is “inconsistent in amplitude with Shamir’s claimed ∼3% signal by a factor of ∼6–12.”
  - As detailed in P4-E23, no place in the body *computes* or demonstrates this 6–12 factor quantitatively; the body only reports:
    - the 0.75% empirical threshold,
    - the 1.88% back-calculated “true underlying” number,
    - Shamir’s 2–4% range.
  - There is no explicit equation, figure, or table supporting “6–12,” nor any exploration of how that factor depends on the null choice or the classification-noise model.
- Required fix:
  - Either:
    - (a) add explicit derivation in Sec. VI B showing exactly how “6–12” is computed (including any assumptions about dilution and survey footprint), and ensure the arithmetic is correct; or
    - (b) remove “6–12” from the abstract, replacing it with a statement directly backed by the body (e.g., “our 0.75% sensitivity is below Shamir’s ∼2–4% claimed amplitude class”).
  - Classification: **MAJOR** (abstract currently over-quantifies the level of disagreement in a way that is not transparently derivable from the body text).

---

If you want, I can next go through each figure systematically (once you provide the figure captions or images) to check the Figure–body claims (class B) and equation-by-equation dimensional consistency (class C) in more detail.