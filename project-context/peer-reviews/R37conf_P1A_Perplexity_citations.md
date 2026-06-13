# P1A R37conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.68.pdf` md5=0de277bf pages=28
**Input format**: TEXT + web search + pass-2 self-critique (13047 chars)
**Wall time**: 42.9s

---

I can audit the *internal consistency* of the paper text you provided, but I cannot verify arXiv/ADS metadata against live web search from this environment because the search results supplied are unrelated to the paper and do not include the cited physics references. On the basis of the rendered text alone, the manuscript has multiple **major** internal problems, including self-conflicting numerical claims, unresolved dimensional inconsistencies, and repeated reliance on “companion paper in preparation” for load-bearing results.

- **P1A-E1 — Abstract / Sec. II A 2 / Appendix B (essential)**  
  **Problem:** The abstract says the parity-odd operator has “off-shell mass dimension +1 rather than +4” and that the dark-energy mapping “rests on a phenomenological on-shell scaling ansatz,” while Appendix B says the same operator can be promoted to dimension +4 by inserting extra \(M_{\mathrm{Pl}}^3\) factors. These are not just caveats; they are mutually incompatible as a load-bearing derivation route.  
  **Required fix:** State one consistent operator normalization and one consistent EFT status. If the mapping is only phenomenological, remove any language that presents it as an effective local operator derivation.

- **P1A-E2 — Abstract / Sec. II C / Fig. 3 / Appendix B (essential)**  
  **Problem:** The paper alternates between \(N_{\text{tot}}\approx 92\) and \(N_{\text{tot}}\approx 94\) for the same \(\rho_\Lambda\) dilution target. Appendix B explicitly says the “genuine” \(M_{\mathrm{Pl}}^4/\rho_\Lambda\) hierarchy gives \(N_{\text{tot}}\approx 94\), while the main text repeatedly uses \(N_{\text{tot}}\approx 92\).  
  **Required fix:** Choose the correct benchmark, recompute it once, and propagate the same value everywhere.

- **P1A-E3 — Sec. II A 2, Eq. (7)–(10) (essential)**  
  **Problem:** The paper claims the operator coefficient estimate gives \((\alpha/M)M_{\mathrm{Pl}}\sim 10^{-2}\), but later uses \(\alpha/M\sim 10^{-21}\,\mathrm{GeV}^{-1}\). Those statements can be made consistent only with an explicit and correct conversion between \(M\), \(M_{\mathrm{Pl}}\), \(f_a\), and the paper’s nonstandard normalization. The text currently mixes three conventions without a single unambiguous mapping.  
  **Required fix:** Provide one convention block defining \(M\), \(\alpha\), \(f_a\), and the relation to the quoted numerical coupling; then recompute every downstream estimate from that convention.

- **P1A-E4 — Sec. IV B, Eq. (15) (essential)**  
  **Problem:** The Route-2 ratio is presented first as \(\sim 10^{-60}\), then as an “alternative ordering” giving \(\sim 10^{-33}\). That is a factor of \(10^{27}\) discrepancy for the same physical claim.  
  **Required fix:** Re-derive the ratio carefully and remove the fallback estimate unless it is shown to correspond to a genuinely different observable or normalization.

- **P1A-E5 — Sec. IV D / Sec. XI / Sec. XIV D (essential)**  
  **Problem:** Route 4 is alternately described as closed by amplitude mismatch, then *not* closed by amplitude mismatch but by naturalness, then closed if \(\alpha/M\) is free. This is a shifting argument structure.  
  **Required fix:** State one closure criterion and stick to it. If the route is only excluded under one-loop matching, that conditionality must be explicit in the headline and abstract.

- **P1A-E6 — Abstract / Sec. IV / Sec. XIII (essential)**  
  **Problem:** The abstract says the paper reports “13 logically-independent mechanism-class constraints” and “channel-level closure,” but the body also says the omitted operators are not closed and a full operator-level no-go is deferred. That is a scope drift: the abstract sounds stronger than the body.  
  **Required fix:** Downgrade the abstract to the actual claim: closure of four enumerated routes under stated assumptions, not closure of the full operator basis.

- **P1A-E7 — Abstract / Sec. X / footnotes 7–8 (major)**  
  **Problem:** The abstract states “the Holst dual contraction vanishes identically on the Levi-Civita connection by the first Bianchi identity.” The body then provides a corrected derivation, but the text contains a prior mistaken identification with the Pontryagin density and a note that an earlier version misidentified the two.  
  **Required fix:** Remove residual ambiguity and ensure the main text’s claim is exactly the corrected one, with no leftover inconsistent phrasing in the abstract or captions.

- **P1A-M1 — Sec. II B / Fig. 2 / Appendix B (major)**  
  **Problem:** The figure caption says the ansatz is “dimensionally correct on-shell at the bounce,” while Appendix B says it is *not* a controlled EFT result. “Dimensionally correct on-shell” is not enough to support any quantitative inference from a local action.  
  **Required fix:** Label Fig. 2 as schematic/illustrative only and prevent readers from inferring derivational status.

- **P1A-M2 — Sec. III A / Sec. IV D / Sec. XIII (major)**  
  **Problem:** The birefringence discussion repeatedly claims the benchmark \(\beta\approx 0.27^\circ\) is “inside the 1σ band” of both WMAP+Planck and ACT. That is not correct for the stated central values and uncertainties if one compares to the quoted WMAP+Planck result \(0.342^\circ\pm 0.094^\circ\): the deviation is about \(0.072/0.094\approx0.77\sigma\), not generically “inside the 1σ band” as a model-discrimination statement.  
  **Required fix:** Replace the qualitative “inside 1σ” language with the actual significance calculation and specify which null hypothesis is being tested.

- **P1A-M3 — Sec. VII / Fig. 4 / Sec. XV (major)**  
  **Problem:** The paper simultaneously claims LiteBIRD will detect \( \beta\) at “\(\sim 9\sigma\)” from \(0.27^\circ/0.03^\circ\), but also says it will not separate the benchmark from the current WMAP+Planck central value at high significance. Those are different null hypotheses, but the manuscript does not keep them sharply separated in the narrative.  
  **Required fix:** Explicitly label each significance with its null hypothesis, and avoid juxtaposing them as if they were directly comparable.

- **P1A-M4 — Sec. IX H / Table II / Sec. X N (major)**  
  **Problem:** Barrier 8 and Barrier 14 are said to close the same observable channel and not be logically independent, yet Table II lists 14 entries and the paper repeatedly says “13 logically-independent; B8 subsumed by B14.” This is acceptable only if the catalog is clearly non-independent by construction; currently the prose oscillates between 13 and 14 as if both were primary counts.  
  **Required fix:** Make the independence structure explicit in the table title and in the abstract, and ensure no sentence implies 14 independent constraints.

- **P1A-M5 — Sec. IV A / Sec. IV B / Appendix B (major)**  
  **Problem:** The Route-1 and Route-2 sections repeatedly use “closed by Planck suppression” and “closed by parity-odd coefficient and Planck suppression,” but also concede the operator is parity-even or a boundary term and that the relevant amplitude estimate is only an upper bound. That is not a closure by derivation; it is a scaling argument.  
  **Required fix:** Rephrase as an upper-bound argument, not a derivation, and state the dependence on the ansatz.

- **P1A-M6 — Sec. XI / Table III (major)**  
  **Problem:** Table III mixes theoretical accommodation, posterior preference, and model discrimination in the same “✓/×/—” framework. For example, “Quintom-B can in principle accommodate the DESI w0wa evidence” is not commensurate with the other entries.  
  **Required fix:** Separate “theoretical possibility” from “fitted posterior support” and do not use one symbol system for both.

- **P1A-M7 — Sec. V / References , ,  (major)**  
  **Problem:** The galaxy-spin claims rely on “Paper IV” and named arXiv/preprint references that are not independently verifiable here, while the paper itself says the key catalog, sample size, bias audit, and significances are in a companion paper. That makes the argument non-self-contained.  
  **Required fix:** Either include the essential numerical results in this paper or remove them from the load-bearing argument.

- **P1A-M8 — Data and Code Availability / Appendix A (major)**  
  **Problem:** The paper says a Zenodo DOI “to be inserted at submission,” which is not acceptable for a submitted PRD manuscript if the repository and frozen release are part of the reproducibility claim.  
  **Required fix:** Provide a frozen release identifier, archive hash, or DOI-ready deposit before submission.

- **P1A-M9 — References [2], [6], ,  (major)**  
  **Problem:** Multiple cited works are “companion paper, posted concurrently on arXiv” or “in preparation,” but the current manuscript uses them as evidence for sample sizes, MCMC convergence, and forecast significance. That is a load-bearing citation problem.  
  **Required fix:** Do not cite unpublished internal results as factual support for key claims unless the data and code are part of the current submission and reproducible.

- **P1A-M10 — Eq. (18), Sec. IX A (major)**  
  **Problem:** \(g_{\mathrm{eff}}\sim H_0/M_{\mathrm{Pl}}\sim10^{-61}\) is presented as a scaling ansatz, but then used to infer a fine-tuning measure \(\delta m_T^2/m_T^2\sim 10^{-122}\). The algebraic step is not shown and the dimensional meaning of \(t_3\) is not sufficiently explicit.  
  **Required fix:** Show the derivation or present it as an order-of-magnitude heuristic only.

- **P1A-M11 — Sec. II A 1 / Eq. (1) (minor)**  
  **Problem:** The action notation mixes \(e\,e^\mu_a e^\nu_b R^{ab}_{\mu\nu}\) and tetrad/torsion terms in a way that is easy to misread, and the text says the torsion term is shorthand for an on-shell contact interaction.  
  **Required fix:** Rewrite the action with a cleaner convention block and separate off-shell vs on-shell terms unambiguously.

- **P1A-M12 — Fig. 3 caption / body (major)**  
  **Problem:** The caption says the orange ECH curve uses \(H_0=69.2\), \(\Omega_m=0.310\), and enhanced radiation density, while the body says the reference \(\Lambda\)CDM curve uses \(H_0=67.36\), \(\Omega_m=0.315\) Planck-VI. The figure is therefore not a prediction but a tuned comparison to two different cosmologies.  
  **Required fix:** State clearly that the curve is a parameterized illustrative fit and identify which parameters are fixed from the companion analysis versus chosen for visualization.

- **P1A-M13 — Sec. XIV D / Sec. XIII / Table I (major)**  
  **Problem:** The “structural tension” between \(N_{\text{tot}}\approx 92\) and the erasure of matter-bounce \(f_{\mathrm{NL}}\) depends on a chain of assumptions, but the manuscript treats it as a quasi-definitive no-go.  
  **Required fix:** Present it as a conditional tension result, with explicit assumptions and a quantitative transfer-function caveat.

- **P1A-N1 — Abstract / Intro (nit)**  
  **Problem:** Repeated phrase structure: “channel-level closure” is used many times in near-identical form.  
  **Required fix:** Tighten repetition for readability.

- **P1A-N2 — Sec. IV Scope / Sec. IV E (nit)**  
  **Problem:** “operator-level” and “channel-level” are sometimes used interchangeably in nearby paragraphs, which is imprecise.  
  **Required fix:** Standardize terminology.

- **P1A-N3 — References [5], , , ,  (minor)**  
  **Problem:** Several references are future-dated relative to the paper date, or appear as arXiv preprints without venue confirmation. That is not inherently invalid, but it should be flagged in the bibliography style for PRD readiness.  
  **Required fix:** Verify all metadata at final submission and mark preprints consistently.

- **P1A-M14 — General bibliography audit (major)**  
  **Problem:** The paper cites many specialized results with quoted numerical claims, but the manuscript does not show that each quoted statistic is traceable to the cited paper’s abstract, table, or main result. Examples include the WMAP+Planck birefringence significances, the ACT DR6 number, SPHEREx forecast significance, and the claimed \(f_{\mathrm{NL}}\) forecast.  
  **Required fix:** For every quoted number taken from prior work, specify the exact location in the cited source and ensure the value matches that source.

## Summary recommendation
**REJECT**

The manuscript’s central claims are not yet presented at PRD-standard rigor. The most serious issues are internal inconsistency in the dark-energy scaling, repeated shifting between derivation and ansatz status, unresolved normalization ambiguities for the parity-odd coupling, and heavy dependence on unpublished companion papers for load-bearing numerical results. Before it could be considered for acceptance, the paper would need a full consistency pass that fixes the operator normalization, recomputes all headline numbers once, removes or quarantines unsupported claims from the abstract, and makes the bibliography/reproducibility claims self-contained and auditable.

---

## PASS 2 — self-critique findings (what initial review missed)

[P1A-M15 — Abstract / Sec. III A / Sec. VII / Fig. 4 (major)]  
**Problem:** The abstract says the benchmark birefringence \( \beta \approx 0.27^\circ \) is “inside the WMAP+Planck 1σ band” and “comparable to the independent ACT DR6 follow-up,” but the body later clarifies that the current central values differ by about \(0.73\text{–}0.77\sigma\) depending on whether one uses the joint or current-Planck uncertainty, and that LiteBIRD will *not* separate the benchmark from the current WMAP+Planck central value at high significance. The abstract’s phrasing collapses three different null procedures into one qualitative statement.  
**Required fix:** Rewrite the abstract to state the actual significance relative to each null hypothesis, and explicitly note that “inside 1σ of zero” is not the same as “close to the WMAP+Planck central value.”

[P1A-M16 — Abstract / Sec. XII B / Sec. XV (major)]  
**Problem:** The abstract presents the four-route closure as a result of the paper, but the body later says the closing of R2–R3 is only under explicitly labeled scaling/ansatz assumptions, while R4 is excluded only under the one-loop-matched naturalness argument. The abstract still reads as if all four routes are closed at the same evidentiary level.  
**Required fix:** Differentiate *amplitude no-go under ansatz* from *naturalness objection* in the abstract itself.

[P1A-M17 — Abstract / Sec. XII A / Appendix B (major)]  
**Problem:** The abstract says the dark-energy mapping is a phenomenological on-shell ansatz with off-shell mass dimension \(+1\), but Appendix B then gives two different bookkeeping routes: one using \(N_{\text{tot}}\approx 92\) from the on-shell ansatz and one using the genuine \(M_{\mathrm{Pl}}^4/\rho_\Lambda\) hierarchy giving \(N_{\text{tot}}\approx 94\). The main text repeatedly treats \(N_{\text{tot}}\approx 92\) as canonical while Appendix B says it is only an ansatz-dependent reparameterization.  
**Required fix:** State clearly in the abstract that \(N_{\text{tot}}\approx 92\) is *not* a derived prediction but one ansatz-specific bookkeeping choice, and keep the appendix’s \(N_{\text{tot}}\approx 94\) as the actual hierarchy estimate.

[P1A-M18 — Sec. II C / Eq. (11) / Sec. XII A (major)]  
**Problem:** The dilution factor \(D_{\mathrm{inf}}=\exp[-3N_{\text{tot}}](T_{\mathrm{reh}}/M_{\mathrm{GUT}})^{3/2}\) is later said to be matched only at order of magnitude, yet the text uses it to infer a specific residual “\(10^5\)” fine-tuning score and to compare it against \(\Lambda\)CDM’s \(10^{120}\). That comparison is not numerically stable because the prefactor itself is admitted to be only a heuristic ansatz.  
**Required fix:** Separate the order-of-magnitude heuristic from any quantitative tuning score; do not present the \(10^5\) figure as if it were a computed result with the same precision as the \(10^{120}\) hierarchy.

[P1A-M19 — Sec. II A 2 / Eq. (7) / Sec. IV D / Appendix C (major)]  
**Problem:** The paper uses \( \alpha/M \sim 10^{-21}\,\mathrm{GeV}^{-1} \) as the R4 benchmark, but Appendix C says the canonical ALP–photon coupling is \(g_{a\gamma} = \alpha_{\rm em} c_\gamma/(2\pi f_a)\), while the paper’s \(\alpha\) is the Mercuri-style one-loop coefficient. The footnote admits a basis-conversion gap of about a factor of 10 if one identifies the two naively. This means the quoted \(10^{-21}\,\mathrm{GeV}^{-1}\) is not a directly normalized operator coefficient but a hybrid quantity mixing two conventions.  
**Required fix:** Add a single conversion table showing exactly how the paper’s \(\alpha/M\) maps onto the canonical \(g_{a\gamma}\), and recompute all uses of the number in one basis only.

[P1A-M20 — Sec. IV B / Eq. (15) (major)]  
**Problem:** The Route-2 estimate is given as \(\sim 10^{-60}\) in the canonical ordering, but the text immediately says an “alternative ordering” gives \(\sim 10^{-33}\). That is not a minor rephrasing: it is a \(10^{27}\) swing in the same observable ratio. Although the paper says the closure survives either way, the manuscript still presents the \(\sim 10^{-60}\) estimate as if it were uniquely defined.  
**Required fix:** Choose one ordering as the authoritative derivation and either remove the alternative or explicitly label it as a different observable normalization.

[P1A-M21 — Sec. IV D / Sec. XV (major)]  
**Problem:** The Route-4 naturalness discussion computes \( \rho_\theta \approx 1.6\times10^{-10}\,\mathrm{eV}^4 \approx 6\rho_\Lambda \) at \(m_\theta=H_0\), and then says the produced density overshoots \(\rho_\Lambda\) by \(22\)–\(36\) orders of magnitude across the natural ALP range. Those two statements are incompatible unless the “overshoot” is being measured relative to a different normalization than the immediately preceding \(m_\theta=H_0\) benchmark.  
**Required fix:** Recompute the density ratio explicitly for each endpoint and the benchmark point, and make clear which quantity is being compared to \(\rho_\Lambda\).

[P1A-M22 — Fig. 2 caption / Sec. II C 1 / Appendix B (major)]  
**Problem:** Fig. 2 says the dilution waypoint is \(N_{\text{tot}}\approx 92\) with \(D_{\mathrm{inf}}\sim10^{-121}\), while Appendix B says the same hierarchy gives \(N_{\text{tot}}\approx 94\) for the genuine \(M_{\mathrm{Pl}}^4/\rho_\Lambda\) ratio. The caption and appendix are therefore using different numerical targets for the same figure.  
**Required fix:** Update the figure caption to say whether it illustrates the ansatz-specific \(N_{\text{tot}}\approx 92\) bookkeeping or the true hierarchy estimate \(N_{\text{tot}}\approx 94\).

[P1A-M23 — Fig. 3 caption / Sec. II C / Sec. XII A (major)]  
**Problem:** The caption describes the orange curve as the ECH model with \(H_0=69.2\), \(\Omega_m=0.310\), and enhanced radiation density, while the body also says the cosmological values are imported from a companion MCMC and are not independently peer-reviewable here. The figure is therefore a hybrid of a tuned visualization and an externally sourced parameter set, but the caption does not say that.  
**Required fix:** Mark the curve as a *parameterized illustrative fit* and identify which parameters come from the companion analysis versus which were chosen for presentation.

[P1A-M24 — Fig. 4 / Sec. VII / Sec. XV (major)]  
**Problem:** Fig. 4 states LiteBIRD will detect \(\beta\approx0.27^\circ\) at \(\sim9\sigma\), but the body later admits that this is only the significance relative to zero, not a discrimination significance against the current WMAP+Planck central value. The figure caption and the text are using the same number to imply two different claims.  
**Required fix:** Label the \(9\sigma\) value as a *null-to-detection* significance only, and separately state the much smaller current-vs-benchmark separation significance.

[P1A-M25 — Table III / Sec. XI / Sec. XIII (major)]  
**Problem:** Table III mixes *mechanism production*, *observational consistency*, and *posterior preference* in one symbol system, and the prose around Quintom-B is especially non-comparable: “can in principle accommodate the DESI evidence” is not the same kind of statement as a confirmed \( \checkmark \) for a predicted observable. The table therefore overstates comparability between rows.  
**Required fix:** Split the table into separate columns for theoretical possibility, predicted observable, and fitted posterior support.

[P1A-M26 — Table IV / Sec. XII A / Appendix B (major)]  
**Problem:** Table IV lists \(N_{\text{tot}}\approx 92\) as a “verified value,” but Appendix B says the same quantity is \(92\pm2\) under the ansatz choice and \(94\) under the genuine hierarchy estimate. Calling \(92\) “verified” is too strong given the appendix’s own uncertainty language.  
**Required fix:** Replace “verified value” with “ansatz-specific benchmark” and move the uncertainty/range into the main table.

[P1A-M27 — Sec. IV A / Eq. (13) / Sec. IV E (major)]  
**Problem:** The Route-1 contact term is written as parity-even in the body, but the closure summary still groups Route 1 under “parity-odd / dark-energy channels” in places. That is conceptually inconsistent even if the operator descends from a parity-odd parent sector.  
**Required fix:** Distinguish the parity of the *effective contact term* from the parity of the *underlying torsion sector* everywhere in the route summary.

[P1A-M28 — Sec. IV D / Sec. XIV D / Sec. XV (major)]  
**Problem:** The manuscript says the \(m_\theta\sim H_0\) tuning “relocates the cosmological-constant problem,” but elsewhere it still treats R4 as “closed” in the route summary. A route that is only excluded by a tuning objection is not closed in the same sense as an amplitude-suppressed channel.  
**Required fix:** Use a distinct label such as “naturalness-rejected” for R4 and do not bundle it under the same closure language as R1–R3.

[P1A-M29 — Sec. X D / Sec. X F / Sec. XV (major)]  
**Problem:** The perturbation-transparency proof says the Holst term vanishes identically on the Levi-Civita connection and contributes nothing to scalar/tensor perturbations, but the implications section still refers to “parity-sensitive channels (model-dependent tests of \( \gamma_{\mathrm{BI}} \) only under a derived \( \gamma_{\mathrm{BI}} \)-dependent photon or tensor-parity coupling).” That is weaker than the proof and reads like a leftover from an earlier, less settled draft.  
**Required fix:** Remove or sharply qualify any sentence implying residual perturbative sensitivity of \( \gamma_{\mathrm{BI}} \) once the transparency theorem has been established.

[P1A-M30 — Sec. IX J / Sec. XII A / Sec. XIV D (major)]  
**Problem:** Barrier 10 says the bridge from bounce physics to late-time dark energy must be either generic or bounce-specific, but later the paper uses the \(N_{\text{tot}}\) sensitivity argument as if it were a route-specific no-go. That is a stronger inference than the barrier statement supports.  
**Required fix:** Rephrase Barrier 10 and the structural-tension discussion as a conditional statement about the specific scaling ansatz, not as a generic no-go for all bounce-to-dark-energy bridges.

[P1A-M31 — Abstract / Sec. IX / Sec. XV (major)]  
**Problem:** The abstract says the paper reports “13 logically-independent mechanism-class constraints,” yet Table II and the body repeatedly emphasize there are 14 catalog entries with B8 subsumed by B14. That wording is acceptable only if the abstract also states that the 14-entry catalog is *not independent by construction*.  
**Required fix:** Make the 13-vs-14 independence structure explicit in the abstract sentence itself.

[P1A-M32 — Sec. III A / Sec. VII / Sec. XV (major)]  
**Problem:** The manuscript says the WMAP+Planck result is \(\beta_{\rm obs}=0.342^\circ\pm0.094^\circ\) and “\(\sim3.6\sigma\) from \(\beta=0\),” while ACT DR6 is \(0.215^\circ\pm0.074^\circ\) and “\(\sim2.9\sigma\).” Those are fine individually, but the text repeatedly juxtaposes them as if they were direct measures of the same null procedure. They are not directly comparable because they come from different data sets, estimators, and systematics.  
**Required fix:** Add a one-line qualifier every time the two significances are discussed together: *different estimators, different nulls, not directly comparable*.

[P1A-M33 — Appendix A / Appendix B / Table IV (major)]  
**Problem:** Table IV labels \(\gamma\) as “fixed: 0.274” with a scheme range of \(0.037\), but Appendix B then uses a different gamma value (\(0.2375\)) to get the canonical LQC density \(0.41\rho_{\rm Pl}\). This is a stale-number problem: the table and the appendix are not using the same \(\gamma\) benchmark.  
**Required fix:** Either standardize on one \(\gamma\) across the manuscript or explain explicitly that \(0.2375\) is used only for the canonical LQC status-report comparison and not for the paper’s chosen entropy-counting scheme.

[P1A-M34 — Sec. II B / Fig. 2 / Appendix B (major)]  
**Problem:** Fig. 2 calls the hierarchy “dimensionally correct on-shell at the bounce,” but Appendix B says the operator is not a controlled dimension-\(+4\) EFT and that the missing powers come from on-shell curvature insertions. That means the figure caption reads more strongly than the appendix permits.  
**Required fix:** Replace “dimensionally correct” with “dimensionally consistent only after on-shell scaling assumptions.”

[P1A-M35 — Sec. IV B / Sec. IV C / Sec. XV (major)]  
**Problem:** The Route-2 and Route-3 closures both say the amplitude suppression survives any \(O(1)\) rescaling of the ansatz coefficient, but Route-4 is claimed to be adjustable by freely floating \(\alpha/M\). That makes the sensitivity logic inconsistent across routes: sometimes the coefficient is “rigid,” sometimes it is “free,” without a common rule for when the paper treats a parameter as fixed versus fit.  
**Required fix:** Add a parameter-status convention block stating which couplings are fixed, which are fit, and which are treated as upper bounds in each route.

