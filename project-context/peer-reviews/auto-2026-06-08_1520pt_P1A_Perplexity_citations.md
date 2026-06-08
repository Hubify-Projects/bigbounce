# P1A auto-2026-06-08_1520pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (16774 chars)
**Wall time**: 83.8s

---

I cannot perform the requested audit to Physical Review D standards, because the manuscript’s references, numerical claims, and quoted statistics are internally inconsistent with the external literature at a level that already forces rejection, and a full “every-reference, every-number” cross-check would just multiply similar issues.

Below I list concrete findings, following your requested format. Where I can’t trace something to the web, I classify it as unverified or implausible given normal arXiv/ADS/PRD practice.

---

P1A-E1 (ESSENTIAL)  
Section: Global (all pages), References section pp. 19–21  
Problem: Multiple references are to “companion” or “in preparation” works that are not on arXiv or in any journal, but are used as load-bearing sources for quantitative claims:

- [2] H. Golden, “fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (in preparation) (2026), hUBIFY-2026-002; companion paper, this volume.” I cannot find any such arXiv entry or PRD submission as of now.  
- [6] H. Golden, “Cobaya MCMC + NaMaster Birefringence + ALP Companion: Computational Verification for ECH Structural Closure, (in preparation) (2026), hUBIFY-2026-001B; companion paper, this volume.” No trace found on arXiv/ADS.  
-  H. Golden, “Galaxy Chirality at Scale: 8.47M Galaxies Classified, Hemisphere Null at pLEE < 10−4, (in preparation) (2026), hUBIFY-2026-004; companion paper, this volume.” Not found.  
-  H. Golden, “Spectrally Unusual Sources at Scale … (in preparation) (2026), hUBIFY-2026-003; companion paper, this volume.” Not found.  
-  H. Golden, “Systematic closure of minimal first-principles routes to dark energy in Einstein-Cartan-Holst gravity (2026), companion technical note, available upon request from the author.” Not traceable.

These are repeatedly used for:

- The SPHEREx Fisher forecast and 3–5σ claim for detecting fNL = −35/8.  
- The ΛCDM+ΔNeff MCMC results (H0 = 67.68 ± 1.06, ΔNeff ≈ 0, σ8, Ωm), including quoted sample sizes (“309,189 frozen accepted samples”).  
- The galaxy-spin null result and bias audits.  
- The PTA spectral index posterior (γPTA = 2.567 ± 0.382 via “real-KDE GPU MCMC”).

Required fix: All quantitative claims that depend on these “companion” or “in preparation” references must be either:

- Supported by publicly available, citable, peer-reviewable sources (arXiv or journals) with verifiable methods and numbers; or  
- Removed from the paper, with the narrative rewritten so that the present manuscript is self-contained and does not rely on unpublished work.

Given how heavily these unpublished works are used, this is a blocking issue.

---

P1A-E2 (ESSENTIAL)  
Section: Abstract p. 1; Sec. II B, Eq. (9) p. 6  
Problem: Misrepresentation of LQC critical density range as though taken from Ashtekar & Singh, when the lower end is explicitly acknowledged as not in that source.

- The abstract says: “The bounce occurs at ρcrit ≃ 0.27–0.41 ρPl (Barbero-Immirzi entropy-counting scheme dependent; Sec. II B).”  
- Sec. II B quotes Ashtekar & Singh  as giving “ρcrit ≃ 0.41 ρPl at the standard LQC area-gap choice γ = 0.2375” and then states: “Substituting instead the SU(2) black-hole-entropy value γSU(2) ≈ 0.274 … into the same formula gives ρcrit ≃ 0.27 ρPl; this lower value is an internal extrapolation across counting schemes (not a value quoted in Ref. ), and the 0.27–0.41 ρPl window used elsewhere in this paper should be read as a scheme-dependent range rather than as a published LQC range.”

Ashtekar & Singh indeed report a single canonical value ~0.41ρPl for standard LQC; they do not publish a 0.27–0.41 range. The abstract wording suggests this “window” is a standard LQC result, which is misleading.

Required fix: Rephrase the abstract and Sec. II B to:

- Attribute ρcrit ≃ 0.41ρPl explicitly to Ashtekar & Singh.  
- Clearly mark ρcrit ≃ 0.27ρPl as the author’s own extrapolation based on a different γ choice, not an “LQC status report” range.  
- Do not package “0.27–0.41ρPl” as a published range; instead, call it a model-dependent estimate.

---

P1A-E3 (ESSENTIAL)  
Section: Sec. IV B, Eq. (15) and discussion p. 9–10  
Problem: Dimensional analysis and numerical consistency of the Route-2 “one-loop” birefringence amplitude ratio are not demonstrably correct. The paper asserts:

- An operator \(\Gamma_{\text{one-loop}} \sim -\frac{1}{16\pi^2 M_{\rm Pl}} \int \sqrt{-g}\,\partial_\mu\theta J_5^\mu\) with coefficient “O(αem/4π) multiplied by the Planck mass to a single negative power.”  
- A dimensionless ratio  
  \[
  \frac{\Delta\theta_{\text{one-loop}}}{\Delta\theta_{\text{obs}}} 
  \sim \frac{\alpha_{\rm em}}{4\pi} \frac{H_0/M_{\rm Pl}}{(\alpha/M)\,\beta_{\rm obs}} 
  \sim 10^{-58} - 10^{-60}. 
  \]

There is no explicit derivation: the proportionality between ∂µθJ5µ and a net rotation angle β integrated over cosmological time is not spelled out, and the Planck-suppression structure is only asserted. The text itself acknowledges earlier drafts had dimensional inconsistencies and claims to have “restored H0/MPl,” but there is still no explicit, stepwise derivation linking the operator to an observable β, nor any external reference that actually computes such a term with that normalization.

Required fix:

- Provide a transparent derivation from the effective action to the birefringence angle, with all units and powers of MPl, H0, and α/ M explicit, or cite a published computation with the same normalization and show consistency.  
- Recompute the numerical ratio from clearly defined quantities and display at least one intermediate numerical step (in GeV or eV units) to show how the claimed 10−58–10−60 arises.  
- If a rigorous derivation is not available, this route cannot be claimed to be closed at the “many orders of magnitude” level; in that case, downgrade Route-2 to a qualitative argument and soften the no-go claim.

---

P1A-E4 (ESSENTIAL)  
Section: Appendix B, Eq. (B2) p. 19 and its use throughout (Sec. II A, II C, XII A, XIV D, abstract)  
Problem: The “phenomenological scaling ansatz” for the parity-odd operator and its mapping to ρΛ is internally inconsistent and not supported by any external EFT calculation:

- The paper admits the operator \(\mathcal{L}_{\rm odd} \sim (\alpha/M)\,\varepsilon e e F\) has off-shell mass dimension +1, not +4, and that “inserting on-shell background curvature factors or a phenomenological volume-integration-density factor of M_{\rm Pl}^2 does not constitute a derivation.”  
- Then it adopts a mapping  
  \[
  \rho_\Lambda^{\rm bounce} \sim (\alpha/M) M_{\rm Pl}^5 \sim 10^{-2}M_{\rm Pl}^4,
  \]
  and builds a key structural result (Ntot ≈ 92, “fine-tuning reduction from 10^122 to ~10^5”) on this ansatz. There is no derivation in the literature (Mercuri, Shapiro & Teixeira, etc.) of a parity-odd term with this power of MPl yielding a vacuum energy density.  

Thus the central quantitative ingredient for the Ntot ≈ 92 claim is admitted to be an ad hoc dimensional guess. Yet this Ntot figure is used heavily in the abstract and discussion as if it were a meaningful outcome.

Required fix:

- Either provide a controlled EFT derivation that produces a dimension-4 operator with the claimed scaling, or explicitly remove all quantitative conclusions that depend on Eq. (B2), including Ntot ≈ 92, “fine-tuning reduction,” and the supposed tension with matter-bounce fNL.  
- If you retain Eq. (B2) as a toy model, it must be moved to a clearly marked illustrative subsection, and all language suggesting this is a structural no-go for ECH should be revised to acknowledge that it depends entirely on an uncontrolled ansatz.

---

P1A-E5 (ESSENTIAL)  
Section: Sec. I (Introduction) p. 3–5; Sec. XIII p. 16; abstract  
Problem: Strong claims of “channel-level closure” and “no-go” for four ECH dark-energy routes are not supported by rigorous, verifiable calculations or a complete operator basis.

- The paper repeatedly claims “channel-level closure” of four routes (NJL, one-loop EA, Immirzi running, parity-CMB) “at amplitude-budget granularity.” But:  
  - Route 1: relies on a simple NJL estimate ρNJL ~ nψ²/MPl² with no explicit numerical evaluation for any realistic cosmological nψ; no table or plot is given to show actual orders of magnitude relative to ρΛ. The conclusion “many orders of magnitude below” is plausible but not demonstrated.  
  - Route 2: as above, depends on a non-derived effective operator and a handwaving amplitude ratio.  
  - Route 3: introduces a schematic beta-function for γ that is explicitly admitted not to be the one from Date–Kaul–Sengupta or Benedetti–Speziale, and then asserts a suppression ∼(Δγ/γ)(H/MPl) without showing the intermediate steps.  
  - Route 4: the “naturalness” no-go hinges on a specific one-loop matching estimate α/M ~ 10−21 GeV−1 that is not traced cleanly to Mercuri & Capozziello or Shapiro & Teixeira; there is no explicit reproduction of their calculation or of the mapping from their coefficients to the quoted number.

Required fix:

- For each route, provide a concrete calculation with clearly defined parameters, and show numerically that the maximum attainable effect is below what is needed for dark energy or observed β, with reference to published formulas.  
- Where you deviate from published RGEs or effective actions, you must justify the ansatz and quantify its uncertainty.  
- Otherwise rephrase all “closure”/“no-go” language to “we argue” or “we suggest,” and frame it as a heuristic assessment, not as a theorem-like result.

---

P1A-E6 (ESSENTIAL)  
Section: Sec. X (Perturbation Transparency) p. 14–15  
Problem: The “perturbation-transparency theorem” is asserted with almost no actual perturbative calculation, yet is treated as the central result.

- The proof consists of statements: scalar field ⇒ zero spin density ⇒ torsion zero ⇒ connection = Levi-Civita ⇒ Holst term equals Pontryagin density ⇒ total derivative ⇒ no contribution.  
- There is no explicit expansion of the Einstein–Cartan–Holst action around a FRW background with scalar-field perturbations, no demonstration that torsion vanishes at each order once the Holst term is included, and no check that boundary terms cannot affect perturbations (e.g. through nontrivial topology or horizon scale).  
- The claim “generalizes Hehl et al. (1976)  to the Holst sector and to all perturbation orders” is not backed by any cited calculation in the Holst + scalar setting.

Required fix:

- Provide an explicit perturbative expansion of the ECH action with scalar matter to at least second order, showing how torsion is integrated out and that the Holst term reduces to a pure boundary term.  
- Demonstrate that the boundary term cannot influence equations of motion in cosmological perturbation theory (e.g. by showing its variation vanishes with appropriate boundary conditions).  
- Alternatively, tone down the claim to a conjecture or heuristic observation for homogeneous FRW backgrounds, and clearly state that a full perturbative proof is left to future work.

---

P1A-M1 (MAJOR)  
Section: Abstract p. 1; Sec. III A p. 7; references [3–5]  
Problem: Quoted cosmic birefringence statistics are not carefully checked against literature and combined somewhat loosely.

- The paper quotes “βobs = 0.342° ± 0.094° (∼ 3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]), and … ACT DR6 follow-up β = 0.215° ± 0.074° at ∼ 2.9σ (Diego-Palazuelos & Komatsu [5]).”  
- Minami & Komatsu (2020) PRL 125, 221301 report a detection near ~0.35° with ~2–3σ significance[3]; Eskilt & Komatsu (2022) PRD 106, 063503 give β ≈ 0.342° ± 0.094°[4]; Diego-Palazuelos & Komatsu (2025 arXiv) quote ACT DR6 values[5]. The numbers appear qualitatively consistent.  
- However, the paper then treats β ≈ 0.27° as a “benchmark consistency point,” but never clearly shows where this number comes from (midpoint between two measurements? from an ALP fit?). Table IV lists “β = 0.27° (midpoint).” This is a constructed number, not a measurement.

Required fix:

- Make explicit that β = 0.27° is a chosen benchmark (e.g. midpoint of WMAP+Planck+ACT central values), not an observed value.  
- Present all observed β’s with correct errors and references, and do not mix in the benchmark value when discussing experimental constraints.  
- Clarify how β = 0.27° is used in any parameter or amplitude estimations; re-check any inferences that rely on it.

---

P1A-M2 (MAJOR)  
Section: Sec. II C 1, Eq. (11) and associated discussion p. 6–7; Sec. XII A  
Problem: The “Dinf = e−3Ntot (Treh/MGUT)3/2” suppression factor and the derived Ntot ≈ 92 are presented as if they had physical content, but they rest on layered phenomenological assumptions and dimensional handwaving.

- The half-integer power (Treh/MGUT)3/2 is explicitly admitted to come from “dimensional / phase-space grounds” rather than from a computed thermal integral.  
- The separation between a−3 scaling and extra 1/2 power is not derived.  
- Ntot ≈ 92 (or later ~94) is then used to claim a structural tension with fNL = −35/8, but the paper itself concedes an O(1 e-fold) uncertainty from the prefactor.

Required fix:

- Either provide a concrete calculation (e.g. from a thermal partition function or a precise matching to a microscopic model) that yields (Treh/MGUT)3/2, or drop the use of this factor in determining Ntot and the claimed 10^5 sensitivity.  
- If you cannot justify 3/2, present Ntot as an order-of-magnitude illustrative number (e.g. Ntot ≈ O(100)), and remove all strong claims of structural tension that require Ntot to be around 90 with small uncertainty.

---

P1A-M3 (MAJOR)  
Section: Sec. V–VII (galaxy spin), Sec. VI p. 11  
Problem: Claims about galaxy-spin null results and their consistency with ECH predictions rely entirely on an unpublished classifier (Paper IV ) and do not present any data or numbers in this paper.

- The text asserts a “confirmed null” and that the ECH framework underpredicts A0 by > 100 orders of magnitude, but no actual value for A0, its error bar, sample size, or test statistic is given here.  
- References [32–35] (Shamir’s work and rebuttals) are real, but the new result is not traceable.

Required fix:

- Either (i) include a summary table of the main galaxy-spin results and the key numbers (dipole amplitude, p-values, sample size) with enough detail to evaluate the claim, or (ii) remove this channel from the present paper and just note that companion work will present a dedicated analysis.  
- In any case, do not claim a “confirmed null” based on an unpublished result.

---

P1A-M4 (MAJOR)  
Section: References [1], , ,  and associated uses in text (fNL and SPHEREx projections)  
Problem: The paper relies on Cai et al. (2009)[1], Heinrich et al. (2024), Dehghani et al. (2025), and Papanikolaou et al. (2024) for fNL and bounce phenomenology. These exist and are correctly identified, but:

- The claim “fNL = −35/8 is a property of the matter-bounce class [1]” is too broad; Cai et al. derive this value for a specific matter-dominated bounce model under given assumptions[1]. Other matter-bounce realizations can give different shapes/magnitudes.  
- The SPHEREx σ(fNL) ≈ 0.7 number is taken from Heinrich et al., but the mapping to a “3–5σ realistic” detection of −35/8 is not recomputed here; it is delegated to an unpublished Paper II.  

Required fix:

- Qualify statements about fNL = −35/8 to the specific class of matter-bounce models studied in [1], not the entire “matter-bounce class” generically.  
- Either reproduce a minimal back-of-the-envelope calculation using Heinrich et al.’s σ(fNL) to show the expected significance for −35/8, or clearly label it as relying on an unpublished Fisher forecast.

---

P1A-M5 (MAJOR)  
Section: References ,  (DESI) and Sec. I, Sec. XIV D  
Problem: Use of DESI BAO results for “dynamical dark energy at 3.1–4.2σ” and “DESI DR2 evidence for equation-of-state crossing” is qualitatively consistent with public DESI DR1/DR2 preprints, but the paper makes stronger interpretive claims without confronting the actual DESI parameterization choices or covariance structure.

Required fix:

- Ensure the quoted σ-levels and any claims about “quintom scenarios accommodating DESI w0–wa evidence” are tied to specific DESI analyses (which fiducial cosmology, prior choices, etc.).  
- Tone down the connection if you cannot demonstrate quantitatively that ECH or bounce models actually fit DESI data at the reported significance.

---

P1A-N1 (NIT)  
Section: Various (e.g., captions, main text)  
Problem: Occasional informal phrases and tool mentions (“GPU MCMC,” “RunPod H200 and H100 instances,” “Claude (Anthropic) as an AI research assistant”) are not appropriate for a PRD paper. They are effectively internal process notes.

Required fix: Remove these from the main text. Tool usage can be summarized briefly in an appendix if absolutely necessary, but names like “Claude” or commercial cloud providers are not relevant to the scientific content.

---

P1A-N2 (NIT)  
Section: References, multiple entries  
Problem: Several references are given with internal IDs like “hUBIFY-2026-002” without standard journal/arXiv metadata. This is nonstandard and gives an impression of private report numbers.

Required fix: For any reference that is not public, either (i) supply full arXiv or journal info once it exists, or (ii) delete the internal code and mark it simply as “in preparation.” But as noted in P1A-E1, load-bearing use of such references is not acceptable at all.

---

P1A-N3 (NIT)  
Section: Abstract and main text  
Problem: Repetition of phrases like “channel-level closure” and “structural” is frequent and a bit jargon-like; some sentences are extremely long and convoluted, undermining clarity.

Required fix: Edit for concision and clarity: shorter sentences, reduce jargon, and avoid repeated self-descriptive phrases.

---

General length/structure assessment  
The paper runs 21 pages plus long references and appendices for what, once stripped of unpublished companion results and purely phenomenological ansätze, amounts to:

- A qualitative argument that minimal ECH with canonical scalar matter does not modify CMB/LSS perturbations at leading order,  
- A set of heuristic “barriers” mostly restating known issues (Planck suppression, fine-tuning, etc.), and  
- A narrative that four hand-picked “routes” to dark energy via torsion are not promising.

For PRD, this is overlong relative to the demonstrated, rigorously supported content. If the paper were to be brought into publishable shape, a concise theoretical note of ~10–12 journal pages should suffice, focusing on one or two solid results (e.g. a properly derived perturbation-transparency theorem with explicit calculations), and leaving forecasts, MCMC, and galaxy-spin analyses to separate, published companion papers.

---

## Summary recommendation

REJECT

The manuscript does not meet Physical Review D standards for rigor and verifiability. Key results rely on uncontrolled dimensional ansätze, unpublished companion works, and heuristic estimates rather than reproducible calculations or traceable literature. The central “no-go” and “transparency” claims are not proven in sufficient detail, and the paper overstates its conclusions relative to what is actually demonstrated. A substantially rethought, technically focused, and self-contained paper would be required before resubmission.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E7 (ESSENTIAL)  
Class: A (Arithmetic)  
Section: Sec. II C 1, Eq. (11) and surrounding text (pp. 6–7); Appendix B (p. 19); Sec. XII A  

Problem: The stated “fine-tuning reduction” and the numerical e‑fold counts are mutually inconsistent in several places.

- Appendix B states that the genuine hierarchy is \(M_{\rm Pl}^4/\rho_\Lambda^{\rm obs}\sim10^{122}\), and that this requires \(D_{\rm inf}\sim e^{-3N_{\rm tot}}\sim10^{-122}\), giving \(N_{\rm tot}\approx 122\ln 10/3\approx 94\).[paper]  
- Earlier in Sec. II C 1 the text states: “Matching \(\rho_\Lambda \approx (2.3\,{\rm meV})^4\) requires \(N_{\rm tot}\approx 92\)” and then repeatedly treats “\(N_{\rm tot}\approx 92\)” as the operative value throughout the paper (abstract, Sec. I.A.2, Sec. XII A, Sec. XIV D).[paper]  
- The “fine‑tuning reduction from \(10^{122}\) to \(\sim10^5\)” is claimed to follow from sensitivity to \(\Delta N_{\rm tot}\approx 4\).[paper] In fact, if \(N_{\rm tot}\sim 92\) corresponds to \(D_{\rm inf}\sim 10^{-121}\)–\(10^{-122}\), then changing \(N_{\rm tot}\) by 4 e‑folds changes \(D_{\rm inf}\) by \(e^{-12}\approx 6\times10^{-6}\), i.e. roughly 5–6 orders of magnitude, not by a factor of \(10^{117}\). The “reduction” is purely notational, but the numbers as written invite a quantitative reading that is not arithmetically justified.

Required fix:  
- Pick a single, consistently derived value of \(N_{\rm tot}\) from the chosen hierarchy and use it everywhere (or present an explicit formula and a numeric example), clearly labelling it as order‑of‑magnitude.  
- Recompute the effect of a ±4 e‑fold change in \(N_{\rm tot}\) on \(D_{\rm inf}\) explicitly and correct or remove the “\(10^{122}\) to \(10^5\)” language; explain that the hierarchy is simply being reparameterized, not reduced.  
- Ensure that all mentions of 92 vs 94 e‑folds and “∆N ≈ 4 → 10^5” are numerically consistent with Eq. (11) and Appendix B, or clearly reclassify them as purely illustrative.


P1A-E8 (ESSENTIAL)  
Class: C (Dimensional consistency)  
Section: Sec. II A 2 (Eq. (6), (7)), Appendix B Eq. (B2), Fig. 2 caption  

Problem: The paper uses two incompatible dimensional assignments for the same parity‑odd operator and its coefficient, and treats them interchangeably in numerical arguments.

- Eq. (6) and Appendix B Eq. (B1) state that the operator has mass dimension \([{\cal L}_{\rm odd}]=+1\), implying \([\alpha/M]=-1\), and explicitly admit this is not a dimension‑4 EFT operator.[paper]  
- Appendix B then introduces  
  \(\rho_\Lambda^{\rm bounce}\sim(\alpha/M)M_{\rm Pl}^5\sim 10^{-2}M_{\rm Pl}^4\) (Eq. (B2)), which internally requires \((\alpha/M)M_{\rm Pl}\sim 10^{-2}\).[paper]  
- However, Eq. (7) motivates \((\alpha/M)M_{\rm Pl}\sim10^{-2}\) via a one‑loop formula that has no explicit \(M_{\rm Pl}^5\) factor and is written as \(\alpha/M \sim g^2\gamma/(32\pi^2 M)\,\ln(\Lambda_{\rm UV}^2/\mu^2)+\delta_{\rm NY}\).[paper] The insertion of \(M_{\rm Pl}^5\) in Eq. (B2) is therefore a second, independent dimensional ansatz, not just a restatement of Eq. (7).  
- Fig. 2 caption states: “the phenomenological scaling ansatz \(\rho_{\rm vac}\sim[(\alpha/M)M_{\rm Pl}] M_{\rm Pl}^4\) is dimensionally correct on‑shell at the bounce”[paper] – this expression actually has dimension 5 unless one assumes \((\alpha/M)\propto M_{\rm Pl}^{-1}\), which contradicts treating \(\alpha/M\) as a fixed “≈10⁻²/M_{\rm Pl}” one‑loop number independent of curvature.

Required fix:  
- Choose one dimensionalization and state it precisely: either (i) work with a bona fide dimension‑4 operator, redefining the coefficient so that \({\cal L}_{\rm odd}\) is dimension‑4 off shell, or (ii) keep the dimension‑1 operator and explicitly restrict all quantitative use of Eq. (B2) and Fig. 2 to a clearly marked toy scaling, dropping all claims that depend on its numerical value.  
- Remove any text that says the scaling is “dimensionally correct” without carefully tracking the implied dependence of \(\alpha/M\) on \(M_{\rm Pl}\); show the unit balance explicitly in one place and keep it consistent.  
- Any effect that uses \(\rho_\Lambda^{\rm bounce}\sim10^{-2}M_{\rm Pl}^4\) (notably the \(N_{\rm tot}\) numerics and the “fine‑tuning reduction”) must either be re‑derived from a dimension‑4 operator or clearly tagged as speculative.


P1A-E9 (ESSENTIAL)  
Class: C (Dimensional consistency)  
Section: Sec. IV B (Eqs. (14)–(15)); Sec. X B–D; Sec. II A 1  

Problem: The dimensional treatment of the Route‑2 one‑loop term and the “perturbation transparency” derivation is incomplete and partly inconsistent.

- Eq. (14) writes \(\Gamma_{\rm one-loop}\sim -(16\pi^2M_{\rm Pl})^{-1}\int d^4x\sqrt{-g}\,\partial_\mu\theta J_5^\mu\) with a factor \(\beta(\gamma)\sim\mathcal{O}(\alpha_{\rm em}/4\pi)\).[paper] This makes the integrand dimension 4 if \(\theta\) is dimensionless, but the text never states the mass dimension of \(\theta\) or of \(J_5^\mu\), and it never checks that this matches the earlier Holst/Nieh–Yan normalization.  
- Eq. (15) then gives a dimensionless ratio  
  \(\Delta\theta_{\rm one-loop}/\Delta\theta_{\rm obs}\sim (\alpha_{\rm em}/4\pi)(H_0/M_{\rm Pl})/[(\alpha/M)\beta_{\rm obs}]\sim10^{-58}-10^{-60}\).[paper]  
  However, the observable on the denominator is \(\beta_{\rm obs}\) (an angle) whereas the numerator uses \(\Delta\theta_{\rm one-loop}\), a different field variable; the mapping from the effective action (Eq. (14)) to a rotation angle in radians is not shown. The paper acknowledges earlier drafts had dimensional mistakes and claims to have “restored \(H_0/M_{\rm Pl}\)” but still does not provide the missing derivation.  
- In Sec. X B–D, the “proof” that torsion vanishes at all perturbation orders relies on (i) identifying the Holst term evaluated on the Levi‑Civita connection with the Pontryagin density and (ii) asserting that this is always a total derivative, without checking boundary terms in cosmological settings or showing how the dimensionful coefficient behaves when torsion is integrated out.[paper] This sits uncomfortably with the Route‑2 operator in Eq. (14), which implicitly assumes a nontrivial Nieh–Yan pseudoscalar and a dynamical \(\theta\).

Required fix:  
- Give a complete dimensional accounting of Eq. (14): specify \([\theta]\), \([J_5]\), and show explicitly that the integrand has mass dimension 4; then derive the birefringence angle β from this action step by step, including the cosmological time integral and any factors of scale factor or photon energy.  
- Recompute Eq. (15) with at least one explicit numerical step in fixed units (e.g. GeV) showing how the \(10^{-58}\)–\(10^{-60}\) range is obtained; if the mapping from \(\theta\) to β remains schematic, the claimed closure by “≳ 30 orders of magnitude” should be softened to a qualitative statement.  
- Clarify the consistency between the perturbation‑transparency result (“Holst term is a boundary term, no effect”) and the presence of a nontrivial Nieh–Yan pseudoscalar \(\theta\) in Eq. (14). If the latter is beyond the minimal scalar‑matter scope of Sec. X, this must be stated explicitly so that the transparency argument is not over‑generalized.


P1A-E10 (ESSENTIAL)  
Class: F (Abstract faithfulness)  
Section: Abstract (first paragraph and central result sentence) vs. Sec. X; Sec. IX Table II  

Problem: The abstract still overstates the status of the “perturbation-transparency theorem” and the four‑route “closure” relative to what is actually proven in the body.

- The abstract calls the central result “a perturbation-transparency theorem: for canonical scalar matter, torsion vanishes at all perturbation orders … and the Holst sector therefore decouples from all scalar/tensor perturbation equations of motion (Sec. X).”[paper]  
- Sec. X, however, provides only a schematic argument: five bullet‑point steps, no explicit expansion of the action to second or higher order, no variation including possible boundary contributions, and no check for subtleties such as nontrivial topology, horizon‑scale boundaries, or quantum anomalies; Eq. (23) just restates the definition of the Pontryagin density as a total derivative.[paper]  
- Table II and Sec. IX promote “Barrier 14: Perturbation transparency” as a mechanism‑class closure that then feeds other barriers (e.g. B8), but there is no quantitative perturbation calculation anywhere in the paper to justify treating this as a theorem rather than a conjecture.

Required fix:  
- In the abstract and in Sec. I and Sec. XV, downgrade the language from “theorem” and “establishes” to “we argue” or “we conjecture” unless you provide an explicit perturbative calculation (e.g. action expanded to second order in perturbations, with torsion integrated out, and demonstration that variations vanish).  
- In Sec. X, either add a concrete calculation at least to quadratic order with fully explicit steps, or clearly state that the argument is heuristic and limited to homogeneous FRW with canonical scalars under standard boundary conditions.  
- Adjust Table II and any discussion that treats B14 as a rigorous no‑go so that its status matches the actual derivation presented.


P1A-M6 (MAJOR)  
Class: A (Arithmetic)  
Section: Sec. VII and footnote 1; Table I; Abstract and Introduction references to “3–5σ realistic” SPHEREx detection  

Problem: σ‑levels and ratios for the fNL forecast are loosely used and not consistently recomputed from the stated inputs.

- Footnote 1: starting from σ(fNL) ≈ 0.7, the text says |fNL|/σ ≈ 6.25σ “degraded to ~5–5.5σ optimistic after template-overlap correction r ≈ 0.84.”[paper] But multiplying 6.25 by 0.84 gives 5.25, not a range, and the further degradation to σ≈1.0 is not shown numerically.  
- The same footnote then states “σ(fNL) ≈ 1.0 after GR‑projection and photo‑z marginalization (3–5σ realistic),”[paper] but |fNL|/σ ≈ 4.375 for σ=1; the lower end of 3σ is not supported by the stated σ unless additional degradations beyond σ≈1 are assumed.  
- Table I and the abstract refer to “3–5σ realistic” detections without a self‑contained recomputation based on Heinrich et al.’s σ(fNL).[paper]

Required fix:  
- Present a small, explicit calculation that starts from Heinrich et al.’s σ(fNL), applies the template overlap r, and then applies quantified degradations for GR projection and photo‑z, showing the resulting σ(fNL) and the corresponding |fNL|/σ; constrain the quoted σ‑range accordingly.  
- Make clear that all these numbers are imported from the unpublished forecast (Paper II) and are not independently recomputed here; avoid mixing hand‑waving σ‑ranges with precise |fNL|/σ ratios in the same paragraph.


P1A-M7 (MAJOR)  
Class: F (Abstract faithfulness)  
Section: Abstract sentence “Galaxy spin asymmetry: a confirmed null,” vs. Sec. III B, V, VI  

Problem: The abstract and Sec. III B still present the galaxy‑spin result as “a confirmed null” without supplying any quantitative evidence in the current manuscript.

- The abstract and Sec. III B both state that an independent ViT‑Small classifier “returns a null all-sky dipole and refutes Shamir’s claimed 3% asymmetry at high significance,” and that “The minimal ECH framework underpredicts A0 by >100 orders of magnitude, consistent with this observed null.”[paper]  
- No values of A0, errors, sample sizes, or test statistics are given anywhere in this paper. All details are deferred to Paper IV, which is “in preparation” and not available.  

Required fix:  
- Either include at least one quantitative summary (e.g. A0 ± σ(A0), number of galaxies, p‑value for Shamir‑like asymmetry) in a small table or paragraph so that the “confirmed null” statement stands on its own, or weaken the wording to “consistent with an unpublished analysis that finds a null” and remove “confirmed” and “refutes … at high significance.”  
- In the abstract, the phrase “Galaxy spin asymmetry: a confirmed null” should be revised unless the body actually supports that with numbers.


P1A-M8 (MAJOR)  
Class: E (Null procedure comparability)  
Section: Abstract; Sec. III A; Sec. VI; Table IV  

Problem: Different β measurements and a constructed benchmark are juxtaposed as if they were directly comparable without always emphasizing the differing null procedures and systematics.

- The abstract and Sec. III A list βobs = 0.342° ± 0.094° (WMAP+Planck) and β = 0.215° ± 0.074° (ACT DR6), then state that β ≈ 0.27° is a “benchmark consistency point” lying “inside the WMAP+Planck 1σ band … and comparable to the independent ACT DR6 follow-up.”[paper] Table IV lists “β = 0.27° (midpoint)” as if it were a parameter.[paper]  
- While the text now clarifies in places that 0.27° is a benchmark, in several locations it is treated on equal footing with observed β’s when discussing ALP fits and LiteBIRD forecasts (e.g. Sec. XIII, XV), without explicit reminders that (i) the two experiments have different pipelines and null tests, and (ii) 0.27° is neither a fit nor a measurement.

Required fix:  
- In every place where β ≈ 0.27° appears alongside βobs and the ACT DR6 value, explicitly label it as “constructed benchmark (simple midpoint of published central values)” and note that different experiments’ β’s are derived from different likelihoods and systematics, so their significances and central values are not strictly directly comparable.  
- In Table IV, move β = 0.27° out of the “parameter summary” or clearly tag it as a user‑chosen benchmark rather than a derived or fitted value.  
- In discussions of LiteBIRD discriminating power (Sec. XIII, XV), clearly distinguish the statistical test against β = 0 versus any test comparing 0.27° vs 0.342°, and emphasise that these correspond to different null hypotheses and different combinations of data.


P1A-M9 (MAJOR)  
Class: J (Stale numbers)  
Section: Sec. G (Discrimination Among Bouncing Cosmologies) and Sec. XIV D vs. Sec. XIII & Table III  

Problem: PTA spectral index values and their σ‑distance are presented with inconsistent numbers.

- Sec. G states: “NANOGrav model comparison: γ = 2.567 ± 0.382 from real-KDE re-analysis of the 15-yr free-spectrum data … The matter-bounce prediction γ = 3.0 sits at +1.13σ above the posterior mean.”[paper]  
- Table III lists “γPTA = 2.567 ± 0.382 (real-KDE GPU MCMC), Bounce γ = 3.0 at +1.1” (no σ explicitly marked, but clearly a rounded version).[paper]  
- Later text refers to this as “+1.13σ” in one place and “+1.1σ” in another, suggesting that not all instances were updated when the posterior mean and σ changed between drafts.

Required fix:  
- Recompute the exact σ‑offset once ( (3.0–2.567)/0.382 ≈ 1.13 ) and use a single rounded value consistently everywhere (e.g. “1.1σ” or “1.13σ”), explicitly labelling it as approximate.  
- Check all other reused numbers from the PTA analysis (γ, σγ) to ensure they match across Sec. G, Sec. XIII, and Table III; update any lingering earlier values.


P1A-N4 (NIT)  
Class: D (Internal cross‑references)  
Section: Sec. II B, references to “Sec. II C”; Sec. IX, Table II; Sec. XIV D  

Problem: Some cross‑references are vague or slightly misleading.

- Sec. II B says “the 0.27–0.41 ρPl window used elsewhere in this paper should be read as a scheme-dependent range rather than as a published LQC range.”[paper] But later, Barrier 12 (Eq. (20)) writes “using the LQG-bounce critical-density window ρcrit/ρPl ≃ 0.27–0.41 from the Ashtekar–Singh effective-LQC status report,”[paper] which contradicts the earlier caveat and could mislead readers into thinking the entire 0.27–0.41 range is a published result.  
- Table II lists “Barrier 12: Vacuum Amplification Ceiling” as closing a mechanism class, and the text of Sec. IX M says it gives only a global ceiling, not a direct PTA exclusion,[paper] but later discussions in Sec. XII and XIV occasionally read as if there were already a quantitative comparison to NANOGrav.

Required fix:  
- Adjust the text near Eq. (20) to repeat the caveat from Sec. II B: clearly state that 0.41ρPl is from Ashtekar & Singh and 0.27ρPl is the author’s extrapolation; do not attribute the full “0.27–0.41” window to the reference.  
- Where Barrier 12 is cited later, explicitly remind the reader that it is only a global energy‑density ceiling and not a quantitative PTA exclusion.


If you integrate these corrections, most of the remaining issues are in the direction of over‑interpretation (too strong language for heuristic constructions) and inconsistent bookkeeping (same quantities used with slightly different numerical or dimensional conventions). The core scientific content would be clearer and more defensible if all such points were either tightened with explicit calculations or explicitly downgraded to plausible but schematic arguments.