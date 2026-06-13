# P1A R40conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1a_ech_nogo.pdf` md5=fd4707e3 pages=28
**Input format**: TEXT + web search + pass-2 self-critique (13126 chars)
**Wall time**: 83.8s

---

P1A-E1 – ESSENTIAL  
Section: Abstract, p.1  
Problem: The abstract references “SPHEREx forecast 2.6–5σ quoted above” and then correctly notes “these significances, and the SPHEREx forecast 2.6–5σ quoted above, arise from different null procedures and are not directly comparable in a single tension table.” This satisfies the “not directly comparable” requirement there, but the same σ(fNL) and σ(β) values are later juxtaposed in Figures 4 and 6 and in Discussion/XIV without repeating this caveat at every juxtaposition, contrary to instruction 7.  
Required fix: At every location where σ values from different null procedures (e.g., Planck β, ACT β, SPHEREx fNL Fisher, LiteBIRD β forecast, fine‑tuning “σ” in Fig. 5) are juxtaposed or visually compared, add an explicit sentence that they arise from different null procedures and must not be interpreted as directly comparable significance levels. Alternatively, avoid multi‑σ plotting/phrasing that visually suggests such a comparison.

P1A-E2 – ESSENTIAL  
Section: Abstract & throughout (multiple pages)  
Problem: Multiple references are made to companion papers “[2, 6, 23, 46]” that are “in preparation” and are used as load‑bearing sources (e.g., SPHEREx Fisher forecast, Cobaya MCMC results, NaMaster validation, galaxy spin catalog, NANOGrav real‑KDE analysis). These are not available on arXiv, have no DOI, and cannot be verified by an external reader. At PRD level, load‑bearing results must be traceable.  
Required fix: Either (a) post these companion papers to arXiv (or in refereed form) with stable identifiers and update the citations accordingly, or (b) remove all load‑bearing dependence on them and replace with self‑contained derivations, explicit tables, and methods in the present paper, or with already‑published literature. For any results that remain purely “internal,” clearly label them as qualitative illustrations only, not as quantitative findings.

P1A-E3 – ESSENTIAL  
Section: Abstract, p.1; Sec. I, Sec. IX, Table II, Sec. XV  
Problem: The paper repeatedly claims “13 logically‑independent barriers (14 historical catalog entries with B8 subsumed by B14)” as a foundational result. However, several of these barriers (notably Barriers 5, 6, 7, 9, 10, 11, 13) are stated as qualitative heuristics or broad philosophical statements with only sketchy or no quantitative derivations. For PRD, such a strong closure claim (channel‑level no‑go) requires that each barrier be (i) precisely defined, (ii) quantitatively demonstrated, and (iii) clearly shown to be independent.  
Required fix: For each barrier in Sec. IX, provide a precise mathematical definition (assumptions, equations, and inequalities), a quantitative derivation or explicit reference to a peer‑reviewed calculation that supports it, and an independence argument (or else explicitly demote it to heuristic commentary and remove it from the count of “logically independent constraints”). Do not claim “13 logically independent” constraints unless you actually prove independence in the text.

P1A-E4 – ESSENTIAL  
Section: Abstract, p.1; Sec. II A.2, Fig. 2; Appendix B  
Problem: The mapping from the parity‑odd operator to dark energy, via the scaling ansatz “ρΛ = Ξ MPl⁴ with Ξ ≡ (α/M) MPl⁵ Dinf” and the statement that the relevant on‑shell operator has “off‑shell mass dimension +1 rather than +4,” is not an EFT‑consistent construction. The paper admits this is an ansatz, but nonetheless uses it to derive specific claims (e.g., Ntot ≈ 92, fine‑tuning “reduced” from 10¹²² to 10⁵). EFT consistency and dimensional analysis are load‑bearing for the cosmological‑constant discussion.  
Required fix: Either (a) provide a fully consistent EFT derivation of the dark‑energy term from a dimension‑4 operator (with the correct mass dimension in the Lagrangian and all powers of MPl explicitly accounted for off‑shell), or (b) clearly separate all results that depend on the “mass‑dimension +1” ansatz into a speculative section, refraining from interpreting Ntot ≈ 92 or the “fine‑tuning reduction from 10¹²² to 10⁵” as anything more than a dimensional toy model. State explicitly that PRD‑level conclusions about the cosmological constant cannot be drawn from this ansatz.

P1A-E5 – ESSENTIAL  
Section: Sec. IV B (Route 2), p.12–13; Eq. (14), (15)  
Problem: The dimensionless ratio “Δθ_one‑loop / Δθ_obs” used to argue that Route 2 is suppressed by ~10⁻⁶⁰ is built from a heuristic chain of factors (α_em/4π, H₀/MPl, (α/M)·MPl, β_obs) without a clearly derived underlying one‑loop calculation. The paper itself says “no published calculation currently derives this exact coefficient structure… we adopt [it] strictly as an upper‑bound EFT ansatz.” Using such an ansatz to claim a no‑go at the 60‑order‑of‑magnitude level is not acceptable at PRD standards.  
Required fix: Provide a rigorous one‑loop calculation (or a precise reference) that leads to Eq. (14) with the stated coefficients, and derive Eq. (15) from that expression carefully, including all relevant mass scales. If this is not feasible, significantly soften the conclusion: present Route 2 as “very likely negligible” with an explicit order‑of‑magnitude uncertainty, rather than as a strict amplitude no‑go.

P1A-E6 – ESSENTIAL  
Section: Sec. IV C (Route 3), p.12–13; Eq. (16)  
Problem: Route 3 uses a schematic beta function “dγ/d ln µ = (1/12π²)(N_FL–N_FR) γ + O(γ²)” as an “EFT upper‑bound ansatz,” but the actual perturbative running of γ in the presence of fermions is non‑trivial and has been computed in the literature (e.g., Benedetti & Speziale). The paper then concludes ∆γ/γ ~ 10⁻² and a suppression (∆γ/γ)(H/MPl) ~ 10⁻⁶³ without showing any explicit calculation or citing a precise result.  
Required fix: Either (a) base the running of γ entirely on an explicit calculation such as Benedetti & Speziale and show the steps leading to the claimed amplitude suppression, or (b) clearly demote Route 3 to a qualitative argument about likely smallness, without quantitative 10⁻⁶³ suppression or strong closure language. Do not present Eq. (16) as a sufficient basis for a quantitative no‑go.

P1A-E7 – ESSENTIAL  
Section: Sec. II B, p.7; Eq. (9) and surrounding text  
Problem: The paper uses Ashtekar & Singh’s formula for ρ_crit, states that Ashtekar & Singh quote ρ_crit ≃ 0.41 ρ_Pl at γ=0.2375, then substitutes γ=0.274 to obtain ρ_crit ≃ 0.27 ρ_Pl and quotes a “0.27–0.41 ρ_Pl window” as if it were an LQC‑established range. For PRD, extrapolations beyond the cited paper must be clearly separated from published results. Here they are somewhat blended.  
Required fix: Rewrite this discussion so that the only value attributed to Ashtekar & Singh is ρ_crit ≃ 0.41 ρ_Pl at their γ; present the γ=0.274 number explicitly as your own extrapolation. Do not describe “0.27–0.41 ρ_Pl” as a “window used in LQC”; describe it as the span between the published value and your preferred γ‑extrapolated value.

P1A-E8 – ESSENTIAL  
Section: Sec. IV D (Route 4), p.13–14; Eq. (17) and numeric argument  
Problem: The ALP‑birefringence mapping is used to claim that with α/M ≈ 10⁻²¹ GeV⁻¹ and m_θ ≈ H₀ one can reproduce both β_obs and ρ_Λ, and that for m_θ in [10⁻²², 10⁻¹⁵] eV the resulting ρ_θ “overshoots” ρ_Λ by 22–36 orders of magnitude. This is a sensitive quantitative statement, but the calculation is not shown in full, and the precise assumptions on ρ_θ (e.g. whether it is all of dark energy vs a fraction) and on the background evolution (frozen vs oscillating field) are not clearly delineated.  
Required fix: Provide an explicit derivation of the relation between β, α/M, m_θ and ρ_θ, including the cosmological evolution regime (m_θ ≲ H₀ vs m_θ ≫ H₀), and show numerically how the overshoot factor is obtained over the stated mass range. Clarify under what assumptions of field fraction and initial misalignment the “overshoot” holds. Without this, the claim that Route 4 “relocates the CC problem” rather than solving it is plausible but not quantitatively substantiated.

P1A-E9 – ESSENTIAL  
Section: Sec. X, p.19–20, especially Eq. (23) and footnote 7  
Problem: The central “perturbation‑transparency” result relies on the statement that the Holst dual contraction RH = (1/2) ε^{μνρσ} R_{μνρσ} (Γ̊) vanishes identically when T=0 by the algebraic Bianchi identity R_{μ[νρσ]}=0, even allowing for non‑metricity. This is a load‑bearing claim but only a brief sketch is given; the proof is not fully explicit, and there is a risk of confusion between different index contractions and topological densities.  
Required fix: Provide a rigorous, coordinate‑based proof (or a precise reference) that for an arbitrary torsionless connection (with or without non‑metricity) the single‑curvature contraction ε^{μνρσ}R_{μνρσ} vanishes identically, and that this is distinct from the Pontryagin density. Explicitly show the step from R_{μ[νρσ]}=0 to ε^{μνρσ}R_{μνρσ}=0. Since this underpins the “Holst sector decouples at all perturbation orders” conclusion, it must be ironclad.

P1A-E10 – ESSENTIAL  
Section: Abstract, p.1; Sec. I, Sec. XIII, Sec. XIV D  
Problem: The abstract claims a strong “structural tension” between dark‑energy suppression (requiring N_tot≈92) and the survival of the matter‑bounce f_NL signal at SPHEREx scales. However, the actual derivation of this tension in Sec. XIV D is qualitative, with only rough scale arguments (k_bounce^phys ∼ k_SP q^{N_tot−N_exit}). There is no explicit transfer function calculation, no quantified suppression of f_NL as a function of N_tot−N_exit, and no clear definition of “definitively erased.”  
Required fix: Either (a) present a quantitative calculation of the fate of the matter‑bounce non‑Gaussianity through the bounce, inflation, and reheating (e.g. computing f_NL(k) with a specific transfer function) and then derive a numerical condition on N_tot−N_exit beyond which f_NL at SPHEREx scales falls below detection threshold, or (b) substantially weaken the structural‑tension language (especially in the abstract) to clearly label it as a qualitative expectation, not a proven incompatibility.

P1A-E11 – ESSENTIAL  
Section: Data and Code Availability, p.25; companion references [2,6,23,46]  
Problem: The GitHub repository is cited with a “tree/main/reproducibility” path but no commit hash or archived DOI. The text promises a Zenodo‑archived release “to be prepared,” but for PRD reproducibility requirements, a frozen artifact corresponding to the submitted version should be in place at publication, with a stable identifier.  
Required fix: At minimum, add a precise commit hash for the repository version used in the paper and, preferably, register a Zenodo (or analogous) DOI for a frozen release. Update the Data & Code Availability section to include that hash/DOI so that future readers can exactly reproduce the computations.

P1A-E12 – ESSENTIAL  
Section: Conclusions, p.24–25  
Problem: The paper repeatedly uses strong language such as “channel‑level closure,” “no‑go,” “constrain each of the four routes,” yet a substantial fraction of the arguments rest on phenomenological ansätze and incomplete quantitative work (as noted in earlier findings) plus several “in preparation” companion results. At PRD standards, such strong claims must be supported by fully self‑contained calculations or by already‑published material.  
Required fix: After addressing the earlier ESSENTIAL issues, reassess the overall strength of the claims. If the remaining arguments are still partly heuristic or dependent on unpublished companions, weaken the conclusions accordingly (e.g., “under the specific ansätze explored here, the four routes appear highly constrained”) rather than “closed” or “no‑go.”

P1A-M1 – MAJOR  
Section: Abstract, p.1; Table I, p.4; Table IV, Appendix A  
Problem: The paper quotes several numerical cosmological parameter values (H₀=67.68±1.06 km/s/Mpc, ∆N_eff, σ₈, etc.) as coming from an internal Cobaya MCMC analysis in a companion paper [6] “in preparation.” These numbers are used to claim consistency with ΛCDM and to motivate some of the discussion, but the MCMC setup, priors, and data combinations are not fully described in the present text.  
Required fix: Either (a) provide a concise but sufficient description of the MCMC setup in the present paper (likelihoods, priors, convergence criteria, basic posterior plots) so that the quoted numbers can be assessed independently, or (b) remove the quantitative parameter statements and replace them with qualitative statements referencing Planck 2018 and DESI DR2 results from published sources.

P1A-M2 – MAJOR  
Section: Sec. III A (CMB EB), p.10; Sec. IV D; Appendix C  
Problem: The birefringence section correctly cites Minami & Komatsu and Eskilt & Komatsu, and ACT DR6, but the paper’s own use of β≈0.27° as a “benchmark” is not clearly propagated into a measurable prediction. Specifically, it is not clear whether the author’s model predicts a specific central value for β or simply chooses a point within the current error bars. The text sometimes reads as if β≈0.27° is a prediction, but elsewhere admits it is a consistency check.  
Required fix: Clarify unambiguously that β≈0.27° is not a prediction of ECH but a phenomenological benchmark consistent with WMAP+Planck and ACT, and that any ALP with appropriate coupling would produce a similar value in GR. Make sure this is stated explicitly in the abstract and in Sec. XIII, and avoid any language that could be read as claiming predictive power.

P1A-M3 – MAJOR  
Section: Sec. III B, p.10; Sec. V, p.15  
Problem: The galaxy spin analysis is summarized as “null,” based on an independent ViT‑Small classifier and companion Paper IV . However, no quantitative details (N_gal, sky mask, classifier accuracy, bias tests, or measured dipole amplitude with error bars) are given in this paper. For PRD, even if the main result is theoretical, an observational null that is used as a constraint should be documented more concretely.  
Required fix: Add a short subsection summarizing the key quantitative aspects of the galaxy‑spin analysis: sample size, redshift range, classifier performance, dipole amplitude and error, and how these numbers lead to the claimed null. Provide enough information for a reader to judge the robustness without needing Paper IV.

P1A-M4 – MAJOR  
Section: Multiple (Introduction, Sec. II, Sec. IV, Sec. XII and XIV)  
Problem: The paper is very long (28 pages plus appendices) and covers multiple semi‑independent themes: ECH theory, bounce cosmology, dark energy, cosmic birefringence, galaxy spins, PTAs, and a barrier catalog. For the specific claimed contribution — channel‑level closure of four ECH dark‑energy routes and the perturbation‑transparency result — much of this material is tangential. At PRD, length should be commensurate with the central result.  
Required fix: Consider a substantial tightening: focus the paper on (i) the perturbation‑transparency theorem and (ii) the four‑route closure analysis, moving the extended observational program descriptions (galaxy spins, PTA anomalies, SPHEREx forecast details, and parts of the barrier catalog that are not used in the formal closure) to companion papers. A target length of ≈18–20 pages (including appendices) would be more appropriate.

P1A-M5 – MAJOR  
Section: Sec. IX, Table II, p.17–18  
Problem: Several barriers use strong terms like “Planck suppression,” “ceiling,” and “impossibility,” but the quantitative statements are either absent or explicitly described as ansatz‑level (e.g., Barrier 12’s GW ceiling based on ρ_crit/ρ_Pl). This risks overstating what is actually demonstrated.  
Required fix: For each barrier, clearly distinguish between (i) rigorous derivations, (ii) order‑of‑magnitude estimates, and (iii) heuristic/philosophical comments. Adjust the language in Table II (“Blocked mechanism”) accordingly; for mechanisms blocked only at heuristic level, say “disfavored under assumptions X, Y” rather than “blocked.”

P1A-M6 – MAJOR  
Section: Sec. X G, p.20; Sec. XIII, p.22; Ref.   
Problem: The PTA spectral index “γ_PTA = 2.567 ± 0.382” from a “real‑KDE GPU MCMC, in preparation ” is used to discuss consistency with a matter‑bounce prediction γ_PTA=3.0 at +1.13σ. There is no description of the data set, likelihood, or model used, and no cross‑check against the official NANOGrav analysis.  
Required fix: Either provide a brief but concrete description of the PTA analysis (data release used, model assumptions, how γ_PTA is defined) and show that this is consistent with or an extension of published NANOGrav results, or remove this discussion from the present paper and leave it to the companion PTA paper.

P1A-M7 – MAJOR  
Section: “Companion paper” paragraph in Sec. I, p.4  
Problem: The paper uses internal MCMC results and pipeline validation as support for some claims but emphasizes that they are not yet publicly available and that the present paper does not depend on them for the closure. The paragraph is long and reads like a roadmap of the author’s project rather than content for this paper.  
Required fix: Streamline this paragraph and remove dependence on yet‑unpublished numerical work where it is not strictly necessary. Focus on what is fully contained and justified in this manuscript.

P1A-M8 – MAJOR  
Section: Abstract‑last drift sweep (entire abstract vs body)  
Problem: The abstract’s first sentences strongly emphasize dark‑energy channel closure and the perturbation‑transparency result, then immediately mention two “surviving predictions” (f_NL and β) that are in fact not predictions of ECH but of broader classes. The body clarifies this nuance, but the abstract could mislead a casual reader.  
Required fix: Rephrase the abstract to clearly distinguish between (i) results specific to minimal ECH (channel‑level closure and perturbation transparency under stated assumptions) and (ii) class‑level observables (matter‑bounce f_NL, spectator‑ALP β) that are simply not ruled out. Make sure the abstract does not imply that ECH predicts f_NL or β.

P1A-N1 – MINOR  
Section: Title and first paragraph, p.1  
Problem: The title “Channel‑Level Closure of Four Minimal Einstein–Cartan–Holst Dark‑Energy Routes” is quite assertive given that the closure relies heavily on model‑dependent ansätze and partial arguments. While this is a nuance compared to the ESSENTIAL findings, PRD readers would benefit from slightly more conservative wording.  
Required fix: Consider softening “Closure” to “Constraints on” or “Strong Constraints on,” or adding “under specified assumptions” either in the title or the abstract’s first sentence.

P1A-N2 – MINOR  
Section: Sec. II A.1, Eq. (1), p.5–6; associated footnotes  
Problem: The action is written with a somewhat unusual combination of conventions and a shorthand T^{abc}T_{abc} term that is “not varied independently.” The footnotes attempt to clarify, but the text is hard to parse for readers not deeply familiar with EC/Holst literature.  
Required fix: Recast the action in a more standard modern EC/Holst form (tetrad + spin connection, with an explicit Dirac term) and then explain in a single, concise paragraph how integrating out torsion recovers the Hehl–Datta contact term. Keep only one convention footnote, clearly stating the choice.

P1A-N3 – MINOR  
Section: Eq. (11) and surrounding text, p.8  
Problem: The term “parity‑odd density‑of‑states factor” and the exponent 3/2 in (T_reh/M_GUT)^{3/2} are heuristic. This is noted in the text, but the phrasing may mislead some readers into thinking a partial thermal calculation has been done.  
Required fix: Explicitly state in one sentence that the 3/2 exponent is a dimensional/phase‑space guess, not a result of a full thermal calculation, and that no attempt is made to derive it from first‑principles statistical mechanics.

P1A-N4 – MINOR  
Section: Fig. 2, caption, p.7  
Problem: The caption introduces “D_inf ~ 10⁻¹²¹” and “N_tot ≈ 92 with D_inf ~ 10⁻¹²¹” but does not define D_inf in the figure itself; one has to refer back to Sec. II C.1.  
Required fix: Add a brief parenthetical in the caption defining D_inf as the inflationary dilution factor e^{-3 N_tot} and note that it is part of a phenomenological scaling ansatz.

P1A-N5 – MINOR  
Section: Multiple figures (3, 4, 5, 6)  
Problem: Several figures show percentage deviations, σ contours, and fine‑tuning “scores” without explicit axis units or precise definitions in the caption (e.g. Fig. 5’s “fine‑tuning score” is said to be in “orders of magnitude,” but the axis is not explicitly labeled as log₁₀ of a ratio).  
Required fix: Ensure that every figure axis has a clear label with units and that the caption defines any derived quantity plotted (e.g. explain that the fine‑tuning score is log₁₀(Λ_natural/Λ_observed) or similar).

P1A-N6 – MINOR  
Section: Footnotes referencing earlier draft errors (e.g., footnote 8 in Sec. X, footnote at Eq. (17))  
Problem: Several footnotes describe “earlier versions of this manuscript” and corrections prompted by “external review.” This kind of version‑history language is not standard in a final PRD article and may confuse readers.  
Required fix: Remove explicit references to earlier drafts and external reviews. Instead, simply present the correct derivation and, if necessary, briefly note that a subtlety about X is clarified here.

P1A-N7 – MINOR  
Section: References, pp.27–28  
Problem: A few references appear to be future‑dated or speculative as of the stated manuscript date (e.g., DESI DR2 “2025,” Dehghani et al. “2025,” several “2026” and “2025” arXiv preprints). For PRD, it is acceptable to cite recent preprints, but they must already be on arXiv at submission. You explicitly claim some are “posted concurrently.” This requires verification at acceptance time.  
Required fix: Ensure that each reference listed as arXiv preprint has a valid arXiv identifier and is publicly accessible. Remove or update any placeholder or “to appear” entries, and do not include references that are not yet publicly posted.

P1A-N8 – MINOR  
Section: Miscellaneous wording (e.g., “fine‑tuning score,” “cosmological‑constant hierarchy,” “relocated the CC problem”)  
Problem: Some phrases are informal and could be misinterpreted as editorializing rather than precise scientific statements.  
Required fix: Where possible, replace colloquial expressions with quantitative definitions (e.g., define a “fine‑tuning score” as a specific logarithmic ratio). Keep commentary about “relocating the problem” but anchor it to a specific equation.

P1A-N9 – NIT  
Section: Typographical / stylistic issues (multiple pages)  
Problem: A few minor typos (e.g., inconsistent spacing in “γBI 2 /(γBI+1)·8πG”, occasional missing or extra spaces before parentheses) and some long sentences spanning several lines without breaks.  
Required fix: Run a thorough language and typesetting pass to clean up minor typographical issues and improve readability (especially by breaking very long sentences).

P1A-N10 – NIT  
Section: Footnotes a and numerical superscripts (p.1 and elsewhere)  
Problem: The superscript “a” after “Sec. X).a” and various footnote markers are easy to miss in the typeset PDF and can be confused with exponent notation.  
Required fix: Ensure that footnote markers are clearly differentiated (e.g. by using symbols or distinct formatting) and that footnote text appears on the same page as the marker where possible.

## Summary recommendation

REJECT

The manuscript contains interesting and ambitious ideas, but the central “channel‑level closure” and “no‑go” claims rely heavily on phenomenological ansätze, partially specified EFT operators with inconsistent off‑shell dimensions, and quantitative arguments that are not fully derived. Several key constraints (Routes 2 and 3, multiple barriers, the dark‑energy suppression vs f_NL tension) are asserted with strong numerical suppression factors without complete calculations, and many load‑bearing results depend on companion papers that are “in preparation.” At PRD standards, a paper making such broad structural claims about Einstein–Cartan–Holst cosmology must be fully self‑contained, with rigorous derivations for each no‑go step and reproducible numerical analyses. Addressing the ESSENTIAL issues would require substantial re‑derivation and restructuring, better suited to a fresh submission once the technical foundations and companion results are fully in place.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E13 – ESSENTIAL  
Section: Sec. IV A, p.11 (Route 1 amplitude estimate)  
Problem: The NJL energy-density estimate converts a physical baryon density \(n_\psi \sim 10^2\ \mathrm{cm}^{-3}\) into natural units as \(n_\psi \approx 7.66\times 10^{-13}\ \mathrm{eV}^3\), using \(1\ \mathrm{cm}^{-3} = (1.973\times 10^{-5}\ \mathrm{eV})^3 \approx 7.66\times 10^{-15}\ \mathrm{eV}^3\).[paper text] This conversion is off by many orders of magnitude: \(1\ \mathrm{cm}^{-1} = 1/(1.973\times 10^{-5}\ \mathrm{eV}^{-1}) \approx 5.07\times 10^4\ \mathrm{eV}\), so \(1\ \mathrm{cm}^{-3} \approx (5.07\times 10^4)^3 \approx 1.3\times 10^{14}\ \mathrm{eV}^3\). For \(n_\psi \sim 10^2\ \mathrm{cm}^{-3}\), the correct order is \(n_\psi \sim 10^{16}\ \mathrm{eV}^3\), not \(10^{-13}\ \mathrm{eV}^3\). This makes the quoted \(\rho_{\mathrm{NJL}} \sim 4\times 10^{-81}\ \mathrm{eV}^4 \sim 4\times 10^{-69}\rho_\Lambda\) numerically wrong by \(\sim 10^{96}\) in \(\rho\), even though the qualitative “far below \(\rho_\Lambda\)” statement is still true.  
Required fix: Recompute \(n_\psi\) in eV units and the resulting \(\rho_{\mathrm{NJL}}\) carefully, show the correct orders of magnitude, and update the numerical comparison to \(\rho_\Lambda\). Make clear that the closure of Route 1 does not rely on the earlier erroneous conversion.

P1A-E14 – ESSENTIAL  
Section: Eq. (18), Sec. IX A, p.16 (mass–coupling lock)  
Problem: The displayed scaling \(g_{\text{eff}} \sim 1/\sqrt{M_{\rm Pl}|t_3|} \sim H_0/M_{\rm Pl} \sim 10^{-61}\) is dimensionally inconsistent as written and the intermediate step is not justified.[paper text] In PGT, \(t_3\) is a coupling in the Lagrangian; taking \(|t_3|\sim m_T^{-1}\) and then writing \(g_{\text{eff}}\sim 1/\sqrt{M_{\rm Pl}|t_3|}\) mixes mass-dimensions in a way that is not shown to give a dimensionless coupling. The claimed equality to \(H_0/M_{\rm Pl}\) is presented as a “scaling ansatz” but no explicit algebra is given, and the dimensions do not obviously match.  
Required fix: Write down the underlying PGT Lagrangian terms, assign mass dimensions to \(t_3\), \(m_T\), and \(g_{\text{eff}}\), and show explicitly how a **dimensionless** effective coupling emerges and under what assumptions it scales like \(H_0/M_{\rm Pl}\). If a dimensionless \(g_{\text{eff}}\) cannot be obtained with the given ansatz, either correct the formula or demote Eq. (18) to a qualitative statement without the specific \(10^{-61}\) numerical claim.

P1A-E15 – ESSENTIAL  
Section: Sec. IX L, Eq. (20), p.17–18 (vacuum amplification ceiling)  
Problem: The ceiling \(\Omega^{\rm ECH}_{\rm GW}|_{\rm bounce}\lesssim (\rho_{\rm crit}/\rho_{\rm Pl})^2\simeq 0.07–0.17\) is introduced as an “order-of-magnitude ceiling ansatz” without derivation, but it is then used as if it were a quantitative bound, and the square on \(\rho_{\rm crit}/\rho_{\rm Pl}\) is not dimensionally or physically motivated.[paper text] In particular, if \(\rho_{\rm crit}/\rho_{\rm Pl}\sim\mathcal{O}(0.3)\), a ceiling linear in that ratio would also be \(\mathcal{O}(0.3)\); squaring it materially tightens the ceiling but no argument is given for this choice over other scalings.  
Required fix: Either (a) derive Eq. (20) from an explicit bounce–GW calculation (e.g. starting from the stress–energy of tensor modes near \(\rho_{\rm crit}\) and showing why the ceiling scales as the *square* of \(\rho_{\rm crit}/\rho_{\rm Pl}\)), or (b) clearly label Eq. (20) as a heuristic, non-rigorous upper bound and avoid using it in any argument that requires a quantitatively reliable ceiling. If (b) is chosen, soften Barrier 12 correspondingly so it is clearly not a quantitative no-go.

P1A-M9 – MAJOR  
Section: Sec. IV D, Eq. (17) and following ALP numerics, p.13–14  
Problem: The mapping from \(\beta\) to \(\rho_\theta\) is used to claim “\(\rho_\theta \approx 1.6\times 10^{-10}\ \mathrm{eV}^4 \approx 6\rho_\Lambda\)” at \(m_\theta\simeq H_0\), and 22–36 orders-of-magnitude overshoots at \(m_\theta\in[10^{-22},10^{-15}]\ \mathrm{eV}\).[paper text] However, the intermediate arithmetic is not shown. In particular, the numerical value of \(H_0\) in eV, the precise \(\beta\) used in radians, and the combination \((\alpha/M)^{-2}\) are only given approximately, so it is not transparent that the factor of ~6 and the 22/36 OOM bounds follow. Since these numbers underpin the “relocates the CC problem” argument, opaque arithmetic undercuts the quantitative credibility.  
Required fix: Explicitly compute \(\rho_\theta = 2m_\theta^2 \beta^2 / (\alpha/M)^2\) in the text or an appendix: state the numerical values for \(H_0\), \(\beta\) and \(\alpha/M\) used, show the intermediate steps, and then show how the ~6, 22 and 36 OOM factors are obtained. If the result is sensitive at the factor-of-few level to these choices, state the associated uncertainty and adjust the “22–36 OOM” language to a clearly approximate range.

P1A-M10 – MAJOR  
Section: Sec. VII & Fig. 4 caption, p.15–16; Table I footnote b  
Problem: The quoted SPHEREx significance range “2.6–5σ realistic” is built from several nested assumptions (Fisher σ(fNL)=0.7, template-overlap factor r≈0.84, GR-projection and photo-z degradation) and a one-sided detection of \(f_{\rm NL}=-35/8\).[paper text] However, the arithmetic behind the 2.6 and 5 endpoints is not transparently reconstructed anywhere—e.g. whether 2.6σ corresponds to |fNL|/σ=4.375/1.7, or some other combination, is not shown—and different sentences appear to mix the “ideal” and “degraded” σ values in slightly different ways. This makes it hard for a reader to verify the quoted 2.6–5σ range directly from the described inputs.  
Required fix: Add a compact explicit calculation (one or two lines in Sec. VII or the caption) that shows how you go from σ(fNL)=0.7 (ideal) and σ(fNL)≈1.0 (after systematics) to the 2.6–5σ range, including the effect of r≈0.84. Make sure the same combination is used consistently wherever the 2.6–5σ range is quoted.

P1A-M11 – MAJOR  
Section: Sec. III A, Eq. (12); Sec. VII (falsifiability)  
Problem: Eq. (12) gives the small-angle EB relation \(C_\ell^{EB}\approx 2\beta\,C_\ell^{EE}-C_\ell^{BB}\), but the text then uses the measured β to motivate a falsifiability program without ever quantifying how large an EB signal would follow for the chosen benchmark β≈0.27° in terms of \(C_\ell^{EB}\) compared to experimental noise and systematics.[paper text] This is a subtle but common “hedge”: statements about “EB pattern consistent with β” are made qualitatively, but the actual EB amplitude and its S/N in current or future experiments are not given.  
Required fix: Provide at least one explicit numerical estimate of the expected \(C_\ell^{EB}\) amplitude (or an integrated S/N) for β≈0.27° using a representative \(C_\ell^{EE}\) at the scales of interest, and compare that to current WMAP+Planck and future LiteBIRD sensitivities. This will make the “falsifiability” claims quantitatively transparent.

P1A-M12 – MAJOR  
Section: Sec. X G (PTA), p.20; Fig. 1 caption; Table IV row for γPTA  
Problem: The text now clearly labels γPTA=2.567±0.382 as coming from a “real-KDE GPU MCMC, in preparation ”, but it also says “the matter-bounce prediction γPTA=3.0 sits at +1.13σ above the posterior mean, consistent with the data”.[paper text] There is still no formula for how γPTA is defined, no frequency range or noise model, and no explicit comparison to the official NANOGrav spectral-index constraints, which makes the +1.13σ statement unverifiable. This falls under “unquantified hedges” and “unsupported novelty” in PTA space.  
Required fix: Either (a) give a minimal but precise definition of γPTA (e.g. \(S_h(f)\propto f^{-\gamma_{\rm PTA}}\) over what band), state which public PTA dataset and likelihood are used, and show that your γPTA posterior is consistent with (or a simple reparameterization of) the published NANOGrav results; or (b) remove the numerical +1.13σ distance and soften to a qualitative statement like “a power-law index near 3 remains allowed by current PTA constraints” until the companion paper is published.

P1A-M13 – MAJOR  
Section: Sec. XIV D, “Structural Tension”  
Problem: The “definitively erased” language for the matter-bounce \(f_{\rm NL}\) relies on a scale-mapping argument \(k_{\rm bounce}^{\rm phys}\sim k_{\rm SPHEREx}^{\rm phys} e^{N_{\rm tot}-N_{\rm exit}}\sim e^{32} k_{\rm SPHEREx}^{\rm phys}\) and the assertion that such modes lie “deep inside the inflationary subhorizon regime carrying purely vacuum-inflationary fluctuations”.[paper text] However, there is no quantitative calculation of how the mode functions or \(f_{\rm NL}(k)\) are suppressed as a function of this displacement; even the definition of “deep” (e.g. \(k/(aH)\gtrsim 10, 10^3,\dots\)) is not specified. This leaves “definitively erased” as a qualitative hedge, not a demonstrable bound.  
Required fix: Either (a) quantify the suppression: choose a simple transfer model, compute \(f_{\rm NL}(k)\) as a function of \(N_{\rm tot}-N_{\rm exit}\), and show at what value the SPHEREx-band \(f_{\rm NL}\) drops below, say, 1σ of the forecast sensitivity; or (b) explicitly downgrade the language in Sec. XIV D from “definitively erased” to “expected to be strongly suppressed” and state that a rigorous transfer-function calculation is left to future work.

P1A-N5 – MINOR  
Section: Abstract vs. Sec. IX/Table II; “13 logically-independent barriers”  
Problem: The abstract and several early sections still state “13 logically-independent barriers (14 historical catalog entries with B8 subsumed by B14)” as if logical independence had been demonstrated, but Sec. IX itself acknowledges that some barriers (notably 5, 6, 7, 9, 13) are partly heuristic and that B8 and B14 are not independent.[paper text] There is no explicit independence proof (e.g. no argument that, say, “scale separation” cannot be derived from “mass–coupling lock” plus “Liouville conservation”, etc.). This makes the “logically-independent” descriptor stronger than the actual content supports.  
Required fix: Either provide a short independence discussion (even at a schematic level) showing that each of the 13 is not a logical consequence of the others under the stated assumptions, or soften the phrasing throughout to “13 mechanism-class constraints (14 catalog entries…)” without the “logically-independent” qualifier.

P1A-N6 – MINOR  
Section: Multiple places where σ-values from different nulls are juxtaposed  
Examples:  
– Fig. 5 caption: “fine-tuning-score comparison… (σ values across panels use different null procedures; see text).”[paper text]  
– Fig. 6 caption: “2.6–5σ projection” for SPHEREx and “σ(β)≈0.03°” for LiteBIRD, plotted together.[paper text]  
Problem: You have added local caveats in some places (e.g. in the abstract for the birefringence σ-values; in Fig. 5’s caption). However, Fig. 4, Fig. 6, and the surrounding discussion still present joint “2.6–5σ” and “σ(β)=0.03°” significance bands in a way that visually encourages cross-comparison, while the “different null” caveat is easy to miss and not always repeated in the text around each figure. This partially addresses, but does not fully resolve, the comparability issue.  
Required fix: For every figure or sentence that places two or more σ-based significances from different null procedures side by side (SPHEREx Fisher σ, WMAP+Planck β significance, ACT β significance, LiteBIRD σ(β), OOM “fine-tuning σ” in Fig. 5), ensure there is an explicit local sentence stating that these σ-values are based on different nulls and must *not* be interpreted as directly comparable. If necessary, adjust y-axis labels or legends so they do not visually suggest direct cross-comparison of σ across panels.

P1A-N7 – MINOR  
Section: Sec. II C 1, Eq. (11) and “Reheating thermal-reset barrier” paragraph  
Problem: The paper states that \(D_{\rm inf} = \exp[-3N_{\rm tot}]\times (T_{\rm reh}/M_{\rm GUT})^{3/2}\) with a discussion that the \((T_{\rm reh}/M_{\rm GUT})^{3/2}\) factor is an “order-of-magnitude” density-of-states ansatz, not a derived thermal result, and that the “fine-tuning reduction” from \(10^{122}\) to \(10^5\) is just a reparameterization.[paper text] However, the arithmetic linking \(N_{\rm tot}\approx 92\), \(D_{\rm inf}\sim10^{-121}\), and the residual \(10^5\) “score” is only sketched, not explicitly shown, which can make it hard for a reader to reconstruct how 4 extra e-folds map to a factor of \(10^5\).  
Required fix: Add a single explicit line (either here or in Appendix B) showing the mapping \(D_{\rm inf}\propto e^{-3N_{\rm tot}}\Rightarrow \Delta\log_{10}(\mathrm{fine\text{-}tuning})\approx (3\Delta N_{\rm tot})/\ln 10\), and then plug \(\Delta N_{\rm tot}\approx 4\) to get \(\sim 5\) orders of magnitude. This will make clear that the “\(10^5\)” is a simple reparameterization choice and not an independently derived physical quantity.

If you resolve these new issues along with the earlier ones, the manuscript’s quantitative and logical foundations will be substantially clearer and more in line with PRD’s expectations for rigor.