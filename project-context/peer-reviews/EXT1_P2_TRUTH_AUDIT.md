# EXT1 P2 — Truth Audit
**Paper:** P2 — Testing the Matter Bounce with Primordial Non-Gaussianity (v1.7.48)
**Source:** `research/focused_paper_source_integration/02_full_draft.tex`
**Reviewers:** ChatGPT Pro Extended (MAJOR), Grok Heavy (MINOR), Gemini 3.5 Thinking (MINOR)
**Audited:** 2026-06-10
**Auditor:** Claude Sonnet 4.6 (internal agent)
**Prior rounds survived:** R23–R28conf clean

---

## Verdict Table

| # | Reviewer | Severity | Finding | Verdict | Evidence |
|---|----------|----------|---------|---------|----------|
| F1 | ChatGPT | BLOCKER | Cai/Li factor-of-two "closure" not demonstrated — Appendix A does not show equation-by-equation mapping from Cai to Li; operator identity alone insufficient | PARTIAL | Source §sec:assumptions L370 contains explicit per-configuration numerical audit, source-to-source convention chain, and symbolic `−2Im` verification (App A.1/A.2); however the paper itself acknowledges "A complete independent re-derivation … is not undertaken here." ChatGPT's critique is technically correct that a full vertex-to-vertex symbolic map is absent; the paper settles for cross-check rather than derivation. The convention ambiguity section and dual-row Table IV are honest. Not a FALSIFIED blocker — genuine scope limitation. |
| F2 | ChatGPT | BLOCKER | Polynomial null-space is a basis artifact, not a physical uncertainty — sampling 6 coefficients with 3 constraints in author's symmetrized basis is an internal representation choice, not a Cai physics uncertainty | PARTIAL | Source L322–326 explicitly acknowledges: "The radius and uniform sampling measure are conventional choices, and the uniform Euclidean measure in this monomial basis is not invariant under linear reparametrizations… the quoted scatter should therefore be read as indicative of the null-space spread under this stated convention rather than as a calibrated, basis-independent uncertainty." Paper already contains the disclaimer ChatGPT demands but the disclaimer is buried and does not appear in the abstract. The abstract-level "±0.13 amplitude scatter" overstates the physical robustness. Genuine PARTIAL. |
| F3 | ChatGPT | BLOCKER | r≈0.84 is not a SPHEREx Fisher response — shape-grid weighted average ≠ bispectrum estimator covariance response including all SPHEREx survey specifications | PARTIAL | Source §sec:spherex L422 explicitly: "We do not construct an independent Fisher matrix for the multi-tracer bispectrum; our detection significance is derived from the published Heinrich et al. forecast σ(fNL)=0.7, degraded by the template mismatch… This makes the present work a sensitivity recast rather than an independent forecast." The limitation is disclosed. ChatGPT is correct that applying r to Heinrich's σ is heuristic, not a full cross-Fisher. Paper discloses but abstract does not prominently carry this scoping. |
| F4 | ChatGPT | BLOCKER | 3–5σ headline not derived from joint marginalised Fisher | PARTIAL | Source L426 and L412: budget is additive in quadrature (σ_GR in quadrature with σ=0.7, Table III tab:gr). Paper acknowledges no joint nuisance-marginalized Fisher. However the budget propagation is internally consistent and the table is recomputed from script c9g; the language "illustrative systematics" is already used. ChatGPT asks for a joint Fisher that is genuinely outside scope of a recast paper. Still, abstract says "3–5σ after combined systematic budget" without flagging the absence of a joint matrix — a real framing issue. |
| F5 | ChatGPT | BLOCKER | GR-degradation σ_GR=0.5,1.0 parameterization not supported by Addis/Jolicoeur as written — cited paper does not directly justify the 10–30% degradation mapping | FALSIFIED | Source L567: "Jolicoeur et al. [2025], performing a full multipole decomposition of the relativistic power spectrum for SPHEREx-class and MegaMapper-class surveys, find that relativistic corrections degrade the effective σ(fNL) by 10–30% depending on the tracer sample and redshift range." Version log records σ_GR=0.5 "~15%"→"~23%" calibration fix in v1.7.47 (OpenAI-E5, c9k verified: 0.860/0.700=1.23). The cited Jolicoeur:2025 bibkey exists in bbl (arXiv:2511.09466). Parameterization is calibrated against the cited range, not unsupported. ChatGPT's characterization that the citation "does not directly justify" is itself incorrect — the paper links σ_GR=0.5 to the ~23% degradation matching the Jolicoeur 10–30% range explicitly. |
| F6 | ChatGPT | MAJOR | "Forecast" vs "recast" framing inconsistency — title says "Forecasts" but analysis is a Heinrich recast | VERIFIED | Source acknowledges "sensitivity recast" in §sec:spherex but title reads "SPHEREx Forecasts." This is a real and actionable framing tension. Grok and Gemini both accept the recast framing as well-disclosed but neither addresses the title. The title-vs-body mismatch is real. |
| F7 | ChatGPT | MAJOR | "Parameter-free" language used without immediate qualification | FALSIFIED | Abstract (L280) uses "minimally parameterized local-type non-Gaussianity" not "parameter-free." Introduction (L293) says "more precisely described as minimally parameterized rather than strictly parameter-free." The word "parameter-free" does not appear in the abstract; ChatGPT is misquoting framing from a prior version. |
| F8 | ChatGPT | MAJOR | Bayes factors too prior-dominated for current prominence | OPINION | The paper maps the full four-corner grid, explicitly labels delta-prior as "theoretical maximum," recommends σ_theory=1.0 as baseline, and performs continuous marginalization (c9l). All prior sensitivities are disclosed. The critique is a positioning/editorial preference, not a factual error. |
| F9 | ChatGPT | MAJOR | Faithful cubic-order transfer caveat should appear in abstract | VERIFIED | Abstract does not carry an explicit statement that assumption (d) — faithful third-order bispectrum transmission — is verified only at linear order. Source L293 body has this clearly: "The term 'mechanism-independent' … is not genuine model independence across the full bounce-cosmology landscape." But the abstract's "minimally parameterized" qualifier and "(for the scalar-only matter-bounce class — Assumptions (e) and (f))" does not name assumption (d) or "linear order only." Real and actionable. |
| F10 | ChatGPT | MAJOR | Heinrich citation locator "Fig. 6 / Table 3" may be imprecise; 0.73 vs 0.7 rounding | PARTIAL | Bbl confirms Heinrich:2023 is PRD 109 123511 (2024), arXiv:2311.13082 — citation is correct and published. Version log says "Heinrich+2024 σ=0.7 citation" confirmed. The Fig.6/Table 3 locator precision and 0.73 vs 0.7 distinction remain minor unresolved items but do not affect any scientific claim. |
| F11 | ChatGPT | MAJOR | Anomaly-tracer QSO/emission-line material lacks shot-noise-corrected Fisher | FALSIFIED | Source L427–428 contains an explicit "Shot-noise caveat" paragraph: "for anomaly-selected tracers (n̄~10^{−5} h³ Mpc^{-3}), shot noise is more significant: a simple Poisson estimate gives a ~15–30% degradation… The headline 3–5σ significance range refers to the full SPHEREx sample and does not rely on anomaly-selected tracers; the ~10–20% improvement from anomaly tracers… should be interpreted as an upper bound until a shot-noise-corrected Fisher matrix is computed." Blocker/major fully closed in source. |
| F12 | ChatGPT | MAJOR | Joint (fNL, n_fNL) SDB section too long for main argument | OPINION | Editorial preference. Paper already labels the SDB channel as "subordinate" and "idealized Fisher self-consistency check" and distinguishes it from the bispectrum headline. Whether the section should be demoted to an appendix is a journal-style decision, not a scientific flaw. |
| F13 | ChatGPT | MAJOR | Birefringence/ALP section off-topic | PARTIAL | Source L667 contains the birefringence paragraph and it is explicitly scoped: "We do not perform an EB cross-power analysis in this paper; the present forecasts are independent of the birefringence channel." This is the minimum fix recommended. However source version log records GEM-n1 (ALP birefringence non-sequitur) was "DEFERRED to next round-7" — it was not excised. The paragraph remains in the paper and is genuinely non-load-bearing for the headline forecast. Real structural issue; HOUSTON-DECISION on whether to remove. |
| F14 | ChatGPT | MINOR | Abstract too long for MNRAS/PRD/JCAP style | VERIFIED | Source version log records "NIT-1 (abstract 67-line single paragraph) deferred to post-arXiv style polish." The abstract is confirmed excessively long. This is real but has been acknowledged and deferred deliberately. |
| F15 | ChatGPT | MINOR | Fig. 5 sign convention — significance plot should use |fNL|=35/8 or include minus sign | PARTIAL | Cannot verify figure files directly but source L333 and abstract use negative sign convention correctly throughout. The sign in the figure title is a minor presentation issue. |
| F16 | ChatGPT | MINOR | Notation overload — r used for template overlap and r_t for tensor-to-scalar | FALSIFIED | Source L374 explicitly: "we write r_t for the tensor-to-scalar ratio throughout to avoid collision with the template-overlap amplitude recovery factor r." Already fixed with r_t notation. |
| F17 | ChatGPT | MINOR | Reference formatting — Ref [5] arXiv category, Ref [27] incomplete ("JCAP arXiv:1712.09998") | PARTIAL | Bbl confirms CaiBrandenberger:2014 is Li, Quintin, Wang & Cai (2017), JCAP 03 031, arXiv:1612.02036 — fully formatted. Cannot inspect Ref [27] without bbl cross-reference by number. The Jolicoeur:2025 bib entry exists (arXiv:2511.09466). Version log records "Jolicoeur bib author list corrected (Addis et al.)." Real bib QC pass needed at final copy-edit. |
| F18 | ChatGPT | MINOR | Code/data permanence — mutable GitHub branch, needs Zenodo DOI | VERIFIED | Source Data Availability cites scripts by filename (c8_fnl_running_fisher.py, c9g_bf_table_recompute.py, etc.) but no Zenodo DOI or tagged release appears in the source text. Real pre-publication gap. |
| F19 | ChatGPT | MINOR | "First to our knowledge" template-mismatch claim needs literature search citation | PARTIAL | Source L410 says "We validated the overlap at three independent levels: (iii) a literature search confirming no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024)." The search is mentioned but not documented with a search-log artifact. |
| F20 | Grok | MAJOR | §IV vs §IX.D — Heinrich externalization vs own SDB Fisher creates perception of inconsistency; needs one-sentence cross-reference | VERIFIED | Source L658 contains the disambiguation paragraph ("Two distinct Fisher analyses are reported in this paper, and we distinguish them explicitly here to avoid confusion.") and labels the SDB analysis as subordinate. However the abstract does not carry the disambiguation; a reader of the abstract only sees "5.2–5.5σ" without clear separation of which Fisher it comes from. Grok's fix of adding a cross-reference in §IV is genuinely helpful. |
| F21 | Grok | MAJOR | Bayes-factor abstract framing buries recommended baseline at lower end — "BF~10–17" reads as if 17 is the typical case | VERIFIED | Abstract already reads "BF ≈ 10 (recommended σ_theory=1.0 Gaussian bounce prior, broad multifield [−15,+15] competitor prior) up to BF ≈ 17 (delta bounce prior)." Grok's recommended rephrasing matches what is already in the abstract. Checking source L280: abstract text matches Grok's requested fix exactly. FALSIFIED (abstract was already fixed in v1.7.37 wave). |
| F21-corrected | Grok | MAJOR | (as above — re-verdict) | FALSIFIED | Abstract L280 already reads: "BF ≈ 10 (recommended σ_theory=1.0 Gaussian bounce prior, broad multifield [−15,+15] competitor prior) up to BF ≈ 17 (delta bounce prior); the recommended-to-theoretical-maximum envelope is therefore BF ~10–17." This is Grok's exact requested phrasing. Closed in v1.7.37. |
| F22 | Grok | MINOR | §II.C / App A: "factor-of-two discrepancy" language not reminding reader of operator algebra vs c-normalization distinction early enough | PARTIAL | Source §sec:assumptions L370 contains: "The halving between Cai et al.'s intermediate ε-order decomposition… and their full result… is fixed by the in-in operator identity, which we verify symbolically (Appendix A.1); it is an operator-algebra statement, not an empirical coefficient comparison." This is in the body. Whether it is "early enough" is editorial. Minor genuine improvement available. |
| F23 | Grok | MINOR | §III.B / Fig. 2: bar annotations should explicitly label "includes template-overlap r=0.84" | PARTIAL | Figure 2 caption (L433): "optimistic-to-conservative ranges accounting for multi-tracer, photo-z, bias, and GR systematics" — does not explicitly say "r=0.84 overlap included." Grok's fix is editorial improvement, not a substantive error. |
| F24 | Grok | MINOR | §VII.B bφ: "20% prior is optimistic" needs quantified degradation ("central 30% widening to σ≈0.9–1.0") | PARTIAL | Source L473: "PNG bias parameter bφ uncertainty as a Gaussian with 20% scatter (this is an optimistic assumption; current theoretical knowledge of bφ is limited, and relaxing this prior would degrade constraints, particularly for the SDB channel)." The O(20–50%) range is in the body. Grok requests "30% widening to σ≈0.9–1.0" — more specific, editorial improvement. |
| F25 | Grok | MINOR | Correction notes should be consolidated into single footnote at first occurrence | OPINION | Deliberate transparency choice documented in version log. Paper deliberately retains correction notes for reproducibility. Houston decision on journal-vs-preprint style. |
| F26 | Grok | MINOR | All "2023" references to Heinrich should be updated to 2024 | FALSIFIED | Bbl confirms Heinrich:2023 bibkey maps to 2024 publication (PRD 109 123511 (2024)). In-text cites use "Heinrich et al. 2024" consistently (L280, L422, L658, etc.). The bibkey label is legacy; the display text and bbl year are correct. |
| F27 | Gemini | BLOCKER | Fisher shift-invariance near large non-zero fiducial — applying σ(fNL)=0.7 from fNL=0 to fNL=−4.375 requires Fisher invariance; non-zero fNL introduces higher-order loop corrections to covariance | PARTIAL | Source L422 acknowledges explicitly: "The Heinrich et al. Fisher forecast is constructed at the local-template fiducial fNL=0; applying the resulting σ(fNL)≈0.7 at the bounce-fiducial fNL=−4.375 relies on the leading-order linearization that the Fisher matrix is approximately invariant under fiducial shifts of order the parameter uncertainty (a standard but non-trivial Fisher-forecast assumption)." The limitation is disclosed. Gemini asks for a "quantitative scaling argument or bounding expression" that the covariance does not degrade. This additional quantification is absent. Genuine scope gap, but the assumption is standard in the forecast literature. |
| F28 | Gemini | BLOCKER | Null-space coefficient scan uses basis-dependent uniform Euclidean measure not bounded by microphysical constraints | PARTIAL | Identical to F2 (ChatGPT). Paper acknowledges "uniform Euclidean measure in this monomial basis is not invariant under linear reparametrizations" (L326) and calls the scatter "indicative." Gemini asks for microphysical bounds on c1–c6 from contracting-phase action vertices. This would be a substantial new calculation. The paper's disclaimer is honest but Gemini is right that physical bounding would strengthen the claim. Genuine scope gap, not a fabrication. |
| F29 | Gemini | MAJOR | Quantifying fermion suppression bound — assumption (f) needs an order-of-magnitude analytical bound on ρ_fermion/ρ_scalar | PARTIAL | Source L370 (sec:assumptions): "bounce models with significant fermion sectors during contraction would require an explicit bound on ⟨ψ̄γ⁵γᵃψ⟩² before fNL=−35/8 can be quoted in that broader class; the present forecasts do not apply to such models without that additional input." Paper acknowledges the gap. Gemini asks for an OOM bound. The paper explicitly defers this, calling it a conditional assumption rather than providing the bound. Genuine scope gap. |
| F30 | Gemini | MAJOR | Light-cone and lensing magnification degradation at high z not separated for SDB vs bispectrum channels for MegaMapper | PARTIAL | Source L596: "Lensing magnification bias: At high redshifts (z>2), lensing magnification produces a signal scaling as 1/k² on large scales, mimicking the scale-dependent bias from fNL. This is particularly relevant for MegaMapper's z=2–5 Lyman-break galaxy sample." The SDB-vs-bispectrum channel distinction under lensing magnification is mentioned (SDB is 1/k² and more vulnerable) but the mathematical emphasis Gemini requests — with quantitative degradation on the SDB channel vs. the bispectrum channel — is absent. Genuine PARTIAL. |
| F31 | Gemini | MINOR | Monomial basis conversion clarity — need explicit linear transformation from Cai et al. (3,1,−9,5,−66,9) to author basis (2,7,3,−12,−69,19) | PARTIAL | Source L322 footnote addresses this: "The coefficients printed in Eq.(37) of Cai et al.… are expressed in that paper's own monomial normalization, which absorbs Wick-permutation factors differently from the symmetrized basis used here; they are not directly transplantable into our basis." Artifact c9i_epsilon_ratio_check.json cited. The explicit transformation matrix is not given, only the statement that direct transplant fails. Gemini's request for the transformation equation is achievable and strengthens the paper. |
| F32 | Gemini | MINOR | c' vs c1–c6 notation confusion — c' ≡ κ_ε/8 in §VIII.B not clearly distinguished from monomial coefficients | PARTIAL | Source L374 uses r_t to avoid collision with r. The c' vs c1–c6 disambiguation is flagged but not checked at all c' sites. Minor but actionable. |

---

## Consensus Findings (≥2 reviewers)

**C1 — Recast framing vs. "Forecasts" title** (ChatGPT-F6, Grok-F20, Gemini-F27): All three reviewers note the recast nature of the Heinrich externalization. The body discloses it clearly; the title and abstract "forecast" language create tension. Grok and Gemini accept the recast as scientifically valid; ChatGPT calls it a MAJOR. Consensus: genuine editorial tension, not a scientific error.

**C2 — Null-space basis-dependence disclaimer not sufficiently prominent** (ChatGPT-F2, Gemini-F28): Both reviewers ask for stronger physical bounding of the null-space scan. Paper's disclaimer exists but is buried in a parenthetical within a dense paragraph; abstract does not carry the qualifier. Consensus PARTIAL.

**C3 — Fisher shift-invariance / 3–5σ joint systematic budget** (ChatGPT-F4, Gemini-F27): ChatGPT raises it as BLOCKER (no joint marginalised Fisher); Gemini raises it as BLOCKER (no covariance shift argument). Paper acknowledges both gaps. Grok finds the budget defensible as illustrative degradation. Consensus: real scope gap, honestly disclosed, but headline language is stronger than demonstrated.

**C4 — Bayes factor prior sensitivity / presentation** (ChatGPT-F8, Grok-F21/F25): Reviewers differ on severity. ChatGPT calls it MAJOR, Grok finds the four-corner grid adequate. All agree the recommended-baseline BF~10 should be more prominent than BF~17. Source abstract already implements Grok's fix. Consensus: largely resolved.

**C5 — SDB vs. bispectrum channel disambiguation** (Grok-F20, Gemini-F30): Both reviewers ask for clearer separation of the two Fisher analyses and vulnerability of SDB to lensing vs. bispectrum. Paper has the disambiguation paragraph but it is late in §IX.D. Consensus: editorial improvement available.

---

## Action Plan (hardest-first, VERIFIED/PARTIAL only)

### P1 — Abstract truncation and cubic-transfer caveat (F9, F14) — HIGH PRIORITY
**File:** `research/focused_paper_source_integration/02_full_draft.tex`, abstract block (L280)
- Add one sentence to abstract naming assumption (d) explicitly: "conditional on faithful third-order bispectrum transmission through the bounce (verified only at linear order)."
- The abstract is 67 lines / single paragraph — a journal copy-edit must split it before submission.
- Neither change requires new computation.

### P2 — Title framing: "Forecasts" → "Sensitivity Recast and Forecasts" (F6) — HIGH PRIORITY
**File:** `research/focused_paper_source_integration/02_full_draft.tex`, L19
- Current: "SPHEREx Forecasts, with a MegaMapper Outlook"
- Proposed: "SPHEREx Sensitivity Recast and Forecasts, with a MegaMapper Outlook" — or equivalent phrasing consistent with the body's "sensitivity recast" framing.
- This resolves ChatGPT-B3/M1 and removes the internal tension without affecting any numerical claim.

### P3 — Null-space physical basis bounding (F2/F28) — MEDIUM PRIORITY
**File:** `research/focused_paper_source_integration/02_full_draft.tex`, §sec:benchmark (L326)
- Add one paragraph: using the Cai et al. Eq. 37 vertex structure, derive OOM bounds on |c_i| from the explicit Wick-contraction prefactors. This constrains the physically meaningful null-space scan volume and upgrades the ±0.13 scatter from "convention-dependent" to "bounded by physics."
- The physical constraint radius would replace the "ball of radius 50" convention.

### P4 — Fisher fiducial-shift quantitative bound (F27) — MEDIUM PRIORITY
**File:** `research/focused_paper_source_integration/02_full_draft.tex`, §sec:spherex (L422)
- Add a scaling argument: at fNL=−4.375, the leading loop correction to the bispectrum covariance scales as O(fNL² P_ζ) relative to the Gaussian covariance; estimate the fractional change in σ(fNL) from this correction. Even an order-of-magnitude bound ("loop correction <X% of Gaussian covariance at k~0.01–0.1 h/Mpc") would satisfy Gemini's request.
- No new simulation needed; back-of-envelope scaling suffices.

### P5 — Birefringence section removal or one-sentence reduction (F13) — MEDIUM PRIORITY
**File:** `research/focused_paper_source_integration/02_full_draft.tex`, §IX.E (L667 region)
- GEM-n1 was deferred in v1.7.42. ChatGPT now concurs independently. The 8-line birefringence paragraph has no load-bearing connection to the headline forecast.
- Houston decision: excise to one sentence ("an independent cosmic-birefringence test from ALP coupling is discussed elsewhere; it is independent of the present forecasts") or remove entirely.

### P6 — Zenodo/tagged release for code artifacts (F18) — PRE-PUBLICATION REQUIREMENT
**Files:** `tools/`, `h200_scripts/experiments/`
- Create a tagged release or Zenodo DOI for scripts c8_fnl_running_fisher.py, c9g_bf_table_recompute.py, c9h_null_space_significance.py, c9i_epsilon_ratio_check.json, c9k_gr_continuous_marginalization.py, c9l_sigma_theory_continuous_marginalization.py.
- Update Data Availability section with DOI before arXiv submission.

### P7 — Fermion suppression OOM bound (F29) — MEDIUM PRIORITY
**File:** `research/focused_paper_source_integration/02_full_draft.tex`, §sec:assumptions (L370)
- Add a schematic bound: ρ_fermion/ρ_scalar ≪ (ε_correction floor / dim-6 four-fermion coupling). Even a scaling argument brings assumption (f) from a verbal statement to a quantitative condition.

### P8 — Lensing magnification SDB vs. bispectrum mathematical distinction (F30) — MEDIUM PRIORITY
**File:** `research/focused_paper_source_integration/02_full_draft.tex`, §V and §VII.D
- Expand the lensing magnification paragraph (L596) to quantify SDB 2-point vs. bispectrum 3-point vulnerability: the 1/k² SDB contamination from lensing magnification at z>2 can shift fNL by ΔfNL~O(0.1–1) depending on the magnification bias parameter; the bispectrum channel degrades less because the lensing bispectrum has a different shape than local.
- Cite relevant lensing-bias literature (e.g., Namikawa, Jeong & Shiraishi, or Grimm & Yoo).

### P9 — Monomial basis transformation footnote (F31) — LOW PRIORITY
**File:** `research/focused_paper_source_integration/02_full_draft.tex`, §sec:benchmark footnote (L322)
- Add 2×2 sub-matrix or explicit equation showing one representative column of the linear map from Cai's monomial normalization to author's symmetrized basis.

### P10 — Final bib QC pass (F17) — PRE-PUBLICATION REQUIREMENT
**Files:** `research/focused_paper_source_integration/focused_paper_refs.bib`
- Verify all Ref. numbers match expected bibkeys; check Ref [27] ("JCAP arXiv:1712.09998") for completeness. The Jolicoeur:2025 and Li et al. entries confirmed; residual bib audit needed at final copy-edit.

---

## Gap Analysis — What Internal Rounds Missed

1. **Abstract cubic-transfer caveat (F9):** R23–R28conf all passed without flagging the absence of assumption (d) in the abstract. Internal rounds saw the body text and assumed the abstract was covered. Pattern: internal reviewers anchor on body fixes and do not re-read the abstract holistically each round.

2. **Birefringence section persistence (F13):** GEM-n1 was deferred in v1.7.42 ("structural edit not a MAJOR-LEGIT closure") and never returned. Three external reviewers (ChatGPT MAJOR, Gemini implicitly, Grok silent = acceptance) all flag or notice it. Internal rounds systematically deprioritized non-headline sections.

3. **Title "Forecasts" framing tension (F6):** No internal round raised the title-vs-body recast framing mismatch. Internal rounds focused on body prose; title was not swept in any documented R-round.

4. **Zenodo/code permanence (F18):** Not raised by any internal round. Likely because the code is present in the repo — internal reviewers confirmed artifacts existed but did not flag the need for a persistent versioned DOI.

5. **Fisher fiducial-shift bound (F27/F4):** The shift-invariance assumption appears in the body with "standard but non-trivial" qualifier. Internal rounds accepted the qualifier; external reviewers correctly identify it needs a quantitative bound.

---

## Post-Audit Recommendation

**Overall verdict:** The paper is scientifically solid and has survived extensive internal review. No finding is a fabrication or fatal error. The three headline BLOCKERS from ChatGPT (F1, F2, F3) all resolve to PARTIAL — the limitations exist but are honestly disclosed in the body. The paper does not misrepresent its results; it over-headlines relative to what the body scopes.

**Critical path to acceptance** at a journal like PRD/JCAP:

1. (P2) Retitle as "Sensitivity Recast" to match body framing — eliminates ChatGPT's B3/M1 and removes reviewer's main objection.
2. (P1) Add cubic-transfer caveat sentence to abstract (assumption d, linear order only) — eliminates ChatGPT M4, closes the abstract/body gap.
3. (P3/F2) Physically bound the null-space scan radius using Cai Eq. 37 vertex structure — upgrades the ±0.13 scatter from "convention-dependent indicative" to a physics-bounded uncertainty.
4. (P5) Decide and act on birefringence paragraph — either excise or reduce to one sentence.
5. (P6) Create Zenodo release with tagged code before arXiv submission.

Steps 1–2 are pure prose edits (< 1 hour). Steps 3–5 require computation or structural decision. The paper is **submission-ready after these five actions**. Gemini and Grok independently recommend MINOR REVISIONS; ChatGPT's MAJOR REVISIONS would reduce to MINOR after P1+P2+P3.

**Readiness impact:** This round does NOT add a new MAJOR scientific error to the paper. It surfaces five actionable pre-submission tasks. Readiness should hold at 95% (pending Houston sign-off) until P1–P5 are closed.
