# P1A R26conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.53.pdf` md5=878edf0c pages=25
**Input format**: TEXT + web search + pass-2 self-critique (14242 chars)
**Wall time**: 66.9s

---

P1A-E1 (ESSENTIAL)  
Section: Abstract, p.1; throughout text  
Problem: Multiple references are cited as “companion work in preparation” with explicit arXiv-style identifiers and are treated as if already “posted concurrently on arXiv,” but there is no trace of them on arXiv or NASA ADS. Specifically:  
• [2] “H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (2026), companion paper, posted concurrently on arXiv.”  
• [6] “H. Golden, Cobaya MCMC + NaMaster Birefringence + ALP Companion…, (2026), companion paper, posted concurrently on arXiv.”  
• , ,  similarly described as companion/technical works “posted concurrently” or “available upon request.”  
Searches for these titles and author on arXiv and ADS give no matches; neither arXiv IDs nor journal DOIs are provided.[1][5]  
Required fix: Either (i) provide actual arXiv IDs/DOIs and verify that the titles, authors, and years match the bibliography, or (ii) if these works are not yet public, rephrase all references to them as “in preparation, private work” and remove all “posted concurrently” language. For any quantitative or methodological claims that depend critically on these unseen papers (e.g., SPHEREx Fisher forecasts, MCMC numerical results, anomaly catalog statistics), either make the relevant material self-contained in this manuscript or remove the claims.

---

P1A-E2 (ESSENTIAL)  
Section: Abstract, p.1; Sec. III A, p.8; Sec. XIII, p.19–20; Appendix C, p.23  
Problem: The paper quotes several key numerical results from the literature without giving sufficient bibliographic detail and, in at least one case, introduces a future-dated arXiv ID. Example issues:  
• Cosmic birefringence from Minami & Komatsu [3] and Eskilt & Komatsu [4] is quoted as “βobs = 0.342° ± 0.094° (∼ 3.6σ from β = 0).” This matches the value in Eskilt & Komatsu 2022, Phys. Rev. D 106, 063503.[4] However, the paper also refers to a WMAP+Planck “first reported by Minami & Komatsu [3]” without specifying that [3] is Phys. Rev. Lett. 125, 221301 (2020), which has different central values.  
• ACT DR6 result “β = 0.215° ± 0.074° at ∼ 2.9σ (Diego-Palazuelos & Komatsu [5])” is attributed to “arXiv:2509.13654.” No such arXiv entry exists as of now; searching for “Diego-Palazuelos Komatsu birefringence ACT DR6” yields no arXiv record.[1]  
• Liu et al. 2025 torsion cosmology  is referenced as arXiv:2507.04265; that ID exists and is “Torsion cosmology in the light of DESI, supernovae and CMB.”[1][5] However, the quoted numbers in P1A (“torsion fits the S8 tension”) are only loosely described and not numerically cross-checked.  
Required fix:  
1. For [3] and [4], provide correct journal citations and ensure each quoted β and σ value can be traced to explicit equations/tables.  
2. For the ACT DR6 result, either supply the correct arXiv ID / journal DOI, or, if not yet public, remove the arXiv identifier and mark it explicitly as “private communication” or “in preparation”; do not give a future-dated arXiv number.  
3. For  (torsion cosmology), explicitly cross-check any quoted H0, S8, and α constraints against the actual values in the paper and adjust text to match.[1]  

---

P1A-E3 (ESSENTIAL)  
Section: Tables & Abstract (Table I, p.4; Table III, p.19; Appendix B, p.22)  
Problem: The abstract and body emphasize numerical hierarchies and “fine-tuning reductions” (e.g., “reduction from 10^120 to 10^5,” “N_tot ≈ 92 e-folds”) that are tied to an explicitly ad hoc dimensional ansatz ρ_Λ ~ [(α/M) M_Pl]^5 / M_Pl, see Appendix B. These numbers cannot be traced to any external reference and are not derived consistently from a dimension-4 operator. The paper acknowledges this is a phenomenological ansatz, but still uses it as if it were a quantitative, well-defined result (e.g., Figure 5 “fine-tuning-score comparison” bar chart, Appendix B eqs. (B1)–(B2)). No external paper derives this scaling; it is introduced here.  
Required fix: Either fully derive a dimension-4, diffeomorphism-invariant effective operator whose on-shell evaluation yields the stated scaling, with clear mass-dimension counting and Planck factors, or clearly demote all numerical claims that depend on this ansatz to qualitative, order-of-magnitude illustrations, removing specific figures (e.g., 10^5 hierarchy, N_tot = 92) wherever they could be interpreted as quantitative predictions. In particular, Figure 5 and related text should be rewritten or removed unless a controlled EFT derivation is supplied.

---

P1A-E4 (ESSENTIAL)  
Section: Global; Abstract p.1; Sec. I A p.3–4; Sec. IV E p.12; Sec. XV p.21–22; Appendix B p.22  
Problem: The manuscript repeatedly uses version-history/self-audit language inconsistent with PRD style, and also includes meta-information about earlier drafts and internal corrections within the body text and footnotes. Examples:  
• “Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion…” (p.2 footnote, again in Sec. X footnote on p.17).  
• “This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts; the migration is documented in Paper III §6.” (Sec. XIII, p.20.)  
• Multiple references to “earlier drafts,” “misstated in earlier drafts,” “correction preserves the headline conclusion,” internal chain status commentary in Table III, etc.  
Required fix: Remove all draft-history and internal-revision commentary from the main text and appendices. If a previous published paper made an error, that must be handled via a separate erratum, not embedded in this manuscript. Rephrase any necessary clarifications in a timeless form (e.g., “The Holst dual contraction must be distinguished from the Pontryagin density…” without referring to earlier versions).

---

P1A-E5 (ESSENTIAL)  
Section: Global (references and in-text claims)  
Problem: Multiple references are used to support specific numerical “firsts” or strong-statistics claims without adequate verification or with overstatements:  
• DESI DR2 dynamical dark energy: The paper cites “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9,10].” DESI DR2 analyses do report tensions with ΛCDM at ~2.5–3.9σ depending on datasets, but the paper does not state which exact combination yields 4.2σ and how this number is computed; the source  quotes specific significances (e.g. 2.5–3.9σ) that should be reproduced numerically.[3]  
• Several “3–5σ” SPHEREx forecasts for f_NL = −35/8 are asserted with concrete σ(f_NL) ≃ 0.7–1.0, but all of these numbers depend on the unseen “Paper II” forecast and are not traceable to a public reference.  
Required fix: For each quoted σ-level or significance derived from external work, explicitly state the original numerical value and dataset combination as reported in the cited paper and check that the significance matches the cited authors’ tables/figures. Where your numbers depend on non-public companion works, either (i) bring the relevant derivation into this manuscript in enough detail to recompute the σ values, or (ii) weaken the claims to purely qualitative statements without specific σ levels.

---

P1A-E6 (ESSENTIAL)  
Section: Entire paper (esp. Abstract, Sec. I A, Sec. IV, Sec. IX, Conclusions)  
Problem: The central claim that “we close four enumerated minimal-ECH dark-energy routes” is presented as a major result, but several of the “closures” are admitted to rest on strongly phenomenological assumptions (non-EFT ansatz for ρ_Λ, assumed mapping between α/M and birefringence, specific chiral-running ansatz, etc.), and at least one route (Route 4) is closed only by a naturalness objection, not by a strict amplitude bound. This is not framed clearly enough; a non-expert reader might infer a rigorous no-go theorem where the paper actually has a conditional set of arguments with substantial theory-uncertainty.  
Required fix: Rephrase the headline statements and conclusion to make explicit that (1) the four-route “closure” is conditional on the stated EFT ansätze and parameter choices; (2) only some routes are amplitude-excluded, while Route 4 is “disfavored on naturalness grounds but not ruled out”; (3) no operator-basis completeness is achieved. The abstract and Sec. XV must be rewritten to avoid overstating the rigor of the no-go result.

---

P1A-M1 (MAJOR)  
Section: References [1]–[5], –, –, –  
Problem: Spot checks of several key references show mixed quality of citation metadata:  
•  and  correspond to DESI BAO cosmology papers.  is correctly “DESI DR2 results II: Measurements of BAO…” (PRD 112, 083515 (2025)). The quoted H0 and σ8 values in the text are roughly consistent with published numbers, but are sometimes presented without explicit uncertainties or dataset context.  
•  Ashtekar & Singh 2011 CQG “Loop quantum cosmology: a status report” is correctly cited and the critical density range ρ_crit ≃ 0.27–0.41 ρ_Pl is described as a scheme-dependent range; this is consistent with Ashtekar & Singh’s ρ_crit ≃ 0.41 ρ_Pl and variations when γ is changed.  
• , , ,  (Freidel–Minic–Takeuchi; Mercuri; Shapiro–Teixeira; Mercuri–Capozziello) are cited for structure of Holst/NY invariants and loop-induced terms. An ADS check confirms the titles and journal information.  
•  Heinrich et al. JCAP 2024 is correctly an f_NL forecast paper; the σ(f_NL) ~ 0.7 Fisher number cited in the text appears plausible but is not numerically reproduced here due to lack of explicit table reproduction in the manuscript.  
However, there is no systematic check of *all* references in the manuscript (and it is long); given the presence of at least one fabricated-looking arXiv ID (see P1A-E2), the entire bibliography needs a thorough check.  
Required fix: Perform a complete audit of the bibliography:  
1. For every reference with an arXiv ID, verify that the ID exists and the title/authors/year match.  
2. For every journal citation, check volume, page, year, and DOI against ADS.  
3. Correct any mismatches and remove any references that cannot be verified. Provide corrected metadata in the revised manuscript.

---

P1A-M2 (MAJOR)  
Section: Sec. X (Perturbation Transparency), p.16–17; footnotes on p.2 and p.17  
Problem: The Holst-term “Bianchi vanishing” argument is correct in broad spirit (on a torsionless connection, the Holst term is non-dynamical), but the way it is written could confuse the Holst dual contraction with a genuine scalar built from curvature. In standard formulations, the Holst term is \( \epsilon^{\mu\nu\rho\sigma} R_{\mu\nu\rho\sigma} \) with internal indices, and care is required to distinguish internal vs spacetime epsilon tensors. The text partially corrects an earlier misidentification with the Pontryagin density, but the explanation is verbose and mixes form-language with coordinate components in a way that obscures the clean algebraic reason for vanishing. No external reference is cited for the exact form of the Bianchi argument.  
Required fix:  
1. Provide a concise, covariant derivation of the vanishing of the Holst contribution on a torsion-free FRW background, with clear notation distinguishing internal Lorentz indices and spacetime indices.  
2. Cite at least one standard reference (e.g., Holst 1996, or a modern review of ECH with fermions) that presents this reduction.  
3. Clean up the repeated, draft-history-laden footnotes, focusing only on the final, correct statement.

---

P1A-M3 (MAJOR)  
Section: Sec. IV A–D (Four routes), p.9–12  
Problem: Several amplitude estimates are given (e.g. “Route 2 one-loop induced β is suppressed by ≥ 10^{-58}”, “overshoot by 22–36 orders of magnitude,” “∆γ/γ ∼ 10^{-2}”) without transparent, recomputable numerical steps. The text sometimes mixes GeV and eV units and refers to “two orders-of-magnitude allowance” without showing intermediate calculations. These are central to the claimed amplitude-level closures, but the reader cannot independently recompute them from the given numbers alone.  
Required fix: For each of the four routes, add a short, explicit numerical subsection or table that:  
1. Lists the numerical inputs with units (e.g. H0 in eV, M_Pl in GeV, α_em, β_obs in radians, etc.).  
2. Shows the intermediate steps leading to the quoted suppression factors or overshoots.  
3. Verifies that dimensions are consistent at each step.  
This is necessary for PRD-level reproducibility of key quantitative claims.

---

P1A-M4 (MAJOR)  
Section: Abstract p.1; Sec. XIII & XIV, p.19–21  
Problem: Sigma values from different null procedures and different classes of data are juxtaposed in ways that could mislead readers into direct comparison, contrary to the review instruction:  
• The paper places the ∼3.6σ birefringence detection next to forecasted 3–5σ SPHEREx f_NL and ≳5σ LiteBIRD β constraints, and also next to dynamical-DE significances (3.1–4.2σ from DESI).  
• There is no explicit statement that these σ values arise from entirely different likelihoods and null hypotheses, and hence are not directly comparable metrics of tension.  
Required fix: Whenever σ values from unrelated procedures are mentioned in the same sentence/paragraph (e.g., in the abstract and in Sec. XIII), explicitly add language such as “These σ values are not directly comparable, as they arise from distinct datasets and null tests,” and avoid implying any relative ranking between them.

---

P1A-M5 (MAJOR)  
Section: Length and scope (entire paper, 25 pages)  
Problem: The paper is very long relative to its concrete, rigorously established contribution. Much of the text is expository, speculative, or devoted to internal programme logistics and future work (e.g., Paper I(b), Paper II, III, IV). For a PRD article, the core novel content—careful amplitude and naturalness analysis of four ECH channels and a clear perturbation-transparency statement—could be presented in a significantly shorter paper.  
Required fix: Condense the manuscript to focus strictly on:  
• The precise definition of the four channels.  
• The perturbation-transparency derivation.  
• The key amplitude/naturalness estimates that demonstrably close each route, with clear caveats.  
• A minimal discussion of implications.  
Remove or drastically shorten internal-programme commentary, future-work roadmaps, and repeated descriptions of external surveys. Recommended maximum length ~15 journal pages.

---

P1A-m1 (MINOR)  
Section: Abstract, p.1; Sec. I A p.3; Sec. XIV D p.21  
Problem: The tension between “N_tot ≈ 92 e-folds” and “matter-bounce f_NL = −35/8 survives” is discussed at length. While the qualitative argument is reasonable, the quantitative mapping of SPHEREx k-range to bounce scales (k_physical^bounce ≈ e^{N_tot − N_exit} k_physical^SPHEREx) is only sketched; the corresponding numerical example “e^{32}” should be supported by explicit numbers for H, a, etc., or else stated more cautiously as an order-of-magnitude illustration.  
Required fix: Clarify that the e^{32} factor is illustrative and provide a one-line derivation showing how the physical scales are related, or remove the numerical exponent and keep the qualitative statement only.

---

P1A-m2 (MINOR)  
Section: Sec. V, p.12–13; Sec. III B p.8, references –  
Problem: The paper refers to a new galaxy spin chirality analysis (Paper IV ) and to Shamir’s prior claims. This is fine, but the text occasionally uses phrases like “confirmed null” and “p_LEE < 10^{-4}” without specifying exactly what null test or look-elsewhere correction was used; moreover, these numbers cannot be checked because  is not public.  
Required fix: Either (i) provide enough methodological detail within this manuscript for the reader to understand the null test and p-value definition, or (ii) soften the wording to “consistent with no dipole within current errors, per our companion analysis ” without quoting untraceable p-values.

---

P1A-m3 (MINOR)  
Section: Table IV, p.23  
Problem: Table IV mixes “Verified Value” (e.g. γ = 0.274) with “fitted” or “midpoint” values (N_tot ≈ 92, β ≈ 0.27°, f_NL = −35/8) without clearly distinguishing which are empirical constraints, which are theoretical exact predictions, and which are chosen benchmarks.  
Required fix: Add a column or explicit note clarifying for each parameter whether it is: fixed by theory, fitted to data, a benchmark choice, or a class-level prediction. Ensure the table caption explains this.

---

P1A-n1 (NIT)  
Section: Multiple (e.g. Sec. I A, Sec. II C, Sec. XII A)  
Problem: Some phrases are slightly promotional or colloquial for PRD (e.g. “burned-in dilution waypoint,” “mathematical scaffolding,” “reparameterization as sensitivity,” “native-trained novelty rates”).  
Required fix: Edit for a more neutral, technical style; remove marketing-like phrasing.

---

## Summary recommendation

REJECT.

The manuscript has an interesting and potentially useful goal—systematically assessing several Einstein–Cartan–Holst dark-energy channels and making a clear perturbation-transparency statement—but it does not currently meet PRD standards for citation reliability, theoretical rigor, or focus. There are serious issues with unverifiable or future-dated companion references, heavy reliance on an ad hoc dimensional ansatz for key numerical claims, and over-ambitious “closure” statements that go beyond what is strictly demonstrated. Fixing these would require substantial restructuring, clearer derivations, and publication of the companion works; the resulting contribution would likely be better presented as a shorter, more focused paper.

---

## PASS 2 — self-critique findings (what initial review missed)

[P1A-M6] **Abstract faithfulness / internal inconsistency:** the abstract says the paper “assess[es] four enumerated minimal-ECH spin-torsion channels as candidate sources of late-time dark energy and find[s] that each fails at the amplitude level under stated assumptions,” but the body later concedes that Route 4 is *not* an amplitude no-go and is only “closed by a naturalness objection” with a free-coupling spectator-ALP fit that can reproduce both \( \beta_{\rm obs} \) and \( \rho_\Lambda \) by tuning \( m_\theta \sim H_0 \). That means the abstract overstates the result: the manuscript does not establish that *each* route fails at the amplitude level.[paper text]

[P1A-M7] **Abstract faithfulness / overclaim about “13 logically-independent mechanism-class constraints”:** the abstract says the paper reports “13 logically-independent mechanism-class constraints,” but Table II explicitly states that Barrier 8 and Barrier 14 “close the same observable channel” and that B14 “subsumes” B8, so they are *not* logically independent. The body later repeats that one barrier is retained only for “historical mechanism-class completeness,” so the abstract’s “13 logically-independent” wording is not faithful to the manuscript’s own classification.[paper text]

[P1A-M8] **Arithmetic / stale count mismatch:** the abstract and opening pages state “13 logically-independent barriers (Sec. IX; 14 historical catalog entries, of which B8 is subsumed by B14),” but the *table* and later discussion count 14 mechanism-class constraints. The manuscript alternates between “13 logically-independent,” “14 historical catalog entries,” and “14 mechanism-class constraints” without a single unambiguous convention, which is an internal counting inconsistency rather than just a wording choice.[paper text]

[P1A-M9] **Arithmetic / inconsistent fine-tuning hierarchy:** the abstract claims the phenomenological ansatz yields a reduction from \(10^{120}\) to \(10^{5}\), while Appendix B corrects the genuine cosmological-constant hierarchy to \(\sim 10^{122}\) and says the residual \(10^{5}\) is only a qualitative reparameterization as sensitivity to \(N_{\rm tot}\), not a quantitative bookkeeping result. That means the headline “reduction from \(10^{120}\) to \(10^{5}\)” in the front matter is numerically stale relative to the appendix’s corrected hierarchy.[paper text]

[P1A-M10] **Arithmetic / \(N_{\rm tot}\) inconsistency:** the front matter and main text use \(N_{\rm tot}\approx 92\) as the canonical value, but Appendix B says the same scaling argument implies \(N_{\rm tot}\approx 94\) from \(10^{122}\rightarrow e^{-3N_{\rm tot}}\), and then reassigns \(92\pm2\) as an order-of-magnitude estimate. The paper therefore presents \(N_{\rm tot}\approx 92\) as both a fitted value and a schematic estimate from a different hierarchy calculation, without clearly reconciling the two numbers.[paper text]

[P1A-M11] **Equation dimensional consistency / Eq. (7):** the manuscript says the one-loop estimate is
\[
\alpha/M \sim \frac{g^2\gamma}{32\pi M}\ln(\Lambda^2_{\rm UV}/\mu^2)+\delta_{NY},
\]
but the line immediately below treats \([(\alpha/M)M_{\rm Pl}]\) as a dimensionless quantity of order \(10^{-2}\). As written, the displayed formula is dimensionally incomplete unless the logarithm and \(\delta_{NY}\) are both dimensionless and the \(1/M\) factor is being interpreted as a mass-suppressed coupling; the paper never makes this dimensional bookkeeping explicit in the equation itself, even though later sections rely on it numerically.[paper text]

[P1A-M12] **Equation dimensional consistency / Eq. (10):** the paper defines
\[
\Lambda_{\rm eff}=\Xi M_{\rm Pl}^2+c_\omega\omega^2,\qquad \Xi\equiv (\alpha/M)M_{\rm Pl}D_{\rm inf},
\]
and then later says \(\rho_\Lambda=\Lambda_{\rm eff}M_{\rm Pl}^2=\Xi M_{\rm Pl}^4\). This only works if \(\Xi\) is dimensionless and \(\Lambda_{\rm eff}\) has units of mass\(^2\), but the sentence “\(\Xi\) is the dimensionless ratio \(\rho_\Lambda/M_{\rm Pl}^4\)” is not consistent with the earlier definition unless the reader infers an additional implicit normalization. The paper should state the unit convention once and keep it fixed.[paper text]

[P1A-M13] **Equation dimensional consistency / Appendix B Eq. (B2):** Appendix B says \( [\alpha/M]=-1\) and \( [\varepsilon e e F]=+2\), giving \([L_{\rm odd}]=+1\), then “promotes” the operator by replacing \(\alpha/M\to \alpha M_{\rm Pl}^3/M\) to obtain dimension \(+4\). That promotion is not an EFT derivation but a dimensional patch, and the appendix itself admits this. Because the main text later uses the resulting \(\rho_\Lambda^{\rm bounce}\sim (\alpha/M)^5 M_{\rm Pl}\) scaling as though it were derived, the operator-dimension inconsistency propagates into the headline hierarchy claims.[paper text]

[P1A-M14] **Arithmetic / Eq. (18) Planck-suppression chain:** Barrier 1 states
\[
g_{\rm eff}\sim \frac{H_0}{M_{\rm Pl}}\sim 10^{-61},
\]
and then says the required fine-tuning is \(\delta m_T^2/m_T^2\sim(H_0/M_{\rm Pl})^2\sim10^{-122}\). Those two quoted orders of magnitude are internally consistent, but the text then says “to achieve \(g_{\rm eff}\sim1\), one needs \(m_T\sim M_{\rm Pl}\),” which is not a derivation from the displayed equation unless one also assumes \(t_3\sim m_T^{-1}\) *and* ignores the earlier statement that Eq. (18) is only a scaling ansatz. The manuscript should not present the \(m_T\sim M_{\rm Pl}\) conclusion as if it follows uniquely from the formula as written.[paper text]

[P1A-M15] **Equation dimensional consistency / Fig. 2 caption vs body:** Fig. 2 captions the “energy density hierarchy” as illustrating the ansatz
\[
\rho_{\rm vac}\sim[(\alpha/M)M_{\rm Pl}]^4 M_{\rm Pl}^4,
\]
but the body repeatedly calls the operator in Eq. (6) dimension \(+1\) and then says the map to \(\rho_\Lambda\) is an on-shell scaling ansatz. The figure caption presents the relation as if it were a derived “energy density hierarchy,” whereas the main text admits it is only a phenomenological bookkeeping device.[paper text]

[P1A-M16] **Null-procedure comparability / Table I and Sec. III:** Table I places “\(f_{\rm NL}=-35/8\) (Paper II forecast)” next to “\(H_0=67.68\pm1.06\)” and “\(\Delta N_{\rm eff}\approx0\),” while the body says the \(f_{\rm NL}\) number is a Fisher forecast from a companion analysis and the cosmological fit values come from a separate MCMC proxy. These are different null procedures and likelihood constructions, but the table does not say they are not directly comparable, so the reader could mistakenly treat them as commensurate constraints.[paper text]

[P1A-M17] **Null-procedure comparability / significance juxtaposition in Sec. VI and XIII:** the manuscript juxtaposes \(3.6\sigma\) WMAP+Planck birefringence, \(2.9\sigma\) ACT DR6 birefringence, \(3.1\)–\(4.2\sigma\) DESI dark-energy preference, and \(3\)–\(5\sigma\) SPHEREx \(f_{\rm NL}\) forecast in the same argumentative chain. The text sometimes says these are “not directly comparable,” but not consistently; several passages still read as if the various \(\sigma\)-values rank mechanisms on a single scale. This should be flagged wherever the manuscript uses them to support a common “strength” narrative.[paper text]

[P1A-M18] **Figure-caption vs body mismatch / Fig. 4:** Fig. 4 says the LiteBIRD \(\sigma(\beta)\approx0.03^\circ\) forecast will “either confirm a non-zero birefringence at high significance or rule out the spectator-ALP class,” but the body later corrects this and says LiteBIRD alone will *not* separate the spectator-ALP value \(0.27^\circ\) from the current WMAP+Planck central value because the prior \(0.094^\circ\) uncertainty dominates. The figure caption therefore overstates the discriminating power relative to the later, more careful discussion.[paper text]

[P1A-M19] **Figure-caption vs body mismatch / Fig. 5:** Fig. 5’s caption describes a “fine-tuning-score comparison” with \(\Lambda\)CDM \(10^{120}\), quintessence \(10^{60}\), \(f(R)\) gravity \(10^{40}\), and this work \(10^5\), and says the “115 orders of magnitude improvement” annotation refers to that score difference. But Appendix B says the \(\sim10^5\) residual is only a reparameterization of sensitivity to \(N_{\rm tot}\), not a real resolution, and that the true hierarchy is \(\sim10^{122}\). So the figure caption is semantically incompatible with the appendix’s more cautious interpretation.[paper text]

[P1A-M20] **Internal cross-reference / Appendix C vs Sec. IV D:** Sec. IV D derives the relation \( \beta=(\alpha/2M)\Delta\theta\) and cites Appendix C for the factor of \(1/2\). Appendix C indeed derives that factor, but it does so for a homogeneous pseudoscalar \(\theta\) in Maxwell–Chern–Simons theory, not for the ECH torsion sector itself. The main text sometimes writes as if the appendix derivation directly validates the ECH identification \(\alpha/M\sim10^{-21}\,\mathrm{GeV}^{-1}\), but Appendix C only justifies the Chern–Simons normalization, not the ECH-to-ALP parameter mapping.[paper text]

[P1A-M21] **Unsupported novelty claim / “14-constraint catalog” as “novel results”:** Table II classifies Barriers 1, 2, 3, 4, 8, 10, 11, 12, 14 as “Novel results” and 5, 6, 7, 9 as “Known results.” That is a strong novelty taxonomy, but the manuscript never provides an explicit comparison against all prior ECH, PGT, Holst, bounce, and birefringence literature showing these barriers are genuinely new as stated. In particular, several barriers are rephrasings of standard arguments (Planck suppression, scale separation, Liouville conservation), so the novelty labeling is not supported in the text.[paper text]

[P1A-M22] **Unsupported novelty claim / “first-principles structural result” for perturbation transparency:** Sec. X and the conclusions call perturbation transparency a “central result” and say it “generalizes Hehl et al. (1976) to the Holst sector and to all perturbation orders.” That is a strong novelty claim, but the paper itself also says the result is a straightforward consequence of \(T=0\) and the Bianchi identity. If the argument is standard, the manuscript should not imply a more novel theorem without explicit comparison to prior Holst/Nieh–Yan treatments.[paper text]

[P1A-M23] **Appendix vs main-text mismatch / Table IV parameter semantics:** Table IV labels \(N_{\rm tot}\) as “Total e-folds” with prior \([60,120]\) flat and “\(\approx92\) (fitted),” while Appendix B says \(N_{\rm tot}\approx92\pm2\) is an order-of-magnitude estimate dependent on the ansatz choice and not a precise fitted quantity. The same parameter is therefore presented as a fitted result in one place and a systematic-sensitive estimate in another.[paper text]

[P1A-M24] **Internal cross-reference / Section XIV D vs Sec. II C 1:** Sec. XIV D says the structural-tension result follows from \(N_{\rm tot}\approx92\) and the SPHEREx accessible range, and cross-references the “Reheating thermal-reset barrier” in Sec. II C 1. But Sec. II C 1’s barrier is actually embedded in the discussion of inflationary dilution in Sec. II C, and the text’s claim that reheating “already closes the bounce-era-memory dilution channel” is a later argumentative strengthening, not a result proven in the earlier section. The cross-reference therefore points to a weaker statement than the one the later section attributes to it.[paper text]

[P1A-M25] **Unsupported p-value / Table III footnote:** Table III footnote says the galaxy-spin null results are reported with “pLEE < 10^{-4}” and refers to a dipole/hemisphere/fCW significance suite, but the main text never defines the look-elsewhere correction, the trial factor, or how that \(p\)-value is computed from the classifier outputs. The quoted \(p\)-value therefore cannot be independently checked from the manuscript itself.[paper text]

[P1A-M26] **Arithmetic / ACT-Planck discrepancy calculation:** In Sec. IV D the paper computes
\[
|0.342-0.215|/\sqrt{0.094^2+0.074^2}=0.127/0.120\approx1.06,
\]
which is correct arithmetically, but the next sentence says this “bounds \(\alpha/M\) at \(\sim10^{-21}\,\mathrm{GeV}^{-1}\), identical to the value already quoted in Sec. II A 2.” That step is not a numerical consequence of the difference calculation; it is an external model identification. The manuscript mixes a valid arithmetic comparison with a parameter inference that is not derived from that comparison alone.[paper text]

[P1A-M27] **Arithmetic / SPHEREx significance arithmetic:** The SPHEREx footnote says \(\sigma(f_{\rm NL})\approx0.7\) implies raw significance \(|f_{\rm NL}|/\sigma = 4.375/0.7\approx6.25\sigma\), which is then “degraded” to \(3\)–\(5\sigma\) after corrections. That arithmetic is internally consistent, but the table and narrative often quote \(3\)–\(5\sigma\) as if it were a direct forecast rather than a post-processed, systematics-degraded range. The manuscript should keep the raw Fisher significance and the degraded realistic range distinct throughout.[paper text]

[P1A-M28] **Appendix B vs main-text hierarchy numbers:** Appendix B says the local pseudo-density \(\rho_\Lambda^{\rm bounce}\sim10^{-2}M_{\rm Pl}^4\) is *not* the bounce-scale density \(\rho_{\rm bounce}\sim M_{\rm Pl}^4\), and that the true \(M_{\rm Pl}^4/\rho_\Lambda^{\rm obs}\) hierarchy is \(\sim10^{122}\). Main-text figures and captions still present “\(10^5\)” and “115 orders of magnitude improvement” as if they describe the same hierarchy. The appendix correction does not propagate cleanly into the main-text quantitative narrative.[paper text]

[P1A-M29] **Internal cross-reference / Section III A and Appendix C:** Sec. III A says the paper performs no independent EB-based \(\beta\) extraction and simply uses published \(\beta_{\rm obs}\). Yet Appendix C presents a full derivation of the rotation mapping and later says it “closes the normalization chain from the Lagrangian to the numerical prediction.” That is not a contradiction, but the main text still implies the numerical value is a benchmark only, while the appendix frames the mapping as a predictive derivation. The manuscript should be clearer that the derivation is only of normalization, not of the observed value itself.[paper text]

