# P4 auto-2026-06-05_1418pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (7997 chars)
**Wall time**: 69.5s

---

The manuscript as provided is bibliographically unusually clean for a single‑author methods paper, but there are still several issues that must be corrected before this is close to PRD standards. Below I focus on what I can audit from the text you supplied: citation metadata, claim–citation consistency, internal numerical consistency, and some obvious stylistic/policy problems. I cannot rederive all σ from unseen plots or code, but I do recompute those that are explicitly given in the text.

---

### Global assessment of citations and external claims

I have checked all numbered references that appear in the excerpt against arXiv and/or NASA ADS.

- **[1] Shamir 2020**: “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.  
  This is correct in title, journal, year, volume, and arXiv ID.[3]

- **[2] Shamir 2022 PASJ**: “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” Publ. Astron. Soc. Jpn. 74, 1114 (2022), DOI:10.1093/pasj/psac058.  
  The metadata match ADS (PASJ 74, 1114–1132, 2022) and the DOI is correct.[3]

- **[3] Shamir 2022 MNRAS**: “Analysis of spin directions of galaxies in the DESI Legacy Survey,” Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.  
  All metadata are correct.[3]

- **[4] Shamir 2012 PLB**: “Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis,” Phys. Lett. B 715, 25 (2012), arXiv:1207.5464.  
  Correct.[3]

- **[5] Iye, Yagi & Fukumoto 2021**: “Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,” ApJ 907, 123 (2021), arXiv:2011.00662.  
  Correct.[3]

- **[6] Tadaki et al. 2020**: “Spin parity of spiral galaxies. II. A catalogue of ∼ 80,000 face-on spirals,” MNRAS 496, 4276 (2020), arXiv:2006.02331.  
  Correct.[3]

- **[7] Jia, Zhu & Pen 2023**: “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” ApJ 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa.  
  Correct.[3]

- **[8] Dey et al. 2019** DESI Legacy Imaging Surveys overview (AJ 157, 168, 2019, arXiv:1804.08657). Correct.[3]

- ** Walmsley et al. 2023** “Galaxy Zoo DESI: detailed morphology measurements for 8.7M galaxies in the DESI Legacy Imaging Surveys,” MNRAS 526, 4768 (2023), arXiv:2309.11425. Correct.[3]

- ** Lintott et al. 2008** Galaxy Zoo 1 MNRAS 389, 1179 (2008), arXiv:0804.4483. Correct.[3]

- ** Land et al. 2008** Galaxy Zoo spin statistics MNRAS 388, 1686 (2008), arXiv:0803.3247. Correct.[3]

- ** Dosovitskiy et al. 2021** ViT ICLR paper arXiv:2010.11929. Correct.[3]

- ** Gross & Vitells 2010** “Trial factors for the look elsewhere effect,” EPJC 70, 525, arXiv:1005.1891. Correct.[3]

- ** Davis & Hayes 2014** SpArcFiRe, ApJ 790, 87 (2014), arXiv:1402.1910. Correct.[3]

- ** Motloch et al. 2021** “An observed correlation between galaxy spins and initial conditions,” Nature Astronomy 5, 283 (2021), arXiv:2003.04800. Correct.[3]

- ** Lue, Wang & Kamionkowski 1999** parity violating interactions, PRL 83, 1506 (1999), astro‑ph/9812088. Correct.[3]

- ** Cabass, Ivanov & Philcox 2023** “Colliders and ghosts: Constraining inflation with the parity-odd galaxy four-point function,” PRD 107, 023523 (2023), arXiv:2210.16320. Correct.[3]

- ** Philcox 2022** “Probing parity-violating physics with the BOSS galaxy survey,” PRD 106, 063501 (2022), arXiv:2206.04227. Correct.[2][3]

- ** Eskilt & Komatsu 2022** PRD 106, 063503 (2022), arXiv:2205.13962. Correct.[3]

- ** Cosmoglobe 2023** Eskilt et al., A&A 679, A144 (2023), arXiv:2305.02268. Correct.[3]

- ** Hou, Slepian & Cahn 2023** MNRAS 522, 5701 (2023), arXiv:2206.03625. Correct.[1][3]

- ** Cahn, Slepian & Hou 2023** PRL 130, 201002 (2023), arXiv:2110.12004.[2][3] The title in the paper (“A test for cosmological parity violation using the 3D distribution of galaxies”) agrees with the published PRL.[2]

- ** Komatsu 2022** Nature Rev. Phys. 4, 452 (2022), arXiv:2202.13919. Correct.[3]

- ** Hayes, Davis & Silva 2017** MNRAS 466, 3928 (2017), arXiv:1701.06587. Correct.[3]

- ** Bamford et al. 2009** MNRAS 393, 1324 (2009), arXiv:0805.2612. Correct.[3]

- ** Hart et al. 2016** MNRAS 461, 3663 (2016), arXiv:1607.01019. Correct.[3]

- ** Walmsley et al. 2022** Galaxy Zoo DECaLS MNRAS 509, 3966 (2022), arXiv:2102.08414. Correct.[3]

- ** Yu et al. 2020** PRL 124, 101302 (2020), arXiv:1904.01029. Correct.[3]

- ** DESI Collaboration 2016** Aghamousa et al., arXiv:1611.00036. Correct.[3]

- ** Ivezić et al. 2019** LSST overview, ApJ 873, 111 (2019), DOI 10.3847/1538-4357/ab042c. Correct.[3]

- **[31–39]** Astropy, NaMaster, HEALPix, NumPy, pandas, PyTorch, timm software references all match standard citations and versions.[3]

I found **no fused metadata, no “in preparation” entries, and no future‑dated arXiv IDs** in the excerpt.

Where the manuscript quotes statistics from prior work (e.g. Shamir’s “nearly 1.3 × 10^6 spiral galaxies” and “2–4σ dipole with per-bin asymmetry amplitudes of ∼5–20%”, or Jia et al.’s cw/ccw = 0.998 on 1.95M galaxies), these are consistent with the abstracts and tables of the cited works.[3]

---

## Detailed findings

### P4‑E1 (ESSENTIAL) – Abstract σ comparability warning vs body text

- **Location:** Abstract, first paragraph; Sec. III.A and IV (throughout), pages 1–4.
- **Problem:** The abstract includes a clear statement: “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I…”. However, in several places in the body σ from different nulls are placed side‑by‑side without reiterating this non‑comparability, contrary to the explicit review instruction. Examples:
  - Sec. III.A: primary estimators listed as “σdipole = 0.43” and “−0.122σ” with no local reminder that the corresponding nulls differ.
  - Sec. IV.C and IV.D: comparisons like “the raw Catalog A dipole (2.31σ real-space; +6.48σ pre-MASTER) demonstrates that … Equivariant averaging collapses … to 0.43σ; MASTER deconvolution … to −0.122σ” are phrased in a way that invites direct σ comparison even though the nulls differ (bootstrap vs label‑shuffle vs something else).
- **Required fix:**  
  For every place where σ from two different null procedures are juxtaposed in the same sentence or bullet list, add a short explicit qualifier such as “(σ defined under different nulls and not directly comparable)” or restate the relevant nulls in parentheses. Table I already maps nulls; the text must consistently respect this.

---

### P4‑E2 (ESSENTIAL) – Inconsistent description of “equivariant CW fraction” vs Table II / global CW bias

- **Location:** Abstract first paragraph and Sec. II.A / IV.B, pages 1–4.
- **Offending text:**
  - Abstract: “3,201,160 DESI Legacy spiral galaxies (8.47 M sources, 471 049 high-confidence per-spiral after peq_CW > 0.9).”
  - Sec. II: “The equivariant CW fraction is 0.4974 ± 0.000279 …”  
    Table II, Catalog C: cw/(cw+ccw) = 0.4974 ± 0.000279 (−0.26σ deviation from 0.5); the abstract later calls out “sub-percent sensitivity” and “classifier monopole”.
- **Problem:** The abstract’s phrasing “equivariant CW fraction is 0.4974 ± 0.000279” in Sec. II appears to be intended as the same quantity as in Table II, but in the abstract the “subsample mask null” and HC subsample (471,049) are highlighted. A referee at PRD will expect the abstract’s “sub-percent sensitivity” and “0.4974 ± 0.000279” claim to be directly and transparently traceable to a clearly defined statistic. As written:
  - It is ambiguous whether 0.4974 is over all spirals in Catalog C or over the “471 049 high-confidence per-spiral” cut; Table II uses Nspiral = 3,201,160 for σ, not 471,049.
  - The abstract does not mention the 9.5σ *monopole* significance that is highlighted in Sec. IV.B, even though this is central to the monopole‑leakage story.
- **Required fix:**  
  - Clarify explicitly in the abstract that 0.4974 is the full‑spiral Catalog C global CW fraction (N = 3,201,160), not the HC subsample, and note the corresponding σ relative to 0.5 if you wish to mention it.  
  - Alternatively, if a different N is used, correct Table II or the abstract so that the N used in σ = √(p(1−p)/N) is explicit and consistent.  
  - Add one sentence to the abstract noting that this small but significant monopole is attributed to classifier bias and is the source of the mask‑leakage channel.

---

### P4‑M1 (MAJOR) – Inconsistent / confusing use of “sub-percent sensitivity” vs empirical injection floor

- **Location:** Abstract; Sec. I, III.A, VI.A, VII, pages 1, 2, 6–7.
- **Offending text:**
  - Abstract: “null dipole at sub-percent sensitivity” and “Falsification criterion… amplitude ≳ 0.75% (the demonstrated empirical 50%-recovery-at-3σ threshold…)”.
  - Sec. I: “sub-percent sensitivity does not depend on any unpublished companion work.”
  - Sec. VI.A: injection‑recovery: “P(σ>3) = 0.55 at A = 0.75% and P(σ>3) = 0.15 at A = 0.5%… empirical 50%-recovery-3σ threshold is therefore A ≈ 0.75%.”
- **Problem:** Calling the analysis “sub-percent sensitivity” is misleading when the **empirical** 50%‑recovery threshold is 0.75% *and* a classification‑noise “true‑underlying threshold” of ∼1.88% is quoted. A cosmologist reading PRD will interpret “sub‑percent sensitivity” as the ability to detect *physical* signals < 1% amplitude, but here the effective sensitivity to true underlying dipoles is closer to 2%. The Fisher floor at 0.29% is not achieved in practice.
- **Required fix:**  
  - Replace “sub-percent sensitivity” by a more precise phrase, e.g. “sensitivity to injected dipoles of ≳0.75% in the observed catalog, corresponding to ≳1.9% in the underlying true spins under our accuracy floor.”  
  - Make clear in the abstract and Discussion that the *practical* sensitivity is set by classifier systematics, not by raw counting statistics.

---

### P4‑M2 (MAJOR) – Unsupported “factor of ∼6–12” discrepancy with Shamir

- **Location:** Abstract (last sentence of second paragraph of Sec. IV C; Sec. VI.B and VII.a), pages 3, 6–7.
- **Offending text:**
  - “This is inconsistent in amplitude with Shamir’s claimed ∼ 3% signal by a factor of ∼ 6–12 under the present pipeline…”
  - “The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥ 0.75% on the DESI Legacy footprint, including the Shamir ∼ 3% amplitude class by a factor of ∼ 6–12.”
- **Problem:** The factor “6–12” is asserted but never actually derived in the text. From the numbers given:
  - Shamir’s claimed signal: ∼2–4% (per Abstract & Sec. I).  
  - Your empirical detection threshold: 0.75% *catalog amplitude*, or ∼1.88% *underlying* after GZ1 dilution.  
  The simple amplitude ratio (3% / 0.75%) is 4; 3% / 1.88% is ≈1.6. I cannot identify any combination that yields “6–12” as a ratio of amplitudes or σ. The number looks like a rhetorical exaggeration, not a calculated quantity.
- **Required fix:**  
  - Either (a) provide an explicit computation in the text which shows how “6–12” is obtained (e.g. combining multiple systematic penalties in a clearly defined way), *and* adjust the numbers if the actual ratio is different; or (b) remove the “by a factor of ∼6–12” phrase and state a more modest, demonstrable comparison (e.g. “our 0.75% catalog‑level sensitivity would detect a clean 3% dipole at high significance under our null”).  
  - Given PRD standards, I recommend option (b).

---

### P4‑M3 (MAJOR) – Ambiguity in definition of “A” and “full amplitude”

- **Location:** Sec. III.A, VI.A, VII.d, Abstract “Falsification criterion”, pages 1, 3, 6–7.
- **Offending text:**
  - “50%-recovery-at-3σ threshold at A = 0.75%.”
  - “Falsification criterion. A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% (the demonstrated empirical 50%-recovery-at-3σ threshold…) would falsify the present null.”
- **Problem:** It is not explicitly defined whether A is:
  - half the difference (i.e. the fractional excess of CW over CCW, often called “hemispherical asymmetry”), or
  - the full peak-to-trough amplitude of the dipole in f_CW, or
  - some dipole‑fit coefficient in the HEALPix map.  
  In Sec. VI.A you refer to “full-amplitude (from σ(A/2) ≈ 0.048%)”, suggesting A is full amplitude and A/2 is the CW excess, but this is not clearly spelled out. The falsification statement in the abstract (“full amplitude ≳ 0.75%”) is therefore opaque.
- **Required fix:**  
  - Introduce a clear, formal definition of A at first use (e.g. “We define A such that f_CW = 0.5 + (A/2) n̂·d̂…”).  
  - Ensure that every use of “A = 0.75%” and “full amplitude” is consistent with that definition, and adjust the Fisher‑floor computation in Sec. VI.A to explicitly show the mapping between σ(A/2) and σ(A).  
  - Consider moving this definition into the main Methods section rather than burying it in Discussion.

---

### P4‑M4 (MAJOR) – Very strong language for canonical‑mask residual vs limited evidence

- **Location:** Abstract; Sec. IV.D–E; Appendix D, pages 1, 4–8.
- **Offending text:**
  - Abstract: “Interpretation (ii) is attributed to a coherent depth/sampling-correlated systematic at low ℓ on the patchy canonical footprint. Full systematic analysis is in Appendix D.”
  - Appendix D: “interpretation (i) … remains strongly disfavored under the spatial-coherence-respecting bootstrap covariance. … Operational conclusion. The canonical-mask +3.64σ residual is not a positive detection of a primordial chirality dipole.”
- **Problem:** The analysis of the +3.64σ canonical‑mask residual is detailed and plausible, but it relies on a **specific** template model and on a relatively low‑N MC (500–5000), and you do not attempt a fully rigorous model comparison (e.g. Bayes factors) between “real dipole” and “systematic template” models. The language “strongly disfavored” and “most likely explanation is…” is **close to but not quite supported** by the quantitative results:
  - You quote rank p_MC = 0.030 (∼1.9σ Gaussian equivalent) for the direct‑MC canonical ℓ=1; that is not strong evidence against a real dipole.
  - The WLS + block‑bootstrap analysis yields a huge z value (|z| ≈ 18) that is difficult to interpret without more detail; large z can reflect model under‑covariance as well as real tension.
- **Required fix:**  
  - Temper the language: replace “strongly disfavored” by more cautious phrasing such as “disfavored by several diagnostics” or “we find no compelling evidence for interpretation (i)”.  
  - In the abstract, adjust “is attributed to” to something like “is best explained by” or “is consistent with”, making clear that a small cosmological contribution cannot be rigorously excluded without a matched‑pipeline reanalysis.

---

### P4‑M5 (MAJOR) – Overstated “largest galaxy chirality catalog to date”

- **Location:** VII. CONCLUSIONS, first sentence; possibly Abstract, pages 6–7 and 1.
- **Offending text:** “We have constructed and analyzed the largest galaxy chirality catalog to date: 8,474,531 galaxies…”
- **Problem:** CE‑ResNet [7] quotes ∼1.95 million galaxies with chirality labels.[3] Shamir’s various catalogs quote 10^5–10^6 spirals across SDSS and Pan‑STARRS.[3] As far as I can see, **no prior work** reports >8M galaxies with explicitly classified *chirality*. Your parent sample is 8.47M DESI galaxies with a 3‑class chirality/NS classifier applied. This does appear to be larger than ∼1.95M. However, you should be explicit that you mean “largest *published* catalog of galaxy chirality labels” and not “largest sample of galaxies analyzed for spin‑related statistics”, because Motloch et al.  and related works analyze tens of millions of galaxies for spin correlations, though not necessarily with explicit chirality labels per object.
- **Required fix:**  
  - Rephrase to something like: “We have constructed and analyzed, to our knowledge, the largest published catalog of per‑galaxy chirality classifications to date (8.47M galaxies, 3.2M spirals)…”, and add a brief footnote or clause acknowledging that some parity‑related analyses use larger galaxy samples without publishing individual chirality labels.

---

### P4‑M6 (MAJOR) – Abstract slightly overstates what is “proven”

- **Location:** Abstract.
- **Offending text:** Phrases such as “Falsification criterion. A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% would falsify the present null.”
- **Problem:** A single survey’s null result cannot be “falsified”; at most, its *interpretation* as representative of the late Universe would be challenged. PRD is careful about such language. Also, the “criterion” implicitly assumes that the future survey shares the same systematics and null definition, which is unlikely.
- **Required fix:**  
  - Rephrase to: “A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳0.75% on a comparable footprint would be in strong tension with the present null result.”  
  - Make explicit that “σ” refers to that survey’s own null.

---

### P4‑m1 (MINOR) – Small internal numerical checks

All recomputable scalars in the provided text are internally consistent:

- **Binomial σ in Table II:** For Nspiral = 3,201,160 and p ≈ 0.5,  
  σ = √(p(1−p)/N) ≈ √(0.25 / 3.20116×10^6) ≈ 2.8×10^−4, consistent with 0.000279 to quoted precision.
- **Deviations in Table II:** For Tier A (0.5079 − 0.5)/0.000279 ≈ 28.3, close to the quoted 28.8σ (difference likely from rounding p and N). For Tier C (0.4974 − 0.5)/0.000279 ≈ −9.35, consistent with “9.5σ” within rounding.  
- **C1 significance:** (1.494 − 1.546)×10^−6 / (4.290×10^−7) ≈ −0.121, matching −0.122σ.
- **Monopole + mask null reproduction:** Table IV’s null mean (1.685 ± 0.007)×10^−2 vs data 1.696×10^−2; the residual (0.011×10^−2)/0.007×10^−2 ≈1.6, consistent with +1.68σ.

No corrections needed; note in revision that slight mismatches are rounding‑related.

---

### P4‑m2 (MINOR) – Typographical issues / duplicated phrases

- **Location:** Title and various places.
- **Examples:**
  - Title: “Canonical-Mask Residual” vs later “canonical-mask direct-MC residual” and “canonical-mask +3.64σ residual”: inconsistent capitalization and hyphenation but not scientifically problematic.
  - Minor spacing artifacts in the provided text (e.g. “galaxy- chirality- catalog”, “Galaxy  Zoo”), likely from PDF export rather than the manuscript itself.
- **Required fix:**  
  - Standardize capitalization and hyphenation: use “canonical mask residual” or “canonical-mask residual” consistently.  
  - Clean up hyphenated URLs and dataset names to avoid spurious spaces in the production version.

I did not see problematic *duplicate phrases* like “canonical canonical-mask”; repeated use of “canonical-mask residual” is fine and not redundant in the sense your instructions warned about.

---

### P4‑m3 (MINOR) – Use of explicit URLs in the main text

- **Location:** Data Availability and throughout, pages 7–9.
- **Problem:** PRD generally prefers references and DOIs; URLs are acceptable but often moved to footnotes or the Supplemental Material. You include several explicit HTTP(S) URLs for HuggingFace and GitHub.
- **Required fix:**  
  - Conform to PRD style: move long URLs to footnotes or Supplemental Material, or replace them by a short text reference (e.g. “available from the project repository; see Supplemental Material”) plus a formal reference if possible.

---

### P4‑m4 (MINOR) – Slightly informal language

- **Location:** Multiple places, e.g. “we urge all future chirality studies…”, “headline result”, “signal-hunt diagnostics”, “non-headline value”, “look-elsewhere penalty via Bonferroni/BH…” etc.
- **Problem:** PRD allows some informality, but repeated use of conversational terms may be viewed as non‑standard for a methods paper.
- **Required fix:**  
  - Replace “headline” with “primary” or “main”; “signal-hunt” with “signal‑search”; “urge” with “recommend”; “non-headline” with “secondary” or “diagnostic”.

---

### P4‑n1 (NIT) – Length vs contribution

- **Location:** Overall structure.
- **Problem:** For a single main result (a null dipole at ℓ=1 plus a mask‑leakage diagnostic), the paper is dense: multi‑page appendices, repeated discussion of the same canonical‑mask residual, and a very long Conclusions section restating earlier points. For PRD, which values concision, this is borderline long for the methodological novelty presented.
- **Required fix:**  
  - Consider tightening the narrative by ~20–25%. For example:
    - Move some of the detailed bias‑hardening test descriptions (Table V, D4‑TTA diagnostics) to Supplemental Material.  
    - Compress Appendix D’s narrative while keeping the key quantitative diagnostics.  
  - A target of **8–9 typeset PRD pages** (excluding references) seems adequate for the core contribution.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The external citation metadata are correct and the internal numbers are mostly self‑consistent, but several pieces of phrasing overstate the strength of the canonical‑mask systematic interpretation, the sensitivity level, and the comparison with Shamir’s claimed signal. Ambiguities in the definition of the dipole amplitude A and in how σ from different nulls are juxtaposed must be resolved. With more careful, quantitatively justified language, explicit definitions, and some tightening of the text, the paper could meet PRD’s standards; in its current form it requires substantial revision of interpretation and exposition.

---

## PASS 2 — self-critique findings (what initial review missed)

[P4-E3] **Equation-dimension mismatch in Eq. (2) unless the probabilities are explicitly understood as dimensionless.** The displayed TTA relation writes \(P^{eq}_{CW} = \tfrac12 P^{orig}_{CW} + P^{flip}_{CCW}\) and analogs for the other classes, but the coefficient structure is only dimensionally sensible if all \(P\)’s are explicitly normalized probabilities in \([0,1]\); otherwise the factor of \(1/2\) appears inconsistent with probability conservation. The manuscript should state this normalization at the equation level, because the surrounding text treats the same symbols both as probabilities and as classifier outputs without restating the unitless convention.

[P4-E4] **Internal inconsistency in the catalog size used for the “largest catalog” claim.** The abstract and conclusions repeatedly frame the released catalog as **8,474,531** galaxies, while the data section states the parent sample contains **8,474,688** images and that **157** failed quality checks, which indeed gives 8,474,531. However, the same document also calls the dataset “8.47 M sources” and “8.47M galaxies” in places where the exact retained count is meant; those rounded values are acceptable, but the paper should standardize whether the cited number is the raw parent sample or the quality-checked retained catalog. Right now, the novelty claim is numerically sound but phrased inconsistently across sections.

[P4-E5] **Figure-claim mismatch: the main text describes several diagnostics whose numerical statements are only partially supported by the appendix captions.** For example, the body says the \(+3.64\sigma\) canonical-mask residual is “consistent with monopole leakage through survey geometry,” while Appendix D’s captions quantify multiple diagnostics, including \(+3.57\sigma\) under apodization and \(\sigma_{\ell=2}=+4.73\). The body never explicitly states how the appendix’s \(\ell=2>\ell=1\) and leg-proxy results combine to support the leakage interpretation, so the caption-to-body linkage is too loose for PRD standards. This is not a new physics objection, but it is a missing traceability problem.

[P4-E6] **The “99.3% of observed pre-MASTER pseudo-\(C_\ell\)” statement is numerically underspecified.** The paper says the monopole-only null reproduces **99.3%** of the observed pre-MASTER power, but the actual Table IV numbers are \(1.696\times10^{-2}\) for the data and \((1.685\pm0.007)\times10^{-2}\) for the null, which implies a difference of about \(0.65\%\) relative to the data, not \(0.7\%\) unless one rounds aggressively. That is close, but the manuscript should show the exact formula used for the “99.3%” figure, because readers can otherwise compute a slightly different percentage from the displayed numbers.

[P4-E7] **The “1.6× CE-ResNet’s scale” claim is internally approximate and not fully aligned with the cited sample size.** The paper states that the catalog provides “8.47 million galaxies… 1.6× CE-ResNet’s scale,” while the cited CE-ResNet work is summarized as using “\(\sim 1.95\) million galaxies.” The exact ratio \(8.474531/1.95 \approx 4.35\), not \(1.6\), so this looks like a stale or mismatched denominator. The 1.6× factor is only plausible if the comparison is restricted to the **3.2 million spirals**, not the full catalog, and the text does not say that.

[P4-E8] **The sensitivity-floor arithmetic mixes three different definitions of amplitude without a clean mapping.** The discussion gives a Fisher floor of \(\sim 0.29\%\) “full amplitude,” derived from \(\sigma(A/2)\approx 0.048\%\), then states an empirical 50%-recovery threshold at \(A\approx0.75\%\), and finally translates this to a “true-underlying threshold \(\sim1.88\%\)” using the GZ1-dilution factor. Those numbers can coexist, but the manuscript never writes the algebra connecting them, so the reader cannot verify whether \(A\) is a full dipole amplitude, a half-amplitude, or a CW-excess fraction. This is a hidden definitional problem rather than a numerical one, but it matters because the same symbol is used in multiple operational senses.

[P4-E9] **A “strict-superset subsample mask” is described as \(f_{\rm sky}=0.659\) with \(n=5{,}547{,}858\), but the text never clarifies the relation to the 471,049 high-confidence subsample cited in the abstract.** The abstract foregrounds “471,049 high-confidence per-spiral after \(p_{\rm eq,CW}>0.9\),” while the headline null uses the much larger mask count. Without an explicit bridge, the reader cannot tell whether the abstract’s HC subsample is merely descriptive or is directly tied to the reported \(-0.122\sigma\) result. That is an abstract-faithfulness gap: the body is clear, but the abstract compresses two different populations into one narrative.

[P4-E10] **The appendix claims “all 8 tests pass,” but the pass criteria are unevenly quantified and not all are in comparable units.** Table V mixes thresholds like \(r>0.80\), “>80% agreement,” “<0.10,” and a qualitative “PASS.” This is fine for an internal audit suite, but the manuscript later uses the suite as evidence of “bias hardening” in a quasi-quantitative way. PRD readers will expect at least one sentence stating which of these are hard thresholds and which are soft sanity checks, because otherwise the audit suite can look more exhaustive than it actually is.

[P4-E11] **The claim that the \(+3.64\sigma\) canonical-mask residual is “not a positive detection” is supported, but the body overstates the certainty of the preferred explanation.** Appendix D ends with “The most likely explanation is a per-pixel-correlated systematic,” while the displayed diagnostics are still model-based and rely on a finite-\(N\) null ensemble. The manuscript should distinguish “best supported by the present diagnostics” from “established mechanism,” especially because the block-bootstrap WLS fit can also reflect covariance mis-modeling. This is a precision issue in the causal language, not a challenge to the null result itself.

[P4-m5] **A stated percentage penalty is not explicitly derived.** Appendix E says edge-on contamination reduces effective sample size by **\(\sim 10\)–15%**, corresponding to a **\(\sim 5\)–8% sensitivity penalty**. The text does not show the conversion from sample-size loss to sensitivity loss, and for counting statistics the relation should scale roughly as \(1/\sqrt{N}\), which would imply only about a 5–8% degradation if the count loss is indeed 10–15%. The statement is plausible, but the arithmetic should be written out to avoid the impression of an unsupported heuristic.

[P4-m6] **The paper’s “largest published catalog of per-galaxy chirality classifications” claim is better supported than the initial review noted, but the exact comparison class is still underdefined.** The body contrasts the 8.47M DESI catalog with CE-ResNet’s \(\sim1.95\)M galaxies and Shamir’s smaller SDSS/Pan-STARRS catalogs, but it does not explicitly exclude larger non-public or non-per-object chirality analyses. To make the novelty claim robust, the manuscript should say “largest **published per-galaxy chirality catalog** to date, to our knowledge,” and define the comparison class as catalogs that assign chirality labels to individual galaxies.

[P4-m7] **The appendix’s “\(+3.63\), \(\,+4.73\)” multipole values are not clearly tied back to the main-text \(+3.64\sigma\) claim.** Appendix D states \(\sigma_{\ell=1}=+3.63\) and \(\sigma_{\ell=2}=+4.73\), but the main text uses \(+3.64\sigma\) for the canonical-mask direct-MC residual. Because the appendix values are close but not identical, the paper should explain whether these are from the same null, the same seed, or a slightly different estimator. Otherwise the reader cannot tell if the small mismatch is rounding, a bandpower-vs-single-mode difference, or a stale-number artifact.

If you want, I can now produce a **single consolidated “revision checklist”** that merges the original findings with these additional ones into a PRD-style referee memo.