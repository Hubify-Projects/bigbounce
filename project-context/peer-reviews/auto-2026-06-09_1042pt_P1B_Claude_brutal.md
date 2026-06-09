# P1B auto-2026-06-09_1042pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14220 chars)
**Wall time**: 492.3s

---

# Referee Report: P1B — "Technical Verification Companion to the ECH Spin-Torsion Program"

## Overview

This manuscript is presented as a "technical verification companion" to a separate (in-preparation) Paper I(a). It documents three numerical exercises: (1) a stock-CAMB ΛCDM+ΔNeff Cobaya MCMC, (2) a NaMaster pseudo-Cℓ injection-recovery test on the Planck Commander map, and (3) a spectator-ALP consistency check against published birefringence values. The author repeatedly and emphatically disclaims that any of these analyses test the ECH spin-torsion theory or constitute distinctive predictions. After cutting through ~10 pages of scope-disclaimer prose, what remains is: (i) a null ΔNeff posterior consistent with standard ΛCDM, (ii) a pipeline-recovery bias of 0.03–0.04°, and (iii) a confirmation that an ALP with parameters tuned to match data matches data. None of this is independently publishable, and a great deal of it is in arithmetic, organizational, or representational disrepair.

I am recommending **REJECT**. The detailed findings follow.

---

## ESSENTIAL

### P1B-E1 — Table II footnote b: the displayed σ_wpivot derivation is arithmetically wrong (page 4)

Footnote b states:
> "σ²_wpivot = σ²_w0 + (1 − ap)² σ²_wa = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²"

Direct evaluation of the middle expression gives
0.0436² + (0.3320)²(0.1864)² = 0.001901 + 0.003829 = 0.005730,
i.e. σ_wpivot = √0.005730 = **0.0757**, not 0.0301.

The correct pivot variance must include the cross-covariance term:
σ²_wpivot = σ²_w0 + (1−ap)²σ²_wa + 2(1−ap)Cov(w0, wa).
Working backwards from σ_wpivot = 0.0301 and σ(w0+wa)=0.1485 one recovers Cov(w0,wa) ≈ −0.00727, consistent with the σ(w0+wa) value — but inconsistent with the formula as printed. The displayed equation is therefore both incomplete (missing cross term) and numerically self-inconsistent (its own RHS evaluates to a different number than its LHS). This is a load-bearing footnote for the headline +4.3σ claim and the "wpivot consistent with −1 at −1.1σ" framing.

**Fix:** Replace the footnote with the correct three-term formula, state the actual Cov(w0,wa) used, and verify σ_wpivot = 0.0301 reproduces from chain samples (not from algebra).

### P1B-E2 — Abstract suppresses the headline finding that actually appears in the body

The abstract concludes ΔNeff consistent with zero, H0 consistent with Planck ΛCDM, and that "the spin-torsion framework alone does not resolve cosmological tensions." Section V.B then declares as the **"headline result"**:
> "w0 = −0.812 ± 0.044 (departing from the ΛCDM point w0 = −1 at +4.3σ) and wa = −0.667 ± 0.186 (departing from wa = 0 at −3.6σ), with w0 + wa = −1.48 ± 0.15 requiring phantom crossing."

A purported >4σ joint departure from ΛCDM is not mentioned anywhere in the abstract. Either the headline w0wa claim is real (in which case the abstract is grossly incomplete and the whole framing of the paper is wrong) or it is not (in which case it should be removed). Either way the abstract and body do not describe the same paper.

**Fix:** Pick one. If the w0wa result is the headline, rewrite the abstract and reorganize the paper around it. If it is a separate auxiliary chain, demote it accordingly and stop calling it the headline.

### P1B-E3 — Three different MCMC runs presented as if they were one verification programme

The reader is asked to keep track of:
- Table I: 6-chain, 176,240+132,949 = 309,189 sample ΛCDM+ΔNeff runs;
- Table II: 16-chain, 128,385 sample w0wa run with a *different* Planck likelihood stack ("Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native + DES-Y5 + Pantheon+") and a *different* parameter dimensionality (8+9 vs 7+10);
- Appendix C: 9,720-sample ALP MCMC, 3,240 per Caγ slice, on Planck PR4 + ACT DR6 EB.

The "309,189 sample" headline in the abstract refers only to the first run. The w0wa "headline" comes from the second. The β_ALP figure comes from the third. The paper does not provide a unified table of which run, which YAML, which likelihood stack, which sampler settings, and which convergence diagnostic produced which number. This is unacceptable for a paper whose only stated purpose is technical verification.

**Fix:** Add a single Methods table listing every chain, its YAML, its dataset combination, sample counts, R̂, ESS, and which result column it feeds.

### P1B-E4 — PR3 vs PR4 ambiguity in the headline β = 0.342° ± 0.094° claim (footnote a, abstract; §VI)

Footnote a on page 1 candidly admits that the "0.342° ± 0.094° (3.6σ)" headline is from the *published* PR3+WMAP9 analysis, while the ALP-MCMC re-runs that produce β_ALP = 0.336° ± 0.107° use the *repository* code, which was subsequently updated to PR4/NPIPE. The model fit (β_ALP) and the observed value (β_obs) the body claims it is consistent with are therefore against **different datasets**. This is not a minor labelling issue: a likelihood-level fit against PR4 cannot be quoted as "consistent with the published PR3 headline" without an explicit error budget for the dataset swap. The author neither closes nor quantifies this gap; the "disambiguation" footnote merely acknowledges it exists.

**Fix:** Either re-quote the published value against the actual dataset used in the MCMC, or refit against the PR3+WMAP9 likelihoods. Stop quoting cross-dataset agreements as scientific consistency.

### P1B-E5 — Review-log/internal-bookkeeping prose throughout the body

Multiple sentences appearing in the rendered PDF are clearly responses to (presumably internal) reviewer correspondence and have no place in a PRD submission. Each of the following must be flagged and removed:

- §III (page 3): "An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain there are zero free-w0wa samples at the LCDM point..."
- §III (page 3) Caveats (a): "(note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but with zero free-w0wa samples at the LCDM point the KDE estimator fails catastrophically)."
- §III (page 4): "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood..."
- §III (page 4–5): "MB–H0 joint-posterior offset check. A concern was raised that the joint posterior mean (MB = −19.263, H0 = 67.69) was inconsistent with an active sn.pantheonplus likelihood, claiming a Cobaya YAML alias failure. Direct arithmetic audit: ..." [entire paragraph]
- §IV (page 6): "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°, a relative ∼ 12% amplitude-dependent component."
- §VI footnote 5 (page 7): retains the "[0.5, 2]" prior "for envelope-completeness purposes" while admitting it is "not the spectator-consistent sub-range" — i.e. the prior is left in for legacy reasons rather than physics.
- Section III heading parenthetical "(NOT A SPIN-TORSION THEORY MODULE)" — this is review-response language inside a section title.

This is a real PRD submission, not a versioned response document. Whatever prior reviewers asked, the manuscript must read as the *final* version, not as a real-time defense of past mistakes.

**Fix:** Strip every "earlier count," "an earlier reviewer," "concern was raised," "initially characterized," "this addresses" sentence. State the correct numbers and methods only.

### P1B-E6 — Abstract over/understates NaMaster bias

The abstract states the recovery bias as "0.032°," derived from the β = 0.27° injection only. The body (§IV, page 6) and §VII concede the worst-case bias is **0.040°** for the β = 0.342° injection. The abstract is therefore not the worst-case figure. Fig. 3's caption further claims "Bias β̂ − βinj is below 0.04° across the natural resolution range" — at 0.040° exactly this is at best borderline-false and at worst dishonest.

**Fix:** Quote the worst-case bias (0.040°) in the abstract and the figure caption, and report both bias values explicitly in the abstract.

### P1B-E7 — Spectator label requires fine-tuning the author calls "∼ 25×" — buried in footnote, abstract gives the misleading "natural parameters" framing

Abstract: "Spectator-ALP consistency check: a field with fa ∼ MPl, m ∼ H0 is consistent with the published joint WMAP+Planck value..."
The body and footnote 5 then disclose that the spectator status (Ωa ≪ 1) requires θi ~ 0.1, a ∼25× tuning relative to the natural-prior midpoint θi = 0.5, and that this in turn forces Caγ outside KSVZ/DFSZ benchmarks (the body quotes a required range 9 ≤ Caγ ≤ 51, "the entire required range therefore lies outside minimal ALP photon-coupling benchmarks"). The abstract presents this as a consistency check on "natural" parameters; the body shows it is not consistent on natural parameters and requires either misalignment fine-tuning or non-minimal photon couplings. The abstract is misleading.

**Fix:** State in the abstract that the spectator-consistent corner requires (a) θi ≈ 0.1 misalignment tuning and (b) Caγ ~ 9–51, outside minimal benchmarks.

### P1B-E8 — "Independent cross-validation" with Liu et al. (page 5) is unsupported and likely circular

The text reads:
> "Liu et al. [11] constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (∆AIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8."

No table or figure shows Liu's H0 or σ8 values, no covariance for the σ-distance is specified, and Liu's paper studies a different physical model. Agreement in H0 and σ8 between a torsion-extended fit and a stock-CAMB ΔNeff fit is not "independent verification" of either. This paragraph either needs the Liu numbers, the formal definition of "σ agreement" used, and the explicit caveat that the two extensions are physically distinct — or it must be deleted.

---

## MAJOR

### P1B-M1 — What does this paper actually prove?

After applying the author's own scope statements, the residue is:
1. A null ΔNeff posterior — not new (Planck, ACT, BICEP, DESI have all found this).
2. A NaMaster injection-recovery test confirming the pipeline is unbiased at 0.04° — not new; NaMaster is a published, validated tool [Alonso et al. 2019].
3. A confirmation that a tuned ALP can produce a tuned β — not new; Fujita et al. 2021 [21] did this first and the author cites them.

The paper itself states each result "is not a distinctive ECH prediction," "is not a sky measurement," and "does not test the spin-torsion theory module itself." If none of the analyses test the theory and none are independently new, the paper has no scientific deliverable.

**Fix:** State a single quantifiable falsifiable claim that this paper, on its own, establishes. If none exists, the paper should be merged into Paper I(a) as an appendix.

### P1B-M2 — Sample-count inconsistencies between Fig. 1, Fig. 2, Table I, and footnote 1 (pages 2–3, 5)

- Table I row "Total samples" full-tension: 176,240.
- Footnote 1: post-burnin 176,240 × 0.7 = 123,368, but Fig. 1 caption gives 119,617 ("getdist-thinned"); the explanation is a parenthetical, not a documented procedure.
- Fig. 2 caption gives "175 545 samples" for full-tension — **neither 176,240 nor 119,617**. No footnote reconciles this.
- "the post-burnin count of the full-tension subset alone is 123,129 (within ±1% of the 123,368 exact computation, with the small offset reflecting the chain-end-truncation of partial samples at the burn-in cut)" — so now there are also 123,129 samples, and the discrepancy is hand-waved as "within ±1%."

Four different numbers for what should be the same chain, all in the same paper. This is sloppy.

**Fix:** Reconcile to a single canonical post-burnin count per chain.

### P1B-M3 — Worst R̂−1 = 0.003 reported as converged is borderline

PRD-grade MCMC convergence is conventionally R̂−1 < 0.01 (acceptable), with < 0.001 preferred for headline cosmological constraints. The Planck+BAO+SN chain at R̂−1 = 0.003 across 17 parameters with min ESS = 4,692 is marginal for parameters appearing at the percent level (S8, σ8). The third "Planck-only" chain at R̂−1 ~ 0.05 is reported as "ongoing" but quoted in Table I — it is unconverged by any reasonable standard and should be removed or labelled "preliminary, do not cite."

**Fix:** Either continue the chains to R̂−1 < 0.001 or quote uncertainties inflated to account for residual chain noise.

### P1B-M4 — Bayes factor / model comparison "deferred" — but the headline w0wa claim depends on it

§V.B candidly admits no ∆AIC, ∆BIC, or ln B is computed, that a Savage-Dickey readout fails (ΛCDM point unsampled at >4σ), and that "robust ln B computation requires nested sampling." Yet the body then states as the "headline result" that w0wa departs from ΛCDM "at +4.3σ" and is "requiring phantom crossing (the canonical quintom signature)." A purely marginal-tail extrapolation is **not** a model-rejection σ — and the author flags this themselves in footnote a of Table II — but the framing in §V.B, §VII, and the discussion narrative reads as if a quintom preference has been established.

**Fix:** Run PolyChord/MultiNest on the same likelihood stack and quote ln B. Until then, do not call a posterior-tail distance a "headline result" or a "departure at +4.3σ."

### P1B-M5 — Equation (3) is dimensionally unclear

§VI Eq. (3): "β ≈ (αEM × 8 / 4π) × 1.07 ≈ 0.29°"
The RHS in radians is αEM·8/(4π)·1.07 ≈ 4.97×10⁻³ rad, which converts to 0.285° — fine, but the equation appears to equate a dimensionless number on the left to a degree-valued number on the right without an explicit rad → deg conversion. Either the equation needs `(180°/π)` explicit or the result needs to be in radians.

**Fix:** Write the conversion factor explicitly.

### P1B-M6 — Spectator-ALP MCMC details are insufficient (Appendix C is one page)

The β_ALP, β_free fits are quoted to three significant figures, but Appendix C contains essentially: (i) Caγ fixed to {4, 8, 12}, (ii) m/H0 ∈ [1, 3] uniform, (iii) θi ∈ [0.5, 2] uniform, (iv) fa fixed at MPl. 9,720 samples across 3 configurations = 3,240 per config. There is no convergence diagnostic per config (only "R̂ − 1 < 0.01 for all runs"), no posterior corner plot, no chain trace, no likelihood description beyond "Planck PR4 + ACT DR6 EB-spectrum likelihoods... combined with shared calibration covariance." 3,240 samples per configuration with a 2D parameter posterior is borderline thin.

**Fix:** Provide chain diagnostics, prior plots, and a posterior corner plot for the ALP fit.

### P1B-M7 — Footnote 1 is doing the work of a Methods subsection

Footnote 1 on page 2 runs nearly half a column reconciling sample-count numbers. Footnotes are not the place for paper architecture. This material belongs in §III as a Methods paragraph.

### P1B-M8 — Footnote 2 EFT cutoff Λstrong ∼ MPl/√γBI is unjustified inside a footnote

The footnote asserts the four-fermion EFT breaks down at Λstrong ∼ MPl/√γBI but cites only one paper (Mercuri 2006). For a paper whose central claim is that ECH effects can be encoded as a ΔNeff proxy at recombination, the cutoff that justifies the EFT framing should be in the body and supported.

### P1B-M9 — Fig. 3 caption claim "Bias β̂ − βinj is below 0.04° across the natural resolution range"

For β_inj = 0.342° the bias is 0.040° per the body. Stating it is "below 0.04°" in the figure caption is at best ambiguous, at worst false. The caption should report the actual maximum bias across the injections shown.

### P1B-M10 — Abstract is over-long and mostly disclaimer

The abstract runs ~600 words and is roughly 70% scope disclaimers ("Not a Spin-Torsion Theory Module," "Scope of the validation," "Spectator-status caveat," "is not a distinctive ECH prediction"). PRD abstracts should communicate the results, not pre-emptively disclaim them. If the results require this many caveats, the paper isn't ready.

### P1B-M11 — Sec II is a single paragraph that says nothing not said elsewhere

Section II ("Cosmological Tensions: H0 and σ8") contributes no result. It states that "(ω/H)0 and Ωk are fixed to zero" and that SH0ES is included but Planck dominates. Both points are repeated in §III and §V. Delete or merge.

### P1B-M12 — Self-citations to "(in preparation)" papers

References [1], [4], [5], [6] are all author's own "(in preparation)" papers identified by internal tag "HUBIFY-2026-XXX." A companion paper that depends critically on an unpublished primary paper (Paper I(a)) cannot be assessed by referees without that primary paper. PRD does not accept such forward-references.

**Fix:** Submit Paper I(a) simultaneously, or restructure to be standalone.

### P1B-M13 — The angular-momentum parameter (ω/H)0 is invoked, mentioned as "phenomenological bounce-class indicator," then never quantified

§V.A: "both (ω/H)0 and Ωk fixed to zero in the actual sampled YAML." If (ω/H)0 is the parameter that would actually distinguish the ECH bounce from ΛCDM, fixing it to zero and then doing a ΔNeff proxy fit is fitting a model that has no spin-torsion content. This makes the disclaimer in the abstract ("not a torsion modification") not a methodological caveat but a fundamental indictment of the entire MCMC programme.

---

## MINOR

### P1B-N1 — Eq. (2) and the "midpoint" inconsistency
Eq. (2): "∆ϕ/fa ≈ 0.65 (m = H0, θi = 1)."
Text immediately below: "β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H0, ∆ϕ/fa ≈ 1.0."
The midpoint of m/H0 ∈ [1, 3] is 2, not 1.8. The midpoint Δφ/fa is not reported and 1.0 doesn't match Eq. (2)'s 0.65 at θi=1. Reconcile.

### P1B-N2 — "Independent verification (production 500-realization run, April 2026)" (§IV, page 6)
"Independent" of what? The author is the sole author. This is not an independent verification; it is the author re-running their own pipeline. Drop the "independent" framing.

### P1B-N3 — Eq. (4) labelled "(3.9)" — formatting unclear
The "(3.9)" should be "3.9σ" or formatted distinctly from the equation number.

### P1B-N4 — Inverse-variance combination presented but disowned
§VI presents Eq. (4) inverse-variance combination yielding 3.9σ, then immediately calls it an "Auxiliary cross-check only" and an "upper bound on the true significance." If it isn't used, don't display it. If it is, integrate it into the result properly.

### P1B-N5 — Acknowledgment paragraph about AI usage
"The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation." This is fine policy-wise but combined with the single-author independent-researcher framing and the visible review-log prose (E5), it raises questions about the manuscript-preparation pipeline.

### P1B-N6 — Reference [10] arXiv ID is not hyperlinked; year mismatch
Cai, Xue, Brandenberger, Zhang, "Non-gaussianity in a matter bounce," JCAP 0905 (2009) is OK but the year "2009" is missing from the bibliographic line. Standardize the format.

### P1B-N7 — Reference [12] DESI DR2 II paper attributed to "M. Abdul-Karim"
The DESI papers are large-collaboration outputs. Standard PRD style is "DESI Collaboration, M. Abdul-Karim et al." which the entry does say, but verify the alphabetical first-author convention against published.

### P1B-N8 — Section III statement "ΔNeff = −0.020 ± 0.169 (full-tension) and +0.065±0.17"
±0.17 vs ±0.169 — inconsistent significant-figure precision between the two combinations. Use a consistent precision (presumably 0.169 and 0.170).

### P1B-N9 — "BAO + CMB + SN-only, no local-distance ladder" (page 4)
After stating in §III that "the full-tension dataset combination includes the SH0ES H0 prior," §III(c) on page 4 then says about the Table II run "(BAO + CMB + SN-only, no local-distance ladder)." This switch between which chain is being discussed is confusing on first reading.

### P1B-N10 — Fig. 2 sub-caption (b) labels and units
The right panel labels read "(x − xfull_tension) / σfull_tension" but the panel has no clear axis title in the version I can read. Verify legibility.

### P1B-N11 — Inconsistent km/s/Mpc unit formatting
The abstract uses "km s⁻¹ Mpc⁻¹" while Table I/II use "[km/s/Mpc]." Standardize to PRD style.

### P1B-N12 — "k = 7" mentioned only in Table I footnote a
The Table I footnote a says "references to 'k = 7' elsewhere in this paper refer to the cosmological-parameter count only" but no such reference appears elsewhere in the body I can find. Either the footnote refers to a deleted section or the reference is missing. Suggests editing-state residue.

### P1B-N13 — "frozen" used as a technical term without definition
"frozen MCMC program," "two frozen dataset combinations," "frozen posterior" — the word "frozen" is doing a lot of work without ever being defined. Define on first use.

---

## Page-count assessment

The actual scientific content here is roughly two pages: the ΔNeff posterior summary, the NaMaster bias number, and the ALP MCMC posterior. The remaining 9 pages are scope statements, disclaimer footnotes, defensive-explanatory paragraphs against unnamed reviewer concerns, and the unrelated w0wa "headline." Recommended maximum page count if the paper were rewritten as a focused methods note: **4 pages including refs**.

---

## Summary recommendation

**REJECT**

The paper does not establish a scientific result that the author themselves is willing to claim. Each of the three analyses is followed by a disclaimer that it is not what it appears to be: the MCMC is "not a spin-torsion theory module," the NaMaster recovery is "not a competitive sky measurement," the ALP fit is "not a distinctive ECH prediction." The "headline" w0wa quintom departure is not in the abstract, is computed without the model-comparison machinery required to support it (Savage-Dickey fails by the author's own admission), and contradicts the rest of the manuscript's "ΛCDM is fine" framing. Table II footnote b contains a numerically wrong equation (P1B-E1). The PR3-vs-PR4 dataset mismatch is acknowledged in a footnote but not corrected (P1B-E4). The body retains visible review-log artifacts — "an earlier count erroneously quoted," "a concern was raised," "this addresses earlier reviewer concerns" (P1B-E5). The abstract substantively misrepresents the bias (P1B-E6) and the "natural parameters" framing of the ALP (P1B-E7). Sample counts disagree across the abstract, Table I, footnote 1, Fig. 1, and Fig. 2 (P1B-M2). Critical inputs depend on an unpublished primary paper (P1B-M12). A complete rewrite around a single quantifiable claim, against a single internally-consistent likelihood stack, with the review-history language excised, would be required before resubmission to PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

# Supplementary Findings — Second-Pass Review of P1B

After a systematic re-pass through the manuscript using the rubric above, the following new issues emerge. These are in addition to (not replacing) the items in my initial review.

---

## ESSENTIAL (new)

### P1B-E9 — Fig. 3 title contradicts the body text on which Planck map was analyzed (page 6, vs §IV page 5)

Fig. 3's figure title reads:
> "Cosmic birefringence β vs map resolution (NaMaster, **Planck SMICA**)"

But §IV explicitly and repeatedly states the analysis was performed on the **Planck Commander** map (e.g., "The Planck Commander Q/U maps are provided at Nside = 2048..."; "We performed a NaMaster pseudo-Cℓ analysis on the Planck Commander map with 500 MC noise realizations"; "The Commander map is a foreground-cleaned CMB-only product..."). SMICA and Commander are *different* component-separation pipelines with materially different foreground-residual properties (in particular different residual dust/synchrotron leakage in B). The paper does not state which one was actually used; one of the two is wrong. Given that the entire purpose of §IV is methodological validation, the input data identity must be unambiguous.

**Fix:** Determine which map was actually used. Correct the figure title or the body text accordingly, and add a note explaining why the choice matters for the β–α degeneracy discussion in the abstract.

### P1B-E10 — Table II footnote b: the decorrelation pivot ap = 0.6680 is inconsistent with the implied posterior covariance (page 4)

Extending E1: working backwards from σ(w0+wa) = 0.1485, σ(w0) = 0.0436, σ(wa) = 0.1864 yields Cov(w0, wa) ≈ −7.3×10⁻³. The standard decorrelation pivot is
ap = 1 + Cov(w0, wa)/σ²_wa ≈ 1 + (−7.3×10⁻³)/(0.03474) = **0.790**, **not 0.668**.

The footnote's stated formula `ap = 1 − Cov(w0,wa)/Var(wa)` is also wrong-signed: applied to the implied Cov it yields ap = 1.21, not 0.668. There is no consistent choice of (Cov, formula) under which both ap = 0.668 *and* σ_wp = 0.0301 reproduce. The footnote contains at minimum: a sign error in the decorrelation formula, an incorrectly stated σ²_wp formula (E1), an internally inconsistent numerical evaluation (E1), and a pivot ap whose value is unsupported by the chain's own posterior covariance. This compromises the entire wpivot = −1.034 ± 0.030 "consistent with −1 at −1.1σ" framing.

**Fix:** Recompute ap and σ_wp directly from chain samples using `getdist` or equivalent, and quote the actual posterior Cov(w0, wa) explicitly.

### P1B-E11 — Manuscript dated 2026-06-08 PDT — date is in the future

The cover line reads "(Dated: 2026-06-08 PDT)". References [3], [11], [12] are 2025 arXiv preprints; references [4], [5], [6] are "(in preparation)" by the same author and dated "2026". PRD does not accept manuscripts dated in the future, and the choice of June 2026 cannot be reconciled with the apparent submission timeline. This signals either a copy-paste error from a draft template or an attempt to forward-date the work.

**Fix:** Use the actual submission date.

### P1B-E12 — Reference list contains internal editorial line-number annotations (page 11)

Reference [15] (Diego-Palazuelos et al. 2022) carries the note:
> "reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at **L256/L416 of P1B**"

Reference [22] (Cai et al. 2010 quintom review) carries the note:
> "canonical quintom-cosmology review... Used in **P1A Sec. VI** to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers"

Reference notes are not the place for internal source-line annotations ("L256/L416 of P1B") or cross-paper editorial notes ("Used in P1A Sec. VI"). This is reviewer-facing or draft-internal text that has been published-typeset by mistake.

**Fix:** Strip all internal editorial annotation from bibliography entries.

---

## MAJOR (new)

### P1B-M14 — DESI DR1 vs DR2 confusion across runs (§V.A vs Table II)

§V.A explicitly states the dataset combinations use **"DESI 2024 DR1 BAO [18]"** (reference [18] = arXiv:2404.03002, DESI 2024 VI). Table II's likelihood stack uses **"DESI DR2 BAO"** (reference [12] = arXiv:2503.14738, DESI DR2 II). The two BAO releases are not interchangeable: DR2 BAO has approximately a factor √2 tighter errors and shifted central values relative to DR1, and the published DESI w0wa tension depends sensitively on which release is used. The paper switches between releases without acknowledging this affects which result applies to which dataset.

**Fix:** Make explicit which chain used which DESI release, and harmonize the dataset-citation language across §V.A, §V.B, Table II, and the Conclusions Forward paragraph.

### P1B-M15 — "Planck 2018 NPIPE" is a contradictory dataset label

Multiple instances (§V.A, Table II caption, abstract) use "Planck 2018 NPIPE." Planck NPIPE is the PR4 reprocessing released in 2020 (with the official likelihood paper, Rosenberg, Gratton, Efstathiou 2022); the 2018 release is PR3. The two are different sky reconstructions with different noise residuals and slightly different inferred cosmologies. "Planck 2018 NPIPE" is not a coherent dataset name.

**Fix:** Use either "Planck PR3 (2018)" or "Planck PR4 (NPIPE)" and cite the appropriate likelihood paper (Rosenberg, Gratton, Efstathiou 2022 is not currently in the bibliography even though "CamSpec NPIPE" is used).

### P1B-M16 — DES Y3 vs DES-Y5 confusion

§V.A lists the fourth dataset combination as "+SH0ES H0 prior [7] + DES Y3 S8 [19]" with ref [19] = DES Y3 weak-lensing cosmology. Table II's likelihood stack uses "DES-Y5 + Pantheon+" with the DES Y5 SNe reference [14]. DES Y3 (weak lensing) and DES-Y5 (Type Ia SNe) are *different* DES products with different physical content; the paper's prose conflates them as "DES" data. The two also enter the chain in completely different ways (S8 vs distance moduli).

**Fix:** State the two DES products and their physical content separately.

### P1B-M17 — A fifth sample count (175,545) appears in Fig. 2 caption with no reconciliation

In addition to the four sample counts I flagged in M2 (176,240, 123,368, 119,617, 123,129), Fig. 2(a) panel caption introduces a fifth: "Full tension (**175 545 samples**)." This number is 695 below the Table I raw count (176,240) and is not derivable from any documented thinning procedure. The Planck+BAO+SN number in the same caption (132,949) matches the Table I raw count — so Fig. 2 is mixing one pre-thinning and one post-thinning number within a single figure, inconsistently.

**Fix:** Document the exact getdist thinning, sample-cut, and weighted-sample procedure that produces each number, and reconcile to a canonical count per chain.

### P1B-M18 — Table III's "Verified" status for β_ALP = 0.336° ± 0.107° overclaims given the chain size

Table III labels the β_ALP = 0.336° ± 0.107° result as "Verified" using 9,720 accepted samples *across three configurations* — i.e., 3,240 per Caγ slice. With a 2D non-Gaussian posterior (m/H0, θi) and a fixed Caγ axis, 3,240 effective samples per configuration is at the marginal lower bound of what would normally support a published parameter estimate, and the per-configuration ESS, autocorrelation, and convergence statistics are not reported anywhere in the paper. "Verified" is too strong.

**Fix:** Either tighten the ALP-MCMC convergence diagnostics with per-configuration ESS / R̂ reports, or downgrade the label to "Indicative."

### P1B-M19 — Eq. (3)'s "1.07" multiplier is undefined

§VI Eq. (3): "β ≈ (αEM × 8 / 4π) × 1.07 ≈ 0.29°." The numerical multiplier 1.07 is not defined in the text. From context it is presumably ∆φ/fa evaluated at the specific (m = 2H0, θi = 1) point, but this is never stated. The very next sentence then asserts "The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H0, ∆ϕ/fa ≈ 1.0" — i.e., a *different* value of ∆ϕ/fa, ostensibly for the abstract's β = 0.27° fiducial. The reader is left to guess at the relationship between Eq. (2) (∆ϕ/fa = 0.65 at m=H0, θi=1), Eq. (3)'s 1.07, and the "midpoint" 1.0.

**Fix:** Define every numerical factor in Eq. (3) and tabulate ∆ϕ/fa at the (m, θi) corners actually used.

### P1B-M20 — Missing CamSpec NPIPE likelihood citation

§V.A says the proxy run uses "Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing." The CamSpec NPIPE likelihood is from Rosenberg, Gratton & Efstathiou (MNRAS 517, 4620, 2022) — that paper is not cited in the bibliography. For a paper whose core ΔNeff number depends on the NPIPE CamSpec implementation specifically (which differs materially from the public Plik likelihood), the underlying likelihood paper is a required citation.

**Fix:** Add Rosenberg, Gratton, Efstathiou 2022 and explicitly cite it at the §V.A dataset description.

### P1B-M21 — Two different H0 posteriors from two ostensibly compatible chains, not reconciled

Table I: H0 = 67.68 ± 1.06 (ΔNeff full-tension chain). Table II: H0 = 67.185 ± 0.455 (w0wa chain). The two chains use overlapping data and overlapping cosmological parameters, but report H0 values shifted by ≈0.5 km/s/Mpc with errors differing by a factor 2.3. The text attributes neither the shift nor the error reduction explicitly. Some of this is the open ΔNeff direction in chain 1; some is the added DESI DR2 in chain 2; some is the addition of CamSpec high-ℓ in chain 2. None of this is broken down for the reader.

**Fix:** Include a comparison table of the H0/Ωm/σ8 posteriors from both chains with explicit attribution of which dataset/parameter difference accounts for which shift.

---

## MINOR (new)

### P1B-N11 — Riess+2020 vs Riess+2022 mislabelling
The page-4–5 MB–H0 discussion repeatedly invokes "Riess+2020 SH0ES value MB = −19.253 ± 0.027" and "Riess+2020 anchor (MB = −19.253, H0 = 73.04)" but the only Riess reference in the bibliography is [7], Riess et al. **2022** (ApJL 934, L7). The MB = −19.253 ± 0.027 value is from a different Riess paper. Either cite the correct paper or update the in-text date stamps.

### P1B-N12 — PACS classification numbers are obsolete
"PACS numbers: 98.80.-k, 95.36.+x, 04.50.Kd" — PACS was retired in 2010 and replaced by PhySH for PRD submissions. Update.

### P1B-N13 — Section III footnote 2 introduces a UV cutoff Λ_strong ∼ MPl/√γ_BI in a footnote
The justification for the four-fermion EFT validity below Λ_strong ∼ MPl/√γ_BI is given in a footnote and is the only physics content connecting Holst-sector torsion to the ΔNeff proxy. This is too important to live in a footnote.

### P1B-N14 — Fig. 3's y-axis label and the body's "natural resolution range" phrasing
The fig caption phrases the bias as "below 0.04° across the natural resolution range" but the actual NSIDE-dependent values at NSIDE = 256 and 2048 in the plot are nowhere quoted in the body — the figure shows the bias drifts with resolution but the only number tracked in the text is from NSIDE = 512. A table of (NSIDE, β̂, σ_β̂, bias) would be more honest than the figure's loose verbal characterization.

### P1B-N15 — Min ESS per chain not reported
Table I reports total min ESS (4,744; 4,692). With 6 chains, per-chain ESS ~790 is modest, but neither the per-chain breakdown nor the autocorrelation length is reported. For a "publication-quality" claim this should be in the table or its caption.

### P1B-N16 — Reference [11] description does not match the cited title
Reference [11] is described in the §III body as constraining "an EC torsion model" with ΔAIC = −5.7 to −6.6. The reference is "Liu, X. Li, T. Xu, M. Biesiada, J. Wang, Torsion cosmology in the light of DESI..." (arXiv:2507.04265). The "EC torsion" claim and the AIC numbers should be verified against the actual cited paper; presently no page/section/table number from Liu et al. is given.

### P1B-N17 — §VI in-line claim "Caγ between ∼9 and ∼51" needs the joint-prior support
The derived Caγ range arises from the natural envelope ∆φ/fa ∈ [0.2, 1.1]; the lower endpoint 0.2 corresponds to (m/H0=3, θi=0.5), which is the most heavily-damped corner. But the spectator-consistent θi ∼ 0.1 corner (footnote 5) gives ∆φ/fa proportionally smaller, pushing the required Caγ even higher. The "∼ 9 to ∼ 51" range therefore *understates* the required photon coupling for the spectator-consistent regime — by another factor of ∼5 it would be 45–255. The §VII conclusion phrasing ("Caγ between ∼9 and ∼51") should make this explicit.

### P1B-N18 — Section II self-references its own footnote logic recursively
§II concludes: "We do not therefore claim that the SH0ES tension is resolved or even moved by adding ΔNeff in stock CAMB." Then §III concludes the same thing. Then §VII concludes the same thing. Three sections, one finding.

### P1B-N19 — "MPI chains" in §VII Forward paragraph
"128,385 accepted samples across 16 MPI chains" — but "MPI chains" is not standard MCMC terminology; the appropriate phrase is "16 chains run in parallel via MPI." Minor stylistic issue but indicative.

### P1B-N20 — Conclusions paragraph "LiteBIRD will settle this at ∼ 9σ in the early 2030s"
"In the early 2030s" — LiteBIRD's published launch target is 2032, so this is broadly correct, but a precise launch-year-to-data-release timeline citation from the LiteBIRD collaboration would be more appropriate.

---

## Summary of second pass

The most consequential new findings are **E9** (figure-caption / body-text data mismatch — SMICA vs Commander), **E10** (Table II decorrelation pivot internally inconsistent — extends E1), **E11** (manuscript dated in the future), **E12** (editorial annotations leaked into the bibliography), and **M14–M17** (multiple dataset-citation inconsistencies — DR1 vs DR2, PR3 vs PR4, DES Y3 vs Y5, and a fifth sample-count number in Fig. 2).

Taken together with my initial review, the cumulative pattern is a manuscript that has been heavily edited in response to internal review without ever being read end-to-end in a single coherent pass. The dataset labels, sample counts, and arithmetic do not close. Combined with the original recommendation of **REJECT**, these findings strengthen that recommendation: the manuscript is not in a state where a referee can verify what was actually computed.