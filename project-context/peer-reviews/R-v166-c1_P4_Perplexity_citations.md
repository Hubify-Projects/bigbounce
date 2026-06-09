# P4 R-v166-c1 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (8683 chars)
**Wall time**: 78.8s

---

P4 REPORT – CITATION & METHODS FORENSICS (DESI CHIRALITY PAPER)

I cannot access arXiv/ADS directly from the PDF you provided, so I rely on web search for each cited item and cross‑check against the paper’s claims. Below I list all concrete problems I can identify from the supplied text plus searches.

---

### P4‑E1 (ESSENTIAL) – Mis‑cited Shamir 2022 paper and fused metadata  
- **Location:** References [2], [3], p.14; text p.2 (“Shamir (2020) [1] and Shamir (2022) [3] …”) and p.8.  
- **Problem:**  
  - Ref. [2] is given as: *“L. Shamir, ‘Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,’ PASJ 74, 1114 (2022), DOI:10.1093/pasj/psac058.”*  
  - Ref. [3] is: *“L. Shamir, ‘Analysis of spin directions of galaxies in the DESI Legacy Survey,’ MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.”*  
  - Web search confirms [3] (MNRAS DESI Legacy paper) is correct.[1]  
  - For [2], searching PASJ 74, 1114 and DOI 10.1093/pasj/psac058 shows that this is indeed a Shamir PASJ paper on spin directions, but the exact title used in the paper must be checked against the journal metadata – the supplied text is plausible but slightly paraphrased compared to typical PASJ titles.  
  - Additionally, in the *Introduction* the text says: “Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼2–4% asymmetries on DESI Legacy samples.” But Shamir (2020) [1] is an SDSS+Pan‑STARRS analysis, not DESI Legacy; DESI Legacy is Shamir (2022) MNRAS ([3]) only.  
- **Required fix:**  
  - Verify the exact title of the PASJ Shamir 2022 paper in [2] against PASJ; if the wording is not exact, correct it to the published title.  
  - In the text on p.2, restrict “DESI Legacy samples” to Shamir (2022) MNRAS only (Ref. [3]) and state clearly that Shamir (2020) [1] is SDSS/Pan‑STARRS, not DESI Legacy.  
  - Ensure that wherever Shamir (2020) is referenced as DESI Legacy, that wording is corrected.

---

### P4‑E2 (ESSENTIAL) – Unverified numerical claim for CE‑ResNet cw/ccw = 0.998  
- **Location:** Abstract (p.1): “Jia et al.  … yielding cw/ccw = 0.998 on ∼1.95 million galaxies.” Also in Comparison with CE‑ResNet (p.8).  
- **Problem:**  
  - Reference  is *H. Jia, H.-M. Zhu, and U.-L. Pen, “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” ApJ 943, 32 (2023), arXiv:2210.04168.*  
  - The statement “cw/ccw = 0.998” is clearly a ratio extremely close to 1, but the paper text treats it as a *metric* of near‑perfect balance between CW and CCW. Without reading Jia et al. directly, I cannot confirm that 0.998 is actually quoted in that paper, nor that it refers to the **global CW fraction** rather than some other diagnostic (e.g., parity-symmetry test, confusion‑matrix element, or structural parameter).  
  - PRD‑level standards require that such a load‑bearing numerical comparison be traceable to a specific table or figure in . That cross‑reference is not given.  
- **Required fix:**  
  - Explicitly cite where in Jia et al. (2023) the value 0.998 comes from (table/figure/equation) and clarify what quantity it is (e.g., cw/(cw+ccw), parity‑symmetry metric, etc.).  
  - If 0.998 is *not* a literal published number in  but rather derived from their catalog or plots, say so and briefly describe the derivation; otherwise, remove or correct the number.  
  - Ensure the comparison “Our Catalog C … with cw/(cw+ccw)=0.4974 ± 0.0003 vs CE‑ResNet cw/ccw = 0.998” does not misrepresent ’s result.

---

### P4‑E3 (ESSENTIAL) – Untraceable Shamir amplitude statistics  
- **Location:** Abstract (p.1), Introduction (p.2), Discussion (p.9–10).  
- **Problem:**  
  - The paper repeatedly states that Shamir’s work finds “∼2–4% asymmetries” or “∼3% amplitude” and that the present null is inconsistent by a factor of “∼6–12.” These are central to the comparison claims.  
  - The cited Shamir papers [1]–[4] (2012 Phys. Lett. B; 2020 Astrophys. Space Sci.; 2022 PASJ; 2022 MNRAS DESI Legacy) do report chirality asymmetries, but the exact amplitudes and how they are defined (per‑bin vs. global, fractional vs. difference, etc.) are not explicitly tied here to specific equations or tables in those works.  
  - The numbers “5–20% per-bin asymmetry” (for Shamir 2012) and “2–4% asymmetries” (for Shamir 2020/2022) are quoted without any internal derivation or table reference; a referee cannot trace them from the present paper alone.  
- **Required fix:**  
  - For each quoted Shamir amplitude (5–20% per bin, 2–4%, ~3%), either:  
    - give a parenthetical “(cf. Table X / Fig. Y of [1]/[3])” and ensure the numbers match the cited tables, or  
    - explicitly state that these are approximate values derived by the present author from re‑reading Shamir’s plots, with a one‑sentence explanation of how.  
  - Re‑check that the factor‑of‑6–12 inconsistency claim is computed from consistent definitions of amplitude in Shamir vs. in the present work; if different, say so and avoid implying direct quantitative exclusion.  

---

### P4‑E4 (ESSENTIAL) – σ values from different nulls juxtaposed without local comparability caveat  
- **Location:** Multiple; particularly Abstract p.1, Table I p.4, main text p.4–8, Appendix A–D.  
- **Problem:**  
  - The instructions for this review explicitly require: “If sigma values from different null procedures appear side‑by‑side without explicit ‘not directly comparable’ qualification at every juxtaposition, flag ESSENTIAL.”  
  - The paper has one global statement at the top of Section IV: “Significance … σ from distinct null procedures are not directly comparable.” This is good but not sufficient under the explicit review rule when numbers are juxtaposed closely.  
  - Examples where σ from distinct nulls are presented side‑by‑side with no local caveat:  
    - Table I: rows (i)–(vii) list σ = +0.43 (iso bootstrap), +3.64 (per‑pixel shuffle), +7.28 / +7.13 (two different nulls), +1.68 (monopole‑only null), “50%-rec‑3σ at A=0.75%” all in one table cell; no local “not comparable” warning in the caption.  
    - Table III: ℓ=1 and several bandpowers with σ values all derived from different null constructions.  
    - Section IV C: juxtaposes +0.43σ real‑space dipole, +6.48σ pre‑MASTER pseudo‑Cℓ, +7.28σ post‑MASTER, +3.64σ canonical residual, etc., in contiguous text without repeating the comparability caveat.  
    - Appendix D: many σ’s from different nulls (label‑shuffle, density‑stratified, block‑bootstrap) compared qualitatively without local reminder.  
- **Required fix:**  
  - For every figure/table or contiguous paragraph where multiple σ from different nulls are presented, add a local sentence or footnote explicitly stating that those σ are defined relative to distinct null procedures and *must not* be directly compared as equal‑footing “sigmas.”  
  - In Table I and Table III captions, insert a sentence to this effect and, ideally, name the null type for each row.  
  - Where the text uses qualitative comparison like “+7.28σ vs. +3.64σ,” add “(different nulls; σ not directly comparable)” or rephrase to avoid implying a direct ranking.

---

### P4‑E5 (ESSENTIAL) – Internal version‑history and audit‑log language in body text  
- **Location:** Abstract p.1, Appendix A p.10–11, Appendix C–E footnotes.  
- **Problem:**  
  - The review instructions prohibit “version-history language, internal audit tags (‘R7’, ‘R8’, ‘R-round’), ‘superseded’, ‘earlier draft’, review-log prose, or internal-bookkeeping placeholders” in the body.  
  - The paper repeatedly references prior paper versions and internal audit provenance, e.g.:  
    - Abstract: “Withdrawal note: versions ≤1.0.165 of this paper reported … it is withdrawn — the faithful real-catalog rerun is strongly non-null and systematics-attributed (Appendix A).”  
    - Appendix A: “Versions ≤1.0.165 of this paper reported … A June 2026 provenance audit found … result is therefore withdrawn.”  
    - Multiple “Artifact:” lines with explicit paths like `pipelines/p2_chirality/outputs/canonical_provenance/...json` are internal bookkeeping, not scientific content.  
  - PRD allows errata and clarifications, but embedded versioning and path‑level audit logs are not appropriate for a final article.  
- **Required fix:**  
  - Move all explicit “versions ≤1.0.165,” “June 2026 provenance audit,” and filesystem‑path commentary into a short, clearly marked “Note added in proof” or “Provenance note” subsection, or – preferably – into an arXiv‑only ancillary note and out of the PRD manuscript.  
  - In the main text, retain only the scientifically necessary information: that an earlier analysis using a different mask was based on a synthetic footprint and is no longer used, and that all current headline results use the real catalog.  
  - Remove explicit pipeline path names and “Artifact:” lines; they belong in a README or reproducibility package, not in the physics paper.

---

### P4‑M1 (MAJOR) – Real‑space +0.43σ null vs. +4.31σ monopole‑preserving pseudo‑Cℓ juxtaposition  
- **Location:** Appendix E, footnote attached to the “monopole‑preserving” pseudo‑Cℓ; Section IV C–D references.  
- **Problem:**  
  - The paper explains that a “monopole‑preserving” Catalog‑C full‑footprint pseudo‑Cℓ estimator gives +4.31σ at ℓ=1, while the real‑space dipole is +0.43σ. The footnote argues they are “not directly comparable” because one is heavily contaminated by monopole‑mask leakage.  
  - However, this +4.31σ figure is still presented without a clear, local caution that readers **must not** interpret it as evidence for a dipole on the same footing as the +0.43σ real‑space result.  
  - Given the retraction history for a previous “−0.122σ MASTER ℓ=1 null,” PRD will demand that all such high‑σ pseudo‑Cℓ values be clearly labeled as diagnostic, not cosmological, and that the consistency of various estimators be explained more transparently.  
- **Required fix:**  
  - In the paragraph where +4.31σ is introduced, explicitly mark it as a *non‑headline, systematics‑dominated diagnostic estimator*, analogous to how +3.64σ and +7.28σ are already described.  
  - Add a compact explanatory sentence: e.g. “This 4.31σ is entirely dominated by monopole‑mask leakage and does not indicate a genuine dipole; in contrast, the leakage‑insensitive real‑space estimator is 0.43σ and is the relevant cosmological null.”  
  - Consider moving the +4.31σ number out of the main appendices into a supplemental repository if it is only used operationally.

---

### P4‑M2 (MAJOR) – Incomplete formal link between falsification criterion A₉₅ and injection study  
- **Location:** Abstract p.1, “Falsification criterion” paragraph; Discussion VI.A p.9–10; Appendix D.  
- **Problem:**  
  - The paper states a falsification threshold: “A95 ≈ 1.5–2% is the amplitude at which the present injection‑recovery analysis would have detected a signal at ≥95% probability under the per‑pixel‑shuffle null.” A50≈0.75% is supported by explicit injection statistics (P(σ>3)=0.55 at A=0.75%; P(σ>3)=0.15 at A=0.5%).  
  - However, no explicit quantitative evidence is shown for the **95%** recovery point (A95); the value of 1.5–2% is only stated qualitatively, without tables or a fit that a referee can reconstruct from the text.  
- **Required fix:**  
  - Either add a small table or figure in the main text or appendix giving at least 3–4 injection amplitudes with measured recovery probabilities, including the point where P(σ>3) crosses ~0.95, or remove the specific numeric range “1.5–2%” and state only qualitatively that “A95 is about twice A50.”  
  - Make clear whether A95 is extrapolated from a model fit to the injection‑recovery curve (e.g. logistic fit) or measured directly at specific amplitudes.

---

### P4‑M3 (MAJOR) – Insufficient documentation that all text relying on withdrawn subsample‑mask null has been updated  
- **Location:** Abstract p.1; Appendix A (provenance note); scattered references to “strict‑superset subsample mask” and “synthetic catalog artifact.”  
- **Problem:**  
  - The paper identifies a withdrawn result: an earlier “−0.122σ MASTER ℓ = 1 null on a putative ‘strict-superset subsample mask’ (fsky=0.659).” It now states that this came from a synthetic catalog and is withdrawn.  
  - The abstract says the paper is “re‑anchored on the real-space +0.43σ null + WLS template‑fit exclusion of a clean 1.7% dipole,” and the MASTER pseudo‑Cℓ is “a systematics diagnostic, not an independent cosmological null.”  
  - However, there is no explicit place where the author lists which *sections* of the analysis were affected by the synthetic footprint and confirms that all downstream discussions that might have referred to the old null have been updated. This makes it hard for a referee to certify that “no text still relies on the withdrawn null.”  
- **Required fix:**  
  - Add a short, explicit statement (e.g., at the end of Appendix A): “No quantitative conclusion in Sections IV–VII uses the withdrawn −0.122σ subsample‑mask null; all headline statements rely exclusively on the real‑space dipole and the WLS template‑fit exclusion computed on the real catalog.”  
  - Scan the manuscript and remove any residual wording suggesting that a MASTER ℓ=1 null on fsky≈0.659 carries cosmological weight. Right now, this is implied to be gone, but not demonstrated.

---

### P4‑M4 (MAJOR) – Length relative to claimed contribution  
- **Location:** Entire manuscript (15+ pages including appendices).  
- **Problem:**  
  - The core scientific result is conceptually simple: a null real‑space chirality dipole and a quantified monopole‑mask leakage mechanism on one large survey catalog, plus an injection‑recovery sensitivity floor.  
  - A very large fraction of the paper (especially Appendices B–E) is devoted to internal pipeline diagnostics, bias‑hardening test lists, explicit seed values, and detailed provenance notes better suited to a companion “data release” or code‑release document.  
  - For PRD, this level of operational detail obscures the physics message and makes the paper substantially longer than necessary for the scientific contribution.  
- **Required fix:**  
  - Compress the operational content:  
    - Move detailed pipeline paths, specific seeds, and low‑level architectural hyperparameters into an online supplement or code README.  
    - Condense the eight‑test bias suite into a brief summary table with pointers to code; keep only the elements directly used in physics interpretations.  
    - Shorten or move parts of Appendices C–E that reproduce granular diagnostics whose only function is to support a qualitative statement (“consistent with systematics”).  
  - A target length of ≈10–11 journal pages (main text plus one or two concise appendices) would be more appropriate; keep the rest as online supplementary material.

---

### P4‑m1 (MINOR) – Ambiguous description of “cw/ccw = 0.998” vs. 0.5  
- **Location:** Introduction p.2–3, Comparison with CE‑ResNet p.8.  
- **Problem:**  
  - The phrase “cw/ccw = 0.998” is easy to misread as “the CW fraction is 0.998,” i.e. 99.8% of galaxies CW, which is the opposite of what is intended. It is intended to mean the *ratio* of cw to ccw counts is 0.998.  
- **Required fix:**  
  - Rewrite as, e.g., “with a global CW/CCW *count ratio* of 0.998 (i.e. 49.9% vs. 50.1%)” so that the meaning is unambiguous.

---

### P4‑m2 (MINOR) – Data availability URLs and identifiers  
- **Location:** Data Availability section p.13.  
- **Problem:**  
  - The paper lists HuggingFace and GitHub URLs and a “release tag: v2026.04” but does not provide stable DOIs or arXiv ancillary references. For long‑term reproducibility in PRD, persistent identifiers are strongly preferred.  
- **Required fix:**  
  - Register DOIs for the main catalog and code archive via Zenodo or similar, and cite those DOIs in the Data Availability section (while still keeping human‑readable URLs if allowed).  
  - Ensure that the exact version used for the analysis (commit hash / tag) is clearly stated.

---

### P4‑m3 (MINOR) – Global CW fraction 0.4974 ± 0.000279: consistency check  
- **Location:** Table II, p.5; Abstract p.1.  
- **Problem:**  
  - Binomial σ for p=0.4974 and N=3,201,160 is σ = sqrt(p(1−p)/N) ≈ sqrt(0.25 / 3.2×10⁶) ≈ 2.79×10⁻⁴, consistent with the quoted 0.000279. The deviation from 0.5 is (0.4974−0.5)/σ ≈ −0.0026 / 2.79×10⁻⁴ ≈ −9.3, reasonably close to the quoted −9.5. Minor rounding differences may arise from treating p in the variance.  
- **Required fix:**  
  - No numerical change is strictly required, but consider stating the number of standard deviations with one decimal fewer (e.g. “≈9.3σ”) to avoid implying unwarranted precision.

---

### P4‑m4 (MINOR) – Clarity of “z ≈ −18” notation  
- **Location:** Abstract p.1; Section IV C–D; Appendix D.  
- **Problem:**  
  - The notation “z ≈ −18” is used for the template‑fit disfavor significance, not for redshift, in a context where “z” usually means cosmological redshift. In some places this is clear from context (z = Δ/σ) but in the abstract it can be momentarily confusing.  
- **Required fix:**  
  - In the first occurrence in the abstract, write “z‑score z ≈ −18” or “test statistic z ≈ −18” to avoid confusion with redshift.  

---

### P4‑n1 (NIT) – Minor typographical and style issues  
- **Location:** Various.  
- **Problems & fixes:**  
  - “cw/ccw = 0.998” vs “CW/CCW” – adopt consistent capitalization.  
  - Occasional missing spaces around “≥”, “≲” and between “3σ” and surrounding text; proofread for typographic uniformity.  
  - “chirality-equivariant” vs “chirality equivariant” appears with and without hyphen; choose one convention.  

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific result—a null real‑space chirality dipole with a carefully analyzed mask‑leakage systematic—appears conceptually strong and internally consistent, but several issues prevent PRD‑level acceptance in its current form: (i) the handling of the withdrawn MASTER null and of high‑σ pseudo‑Cℓ estimators needs a cleaner, less version‑laden presentation; (ii) multiple load‑bearing numerical comparisons to previous work (especially Shamir and CE‑ResNet) are not fully traceable to the cited papers; (iii) σ values from different nulls are frequently juxtaposed without local non‑comparability warnings; and (iv) the manuscript is excessively long and operational for the size of the physics result. Addressing the essential and major items above, and tightening the presentation, is necessary before this can be considered for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

P4‑E6 (ESSENTIAL) – Systematic σ/“significance” arithmetic errors in Table III bandpowers  
- **Location:** Table III, p.7 (“Angular power spectrum of the chirality asymmetry map”).  
- **Problem:**  
  - The table states, e.g., for the bandpowers:
    - ℓeff = 9: \(C_\ell = -0.248\times 10^{-6}\), \(\sigma_{\text{null}} = 0.574\times 10^{-6}\), “Significance = +2.232σ.”  
      The naive z‑score is \(-0.248/0.574 \approx -0.43\), not +2.23.  
    - ℓeff = 14: \(-0.387/0.446 \approx -0.87\), not +2.626.  
    - ℓeff = 19: \(-0.576/0.420 \approx -1.37\), not +2.229.  
    - ℓeff = 24: \(-0.648/0.366 \approx -1.77\), not +2.470.  
  - Even allowing for an alternative “moment‑ratio” or χ²‑style definition (as used elsewhere for z), it is mathematically impossible for the *signed* z‑values to all be positive given negative \(C_\ell\), and the magnitudes do not match any obvious transformation of the listed means and σ’s.  
  - The caption describes the last column simply as “Significance (σ)”; no alternate definition is given, so readers will naturally interpret these as \(C_\ell/\sigma_{\text{null}}\).  
- **Required fix:**  
  - Recompute and correct all “Significance (σ)” entries in Table III directly from the stated \(C_\ell\) and \(\sigma_{\text{null}}\), with appropriate sign, or explicitly define and justify a different statistic if used.  
  - Ensure consistency between these fixed values and any downstream textual statements that rely on these σ’s (e.g., “Residual mask coupling” classification).  

---

P4‑M5 (MAJOR) – Inconsistent treatment of hemispheric/LEE significance between text and Table I  
- **Location:** Table I row (v), p.4; Appendix C, “Hemisphere asymmetry and look‑elsewhere”; Discussion p.9.  
- **Problem:**  
  - Table I lists for “hemisphere LEE (MC)” the entry “pLEE ≤ 10⁻⁴”.  
  - Appendix C explains that a direct‑MC look‑elsewhere test over hemisphere pairs gives \(p_{\text{LEE}} \le 10^{-4}\), but then states that after conservative Bonferroni/BH correction across ∼650 tested directions the *post‑LEE significance* drops below |σ| < 1, attributing the small raw p to the same low‑level systematic as the global monopole.  
  - In the Discussion, the text again emphasizes the post‑LEE downgrade (“post‑LEE significance drops below |σ| < 1”), but Table I only shows the raw “\(p_{\text{LEE}} \le 10^{-4}\)” without any explicit note that this is a *pre‑correction* diagnostic and *not* a cosmological detection.  
- **Required fix:**  
  - In Table I, qualify row (v) to make clear that “\(p_{\text{LEE}} \le 10^{-4}\)” is a raw Monte‑Carlo value *before* multiple‑comparison correction and that, after correction, significance is <1σ and non‑cosmological (as described in Appendix C).  
  - Consider adding a short footnote or parenthetical “(pre‑correction diagnostic; post‑LEE |σ| < 1, non‑cosmological)” so that the headline table does not appear to advertise a very small p‑value with no context.  

---

P4‑M6 (MAJOR) – Null‑procedure comparability caveat missing at key σ juxtapositions in Discussion/Conclusions  
- **Location:** Discussion VI.A–C, VII.a–d.  
- **Problem:**  
  - Although the abstract and Section IV explicitly note that σ values from distinct nulls are not directly comparable, the Discussion and Conclusions repeatedly juxtapose σ values from different null procedures without *local* reminders, e.g.:  
    - VI.A: compares the empirical injection‑recovery \(P(\sigma>3)\) at different A values (from a per‑pixel‑shuffle null on a restricted HC subset) to the Fisher‑floor 3σ estimate (analytical Poisson limit on the full catalog).  
    - VI.B and VII.c–d bring together the +0.43σ real‑space dipole (isotropic bootstrap), the template‑fit z ≈ −18 (block‑bootstrap WLS on templates), and pseudo‑Cℓ σ’s (+3.64, +7.28) within contiguous argument, sometimes in the same bullet point, without restating the null‑incomparability caveat.  
  - This undercuts the otherwise careful warning in Section IV and violates the stricter requirement you quoted in your instructions (local caveats at each juxtaposition).  
- **Required fix:**  
  - In VI.A–C and the numbered conclusions VII.a–d, where multiple σ’s from distinct nulls appear in the same sentence, bullet, or short paragraph (e.g., “0.43σ real‑space dipole… +6.48σ pre‑MASTER… +3.64σ canonical”), insert short parenthetical remarks such as “(different nulls; σ not directly comparable)” or rephrase to avoid any implied ranking by σ.  
  - Ensure that the Fisher‑floor 3σ calculation is described explicitly as a *different benchmark* from the injection‑recovery σ values so that readers do not conflate them.  

---

P4‑M7 (MAJOR) – Abstract claim “3.86× asymmetry-suppression factor” not arithmetically documented in body  
- **Location:** Abstract p.1, sentence “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%…”; body: Section IV.B, footnotes.  
- **Problem:**  
  - The text states that the raw Catalog A has a +2.05% classifier CW excess and Catalog C has −0.53% residual; this implies an asymmetry reduction factor roughly \(2.05/0.53 \approx 3.87\).  
  - However, the only explicit numerical asymmetries actually tabulated for A and C in Table II are “Excess (%) = +0.79” and “−0.26,” not 2.05% and 0.53%. It is unclear what exactly is meant by “+2.05%” versus “+0.79%” and “−0.53%” versus “−0.26%,” and no equation defines “asymmetry” there.  
  - As a result, a referee cannot reconstruct the 3.86× factor from the numbers given in the main text or tables; it appears to use a different normalization or sample than Table II, but this is not explained.  
- **Required fix:**  
  - Explicitly define the “asymmetry” used for the 2.05% and 0.53% numbers (e.g., is it \((f_{\text{CW}}-0.5)\), or a per‑pixel averaged quantity, or a specific subset?), and show these values in a table or numerical sentence in Section IV.B.  
  - Make sure that the 3.86× factor can be recomputed from those explicit values. If it relies on a different catalog cut or weighting than Table II, state that clearly.  
  - Alternatively, if you intend to refer to the Table‑II “Excess (%)” (0.79% → −0.26%), recompute the corresponding suppression factor and replace “3.86×” with the correct value.  

---

P4‑m5 (MINOR) – Confusing duplication of “z ≈ −264.5” and “z ≈ −250” for the same 1.7% template‑fit reference  
- **Location:** Appendix D.f (WLS fit) and nearby discussion lines.  
- **Problem:**  
  - Appendix D.f writes “the interpretation (i) reference amplitude 1.7% at z = −264.5 from the naive WLS posterior (far‑tail).” A few lines later, when discussing the extended 24‑template fit, it states “z ≈ −250,” again apparently for the same 1.7% interpretation.  
  - No intermediate numbers are shown to justify either of these large negative z‑values; more importantly, having two different z’s (−264.5 vs −250) for the same conceptual statement without clarification looks like a stale‑number artifact from earlier tuning or rounding.  
- **Required fix:**  
  - Recompute the WLS‑posterior z‑score for the A = 1.7% hypothesis once, and quote a single consistent value (with reasonable rounding, given that z ≫ 10). Clarify explicitly if −250 refers to a different model (e.g., with additional templates) than −264.5, or collapse to a single representative number.  
  - Given that these are “far‑tail” values, you might also consider de‑emphasizing excessive precision (e.g., “z ≈ −250” only once) rather than two distinct, apparently over‑precise numbers.  

---

P4‑m6 (MINOR) – Ambiguous use of “σiso” and “σ” in hemisphere diagnostics  
- **Location:** Appendix C.b–c, Discussion p.9.  
- **Problem:**  
  - Appendix C.b refers to “NGP (b > 0) gives σiso = +0.47; SGP (b < 0) gives +2.02.” Later, hemisphere tests mention “maximum asymmetry 3.05σ” and “post‑LEE significance drops below |σ| < 1.”  
  - It is not stated explicitly whether σiso for the NGP/SGP refers to the same null and definition as the 3.05σ LEE statistic (which is defined via hemisphere scans and MC). This matters for readers trying to interpret hemisphere results quantitatively.  
- **Required fix:**  
  - Add a brief clarifying sentence in Appendix C that all hemisphere and NGP/SGP σ values are computed under the same isotropic‐or‑label‑shuffle null (specify which) and using the same test statistic, or explicitly state if they differ.  
  - This will prevent misinterpretation of σiso vs σ as different statistical quantities.  

---

If you want, I can next go systematically through each table and equation and enumerate any remaining arithmetic checks (A) or dimensional‑consistency checks (C) you explicitly want verified.