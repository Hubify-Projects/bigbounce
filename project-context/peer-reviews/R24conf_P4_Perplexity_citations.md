# P4 R24conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v168.pdf` md5=90c4a8a3 pages=19
**Input format**: TEXT + web search + pass-2 self-critique (15645 chars)
**Wall time**: 130.3s

---

P4 cannot be accepted in its current form. The analysis is sophisticated, but the manuscript is riddled with internal-inconsistency flags, version-history language, supersession notes, and several PRD‑level methodological and presentation issues that must be fixed. Below I list findings systematically.

I only had access to the text you provided, not the actual rendered PDF, so I reference “page” as implied by the layout breaks in the excerpt; for PRD you must map these to real page numbers in the typeset PDF.

---

## ESSENTIAL ISSUES (paper not publishable without these)

### P4‑E1: Explicit version-history / audit / artifact prose in body

- **Location:** Abstract; Sec. III.A; Sec. IV.C; Sec. IV.D; Appendix A; Appendix B; Appendix C; Appendix D; Data Availability; footnotes and parenthetical notes throughout.
- **Problem:**
  - The paper repeatedly includes internal‑provenance and version‑history prose, e.g.:
    - Abstract: “An earlier version of this paper reported a MASTER ℓ = 1 null … that result is withdrawn (Appendix A)…”  
    - Sec. III.A: “…declared in early versions of this analysis and predates the provenance audit described in Appendix A…”
    - Sec. IV.C: “[Correction note: an earlier version printed 0.43σ… the generator was repaired… Artifact: outputs/dipole/catalog c summary.json.]”
    - Sec. IV.D footnote 1: “an earlier version of this paper misquoted this factor, a value traced to the withdrawn synthetic-catalog artifact (provenance note, Appendix A, where the supporting artifact files are listed).”
    - Appendix A: “An earlier version of this paper reported a −0.122σ… A subsequent provenance audit found… The result is therefore withdrawn… affected manuscript versions (≤v1.0.165)…”
    - Appendix B–E/Data Availability: dozens of explicit references to Git paths (“pipelines/p2_chirality/outputs/…”) and repository commits (“commit 2a2939b2 (June 2026)”).
  - This reads like an internal lab notebook and arXiv changelog, not like a stable PRD article.
  - PRD expects the published paper to read as a coherent, self‑contained account of the final analysis, not a revision log.
- **Required fix:**
  - Remove all version‑history language, “earlier version” commentary, and references to specific manuscript versions and artifact file names from the main text and abstract.
  - Keep essential *scientific content* of the provenance audit, but rewrite it as a clean, static description of:
    - what estimator was incorrectly configured,
    - how you discovered and corrected it,
    - what the corrected result is,
    - why no current conclusion relies on the incorrect result.
  - Move any detailed audit‑trail narrative (specific file paths, old run IDs, etc.) to a brief supplementary/miscellaneous note or to the code repository README, not in the PRD paper.
  - The abstract should not mention withdrawn earlier results; it should state only the *final* analysis and findings.

---

### P4‑E2: Sigma values from different nulls presented side-by-side without constant, explicit “not comparable” caveats

- **Location:** Abstract; Table I; many sections (III.A, IV.C–E, VI, VII, Appendices C–D).
- **Problem:**
  - Multiple σ’s are juxtaposed without always clearly restating they are not comparable:
    - Abstract: “+0.41σ (empirical-rank p = 0.31, 10⁴ isotropic-null realizations; … z = 0.70 …), and … diagnostics carry systematics-attributed residuals (+3.64σ …; +7.28σ, apodized footprint)…”
      Here 0.41σ, 3.64σ, 7.28σ appear in a single sentence; there is no immediate reminder that they use different nulls and estimators.
    - Table I lines (iii)–(iv): “+3.64σ” and “+7.28/+7.13σ” are listed next to the +0.41σ dipole, with only a brief note in the caption that values are “not directly comparable across rows.” However, in the main text, these are repeatedly described together (“+0.41σ vs +7.28σ gap is not a 17× discrepancy…”) without a clear caveat at *every* juxtaposition.
    - Sec. VI and VII list several σ values from different channels in paragraph form.
  - Per your instructions, any side‑by‑side appearance of σ’s from different null procedures must be explicitly labeled as not directly comparable *each time* they are juxtaposed, to avoid misleading readers.
- **Required fix:**
  - In every place where two or more σ’s from different null procedures (or different estimators) appear in the same sentence, figure caption, table, or comparative statement, add an explicit clause such as:
    - “(note: these σ values are defined with different estimators and nulls and are not directly comparable).”
  - For Table I, strengthen the caption: e.g., “All σ values are against the null listed in column ‘Null’; they are not directly comparable between rows, and any comparison must be done via explicit injection/recovery or cross‑projection, as in Sec. VII.”
  - Ensure the abstract itself does not invite a naive reading that +3.64σ and +7.28σ are stronger “detections” than +0.41σ; either remove σ’s for purely diagnostic channels from the abstract, or qualify them inline as systematics diagnostics with incomparable significance scales.

---

### P4‑E3: Abstract statistics vs body: consistency and traceability

- **Location:** Abstract vs body (Sec. II, IV, VI–VII; Table II; Table V; Appendices).
- **Problem:**
  - The abstract quotes several load‑bearing statistics; they must be reproducible from explicit numbers in the body:
    - Catalog size: “8,474,531 DESI Legacy DR8 galaxies … Nspiral = 3,201,160 spirals” — consistent with Sec. II.A & IV.A and Table II (3,201,160), good.
    - Headline dipole: “+0.41σ (empirical-rank p = 0.31, 10⁴ realizations)” — Sec. IV.C gives amplitude 4.4×10⁻³ and rank‑p=0.31; you *do* mention that z=0.41 is a moment‑ratio, but the relation between these numbers is not explicit (no table showing ⟨A⟩null, σnull). A referee cannot reproduce 0.41σ from the provided text alone.
    - “monopole-only generative null reproduces 99.32% of the raw pre‑MASTER ℓ=1 power” — Table IV quotes 1.6961×10⁻² data and null 1.6846×10⁻². The ratio ~0.9932 is consistent; however, the method for mapping that to “+1.69σ residual” is not fully explicit (only σ of 6.8×10⁻⁵ is quoted in the table).
    - “+3.64σ moment‑z, ≈1.9σ Gaussian‑equivalent” — Table III canonical ℓ=1 row gives z=+7.93 and rank‑p=3×10⁻⁴ for the redefined estimator, which is larger than “1.9σ” Gaussian equivalent. The text states the earlier +3.64σ is “superseded as a table entry but retained in the text”; the abstract still cites +3.64σ, which is now tied to a non‑canonical variant. This is confusing and not internally clean.
  - For PRD‑level rigor, every quoted σ or p in the abstract must be recomputable from clearly given numbers (means, variances, N) in the main text or tables, using standard formulas.
- **Required fix:**
  - For each abstract number:
    - Provide in the main text or table:
      - the underlying estimator definition,
      - the null mean and standard deviation (or full empirical distribution reference),
      - enough digits to recompute the quoted σ or p.
  - Align terminology:
    - If you keep “+3.64σ” in the abstract, dedicate a short paragraph clearly tying that number to a unique, explicitly defined estimator in the body (including the difference from the +7.93σ in Table III).
    - Alternatively, remove “+3.64σ” from the abstract and only mention that harmonic diagnostics show significant systematics; keep detailed σ’s in the main text.
  - Ensure all headline σ’s in the abstract correspond to the *current* canonical estimators, not to superseded ones.

---

### P4‑E4: Use of “superseded”, “earlier version”, “artifact” terms in scientific narrative

- **Location:** Abstract; Sec. IV.D, IV.E; Appendix A; footnotes; notes throughout.
- **Problem:**
  - Terms such as “superseded”, “artifact,” “earlier version misquoted,” “withdrawn synthetic‑catalog artifact,” “artifact c9b/c11b…”, “supporting audit artifacts,” etc., are sprinkled through the scientific narrative.
  - While transparency about corrections is commendable, the published paper must present a *clean* final analysis; internal run IDs and artifact labels are not appropriate in a PRD article’s main body and distract from the science.
- **Required fix:**
  - Replace “artifact c9b” / “artifact c11b…” etc., with neutral pointers such as “see supplementary material for arrays and code” or “see companion data release.”
  - Remove “superseded by…” phrasing and instead present only the final estimator and numbers; any comparison to prior internal versions belongs in a short “provenance note” boxed subsection or in supplemental material, not woven into technical arguments.
  - Ensure the narrative reads like a single, internally coherent analysis, not an incremental log of debugging steps.

---

### P4‑E5: Ambiguous “z” notation and sigma semantics

- **Location:** Abstract; Table I; Sec. IV.C–D; Sec. VI.A; VII; Appendices.
- **Problem:**
  - You use “z” for at least three different notions:
    1. Redshift (e.g., “at z ≈ −18” clearly not redshift but a confusion with significance; also “z ≈ −18” for block‑bootstrap).
    2. Standard‑deviation significance of a measured quantity vs null (moment‑ratio).
    3. “Gaussian‑equivalent” significance derived from rank p.
  - Example: Table I “(ii) WLS template excl. … z ≈ −18” with no units; in Sec. D you say “zboot ≈ −18.1”; someone could confuse this with redshift as in cosmology.
  - The abstract writes: “z = 0.70” and “+3.64σ moment‑z, ≈1.9σ Gaussian‑equivalent” with no explicit equation linking moment‑z to p‑derived σ.
- **Required fix:**
  - Standardize notation:
    - Use explicitly \( z_{\rm sig} \) (or similar) for standardized significance statistics, and reserve plain “z” strictly for redshift.
    - State once, in a dedicated subsection, how each z is defined (moment-ratio vs null; p→σ conversion).
  - In all tables, include subscript or label in column headers, e.g. “z (moment)” and “σ_G (Gaussian‑equiv.)”.
  - Remove “z ≈ −18” phrasing in contexts where redshift might be inferred and replace by “significance ≈ −18σ” or “z_sig ≈ −18.”

---

### P4‑E6: Mixing of “ideal Fisher floor” vs empirical sensitivity and underlying vs observed amplitudes

- **Location:** Sec. VI.A; Sec. VII.e; Table V.
- **Problem:**
  - The paper states:
    - Fisher floor 3σ detection at A≈0.29% (for perfect classification).
    - Empirical A₅₀≈0.75% for the *observed* catalog with label noise and footprint.
    - Then applies a “GZ1 dilution factor g=2a−1≈0.398” to get an “underlying threshold ∼1.88%.”
  - However, there is no explicit derivation to show that the injection procedure (which injects in the *observed* catalog via label permutations) corresponds to that transformation to a true underlying sky dipole. It is plausible, but not fully explicated.
- **Required fix:**
  - Add a short derivation making explicit:
    - How classification accuracy a propagates a true dipole amplitude A_true into an observed effective amplitude A_obs = g A_true (or similar).
    - Show numerically how A₅₀(obs)=0.75% maps to A₅₀(true)≈1.88%.
  - Clarify in the abstract and conclusions whether quoted A₅₀ and A₉₅ are *observed* catalog amplitudes or inferred underlying true‑sky amplitudes, and keep the two clearly separated.

---

### P4‑E7: “Standalone observational result” vs dependence on unpublished companion work

- **Location:** Introduction (first page).
- **Problem:**
  - You state: “The present paper is a standalone observational result: our null dipole at sub-percent sensitivity does not depend on any unpublished companion work.”
  - Yet multiple parts (including the falsification criterion; injection/recovery; future theory mapping to parity‑violating sectors) allude to transfer functions or analyses not carried out here.
  - The sentence itself is okay *if* literally true; but nothing in the text actually cross‑checks that all key methods and diagnostics are fully defined here and not in a “posted concurrently” companion.
- **Required fix:**
  - Either:
    - Ensure all methods, estimators, nulls, and thresholds needed to reproduce the headline claim are fully specified in this paper (not just in code), and clarify explicitly that companion papers, if any, are purely theoretical or ancillary, *or*
    - If some load‑bearing methodology is deferred to a companion paper, explicitly cite that companion as “in preparation” only if it is already on arXiv; otherwise remove the “standalone” claim.
  - For PRD, the observational result and its error budget must be fully reproducible from this paper plus the released data, without relying on future work.

---

## MAJOR ISSUES

### P4‑M1: Excessive length and narrative redundancy for the claimed contribution

- **Location:** Whole manuscript (19+ pages plus numerous appendices).
- **Problem:**
  - For a methods‑driven null result, the paper devotes very extensive text to internal audits, provenance details, and repeated restatements (e.g., multiple paragraphs explaining the same leakage channel with slightly different emphases).
  - For PRD, this is overly long for the core contribution: a large chirality catalog, a real‑space null dipole, and characterization of monopole–mask leakage.
- **Required fix:**
  - Tighten the paper aggressively:
    - Move most of Appendices C–E and code‑path details (file paths, seed values, etc.) to online supplementary material, keeping only essential definitions and one or two key validation tables in the paper.
    - Remove repeated explanations of the same concept (e.g., leakage channel) and instead reference a single detailed subsection.
  - A reasonable target is ≤ 12–14 journal pages for the main text (excluding references), with appendices reserved for indispensable technical derivations.

---

### P4‑M2: Ambiguous labeling of “null” vs “detection” in harmonic diagnostics

- **Location:** Sec. IV.C–D; Fig. 8; Table III; Appendix D.
- **Problem:**
  - You emphasize that MASTER ℓ=1 is a systematics diagnostic, not a cosmological estimator, yet the language sometimes reads like a detection:
    - “+7.28σ vs global label shuffle” and “strongly non‑null +7.28σ / +9.78σ excess.”
  - The reader may misinterpret this as a genuine detection of a physical signal rather than an instrument/classifier systematic; although you do state it’s “systematics‑attributed,” the repeated σ language blurs the message.
- **Required fix:**
  - Explicitly label these σ values as “significance of deviation from the label‑shuffle null attributed to systematics” every time they are mentioned.
  - In the abstract and conclusions, clearly separate “cosmological null result” from “significant systematics signatures in diagnostic channels.”

---

### P4‑M3: Treatment of unthresholded‑sample 4.2σ / 0.57% dipole

- **Location:** Sec. IV.C (confidence‑threshold sensitivity disclosure).
- **Problem:**
  - You state that removing the confidence cut yields a 0.57% dipole at z≈4.2–4.4σ, attributed to low‑confidence tail systematics and below A₅₀≈0.75%, and that it is “reported here as a systematics-sensitivity diagnostic, not a detection.”
  - However, 0.57% is close to the 0.75% sensitivity floor, and 4σ is high enough that some readers could wonder whether this is a weak signal rather than pure systematic.
  - There is no clear quantitative demonstration that this 0.57% amplitude is consistent with the same leakage/morphology systematics that explain the harmonic channel.
- **Required fix:**
  - Provide a quantitative test showing the 0.57% unthresholded dipole is aligned with the same depth/mask or morphology proxies that drive the canonical harmonic residual (e.g., cross‑correlation with depth or leg masks).
  - Alternatively, omit explicit σ for this unthresholded result in the main text and simply state that low‑confidence tails are demonstrably systematics‑dominated and therefore excluded from the headline estimator.

---

### P4‑M4: Clarity of Falsification criterion and A₉₅ interval

- **Location:** Abstract; Sec. VI.A; Sec. VII.e.
- **Problem:**
  - You define a falsification criterion as a future ≥5σ detection at amplitude \(A \gtrsim A_{95}\), with A₉₅ bracketed between 1.0% and 1.5%.
  - However, A₉₅ is not actually measured; only bounding values at discrete grid points are given (0.91 at 1.0%, 1.00 at 1.5%). The term “A95” suggests a well-defined number, not an interval.
- **Required fix:**
  - Rephrase consistently as “A₉₅ is constrained to lie in (1.0%,1.5%] under our coarse grid; we did not interpolate or measure it more precisely.”
  - In the abstract, either:
    - remove the symbol “A95” and simply say “between 1.0% and 1.5%,” or
    - clearly state that “A95 is bracketed rather than precisely estimated.”

---

### P4‑M5: Claims of “largest chirality-labeled galaxy catalog” and factor comparisons

- **Location:** Abstract and Introduction; Sec. V.
- **Problem:**
  - You claim “the largest chirality-labeled galaxy catalog to date: 8,474,531 DESI Legacy DR8 galaxies … 3,201,160 spirals, 1.6× CE-ResNet’s scale” and “a ≳25× sample extension over the 1.27×10⁵‑galaxy SDSS sample underlying the critiqued analyses.”
  - I cross‑checked the key cited works:
    - Jia et al. 2023 (CE‑ResNet) report cw/ccw of ∼1.95M galaxies, which matches your 1.6× claim.[7]
    - Shamir 2012 uses ∼1.27×10⁵ SDSS spirals; your 3.2×10⁶ spirals indeed give ≈25× more.[4][5][6]
  - These comparisons are numerically consistent, but the “largest” claim should be explicitly bounded by survey type and epoch (e.g. “to date in the literature”).
- **Required fix:**
  - Add a qualifier: “to our knowledge, the largest published chirality-labeled catalog to date” and specify that this is based on a literature survey up to 2026.
  - Confirm no more recent (e.g. late‑2025/2026) large‑scale chirality catalogs exist; if they do, update comparisons.

---

## MINOR ISSUES

### P4‑m1: Dimensional consistency and clarity in Eq. (4)

- **Location:** Sec. VI.A (Fisher floor).
- **Problem:**
  - You write \( \sigma(A) = \sqrt{3/N_{\rm spiral}} = 2\sqrt{3}\,\sigma(f_{\rm CW}) = 9.7\times10^{-4}\).  
    The relation \( \sigma(f) = \sqrt{p(1-p)/N} \) with p=1/2 gives σ(f)=1/(2√N); then 2√3σ(f)=√3/N, but your first equality uses √(3/N). The text is slightly confusing.
- **Required fix:**
  - Rewrite the derivation cleanly:
    - Show explicitly \( \sigma(f_{\rm CW}) = 1/(2\sqrt{N}) \), then \( \sigma(A)=2\sqrt{3}\sigma(f_{\rm CW})=\sqrt{3/N} \).
  - Check algebra and ensure the exact factors are correct, with a short explanatory line so readers can follow.

### P4‑m2: Possible typo/misleading notation “z ≈ −18 (z ≈ −18)” in Sec. VII.d

- **Location:** Sec. VII.d; Appendix D / Table IX.
- **Problem:**
  - You refer to “the template-fit exclusion of a clean 1.7% dipole (z ≈ −18, Appendix D)” while the WLS table gives z=−264.5 (naive WLS) and z_boot≈−18.1; you later say the naive value is superseded.
- **Required fix:**
  - Standardize the reported significance to a single canonical value (the block‑bootstrap z_boot≈−18).
  - Always label it “z_boot” or “bootstrap significance” to avoid confusion.

### P4‑m3: Occasional duplicated or near-duplicated phrasing

- **Location:** Various places (e.g., repeated long footnotes about mask / leakage).
- **Problem:**
  - While I did not see literal phrase duplication like “canonical canonical‑mask,” there are several near‑duplicate explanations of the same ideas, which hurts readability.
- **Required fix:**
  - Carefully edit for redundant sentences and paragraphs; keep one canonical explanation and refer back to it.

### P4‑m4: Axis selection protocol wording

- **Location:** Sec. VI.A, injection protocol.
- **Problem:**
  - You write “θ ∼ U(0,π)… uniform in polar angle, which mildly over-weights near-polar axes relative to an area-uniform draw.”  
    In fact, θ uniform in [0,π] *underweights* near poles; area‑uniform draws have sinθ weighting. The text is confusing.
- **Required fix:**
  - Correct the description:
    - Either state that the distribution is not area‑uniform and briefly quantify the impact on P(σ>3), or actually use an area‑uniform axis draw (cosθ uniform) in the injection tests and update numbers accordingly.

### P4‑m5: Repeated “per-pixel-shuffle” / “label-shuffle” terminology

- **Location:** Throughout.
- **Problem:**
  - Several different nulls are all called “label-shuffle” / “per-pixel-shuffle,” which risks confusion (e.g., shuffles across pixels vs within pixels vs within depth strata).
- **Required fix:**
  - Give each null a distinct name (e.g., global‑pixel‑permute, per‑galaxy label shuffle, depth‑stratified shuffle) and use them consistently.

---

## NITS (cosmetic / style)

### P4‑n1: Use of first person singular

- **Location:** Many places (“I assemble labels,” “I do not claim…”).
- **Fix:** PRD typically uses “we,” including for single‑author papers. Convert to “we” uniformly.

### P4‑n2: Footnote formatting and length

- **Location:** Long explanatory footnotes in Sec. IV.D and Appendix D.
- **Fix:** Consider moving long footnotes into the main text or appendices to improve readability.

### P4‑n3: Minor typographical issues

- **Location:** A few examples:
  - “z ≈ −18; Appendix D” (should clearly be “significance z_sig ≈ −18”).
  - “falsification boundary) is bracketed, not measured :” extra space before colon.
- **Fix:** Run a careful copy‑edit for punctuation spacing, hyphenation (e.g. “block-bootstrap”), and consistent capitalization (e.g. “MASTER” vs “MASTER deconvolution”).

---

## Citation Forensics

Given the excerpt, I can only verify the references explicitly listed at the end.

- **Shamir (2012, 2020, 2022)**  
  - [1] L. Shamir 2020 Astrophys. Space Sci. 365, 136, arXiv:2007.16116 — matches “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles.”[1]
  - [2] L. Shamir 2022 PASJ 74, 1114 — DOI, title, and year are consistent.[2]
  - [3] L. Shamir 2022 MNRAS 516, 2281, arXiv:2208.13866 — matches “Analysis of spin directions of galaxies in the DESI Legacy Survey.”[3]
  - [4] L. Shamir 2012 Phys. Lett. B 715, 25, arXiv:1207.5464 — correct.[4]

- **Iye et al., Tadaki et al., Jia et al.**  
  - [5] Iye, Yagi, Fukumoto 2021 ApJ 907, 123, arXiv:2011.00662 — correct.[5]
  - [6] Tadaki et al. 2020 MNRAS 496, 4276, arXiv:2006.02331 — correct.[6]
  - [7] Jia, Zhu, Pen 2023 ApJ 943, 32, arXiv:2210.04168 — title and journal match.[7]

- **DESI Legacy Survey and Galaxy Zoo DESI**  
  - [8] Dey et al. 2019 AJ 157, 168, arXiv:1804.08657 — DESI Legacy Imaging Surveys overview.[8]
  - [9] Walmsley et al. 2023 MNRAS 526, 4768, arXiv:2309.11425 — Galaxy Zoo DESI.[9]

- Other cosmology/analysis references (NaMaster, HEALPix, etc.) appear accurate in journal, year, and general description; I did not see any obvious fused metadata or future‑dated arXiv IDs.

- **Quoted statistics vs cited papers:**
  - Shamir 2012: your mention of “2–4σ dipole” and “5–20% per-bin asymmetry” is consistent with PLB 715, 25 and its abstract/tables.[4]
  - Shamir 2020/2022: the “∼2–4%” asymmetry class matches values quoted in their abstracts.[1][3]
  - Jia et al. 2023: your cw/ccw=0.998 on ∼1.95M galaxies is explicitly stated in their paper.[7]

I did not find any “in preparation” fake references, imaginary arXiv IDs, or mismatched DOIs in the provided reference list.

---

## Summary recommendation

**MAJOR REVISIONS**

The core scientific result—a carefully bias‑hardened null dipole with a very large chirality catalog—is potentially suitable for PRD, but the manuscript in its present form reads as a heavily annotated internal audit log rather than a polished journal article. You must remove version‑history language and artifact path references from the main text, clarify the σ and null‑hypothesis semantics at every juxtaposition, clean up statistical derivations, and significantly tighten the presentation. Once these essential and major issues are addressed, the paper could be re‑evaluated for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

P4‑E8: Additional arithmetic / consistency errors and stale numbers remain and must be fixed; your current draft is not arithmetically clean enough for PRD.

Below are only *new* findings that were not in your prior review, grouped by your requested checklist. I focus on things that are plausibly PRD‑blocking if not corrected.

---

## NEW ESSENTIAL ISSUES

### P4‑E8: Sloppy σ, p, and ratio arithmetic and/or missing explicit derivations

This is a cluster of small but cumulatively serious problems: some numbers are right but not demonstrably recomputable from what is written; some are ambiguous; and one or two are at least confusingly presented.

**(A) Arithmetic / recomputability checks**

1. **Global CW fraction deviations and σ values**

   Table II:

   - Catalog C fraction: \(f_{\rm CW}=0.497353(279)\).  
     The binomial σ is stated as \(\sigma = \sqrt{f(1-f)/N}\) with \(N=3{,}201{,}160\).  
     With \(f \approx 0.49735\), \(\sigma \approx \sqrt{0.49735\cdot 0.50265 / 3.20116\times10^{6}} \approx 2.80\times10^{-4}\).  
     That matches 0.000279 to rounding, and the 1σ parentheses notation is consistent.
   - The deviation “Dev. (σ) = −9.47” should equal \((0.497353-0.5)/0.000279\).  
     Numerically: \(-0.002647 / 0.000279 \approx -9.49\). You quote −9.47, which is probably just from using internal higher precision; but you never show the exact \(N\) actually used for σ (Table II says \(N^{C}_{\rm spiral}=3{,}201{,}160\) but Sec. IV.A earlier gives 3,201,160; Introduction repeats 3.2×10⁶).  
     **New issue:** the reader cannot reproduce −9.47 exactly from the published digits; this is minor, but since you are hanging a “9.5σ monopole” on it and use that elsewhere, you should:
     - either give \(f_{\rm CW}\) with one more digit, or
     - quote Dev to one decimal (−9.5σ) rather than two decimals suggesting unwarranted precision.
     This is a general pattern: you push σ to two decimal places without exposing enough significant figures in inputs to reconstruct them.

2. **Monopole‑mask leakage “99.32%” and “+1.69σ” are arithmetically consistent but not fully explicit**

   Table IV:

   - Data: \(C_1^{\rm data} = 1.6961\times10^{-2}\).
   - Null mean: \(1.6846\times10^{-2}\), σ = \(0.0068\times10^{-2}\).
   - Reproduction fraction: \(1.6846/1.6961 \approx 0.9932\) = 99.32% (fine).
   - Residual significance: \((1.6961 - 1.6846)/0.0068 \approx 1.69\), consistent with “+1.69σ”.

   You *do* state in text that 0.0068×10⁻² is “per‑realization scatter” and then derive the standard error 0.018 percentage points for the ratio. That is fine. However:

   - You never give the *mean* reproduction fraction ± σ of the fraction explicitly; readers must reverse‑engineer it from C₁.  
   - In the abstract you only quote “99.32% of the raw pre‑MASTER ℓ=1 power” with no σ on that percentage; the 0.40 pp scatter and ±0.018 pp on the mean are only in Sec. IV.D. For PRD, the abstract-referenced number should be clearly reconstructible from a table entry, which it is, but only via an implicit ratio; raising this explicitly would strengthen traceability.

3. **MASTER Table III “z” and rank‑p vs Gaussian σ**

   Table III entries are internally consistent:

   - Example: apodized ℓ=1 row:  
     data = 24.74×10⁻⁶, null mean 1.93×10⁻⁶, σ = 3.12×10⁻⁶.  
     Moment z = (24.74−1.93)/3.12 ≈ 7.31, matching table.  
     Rank p = 6×10⁻⁴ (k=5 of 10⁴) gives a Gaussian‑equivalent of ≈3.2σ (one‑sided), which you *do not* quote in the table, only in prose (“need not agree”), so there is no explicit arithmetic inconsistency.

   **But:** your abstract still highlights “+3.64σ moment‑z, ≈1.9σ Gaussian‑equivalent” for the canonical diagnostic, while Table III shows +7.93 and rank p = 3×10⁻⁴ for the canonical ℓ=1 *canonical* estimator. This is already in your earlier P4‑E3, but the **new point** is:

   - The abstract’s 1.9σ Gaussian‑equivalent number (for 3.64σ canonical‑N) is **not** recomputable from any table now, because the canonical‑N single‑mode line is gone from Table III, and you never tabulate the null mean and σ for that estimator anywhere else.

   So for that particular “1.9σ,” the reader has no way to check the mapping. You either need to:
   - restore a minimal one‑row table including mean, σ, and rank‑p for the canonical‑N estimator, or
   - remove “≈1.9σ Gaussian‑equivalent” from the abstract and/or main text.

4. **Injection‑recovery Table V numbers are consistent, but Fisher floor mapping is implied, not derived**

   Table V:

   - You state Fisher σ(A) = 9.7×10⁻⁴ (see Eq. (4)), so 3σ(A) ≈ 2.9×10⁻³ = 0.29%.  
   - From Table V: P(σ>3)=0.15 at A=0.5%, rising to 0.55 at A=0.75%. Those are qualitatively consistent (classification noise plus footprint effects), but nowhere do you show a quantitative mapping from Fisher expectation to this curve.

   That is more conceptual than arithmetic, and parts are in your previous P4‑E6, but the **new aspect** is: the phrase “empirical 50%-recovery‑3σ injection–recovery threshold at |A|≥0.75%” in the Introduction is not obviously traceable back to a *figure label* or explicit definition of “threshold” in Table V. A referee must infer that “threshold” = amplitude where P(σ>3) crosses 0.5. You never say that explicitly.

   For PRD, this is borderline: the number is consistent, but the definition is only implicit.

**(B) Equation‑level issues / dimensional consistency**

5. **Eq. (4) algebra is ultimately correct but the narrative is confusing**

   Eq. (4):

   \[
   \sigma(A) = \sqrt{\frac{3}{N_{\rm spiral}}} = 2\sqrt{3}\,\sigma(f_{\rm CW}) = 9.7\times10^{-4}.
   \]

   From the binomial variance with p=1/2:

   - \(\sigma(f_{\rm CW}) = \sqrt{p(1-p)/N} = 1/(2\sqrt{N})\).
   - Then 2√3 σ(f) = 2√3 · 1/(2√N) = √3/√N = √(3/N).

   So the equality chain is mathematically consistent. **However**, the text *just before* this equation says “with the full‑sky idealization ⟨cos²θ⟩=1/3,” and the per‑galaxy Fisher information derivation is not shown. You jump from words to Eq. (4) with two equalities chained, relying on readers to infer both the Fisher calculation and the binomial variance step.

   This was already flagged as P4‑m1 in your earlier review, but reviewing with a “fresh eyes arithmetic” lens: this is a spot where a referee will pause and recalc. If you keep Eq. (4), you should:

   - Show explicitly: \(I(A) = \sum \cos^2\theta/[p(1-p)](\partial p/\partial A)^2\) with p=1/2, leading to Var(A) = 1/I = 3/N.  
   - Then separately derive the binomial relation, and *then* show that they match.

   As written, the reader must trust two unshown steps; that’s fragile for a load‑bearing sensitivity number.

6. **“A_true ≈ A_obs/g” mapping to 1.88% underlying threshold is numerically fine but unshown**

   In Sec. VI.A:

   - You state the GZ1 dilution factor g=2a−1≈0.398 (a=0.6991).
   - Then: “giving a true‑underlying threshold ∼1.88%.”

   If A₅₀(obs)=0.75% and A_true ≈ A_obs/g, then 0.75%/0.398≈1.89%, consistent with your “∼1.88%.”

   **New issue:** you never write that equation. For a key conversion between catalog‑level and physical amplitude, that’s too implicit. PRD readers will want the explicit mapping and a brief justification that a simple multiplicative g is appropriate for your injection protocol.

---

## NEW MAJOR ISSUES

### P4‑M6: Abstract vs body consistency for several nuanced claims

This is distinct from your earlier P4‑E3, focusing now on *other* sentences.

1. **“Standalone observational result” vs explicit dependency on external training labels**

   You say:

   > “The present paper is a standalone observational result: our null dipole at sub-percent sensitivity does not depend on any unpublished companion work.”

   The *methodology* for the chirality catalog *does* depend on:

   - CE‑ResNet pseudo‑labels for ~66.5% of the training set.
   - Smith42/galaxies data selection and Galaxy Zoo DESI cuts.

   That’s acceptable—these are all published datasets and models. The **new concern** is that the falsification criterion and sensitivity floor *also* depend conceptually on:

   - The GZ1 accuracy floor (69.91%), which you use as the dilution factor a in g=2a−1.
   - The injection protocol code, which is only briefly summarized.

   The abstract’s “standalone” language is borderline misleading unless you explicitly say in the body that:

   - All needed information about CE‑ResNet and GZ1 is in the cited literature, and
   - The injection and null procedures are fully specified in this paper plus the public code, not in a separate “in prep” companion.

   You *do* lean in that direction, but a careful referee could read “standalone” as stronger than what you have actually demonstrated. This is a nuance you did not address in P4‑E7.

2. **“Monopole-only generative null reproduces 99.32% of the raw pre‑MASTER ℓ=1 power” vs Table IV**

   The abstract implies this 99.32% is a *single* number with some relevance to the main cosmological conclusions. Table IV shows it is:

   - specific to the pre‑MASTER pseudo‑Cℓ on the canonical mask,
   - tied to a relatively small N=500 MC, and
   - has a non‑negligible scatter (±0.40 pp per realization).

   The new issue here is scope: the abstract suggests this explains “prior literature’s pre‑MASTER dipole‑detection claims” in general. In the body, you are explicit that this is under “our DESI/ViT‑Small pipeline.” For PRD, that nuance should be in the abstract sentence itself (e.g. “under our DESI/ViT‑Small pipeline and mask geometry”). As written, the abstract overgeneralizes slightly compared to the more careful body wording.

3. **“Largest chirality‑labeled galaxy catalog to date” is not locally supported in the body**

   You make the “largest” claim in abstract, Introduction, and Conclusions. The Comparison‑with‑Previous‑Work section gives numerical comparisons to Shamir and CE‑ResNet, but you do *not* actually write the explicit inequalities in one place (e.g., “Shamir 2012 used 1.27×10⁵; Shamir 2022b ~1.3×10⁶; Jia et al. 2023 use ~1.95×10⁶; our spiral count is 3.20×10⁶ > 1.95×10⁶ > 1.3×10⁶”); instead, you summarize verbally (“1.6× CE‑ResNet’s scale,” “≳25× sample extension”). That’s OK, but:

   - The “to date” claim ideally should be backed by a clear statement that you searched the literature up to a certain date and did not find larger chirality catalogs.
   - Right now, the text only demonstrates “larger than those specific named works,” not “largest to date.”

   This was partially in your previous P4‑M5, but the subtle **new** issue is that the *body* never actually uses the phrase “to our knowledge,” which you recommended in the earlier review; the current version here still has “largest ... to date” unqualified.

---

## NEW MINOR ISSUES

### P4‑m5: Axis‑draw protocol wording is still mathematically wrong

Sec. VI.A:

> “each injection draws an independent random dipole axis (polar angle θ ∼ U(0,π) … uniform in polar angle, which mildly over‑weights near-polar axes relative to an area-uniform draw)”

Uniform θ underweights poles relative to area‑uniform sampling; area‑uniform requires sinθ weighting. You already flagged this once as P4‑m4, but **looking fresh**: this is not just a wording nit; it affects how readers interpret “axis‑averaged” P(σ>3). If you keep uniform‑θ, you must:

- Correct the description: “underweights near-polar axes,”
- Explicitly note that your sensitivity curve is slightly biased toward equatorial axes relative to an area‑uniform metric.

Otherwise, the definition of “axis‑averaged” in the falsification criterion is not as stated.

### P4‑m6: Some null‑procedure comparability caveats are missing in dense juxtapositions

You already have a global caveat in Sec. IV (“values from distinct null procedures are not directly comparable”) and in Table I’s caption; and this was the focus of P4‑E2. With fresh eyes, there are *still* a few dense comparisons where the caveat is absent:

1. **Sec. VI first paragraph**

   - You say: “2.31σ real-space; +6.48σ pre‑MASTER ... Equivariant averaging collapses the real-space dipole from 2.31σ to 0.41σ; MASTER deconvolution substantially reduces the monopoly‑mask leakage that sources the +6.48σ pre‑MASTER pseudo‑Cℓ.”
   - These σ’s are from different nulls (real‑space permutation vs pre‑MASTER label shuffle) and different estimators.
   - There is no parenthetical “(different nulls; not directly comparable)” immediately attached to this juxtaposition.

2. **Conclusions subsection (d)**

   - You mention “2.31σ real-space dipole and a +6.48σ pre‑MASTER pseudo‑Cℓ ... Equivariant post‑processing collapses the real‑space dipole to 0.41σ; MASTER ... reduces the monopole‑mask leakage.”
   - Again, no local caveat about incomparable σ scales.

Given your own strong rule that *every* side‑by‑side σ from different nulls must be marked as noncomparable, these are misses.

### P4‑m7: A95 symbol usage is still slightly misleading relative to Table V

You now clearly state in Sec. VI.A that “A95 is bracketed, not measured … A95 ∈ (1.0%,1.5%] on the tested grid.” However:

- The abstract still uses “A ≳ A95” and “A95 between 1.0% and 1.5%” in a way that reads as if A95 were a single well‑defined parameter, not a bracketed interval.
- In Conclusions (e), you again use “A95” as if it were a number.

With fresh eyes: this is not wrong, but it is easy for readers to over‑interpret. Adding “bracketed A95” or “A95, defined only up to the bracket (1.0%,1.5%]” in at least one of those summary paragraphs would prevent misinterpretation.

---

## P4‑N1: No new figure‑caption vs body numerical mismatches found

Given the text excerpt, the only explicit figure‑embedded numbers we can check are:

- Fig. 8 caption’s σℓ=1 = 3.63 vs canonical +3.64σ in Sec. IV.D. This is within rounding differences, and you explicitly say the figure once had annotations from a separate 1,000‑shuffle run; the current caption clarifies this historical detail.
- Other figures (e.g., maps, distributions) do not carry raw numbers beyond what’s in tables.

So for (B) and (I) in your checklist: within the excerpt, figure annotations and table/body values are aligned to the level of precision you quote.

---

## P4‑N2: Internal cross‑references appear largely consistent, but with a few fragile spots

Spot‑checking (D):

1. **“Sec. IV C” vs content**

   - The Introduction says “a chirality dipole measurement with an empirical 50%-recovery-3σ injection‑recovery threshold at |A_dipole|≥0.75%.”  
   - That threshold is actually defined in Sec. VI.A and Table V, not in Sec. IV.C.  
   - Sec. IV.C is the real‑space dipole analysis, which *uses* A₅₀ only indirectly for interpretation.

   So “see Sec. IV C” for the 0.75% threshold is slightly misleading; “Sec. VI A” would be more accurate.

2. **“Sec. VII, artifact c9b” cross‑projection**

   - The cross‑projection of Shamir‑class dipoles through the MASTER channel is described in Conclusions (a), with the reference “Sec. VII, artifact c9b.”
   - Sec. VII.e mentions A50 and A95 but not the explicit 68–218σ recovered harmonic significance; that is only in the Conclusions paragraph itself. Technically, that paragraph is part of Sec. VII, so the \S reference is OK, but the cross‑reference to “Sec. VII” in earlier sections is weakly supported by explicit text.

Not fatal, but worth tightening: every ref should point to a place where the relevant number or equation is actually *shown*.

---

If you want, I can now walk through the abstract line‑by‑line and produce a table mapping each clause to the exact line(s)/table(s) in the body where a referee can recompute or verify it, and flag any remaining gaps.