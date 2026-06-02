# P1A v1A.0.36-39 — External 3-Reviewer Review (Houston-shared, 2026-06-02)

**Paper**: P1A — "Structural Closure of Einstein–Cartan–Holst Dark Energy: A No-Go Theorem and the Matter-Bounce Tests It Does Not Predict"
**Manuscript version on which reviewers ran**: PDF labeled v1A.0.35 / v1A.0.36 (ChatGPT saw v1A.0.35; Grok header says v1A.0.36; Gemini doesn't specify but cites v1A.0.28/29 internal R-round artifacts as evidence of embedded review-log → must be the same v1.0.3x-era PDF Houston shared)
**Reviewers**: 3 frontier-model UIs run by Houston
- **Grok**: MAJOR REVISIONS
- **Gemini**: MAJOR REVISIONS
- **ChatGPT**: REJECT

**Headline convergence**:
- **2/3 reviewers** flag the ALP birefringence attribution as wrong (Eskilt 2022 is WMAP+Planck, NOT Planck/ACT DR6; ACT DR6 = 0.215° ± 0.074° at 2.9σ per arXiv:2509.13654)
- **2/3 reviewers** flag the "no-go theorem" scope as overclaim relative to the explicit operator-basis incompleteness disclaimer
- **2/3 reviewers** flag the 14-barrier catalog as over-counted (B8 ⊂ B14 on the paper's own admission; B5/6/9/13 are heuristic not derived)
- **2/3 reviewers** flag companion-paper self-citations as unverifiable
- **1/3 (Gemini, BLOCKER-grade)** flags raw internal LLM/multi-vendor R-round logs embedded in the paper body — the single most damning editorial issue
- **1/3 (ChatGPT, BLOCKER B6)** flags Date-Kaul-Sengupta β-function attribution as wrong source (correct: Benedetti-Speziale arXiv:1104.4028)

**Learning-loop note**: this external round caught issues that 8 internal direct-vendor R-rounds did not. The patterns we trained against in the internal cycle (Grok-4 + GPT-4o + Perplexity Sonar Pro + Gemini-failed-billing) are blind to:
1. Editorial hygiene (embedded LLM-tracking text in paper body) — `pattern-014` was a partial detector; was not run as a pre-review gate
2. Convergent external attribution forensics on ALP (3/3 vendors converged — internal vendors only Perplexity which has its OWN attribution-confabulation pattern that triggered FALSIFY-then-revert reflex)
3. Cross-vendor source verification for theoretical-basis citations (Date-Kaul-Sengupta vs Benedetti-Speziale β-function)

This file is the canonical verbatim copy. Truth-audit + closure proceeds in `2026-06-02_P1A_houston_external_synthesis.md`.

---

## Reviewer 1 — Grok

**Referee Report: MNRAS / PRD / JCAP style**
**Manuscript: HUBIFY-2026-001A v1A.0.36**
**Title:** Structural Closure of Einstein–Cartan–Holst Dark Energy: A No-Go Theorem and the Matter-Bounce Tests It Does Not Predict
**Author:** Houston Golden (independent)
**Received:** 22 May 2026 (arXiv version provided)

**Recommendation: MAJOR REVISIONS**

The manuscript presents a channel-level no-go on four enumerated minimal-ECH routes to late-time dark energy, supported by a 14-barrier catalog (13 logically independent) and a clean perturbation-transparency theorem. The central physics—torsion sourced only by spin density, hence vanishing for canonical scalar matter, with the Holst term becoming purely topological—is correct and well-executed. However, the paper overclaims a "structural closure" while simultaneously admitting (Appendix B, Sec. XIV) that the entire dark-energy ansatz is a phenomenological scaling relation, not a derived EFT operator. Observational tensions (especially the ALP birefringence central value) are glossed over, companion-paper infrastructure is cited as if published, and the barrier catalog mixes novel ECH-specific results with rephrased known facts. The work is not yet publication-ready in its current form.

**BLOCKERS (must be fixed before any acceptance)**

**B1. ALP birefringence central-value mismatch (Sec. II A 2, XIII, Table IV, line ~320; also abstract and Conclusions)**
The paper repeatedly states β ≈ 0.27° is "consistent with the published Planck/ACT DR6 3.6σ signal" and cites Eskilt et al. (0.342°⁺⁰.⁰⁹⁴₋⁰.⁰⁹¹). This is factually incorrect. Recent ACT DR6 analysis (arXiv:2509.13654 and related 2025/2026 publications) measures β = 0.215° ± 0.074° (2.9σ), with Planck+WMAP reanalyses yielding ~0.26°–0.34°. The combined posterior is ~0.26° ± 0.06°. The manuscript's spectator-ALP "prediction" of 0.27° is therefore inside the new 1σ band but was chosen to match an outdated central value; the text still quotes the old 0.342° ± 0.094° as "βobs".
**Fix:** Update all numerical statements, Table IV, and LiteBIRD forecasts to the latest combined Planck+ACT DR6 posterior. Explicitly state that the 0.27° value was a pre-DR6 target and is now consistent but no longer a sharp prediction. Otherwise the claim is misleading.

**B2. Dimensional status of the parity-odd operator (Appendix B; also Sec. II A 2, II C 1, XIV D)**
The paper now correctly labels ρ_Λ ∼ [(α/M) M_Pl] M_Pl⁴ as a "phenomenological on-shell scaling ansatz" (improvement over earlier drafts), but still derives N_tot ≈ 92 and the entire "inflationary suppression" fine-tuning reduction (10¹²² → 10⁵) from this ansatz. The main text and abstract treat the no-go as derived from minimal ECH dynamics; the appendix admits the operator has [ℒ_odd] = +1 off-shell. This is not a minor technicality—it is the entire dark-energy mechanism.
**Fix:** Either (i) derive a controlled dim-4 operator (e.g., α M_Pl³ ε e e F / M_Pl⁴ or equivalent with explicit curvature insertions that survive on-shell), or (ii) move the entire dark-energy ansatz to a clearly labeled "phenomenological toy model" section and rename the no-go "channel-level closure of the minimal ECH + scaling-ansatz dark-energy route". The current hybrid framing is unacceptable.

**B3. Scope of the "no-go theorem" (Abstract, Sec. IV E, Sec. IX, Sec. XIV E)**
The title and abstract call it a "structural closure" and "no-go theorem". Sec. IV and IX repeatedly say "channel-level, not operator-level" and list omitted operators (Jackiw–Pi Chern–Simons, parity-odd four-fermion partner). The perturbation-transparency theorem (Sec. X) is genuine but only kills perturbative signatures; non-perturbative or hybrid routes remain open by the paper's own admission.
**Fix:** Change title/abstract to "Channel-Level No-Go on Four Enumerated Minimal-ECH Dark-Energy Routes" and add a prominent "Scope and Limitations" paragraph in the introduction stating explicitly that a full operator-basis closure is deferred.

**MAJORS (should be addressed)**

**M1. 14-barrier catalog (Sec. IX + Table II)**
Several barriers are not logically independent or are known results rebranded:
- Barrier 8 (parity-even interaction) is explicitly subsumed by Barrier 14 (perturbation transparency) per the paper's own note.
- Barriers 5, 6, 7, 9, 13 are generic to any bounce + inflation setup or Poincaré-gauge theory, not ECH-specific.
- "Gravitational democracy" (B13) and "Liouville conservation" (B9) are philosophical statements, not quantitative constraints.
The claim of "13 logically-independent mechanism-class constraints" is therefore inflated.

**Fix:** Collapse Table II to the genuinely novel ECH-specific barriers (at most 7–8). Move the rest to a separate "generic bounce constraints" subsection with proper literature citations.

**M2. Perturbation-transparency theorem (Sec. X)**
The proof (scalar + tensor sectors) is correct and clean, but the statement "the Holst sector decouples from all scalar/tensor perturbation observables" is already implicit in Hehl et al. (1976) + Freidel et al. (2005) for spinless matter. The paper's "generalization to all orders" is useful but not revolutionary. Sec. X.D's explicit second-order verification is good but should cite the standard cosmological perturbation literature for Holst-modified actions (e.g., recent works on parity-violating gravity).

**Fix:** Tone down novelty claims; add citations and one sentence acknowledging the result follows directly once torsion vanishes.

**M3. Mercuri–Capozziello one-loop framing (§II C 1, post-R23)**
The paper now distinguishes "phase-space ansatz" from the chiral-anomaly loop coefficient, which is an improvement. However, the (T_reh / M_GUT)³/² factor remains a "dimensional-analysis-aesthetic estimate" with no first-principles derivation. The reheating thermal-reset barrier is presented as a new thermodynamic closure, yet it is standard knowledge that non-propagating torsion tracks instantaneous fermion density.

**Fix:** Either compute the thermal phase-space factor rigorously (or drop the ³/² claim) or relegate the entire inflationary-suppression section to an appendix labeled "phenomenological parameterization".

**MINORS (polish)**

- Companion-paper citations (Paper I(b), II, III, IV) appear throughout as if already published. Provide arXiv numbers or remove quantitative claims (e.g., 3–5σ SPHEREx forecast) that rely on them.
- Inconsistent β notation: abstract uses 0.27°, Table IV uses 0.27° (midpoint), main text sometimes 0.342°. Standardize.
- Table I and Fig. 1 contain minor LaTeX artifacts ("ρ_F1", "ECH/torsion" box).
- References: some arXiv numbers are malformed; DESI 2025 citations are future-dated relative to manuscript date—verify or use latest available.
- Galaxy-spin ViT-Small analysis is self-cited to Paper IV with no numbers here; either summarize key null-result statistics or remove.
- Minor typos: "f_NL = −35/8 signature, which would be definitively erased" (repeated), "SPHEREx-accessible comoving wavenumbers" (scale mapping explanation is correct but wordy).

**STRENGTHS**

- The perturbation-transparency theorem (Sec. X) is a clean, positive structural result that cleanly separates perturbative from non-perturbative tests of the Barbero–Immirzi parameter. The five-step proof is textbook-ready.
- Systematic barrier catalog (even if over-counted) is a useful organizational device that forces the community to confront the amplitude-budget problem in ECH dark-energy proposals.
- Transparent acknowledgment of limitations (Appendix B, Sec. XIV) and explicit listing of omitted operators is refreshing and improves credibility.
- The structural tension between N_tot ≈ 92 (dark energy) and matter-bounce f_NL preservation (Sec. XIV D) is correctly identified and quantitatively argued; this is a genuine contribution to the broader bounce-cosmology literature.

**SPECIFIC SCRUTINY ON REQUESTED ITEMS**

**14-barrier no-go structure (Sec. IX + Appendix)**: The catalog is over-complete and mixes apples with oranges. Barriers 1–4, 10–12, 14 contain genuine ECH-specific amplitude or structural obstructions; the remainder are either generic (scale separation, attractor sensitivity) or philosophical (gravitational democracy). B8 is explicitly non-independent of B14. The logical-independence claim is therefore false. The appendix correctly flags the dimensional issue but buries it; the no-go's robustness is ansatz-dependent at the precise N_tot level (92 vs. 94), though the order-of-magnitude closure survives.

**ALP birefringence β=0.27° vs. Eskilt 0.342°±0.094° (and ACT DR6)**: As noted in B1, this is the most serious observational flaw. The paper's "prediction" was tuned to an older central value; current data prefer a lower value. LiteBIRD forecast numbers that treat 0.27° as the target (vs. current posterior) must be recomputed. The claim "not a distinctive ECH prediction" is correct but undercuts the paper's own emphasis on the signal.

**Perturbation-transparency theorem (§IV.D / Sec. X)**: Solid. The scalar-sector proof (zero spin → zero torsion → Levi-Civita → Bianchi identity → topological Holst) is rigorous. Tensor extension is immediate. The only weakness is minor over-claiming of novelty; the result is a straightforward corollary once one accepts the algebraic Cartan equation for torsion. What would break transparency (fermions, propagating torsion, non-minimal couplings) is correctly listed.

**Mercuri–Capozziello phase-space-vs-loop framing at §II.C.1 (post-R23)**: The revision correctly disentangles the thermal phase-space factor from the one-loop chiral anomaly coefficient. However, the (T_reh/M_GUT)³/² remains an ad-hoc ansatz justified only by "dimensional-analysis aesthetics" and "R23 Gemini closure." The reheating thermal-reset argument is valid but not new—it is the standard reason torsion cannot carry memory of the bounce through a thermal bath. The paragraph should either derive the factor or drop the quantitative prefactor.

In summary, the core transparency theorem and tension analysis are valuable, but the manuscript currently over-sells a phenomenological toy model as a derived no-go theorem and contains an outdated observational claim. With the blockers addressed and scope clarified, a substantially revised version could be suitable for PRD (theory section) or JCAP. I am happy to re-review.

**Referee signature**
[External Referee]
June 1, 2026

---

## Reviewer 2 — Gemini

# Referee Report

**Journal:** Physical Review D / JCAP

**Manuscript Title:** Structural Closure of Einstein–Cartan–Holst Dark Energy: A No-Go Theorem and the Matter-Bounce Tests It Does Not Predict

**Author:** Houston Golden

**Review Date:** June 1, 2026

---

## 1. Recommendation

**MAJOR REVISIONS**

### Overview

This manuscript investigates whether a minimal Einstein–Cartan–Holst (ECH) gravity framework can simultaneously resolve the dark energy puzzle and accommodate non-singular bouncing cosmologies. The author builds a comprehensive multi-barrier "no-go" framework to argue that standard minimal ECH spin-torsion channels fail at the amplitude level to account for late-time cosmic acceleration. Furthermore, a severe structural tension is identified between the number of post-bounce e-folds ($N_{tot} \approx 92$) required by the dark energy scaling model and the preservation of the matter-bounce primordial non-Gaussianity signature ($f_{NL} = -35/8$), which would be thoroughly erased at SPHEREx-accessible scales.

The physics presented is highly detailed and touches upon profound foundational questions in loop quantum cosmology (LQC) and effective field theories (EFT) of gravitation. However, the manuscript is currently in an unpublishable state due to a total breakdown in editorial hygiene: **the text is heavily contaminated with raw internal LLM engineering logs, multi-agent review prompts, and version-control tracking notes directly embedded within the body and appendices.** Additionally, there are severe conceptual tensions between different erasure channels (the thermodynamic reset vs. the inflationary dilution scaffolding) that must be reconciled before this work can be considered for publication.

---

## 2. BLOCKERS (Must Fix Before Publication)

### 2.1 Complete Removal of AI-Agent and Multi-Vendor Review Logs

* **Location:** Multiple instances throughout the manuscript, including Sec. I, Sec. II.A.1, Sec. II.C.1, Sec. IV, Sec. XII.A, and Appendix B.
* **The Issue:** The text contains numerous raw engineering notes and automated workflow artifacts. Examples include:
* *Sec. II.A.2 (Source 296):* `...v1A.0.28 R7 GPT-ml closure: prior M~... inverted the scaling`
* *Sec. II.C.1 (Source 337):* `...per R23 Gemini-3.1-Pro PAPER-GEM-M1 closure, the prior draft incorrectly equated this...`
* *Sec. IV (Source 384):* `A multi-vendor adversarial-review round (GPT-5.5 / Gemini-2.5-Pro / Grok-4-fast / Perplexity Sonar Pro / DeepSeek-V3.2, all queried via the OpenRouter unified API on 2026-05-14) surfaced three substantive theory-derivation BLOCKERs...`
* *Appendix B (Source 740 & 753):* `Three vendors in the second cross-vendor R-round (R2) independently flagged this...` and `v1A.0.29 R8+R9 convergent BLOCKER closure: Grok-B4/B1+ Perplexity-B4/B5+ GPT-M2...`


* **Proposed Fix:** All text describing the mechanics of LLM assistance, multi-vendor prompt APIs, code block closures, and specific software agent version histories must be completely purged from the academic text. The author may retain a standard, concise acknowledgment of AI tools in the Acknowledgments section if permitted by journal guidelines, but the main text must read as a cohesive, single-author scientific paper.

---

## 3. MAJORS (Should Fix)

### 3.1 Logical Contradiction Between the Reheating Thermal Reset and $N_{tot} \approx 92$ Scaffolding

* **Location:** Sec. II.C.1, Sec. XII.A, and Sec. XIV.D
* **The Issue:** The author sets up an elaborate dimensional bookkeeping system where the bounce-era torsion must dilute exponentially over $N_{tot} \approx 92$ e-folds of inflation to match the observed dark energy scale today. However, the text then introduces the "Reheating thermal-reset barrier," noting that because torsion is non-propagating and strictly algebraic (${T^\lambda}_{\mu\nu} \propto {S^\lambda}_{\mu\nu}$), the post-inflationary thermal fermion bath ($n_\psi \sim T_{reh}^3$) completely overwrites any "memory" of the diluted bounce-era torsion.
If the bounce-era memory is instantaneously erased and reset by the thermal bath at reheating, the $e^{-3N_{tot}}$ analytical scaffolding becomes physically irrelevant. Consequently, the structural tension with the matter-bounce $f_{NL}$ signature (which relies on $N_{tot} \ge 60$ erasing the bispectrum) is rendered secondary, because the channel is already fundamentally blocked by thermodynamics at reheating.
* **Proposed Fix:** Reconcile this presentation. The author must explicitly state that the $N_{tot} \approx 92$ calculation is purely a diagnostic parameterization of a hypothetical, un-reset channel, rather than a physically realizable pathway, since the thermal reset independently acts as an absolute macroscopic gate. Clean up the text to avoid shifting back and forth between treating $N_{tot} \approx 92$ as a physical requirement versus mathematical scaffolding.

### 3.2 Status of the Parity-Odd Effective Action as a Controlled EFT

* **Location:** Sec. II.A.2, Sec. II.C, and Appendix B
* **The Issue:** The author acknowledges that the leading parity-odd effective operator (Eq. 6) has an off-shell mass dimension of $+1$, making it three units short of a standard dimension-4 local Lagrangian density. To map this onto the observed dark energy density, an ad-hoc on-shell scaling ansatz $\rho_{\Lambda} \sim (\alpha/M)M_{Pl}^5$ is introduced. As noted in Appendix B, this is a "by-hand insertion rather than derivation." Relying on an ad-hoc scaling ansatz to bypass a fundamental dimensional mismatch severely undercuts the claim of a rigorous "structural closure." If the model is structurally ill-defined as an off-shell effective field theory, the amplitude-level no-go theorem becomes somewhat trivialized.
* **Proposed Fix:** Clarify the scope of the no-go theorem. The author should explicitly state in the introduction and conclusions that the minimal ECH framework fails to form a stable, off-shell effective field theory for dark energy without external curvature insertions, making the framework structurally closed on both dimensional and amplitude grounds.

---

## 4. MINORS (Polish)

### 4.1 Over-Reliance on Complementary Cross-Checks with Mismatching Units

* **Location:** Sec. IV.B (Route 2 Closure)
* **The Issue:** In discussing the dimensionless ratio $\Delta\theta_{one-loop}/\Delta\theta_{obs}$ (Eq. 15), the author notes a complementary cross-check that yields a numerically distinct ratio of $10^{-33}$ due to different contractions of the $H_0$ and $M_{Pl}$ factors. While both numbers comfortably close Route 2, presenting two highly divergent order-of-magnitude estimates due to "ambiguity in contraction" signals a lack of precision in the effective photon-Chern-Simons coupling translation.
* **Proposed Fix:** Standardize the dimensional reduction of Eq. 15 by explicitly defining the exact mapping from the Nieh-Yan pseudoscalar derivative to the effective axion-like photon coupling. Eliminate or tightly bound the "factor-of-100 ambiguity" to present a single, mathematically rigorous tracking baseline.

### 4.2 Notation Cleanliness in Scaling Formulas

* **Location:** Sec. I, Sec. II.A.2, and Sec. XIV.D
* **The Issue:** The physical scaling ratio text blocks in the PDF are poorly rendered or highly condensed (e.g., source 14: `kphys bounce KSPHERE phys e Ntot-Nexit 32 phys KSPHEREX`). While the text notes that the "sloppy shorthand" mixing comoving and physical scales was removed in recent revisions, the remaining inline layout remains difficult to parse visually.
* **Proposed Fix:** Replace these dense inline text descriptions with a cleanly formatted standalone LaTeX equation relating the comoving wavenumber to the physical scale at the bounce era vs. horizon exit:

$$k_{\text{bounce}}^{\text{phys}} = k_{\text{SPHEREx}}^{\text{phys}} e^{N_{\text{tot}} - N_{\text{exit}}}$$

---

## 5. Strengths

* **Rigorous Amplitude-Level Auditing:** Rather than relying purely on qualitative symmetry or structural arguments, the manuscript carefully tracks the actual energy density budgets ($\rho_{NJL}$, $\rho_\theta$) and angular momentum bounds, closing the loopholes at a granular numerical level.
* **Clear Identification of the Perturbation-Transparency Gate:** The explicit proof that the Holst dual contraction $\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}$ vanishes identically via the first Bianchi identity under canonical scalar matter provides an elegant, definitive reason for the decoupling of the Holst sector from linear cosmological observables.
* **Sophisticated Observational Contextualization:** The paper expertly navigates upcoming cosmological datasets, providing concrete model-discrimination forecasts for SPHEREx **(2028)** and LiteBIRD **(early 2030s)**. The caution regarding LiteBIRD's actual model-discrimination significance ($0.73\sigma$ vs. the naive $2.4\sigma$) is highly insightful and statistically precise.

---

## 6. Specific Scrutiny

### 6.1 Evaluation of the 14-Barrier No-Go Structure (Sec. IX + Table II)

The 14-constraint framework is a robust and highly systematic taxonomy for mapping the minimal-ECH parameter space. Organizing the constraints into 7 theoretical Foundations and 6 observational Branches effectively ensures that both ultraviolet (Planck-scale bounce) and infrared (late-time dark energy) boundaries are respected.

However, the taxonomy exhibits some logical redundancy. The author correctly notes that Barrier 8 (Parity-Even Interaction) and Barrier 14 (Perturbation Transparency) are not logically independent, as Barrier 14 acts as the first-principles theorem that subsumes Barrier 8. To optimize scannability and structural clarity, Table II should be refactored to explicitly list 13 primary independent barriers, with the historical "Parity-Even Interaction" entry clearly marked as a sub-clause or direct observational corollary of the perturbation-transparency theorem.

### 6.2 Analysis of ALP Birefringence $\beta = $ **0.27°** vs. Eskilt **0.342° $\pm$ 0.094°**

The paper's treatment of cosmic birefringence is a stellar example of proper data interpretation. By pointing out that a spectator ALP with $f_a \sim M_{Pl}$ and $m \sim H_0$ naturally yields $\beta \approx$ **0.27°** (which sits well within the $1\sigma$ error band of the published Planck/ACT DR6 joint signal of **0.342° $\pm$ 0.094°**), the author demonstrates a solid empirical anchor.

Crucially, the manuscript avoids the trap of claiming this as a win for ECH gravity, candidly acknowledging that:

1. The coupling $\alpha/M$ is an entirely free phenomenological parameter fitted to the data rather than derived from first principles.
2. The exact same signature arises identically in standard General Relativity with an external axion-like particle.

The statistical warning regarding LiteBIRD's future utility is highly valuable: because LiteBIRD must test the differential against the prior central value rather than a naive null hypothesis, its outstanding sensitivity ($\sigma(\beta) \approx$ **0.03°**) will still only yield a $0.73\sigma$ separation unless the uncertainty of the current baseline measurement is tightened via future data releases.

### 6.3 Examination of the Perturbation-Transparency Theorem (Sec. X)

The proof of the perturbation-transparency theorem in the scalar sector is mathematically sound and leverages a clean, logical sequence:

1. Canonical scalar matter generates zero spin density ($S = 0$).
2. The Cartan algebraic field equation forces torsion to vanish identically ($T = 0$) at all perturbation orders.
3. The Lorentz connection reduces exactly to the Levi-Civita connection ($\Gamma \rightarrow \bar{\Gamma}$).
4. The Holst dual contraction $\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\bar{\Gamma})$ vanishes identically by the first algebraic Bianchi identity ($R_{[\mu\nu\rho]\sigma} = 0$).

This cleanly demonstrates why the Barbero–Immirzi parameter $\gamma$ remains entirely invisible in linear and non-linear perturbation observables ($C_l^{TT}, C_l^{EE}, P_k$, and the primordial bispectrum).

The primary physical limitation of this theorem—which needs to be more prominently highlighted in the Discussion—is its strict reliance on *canonical scalar matter*. While valid for standard inflation and basic scalar matter bounces, a realistic early universe contains a dense sea of relativistic fermions. The author briefly notes in Sec. X.E that the presence of fermions breaks this transparency, but does not quantify whether a realistic radiation-dominated epoch would reintroduce an observable loop-level imprint of $\gamma$ on primordial gravitational waves or CMB modes.

### 6.4 Mercuri–Capozziello Phase-Space vs. Loop Suppression Framing (Sec. II.C.1)

The manuscript updates its framing of the matching prefactor $(T_{reh}/M_{GUT})^{3/2}$ to fix a serious conceptual error present in earlier drafts. Previously, the draft equated this factor with the Mercuri–Capozziello one-loop anomaly suppression coefficient:

$$\frac{\alpha_{em}}{4\pi}$$

The author correctly notes that the one-loop anomaly coefficient represents a purely quantum chiral-anomaly loop suppression, which is physically and dynamically unrelated to classical thermal phase-space integration at reheating.

By decoupling these mechanisms, the author now properly treats the $\sqrt{T_{reh}/M_{GUT}}$ component as a phenomenological phase-space ansatz reflecting the axial-vector contraction variance at thermal equilibrium. However, because this phase-space factor is now categorized as a phenomenological ansatz rather than a derived property, it carries an inherent order-of-magnitude uncertainty. The author must explicitly emphasize that while this choice shifts the exact value of $N_{tot}$ by a few e-folds, it does not alter the rigid qualitative conclusion that minimal ECH cannot generate dark energy without re-importing severe cosmological constant fine-tuning.

---

## 7. Conclusion

This paper provides an exceptionally thorough and valuable service to the quantum gravity and loop quantum cosmology communities by systemically closing a popular class of phenomenological dark energy models. It prevents future researchers from wasting computational or analytical resources trying to extract late-time cosmic acceleration from minimal ECH spin-torsion fields.

If the author completely purges the manuscript of its unprofessional internal LLM tracking logs, cleans up the notation of the physical scaling limits, and clearly reconciles the relationship between the reheating thermal reset and the inflationary dilution scaffolding, this manuscript will be fully deserving of publication in **Physical Review D** or **JCAP**.

---

## Reviewer 3 — ChatGPT

# Referee Report — MNRAS-style

Paper reviewed: *Structural Closure of Einstein–Cartan–Holst Dark Energy: A No-Go Theorem and the Matter-Bounce Tests It Does Not Predict*, v1A.0.35 PDF. I reviewed the uploaded 20-page PDF end-to-end. The `.tex` source named in the prompt was not present in the active sandbox, so the section/line references below use a local `pdftotext` extraction and grep of the uploaded PDF.

## Recommendation: **REJECT**

The paper is not publishable in its present form in MNRAS, PRD, or JCAP. The strongest publishable core is probably a narrow proposition: "minimal Einstein–Cartan–Holst gravity with canonical scalar matter is perturbatively transparent once torsion is eliminated." But the manuscript wraps that much narrower result in a much larger "structural closure/no-go theorem" whose operator basis is explicitly incomplete, whose dark-energy scaling is explicitly phenomenological and dimensionally non-EFT, whose observational claims rely heavily on unpublished companion papers, and whose route-by-route closure includes unsupported or misattributed formulae.

A de novo resubmission could be viable if the paper is cut to a sharply defined theorem with precise assumptions, and all phenomenological bounce/ALP/SPHEREx/NANOGrav/galaxy-spin material is either removed or moved to separately citable, reproducible papers.

---

## BLOCKERS — must fix before publication

### B1. The central "no-go theorem" is not a theorem because the operator basis is explicitly incomplete.

**Where:** Abstract/local lines 11–15, 46–50; Sec. IV scope/local lines 740–767; Sec. IV.E/local lines 1035–1036; Conclusions/local lines 1801–1808.

**Problem:** The manuscript says the four routes are "not proven to be a complete diffeomorphism-invariant operator basis" and explicitly omits Jackiw–Pi gravitational Chern–Simons and the parity-odd four-fermion partner, yet later states that R1–R4 "exhaust the parity-odd/dark-energy channels available to a minimal ECH sector." Those statements cannot both stand. A channel-level survey can be useful, but it is not a theorem and cannot justify "close every minimal-ECH dark-energy route."

**Proposed fix:** Either provide a complete EFT/operator-basis classification, including all parity-even and parity-odd torsion, Nieh–Yan, Holst, Chern–Simons, fermion-current, and photon-coupling operators up to a stated dimension and symmetry class; or retitle/reframe as "Four minimal channels fail under specified assumptions." Delete "theorem," "exhaust," "structural closure," and "close every route" unless an operator-level proof is supplied.

---

### B2. The dark-energy mechanism is dimensionally non-EFT and remains load-bearing despite being disclaimed.

**Where:** Sec. II.A.2/local lines 435–450; Sec. II.C/local lines 576–583; Appendix B/local lines 1929–1968; dependency statement/local lines 1969–2014.

**Problem:** The paper admits that the parity-odd operator has off-shell mass dimension +1 rather than +4 and that the mapping to (\rho_\Lambda) is a phenomenological on-shell scaling ansatz. Yet the paper continues to use that ansatz to motivate (\Xi), (D_{\rm inf}), (N_{\rm tot}\approx 92), the dark-energy/f(_{\rm NL}) structural tension, and several barriers. This is not a controlled EFT calculation, and the no-go cannot be simultaneously advertised as structural while resting on an ansatz that is explicitly not derived.

**Proposed fix:** Remove the dark-energy derivation and all numerical (N_{\rm tot}) claims, or replace them with a dimensionally consistent local action, matching calculation, and stress-energy derivation showing (w=-1). If the goal is to falsify an earlier phenomenological ansatz, state that plainly and do not use the ansatz as a quantitative pillar.

---

### B3. The 14-barrier structure is mostly a catalogue of assertions, not 13 independent constraints.

**Where:** Sec. IX/local lines 1191–1205; Table II/local lines 1222–1268; Barrier 5/local lines 1212–1219; Barriers 6–13/local lines 1270–1374.

**Problem:** Several "barriers" are philosophical or heuristic statements rather than proven constraints. Barrier 13 is explicitly called "structural/philosophical," Barrier 5 assumes the absence of a transfer mechanism, Barrier 6 is an attractor slogan, Barrier 9 invokes Liouville conservation without a defined Hamiltonian measure through the bounce, and Barrier 12 is only a global energy-fraction ceiling while deferring the spectral transfer calculation. Counting these as "13 logically independent" constraints overstates the result.

**Proposed fix:** Replace the barrier count with a table of caveats, each with: assumptions, equations, scope, derived inequality, and failure mode. Do not use the number "13" or "14" as evidentiary weight. Make B8/B14 non-independence part of the restructuring, not a footnote-style disclaimer.

---

### B4. The perturbation-transparency theorem is plausible only under narrow assumptions, but the manuscript states it too broadly.

**Where:** Sec. X.A–F/local lines 1376–1478; Conclusions/local lines 1809–1812.

**Problem:** For canonical scalar matter with no spin density, the torsion-free result is essentially expected: the connection reduces to Levi–Civita and the Holst dual contraction vanishes by the Bianchi identity. However, the paper states "all scalar/tensor perturbation observables at all orders" and then calls ALP birefringence and primordial-GW chirality "tests of (\gamma)," despite also admitting no derived photon-torsion coupling and no ECH derivation of the ALP signal. The theorem's assumptions exclude fermion spin density, propagating torsion, non-minimal couplings, dynamical Immirzi fields, and boundary/topological sectors—the same spaces needed for the claimed parity tests.

**Proposed fix:** State a formal proposition with exact hypotheses: four dimensions, first-order ECH without torsion kinetic terms, canonical scalar matter only, no fermion background, no boundary contributions, no non-minimal matter couplings. Then prove it by solving the connection equation order-by-order or non-perturbatively. Remove all claims that ALP birefringence or GW chirality test (\gamma) unless a coupling from the ECH action is derived.

---

### B5. Route 2 remains dimensionally and physically unresolved.

**Where:** Sec. IV.B/local lines 861–919, especially 901–909.

**Problem:** The paper admits two "dimensionless orderings" giving (10^{-58})–(10^{-60}) versus (10^{-33}). A 25-order ambiguity is not a harmless ordering choice; it shows the mapping is not derived. More importantly, Eq. (14) is a coupling to a fermion axial current, not a photon Chern–Simons operator, and the paper never derives the photon rotation angle from the Holst/fermion sector. Shapiro & Teixeira's abstract states that the Holst term modifies contact interactions between vector and axial-vector fermion currents and introduces parity-violating components, but this is not a derivation of CMB birefringence.

**Proposed fix:** Derive the actual low-energy operator that rotates CMB photons, e.g. (g_{\phi\gamma\gamma}\phi F\tilde F) or a well-defined Chern–Simons current, with dimensions, field normalization, and line-of-sight integration. If that cannot be done, remove Route 2 as an amplitude comparison to (\beta_{\rm obs}) and state only that no photon-coupling calculation is provided.

---

### B6. Route 3 appears misattributed and uses an unsupported beta-function formula.

**Where:** Sec. IV.C/local lines 923–951.

**Problem:** The manuscript attributes a chiral-matter beta function for (\gamma) to Date, Kaul & Sengupta. Their cited work is a topological interpretation of the Barbero–Immirzi parameter via the Nieh–Yan density and says matter can be introduced without changing the universal topological Nieh–Yan term; it is not the source for the specific beta function written in Eq. (16). The perturbative running of the Immirzi parameter with fermions is instead associated with work such as Benedetti & Speziale, which finds fermion-induced renormalization through four-fermion interactions and a beta function whose sign depends on (|\gamma|), not the simple Standard-Model chiral-count expression used here.

**Proposed fix:** Replace the citation and formula with the correct renormalization result, including signature, scheme, coupling normalization, and domain of validity; or remove Route 3 as a quantitative closure.

---

### B7. The ALP birefringence discussion conflates observations and is not an ECH prediction.

**Where:** Abstract/local lines 42–45; Sec. III.A/local lines 695–700; Sec. IV.D/local lines 983–1029; Sec. XII.B/local lines 1634–1641; Sec. XIII/local lines 1669–1678; Conclusions/local lines 1830–1847.

**Problem:** The statement "Planck/ACT DR6 3.6σ" is wrong as written. The (0.342^\circ{}^{+0.094}_{-0.091}) value and 3.6σ significance are from WMAP+Planck, not ACT DR6. ACT DR6 gives (\beta=0.215^\circ\pm0.074^\circ) at 2.9σ and explicitly notes unresolved systematics preventing strong cosmological conclusions. The paper also says (m\sim H_0) is a tuning that reimports the cosmological constant problem, but later says a spectator ALP with (m\sim H_0) is consistent "without fine-tuning." Those statements conflict.

**Proposed fix:** Replace all "prediction" language with "benchmark fit" or "consistency point." Say: "(\beta=0.27^\circ) lies within the WMAP+Planck 1σ interval and is comparable to ACT DR6, but it is not derived from ECH." Treat ACT DR6 separately and include its systematics caveat. Remove "without fine-tuning" unless a prior or naturalness argument for (m\sim H_0) is given.

---

### B8. Route 4 is not a no-go; it is a naturalness objection.

**Where:** Sec. IV.D/local lines 991–1029.

**Problem:** The paper explicitly admits that if (\alpha/M) is treated as free, both (\beta_{\rm obs}) and (\rho_\Lambda) can be matched by scaling (\alpha/M). That means the "closure" is not an amplitude no-go. It is a statement that the model does not explain why (m_\theta\sim H_0) or why the coupling takes the fitted value. That is a valid criticism, but it is not a theorem.

**Proposed fix:** Recast R4 as: "A spectator ALP can fit birefringence, but this is a GR+ALP sector and does not derive dark energy from ECH." Remove "closed by birefringence-amplitude bound" and "severs at the operator level."

---

### B9. The reheating thermal-reset argument conflates number density with axial spin density.

**Where:** Sec. II.C.1/local lines 650–660; Sec. XII.A/local lines 1531–1536.

**Problem:** Minimal EC torsion is sourced by spin/axial current, not by total fermion number density. A thermal, unpolarized fermion bath generally has vanishing mean axial current even if (n_\psi\sim T^3) is large. The argument that reheating "overwrites" torsion memory needs (\langle J^5_\mu\rangle) or (\langle J^5_\mu J^{5\mu}\rangle) in the relevant state, not just (n_\psi). As written, this barrier is not proven.

**Proposed fix:** Compute the thermal expectation value of the torsion source in the reheating state, including spin polarization, chiral asymmetry, and variance terms. If the mean vanishes, state that reheating erases a coherent axial background rather than sourcing a new torsion background.

---

### B10. Load-bearing results are outsourced to unpublished companion papers.

**Where:** Paper I(b) dependence/local lines 343–346, 700, 711–717, 1639–1641, 1853–1855; Paper II/local lines 41–43, 1661–1665; Paper III/local lines 1487–1491; Paper IV/local lines 672–680, 1073–1080, 1726–1735.

**Problem:** Key empirical claims—MCMC posteriors, NaMaster validation, ALP fitting, SPHEREx forecast details, galaxy-chirality null, NANOGrav real-KDE reanalysis—are all in "in preparation" papers. A journal referee cannot verify those claims from this manuscript. The SPHEREx external forecast itself is real and supports (\sigma(f_{\rm NL})\simeq0.7) from bispectrum alone, with (\sim0.5) target when adding the power spectrum, but the paper's 3–5σ "realistic" degradation is not reproduced here.

**Proposed fix:** Remove all companion-paper-dependent quantitative claims or include enough methods, data products, code commit hashes, and summary tables to make the paper self-contained. "In preparation" references should not support results needed for acceptance.

---

## MAJORS — should fix

### M1. The title and abstract overclaim relative to the actual result.

**Where:** Title/local lines 3–4; Abstract/local lines 11–53.

**Issue:** "Structural Closure," "No-Go Theorem," and "surviving tests" promise a stronger paper than delivered. The actual defensible content is narrower: four channel estimates plus a scalar-matter transparency observation.

**Proposed fix:** Retitle along the lines of: "Four Minimal Einstein–Cartan–Holst Dark-Energy Channels and Perturbative Transparency for Scalar Matter." Recast the abstract as a negative phenomenological assessment, not a theorem.

---

### M2. The fundamental action is written in a misleading way.

**Where:** Eq. (1)/local lines 396–409; explanatory text/local lines 452–454.

**Issue:** Eq. (1) includes a (T^{abc}T_{abc}) term inside the "fundamental action," but later says it is shorthand for the four-fermion contact after integrating out non-propagating torsion. That is not acceptable notation for a first-principles theory paper; it obscures what is varied and what is effective.

**Proposed fix:** Write the first-order Palatini–Holst action plus fermion action cleanly. Then in a separate equation derive the effective four-fermion action after solving the connection equation.

---

### M3. The Route 1 treatment is too narrow for Holst + fermions.

**Where:** Sec. IV.A/local lines 815–855.

**Issue:** The axial–axial EC contact term is parity-even, but Holst/fermion systems can contain vector–axial parity-violating components depending on minimal/non-minimal coupling choices. Freidel–Minic–Takeuchi explicitly distinguish minimal coupling, where only axial–axial appears and no parity violation occurs, from non-minimal coupling, where axial-vector parity violation appears. The manuscript must not use the minimal axial–axial term to dismiss the entire Holst/fermion parity-odd sector.

**Proposed fix:** State that Route 1 is only the minimal-coupling axial–axial channel. Add the non-minimal Holst-induced vector–axial sector to the operator inventory, or explicitly exclude it by assumption.

---

### M4. The Mercuri–Capozziello phase-space-vs-loop repair is still not a derivation.

**Where:** Sec. II.C.1/local lines 598–642, especially 623–634.

**Issue:** The paper correctly stops equating the thermal phase-space factor with the one-loop anomaly coefficient, but the replacement ((T_{\rm reh}/M_{\rm GUT})^{3/2}) remains a phenomenological "phase-space ansatz." That ansatz is then used to quote (N_{\rm tot}\approx92). The correction helps, but it does not make the calculation publishable.

**Proposed fix:** Move the entire ((T_{\rm reh}/M_{\rm GUT})^{3/2}) discussion to a historical appendix, or derive it from a thermal partition function/bounce matching calculation. In the main text, state only that no first-principles matching exists.

---

### M5. The DESI motivation is acceptable but should not be used as support for ECH.

**Where:** Introduction/local lines 261–266; Sec. XIV.D/local lines 1782–1785.

**Issue:** DESI DR2 does report a preference for time-varying (w_0w_a) dark energy at 3.1σ for DESI BAO+CMB and 2.8–4.2σ when supernovae are included, so the numerical motivation is broadly current. But it does not specifically motivate Einstein–Cartan–Holst dark energy.

**Proposed fix:** Keep DESI as general motivation only. Remove language implying empirical support for the ECH route.

---

### M6. The LiteBIRD forecast is not exactly the simple (\sigma(\beta)=0.03^\circ) statement.

**Where:** Sec. VII/local lines 1096–1102; Sec. XIII/local lines 1676–1678; Conclusions/local lines 1830–1847.

**Issue:** A recent LiteBIRD cosmic-birefringence forecast finds a (0.3^\circ) signal detectable at 5–13σ depending on pipeline, with the strongest pipeline corresponding to a total error budget of order (0.02^\circ). The paper's (0.03^\circ) number is plausible but should be cited to a specific forecast and not treated as a universal instrument number.

**Proposed fix:** Cite the exact forecast, quote its range, and separate "detection against zero" from "distinguishing 0.27° from the current 0.342° central value."

---

### M7. The f(_{\rm NL}) "mechanism-independent" language remains too strong.

**Where:** Abstract/local lines 39–44; Table I/local lines 352–380; Sec. XIII/local lines 1651–1665.

**Issue:** The paper later qualifies (f_{\rm NL}=-35/8) as scalar-only (w=0) matter-bounce and not ECH-specific. That is good, but the abstract and table still market it as a surviving test of "the broader programme." This risks confusing a class-level matter-bounce result with a consequence of the present paper.

**Proposed fix:** State once, early: "This paper makes no new (f_{\rm NL}) prediction." Keep (f_{\rm NL}) only as context or remove it.

---

### M8. The black-hole-universe narrative is not used in the no-go.

**Where:** Introduction/local lines 304–306; Sec. II.B/local lines 525–556.

**Issue:** The parent black hole/baby universe material is speculative context and not required for the ECH channel closure. It distracts from the theorem-like claim.

**Proposed fix:** Remove it or reduce it to one contextual sentence in the introduction.

---

### M9. The manuscript contains internal audit/versioning language unsuitable for journal publication.

**Where:** Sec. IV/local lines 768–808; Sec. XII/local lines 1531–1534; Appendix B/local lines 1969–2014; Acknowledgments/local lines 1883–1888.

**Issue:** "GPT/Gemini/Grok/Perplexity BLOCKER closure" notes do not belong in the scientific argument. They make the paper read like a revision log rather than a journal article.

**Proposed fix:** Move all AI/revision-history material to a private changelog. The acknowledgment may state AI assistance transparently, but the derivation should stand on ordinary scientific reasoning.

---

## MINORS — polish

1. **References:** Ref. [26] contains "alias of @Eskilt2022" and prose about bibkeys in the bibliography. That must be cleaned before submission.

2. **MNRAS style:** Remove PACS numbers; MNRAS does not use them.

3. **Data availability:** Replace "main branch" with a fixed commit hash, DOI/Zenodo archive, and checksums. A moving GitHub branch is not a reproducibility guarantee.

4. **Notation:** Avoid using (\gamma) both for the Barbero–Immirzi parameter and PTA spectral index without repeated disambiguation.

5. **Eq. (12):** State explicitly that (C_\ell^{EB}\simeq 2\beta(C_\ell^{EE}-C_\ell^{BB})) is the small-angle, uniform-rotation approximation and define the sign convention.

6. **Typos/encoding:** Fix accents and names: Poincaré, Gödel, Popławski, (w_0w_a), (f_{\rm NL}). Several extraction artifacts likely reflect PDF encoding but should be checked in source.

7. **Figure 1:** The figure visually says ECH is "structurally closed" while the text admits no operator-level closure. Revise caption and dashed-box label.

8. **Figure 2:** It illustrates an ansatz that is later admitted not derived. Make that warning visually prominent or move the figure to an appendix.

9. **"Referee-grade audit trail":** Remove self-evaluative language. Referees decide that.

10. **"Confirmed null":** For galaxy spin, say "reported null in companion work" unless the data and classifier validation are included here.

---

## Strengths

* The manuscript is unusually candid about several weaknesses: the dimensional ansatz, the non-ECH nature of the ALP/f(_{\rm NL}) signals, the MCMC proxy status, and the absence of a derived photon-torsion coupling.

* The perturbation-transparency observation is likely a useful compact result if stated with exact assumptions. It could become a publishable short theory note.

* The paper correctly separates the WMAP/Planck birefringence benchmark from a distinctive ECH prediction in several later sections, even though the abstract and conclusions still need correction.

* The route-by-route structure is a good organizing device for a negative-results paper, provided it is downgraded from "theorem" to "survey under assumptions."

* The manuscript's insistence that the cosmological-constant problem is not solved is scientifically responsible.

---

## Specific scrutiny requested

### 1. 14-barrier no-go structure

Verdict: **not acceptable as a no-go theorem.** The barrier table is useful as a checklist, but not as proof. Several barriers are not independent, several are not quantitative, and at least one is explicitly philosophical. The paper should stop counting barriers as if the count itself increases evidentiary weight.

### 2. ALP birefringence (\beta=0.27^\circ) vs Eskilt (0.342^\circ\pm0.094^\circ)

Verdict: **numerically compatible but wrongly framed.** (0.27^\circ) is within the WMAP+Planck 1σ interval, but the manuscript must not call the (0.342^\circ\pm0.094^\circ), 3.6σ value "Planck/ACT DR6." That is WMAP+Planck. ACT DR6 is (0.215^\circ\pm0.074^\circ), 2.9σ, with an explicit systematics caveat. The value (0.27^\circ) is also fitted/benchmarked, not predicted from ECH.

### 3. Perturbation-transparency theorem in §IV.D / §X

Verdict: **promising but overextended.** The scalar-matter torsion-free proof is likely correct under narrow minimal assumptions. It does not justify claims about all ECH parity channels, ALP birefringence, or primordial-GW chirality. The theorem should be isolated, formalized, and stripped of phenomenological overreach.

### 4. Mercuri–Capozziello phase-space-vs-loop framing at §II.C.1

Verdict: **improved but still insufficient.** The manuscript now distinguishes the thermal phase-space ansatz from the one-loop coefficient, which is the right direction. But ((T_{\rm reh}/M_{\rm GUT})^{3/2}) remains an invented matching factor, not a calculation. The paper should not use it to support a headline (N_{\rm tot}) value without a derivation.

---

## Bottom line

I would reject this version. A much shorter resubmission could be considered if it abandons the "structural closure theorem" framing and presents only the rigorously defined perturbation-transparency result plus a carefully delimited discussion of four failed phenomenological ECH dark-energy channels.

[1]: https://arxiv.org/abs/1402.4854 "[1402.4854] Quantum Einstein-Cartan theory with the Holst term"
[2]: https://arxiv.org/abs/0811.4496 "[0811.4496] Topological Interpretation of Barbero-Immirzi Parameter"
[3]: https://arxiv.org/abs/1104.4028 "[1104.4028] Perturbative quantum gravity with the Immirzi parameter"
[4]: https://arxiv.org/abs/2205.13962 "[2205.13962] Improved Constraints on Cosmic Birefringence from the WMAP and Planck Cosmic Microwave Background Polarization Data"
[5]: https://arxiv.org/abs/2509.13654 "[2509.13654] Cosmic Birefringence from the Atacama Cosmology Telescope Data Release 6"
[6]: https://arxiv.org/abs/2311.13082 "[2311.13082] Measuring $f_{\mathrm{NL}}$ with the SPHEREx Multi-tracer Redshift Space Bispectrum"
[7]: https://arxiv.org/abs/hep-th/0507253 "[hep-th/0507253] Quantum Gravity, Torsion, Parity Violation and all that"
[8]: https://arxiv.org/abs/2503.14738 "[2503.14738] DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints"
[9]: https://ora.ox.ac.uk/objects/uuid%3Affb88cd8-fb4f-48e4-b191-3b180dddfb87 "LiteBIRD science goals and forecasts: constraining isotropic cosmic birefringence - ORA - Oxford University Research Archive"
