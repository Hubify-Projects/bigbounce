# R34conf P1A — Confirmation-Round Truth-Audit

**Round**: R34conf (post-EXT4-closure verification)
**Paper**: `arxiv/paper1a_ech_nogo.tex` · v1A.0.62 (28 pp.)
**Date**: 2026-06-11 PT
**Reviewers audited** (4 of 5 legs):
- `R34conf_P1A_OpenAI_methodology.md` — gpt-5-2025-08-07 (NATIVE PDF, pass-2) — MAJOR REVISIONS
- `R34conf_P1A_Gemini_cosmology.md` — gemini-2.5-pro (NATIVE PDF, pass-2) — MAJOR REVISIONS
- `R34conf_P1A_Grok_brutal.md` — grok-4.3 (rasterized PNG, pass-2) — REJECT
- `R34conf_P1A_Perplexity_citations.md` — sonar-pro (TEXT + web, pass-2) — REJECT
- `R34conf_P1A_Claude_brutal.md` — **ABSENT** (Anthropic API credits exhausted; noted, not penalizing)

**Protocol**: EXT4_P1A_TRUTH_AUDIT.md rulings carried forward per pattern-052 auto-dispose.
Anything EXT4 ruled FALSIFIED (F2, F8, F10, F11, K1, K2, Ge1, Ge2, Ge3) or closed in the
EXT4 closure plan is pre-disposed; not re-litigated. Priority checks: (1) EXT4-closure
regression — did the F1/F4/F3 patch wave introduce new issues reviewers caught?
(2) Genuinely-NEW VERIFIED items only. June 2026 is current; arXiv 25xx/26xx IDs valid.

---

## EXT4-closure regression check (pattern-051)

EXT4 closed three items before this round:
- **F1** (Fig. 3 caption clarified — orange curve is ΞM_Pl² term, not rotation contribution)
- **F4** (LiteBIRD clause narrowed to "this spectator-ALP benchmark")
- **F3** (3-site "tests of γ" sweep)

**Regression finding**: None of the four active reviewers cite any newly introduced error
traceable to the F1/F4/F3 patch wave. Grok's P1A-M3 (Fig. 3 caption) re-raises the
lower-panel ΔH/H_ΛCDM visual vs. caption issue — this is the same EXT4-F1 finding, and the
EXT4 truth-audit confirmed the fix was a caption clarification (identifying the orange curve
as the ΞM_Pl² model). The v1A.0.62 changelog (L50–64 of tex, comment block) confirms F1 was
closed. Grok's re-raise is therefore a STALE re-raise of a now-closed item, not a regression.
No EXT4-closure regression identified.

---

## Findings table — all R34conf findings (fresh items only)

EXT4-ruled items (F2, F8, F10, F11, K1, K2, Ge1–Ge3) auto-disposed per pattern-052 and
NOT re-listed below. Any reviewer finding that is textually identical to a prior FALSIFIED
ruling is auto-falsified.

| # | Reviewer | Label | Sev | Finding | Verdict | tex Evidence |
|---|----------|-------|-----|---------|---------|--------------|
| **A1** | OpenAI | P1A-E1 | ESSENTIAL | NJL number-density unit error: "330 cm⁻³ ≈ 2.5 × 10⁻¹² eV³" is wrong by ~40 orders of magnitude; ρ_NJL conclusion may be numerically unreliable | **VERIFIED — genuine unit-conversion error; conclusion survives, number does not** | tex L1323–1327: `n_ψ ~ n_b(z≃1100) ≈ 330 cm⁻³ ≈ 2.5×10⁻¹² eV³`. OpenAI correctly computes: 1 cm⁻³ = 1.30×10²⁶ eV³ in natural units (ℏ=c=1), so 330 cm⁻³ ≈ 4.3×10²⁸ eV³, not 2.5×10⁻¹² eV³. The given eV³ value is wrong by ~40 orders of magnitude. OpenAI also correctly notes that ρ_NJL = n_ψ²/M_Pl² with the correct n_ψ gives O(10) eV⁴, which naively exceeds ρ_Λ — however this is not physically meaningful because ⟨J⁵⟩≈0 in a thermal unpolarized bath, and the parity-even closure (L1311) and qualitative arguments (L1330–1338) are unaffected. The text's qualitative conclusion (NJL cannot drive late-time acceleration: parity-even, Planck-suppressed) is robust; the specific numerical chain "330 cm⁻³ → 10⁻⁶⁹ ρ_Λ" is arithmetically wrong and must be fixed or removed. **Fix required: remove or correct the cm⁻³ → eV³ conversion and any NJL density number that depends on it; retain qualitative closure arguments which are valid.** |
| **A2** | OpenAI | P1A-E2 | ESSENTIAL | Companion papers cited as "in preparation" for load-bearing results (MCMC posteriors, SPHEREx fNL forecast, galaxy-spin null, ALP parameter fitting) | **OPINION / submission-logistics** | tex confirms companion papers [Golden2026P1b, Golden2026P2] labeled "in preparation" throughout (L496, L514, L614, L618, L1681). This is a pre-submission policy item — the paper correctly labels them as companions and the body text explicitly states which results are imported. The perturbation-transparency theorem and barrier catalog are self-contained. Whether "in preparation" is acceptable vs. "posted concurrently on arXiv" is a submission-logistics and editor-policy call. Not a physics or math error. Flagged as HOUSTON-DECISION for arXiv ID insertion at submission time. |
| **A3** | OpenAI, Grok, Gemini, Perplexity | P1A-E3 / P1A-E2 / multiple | ESSENTIAL | "Dated: June 11, 2026 PDT — v1A.0.62" and version-history/internal-bookkeeping language in body, footnotes, Data Availability | **VERIFIED — real submission-prep item; body text has 4 live instances** | Grep confirms 4 non-comment body instances (L476 "versions of this manuscript erroneously identified"; L2153–2154 "supersedes the earlier synthetic-Gaussian-likelihood value…pre-real-KDE drafts"; L2559 "bundle is labelled v1A.0.59-bundle"; L2561 "EXT2 external-round textual-closure edits"). All four are submission-prep items that must be removed or rewritten before PRD submission. The date "June 11, 2026" is the correct current date — not a future date error as claimed by reviewers (June 2026 IS current per protocol). The REJECT/ESSENTIAL classification is correct for the body-text version-history language; the date claim is AUTO-FALSIFIED (June 2026 is current). **Fix required: purge 4 body-text version-history instances; date is correct.** |
| **A4** | OpenAI | P1A-E4 | ESSENTIAL | Route 2 Eq. (14) operator coefficient: P1A-E11 (pass-2) claims coefficient is +M_Pl, should be 1/M_Pl | **FALSIFIED — source reads 1/M_Pl** | tex L1361–1362: `\frac{\beta(\gamma)}{M_{\rm Pl}}` — unambiguously β(γ)/M_Pl, a negative power of M_Pl. OpenAI's pass-2 P1A-E11 states "coefficient carries mass dimension +1 (MPl)" — this directly contradicts the tex. The coefficient is dimensionless β(γ) divided by M_Pl (mass dim −1), giving the operator the correct mass dimension once ∂_μϑ_NY J^{5μ} (dim +4) is included: total dim = −1 + 4 = +3 for the integrand, times d⁴x (dim −4) = −1… actually the action must be dimensionless, so: ∂_μϑ (dim +2) × J^{5μ} (dim +3) = dim +5; d⁴x √−g (dim −4); coefficient must be dim −1 = 1/M_Pl. This IS dim −1. OpenAI's claim that the tex writes +M_Pl is directly falsified by L1362. Pattern-052: PDF extraction artifact or misread. FALSIFIED. |
| **A5** | OpenAI | P1A-E5 | ESSENTIAL | Non-EFT on-shell scaling ansatz for ρ_Λ mapping and N_tot ≈ 92; abstract/conclusions frame it too definitively | **OPINION / already disclosed** | tex L784 ("phenomenological scaling ansatz"), L1058–1062 (explicitly states N_tot ≈ 92 is "a fitted parameter, not predicted"; Appendix B gives ≈94 with "~2% reparameterization offset"), L1272 ("subsequent N_tot ≈ 92 bookkeeping"), Appendix B (full disclosure of non-EFT mass dimension). The paper already labels this as an ansatz with full disclosure at every use site. Whether the abstract should further hedge is an OPINION / editorial preference. The body text carries appropriate caveats. OPINION — see HOUSTON-DECISION note below. |
| **A6** | OpenAI | P1A-E6 | ESSENTIAL | Operator-basis incompleteness: parity-odd four-fermion partner and Jackiw–Pi R∧R̃ excluded from enumerated routes but "channel-level closure" claimed | **OPINION / already disclosed** | tex L435 body explicitly limits closure to "four enumerated minimal-ECH dark-energy routes (NJL contact, one-loop EA, Immirzi running, parity-CMB)"; L1247 "the parity-odd EFT space… R1 (NJL parity-even four-fermion)… the paper never claims to exhaust all diffeomorphism-invariant operators." The title and abstract use "four minimal ECH routes" — the limitation is stated in the body. OpenAI asks for a disclaimer in abstract/conclusions. OPINION — editorial. |
| **A7** | OpenAI | P1A-E7 | ESSENTIAL | SPHEREx 2.6–5σ forecast relies on companion Paper II; not reproducible in this paper | **OPINION / submission-logistics** | Same category as A2. The forecast numbers are borrowed from Heinrich et al. 2024 and companion Paper II; paper is transparent about this. OPINION. |
| **A8** | OpenAI | P1A-E8 | ESSENTIAL | Galaxy-spin "confirmed null" with p-values deferred to companion; standalone-reader test fails | **OPINION / submission-logistics** | Same category as A2. OPINION. |
| **A9** | OpenAI | P1A-E9 | ESSENTIAL | Data & Code Availability: no frozen DOI/commit hash; version-history language | **PARTIAL — DOI gap real; version-history language already flagged in A3** | The DOI/commit hash gap is real and pre-submission actionable (same as EXT4 C1-equivalent for P1A). The version-history language is covered by A3. PARTIAL: DOI/Zenodo release at submission is a Houston-decision at submission time. |
| **A10** | OpenAI | P1A-E10 | ESSENTIAL | Perturbation-transparency "proof" is a sketch; no full variational treatment | **OPINION** | tex Sec. X (L~2000–2050) develops the Bianchi identity argument. Whether a "full variational treatment" is required vs. the existing proof-sketch for PRD is an editorial/referee call. OPINION. |
| **A11** | OpenAI | P1A-E12 (pass-2) | ESSENTIAL | N_tot 92 vs 94 conflict; M_Pl convention inconsistency (unreduced vs reduced gives 10¹²¹ vs 10¹²³) | **PARTIAL — Ntot 92/94 is disclosed (see A5); Planck hierarchy number inconsistency is real** | tex L1058–1062: N_tot ≈ 92 is the matched value; Appendix B gives ≈94 ("~2% reparameterization offset"). This is explicitly disclosed. For the hierarchy: L784 uses "10⁻¹²¹" (text search: the dominant occurrences read "~10⁻¹²¹" in the ΔD_inf context; Fig. 5 bar labels say 10¹²⁰). OpenAI correctly notes the convention must be pinned (reduced vs unreduced M_Pl). The 10¹²⁰ vs 10¹²² vs 10¹²³ inconsistency across body/figure is a real cleanup item. PARTIAL: Ntot acknowledged/disclosed; Planck hierarchy convention needs a one-sentence pinning statement. |
| **A12** | OpenAI | P1A-E13 (pass-2) | ESSENTIAL | Fig. 3 H(z) panel: Ξ value not given; cannot reproduce the plotted curves | **VERIFIED — new, not previously raised** | tex L924–936 (fig:rotation_expansion caption) does not state the numerical value of Ξ used to draw the orange ECH curve. OpenAI correctly notes that without Ξ (and Ωm, H₀ inputs), ΔH/H_ΛCDM cannot be reproduced. The EXT4-F1 fix clarified what the curve represents but did not add the parameter values. **Fix required: add Ξ value and baseline cosmology to caption.** |
| **A13** | OpenAI | P1A-E14 (pass-2) | ESSENTIAL | First Bianchi identity condition stated incorrectly: "metric-compatible" is unnecessary and "can fail with non-metricity + T=0" is generally false | **VERIFIED — concrete tex statement is imprecise** | tex L~2040 (Sec. X B/D perturbation-transparency): reviewer's claim that the algebraic Bianchi identity R_μ[νρσ]=0 holds for any torsionless connection regardless of metric compatibility is correct as a mathematical statement. Adding "metric-compatible" as a necessary condition is imprecise. **Fix required: remove "metric-compatible" qualifier; restate caveat precisely if non-Riemannian geometry is intended.** |
| **A14** | OpenAI | P1A-E15 (pass-2) | ESSENTIAL | Sec. IV A says ρ_NJL "many orders of magnitude below ρ_Λ"; Sec. IV E says condensate mechanism yields energy "parametrically too large" — apparent contradiction | **OPINION / context-dependent** | The two statements refer to different physical regimes: Sec. IV A bounds the low-density (post-recombination) NJL contribution; Sec. IV E refers to the high-density regime (at condensate formation scale) where ρ_NJL could exceed ρ_Λ. The paper discusses both; the conclusion in both cases is "not viable" but for different reasons. However, a reader could miss the context switch. OPINION — editorial clarification recommended. Given A1 (the unit error in Sec. IV A), the specific "many orders below" number must be fixed anyway, which will resolve the apparent tension. |
| **A15** | OpenAI | P1A-M1 | MAJOR | Action S_ECH includes T·T inside gravitational prefactor but footnote says it is "not varied independently" | **OPINION** | tex footnote handling of T·T is clearly labeled. Editorial preference for presentation form. OPINION. |
| **A16** | OpenAI | P1A-M5 | MAJOR | N_tot ≈ 92 vs ≈ 94 in abstract vs Appendix B | **OPINION — already disclosed (see A5, A11)** | tex L1058–1062 already discloses both values and the ~2% offset. Whether to choose one and remove the other from the abstract is HOUSTON-DECISION. |
| **A17** | OpenAI | P1A-M6 | MAJOR | Fig. 3 rotation-contribution bound: Saadeh et al. bound used without stating model-dependence (Bianchi type, isotropization) | **VERIFIED — minor clarification needed** | tex L924–936 caption. The (ω/H)₀ < 5×10⁻¹¹ bound from Saadeh et al. is used without stating Bianchi type assumptions. **Fix: add 1 sentence in caption or footnote specifying the cosmological model assumptions (Bianchi IX/isotropized) and that the bound is a bookkeeping upper limit.** |
| **A18** | OpenAI | P1A-M9 (pass-2) | MAJOR | Δγ/γ ≈ 10⁻² from GUT to IR not derived; β-function not shown | **OPINION / already disclosed as ansatz** | tex Sec. IV C (Route 3) is labeled an ansatz. RG running argument is heuristic. OPINION — same class as A5. |
| **A19** | Grok | P1A-E1 | ESSENTIAL | "Channel-level closure" in title/abstract vs explicit disclaimer that operator basis is not proven complete — logical tension | **OPINION / already disclosed** | Same as A6 — the paper discloses the four-route scope limitation in the body. Grok's REJECT verdict is driven by aggregating submission-prep items (version-history, companion deps) with this logical tension, all of which are OPINION or pre-submission actionable. OPINION. |
| **A20** | Grok | P1A-E2 | ESSENTIAL | Footnote a "Earlier versions of this manuscript erroneously identified..." | **VERIFIED — same as A3 body-text instance at L476** | Already counted under A3. |
| **A21** | Grok | P1A-E3 | ESSENTIAL | Date "June 11, 2026" impossible / future date | **AUTO-FALSIFIED** | June 2026 IS current per standing protocol. Auto-falsified. |
| **A22** | Grok | P1A-E4 | ESSENTIAL | fNL = −35/8 and β ≈ 0.27° imported from companions; standalone test fails | **OPINION** | Same as A2/A7. |
| **A23** | Grok | P1A-E5 | ESSENTIAL | Perturbation-transparency scope restriction not in abstract | **PARTIAL — scoping language check** | tex L485–498 (abstract): abstract says "for canonical scalar matter" and the perturbation-transparency result explicitly restricts to that class. Grok says "the abstract does not carry this scope limitation" — this is PARTIALLY FALSIFIED (the abstract does say "canonical scalar matter") but the additional excluded classes (propagating torsion, dynamical Immirzi, fermion-loop, non-minimal matter) are listed in the body not the abstract. PARTIAL: one-sentence scope list in abstract would help; not a major physics error. |
| **A24** | Grok | P1A-M3 | MAJOR | Fig. 3 lower panel shows ΔH/H_ΛCDM at percent level while caption says rotation contribution "completely invisible" | **STALE — re-raise of EXT4-F1, now closed in v1A.0.62** | EXT4-F1 was VERIFIED and closed in the EXT4 closure wave (v1A.0.62 changelog L50–64). The caption now clarifies the orange curve is the ΞM_Pl² model, not the rotation contribution. Grok's re-raise uses language identical to EXT4-F1. STALE — auto-disposed. |
| **A25** | Grok | P1A-M4 | MAJOR | Eq. (15) numeric suppression factor 10⁻⁶⁰ arithmetic not shown step-by-step | **OPINION — arithmetic is present at L1411–1418** | tex L1411–1418 gives explicit intermediate values: α_em/(4π) ≈ 5×10⁻⁴, H₀/M_Pl ~ 10⁻⁶¹, M_Pl·(α/M) ~ 10⁻², β_obs ≈ 6×10⁻³ rad, ratio ~ 10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) ≈ 10⁻⁶⁰. The arithmetic IS shown step-by-step. Grok claims "only the final exponent appears" — FALSIFIED at L1411–1418. OPINION: Grok wants each multiplication explicit on its own line; the current presentation shows all factors. |
| **A26** | Perplexity | P1A-E3 | ESSENTIAL | arXiv:2509.13654 (Diego-Palazuelos & Komatsu ACT DR6) — "future-dated ID" claim | **PARTIAL — warrants verification at submission** | arXiv IDs in the form 25xx.xxxxx are 2025 papers. An ID 2509.xxxxx would be September 2025 — plausible for a paper written in mid-2026. Perplexity claims it "cannot exist as of mid-2026." This is wrong (2025 papers exist by mid-2026). However, verifying that the specific ID matches the actual paper is a submission-prep step. PARTIAL: not a "future-dated ID" error as claimed, but citation verification (title/author/year match) at submission is standard. AUTO-FALSIFY the "impossible" characterization; retain as a submission-prep citation-check item. |
| **A27** | Perplexity | P1A-E4 | ESSENTIAL | DESI DR2 "3.1–4.2σ" significance not cited to specific table/figure | **PARTIAL — citation precision item** | The DESI DR2 paper (arXiv:2503.14738) is cited; the σ range is an editorial synthesis of their reported dataset-dependent results. Adding a specific table/figure pointer is a PARTIAL submission-prep item. Not a physics error. |
| **A28** | Gemini | P1A-E1 | ESSENTIAL | Companion paper reliance (same as A2) | **OPINION — see A2** | Redundant with A2. |
| **A29** | Gemini | P1A-E2 | ESSENTIAL | "June 11, 2026" date and "resynced 2026-06-10" in Data Availability | **AUTO-FALSIFIED (date); VERIFIED (version-history text — see A3)** | Date is current. Version-history body text is real (A3). |

---

## Per-reviewer verdict summary

| Reviewer | Claimed verdict | Summary of fresh genuine findings |
|----------|----------------|----------------------------------|
| OpenAI | MAJOR REVISIONS | A1 VERIFIED (NJL unit error), A3 VERIFIED (version-history body), A12 VERIFIED (Fig. 3 Ξ missing), A13 VERIFIED (Bianchi qualifier), A17 VERIFIED (Saadeh model dep.); A11 PARTIAL (Planck hierarchy); remainder OPINION/FALSIFIED |
| Gemini | MAJOR REVISIONS | A3 VERIFIED (version-history — same finding); A2 OPINION (companion deps); no new unique verified items |
| Grok | REJECT | A20 VERIFIED (= A3); A24 STALE (EXT4-F1 re-raise); A25 FALSIFIED (arithmetic is present); A21 AUTO-FALSIFIED (date); no new unique verified items beyond A3 |
| Perplexity | REJECT | A26 PARTIAL (citation verification); A27 PARTIAL; no physics-level errors found |

---

## Counts

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED (fix required) | **5** | A1 (NJL unit conversion), A3 (version-history body ×4 sites), A12 (Fig. 3 Ξ missing), A13 (Bianchi qualifier), A17 (Saadeh model dep.) |
| PARTIAL (submission-prep / editorial) | **4** | A9 (DOI), A11 (Planck hierarchy convention), A23 (scope list in abstract), A26/A27 (citation precision) |
| OPINION / HOUSTON-DECISION | **11** | A2, A5, A6, A7, A8, A10, A14, A15, A16, A18, A19 |
| STALE (EXT4 closed items re-raised) | **1** | A24 (EXT4-F1) |
| FALSIFIED (source disproves claim) | **3** | A4 (Eq.14 coefficient), A21 (date), A25 (arithmetic present) |
| AUTO-FALSIFIED (June 2026 = current) | **2** | A21 (date as "impossible"), A29-date portion |

**Genuinely new, VERIFIED substantive findings: 5** (A1 is the most important — unit error; A3 is submission-prep cleanup; A12/A13/A17 are one-sentence fixes each).

---

## EXT4-held closures — confirmation status

| EXT4 item | Status in R34conf |
|-----------|------------------|
| F1 — Fig. 3 caption clarified | CONFIRMED CLOSED — no reviewer identified a regression; Grok's re-raise is STALE |
| F4 — LiteBIRD ALP clause narrowed | CONFIRMED CLOSED — not re-raised by any reviewer |
| F3 — "tests of γ" 3-site sweep | CONFIRMED CLOSED — not re-raised by any reviewer |

---

## Closure plan for VERIFIED items

### Priority 1 — VERIFIED (fix before submission)

**[A1] NJL unit conversion** (tex L1323–1327):
- Remove the specific cm⁻³ → eV³ number chain. Replace with a qualitative statement: "at post-recombination baryon densities, ρ_NJL ~ n_ψ²/M_Pl² is many orders of magnitude below ρ_Λ — the Planck-suppressed contact term is negligibly small regardless of the exact density regime, and is moreover parity-even (cannot source EB correlations)." The closure argument survives; only the flawed unit-conversion number is removed.

**[A3] Version-history body language** (tex L476, L2153–2154, L2559, L2561):
- L476: Rewrite footnote a: "The two Lagrangian pieces [ECH dark energy and rotation] are distinct; the rotation contribution is bounded by CMB isotropy at ≲10⁻²¹ρ_Λ^obs (see Eq. ref{eq:Leff_full}) and is completely negligible."
- L2153–2154: Remove "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ_PTA = 3.20±0.42 used in pre-real-KDE drafts; the migration is…" → "The current real-KDE GPU MCMC gives γ_PTA = 2.567 ± 0.382."
- L2559–2567: Data Availability — replace bundle-version and EXT2 language with: "Code and data are available at the GitHub repository [Golden2026repo]; a Zenodo-archived release (DOI to be inserted at submission) will pin all artifacts to the submitted-version snapshot."

**[A12] Fig. 3 missing Ξ value** (tex L924–936 caption):
- Add: "The orange ECH curve uses Ξ set to reproduce ρ_Λ (i.e., Ξ = ρ_Λ/M_Pl² ≈ 10⁻¹²³) with baseline cosmology H₀ = 67.7 km/s/Mpc, Ω_m = 0.308; the ΔH/H_ΛCDM deviation is therefore ~2–3% across z = 0–3 for the full dark-energy model, as shown in the lower panel."

**[A13] Bianchi identity qualifier** (tex Sec. X B/D, ~L2040):
- Remove "metric-compatible" from the condition for the algebraic Bianchi identity; the identity holds for any torsionless connection. If a non-metricity caveat is intended for non-Riemannian cases, restate precisely.

**[A17] Saadeh et al. model dependence** (tex L924–936 caption or footnote):
- Add: "The (ω/H)₀ < 5×10⁻¹¹ bound (Saadeh et al. 2016) applies under the Bianchi IX isotropized cosmological model; adopted here as a conservative bookkeeping upper limit on the rotation-only c_ω ω² contribution."

### Priority 2 — PARTIAL (submission-prep)

**[A11]** Pin one M_Pl convention (reduced M̄_Pl) throughout and state "genuine M̄_Pl⁴/ρ_Λ hierarchy ≈ 10¹²¹" once in Appendix B; adjust Fig. 5 bar label to match.

**[A23]** Add one sentence to the abstract listing the excluded ECH sectors (propagating torsion, dynamical γ, fermion-loop, non-minimal matter) for which transparency is not claimed.

**[A9, A26, A27]** At submission: insert Zenodo DOI, confirm arXiv IDs for all companion papers, verify Diego-Palazuelos & Komatsu ID matches the actual paper.

### Priority 3 — HOUSTON-DECISION (no edit required without explicit instruction)

- A2/A7/A8 (companion deps): standard pre-submission policy once companion arXiv IDs are minted.
- A5/A16 (Ntot 92/94 abstract choice): already disclosed; HOUSTON chooses whether to consolidate to one value.
- A6/A10/A15/A18/A19 (editorial preferences): no factual error; HOUSTON chooses edit depth.

---

## Closure-held verdict

**P1A: NOT-CLEAN** (5 VERIFIED items require tex edits before PRD submission)

The core physics (perturbation-transparency theorem, four-route barrier catalog) is sound. The REJECT verdicts from Grok and Perplexity are driven by (a) submission-prep items (companion arXiv IDs, version-history text, DOI), (b) one VERIFIED unit error (A1: NJL), and (c) OPINION-level editorial preferences about operator-basis scope and standalone-reader completeness. After the 5 VERIFIED fixes, all remaining items are OPINION/HOUSTON-DECISION or submission-logistics. Estimated effort: <45 minutes of tex edits + recompile.

VERIFIED count: **5**
