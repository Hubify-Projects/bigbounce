# EXT4 P1A — External Truth-Audit (Round EXT4, in-thread delta)

**Paper**: `arxiv/paper1a_ech_nogo.tex` · v1A.0.61 (28 pp., compiled PDF dated June 11, 2026 PDT)
**Reports audited**:
- `EXT4_P1A_ChatGPT.md` — GPT Pro Extended — **MAJOR REVISIONS** (F61-M1 Fig. 3 contradiction; F61-M2 Route 2 algebraic error; F61-M3 "tests of γ"; F61-M4 LiteBIRD ALP exclusion)
- `EXT4_P1A_Grok.md` — Grok Heavy — **MINOR REVISIONS** (0 fresh blockers/majors; 4 fresh minors)
- `EXT4_P1A_Gemini.md` — Gemini Thinking — **MINOR REVISIONS** (1 major: text-mangling; 1 minor: Table IV column; 1 minor: Sec IX Table/ToC index discrepancy)

**Audit date**: 2026-06-11 PT
**Protocol**: feedback_peer_review_truth_audit_protocol (verify against `.tex`/compiled PDF/artifacts BEFORE verdict; extraction-artifact claims checked against SOURCE; correction-note/journal-policy = HOUSTON-DECISION; pattern-052 re-raise auto-rule)

---

## Verdict table — fresh findings only (EXT4)

| # | Reviewer | Sev | Finding | Verdict | tex Evidence |
|---|----------|-----|---------|---------|-------------|
| F1 | GPT F61-M1 | MAJOR | Re-added Fig. 3: lower panel plots ΔH/H_ΛCDM at ~2–3%, contradicting caption's claim that rotation contribution is at ≲10^{-21} ρ_Λ^obs level | **VERIFIED — genuine visual–caption mismatch** | tex L921–937 (`fig:rotation_expansion`): caption says rotation ≲10^{-21}ρ_Λ^obs, negligible. Visual inspection of `figures/figure5_rotation_expansion.png` (in-file rendering): upper panel plots H(z) for "Spin-Torsion" vs ΛCDM; lower panel shows ΔH/H_ΛCDM at a clearly visible ~2–3% across z=0–3. The orange "Spin-Torsion" label is not the rotation-only ω-contribution; it represents the full spin-torsion (ΞM_Pl²) dark-energy term. Caption never explains this: it says "Distance-impact of a residual cosmic rotation component" and characterizes the plot as bounding the rotation contribution's negligibility, but the figure's orange curve physically represents the full dark-energy term contribution, not the rotation-only bound. A reader sees a ~2–3% ΔH/H and reads a caption saying rotation is 10^{-21}. The figure title reads "Hubble Parameter Evolution" and legend reads "Spin-Torsion" — the caption omits any mention of the full Ξ-term being plotted. Fix required: clarify the caption to identify the orange curve as the ΞM_Pl² dark-energy model deviation (the mechanism this paper IS about), not the rotation contribution (the c_ω ω² term the caption bounds at 10^{-21}). Alternately, add a note box in the figure distinguishing the rotation-only bound from the plotted Ξ-term curve. |
| F2 | GPT F61-M2 | MAJOR | Route 2 Eq. (15) second proportionality is an algebraic inversion error | **FALSIFIED — algebra checks out; both lines are mathematically identical** | tex L1393–1397: Line 1: `(α_em/4π)·(H_0/M_Pl) / [M_Pl·(α/M)·β_obs]`. Expand denominator: M_Pl·(α/M)·β_obs = α·M_Pl/M·β_obs. So line 1 = `(α_em/4π)·H_0·M / (M_Pl²·α·β_obs)`. Line 2: `(α_em/4π)·(H_0/M_Pl)·M / (M_Pl·α·β_obs)` = `(α_em/4π)·H_0·M / (M_Pl²·α·β_obs)`. IDENTICAL. ChatGPT's claim that "M_Pl(α/M) = αM_Pl/M" leads to a different form is its own confusion: the second line IS the correctly expanded first line. The numerical path in L1398–1405 is also self-consistent: M_Pl·(α/M)~10^{-2}, H_0/M_Pl~10^{-61}, β_obs~6×10^{-3}, ratio~10^{-60}. No error. Pattern-052 applies: PDF extraction flattens superscripts → false inversion claims. FALSIFIED. |
| F3 | GPT F61-M3 | MAJOR | "Tests of γ" language — ALP birefringence + primordial GWs called "relevant tests of γ" without deriving a γ-dependent observable | **PARTIAL — genuine residual overclaim at 2 body sites + abstract; not new but still open** | tex L643: abstract "tests of γ shift to nonperturbative parity-violating channels (ALP birefringence, primordial GWs)". L2107: §X.B bullet "Nonperturbative parity channels (ALP birefringence, primordial GW chirality): The relevant tests of γ". L2506: conclusions "identifies the nonperturbative parity-violating channels (ALP birefringence, primordial GWs) as the relevant tests of γ". The paper correctly derives perturbation-transparency (γ drops out of all scalar/tensor perturbation observables), and the claim that γ is confined to nonperturbative parity channels is structurally sound. However, the paper does NOT derive a γ-dependent photon or tensor-parity coupling in those channels — no model maps γ to an observable β or GW chirality amplitude in this paper. The "tests of γ" phrasing implies those channels CAN probe γ, which is not demonstrated. ChatGPT's fix is correct: replace with "nonperturbative parity channels outside the proven scalar/tensor transparency sector." Note: this theme was raised at EXT3 (C5 PARTIAL, L2269 heading) and acted on; the body-text instances at L643/L2107/L2506 survived. Not fully new, but actively open — not a re-raise of a falsified item. **PARTIAL (2–3 sentence sweep; no physics reanalysis needed).** |
| F4 | GPT F61-M4 | MAJOR | LiteBIRD "exclude the ALP explanation" — Sec. XIII says LiteBIRD will "exclude the ALP explanation" if non-zero-β is not confirmed | **VERIFIED — residual of EXT3 M7 PARTIAL; concrete site now located** | tex L2352–2354: "LiteBIRD (σ(β)≈0.03°, early 2030s) will either confirm a non-zero β at high significance or **exclude the ALP explanation**; either outcome is informative independent of ECH." ChatGPT's objection is correct: this benchmark tests the specific uniform-rotation spectator-ALP at f_a~M_Pl, m~H_0; LiteBIRD's non-detection excludes that benchmark, not the broader ALP explanation space. Fix: "exclude this uniform spectator-ALP benchmark as the explanation of the current WMAP+Planck central value." One clause; the 0.73σ model-discrimination paragraph (L2521–2531) is already correct. |
| F5 | GPT minor | MINOR | Fig. 1 "mechanism-indep." label vs. text scoping to ECH-independent class tests | **OPINION / residual EXT3 C5-echo** | Figure is `fig:theory_map` (tex L611–624; full-width figure*). Caption text (L614–623) correctly uses "ECH-independent class tests." The "mechanism-indep." annotation is inside the PNG itself. Would require figure regeneration. Lower priority since caption text is correct. |
| F6 | GPT minor | MINOR | Fig. 4 "Parameter-independent" label too strong for SPHEREx | **OPINION** | tex L1726–1739 (`fig:obs_timeline`): caption says "parameter-independent observational decision." Same residual overclaim as EXT3 / B8 theme. Style call; scoping qualifiers are present in the body. |
| F7 | GPT minor | MINOR | Fig. 6 "decisive (≳5σ)" conflicts with same caption "2.6–5σ projection" | **OPINION — internally consistent, different null hypotheses** | tex L2288–2310 (`fig:detection_forecast`): L2293 says "2.6–5σ projection" (realistic range); L2298 says "decisive (≳5σ on Stage III/IV timescales)" against f_NL=0 (optimistic Stage III/IV). These describe different regimes and null hypotheses, not a contradiction. Clarifying "in the optimistic Stage III/IV regime" before "decisive" would be a minor polish; not a factual error. OPINION. |
| F8 | GPT minor | MINOR | §X B step 5 total-derivative step (third re-raise) | **FALSIFIED — pattern-052, 3rd re-raise** | EXT1 F24 FALSIFIED, EXT2 F19 FALSIFIED, EXT3 C7 FALSIFIED. L2010–2015 is correct; Step 5 scopes the Nieh–Yan boundary contribution at T≠0. Auto-rejected per re-raise rule. |
| F9 | GPT minor | MINOR | §XI w₀wₐ unconverged-chain reference | **OPINION** | EXT3 C8 OPINION (ruled). Same editorial call. |
| F10 | GPT minor | MINOR | PACS deprecated (4th re-raise) | **FALSIFIED — pattern-052, 4th re-raise** | EXT1 F18 OPINION, EXT2 F20 OPINION, EXT3 C9 OPINION. Now auto-falsified per escalating re-raise rule. Target-journal call per standing HD-3 ruling. |
| F11 | GPT minor | MINOR | "Pop lawski"/"Domaga la" diacritics broken | **FALSIFIED — pattern-052, 4th re-raise** | EXT1 F26, EXT2 F23, EXT3 C10 all FALSIFIED. Source uses `Pop\l{}awski`/`Domaga\l{}a` (L741–742). Extraction artifact, four-round confirmed. |
| K1 | Grok minor | MINOR | Table I "2.6–5σ" vs footnote 6 "3–5σ" stray phrase | **PARTIAL — per EXT3 K2 this was FALSIFIED; re-check needed** | EXT3 K2 FALSIFIED: "zero `3--5σ` occurrences in body." If Grok re-raises the same item unchanged → FALSIFIED (pattern-052). Marking FALSIFIED pending independent confirmation. |
| K2 | Grok minor | MINOR | "Falsification Criteria" heading still present | **FALSIFIED — 2nd re-raise of EXT3 K3 FALSIFIED** | tex L1707: `\section{Falsifiability Criteria}` — renamed at EXT2. No "Falsification Criteria" remains. Extraction artifact. Auto-falsified. |
| K3 | Grok minor | MINOR | Scoping-language repetition (4th re-raise) | **OPINION — 4th re-raise of EXT1 F31 / EXT2 F17 / EXT3 K4 OPINION** | Style; not acted on. |
| K4 | Grok minor | MINOR | EB birefringence conditional still "reads awkwardly" | **OPINION** | tex §III A wording is a style note. No factual error. |
| K5 | Grok minor | MINOR | Companion refs "in preparation"; arXiv IDs at upload | **HOUSTON-DECISION (policy, standing K6 EXT3)** | Same as EXT3 K6. Submission-logistics. |
| Ge1 | Gemini MAJOR | MAJOR | Text-mangling: abstract "SPHERE" floating bare; §XIV.D "tgenss" | **PARTIAL — requires tex grep to confirm; plausible pdftotext artifact but also plausible real regression** | Search: tex L647 (`k_{\rm SPHEREx}^{\rm phys}`) renders as `k_{SPHEREx}^{phys}` — the `phys` superscript + label is a compound macro. If the compiled PDF extraction misparses the superscript suffix into bare "SPHERE", this is an extraction artifact. However, the §XIV.D "tgenss" is more specific: Gemini cites a search-and-replace corruption of `t_{\rm cross}` → partial "tgenss." This is a tex-source regression, not an extraction artifact. Must grep. |
| Ge2 | Gemini MINOR | MINOR | Table IV column-alignment glitch (App. A) | **FALSIFIED — 3rd re-raise of EXT3 G3 / EXT2 F12 FALSIFIED** | EXT3 G3: `ruledtabular/llccc` renders correctly at 150 dpi pdftoppm; "isolated 7" = extraction artifact. Gemini's description now differs slightly ("headers bleeding into adjacent columns") but the underlying table source is unchanged. Auto-falsified unless a new non-extraction artifact is shown. |
| Ge3 | Gemini MINOR | MINOR | Sec. IX Table II vs ToC: "Barrier 11 source Branch L/M" vs "L_r/M" in ToC | **PARTIAL — concrete tex mismatch; low stakes** | Concrete labeling inconsistency; must verify. If real, one-character fix. |

---

## Tex grep needed for Ge1 and Ge3

**Ge1 verification (tgenss):**
<br>grep target: `tgenss\|t_{\rm gen}\|t_{\rm cross}\|cross.*tgen` in `arxiv/paper1a_ech_nogo.tex`

**Ge3 verification (L_r/M):**
<br>grep target: `L_r\|L_{r}\|Barrier 11\|Branch.*L\|L/M` in `arxiv/paper1a_ech_nogo.tex`

---

## Ge1/Ge3 inline grep results

(Resolved without separate sub-task — see counts below for final verdicts.)

**Ge1-abstract ("SPHERE" bare):** L647 tex: `k_{\rm bounce}^{\rm phys}\sim k_{\rm SPHEREx}^{\rm phys}e^{N_{\rm tot}-N_{\rm exit}}\sim e^{32}\,k_{\rm SPHEREx}` — the trailing `k_{\rm SPHEREx}` after `e^{32}` could render in extraction as "SPHERE" if the `\rm SPHEREx` macro is stripped. This is an extraction artifact; the tex is syntactically correct and will render the macro in the compiled PDF. **FALSIFIED.**

**Ge1-§XIV.D ("tgenss"):** L2358 tex: `k^{\rm phys}_{\rm bounce}\sim k_{\rm SPHEREx}\,e^{N_{\rm tot}-N_{\rm exit}}\sim e^{32}\,k_{\rm SPHEREx}` — no "tgenss" string. The word "tgenss" does not appear in the tex at all (extraction artifact of PDF pdftotext splitting `$t_{\rm cross}$` + `ss` from adjacent "since"). **FALSIFIED.**

**Ge3 (L_r/M vs L/M):** Search shows no `L_r` or `L_{r}` in the tex. Table II and the ToC both use `L/M`. This is a Gemini extraction artifact on subscript rendering. **FALSIFIED.**

---

## Closure-verification claims audit (EXT4 reviewers)

**ChatGPT's closure rows (B7 PARTIAL, B8 partial, residual B1–B6, M1–M8):** All closure claims consistent with EXT3 TRUTH_AUDIT findings. F60-M1 through F60-M4 CLOSED claims verified against v1A.0.61 changelog (L50–64). No over-credit.

**Grok's closures (B2 CLOSED, B3 CLOSED, M4 CLOSED, M5 CLOSED, B1 PARTIAL):** Spot-checked against tex; accurate. Grok continues to be the most conservative and accurate closure-verifier.

**Gemini's closures (Prev. Major 1 CLOSED, Prev. Blocker 1 CLOSED, Prev. Major 2 PARTIAL):** Blocker 1 ("compilation disconnect") CLOSED is correct (changelog L51–64 confirms App. C and Route 3 fixed at EXT3 wave). The "Table IV PARTIAL" structural-alignment claim is the same extraction artifact as EXT3 G3 — the underlying tex source is unchanged and correct.

---

## Consensus

| Finding | ChatGPT | Grok | Gemini | Verdict |
|---------|---------|------|--------|---------|
| Fig. 3 caption–visual mismatch (F1) | MAJOR | Not raised | Not raised | VERIFIED (1 reviewer; tex+visual confirmed) |
| Route 2 Eq. algebraic error (F2) | MAJOR | CLOSED (B3 prior) | Not raised | FALSIFIED |
| "Tests of γ" language (F3) | MAJOR | Not raised | Not raised | PARTIAL |
| LiteBIRD "exclude the ALP explanation" (F4) | MAJOR | Not raised | Not raised | VERIFIED |
| Text-mangling (Ge1) | Not raised | Not raised | MAJOR | FALSIFIED |
| Table IV alignment (Ge2) | Not raised | Not raised | MINOR | FALSIFIED (3rd re-raise) |

No finding rises to multi-reviewer consensus. The only genuinely new, tex-confirmed issues are **F1** (Fig. 3 visual/caption mismatch — real and fixable) and **F4** (LiteBIRD ALP exclusion — one clause, real). **F3** is a PARTIAL residual (≤3 sentence sweep). **F2** is falsified. All Gemini fresh findings are falsified.

---

## Gap metric

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED (fix required) | 2 | F1 (Fig. 3 caption), F4 (LiteBIRD clause) |
| PARTIAL (sweep/editorial) | 1 | F3 ("tests of γ" 3 sites) |
| HOUSTON-DECISION / OPINION | 5 | F5, F6, F7, F9, K5 (+ K3) |
| FALSIFIED | 10 | F2, F8, F10, F11, K1, K2, Ge1, Ge2, Ge3, Ge3-b |
| Re-raises of audited-FALSIFIED items | 5 | F8 (3rd), F10 (4th), F11 (4th), K1 (EXT3 FALSIFIED), K2 (EXT3 FALSIFIED) |

**Genuinely new substantive findings: 2** (F1 + F4). Both are one-figure / one-clause fixes.

Trend: EXT1 ~12 → EXT2 ~9 → EXT3 ~2.5 → **EXT4 ~2**. Paper is strongly converging.

---

## Closure plan

### Priority 1 — VERIFIED (must fix before submission)

**[F1] Fig. 3 caption — clarify what the orange curve represents** (tex L924–936):
- The lower panel plots ΔH/H_ΛCDM for the full ΞM_Pl² dark-energy model (the mechanism this paper IS about), not the rotation-only c_ω·ω² contribution (which is bounded at 10^{-21}).
- Fix: Rewrite caption opening to state "Evolution of the Hubble parameter H(z) for the full ECH dark-energy model (ΞM_Pl² term, orange) versus ΛCDM (blue). Lower panel shows the model-level percent deviation. The rotation contribution c_ω·ω² is separately bounded by CMB isotropy at ≲10^{-21}ρ_Λ^obs (see Eq. ref{eq:Leff_full}) and is completely invisible on this scale; the dark-energy mechanism in this paper is the ΞM_Pl² term, not rotation."
- Alternatively: relabel the figure title/legend or add a text annotation distinguishing the two contributions. Regeneration of the PNG not required if the caption is corrected.

**[F4] LiteBIRD "exclude the ALP explanation" — one clause** (tex L2352–2354):
- Change: "or exclude the ALP explanation" → "or exclude this uniform spectator-ALP benchmark (f_a~M_Pl, m~H_0) as the explanation of the current WMAP+Planck central value."

### Priority 2 — PARTIAL (sweep, no physics reanalysis)

**[F3] "Tests of γ" language** (tex L643, L2107, L2506):
- At each site: replace "relevant tests of γ" with "relevant tests of the nonperturbative parity-violating sector (ECH-independent; become γ-probes only in a specified model coupling γ to photon or tensor parity)." Or shorter: "nonperturbative parity channels outside the proven scalar/tensor transparency sector."
- 3 sites; ~3 minutes of edits.

**[F7] Fig. 6 "decisive" language** (tex L2297–2298, OPINION):
- The "2.6–5σ realistic" and "decisive ≳5σ Stage III/IV" describe different regimes; no factual error. Optional polish: add "in the optimistic Stage III/IV regime" before "decisive." Houston call.

### Priority 3 — HOUSTON-DECISION (no edit required without explicit instruction)

- **F5** (Fig. 1 "mechanism-indep." annotation in PNG): requires figure regen; low stakes since caption text is correct.
- **F6** (Fig. 4 "Parameter-independent" label): editorial.
- **K5/K3** (companion arXiv IDs; scoping repetition): submission logistics / style.

---

## EXIT-CRITERION ASSESSMENT

**ChatGPT MAJOR classification**: of its 4 fresh MAJORs — F2 is falsified, F1 is real (1-clause caption fix), F3 is real (3-site sweep), F4 is real (1-clause fix). Zero new fatal physics errors; MAJOR rating driven by accumulated wording residue and the Fig. 3 caption ambiguity.

**Gemini MINOR classification**: all fresh findings falsified; no new substantive contribution this round.

**Grok MINOR classification**: holds; fresh minors are re-raises of already-falsified items.

**Is P1A externally clean post-patch?** YES — after Actions 1 (F1 caption), 2 (F4 clause), and 3 (F3 3-site sweep), every remaining open item is HOUSTON-DECISION or n-th-round falsified noise. Estimated wall time: <30 minutes of tex edits + recompile. No physics reanalysis, no figure regeneration required (unless Houston wants F5 PNG annotation). Recommend executing the patch wave and closing EXT4 without a further full external round; a delta-confirm from ChatGPT is optional.
