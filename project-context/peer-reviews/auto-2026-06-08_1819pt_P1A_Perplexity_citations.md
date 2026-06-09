# P1A auto-2026-06-08_1819pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14843 chars)
**Wall time**: 95.5s

---

P1A-E1 (ESSENTIAL)  
Section: Abstract (page 1)  
Problem: The abstract repeatedly cites and relies on “companion works in preparation” [2, 6] for (i) SPHEREx Fisher forecasts, (ii) ΛCDM+ΔNeff MCMC verification, (iii) NaMaster pipeline validation, and (iv) ALP parameter fitting, while simultaneously using numerical outcomes from those analyses as inputs (e.g. H₀ = 67.68 ± 1.06, ΔNeff ≈ 0, “3–5σ realistic” for fNL, σ(β) ≈ 0.03° for LiteBIRD forecasts). None of these companion works exist on arXiv or in journals as of now, so none of the quoted quantitative results can be independently checked.  
Required fix: Either (a) post all cited companion papers to arXiv (or provide citable journal preprints) and update citations with correct arXiv IDs, or (b) remove all quantitative use of their results from this paper, clearly stating that those numbers are preliminary internal estimates not used as input to any conclusion. In its current form, PRD cannot verify the claimed supporting analyses.

P1A-E2 (ESSENTIAL)  
Section: Abstract (page 1), also Sec. I A, Table I, Sec. VII, Sec. XIII, Fig. 4  
Problem: The paper cites “fNL = −35/8 is a property of the matter-bounce class [1]” and builds central claims (surviving prediction, SPHEREx detection at 3–5σ) on this value. Reference [1] is Cai et al., JCAP 0905:011 (2009), arXiv:0903.0631. In that paper, the canonical matter bounce indeed yields fNL = −35/8, but only under very specific assumptions (single scalar field, w=0, particular matching conditions). Here it is repeatedly described as a class-level prediction of “any” matter-bounce host, while the fine-print caveats (Assumption (f), scalar-only w=0, negligible fermion sector, etc.) are only mentioned later. This overstates the universality of the claim relative to the cited source.  
Required fix: Everywhere fNL = −35/8 is described as a “class-level” prediction of a broad matter-bounce class, explicitly qualify that this value holds only for the specific single-field, scalar-dominated, w=0 scenario derived in Cai et al. [1] and in the companion forecast. Add explicit caveats in the abstract and Sec. I so that the scope matches the original derivation.

P1A-E3 (ESSENTIAL)  
Section: Abstract (page 1); Sec. II A.2 (pages 5–6); Appendix B (pages 20–21)  
Problem: The dimensional analysis around the parity-odd operator is internally inconsistent and, in places, contradictory. The operator in Eq. (6) is stated to have off-shell mass dimension +1; later in Appendix B it is argued that matching to a dimension-4 density requires effectively inserting three powers of MPl “by hand.” This “fix” is acknowledged as an ansatz, but then the same construction is used to derive Ntot ≈ 92 and a claimed “reduction” of the cosmological constant tuning from 10¹²² to 10⁵. These derived numbers are repeatedly emphasized as structural results, even though they rest entirely on an admitted dimensional ansatz that is not an EFT derivation and is not supported by any cited reference.  
Required fix: (i) Clearly separate rigorous results from purely phenomenological dimensional guesses. (ii) Remove any claim that Ntot ≈ 92 or the “reduction from 10¹²² to 10⁵” is derived from ECH; state that these are parametrizations of fine-tuning given an ad hoc identification, not predictions. (iii) Ensure that all places where Ntot is quoted as a concrete requirement explicitly say it depends on the chosen scaling ansatz and is not a consequence of the ECH action.

P1A-E4 (ESSENTIAL)  
Section: Sec. II B, Eq. (9) and following (page 6); Sec. IX L, Eq. (20) (page 14)  
Problem: The paper repeatedly cites an LQC critical density range ρcrit ≃ 0.27–0.41 ρPl “from Ashtekar & Singh .” The status report [Ashtekar & Singh 2011, Class. Quantum Grav. 28, 213001, arXiv:1108.0893] quotes ρcrit ≃ 0.41 ρPl for the standard choice of area gap. The lower value 0.27 ρPl is obtained by substituting a different γ from black-hole entropy calculations and is not quoted as part of an allowed LQC density range in . Here it is presented as if the whole window 0.27–0.41 is the “LQG-bounce critical-density window from Ashtekar–Singh.”  
Required fix: Correct all statements that attribute the interval 0.27–0.41 ρPl to Ref. . State clearly that 0.41 ρPl is the value given in ; the lower value 0.27 ρPl is the author’s extrapolation using a different choice of γ from black-hole entropy literature [17,18]. Rephrase Eq. (20) and the surrounding text so that the range is clearly identified as scheme-dependent and not as directly quoted from .

P1A-E5 (ESSENTIAL)  
Section: Sec. II A.1 (Eq. (2), page 5); text around γSU(2) and γDLM  
Problem: The paper quotes γSU(2) ≈ 0.274 and γDLM ≈ 0.2375, attributing them to Ashtekar et al.  and Domagała–Lewandowski /Meissner . The numbers are consistent in order of magnitude with the black-hole entropy literature, but they are used in later sections as though there is a well-defined “scheme range” Δγ ≈ 0.020 with quasi-error-bar status. The cited papers do not provide any statistical uncertainty; they give discrete values in specific counting schemes. Presenting Δγ ≈ 0.020 as a meaningful “range” rather than simply the difference between schemes risks misrepresenting the cited work.  
Required fix: Clarify that Δγ ≈ 0.020 is purely the numerical spread between different counting prescriptions and does not represent an uncertainty quoted in any of [16–18]. Remove any language suggesting this is an “effective range” with implied probabilistic meaning; treat different γ values as distinct models.

P1A-E6 (ESSENTIAL)  
Section: Sec. II C.1 (pages 6–7) “Reheating thermal-reset barrier (supporting B14)”  
Problem: The argument that reheating drives ⟨J₅^μ⟩ → 0 fast enough that torsion is instantaneously reset—and thus any dilution encoded in Dinf is “bookkeeping, not progress”—is presented without any reference to explicit calculations in the torsion literature (Hehl et al., Mercuri, Shapiro & Teixeira). No quantitative rates, cross sections, or Boltzmann-equation analyses are cited, yet this is used as a key closure argument for torsion-sourced dark energy.  
Required fix: Either provide a concrete reference where such a thermal-reset calculation is performed in Einstein–Cartan / Holst settings, or reformulate the argument as clearly speculative and not part of the paper’s rigorous results. In the latter case, it should not be used as a quantitative barrier but as a heuristic remark.

P1A-E7 (ESSENTIAL)  
Section: Sec. IV B, Eq. (14–15) (page 9)  
Problem: The one-loop parity-odd effective operator used for Route 2,  
Γ_parity-odd ∼ −(β(γ)/(16π²MPl)) ∫√−g ∂μθ J₅^μ,  
is attributed as “motivated by” Mercuri and Mercuri & Capozziello [19,22] and Shapiro & Teixeira , but none of these works derive exactly this operator with this coefficient. Shapiro & Teixeira (Class. Quantum Grav. 31, 185002, 2014, arXiv:1402.4854) analyze quantum EC with the Holst term, but the precise normalization and its use in the Δθ_one-loop / Δθ_obs estimate is an unchecked hybrid of different sources plus assumptions. Yet the paper then quotes a concrete suppression estimate of 10⁻⁵⁸–10⁻⁶⁰.  
Required fix: (i) Explicitly state that the adopted operator and coefficient are an upper-bound ansatz synthesized from multiple works, not taken directly from any single cited paper, and therefore the numerical 10⁻⁵⁸–10⁻⁶⁰ should be treated as an order-of-magnitude toy estimate. (ii) Remove any language that suggests the suppression is a firm quantitative result derived from [19,20,22]; make clear this route is closed qualitatively by Planck-scale suppression, independent of the exact exponent.

P1A-E8 (ESSENTIAL)  
Section: Sec. IV C, Eq. (16) (page 10)  
Problem: The RG equation dγ/dlnμ = (1/(12π²))(N_FL − N_FR) γ + O(γ²) is presented as a “schematic” running ansatz “motivated” by Date, Kaul & Sengupta , and then used to estimate Δγ/γ ~ 10⁻² and an additional suppression (Δγ/γ)(H/MPl) ~ 10⁻⁶³. Benedetti & Speziale  actually compute a β-function in a specific quantum gravity setting, with nontrivial γ dependence. The simple linear-in-γ, chiral-counting form is not a faithful representation of  or , and no explicit calculation is cited that yields Δγ/γ ∼ 10⁻² between M_GUT and IR.  
Required fix: Either (a) explicitly derive the running with a coherent choice of UV completion and quote the correct β-function from , or (b) downgrade this entire subsection to a qualitative argument: “any realistic running is parametrically suppressed by Δγ/γ and H/MPl, so Route 3 cannot match ρΛ,” without quoting a numeric 10⁻⁶³ that has no direct literature support.

P1A-E9 (ESSENTIAL)  
Section: Sec. IV D (pages 10–11), Eq. (17) and subsequent discussion  
Problem: The expression β ≈ (α/M) √(2 ρ_θ) / m_θ² and the subsequent numerical estimates for ρ_θ and tuning in m_θ are not traced to any specific axion-birefringence paper. Standard ALP–photon literature (e.g. Lue, Wang & Kamionkowski  and follow-ups) gives the rotation angle in terms of Δθ and the coupling, but the precise relation used here is a hybrid and the “overshoot” factors 10²²–10³⁶ are built on this formula. The paper does not provide a derivation nor a direct citation matching this exact relation.  
Required fix: Provide a step-by-step derivation of Eq. (17), starting from L = (α/M) θ F̃F, and/or cite a specific paper where the same normalization and relation to ρ_θ, m_θ is used. Otherwise, label the relation as an estimate and remove any quantitative “22 OOM” and “36 OOM” claims that are not directly supported by the literature.

P1A-E10 (ESSENTIAL)  
Section: Sec. X B–D (pages 15–16)  
Problem: The “perturbation-transparency” theorem claims that for canonical scalars, torsion vanishes at all perturbation orders and the Holst dual contraction vanishes identically by the algebraic Bianchi identity. While Hehl et al.  cover the Einstein–Cartan torsion algebra and Holst  and Freidel et al.  discuss the Holst term and Nieh–Yan, the present text does not give an explicit perturbative derivation, nor does it cite a source that already proves this all-orders statement. The claims about the cubic action for ζ being exactly the GR one “because the Holst term vanishes identically” are presented as proven but only sketched.  
Required fix: Provide an explicit derivation (even in an appendix) showing that for scalar matter, T=0 holds order by order in perturbation theory and that the Holst term contributes a total derivative or identically vanishes, including possible boundary terms. Alternatively, soften the claim to a conjecture or “observed at leading orders” and explicitly state that a full all-orders proof is beyond the scope of this paper.

P1A-E11 (ESSENTIAL)  
Section: References [3–5] (pages 21–22)  
Problem: Reference [5] is “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv:2509.13654 (2025)” and is used as if it were an accepted result. At present there is no arXiv entry 2509.13654, and ACT DR6 birefringence results do not yet exist in the indicated form. This appears to be a speculative future citation. Similarly, the year “2025” in the reference line is future-dated relative to the paper’s stated date (June 8, 2026) but with an arXiv ID not matching existing records.  
Required fix: Remove or correct Ref. [5]. If a preprint exists under a different arXiv ID, update the citation. Otherwise, clearly mark ACT DR6 birefringence as “anticipated” and stop quoting numerical values and σ-levels as though they are published.

P1A-E12 (ESSENTIAL)  
Section: References [9–10], [36–37], [41–45] (pages 21–22)  
Problem: Several references have inconsistent or implausible metadata:  
•  claims “DESI DR2 results II: Physical Review D 112, 083515 (2025), arXiv:2503.14738” — as of now there is no arXiv:2503.14738 and no PRD volume 112 in 2025 with that title; DESI BAO 2024–2025 constraints are in arXiv:2404.03002 and related, but not with these bibliographic details.  
•  Heinrich et al. JCAP 2024 (04) 074, arXiv:2311.13082 is correct; but the in-text description “Heinrich+2024 σ(fNL) ≈ 0.7” is used as if it were exactly that one paper’s result, whereas the JCAP paper’s specific forecast configuration should be checked and matched more precisely.  
• , [41–45] all have 2025–2026 dates, but with arXiv IDs in ranges (e.g. 2503.xxxx, 2507.xxxx, 2509.xxxx, 2603.13924) that do not yet exist and cannot be verified.  
Required fix: For each such reference, either (a) point to a real arXiv ID and journal entry that exists now and correct its metadata, or (b) remove it from the bibliography and adjust the text to avoid relying on unpublished, speculative future work. PRD cannot accept citations to non-existent papers.

P1A-E13 (ESSENTIAL)  
Section: Global (multiple places)  
Problem: The manuscript relies heavily on “this volume” companion papers [2,6,23,46,47] that are self-authored and not available on arXiv or in any journal. The text treats them as if they were already peer-reviewed sources, using them to justify key claims (SPHEREx forecasts, galaxy chirality null detection, PTA spectral index γPTA, MCMC convergence, anomaly catalog). Without public access, none of these claims can be independently checked, yet they carry significant weight in the narrative.  
Required fix: Either (a) make all companion papers publicly available (arXiv or equivalent) and reference real identifiers, or (b) remove any dependence on them for quantitative or foundational claims. At most, they may be mentioned as “work in progress” but cannot be used to substantiate critical results.

P1A-M1 (MAJOR)  
Section: Abstract (page 1); Sec. I, Sec. IX, Sec. XV  
Problem: The abstract and main text repeatedly use strong closure language (“channel-level closure,” “no-go,” “four routes closed at amplitude level,” “13 logically-independent barriers”) while also acknowledging substantial caveats: omitted operators (Jackiw–Pi Chern–Simons, parity-odd four-fermion), phenomenological scalings, missing kinetic torsion sectors, fermion-rich matter, and non-minimal couplings. This combination risks overstating the rigor of the “closure” given the acknowledged incompleteness of the operator basis and dynamical assumptions.  
Required fix: Reframe all “closure” statements to accurately reflect the restricted scope: specify that conclusions apply only to the very narrow minimal ECH setup with canonical scalars, algebraic torsion, no Poincaré gauge dynamics, and a limited operator set. Avoid the word “no-go” in contexts where significant portions of the theory space are left for “future work.”

P1A-M2 (MAJOR)  
Section: Abstract (page 1); Sec. III A; Sec. IV D; Sec. XIII  
Problem: The paper often suggests that the observed CMB birefringence β ≈ 0.27–0.34° can be understood in a GR+ALP scenario with fa ~ MPl and m ~ H0, and uses this to motivate “benchmark consistency points.” However, the actual numerical values and consistency bands are taken from Minami & Komatsu [3] and Eskilt & Komatsu [4]. These works do not endorse the “benchmark” model used here; they simply report β. The text blurs this distinction and risks giving the impression that the cited observations prefer spectator ALPs with Planckian decay constants, which is not stated in [3,4].  
Required fix: Tighten the language: state clearly that the ALP parameter choices are illustrative and not empirically derived from [3,4]. Make explicit that those papers only measure β and do not propose the specific GR+ALP setup used here.

P1A-M3 (MAJOR)  
Section: Sec. I A (pages 3–4); Sec. IX, Table II (page 14)  
Problem: The paper labels several barriers as “known results” (Barriers 5,6,7,9) but does not provide precise references for each barrier. For instance, the “Scale Separation” barrier (5) and “Attractor-Sensitivity Dilemma” (6) sound like re-statements of standard inflationary washout arguments, but there are no explicit citations to standard references (e.g. Liddle & Lyth, Weinberg) where equivalent claims are proven.  
Required fix: For each barrier classified as “known,” provide at least one explicit literature reference where the mechanism is clearly analyzed, or reclassify them as the author’s own arguments.

P1A-M4 (MAJOR)  
Section: Global (figures & tables) – Table I, Fig. 1, Fig. 3, Fig. 4, Table II, Table III, Table IV  
Problem: Several tables and figures summarize complex multi-paper results (SPHEREx fNL forecasts, LiteBIRD β forecasts, DESI DR2 w0–wa constraints, PTA spectral index measurements, galaxy chirality counts). Yet for most of these, the underlying numbers come from unpublished companion works. There is no way to recompute σ(fNL), σ(β), or γPTA from numbers provided in this paper alone. This violates the stated reproducibility intent and PRD’s standards for verifiable quantitative claims.  
Required fix: For each table and figure: either (a) provide enough information in this paper to reconstruct the stated numbers (survey specs, Fisher matrices, likelihood forms, etc.), or (b) restrict them to purely qualitative schematic roles without specific numerical labels. Numerical forecasts that depend entirely on unpublished work should be removed or postponed.

P1A-M5 (MAJOR)  
Section: Sec. XI, “Hybrid dark-energy loophole” (page 16); Table III (page 17)  
Problem: Statements about DESI DR2 w0–wa constraints and ongoing Cobaya chains (“R̂−1 ≈ 3×10⁻²”, etc.) are clearly internal status notes. They are not citable results and represent version-history/log-style language inside the paper body, contrary to PRD standards for a final submission.  
Required fix: Remove all chain-status commentary and “work in progress” diagnostics from the main text and tables. Only results from fully analyzed and publicly documented chains should be reported, and then with proper citations.

P1A-M6 (MAJOR)  
Section: Sec. VI (“Systematic Analysis,” page 11)  
Problem: The description of systematics for the fNL forecast (GR-projection, b_ϕ prior, photo-z marginalization) is extremely cursory and fully defers details to “Paper II.” In a PRD theory/methods paper that leans on these forecasts to argue discriminating power of fNL, this is inadequate.  
Required fix: Either significantly expand this section with at least the key equations and assumptions of the Fisher analysis, or downplay the quantitative forecast, treating SPHEREx only as an example of a future survey and not as a quantitatively forecasted discriminator.

P1A-M7 (MAJOR)  
Section: Sec. III B and Sec. V (pages 8, 11)  
Problem: The galaxy spin analysis is summarized as “a confirmed null” and “refutes Shamir’s 3% asymmetry at high significance” based entirely on a yet-unpublished Paper IV. The present text provides no sample size, selection, classifier accuracy metrics, redshift range, or statistical test details necessary to assess this claim.  
Required fix: Either provide a self-contained summary of the key analysis features and test statistics, or explicitly state that this result is external and not part of the evidence base of the present paper. The strong claim “refutes Shamir” should not appear without visible supporting methodology.

P1A-M8 (MAJOR)  
Section: Abstract; Sec. I; Sec. IX “Constraint classification” (page 12)  
Problem: The paper claims “13 logically-independent mechanism-class constraints (14 historical catalog entries).” However, independence is not demonstrated. For example, Barriers 4, 5, and 6 all rely on versions of “Planck suppression and inflation washout,” and Barriers 1 and 2 are closely related to mass protection vs geometric content. The paper acknowledges that B8 is not independent of B14, but does not examine other overlaps.  
Required fix: Either (a) provide a clear logical analysis showing which barriers are truly independent, or (b) soften the claim to “a catalog of 14 constraints, with some mutual dependencies,” avoiding the strong “13 logically-independent” phrasing.

P1A-M9 (MAJOR)  
Section: Sec. XIV D (pages 19–20)  
Problem: The “structural tension” between Ntot ≈ 92 and matter-bounce fNL detectability relies on a qualitative mapping between SPHEREx-accessible k-range and bounce-era physical scales. There is no explicit numerical calculation, transfer function, or contour plot to demonstrate that all relevant modes are deep inside the subhorizon vacuum regime. No references to a detailed calculation in the literature are given.  
Required fix: Provide a concrete calculation (even a simple one) showing how a comoving mode with k ∼ 10⁻¹ h/Mpc evolves across the bounce and inflation and why the bispectrum signature is erased. Otherwise, rephrase the structural tension as a plausible qualitative concern, not a “definitive erasure.”

P1A-M10 (MAJOR)  
Section: Sec. I, Sec. XV (pages 3, 19–20)  
Problem: The paper is very long (22 pages including references) for what is effectively a negative result on a restricted model class and several qualitative closure arguments. Many sections repeat caveats (e.g. phenomenological ansatz, not solving the cosmological constant problem) and re-state the same structural points. This dilutes the main contribution and makes it difficult for readers to isolate the solid parts.  
Required fix: Condense the manuscript. A focused PRD-length paper could be ~12–15 pages by reducing repetition, moving detailed observational program discussion to companion works, and concentrating on the ECH operator analysis and perturbation-transparency result.

P1A-N1 (NIT)  
Section: Footnote “Earlier versions of this manuscript...” (page 1 and again in Sec. X, footnote 2)  
Problem: Multiple mentions of “earlier versions of this manuscript erroneously...” and “superseded drafts” appear in the body text and footnotes. This is version-history language inappropriate for a final PRD submission.  
Required fix: Remove or compress these historical notes; at most, retain a single short remark in an appendix or footnote clarifying the Holst vs Pontryagin distinction without referring to earlier drafts.

P1A-N2 (NIT)  
Section: Acknowledgments (page 20)  
Problem: The acknowledgment of using “Claude (Anthropic) as an AI research assistant” is unusual for PRD and verges on process disclosure rather than scientific content. It may also conflict with standard authorship and responsibility expectations.  
Required fix: Check PRD’s editorial policy on AI assistance acknowledgments; if disallowed or discouraged, remove this sentence.

P1A-N3 (NIT)  
Section: Throughout (e.g. Table III footnotes, Sec. XI)  
Problem: There are long footnotes describing chain configurations, MPI pod setups, OMP threads, etc. This is internal computing-log information not needed for the scientific narrative and distracts from the main text.  
Required fix: Remove or move such details to a separate reproducibility note or ancillary file; in the main paper, only describe essential computational aspects at a high level.

P1A-N4 (NIT)  
Section: Figures 1, 3, 4 captions  
Problem: Some captions are more like mini-essays, mixing descriptive text with interpretive claims that repeat material from the main text.  
Required fix: Shorten captions to focus on what is shown in the figure. Keep interpretive/origin discussions in the body text.

P1A-N5 (NIT)  
Section: Typos and style (e.g. “he UBIFY-2026-002”; inconsistent space before units; occasional missing commas)  
Problem: Minor typographical inconsistencies throughout; some internal report codes (“hUBIFY-2026-002”) appear without explanation.  
Required fix: Run a thorough proofread, standardize notation and formatting, and either explain internal report codes or remove them.

## Summary recommendation

REJECT

The paper’s core ideas—systematic scrutiny of minimal Einstein–Cartan–Holst routes to dark energy and the observation that torsion/ Holst contributions decouple from scalar perturbations—are potentially valuable, but the manuscript falls well short of PRD standards. Many key quantitative claims (forecasts, MCMC results, galaxy spins, PTA indices) rely on unpublished companion papers and even on non-existent future-dated references. Several central formulae and suppression estimates (parity-odd operator dimension, one-loop Holst corrections, Immirzi running, ALP energy-density matching) are based on heuristic ansätze rather than derivations or clear citations, yet are treated as numerically robust. The operator-basis closure is incomplete while the language suggests a broad “no-go.” Substantial rewriting, removal of speculative citations, and consolidation into a shorter, more sharply focused paper would be required before a fresh submission could be considered.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E14 (ESSENTIAL)  
Section: Table I (page 4), Sec. VII (page 11), Sec. XIII (pages 17–18), Fig. 4  
Problem: The paper quotes a SPHEREx matter-bounce detection significance of “3–5σ realistic” for \(f_{\mathrm{NL}}=-35/8\), decomposed into a “Fisher-ideal” \(\sigma(f_{\mathrm{NL}})\approx 0.7\) from Heinrich et al. (2024) and a “σ(fNL) ≈ 1.0 after GR-projection and photo-z marginalization,” but there is no place in the manuscript where the 3–5σ range is actually recomputed from explicitly stated survey specs or a Fisher matrix. The only quantitative inputs are: (i) Heinrich et al. \(\sigma(f_{\mathrm{NL}})\approx 0.7\) for a *specific* SPHEREx configuration; (ii) a hand‑waved “~1.0” after systematics; (iii) the raw ratio 4.375/0.7 ≈ 6.25σ mentioned in a footnote. This does not transparently support the 3–5σ “realistic” band that is repeatedly used in Table I, Sec. VII, Sec. XIII, and Fig. 4.  
Required fix: Either (a) add a compact, explicit calculation that shows how the stated 3–5σ “realistic” range is obtained from clearly defined survey parameters and degradation factors (GR projection, \(b_\phi\) prior, photo‑z), or (b) rephrase all such claims to a qualitative “SPHEREx‑like surveys are expected to reach \(\sigma(f_{\mathrm{NL}})\sim 1\) for local shapes, which would clearly test \(f_{\mathrm{NL}}=-35/8\),” without attaching an explicit 3–5σ detection band.

P1A-E15 (ESSENTIAL)  
Section: Sec. II C.1, Eq. (11) and numerical estimate below (pages 6–7); Sec. XII A, Appendix B  
Problem: The “inflationary suppression factor” calculation has inconsistent numeric bookkeeping across the paper. In Sec. II C.1, the text claims \((T_{\mathrm{reh}}/M_{\mathrm{GUT}})^{3/2}\approx 0.03\) at \(T_{\mathrm{reh}}\approx 10^{15}\,\mathrm{GeV}\), \(M_{\mathrm{GUT}}\approx 10^{16}\,\mathrm{GeV}\), but \((10^{15}/10^{16})^{3/2}=0.1^{1.5}\approx 0.0316\) only if one uses exactly 1 order of magnitude; elsewhere, the same factor is described as “order 0.01–0.1” and then taken as effectively fixed when discussing the residual “\(10^5\)” tuning and \(N_{\mathrm{tot}}\approx 92\). In Appendix B, the hierarchy from \(M_{\mathrm{Pl}}^4\) to \(\rho_\Lambda\) is said to be \(10^{122}\), implying \(e^{-3N_{\mathrm{tot}}}\sim10^{-122}\Rightarrow N_{\mathrm{tot}}\approx 94\), whereas in the main text \(N_{\mathrm{tot}}\approx 92\) is repeatedly quoted as if it directly followed from the same calculation. The two values are acknowledged as “∼2%” different but are used without a clear, consistent numerical chain.  
Required fix: Present a single, coherent calculation: pick a definite \(T_{\mathrm{reh}}\), \(M_{\mathrm{GUT}}\) and cosmological-constant hierarchy, show the resulting \(D_{\mathrm{inf}}\) and the implied \(N_{\mathrm{tot}}\), and then propagate that same value consistently throughout the text. Explicitly label any shift between 92 and 94 e‑folds as an order‑of‑magnitude choice, not as a sharp structural number.

P1A-E16 (ESSENTIAL)  
Section: Sec. IV B, Eq. (15) (page 9); Sec. XIII (spectator‑ALP birefringence discussion)  
Problem: The dimensionless ratio \(\Delta\theta_{\text{one-loop}}/\Delta\theta_{\text{obs}}\) used to claim a “\(10^{-58}–10^{-60}\)” suppression is not arithmetically transparent. The text states \(H_0/M_{\mathrm{Pl}}\sim 10^{-61}\), \(\alpha_{\mathrm{em}}/(4\pi)\sim 6\times10^{-4}\), \(M_{\mathrm{Pl}}(\alpha/M)\sim10^{-2}\), and \(\beta_{\mathrm{obs}}\sim 6\times10^{-3}\,\mathrm{rad}\), which numerically gives  
\[
\frac{\Delta\theta_{\text{one-loop}}}{\Delta\theta_{\text{obs}}}
\sim\frac{6\times10^{-4}\times10^{-61}}{10^{-2}\times 6\times10^{-3}}
\sim\frac{6\times10^{-65}}{6\times10^{-5}}\sim 10^{-60}.
\]  
No parameter variation is shown that would yield \(10^{-58}\); the quoted “58–60” range therefore looks like an unexplained ±2‑dex band, not the direct consequence of the numbers in Eq. (15).  
Required fix: Either (a) stick to a single clearly computed value (e.g. “\(\sim 10^{-60}\)”) given the stated numerical inputs, or (b) explicitly show which parameter ranges (e.g. slightly different \(H_0\), \(\alpha/M\), or \(\beta_{\mathrm{obs}}\)) generate the quoted \(10^{-58}–10^{-60}\) spread. In all cases, the order-of-magnitude status of the exponent should be emphasized.

P1A-E17 (ESSENTIAL)  
Section: Sec. IV D, Eq. (17) and numerical examples (page 10); Sec. XIII; Table IV (β row)  
Problem: Several numerical claims about the spectator‑ALP energy density and tuning are not fully recomputed from the given inputs:  
• The text states that for \(\alpha/M=10^{-21}\,\mathrm{GeV}^{-1}\), \(\beta\simeq6\times10^{-3}\,\mathrm{rad}\), and \(m_\theta=H_0\approx1.5\times10^{-33}\,\mathrm{eV}\), Eq. (17) gives \(\rho_\theta\simeq 2.8\times10^{-11}\,\mathrm{eV}^4\simeq\rho_\Lambda\). Using \(\rho_\theta=m_\theta^2\beta^2/[2(\alpha/M)^2]\) with these inputs, and converting \(\alpha/M\) to eV\(^{-1}\), does yield a number of the right order, but the intermediate steps are non‑transparent and units are mixed (GeV vs eV) entirely in prose.  
• The “overshoot” claims of “∼22 OOM at \(m_\theta\sim10^{-22}\,\mathrm{eV}\)” and “∼36 OOM at \(m_\theta\sim10^{-15}\,\mathrm{eV}\)” are consistent with \((m_\theta/H_0)^2\) qualitatively, but no explicit computation or table is shown; the reader must trust the exponents.  
Required fix: Provide at least one explicit worked example showing all unit conversions and intermediate numerical steps for Eq. (17), and either (a) add a compact table or footnote verifying the 22 and 36 orders of magnitude overshoot numbers from the chosen \(m_\theta\) values, or (b) restate them as “\(\mathcal{O}(10^{20})\)” and “\(\mathcal{O}(10^{35})\)” overshoots, clearly labelled as order‑of‑magnitude estimates.

P1A-E18 (ESSENTIAL)  
Section: Sec. X B–D, Eq. (23), footnote 2 (pages 15–16)  
Problem: The perturbation‑transparency “proof” uses the statement that the Holst dual contraction \(\tfrac{1}{2}\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\Gamma^\circ)\) “vanishes identically by the first (algebraic) Bianchi identity” and writes this as Eq. (23): \(R(\Gamma^\circ)=\tfrac{1}{2}\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\Gamma^\circ)=0\). However, (i) the notation “\(R(\Gamma^\circ)\)” is ambiguous, since \(R\) normally denotes the Ricci scalar, not the dual contraction; (ii) the Bianchi identity guarantees antisymmetric cyclic sums of the curvature components but the manuscript does not show the explicit contraction that takes this to zero for all perturbation orders; and (iii) later, the same quantity is erroneously referred to as “\(R\tilde{R}\)” in earlier drafts. Even in this version, the distinction between \(\epsilon e e R\) and the Pontryagin density is only explained in footnotes, not in a clean derivation.  
Required fix: Rewrite Eq. (23) to use unambiguous notation (e.g. \(H \equiv \tfrac{1}{2}\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}\)), and add a short but explicit algebraic demonstration in the main text or an appendix showing how the algebraic Bianchi identity forces \(H=0\) on any torsion‑free connection, including at the level of perturbed FRW metrics. Make sure it is clear that this is not the Pontryagin density and that the all‑orders nature of the statement does not rely on heuristic arguments.

P1A-E19 (ESSENTIAL)  
Section: Sec. IX, Constraint classification paragraph; Table II; Abstract; Sec. XV  
Problem: The manuscript now partly walks back the “13 logically‑independent constraints” claim by acknowledging that B8 is not independent of B14 and that some barriers rest on standard inflationary washout arguments, but the wording is inconsistent. The abstract still speaks of “13 logically-independent mechanism-class constraints,” Table II lists 14 barriers with only a marginal note about B8 vs B14, and Sec. IX’s classification paragraph is not precise enough to justify logical independence pairwise (e.g. B4 Planck suppression, B5 scale separation, and B12 vacuum amplification ceiling are all different faces of the same amplitude hierarchy). This is precisely the kind of over‑tight logical language that PRD editors scrutinize.  
Required fix: Replace all remaining “13 logically-independent” phrasing with more careful language such as “a catalog of 14 structural constraints, with some mutual dependencies (e.g. B8 vs B14, and shared reliance on Planck suppression and inflationary washout in B4, B5, B12).” If the author wishes to retain any independence claim, provide a short explicit mapping or table justifying which subsets are independent and in what precise sense (e.g. independent physical assumptions).

P1A-M10 (MAJOR)  
Section: Sec. III A–B; Sec. V; Sec. VI; Fig. 1 & Fig. 3 captions  
Problem: There are several instances where σ values from fundamentally different null procedures are juxtaposed without an explicit warning that they are not directly comparable (violating the “null-procedure comparability” best practice): e.g. the galaxy-spin “pLEE<10⁻⁴” dipole null (from a specific classifier and sky mask), CMB birefringence σ(β) from WMAP+Planck and anticipated LiteBIRD, and SPHEREx σ(fNL) Fisher values from Heinrich et al. are placed side‑by‑side in Fig. 1 and Fig. 3 as if they lived on a single “amplitude budget” axis. The text does not always remind the reader that these σ’s arise from different likelihoods, data splits, and systematics, and hence cannot be directly ranked as “stronger” or “weaker” constraints.  
Required fix: Wherever σ values from different experiments or pipelines are plotted or quoted in close proximity (especially in high‑level summary figures and tables), add a brief sentence clarifying that these constraints stem from different null procedures and are not strictly comparable in a frequentist sense. Where possible, rephrase qualitative comparisons to avoid implying a direct ranking of σ(fNL), σ(β), and galaxy‑spin p‑values on a single scale.

P1A-M11 (MAJOR)  
Section: Abstract (entire paragraph describing scope and “channel‑level closure”); Sec. I A (“Scope and limitations”); Sec. IV E; Sec. XV  
Problem: The abstract now contains many caveats, but there are still spots where the language is tighter than the body supports. In particular, “We assess four enumerated minimal-ECH spin-torsion channels … and find that each fails at the amplitude level under stated assumptions” and “the role of this paper is the channel-level closure of the four enumerated minimal-ECH dark-energy routes … at amplitude-budget granularity” could be read as stronger than the later admissions that (i) several key operators (Jackiw–Pi, parity‑odd four‑fermion) are not actually evaluated quantitatively, and (ii) the parity‑odd density mapping itself is based on a non‑EFT ansatz. The body does say this, but only after several pages.  
Required fix: Tighten the abstract and early Sec. I language further so that the structural limitations are front‑loaded. For example, explicitly say: “Within a restricted minimal operator set (excluding Jackiw–Pi Chern–Simons and the parity‑odd four‑fermion partner) and under a phenomenological dimensional ansatz, we show that four commonly discussed channels fail at the amplitude level.” This will align the rhetorical strength of the closure claim with what the manuscript actually demonstrates.

P1A-M12 (MAJOR)  
Section: Sec. III A; Sec. XIII; Table IV (β row)  
Problem: The treatment of the CMB birefringence measurements vs the “benchmark β≈0.27°” uses hedge phrases like “consistent with,” “inside the 1σ band,” and “comparable to ACT DR6” but never quantifies the actual difference between the benchmark and the measurements in σ units. The one place where such a computation is done (near the end of Sec. XV, with \(|0.342-0.27|/\sqrt{0.03^2+0.094^2}\approx 0.73σ\)) appears only very late and is itself embedded in a complex sentence. This invites confusion about whether the chosen benchmark is in any way preferred by the data.  
Required fix: In Sec. III A or Sec. XIII, add a concise, early quantitative statement: e.g. “A benchmark β=0.27° differs from the current WMAP+Planck central value 0.342°±0.094° by only ~0.7σ and from the ACT DR6 value 0.215°±0.074° by ~0.5σ, so it is purely illustrative and not singled out by data.” This will make the hedge phrases quantitatively backed rather than impressionistic.

P1A-m1 (MINOR)  
Section: Sec. II A.1, paragraph after Eq. (2) (page 5); Table IV (γ row); Sec. II B, Eq. (9) and surrounding text  
Problem: The manuscript now correctly states that the “∼0.020” spread in γ is scheme‑dependence, not an uncertainty, and that ρcrit≈0.41ρPl is from Ashtekar–Singh while ρcrit≈0.27ρPl is an internal extrapolation. However, Table IV still lists “γ: 0.274 (scheme range ∼0.020)” in a way that can be read as an error bar, and Sec. II B still refers to “the LQG-bounce critical-density window 0.27–0.41 ρPl” as if it had equal standing.  
Required fix: In Table IV, change “scheme range ∼0.020” to “scheme spread (model‑to‑model)” or similar non‑probabilistic language, and in Sec. II B’s Eq. (9) paragraph explicitly mark 0.41ρPl as the Ashtekar–Singh value and 0.27ρPl as “our own extrapolation using γSU(2).”

P1A-m2 (MINOR)  
Section: Sec. XI (Hybrid dark‑energy loophole); Table III footnote; Sec. XV (MCMC discussion)  
Problem: Chain‑status commentary (“chain has accumulated ∼3.8×10⁴ accepted samples,” “R̂−1≈3×10⁻², descending”) still appears in Table III and Sec. XI, even though Sec. I and later sections now say that quantitative DESI w₀–wₐ posteriors are deferred. These status snippets read like lab‑notebook fragments and are inappropriate for a final PRD article.  
Required fix: Remove all references to current chain lengths, interim R̂ values, and “we deliberately do not commit to a calendar date” from the main text and tables. Replace them with a simple statement that “w₀–wₐ chains are in progress and not used in the present analysis.”

P1A-m3 (MINOR)  
Section: Figure captions (Figs. 1, 3, 4); Sec. I B (Paper Organization)  
Problem: Several figures and organizational paragraphs still refer to companion “Paper II,” “Paper III,” and “Paper IV” as if they are co‑published in “this volume,” even though the references section lists them as “in preparation.” Unless PRD is indeed publishing a special issue containing all of these, this phraseology is misleading.  
Required fix: Replace “this volume” everywhere with neutral phrasing such as “companion work (in preparation)” and insert an explicit sentence in Sec. I B noting that these are not yet publicly available and therefore not part of the citable evidence base of this article.

If these issues are corrected in a clean, numerically explicit way—and the remaining rhetorical overstatements are softened—the manuscript will be much closer to PRD’s standards for internal consistency and verifiability.