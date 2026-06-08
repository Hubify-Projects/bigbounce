# P1B auto-2026-06-08_1424pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11435 chars)
**Wall time**: 431.4s

---

# Referee Report: P1B — Technical Verification Companion to ECH Spin-Torsion Program

**Manuscript:** "Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model"
**Author:** H. Golden (Independent Researcher)
**Target Journal:** Physical Review D

---

## Overall Assessment

This paper is a "companion" to a Paper I(a) that the reader cannot access (listed as "in preparation"), and it documents three numerical exercises, each of which the author *himself* concedes is not what it superficially appears to be:

1. An MCMC that does **not** test the theory the paper claims to support
2. A pipeline validation that the author concedes is **not** a sky measurement
3. A consistency check that the author concedes is **not** a distinctive prediction of the theory

After stripping these concessions, what remains is: (a) a stock-ΛCDM+ΔNeff null result that anyone could have run; (b) a pseudo-Cℓ Monte Carlo recovery on a foreground-cleaned map that cannot break the α–β degeneracy; (c) an ALP fit that requires ~25× misalignment tuning and Caγ up to ~51 to match observations. This is not a publishable PRD contribution. It is the supplementary materials for a paper that does not yet exist.

The manuscript also references four other "companion" papers (Paper I(a), II, III, IV), all "in preparation." A companion to nothing is nothing.

---

## ESSENTIAL Findings

### P1B-E1 — Companion paper has no parent (p. 1–2, 8)
The abstract and §I declare this a "Technical Verification Companion to … Paper I(a) [1]," and reference [1] is "H. Golden, *Structural Closure of Einstein–Cartan–Holst Dark Energy…*, (in preparation) (2026)." References [4], [5], [6] are likewise "in preparation."
**Problem:** A verification companion cannot be evaluated independently of the paper it verifies. PRD does not accept companions to unpublished work. Either Paper I(a) must be submitted simultaneously and referee-able, or this paper must stand alone — in which case the entire framing collapses.
**Fix:** Withdraw until Paper I(a) is available for joint review, or rewrite as a stand-alone methods paper with its own scientific claim.

### P1B-E2 — Headline ΔNeff result is not a test of the stated theory (Abstract, §III)
The abstract claims this is "verification material for the Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program," yet §III explicitly states: "*No custom CAMB modifications are used; no torsion-modified Boltzmann equations are solved.*" The author concedes (§III(a)): "the stock-CAMB ΛCDM+ΔNeff proxy run does not test the ECH spin-torsion sector directly."
**Problem:** A null result on a vanilla ΛCDM+ΔNeff run carries zero information content about spin-torsion. Calling it "verification" of an ECH program is misleading. The MCMC reproduces known Planck results.
**Fix:** Remove "verification" framing entirely; either run a torsion-modified Boltzmann code, or remove this analysis from a paper about spin-torsion.

### P1B-E3 — NaMaster "recovery" cannot measure the claimed quantity (Abstract, §IV)
The abstract concedes: "the test confirms the algebraic pseudo-Cℓ E→B deconvolution under MASTER mode coupling, NOT the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α." A foreground-cleaned Commander map by construction lacks the unrotated galactic foreground needed to break the β–α degeneracy.
**Problem:** Then what is the scientific content? The "recovery" of an injected signal on a map known not to contain α–β information is a NaMaster unit test, not physics. The 20.32σ and 25.71σ pipeline-recovery SNRs are also misleading even with the disclaimer because they will be cited out of context.
**Fix:** Remove all sigma values for the MC recovery from the abstract. Demote to a software-validation appendix or remove entirely.

### P1B-E4 — ALP "consistency check" is not distinctive to ECH (Abstract, §VI)
Author concedes in abstract: "The same birefringence arises in standard GR with an identical ALP; it is not a distinctive ECH prediction." §VI repeats this: "no ECH-specific derivation connects the Holst action to the photon-torsion coupling required."
**Problem:** Then this section provides no support for the ECH program. It is a generic ALP+GR exercise dressed up as ECH motivation. Spectator status further requires fine-tuning θᵢ ~ 0.1 (a ~25× tuning of misalignment) AND Caγ ~ 9–51 (outside KSVZ/DFSZ benchmarks). The author has confessed the result is unconnected to the theory and fine-tuned.
**Fix:** Remove from any paper claiming to support ECH. If retained, present as a generic ALP fit unrelated to the program.

### P1B-E5 — Abstract advertises 309,189 samples as "convergence" headline; this is sample count, not convergence (Abstract, p. 1; §III)
The abstract reads "309,189 frozen samples across two converged dataset combinations, plus a third Planck-only combination ongoing." A third combination at R̂−1 ~ 0.05 is **not converged** by the paper's own ±10⁻² criterion (§VII). Reporting it in the same breath as the converged chains in the abstract conflates the two.
**Fix:** State explicitly in the abstract that the third (Planck-only) chain is unconverged and not part of any quoted result.

### P1B-E6 — Pipeline-recovery SNRs juxtaposed with published sky-detection σ values without per-juxtaposition qualification (Abstract, §IV)
The abstract says "βˆ = 0.238° (pipeline-recovery bias 0.032°)" — a recovery figure — and then "the published Planck/ACT DR6 2.4–2.9σ." Even with the disclaimer paragraph, the abstract still presents both as if they are comparable measurements of the same kind. Per the explicit reviewer instruction: side-by-side σ values from different null procedures without explicit "not directly comparable" qualification *at every juxtaposition* are an ESSENTIAL flag.
**Fix:** Either remove all sigma/SNR numbers from the abstract, or insert "not a sky-detection significance" inline at every numerical occurrence.

### P1B-E7 — DESI DR2 w₀wₐ chain results (Table II) appear without scope justification in a paper whose stated subject is the ECH spin-torsion program (p. 4)
Table II reports an 8-parameter w₀wₐ MCMC with quintom-signature claims (w₀ + wₐ = −1.48 ± 0.15, "+4.3σ from ΛCDM" for w₀). This is a major result that has nothing to do with the stated subject of the paper, is not previewed in the abstract, and arrives without exposition. The "+4.3σ" departure is presented but the author then concedes the LCDM point is "unsampled," that a Savage–Dickey readout "is not viable," and that robust ln B is "left to a follow-up." So the "+4.3σ" is a posterior-tail extrapolation distance, not a statistical exclusion.
**Problem:** The "+4.3σ" framing in Table II is highly misleading. The author admits in footnote (a) it is "*not a Bayes-factor or ln B exclusion and not a frequentist tension*," yet the column is still labeled "vs LCDM" with "+4.3σ" entries. This will be misread.
**Fix:** Either (i) remove Table II entirely as off-topic, or (ii) replace "+4.3σ" with explicit "marginal-tail distance only, no model comparison possible." Both should be done.

### P1B-E8 — Internal audit/version language present in body (multiple)
The body contains numerous internal-audit tags and bookkeeping phrases that must not appear in a published PRD article:
- p. 3: "An earlier count erroneously quoted '98.6% quintom-B' weight"
- p. 3: "An earlier count" / "An earlier draft promised a Savage-Dickey ratio"
- p. 3: "prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but with zero free-w0wa samples at the LCDM point the KDE estimator fails catastrophically"
- p. 4–5: "MB–H0 joint-posterior offset check. A concern was raised that…"
- p. 5: "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood"
- p. 6: "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°"
- p. 7: "§VI for the explicit numerical derivation correcting the earlier Caγθᵢ product"
- p. 5: "iter2 chain"
- p. 3: footnote 1 reads as a referee-response document, not a footnote

**Problem:** These are review-log artifacts, not a published-paper voice. They reveal an unfinished editorial process.
**Fix:** Remove every "earlier count," "earlier draft," "prior caveat promised," "addresses earlier reviewer concerns," "iter2," "initially characterized," and "correcting the earlier" phrase. Rewrite the relevant content as positive statements.

### P1B-E9 — Arithmetic inconsistency in sample-count footnote (p. 2 fn. 1)
Footnote 1: 176,240 × 0.7 = 123,368, but it says "the 119,617 figure in Fig. 1 reflects additional getdist effective-sample weight-based thinning." Then "The post-burnin count of the full-tension subset alone is 123,129 (within ±1% of the 123,368 exact computation, with the small offset reflecting the chain-end-truncation of partial samples at the burn-in cut); the correct both-chains post-burnin total is 216,432."
**Problem:** The reader is presented with four different sample counts (309,189, 216,432, 123,368, 123,129, 119,617) and must reconcile them across the footnote. Fig. 1 caption gives 119,617; Table I rows give 176,240 and 132,949; abstract gives 309,189. The footnote's own arithmetic produces three different "post-burnin" numbers within one paragraph. This is a sign of an undisciplined accounting.
**Fix:** Pick one accounting (raw / post-burnin / effective), use it consistently, and report a single number per chain.

### P1B-E10 — Table II χ²ₜₒₜₐₗ arithmetic does not match the components within stated uncertainty (p. 4)
χ²BAO + χ²CMB + χ²SN = 10.6 + 10983.9 + 3043.0 = 14037.5. Reported χ²ₜₒₜₐₗ = 14037.4 ± 5.6. The 0.1-unit mismatch is dismissed as "arithmetic-rounding artifact." But for χ² values with ±1.6 to ±5.6 uncertainties, the components do not have to sum to the total — they may share covariances. The footnote handwaves "formally identical to within sampling precision" without showing this.
**Fix:** Either reconcile the arithmetic exactly or remove the χ² decomposition; the 0.1 unit "rounding artifact" claim is not credible for differently-weighted likelihood means.

### P1B-E11 — The +4.3σ marginal departure number does not match the stated w₀ posterior (p. 4)
w₀ = −0.8122 ± 0.0436. Departure from −1: (−0.8122 − (−1))/0.0436 = 0.1878/0.0436 = **4.31σ**. ✓ checks. But wₐ = −0.6666 ± 0.1864; departure from 0: 0.6666/0.1864 = **3.58σ** ≈ 3.6σ. ✓ checks. Then w₀ + wₐ = −1.4788 ± 0.1485. From −1: 0.4788/0.1485 = **3.22σ**, not the "phantom-crossing required" framing's implied significance. OK — the arithmetic for w₀, wₐ checks; w₀+wₐ is consistent. But the paper presents these as if they were a joint exclusion. They are marginal-tail distances of correlated parameters. The author admits this in the footnote but it's buried.
**Fix:** State that w₀ and wₐ are anti-correlated and that the marginal tail distances do not multiply into a joint exclusion.

### P1B-E12 — The Caγ ≈ 10.3 derivation in §VI is internally inconsistent with the headline parameter envelope (p. 7)
Eq. (3): β ≈ (αEM × 8)/(4π) × 1.07 ≈ 0.29°. Compute: α/(4π) = (1/137.036)/(4π) = 5.81×10⁻⁴; ×8 = 4.65×10⁻³ rad = 0.266°. Then ×1.07 = 0.285°. ✓ rounded to 0.29°.

Now the body text states Caγ Δφ/fa ≈ 10.3 for β = 0.342°. Check: 0.342° in rad = 5.97×10⁻³; divide by αEM/(4π) = 5.81×10⁻⁴ → **10.27**. ✓.

But then the body claims the "natural" parameter range gives β = 0.17–0.43°, "comfortably bracketing the observed value." The lower end (0.17°) corresponds to Caγ Δφ/fa ≈ 5.1, the upper (0.43°) to ≈ 12.9. With Caγ ∈ [4, 12] and Δφ/fa ∈ [0.2, 1.1], the product ranges 0.8 to 13.2 — so 10.3 is at the very top of the joint envelope, not "comfortably bracketing." The author later concedes Caγ must reach ~51 in the spectator-consistent regime.
**Problem:** "Comfortably bracketing" is false. The "natural" envelope barely reaches the headline value at one corner, and the spectator-consistent corner requires Caγ × 5 beyond natural.
**Fix:** Remove "comfortably bracketing"; state explicitly the headline lives at the upper edge of the natural envelope and outside KSVZ/DFSZ.

### P1B-E13 — Inverse-variance combination giving 3.9σ "auxiliary cross-check" double-counts data (Eq. 4, p. 7)
Eq. (4) combines Planck NPIPE β = 0.30 ± 0.11 [15] with ACT DR6 β = 0.215 ± 0.074 [3] to get 0.241 ± 0.061° at 3.9σ. The author flags this as "neglects shared calibration systematics." But ref [15] (Planck NPIPE) is *the same dataset* used by [2] (Eskilt & Komatsu joint), and ACT DR6 [3] is independent — the appropriate combination is more like 2.4σ⊕2.9σ accounting for shared signal and likely calibration covariances, not naive inverse-variance.
**Problem:** The 3.9σ is incorrect even as an "auxiliary" — it inflates significance by ignoring that the [2] joint already partially absorbed the Planck signal in [15]. The phrase "auxiliary cross-check only" does not rescue it because the wrong number is still in print and will be misquoted.
**Fix:** Remove Eq. (4) entirely. The published joint value is the only legitimate combination.

### P1B-E14 — Fig. 1 caption says "119,617 post-burnin samples, getdist-thinned from 176,240 raw"; this number contradicts the body sample accounting (p. 5)
See P1B-E9. Three sample-count chains in different places of the same paper.
**Fix:** Reconcile.

### P1B-E15 — Reference [11] cited as independent cross-validation, but is mis-described (p. 5)
Liu et al. is cited as constraining EC torsion with "∆AIC = −5.7 to −6.6" (torsion preferred). The body then says "Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈." But this paper's MCMC has *no torsion modifications* by the author's own repeated admission. So agreement on H₀ between a torsion-modified Boltzmann run and a vanilla ΛCDM+ΔNeff run is not meaningful "cross-validation"; both are consistent with Planck cosmology and the H₀ ~ 67–68 result is generic.
**Fix:** Remove the cross-validation framing.

---

## MAJOR Findings

### P1B-M1 — Paper length grossly disproportionate to content (whole paper)
After removing (i) deferred items ("left to follow-up nested sampling"), (ii) review-log prose, (iii) Table II off-topic dark-energy material, (iv) repeated disclaimers, what remains is approximately: ΔNeff = 0; 500-MC NaMaster passes a unit test; an ALP can match observations with tuning. This is a 2–3 page Brief Report at most. The current 10-page article is bloated by self-defensive scope statements.
**Fix:** Cut to ≤4 pages or withdraw.

### P1B-M2 — "Frozen" terminology is non-standard (Abstract, §III, throughout)
The paper repeatedly says "frozen samples," "frozen chains," "frozen dataset combinations." This is jargon not used in the MCMC literature. Standard terminology is "converged chains," "post-burnin samples."
**Fix:** Use standard terminology.

### P1B-M3 — Abstract footnote (footnote a) is too long and editorializes (p. 1)
The abstract footnote on PR3/PR4/NPIPE attribution is half a column and discusses repository updates. This belongs in the body, not in an abstract footnote.
**Fix:** Move to §IV or §VI.

### P1B-M4 — No model-comparison statistics reported (Abstract, §V.B, §VII)
The paper repeatedly defers AIC, BIC, ln B "to a follow-up nested-sampling analysis." A "verification" paper that cannot compare its model to ΛCDM has not verified anything. The justification (Savage–Dickey not viable because LCDM is unsampled) is correct, but it means the paper has no way to make a quantitative claim of preference or disfavor for any extension.
**Fix:** Run the nested sampling before publication. Or remove all "preference/disfavor" framing.

### P1B-M5 — Spectator-status fine-tuning rendered as a parenthetical (Abstract, §VI fn. 4)
The 25× fine-tuning of θᵢ is critical to whether the model is "natural." It is buried in the abstract's middle and in fn. 4. A reader who skims will conclude the ALP is consistent with natural parameters when in fact a fine-tuning is required.
**Fix:** State plainly in the abstract that the headline value requires θᵢ ~ 0.1, a ~25× tuning, and Caγ outside KSVZ/DFSZ.

### P1B-M6 — Conflict between abstract ("β = 0.342 ± 0.094° (3.6σ)") and reference [2]'s scope (p. 1, fn. a)
The abstract attributes the 3.6σ joint value to [2], and then footnote (a) confesses that the *abstract* uses the PR3+WMAP9 value from the *published* paper, but the *code* uses PR4/NPIPE — so the "Planck PR4 + ACT DR6 EB-spectrum likelihoods" used in the ALP-MCMC (Appendix C) is a *different* observable than the headline. The fits are then compared to a measurement they did not use.
**Fix:** Use consistent observables between the constraint quoted and the fit performed.

### P1B-M7 — Equation (3) prefactor "1.07" is undocumented (p. 7)
β ≈ (αEM × 8)/(4π) × 1.07. The 1.07 factor is the field-displacement Δφ/fa value at the chosen benchmark, but this is not stated next to the equation. The reader must infer it.
**Fix:** Write β = (αEM Caγ)/(4π) × (Δφ/fa) with all symbols defined explicitly.

### P1B-M8 — "Phantom crossing in the redshift range probed" — no demonstration (p. 3)
The text asserts w₀ + wₐ = −1.48 requires phantom crossing in the redshift range probed. But the relevant redshift of phantom crossing w(z*) = −1 in CPL is z* = wₐ/(−1−w₀) × (some sign) — at w₀ = −0.81, wₐ = −0.67, w(z) = w₀ + wₐ z/(1+z) = −1 at z/(1+z) = (−1−w₀)/wₐ = (−0.19)/(−0.67) = 0.284 → z* = 0.40. The author should state this, not just assert "phantom crossing in the redshift range probed."
**Fix:** Compute and report z*.

### P1B-M9 — Table I "Worst R̂ − 1 = 0.001" but footnote says 9.74×10⁻⁴ (p. 3)
0.001 ≈ 9.74×10⁻⁴ is consistent; but "Worst R̂ − 1 = 0.001" for full-tension and "0.003" for Planck+BAO+SN — yet the body text says "all 17 sampled parameters across both frozen combinations satisfy R̂−1 < 3×10⁻³." So one chain saturates the threshold the body advertises. State this.
**Fix:** Clarify which chain is at the boundary.

### P1B-M10 — Inconsistent ΔNeff posterior reporting precision (Table I, abstract, §III)
Abstract: "−0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN" — note 0.169 vs 0.17, mixed precision. Table I gives both as 0.169 and 0.17. Pick one.
**Fix:** Use consistent precision.

### P1B-M11 — DES Y3 S8 prior allegedly included in "full-tension" combination but result not reported (p. 6)
§V.A: "(4) +SH0ES H0 prior [7] + DES Y3 S8 [19]". Table I full-tension column shows S₈ = 0.814 ± 0.008. But no statement of whether the DES Y3 likelihood is *actively* included (cf. the laborious SH0ES-MB check at p. 4–5).
**Fix:** State explicitly which likelihoods are active in each YAML.

### P1B-M12 — "Spin-torsion sector's possible effective radiation contribution" is asserted without derivation (§III, p. 2)
The author says ΔNeff is "a generic phenomenological proxy for the spin-torsion sector's possible effective radiation contribution." But the §III(a) discussion says torsion contributes a dimension-6 four-fermion contact term, M_Pl⁻² suppressed, with "no ΔNeff at recombination." So the parameter is not a proxy for spin-torsion at all.
**Fix:** Either remove the proxy framing or derive the connection.

### P1B-M13 — "k = 7" vs "17 sampled parameters" inconsistency referred to but not resolved cleanly (Table I footnote, p. 3)
The footnote says "references to 'k = 7' elsewhere in this paper refer to the cosmological-parameter count only." But "k = 7" does not appear visibly in the paper.
**Fix:** Remove the dangling reference or include the AIC/BIC computation that needs it.

### P1B-M14 — Equation (2): Δφ/fa ≈ 0.65 for (m=H₀, θᵢ=1), but Eq. (3) uses Δφ/fa ≈ 1.07 (p. 7)
Eq. (2) gives Δφ/fa ≈ 0.65 at (m=H₀, θᵢ=1). Eq. (3) uses 1.07 at (m=2H₀, θᵢ=1). These are different benchmarks but the prose says "fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H₀, Δφ/fa ≈ 1.0" — yet Eq. (3) uses m ≈ 2H₀ and Δφ/fa ≈ 1.07. The "fiducial" definition slides.
**Fix:** Pick one fiducial and use it consistently.

---

## MINOR Findings

### P1B-N1 — "(Sec. III, *Model-comparison statistics* paragraph)" cross-reference style is inconsistent (p. 8, 9)
Sometimes "Sec. V," sometimes "§VI body text," sometimes named "*Model-comparison statistics paragraph*." Standardize.

### P1B-N2 — "Forward" subsection at p. 8 reads like a private status update (p. 8)
"A DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR cobaya chain ... has converged ... GetDist posteriors on w0wa are available as an empirical test of the quintom-B scenario." This is forward-looking publication-tracking prose; reword as forward-looking science.

### P1B-N3 — Appendix B title "Claims Classification" (p. 9)
A "claims classification" table with rows labeled "Verified," "Omitted," "Cited" is internal-project-management style, not journal style.

### P1B-N4 — Acknowledgments disclose AI assistant (p. 8)
"the author acknowledges the use of Claude (Anthropic) as an AI research assistant." This is fine and increasingly standard; only NIT because some readers will want more specificity about which sections used it.

### P1B-N5 — Self-funded RunPod H200 instances noted (p. 8)
Cute but unnecessary in an acknowledgments section.

### P1B-N6 — "iter2 chain" reference (p. 4 fn. b)
"On the converged iter2 chain ap = 0.6680." "iter2" is internal nomenclature.

### P1B-N7 — Footnote 1 length (p. 2)
Footnote 1 is essentially a 200-word internal reconciliation memo. Move to a paragraph in §III if it must be kept; preferably delete.

### P1B-N8 — "RunPod H200 instances" in acknowledgments (p. 8)
Acknowledge compute provider properly or omit.

### P1B-N9 — Hyphenation: "spin-torsion" vs "spin torsion" usage is mixed (multiple)
Standardize.

### P1B-N10 — "fn. a" inline reference style in body text (p. 3)
The body refers to "fn. a"; standard practice is "footnote a" or "Note a."

### P1B-N11 — Reference [22] annotation reads as an internal note (p. 10)
"Canonical quintom-cosmology review (two-field DE with w crossing -1). Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers."
**Problem:** This is a reviewer-note, not a bibliographic annotation. "P1A Sec. VI" is the author's own internal paper code. Remove "Used in P1A…"; "P1A" is not visible to journal readers.

### P1B-N12 — Reference [15] annotation similarly reads as reviewer note (p. 10)
"reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B" — L256/L416 are line numbers in the author's draft, "P1B" is an internal tag. Remove.

### P1B-N13 — Inconsistent rounding of σ values (Table II, abstract)
σH₀ = 1.06 (Table I) vs 0.455 (Table II for a different chain) vs "± 0.094" etc. Adopt consistent significant figures.

---

## Summary of Critical Issues

1. **Companion to non-existent paper** — references [1, 4, 5, 6] all "in preparation"
2. **Author concedes none of the three analyses actually verify the ECH theory**
3. **DESI w₀wₐ section (Table II) is off-topic and contains misleading "+4.3σ" framing**
4. **Multiple review-log artifacts** ("earlier count erroneously quoted," "addresses earlier reviewer concerns," "iter2," "initially characterized")
5. **Internal annotations in bibliography** ("Used in P1A Sec. VI," "L256/L416 of P1B")
6. **Sample-count accounting** gives different numbers in abstract, table, footnote, figure caption
7. **Inverse-variance 3.9σ combination** double-counts data
8. **"Comfortably bracketing" the headline β is false** — headline lives at envelope edge or outside it
9. **No model-comparison statistics**, all deferred
10. **Pipeline-recovery σ values in abstract** invite misreading as sky-detection significance

---

## Summary recommendation

**REJECT**

This manuscript should not be published in PRD in any form close to its current state. It is a "verification companion" to a paper that does not exist. Each of its three analyses is conceded by the author to (i) not test the theory being verified (stock CAMB has no torsion), (ii) not measure the quantity it claims to recover (foreground-cleaned map cannot break α–β degeneracy), or (iii) not be distinctive to the theory (any GR+ALP gives the same result, and even then requires ~25× misalignment fine-tuning and Caγ ≈ 9–51 outside KSVZ/DFSZ). The body is contaminated with review-log prose ("earlier count erroneously quoted," "addresses earlier reviewer concerns," "iter2 chain"), the bibliography contains internal annotations referencing line numbers of the author's own draft, sample counts are reconciled across an undisciplined sequence of three or four different numbers within a single footnote, and the off-topic DESI w₀wₐ Table II carries misleading "+4.3σ vs ΛCDM" entries that the author himself confesses are tail-extrapolations not exclusions. Model-comparison statistics are uniformly deferred to a future nested-sampling analysis that has not been performed. Withdraw, perform the nested sampling, submit Paper I(a) for joint review, remove all review-log artifacts, and reduce to a Brief Report focused on the single genuine technical contribution (the NaMaster MC validation as a pure software test).

---

## PASS 2 — self-critique findings (what initial review missed)

# Fresh-Eyes Pass: Additional Findings

I went back through the paper with the checklist. A surprising number of new issues turned up, including one serious arithmetic inconsistency that completely undermines a footnote, and one direct contradiction between the body text and Table I that I missed entirely on the first pass.

---

## NEW ESSENTIAL Findings

### P1B-E16 — Table II footnote (b) σ_wpivot derivation is mathematically inconsistent (p. 4)

This is a serious arithmetic error that I missed. The footnote claims:
> "*σ²_wpivot = σ²_w0 + (1 − ap)²σ²_wa = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²*"

Direct recomputation:
- (0.0436)² = 0.001901
- (0.3320)² × (0.1864)² = (0.0619)² = 0.003830
- Sum = 0.005731
- √Sum = **0.0757**, not 0.0301

So the stated formula does not produce the claimed σ_wpivot = 0.0301°.

Worse — the correct decorrelation formula is **σ²_wpivot = σ²_w0 − Cov²/Var(wa)** (subtraction, not addition; the cross-term cancels the second term and flips its sign). Using the claimed ap = 0.6680:
- (1 − ap) = 0.3320 = −Cov/Var(wa) → Cov = −0.01154
- This implies correlation |ρ| = |Cov|/(σ_w0 σ_wa) = 0.01154/(0.0436 × 0.1864) = **1.42 > 1** — algebraically impossible.

Cross-check from σ(w0+wa) = 0.1485: this implies Cov = −0.00733, |ρ| = 0.90, ap ≈ 0.79 (NOT 0.668), and σ_wpivot ≈ 0.019 (NOT 0.030). The four quoted numbers (σ_w0, σ_wa, σ(w0+wa), σ_wpivot, ap, zp) are mutually inconsistent — at most three can simultaneously be right.

**Problem:** The +4.3σ marginal-tail framing of w0wa departs from ΛCDM relies on these parameter posteriors being internally consistent. If σ_wpivot is wrong, then the entire pivot-decorrelation story (and the claim that "the dark-energy departure is dominated by wa rather than w0") rests on bad arithmetic.

**Fix:** Recompute ap, zp, σ_wpivot from the actual chain covariance and report a self-consistent set. Drop the footnote until the arithmetic checks out. This is also further evidence (in addition to the unsampled-LCDM point and the missing nested sampling) that Table II is not ready for publication.

### P1B-E17 — Planck-only chain claimed to be "reported separately in Table I" — but Table I has no such column (footnote 1 p. 2; §VII p. 8)

Footnote 1: "*The third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating samples, is reported separately in Table I…*"

§VII Conclusions: "*…an additional 114,992-sample Planck-only run is still accumulating at R̂ − 1 ∼ 0.05 and is reported separately in Table I, not aggregated into the frozen headline.*"

Direct inspection of Table I (p. 3): two columns only, "Full-tension" and "Planck+BAO+SN". There is no third column.

**Problem:** A direct factual contradiction between body/footnote and the table. Two separate places in the paper assert a Table I row/column that does not exist. This signals that either Table I was meant to have three columns and one was dropped, or the body claims are stale. Either way it must be reconciled.

**Fix:** Either add the Planck-only column to Table I (with appropriate caveats about non-convergence), or correct both the footnote and §VII to state the Planck-only chain is *not* in Table I.

---

## NEW MAJOR Findings

### P1B-M15 — NaMaster pipeline bias is essentially a constant 12% multiplicative shift, not "amplitude-dependent" (p. 6)

The §VI body text says: "*the absolute bias scales mildly with injected amplitude (the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°, a relative ∼ 12% amplitude-dependent component)*"

Fractional bias check:
- At β_inj = 0.27°, bias = 0.032°, fractional = 0.032/0.27 = **11.85%**
- At β_inj = 0.342°, bias = 0.040°, fractional = 0.040/0.342 = **11.70%**

The fractional bias is constant to within 0.15 percentage points — i.e., the pipeline has a **multiplicative bias of ~12%**, not an "amplitude-dependent component." The recovered β is approximately β_inj × 0.88 across the tested range.

**Problem:** A 12% multiplicative bias on a 0.342° signal is a 0.04° systematic — comparable in magnitude to the published statistical uncertainty (0.094°). If this pipeline were ever used for a real measurement, the bias would have to be calibrated out as a multiplicative correction. The author's framing as "absolute bias is 0.04° at worst" understates this: the absolute bias scales with the signal because it *is* the signal × 0.12. This should be characterized explicitly as a multiplicative bias and the source diagnosed (apodization, mode coupling, mask leakage).

**Fix:** Re-characterize the bias as multiplicative (β̂ ≈ 0.88·β_inj), state the calibration factor explicitly, and discuss whether this is a known pseudo-Cℓ artifact or a pipeline-specific issue.

### P1B-M16 — Full-tension S8 = 0.814 is inconsistent with an active DES Y3 S8 prior (p. 3 Table I, §V.A)

§V.A states the full-tension combination includes "(4) +SH0ES H0 prior + DES Y3 S8 [19]." DES Y3 3×2pt: S8 = 0.776 ± 0.017. Planck-only ΛCDM: S8 ≈ 0.83 ± 0.013.

If both were active and treated as Gaussian priors, naive inverse-variance combination gives:
- S8 ≈ (0.776/0.017² + 0.83/0.013²)/(1/0.017² + 1/0.013²) ≈ 0.81
- σ(S8) ≈ 0.010

But the chain gives S8 = 0.814 ± 0.008 — within 0.4σ of the *Planck-only* expectation, and on the *Planck side* of the DES value, with even smaller uncertainty.

**Problem:** This is the same diagnostic situation as the SH0ES MB check (p. 4–5) — a likelihood listed in the YAML configuration whose pull on the posterior is much smaller than expected. The author was meticulous about the SH0ES/MB diagnostic but did not perform the parallel check on the DES Y3 S8 likelihood. Either DES Y3 is being included in some way that down-weights its constraint, or it isn't actually pulling the chain. Given the precedent set by the SH0ES audit, this deserves the same explicit diagnostic.

**Fix:** Provide a YAML-and-posterior-readout diagnostic for the DES Y3 S8 likelihood analogous to the MB diagnostic. State explicitly whether DES Y3 is contributing to the full-tension constraint and at what effective weight.

### P1B-M17 — βfree "fit" reproduces the input observation to within rounding (§VI, p. 7)

The "model-independent fit" gives βfree = 0.344° ± 0.096°. The headline observational input is βobs = 0.342° ± 0.094°.

The recovered uncertainty (0.096°) is essentially identical to the input observation's uncertainty (0.094°), and the mean differs by 0.002°. This is consistent with a fit that simply recovers its input data with no additional constraint — i.e., it adds no information.

**Problem:** Reporting "βfree = 0.344° ± 0.096° agrees with βobs = 0.342° ± 0.094° within 1σ" creates the impression of an independent measurement that confirms the observation. In fact, βfree is the same data fit with one free parameter; the agreement is tautological by construction. This is not a "consistency" result; it is a sanity check that the chain ran without crashing.

**Fix:** Either drop the βfree result or label it explicitly as "input-recovery sanity check, by construction reproduces the input observation."

---

## NEW Minor Findings

### P1B-m1 — zp = 0.497 mismatched with cited literature value (Table II fn. b, p. 4)

The footnote acknowledges "this is internal to the dataset stack … and is not the literature de Putter–Linder zp ≈ 0.4 value," then claims that switching dataset stacks would shift zp by "≲ 0.1." But zp = 0.497 is already ~0.1 away from the literature value, so the qualifier is at the edge of self-consistency. The "linear-Fisher prediction" referenced is not derived in the paper.

**Fix:** Either provide the linear-Fisher computation explicitly or remove the predictive claim.

### P1B-m2 — Min ESS = 4,744 across 17 parameters (Table I, p. 3)

With 176,240 raw samples and 6 chains, ESS = 4,744 implies an autocorrelation length of ~37 samples per effective independent draw. For an MCMC reporting 4-decimal posterior precision (e.g., 100θMC = 1.04087 ± 0.000239 in Table II), this is on the marginal end. No immediate red flag, but combined with R̂ − 1 sitting close to the threshold (P1B-M9), the chain is at the lower end of what should be reported as "converged."

**Fix:** Either run longer chains or be more modest about quoted posterior precision.

### P1B-m3 — Table II χ² uncertainty addition is plausible but not formally checked (p. 4)

Reported χ²_total = 14037.4 ± 5.6. Quadrature of channel uncertainties: √(1.8² + 5.3² + 1.6²) = 5.82. Sum (full positive correlation): 8.7. The paper's 5.6 falls slightly below the independent-channel quadrature. This is plausible for cross-covariances but is not justified anywhere in the text.

**Fix:** Either explain the cross-covariance or report the independent-channel quadrature value (5.8).

### P1B-m4 — "Natural" is used as a technical qualifier without rigorous definition (§VI repeated)

§VI uses "natural parameter range," "natural parameter values," "natural-misalignment range," and "natural prior midpoint" without defining what makes the chosen ranges (m/H0 ∈ [1, 3], θi ∈ [0.5, 2], Caγ ∈ [4, 12]) natural in a particle-physics sense. KSVZ/DFSZ benchmarks predict |Caγ| ~ O(1), so Caγ ∈ [4, 12] is already not minimal-axion-natural. The word "natural" should not be used to denote an ad-hoc scan prior.

**Fix:** Define the prior ranges by their explicit theoretical motivation; use "scan range" or "benchmark range" rather than "natural" when no natural-prior argument is given.

### P1B-m5 — Footnotes 4 (main text) and 5 (Appendix C) repeat the same backreaction/fine-tuning caveat (p. 7, p. 9)

The 25× misalignment fine-tuning caveat appears in (i) the abstract, (ii) §VI body, (iii) footnote 4 of §VI, (iv) §VII conclusions, and (v) footnote 5 of Appendix C. This indicates either insufficient confidence in the consistency claim, or a layout problem. The information should appear once, prominently, in §VI.

**Fix:** Consolidate into a single, clearly-stated paragraph in §VI; remove the redundant footnotes.

### P1B-m6 — Section heading "Cosmic Birefringence: Spectator ALP Consistency Check" advertises a consistency check that requires θi tuning, Caγ above KSVZ/DFSZ, and bears no relation to the stated ECH theory (§VI heading)

Combining the three concessions (P1B-E4, P1B-E12, the 25× tuning), the section heading promises more than the section delivers.

**Fix:** Rename the section to "Generic ALP Birefringence: Order-of-Magnitude Fit and Tuning Requirements."

---

## Summary

The fresh-eyes pass added **two new ESSENTIAL findings** (a major arithmetic inconsistency in Table II's pivot derivation, and a direct contradiction between body text and Table I about the Planck-only chain), **three new MAJOR findings** (the pipeline bias is a calibration-grade ~12% multiplicative shift; the DES Y3 S8 likelihood is plausibly inactive analogous to the SH0ES/MB diagnostic; the βfree "fit" is a tautological recovery of the input), and several minor items.

The pivot-formula arithmetic inconsistency (P1B-E16) is particularly damaging because it sits inside a footnote that was clearly added to *prove* the arithmetic to a skeptical reader. The Planck-only-in-Table-I contradiction (P1B-E17) shows that even the table layout has not been finalized. Combined with the original findings, these reinforce the conclusion that this paper is not ready for PRD.