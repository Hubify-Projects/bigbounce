# P2 R23conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.45.pdf` md5=d421f116 pages=22
**Input format**: TEXT + web search + pass-2 self-critique (18096 chars)
**Wall time**: 101.9s

---

P2-E1 (ESSENTIAL) – Global (all pages) – No actual PDF available  
Problem: The review instructions require auditing “the rendered PDF you are looking at,” but only LaTeX-like body text has been provided in the prompt. I cannot see the actual typeset PDF (no page breaks, figure rendering, axis labels, or the actual formatted reference list as it appears in the submission). I also cannot access an external PDF version of this exact PRD submission via web search, since the draft appears to be an as‑yet‑unpublished manuscript.  
Required fix: The journal/editor must ensure that citation forensics and consistency checks are performed on the actual typeset PDF (including figures, tables, equations, and the formatted bibliography). My findings below are therefore limited to the plain text supplied, which cannot be mapped reliably to page numbers or to the exact reference list formatting.

Given that constraint, I can still audit the **citation forensics** and **numeric/statistical claims** against the external literature and internal consistency. I label findings by approximate section rather than page.

---

## 1. Citation forensics and reference integrity

### P2-E2 (ESSENTIAL) – References [7], , and the −35/8 vs −35/16 claim

**Location:** Sec. II A, II C, Appendix A (and Abstract).  
**Quoted text (representative):**

- “a matter-dominated contracting phase … produces a … local-type non-Gaussianity \(f_{\mathrm{NL}} = -35/8 = -4.375\) (Cai et al. 2009).”
- “Cai & Brandenberger  obtain \(f_{\mathrm{NL}}=-35/16=-2.1875\)… We performed a source-to-source normalization audit and established that this is a convention difference, not a physical one.”
- Appendix A claims the factor-of-two is entirely an in–in commutator issue, not physics.

**External check:**

- The primary “Non-gaussianity in a matter bounce” paper is Cai et al., JCAP 0905:011 (2009), arXiv:0903.0631.[7] That paper indeed computes a negative local-type \(f_{\mathrm{NL}}\) with benchmark values \(-35/8\) in their normalization.  
- The later “Non-Gaussianity in a matter bounce” by Cai & Brandenberger, Phys. Rev. D 90, 023534 (2014), arXiv:1404.4364, does find a different normalization; that difference is subtle and involves conventions (e.g. the \(c=1\) vs \(c=2\) Komatsu–Spergel/Planck prefactor) as well as treatment of time orderings.

I cannot, without inspecting those PDFs line‑by‑line, confirm the *exact* operator-level mapping the author asserts (that Cai & Brandenberger’s −35/16 is literally the single‑time‑ordered result in the same c=2 convention, rather than a different c). The paper presents this as a completed, “established” equivalence.

**Problem:** The claim that the two published results are *physically identical* and differ only by the missing commutator factor is strong and nontrivial. Given PRD standards, this needs:

- explicit, checkable algebra that matches the precise definitions used in both cited works, *including* their choice of \(B_\zeta\) normalization and \(f_{\mathrm{NL}}\) convention, not just a qualitative argument,
- and ideally some phrase that acknowledges that this is *the author’s re‑interpretation*, not a statement made by Cai or Cai & Brandenberger themselves.

At present, the argument in Appendix A is heuristic (and not obviously derived from the actual equations in [7] and  with the precise notational mapping).

**Required fix:**

- Either downgrade the language to clearly own this as the author’s interpretation (e.g. “we argue that…”, “our analysis suggests…”) and document the exact mapping between the normalizations in the two papers with explicit equation numbers from [7] and ; or provide a full, self‑contained derivation of the bispectrum from the Maldacena action to the final \(f_{\mathrm{NL}}\), in the Planck \(c=2\) convention, verifying −35/8 independent of Cai et al.
- Make clear that, to the best of your knowledge, neither [7] nor  themselves state that one is a single‑ordering version of the other in the same convention.
- Until such a derivation is included, the strong language (“established”) should be softened and the convention ambiguity treated as a genuine theoretical uncertainty, not as completely resolved.

---

### P2-E3 (ESSENTIAL) – Nonexistent or unverifiable internal citation / code archive URL

**Location:** Data and Code Availability section.  
**Text:**  
“all analysis code … are available at `https://github.com/Hubify-Projects/bigbounce/tree/main/research/`.”

**External check:** I cannot access non-public GitHub repositories or confirm that this exact path exists and contains what is claimed. The repository name and path look “personal” and are not standard for a PRD submission.

**Problem:** PRD does not require public code hosting, but if a specific repository path is cited as containing the full reproducibility stack, it must actually exist and be stable. As of now, from the review environment, this is unverifiable.

**Required fix:**

- Either (a) ensure the repository is public, stable, and actually contains the promised code and data, and adjust the text to indicate a DOI‑backed archive (e.g., Zenodo) for long‑term preservation, or (b) remove/soften the claim and state that code will be made available upon reasonable request.
- In any case, remove the full HTTPS URL if PRD’s style discourages it; instead describe the archive in a way that can go into the journal (e.g. “public GitHub repository ‘Hubify‑Projects/bigbounce’ and DOI‑archived snapshot”).

---

### P2-M1 (MAJOR) – Citation  (Zhu & Cai 2026, arXiv:2603.13924)

**Location:** Sec. II C (assumption (e) discussion).  
**Text:**  
“… as required by certain dark-energy mechanisms in modified-gravity bounce cosmologies; e.g., Zhu & Cai …”  

**External check:** arXiv:2603.13924 is stated in the reviewer metadata as existing. I cannot directly inspect it from this environment, but assuming this is a 2026 preprint, using it in a PRD 2026 submission is acceptable. However:

- The citation is used as an *example* of bounce models with prolonged post‑bounce inflation “as required by some dark-energy-from-bounce constructions.”

Without inspecting 2603.13924, I cannot confirm that it indeed presents “dark-energy-from-bounce” with prolonged inflation, rather than something else.

**Required fix:**

- Verify explicitly that Zhu & Cai 2603.13924 actually discusses prolonged post‑bounce inflation for dark‑energy purposes, and adjust the prose if the cited paper’s focus is different (e.g. relic gravitational waves).
- If not exact, replace or supplement with a paper that *does* explicitly show the mechanism you are invoking.

---

### P2-M2 (MAJOR) – Reference formatting and completeness (general)

**Location:** Entire reference list.  

By comparing the in‑text citations with the listed references at the end, I see:

- [1] Maldacena, JHEP 0305 (2003) – looks correct.  
- [2] Pajer et al. 2013; [3] Tanaka & Urakawa 2011 – look plausible and consistent.  
- [4] Heinrich et al. 2024, Phys. Rev. D 109, 123511 – matches arXiv:2311.13082.[4]  
-  Doré et al. 2014 SPHEREx white paper – correctly identified as arXiv e‑print 1412.4872.  
-  Schlegel et al. 2022 MegaMapper concept – arXiv:2209.04322.  
-  Addis et al. 2025, arXiv:2511.09466 – future‑dated but flagged in the reviewer metadata as existing.

Potential issues:

- Some later references ( Jung et al. 2025 Planck PR4,  Euclid 2025,  Diego-Palazuelos 2025) are cited as “astronomy & astrophysics 702, A204 (2025)” or “arXiv preprint 2509.13654” etc. I cannot fully verify volume/page/issue numbers for these 2025–26 works, since they may not yet be in final journal form.  
- The paper mixes “arXiv e‑prints (2014)” with explicit journal metadata inconsistently.

**Required fix:**

- Once the final journal references are available (or if not, at least the confirmed arXiv IDs with correct titles and authors), standardize the bibliography to PRD format: author list, journal, volume, page, year, and arXiv ID.
- Double‑check each future‑dated reference (years 2025–26): are they accepted/published, or still preprints? Use consistent labels (“arXiv e‑print” for unpublished, journal citation for published).
- For every reference from which a specific numerical forecast or constraint is taken (e.g. \(σ(f_{\mathrm{NL}})=0.7\) from Heinrich et al., Planck \(f_{\mathrm{NL}}\) errors from Jung et al.), explicitly confirm that the quoted numbers match their abstract/tables, and if not, correct them and update the citation.

---

## 2. Internal numerical/statistical consistency

### P2-E4 (ESSENTIAL) – Ambiguity and possible internal inconsistency in detection significance calculations

**Location:** Abstract, Sec. III B, Sec. IV, Fig. 2, Appendix A.2.  
**Key claims:**

- SPHEREx bispectrum forecast: \(σ(f_{\mathrm{NL}}^{\rm local}) ≈ 0.7\) from Heinrich et al. [4], leading to:

  - naive significance for \(f_{\mathrm{NL}}=-4.375\): \(6.25σ\),
  - template overlap \(r ≈ 0.84\) reduces this to \(5.2–5.5σ\) before other systematics,
  - after “full systematic budget,” “headline” \(3–5σ\).

- Appendix A.2 table explicitly gives \(5.25σ\) (using \(r=0.84\) and \(σ=0.7\)).

**Problem:**

1. In several places, the text states ranges (e.g. “5.2–5.5σ”) that are only loosely justified. Given the inputs:

   \[
   f_{\mathrm{NL}} = -4.375, \quad σ = 0.7, \quad r = 0.84 \pm 0.02,
   \]
   the central significance is
   \[
   |f_{\mathrm{NL}}|\,r/σ = 4.375 × 0.84 / 0.7 ≈ 5.25,
   \]
   corresponding to a *very narrow* range (roughly 5.1–5.4σ across \(r\in[0.83,0.88]\)). The text’s 5.2–5.5σ seems to round upward without clearly stating which values of \(r\) and ϵ‑correction are being combined.

2. The jump from “5.2–5.5σ prior to systematics” to “3–5σ after systematics” is qualitatively justified (GR, \(b_\phi\), photo‑z, etc.) but not *quantitatively* transparent. The reader cannot reconstruct the endpoints of “3” and “5” from the listed degradations (10–30% here, 20–50% there). Some combinations (max degradations stacked) arguably could push the lower end *below* 3σ, but this is not discussed.

3. The abstract gives both “3–5σ” and “5.2–5.5σ as the optimistic case…” but the body uses slightly different language in different locations; this is easy to misinterpret as mixing distinct null procedures, violating the journal’s requirement that sigma values from different procedures not be juxtaposed without explicit warnings.

**Required fix:**

- Provide a single, explicit “sigma pipeline” table (or a short subsection) that starts from:

  - the Heinrich et al. baseline \(σ(f_{\mathrm{NL}})=0.7\),
  - then *multiplicatively* applies: template mismatch (r), ϵ‑correction, GR degradation (σ_GR choice), \(b_\phi\) prior broadening, photo‑z, etc.,

  and shows clearly:

  \[
  σ_{\rm eff}^{\rm optimistic}, \quad σ_{\rm eff}^{\rm baseline}, \quad σ_{\rm eff}^{\rm conservative},
  \]
  plus the corresponding significances. Reference this explicitly in the abstract and in Fig. 2, so that each quoted sigma range can be recomputed by the reader.

- Avoid mixing slightly different numeric ranges (“5.2–5.5σ” vs explicit “5.25σ”) without explaining the origin of the difference (e.g. rounding, different r values).
- In the abstract, explicitly state that the 3–5σ range corresponds to *after applying the full systematic budget described in Sec. VII*, and that 5.2–5.5σ is the optimistic, template‑only correction, so the two σ’s are not from the same null procedure.

---

### P2-M3 (MAJOR) – Joint \((f_{\rm NL}, n_{f_{\rm NL}})\) Fisher numbers vs withdrawn “9.9σ” claim

**Location:** Round context in metadata; Sec. VIII D and the correction note in Sec. IX.  
The reviewer metadata says the previous version had a “withdrawn ~9.9σ SDB joint-Fisher claim,” replaced here by:

- \(σ(n_{f_{\rm NL}})=0.295/0.596\),
- \(σ_{\rm marg}(f_{\rm NL}) = 3.08/7.06\),
- fixed‑bias vs bias‑marginalized.

In the text you clearly mark the old result as withdrawn and provide the new, weaker numbers.

**Problem:**

- For PRD, any previous over‑optimistic claim must be fully quarantined. The current text does a decent job, but some phrases (“could not be reproduced from documented survey inputs and are withdrawn”) presume a version‑history context that does not belong in a standalone PRD article.
- It is also not fully clear to the reader whether all subsequent uses of joint \((f_{\rm NL}, n_{f_{\rm NL}})\) constraints in the paper (e.g. in Sec. IX) rely only on the new numbers, and whether any of the 3–5σ detection headlines were ever influenced by the old 9.9σ pipeline.

**Required fix:**

- Remove all version‑history language (“earlier version,” “withdrawn”) from the main body. Instead, simply present the current joint Fisher result and explain its (limited) role: that the bispectrum‑only σ=0.7 forecast is the primary driver of the headline and the SDB joint analysis is only a cross‑check.
- If the journal allows, mention the correction history in a short footnote or erratum note, but not as in‑line narrative.
- Ensure that no detection claims rely on the old 9.9σ result; if any residual text appears to do so, revise.

---

### P2-M4 (MAJOR) – Bayes factor claims vs inputs

**Location:** Sec. VI, Table II, Table III.  
Claims: BF ∼ 10–17 vs tuned multifield, with a range across priors and GR systematics.

**Problem:**

- The Bayes factors are derived from a simple Gaussian‑likelihood, uniform‑prior model. The paper quotes specific numbers (e.g. BF=13.91, BF=9.80, BF=5.65) but only loosely gives formulas. For PRD, any Bayes factor above ~10 used as “headline” model-comparison evidence must be transparently traced back to its likelihood and prior widths.
- In particular, the dependence on σ_theory and competitor prior width is strong; the text acknowledges this but still presents BF ∼ 10–17 in the abstract as a “headline envelope,” which risks overinterpretation.

**Required fix:**

- Include a compact explicit formula for the Bayes factor used (for a delta prior vs uniform prior, and for a Gaussian prior vs uniform prior), with all symbols defined.
- In Table II, give the *assumed σ(f_{\rm NL})* and central value for each scenario, not just BF. Make it clear that BF ≥ 10 occurs only under relatively optimistic assumptions: σ_theory ≲ 1 and competitor prior width [−15, +15].
- In the abstract, explicitly qualify the BF ∼ 10–17 statement as “conditional on the assumed priors [as detailed in Sec. VI]” and clarify that the most physically motivated baseline is BF ∼ 10, not the upper 17.

---

## 3. Conceptual and phrasing issues

### P2-M5 (MAJOR) – Use of “mechanism-independent” vs “UV-completion-independent”

**Location:** Sec. I, II B, II C.  

You correctly backpedal from “mechanism-independent” to “UV-completion-independent within the scalar-only Wilson–Ewing class, conditional on assumptions (a)–(f).”

**Problem:** In some places (e.g. abstract, introductory lines) the language remains strong enough that a non-expert might misread this as generic model-independence across the entire bounce landscape.

**Required fix:**

- Replace any remaining occurrences of “mechanism-independent” in the main text and abstract with the more precise phrase you already use in the body: “UV-completion-independent within the scalar-only matter-bounce/Wilson–Ewing class under assumptions (a)–(f).”
- Emphasize once in the abstract that the prediction is *not* model‑independent once fermions, modified gravity, or prolonged post-bounce inflation are allowed.

---

### P2-N1 (NIT) – Minor duplicated/verbatim phrases

I did not see obvious “canonical canonical-mask”–type duplicated phrases in the provided text, but the manuscript is long. A simple search on the LaTeX source is advisable to ensure no duplicated constructions or copy‑paste glitches remain (e.g. repeated entire sentences in different sections).

**Required fix:** Run an automated search for repeated multi‑word strings; remove or rephrase any exact duplicates that are not intentional.

---

### P2-N2 (NIT) – Length vs contribution

**Location:** Global.  

At 22 pages of dense text plus heavy appendices, the paper is quite long for a single forecast and conceptual comparison, especially given that:

- It **does not** perform a full independent SPHEREx Fisher forecast (it recasts Heinrich et al.),
- The bispectrum/bounce algebra is only partially recomputed (relying on Cai et al.),
- The Bayesian comparison is conceptually straightforward once the Gaussian likelihood is fixed.

**Required fix / recommendation:**

- The main body could reasonably be reduced to ≈16–18 PRD pages by compressing:

  - the lengthy narrative around the coefficient‑null‑space scan (Sec. II),  
  - some of the systematics discussion (Sec. VII) that currently reads like a mini‑review,  
  - and especially the extended version‑history and correction commentary.

- Keep the full technical details (e.g. the Wick‑doubling appendix) but tighten the prose and remove repetition.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The draft is ambitious and technically sophisticated, but several key claims that are central for a PRD‑level “headline” (the normalization of \(f_{\mathrm{NL}}\), the SPHEREx detection significance chain, and the Bayes factor range) are not yet documented with sufficient rigor and transparency. The normalization reconciliation between Cai et al. and Cai & Brandenberger needs either a fully explicit derivation or a more cautious, clearly labeled interpretation. The multi‑σ detection claims and Bayes factors must be backed by clean, reconstructible calculations, and version‑history/correction language must be removed from the main narrative. Once these issues are addressed and the exposition is tightened, the paper could be suitable for serious consideration.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E5 (ESSENTIAL) – Arithmetic and percentage inconsistencies in abstract vs body (template overlap and null‑space scatter)  

- **Location:** Abstract; Sec. II A (null‑space scan); Sec. III B (template overlap); around Eq. (6).  
- **Issue 1 – Null‑space scatter phrasing is mathematically inconsistent.**  
  Abstract: “polynomial‑coefficient null-space amplitude scatter ±0.13 absolute in r (corresponding to ∼15% relative scatter at r̄ = 0.85, range 0.55–1.14 in the body of §II C).”  
  Body: “The amplitude recovery factor is r = 0.85 ± 0.13 (range: 0.55–1.14)… the median r = 0.85 and the interquartile range [0.75, 0.94]…”  

  Problems:  
  - If the distribution is *mean* 0.85 with **symmetric** ±0.13, the implied range would be [0.72, 0.98], not [0.55, 1.14]. The quoted 0.55–1.14 is ~±0.30 about 0.85, more than 2σ if 0.13 is interpreted as 1σ.  
  - “±0.13” is presented as *absolute* scatter and simultaneously mapped to “range 0.55–1.14,” which is inconsistent unless ±0.13 is meant as something like half the interquartile width, while the 0.55–1.14 range refers to full extremes. This is never stated.  
  - 0.13/0.85 ≈ 15.3%, so the “∼15%” statement is arithmetically correct, but the mixture of “±0.13” and full range 0.55–1.14 is conceptually inconsistent.  

  **Required fix:**  
  - Clarify whether ±0.13 is the standard deviation, the half‑width of the interquartile range, or something else.  
  - If the full sample range is 0.55–1.14, state that explicitly (e.g., “median 0.85, IQR [0.75, 0.94], full range [0.55, 1.14]”), and remove or redefine the misleading “±0.13.”  
  - Align the abstract wording with the clarified statistics in the body.

- **Issue 2 – Overlap ranges and degradations are internally inconsistent.**  
  Abstract: r ∈ [0.829, 0.876]; body:  
  - Eq. (6): r = 0.84 ± 0.02 with “range r ∈ [0.829, 0.876] spanning all physically motivated weighting schemes.”  
  - Immediately after: “the three noise-weighted values 0.829, 0.830, 0.835, together with the signal-only value 0.876 — four values total.”  

  There is no explicit fifth point that would fill the entire closed interval [0.829, 0.876]; the “range” is actually the min and max of four discrete values. This is a minor but pervasive sloppiness in how ranges are described.  

  **Required fix:**  
  - Phrase this as “we obtain four overlap values between 0.829 and 0.876 (0.829, 0.830, 0.835, 0.876)…”, not as a continuous “r ∈ [0.829, 0.876] across schemes,” unless an actual continuous scan is done.  
  - Make clear that the ±0.02 around 0.84 is an envelope from the weighting‑scheme variation, not an actual 1σ statistical error.

---

P2-E6 (ESSENTIAL) – Misleading “3–5σ” range construction and mixing of envelopes from different null procedures  

- **Location:** Abstract; Sec. IV; Fig. 2 caption; Sec. VII B; Sec. X; Appendix A.2 table.  
- **Issue:** The “3–5σ” SPHEREx range is presented as a single object but is numerically constructed by mixing *different* assumptions and null procedures:  
  - Baseline: Heinrich et al. σ(fNL) = 0.7 (bispectrum only).  
  - Template‑only: r ≈ 0.83–0.88 ⇒ 5.2–5.5σ.  
  - “Realistic” 3–5σ: includes GR, bϕ, photo‑z, etc., but the exact multiplicative degradations applied to go from 5.2–5.5σ down to 3–5σ are never tabulated.  
  - Sec. VII B states that relaxing bϕ universality alone can degrade 5.2–5.5σ to “∼4.0–4.5σ (30% central) and ∼3.5–3.7σ (50% conservative).” Combining this with GR (10–30%) and other effects could easily push the *lower* end of the total significance below 3σ, yet the abstract and Fig. 2 keep “3–5σ” as the post‑systematics headline without acknowledging that some plausible combinations of degradations yield <3σ.  

  This violates the requested “null‑procedure comparability”: sigma values derived under different combinations of systematics and prior assumptions are juxtaposed as a coherent range, and the lower bound (“3σ”) is not transparently tied to a specific set of assumptions in the body.  

  **Required fix:**  
  - Add a compact table that starts from 6.25σ (|fNL|/σ), then clearly and *multiplicatively* applies: r, ϵ‑correction, GR degradation (e.g., 15% or 30%), bϕ marginalization (20–50%), photo‑z, etc. Provide three explicit rows: optimistic, baseline, conservative, with the final σ for each.  
  - Explicitly tie the “3σ” end of the 3–5σ range to a particular conservative combination (e.g., r = 0.83, ϵ worst case, 30% GR, 50% bϕ), and state that even more conservative assumptions would drop below 3σ and are not included in the headline.  
  - In the abstract and Fig. 2, explicitly label “3–5σ” as an *envelope over distinct scenarios*, not a single error bar, and explicitly mark that it is not directly comparable to the 5.2–5.5σ template‑only value.

---

P2-M6 (MAJOR) – Inconsistent and unclear use of “σ(fNL) ≈ 0.7” vs “σ(fNL) ≈ 0.5” across abstract, Sec. IV, Sec. VIII B  

- **Location:** Abstract; Sec. IV; Sec. VIII A and VIII B; Conclusion.  
- **Issue:** The paper oscillates between σ(fNL) ≈ 0.7 and “≈0.5–0.7” for SPHEREx without clear bookkeeping of which number is used where:  
  - Abstract: “SPHEREx multi-tracer bispectrum achieves σ(fNL^local) ≈ 0.7… The bispectrum-only 5.2–5.5σ is the headline forecast of this paper.”  
  - Sec. IV: “σ(fNL) = 0.7 as our baseline… The Heinrich et al. forecast… σ(fNL^local) = 0.7 from the bispectrum alone, with σ(fNL^local) = 0.5 when combined with the power spectrum… The abstract’s headline σ(fNL) ≈ 0.7 is the bispectrum-only number, and is consistent with the lower end of the ≈ 0.5–0.7 range quoted here.”  
  - Sec. VIII B: “σ(fNL) ≈ 0.7 for the bispectrum-only forecast, or ≈ 0.5 for the joint bispectrum-plus-power-spectrum forecast, from Heinrich et al. 2024; the abstract’s headline σ(fNL) ≈ 0.7 is the bispectrum-only number, and is consistent with the lower end of the ≈ 0.5–0.7 range quoted here.”  

  Problems:  
  - The abstract never mentions the 0.5 value; the body uses it when convenient (for “joint” ns–fNL discussion) but then explicitly says the *headline* uses 0.7.  
  - Detection significances quoted (5.2–5.5σ) are based on σ = 0.7, but the reader could easily misread later mentions of σ ≈ 0.5 as part of the same pipeline or as supporting a stronger detection; the paper does not clearly fence off the joint (power+bispectrum) σ from the bispectrum-only pipeline used in Bayes factors and decision thresholds.  

  **Required fix:**  
  - State once, near the beginning of Sec. IV, that *all* detection significances and Bayes factors in this paper use the σ = 0.7 bispectrum-only forecast, and that the σ ≈ 0.5 combined forecast is cited only as context, not used in any numbers.  
  - Wherever σ = 0.5 is mentioned (Sec. IV, Sec. VIII B), add an explicit sentence: “We do not use this σ = 0.5 value in any significance or Bayes‑factor calculation in this work.”  
  - Ensure that plots and tables (decision thresholds, Bayes factors) are clearly labeled as using σ(fNL) = 0.7.

---

P2-M7 (MAJOR) – Misleading “factor‑of‑two” and “halving” language for the Cai vs. Li–Brandenberger convention  

- **Location:** Abstract (final caveat); Sec. II C (paragraph on factor‑of‑two discrepancy); Conclusion; Appendix A.2 and Table IV.  
- **Issue:** Numerically, the change from −35/8 to −35/16 reduces |fNL| by a factor of 2 (4.375 → 2.1875). However, the way the “halving” is propagated through significances is sloppy:  
  - Abstract: “the optimistic, pre-systematic-budget 5.2–5.5σ range halves to ∼ 2.6–2.75σ, and the post-systematic-budget headline 3–5σ halves to ∼ 1.5–2.5σ.”  
  - Appendix A.2 shows |fNL|r/σ = 5.25σ vs 2.63σ for the two conventions (exact factor of 2 in the central optimistic case), but for the 3–5σ envelope there is no explicit recomputation; the “halves to 1.5–2.5σ” phrase implicitly assumes every part of the systematic budget (including r, GR, bϕ) is independent of convention and thus that every point in the 3–5σ envelope scales exactly by 1/2.  

  In reality:  
  - The systematic degradations (GR, bϕ marginalization, photo‑z, null‑space scatter) are *σ‑inflating* factors, independent of convention, so significance scales as |fNL|/σ_eff. Changing |fNL| by 2 does indeed divide all significances by 2, but that *only* holds if σ_eff is the same in both conventions. The paper mixes this exact arithmetic identity with hand‑wavy 3–5σ envelopes without showing σ_eff explicitly, so the “halving” of the entire envelope is asserted but not demonstrated.  

  **Required fix:**  
  - Add an explicit statement (ideally a short equation) that for fixed σ_eff, changing from fNL = −35/8 to −35/16 simply multiplies all detection significances by 1/2, independent of the systematic budget.  
  - In the abstract and conclusion, replace the casual “halves to 1.5–2.5σ” with a more explicit explanation: e.g., “all quoted significances scale linearly with |fNL|; adopting −35/16 instead of −35/8 divides every σ by 2, so the 3–5σ envelope becomes 1.5–2.5σ under otherwise identical assumptions.”  
  - Make sure this is clearly distinguished from any change in σ(fNL) itself (which is *convention‑independent*, as correctly noted in Appendix A.2).

---

P2-M8 (MAJOR) – Ambiguous handling of r > 1 and consistency with Eq. (5)  

- **Location:** Sec. III B, Eq. (5) and surrounding text; footnote 2; Sec. II A null‑space scan discussion.  
- **Issue:**  
  - Eq. (5) defines the relation between the measured local‑template amplitude and the “true” bounce amplitude as  
    \[
    f_{\rm NL}^{\rm measured} = r \times f_{\rm NL}^{\rm bounce},\quad \sigma(f_{\rm NL}^{\rm bounce}) = \sigma(f_{\rm NL}^{\rm local})/r.
    \]
  - The text then says “The canonical inequality 0 < r ≤ 1 holds strictly for canonical single-field bispectra… for the matter-bounce shape, the weighted average can mildly exceed unity (up to r ≲ 1.2 in our 10,000-sample null-space scan…).” A footnote explains this as some coefficient choices making |BNL| at intermediate triangles larger than in the squeezed limit.  

  Problems:  
  - If r > 1 is allowed, the simple interpretation of r as “fraction of the bounce signal recovered by a local template” breaks: the local template cannot recover more than 100% of the amplitude unless “amplitude” is defined relative to the squeezed limit only. The text alludes to this but does not reconcile it with Eq. (5), which still treats r as if it were always ≤ 1.  
  - The abstract and several sections use language like “recovers 84% ± 2% of the bounce signal” and “template mismatch… r = 0.84 ± 0.02,” which implicitly assumes r ≤ 1. The existence of r > 1 samples in the null‑space scan is potentially confusing and could be misinterpreted as the forecast occasionally *overstating* the bounce amplitude.  

  **Required fix:**  
  - Restrict the use of Eq. (5) (and all detection‑significance calculations) explicitly to the physically motivated coefficient set with r < 1 (the reference set and the noise‑weighted averages), and make clear that the r > 1 cases are pathological null‑space directions used only to characterize shape variability, not to define the effective r entering forecasts.  
  - Alternatively, redefine r consistently as the Fisher‑weighted overlap normalized to the *true* Fisher‑optimal estimator, and explain explicitly how r > 1 is interpreted (e.g., as an artifact of using the squeezed‑limit normalization).  
  - In the abstract, remove or qualify “84% ± 2% of the bounce signal” so that it is strictly true for the coefficient choices actually used in forecasts.

---

P2-M9 (MAJOR) – Abstract “first time” novelty claim not fully supported  

- **Location:** Abstract, first paragraph: “We quantify for the first time the template mismatch between the matter-bounce and local templates…”  
- **Issue:** This is a strong novelty claim. The body states “a literature search confirming no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024).” There is no detailed comparison with related work (e.g., generic shape‑cosine studies that might have included matter‑bounce‑like shapes), no explicit citation that “no one has done this,” and no systematic evidence that the search was exhaustive.  

  **Required fix:**  
  - Soften the claim: e.g., “We provide a detailed quantification of the template mismatch…” or “To our knowledge, this is the first explicit quantification…” and keep the “literature search” remark as the support.  
  - Optionally, add 1–2 sentences in Sec. III B summarizing what related works (if any) have done for other non‑inflationary shapes, to justify the “to our knowledge” phrasing.

---

P2-M10 (MAJOR) – Weak support for “unprecedented precision” and other superlatives  

- **Location:** Introduction, last paragraph: “constrain local-type fNL at unprecedented precision through the scale-dependent bias effect and the galaxy bispectrum.”  
- **Issue:** “Unprecedented precision” is a novelty/superlative claim. The paper cites future σ forecasts for SPHEREx, DESI, Euclid, LSST, CMB‑S4 later, but never explicitly compares the SPHEREx σ(fNL) = 0.7 (or 0.5) to the *best existing* constraints in a numerical way in the introduction. Planck σ ≈ 5 is quoted later, but the text does not explicitly connect that to the “unprecedented” claim where it is made.  

  **Required fix:**  
  - In the introduction, immediately follow “unprecedented precision” with an explicit contrast: e.g., “Planck PR4 currently gives σ(fNL) ≈ 5, while SPHEREx forecasts σ(fNL) ≈ 0.7 from the bispectrum and ≈ 0.5 when combined with the power spectrum.”  
  - Alternatively, remove “unprecedented” and say “substantially improved precision.”

---

P2-m11 (MINOR) – Abstract numerical parenthetical inconsistent with body description of null-space range  

- **Location:** Abstract: “…null-space scan of the underdetermined polynomial coefficients (shape cosine r_cos > 0.97 for all samples).”  
- **Body:** Sec. II A: “The shape cosine exceeds 0.97 for all 10,000 samples (r_cos = 0.985 ± 0.007).”  

  These are consistent numerically, but the abstract’s “> 0.97” could be misread as the *minimum* cosine, whereas the body provides a mean ± scatter. This is minor, but given the emphasis on robustness, the abstract could be more precise.  

  **Required fix:**  
  - Optionally rephrase abstract to “(shape cosine r_cos = 0.985 ± 0.007, always > 0.97 across 10,000 samples)” to match the body.

---

P2-m12 (MINOR) – Decision-threshold figure and text understate dependence on systematic budget  

- **Location:** Fig. 6 and its description; Sec. IX C.  
- **Issue:** Fig. 6 shows “green: strongly favors bounce; red: strongly disfavors… Error bars: SPHEREx (σ = 0.7) and MegaMapper conservative (σ = 1.5).” The main text says a null measurement would exclude the bounce at >4σ “after the realistic systematic budget of Sec. VII,” but there is no visual indication in Fig. 6 of how the significance changes under different systematics scenarios (e.g., σ inflated to 0.9–1.0). This can be misread as suggesting that the decision thresholds are robust to all systematics.  

  **Required fix:**  
  - Add a thin secondary error bar or shading on the SPHEREx point showing the σ range under baseline vs conservative systematics (e.g., σ = 0.7–1.0), or explicitly state in the caption that the plotted error bars correspond to the *ideal or baseline* σ only, not to the full 3–5σ envelope.  

---

P2-m13 (MINOR) – Abstract “3–7σ” MegaMapper range not transparently backed by numbers  

- **Location:** Abstract: “MegaMapper … could reach σ(fNL) ≈ 0.5 ideally (3–7σ realistic…).”  
- **Body:** Sec. V:  
  - “7.4–7.7σ at the published ideal σ(fNL) = 0.5… 3–5σ after the same GR marginalization and bϕ uncertainty budget… At an intermediate σ(fNL) = 0.7…, the template-corrected significance is ∼ 5.2σ optimistic, ∼ 3.5σ conservative. The abstract quotes a wide 3–7σ range spanning the full envelope from the conservative systematic scenario to the midpoint between the ideal and degraded cases; this range reflects design uncertainty… and should not be interpreted as a well-characterized error bar.”  

  The abstract’s “3–7σ realistic” wording can be misread as a standard 1σ error range, whereas in the body it is explicitly called a qualitative envelope tied to both instrument design uncertainty and systematics.  

  **Required fix:**  
  - In the abstract, qualify this explicitly as an “indicative 3–7σ envelope (not a formal error bar), reflecting both design and systematics uncertainty as detailed in Sec. V.”  

---

P2-m14 (MINOR) – Slight mismatch in Planck PR4 recast arithmetic  

- **Location:** Sec. VIII A.  
- **Text:** “Planck PR4/NPIPE… fNL = −0.1 ± 5.0… Recasting… with r = 0.876 gives fNL^bounce = −0.1 ± 5.7… 0.7σ from the bounce prediction and 0.02σ from zero…”  

  Checks:  
  - σ_bounce = 5.0 / 0.876 ≈ 5.71 (quoted 5.7; OK).  
  - Distance to bounce (−4.375): |−0.1 − (−4.375)| / 5.7 ≈ 4.275 / 5.7 ≈ 0.75σ, quoted 0.7σ – slight rounding, acceptable.  
  - Distance to zero: |−0.1| / 5.0 = 0.02σ: exact.  

  Nothing is numerically wrong, but the bounce distance is rounded differently from other σs in the paper.  

  **Required fix:**  
  - Optional: either quote 0.75σ or say “≈0.8σ” for consistency with usual rounding.

---

NO additional dimensional‑consistency or cross‑reference errors identified beyond those in the initial review  

- Dimensional analysis of the key equations (e.g., Eqs. (3)–(4) for Δb and M(k,z); the fNL–ns relation Eq. (8); the Bayes‑factor expression Eq. (7)) is standard and appears consistent within the usual cosmology conventions.  
- Internal \ref/\eqref/\cite uses in the provided text generally point to the correct sections and equations; the main cross‑reference problems are conceptual (e.g. mixing different Fisher matrices) rather than pointing to the wrong equation.  

Given the constraints (text‑only, no actual PDF; some material truncated), these additional findings focus on arithmetic, envelope construction, and novelty/support issues that were not emphasised enough in the initial review.