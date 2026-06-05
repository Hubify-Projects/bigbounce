# P1B auto-2026-06-05_1418pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (13693 chars)
**Wall time**: 395.2s

---

# Referee Report — Paper P1B
## "Technical Verification Companion to the ECH Spin-Torsion Program"

I have read the manuscript end-to-end, audited tables, recomputed σ values, and checked the bibliography. My conclusion before listing the findings: **this paper has no extractable PRD-grade scientific content**. By the author's own scope statements, (i) the MCMC uses stock CAMB with no torsion modifications and finds the data consistent with ΛCDM, (ii) the NaMaster work is not a sky measurement, and (iii) the ALP "consistency check" is "not a distinctive ECH prediction." The paper is also a companion to four separate papers by the same author, all "in preparation," none of which I can verify. I cannot recommend publication in any form close to the current draft.

---

## ESSENTIAL findings

**P1B-E1 — All four referenced "companion papers" are unpublished.** Page 1–2, 7, 10. References [1], [4], [5], [6] are all "Golden, in preparation, HUBIFY-2026-001A/002/003/004." Reference [1] (Paper I(a)) is the entire load-bearing parent paper this companion exists to support. PRD cannot accept a "verification companion" to a non-existent paper. The 14-barrier structural-closure no-go program, the perturbation-transparency theorem, and the f_NL = −35/8 prediction are not available for review. *Fix:* withdraw until at least Paper I(a) is submitted as a co-submission, or merge content into a single self-contained paper.

**P1B-E2 — Abstract and body describe materially different analyses.** Abstract: "(1) Stock-CAMB ΛCDM+∆N_eff MCMC proxy ... 309,189 frozen samples across two converged dataset combinations, plus a third Planck-only combination ongoing." Body Sec. V.B and Table II: an entirely separate DESI DR2 + Planck NPIPE + DES-Y5 + Pantheon+ chain in (w₀,wₐ) with **128,385 samples** is reported, and its result is explicitly called "**the headline result is w₀ = −0.812 ± 0.044 ... at +4.3σ ... wₐ = −0.667 ± 0.186 ... at −3.6σ.**" None of this appears in the abstract. A 4σ-scale dark-energy claim cannot be absent from the abstract while a null Neff result is. *Fix:* reconcile abstract with body; if w₀wₐ is the actual headline, restructure the paper around it (subject to E3 below).

**P1B-E3 — The "headline" 4.3σ result is self-disclaimed as meaningless.** Page 3 and Table II footnote a: "LCDM is unsampled by this chain (no w₀ = −1, wₐ = 0 samples in the present Metropolis-Hastings run), so the +4.3σ figure is a posterior-tail extrapolation distance only, **not a Bayes-factor or ln B exclusion and not a frequentist tension**." Page 6 then states the same result is "the headline result." A number explicitly disclaimed as neither a Bayes factor nor a frequentist tension cannot be a "headline" anywhere in a PRD paper. Either compute the nested-sampling ln B (which the authors say they will not do here) or remove the σ language. *Fix:* delete every "+4.3σ" / "−3.6σ" headline framing or reformulate as posterior moments without tension language.

**P1B-E4 — Pervasive internal-audit / reviewer-log prose embedded in the body.** Multiple passages read as visible response-to-reviewer text:
- Page 3: "An earlier count erroneously quoted '98.6% quintom-B' weight."
- Page 3: "note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but with zero free-w₀wₐ samples at the LCDM point the KDE estimator fails catastrophically."
- Page 4: "**This addresses earlier reviewer concerns** that the reported 67.68 was inconsistent with active SH0ES likelihood."
- Page 4: "**A concern was raised** that the joint posterior mean (MB = −19.263, H0 = 67.69) was inconsistent with an active sn.pantheonplus likelihood, claiming a Cobaya YAML alias failure."
- Page 5–6: "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°."
- Page 7: "§VI for the explicit numerical derivation **correcting the earlier C_aγ θ_i product**."

All of this must be removed; PRD does not publish response-to-referee text in the body. *Fix:* rewrite each passage as a clean methods statement.

**P1B-E5 — No novel physics content.** The author's own scope statements make this explicit:
- Sec. III: "*Not a spin-torsion theory module.* The Boltzmann code carries no torsion modifications."
- Sec. IV/VI: "*Not a competitive sky detection.*"
- Sec. VI: "*Not a distinctive ECH prediction. The same β ≈ 0.27° arises in any GR+ALP setup with the same parameters; no ECH-specific derivation connects the Holst action to the photon-torsion coupling required.*"
- Sec. V.A: "(ω/H)₀ and Ω_k are fixed to zero in the actual sampled YAML configuration."

What remains: a vanilla stock ΛCDM+N_eff run (a null result), a pipeline-validation MC, and a check that a standard ALP can produce ~0.3° birefringence (known since Fujita et al. 2021, [21]). None of this clears the PRD novelty bar.

**P1B-E6 — Pipeline-recovery SNR figures (20.32, 25.71) are decorative and misleading.** These numbers depend entirely on the chosen MC noise floor (Δ_P = 10 μK·arcmin, 500 realizations) and have no physical meaning, as the authors themselves repeatedly warn. They should not appear as quantitative results. The fact that they had to be wrapped in three separate disclaimers in the abstract alone ("Scope of the validation:", "MC recovery is therefore a pipeline-validation figure...", "the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements") indicates the figures themselves should be removed. *Fix:* delete the SNR figures or replace with a single bias-table entry.

**P1B-E7 — Sigma values from incommensurate procedures are juxtaposed.** Abstract and body juxtapose:
- "pipeline-recovery SNR = 20.32σ" (MC bias-injection)
- Published Planck/ACT DR6 "2.4–2.9σ" (sky measurement)
- ALP-MCMC βALP = 0.336° ± 0.107° (3.1σ if dividing)
- Eskilt+Komatsu joint "3.6σ"
- Auxiliary inverse-variance "3.9σ"
- DESI w₀ "+4.3σ" (posterior-tail extrapolation, not a tension)

Per the reviewer instructions: any time σ values from different null procedures appear adjacent, the paper must state "not directly comparable" at every juxtaposition. The current "Scope of the validation" paragraph in the abstract is the only place this is done; it is not done in Sec. III, Sec. V.B, Sec. VI body, or Table III. *Fix:* add explicit non-comparability statements at every σ juxtaposition or harmonize the figures of merit.

**P1B-E8 — The spectator-ALP scan is performed outside the spectator regime.** Footnote 4 (p. 7) and footnote 5 (p. 9) explicitly state Ω_a ≪ 1 requires θ_i ∼ 0.1, while the MCMC prior is θ_i ∈ [0.5, 2] and the quoted β range [0.17°, 0.43°] is evaluated there. The claim "consistent for natural parameters" is therefore evaluated in a range the author has separately identified as the dark-energy-ALP regime, **not** the spectator regime. The "consistency check" never actually computes the prediction in the regime it claims to validate. *Fix:* re-run the MCMC with θ_i ∈ (0, 0.2] (or equivalent log-prior) and report whether the observed β still falls in the prior envelope.

---

## MAJOR findings

**P1B-M1 — Required C_aγ ∈ [9, 51] is far outside the KSVZ/DFSZ benchmark range.** Page 7: "Both ends are larger than the standard KSVZ/DFSZ benchmark range, which predicts |C_aγ| ∼ O(1); the entire required range therefore lies outside minimal ALP photon-coupling benchmarks and requires non-minimal model building." This is an honest disclosure but the abstract still claims "natural parameters." A C_aγ ∼ 50 ALP coupled to gravity-scale f_a ∼ M_Pl is not "natural" in any standard sense; the abstract is overstated.

**P1B-M2 — Reading-room arithmetic check on Eq. (3).** β = (α_EM × 8)/(4π) × 1.07. Compute α_EM/(4π) = (1/137.036)/(12.566) = 5.806×10⁻⁴ rad; × 8 × 1.07 = 4.97×10⁻³ rad = 0.285°. Paper says "≈ 0.29°." OK numerically. But the factor 1.07 (= Δϕ/f_a here?) is inconsistent with Eq. (2), which gives Δϕ/f_a = 0.65 for m = H_0, θ_i = 1. The 1.07 corresponds to m ≈ 1.8 H_0, but Eq. (3) uses "m ≈ 2H_0" in the prefix. Internal inconsistency between Eqs. (2) and (3). *Fix:* state Eq. (3) at a single parameter point.

**P1B-M3 — Sample-count reconciliation footnote does not reconcile.** Footnote 1 (p. 2): 176,240 × 0.7 = 123,368 post-burn-in for the full-tension subset; Fig. 1 caption (p. 5) says 119,617 post-burn-in; body footnote then introduces a third number, 123,129, as the "post-burnin count of the full-tension subset alone." Three numbers (119,617; 123,129; 123,368) for a single subset is bookkeeping noise that should not be in a published paper. *Fix:* report a single canonical number with one definition of "post-burn-in."

**P1B-M4 — Table II "marginal-tail" σ is methodologically incoherent.** Reporting +4.3σ on w₀ when the LCDM point is unsampled is, by the authors' own admission, "kernel-dependent noise." A "marginal-tail posterior-extrapolation distance" is not a quantity that PRD reports. Either delete or replace by a tail-probability with an explicit estimator (e.g., importance-sampling lower bound, nested sampling). *Fix:* nested-sampling ln B as the authors promise, or remove the number entirely. Promising future work in the present paper is not acceptable; the paper must be coherent today.

**P1B-M5 — DESI DR2 BAO χ²_BAO = 10.6 ± 1.8 reported without degrees of freedom.** Table II. Without N_dof a χ² is uninterpretable. Similarly χ²_CMB = 10983.9 ± 5.3 and χ²_SN = 3043.0 ± 1.6. *Fix:* include N_dof per channel.

**P1B-M6 — Foreground-cleaned Commander map invalidates the bias-injection logic for the cosmic-rotation question, but the paper uses it anyway.** The abstract explicitly states: "the foreground-cleaned Commander map removes the very component that breaks the β–α degeneracy in published Planck/ACT DR6 measurements." If the chosen map structurally cannot separate β from α, then injecting β into it and "recovering" β is a tautological closed-loop test. The validation is even weaker than the disclaimers admit — it does not validate any pipeline that could be used on data. *Fix:* either move to a foreground-uncleaned map or remove the analysis.

**P1B-M7 — Cobaya version mismatch.** Sec. V.A: "Cobaya [20] (v3.5 original; v3.6.1 verification)." Abstract says only v3.6.1. Internal version history in the methods section is not acceptable. *Fix:* state one version (the one whose chains are reported).

**P1B-M8 — Eskilt & Komatsu "PR3 vs PR4" disambiguation footnote.** Page 1 footnote a: the headline σ in the abstract (3.6σ, PR3+WMAP9 published) and the dataset actually used in the ALP-MCMC (PR4/NPIPE from the GitHub README) are different. PRD requires that the data used in the analysis be cited explicitly, not deferred to a GitHub README. *Fix:* cite a single dataset throughout; if PR4/NPIPE is used, cite the corresponding paper, not the PR3 one.

**P1B-M9 — Hubble-tension discussion is an apology, not a result.** Sec. III, p. 2: "the SH0ES H₀ prior is in the Cobaya likelihood configuration, but ... the posterior H₀ in the proxy run is pulled to 67.68 ± 1.06 ... rather than to the simple Gaussian-combination value ~70 that would emerge if SH0ES and Planck were equally weighted. We do not therefore claim that the SH0ES tension is resolved or even moved." This passage exists only to defuse a referee question; it is not a scientific result and consumes a third of Sec. II + half of Sec. III.

**P1B-M10 — The ω₀, Ω_k clarification ("fixed to zero") undermines the entire purpose of the proxy.** If the *actual* bounce-class indicators are fixed to zero and only N_eff is varied, this is just a vanilla ΛCDM+N_eff analysis, which is not new. *Fix:* either justify why N_eff alone is a sufficient proxy, or vary the indicators that distinguish the bounce.

**P1B-M11 — Worst R̂ − 1 reconciliation.** Table I lists "Worst R̂ − 1 = 0.001" for full-tension; footnote a says "9.74 × 10⁻⁴." These round to "0.001" only at one significant figure. Inconsistent precision presentation. *Fix:* report one consistent precision.

**P1B-M12 — "Convergence: R̂ − 1 < 0.01 for all runs" in Sec. VI vs. "R̂ − 1 < 3 × 10⁻³" for cosmology runs.** Different convergence floors for different runs are not flagged; the looser ALP-MCMC convergence is a weaker criterion than Gelman-Rubin best practice for posterior-tail interpretation, especially when extracting σ-level statements. *Fix:* converge to <10⁻³ before quoting tail σ.

**P1B-M13 — w_pivot vs (w₀, wₐ) tension is self-contradicting headline framing.** Table II: w_pivot = −1.034 ± 0.030 is consistent with −1 at −1.1σ (i.e., **no tension**), but the body trumpets w₀ at +4.3σ and wₐ at −3.6σ as a "canonical quintom signature." A pivot-redshift parametrization that is consistent with LCDM at 1σ but exhibits 4.3σ "tension" away from it is a Jacobian rotation artifact, not new physics. *Fix:* lead with w_pivot, not with the rotated (w₀, wₐ) marginals.

**P1B-M14 — Section V title "Cosmological Fits and Model Comparison" but no model comparison performed.** Sec. V.B explicitly says "We do not report χ²_eff, AIC, BIC, or ln B Bayes-factor model-comparison numbers in this paper." A section titled "Model Comparison" that does not perform model comparison is mislabeled. *Fix:* retitle.

**P1B-M15 — "Independent cross-validation" with Liu et al. (Sec. III) is not a cross-validation.** Liu et al. find torsion preferred by AIC (ΔAIC = −5.7 to −6.6); this paper does not compute AIC. Reporting "0.5σ in H₀" agreement between two different model fits is not a cross-validation, it is a fortuitous parameter coincidence. *Fix:* either compute AIC on the same likelihood stack or remove the cross-validation claim.

**P1B-M16 — Table III "Claims classification" is unprofessional.** Listing "Stock CAMB proxy ≠ ECH theory module" and "ALP birefringence not distinctive ECH prediction" as "Scope" claims with "Defn." status is administrative paperwork, not scientific content. A reader who needs a table to be told what is *not* claimed is being warned that the rest of the paper overreaches.

---

## MINOR findings

**P1B-Mi1 —** Reference [9] arXiv ID is "gr-qc/0601013" but the Mercuri PRD paper is correctly cited; verify the arXiv identifier resolves to the published PRD paper.

**P1B-Mi2 —** Reference [3] (Diego-Palazuelos & Komatsu 2025, arXiv:2509.13654) is cited as the source of "β = 0.215° ± 0.074° (ACT DR6)" — verify this matches the cited abstract, since the original ACT DR6 DR6 paper used different conventions.

**P1B-Mi3 —** Reference [22] description "Quintom Cosmology... canonical quintom-cosmology review... Used in P1A Sec. VI..." — internal reference annotation "P1A Sec. VI" should be removed; the bibliography is not a place for internal notes.

**P1B-Mi4 —** Reference [11] "Liu et al. 2025" arXiv:2507.04265 — verify this exists (date 2025-07 plausible for a 2026 paper).

**P1B-Mi5 —** Table II footnote b ("0.1-unit arithmetic-rounding artifact") is a footnote about rounding noise; should be deleted.

**P1B-Mi6 —** Sec. III footnote 2 EFT discussion (Λ_strong ∼ M_Pl/√γ_BI) belongs in Paper I(a), not here; out of scope for a "verification" companion.

**P1B-Mi7 —** Sec. IV: "ACT-noise level ΔP = 10 μK·arcmin (a conservative worst-case bias check)" — ACT DR6 is closer to 10 μK·arcmin coadded but Commander is Planck; mixing noise levels across experiments needs justification.

**P1B-Mi8 —** Figure 1 axes: ∆N_eff axis shows ticks at −0.5, 0.0, 0.5 — the reported posterior is −0.020 ± 0.169, so the panel is mostly empty space; tighten.

**P1B-Mi9 —** Page count: 10 pages for "no novel claims" content. Recommended maximum if this is published in any form: **4 pages** (PRL-style note or PRD Brief Report), not a full PRD article.

**P1B-Mi10 —** "Houston Golden, Independent Researcher, Los Angeles, California" — affiliation OK, but corresponding email "houston@hubify.com" is a private/commercial domain. PRD does not require institutional, but flag for editorial.

---

## NITs

**P1B-N1 —** "Frozen MCMC program: 309,189 raw samples" — "frozen" is not standard MCMC terminology; rephrase to "finalized" or "publication-quality."

**P1B-N2 —** Footnote a in Sec. VI inflates inverse-variance combination to 3.9σ but immediately tells the reader to ignore it — delete the auxiliary cross-check.

**P1B-N3 —** "comfortably bracketing the observed value" (p. 7) is colloquial.

**P1B-N4 —** Abstract uses both "βˆ" (hat) and plain "β" inconsistently.

**P1B-N5 —** Date stamp "2026-06-03 PDT" with explicit timezone in the date field is unusual.

---

## Summary recommendation

**REJECT**

The author has, with admirable honesty, told the reader that the three analyses in this paper are (i) a stock CAMB null with no torsion modifications, (ii) a pipeline-validation MC that is not a sky measurement, and (iii) an ALP consistency check that is not a distinctive prediction of the framework the paper claims to support. The paper is a "verification companion" to four other papers by the same author, all "in preparation" and none available for review. A fifth, separately converged DESI w₀wₐ chain that is not in the abstract is then presented inside the body as the "headline 4.3σ result," only to be immediately disclaimed as "not a Bayes factor and not a frequentist tension." The body contains extensive response-to-reviewer prose ("a concern was raised," "this addresses earlier reviewer concerns," "an earlier count erroneously quoted"). The ALP "spectator-consistency" check is performed in a parameter range the author identifies as the dark-energy regime, not the spectator regime. Required photon couplings are C_aγ ∈ [9, 51], far outside KSVZ/DFSZ. None of this clears the PRD novelty or rigor bar. The author should withdraw and re-submit a unified Paper I(a)+companion once the parent paper exists, the headline result is decided, the audit prose is removed, and an actual physics claim is supported by a self-contained analysis.

---

## PASS 2 — self-critique findings (what initial review missed)

# Re-Review: Additional Findings (Fresh-Eyes Pass)

After a second pass focused on arithmetic recomputation, citation auditing, and figure/table cross-checking, I find a substantial number of additional problems my initial review missed. The fresh-eyes pass turned up arithmetic errors, citation errors, dangling references, and an internal claim about a "canonical" agreement that does **not** actually arithmetically agree.

---

## NEW ESSENTIAL findings

**P1B-E9 — Arithmetic claim "this offset is ∼3.2σ ... corresponds exactly to the canonical 3.6σ Hubble tension" is internally inconsistent.** Page 4: the paper computes a 0.155 mag M_B-axis offset (verified: −19.263 − 5 log₁₀(67.69) = −28.4157 vs. −19.253 − 5 log₁₀(73.04) = −28.5707; difference = 0.155 ✓), then divides by σ_MB = 0.049 to get 3.16σ ≈ 3.2σ ✓. The same paragraph then asserts this "corresponds **exactly** to the canonical 3.6σ Hubble tension." 3.2σ ≠ 3.6σ — these are different numbers from different axes (M_B-axis vs. H₀-axis), and the paper's own arithmetic produces 3.2σ on the M_B axis, not 3.6σ. The word "exactly" is unsupported. *Fix:* either acknowledge the 0.4σ discrepancy between M_B-axis and H₀-axis tension, or remove the "exactly" claim.

**P1B-E10 — Citation error in abstract: ref [2] is misattributed for the "2.4–2.9σ" claim.** Abstract: "The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2, 3]." But reference [2] is Eskilt & Komatsu 2022, which is explicitly the **3.6σ** joint WMAP+Planck PR3 paper (the abstract's *own footnote a* on page 1 confirms this: "the abstract β = 0.342° ± 0.094° (3.6σ) headline is from the published PR3+WMAP9 joint analysis"). The 2.4–2.9σ range must instead come from refs [15] (Planck NPIPE individually, 0.30°/0.11° = 2.73σ) and [3] (ACT DR6 individually, 0.215°/0.074° = 2.90σ). The abstract cites [2] for a range to which [2] does **not** belong. Furthermore, **2.4σ does not match either individual reference**; the lowest is 2.73σ. *Fix:* replace [2] with [15] and document the source of the 2.4σ lower bound, or correct the range to "~2.7–2.9σ."

**P1B-E11 — Dangling internal reference to "§ Headline-result discussion".** Table II footnote a (page 4): "robust ln B is left to a follow-up nested-sampling analysis (see § Headline-result discussion)." **No such section exists** in this paper. The closest is the unlabeled "headline result" paragraph in Sec. V.B. PRD requires unambiguous internal references. *Fix:* either create the section, or replace with "(see Sec. V.B paragraph beginning 'The headline result is...')."

---

## NEW MAJOR findings

**P1B-M17 — Eq. (3) and its surrounding prose describe inconsistent parameter points.** Page 7: Eq. (3) is written as "For C_aγ = 8, θ_i = 1, **m ≈ 2H₀**: β ≈ (α_EM × 8)/(4π) × 1.07 ≈ 0.29°." The very next sentence reads: "The fiducial value β ≈ 0.27° corresponds to the midpoint **m ≈ 1.8 H₀**, Δϕ/f_a ≈ 1.0." But Eq. (2) gives Δϕ/f_a = 0.65 for m = H₀, θ_i = 1, so the 1.07 used in Eq. (3) requires a yet-different parameter point. Three distinct (m, Δϕ/f_a) pairs in three consecutive sentences. *Fix:* fix Eq. (3) to a single parameter point and use consistent values in the surrounding text.

**P1B-M18 — Eq. (3) silently mixes radians and degrees.** The right-hand side α_EM × 8/(4π) × 1.07 = (1/137.036) × 8/(12.566) × 1.07 ≈ 4.97 × 10⁻³ **radians**. The "≈ 0.29°" requires multiplication by 180/π ≈ 57.3. The conversion factor is not shown anywhere in the equation. A PRD equation that crosses units without writing the conversion is improper formatting. *Fix:* either insert the explicit factor or write the equation in radians and then state the value in degrees as a numerical conversion.

**P1B-M19 — Cited "2.4σ" lower bound has no source in the bibliography.** Working through the cited refs:
- Ref [2] Eskilt+Komatsu = 3.6σ (their headline)
- Ref [3] Diego-Palazuelos+Komatsu ACT DR6 = 0.215°/0.074° = **2.90σ**
- Ref [15] Diego-Palazuelos et al. Planck NPIPE = 0.30°/0.11° = **2.73σ**

None gives 2.4σ. The "2.4–2.9σ" range claimed in the abstract and Sec. VII conclusions ("Planck/ACT DR6 2.4–2.9σ measurements") has no supporting reference. *Fix:* identify the 2.4σ source or correct the range.

**P1B-M20 — Parameter-count split inconsistent between Table I and Table II.** Table I footnote a: "all 17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance)." Table II header: "8 cosmological + 9 nuisance parameters." Both sum to 17, but with **different splits**. Either (a) the same parameter is moved between categories (e.g., M_B classed as "cosmological" in one and "nuisance" in the other), or (b) the chains have genuinely different parameter sets and the tables are reporting different runs. In either case, this is bookkeeping noise that the author has not resolved. *Fix:* document explicitly which parameter is reclassified and why.

**P1B-M21 — βfree absent from the Claims Classification (Table III).** Table III lists "βALP = 0.336° ± 0.107°" but omits "βfree = 0.344° ± 0.096°" which is given equal prominence in Sec. VI. The two are presented as cross-validating one another, so omitting one from the claims table is misleading. *Fix:* add βfree to Table III.

**P1B-M22 — "Planck-only" run sample count contradicts the abstract's "two converged dataset combinations" framing.** Abstract: "two converged dataset combinations, plus a third Planck-only combination ongoing." Footnote 1: "The third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating." But Table I has **only two columns** (full-tension, Planck+BAO+SN) — the Planck-only run does not appear in the table at all. Page 8 conclusions then refer to "an additional 114,992-sample Planck-only run." If the run is not tabulated, the abstract should not advertise it. *Fix:* either include the Planck-only column in Table I (with a clear "preliminary, R̂ − 1 = 0.05" warning) or remove all mention from the abstract.

**P1B-M23 — Loose R̂ − 1 convergence threshold for the w₀wₐ chain.** Page 8: "R̂ − 1 = 0.00820, below the standard R̂−1<10⁻² publication target." But the cosmology chains in Table I converge to R̂ − 1 < 3 × 10⁻³ (footnote a), and the standard PRD convergence target for posterior-tail inference is R̂ − 1 < 10⁻³. A "+4.3σ marginal-tail" claim on a chain converged only to 8.2 × 10⁻³ is methodologically suspect; tail probabilities are precisely where loose convergence fails. *Fix:* tighten convergence before quoting tail σ.

**P1B-M24 — Table II χ²_BAO = 10.6 ± 1.8 for DESI DR2 is suspiciously low.** DESI DR2 BAO has ~12 observables (multiple z-bins × tracers). χ² = 10.6 over ~12 dof is reasonable, but the **uncertainty** ±1.8 is implausible — χ² evaluated at a single best-fit point has no Monte Carlo width; ±1.8 must be the std of χ² evaluated at posterior samples (i.e., a posterior spread, not a measurement error). The notation is misleading. *Fix:* clarify whether ±1.8 is the posterior std of χ² across MCMC samples, and report N_dof.

**P1B-M25 — Table I uncertainty inconsistency on σ_∆Neff.** Table I lists ∆N_eff = −0.020 ± 0.169 (full-tension) and +0.065 ± 0.17 (Planck+BAO+SN). The uncertainties are quoted to **different precisions** (3 vs 2 significant figures). The abstract reproduces this inconsistency verbatim. *Fix:* standardize to 0.169 / 0.170 or 0.17 / 0.17.

**P1B-M26 — Fig. 1 corner-plot axis ranges inconsistent with reported 1σ widths.** The corner plot (Fig. 1) shows σ₈ axis 0.78–0.84 (range 0.06) but Table I reports σ_σ8 = 0.008 — meaning the panel spans ~±4σ. The ∆N_eff axis spans −0.7 to +0.7 (~±4σ), matching. But S₈ axis 0.78–0.84 (range 0.06) with σ_S8 = 0.008 also gives ~±4σ. The Planck+BAO+SN column reports σ_S8 = 0.018, so a single corner plot cannot match both. The caption clarifies that Fig. 1 shows only the full-tension chain — so the ±4σ framing is correct. However, the body's claim "S₈ = 0.814 ± 0.008 (full-tension)" with the DES Y3 S₈ prior active is suspicious: DES Y3 measures S₈ ≈ 0.776 ± 0.017, so a posterior at 0.814 ± 0.008 is in ~2.2σ tension with the prior, yet this is not flagged. *Fix:* either explain why the posterior pulls away from the DES Y3 prior with reduced uncertainty, or check whether the DES Y3 prior is actually active in the YAML.

**P1B-M27 — Eq. (3) "1.07" factor has no traceable parameter-point origin.** Working back: Eq. (3) needs Δϕ/f_a = 1.07 to give β = 0.29° for C_aγ = 8. Eq. (2) gives Δϕ/f_a = 0.65 for m = H₀, θ_i = 1. To get Δϕ/f_a = 1.07 from the natural-parameter scan requires m/H₀ between 1 and 3 AND θ_i between 0.5 and 2, but the prefix of Eq. (3) states θ_i = 1, m ≈ 2H₀ — these specific values were not separately computed and quoted earlier. The 1.07 appears to be reverse-engineered to make the result land at 0.29°. *Fix:* show the ALP-EOM integration at the specific point (m = 2H₀, θ_i = 1) that gives 1.07, or remove the spurious precision.

**P1B-M28 — "Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈" with Liu et al. is unverifiable.** Page 5: the cited Liu et al. [11] H₀ and σ₈ values are not quoted in the present paper, so the σ-level agreement claim cannot be checked from the manuscript alone. Cross-validation claims must be self-contained. *Fix:* quote Liu et al. H₀ and σ₈ values inline.

---

## NEW MINOR findings

**P1B-Mi11 —** Page 2: "the (ω/H)₀ parameter is discussed in Paper I(a) as a phenomenological bounce-class indicator." Since Paper I(a) is not yet published (P1B-E1), this forward reference is unverifiable.

**P1B-Mi12 —** The auxiliary "β_combined = 0.241° ± 0.061° (3.9σ)" inverse-variance combination (Eq. 4) is computed wrong if shared systematics matter. With β_1 = 0.30 ± 0.11 and β_2 = 0.215 ± 0.074, inverse-variance weights give:
σ⁻² = 1/0.11² + 1/0.074² = 82.6 + 182.6 = 265.2 → σ_comb = 0.0614 ≈ 0.061 ✓
β = (0.30/0.0121 + 0.215/0.00548)/265.2 = (24.79 + 39.23)/265.2 = 64.02/265.2 = 0.2414 ✓
β/σ = 0.2414/0.0614 = 3.93σ ≈ 3.9σ ✓.
Arithmetic OK; concern is only that the paper itself then disclaims this number. Why include a number you tell readers to ignore? *Fix:* remove Eq. (4) entirely.

**P1B-Mi13 —** Page 1 abstract: "Worst R̂ − 1 = 0.001" in Table I footnote a is then expanded as "9.74 × 10⁻⁴ for n_s in the full-tension combination." Two different significant-figure precisions for the same quantity. (Same issue noted at M11 but with a different value pair.)

**P1B-Mi14 —** Page 5: "Cobaya v3.5 original; v3.6.1 verification" — was the abstract's "Cobaya v3.6.1" the version that produced the chains, or just the version that verified them? Major Cobaya version difference (3.5 → 3.6) can change posteriors at the percent level. (Same issue as M7, now with extra suspicion about which chains were used to produce the reported numbers.)

**P1B-Mi15 —** Table II "ω_b h² 0.02224 ± 0.000125" — the uncertainty 0.000125 is **smaller** than Planck-only (typically 0.00015), which is plausible only if DESI BAO breaks ω_b h² degeneracies. No discussion of where the tightening comes from.

**P1B-Mi16 —** Eq. (2) "(m = H₀, θ_i = 1)" — but the spectator-status disclaimer requires θ_i ∼ 0.1, so the entire Eq. (2) is evaluated outside the spectator regime that the section title claims to validate.

**P1B-Mi17 —** Page 7 prefactor arithmetic: "the prefactor α_EM/(4π) is 5.8 × 10⁻⁴" — actual = (1/137.036)/(12.566) = 5.806 × 10⁻⁴, OK at 2 sig figs.

**P1B-Mi18 —** Page 7: "β = 0.342° in radians is 5.97 × 10⁻³" — check: 0.342 × π/180 = 0.005969 ✓.

**P1B-Mi19 —** Appendix C states the model-independent β prior is uniform on [−2°, 2°], but Sec. VI body never states this prior explicitly. The prior is unusually wide given σ(β) ≈ 0.1°, but the posterior would still be data-dominated.

**P1B-Mi20 —** Page 8: "GetDist posteriors on w₀wₐ are available as an empirical test of the quintom-B scenario." But the result is then disclaimed as not a Bayes-factor or frequentist tension (P1B-E3). Available ≠ usable.

---

## NEW NITs

**P1B-N6 —** "we therefore claim" (page 2, Sec. II) → "do not therefore claim" — awkward phrasing.

**P1B-N7 —** Table II header parameter-count parenthetical comes before the likelihood stack, breaking standard caption-flow.

**P1B-N8 —** "marginal-tail posterior-extrapolation departure" (Table II) — non-standard term. Standard terms are "tail probability" or "p-value at point estimate." Inventing terminology to avoid the standard meanings of σ is a flag.

**P1B-N9 —** Section VII title "Conclusions" but the section opens by describing what is *not* concluded (no Bayes factors, no novel claims, no tension resolution). Conclusion section should conclude.

**P1B-N10 —** Page 7 phrase "comfortably bracketing the observed value" — when the bracket requires a 25× misalignment tuning per footnote 4, "comfortably" is unjustified.

---

## Updated summary

The fresh-eyes pass reveals: (a) an explicit arithmetic claim of "exactly 3.6σ" that the paper's own arithmetic produces at 3.2σ; (b) a citation error in the abstract pointing to ref [2] for a "2.4–2.9σ" range that [2] does not contain; (c) a dangling reference to a section that does not exist; (d) an equation (Eq. 3) whose parameter point disagrees with both the preceding equation (Eq. 2) and the immediately following text; (e) a "2.4σ" lower bound that no cited reference supports; (f) parameter-count inconsistencies between Tables I and II; and (g) an undisclosed "βfree" result that is given equal prominence in the body but omitted from the Claims Classification table. These are the kinds of errors that, individually, would each warrant revision, and collectively confirm the initial reject recommendation. **My recommendation stands: REJECT.**