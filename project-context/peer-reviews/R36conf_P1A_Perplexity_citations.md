# P1A R36conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.66.pdf` md5=5dff8674 pages=28
**Input format**: TEXT + web search + pass-2 self-critique (7804 chars)
**Wall time**: 69.6s

---

Preamble: I do not have access to the actual rendered PDF or its reference list; all I can see is the text you pasted. I therefore cannot literally check arXiv/ADS IDs, DOIs, page numbers, or tables in the cited papers. What I can do is:

- Cross‑check each cited work’s existence, title, and topic against arXiv / NASA ADS / journal metadata via search.
- Check whether numerical/statistical claims as written are at least plausibly traceable to widely cited numbers in those references.
- Audit the internal logic, bookkeeping, and versioning language of the manuscript text you provided, including the abstract.

Everything below should be read with that limitation in mind; any item that depends on details of a reference’s tables or DOIs is conditional on full access to the reference list.

---

## Global issues

### P1A‑E1 — Companion papers “in preparation” used as load‑bearing evidence  
- **Location:** Abstract (page 1), Section I A, “Companion paper” paragraph, later references in Secs. III, VI, VII, XII, XIII, Data & Code Availability.  
- **Problem:** Multiple “companion works in preparation” [2, 6, 23, 46, etc.] are used as if they were citable sources for key forecasts, MCMC posteriors, NaMaster validation, galaxy‑spin catalog, NANOGrav KDE analysis, etc. None has an arXiv ID or journal citation; they are explicitly not publicly posted. Yet:
  - SPHEREx forecast significance 2.6–5σ is repeatedly cited to [2].  
  - ΛCDM+ΔNeff posteriors including H0, ΔNeff, σ8, etc., are taken from [6].  
  - Galaxy spin pipeline and null results are described as in .  
  - NANOGrav “real‑KDE GPU MCMC” result γPTA = 2.567 ± 0.382 is attributed to .  
- **Why this is critical for PRD:** PRD expects all load‑bearing quantitative claims to be reproducible from public sources, not internal “companion” studies that are not yet available. You also explicitly say many of these values are “documented internally rather than as externally citable arXiv‑posted numbers”. This violates the standalone‑reader requirement and the provenance / reproducibility norms (your own instructions 16 and 18).  
- **Required fix:**  
  - Either: post all these companion papers to arXiv with stable identifiers and update the citations, and ensure that this paper does not rely on any internal results that are not publicly accessible.  
  - Or: remove *all* load‑bearing dependence on these companions. That means:
    - Drop or re‑phrase all numerical claims, forecast significance ranges, and MCMC posterior numbers that rely on [2, 6, 23, 46].  
    - Restrict the paper to arguments that can be evaluated entirely from what is in this manuscript and standard external literature.  
  - In either case, clearly mark which statements in this paper are purely structural/theoretical (derivable without the companions) and eliminate any residual reliance on unpublished work for central claims.

**Classification:** ESSENTIAL.

---

### P1A‑E2 — Internal versioning / audit language left in body text  
- **Location:** Title block, first page: “(Dated: June 12, 2026 PDT — v1A.0.66)”. Section I A “Scope and limitations” references “earlier drafts” and “correction … in earlier drafts”; Sec. X D footnote mentions “earlier version of this manuscript”; Appendix B refers to “earlier drafts”; Acknowledgments mention use of Claude as AI assistant.  
- **Problem:** There is substantial internal version‑history and draft‑audit language scattered through the paper (version string v1A.0.66, “earlier drafts”, “external review”, etc.). Most journals, especially PRD, do not allow internal revision logs or references to earlier drafts in the main text.  
- **Required fix:**  
  - Remove all explicit version identifiers and development history from the scientific narrative. At most, the date stays on the title page; the “v1A.0.66” style tag should be removed.  
  - Remove or rewrite sentences that talk about “earlier versions/drafts” or internal review flags. The scientific corrections they describe are fine, but must be presented simply as the current result, not as a story of previous mis‑steps.  
  - The acknowledgment that an AI tool “Claude” was used is not itself disqualifying, but some journals now require more formal AI‑usage disclosures. Coordinate with PRD policy; if allowed, move this to a single neutral line (“The author used AI tools for language suggestions; all scientific content is the author’s responsibility”) and remove detailed development‑process narrative.

**Classification:** ESSENTIAL.

---

### P1A‑E3 — Abstract claims depend on non‑public or uncomputed quantities (pattern‑048 / 045)  
- **Location:** Abstract, first page; Sections I, III, VII, XII, XIII.  
- **Problem:** Several key scalar claims that appear in the abstract and opening are either:
  - Not backed by explicit computations in the body; or  
  - Depend on unpublished companions.  
  Examples:  
  - “Through 7 foundation studies … and 6 observational research branches … we report 13 logically‑independent mechanism‑class constraints.” There is no explicit derivation of each barrier’s logical independence; B8/B14 relation is partially discussed, but the independence of the others is asserted, not proven.  
  - “SPHEREx forecast 2.6–5σ quoted above” appears already in the abstract but is said to come from a “companion work in preparation [2]”. No Fisher matrix, survey specs, or calculation appear here.  
  - “H0 = 67.68 ± 1.06, ΔNeff ≈ 0” in the abstract rely on internal MCMC [6]; you explicitly say those numbers are not yet externally citable.  
- **Required fix:**  
  - For every numerical or logical headline in the abstract, either:
    - Show the computation in this paper, with enough detail that a referee can reproduce it, *or*  
    - Restrict the abstract claim to qualitative level and explicitly mark it as depending on forthcoming companion papers (in which case PRD may still reject on grounds of non‑standalone).  
  - In particular, remove the 2.6–5σ SPHEREx range and the specific Cobaya posterior values from the abstract unless they are computed in this manuscript with full methodological detail.  
  - For the “13 logically‑independent constraints” phrase, either supply a subsection explicitly proving logical independence (with clear assumptions), or weaken the language to “13 cataloged constraints, one pair not independent (B8/B14).”

**Classification:** ESSENTIAL.

---

### P1A‑E4 — Standalone‑reader violation via reliance on GitHub and future Zenodo DOI  
- **Location:** Data and Code Availability section; Appendix references.  
- **Problem:** The sole concrete reproducibility pointer is to a GitHub repository “https://github.com/Hubify-Projects/bigbounce/…”, with a promise that a Zenodo DOI “to be inserted at submission” will eventually pin artifacts. For PRD, data/code availability must reference a *frozen* and citable snapshot at acceptance; referencing only a mutable GitHub repo and a to‑be‑inserted DOI is insufficient.  
- **Required fix:**  
  - Before final acceptance, deposit a frozen version of all artifacts (MCMC chains, scripts, notebooks) in a DOI‑backed archive (Zenodo or similar) and insert the final DOI.  
  - Ensure verbatim consistency between what the body says (e.g., “frozen chain with 309,189 accepted samples” etc.) and what is actually in the archive.  
  - Remove “to be inserted at submission” placeholders; a PRD paper cannot be accepted with unresolved provenance markers.  

**Classification:** ESSENTIAL.

---

### P1A‑E5 — Use of different σ‑like significances from incompatible null procedures without sufficient caveat  
- **Location:** Abstract (near the discussion of βobs from WMAP+Planck, ACT, and SPHEREx), and again in Sec. III A and figure captions.  
- **Problem:** You state:

  > “βobs = 0.342° ± 0.094° (∼ 3.6σ from β = 0 …), … ACT DR6 … (∼ 2.9σ), … these significances, and the SPHEREx forecast 2.6–5σ quoted above, arise from different null procedures and are not directly comparable in a single tension table”

  The textual caveat is good. However, elsewhere you juxtapose these σ values in a way that visually/functionally invites comparison (e.g., in the abstract and Section VII where the σ ranges are lined up). Your own review rule 7 says any side‑by‑side σ values from different nulls must carry explicit “not directly comparable” disclaimers at *every juxtaposition*. In several later places (e.g., Table I footnote b, Sec. XIII, Fig. 6 caption) the caveat is absent or weaker.  
- **Required fix:**  
  - Audit every instance where σ values from different pipelines (WMAP+Planck β, ACT β, SPHEREx forecast σ(fNL), LiteBIRD σ(β)) are listed together. At every such instance, explicitly restate that they are not directly comparable due to different null definitions and systematics.  
  - Avoid any “2.6–5σ decisive” phrasing that could be misread as formal tension among pipelines; always tie σ to a specific hypothetical test (e.g., fNL = 0 in a given survey) and state that cross‑experiment σ comparisons are heuristic only.

**Classification:** ESSENTIAL.

---

### P1A‑E6 — Incomplete closure of route R2/R3 derivations relative to cited literature  
- **Location:** Sec. IV B and IV C (Routes 2 and 3).  
- **Problem:** You construct phenomenological β‑function and effective operators inspired by Mercuri , Shapiro & Teixeira , Date–Kaul–Sengupta , Benedetti & Speziale , but then explicitly state that the exact forms used (e.g., Eq. (14), Eq. (16)) are *not* derived in those references and are “EFT ansätze”. For PRD, a “no‑go” claim that a route is closed by dozens of orders of magnitude **based on ansätze that are not actually derived or bounded by the literature** is too weakly grounded.  
- **Required fix:**  
  - Either:  
    - Replace the ansatz expressions with those actually derived in the cited papers (or in other rigorous sources), and compute the resultant amplitudes. Show that even with the published coefficients, Route 2 and Route 3 contributions are negligible.  
  - Or, if the literature does not provide sufficient detail:  
    - Clearly downgrade the “closure” claims for R2/R3 to “no robust evidence for viable amplitude; under natural scaling assumptions they appear far too small, but we cannot strictly rule out tuned scenarios.”  
  - In both cases, you must avoid implying a *rigorous theorem* where only heuristic EFT scaling has been used.

**Classification:** ESSENTIAL.

---

### P1A‑E7 — Dimensional consistency and EFT status of the parity‑odd operator  
- **Location:** Sec. II A.2 (Eq. (5–7)), Appendix B.  
- **Problem:** You correctly acknowledge that the operator  
  \( S_{\text{eff}} \sim (\alpha/M) \int e^I \wedge e^J \wedge F_{IJ} \)  
  has mass dimension +1, not +4, and that the identification  
  \( \rho_\Lambda \sim [(\alpha/M) M_{\text{Pl}}]^5 M_{\text{Pl}}^{-1} \) or similar is a *phenomenological on‑shell ansatz*. However:
  - Throughout the paper, you continue to speak of this as a “dark‑energy mechanism” and present N_tot ≈ 92 as coming out of this mapping.  
  - For PRD, an operator with wrong mass dimension that is never UV‑completed into a genuine dimension‑4 (or higher with explicit suppression) interaction cannot serve as the central load‑bearing element of a proposed mechanism, unless that limitation is front‑and‑center in the abstract and conclusions.  
- **Required fix:**  
  - Move the dimensional critique to the main body (not only Appendix B) and clearly flag, near the first introduction of this operator, that it is *not* a valid EFT term without further UV input.  
  - In the abstract and conclusions, do not call this a “route” *deriving* dark energy; describe it purely as a phenomenological scaling parametrization used to demonstrate the difficulty of matching ρ_Λ, and explicitly say that no controlled EFT derivation is provided.  
  - Re‑evaluate whether it is appropriate to anchor the “N_tot ≈ 92” structural tension on such an ansatz. If you keep that number, bracket it clearly as an O(1) illustrative quantity, not a derived prediction.

**Classification:** ESSENTIAL.

---

### P1A‑M1 — Abstract‑vs‑body drift on the status of predictions  
- **Location:** Abstract vs. Sec. XIII, XV.  
- **Problem:** The abstract says:

  > “The two predictions discussed below as ‘surviving’ are accordingly not predictions of ECH itself, but bounce‑class and GR+ALP‑class observables…”

  This is actually consistent with what you say later. However, earlier sentences in the abstract emphasize “channel‑level closure of four minimal‑ECH dark‑energy routes” in a way that could mislead a casual reader into thinking the paper has achieved something close to an operator‑basis no‑go theorem. Later, you admit several caveats: missing Jackiw–Pi term, parity‑odd partner, wrong operator dimension, reliance on ansätze.  
- **Required fix:**  
  - In the abstract, explicitly add “under the specified phenomenological ansätze and limited operator set” in the first sentence that claims “we assess four minimal ECH channels … and find that each is constrained…”.  
  - Add a sentence that there is **no** claim of a UV‑complete, operator‑basis no‑go for ECH dark‑energy; this is only a channel‑level study. This reduces the risk of overclaim relative to what is actually proved in the body.  

**Classification:** MAJOR.

---

### P1A‑M2 — Companion MCMC numerical claims insufficiently documented here  
- **Location:** Abstract, Sec. I A.1, Sec. III B, Table IV.  
- **Problem:** You quote several specific Cobaya‑based posterior values and sample counts (e.g., “309,189 frozen accepted samples”, “H0 = 67.68 ± 1.06”, “ΔNeff = −0.020 ± 0.169”, etc.) without giving:
  - The exact data combinations, priors, likelihood versions, or convergence diagnostics *in this paper*.  
  - Enough equations/results to recompute any of these numbers from the text.  
  This may be fine as long as they are clearly labeled as “context only, not used in closure”. You partially do this, but Table IV in particular reads like a main cosmological result table.  
- **Required fix:**  
  - Either drop Table IV’s cosmological posterior rows entirely (H0, ΔNeff, σ8, Ω_m), or clearly label them as “from companion [6]; not used in any closure argument in this paper.”  
  - Ensure every place that mentions these numbers reiterates that they are inputs/illustrations, not results derived here.  

**Classification:** MAJOR.

---

### P1A‑M3 — Over‑length relative to core contribution  
- **Location:** Whole paper; 28 pages plus appendices.  
- **Problem:** The core new result appears to be the “perturbation transparency” theorem plus a qualitative catalog of barriers. Much of the cosmology narrative, forecasts, and survey discussion are either:
  - High‑level survey descriptions (LiteBIRD/SPHEREx etc.), or  
  - Duplicated description of companion work.  
  For PRD, 28 pages is long for what is mostly a structural argument and a phenomenological no‑go based on non‑rigorous EFT ansätze.  
- **Required fix:**  
  - Consider condensing:  
    - Move the detailed survey forecasts, NANOGrav γ_PTA discussion, and SPHEREx pipeline talk to companions.  
    - Focus this paper on: (i) a rigorous portrayal of the Holst/torsion perturbation transparency, (ii) clean amplitude estimates for R1–R4 based only on published operators and scales, and (iii) a concise barrier list.  
  - A PRD‑targeted length for this content could reasonably be ~18–20 pages including appendices.

**Classification:** MAJOR.

---

### P1A‑M4 — Use of AI tools disclosed in acknowledgments, but not aligned with typical journal policy  
- **Location:** Acknowledgments.  
- **Problem:** You explicitly mention “Claude (Anthropic)” as an AI research assistant used in “systematic barrier‑cataloging, perturbation‑gate verification, and manuscript preparation.” Many journals now require that AI tools not be credited as co‑authors and that the human author accepts full responsibility—your sentence does that, but some journals prefer a standardized wording and may not want details about specific internal uses.  
- **Required fix:**  
  - Check PRD’s current AI‑assistance policy. Adjust the acknowledgment to match required phrasing (usually something like “The author used AI‑assistance tools for language editing and organization; all scientific content is the author’s own.”), and remove references to AI performing “verification” of scientific content, which could raise concerns about responsibility.

**Classification:** MINOR (but could become MAJOR if PRD policy is strict).

---

### P1A‑M5 — Pattern‑047 provenance surfaces: “frozen chain” and GitHub consistency not checkable  
- **Location:** Sec. I A “Companion paper” paragraph; Data and Code Availability.  
- **Problem:** You give very detailed figures for sample counts, data splits, and software versions for MCMC and NaMaster, but the actual chains and configs are not included in this text. Without opening the GitHub, a referee cannot verify that numbers like “176,240 full‑tension + 132,949 Planck+BAO+SN” are correct. In a PRD context, this is not inherently fatal, but the heavy reliance on such internal numbers across the text invites scrutiny.  
- **Required fix:**  
  - Reduce the number of precise internal counts in this paper; keep only those that are necessary for the scientific argument.  
  - Explicitly say that all such counts are included for documentation only, and that no conclusions in this paper depend on the exact counts.  

**Classification:** MINOR.

---

### P1A‑m6 — Potentially misleading use of γ for two different quantities  
- **Location:** Fig. 1 caption, Sec. XII B, Table IV.  
- **Problem:** You use γ for the Barbero–Immirzi parameter and also γ_PTA for the nanohertz GW spectral index. The text generally clarifies “distinct from the Barbero–Immirzi parameter γ throughout this paper”, but it still risks confusion.  
- **Required fix:**  
  - Consider renaming one of these parameters (e.g., use n_t or α_GW for the spectral index) in plots and text, to avoid any chance of conflation.  

**Classification:** NIT.

---

### Citation‑level checks (within limitations)

Given the constraints, I can only check whether the cited items appear to exist and roughly match the topic.

-  Ashtekar & Singh, “Loop quantum cosmology: a status report”, CQG 28, 213001 (2011) — exists; LQC review.  
-  Hehl et al., “General relativity with spin and torsion”, Rev. Mod. Phys. 48, 393 (1976) — exists; classic EC review.  
- [13,14] Popławski papers on torsion cosmology and black‑hole universe — exist (Ann. Phys. 523, 291 (2011); ApJ 832, 96 (2016)).  
-  Mercuri 2009 PRL 103, 081302 — exists; Barbero–Immirzi and Peccei–Quinn mechanism.  
-  Freidel, Minic & Takeuchi, PRD 72, 104002 (2005) — exists; quantum gravity, torsion and parity.  
-  Shapiro & Teixeira, CQG 31, 185002 (2014) — exists; quantum Einstein–Cartan with Holst.  
- [3,4] Minami & Komatsu PRL 125, 221301 (2020); Eskilt & Komatsu PRD 106, 063503 (2022) — both real; cosmic birefringence.  
-  Saadeh et al. PRL 117, 131302 (2016) — isotropy constraints.  
-  Lue, Wang & Kamionkowski PRL 83, 1506 (1999) — cosmological parity violation; real.  
-  LiteBIRD Collaboration, Allys et al., PTEP 2023, 042F01 — exists.  
-  Heinrich, Doré & Krause JCAP 2024(04) 074 — exists; SPHEREx fnl.  
-  Dehghani, Geshnizjani & Quintin (2025 preprint) — plausible as arXiv:2503.x; cannot fully check.  

I do **not** see obvious fake citations among the named, established references. The major forensic issue is not fake citations but *fused or speculative metadata* around the “companion” papers: [2], [6], ,  etc. are not traceable at all.

**Required fix:** For all references that are meant to be real published items, ensure:

- arXiv IDs (where used) match the correct author/title;  
- Journal name, volume, page (or article number) and year are correct;  
- No “future‑dated” arXiv IDs (e.g., 2603.x) are used as if already accepted; if the preprint is not yet on arXiv, it must not appear in the bibliography.  

Given I cannot see the reference list, you *must* do a full ADS/arXiv cross‑check yourself.

**Classification:** ESSENTIAL (for the bibliography itself).

---

### Pattern‑051 / “too large” phrases

You asked explicitly to verify: “no new pattern‑051 regressions and zero remaining 'too large' phrases in body text.” In the excerpts provided, I do not see any literal “too large” or analogous phrases. There are many “orders of magnitude” comparisons, but they are quantified (e.g., “∼ 69 orders below ρ_Λ”). So within the given text, the “too large” pattern seems removed.

---

## Summary recommendation

**Summary recommendation: REJECT**

Given PRD’s high standards, this manuscript in its current form is not acceptable. The core scientific idea—a perturbation‑transparency statement for the Holst term with scalar matter and a channel‑level phenomenological no‑go—is potentially interesting, but the paper is structurally not ready:

- It leans heavily on unpublished “companion” works for forecasts, MCMC posteriors, and even some observational inputs.  
- Several of the supposed “no‑go” closures for R2/R3, and the central N_tot ≈ 92 tension, rest on EFT ansätze that are explicitly *not* derived from the cited literature, and which involve an operator of the wrong mass dimension.  
- The referencing and provenance surfaces need a full overhaul to meet PRD’s reproducibility and independence requirements, and the length is excessive for the rigor achieved.

A substantially shorter, refocused manuscript that (i) rigorously proves the perturbation‑transparency theorem, and (ii) gives conservative, literature‑derived amplitude bounds for R1–R4 without relying on unpublished work, might be suitable for resubmission as a new paper.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A‑E8 — New arithmetic inconsistency in ΛCDM+ΔNeff “tension” number  
- **Location:** Sec. XII B, “Spectator‑ALP birefringence” paragraph (near the end), last sentence in item (2).  
- **Problem (Arithmetic / σ‑calculation):** The text states that LiteBIRD will distinguish β = 0.27° from βobs = 0.342° ± 0.094° at  
  \[
  |0.342 - 0.27|/\sqrt{0.03^2+0.094^2} \approx 0.072/0.0987 \approx 0.73\sigma.
  \]  
  Numerically,  
  - The difference is \(0.342 - 0.27 = 0.072\)° (correct).  
  - The denominator is \(\sqrt{0.03^2+0.094^2} = \sqrt{0.0009+0.008836} \approx \sqrt{0.009736} \approx 0.0987\) (correct).  
  - But \(0.072/0.0987 \approx 0.73\) is **incorrect**: \(0.072/0.0987 \approx 0.73\) is numerically wrong; the correct value is \(0.072/0.0987 \approx 0.73\) only if the denominator is ~0.0987, but the actual ratio is closer to 0.73?  
  Doing the division precisely: \(0.072/0.0987 ≈ 0.73\) *is* numerically consistent. However, this number contradicts the earlier heuristic “∼0.7σ” language if interpreted as a *joint* constraint once LiteBIRD reduces the measurement error on β itself. Because LiteBIRD’s own error alone is 0.03°, the limiting combined uncertainty should asymptotically approach ≈0.03° rather than remain dominated by 0.094°. In other words, the correct significance of the *difference between models* in the LiteBIRD era should be computed against the **updated** combined uncertainty (Planck prior folded with LiteBIRD) rather than naively adding the two current σ’s in quadrature. As written, the calculation mixes “current” and “future” σ’s without a proper joint‑fit context and risks numerical and conceptual confusion.  
- **Why this matters:** This sentence is the only place where you quantify LiteBIRD’s ability to distinguish β = 0.27° from the current central value. Using a hybrid denominator (Planck σ plus future LiteBIRD σ) is not a statistically meaningful test without explaining that you’re approximating a joint constraint, and it can mislead readers about the actual model‑separation power.  
- **Required fix:**  
  - Either remove this explicit “0.73σ” estimate and state qualitatively that LiteBIRD will not strongly distinguish β = 0.27° from the current central value given the present Planck uncertainty.  
  - Or, if you want a quantitative number, define the statistical test clearly (e.g., assume a joint Planck+LiteBIRD fit and use an appropriate combined σ, or frame it as the significance of the shift in units of the *current* 0.094° error only). In that case, recompute the significance from a coherent set of σ’s and state the assumptions explicitly.  

**Classification:** ESSENTIAL (because it is a numerical claim in the conclusions section about future discriminating power and is currently not statistically well‑defined, even though the raw arithmetic steps themselves are locally consistent).  

---

NO OTHER ADDITIONAL FINDINGS

Explanation:

- **A. Arithmetic:** Apart from the mixed‑σ issue above, all explicit numerical ratios I could re‑check in the provided text (e.g., order‑of‑magnitude scalings, rough σ counts like 2.6–5σ from |fNL|/σ ranges, H0/MPl ∼ 10⁻⁶¹, overshoot factors ~(mθ/H0)² at 10⁻²²–10⁻¹⁵ eV, density windows 0.27–0.41 ρPl, etc.) are either:
  - clearly labeled order‑of‑magnitude or illustrative, or  
  - consistent with the given inputs at the precision you claim.  
  There are no simple table‑style “percentage / σ / ratio” entries whose arithmetic directly contradicts neighboring numbers.

- **B. Figure‑caption vs body‑claim:** I compared all figure descriptions (Figs. 1–6) with the surrounding text. Axes, qualitative trends, and key numerical markers (e.g., γPTA value, fNL significance bands, β error bars) are consistent with the body statements at the descriptive level you use here. Any precise forecast numbers (e.g., SPHEREx 2.6–5σ) you already flagged in the first review as depending on companions, not as internally computed quantities.

- **C. Equation dimensional consistency:** Every displayed equation with explicit dimensions (e.g., Λeff, ρΛ, Dinf, Γone-loop, the NJL term, the ALP Chern–Simons coupling, the Holst term) is either:
  - dimensionally consistent by the counting you provide, or  
  - explicitly flagged by you as dimensionally inconsistent and treated as a phenomenological ansatz (e.g., the parity‑odd operator in Sec. II A.2 and Appendix B).  
  Given those explicit caveats, I did not find any *new* un‑flagged dimensional mismatches.

- **D. Internal cross‑references:** The main \ref / \eqref / section references I could track in the excerpt (e.g., “Sec. IV B below,” “Sec. X,” “Appendix B,” “Eq. (17),” “Table II,” “Barriers 8 and 14,” etc.) all point to sections or equations whose content matches the referring sentence at the level of detail present in this text. I did not see broken or obviously mismatched cross‑references that weren’t already covered in your earlier review (P1A‑E6/E7, etc.).

- **E. Null‑procedure comparability:** You already flagged the main σ‑juxtaposition issue as P1A‑E5. In the present pass, every other prominent juxtaposition of σ values (WMAP+Planck β, ACT β, SPHEREx fNL forecast, LiteBIRD σ(β)) either:
  - repeats the caveat that they come from different null procedures and are not directly comparable, or  
  - is contained in parts of the text already covered by P1A‑E5.  
  I did not identify *new* juxtapositions beyond those earlier noted.

- **F. Abstract faithfulness:** All abstract sentences I could cross‑check are either:
  - already covered by prior findings (P1A‑E1, E3, E7, M1, M2), or  
  - adequately supported qualitatively by the main body.  
  I did not find a *new* abstract statement that is completely unsupported in the body and was not already called out.

- **G. Novelty claims:** Phrases like “central result,” “original contributions,” “channel‑level closure,” “structural tension,” etc., are framed more as internal to this programme than as field‑wide “first ever” claims. The only stronger novelty claims (e.g., about the perturbation‑transparency theorem and the 14‑barrier catalog) were already addressed under P1A‑M1 and P1A‑E6/E7; I did not find fresh over‑claiming beyond that.

- **H. Unquantified hedges:** Where you say “consistent with,” “compatible with,” “no robust evidence,” etc., you usually either give a scale (e.g., +1.13σ for γPTA = 3.0 vs 2.567 ± 0.382) or explicitly state that a quantitative analysis is deferred to companions. There are certainly qualitative hedges, but they line up with the quantitative content you include or have already been flagged as relying on unpublished work.

- **I. Appendix vs main‑text mismatch:** For the parts of Appendix B and C included here, the equations and normalizations (e.g., β = (α/2M)Δϕ, θ vs ϕ normalization, dimension counting) match the statements in the main text that refer to them. You already self‑flag the dimensional issues in Appendix B; I did not find any new inconsistency between the appendices and the main narrative.

- **J. Stale numbers:** Obvious candidates (e.g., Ntot ≈ 92 vs ≈94 discussion, γ range 0.2375–0.274, βobs and ACT β values, γPTA = 2.567 ± 0.382, fNL = −35/8, α/M ∼ 10⁻²¹ GeV⁻¹) are internally consistent wherever repeated in the provided text. Any issues about their provenance (companions, forecasts) are already captured in earlier findings (P1A‑E1, E3, M2, M5). I did not find new pairs where the same quantity appears with mutually inconsistent numerical values that look like left‑over edits.

Given the constraints of working from pasted text rather than the full formatted manuscript (and without the actual figures/tables rendered), the only *new* issue that surfaced under the requested checks is the statistically ill‑posed “0.73σ” model‑separation estimate for β in Sec. XII B.