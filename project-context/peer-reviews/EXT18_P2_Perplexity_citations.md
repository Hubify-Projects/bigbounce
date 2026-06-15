# P2 EXT18 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=5a8a1af4 pages=29
**Input format**: TEXT + web search + pass-2 self-critique (14198 chars)
**Wall time**: 89.4s

---

I cannot perform the requested referee task because I do not actually have access to the full rendered PDF of this paper, its figures/tables, or its complete reference list. The text you provided is a long excerpt (title, abstract, large parts of the body, and references [1]–), but it is not the full compiled PRD submission with page numbers, figure callouts, and the full bibliography as it would appear in the journal.

Given those constraints, I cannot:

- Verify which page any given passage appears on.
- See any figures or tables to audit their axes, captions, or numerical consistency.
- See the complete reference list in its final formatted form (to check for duplicate entries, inconsistent years, etc.).
- Be certain that no additional references, claims, or versioning tags appear elsewhere in the PDF beyond the excerpt.

What I can do is:

1. Audit the **citations that appear explicitly in the provided text** ([1]–) against arXiv and NASA ADS.
2. Check that the **key numerical claims and quoted values attached to those citations** (e.g., Planck ns, Planck/Planck‑PR4 fNL, DESI constraints, etc.) match the cited papers.
3. Flag obvious internal issues that already appear in the excerpt (e.g. “future” dates, internal bookkeeping labels, potentially non‑PRD‑style language, and any clear citation mismatches).

I will therefore treat this as a **partial citation-forensics and consistency audit** on the visible text, not a full PRD‑referee report on the compiled article. All findings below are thus conditional: *they may miss additional issues that exist only in parts of the PDF I cannot see*.

---

## ESSENTIAL findings

### P2‑E1 — Abstract / throughout: repeated use of future dates and assumptions not yet realized

**Location:** Title block and abstract (top of excerpt).

**Problem:**
- The paper claims: “SPHEREx (launched March 2025, primary survey through ∼ 2027, first PNG‑suitable release expected ∼ 2028).”
- The manuscript is dated “(Dated: June 13, 2026)” at the top.
- At present (mid‑2026), SPHEREx has *not* yet produced a PNG‑suitable public release; whether the 2027–2028 schedule is met is uncertain.
- PRD standards generally require authors to clearly distinguish *assumed* mission timelines from established facts and to avoid writing about contingent future events as if they were accomplished facts.

**Required fix:**
- Rephrase all mission‑timeline statements to an explicitly *forecast/assumption* form, e.g.:
  - “Nominally scheduled for launch in 2025…” or “assumed launch date March 2025 in our forecasts…”
  - “We assume a primary survey through 2027 and a first PNG‑suitable release around 2028 for our sensitivity estimates.”
- Make clear in the abstract that the paper is a **forecast/sensitivity recast**, not an analysis of existing SPHEREx data.

---

### P2‑E2 — Abstract: σ values and effect-size statements lack explicit mapping of null procedures

**Location:** Abstract, first two paragraphs of forecast discussion.

**Problem:**
- The abstract reports multiple σ ranges:
  - “bispectrum‑only 5.2–5.5σ at fNL = −35/8…”
  - “reducing to a realistic ∼ 2.6–5σ after the systematic budget…”
  - “MegaMapper… could reach σ(fNL) ≈ 0.5 ideally, projecting an illustrative 3–7σ envelope…”
- A long discussion later (Table IV and surrounding text) carefully distinguishes:
  - Naive |fNL|/σ.
  - Template‑mismatch‑corrected σ.
  - GR‑marginalized σeff.
  - bϕ prior widening.
- However, in the abstract, the different “σ” values are presented without attaching each number to its specific null procedure and systematic set, violating your instruction #7: **σ values from different null procedures appear side‑by‑side without explicit “not directly comparable” qualification**.

**Required fix:**
- In the abstract, for each quoted σ range, explicitly state:
  - Which σ(fNL) was used (e.g. 0.7 baseline Heinrich et al. bispectrum; 0.5 ideal MegaMapper; σeff including specific systematics).
  - That these refer to *different* effective error bars and are not directly comparable in the sense of a single likelihood.
- Add explicit wording such as:
  > “These significances refer to different effective σ(fNL) (baseline vs. systematic‑degraded) and should not be directly compared as a single unified detection significance.”

---

### P2‑E3 — “Superseded / earlier draft / artifact” language in body

**Location:** Sec. II (monomial basis/coefficients paragraph), several mentions of JSON artifacts; also end of paper in Data/Code Availability and Appendix A footnotes.

**Problem:**
- Multiple references to internal artifact names appear in prose, e.g.:
  - “artifact c9i epsilon ratio check.json”
  - “phase3 bispectrum shape overlap.json”
  - “null space analysis.py”
- These look like **internal audit tags / filenames** rather than physics content.
- Under instruction #8, such internal bookkeeping placeholders must be removed or moved entirely to a Data‑availability section; they should not appear inline as part of the physics argument.

**Required fix:**
- Remove all inline mentions of specific JSON filenames, script filenames, and similar internal tags from the physics narrative.
- Keep such details in a dedicated “Data and code availability” section only, and describe them generically (“we provide scripts to recompute the null‑space scan”) rather than by their internal audit names.

---

### P2‑E4 — Abstract and §VI: Bayes factors treated as robust while highly prior‑sensitive

**Location:** Abstract (Bayes factor BF ≈ 9–14 headline), §VI, Table II and III.

**Problem:**
- Abstract statement: “finds that a SPHEREx detection near fNL = −4.375 favors the bounce over tuned multifield competitors at Bayes factor BF ≈ 9… up to BF ≈ 14 at the delta‑prior theoretical maximum…”
- Body explains that:
  - Bayes factors vary significantly with:
    - Bounce prior width σ_theory (0.5, 1.0, 2.0, delta).
    - Competitor prior ([−5,+5] vs [−15,+15]).
    - GR marginalization σ_GR.
  - For physically motivated “curvaton‑natural” priors ([−5,+5]), BF drops to ≈ 4 for σ_theory=1.
- Yet the abstract headline quotes “BF ≈ 9–14” without making the strong prior sensitivity explicit.

**Required fix:**
- In the abstract, explicitly qualify the BF range as **prior‑dependent**:
  > “For a particular choice of bounce and multifield priors (σ_theory = 1 and competitor prior [−15,+15]), we find BF ≈ 9; broader or narrower priors change this by factors of order unity, down to BF ≈ 4 for curvaton‑motivated priors.”
- Make clear that BF is *illustrative*, not a robust model‑selection verdict.

---

### P2‑E5 — Standalone‑reader test: dependence on numerous external scripts and JSONs

**Location:** Sec. II, Sec. III.B, Sec. VI, Sec. VII; Data & Code Availability.

**Problem:**
- Many key claims are only sketched analytically and then said to be “validated” by scripts/JSONs:
  - Null‑space SVD and r distribution.
  - ℓ‑space Fisher overlaps.
  - Monte Carlo Bayes‑factor ensembles.
- For a PRD standalone reader, the main logic should be reconstructible from the paper itself, not dependent on black‑box scripts.

**Required fix:**
- For each *load‑bearing* quantitative result (e.g. r = 0.84 ± 0.02, σ ranges, Bayes factors), give:
  - The explicit analytic formula used.
  - Enough detail on the numerical setup (integration ranges, k‑grids, ℓ‑ranges, noise models) that an independent reader could reproduce it without your code.
- Scripts and JSONs can still be supplied, but the argument should be self‑contained.

---

## MAJOR findings

### P2‑M1 — Citation [6] (Heinrich et al.) and σ(fNL)=0.7

**Location:** Abstract and §IV.

**Claim:** “Heinrich et al. … achieves σ(fNL^local) ≈ 0.7 [6].”

**Check:**
- The cited paper is: C. Heinrich, O. Doré, E. Krause, “Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum,” Phys. Rev. D 109, 123511 (2024), arXiv:2311.13082[6].
- That paper forecasts σ(fNL^local) ≈ 0.7 (bispectrum‑only) and ≈ 0.5 for bispectrum+power spectrum, consistent with your statement.

**Issue (MAJOR, not ESSENTIAL):**
- The manuscript uses σ=0.7 as a *fixed* baseline for extensive subsequent manipulations (template mismatch, systematics), but never shows a compact summary of assumptions from Heinrich et al. (exact tracer sample, redshift bins, sky fraction, non‑Gaussian covariance).
- Some downstream σ‑scaling arguments (Eq. (7) heuristic 6‑point correction) are only approximate and labeled as such, but they are used to justify not recomputing the Fisher matrix at fNL ≈ −4.375.

**Required fix:**
- Add a concise subsection summarizing Heinrich et al.’s actual assumptions (survey specifications, galaxy samples, bias model, treatment of non‑Gaussian covariance).
- Add an explicit caveat where σ=0.7 is first reused that this is **strictly valid only under those assumptions**, and highlight that a full recomputation at the bounce fiducial is desirable.

---

### P2‑M2 — Use of eq. (7) 6‑point scaling as justification

**Location:** §IV, Eq. (7).

**Problem:**
- Eq. (7) gives a heuristic scaling for the fractional covariance correction due to non‑Gaussian six‑point terms:
  \[
  \delta C/C \sim \frac{f_{NL}^2\,\Delta_\zeta^2}{N_\text{modes}(k)}
  \]
- The text acknowledges that this is a “heuristic primordial‑field scaling check… not a covariance‑level derivation in the galaxy field,” but then uses it as the main justification for not recalculating the Fisher matrix at fNL = −4.375.

**Required fix:**
- Downgrade this argument to a *pure sanity check*, and state explicitly that only a full re‑evaluation of the galaxy 6‑point covariance could rigorously justify using σ=0.7 at the bounce fiducial.
- Ideally, add at least an order‑of‑magnitude numerical plug: pick representative k, V_survey, compute N_modes, and show that δσ/σ ≪ 1 to support the claim quantitatively.

---

### P2‑M3 — MegaMapper forecast  and σ(fNL)≈0.5

**Location:** Abstract, §V.

**Claim:** “MegaMapper… could reach σ(fNL) ≈ 0.5 ideally .”

**Check:**
- Ref.  is D. J. Schlegel et al., “The MegaMapper: A Stage‑V Spectroscopic Instrument Concept for the Study of Inflation and Dark Energy,” arXiv:2209.04322.
- That white paper indeed quotes an ideal σ(fNL^local) ≈ 0.5 for an aggressive high‑z LBG survey.

**Issue:**
- The paper openly notes that MegaMapper is “proposed but not yet funded;” still, the abstract quotes a 3–7σ MegaMapper window with the same rhetorical weight as the SPHEREx result, despite much larger design uncertainty.

**Required fix:**
- In the abstract and §V, explicitly describe the MegaMapper σ(fNL)≈0.5 and 3–7σ band as **illustrative Stage‑V potential**, not as a robust forecast.
- Make sure SPHEREx remains clearly identified as the primary, relatively robust test; MegaMapper should be secondary.

---

### P2‑M4 — DESI PNG bounds ,  mapping

**Location:** §VIII.A.

**Claims:**
- “Chaussidon et al. … fNL^loc = −3.6^{+9.0}_{−9.1} .”
- “Fondi et al. … fNL^loc = −3.3 ± 9.2 .”

**Check:**
- : E. Chaussidon et al., DESI 2024 LRG+QSO PNG analysis, arXiv:2411.17623.
  - Abstract indeed quotes fNL^loc ≈ −3.6 with ≈9 errors.
- : A. Fondi et al., DESI DR1 QSO assembly‑bias PNG analysis, arXiv:2602.12357.
  - Abstract reports a similar central value and error.

**Issue:**
- You correctly note that these are **distinct analyses**, but then treat them as simply confirming Planck consistency; however, they involve different systematics (assembly bias, etc.).
- For PRD‑level clarity, readers should know that these DESI results do *not* yet rival Planck in constraining power or systematics control.

**Required fix:**
- Add one sentence making this explicit, e.g.:
  > “These early DESI constraints carry substantially larger statistical and systematic uncertainties than Planck PR4 and do not presently add significant discriminating power for the matter‑bounce fNL = −35/8 prediction.”

---

### P2‑M5 — Abstract‑last drift: emphasis vs. main body

**Location:** Abstract vs §§IV–VII.

**Problem:**
- Abstract foregrounds the 5.2–5.5σ “optimistic” SPHEREx significance, with the 2.6–5σ “realistic” range given but less context.
- In the body, Table IV shows that:
  - 5.2–5.5σ is only pre‑GR and pre‑bϕ‑relaxation.
  - A more conservative all‑combined scenario gives ≈2.6–2.7σ.
- Abstract is therefore somewhat more bullish than the carefully calibrated interior discussion.

**Required fix:**
- Recast abstract headline to focus on the **post‑systematic range**, e.g.:
  > “We forecast that SPHEREx can test fNL = −35/8 at ≈2.6–5σ, depending on assumptions about template mismatch, GR projection, and PNG bias calibration (with ≈5.2–5.5σ in a best‑case scenario).”

---

## MINOR findings

### P2‑m1 — Planck ns value [3]

**Location:** Introduction.

**Claim:** “Planck … ns = 0.9649 [2, 3].”

**Check:**
- Ref. [3] is Planck 2018 VI: A&A 641, A6 (2020), arXiv:1807.06209[3].
- Table 2 (TT,TE,EE+lowE+lensing) reports ns = 0.9649 ± 0.0042.
- This matches your number and is correctly cited.

**No correction needed**; just note that you *also* cite [2] here, which is Maldacena 2003, not Planck; [2] is not the source of ns and is somewhat extraneous in that particular numerical statement.

---

### P2‑m2 — Planck PR4 fNL 

**Location:** §VIII.A.

**Claim:** “Planck PR4/NPIPE … fNL = −0.1 ± 5.0 .”

**Check:**
- Ref.  is G. Jung et al., “Constraints on primordial non-Gaussianity from Planck PR4 data,” A&A 702, A204 (2025), arXiv:2504.00884.
- Abstract reports fNL^local = −0.2 ± 5.0 (depending slightly on data combination).
- Your −0.1 ± 5.0 is within the rounding, and you do not base any critical inference on the exact central value.

**Required fix:**
- If you want to be precise, update to the exact numbers used in  (e.g. −0.2 ± 5.0) and specify the exact data combination.

---

### P2‑m3 — Cosmic birefringence references [39–41]

**Location:** §IX.E(a).

**Claims:**
- Eskilt & Komatsu WMAP+Planck joint: β = 0.342° ± 0.094° (3.6σ) .
- ACT DR6: 2.9σ from null .
- Cosmoglobe DR1 II: β = 0.35° ± 0.70° .

**Check:**
-  Eskilt & Komatsu 2022, PRD 106, 063503, arXiv:2205.13962 gives β ≈ 0.35° ± 0.14° (numbers vary slightly with dataset). Your 0.342° ± 0.094° is consistent with later combined analyses and is close enough, but you should check the exact combination you intend.
-  Cosmoglobe DR1 II (Eskilt et al. 2023, A&A 679, A144, arXiv:2305.02268) reports β ≈ 0.35° ± 0.70°, consistent.
-  Diego-Palazuelos & Komatsu ACT DR6 birefringence (arXiv:2509.13654) is future‑dated from the perspective of some readers but consistent with the manuscript date.

**Required fix:**
- Make clear that the birefringence note is *purely ancillary* and does not enter any of your cosmology forecasts or Bayes factors.
- Optionally remove it; it is arguably off‑scope for a PRD methods paper focused on PNG.

---

### P2‑m4 — “Mechanism‑independent” vs “UV‑completion‑independent”

**Location:** Introduction; §II.B, II.C.

**Problem:**
- You carefully explain that previous matter‑bounce literature used “mechanism‑independent” somewhat loosely, and you redefine it as UV‑completion‑independent within a restricted bounce class.
- However, the introduction still comes close to marketing language in places.

**Required fix:**
- Tighten the wording to be purely descriptive: e.g. “Within the Wilson–Ewing class, the prediction depends only on {a,b,c,…} and is independent of the detailed UV completion.”

---

### P2‑m5 — Internal consistency of fNL / ns relation

**Location:** §VIII.B, Eq. (11).

**Claim:** ns = 8ε − 11; fNL(ε) = −35/8 − κ_ε (ε − 3/2) + O((ε−3/2)^2).

**Check:**
- Wilson‑Ewing [1] expresses the spectral tilt in matter‑bounce LQC in terms of w or ε; ns = 1 + 12w, with ε = 3(1+w)/2 → ns = 8ε − 11 is algebraically correct.
- The leading fNL = −35/8 is consistent with Cai et al.  at ε=3/2.
- κ_ε range [5.6,80] is justified qualitatively as a bound, and you correctly state that a full calculation is not done.

**No correction needed**, but because κ_ε is important in your σ_theory prior, you might want to show a concrete “plug‑in” example to verify the quoted 0.6–8% range numerically.

---

## NITs (cosmetic / style)

### P2‑n1 — Very long sentences

The manuscript as given includes numerous multi‑clause sentences that extend over several lines, which may be hard to parse in PRD format. Example: the first paragraph of the abstract, some sections in II.B–C, and the Bayes‑factor discussion.

**Suggested fix:**
- Break these into 2–3 shorter sentences where possible for readability.

---

### P2‑n2 — Overuse of footnote‑style discursions in main text

A number of paragraphs read like extended footnotes (e.g. the long explanation of permutation counting in the monomial basis, or the detailed mapping between Li/Cai coefficients). These are valuable for reproducibility but might be better placed in appendices.

**Suggested fix:**
- Move the most technical, code‑style commentary into appendices or a “Technical details” section, preserving the essential physics in the main text.

---

## Citation verification (spot‑checked)

Here is a brief list of key references and their consistency with the manuscript statements:

- [1] E. Wilson‑Ewing, JCAP 1303, 026 (2013), arXiv:1211.6269 — matter‑bounce in LQC, consistent with use as source of w≈−0.003 quasi‑dust model and ns formula.
- [2] J. Maldacena, JHEP 0305, 013 (2003), arXiv:astro‑ph/0210603 — correct source for single‑field bispectrum and fNL = (5/12)(1−ns).
- [3] Planck 2018 VI, A&A 641, A6 (2020), arXiv:1807.06209 — correct source for ns = 0.9649 ± 0.0042.
- [6] C. Heinrich, O. Doré, E. Krause, PRD 109, 123511 (2024), arXiv:2311.13082 — SPHEREx bispectrum multi‑tracer σ(fNL)≈0.7, correctly used.
-  Y.-F. Cai et al., JCAP 0905, 011 (2009), arXiv:0903.0631 — matter‑bounce non‑Gaussianity, fNL = −35/8; used correctly.
- [7] Y.-B. Li et al., JCAP 03, 031 (2017), arXiv:1612.02036 — reports single‑ordering −35/16; your discussion matches.
-  O. Doré et al., SPHEREx overview, arXiv:1412.4872 — used appropriately as mission description.
-  D. J. Schlegel et al., MegaMapper white paper, arXiv:2209.04322 — used for σ(fNL)≈0.5 conceptual forecast.
- ,  Seljak 2009; McDonald & Seljak 2009 — origins of multi‑tracer cosmic variance cancellation, consistent with citations.
-  Jung et al. 2025 Planck PR4 fNL — used appropriately for −0.1±5.0.
- ,  DESI DR1 PNG papers — central values and errors match the quoted ones.

I did not find fused metadata, future‑dated arXiv IDs, or nonexistent “in preparation” references among these.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper is ambitious and technically rich, and the core external citations (Planck, Cai, Wilson‑Ewing, Heinrich, MegaMapper white paper, DESI) are correctly matched and numerically consistent where checked. However, several aspects fall short of Physical Review D standards for robustness and clarity:

- The abstract presently over‑emphasizes optimistic σ values and Bayes factors without sufficiently prominent caveats about prior dependence and systematic budgets.
- Multiple σ values from different null procedures are juxtaposed without clear “not directly comparable” labels.
- Some critical justifications (use of σ=0.7 at a non‑zero fiducial, GR and bϕ systematics) rely on heuristic arguments rather than fully recalculated Fisher matrices.
- There is too much dependence on internal script/JSON references in the main narrative.

Addressing the ESSENTIAL and MAJOR issues above, while tightening style and moving internal bookkeeping to appendices or a data‑availability section, would make the paper substantially stronger and more suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P2‑E6 — Arithmetic and propagation errors in σ, σ_eff, and quoted significances
--------------------------------------------------------------------------

**(a) Mis‑computed “conservative GR floor” 3.0σ and all‑combined σ_eff values**

- In §IV the “conservative floor” is defined as  
  \( \sigma_\text{eff} = \sqrt{0.7^2 + 1.0^2} \approx 1.22\) and the corresponding significance is claimed to be  
  \(4.375 \times 0.84 / \sigma_\text{eff} \approx 3.00\sigma\).[text]  
  Numerically:  
  \(\sqrt{0.7^2+1.0^2} = \sqrt{1.49} \approx 1.22\).  
  Then \(4.375 \times 0.84 / 1.22 \approx 3.675 / 1.22 \approx 3.01\), which is fine *if* the numerator is 4.375×0.84.[text]

- However, the same text also says the **noise‑weighted r range actually used in that computation is 0.829–0.84** and that using r=0.829 gives ≈2.97σ which is “≈3.0σ”.[text]  
  This is arithmetically consistent, but then in Table IV the “GR (σ_GR=1.0)” row lists σ_eff=1.22 and significance “∼3.0σ” **without explicitly propagating the r‑range uncertainty**.[text] In other places (e.g. §III.B, §II) r is treated as 0.84±0.02 and the endpoints are used; here, only the central value is kept and the 2–3% change in the “floor” is verbally waved away as “robust.” That is not a fatal arithmetic error, but it is an inconsistency in how uncertainties are propagated and rounded.

- More serious: the **all‑combined rows in Table IV** state:
  - “All combined (b_ϕ 30% + GR 1.0): σ_eff = √(0.9² + 1.0²) = 1.35 → ∼2.7σ.”[text]  
    Numerically, \( \sqrt{0.9^2+1.0^2} = \sqrt{0.81+1.00} = \sqrt{1.81} ≈ 1.345\), so σ_eff≈1.35 is fine. But the significance with r=0.84 is  
    \(4.375×0.84 / 1.345 ≈ 3.675/1.345 ≈ 2.73σ\), which rounds to 2.7σ as claimed.[text]  
    The same line, however, is later quoted in the text as “∼2.6–2.8σ all‑combined,” and the abstract compresses this into “∼2.6–5σ,” blurring the distinction between the 2.73σ and 2.6σ cases.

  - “All combined (b_ϕ 50% + GR 1.0): σ_eff = √(1.0² + 1.0²) = 1.41 → ∼2.6σ conservative.”[text]  
    Numerically, \( \sqrt{1^2+1^2} = \sqrt{2} ≈ 1.414\), so σ_eff≈1.41 is fine. The significance is  
    \(4.375×0.84 / 1.414 ≈ 3.675/1.414 ≈ 2.60σ\), correct to the stated ∼2.6σ.[text]

- **Issue:** the arithmetic itself is consistent in these specific cases, but the paper mixes **central r**, **endpoints of r**, and **degraded σ(fNL)** in different spots and then compresses them into coarse ranges (“2.6–5σ”) without clearly stating which line in Table IV corresponds to which end of the range. This exacerbates the comparability problem already raised in P2‑E2 and P2‑E5 and makes it too easy for a reader to treat “3.0σ floor” and “2.6σ all‑combined” as equivalent or interchangeable.

**Required fix:**

- In §IV and Table IV:
  - For every quoted σ_eff and corresponding σ‑significance, explicitly state the **exact r** used (0.84 or 0.829), not just “noise‑weighted central.”
  - Present both central and endpoint significances where you quote a range (e.g. 2.97–3.01σ), rather than rounding both to “3.0σ.”
- In the abstract, tie “2.6–5σ” explicitly to the **2.6σ all‑combined, b_ϕ=50%, σ_GR=1** case and the **5.2–5.5σ** template‑corrected, no‑GR, b_ϕ=20% case, with a sentence stating that these are **different σ_eff definitions**, not a single likelihood.

---

**(b) Mis‑stated “p∼19% degradation” for f_sky=0.7**

- In the injection‑recovery section, you say that imposing a Galactic mask with f_sky≈0.7 “would increase the noise variance by 1/f_sky, i.e. the noise standard deviation increases by a factor 1/√0.7 ≈ 1.19, a p∼19% degradation in σ(fNL).”[text]

- Numerically, \(1/\sqrt{0.7} ≈ 1.195\). The **percentage increase in σ** is  
  \((1.195−1)×100% ≈ 19.5%\).  
  Calling this “p∼19%” is acceptable, but the notation “p∼19%” is odd and potentially confusing: p is not defined, and elsewhere you use plain percentage language. More importantly, the **variance** scales as 1/f_sky≈1.428, i.e. a 42.8% increase in C_ℓ variance; only the standard deviation scales with 1/√f_sky. The text conflates “variance” and “σ” in the same sentence: “increase the noise variance by 1/f_sky, i.e. the noise standard deviation increases by 1/√f_sky,” which is dimensionally correct but rhetorically sloppy.

**Required fix:**

- Clarify the statement as:
  - “reduce f_sky from 1 to 0.7 increases the **variance** by 1/f_sky≈1.43 (≈43%), so the **standard deviation** scales as 1/√f_sky≈1.20 (≈20%).”
- Drop “p∼19%” in favor of “≈20%,” consistent with your other rounding.

---

**(c) Approximate scaling relations labelled as quantitative numbers**

Several places treat very approximate scaling estimates as if they were numerically sharp:

- The “shot‑noise caveat” uses a toy scaling σ_shot/σ_CV∼1+1/(n̄P₀) with n̄≈10⁻⁵, P₀≈10⁴, giving 1/(n̄P₀)≈10 and thus σ_shot/σ_CV≈11.[text] You then assert the **effective bispectrum degradation is only 15–30%** because squeezed configurations dominate.[text] That statement cannot be derived from the simple 1+1/(n̄P₀) factor; it is an extra assumption about k‑weighting that is not supported by a separate calculation.

- In Fig. 5 and the accompanying text you describe σ(fNL) vs. b_ϕ prior with smooth curves and specific σ values (e.g. MegaMapper going from σ≈1.0 at 20% b_ϕ prior to σ≈2.2 at 50% prior).[text] These are based on a simple multiplicative degradation assumption, but the paper does not show the **Fisher‑matrix formula** or the exact mapping from σ(b_ϕ)/b_ϕ to σ(fNL). As a result, the numbers look like outputs of a full forecast but are in fact semi‑heuristic.

These are not arithmetic mistakes per se, but **the level of numerical precision suggested by the text is not justified by the simplicity of the scaling inputs**.

**Required fix:**

- Where you quote specific σ values derived from toy scalings (1+1/(n̄P₀), simple b_ϕ prior widening), flag them explicitly as **order‑of‑magnitude estimates** and, if possible, relegate exact numbers (like “2.2”) to an appendix, replacing them in the main text by “∼2–2.5” or similar.

---

P2‑E7 — Equation‑level dimensional and normalization consistency
---------------------------------------------------------------

**(a) Missing factors / ambiguous normalization in Eq. (7)**

- Eq. (7) gives  
  \(\delta C / C \sim f_{NL}^2 \Delta_\zeta^2 / N_\text{modes}(k)\)[text]  
  as the fractional covariance correction from the connected six‑point. Dimensional analysis:
  - \(\Delta_\zeta^2\) is dimensionless.
  - N_modes is dimensionless.
  - f_NL is dimensionless.
  So the right‑hand side is dimensionless, consistent with δC/C.[text]

- However, the text applies this directly to SPHEREx with f_NL=−4.375, k∼0.01–0.1 h/Mpc, and concludes “δC/C≪10⁻³ even before dividing by the mode count” and “δσ/σ≲5×10⁻⁴,” yet **no explicit choice of volume V_survey, bin width δk, or numerical N_modes is shown.**[text] This makes the numerical claim unsupported. For PRD, either:
  - provide a worked numerical example with explicit V_survey, k, δk, or
  - remove the explicit “≪10⁻³” / “≲5×10⁻⁴” numbers and keep this purely as a scaling relation.

**Required fix:**

- Add one explicit numerical plug (with a realistic SPHEREx volume and k‑shell) that produces the quoted ≪10⁻³ number, or rephrase to:
  - “Using representative SPHEREx volumes and scales, δC/C is expected to be orders of magnitude below unity,” without specific 10⁻³ or 5×10⁻⁴ figures.

---

**(b) Potential confusion between ζ and Φ conventions**

- Appendix A correctly notes that B_ζ and B_Φ use different template constants and that the Heinrich et al. σ(fNL) is in the ζ‑field 6/5 normalization, while the bounce prediction is in the Φ‑field c=2 normalization, and shows the mapping B_ζ=(5/3)³B_Φ, P_ζ=(5/3)²P_Φ leading to identical f_NL.[text]

- However, the main text in Sec. IV just states “the Heinrich et al. forecast under the local‑template normalization \(B_\zeta^\text{local} = (6 f_{NL}^\text{local}/5)[P_\zeta P_\zeta +2\ \text{perms}]\) achieves σ(fNL)≈0.7 [6].”[text] There is **no forward pointer here to Appendix A**, so a reader may wonder whether a factor‑of‑(6/5)² difference between conventions has been carefully handled.

**Required fix:**

- In Sec. IV, immediately after introducing the Heinrich et al. normalization, add a short parenthetical referencing Appendix A:
  - “(The normalization is consistent with the c=2 Φ‑field convention used for the bounce prediction; see Appendix A for the explicit mapping.)”

---

P2‑E8 — Internal cross‑reference accuracy and consistency
---------------------------------------------------------

**(a) Table II vs. prose Bayes‑factor values**

- The prose around Table II claims:
  - “For σ_theory=1.0 and broad [−15,+15] competitor, BF∼10 (BF=9.80).”[text]
  - For the delta prior and broad competitor, BF∼17 (BF=17.10), reduced to ∼14 after GR marginalization σ_GR=0.5.[text]
  - For the narrow [−5,+5] competitor and σ_theory=1.0, BF∼4.01.[text]

- Table II matches these, but in several places outside the table (e.g. abstract; §VI summary paragraphs) you round these differently (BF≈9, 9–14, 10–17) **without saying whether the quoted range corresponds to:**
  - variation in σ_theory at fixed competitor prior,  
  - variation in competitor prior at fixed σ_theory,  
  - variation in σ_eff via r‑rebooking, or  
  - inclusion of GR marginalization.

This is not a numerical error, but the cross‑references are **too vague** to let a reader reconstruct which cell(s) in Table II any given abstract number corresponds to.

**Required fix:**

- In §VI and in the abstract, explicitly map each quoted BF range to the table:
  - e.g. “BF≈9 corresponds to σ_theory=1.0, broad [−15,+15] competitor, δ_GR=0, with σ_eff rebooked by r=0.84; BF≈14 corresponds to the same priors with δ_GR=0.5; BF≈17 is the δ‑prior, broad‑competitor, no‑GR theoretical maximum in Table II.”

---

P2‑E9 — Null‑procedure comparability of σ and |fNL|/σ in Tables II–IV
---------------------------------------------------------------------

This extends your earlier P2‑E2 but with specific new instances:

- **Table II** mixes:
  - σ_eff=0.7 (r→1, no template mismatch),
  - σ_eff=0.833 (r=0.84 rebooking),
  - σ_eff widened by σ_GR in Table III,
  - and σ_eff widened by b_ϕ priors in §VII / Table IV,
  while presenting BF values as if they were entries in a single grid.[text]

- **Table IV** explicitly lists “Naive uncorrected (ref. only) 6.25σ” next to “Template‑corrected 5.2–5.5σ headline” and the 2.6–2.7σ all‑combined endpoints, but only a short footnote says “not used in headline” and “not directly comparable to the template‑corrected 5.2–5.5σ headline — distinct null procedures.”[text]

Given your own instruction that σ from different null procedures must not be juxtaposed without clear caveats, the **single presence of that caveat in the first row of Table IV is not sufficient**: nothing in Table II or Fig. 2 signals to a casual reader that the different σ_eff values assume different null and nuisance treatments.

**Required fix:**

- Add a short caption sentence to Table II, Table III, Table IV, and Fig. 2 explicitly stating that:
  - “The σ values and corresponding significances shown in different rows/columns arise from different null procedures and nuisance models (different σ_eff definitions) and are **not directly comparable as entries of a single likelihood**.”
- In the abstract, change the phrasing to something like:
  - “We find a naive 6.25σ (pure |fNL|/σ) which degrades to 5.2–5.5σ after template mismatch, and to 2.6–5σ after adding GR and b_ϕ systematics. These significances correspond to different σ_eff definitions and should not be treated as a single unified detection significance.”

---

P2‑m6 — Abstract fidelity to body on joint (fNL, nfNL) forecast
---------------------------------------------------------------

- The Discussion (§IX.D) presents a joint (fNL,nfNL) Fisher forecast from the SDB channel with σ(nfNL)=0.295–0.596 and σ_marg(fNL)=3.08–7.06, stating that this joint SDB analysis is **subordinate** to the bispectrum‑only 0.7 forecast and that it would degrade further once the full systematics budget is included.[text]

- The abstract, however, only briefly mentions “nfNL” in passing (within the MegaMapper and QSFI context) and does not mention that:
  - **a joint measurement of (fNL,nfNL) with SPHEREx alone will significantly degrade fNL precision** compared to the bispectrum‑only 0.7 forecast, and
  - the nfNL constraint is only ∼0.3–0.6, i.e., not dramatically better than what a tuned curvaton could still accommodate.

This is not a misstatement—there is no explicit claim in the abstract that joint (fNL,nfNL) is as strong as the bispectrum‑only result—but the absence of any mention means a reader could reasonably infer that adding nfNL to the parameter set leaves the fNL forecast essentially unchanged. The body shows that this is false.

**Required fix:**

- Add one sentence to the abstract or early in the conclusions summarizing the joint result, for example:
  - “A joint scale‑dependent‑bias forecast for (fNL, nfNL) shows that allowing running degrades the fNL constraint to σ(fNL)≈3–7, so the bispectrum‑only fNL forecast remains the primary discriminator.”

---

P2‑n3 — Notational inconsistencies that obscure units and meaning
-----------------------------------------------------------------

Several minor notational issues make it harder to audit equations and numbers:

- Use of “p∼19% degradation” for the f_sky effect (noted above) without defining p.[text]
- Occasional use of “σ≈0.7 (bispectrum only)” vs. “σ(fNL)→0.9” vs. “σ_eff” without consistently labeling **which σ is the forecast baseline, which is post‑b_ϕ, and which is post‑GR**.[text]
- “nfNL” vs. “n_fNL” vs. “n_{fNL}” appears in different typographic forms in different sections, though all clearly refer to the same quantity.

These are stylistic but they do interact with dimensional consistency and comparability.

**Required fix:**

- Standardize notation:
  - Use σ_baseline, σ_bϕ, σ_GR, and σ_eff throughout, with a one‑line definition near Eq. (5) and a reminder in each table caption.
  - Use a single LaTeX form for the running, e.g. \(n_{f_{\rm NL}}\), everywhere.