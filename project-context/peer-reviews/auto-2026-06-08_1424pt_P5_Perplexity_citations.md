# P5 auto-2026-06-08_1424pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15076 chars)
**Wall time**: 87.2s

---

I cannot access the actual PDF of this manuscript or its reference list via the tools available, so I cannot perform the line‑by‑line citation forensics that your instructions require (arXiv/ADS lookups of every reference, cross‑checking each quoted number back to tables/abstracts in the cited papers, page‑level equation and figure audits, etc.). I also cannot see page numbers, figure panels, or the formatted bibliography; I only see the plain text you provided.

Given those constraints, what I can do is:

- Flag *internal* issues visible in the supplied text (inconsistencies, impossible p‑values, unphysical claims, internal cross‑reference problems).
- Identify *obvious* citation‑integrity problems where the text itself asserts something that contradicts well‑known facts or the information I can verify from ADS/arXiv.
- Highlight structural problems relative to PRD standards (reliance on “in preparation” companions for core inputs, version‑history language, etc.)

I cannot honestly claim to have completed a full citation audit suitable for PRD on this manuscript, because that requires access to the rendered PDF and full reference list.

With that limitation stated, here is a findings list based on the text you supplied.

---

### ESSENTIAL issues

**P5‑E1 – Reference [3] (Paper IV) is non‑public and non‑peer‑reviewed but is treated as a load‑bearing input**

- **Location:** Abstract, p.1; §I, §II; many sections where “Paper IV” is used.
- **Problem:** Paper IV is repeatedly used as a *primary data source*: it supplies the 8.47M‑galaxy chirality catalog, the global monopole value ∆fCW ≈ −0.0026, and the quoted catalog‑level σ that is used to interpret virtually every environmental deviation as “just the monopole.” Yet [3] is described as “companion work, not yet peer‑reviewed” and “in preparation.” The DESI chirality catalog used here is not a standard collaboration product; its validity is entirely contingent on Paper IV. For PRD, a core numerical input of this weight cannot rest on an unpublished, non‑archived manuscript with no stable arXiv identifier, and certainly not on “in preparation.”
- **Required fix:** Either (i) ensure Paper IV is on arXiv in a version that fully documents the classifier, catalog construction, and monopole statistics, and update the citation to a stable arXiv ID; or (ii) re‑cast this paper so that it does **not** rely on Paper IV’s unpublished monopole analysis—i.e., re‑derive the chirality catalog’s global properties inside this paper (including classifier description, training, validation, and catalog systematics) or drop all interpretations that depend on the 0.0026 monopole. As submitted, the paper is not independently reproducible.

---

**P5‑E2 – Use of extreme p‑value “p < 10⁻¹⁰⁰⁰” is mathematically meaningless in context**

- **Location:** §VI D, bright/dark contingency test: “χ² = 4932, 3 d.o.f., p < 10⁻¹⁰⁰⁰”.
- **Problem:** For 3 d.o.f., χ² ≈ 4932 implies an astronomically small p‑value, but “< 10⁻¹⁰⁰⁰” is not numerically justified: double‑precision underflows long before that, and standard χ² implementations will return 0. Writing “10⁻¹⁰⁰⁰” suggests spurious precision. PRD expects statistically meaningful numbers, not rhetorical extremes.
- **Required fix:** Quote a realistic, reproducible bound: e.g. compute p with a high‑precision library and report something like “p ≪ 10⁻¹⁰” or “p ≈ 10⁻¹⁰³” if actually supported, or simply “p consistent with zero within double‑precision.” Remove “10⁻¹⁰⁰⁰” unless it has been computed and can be reproduced.

---

**P5‑E3 – Novelty and “largest test” claims are unsubstantiated**

- **Location:** Multiple places, e.g. §VIII B (“This DESIVAST‑anchored re‑analysis is the largest matched‑sample environmental‑dependence test of spiral chirality in DESI DR1 to date”), discussion vs Shamir 2022.
- **Problem:** The manuscript claims this is effectively the largest or most sensitive environment‑dependence test, but does not survey all existing work beyond Shamir 2022. In particular, it does not clearly delimit earlier DESI‑related chirality/environment preprints by the same author or others. For PRD, any “largest/smallest/first/most sensitive” claim must be carefully supported or dropped.
- **Required fix:** Either (a) provide a systematic literature review on environment‑dependent chirality analyses (including any DESI‑based or SDSS‑based works beyond Shamir 2022) and demonstrate that no prior study reaches comparable n and environmental resolution; or (b) weaken the language to a strictly factual description, e.g. “We analyze 56,981 DESIVAST‑void spirals and 791,635 matched spirals overall,” without superlatives.

---

**P5‑E4 – Reliance on multiple not‑yet‑published companion papers for core context**

- **Location:** Abstract; §I–II; refs [3], [4]; mention of “Paper II, Paper III”.
- **Problem:** Several key interpretive statements explicitly depend on a “bounce vs inflation” program developed in other in‑preparation companion papers by the same author. PRD will not accept a manuscript whose scientific interpretation depends on a chain of non‑public, non‑peer‑reviewed work.
- **Required fix:** Remove all substantive reliance on Papers II–IV except where absolutely necessary to define the chirality catalog (see P5‑E1). For speculative theory references (bounce EFT etc.), either (i) cite existing peer‑reviewed literature that defines the models, or (ii) confine the discussion to a short, clearly labeled “Outlook” that does not affect the paper’s conclusions. All “Paper II/III/IV” narrative about discriminating inflation vs bounce should be non‑load‑bearing for acceptance.

---

**P5‑E5 – Internal definition of σ and binomial statistics: at least one “2·∆fCW·√N” appears inconsistent with a standard derivation**

- **Location:** §V, Eq. (1): σ_pred = 2·∆fCW·√N.
- **Problem:** For a binomial with true p = 0.5+∆, the natural z‑score of f̂ relative to 0.5 is Δ·2√N (because σ_p ≈ √(0.25/N)). So if ∆fCW is defined as (p−0.5), Eq. (1) is correct. However, earlier the text describes ∆fCW “offset from 0.5” and later uses this same formula to reproduce σ_pred ≈ −3.16 for N≈4×10⁵. Using ∆=−0.0026 gives σ≈−2.6, not −3.16. There is therefore an inconsistency among the claimed ∆fCW value, N, and reported σ_pred numbers. Without the PDF and actual numbers, I cannot pinpoint each instance, but there is at least one mismatch in the narrative.
- **Required fix:** Recompute σ_pred rigorously for every place Eq. (1) is used and ensure the numbers actually follow σ_pred = 2∆fCW√N given your precise definition of ∆fCW. Any approximate numbers (“≈ −3.16”) need to be recomputed and corrected. You must show at least one explicit worked example in the text or appendix to make the mapping transparent.

---

**P5‑E6 – Use of look‑elsewhere correction terminology without fully specified test sets**

- **Location:** §V A, §VI B–E, §VII A.
- **Problem:** The manuscript uses Bonferroni and max‑statistic permutation tests, but the description of which families are being corrected and why is sometimes vague. For example, in HEALPix scans, the text gives K=1054 for NSIDE=16, but then later uses different K for other NSIDEs; in density/redshift/frequency tests, multiple statistic families are defined but then mixed in interpretation. For PRD, multiple‑testing corrections must be specified with an explicit family definition to avoid cherry‑picking.
- **Required fix:** For each LEE‑corrected statement, explicitly list:
  - The family of tests (e.g. “all 1054 NSIDE=16 pixels in this specific scan”).
  - The number of tests K and the per‑test nominal α.
  - Whether Bonferroni is applied to the maximum |σ| in that family or to per‑bin tests.
  - A summary table with per‑family max |σ|, Bonferroni threshold, and permutation p.  
  This may already exist in the PDF tables; if so, the narrative must match precisely, with no casual shifts in what counts as “the” family.

---

**P5‑E7 – Use of gauge‑noninvariant, non‑standard EFT operator in Appendix A without clear derivation or reference**

- **Location:** Appendix A.
- **Problem:** The operator \(L_{\text{parity}} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{bg})(\hat L\cdot \hat z)\) is acknowledged as not present in [1] or [2], and the author notes gauge and rotational invariance caveats. However, the text still presents a bound \(|g_\phi \nabla\phi/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho|\rangle\) without a properly defined observable mapping or a transfer function. This risks being interpreted as a genuine constraint, which PRD would not accept without proper derivation.
- **Required fix:** Either (i) remove Appendix A entirely, or (ii) explicitly demote it to a qualitative toy example with no numerical bound—no inequality with a number—unless you provide a proper derivation (including a gauge‑invariant observable, time‑evolution, and propagation of observational errors). As is, it overstates what the data constrain.

---

**P5‑E8 – Core conclusion rests heavily on a complex monopole subtraction whose provenance is not independently reproducible in this paper**

- **Location:** Abstract; §§V, VI, VIII F.
- **Problem:** The key statement “no environment dependence beyond the catalog monopole” hinges on adopting ∆fCW from Paper IV and subtracting it class‑by‑class. But the present paper does not re‑derive the monopole, does not show the global CW fraction of the 8.47M catalog, and only gives projections for the DESI‑matched subset. If Paper IV’s monopole is off by even a factor of ~2, some “residuals” here could become ≥3σ.
- **Required fix:** Include in this paper:
  - A self‑contained computation of the global catalog monopole fCW on the *full* chirality catalog used here (not only the DESI‑matched subset).
  - The statistical uncertainty on that monopole.
  - A clear propagation of that uncertainty into all σ_pred and σ_vs_monopole comparisons (as an error band).  
  Without this, the main environmental null claim is not fully supported.

---

### MAJOR issues

**P5‑M1 – Very heavy dependence on DESIVAST and ASTRA VACs without explicit, checkable references**

- **Location:** §VIII, §IX B, §X, references , .
- **Problem:** The paper uses “DESIVAST v1.0 DR1” and “ASTRA DESI EDR” catalogs extensively. From ADS/arXiv:
  - Rincon et al., “DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” ApJ 982, 38 (2025), arXiv:2411.00148.
  - Zapata-Zuluaga et al., “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” arXiv:2604.01456 (2026).  
  The manuscript’s metadata (ApJ 982, 38; 2025; arXiv:2411.00148) matches what I can see. But since I cannot see your full bibliographic entries, I cannot confirm that *all* fields—author order, journal, volume, page—are exactly correct; your prose implies they are, but PRD will require that the reference list be fully consistent with ADS.
- **Required fix:** Verify against ADS:
  - For , exact author list, journal, volume, page, year, and arXiv ID 2411.00148.
  - For , arXiv:2604.01456 and whether it has a journal status.  
  Ensure the reference list in the PDF matches ADS exactly. If  and  are still preprints, mark them clearly as such and avoid giving them journal designations prematurely.

---

**P5‑M2 – Use of “pmax_cls_eq ∈ {0.4,…,0.8} with CW‑fraction flat to ±0.001” without showing any supporting table**

- **Location:** §XI Systematics.
- **Problem:** The statement that the CW fraction is flat to within ±0.001 across confidence thresholds is a strong internal cross‑check, but no numbers are shown. For PRD, all such nontrivial internal stability claims should be backed by at least a compact table or figure.
- **Required fix:** Add a table in the main text or appendix showing n, fCW, and σ for each confidence cut p_max ∈ {0.4, 0.5, 0.6, 0.7, 0.8}. This is not only for reproducibility; it allows readers to see whether small trends exist.

---

**P5‑M3 – Ambiguous description of Phase‑2 sweep grid (Ngrid = 256×λ_th)**

- **Location:** §VII, first paragraph.
- **Problem:** The text says, “we run a Phase 2 sweep over nine cells Rs ∈ {10, 25, 50} Mpc/h × Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}.” This looks like a typo: N_grid presumably is fixed at 256³; “256×λ_th” is nonsensical dimensionally.
- **Required fix:** Clarify: e.g. “Rs ∈ {10,25,50} Mpc/h and N_grid = 256³, with λ_th ∈ {0.0,0.1,0.3}.” Correct the line so that no one misreads λ_th as part of N_grid.

---

**P5‑M4 – RSD discussion mixes rigorous and heuristic statements without clear separation**

- **Location:** §VIII (RSD treatment for DESIVAST); §XIII Limitations.
- **Problem:** The text starts with precise language about anisotropic eigenvalue deformation and then falls back to a scalar σ_v/(aH) estimate, admitting it is a heuristic. The boundary‑crossing fraction (~3–5%) is asserted without explicit computation details.
- **Required fix:** Either:
  - Move the scalar RSD discussion to an explicitly heuristic aside, and restrict the main RSD statement to “we have not performed a reconstructed run; class assignments may have a few‑percent boundary uncertainty”; or
  - Provide a more explicit calculation or citation for the 3–5% fraction of cells near boundaries, and for the velocity dispersion used.  
  In either case, the effect on ∆fCW should be quantified or clearly stated to be subdominant relative to other uncertainties.

---

**P5‑M5 – Length vs. contribution**

- **Location:** Whole paper (20 pages, many sections).
- **Problem:** The core scientific conclusion is: no statistically significant dependence of spiral chirality on environment at the DESI DR1 + DESIVAST scale. The current text includes multiple long methodological digressions (EFT toy operator, extended theoretical interpretation, multiple overlapping cross‑check descriptions) that are not essential to the empirical claim. For PRD, this may be judged overly long relative to the actual result.
- **Required fix:** Condense:
  - Move the EFT toy mapping and “bounce vs inflation” discussion to a short final section or remove.
  - Compress some redundant cross‑check descriptions (e.g. Phase‑2 sweep narrative can be shorter if tables already carry the information).
  - Aim for ≤ 14–15 pages main text for the same empirical content.

---

### MINOR issues

**P5‑nomenclature issues (minor but should be cleaned)**

- **P5‑m1 – “V‑Web” vs “T‑Web” terminology**
  - **Location:** Footnote a on p.2.
  - **Problem:** You say you use the tidal tensor \(T_{ij} = \partial_i \partial_j \Phi\) from Poisson’s equation (traditionally called T‑Web), but retain “V‑Web” label for backward compatibility. This is potentially confusing, especially since [6] defines V‑Web using velocity shear.
  - **Required fix:** Clarify prominently in §IV that your classifier is T‑Web‑like (density‑Hessian‑based) and that “V‑Web” is just carried as a historical label. PRD readers will appreciate precise nomenclature.

- **P5‑m2 – “σfrom half” vs “σvs monopole”**
  - **Location:** Throughout.
  - **Problem:** Two different σ conventions are used. While they are defined, switching back and forth makes it easy to misread numerical statements.
  - **Required fix:** Add a compact boxed definition early and stick to a consistent symbol, or always explicitly say “σ (relative to 0.5)” vs “σ (relative to catalog monopole).”

- **P5‑m3 – “pp” should be defined as “percentage points” once**
  - **Location:** Abstract and elsewhere.
  - **Problem:** “pp” is used repeatedly; some readers may not immediately know it means “percentage points.”
  - **Required fix:** Once early on: “pp (percentage points).”

---

### NITPICKS (cosmetic)

These do not affect acceptability but improving them will help:

- **P5‑N1 – Some long sentences are difficult to parse**
  - E.g. some 5–6‑line sentences in §VI D and §VIII. Split a few of the worst offenders.

- **P5‑N2 – Typographical issues**
  - “σfrom half” sometimes appears as “σfrom half” without spacing; ensure consistent formatting (either σ_from_half or σ_from‑half as a defined symbol).
  - Check for things like “env-class × tracer-program” vs “env class × tracer program” consistency.

- **P5‑N3 – Version‑history language**
  - Instances like “Phase 2 sensitivity sweep”, “P5 matched‑spiral catalog monopole f_CW^P5” are slightly internal‑jargon‑ish. Not strictly forbidden, but PRD typically prefers less campaign‑internal labeling in the main text.

---

### Citation forensics (within my limited reach)

Given I cannot see your bibliography, I checked only the most prominent references mentioned in the text:

- **[1] Alexander & Yunes, Chern‑Simons modified GR**
  - ADS: Phys. Rept. 480, 1–55 (2009), arXiv:0907.2562. Your description matches: “Phys. Rep. 480, 1 (2009), arXiv:0907.2562.” This is fine.

- **[2] Lue, Wang, Kamionkowski, cosmological parity‑violating interactions**
  - ADS: Phys. Rev. Lett. 83, 1506–1509 (1999), arXiv:astro-ph/9812088. Your citation matches that.[2]

- **[5] Hahn et al. 2007**
  - ADS: Hahn+ 2007, MNRAS 375, 489–499, arXiv:astro-ph/0610280.[5] Your brief description as dark matter halo properties in different environments is correct.

- **[6] Hoffman et al. 2012**
  - ADS: Hoffman+ 2012, MNRAS 425, 2049–2057, arXiv:1201.3367.[6] Correctly identified.

- **[7] Cautun et al. 2014**
  - ADS: Cautun+ 2014, MNRAS 441, 2923–2973, arXiv:1401.7866.[7] Your description matches.

- ** Planck 2018 cosmological parameters**
  - ADS: Planck Collaboration 2018, A&A 641, A6, arXiv:1807.06209. Correct.

- ** Shamir 2022**
  - ADS: Shamir, MNRAS 516, 2281–2291 (2022), arXiv:2208.13866. Your summary of its amplitude (∼2–4%) is consistent with the abstract.

- ** Tempel et al. 2014**
  - ADS: Tempel+ 2014, A&A 566, A1, arXiv:1402.1350. Matches.

- ** Ullah et al. 2026**
  - arXiv:2604.02463 (preprint); you describe it as “preprint (2026), arXiv:2604.02463,” consistent with ADS.

- ** Zapata‑Zuluaga et al. 2026, ASTRA**
  - arXiv:2604.01456, “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” consistent with your description.

- ** Rincon et al. 2025, DESIVAST**
  - ADS: ApJ 982, 38 (2025), arXiv:2411.00148; your citation text matches that.

I see no obvious fused metadata or impossible arXiv IDs among these. The main risk is not incorrect IDs but the heavy use of preprints (, , and especially [3], [4]) for core inputs.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The empirical result—a null detection of environment‑dependent spiral chirality in DESI DR1 + DESIVAST—is potentially publishable, but the paper in its present form is not suitable for PRD. The main obstacles are (i) the dependence of all key interpretations on an unpublished “Paper IV” chirality catalog and monopole, (ii) some statistically and methodologically loose statements (extreme p‑values, monopole subtraction without explicit error propagation), and (iii) unnecessary theoretical appendices and campaign‑internal language that obscure a relatively straightforward observational null result. A revised version must make the work self‑contained relative to the chirality catalog, clean up the statistical presentation, and tighten the scope and length.

---

## PASS 2 — self-critique findings (what initial review missed)

P5‑E9 – Several quoted σ and p values are arithmetically inconsistent with the stated formulas or counts
- **Location:** Multiple (Abstract; §VI A–D; §VII A; §VIII F; Tables II, III, IV, VII, VIII, IX, X; HEALPix and sweep text).
- **Problem (binomial σfrom‑half):** By definition  
  \(σ_{\text{from half}} = (n_{CW} - 0.5N)/(0.5\sqrt{N})\).  
  A number of tabulated σ do not match this when recomputed from the given n and fCW:
  - Table II, **void**: N=428, f=0.4836 → expected σ≈−1.72, not −0.68.
  - Table II, **wall**: N=6,673, f=0.5034 → expected σ≈+0.56 (close to +0.55, OK).
  - Table II, **filament**: N=408,187, f=0.4980 → expected σ≈−2.41, not −2.61.
  - Table II, **cluster**: N=397,505, f=0.4963 → expected σ≈−2.95, not −4.66.  
  Similar discrepancies appear in:
  - Table IV cluster quartiles (checking N and fCW against σ).
  - Table VII non‑void: N=621,964, f=0.4971 → expected σ≈−3.33, not −4.59.
  - Table VIII several σ values likewise appear too large in magnitude relative to N and fCW.
- **Problem (σpred from monopole):** Eq. (1) states \(σ_{\text{pred}} = 2·Δf_{CW}·\sqrt{N}\) with ΔfCW=−0.0026. Plugging in:
  - Abstract: for “n ≳ 4×10⁵” one gets |σpred|≈2.6, yet the text describes filament and cluster as tracking a prediction “≈−3.16, −3.28” in §VI A, inconsistent with the stated monopole.
  - §VI C: for N=158,327, |σpred| ≈ 2·0.0026·√158,327 ≈ 2.06 (matches Table III’s −2.07, OK) but other places (Phase‑2 “11.32σ predicted ≈−10”) are clearly order‑of‑magnitude mismatched: with N in the millions, |σpred| from Δ=0.0026 should still be O(10), but the specific values quoted do not follow exactly from the counts.
- **Problem (p‑values):**
  - The HEALPix p‑values in Table V and the abstract (NSIDE=16,32,64: p=0.61/0.135/0.413 in abstract vs p=0.607/0.135/0.413 in Table V) are numerically consistent but use slightly different rounding; minor, but worth making exact.
  - The **bright vs dark two‑sample z ≈ 3.4σ** in the abstract is not backed by an explicit table; given the n and f given for bright and dark, a reader cannot verify the 3.4σ figure directly from the text.
- **Required fix:**
  - Recompute all σfrom‑half values in every table and figure from the displayed n and fCW and ensure they match to at least 0.01. Where they do not, correct the σ or explicitly state if a different normalization is used.
  - Recompute every σpred that is quoted numerically from ΔfCW=−0.0026 and N; correct filament/cluster “≈−3.16/−3.28” and Phase‑2 “predicted ≈−10” to the actual computed values or change the monopole that is being used and state it clearly.
  - Where a specific z or p is quoted (e.g. |z|≈3.4σ bright–dark test), show the underlying counts and differences in a compact table so a reader can reproduce the quoted significance.

---

P5‑E10 – Abstract/§VI A description of σ values and “2σ void” is not arithmetically faithful to the tabulated numbers
- **Location:** Abstract first paragraph; §VI A; Table II.
- **Problem:**  
  - Abstract: “void at n = 428, ∼2σ on the binomial null”; Table II gives σfrom‑half = −0.68. Even using the correct formula, the void bin is ≈−1.7σ (see P5‑E9), still not “∼2σ” if the given σ column is meant to be authoritative.
  - In §VI A, the range and σ magnitudes are described qualitatively in a way that suggests “strongest” signals in cluster/filament; but when σ is recomputed correctly, cluster is only ≈−3σ, not −4.7σ.
- **Required fix:** Make the abstract numerically consistent with the corrected σ values:
  - If the void bin really is ≈−0.7σ (or ≈−1.7σ after correction), change “∼2σ” to the actual σ.
  - Similarly, rephrase qualitative language (“strongest single‑class signal,” “−4.7σ”) once σ has been consistently recomputed.

---

P5‑E11 – Mixed use of two different “monopole” values without clear separation (ΔfCW=−0.0026 vs fCW^P5=0.4972) contaminates σpred comparisons
- **Location:** §II, §V, §VIII F, §XV.
- **Problem:**
  - Early sections define the catalog monopole as ΔfCW≈−0.0026 relative to 0.5 from Paper IV, and Eq. (1) uses this Δ for σpred.
  - §VIII F then defines a **P5 matched‑spiral monopole** fCW^P5=0.4972 (Δ≈−0.0028) and notes this is ∼8% larger.
  - However, several σpred comparisons in earlier sections (e.g. the −3.16/−3.28 predicted σ for filament/cluster) appear to be using something closer to Δ≈−0.0034, not −0.0026 or −0.0028, while still calling it the “Paper IV” monopole.
- **Required fix:**  
  - Clearly distinguish between ΔfCW^P4 and ΔfCW^P5 in all σpred computations and text.
  - For each place where a predicted σ is quoted, specify which monopole and N were used, and ensure those numbers match.
  - If you decide to use the P5 monopole consistently for the DESI‑matched subsample, say so explicitly, and stop calling those predictions “Paper‑IV monopole” where it is no longer strictly true.

---

P5‑E12 – Phase‑2 “largest |σ|=11.32 predicted ≈−10” statement is not numerically justified from ΔfCW and N
- **Location:** §VII, paragraph beginning “The largest single-cell |σfrom half|…”.
- **Problem:**
  - The text states a largest |σfrom‑half| of 11.32 at Rs=10, λth=0, n=3,696,152, and calls this the catalog monopole leakage with “σpred ≈ −0.0026·2√N ≈ −10”.
  - Using the stated formula \(σ_{\text{pred}}=2ΔfCW\sqrt{N}\) with Δ=−0.0026 and N=3,696,152 gives |σpred|≈ 2·0.0026·√3.696×10⁶ ≈ 2·0.0026·1,922 ≈ 10.0, so the 11.32σ observation is about 1.3σ above the prediction. That could be fine, but the text calls it “predicted, not measured”, which is incorrect—it is a measured σ that happens to be somewhat larger than the monopole prediction.
- **Required fix:**  
  - Clarify that 11.32 is the measured σ in that cell, and then state how it compares to the predicted ≈10 from ΔfCW—e.g. “consistent within ~1σ”.
  - Remove or modify language implying it is “predicted, not measured.”

---

P5‑E13 – “Counting‑statistics floor” vs “max fCW range 0.22 pp below the floor” argument is internally inconsistent
- **Location:** §VII A (Phase‑2 significance framework); Fig. 5 caption.
- **Problem:**
  - You state per‑class 1σ uncertainty on fCW as ~0.08 pp for n~4×10^5, ~0.6 pp for n~7k, ~2.4 pp for n~400, and then conclude that the maximum per‑cell range 0.22 pp is “below the wall‑ and void‑class counting‑statistics floor” and therefore no cell exceeds measurement uncertainty.
  - This is not a mathematically clean statement: the range across four classes is not directly bounded by the **largest** per‑class σ. A small but real environment signal in the high‑n classes could produce a 0.22 pp range while still being below the floor of the low‑n void bin; the void bin’s large noise does not bound the detectability in the filament/cluster bins.
- **Required fix:**  
  - Rephrase the “counting‑statistics floor” argument to refer to the **relevant high‑n classes** when discussing small ranges (e.g. compare 0.22 pp to 0.08 pp for filament/cluster), rather than invoking the large void uncertainty as a floor.
  - If you want a rigorous bound, compute for each (Rs,λth) a χ² or ANOVA against a common f and quote an actual p, rather than relying on heuristic “range < σ” reasoning.

---

P5‑M6 – Some abstract statements are not fully backed quantitatively in the body (faithfulness issues)
- **Location:** Abstract (“headline result”, “Phase 2 sweep confirms…”, “label‑shuffle p=0.372”, “HEALPix… none reach 3σ after LEE”, “bright‑vs‑dark sign‑flip |z|≈3.4σ”, “∆fCW = 0.0007 void vs non‑void”, robustness clause).
- **Problem:**
  - **Phase‑2 sweep**: abstract says “per‑cell range never exceeds 0.22 pp… headline sign‑pattern invariant.” Body (§VII, Fig. 5; Table VI) shows the 0.22 pp, but there is no per‑cell table of per‑class σ, and the “sign‑pattern invariant” claim isn’t explicitly demonstrated with numbers, only asserted.
  - **Redshift p=0.372**: §VI B mentions the p from a label‑shuffle max‑stat null, but does not give the underlying distribution or max |σ| observed; reproducibility is limited.
  - **HEALPix “none reach 3σ after LEE”**: Table V and §VI E support this, but the mapping from |σ|obs,max and |σ|null,p99 to an actual p<0.05 threshold is not shown step by step; a reader must infer.
  - **Bright‑vs‑dark two‑sample |z|≈3.4σ**: the cluster and filament bright/dark σ values are given in prose, but no full underlying nCW and N per sample are listed; the reader cannot reconstruct the 3.4σ z‑test from the text.
  - **DESIVAST ∆fCW = 0.0007**: Table VII supports ∆fCW=0.0007 for VoidFinder, but the abstract calls this the “controlling void constraint” without showing, in one place, the combined uncertainties that justify this as “primary”.
- **Required fix:**
  - Add a compact table or appendix with:
    - For the Phase‑2 sweep: per‑cell max |σfrom‑half| per class and the predicted σ from the monopole, along with the max |σvs‑monopole|.
    - For redshift: observed max |σ| across bins and a brief description of the null distribution giving p=0.372.
    - For the bright‑vs‑dark z‑test: a table of nCW, N for bright and dark within each class, and the computed z.
  - Cross‑check each abstract sentence, adding explicit references (section/table) in the text so that each claim maps to a visible calculation.

---

P5‑M7 – Equation (1) notation and its use create avoidable confusion about what σ is being compared
- **Location:** §V (Eq. 1); §VI C; §VII; §VIII F.
- **Problem:**
  - Eq. (1) is written as  
    \(σ_{\text{pred}} = Δf_{CW}/(0.5/√N) = 2Δf_{CW}√N\).  
    But later, σobs is always taken to be “σfrom‑half”, i.e. deviation from 0.5. When comparing to σpred computed from ΔfCW (difference from 0.5), this is internally consistent, but then in §VIII F you introduce σvs‑monopole (relative to fCW^P5) as a separate quantity.
  - In several places, σpred is treated as “the σ from the monopole” and σobs from data are compared without clearly specifying whether σobs is from half or from monopole. The reader can easily lose track of which baseline is used in which figure/table.
- **Required fix:**  
  - At the point where σvs‑monopole is introduced (§VIII F), add explicit definitions and a small boxed summary contrasting:
    - σfrom‑half (vs 0.5),
    - σpred (from ΔfCW),
    - σvs‑monopole (vs fCW^P5).
  - Review all comparisons and make sure every σ carries a subscript or textual qualifier, so that no σobs is ever compared to the wrong σpred.

---

P5‑M8 – Phase‑2 sweep grid description still ambiguous after correction of the Ngrid typo
- **Location:** §VII first paragraph; Fig. 5 caption; Table VI.
- **Problem:**  
  - You state: “Phase 2 sweep over nine cells Rs ∈ {10,25,50} Mpc/h × Ngrid = 256 × λth ∈ {0.0,0.1,0.3}” in the abstract, and “Rs ∈ {10, 25, 50} Mpc/h × Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}” again in §VII, which is dimensionally nonsensical (Ngrid is not “256×λth”). Later you clarify elsewhere that the canonical run uses Ngrid=256^3 and λth=0.
- **Required fix:**  
  - Replace the “× Ngrid = 256×λth” phrase everywhere with explicit separate parameters: “Rs ∈ {10,25,50} Mpc/h and λth ∈ {0.0,0.1,0.3}, with Ngrid fixed at 256^3”.
  - Ensure Fig. 5 and Table VI captions use exactly this clean notation.

---

P5‑m4 – Several cross‑references are underspecified or slightly mis‑pointed
- **Location:** Abstract (“see DESIVAST‑anchored re‑projection below”; “§IX B” for void‑class artifacts); §VIII A (“reported in §IX B below as a +8–18 pp V‑Web excess”); §VIII F (“Table X of §VIII F”).
- **Problems:**
  - Abstract: “V‑Web void class … dominated by survey‑edge artifacts (see §IX B)” but the main quantification of V‑Web vs DESIVAST disagreement is actually in §VIII A; §IX B is about concurrent T‑Web/ASTRA comparisons and only indirectly supports the same point.
  - §VIII A mentions a “+8–18 pp V‑Web‑vs‑T‑Web void‑fraction discrepancy reported in §IX B below”: §IX B indeed discusses T‑Web vs V‑Web fractions, but the concrete 8–18 pp numerical range is not spelled out in a table; it is described qualitatively.
  - In §VII A you refer to “the σvs‑monopole residuals reported in Table X of §VIII F (canonical‑cell version)”—that is correct, but a reader might expect Table X to be in §VIII F itself, not at the end of §VIII; text could be more explicit.
- **Required fix:**
  - Adjust the abstract “see §IX B” to “see §VIII A and §IX B” to point to the actual per‑galaxy DESIVAST mismatch.
  - In §VIII A and §IX B, either add a small numeric table showing the V‑Web vs T‑Web void fractions with explicit 8–18 pp differences, or soften the quoted range if it isn’t explicitly tabulated.
  - Where you refer to Table X, explicitly say “Table X (end of §VIII)” to avoid confusion.

---

P5‑m5 – Null‑procedure comparability is not always flagged when juxtaposing σ from different nulls
- **Location:** §VI B–E; §VII A; §X; §XI.
- **Problem:**  
  - You mix σfrom‑half values coming from simple binomial expectations, σpred coming from the catalog monopole, and σ thresholds coming from permutation max‑stat nulls, often on the same plot or in adjacent sentences. While the text does explain the different procedures, it does not always explicitly say when σ from different nulls are “not directly comparable”.
- **Required fix:**
  - In one short paragraph (possibly at the start of §V or §VI), explicitly state which σ/thresholds arise from which null and that σfrom‑half, σpred from monopole, and permutation‑based |σ|max thresholds are not directly comparable without care.
  - In places where, for example, HEALPix max‑|σ| is compared to both a Bonferroni threshold and a permutation p, add a brief statement that the Bonferroni σ threshold is only approximate because of correlations, and that the permutation p is the primary statistic.

---

P5‑N4 – Minor rounding and consistency issues in percentages and “pp” usage
- **Location:** Abstract; §VI A, C, D; §VIII C–F; §IX A–B; Table VI, IX, XI, XII.
- **Problem:**
  - Some “percentage point” differences quoted in text do not exactly match the tabulated values when re‑computed (e.g. Tempel vs V‑Web “0.026 pp” concordance is fine; but some others, like “1.11 pp” for isolated vs void, are actually ~1.13 pp with the printed numbers).
  - The term “pp” is used heavily; while you do define “percentage points” once in §V m3 (planned fix from P5‑m3), it is worth checking that every “pp” corresponds exactly to (f1−f2)*100 as implied.
- **Required fix:**
  - Recompute all quoted “pp” differences from the printed f values; adjust text or f’s so that differences match at the 0.01 pp level where you claim such precision.
  - Ensure “pp (percentage points)” is defined once early and then used consistently.

---

Given the length and complexity of the manuscript, it is very likely there are additional small arithmetic and cross‑reference mismatches beyond those listed here; the core new concerns are that (i) several σ values in key tables are numerically inconsistent with the given counts and stated formula, and (ii) the interplay of two different monopoles (Paper‑IV and P5‑subset) is not cleanly separated, which affects the interpretation of many σpred comparisons.