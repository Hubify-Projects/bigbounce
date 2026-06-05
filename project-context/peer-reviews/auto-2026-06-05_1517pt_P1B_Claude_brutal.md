# P1B auto-2026-06-05_1517pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14468 chars)
**Wall time**: 468.4s

---

# Referee Report — P1B (Technical Verification Companion)
## Physical Review D — Brutal-Honesty Review

This is a 10-page "technical verification companion" paper. Before listing findings I need to state the structural problem plainly: **the paper explicitly disowns the ECH-specific content of all three of its "verification" analyses**.

- §III "Stock-CAMB ΛCDM+∆Neff MCMC … (Not a Spin-Torsion Theory Module)" — "no torsion modifications to the Boltzmann equations."
- §IV "NaMaster pipeline validation" — "Not a competitive sky detection."
- §VI "Spectator-ALP consistency check" — "Not a distinctive ECH prediction. The same β ≈ 0.27° arises in any GR+ALP setup."

This is the entire substance of the paper. There is no test of ECH spin-torsion in this manuscript. There is no original sky measurement. The MCMC is a stock-CAMB null check that recovers ΛCDM. The 10-page length cannot be justified.

That alone is grounds for rejection. The remaining findings document why even on its own narrower terms the paper is not PRD-ready.

---

## ESSENTIAL findings

**P1B-E1 (Abstract → §III, p.1–2, p.6):** The abstract and §III both concede the load-bearing MCMC is a stock-CAMB ΛCDM+∆Neff run with no ECH modification. There is no derivation linking the ECH spin-torsion sector to the ∆Neff proxy beyond the assertion "minimal matter-bounce class predicts ∆Neff ≈ 0 by construction." That statement is asserted, not derived, and footnote 2 explicitly notes the parity-even four-fermion contact operator is dimension-6 and "does not produce a ∆Neff at recombination." The paper therefore admits the MCMC has zero discriminating power for ECH. **Fix:** either remove the MCMC analysis from a paper claiming ECH verification, or supply a quantitative derivation mapping ECH parameters to a Boltzmann-sector observable.

**P1B-E2 (multiple sections):** The body text contains extensive internal review-log / audit-trail prose that does not belong in a PRD publication:
- §III "An earlier count erroneously quoted '98.6% quintom-B' weight" (p.3).
- §IV "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°" (p.5–6).
- §III "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood" (p.4).
- §III "MB–H0 joint-posterior offset check. A concern was raised that…" (p.4).
- §III "(note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but with zero free-w0wa samples at the LCDM point the KDE estimator fails catastrophically)" (p.3).
- §VI Conclusions: "§VI for the explicit numerical derivation correcting the earlier Caγθi product" (p.8).
- Abstract footnote (a) "Eskilt & Komatsu 2022 disambiguation" — an admission that the labels in the paper do not match the published reference.

**Fix:** strip all version-history, concern-rebuttal, and self-correction prose. A PRD paper presents the final analysis, not the audit trail.

**P1B-E3 (Table I vs §III body, p.3 vs p.4):** Table I reports H₀ = 67.68 ± 1.06 km/s/Mpc (full-tension). The body text on p.4 reports "H₀ = 67.69 ± 1.06 km/s/Mpc" for the same full-tension chain. The abstract uses 67.68. These are the same chain; the values must agree. **Fix:** reconcile.

**P1B-E4 (Abstract vs §III, §V, p.1, p.3–4, p.6):** The abstract claims "**309,189 frozen samples across two converged dataset combinations**" and frames the paper as a null-consistency MCMC. The body then introduces, *prominently in §III*, an entirely separate **DESI DR2 w0wa chain (Table II, 128,385 samples)** that claims a +4.3σ departure of w₀ from ΛCDM and "phantom-crossing required" — a result that, if real, is the main finding of the paper. This chain is not mentioned in the abstract. The framing is bait-and-switch: a null verification paper that, mid-section, displays a quintom-B headline that the authors then refuse to evaluate via Bayes factor. **Fix:** either (a) move the w0wa analysis to a dedicated paper with proper nested-sampling Bayes-factor analysis and full likelihood-stack documentation, or (b) put it in the abstract and defend its significance.

**P1B-E5 (Table II, p.4):** The w₀ "+4.3σ" claim is built on a Metropolis–Hastings posterior tail extrapolation at a point the chain *did not sample*. The footnote (a) admits "LCDM is unsampled by this chain … the +4.3σ figure is a posterior-tail extrapolation distance only, *not* a Bayes-factor or ln B exclusion and *not* a frequentist tension." The same caveat is repeated in §V. A "+4.3σ" headline that the authors themselves say is neither a Bayesian nor a frequentist tension is not publishable in PRD. Either compute a controlled evidence (nested sampling) or remove the σ-language from the Table II "vs LCDM" column. **Fix:** delete the σ column from Table II or supply ln B from PolyChord/MultiNest.

**P1B-E6 (Abstract, §III, §V, multiple):** Side-by-side σ values that are *not directly comparable* appear without explicit per-juxtaposition flagging. The abstract puts "pipeline-recovery 20.32σ" near the published "2.4–2.9σ" Planck/ACT detection. The conclusions section repeats this. The hedging in the body is present but inadequate — the σ numbers must be either typographically distinguished or removed from the abstract. As written the abstract invites direct misreading. **Fix:** in every juxtaposition, label the SNR figure explicitly as "MC injection recovery — not a sky detection significance" *at that location*, not in a separate caveat sentence.

**P1B-E7 (Abstract footnote a, p.1):** The "Eskilt & Komatsu 2022 disambiguation" footnote concedes the dataset label "PR4/NPIPE" applied throughout the paper to the Eskilt+Komatsu likelihood **does not correspond to the published 3.6σ value**, which used PR3+WMAP9. This is a dataset-labeling failure that propagates throughout §VI and Appendix C. The "headline" 3.6σ is being attributed to a dataset combination the authors did not actually use in their ALP-MCMC. **Fix:** state the dataset combination used by the ALP-MCMC explicitly (PR4/NPIPE per the repo README), and quote the corresponding published value for that combination, not the PR3+WMAP9 abstract number.

**P1B-E8 (§V.B, p.6):** Model-comparison statistics (χ²_eff, AIC, BIC, ln B) are explicitly *omitted*. For a paper centered on a quintom-vs-ΛCDM headline (Table II) and an ECH-vs-ΛCDM proxy run, omitting all evidence metrics removes the only quantitative basis for any preference claim. The authors acknowledge a Savage-Dickey readout fails and defer to nested sampling — then publish the σ-language anyway. **Fix:** either run the deferred nested-sampling analysis or remove all preference/tension language.

**P1B-E9 (§VI, p.7):** The Caγ requirement is computed as Caγ ∈ [9, 51] from the natural envelope ∆ϕ/fa ∈ [0.2, 1.1]. The authors note the upper end "requires either substantial UV-completion enhancement … the upper-coupling end is not generic." Then in the *spectator-consistent corner* (θᵢ ~ 0.1, ~25× tuning), Caγ must rise *further*. The paper acknowledges this but still claims the ALP "accommodates" the signal "for natural parameter values." This is internally contradictory: the natural-prior midpoint requires Ω_a ~ 1 (DE-ALP, *not* spectator); the spectator regime requires 25× misalignment fine-tuning *and* super-KSVZ/DFSZ photon coupling. The "natural" claim must be dropped. **Fix:** restate the conclusion as "consistent only under simultaneous misalignment fine-tuning and non-KSVZ photon coupling enhancement."

---

## MAJOR findings

**P1B-M1 (§VI, fn. 4, p.7):** Footnote 4 is itself a major caveat masquerading as a footnote: "a ∼25× fine-tuning of the misalignment initial condition is required to keep the ALP a true spectator." This belongs in the abstract claim, not buried in fn. 4. The abstract calls fa ~ MPl, m ~ H0 a *consistency*; under disclosed fine-tuning that wording is misleading.

**P1B-M2 (§III, p.3–4, "Physics interpretation"):** The "Physics interpretation (Table II)" paragraph is inserted into §III, the stock-CAMB ∆Neff proxy section. The DESI DR2 w0wa chain belongs in §V or in its own section. As placed, the paper reads like the verification was abandoned mid-section to insert a different analysis.

**P1B-M3 (Footnote 1, p.2–3):** The "Sample-count stratification (reconciliation)" footnote is review-bookkeeping prose: "(within ±1% of the 123,368 exact computation, with the small offset reflecting the chain-end-truncation of partial samples at the burn-in cut); the correct both-chains post-burnin total is 216,432." This level of bookkeeping detail must move to supplementary material or be removed.

**P1B-M4 (Fig. 1, p.5):** The corner plot caption claims "119,617 post-burnin samples, getdist-thinned from 176,240 raw." The axis labels are small and difficult to read at the rendered scale; the parameter labels along the diagonal are barely legible. The thinning factor (176,240 → 119,617 = 32% removal) is not documented (footnote 1 only describes burn-in removal of 30%, which would give 123,368 — different from 119,617).

**P1B-M5 (Table I footnote a, p.3):** The footnote distinguishes "k=7" cosmological from "17 sampled" total — necessary for transparency, but the awkward phrasing "references to 'k = 7' elsewhere in this paper refer to the cosmological-parameter count only" is internal-disambiguation prose.

**P1B-M6 (§III MB–H0 audit, p.4–5):** The arithmetic check 0.155 mag / σ_MB = 0.049 gives 3.16σ, which the text then identifies as "exactly the canonical 3.6σ Hubble tension." 3.16σ is not 3.6σ. The actual relation between an MB-axis discrepancy and the H₀-axis discrepancy is degeneracy-direction dependent; the "exactly" claim is unjustified.

**P1B-M7 (§V.A, p.6):** "Reproducibility materials at https://…" — URL given in body text rather than as a structured data-availability statement; YAML name `spin_torsion.input.yaml` is referenced in §III but not cataloged in the reproducibility appendix.

**P1B-M8 (PACS, p.1):** PACS classification codes were discontinued by AIP in 2010 and PRD no longer uses them. The "PACS numbers: 98.80.-k, 95.36.+x, 04.50.Kd" line is non-standard.

**P1B-M9 (Acknowledgments, p.8):** "The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation. All scientific claims, derivations, numerical results, and bibliographic attributions were independently verified by the author." PRD/APS policy requires this disclosure to be more specific about what the AI tool generated (text? code? analysis?) and which portions were independently verified. As written this disclosure is too generic for the journal's authorship policy.

**P1B-M10 (References [15], [22], p.10):** Reference annotations contain editorial prose:
- [15] "reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B"
- [22] "Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers."

Line-number references ("L256/L416 of P1B") and cross-paper editorial notes do not belong in a reference list. **Fix:** strip annotations; cite per PRD style.

**P1B-M11 (Title vs content):** The title says "Technical Verification Companion." The paper verifies nothing about ECH (per §III, §IV, §VI scope statements). The title is misleading. **Fix:** rename, e.g., "Stock-CAMB ΛCDM+∆Neff Posteriors and Pipeline Validation Notes."

**P1B-M12 (Abstract, p.1):** "plus a third Planck-only combination ongoing." Ongoing analyses do not belong in a publication abstract. Either include the analysis or omit the mention.

**P1B-M13 (§VI, p.7):** "βfree = 0.344° ± 0.096° (our internal model-independent MCMC fit to the Planck PR4 + ACT DR6 EB-spectrum likelihoods with β as a free parameter, 9,720 accepted samples across the 3 ALP-MCMC configurations described in Sec. VI (configurations Caγ = 4, 8, 12 on Planck PR4 + ACT DR6 EB-spectrum likelihoods with β as a free parameter; full priors and dataset details in Appendix C); βfree denotes the unconstrained-amplitude fit distinct from βALP which has Caγ = 8 fixed) and the observed βobs = 0.342° ± 0.094°." This sentence has nested parentheses that are unparseable. **Fix:** restructure as multiple sentences.

**P1B-M14 (§II, p.2):** "The bounce scenario motivates extending ΛCDM by ∆Neff (particle production at the bounce) as a phenomenological proxy parameter; (ω/H)₀ … and Ωₖ are fixed to zero in the actual sampled MCMC configuration." So the MCMC samples *one* extra parameter (∆Neff) over ΛCDM, with the other two bounce-discriminators frozen. Any "verification of bounce class" claim is then reduced to a single-parameter null check. **Fix:** state plainly: the MCMC is a one-parameter ΛCDM extension that does not discriminate any bounce model.

**P1B-M15 (§IV pipeline validation):** The NaMaster bias scales from 0.032° at injection 0.27° to 0.040° at injection 0.342°, described as a ~12% amplitude-dependent component. With only two injection values it is impossible to characterize amplitude dependence. The "NaMaster systematic floor of 0.04°" claim rests on two data points.

**P1B-M16 (Conclusions vs body, p.7–8):** Conclusions repeat the Caγ ∈ [9, 51] derivation and the 25× fine-tuning disclosure but soften them: "LiteBIRD will settle this at ~9σ in the early 2030s." LiteBIRD will settle whether β is consistent with zero, not whether a 25×-tuned ALP is the explanation. The 9σ figure applies to detection of β = 0.27°, not to model preference.

---

## MINOR findings

**P1B-N1 (p.1 header):** "(Dated: 2026-06-03 PDT)" — PRD does not use PDT timestamps; use the standard date-only format.

**P1B-N2 (Affiliation, p.1):** "Independent Researcher, Los Angeles, California, USA" — PRD requires an institutional affiliation or accepts "independent" with full address.

**P1B-N3 (§I, p.2):** "fNL = −35/8" is presented as a "surviving matter-bounce" prediction without citation in this paper (referred to companion paper). Acceptable for a companion, but the fraction form is mildly unusual.

**P1B-N4 (Conclusions, p.8):** "Forward.—A DESI DR2 + Planck NPIPE … cobaya chain with the w0wa free-parameter extension has converged …" — informal "Forward" header for what is actually the load-bearing analysis result of Table II.

**P1B-N5 (§VI, p.7, Eq. (4)):** "βcombined = 0.241° ± 0.061° (3.9σ)" — value not used as headline but presented prominently; the auxiliary cross-check could be moved to a footnote.

**P1B-N6 (§I, p.2):** "(taken at scan-prior midpoint values; the ~25× misalignment tuning required to reconcile the headline result with the spectator-consistent corner is disclosed in Sec. VI and fn. 4)" — this is a third-level qualification appearing inside a scope statement bullet. The paper has too many nested disclosures.

**P1B-N7 (Appendix C, p.9):** Caγ values {4, 8, 12} are fixed per chain. With only three discrete photon-coupling points, smooth marginal posterior interpretation of Caγ is impossible; the text repeatedly refers to a Caγ "envelope" as if it were sampled.

**P1B-N8 (§V.A, p.6):** "Cobaya … (v3.5 original; v3.6.1 verification)" — running two Cobaya versions for the same chain is unusual; if posteriors differ between versions this needs disclosure.

**P1B-N9 (Eq. (1), p.5):** The β-recovery equation is labeled (1) and the field-displacement equation later is labeled (2). Equation labels appear out of order across the manuscript (Eq. (1) inside §IV before any §VI equation).

**P1B-N10 (§VI, p.7):** "(see Appendix C for the full ALP-MCMC sampled-parameter list…)" — multiple "see X" references suggest the material should be consolidated.

---

## Length recommendation

For the actual scientific content (a null MCMC, a pipeline injection-recovery test, and a non-original ALP consistency check), the paper should be no more than **4–5 pages**. The current 10 pages is sustained by audit-trail prose, internal disambiguation footnotes, repeated scope disclaimers, and a misplaced w0wa headline analysis.

---

## Summary recommendation
**REJECT**

The paper fails the PRD bar on three independent grounds. (1) **Novelty:** the paper itself disowns the ECH content of all three analyses (Sec. III "Not a Spin-Torsion Theory Module"; Sec. IV "Not a competitive sky detection"; Sec. VI "Not a distinctive ECH prediction"). (2) **Substantive claims:** the most striking result — the DESI DR2 +4.3σ w₀ departure (Table II) — is presented with a footnote conceding it is neither a Bayes-factor exclusion nor a frequentist tension, model-comparison statistics are explicitly deferred, and the analysis is invisible in the abstract. (3) **Manuscript hygiene:** extensive internal review-log prose, dataset-label inconsistencies between the headline reference and the actual likelihood used (footnote a on p.1), table/text numerical inconsistencies (67.68 vs 67.69), pseudo-equation-quality arithmetic ("3.2σ corresponds exactly to the canonical 3.6σ"), discontinued PACS codes, and reference annotations containing internal cross-paper line numbers ("L256/L416 of P1B"). The paper cannot be accepted; substantial restructuring, removal of all audit-trail prose, and either dropping or properly defending the DESI w0wa analysis with nested sampling would be needed before re-evaluation.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P1B (Second Pass, Fresh-Eye Review)

I focused on arithmetic verification, cross-reference integrity, appendix-vs-body consistency, and abstract faithfulness. Several substantive issues were missed on the first pass.

---

## NEW ESSENTIAL findings

**P1B-E10 (Footnote 1, p.2–3 vs Table I, p.3, AND §VII Conclusions, p.7–8):** Footnote 1 explicitly states the third (Planck-only) combination "**is reported separately in Table I**, and is not aggregated into the 309,189-sample headline." The Conclusions section repeats: "an additional 114,992-sample Planck-only run is still accumulating … is reported separately in Table I." **Table I contains only two columns: "Full-tension" and "Planck+BAO+SN." There is no Planck-only column.** Either Table I is missing the third column, or both footnote 1 and the Conclusions contain a factually false cross-reference. **Fix:** add the Planck-only column to Table I, or correct both prose references.

**P1B-E11 (Footnote 4, p.7):** The text "the abstract spectator-status restriction θᵢ ≪ 1 (**Eq. (1)**-adjacent disclaimer)" cites Eq. (1). Eq. (1) in this paper is **β̂_NaMaster = 0.238°** (the NaMaster pipeline recovery, §IV) — it has nothing to do with the ALP spectator-status disclaimer. The spectator-status disclaimer is in the abstract and the §VI body, not adjacent to any labeled equation. This is a stale or wrong cross-reference. **Fix:** rewrite to cite the correct location (abstract or §VI body) by section, not equation.

**P1B-E12 (§VI body p.7, Conclusions p.8, fn. 4 p.7 — quantitative inconsistency on the "midpoint"):** The "25× tuning" is computed relative to "the natural prior midpoint θᵢ ∼ 0.5" (§VI body), and footnote 4 calls θᵢ = 0.5 "the scan-midpoint." **The actual sampled prior in Appendix C is uniform on [0.5, 2.0], whose arithmetic midpoint is 1.25 (geometric mean 1.0).** θᵢ = 0.5 is the *lower edge* of the prior, not the midpoint. Using the actual midpoint:
- Arithmetic midpoint 1.25: Ωₐ(0.1)/Ωₐ(1.25) = (0.1/1.25)² = 1/156 → ~**156×** tuning, not 25×.
- Geometric midpoint 1.0: Ωₐ(0.1)/Ωₐ(1.0) = 1/100 → ~**100×** tuning.

Either the "midpoint" label is incorrect, or the tuning factor understates the actual fine-tuning by a factor 4–6. Given how often "25×" is invoked across the abstract, §VI, fn. 4, and Conclusions as the load-bearing tuning quantification, this is a meaningful quantitative error. **Fix:** reconcile by either (a) redefining "midpoint" honestly as "prior lower edge" and acknowledging the quoted 25× is the most-favorable-edge case, or (b) recomputing relative to the actual prior midpoint and reporting ~100–156×.

**P1B-E13 (§VI p.7, Appendix C p.9 — βfree vs ALP-MCMC config conflation):** §VI body states "βfree = 0.344° ± 0.096° (our internal model-independent MCMC fit … **9,720 accepted samples across the 3 ALP-MCMC configurations** described in Sec. VI (configurations Caγ = 4, 8, 12…))." But Appendix C explicitly separates two distinct MCMC setups:
- **"Sampled parameters and priors (model-dependent ALP fit)":** Caγ ∈ {4, 8, 12} fixed, m/H0 and θᵢ sampled, 3,240 samples per Caγ-config → 9,720 total.
- **"Sampled parameters and priors (model-independent βfree fit)":** β alone sampled with a uniform prior, no Caγ stratification.

These are two different MCMCs. βfree cannot simultaneously be "model-independent" *and* sourced from "9,720 samples across the 3 Caγ-fixed ALP configurations." Either βfree is a separate chain (and the sample count quoted in §VI is wrong) or it's a re-projection of the model-dependent runs (in which case calling it "model-independent" is wrong). **Fix:** clarify which chain produced βfree, give that chain's actual sample count and configuration, and reconcile with Appendix C.

**P1B-E14 (Table I, Planck+BAO+SN column, S₈ row):** The Planck+BAO+SN values are σ₈ = 0.812 ± 0.009, Ωₘ = 0.312 ± 0.006, S₈ = 0.831 ± **0.018**. Two checks:
- (a) Mean consistency: S₈ = σ₈ √(Ωₘ/0.3) = 0.812 × √(1.04) = 0.828. Table reports 0.831. The 0.003 mean offset is within σ_S₈ but indicates the row is not a direct deterministic derivation (correlations matter — fine).
- (b) **σ consistency: with σ_σ₈ = 0.009 and σ_Ωₘ = 0.006, error propagation gives σ_S₈ ≈ 0.012, not 0.018.** Furthermore, the full-tension column reports σ_S₈ = 0.008 with σ_σ₈ = 0.008 (S₈ σ ≈ σ₈ σ, expected). The Planck+BAO+SN σ_S₈ = 0.018 is 2.25× larger than σ_σ₈ = 0.009, which is inconsistent with standard error propagation and inconsistent with the full-tension column behavior. This is almost certainly a typo (likely 0.008 or 0.012). **Fix:** verify Table I S₈ Planck+BAO+SN uncertainty against the chain.

**P1B-E15 (§III "M_B–H₀ joint-posterior offset check" p.4, σ-comparison conflation):** The chain returns σ_MB = 0.049 mag (marginal posterior). The Riess+2020 SH0ES prior has σ_MB = 0.027 mag. The text computes "M_B = −19.263 ± 0.049 mag, agreeing with the Riess+2020 SH0ES value MB = −19.253 ± 0.027 mag at 0.2σ" using the combined σ √(0.049² + 0.027²) = 0.056, giving 0.010/0.056 = 0.18 ≈ 0.2σ.

Two separate issues:
- (a) **Marginal-vs-conditional conflation:** The chain σ_MB = 0.049 is the H₀-marginalized posterior on M_B. The Riess σ = 0.027 is the conditional uncertainty along the SN distance-ladder constraint. Combining them in quadrature as if they were independent measurements of the same quantity is incorrect.
- (b) **Active-prior inconsistency:** If the Riess M_B prior (σ = 0.027) is actually active in the likelihood, the marginal posterior σ_MB cannot exceed 0.027 unless the H₀ marginalization is broadening it. The text claims active SH0ES likelihood and σ_MB = 0.049 > 0.027 simultaneously — this requires explicit justification via the H₀–M_B degeneracy projection, which is not given.

Combined with the body's own claim that 3.16σ (= 0.155/0.049) "corresponds **exactly** to the canonical 3.6σ Hubble tension" (already flagged in M6), the M_B audit-paragraph contains three separate quantitative confusions. **Fix:** redo the M_B consistency check explicitly along the H₀–M_B degeneracy direction, or drop the "0.2σ agreement" claim.

---

## NEW MAJOR findings

**P1B-M17 (§III p.5, "Independent cross-validation" — Liu et al. comparison):** The text claims "Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈" with Liu et al. [11]. The paper **does not quote Liu et al.'s H₀ or σ₈ values**, so the 0.5σ and 0.4σ figures cannot be verified from the manuscript. For a referee, this means the comparison is unverifiable in-text. **Fix:** quote Liu et al.'s posterior means and σ values inline.

**P1B-M18 (§VI body p.7, "[0.17, 0.43°]" envelope lower bound):** The paper claims "The prediction spans β ≈ 0.17–0.43°" over (Caγ, m/H₀, θᵢ) ∈ ([4,12], [1,3], [0.5,2]). The naive product of extremes gives:
- Upper: Caγ=12, ∆ϕ/fa=1.1 → β = (5.8×10⁻⁴)·12·1.1 = 7.66×10⁻³ rad = 0.439° ✓ matches 0.43°.
- Lower: Caγ=4, ∆ϕ/fa=0.2 → β = (5.8×10⁻⁴)·4·0.2 = 4.64×10⁻⁴ rad = **0.027°** — not 0.17°.

The paper acknowledges this: "not from an independent-extremes product (which would give the wider naive envelope [0.027, 0.44°]); ∆ϕ/fa is a function of m/H₀ and θᵢ along ALP trajectories." But **no trajectory-scan calculation is shown** that yields 0.17° as the lower bound. The reader cannot verify how 0.17° was obtained — it requires a numerical minimization over the joint (Caγ, m/H₀, θᵢ) constrained surface that is not exhibited. **Fix:** either show the scan output (range of ∆ϕ/fa as a function of m/H₀ × θᵢ from the EOM integration) or report the honest naive envelope [0.027°, 0.44°] and note that the trajectory constraint is tighter.

**P1B-M19 (§IV "ACT-noise level" attribution, p.5):** "The 500 Monte Carlo realizations are drawn at **ACT-noise level** ∆P = 10 µK · arcmin (a conservative worst-case bias check)." The analysis is on the **Planck Commander** map, whose intrinsic polarization noise is ~30–50 µK·arcmin at 143 GHz. Adding 10 µK·arcmin in quadrature gives an effective noise dominated by the Planck floor, not ACT. The "ACT-noise" framing is therefore misleading: either (a) the MC noise overrides the Commander map noise (would require source-noise-subtracted simulations on the Commander signal-only template, which is not stated), or (b) the actual effective noise floor is Planck-dominated and the "ACT-noise" attribution is incorrect. **Fix:** clarify whether the 10 µK·arcmin is added to the Commander noise or replaces it, and report the effective noise level used in the recovery.

**P1B-M20 (Table I "CAMB v1.6.5"):** As of mid-2026 (paper date), CAMB releases on PyPI are in the 1.5.x series (1.5.0 in 2023, 1.5.4 in 2024). "v1.6.5" may not exist yet. **Fix:** verify the actual CAMB version run against the public release history; correct if mis-stated.

**P1B-M21 (§II opening, parameter scope, p.2):** "The bounce scenario motivates extending ΛCDM by ∆Neff (particle production at the bounce) as a phenomenological proxy parameter." This is the **only** physical motivation given in the manuscript for the ∆Neff proxy. However, the discussion in §III footnote 2 then states the parity-even four-fermion contact operator (the only EFT operator that survives torsion elimination) is "dimension-6 and M_Pl⁻²-suppressed" with the leading effect being "a scattering-amplitude shift, **not a relativistic species**, and it does not produce a ∆N_eff at recombination." These two statements are in direct logical conflict: the abstract motivation claims ∆N_eff is the bounce-proxy parameter, while the body explicitly says the ECH spin-torsion sector does not produce ∆N_eff. The paper therefore has no coherent physical link between the proxy and the underlying theory. **Fix:** either provide a derivation linking bounce particle production to a recombination-era ∆N_eff (currently absent), or remove the bounce-motivation framing of the proxy.

**P1B-M22 (§III "Backreaction disclosure" abstract claim, p.1):** Abstract: "for θᵢ ∼ 1 the ALP energy density ρa ∼ m²fa²θᵢ² ∼ H₀²M²_Pl is of order the critical density today." With m ~ H₀, fa ~ M_Pl (reduced) and θᵢ = 1: ρa ~ H₀²M²_Pl ≈ (8π/3) ρ_crit ≈ **8 ρ_crit**, i.e., several times critical, not "of order." For unreduced M_Pl the factor is even larger. The phrase "of order the critical density" understates the magnitude by a factor ~few–10. While loose, this matters because it weakens the urgency of the spectator-status disclaimer the abstract is trying to make. **Fix:** state "several × critical density" or quote the actual factor.

---

## NEW MINOR findings

**P1B-m23 (Table I min ESS, p.3):** Reported min ESS = 4,744 (full-tension) and 4,692 (Planck+BAO+SN) against 176,240 and 132,949 total samples gives ESS/N ≈ 2.7% and 3.5%, respectively. While the R̂ values are excellent (< 10⁻³), the low ESS/N ratios indicate substantial autocorrelation. This is acceptable but the autocorrelation length is not characterized.

**P1B-m24 (Eq. (2), p.6):** "∆ϕ/fa ≈ 0.65 (m = H₀, θᵢ = 1)" — given as a single numerical value from numerical integration without any equation of motion details, a plot, or a noise estimate on the numerical integration. For a paper that hinges on the Caγ ∆ϕ/fa = 10.3 relation, the underlying ALP-trajectory integration deserves a figure showing ϕ(z) for representative parameters.

**P1B-m25 (Conclusions p.8, "LiteBIRD will settle this at ~9σ in the early 2030s"):** σ(β)_LiteBIRD ≈ 0.03°, and for β = 0.27°: 0.27/0.03 = 9.0σ ✓. But the 9σ figure is for *detection of a fiducial β = 0.27°*, not for *model-preference between the 25×-tuned spectator-ALP and ΛCDM*. The sentence "will settle this at ~9σ" conflates a detection significance with a model-discrimination significance.

**P1B-m26 (§VI, p.7, βfree vs βobs apparent identity):** "βfree = 0.344° ± 0.096°" and "βobs = 0.342° ± 0.094°" agree to 2 milli-degrees in mean and 2 milli-degrees in σ. βfree is described as an internal re-fit on "Planck PR4 + ACT DR6 EB-spectrum likelihoods" — but the published βobs = 0.342° ± 0.094° is from **PR3+WMAP9** per the abstract footnote a disambiguation. The fact that a PR4+ACT DR6 fit returns a mean and σ identical to a PR3+WMAP9 published value to 3 significant figures is implausible (different datasets, different masks, different ℓ ranges should not agree to 2 mU). Either (a) the βfree was actually fit to PR3+WMAP9 contrary to the §VI text, or (b) the agreement is coincidental, or (c) the internal fit is not what is described. The footnote-a disclosure of the labeling failure makes (a) the most likely explanation. **Fix:** state which dataset βfree actually used and reconcile with §VI body text.

**P1B-m27 (Fig. 1 thinning factor, p.5):** Caption: "119,617 post-burnin samples, getdist-thinned from 176,240 raw." Footnote 1: post-burnin (after 30% removal) is "123,368 (or 123,129 after chain-end truncation)." So 119,617 = additional 3.0–3.4% getdist-thinning of the 123,129 figure. The thinning factor is undocumented; getdist effective-sample weighting is mentioned in fn. 1 but the actual thinning prescription (autocorrelation-based?) is not stated.

**P1B-m28 (§III p.3, "98.6% quintom-B" → "zero free-w₀wa samples at LCDM point" retraction):** The retraction sentence ("An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain there are zero free-w₀w_a samples at the LCDM point") leaves unanswered: what fraction of the posterior is in the quintom-B quadrant (w₀ > −1, w_a < 0 such that w₀ + w_a < −1)? The retraction removes a wrong number but provides no replacement, so the actual posterior quintom-B fraction is undocumented.

---

## Summary

The fresh-eye pass identifies six new ESSENTIAL findings — five quantitative/cross-reference errors and one definitional inconsistency between the bounce-proxy motivation and the body's own EFT discussion. The E10 (Planck-only column missing from Table I despite explicit "reported separately in Table I" statements), E12 (the "25×" tuning factor understated by 4–6× via the "midpoint" mislabeling), E13 (βfree chain-source conflation with Appendix C), and E14 (Table I S₈ σ typo) are reproducibility-impairing errors that a referee should require be corrected before any re-review.

The overall recommendation from the first-pass review (REJECT) stands. The new findings strengthen rather than weaken the case: in addition to the structural disowning of ECH content, the manuscript contains internal quantitative inconsistencies that survived the author's stated verification process.