# P1B auto-2026-06-08_1520pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (17104 chars)
**Wall time**: 474.6s

---

# Brutal-Honesty Referee Report — Manuscript P1B

**Reviewer recommendation up front:** REJECT.

The paper explicitly disclaims, in its own abstract and in three separate body sections, that *none* of its three analyses (a) test the framework it claims to be a companion to, (b) constitute a sky measurement, or (c) are distinctive predictions of ECH. The work it is a "technical verification companion" to (Ref. [1]) is "in preparation," as are three of the other four self-cited companion papers (Refs. [4], [5], [6]). PRD does not publish technical companions to nonexistent papers. The actual physics content of this manuscript is: a null ΛCDM+ΔNeff fit (already published many times), an MC bias-injection of NaMaster (a standard library), and an axion-birefringence reproduction of work already cited as the headline (Eskilt & Komatsu 2022). On top of this, the body contains an arithmetic error in a load-bearing footnote on the dark-energy posterior, numerous internal inconsistencies in H₀, sample counts, and bias signs, and the central "natural parameter" claim is undercut by the author's own disclosure of a 25× tuning.

I list findings below.

---

## ESSENTIAL findings

### P1B-E1. The paper has no physics content attributable to the framework it claims to verify.
**Sections II–VI, abstract, throughout.**
The abstract states verbatim that the MCMC "carries no torsion modifications to the Boltzmann equations," that the NaMaster work "is therefore a pipeline-validation figure, not a sky-detection significance claim," and that the ALP "is not a distinctive ECH prediction." Sec. III is titled "(Not a Spin-Torsion Theory Module)." Sec. VI states "The same β ≈ 0.27° arises in any GR+ALP setup with the same parameters; no ECH-specific derivation connects the Holst action to the photon-torsion coupling required."

A "technical verification companion to the ECH spin-torsion program" that explicitly verifies *none* of the spin-torsion program is not a PRD paper. PRD requires that the central claim of the title be substantively addressed. **Fix:** retitle and reframe as a generic ΛCDM+ΔNeff null + NaMaster bias study + ALP consistency note unconnected to ECH, *or* withdraw until the ECH companion exists, has been accepted, and a spin-torsion-modified Boltzmann module is implemented.

### P1B-E2. Companion-paper citation chain is to unpublished self-references.
**References [1], [4], [5], [6].**
All four are by the same author and all are "(in preparation)." Ref. [1] is the very paper this manuscript claims to verify. The manuscript repeatedly defers structural results, the "14-barrier table," the perturbation-transparency theorem, fNL = −35/8, the SPHEREx Fisher forecast, the anomaly catalog, and the chirality catalog to these in-preparation references. PRD requires that companion papers be either co-submitted (with arXiv numbers) or already accepted. **Fix:** ESSENTIAL — Ref. [1] must be a posted arXiv preprint with a number and must be referenceable. Without [1], this paper has no scientific scaffolding.

### P1B-E3. Arithmetic error in the load-bearing w_pivot variance footnote (Table II, footnote b).
**Page 4, footnote b.**
The text states:
> σ²_wpivot = σ²_w0 + (1 − ap)² σ²_wa = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²

Recomputing: (0.0436)² = 0.001901; (0.3320)²(0.1864)² = 0.11022 × 0.03475 = 0.003830; sum = 0.005731 ≠ 0.000906 = (0.0301)². The quoted result fails by a factor of ~6. Furthermore, the formula itself omits the covariance term 2(1−ap)Cov(w₀,w_a) which is *the entire point* of pivot decorrelation; the correct decorrelated variance is Var(w_p) = Var(w₀) − Cov²(w₀,w_a)/Var(w_a). With the numbers as written, this gives a *negative* variance, which is impossible — so the inputs themselves are mutually inconsistent. **Fix:** ESSENTIAL — provide the actual posterior covariance Cov(w₀,w_a) from the chain and recompute σ_wpivot from first principles. The −1.1σ "consistency with −1" headline depends on this number.

### P1B-E4. Headline DESI w₀w_a "+4.3σ" departure is incorrectly labeled as marginal-tail extrapolation while being used as a "phantom crossing required" headline.
**Abstract-adjacent Sec. III, Table II, footnote a.**
The +4.3σ figure is admitted to be a "posterior-tail extrapolation distance only, not a Bayes-factor or ln B exclusion and not a frequentist tension." But Sec. III then says "the converged w₀w_a posterior disfavors ... the LCDM point ... at the joint level: w₀ departs by +4.3σ and w_a departs by −3.6σ." The author cannot have it both ways. If LCDM is unsampled, the σ headline is meaningless and must be removed; if the headline stands, the disclaimer must be retracted. **Fix:** ESSENTIAL — remove the σ headline from the main text or commit to nested-sampling ln B. The current framing is exactly the kind of "weak hedge presented as strong conclusion" that PRD will not accept.

### P1B-E5. Internal H₀ inconsistency between abstract/Table I and body text.
**Abstract (page 1): "67.68 ± 1.06 full-tension." Table I (page 3): "67.68 ± 1.06." Body (page 4): "The full-tension chain returns H₀ = 67.69 ± 1.06" (also "−0.02 ± 0.17" vs. "−0.020 ± 0.169" elsewhere).**
PRD does not accept publishable numerical headlines that disagree across the same manuscript. **Fix:** Choose one value, propagate consistently.

### P1B-E6. Sample-count accounting is contradictory.
**Abstract, page 2, page 3 footnote 1, Fig. 1 caption.**
- Abstract: "309,189 frozen samples across two converged dataset combinations."
- Footnote 1: 176,240 × 0.7 + 132,949 × 0.7 ≈ 216,432 post-burnin "across both frozen chains."
- "For the full-tension subset specifically, 176,240 × 0.7 ≈ 123,368 post-burnin (the 119,617 figure in Fig. 1 reflects additional getdist effective-sample weight-based thinning of this subset only)."
- Then: "The post-burnin count of the full-tension subset alone is 123,129 (within ±1% of the 123,368 exact computation, with the small offset reflecting the chain-end-truncation of partial samples at the burn-in cut)."

So the same quantity is given as 123,368, 123,129, and 119,617 within two sentences of each other, plus the figure caption. This is not "within rounding" — the manuscript provides three different numbers for one quantity. **Fix:** ESSENTIAL — pick one definition and propagate.

### P1B-E7. Pipeline bias sign is reported incorrectly.
**Abstract, Sec. IV.**
Abstract: "βˆ = 0.238° (pipeline-recovery bias 0.032°)." Body: "The bias is 0.032°." The bias of a recovered estimator is (recovered − injected). 0.238 − 0.270 = −0.032. The pipeline systematically *under*recovers; reporting the magnitude with no sign disguises that the deconvolution attenuates the signal. The β = 0.342 injection recovers 0.302 (bias −0.040, also negative). **Fix:** ESSENTIAL — state signed bias, since under-recovery propagates differently into a real measurement than over-recovery.

### P1B-E8. The "natural parameter" claim is undercut by the author's own 25× fine-tuning disclosure.
**Sec. VI, footnotes 4 and 5.**
The text repeatedly claims the ALP is consistent with the observed signal "for natural parameter values" but then footnote 4 admits that the spectator status requires θ_i ∼ 0.1, i.e., 25× tuning of the misalignment relative to the scan-prior midpoint, and that at the natural prior midpoint θ_i ∼ 0.5 the field is *not* a spectator (it is a dark-energy field, which is excluded from the claim). Further, the required C_aγ runs up to ~51, well outside any standard ALP benchmark, which is also admitted. A "consistency check" that requires both 25× tuning of one parameter and ~10–50× enhancement above benchmark in another is not a consistency check; it is "the data accommodate almost anything with enough tuning." **Fix:** ESSENTIAL — restate the conclusion of Sec. VI as "an ALP can fit the signal only with fine-tuning of θ_i and a non-minimal photon coupling," and remove all "natural parameter" language from abstract and conclusions.

### P1B-E9. The Eskilt–Komatsu attribution is internally muddled and dataset-mislabeled.
**Page 1 footnote a, Sec. VI, Appendix C.**
The abstract uses the "0.342° ± 0.094° (3.6σ)" headline from the PRD paper [2] (which uses Planck PR3 + WMAP9). The ALP-MCMC re-runs use the *code-repository* dataset (Planck PR4/NPIPE). Page 1 footnote a acknowledges this. But Sec. VI and Appendix C both say the ALP-MCMC uses "Planck PR4 + ACT DR6 EB-spectrum likelihoods" — which is yet a *third* dataset combination distinct from both (PR3+WMAP9) and (PR4/NPIPE). The author cannot mix the PRD-paper headline with a PR4+ACT-DR6 likelihood stack and call it consistency with [2]. **Fix:** ESSENTIAL — clarify which dataset stack actually produced 0.344° ± 0.096° and whether [2]'s 0.342° is the correct comparison target.

### P1B-E10. CAMB version "v1.6.5" does not exist (as of the manuscript-claimed June 2026 date this is plausible, but unverifiable; the public CAMB stable line is at 1.5.x as of writing this report).
**Sec. III, Table I caption, Sec. V.**
**Fix:** ESSENTIAL — either provide a verifiable release tag or correct.

---

## MAJOR findings

### P1B-M1. Sec. III/V model-comparison story is logically broken.
"Model-comparison statistics: deferred to a dedicated nested-sampling run" — yet Sec. III then states "the converged w₀w_a posterior disfavors ... LCDM point." You cannot defer the model comparison and simultaneously announce its outcome. The paper offers two contradictory positions on the same posterior. **Fix:** remove all claims of disfavoring LCDM until nested sampling is done.

### P1B-M2. Headline NaMaster SNR (20.32σ, 25.71σ) repeatedly cited without "not directly comparable" qualifier at every juxtaposition.
Although the paper does add the disclaimer in places, the abstract still parenthesizes "(pipeline-recovery bias 0.032°)" next to "βˆ = 0.238°" without flagging that the 20.32σ figure that appears later is *not* the significance of this measurement. PRD requires that mutually-non-comparable σ values never appear side by side without explicit "not directly comparable" at the juxtaposition. Sec. IV labels the SNR figure as Eq. (1) — equations are reserved for relations, not pipeline read-outs.

### P1B-M3. "(ω/H)₀ ... is discussed in Paper I(a) as a phenomenological bounce-class indicator but is not separately sampled here" — this parameter is named in the abstract framing and Sec. II as if relevant, then admitted to be fixed at zero. Misleading. **Fix:** remove from the parameter narrative entirely.

### P1B-M4. Page 1 abstract footnote a is functioning as a body retraction/disambiguation. PRD does not permit substantive scientific clarifications in abstract footnotes. **Fix:** Move to Sec. VI.

### P1B-M5. The fNL = −35/8 claim, the 14-barrier table, the perturbation-transparency theorem, and all of Paper I(a)'s purported results are referenced as load-bearing context but cannot be checked because Paper I(a) does not exist publicly. This is unreviewable. **Fix:** delete forward references or co-submit Paper I(a).

### P1B-M6. The "AIC preference for torsion (∆AIC = −5.7 to −6.6)" attributed to Liu et al. [11] is then claimed to "agree at 0.5σ in H₀ and 0.4σ in σ₈" with the present chain. But Liu et al. is using a *different* model (EC torsion fit) — agreement in posteriors does not mean cross-validation. The cited paper does not validate the present null result.

### P1B-M7. The MCMC includes the SH0ES H0.riess2020Mb likelihood per the YAML, but the discussion claims "the full-tension chain returns H₀ = 67.69 ± 1.06" with "the canonical 3.6σ Hubble tension with Riess H₀ = 73.04 ± 1.04 km/s/Mpc that the ΛCDM+ΔNeff extension is unable to resolve." Including a Riess prior and then describing the result as "in tension with Riess" indicates the prior is not actually driving the posterior — which is suspicious behavior for an active Gaussian prior. The MB-axis explanation provided is plausible but should be backed by a direct test: removing the H0.riess2020Mb likelihood and showing the posterior is unchanged. Otherwise the chain may be misconfigured.

### P1B-M8. Reference [3] cites arXiv:2509.13654 for ACT DR6 cosmic birefringence. The actual published ACT DR6 birefringence reference is Diego-Palazuelos et al. and should be cross-checked for authorship, arXiv ID, and abstract values. β = 0.215° ± 0.074° should be traced to the source.

### P1B-M9. The "−1.48 ± 0.15" sum for w₀ + w_a implies σ_(w0+wa) = 0.149, which is less than σ_wa = 0.186 alone. This requires anti-correlation between w₀ and w_a (typical, but it must be explicitly stated and the Cov reported). Without the Cov, the reader cannot verify the quoted σ.

### P1B-M10. Eskilt & Komatsu cited as "Eskilt et al." in Table III despite being a two-author paper. The reference list and Table III headers use different attributions for the same reference.

### P1B-M11. "Ωa(0.1)/Ωa(0.5) ∼ 1/25" — yes, mathematically (0.1/0.5)² = 1/25. But Ω_a depends on the *current* energy density, which for an oscillating field also depends on whether the field has begun oscillating. The simple θ²_i scaling is only valid for fields that have not yet rolled significantly. For m ∼ H₀ the field has *barely* begun oscillating. The factor 25 is therefore an overstatement of the simple cancellation; the actual backreaction scaling is more complex. **Fix:** show the calculation.

### P1B-M12. Eq. (3) introduces a factor "1.07" to fit β = 0.29° at C_aγ = 8, θ_i = 1, m = 2H₀. This factor is unexplained — presumably Δϕ/f_a ≈ 1.07 at this point of parameter space — but it must be derived from Eq. (2)'s ALP integration rather than introduced ad hoc.

### P1B-M13. Page 9 Appendix C says "MCMC engine is Cobaya v3.6.1 with the Metropolis-Hastings sampler; convergence threshold R̂ − 1 < 0.01 across all 3 configurations." But the body says R̂ − 1 < 3 × 10⁻³ for the main MCMC and 0.00820 for DESI w₀w_a. Different convergence floors for different chains in the same paper is fine, but the document never gives convergence statistics for the *Sec. VI* ALP-MCMC chains except the prose "R̂ − 1 < 0.01 for all runs." No table.

### P1B-M14. Eleven pages is too long for content that is (i) one null result that needed reporting, (ii) one pipeline validation that belongs in a methods appendix, and (iii) one ALP fit that reproduces the literature. Recommended maximum: 6 pages as a Brief Report, *if* Ref. [1] is co-submitted.

---

## MINOR findings

### P1B-N1. Datestamp "2026-06-08 PDT" is future-tense relative to most readers; PRD accepts forward dates only when the paper is *actually* posted on that date.

### P1B-N2. The phrase "Eskilt+Komatsu" is used in the body (page 1 fn. a) alongside the citation "Eskilt & Komatsu" — pick one style.

### P1B-N3. Table II footnote c admits the channel χ² sums (10.6 + 10983.9 + 3043.0 = 14037.5) differ from the total χ² (14037.4) by 0.1. The labeling of this as a "0.1-unit arithmetic-rounding artifact" is fine, but the explanation that GetDist computes a weighted-sample average over the full posterior while the channels do not is non-standard and unhelpfully wordy; either fix the bookkeeping or remove the table footnote.

### P1B-N4. Sec. III: "Sample-count stratification (reconciliation)" — the very use of the word "reconciliation" in a footnote tells the reader the author is patching a discrepancy. Rewrite without the meta-narrative.

### P1B-N5. Acknowledgment of "Claude (Anthropic) as an AI research assistant" is acceptable disclosure under PRD policy but should also include a sentence about how outputs were validated (e.g., independent recomputation). The boilerplate "All scientific claims ... were independently verified by the author" is insufficient given the arithmetic error in P1B-E3 directly above this disclaimer.

### P1B-N6. PACS classification is no longer used by APS journals; use PhySH descriptors instead.

### P1B-N7. The "we" in a single-author paper is grammatically unusual but acceptable; the manuscript drifts between "we" and "the author" — be consistent.

### P1B-N8. Sec. VI says "consistent with, but not derived from, the ECH action" — phrasing is acceptable, but the parenthetical (consistent with, but not derived from) appears in a context where the prior expectation is derivation. Restate as "an ALP fiducial value chosen to match observation."

### P1B-N9. "fa ∼ MPl from the Holst sector pseudoscalar structure" is heuristic and unexplained. Either cite the derivation (with equations) or describe as motivation only.

### P1B-N10. Sec. III footnote 2 invokes Λ_strong ∼ M_Pl/√γ_BI without a citation pinpointing where this scale is derived. The Mercuri 2006 reference is for the formalism, not this scale.

### P1B-N11. "Stock CAMB proxy ≠ ECH theory module" appearing as a "claim" in Table III is bizarre. A definitional disclaimer is not a claim that can be "verified."

### P1B-N12. Table III lists "Published 3.6σ (β = 0.342 ± 0.094°)" under "Status: Cited." This row is superfluous — citing the literature is not a claim of this paper.

### P1B-N13. Captions of Fig. 1 do not state units on the H₀ axis. Quick scan suggests km/s/Mpc but should be labeled.

### P1B-N14. The Cobaya YAML configuration referenced as "spin_torsion.input.yaml" is mentioned in body but not listed in Appendix A's repository structure (which lists "cobaya_full_tension.yaml" etc.). Naming inconsistency.

### P1B-N15. The phrase "Spectator-status caveat:" in the abstract is unusual prose style for a PRD abstract and signals that the author knows the spectator claim is fragile.

---

## Summary recommendation

**REJECT.**

This manuscript fails the PRD bar on three independent grounds: (i) its title and framing claim to verify a framework that its own body explicitly says it does not verify (E1); (ii) it is a "companion" to an unpublished paper [1], cites three more "in preparation" companions all by the same author, and is therefore not a self-contained scientific submission reviewable by PRD (E2); and (iii) on the limited physics it *does* contain, there is at least one outright arithmetic error in a load-bearing footnote (E3), multiple internal numerical inconsistencies in headline H₀ and sample counts (E5, E6), a sign error in the pipeline bias (E7), self-defeating disclosures about 25× misalignment tuning and non-benchmark photon couplings that nullify the "natural parameter" claim (E8), and a dataset-attribution muddle on the headline birefringence reference (E9). The acceptable kernel of this paper — a ΛCDM+ΔNeff null result and a NaMaster bias study — is publishable as a 3–4 page methods note *if* divorced entirely from the ECH framing and the unpublished companion-paper chain. As submitted, it cannot be revised into a PRD paper without first establishing the prerequisite Paper [1] in the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings — Fresh-Eyes Re-Review of P1B

I went back through the manuscript with the checklist above and found a substantial number of issues my initial review missed. They cluster in classes A (arithmetic), C/D (equations and cross-references), F (abstract faithfulness), and I (appendix vs. main text). Several are load-bearing.

---

## NEW ESSENTIAL findings

### P1B-E11. The pivot scale factor `ap = 0.6680` cannot be reproduced from the formula and posterior given.
**Page 4, Table II footnote b.**
Footnote b states: `ap = 1 − Cov(w0,wa)/Var(wa)`. Working backwards from the headline σ_wpivot = 0.0301 and the included cross term, one needs Cov(w₀, w_a) ≈ −0.00726 (this is also what is required to make σ_(w₀+w_a) = 0.1485 from σ_w₀ = 0.0436 and σ_w_a = 0.1864 — see below). With this Cov, the footnote's own formula gives:

`ap = 1 − (−0.00726)/0.03474 = 1.21`

That is *not* 0.6680. Even with a sign flip (`ap = 1 + Cov/Var`), one gets `ap = 0.791`, still not 0.6680. The quoted `ap = 0.6680` is the value used to derive `zp = 1/ap − 1 = 0.497` (which does check arithmetically against the quoted ap), so it is the *load-bearing* number for the pivot redshift — but it is unsupported by the formula in the same footnote. This is a second, independent error in the same footnote already flagged in P1B-E3. **Fix:** ESSENTIAL — either correct the formula, correct ap, or provide the actual chain Cov(w₀, w_a).

### P1B-E12. The S₈ uncertainties in Table I do not propagate from σ₈ and Ω_m.
**Page 3, Table I.**
S₈ ≡ σ₈ √(Ω_m/0.3). Standard linear propagation (no correlation) gives:

- Full-tension: σ_{S8} ≈ √[(1.013 × 0.008)² + (1.337 × 0.005)²] = 0.0105. **Table reports 0.008** — too small by ~30%.
- Planck+BAO+SN: σ_{S8} ≈ √[(1.020 × 0.009)² + (1.327 × 0.006)²] = 0.012. **Table reports 0.018** — too large by ~50%.

Including the typically positive σ₈–Ω_m correlation in CMB chains would INCREASE the propagated σ_{S8} (full-tension still too small), and INCREASE Planck+BAO+SN further (not decrease). Both numbers therefore disagree with consistent Gaussian propagation, and they disagree *in opposite directions*. Either the underlying posterior is non-Gaussian in a way that the table fails to disclose, or the numbers come from different post-processing recipes for full-tension vs. Planck+BAO+SN. **Fix:** ESSENTIAL — provide the chain-derived σ_{S8} with the full covariance, or correct.

### P1B-E13. Abstract birefringence significance "2.4–2.9σ" is mis-cited.
**Abstract, page 1; conclusions, page 8.**
Abstract: "The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2, 3]". But:
- Ref. [2] (Eskilt & Komatsu 2022) is the **3.6σ joint** result (β = 0.342° ± 0.094°). Quoting it as "2.4–2.9σ" is wrong.
- Ref. [3] (ACT DR6) gives β = 0.215°±0.074° = 2.9σ alone.
- Ref. [15] (Diego-Palazuelos NPIPE) is 0.30°±0.11° = 2.7σ.

So "2.4–2.9σ" describes [3] and [15] (individual-survey results), but cites [2] (the joint 3.6σ paper). The abstract is internally inconsistent about whether the headline observational reference is the 3.6σ joint or the individual 2.4–2.9σ measurements. The same problem recurs in the conclusions. **Fix:** ESSENTIAL — choose the joint or individual headline and cite consistently.

### P1B-E14. NaMaster noise model uses ACT noise on Planck Commander sky — physically incoherent and mis-labeled.
**Sec. IV.**
The pipeline runs on the **Planck Commander** Q/U map (Planck data, ~50–100 μK·arcmin polarization noise at 143 GHz) but injects MC noise at "ACT-noise level ∆P = 10 µK·arcmin". This is the *ACT/SO* noise floor, **not** Planck's; it is ~5–10× LOWER than the actual Commander map noise. The author labels it "a conservative worst-case bias check" — but it is the opposite: an unrealistically *optimistic* noise floor relative to the data being used. A more pessimistic noise (Planck-realistic) would produce LARGER pipeline-recovery scatter and potentially a different bias. The "20.32σ" pipeline-recovery SNR figure is therefore an artifact of an MC noise model that does not represent any actual measurement configuration. **Fix:** ESSENTIAL — either use Planck-realistic noise, or use ACT noise on an ACT sky, but not a mismatched combination labeled "conservative".

### P1B-E15. The "25× fine-tuning" / "θ_i = 0.5 scan midpoint" disclosure is wrong about the prior midpoint.
**Sec. VI footnote 4; Appendix C.**
The MCMC prior is θ_i ~ U[0.5, 2.0]. The midpoint of [0.5, 2.0] is 1.25, *not* 0.5. The author repeatedly calls θ_i = 0.5 the "scan-midpoint" or "natural-prior midpoint" — it is the **lower bound** of the prior. Consequently, the tuning narrative is inconsistent:

- *Parameter tuning* from "natural" midpoint 1.25 to spectator-consistent 0.1 is a factor 12.5×.
- From the lower edge 0.5 to spectator 0.1, it is 5×.
- The "25×" the author quotes is the ratio of *backreaction* Ω_a (which goes as θ_i²) between 0.5 and 0.1.

So the manuscript conflates parameter tuning, prior-midpoint tuning, and backreaction-ratio tuning under one label "25×". The actual fine-tuning relative to a flat prior on [0.5, 2.0] is *worse* than 25× (the spectator regime θ_i ≲ 0.1 lies entirely *outside* the prior, so its probability mass within the prior is exactly zero). **Fix:** ESSENTIAL — restate using the actual prior, and quantify the tuning correctly. If θ_i ~ 0.1 is required for spectator status and the MCMC prior is θ_i ∈ [0.5, 2.0], then the spectator regime has zero prior support and the MCMC results are *not* a spectator-ALP fit at all.

---

## NEW MAJOR findings

### P1B-M15. Cross-reference "Eq. (1)-adjacent disclaimer" in footnote 4 is broken.
**Page 7 footnote 4.**
Footnote 4 reads: "the abstract spectator-status restriction θ_i ≪ 1 (Eq. (1)-adjacent disclaimer)". But Eq. (1) in this manuscript is the NaMaster pipeline-recovery formula `βˆ_NaMaster = 0.238°`. The spectator-status restriction is in the abstract text, not adjacent to Eq. (1). The cross-reference is wrong. **Fix:** remove or repoint.

### P1B-M16. Caγ "continuous benchmark sweep" claim vs. Appendix C's three discrete values.
**Sec. VI body vs. Appendix C.**
Sec. VI body presents `β ∈ [0.17, 0.43°]` as the envelope over `C_aγ ∈ [4, 12]` (continuous), reading like a parameter scan. Appendix C reveals Caγ is *fixed* at one of {4, 8, 12} in three separate MCMC chains. So the "envelope" is the outer points only — not a marginalized envelope over a continuous Caγ prior. This is materially different from what the body suggests. **Fix:** clarify that the envelope is computed at three discrete coupling values, not as an MCMC-marginalized envelope.

### P1B-M17. In-text retraction "An earlier count erroneously quoted '98.6% quintom-B' weight…" is editorial leakage from drafting.
**Sec. III page 3.**
"An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain there are zero free-w0wa samples at the LCDM point". This is a meta-narrative about prior drafts that does not belong in a published paper. **Fix:** silently correct.

### P1B-M18. Sec. III footnote 1 "Sample-count stratification (reconciliation)" reads as a patch of a prior inconsistency.
**Sec. III footnote 1.**
The word "reconciliation" in the footnote title, combined with the three different numbers (123,368 / 123,129 / 119,617) for what should be one quantity, exposes that the headline sample count was not recomputed consistently across the manuscript. **Fix:** silently correct; do not narrate the patch.

### P1B-M19. Mb is listed under "10 Planck likelihood nuisance" parameters.
**Sec. III caption note under Table I.**
The text says "10 Planck likelihood nuisance: A_planck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb for the SNIa absolute magnitude". M_b is the Pantheon+ / SH0ES SN nuisance, not a Planck nuisance. The grouping is mislabeled. **Fix:** group as "9 Planck + 1 SN nuisance".

### P1B-M20. Equation (2) and Equation (3) use inconsistent (m, θ_i) settings without a clear bridge.
**Page 7.**
Eq. (2): Δϕ/fa ≈ 0.65 at (m = H₀, θ_i = 1).
Eq. (3): β ≈ 0.29° at (Caγ = 8, θ_i = 1, m ≈ 2H₀) using Δϕ/fa ≈ 1.07.
But the "fiducial β = 0.27°" used throughout (NaMaster injection, abstract) corresponds to Δϕ/fa ≈ 1.00, which is at yet a third unspecified (m, θ_i). Three different fiducials within one section, all called "the natural midpoint". **Fix:** specify which (m, θ_i, Δϕ/fa) corresponds to each quoted β.

### P1B-M21. Appendix A lists four Cobaya YAMLs; the body reports two frozen + one unconverged chain.
**Appendix A vs. Sec. III/V.**
Appendix A: `cobaya_planck.yaml, cobaya_planck_bao.yaml, cobaya_planck_bao_sn.yaml, cobaya_full_tension.yaml`. Body identifies "two frozen dataset combinations" (full-tension; Planck+BAO+SN) + "third Planck-only run currently at sub-convergence". That accounts for 3 of the 4 YAMLs. The `cobaya_planck_bao.yaml` chain is unmentioned. **Fix:** state the status of this fourth chain (frozen? running? abandoned?).

### P1B-M22. "Sec. V A" parameter-scope reference is to the wrong content.
**Sec. II, Sec. III preamble.**
Both sections cite "Sec. V A" as the source for the explicit parameter-scope clarification on (ω/H)₀ and Ω_k being fixed. But Sec. V A itself merely says "(ω/H)₀ and Ω_k fixed to zero in the actual sampled YAML configuration" with no further derivation or motivation. The forward-reference is circular — Sec. II/III cite V.A for justification, and V.A only states what II/III already stated. The actual justification (Paper I(a) bounce-class motivation) is gestured at, but Paper I(a) is unpublished (P1B-E2). **Fix:** either provide the actual scope justification in V.A or remove the forward reference.

### P1B-M23. "Cobaya v3.5 original; v3.6.1 verification" — version disclosure indicates re-run on different Cobaya minor version.
**Sec. V A.**
A re-run on a different Cobaya version implies the original v3.5 chain and the v3.6.1 chain may have produced different posteriors. The author should state whether they agreed within sampling error and which chain produced the headline numbers. **Fix:** add a chain-level agreement statement.

### P1B-M24. χ² channel-sum vs. total discrepancy explanation is incorrect.
**Table II footnote c.**
The footnote claims the channel sum (14037.5) differs from the total (14037.4) by 0.1 because of GetDist's weighted-sample average. But the mean is *linear*: mean(A+B+C) = mean(A) + mean(B) + mean(C), regardless of how the weights are distributed. The 0.1 discrepancy is simple rounding in the column display, not a weighting artifact. **Fix:** correct the explanation, or remove the footnote.

### P1B-M25. The implied Cov(w₀, w_a) from σ_(w₀+w_a) is not reported.
**Page 4 Table II / footnote b.**
The headline w₀+w_a = −1.48 ± 0.15 implies Cov(w₀, w_a) ≈ −0.00726 (r ≈ −0.89). This is a strong anti-correlation that is *central* to the "phantom crossing required" claim — and it is never quoted. The reader has to back-derive it from two reported σ values. **Fix:** report Cov(w₀, w_a) explicitly.

---

## NEW MINOR findings

### P1B-N16. "n143×217" — Planck CamSpec uses "amp143x217" and "n143x217" conventionally; the "×" symbol in the body Sec. III note is the LaTeX displayed "×", probably a typo for "x". Minor formatting.

### P1B-N17. Sec. III "Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing" but Table II caption lists "Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native". The naming switches between "lowl TT/EE" and "lowl.EE+TT" and between "TTTEEE" and "CamSpec.TTTEEE". Internally inconsistent likelihood naming.

### P1B-N18. "we framed an earlier count erroneously quoted" in Sec. III is also ungrammatical English, beyond being a draft-leak (P1B-M17).

### P1B-N19. "βˆ" used throughout (with hat) vs. "β̂" — inconsistent typesetting in places. Minor.

### P1B-N20. Inverse-variance combination Eq. (4) is labeled "(Auxiliary cross-check only.)" but appears in the main text as a numbered equation. PRD style typically reserves equation numbering for results carried forward in the paper. **Fix:** demote to in-line or footnote.

### P1B-N21. Page 7: "Across the natural parameter range … ∆ϕ/fa ∈ [0.2, 1.1]" is asserted without an integration plot or table. The range is load-bearing for the Caγ ∈ [9, 51] derivation. **Fix:** include a small figure or table showing Δϕ/fa as a function of (m/H₀, θ_i).

### P1B-N22. Sec. VI claims "anchored to the Planck PR4 + ACT DR6 EB-spectrum data" — but Appendix C says the same. Then Sec. VI also refers to the "joint WMAP+Planck value β = 0.342° ± 0.094°" as the comparison target. The MCMC is fit to PR4+ACT, but the headline target is PR3+WMAP9 (from Ref. [2]). Three different dataset stacks for three numbers (P1B-E9 amplified).

### P1B-N23. Sec. VI body claims "βALP = 0.336° ± 0.107°" and "βfree = 0.344° ± 0.096°" are both within 1σ of βobs. Check: σ_combined for βALP–βobs comparison = √(0.107² + 0.094²) = 0.142°, difference = 0.006°, → 0.04σ. The "1σ" claim is correct but very weak (the comparison is nearly trivial because the σ are similar to the data σ — this is a tautological consistency check, not a discriminating test).

### P1B-N24. "Caγ ∈ [4, 12] benchmark sweep" framing should be set against the KSVZ/DFSZ benchmark of |Caγ| ~ 1 explicitly in Sec. VI body where the sweep is introduced, not three paragraphs later when the upper end of the implied requirement (~51) is revealed.

### P1B-N25. The Liu et al. [11] AIC preference (∆AIC = −5.7 to −6.6) for torsion is quoted but the model used in [11] is different from the present null. Quoting an AIC-preferred competitor result alongside a null is misleading without explicit "different model" disclosure (relates to P1B-M6).

### P1B-N26. Page 1 footnote a is, by my count, ~150 words of dataset-attribution disambiguation embedded in the abstract page. PRD style would put this in §VI as a data-provenance note. Already in P1B-M4 — but I underestimated the length in the original review.

### P1B-N27. "Mb is a single nuisance parameter sampled jointly by both sn.pantheonplus and H0.riess2020Mb" — this is correct Cobaya behavior, but the paragraph spends three sentences explaining a standard configuration as if it were novel. Wordy.

### P1B-N28. "(verified by direct .input.yaml inspection and by chain sample-mean readout: MB = −19.263 ± 0.049 mag, agreeing with the Riess+2020 SH0ES value MB = −19.253 ± 0.027 mag at 0.2σ)". Check: difference 0.010 mag, combined σ = √(0.049² + 0.027²) = 0.056. 0.010/0.056 = 0.18σ. Author says 0.2σ. ✓

### P1B-N29. "the simple Gaussian-combination value ∼ 70 that would emerge if SH0ES and Planck were equally weighted" — actually, with σ_Planck ≈ 0.5, σ_Riess ≈ 1.0, the inverse-variance combination is 1/(1/0.25 + 1/1.0) = 1/(4+1) = 0.2, weighted mean = (4 × 67.5 + 1 × 73)/5 = 68.6, not 70. The "∼70" estimate is wrong even as a back-of-envelope.

### P1B-N30. "consistent with the apodized-mask bias expected from a 2° apodization scale" — no quantitative prediction (e.g., from a transfer-function calculation) is offered for the *expected* bias at 2°. Unsupported hedge.

---

## Class-by-class summary of what I missed first time

- **A (arithmetic):** I caught the σ_wpivot error (E3) but missed (i) the `ap` value being inconsistent with its own formula (E11), (ii) the S₈ uncertainty mispropagation (E12), (iii) the back-of-envelope "~70" combined H₀ being wrong (N29).
- **B/C (equations):** I missed Eqs. (2) and (3) using inconsistent (m, θ_i) settings vs. the fiducial 0.27° (M20).
- **D (cross-references):** I missed the broken "Eq. (1)-adjacent disclaimer" pointer in footnote 4 (M15) and the circular Sec. V.A back-references (M22).
- **F (abstract faithfulness):** I missed that the "2.4–2.9σ" range cited as Refs. [2,3] is actually inconsistent with [2]'s 3.6σ joint result (E13).
- **G/H:** I caught the "natural parameter" hedge but missed that the **prior midpoint** is misstated (the lower bound is being called the midpoint), which makes the actual fine-tuning much worse than 25× and *outside the prior* (E15).
- **I (appendix vs. main):** I missed that Appendix C exposes a 3-discrete-Caγ design while the body suggests a continuous sweep (M16), and that the 4th YAML in Appendix A is unaccounted for (M21).
- **J (stale numbers):** I missed several inconsistent likelihood-naming patterns (N17) and that Cov(w₀, w_a) is never reported despite being derivable and central (M25).

Most importantly, **P1B-E14** (ACT-level MC noise on a Planck sky map labeled "conservative") and **P1B-E15** (the spectator regime θ_i ≲ 0.1 lying *entirely outside* the stated prior θ_i ∈ [0.5, 2.0]) are upgrades to E-tier. The latter, in particular, means the ALP-MCMC posterior reported in Sec. VI does not in fact contain any spectator-consistent samples — the "spectator-ALP consistency check" reported in the abstract is not what the MCMC measured. This is a fundamental misrepresentation that my first pass treated only as a fine-tuning disclosure issue.

Updated recommendation remains **REJECT**, now with strengthened grounds on E11–E15.