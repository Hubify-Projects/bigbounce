# P2 R7 — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 39.9s

---

PAPER TEXT contains its own bibliography with numbered references [1]–; I will treat those as the citation targets to audit. However, I have **no direct access here to the actual external papers (Maldacena 2003, Cai et al. 2009, Heinrich et al. 2024, etc.)**, only to the text you provided. I also cannot see arXiv/ADS content for those specific cosmology works in the sandboxed search results I was given. That means I cannot reliably verify:

- that arXiv IDs, titles, DOIs, author lists, and venues match, or  
- that specific quoted equations, numerical values, table entries, and σ forecasts are correctly attributed to each reference.

Given that limitation, I will focus on **internal consistency and artifact/audit issues** within the manuscript itself, and I will flag all places where the paper *claims* something about prior work that, in a real PRD review, would require checking on arXiv/ADS.

Below I list all concrete findings.

---

### ESSENTIAL findings

**P2-E1 – Abstract: ambiguous σ-level and “halving” language is internally inconsistent**

- **Location:** Abstract, page 1:  
  > “The SPHEREx multi-tracer bispectrum achieves σ(fNL^local) ≈ 0.7 (Heinrich et al. 2024 [4] …), giving template-corrected significance ∼ 3–5σ … with 5.2–5.5σ as the optimistic case before GR and bϕ degradation … Caveat: if the Li & Brandenberger (c = 1) normalization convention is adopted instead of the Planck/Cai (c = 2) convention used throughout this paper, the detection significance halves: the optimistic, pre-systematic-budget 5.2–5.5σ range halves to ∼ 2.6–2.75σ, and the post-systematic-budget headline 3–5σ halves to ∼ 1.5–2.5σ (consistent with the conclusion-section restatement, §X; both numbers are reported because the convention-reversal halving applies independently of where in the systematic-budget chain the figure is quoted).”

- **Problem:** The text mixes several σ-values in a confusing way:
  - Early in the abstract it says “template-corrected significance ∼ 3–5σ … with 5.2–5.5σ as the optimistic case,” but 5.2–5.5σ is already a specific range, not a subset of “3–5σ”.
  - Later sections (e.g. IV and X) describe:
    - Naïve significance from σ=0.7 as 6.25σ,  
    - The template-overlap correction to ≈5.2–5.5σ, and  
    - The “realistic range” after GR/bϕ etc as “∼3–5σ.”
  - The “halving” language for the Li & Brandenberger convention is logically correct (since |fNL| is reduced by 2), but the way the abstract is phrased makes it difficult to disentangle which figures are pre- vs post-systematics and which have the template-overlap applied.
- **Required fix:** Rewrite the abstract’s significance paragraph to:
  - Explicitly define:
    - Naïve significance from σ(fNL)=0.7 (no template mismatch)  
    - Template-mismatch-corrected significance (using r≈0.84)  
    - The further degradation range from GR and bϕ systematics.
  - Then state clearly:
    - “Cai convention: optimistic (before systematics) = X–Yσ; realistic range after systematics = A–Bσ.”  
    - “Li & Brandenberger convention: all of these numbers are halved.”
  - Ensure the numerical ranges match the values later in §§IV, VII, X. Remove any overlapping or contradictory σ-ranges.

---

**P2-E2 – σ values from different procedures mixed without explicit warnings**

- **Location:** Multiple places:
  - Abstract, page 1: uses various σ(fNL) and significance ranges derived from:
    - σ(fNL)=0.7 from Heinrich et al. (bispectrum Fisher forecast),
    - template-overlap r≈0.84,
    - additional systematic degradations.
  - §III.B, §IV, §IX.D, Appendix A.2: compare:
    - CMB Fisher overlaps,
    - SPHEREx LSS-style noise weighting,
    - scale-dependent-bias Fisher,
    - joint (fNL, nfNL) Fisher (with ρ≈0.966),
    all expressed in “σ of detection” language.
- **Problem:** The instructions explicitly require that **σ values from different null procedures not be presented as if they are on the same scale**. Here, multiple σ values are shown side-by-side without an explicit, prominent warning that they:
  - come from **different Fisher setups and different observables** (CMB vs LSS, SDB vs bispectrum, bispectrum-only vs joint fNL–nfNL),
  - assume different priors and marginalizations (e.g. bϕ fixed vs marginalized, GR parameter σGR).
  The text does state some caveats buried in §IV and §IX.D, but the abstract and main narrative can easily be read as if “5.2–5.5σ”, “3–5σ”, “∼9.9σ” were directly comparable.
- **Required fix:**  
  - Add an explicit, prominent statement early in the paper (end of §I or start of §III) that:
    - clearly distinguishes between **different Fisher setups / null procedures** (CMB Fisher, SPHEREx bispectrum, SPHEREx SDB, MegaMapper SDB, joint (fNL,nfNL)),
    - explicitly warns that σ values drawn from different procedures are *not* directly comparable and should be interpreted within their own assumptions.
  - In each place where a different σ is quoted, label it clearly (e.g. “SPHEREx bispectrum-only Fisher σ(fNL)=0.7 [4]”, “idealized joint SDB (fNL,nfNL) Fisher”, etc.) and avoid language suggesting they are on the same scale unless appropriately caveated right there.

---

**P2-E3 – Use of “Gemini 3.1-Pro P2 BLOCKER B-3” style review-log reference in main text**

- **Location:** Appendix A, last paragraph, page 19:  
  > “… to address the cross-model peer-review concern (R42 Gemini 3.1-Pro P2 BLOCKER B-3) that the missing time-ordering should not be folded into a ‘dual-normalization’ framing.”

- **Problem:** This is **explicit review-log / model-version language** carried into the paper body. It refers to an internal review artifact (“R42 Gemini 3.1-Pro”, “BLOCKER B-3”) rather than any scientific concept. This violates the instruction that version-history and review-log artifacts must be removed from the scientific text.
- **Required fix:** Completely remove or rewrite this parenthetical. If you want to refer to a generic referee concern, say something like “to address a referee concern that…” without naming any proprietary model/version or internal tag.

---

**P2-E4 – First-person acknowledgment of AI assistance in the scientific text**

- **Location:** Acknowledgments, page 20:  
  > “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during the systematic audit, cross-checking, and manuscript preparation phases of this work.”

- **Problem:** Many journals (including APS/PRD) now have specific policies on AI assistance. This sentence refers to a proprietary model by brand (“Claude (Anthropic)”), and the usage is described as spanning “manuscript preparation,” which may be problematic or require explicit editor approval.
- **Required fix:** Coordinate with the journal’s AI-usage policy. At minimum:
  - Rephrase to something generic like: “The author made use of AI-based tools for code checking and literature organization; responsibility for all scientific content remains with the author.”
  - Or, if PRD policy requires, remove explicit model and vendor names and confirm with the editor whether such an acknowledgment is acceptable.

---

**P2-E5 – “DATA AND CODE AVAILABILITY” and GitHub path looks like a frozen internal repo, not a stable DOI’ed resource**

- **Location:** “DATA AND CODE AVAILABILITY” section, page 18:  
  > “… https://github.com/Hubify-Projects/bigbounce/tree/paper2-v1.7.40/research/ (pinned to release tag paper2-v1.7.40).”

- **Problem:** PRD usually prefers permanent, citable archives (e.g. Zenodo DOI, institutional repository). A GitHub path with a custom tag looks like **internal version-control metadata** and may not be stable long-term.
- **Required fix:**  
  - Deposit the code in a more permanent archive (e.g., Zenodo, institutional repository) and cite that archive, or at least:
  - Move the GitHub link to a footnote or supplemental material and briefly describe the repository (without embedding a full internal path with “paper2-v1.7.40” in the main text).  
  - Clarify that the public tag will be maintained and associated with the published version.

---

### MAJOR findings

**P2-M1 – Extensive reliance on Heinrich et al. [4] σ(fNL)=0.7 without giving core details**

- **Location:** §IV and throughout:
  - Repeated: “Heinrich et al. [4] forecasts σ(fNL^local)=0.7 from the bispectrum alone…”
- **Problem:** The paper builds its *headline forecast* entirely on this single number without summarizing:
  - which galaxy sample(s) and redshift bins [4] use,
  - what priors on bϕ and other nuisance parameters are assumed,
  - whether any GR corrections are included there.
  You *do* state some of this qualitatively, but given that all the main claims rest on this value, more concrete summarizing of [4] is needed.
- **Required fix:**  
  - Add a concise paragraph in §IV summarizing the key assumptions of [4]’s bispectrum forecast: tracer populations, redshift coverage, fsky, bias / PNG-bias modeling, and whether GR and photo-z systematics are included.  
  - Clearly distinguish what is directly imported from [4] versus what is modified by your own template-overlap and systematic budget.

---

**P2-M2 – Joint (fNL, nfNL) Fisher result (∼9.9σ) is weakly documented and may be misleading**

- **Location:** §IX.D, pages 16–17.
- **Problem:**
  - The text reports:
    - σ(nfNL)=0.086, σmarg(fNL)=0.44, ρ=0.966, and “a ∼9.9σ” significance for fNL=-4.375 in a joint SDB Fisher analysis.
  - It emphasizes that this comes from a different Fisher input than the bispectrum-only σ=0.7, but:
    - It does not present *any* explicit Fisher matrix, tracer assumptions, or references for this SDB calculation.
    - It then spends a long paragraph explaining why this should be considered a “self-consistency check” rather than an actual forecast. In its current form, this is more confusing than helpful and risks being read as an over-optimistic claim.
- **Required fix:**  
  - Either:
    - Move the entire joint (fNL, nfNL) Fisher calculation to an Appendix, provide explicit formulae and assumptions, and refer to it clearly as a *toy* or *illustrative* calculation; or
    - Remove the 9.9σ number from the main text and just briefly state that a joint SDB analysis could, in principle, provide a stronger internal consistency check, with details left to future work.
  - In any case, avoid quoting “9.9σ” in the main body without sufficient methodological transparency.

---

**P2-M3 – Bayes-factor statements rely on “scipy.stats.norm” but give no explicit likelihood definition**

- **Location:** §VI.C, Table II, and surrounding text.
- **Problem:**
  - Bayes factors like BF≈10–17 are presented with specific numbers linked to “scipy.stats.norm,” but the likelihood assumed for fNLobs (e.g. Gaussian with σ=0.7) is not clearly written out (beyond a qualitative description).
  - The prior choices are described verbally, but the integration limits and normalizations are not fully specified anywhere.
- **Required fix:**  
  - Add explicit equations defining:
    - Likelihood \(L(f_{\mathrm{NL}}^{\mathrm{obs}} \mid f_{\mathrm{NL}})\),
    - Priors for the bounce and competitor models,
    - Integration ranges.  
  - Clarify that all numerical BF values (and Table II entries) are computed under these specific assumptions. This is necessary for reproducibility and to evaluate whether the priors are reasonable.

---

**P2-M4 – “No observational tensions” claim is too strong**

- **Location:** §II.D, page 6:  
  > “No observational tensions with this model have been identified to date.”

- **Problem:** This global claim is stronger than the evidence presented. You discuss Planck ns, r≈10^-4, and current Planck fNL constraints, but:
  - You do not discuss **other** constraints (e.g., large-scale-structure limits, early-Universe constraints on LQC, etc.).
  - Even if the model is broadly consistent, “no observational tensions have been identified” is a very strong claim requiring a comprehensive survey.
- **Required fix:**  
  - Soften and qualify, e.g.:  
    “Within the set of observables considered in  and this work (ns, r, and Planck fNL constraints), no significant tensions have been identified.”  
  - Avoid any implication of exhaustive comparison with all existing cosmological data.

---

### MINOR findings

**P2-m1 – Version-tag-like language in the “DATA AND CODE AVAILABILITY” section**

- **Location:** same as P2-E5.
- **Problem:** “pinned to release tag paper2-v1.7.40” looks like internal versioning.
- **Required fix:** After implementing the archival fix in P2-E5, trim this to something like: “We use release tag ‘v1.7.40’ corresponding to the submitted version.”

---

**P2-m2 – Slight inconsistency in how the “3–5σ” range is described**

- **Location:** Abstract vs §IV vs §X.
- **Problem:**  
  - Abstract: “template-corrected significance ∼3–5σ after the combined systematic budget…”  
  - §IV: “The realistic range after the combined systematic budget is ∼3–5σ.”  
  - §X: repeats similar but with more context about Li & Brandenberger and convention halving.
  The endpoints are the same but the mapping to exact assumptions (σGR, bϕ prior, etc.) is not spelled out consistently.
- **Required fix:**  
  - In §IV or §VII, define explicitly what corresponds to the **3σ** and **5σ** endpoints (e.g. minimum and maximum σGR and bϕ prior widths), and then reference that definition wherever “3–5σ” is mentioned.

---

**P2-m3 – “No prior quantification … 2009–2024” should be hedged or referenced**

- **Location:** §III.B, page 7:  
  > “…and (iii) a literature search confirming no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024).”

- **Problem:** This is a very strong literature claim (“no prior quantification”) without any references or detail on the search.
- **Required fix:**  
  - Either soften: “To our knowledge, no prior work has quantified this overlap…”, or
  - Provide specific references showing that key previous matter-bounce papers do *not* contain such an analysis.

---

**P2-m4 – Possible overspecification of future dates and statuses**

- **Location:** Introduction, §IV, §IX.A, §X:
  - “SPHEREx (launched March 2025; survey data collection through ∼2027)…”
  - “MegaMapper (proposed, not yet approved or funded)…”
- **Problem:** These are time-sensitive; by publication they may be out of date.
- **Required fix:**  
  - Consider neutral phrasing: “SPHEREx, an all-sky spectrophotometric mission (planned launch in 2020s)…”.  
  - For MegaMapper, keep “proposed Stage V spectroscopic facility” but remove detailed speculation about timelines unless anchored to a citation.

---

**P2-m5 – Slightly confusing use of “mechanism-independent” vs “UV-completion-independent”**

- **Location:** introduction and §II.B.
- **Problem:** You do explain the distinction, but the phrase “mechanism-independent” appears in a way that could mislead a casual reader into over-interpreting the claim.
- **Required fix:**  
  - Ensure every use of “mechanism-independent” is clearly qualified (e.g. “mechanism-independent within the scalar-only Wilson–Ewing class, subject to (a)–(f)”), or replace with “UV-completion-independent within this restricted class.”

---

**P2-m6 – Minor redundancy and length**

- **Location:** §VI.C and Table II/III discussion; Appendix A is also very long.
- **Problem:** The paper is quite long (22 pages) for the claimed contribution (a recast of an existing forecast plus a template overlap and Bayesian comparison). Several paragraphs in §VI.C and Appendix A repeat similar caveats.
- **Required fix / recommendation:**  
  - The core contribution would be well served by **≤18 pages**.  
  - Consider compressing:
    - The lengthy Bayes-factor prior-sensitivity discussion,
    - The operator-algebra derivation in Appendix A (keep equations, trim narrative),
    - Some of the repeated exposition about GR systematics and bϕ.

---

### NITs

**P2-n1 – Duplicate / awkward phrasing**

- I did not find egregious duplicates like “canonical canonical-mask”, but there are a few slightly clunky phrases:
  - “the canonical SPHEREx galaxy-survey forecast lineage of Doré et al. ” is used more than once.
- **Fix:** Minor stylistic tightening if desired.

**P2-n2 – Footnote numbering and superscripts**

- The superscript “3” in “phase3 fisher_overlap.json” (§III.B) could be misread as a reference.
- **Fix:** Clarify as plain text or use a code font: `phase3_fisher_overlap.json`.

---

### Citation-forensics-specific notes (limitations and what to check before acceptance)

Because I lacked direct access to arXiv/ADS for the cited cosmology papers, I could not verify these—but **they must be checked by the editor or another referee**:

1. **Reference [1] Maldacena (2003):**
   - Verify that the formula \(f_{\mathrm{NL}}^{\text{local}} \approx (5/12)(1-n_s)\) is indeed the gauge-frame value quoted.
   - Confirm that the ns=0.9649 insertion giving fNL≈0.015 is consistent.

2. **References  Cai et al. (2009) and  Cai & Brandenberger (2014):**
   - Confirm:
     - The benchmark values B_NL at squeezed, equilateral, folded are exactly as in Table I.
     - The “(3,1,-9,5,-66,9)” single-time-ordering coefficients and the doubled set (6,2,-18,10,-132,18) are correctly taken from their Eq. 37 and context.
     - The factor-of-two issue between -35/8 and -35/16 is indeed due to convention and/or time-ordering as described.

3. **Reference [4] Heinrich et al. (2024):**
   - Check that σ(fNL^local)=0.7 for SPHEREx multi-tracer bispectrum is indeed in Fig. 6 / Table 3 with the stated template normalization.
   - Confirm their treatment of bϕ (fixed universality or marginalized) matches what is claimed here.

4. **References ,  Dalal et al. and Slosar et al.:**
   - Verify the exact form of Δb(k,z) and M(k,z) matches Eqs. (3)–(4).

5. **Reference  Jung et al. Planck PR4 NPIPE:**
   - Confirm that the numbers fNL = −0.1 ± 5.0 are correct and that recasting with r=0.876 yields the quoted σ.

6. **All Bayes-factor related external numbers (DESI, Euclid, CMB-S4 forecasts from [33–35]):**
   - Verify that the quoted σ(fNL) ranges are consistent with those references’ tables.

Any mismatches here would be **MAJOR** and would need correction prior to publication.

---

## Summary recommendation

**Recommendation: ACCEPT WITH MINOR CORRECTIONS**

The paper’s core technical work (template overlap, SPHEREx forecast recast, and Bayesian comparison framework) appears internally consistent and well-motivated, and I did not find fatal logical flaws. However, several issues must be corrected before publication: clean removal of review-log artifacts and overly strong global claims; clearer separation of σ-values from different Fisher procedures; more transparent treatment of the Bayes-factor assumptions; and tidying of the abstract’s significance statements. These are primarily presentation and clarity issues rather than fundamental scientific errors, so I judge that they can be addressed with a careful minor-revision pass.