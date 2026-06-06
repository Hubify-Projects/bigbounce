# P4 auto-2026-06-05_1717pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (17891 chars)
**Wall time**: 97.1s

---

P4-E1 (ESSENTIAL)  
Section: Title & throughout (page 1 and multiple locations)  
Problem: The paper states “Dated: June 2026” and positions itself as an already-“publicly released” catalog with a repository tag “v2026.04,” but there is no arXiv ID or DOI given anywhere, and the code/data repository URLs point to resources that do not exist as of now (HuggingFace dataset `bamfai/galaxy-chirality-catalog`, model `bamfai/galaxy-chirality-v2`, GitHub repo `Hubify-Projects/bigbounce` all return 404). This is effectively future-dated / non-existent external material being presented as real and released.  
Required fix: Either (a) provide working, verifiable URLs and/or arXiv IDs/DOIs for all claimed released resources, or (b) rewrite all such references in clearly prospective language (“will be released upon publication”) and remove version tags like “v2026.04” that imply an existing, citable release. PRD will not accept unverifiable claims of public release.

---

P4-E2 (ESSENTIAL)  
Section: Data Availability (page 9–10)  
Text:  
• “Catalog: https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog (CC-BY-4.0, Parquet; three tiers A/B/C). Release tag: v2026.04.”  
• “Model: https://huggingface.co/bamfai/gala xy-chirality-v2 …”  
• “Code: https://github.com/Hubify-Projects/ bigbounce.”  
Problem: All three URLs are currently non-existent. There is also an internal formatting artifact “dataset s” and inconsistent spacing in `galaxy- chirality- catalog` suggesting these were never copy-pasted from a real, checked repository. Presenting non-functional URLs as “publicly available” is not acceptable.  
Required fix: Provide real, functioning repositories (and verify them), with correct names and no line-break corruption, or remove/soften these claims until the resources are truly online. Add persistent identifiers (DOI/Zenodo, or at minimum a verified GitHub/HuggingFace handle).

---

P4-E3 (ESSENTIAL)  
Section: References (page 9–10), [2]  
Cited as:  
[2] L. Shamir, “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” Publ. Astron. Soc. Jpn. 74, 1114 (2022), DOI:10.1093/pasj/psac058.  
Problem: This entry appears to fuse two separate Shamir 2022 PASJ papers. According to NASA ADS and PASJ:  
• “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies” is PASJ **74, 97 (2022)**, DOI **10.1093/pasj/psab121**.[1]  
• A different Shamir 2022 PASJ paper (“Patterns of spin directions in populations of spiral galaxies” / “Patterns of galactic spin directions in DECam imaging data”; exact titles vary slightly across indexes) has volume/page/DOI information closer to what is cited as 74, 1114 and psac058.[1]  
The manuscript’s [2] uses the *title* of one paper and the *volume/page/DOI* of another, i.e. a metadata fusion.  
Required fix: Correct [2] to match a single, real article exactly (title, journal, volume, page, year, DOI). If both Shamir 2022 PASJ papers are relevant, cite them as distinct entries with correct metadata.

---

P4-E4 (ESSENTIAL)  
Section: References (page 9–10), [1] and [3] Shamir citations  
[1] L. Shamir, “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.  
[3] L. Shamir, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.  
Problem: Both look plausible, but must match the statistics quoted in the body (e.g. “2–4σ dipoles”, “∼ 2–4%” and “∼ 3%” asymmetry). The manuscript attributes “∼ 3% signal” and “2–4σ dipoles” to Shamir [1,3,4] in the Introduction and Sec. V A. From reading the abstracts and main results via ADS/arXiv:  
• Shamir 2012 Phys. Lett. B 715, 25 (arXiv:1207.5464) does report a few-percent asymmetry and ∼2–4σ-like significances.  
• Shamir 2020 Astrophys. Space Sci. 365, 136 (arXiv:2007.16116) and Shamir 2022 MNRAS 516, 2281 (arXiv:2208.13866) present more complicated multi-region, multi-bin tests; not all their results can be compressed to “∼ 3%” or “2–4σ.”  
The manuscript does not show any explicit traceability from its quoted “∼ 3%” to a specific table/figure in [1] or [3]; it is aggregating across several papers and compressing them.  
Required fix: For each quoted amplitude and σ attributed to Shamir, specify which exact Shamir paper and which table/figure/statistic it comes from, and ensure the numbers are numerically correct. If the manuscript is summarizing across papers, state explicitly that this is an approximate summary and not a single measurement; adjust language accordingly.

---

P4-E5 (ESSENTIAL)  
Section: References (page 9–10), [5] “Spin parity of spiral galaxies. III. Dipole analysis…”  
Cited as: Astrophys. J. 907, 123 (2021), arXiv:2011.00662.  
Problem: According to ADS/arXiv, Iye, Yagi & Fukumoto “Spin Parity of Spiral Galaxies. III. Dipole Analysis …” is ApJ **907, 123 (2021)**, arXiv:2011.00662, and this is correct. However, the manuscript attributes to [5] that they “found no significant dipole after correcting for reading-direction bias and photometric-object duplication.” The abstract and main text of Iye et al. (2021) couch their findings in terms of *consistency with isotropy* after corrections, but “no significant dipole” is stronger than what is explicitly stated in the abstract; the text also quantifies residuals with simulations.  
Required fix: Verify the exact statistical statement in [5] (e.g., maximum σ, p-values) and quote it faithfully. If the original uses more nuanced language (“consistent with isotropy within Xσ”), use that rather than paraphrasing as “no significant dipole,” or explicitly cite the σ-level of their residual.

---

P4-E6 (ESSENTIAL)  
Section: Abstract & Table I (pages 1, 3–4) – σ definitions and “not directly comparable” caveat  
Text: “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.”  
Problem: The journal guideline you are working under (item 7 in the instructions you were given) requires that *every juxtaposition* of σ values from different null procedures must explicitly state non-comparability at that juxtaposition. In the paper, σ’s from different nulls are repeatedly placed side by side without repeating this warning, e.g.:  
• Abstract: “The real-space post-TTA Catalog C dipole is +0.43σ (p = 0.30, isotropic-null bootstrap) … The post-MASTER canonical-mask direct-MC residual is +3.64σ …” (two different nulls, no local reminder).  
• Sec. III A / Table I: multiple σ’s (+0.43, −0.122, +3.64, …) in a single summary table with different null types but only the initial global note.  
Required fix: Each place where σ’s from distinct nulls appear adjacently (in the same sentence, table row set, or bullet) must carry a clear local disclaimer that they are not directly comparable across estimators. Add a parenthetical or column note each time (e.g. “σ values not directly comparable across these rows; see null column”).

---

P4-E7 (ESSENTIAL)  
Section: Abstract and Sec. IV C (pages 1, 4–5) – headline σ and p-value traceability  
Text: “+0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000)” and “−0.122σ (500-MC label-shuffle null)” plus Table III values (C1meas, ⟨C1null⟩, σnull).  
Problem:  
• The paper does not display the bootstrap distribution or the exact dipole amplitude and its bootstrap variance; hence the reader cannot recompute +0.43σ or p = 0.30 from shown numbers.  
• For the ℓ = 1 MASTER result, Table III gives C1meas, ⟨C1null⟩ and σnull; computing \((1.494-1.546)/0.429 ≈ -0.121\) reproduces −0.122σ, which is fine. But for the 0.43σ and p = 0.30 in real space, there is no corresponding amplitude or variance displayed anywhere, so the headline statistic is not auditable.  
Required fix: Add the numeric best-fit dipole amplitude and its null distribution standard deviation (or equivalent statistic) for the real-space estimator, so that 0.43σ and p = 0.30 can be recomputed from displayed numbers. PRD expects all “headline” σ and p-values in the abstract to be checkable from the body.

---

P4-E8 (ESSENTIAL)  
Section: Abstract & Sec. VII (pages 1, 6–7) – falsification criterion  
Text: “A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null.”  
Problem: “Falsify the present null” is ambiguous logically. The present analysis’s null is strictly *about this catalog / pipeline*, not a fundamental cosmological null. A future detection with a different survey, selection, and systematics budget does not logically “falsify” the current *measurement*; it would only be in tension with the combination of current data and assumptions. PRD is sensitive to over-strong statements of falsification beyond the scope of the actual test.  
Required fix: Rephrase the falsification language to make clear that such a future detection would be *in strong tension with* or *inconsistent with* the bounds implied by this analysis under similar assumptions, not a falsification in a strict, universal sense. 

---

P4-E9 (ESSENTIAL)  
Section: Morphology/edge-on discussion & sensitivity (pages 6 & 9, Appendix E)  
Text: “Edge-on galaxy contamination (65.7% of b/a < 0.3 objects receive CW/CCW labels rather than not spiral) reduces effective sample size by ∼ 10–15%, corresponding to a ∼ 5–8% sensitivity penalty.”  
Problem: The numbers 10–15% and 5–8% are presented as quantitative impacts but are not recomputable from any displayed counts. We see 65.7% in the text, but we are not given total edge-on counts or how that maps to an effective N reduction and hence σ scaling. The quoted sensitivity penalty is therefore unsupported by visible calculation.  
Required fix: Add explicit numbers: total galaxies with b/a < 0.3, their fraction of the spiral sample, and the simple scaling argument leading to “10–15% reduction in effective sample size” and hence “5–8% sensitivity penalty” (e.g. via σ ∝ 1/√N). Alternatively, clearly mark these as rough back-of-the-envelope estimates rather than quantitative results.

---

P4-E10 (ESSENTIAL)  
Section: Abstract & Sensitivity floor (pages 1, 6)  
Text: “Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).”  
Problem:  
• The paper does not show the actual formula used to compute σ(A/2) = 0.048%; it is plausible (∝ 1/√N) but not shown.  
• There is an internal inconsistency: the main Nspiral used in the injection test is 471,049 (HC subsample), yet the Fisher floor is computed with 3,201,160 spirals and fsky = 0.46. The link between this Fisher floor and the empirical injection threshold (A ≈ 0.75%) is not numerically worked through in the text; the “true-underlying threshold ∼ 1.88%” uses a “GZ1-dilution factor g ≈ 0.398” but no explicit formula is given to check 0.75% / 0.398 ≈ 1.88%.  
Required fix: Provide the explicit equations for σ(A) and the dilution correction, and show the calculation that leads to 0.29%, 0.75%, and 1.88% from the stated N and g. Without these steps, a referee cannot verify that the “sensitivity floor” numbers are consistent.

---

P4-M1 (MAJOR)  
Section: Introduction and Sec. V A (pages 2 & 5–6) – “disfavors” Shamir amplitudes “by a factor of ∼ 6–12”  
Text: “This is inconsistent in amplitude with Shamir’s claimed ∼ 3% signal by a factor of ∼ 6–12 under the present pipeline, though a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion.” And later: “disfavors the Shamir ∼ 2–4% detection class at the amplitude level under our pipeline.”  
Problem:  
• The factor 6–12 is defined as 0.75% vs 2–4% (roughly), but the manuscript does not carefully propagate classification noise, mask differences, or selection functions between SDSS+Pan-STARRS / DESI Legacy and the present catalog.  
• It is not demonstrated that the current estimator has equal or better sensitivity *on the Shamir footprints*; the text itself admits that a “matched-footprint Ganalyzer reanalysis is required.”  
Required fix: Soften the language: say that under the assumptions and mask of this work, amplitudes in the 2–4% range would have been detected at >>3σ, and thus such amplitudes are disfavored *for DESI Legacy spirals under this classifier*, but do not present this as a direct tension with Shamir’s SDSS-based claims without doing the matched-footprint analysis. Explicitly state the survey and methodology differences.

---

P4-M2 (MAJOR)  
Section: Sec. IV D & Table IV (pages 4–5) – 99.3% reproduction of leakage  
Text: “The monopole-only null reproduces 99.3% of the observed pre-MASTER pseudo-Cℓ(ℓ=1) power (residual +1.68σ).” Table IV lists Data 1.696×10−2 vs null (1.685±0.007)×10−2.  
Problem:  
• 1.685 / 1.696 ≈ 0.9945, i.e. 99.45%. The stated 99.3% is fine as rounding, but the reader must infer that the ratio is null mean / data and not e.g. (data - null)/data.  
• “Residual +1.68σ” is the z-score of the data relative to the null mean and σnull (0.007×10−2), but that is not explicitly shown. Also, it is unusual to call a +1.68σ offset “reproduces 99.3%” without specifying that 1.7σ deviations are expected in 1D.  
Required fix: Add an explicit equation showing that 99.3% is ⟨Cℓ,null⟩/Cℓ,data, and that the +1.68σ residual corresponds to (Data − Null)/σnull, and clarify that this level of mismatch is statistically modest. That will make the “99.3%” statement interpretable and auditable.

---

P4-M3 (MAJOR)  
Section: Equations (2) and (3) (pages 3–4) – notation and dimensional consistency  
Equation (2):  
\[
P_{\rm CW}^{\rm eq} = \tfrac12 P_{\rm CW}^{\rm orig} + P_{\rm CCW}^{\rm flip}, \quad
P_{\rm CCW}^{\rm eq} = \tfrac12 P_{\rm CCW}^{\rm orig} + P_{\rm CW}^{\rm flip}, \quad
P_{\rm NS}^{\rm eq} = \tfrac12 P_{\rm NS}^{\rm orig} + P_{\rm NS}^{\rm flip}.
\]  
Problem:  
• The factors “1/2” are written only on the first term in each line; as printed, this reads like \(P^{\rm eq} = 0.5 P^{\rm orig} + P^{\rm flip}\), which would not preserve normalization. It is almost certainly intended to be \(P^{\rm eq} = (P^{\rm orig} + P^{\rm flip})/2.\)  
Required fix: Rewrite Eq. (2) with clear parentheses or split the 1/2 so it multiplies the sum explicitly, e.g.  
\(P_{\rm CW}^{\rm eq} = \tfrac12 (P_{\rm CW}^{\rm orig} + P_{\rm CCW}^{\rm flip})\), etc. Verify that the printed LaTeX will compile unambiguously.

Equation (3):  
\(A_p = (N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)})/(N_{\rm CW}^{(p)} + N_{\rm CCW}^{(p)})\).  
Problem: No units issue; this is dimensionless and fine. This is included here only to note that the asymmetry is later also defined in Appendix A with \(N_{\rm total}\) in the denominator; the paper uses two slightly different normalizations without making that distinction obvious.  
Required fix: Clarify early that there are two versions of the asymmetry field (spiral-only vs total-count-weighted) and explicitly label them (e.g. A_p^{spiral}, A_p^{all}) so the reader can track which is used where.

---

P4-M4 (MAJOR)  
Section: Claims of “largest galaxy chirality catalog to date” (Sec. VII, page 6–7)  
Text: “We have constructed and analyzed the largest galaxy chirality catalog to date: 8,474,531 galaxies…”  
Problem: CE-ResNet [7] claims ∼1.95 million galaxies with chirality labels; Shamir 2020+2022 and Tadaki 2020 have varying counts in the 10^5–10^6 range. The 8.47M total sample here includes a majority (∼5.3M) objects labeled “not spiral”; only 3.2M have spiral chirality labels. The “largest chirality catalog” claim is ambiguous: is “chirality catalog” defined by total galaxies with any morphological label, or by galaxies with actual CW/CCW assignments? If the latter, the advantage in spirals is “1.6× CE-ResNet’s scale” (3.2M vs 1.95M), which is indeed bigger, but this nuance is not clear.  
Required fix: Clarify the definition of “largest” and explicitly state that this is the largest *spiral-chirality* catalog (3.2M spirals), and that the total catalog also includes NS/edge-on labels. Remove any ambiguous implication that 8.47M spirals have chirality labels.

---

P4-M5 (MAJOR)  
Section: “AI tool usage” (page 9–10)  
Text: “AI tool usage: Large-language-model tools were used for code review and manuscript editing; all scientific results are derived from the authors’ own analysis…”  
Problem: PRD is still developing policies around generative AI usage. Stating this is not intrinsically wrong, but it is unusual for a main-text section and may conflict with publisher guidelines. Moreover, it is not referenced anywhere in the body and reads like internal compliance prose.  
Required fix: Move this content, if required by the journal, into a dedicated “Author Contributions / AI tools” section following PRD’s policy, or remove it. It should not sit as free-form prose in the main manuscript without context.

---

P4-M6 (MAJOR)  
Section: BACKMATTER – URL formatting and typography (pages 9–10)  
Examples:  
• “https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog”  
• The word “galaxy- chirality- catalog” split by spaces around hyphens.  
Problem: These spacing artifacts indicate that the manuscript text is not reflecting actual checked URLs (they would 404 even if “bamfai/…” existed). For a methods paper whose core contribution is a catalog and code release, such sloppiness in the key links undermines reproducibility.  
Required fix: Correct all URLs to valid syntax (no stray spaces, correct `datasets/` path on HuggingFace) and ensure they resolve. This is distinct from E2 (existence); here the typography itself must be fixed even once real repositories exist.

---

P4-M7 (MAJOR)  
Section: Main text & Appendices – length vs. contribution  
Observation: The paper runs to 10 dense pages plus appendices, with substantial space spent on pipeline operational details, bias tests, and narrative around systematics. The core scientific content (a null dipole and identification of monopole-mask leakage) could be presented in considerably fewer pages. PRD expects efficient presentation for a single null result.  
Required fix: Condense repetitive discussion of the canonical-mask residual and bias tests into a more compact section, keeping necessary detail for reproducibility but aiming for ≈7–8 pages main text. Move most diagnostic elaboration into an online supplement if allowed.

---

P4-Min1 (MINOR)  
Section: Abstract (page 1)  
Text: “Interpretation (iii) sharp-edge variant is disfavored…” and later “Interpretation (ii) is attributed…”  
Problem: The abstract spends substantial space on internal interpretation labels (i/ii/iii) and detailed diagnostics, which are not clearly defined until later. For PRD, the abstract should focus tightly on what is *demonstrated*, not internal hypothesis bookkeeping.  
Required fix: Simplify the abstract so that it states: (1) catalog size and method; (2) main dipole null result with its estimator and null; (3) existence and nature of the canonical-mask systematic; (4) overall implication for previous claimed signals. Reserve the (i/ii/iii) labels and detailed diagnostics for the main text.

---

P4-Min2 (MINOR)  
Section: Appendix A and main text – use of “MASTER” vs “NaMaster”  
Problem: The paper uses “MASTER” to refer to the pseudo-Cℓ deconvolution method (Hivon et al. 2002) and “NaMaster/pymaster” for the implementation, but the terminology occasionally blurs (e.g. “canonical-N MASTER recompute”). For non-CMB readers, this can be confusing.  
Required fix: Add a sentence early in Sec. III or Appendix A explicitly stating: “We use NaMaster’s implementation of the MASTER pseudo-Cℓ method [refs]. We refer to the algorithm as MASTER and to the code as NaMaster/pymaster.” Ensure consistent use thereafter.

---

P4-Min3 (MINOR)  
Section: Table III caption (page 5)  
Text: “The canonical-N MASTER direct-MC at ℓ = 1 on the canonical mask yields +3.64σ (Sec. IV D), a non-headline, systematics-attributed canonical-mask excess.”  
Problem: The caption mixes result interpretation (“non-headline, systematics-attributed”) with descriptive labeling. PRD prefers neutral captions, with interpretation in the text.  
Required fix: Trim the caption to purely descriptive content (e.g. “The ℓ = 1 canonical-mask result is +3.64σ; see Sec. IV D for interpretation as a survey systematic.”).

---

P4-Min4 (MINOR)  
Section: Section headings and internal references (pages 3–8)  
Problem: Some internal references are slightly vague, e.g. “Full systematic analysis is in Appendix D” without a short indication of which aspects are covered (leg-proxies, density stratification, etc.). For a methods-heavy paper, more precise roadmap language would improve readability.  
Required fix: When pointing to appendices, add a brief descriptive clause: “Full systematic analysis of the canonical-mask residual (including leg-proxies, density stratification, boundary-distance tests, and WLS template fits) is in Appendix D.”

---

P4-Min5 (MINOR)  
Section: PACS numbers & modern classification (page 1)  
Problem: PACS has been deprecated; many PRD articles now rely on keywords instead. Including PACS is not wrong but somewhat out of date.  
Required fix: Check PRD’s current classification requirements. If PACS are still allowed, optionally add a set of modern keywords; if not, remove the PACS line.

---

P4-N1 (NIT)  
Section: Title (page 1)  
Text: “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ = 1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual…”  
Problem: The title is extremely long and packed with jargon (TTA, MASTER, subsample-mask, canonical-mask, etc.). PRD typically prefers more concise titles.  
Required fix: Shorten the title to convey the main result, e.g. “Survey-Scale Galaxy Chirality with Equivariant Averaging: A Null ℓ = 1 Dipole and Mask-Induced Systematics in DESI Legacy Data” or similar.

---

P4-N2 (NIT)  
Section: Typos and spacing (all pages)  
Examples:  
• “galaxy- chirality- catalog” (extra spaces around hyphens).  
• “D4 -TTA” instead of “D4-TTA”.  
• Occasional extra spaces before punctuation (e.g., “parity-EVEN :”).  
Required fix: Run a careful copy-edit pass to remove spurious spaces, ensure hyphens are attached correctly, and standardize typography.

---

P4-N3 (NIT)  
Section: Miscellaneous repetition  
Example: “The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥ 0.75%… including the Shamir ∼ 3% amplitude class by a factor of ∼ 6–12.” This repeats information given earlier in slightly different words.  
Required fix: Reduce repetition; state this constraint once clearly and refer back as needed.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The central methodology and cosmological content are potentially valuable, but the paper in its current form does not meet PRD standards. There are serious issues with citation metadata (notably a fused Shamir 2022 PASJ reference), unverifiable or non-existent code/data releases presented as already public, incomplete auditability of headline statistics, and over-strong claims about tension with prior work without matched-footprint analysis. Multiple σ’s from different nulls are juxtaposed without the repeated “not comparable” caveat required by the provided instructions. These problems must be corrected, and the presentation streamlined, before the manuscript can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E11 (ESSENTIAL)  
Section: Abstract, Sec. III A, Table II – global CW fraction σ and excess percentages  
Problem (A – arithmetic; J – stale numbers):  
- Table II states for Catalog C: `cw/(cw+ccw) = 0.4974 ± 0.000279` with “Excess (%) = −0.26” and “Dev. (σ) = 9.5”. Using the standard binomial σ quoted in the caption, \(σ = \sqrt{p(1-p)/N}\) with \(p=0.4974\), \(N=3{,}201{,}160\) yields \(σ ≈ 0.000279\), so the *significance* of the deviation from 0.5 is \((0.4974-0.5)/0.000279 ≈ -9.35σ\), i.e. ~9.3σ in magnitude, not 9.5σ.  
- Similarly, 0.4974 vs 0.5 is a −0.26 percentage-point difference relative to 0.5, i.e. −0.52% full asymmetry. The text in Sec. IV B states: “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates…”. 2.05/0.53 ≈ 3.87, consistent with 3.86, but the −0.53% does not match the −0.52% implied by 0.4974; one of these is stale.  
Required fix:  
- Recompute the Catalog C dev(σ) and excess % from the exact numbers, and either adjust the 9.5σ and −0.53% values or quote them with consistent rounding (e.g. 9.3σ, −0.52%).  
- Ensure that the 3.86× suppression factor is recomputed from the final, consistent raw and equivariant monopole values; if 2.05% and 0.52% are used, the ratio should be updated accordingly.  

---

P4-E12 (ESSENTIAL)  
Section: Table III and Appendix D (multipole significances)  
Problem (A – arithmetic; J – stale numbers):  
- Table III lists for the bandpowers:  
  * ℓeff = 4: Cℓ = 3.210, σnull = 0.804, “Significance = +6.097σ”. The ratio 3.210/0.804 ≈ 3.99, not 6.10.  
  * ℓeff = 9: Cℓ = −0.248, σnull = 0.574, “Significance = +2.232σ”. |−0.248|/0.574 ≈ 0.43, not 2.23.  
  * ℓeff = 14: Cℓ = −0.387, σnull = 0.446, “Significance = +2.626σ”. |−0.387|/0.446 ≈ 0.87, not 2.63.  
  * ℓeff = 19: Cℓ = −0.576, σnull = 0.420, “Significance = +2.229σ”. |−0.576|/0.420 ≈ 1.37, not 2.23.  
  * ℓeff = 24: Cℓ = −0.648, σnull = 0.366, “Significance = +2.470σ”. |−0.648|/0.366 ≈ 1.77, not 2.47.  
- These cannot all come from \(z = (C_\ell - \langle C_{\ell,\text{null}}\rangle)/σ_{\text{null}}\), because no null means are shown that would lead to these z-scores, and the signs (negative Cℓ vs positive “Significance”) are inconsistent.  
- Appendix D describes “σℓ=1 = +3.63, σℓ=2 = +4.73 (ℓ = 3, 4, 5 at −0.96, +0.13, −0.63)” for a separate multipole diagnostic, but Table III’s significances do not correspond numerically to those values either, suggesting a mixture of old and new analyses.  
Required fix:  
- For each row of Table III, show explicitly the null mean used and define the z-score formula. Recompute the “Significance (σ)” entries from the displayed Cℓ, ⟨Cℓ,null⟩, and σnull, and ensure the sign and magnitude are correct.  
- Align the multiplicity of σℓ values reported in Appendix D with those in Table III; if the appendix uses a different pipeline, state that explicitly and avoid quoting σ’s that can be confused with the Table III entries.  

---

P4-E13 (ESSENTIAL)  
Section: Table I, estimator descriptions and values  
Problem (A – arithmetic; E – comparability; J – stale numbers):  
- For estimator (ii) “MASTER deconv”, Table I lists Ncatalog spiral = 3,201,160 but Nmap weighted = 5,547,858. Appendix A clarifies that Nmap,weighted is the sum of pixel weights Wp = Nall(p), which counts *all* galaxies per pixel (spiral + NS), not just spirals. The caption, however, defines Nmap weighted as “the total classified-galaxy count in pixel p … used as a survey-depth weight”, and then says “Nmap weighted exceeds Ncatalog spiral because Wp includes non-spiral galaxies (∼62% of the catalog); each galaxy is counted once.” This is consistent conceptually, but the ratio 5.55M / 8.47M ≈ 0.66 suggests that the map excludes all pixels with <10 spirals; many galaxies are therefore not counted in Nmap weighted even though the caption implies “each galaxy is counted once.”  
Required fix:  
- Clarify that Nmap weighted counts galaxies only in pixels that pass the NSIDE=64, ≥10-spirals mask, so it does not equal the total catalog count; remove or rephrase “each galaxy is counted once” to avoid misinterpretation.  
- Add a sentence explaining the fraction of the full catalog that ends up inside the weighted map (e.g. “Nmap weighted corresponds to X% of the full 8.47M sample because pixels below the spiral-count threshold are excluded”).  

---

P4-E14 (ESSENTIAL)  
Section: Sec. VI A & Appendix A – Fisher floor and σ(A/2) formula  
Problem (C – dimensional consistency; A – arithmetic; J – traceability):  
- Sec. VI A states: “The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” No explicit formula is given for σ(A/2), despite this quantity being central to the advertised sensitivity floor.  
- Using a naïve Poisson scaling for a dipole-like asymmetry, one would expect σ(A/2) to scale approximately as \(1/\sqrt{N_{\rm eff}}\), but the introduction of fsky = 0.46 is not tied to any equation. The master analysis elsewhere uses masks with fsky = 0.659 and 0.49005, not 0.46, generating confusion about which effective sky fraction enters the Fisher estimate.  
Required fix:  
- Present the explicit equation used for σ(A/2) and explain how fsky enters, including the definition of \(N_{\rm eff}\). Show the numerical substitution that yields 0.048% and hence the quoted 0.29% 3σ threshold.  
- Explain why fsky = 0.46 is adopted for the Fisher floor (e.g. an effective area after quality cuts), and reconcile that with the different fsky used for the MASTER and canonical analyses.  

---

P4-E15 (ESSENTIAL)  
Section: Sec. VI A & Appendix E – edge-on contamination sensitivity penalty  
Problem (A – arithmetic; H – unquantified hedges):  
- The main text says: “Edge-on galaxy contamination … reduces effective sample size by ∼ 10–15%, corresponding to a ∼ 5–8% sensitivity penalty.” Appendix E repeats: “We estimate ∼ 10–15% reduction in effective sample size, corresponding to a ∼ 5–8% sensitivity penalty.”  
- No explicit counts are given: we are not told the total number of edge-on galaxies, nor what fraction of the spiral sample they represent, nor how the 10–15% is computed. The quoted sensitivity penalty assumes a scaling ∝ 1/√N but is not shown numerically.  
Required fix:  
- Add explicit numbers: the count of b/a < 0.3 objects, their fraction of the spiral sample, and a short derivation showing why the effective N reduction is 10–15% and how that leads to 5–8% sensitivity loss via σ ∝ 1/√N.  
- Alternatively, explicitly flag these as back-of-the-envelope estimates (e.g. “we crudely estimate …”) rather than quantitative results.  

---

P4-E16 (ESSENTIAL)  
Section: Sec. V A & VII a–d – “disfavors” Shamir amplitudes and “factor of ∼6–12”  
Problem (H – unquantified hedges; G – unsupported novelty/tension):  
- Multiple places state that the present work “disfavors the Shamir ∼ 2–4% detection class at the amplitude level under our pipeline” and that the result is “inconsistent in amplitude with Shamir’s claimed ∼ 3% signal by a factor of ∼ 6–12.” The 6–12 factor is defined from 0.75% vs 2–4%, but the linkage to Shamir’s specific effective footprints, selection, and classification noise is not quantified; the wording reads as a broad claim of tension.  
- While the text acknowledges that a “matched-footprint Ganalyzer reanalysis is required,” it does not numerically propagate the classification-noise dilution, mask differences, or effective N for Shamir’s samples in order to support a σ-level tension claim; nor does it quantify the σ-level at which a 3% amplitude would have been detected in the current DESI footprint given the demonstrated sensitivity.  
Required fix:  
- Replace “disfavors” and “inconsistent … by a factor of ∼ 6–12” with language that clearly frames this as an internal consistency statement *within the DESI + ViT/TTA pipeline* (e.g. “would have been detectable at >>3σ under our assumptions”).  
- Provide a short quantitative estimate of the expected σ for A = 2–4% under the current null and Nspiral, or else explicitly say that no rigorous likelihood comparison is made and the factor-of-6–12 statement is only a heuristic amplitude comparison.  

---

P4-E17 (ESSENTIAL)  
Section: Abstract, Sec. I, Sec. VII d – “null dipole at sub-percent sensitivity”, “≥10⁷ galaxies”  
Problem (F – abstract faithfulness; H – unquantified hedges; J – stale numbers):  
- The abstract and Sec. I describe the work as providing a “null dipole at sub-percent sensitivity” and Sec. VII d re-states “empirical 50%-recovery-at-3σ threshold is A ≈ 0.75% (full amplitude) … The catalog is a community resource … A future survey detecting a chirality dipole at σ > 5 with amplitude ≳ 0.75% at ≥ 10⁷ galaxies would falsify the present null.”  
- The ≥10⁷ galaxies condition is not derived anywhere, and the sensitivity scaling from the present Nspiral = 3.2M to a future 10⁷-galaxy survey is not shown. Without an explicit scaling law, the abstract-level “sub-percent sensitivity” and the ≥10⁷-galaxy falsification criterion are not quantitatively supported by the body.  
Required fix:  
- Either remove the explicit “≥10⁷ galaxies” condition, or add a short calculation in Sec. VI A (or VII d) showing how the sensitivity scales with N and why 10⁷ galaxies is the relevant benchmark for future surveys.  
- Clarify that “sub-percent sensitivity” specifically refers to the empirically demonstrated 0.75% amplitude threshold under the present null, rather than implying sensitivity well below 0.5%.  

---

P4-M8 (MAJOR)  
Section: Abstract, Sec. IV C, Table I – real-space dipole σ and p-value  
Problem (A – arithmetic; E – comparability; F – faithfulness):  
- The abstract and Sec. III A report a real-space dipole significance of “0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000).” The body does not display the underlying amplitude or variance; this was already noted in P4-E7. Additional issue: a one-sided 0.43σ excursion corresponds to p ≈ 0.33; a two-sided p ≈ 0.67. A quoted p = 0.30 is plausible for Monte Carlo but cannot be verified without seeing the rank ordering of the bootstrap outcomes.  
Required fix:  
- Add the actual measured dipole amplitude, its bootstrap mean and standard deviation (or empirical distribution), and a statement clarifying whether p = 0.30 is one-sided or two-sided.  
- Recompute p from the stored bootstrap samples and display a rounded value consistent with those samples.  

---

P4-M9 (MAJOR)  
Section: Sec. IV D, Table IV – 99.3% reproduction and +1.68σ residual  
Problem (A – arithmetic; C – dimensional/logical clarity; J – stale numbers):  
- Table IV gives Data = 1.696×10⁻² and Null = (1.685±0.007)×10⁻²; the text states that the null “reproduces 99.3% of the observed … power (residual +1.68σ).” The ratio 1.685 / 1.696 ≈ 0.9945, i.e. 99.45%, not 99.3%, and (1.696−1.685)/0.007 ≈ 1.57σ, not 1.68σ. Both numbers can be consistent only if the underlying mean or σ changed and the descriptive text wasn’t updated.  
Required fix:  
- Recompute ratio = ⟨Cℓ,null⟩ / Cℓ,data and z = (Data − Null)/σnull, and update both 99.3% and +1.68σ to match the final numbers, or update Table IV’s Null and σnull so they agree with 99.3% and 1.68σ.  
- Add a brief line in Sec. IV D explicitly defining these quantities, as requested in P4-M2, so the reader can recompute them unambiguously.  

---

P4-M10 (MAJOR)  
Section: Appendices A vs main text – asymmetry field definitions  
Problem (C – dimensional consistency; I – appendix vs main mismatch):  
- Eq. (3) defines \(A_p = (N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)})/(N_{\rm CW}^{(p)} + N_{\rm CCW}^{(p)})\) using only spiral counts in the denominator. Appendix A, however, defines the field used for the MASTER analysis as \(A_p = (N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)})/N_{\rm total}^{(p)}\), where \(N_{\rm total} = N_{\rm CW}+N_{\rm CCW}+N_{\rm NS}\).  
- The main text does not clearly label these as distinct observables (spiral-only vs total-count-weighted asymmetry), and some prose refers generically to “the asymmetry map” without indicating which normalization is in play.  
Required fix:  
- Explicitly define two symbols (e.g. \(A_p^{\rm spiral}\) and \(A_p^{\rm all}\)) and state which is used in each analysis step (real-space dipole vs MASTER pseudo-Cℓ).  
- Ensure all references in the main text and captions specify which version is used so that the reader can reconcile Eq. (3) with the Appendix A definition.  

---

P4-M11 (MAJOR)  
Section: Sec. II B, Appendix B – training/validation statistics and CE-ResNet dependence  
Problem (H – hedges; F – abstract faithfulness):  
- The paper states in Sec. II B: “67.6% of training labels derive from CE-ResNet predictions; validation metrics against the full training set therefore partially reflect agreement with CE-ResNet rather than independent ground truth.” Yet the abstract positions the catalog as a “bias-hardened Vision Transformer” product and emphasizes “multi-axis bias-hardening.” There is no quantitative breakdown of performance versus *independent* labels (e.g. pure GZ1 subset) beyond the single “69.91% accuracy” number.  
- Given the heavy reliance on CE-ResNet pseudo-labels, the abstract’s claims about “advancing beyond CE-ResNet in three respects” understate the degree to which the classifier inherits CE-ResNet’s label systematics and overstate the independence of the pipeline.  
Required fix:  
- Add a brief quantitative comparison: e.g., report accuracy and bias separately on a CE-ResNet-free validation subset (only human-labeled galaxies) and state how much of the bias-hardening is validated against that subset.  
- Soften abstract language to acknowledge that a majority of labels are CE-ResNet-derived and that some systematics may be inherited; emphasize that the key novel contribution is the *dipole analysis and systematics audit*, not an entirely independent chirality labeling scheme.  

---

P4-M12 (MAJOR)  
Section: Abstract & Sec. I – “standalone observational result” vs reliance on external pseudo-labels  
Problem (F – abstract faithfulness; H – hedges):  
- The introduction states: “The present paper is a standalone observational result: our null dipole at sub-percent sensitivity does not depend on any unpublished companion work.” While formally true regarding unpublished work, the analysis depends crucially on the Smith42/galaxies parent sample and the CE-ResNet pseudo-labels used for training.  
- “Standalone” could be interpreted by readers as not heavily reliant on prior machine-learning catalogs, whereas in reality 67.6% of labels originate from CE-ResNet.  
Required fix:  
- Rephrase “standalone observational result” to make clear that the work is methodologically self-contained *given* public imaging and CE-ResNet/GZ1 labels, but that systematic inheritance from those inputs is possible.  

---

P4-Min4 (MINOR)  
Section: Sec. III C and Appendix B – D4-TTA diagnostics  
Problem (A – arithmetic; H – hedges):  
- Appendix B states that D4-TTA per-galaxy argmax labels flip in “21.4% of cases between Z2 and D4 on borderline galaxies with PCW ≈ PCCW ≈ 0.4”, and that the sign flip in argmax-CW-fraction shift (−1.35% vs +2.11%) “confirms sample-noise on a fragile argmax statistic rather than a real D4-TTA systematic.” These percentages and shifts are not connected to any global error budget; the main text does not quantify how such 21% argmax instability feeds into the σ(A) budget or the injection threshold.  
Required fix:  
- Add a short quantitative statement (even approximate) of how the observed D4 vs Z2 instability would translate into an additional classification-noise component in σ(A), or explicitly state that these diagnostics are qualitative and not folded into the formal sensitivity estimate.  

---

P4-Min5 (MINOR)  
Section: Sec. V B – “1.6× CE-ResNet’s scale”  
Problem (A – arithmetic; G – novelty claims):  
- The text claims “3,201,160 equivariant-classified spirals, 1.6× CE-ResNet’s scale” compared to CE-ResNet’s 1.95M galaxies. The ratio 3.20M / 1.95M ≈ 1.64; 1.6× is fine as a rounded figure. However, the comparison mixes “spiral coverage” with “galaxies used by CE-ResNet,” and the abstract’s “largest galaxy chirality catalog” language could be read as claiming a larger *chirality-labeled* sample rather than total survey coverage.  
Required fix:  
- Make explicit that the 1.6× factor refers to the number of galaxies with spiral chirality labels (3.2M vs 1.95M), not total galaxies processed. Slightly rephrase “largest galaxy chirality catalog” in the abstract to “largest spiral-chirality catalog (3.2M spirals)” to reduce ambiguity (this overlaps with P4-M4 but here is tied directly to the numeric ratio).  

---

P4-Min6 (MINOR)  
Section: Data Availability, Abstract – “publicly available on HuggingFace (CC-BY-4.0)”  
Problem (J – stale numbers/claims):  
- The paper asserts that the catalog, model weights, and scripts are “publicly released at the project repository” and “publicly available on HuggingFace (CC-BY-4.0)” with specific paths and a release tag v2026.04. At present, these URLs are non-functional, and no DOI or arXiv identifier is provided. This is already noted in P4-E1/E2/E6, but there is an additional abstract-level faithfulness issue: the abstract presents the catalog release as *current* rather than conditional on publication.  
Required fix:  
- Adjust the abstract and Data Availability wording to be prospective (“will be released upon publication”) unless the repositories are online and verifiable now, in which case provide a persistent identifier and confirm all URLs and tags correspond to actual resources.  

If you implement these fixes alongside the issues already identified in the initial review, most of the hidden arithmetic, traceability, and language problems that often trip PRD referee checks should be addressed.