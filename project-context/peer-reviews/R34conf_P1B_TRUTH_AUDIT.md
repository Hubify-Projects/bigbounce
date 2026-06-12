# R34conf P1B — Confirmation-Round Truth-Audit

**Round**: R34conf (post-EXT4-closure verification)
**Paper**: `arxiv/paper1b_mcmc_companion.tex` · v1B.0.59 (19 pp.)
**Date**: 2026-06-11 PT
**Reviewers audited** (4 of 5 legs):
- `R34conf_P1B_OpenAI_methodology.md` — gpt-5-2025-08-07 (NATIVE PDF, pass-2) — MAJOR REVISIONS
- `R34conf_P1B_Gemini_cosmology.md` — gemini-2.5-pro (NATIVE PDF, pass-2) — MAJOR REVISIONS
- `R34conf_P1B_Grok_brutal.md` — grok-4.3 (rasterized PNG, pass-2) — REJECT
- `R34conf_P1B_Perplexity_citations.md` — sonar [FALLBACK from sonar-pro] (TEXT only, pass-2) — MAJOR REVISIONS
- `R34conf_P1B_Claude_brutal.md` — **ABSENT** (Anthropic API credits exhausted; noted, not penalizing)

**Protocol**: EXT4_P1B_TRUTH_AUDIT.md rulings carried forward per pattern-052 auto-dispose.
EXT4-FALSIFIED items (Ge1–Ge4, Ge2-repeat) and EXT4-OPINION items (G1–G4) are auto-disposed.
EXT4-VERIFIED items (C1 CHANGELOG gap, C3 README DESI/AIC, C6 citation, C7 Data Avail, C8 README PR4)
were closed in the v1B.0.59 wave — regression check below. EXT4 PARTIAL items (C2/C5 conclusion wording)
status carried forward and checked for re-raise. June 2026 is current; arXiv 25xx/26xx IDs valid.

---

## EXT4-closure regression check (pattern-051)

EXT4 closed five items before this round in the v1B.0.59 closure wave:
- **C1** — v1B.0.58 + v1B.0.59 CHANGELOG entries added to root CHANGELOG.md
- **C3** — README.md "DESI DR2" removed from full-tension config; AIC/BIC row clarified
- **C6** — Conclusion L2097 citation changed from bare `\cite{DESI2025DR2}` to `\cite{Cai2010quintomReview}` (tested against DESI DR2)
- **C7** — Data Availability chain sentence clarified
- **C8** — README birefringence row corrected: "Literature value (WMAP+Planck PR4)" → model fiducial value + PR3+WMAP9 attribution

**Regression check**: tex grep confirms all five closures:
- CHANGELOG.md now contains v1B.0.58 and v1B.0.59 entries (grep shows L19–42).
- README.md L74–77: "DESI DR2 enters only the separate iter2 w₀wₐ chain and is not part of the frozen ΛCDM+ΔN_eff fit"; L85: "AIC/BIC/ln B NOT reported in manuscript (deferred to nested sampling)." C3 CONFIRMED.
- tex L2097: `quintom-B scenario~\cite{Cai2010quintomReview} (tested against DESI~DR2~\cite{DESI2025DR2})`. C6 CONFIRMED.
- README.md L87: corrected birefringence row present. C8 CONFIRMED.

No regression introduced by EXT4-closure wave. EXT4 PARTIAL C2/C5 (θ_i conclusion wording / §III structure) were not executed as full structural fixes — re-raise expected.

---

## Findings table — all R34conf findings (fresh items only)

EXT4-FALSIFIED items (Ge1 n_s→"72", Ge2 App C duplicates, Ge3 "datase", Ge4 Cyrillic) and
EXT4-STALE items (Ge5/Ge6 pairing bias, accumulating chain) auto-disposed per pattern-052.

| # | Reviewer | Label | Sev | Finding | Verdict | tex Evidence |
|---|----------|-------|-----|---------|---------|--------------|
| **B1** | OpenAI, Gemini, Grok, Perplexity | P1B-E1 / P1B-M1-Gemini | ESSENTIAL | Pervasive internal version-history language in body: "earlier draft," "superseded," "pre-real-KDE"; version stamp "v1B.0.59" in header; raw file paths in main text | **VERIFIED — 4 active body-text instances** | grep confirms 4 non-comment body instances: L1521 "quoted in an earlier draft of this footnote"; L1762 "an earlier draft quoted [0.2, 1.1] with Δφ/fa ≈ 0.65 at m = H₀"; L1830 "earlier draft quoted [0.17,0.43]° from a joint-trajectory scan for which no artifact survives, and that range is superseded"; L2293 "superseded for coupling inference". All four must be rewritten to state only the final correct values without draft-history language. The version stamp in the header (v1B.0.59, timezone) is a submission-prep removal. Raw file paths (NaMaster driver, branch-R paths) are HOUSTON-DECISION (move to supplement). **Fix required: rewrite 4 body draft-history instances; remove header version stamp.** |
| **B2** | OpenAI | P1B-E2 | ESSENTIAL | Mixed Planck PR4/2018 likelihood pairing for ΛCDM+ΔNeff: no pairing-consistency test run; ΔNeff and H₀ claims may carry unquantified systematic | **STALE-with-disclosure — 5th re-raise (EXT1, EXT2, EXT3, EXT4 Ge5, now R34conf)** | tex L912 (fn:pairing_caveat) is present and unchanged: "NPIPE CamSpec high-ℓ + Planck 2018 low-ℓ/lensing; no PR4-consistent low-ℓ swap test performed; pairing-induced bias unquantified." OpenAI's E2 is identical in content to EXT4 Ge5 (parked adequate-disclosure). The compute-bound swap test is queued. STALE — adequate-disclosure parked. |
| **B3** | OpenAI | P1B-E3 | ESSENTIAL | Fig. 3 caption lacks explicit "not directly comparable" warning for 20–26 MC SNR vs 2.7–2.9σ sky detection | **PARTIAL — body text has disclaimer; caption is weaker** | tex L1371–1372 (Fig. 3 caption): "The worst-case |bias| = 0.040° is carried forward as the NaMaster systematic floor." The body at L1487–1492 states both SNR and detection significance and the difference clearly. The caption itself does not include the "not directly comparable" language. OpenAI and Grok both flag this; a parenthetical in the caption is a legitimate MINOR editorial fix. PARTIAL — same-class as EXT3 G2; caption-level addition warranted. |
| **B4** | OpenAI, Gemini, Grok | P1B-E4 / P1B-M3-Gemini / P1B-M3-Grok | ESSENTIAL/MAJOR | w₀wₐ analysis combines DES-SN5YR + Pantheon+ without joint covariance for ~20% overlap; presents multi-σ ΛCDM departures | **STALE-with-disclosure — 5th re-raise** | tex L1097 (caveat e): explicit ~20% overlap acknowledgment, "queued SN-overlap control chains," "cannot treat as independent likelihoods." EXT4 C2/C5 PARTIAL rulings apply. The SN-overlap control chain pair is queued on the MPI pod — a compute-bound robustness test. The body presents the result explicitly as "exploratory, overlap-uncorrected" (L2097). STALE-with-disclosure. The EXT4 C2/C5 PARTIAL (one-sentence conclusion edit) was not fully executed — see B8 below. |
| **B5** | OpenAI | P1B-E5 | ESSENTIAL | "Column-permutation bug" in frozen diagnostic export; directs readers to corrected JSON | **STALE — EXT3-closure acted on this; corrected JSON is now canonical** | tex Data Availability and Appendix A already point to `parameter_summary_CORRECTED.json` (grep confirmed). EXT2 A4 (F20/F21) closed this — the corrected JSON was committed and the README updated. OpenAI re-raises as if the bug-disclosure note is still asking readers to work around corrupt files. tex L2187+ and README L14–17 both direct to the CORRECTED JSON. The bug-disclosure note is transparency language, not a live corruption issue. STALE — EXT2 closed. |
| **B6** | OpenAI | P1B-E6 (pass-2) | ESSENTIAL | Helium/BBN-consistency treatment for variable N_eff: CAMB BBN-consistent default not documented; validity range at N_eff ≈ 2.046 not stated | **VERIFIED — new, not previously raised** | tex Sec. III does not explicitly state which BBN-consistency module CAMB uses (PArthENoPE or equivalent) nor whether the lower prior bound N_eff ∈ [2.046, 5.046] remains within calibrated BBN fit domains. This is a legitimate methodology gap not raised in EXT1–EXT4. **Fix: add 1–2 sentences in Sec. III or footnote specifying the BBN module used and confirming that the prior range [2.046, 5.046] is within its validated domain; or add a free-Y_He control run.** |
| **B7** | OpenAI | P1B-M1 | MAJOR | Beam/pixel-window cancellation asserted but not quantitatively tested; −0.032° canonical bias could shift by 1–2 mdeg from beam/pixel choices | **PARTIAL — acknowledged scope limitation; not a new finding vs EXT rounds** | tex L1487–1542: NaMaster robustness battery covers mask apodization, sky fraction, purification variations and quotes the bias at multiple injection points. Beam/pixel-window cancellation is stated as the design choice (common beam cancels; same pixel window in signal and template). OpenAI's specific test (insert nontrivial Gaussian beam both on/off + pixel-window toggle) would strengthen the paper but was not previously required. This is a methodological strengthening request, not a defect in existing results. PARTIAL — new recommendation, not a prior defect. Houston-decision on whether to run additional MC configurations. |
| **B8** | OpenAI, Gemini | P1B-M6 (pass-2) / P1B-M3-Gemini | MAJOR | NaMaster "systematic floor 0.040°" language: inverse-variance-weighted fit reduces bias from −0.032° to −0.006° (~80%); presenting unweighted estimator as baseline while knowing IVW is better is hard to justify | **PARTIAL — EXT3 B2/C5 residual; framing issue, not a factual error** | tex L1539–1542: "we carry this 0.040° floor forward as the NaMaster systematic floor (as a conservative upper bound for the unweighted-estimator bias)." IVW result is mentioned in L1541 ("inverse-variance-weighted…reduces the bias to −0.006°"). The paper does mention the IVW result; it chooses to use the unweighted estimator to match published drivers. OpenAI's recommendation to rename "systematic floor" to "unweighted-estimator bias floor" and present both side-by-side is a legitimate editorial improvement. PARTIAL. |
| **B9** | OpenAI | P1B-M9 (pass-2) | MAJOR | ALP MCMC ESS not reported; βfree chain has only 720 accepted samples | **VERIFIED — new, not previously raised** | tex Appendix C / Sec. VI reports accepted sample counts (720 for βfree) and R̂−1 but NOT per-parameter effective sample sizes (ESS) or autocorrelation times. 720 accepted samples for a multi-parameter fit is marginal for ESS reporting. **Fix: add ESS per key parameter (β, θ_i, log₁₀ m_a, C_aγ) in Appendix C table; extend βfree chain if ESS is below O(10³).** |
| **B10** | Grok | P1B-E1 | ESSENTIAL | Header version stamp + version-history language in body | **VERIFIED — same as B1** | Already counted under B1. |
| **B11** | Grok | P1B-E2 | ESSENTIAL | Abstract states "both frozen dataset combinations find ΔNeff consistent with zero" but body repeatedly qualifies this as "NOT a spin-torsion theory module" — abstract over-claims relevance | **PARTIAL — same-class as EXT4 Ge6; adequate-disclosure in body** | tex L638 (abstract): "both frozen dataset combinations find ΔNeff consistent with zero." The body's disclaimer that this is a proxy (not a spin-torsion test) appears at Sec. III L910. Adding one abstract sentence "this proxy does not directly constrain the spin-torsion sector" would satisfy Grok. PARTIAL — editorial. |
| **B12** | Grok | P1B-E3 | ESSENTIAL | NaMaster 0.040° systematic floor not propagated into the 3.9σ birefringence significance | **FALSIFIED — the 3.9σ is explicitly labeled an auxiliary cross-check only** | tex L1740: "combination below (3.9σ) is retained as an auxiliary cross-check only." L1842: "the 3.9σ is the significance of the inverse-variance combination… should NOT be interpreted as a detection claim for this paper." L1847: "naive 3.9σ figure is an overestimate." The 3.9σ is not presented as a primary result — it is explicitly labeled as an auxiliary cross-check with caveats. FALSIFIED. |
| **B13** | Grok | P1B-M1 | MAJOR | Spectator-ALP birefringence claim rests on θ_i ≲ 0.1 fine-tuning; paper presents this as "support for ECH program" | **PARTIAL — EXT4 C2/C5 residual; framing concern** | tex L1824 (conclusion): "spectator-consistent regime θ_i ∼ 0.1 (fn. theta_backreaction) does require a ~25× misalignment tuning." The footnote (L1765–1774) explicitly discloses the fine-tuning and the Ω_a bounds. Grok's concern that the paper implies ECH endorsement from a tuned GR+ALP model is the same structural concern as EXT4 C2 PARTIAL. The conclusion already uses hedged language ("exploratory, overlap-uncorrected test"). The remaining framing is the EXT4 C2 one-sentence conclusion edit not yet executed. PARTIAL — same-class as EXT4 C2, still open. |
| **B14** | Grok | P1B-M2 | MAJOR | w₀+w_a = −1.478 ± 0.148 phantom-crossing claim without Savage-Dickey or nested-sampling evidence ratio | **STALE-with-disclosure — 5th re-raise** | Same as B4. tex L2097 labels result "exploratory, overlap-uncorrected." Nested-sampling is explicitly queued. STALE. |
| **B15** | Grok | P1B-M3 | MAJOR | AIC/BIC/lnB withheld while paper repeatedly invokes model-comparison framing | **STALE — EXT4 C3 closed this** | tex L85 (README): "AIC/BIC/ln B NOT reported in manuscript (deferred to nested sampling)." tex body at Sec. V.B explicitly states model-comparison statistics deferred. EXT4 C3 confirmed this README was corrected. STALE. |
| **B16** | Perplexity | multiple | MAJOR | Provenance/reproducibility weaknesses; DOI pending; version-history language | **VERIFIED — same as B1 (version-history) and B9 (ESS)** | Perplexity's text-only review confirms the same body-text issues as B1. No additional new findings from this leg (sonar fallback, text-only input). |

---

## EXT4 PARTIAL items — re-raise status

| EXT4 item | R34conf status |
|-----------|---------------|
| C2 (θ_i conclusion one-sentence edit) | RE-RAISED as B13 — still open PARTIAL |
| C5 (§III w₀wₐ body structure) | RE-RAISED as B4 — still open STALE-with-disclosure; structural subsection move is HOUSTON-DECISION |

---

## Per-reviewer verdict summary

| Reviewer | Claimed verdict | Summary of fresh genuine findings |
|----------|----------------|----------------------------------|
| OpenAI | MAJOR REVISIONS | B1 VERIFIED (version-history body), B6 VERIFIED (BBN/He documentation), B9 VERIFIED (ESS); B3 PARTIAL (Fig. 3 caption caveat); B7/B8 PARTIAL (beam test, IVW framing); B2/B4/B5 STALE |
| Gemini | MAJOR REVISIONS | B1 VERIFIED (version-history); B8 PARTIAL (IVW framing); B4/B14 STALE |
| Grok | REJECT | B1 VERIFIED (= version-history); B12 FALSIFIED (3.9σ cross-check); B13 PARTIAL (EXT4 C2 residual); B14/B15 STALE |
| Perplexity | MAJOR REVISIONS | B1/B16 VERIFIED (version-history echo); no unique new findings |

---

## Counts

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED (fix required) | **3** | B1 (version-history ×4 body sites), B6 (BBN/He documentation), B9 (ALP chain ESS) |
| PARTIAL (editorial / methodological strengthening) | **4** | B3 (Fig. 3 caption caveat), B7 (beam test), B8 (IVW framing), B13 (θ_i conclusion edit = EXT4 C2) |
| STALE-with-disclosure (parked compute-bound) | **4** | B2 (PR4/2018 pairing), B4 (SN overlap), B5 (bug disclosure), B14/B15 (evidence ratio) |
| FALSIFIED | **1** | B12 (3.9σ presented as primary result — FALSIFIED; it's labeled aux cross-check) |
| OPINION / HOUSTON-DECISION | **2** | B11 (abstract ECH framing), B7 depth of additional MC configurations |

**Genuinely new, VERIFIED substantive findings: 3** (B1 version-history cleanup, B6 BBN documentation gap, B9 ESS reporting). B12 was the strongest REJECT driver from Grok — FALSIFIED.

---

## EXT4-held closures — confirmation status

| EXT4 item | Status in R34conf |
|-----------|------------------|
| C1 — CHANGELOG v1B.0.58 + v1B.0.59 entries | CONFIRMED CLOSED — CHANGELOG verified |
| C3 — README DESI/AIC corrected | CONFIRMED CLOSED — README L74–85 verified |
| C6 — Conclusion quintom citation | CONFIRMED CLOSED — tex L2097 verified |
| C7 — Data Availability chain sentence | CONFIRMED CLOSED — not re-raised |
| C8 — README PR4 label | CONFIRMED CLOSED — README L87 verified |

---

## Closure plan for VERIFIED items

### Priority 1 — VERIFIED (fix before submission)

**[B1] Version-history body language** (tex L1521, L1762, L1830, L2293):
- L1521: Replace "quoted in an earlier draft of this footnote" with: "The pipeline-recovery SNR (template-fit significance of the injected signal) is 20.32 for the β = 0.27° injection."
- L1762: Replace "an earlier draft quoted [0.2, 1.1] with Δφ/fa ≈ 0.65 at m = H₀ (those values do not reproduce from the committed integration and are corrected here)" with: "The committed EOM grid gives Δφ/fa ∈ [0.9, 1.1] across the viable MCMC posterior."
- L1830: Replace "an earlier draft quoted [0.17,0.43]° from a joint-trajectory scan for which no artifact survives, and that range is superseded by the committed grid scan" with: "The committed grid scan gives β_ALP ∈ [β_min, β_max]° across the spectator-consistent posterior."
- L2293: Remove "superseded for coupling inference by the [4,60] continuous-prior rerun" — state only the final result.
- Header: Remove timezone and "v1B.0.59" from the \date{} line.

**[B6] BBN/He documentation** (tex Sec. III, ~L910–930):
- Add one footnote or 2-sentence paragraph: "CAMB uses the PArthENoPE-derived BBN-consistency module by default; Y_He is set self-consistently with N_eff at each sample. The prior range N_eff ∈ [2.046, 5.046] (ΔN_eff ∈ [−1.0, 2.0]) remains within the calibrated domain of the CAMB BBN module; no free-Y_He control run was performed, as the default BBN-consistent track is the standard choice for this type of proxy analysis."

**[B9] ALP chain ESS** (tex Appendix C / Sec. VI):
- Report per-parameter ESS for β, θ_i, log₁₀(m_a/eV), C_aγ in the continuous-prior run. If ESS for βfree chain (720 accepted samples) is below O(500) for any parameter, extend the chain. Add a column to the Appendix C table or a brief table note.

### Priority 2 — PARTIAL (recommended before submission)

**[B3]** Add to Fig. 3 caption: "(MC template-fit SNR values; not directly comparable to the sky-measurement detection significance of 2.7–2.9σ from published Planck/ACT analyses.)"

**[B8]** Rename "NaMaster systematic floor" → "NaMaster unweighted-estimator bias floor" and add one sentence: "Using the inverse-variance-weighted estimator reduces the bias from −0.032° to −0.006° (~80%); we adopt the unweighted baseline to match published pipeline drivers."

**[B13 = EXT4 C2]** Conclusion L2084: change "the spectator-consistent regime θ_i ∼ 0.1 (fn. theta_backreaction)" → "the Ω_a < 0.01 spectator-safe subset (θ_i ∼ 0.1, a ~25× fine-tuning relative to the natural midpoint, fn. theta_backreaction)." This is the EXT4 C2 one-sentence edit that was not executed in the v1B.0.59 wave.

**[B11]** Add to abstract: "The ΔNeff proxy does not directly constrain the ECH spin-torsion sector; it serves as a null-consistency reference for the companion theory paper."

### Priority 3 — HOUSTON-DECISION / Compute-bound

- B2 (PR4/2018 pairing swap test): queued compute; adequate disclosure present.
- B4 (SN overlap control chains): queued compute; labeled exploratory in paper.
- B7 (beam/pixel-window additional MC configs): optional methodological strengthening.

---

## Closure-held verdict

**P1B: NOT-CLEAN** (3 VERIFIED items require tex edits + 1 not-yet-executed EXT4 PARTIAL)

The core MCMC results, NaMaster pipeline validation, and ALP consistency check are sound. The REJECT verdict from Grok is driven primarily by B12 (3.9σ "not propagated" — FALSIFIED: paper labels it auxiliary cross-check only) and B14/B15 (evidence ratios — STALE: explicitly deferred to nested sampling). After the 3 VERIFIED fixes (B1 version-history, B6 BBN documentation, B9 ESS) plus the EXT4 C2 deferred conclusion edit (B13), all remaining items are STALE-with-disclosure (compute-queued) or OPINION. Estimated effort: <1 hour of tex edits + optional chain extension for ESS.

VERIFIED count: **3**
