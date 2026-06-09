# P1A auto-2026-06-09_1042pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (18689 chars)
**Wall time**: 116.7s

---

P1A-E1  
Section: Abstract, p.1  
Problem: The abstract cites “a companion work in preparation [2]” for a “detailed multi-tracer SPHEREx Fisher forecast” and “companion works in preparation [2, 6]” for key observational components (SPHEREx forecast; ΛCDM+ΔNeff MCMC; NaMaster validation; ALP fits). None of [2] or [6] exist on arXiv, in ADS, or in any journal; they are internal, unpublished manuscripts. They are used as if they were citable literature rather than clearly labeled as private communications or internal notes.  
Required fix: Explicitly relabel [2] and [6] throughout as “companion paper, in preparation (unpublished)” and remove them from the numbered bibliography used for external results. Only use them to describe work that is not needed to verify the claims of this paper. Any quantitative claim in the present manuscript that materially relies on [2] or [6] (e.g., σ(fNL) ≈ 0.7, β forecasts, MCMC-derived cosmological parameters) must either be (i) documented and derivable within this paper or (ii) supported by already-published, citable work. Otherwise, downgrade such statements to clearly labeled expectations, not results.

P1A-E2  
Section: Abstract, p.1  
Problem: “spectator-ALP birefringence β ≈ 0.27◦ is a benchmark consistency point… sits inside the WMAP+Planck 1σ band βobs = 0.342◦ ± 0.094◦… and is comparable to the independent ACT DR6 follow-up β = 0.215◦ ± 0.074◦.” The ACT DR6 paper [5] is cited as “arXiv:2509.13654,” which does not exist. The year “2025” for a DR6 birefringence arXiv posting and the angle/uncertainties are therefore unverifiable. No ACT DR6 cosmological birefringence measurement with those parameters is currently findable on arXiv or in ADS.  
Required fix: Correct [5] to a real, published or at least posted reference if it exists, with accurate arXiv ID, title, authors, and numerical values; otherwise remove [5] entirely and remove/soften all sentences that quote or rely on this ACT DR6 result. The birefringence discussion must be based only on established measurements (e.g. Minami & Komatsu; Eskilt & Komatsu) whose values can be traced to the cited papers’ abstracts or tables.

P1A-E3  
Section: References [5], p.22–23  
Problem: Reference [5] is listed as “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” There is currently no such arXiv identifier and no such paper in ADS; the citation is forward-dated and non-existent.  
Required fix: Replace [5] with an existing, correctly formatted reference (correct arXiv ID, year, journal) if/when ACT DR6 birefringence results are actually posted, or remove [5] entirely. PRD cannot publish a paper that cites nonexistent future work as if it were real.

P1A-E4  
Section: Section I (Introduction) and Table IV (parameter summary), pp.3 and 22  
Problem: The paper uses cosmological parameters (e.g. “H0 = 67.68 ± 1.06 km/s/Mpc, ΔNeff ≈ 0,” σ8, Ωm) and claims they are “drawn from the companion internal MCMC analysis (Paper I(b) [6], in preparation)” with no external citation. These parameters are then used as if they were verified constraints. The “Planck prior level” language implies but does not actually cite Planck 2018 for the specific numbers, and they do not match the Planck 2018 best-fit values exactly. There is no way to verify these numbers from the cited literature, only from an unpublished companion.  
Required fix: Either (a) remove explicit numerical values sourced solely from unpublished companion work and instead quote standard published values with proper citations (e.g. Planck 2018), or (b) include enough methodological description and data references in this paper so the stated numbers can be independently replicated without access to [6]. Make clear that any internal-chain numbers are illustrative and not independent constraints unless they can be reproduced from cited public data and codes.

P1A-E5  
Section: Section II.A.1, Eq. (1), p.5  
Problem: The Einstein–Cartan–Holst action is written as  
\(S_{\rm ECH} = \frac{1}{16\pi G}\int d^4x\, e (e^\mu_a e^\nu_b R^{ab}_{\mu\nu} + \frac{1}{\gamma}\epsilon^{abcd} e^ \mu_a e^\nu_b R_{cd\mu\nu}) + \frac14 T^{abc} T_{abc} + S_{\rm matter}\).  
The dimensions and normalization of the torsion term “\( \frac14 T^{abc} T_{abc} \)” are not consistent: there is no explicit factor of \(1/16\pi G\) (or \(1/2\kappa\)) in front, which would be required for dimensional consistency with the Einstein–Hilbert term; as written, that torsion term has the wrong mass dimension relative to the rest of the action. In standard Einstein–Cartan theory the torsion-squared piece shares the same overall \(1/16\pi G\) prefactor as the curvature terms.[3]  
Required fix: Correct Eq. (1) to include the proper gravitational coupling in front of the torsion-squared term or rewrite the action in a standard form (e.g. purely first-order with independent connection, with torsion eliminated later). Check all subsequent uses of Eq. (1), including the derivation of Eq. (3) and the four-fermion term Eq. (4), and fix any coefficients that were implicitly based on the incorrect normalization.

P1A-E6  
Section: II.A.2, Eq. (4), p.5–6  
Problem: The axial–axial four-fermion term is written as  
\( \mathcal{L}_{\rm int} = -\frac{3\pi G}{2} \frac{\gamma^2}{\gamma^2+1} J^\mu_5 J_{5\mu}\).  
Checking against Hehl & Datta  and standard Einstein–Cartan calculations shows the usual coefficient is \( -\frac{3}{16}\kappa \frac{\gamma^2}{\gamma^2+1} J^\mu_5 J_{5\mu} = -\frac{3\pi G}{2} \frac{\gamma^2}{\gamma^2+1}J^\mu_5 J_{5\mu}\) only if specific conventions are used. However, the authors later treat this term as “parity-even NJL contact” and base quantitative amplitude arguments (Route 1 closure) on ρ ~ κ n^2. They never show a traceable derivation from a cited equation in [12,24]; the coefficient as used is plausibly correct but is not explicitly checked against the cited sources, and the subsequent density estimates are not recomputed from it.  
Required fix: In the main text or an appendix, derive Eq. (4) explicitly from the action of Eq. (1), showing each step and matching the final coefficient and sign to Hehl–Datta (or another definitive reference). Then recompute the bound on ρ_NJL in Route 1 using that coefficient and the quoted fermion densities, and show the numerical amplitude (e.g. “≤ 10⁻x ρ_Λ”). This is needed for PRD-level verifiability of the claimed Planck suppression.

P1A-E7  
Section: II.A.2, Eqs. (5–7), p.5–6; Appendix B, pp.21–22  
Problem: The parity-odd operator is written as  
\(S_{\rm eff} = \frac{\alpha}{M}\int e^I\wedge e^J\wedge F_{IJ}\) (Eq. 5) and in components Eq. (6); Appendix B states explicitly that this has off-shell mass dimension +1, not +4. The paper then “identifies” \(ρ_\Lambda = Ξ M_{\rm Pl}^4\) with \(Ξ \sim (\alpha/M M_{\rm Pl})\) via an on-shell scaling ansatz. While the authors admit this is an ansatz, they still feed these quantities into quantitative expressions, including Table I (“phenomenological scaling ansatz ρ_vac ~ [(α/M) M_Pl]^4 M_Pl^4”), Fig. 2, and the N_tot ≈ 92 fine-tuning claim. This uses a dimensionally inconsistent operator as the starting point for semi-quantitative claims.  
Required fix: Either (a) construct a genuinely dimension-four parity-odd operator with explicit mass scales in the coefficient (e.g. \(\alpha M_{\rm Pl}^3/M\) or similar) such that the effective vacuum energy mapping is based on a well-defined EFT, and redo all scaling arguments accordingly, or (b) clearly move all formulas that use this “scaling ansatz” (including the ρ_bounce and N_tot ~ 92 numbers, Fig. 2, Fig. 5, and related text) into a speculative subsection labeled as dimensional speculation, and remove their use as supporting quantitative evidence in the abstract, conclusions, and Section XII. At PRD level, a dimensionally inconsistent operator cannot underpin quantitative claims about the fine-tuning hierarchy.

P1A-E8  
Section: II.C.1, Eq. (11) and discussion, p.7–8; Section XII.A, p.18–19  
Problem: The “inflationary suppression factor” D_inf is given as  
\(D_{\rm inf} = e^{-3N_{\rm tot}} (T_{\rm reh}/M_{\rm GUT})^{3/2}\) and used to claim that the CC hierarchy is “reparametrized” from 10¹²² to 10⁵ via N_tot ≈ 92. However:  
– The exponent 3/2 is admitted to be “dimensional-analysis aesthetic” and not derived from an actual phase-space integral or cited calculation.  
– The required D_inf ≈ 10⁻¹²¹ is used to argue N_tot ≈ 92 based on the dimensional ansatz of Appendix B, not on any ECH-specific dynamics.  
– No numerical recomputation is presented; the CMB/BBN constraints on T_reh and M_GUT are not cited.  
This is a strong, load-bearing claim (inflationary dilution as bookkeeping for CC fine tuning) not backed by verifiable calculations or literature.  
Required fix: Either (i) provide an explicit derivation (or a clear reference that performs it) for the (T_reh/M_GUT)^{3/2} factor and for the mapping from bounce-scale density to ρ_Λ, including a full numerical calculation of D_inf and N_tot within error bars, or (ii) clearly demote the “N_tot ≈ 92” statement to a purely illustrative example, removing any language that suggests a real reduction of the CC hierarchy, and excise related quantitative claims from the abstract, conclusions, and Section XIV.D. PRD cannot accept heuristic dimensional numerology as a quantitative result.

P1A-E9  
Section: III.A & IV.D, Eq. (17), pp.8, 10–11  
Problem: The expression for birefringence,  
\(β \simeq \frac{α}{M} Δθ ∼ \frac{α}{M} \sqrt{2ρ_θ}/m_θ\), is written as \(β ≈ (α/M) 2 ρ_θ / m_θ^2\) (Eq. 17) with dimensional inconsistencies (angles dimensionless, ρ_θ ∼ E⁴, m_θ ∼ E). With α/M ∼ 10⁻²¹ GeV⁻¹, the mapping to ρ_θ ≈ ρ_Λ is claimed, but no explicit, dimensionally consistent derivation is given, nor is a reference (e.g. Lue, Wang & Kamionkowski ) quoted with the exact formula. The quoted numeric coincidence “ρ_θ ≈ 2.8×10⁻¹¹ eV⁴ ≈ ρ_Λ” cannot be traced to a specific equation in the literature because the paper does not show the intermediate steps.  
Required fix: Write down the birefringence angle β for an ALP–photon coupling starting from \(L ⊃ -(1/4) g_{aγ} a F \tilde F\), show the exact expression for β in terms of g_{aγ}, ρ_θ, and m_θ, and match α/M to g_{aγ} with fully explicit dimension and unit checks. Then recompute numerically ρ_θ for α/M = 10⁻²¹ GeV⁻¹, β = 0.342° and m_θ = H₀, and show the resulting value in eV⁴; verify that it agrees with ρ_Λ within stated uncertainties. If it does not, correct the text. If it does, provide the full derivation so readers can trace the result to standard ALP birefringence formulas.

P1A-E10  
Section: IX, Table II and surrounding text, pp.13–15  
Problem: The “14 mechanism-class constraints” are partly described as known results (scale separation, attractor-sensitivity, parameter immunity, Liouville conservation), but the citations are absent or vague. For instance, “Liouville conservation” is asserted as closing a vacuum-selection class, but no explicit reference, equation, or proof is provided, and the claim is not traced to a specific prior work. PRD requires that each load-bearing “no-go” statement either be proved in the paper or attributed precisely to an existing theorem with clear citation.  
Required fix: For each Barrier (1–14), either (a) provide an explicit derivation in the text (or appendix) showing why the claimed mechanism is excluded under the stated assumptions, with equations and quantitative bounds where applicable, or (b) clearly cite the original literature where the barrier was derived, including section or equation numbers. In particular, barriers framed as “known” (Liouville conservation, attractor-sensitivity, parameter immunity, scale separation) must be accompanied by verifiable proofs or references.

P1A-E11  
Section: X (Perturbation-transparency proof), Eqs. (23), (21–22), p.15–16  
Problem: The proof that the Holst term’s dual contraction vanishes identically for torsionless connections relies on “e^I∧e^J∧R_{IJ} = −NY + T^I∧T_I” and the statement that both Nieh–Yan and torsion-squared vanish at T=0. This is conceptually right but no explicit reference is given for the exact algebraic identity, and equation (23) is written as  
“R̃(Γ̊) = ½ ε^{μνρσ} R_{μνρσ}(Γ̊) = 0 (identically, by the first Bianchi identity)”  
without careful index symmetries or cross-check against Holst  or subsequent Einstein–Cartan–Holst analyses.[6][4] Given the centrality of this “perturbation-transparency theorem,” the argument is too schematic for PRD.  
Required fix: Expand the proof: start from the Holst term in differential-form notation, write out explicitly its expression in coordinate indices, and show the contraction with ε^{μνρσ} and the Riemann tensor vanishes using R_{μ[νρσ]} = 0. Provide a precise citation (e.g. Holst 1996, Freidel–Minic–Takeuchi, or Shapiro–Teixeira) where this identity is established. Confirm that no surface terms survive in an FRW or perturbed FRW spacetime. The proof should be detailed enough that a reader can reproduce it step-by-step.

P1A-E12  
Section: Figures 2, 5, 6; Table I, pp.4, 5, 13, 18  
Problem: Multiple figures and Table I show quantitative or semi-quantitative results that depend on the speculative dimensional ansatz and on unpublished companion forecasts:  
– Fig. 2 uses the phenomenological scaling ansatz to plot an “energy density hierarchy.”  
– Fig. 5 shows a “naturalness landscape” based on “(mass×coupling) plane required to source ρ_Λ” that depends on the same ansatz and on approximate estimates for each route’s amplitude.  
– Fig. 6 and Table I quote SPHEREx σ(fNL) ≈ 0.7 and “3–5σ realistic” detection claims that depend on [2] (in preparation).  
These are presented visually as if they summarize established quantitative results. None of the underlying calculations are performed in this paper or traceable to published literature; the axes are dimensionful but not always labeled with units; and the central numbers are not recomputed from input parameters in the text.  
Required fix: For each figure and Table I:  
• Ensure axes have units and clear definitions.  
• Explicitly identify in the caption whether the plot is schematic or based on a concrete numerical calculation.  
• If based on [2] or other unpublished work, either (a) reproduce the relevant calculations briefly in this paper (e.g. one-line Fisher formula with numbers) or (b) clearly label the panels as “conceptual forecast based on companion work in preparation,” and remove any quantitative claims from the main text that rely solely on those forecasts. For PRD, the paper’s conclusions must not depend on non-reproducible figures.

P1A-E13  
Section: Bibliography overall, pp.22–23  
Problem: The paper contains multiple “in preparation” references that are treated as citable sources: [2], [6], , , . While such references may be allowed as notes (“companion work in preparation”), PRD will not accept them as the primary basis for any key numerical result, forecast, or claim. In addition,  is a “companion technical note, available upon request from the author” and is not posted anywhere accessible via arXiv or ADS. That is incompatible with reproducibility.  
Required fix:  
– Reclassify all “in preparation / available on request” works as private communications or internal notes and ensure that none of the main conclusions rely on them in a way that cannot be independently checked.  
– Wherever possible, replace reliance on these with published literature; if that is not possible, the corresponding result should be downgraded to a conjecture or “work in progress,” not a part of the main result.  
– For , either post it publicly (e.g. arXiv) and provide a real identifier or remove it from the bibliography.

P1A-M1  
Section: Abstract, p.1  
Problem: The abstract states “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9,10].” While DESI 2024 preprints do report tensions with ΛCDM, the exact range “3.1–4.2σ” and the combination of datasets used to obtain that range are not spelled out or recomputed in this paper. There is no demonstration that the numbers in the abstract match those in [9,10]; no table reproduces them.  
Required fix: Verify from DESI papers [9,10] the precise σ-values and dataset combinations that yield 3.1 and 4.2σ; quote those combinations explicitly (e.g. “BAO+Planck yields Xσ in w0–wa plane”) and ensure the numbers match the literature. If they do not, update the abstract to the correct range; if DESI’s reported significance is more nuanced (e.g. depends sensitively on priors), describe that nuance qualitatively instead of compressing it into a single range.

P1A-M2  
Section: III.B, V, VI, VIII (galaxy spin), pp.8, 12–13, 18  
Problem: The paper’s claims about galaxy spin asymmetry (“null at the dipole level,” “Shamir’s 3% claim is refuted,” “>100 orders of magnitude underprediction”) rely entirely on Paper IV , which is “in preparation.” No details of the classifier, sample, selection, or test statistics are provided here, and thus no reader can verify that the null result is indeed robust or how it compares numerically to Shamir [32,33] or Patel & Desmond .  
Required fix: Either (a) include a minimal but sufficient summary of the galaxy spin analysis in this paper—sample size, classifier accuracy, main test statistic, and p-values—so that the “confirmed null” and “refutes 3% asymmetry” statements can be checked, or (b) weaken these claims to “preliminary results (Paper IV, in preparation) indicate a null,” and remove them from the main conclusions. For PRD, making strong statements about refuting a published claim requires enough detail to be independently scrutinized.

P1A-M3  
Section: VII (Falsification criteria), XIII, XIV.C–D, p.12, 18–20  
Problem: The SPHEREx fNL forecast and LiteBIRD σ(β) forecast are quoted with fairly specific σ values (σ(fNL) ≈ 0.7, degraded to ≈1.0; σ(β) ≈ 0.03°) and interpreted as “3–5σ realistic” or “∼9σ” detection prospects. Some of these numbers come from Heinrich et al. 2024 , which is fine, but others are described as “companion Paper II [2]” and “Paper I(b) [6].” There is no recomputation in this paper connecting survey specs to σ(fNL) and σ(β).  
Required fix: For each forecast:  
– Confirm which numbers come from published literature (e.g. , ) and cite them directly.  
– If additional degradation factors or multi-tracer improvements are claimed from [2,6], either present the corresponding Fisher-matrix calculations briefly in this paper or clearly mark those numbers as preliminary and not central to the conclusions. Where possible, replace “3–5σ realistic” with “of order a few σ, given current forecasts” unless a full analysis is shown.

P1A-M4  
Section: Throughout, references to “PTA γ = 2.567 ± 0.382 (real-KDE GPU MCMC)” and “γ = 3.0 at +1.13σ,” especially Table III and Section X.G, p.17–18  
Problem: These parameter values for the PTA spectral index γ and their uncertainties are attributed to “companion Paper III ,” which is in preparation. No PTA data or likelihood are described here, and no existing NANOGrav or PTA publication can be traced with those specific posterior means. The numerical values and the “+1.13σ” figure relative to some “bounce γ = 3.0” are therefore non-verifiable.  
Required fix: Either (a) remove the quantitative PTA constraints from this paper and restrict the discussion to qualitative statements (“current PTA data appear broadly consistent with γ ~ 3”), citing published NANOGrav papers directly, or (b) provide enough information in this paper (or a public preprint for ) such that the quoted posterior can be reproduced. At PRD level, untraceable fit numbers from non-public analyses are not acceptable as quantitative evidence.

P1A-M5  
Section: Body text and footnotes, multiple pages (e.g. X footnote, XIV.D)  
Problem: The manuscript repeatedly references “earlier drafts erroneously identified X,” “correction preserves the headline conclusion,” internal run IDs (“Paper I(b) Table IV row ‘DESI DR2 w0wa (new)’”), and detailed MCMC run statuses (“chain has accumulated ∼3.8×10⁴ accepted samples… R̂−1≈3×10⁻²”). These are remnants of internal version history and project bookkeeping, not appropriate content for a PRD article.  
Required fix: Remove or drastically compress all version-history narrative, internal run status reports, and references to specific internal table rows in companion drafts. Replace them with standard, timeless descriptions (e.g. “We performed preliminary w0–wa MCMC runs that have not yet reached convergence; hence, no quantitative constraints are quoted here.”). PRD papers must read as completed, self-contained works, not as a live lab notebook.

P1A-N1  
Section: Footnote “a” under abstract, p.1–2  
Problem: The long footnote explains a previous confusion between the Holst dual contraction and the Pontryagin density, and contains a discursive historical correction. While conceptually relevant, its phrasing (“Earlier versions of this manuscript erroneously identified the two…”) is version-history prose rather than scientific content.  
Required fix: Recast the text into a concise scientific remark within the main body (e.g. in Sec. X), simply stating the correct identity and citing the literature. Eliminate references to “earlier versions of this manuscript.”

P1A-N2  
Section: Internal references like “this volume,” “companion paper,” throughout  
Problem: References such as “[2] … companion paper, this volume,” “Paper IV, this volume” assume simultaneous publication of multiple related papers. That may not hold, and readers cannot rely on unpublished work to interpret the present paper.  
Required fix: Rephrase all such occurrences to avoid “this volume” assumptions. Either treat them as standard “in preparation” notes or wait until the companion papers are actually accepted and then cite them with proper journal references; otherwise, minimize dependence on them.

P1A-N3  
Section: Table IV, parameter description line for γ (“scheme range ~ 0.020”), p.22  
Problem: The “scheme range ∼0.020” for the Barbero–Immirzi parameter is described as an “effective range only and not propagated as a statistical error.” This is fine, but the references [16–18] are not explicitly checked numerically in the paper. The cited values (0.127 for U(1) counting, ~0.274 for SU(2), ~0.2375 for Domagala–Lewandowski–Meissner) do match the literature qualitatively, but the specific “0.020” spread is not explained quantitatively.  
Required fix: Either provide a short explanation in Appendix A or B showing how 0.2375 and 0.274 lead to “∼0.020” as a representative scheme spread, or remove the “∼0.020” number and just state that different counting schemes give γ in the range 0.237–0.274.

P1A-N4  
Section: Entire manuscript length, 23 pages including dense appendices  
Problem: For a paper whose central technical result is essentially a theoretical “no-go” at the channel level (and not an operator-basis theorem) plus high-level synthesis of existing barriers, the manuscript is quite long and includes repeated discussion of the same points (e.g. perturbation transparency, N_tot tension, companion-paper forecasts). Some sections (e.g. repeated discussions of the same birefringence benchmarks, multiple restatements of limitations) appear to be over-explaining rather than presenting new calculations.  
Required fix: Condense the manuscript to ~15–18 pages by:  
– Removing version-history narratives and internal chain-status descriptions.  
– Moving some of the more speculative dimensional scaling discussion (Appendix B, large portions of XII.A) into a shorter, clearly labeled speculative subsection.  
– Removing redundant restatements of the same structural conclusions. This will bring the paper in line with typical PRD standards for conceptual work.

## Summary recommendation

REJECT

The paper attempts a broad, ambitious “channel-level closure” of minimal Einstein–Cartan–Holst dark-energy routes, but the current version falls short of PRD standards in several critical ways. It relies heavily on unpublished companion works for key numerical claims and forecasts; includes at least one clearly non-existent citation (ACT DR6 birefringence, [5]); uses a dimensionally inconsistent parity-odd operator as the basis for quantitative fine-tuning statements; and presents central results (perturbation transparency, inflationary suppression, barrier catalog) with proofs and calculations that are too schematic to be independently verified. Substantial restructuring, removal of speculative numerology from the core claims, elimination of all reliance on non-public analyses, and correction of the citation record would be required. These changes are so extensive that a fresh submission after major revision would be more appropriate than trying to salvage the present manuscript through standard PRD “major revisions.”

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E14  
Section: Sec. II A.2, Eq. (7), p.6; Sec. IV B, Eq. (15), p.9; Appendix B, eqs. (B1–B2), p.21  
Problem (dimensional + arithmetic): The paper mixes three *incompatible* dimensional normalizations for the same parity-odd coefficient α/M and then builds quantitative claims on them.  

- Eq. (7) treats α/M as a *mass⁻¹* coefficient in a one-loop EFT estimate.  
- Appendix B explicitly states the operator in Eq. (6) has mass dimension +1 and that α/M therefore has dimension −1, which is consistent.[B1]  
- But the dark-energy mapping in Eq. (B2) uses ρ_Λ^bounce ∼ (α/M) M_Pl⁵, i.e. assumes *five* powers of M_Pl, not the four required for an energy density, and the text then oscillates between “(α/M) M_Pl³” and “(α/M) M_Pl⁵” language (e.g. “(α/M) M_Pl⁵ ∼ 10⁻² M_Pl⁴”, “[(α/M)M_Pl]⁴ M_Pl⁴” in Fig. 2 caption) without a single consistent dimensional convention. This is dimensionally inconsistent.  

Required fix: Choose a single consistent EFT normalization: either (i) keep the operator dimension-four by defining an explicit dimensionful coefficient (e.g. α M_Pl³/M) and carry that through all subsequent formulas, or (ii) clearly segregate all expressions involving ρ_Λ ∼ [(α/M) M_Pl]⁴ M_Pl⁴, Eq. (B2), Fig. 2, and the N_tot ≈ 92 numerology into a labeled speculative section and *remove them* from any quantitative claims (including abstract, Sec. XII, Sec. XIV.D). As written, the dark-energy mapping rests on mutually inconsistent dimensions and cannot support numerical statements.

---

P1A-E15  
Section: Sec. II A.3 (γ range), Eq. (2) and discussion, p.5; Sec. II B, eqs. (8–9), p.6; Sec. IX, Eq. (20), p.15; Appendix B, paragraph under Eq. (B2), p.21–22  
Problem (arithmetic + internal consistency): The LQC critical density window, the Planck-density hierarchy, and the bounce-to-Λ hierarchy are numerically inconsistent across the paper.  

- Sec. II B says Ashtekar–Singh give ρ_crit ≃ 0.41 ρ_Pl at γ=0.2375 and that substituting γ_SU(2)=0.274 gives ρ_crit ≃ 0.27 ρ_Pl, hence a “0.27–0.41 ρ_Pl” window. Later, Barrier 12 then uses ρ_crit/ρ_Pl ≃ 0.27–0.41 again in Eq. (20). This is fine *only if* Eq. (9)’s explicit formula is actually evaluated and numerically consistent; the derivation uses a non-standard expression with γ³ in the denominator and a specific ∆, but no recalculation is shown and the numbers are simply asserted. Given the sensitivity to γ and ∆, these quoted values need to be checked and documented against the explicit Ashtekar–Singh formulas, not hand-inserted.  

- Appendix B then states the “genuine cosmological-constant hierarchy” is M_Pl⁴ / ρ_Λ ≈ 10¹²² and that the bounce-scale density is ρ_bounce ∼ M_Pl⁴, but earlier in Sec. II C and Fig. 2 the paper effectively uses ρ_bounce^Λ ∼ 10⁻² M_Pl⁴ from Eq. (B2). These two “bounce densities” differ by two orders of magnitude, yet the N_tot ≈ 92/94 calculation is presented as if there is a single unique ratio.  

Required fix: (i) Actually compute ρ_crit(γ) from the Ashtekar–Singh effective LQC expression with the quoted γ values and show the numbers in a table or in Appendix A; if the 0.27 value is not exactly reproduced, quote the *true* computed value and label any extrapolation across counting schemes. (ii) Decide whether the relevant bounce-scale density in the fine-tuning story is ρ_bounce ∼ M_Pl⁴ or ρ_bounce^Λ ∼ 10⁻² M_Pl⁴; recompute D_inf and N_tot consistently from that choice and remove any conflicting sentences that use the other value. As long as the “bounce density” is moving by hand between 10⁰ and 10⁻² M_Pl⁴, the quoted N_tot ≈ 92–94 cannot be considered a controlled result.

---

P1A-E16  
Section: Sec. II C.1, Eq. (11) and surrounding text, p.7–8  
Problem (dimensional consistency + arithmetic): D_inf is written as  
D_inf = exp(−3 N_tot) × (T_reh / M_GUT)^{3/2}.  

- As a pure *dimensionless* factor multiplying ρ_bounce, this is acceptable only if ρ_bounce already has mass dimension 4 and both T_reh and M_GUT are mass scales. However, the derivation paragraph mixes several distinct effects: dilution of a non-propagating torsion field ∝ a⁻³ (giving e^{-3N_tot}) and a “parity-odd density-of-states factor” that is claimed to produce the extra (T_reh / M_GUT)^{3/2}. No explicit integral or phase-space counting is given; the exponent 3/2 is admitted to be aesthetic.  

- The “order-of-magnitude matching” then claims that for T_reh ≈ 10¹⁵ GeV, M_GUT ≈ 10¹⁶ GeV, one finds (T_reh/M_GUT)^{3/2} ≈ 0.03. This is numerically wrong: (10¹⁵/10¹⁶)^{3/2} = 0.1^{1.5} ≈ 0.0316, which is ≈3×10⁻², not 0.03 “to within an order of magnitude” but exactly that value. The point is that the “order-of-magnitude” flavor is being used to gloss that here you *did* do a precise arithmetic evaluation; if you are treating 3/2 as aesthetic, you must also show that varying this exponent within a plausible range (e.g. 1 to 2) does not materially change the N_tot claim.  

Required fix: (i) Either supply an explicit computation of the density-of-states factor for the parity-odd channel that yields the 3/2 exponent, or (ii) replace (T_reh/M_GUT)^{3/2} with a generic (T_reh/M_GUT)^p, state clearly that p is unknown, and then show how N_tot and D_inf change for p in a reasonable range. In either case, remove the present-language suggestion that the 3/2 factor is “matched to first-principles arguments” unless a real derivation is added.

---

P1A-E17  
Section: Sec. II C.1, “Reheating thermal-reset barrier”, p.7–8; Sec. XII.A, “Physical-versus-mathematical scope of D_inf”, p.17–18  
Problem (internal logical inconsistency): Two mutually incompatible stories are told about D_inf and N_tot.  

- The “Reheating thermal-reset barrier” subsection argues that reheating drives the axial current ⟨J_5^μ⟩ to zero and thereby completely erases any bounce-era coherent torsion, independent of N_tot. If accepted, this makes D_inf physically irrelevant; the late-time torsion-sourced contribution to Λ_eff is simply zero after reheating.  

- Sec. XII.A nonetheless continues to treat D_inf and N_tot ≈ 92 as if they encode a meaningful “reparameterization” of the cosmological constant hierarchy, with talk of “reducing 10¹²² to 10⁵” and “sensitivity to ΔN_tot ≈ 4”. This is logically inconsistent with the thermal-reset argument: you cannot both assert that reheating annihilates any coherent torsion *and* use a residual of that torsion to parametrize ρ_Λ.  

Required fix: Choose one consistent physical picture. If reheating truly resets ⟨J_5^μ⟩ and torsion to zero, then D_inf and N_tot cannot be used to parametrize the observed ρ_Λ; the fine-tuning bookkeeping in Sec. XII must be recast as a *hypothetical* exercise (“if reheating did not reset torsion…”) and clearly labeled as counterfactual. Alternatively, if you want to keep D_inf as physically operative, you must explicitly state why the thermal-reset does *not* fully erase the relevant torsion component and compute the residual instead of setting it qualitatively to zero.

---

P1A-E18  
Section: Sec. II A.2, Step 2 and Eq. (4), p.5–6; Sec. IV A, Eq. (13), p.9  
Problem (incomplete derivation + potential coefficient mismatch): The four-fermion contact term is first presented in a γ-dependent form (Eq. (4))  
L_int = − (3πG/2) [γ²/(γ²+1)] J_5^μ J_{5μ}  
and later the NJL term is written as (Eq. (13))  
L_tor^NJL = − (3/16) κ (ψ̄ γ^a γ^5 ψ)², with κ=8πG.  

For large γ, −(3πG/2) ≡ −(3/16) κ numerically, but the text never shows the limiting step or how the γ²/(γ²+1) factor is reconciled. Section IV A claims the Route-1 amplitude bound ρ_NJL ∼ κ n_ψ², but does not use the γ-dependent prefactor nor show how big that prefactor actually is for γ=0.274.  

Required fix: Provide in the main text or an appendix a single, consistent derivation that: (i) starts from the ECH action with Holst term, (ii) integrates out torsion including γ dependence, (iii) derives the explicit coefficient of (ψ̄ γ^a γ^5 ψ)² including the factor γ²/(γ²+1), and (iv) *numerically evaluates* that coefficient for γ=0.274. Then recompute ρ_NJL including this factor and show explicitly the maximum possible contribution at cosmologically relevant n_ψ. Without this, the Route-1 closure mixes two slightly different normalizations and leaves the reader unable to verify the amplitude numerically.

---

P1A-E19  
Section: Sec. II A.2, Eq. (7) and its use, p.6–7; Sec. IV B, Eq. (15), p.9  
Problem (arithmetic and comparability of different “suppression” ratios): The Route-2 closure toggles between two different dimensionless ratios (∼10⁻³³ and ∼10⁻⁵⁸–10⁻⁶⁰) and treats them as equivalent order-of-magnitude results, without ever recomputing the actual observable β.  

- Eq. (15) defines  
Δθ_one-loop / Δθ_obs ∼ [α_em/(4π)] (H₀/M_Pl) / [(α/M) β_obs].  
Plugging in α_em/(4π)≈5.8×10⁻⁴, H₀/M_Pl≈10⁻⁶¹, α/M≈10⁻²¹ GeV⁻¹, M_Pl≈10¹⁹ GeV, β_obs≈6×10⁻³ rad gives  
M_Pl·(α/M)≈10⁻², so the ratio is ∼10⁻³·10⁻⁶¹ / (10⁻²·6×10⁻³) ≈ 10⁻³·10⁻⁶¹ / 6×10⁻⁵ ≈ (10⁻⁶⁴) / 6×10⁻⁵ ≈ 2×10⁻⁶⁰.  
The text quotes “∼10⁻⁵⁸ to 10⁻⁶⁰” but does not show the arithmetic or why an alternative contraction gives ∼10⁻³³; both cannot be “equally valid” if you are claiming a specific suppression factor as part of a no-go.  

Required fix: Explicitly pick one normalization, compute β_one-loop as a function of the loop-induced coefficient and H₀, and then calculate β_one-loop / β_obs numerically. Remove the hand-waving about “another ordering gives 10⁻³³” unless that ordering is physically motivated and shown explicitly. The Route-2 closure should present a single, traceable number (e.g. 10⁻⁶⁰) rather than a ∼27-order-of-magnitude spread in supposed “equivalent” suppressions.

---

P1A-E20  
Section: Sec. IV D, Eq. (17), p.10–11; Sec. XIII (ALP birefringence), p.18; Table IV, β and α/M entries, p.22  
Problem (dimensional inconsistency in β–ρ_θ–m_θ mapping): Eq. (17) states  
β ≃ (α/M) Δθ ∼ (α/M) [2ρ_θ / m_θ²]^{1/2},  
but the text in Sec. IV D then writes β ≈ (α/M) 2ρ_θ/m_θ² and uses that to invert for ρ_θ, obtaining ρ_θ ≈ 2.8×10⁻¹¹ eV⁴ ≈ ρ_Λ.  

- Using L ⊃ −(1/4) g_{aγ} a F \tilde F, the standard homogeneous-ALP birefringence formula is β = (1/2) g_{aγ} Δa, with Δa the change in the background ALP field between recombination and today. If the ALP carries energy density ρ_θ = (1/2) m_θ² a² (ignoring kinetic energy at late times), then a = √(2ρ_θ)/m_θ. Combine these to get β = g_{aγ} √(2ρ_θ)/m_θ, not β ∝ ρ_θ/m_θ². The text’s move from ∼√(ρ_θ) to ∼ρ_θ is dimensionally wrong: ρ_θ has mass⁴, m_θ has mass¹, so √(ρ_θ)/m_θ has mass¹, but β is dimensionless and g_{aγ} ∼ 1/M has mass⁻¹; g_{aγ} √(ρ_θ)/m_θ is dimensionless, while (α/M) ρ_θ/m_θ² has net dimension of mass¹.  

- The numerical coincidence ρ_θ ≈ 2.8×10⁻¹¹ eV⁴ therefore cannot be traced to a correct formula. No explicit derivation is given and no reference is cited at the equation level (e.g. Lue, Wang & Kamionkowski).  

Required fix: Derive β from the standard Chern–Simons coupling. Show step-by-step that for a homogeneous ALP:  
β = (1/2) g_{aγ} Δa, ρ_θ = (1/2) m_θ² a² ⇒ a = √(2ρ_θ)/m_θ,  
then β = g_{aγ} √(2ρ_θ)/m_θ. Map α/M to g_{aγ} with correct units, then invert to obtain ρ_θ for α/M=10⁻²¹ GeV⁻¹, β=0.342° and m_θ=H₀. Present the full arithmetic in eV units. If this does *not* yield ρ_θ ≈ ρ_Λ, correct the claimed coincidence and all downstream statements; if it does, keep the correct square-root dependence and remove the dimensionally inconsistent 2ρ_θ/m_θ² form.

---

P1A-E21  
Section: Table I, row “Testable prediction?”, footnote b, p.4; Sec. VII (Falsification criteria), p.12; Fig. 6 caption and panel, p.18  
Problem (forecast arithmetic + comparability): The SPHEREx detection significance for f_NL is stated inconsistently across the paper and is not recomputed from the quoted σ(f_NL).  

- Table I states “3–5σ realistic after full systematic budget… under Heinrich+2024 σ(f_NL) ≈ 0.7,” and footnote 2 later says the raw ratio is |f_NL|/σ ≈ 6.25σ, “degraded to ∼5–5.5σ optimistic after template overlap,” then to σ(f_NL)≈1.0 after systematics, giving “3–5σ realistic.” However, |f_NL|=4.375 and σ=1.0 gives 4.375σ, not 3–5σ; the quoted range implicitly mixes *different null procedures* (Fisher-ideal, template-overlap-degraded, systematics-degraded) without labels.  

- Sec. VII repeats “3–5σ realistic” while Fig. 6 visually suggests a decisive detection but does not label the exact σ level or which σ(f_NL) scenario is being shown.  

Required fix: Present a small table explicitly listing each σ(f_NL) scenario:  
(i) Fisher-ideal (Heinrich et al.) σ≈0.7 ⇒ 6.25σ;  
(ii) after template-overlap r≈0.84 ⇒ effective σ≈0.7/0.84, etc.;  
(iii) after including GR projection and photo-z, σ≈1.0 ⇒ 4.4σ.  
State clearly which of these you call “optimistic” and which “realistic.” Do *not* compress them into a single “3–5σ realistic” statement without specifying the underlying σ and assumptions; and in Fig. 6 caption, state which σ(f_NL) value is used to draw the forecast band.

---

P1A-E22  
Section: Table IV (Parameter summary), row “γ_PTA”, p.22; Sec. X.G and Table III, p.16–17  
Problem (comparability of σ and σ-based statements from different null procedures): The PTA spectral index γ is quoted as γ=2.567±0.382 “(real-KDE GPU MCMC)” and compared to a “bounce γ=3.0 at +1.13σ,” and Table III treats this as a simple ±σ comparison. But:  

- The γ=2.567±0.382 posterior is said to come from a custom real-KDE likelihood in “companion Paper III,” whereas the “bounce γ=3.0” prediction presumably comes from a *different* theoretical calculation that does not share the same error model or likelihood.  
- The text does not explicitly flag that this σ comparison is not between two measurements with comparable null procedures, but between a data-driven posterior and a theoretical curve, making the “+1.13σ” language potentially misleading.  

Required fix: Replace “γ=3.0 sits at +1.13σ above the posterior mean” with a clearer statement that this is a comparison of a fixed theoretical value with the mean and standard deviation of one *specific* PTA fit under a particular likelihood model. Add an explicit sentence that σ values from this real-KDE analysis are not directly comparable to σ values from NANOGrav’s official likelihood, and that the “1.13σ” is only indicative. This will make the null-procedure mismatch explicit.

---

P1A-E23  
Section: Sec. III A (CMB EB), Eq. (12), p.8; Sec. XIII (ALP birefringence discussion), p.18; Fig. 6 bottom panel, p.18  
Problem (abstract/body consistency + figure vs text): The body text in Sec. III A correctly notes that connecting the parity-odd operator to a specific β requires an explicit photon–torsion coupling “that has not been derived here”; Sec. XIII says the ALP fit and LiteBIRD forecast are in a companion paper and that β≈0.27° is a “consistency check.” However, Fig. 6 bottom panel and its caption present the LiteBIRD forecast as a visually decisive “≳5σ” test, and the abstract mentions a concrete benchmark β≈0.27° “comparable to ACT DR6,” as if those numbers were fully computed in this paper.  

Required fix: In Fig. 6 caption and Sec. XIII, explicitly state that the β forecast curve is taken from external LiteBIRD literature and/or companion Paper I(b) and is *not* independently recomputed here; and that β≈0.27° is a benchmark drawn from a parameter point chosen to fit current WMAP+Planck measurements, not a prediction derived from the ECH action. Also, in the abstract, soften the language so that β≈0.27° is described as an illustrative ALP benchmark consistent with current data, not as a “prediction comparable to ACT DR6” unless ACT DR6 is backed by a real citation (see P1A-E2/E3).

---

P1A-E24  
Section: Sec. XIV.D (Structural tension), p.20  
Problem (internal arithmetic cross-check): The mapping from SPHEREx comoving wavenumbers to bounce-era physical scales is described as  
k_phys^bounce ∼ k_SPHEREx e^{N_tot−N_exit} ∼ e^{32} k_SPHEREx for N_tot∼92,N_exit∼60.  

This is consistent: N_tot−N_exit = 32, e^{32}≈10¹³.9. However, the narrative claims that with N_tot ≳ 60 the matter-bounce f_NL signature is “definitively erased” at SPHEREx scales, even though the actual requirement is that modes that exited during contraction re-enter or are pushed deep inside the horizon; the paper does not present a quantitative calculation of the bispectrum transfer function across this scaling, just the exponent.  

Required fix: Either add a short calculation (or explicit reference) showing that for a given contraction-phase mode with k∼10⁻¹ h/Mpc, pushing it by e^{32} indeed renders the bounce-induced bispectrum negligible at z∼1, or clearly mark the “definitively erased” statement as a qualitative expectation, not a computed result. As written, a strong conclusion is being drawn without the supporting quantitative propagation.

---

P1A-E25  
Section: Abstract, “four enumerated minimal-ECH dark-energy routes”, opening summary and bullet 1 in Sec. I A, p.1–4  
Problem (abstract faithfulness / novelty): The abstract and Sec. I A claim “13 logically-independent mechanism-class constraints,” “14-constraint catalog,” and a “channel-level closure” that “collectively constrain the enumerated channels.” The body presents these as if each barrier is backed either by an explicit derivation or a literature theorem. However, several barriers (e.g. Barrier 5: Scale separation, Barrier 6: Attractor-sensitivity, Barrier 7: Parameter immunity, Barrier 9: Liouville conservation) are described only qualitatively, with no equations, no explicit inequality, and no pinpoint citation to a theorem.  

Your original review already flagged the lack of explicit proofs or references (P1A-E10), but on re-reading the abstract vs. body, the issue is sharper: the abstract’s phrasing could be read as claiming a *rigorous theorem* (“collectively constrain… close… at amplitude-budget granularity”), whereas the body text reveals that a subset of the barriers are philosophical or heuristic.  

Required fix: In the abstract and in Sec. I A, adjust wording to reflect that the 14-barrier set contains a mix of (i) quantitatively derived constraints, (ii) heuristic structural arguments, and (iii) literature-based “known” results for which no full derivation is reproduced. For each barrier in Table II, add a column or footnote indicating which category it falls into, and in the abstract explicitly avoid suggesting that all 14 collectively form a rigorous, theorem-level closure.

---

If you want, I can next walk through a *line-by-line* arithmetic verification of one table (e.g. Table IV) or one figure (e.g. Fig. 2 or Fig. 5), recomputing all stated σ, ratios, and scale hierarchies so you can see exactly where to patch numbers.