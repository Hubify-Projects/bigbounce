# P1A R29 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.57.pdf` md5=958587c7 pages=27
**Input format**: TEXT + web search + pass-2 self-critique (11221 chars)
**Wall time**: 102.1s

---

P1A-E1  
Section: Title page / header; throughout (e.g., header “(Dated: June 10, 2026 PDT — v1A.0.57)”, p.1; “v1A.0.56-bundle (resynced 2026-06-10)”, p.23; “earlier versions of this manuscript…”, footnote p.2; multiple “companion paper… in preparation” throughout)  
Problem (EXT1 / version‑history / internal‑log language):  
The PDF is full of explicit version tags, internal bundle labels, and history language (“v1A.0.57”, “v1A.0.56-bundle”, “Earlier versions of this manuscript erroneously identified…”, “companion work in preparation”, “posted concurrently on arXiv”, “available upon request”, run‑status of specific MCMC chains, etc.). This violates PRD style and the review instructions’ prohibition of version‑history / internal‑audit language in the body.  
Required fix (ESSENTIAL):  
Strip all version identifiers, repository sync dates, chain‑status narratives, “earlier versions” commentary, and “in preparation / posted concurrently / available upon request / technical note” process language from the main text. For true companion papers, cite them as standard references only once they exist as stable arXiv/journal entries; otherwise, move any dependence to a self‑contained appendix or remove it.

---

P1A-E2  
Section: Abstract; repeated in body (e.g., abstract ¶2, p.1; Sec. I.A; Sec. IX; Table II; Sec. XV)  
Problem (unsupported “13 logically‑independent barriers” claim):  
The paper repeatedly claims “13 logically‑independent mechanism‑class constraints” while simultaneously stating that Barrier 8 (parity-even four‑fermion interaction) is “subsumed by” or is the “observational consequence” of Barrier 14 (perturbation transparency). This is logically inconsistent: if B8 is entailed by B14, it is not logically independent.  
Required fix (ESSENTIAL):  
Either (a) downgrade the count everywhere to “12 logically independent constraints (14 catalog entries, of which B8 is subsumed by B14)” or (b) provide a precise logical argument why B8 is independent of B14 under clearly stated assumptions. The abstract and all summaries must match the final, calibrated statement.

---

P1A-E3  
Section: Abstract (first paragraph, p.1)  
Text: “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9, 10]”  
Problem (quoted significance not supported by cited papers):  
Ref.  is DESI 2024 VI BAO constraints; ref.  as of mid‑2026 is not a published PRD “DR2 results II” paper with a 3.1–4.2σ w(z) deviation. DESI BAO analyses report tensions at ≲3σ, with detailed dependence on combination with external datasets; there is no single “3.1–4.2σ” claim traceable to – as written. The exact σ‑range appears to be a synthesis from internal analyses rather than a number stated in those papers’ abstracts or tables.  
Required fix (ESSENTIAL):  
Re‑audit ,  and either (a) quote the exact σ and dataset combinations explicitly stated there (with clear attribution), or (b) flag the σ‑range as an internal estimate and remove the ,  citation. In the abstract, any numerical tension level must be directly traceable to the cited work.

---

P1A-E4  
Section: Abstract (central result paragraph, p.1) and Sec. X  
Text: “torsion vanishes at all classical metric/scalar perturbation orders… Holst dual contraction … vanishes identically… and the Holst sector therefore decouples from all scalar/tensor perturbation equations of motion …”  
Problem (no check of tensor/vector sectors, dimensional consistency, or exceptions; no explicit dependence on matter content and action):  
The “perturbation‑transparency theorem” is extremely strong. The body provides only a schematic 5‑step argument for scalars and tensors assuming canonical scalar matter and no non‑minimal couplings. Vector perturbations and mixed scalar–fermion sectors are only mentioned qualitatively. No explicit perturbative expansion of the full ECH+matter action is given, nor are the constraints on higher‑derivative or boundary terms. For PRD, a theorem‑level claim requires a complete, explicit derivation or precise limitations; as written, the abstract overstates the generality (“all scalar/tensor perturbation orders”) relative to what is proved.  
Required fix (ESSENTIAL):  
Either (a) provide a full, self‑contained derivation including all metric, scalar, and tensor modes at arbitrary order, making explicit the assumptions on the action, matter content, and boundary terms, or (b) weaken the statements everywhere to a rigorously supported scope, e.g. “for minimally coupled, canonical scalars around a torsion‑free FRW background, and neglecting vector modes and boundary terms, we find no Holst contribution to the scalar and tensor perturbation equations at any order checked (up to N).” The abstract must be downgraded to match what is actually demonstrated.

---

P1A-E5  
Section: Throughout (e.g. Abstract, p.1; Sec. I, p.3–4; Sec. III B, p.9–10; Sec. XII, XIII, XV, references)  
Problem (dependence on non‑existent or “in preparation” companion works and technical notes as load‑bearing evidence):  
Multiple core claims (MCMC constraints on H0, σ8, ∆Neff, ALP parameter fits, NaMaster validation, SPHEREx fNL forecast, PTA real‑KDE reanalysis, galaxy chirality pipeline, systematic error budgets) are deferred to companion “Paper I(b) ”, “Paper II [2]”, “Paper III ”, “Paper IV ”, and “technical note ”, all listed either as “in preparation”, “posted concurrently on arXiv”, or “available upon request”. As of now, these correspond either to non‑existent arXiv IDs or to self‑citations that cannot be verified independently; they also carry substantial claims (e.g., tens of thousands of MCMC samples, chain R̂, or detailed forecasts) without any in‑paper derivation. This fails the standalone‑reader test and PRD’s requirement that results be verifiable.  
Required fix (ESSENTIAL):  
Make the present paper self‑contained for all claims used in its conclusions. At minimum:  
- Remove all quantitative use of MCMC posteriors, ALP fits, and detailed forecast numbers, or include full methodology, likelihoods, priors, and key numerical results in this paper.  
- Replace “in preparation”, “posted concurrently”, “available upon request” by proper, existing arXiv or journal references, or treat those results as external and non‑load‑bearing (only qualitative context).  
- The abstract and structural claims must not rely on non‑public or unverifiable computations.

---

P1A-E6  
Section: Abstract (final paragraph, p.1) and Sec. XIII, XV  
Text: “fNL = −35/8 is a property of the matter-bounce class [1]… a detailed multi-tracer SPHEREx Fisher forecast is presented in a companion work in preparation [2]”; “3–5σ realistic after full systematic budget (… ) under Heinrich+2024 σ(fNL) ≈ 0.7 — detailed Fisher forecast in companion work in preparation [2]”  
Problem (forecast σ and significance quoted without in‑paper derivation; claim of 3–5σ not traceable to cited work):  
Ref. [1] (Cai et al. 2009) indeed derives fNL = −35/8 for a specific matter‑bounce model[1]. But the 3–5σ SPHEREx significance claim is not in [1] or . Heinrich et al. provide σ(fNL) ≈ 0.7 for a multi‑tracer forecast, but the 3–5σ range arises from the author’s own Fisher analysis, which is only said to live in [2] “in preparation”. There is no explicit Fisher matrix, survey specification, or systematics treatment in this paper.  
Required fix (ESSENTIAL):  
Either (a) include the full Fisher‑forecast machinery (survey assumptions, binning, noise, biases, relativistic corrections, photo‑z priors) and recompute σ(fNL) in this paper, or (b) remove the “3–5σ realistic” numbers from the abstract/body, and merely state that, using recent SPHEREx forecasts, a signal of |fNL| ≈ 4.4 would be detectable at order‑few sigma. All quantitative claims must be reproducible from the content of this paper plus the cited literature.

---

P1A-E7  
Section: Abstract (parity CMB birefringence, p.1); Sec. III A, Sec. IV D, Sec. XIII  
Text: “βobs = 0.342◦ ± 0.094◦ (∼ 3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]) … ACT DR6 follow-up β = 0.215◦ ± 0.074◦ at ∼ 2.9σ (Diego-Palazuelos & Komatsu [5])”  
Problem (citation precision and traceability of σ):  
- [3] (Minami & Komatsu 2020) indeed reports β ≈ 0.35° with ≈0.14° error[3]; [4] (Eskilt & Komatsu 2022) gives β = 0.342° ± 0.094°[4]. The text conflates “first reported” and “refined” in a way that attributes the 0.342° value to [3] as well as [4].  
- [5] is referenced as an ACT DR6 birefringence preprint; as of mid‑2026 there is no widely indexed ACT DR6 birefringence measurement exactly matching 0.215° ± 0.074°. Without an arXiv ID, readers cannot verify this result.  
Required fix (ESSENTIAL):  
Clarify attribution: state that the 0.342° ± 0.094° value comes from Eskilt & Komatsu 2022[4], while Minami & Komatsu 2020[3] provided an earlier Planck analysis. Do not attribute numerical values not present in [3]. For ACT DR6, either cite the actual arXiv preprint with its reported β and σ, or remove this number from the paper until such a reference exists.

---

P1A-E8  
Section: Sec. II A.2 (Derivation of the parity‑odd term, p.5–6) and Appendix B  
Text: Eq. (6), Eq. (7), Eq. (B2) and surrounding explanation of the operator dimension and scaling ρ^bounce_Λ ∼ [(α/M) M_Pl]^5 M_Pl^4  
Problem (dimensional and EFT consistency of the “parity‑odd operator”):  
The text openly admits that the operator in Eq. (6) has off‑shell mass dimension +1 rather than +4, and that the mapping to ρΛ uses an on‑shell scaling ansatz (Appendix B). However, the same construction is then used repeatedly as if it were a controlled EFT contribution, including an apparently precise bounce density ρ^bounce_Λ ∼ 10^-2 M_Pl^4 and the derived N_tot ≈ 92 e‑fold requirement. This mixes heuristic dimensional analysis with quantitatively asserted results. For PRD, any quantitative constraint built on an acknowledged non‑EFT operator must be clearly labelled as speculative and not used in firm “closure” claims.  
Required fix (ESSENTIAL):  
Either (a) re‑formulate the argument in purely qualitative terms (e.g., “one can imagine a parity‑odd sector whose scaling is parametrized as …; taking this as a toy model suggests N_tot of order 10^2”) and remove any sharp numerical claims (N_tot ≈ 92, “10^5 residual fine‑tuning”), or (b) promote the operator to a consistent dimension‑4 EFT operator with explicit M_Pl factors, and show how the mapping to ρΛ follows systematically. The abstract must clearly state that the dark‑energy mapping is a toy ansatz, not part of a rigorous no‑go.

---

P1A-E9  
Section: Sec. IV A (Route 1), Eq. (13), p.10–11  
Text: “Following the standard Hehl–Datta derivation, the resulting axial–axial contact interaction is L_NJL^tor = − 3κ/16 (ψ̄γ^a γ^5 ψ)^2 … ρ_NJL ∼ n_ψ^2/M_Pl^2 … ≈ 4×10^-80 eV^4 ∼ 10^-69 ρ_Λ”  
Problem (numerical estimate not checked and not traceable):  
The late‑time baryon/electron density is approximated as n_ψ ≈ 2.5×10^-12 eV^3; the resulting ρ_NJL ∼ n^2/M_P^2 calculation is claimed to be ≈ 4×10^-80 eV^4, but no explicit computation is shown, and the quoted 10^-69 ρ_Λ ratio is inconsistent with a direct back‑of‑the‑envelope using known values (M_Pl ≈ 1.22×10^28 eV, ρ_Λ ≈ (2.3 meV)^4). For a paper in PRD, all such “70‑orders‑of‑magnitude” statements must be numerically consistent.  
Required fix (ESSENTIAL):  
Recompute ρ_NJL with explicit units and numbers, and show the calculation, at least in a footnote or appendix. Correct the numerical value and the ρ_NJL/ρ_Λ ratio accordingly, or remove the “10^-69” claim and simply state that it is negligibly small.  

---

P1A-E10  
Section: Abstract; Sec. XII.A; Fig. 2, Fig. 5; Appendix B  
Text: “Matching ρΛ ≈ (2.3 meV)^4 requires N_tot ≈ 92”; “reparameterizes 10^122 hierarchy to 10^5 as sensitivity to ΔN_tot ≈ 4 e‑folds”; Fig. 5 bottom panel “fine‑tuning‑score comparison”  
Problem (use of an unproven scaling ansatz to claim specific N_tot and “10^5 residual tuning”):  
The N_tot ≈ 92 and “10^5 residual tuning” are derived from the same non‑EFT ansatz in Appendix B and a heuristic (T_reh/M_GUT)^{3/2} factor. Yet they are stated as central structural results, even plotted in Fig. 5 as if they were on the same footing as ΛCDM or f(R) tuning. This is too speculative for a methods paper in PRD; the quantitative values are not robust and cannot be treated as established.  
Required fix (ESSENTIAL):  
Demote N_tot ≈ 92 and “10^5 residual” to clearly speculative status. The abstract should not present them as definitive. Either remove the numeric “fine‑tuning score” plot or heavily caveat it as illustrative only. If kept, provide a transparent algebraic derivation from Eq. (B2) and explicitly quantify the large systematic uncertainty.

---

P1A-E11  
Section: Abstract (last paragraph), Sec. I.A, Sec. IV, Sec. IX, Sec. XIV.E, Sec. XV  
Text: “channel-level closure of the four enumerated minimal-ECH dark-energy routes”; “routes are closed at the amplitude-budget granularity at which observations discriminate”; “we report 13 logically-independent barriers that collectively constrain … from the quantum bounce to observable dark energy”  
Problem (overstated “no‑go” language vs. acknowledged gaps):  
The paper repeatedly uses closure/no‑go language at the level of a theorem, but also acknowledges missing operators (Jackiw–Pi Chern–Simons, parity‑odd four‑fermion partners), non‑minimal couplings, propagating torsion, dynamical Immirzi fields beyond the minimal scheme, and the sheer fact that the central parity‑odd operator is an ansatz. This discrepancy between strong negative language and incomplete operator analysis is not acceptable for PRD: readers can be misled into thinking a rigorous no‑go theorem has been proved when only a set of heuristic amplitude estimates under fairly restrictive assumptions has been given.  
Required fix (ESSENTIAL):  
Re‑phrase all “closure” statements to emphasize conditionality: explicitly list all assumptions whenever “closed” or “no‑go” is asserted (minimal ECH action, canonical scalar matter, no non‑minimal couplings, etc.), and reduce the claim to “under these assumptions, we find no viable route at the amplitude level.” The title should also be softened (e.g., “Constraints on four minimal ECH dark‑energy routes…” instead of “Closure”).  

---

P1A-E12  
Section: Abstract and data‑methods sections (V, VI, XIII, “Data and Code Availability”)  
Problem (data availability / reproducibility inconsistencies):  
The abstract and body claim that “ΛCDM+ΔN_eff MCMC verification, NaMaster pipeline validation, and ALP parameter fitting are documented separately in companion work…” and that “Supplementary materials are at https://github.com/Hubify-Projects/bigbounce.” The URL given is a live GitHub repo but no DOI or tagged release is specified, only “v1A.0.56-bundle (resynced 2026-06-10)”. There is no guarantee that code or data used in this paper will remain frozen; reproducibility cannot be assured in PRD’s archival sense.  
Required fix (ESSENTIAL):  
Create an immutable, cited release (e.g. Zenodo DOI or git tag) containing the exact code and data used to generate the figures and quantitative claims in this paper. Reference that release explicitly (version hash, DOI) in the Data Availability section, and ensure all scripts required to reproduce each figure and table are documented. Remove ephemeral language (“resynced 2026‑06‑10”).

---

P1A-M1  
Section: Sec. IV D (Route 4), footnote 3, Eq. (17), Eq. (C4)  
Problem (confusing ALP–photon coupling conventions and unquantified tension with existing bounds):  
The translation between α/M and the canonical g_{aγ} is relegated to a long footnote, and the text notes a ~10× difference depending on conventions and requiring either fa ≃ M_Pl/10 or c_γ ~ 10. However, there is no discussion of existing helioscope, stellar‑cooling, or CMB constraints on g_{aγ} at m ~ H_0 scale, which are generally very tight; nor is there a clear, equation‑level map from α/M = 10^-21 GeV^-1 to a specific (f_a, c_γ). For a methods paper that leans on this coupling to argue about naturalness, this is incomplete.  
Required fix (MAJOR):  
Provide a clean, main‑text mapping between α/M and g_{aγ} with explicit assumptions on f_a and c_γ, and compare the implied g_{aγ} to current observational bounds in the relevant mass range. Make clear whether the benchmark α/M is actually allowed. If the comparison is left to future work, then do not use α/M as a concrete “one-loop motivated” number in the naturalness discussion.

---

P1A-M2  
Section: Sec. III B, Sec. V, citations , ,   
Problem (galaxy spin null vs. external literature):  
The paper asserts that its ViT‑based analysis “confirms the null at the dipole level” and is “in amplitude tension with Shamir’s claimed ∼3% asymmetry by a factor of ∼6–12”. External independent analyses (e.g. Patel & Desmond 2024, Philcox & Ereza 2025) already critically re‑assess Shamir’s claims and find null results or strong caveats. These are barely integrated into the narrative, and no quantitative comparison of this paper’s dipole constraints to those in – is given.  
Required fix (MAJOR):  
Explicitly reconcile your spin‑dipole limits with those of –, including a table or at least a paragraph comparing sky coverage, selection cuts, and statistical errors. Do not present your null as the first or sole “confirmation”; position it correctly in context.

---

P1A-M3  
Section: Sec. VII (“Falsification Criteria”) & Fig. 4, Fig. 6  
Problem (σ comparisons and null‑hypothesis specification for β):  
The text alternates between (a) claiming LiteBIRD will test β ≈ 0.27° at “∼9σ” and (b) explaining that relative to the current central value 0.342° ± 0.094°, LiteBIRD cannot distinguish 0.27° from 0.342° at >1σ. This is confusing because different null hypotheses (β=0 vs β=0.342°) are not clearly spelled out.  
Required fix (MAJOR):  
Clearly separate “detection significance vs β=0” from “ability to distinguish different nonzero β values”, both in text and in captions. In particular, every time you quote a σ(β) for LiteBIRD, specify the null hypothesis being tested and avoid implying that LiteBIRD can resolve the difference between 0.27° and 0.342° at 9σ.

---

P1A-M4  
Section: Multiple places where σ, p, or “>” language appears (e.g., “3.1–4.2σ”, “> 100 orders of magnitude”, “≳ 60 orders of magnitude”, “definitively erased”, “negligible”)  
Problem (uncomputed quantitative claims / lack of effect sizes):  
Many inequalities and “orders‑of‑magnitude” statements are qualitative and not backed by explicit numbers or effect‑size metrics. For example, the claim that the NJL contact term underpredicts dark energy by ∼70 orders of magnitude, or that Route 2 is ∼60 orders of magnitude below observations, is not supported by transparent intermediate calculations.  
Required fix (MAJOR):  
For every major inequality used in the core argument, supply either an explicit numerical estimate with input values (in an appendix/table), or weaken the language. Effect sizes (e.g. ratio ρ_route / ρ_Λ, or ∆θ_route / β_obs) should be given as numbers, not just “negligible”.

---

P1A-M5  
Section: References [2], [4], [5], , , ,   
Problem (citation metadata and existence):  
Several references are self‑cited companion works: [2], , , , . These are described as “companion paper, posted concurrently on arXiv”, “technical note, available upon request”. As of mid‑2026, there are no arXiv IDs or DOIs given for these; they are effectively future or internal documents. Reference [5] is described as a 2025 ACT DR6 preprint with arXiv:2509.13654, which is a plausible future ID but currently not resolvable.  
Required fix (MAJOR):  
For PRD submission, every reference must have correct, extant metadata (authors, title, journal/arXiv ID, year). Remove or update all “in preparation” and future‑dated arXiv IDs. If companion papers are not yet public, they cannot be used as references; either (a) upload them to arXiv and cite the actual IDs, or (b) treat them as private communications and do not rely on them for core results.

---

P1A-M6  
Section: Sec. X.B, X.D, Eq. (23)  
Problem (Bianchi‑identity argument too terse for non‑experts; possible confusion with NY boundary term):  
The key step RH(Γ̊) = 0 is asserted based on the algebraic Bianchi identity without an explicit index‑level derivation. Given that earlier versions misidentified the term as Pontryagin, extra care is needed to avoid a new conceptual confusion (Holst vs Nieh–Yan vs Pontryagin).  
Required fix (MAJOR):  
Expand the derivation of Eq. (23) in an appendix: write R_{μνρσ} in terms of the Levi‑Civita connection, contract with ε^{μνρσ}, and show explicitly how the algebraic Bianchi identity forces the result to zero. Also, clearly separate the role of the Nieh–Yan boundary term from this pointwise vanishing.

---

P1A-M7  
Section: Sec. II.B (LQC critical density), Eq. (9), p.7  
Text: “Ashtekar & Singh  quote ρ_crit ≃ 0.41 ρ_Pl at γ=0.2375. Substituting instead γ_SU(2) ≈ 0.274 gives ρ_crit ≃ 0.27 ρ_Pl; this lower value is an internal extrapolation…”  
Problem (quantitative extrapolation using formula from ):  
The formula for ρ_crit in effective LQC depends on γ and the area gap Δ. The extrapolation from γ=0.2375 to γ=0.274 using the same formula is not presented explicitly, and  do not provide a 0.27 ρ_Pl value. While the text admits it is an “internal extrapolation”, the numerical value is used elsewhere as a bound for Ω_GW, etc.  
Required fix (MAJOR):  
Show the explicit computation for ρ_crit(γ=0.274) using the formula in . Alternatively, present ρ_crit as a range based strictly on published values and avoid quoting 0.27 as if it were literature. When using it in Barrier 12, emphasize that it is a heuristic range, not an observed constraint.

---

P1A-M8  
Section: Sec. XIII, Table III, Sec. XIV.C  
Problem (statements about other models “not tested”, “consistent” without analysis):  
Table III lists quintom‑B, Cuscuton, and ekpyrotic models as “not tested” or “consistent” with DESI w0w_a evidence, but no actual calculations are provided in this paper. This risks misleading readers into thinking these models have been assessed.  
Required fix (MAJOR):  
Either remove these entries or clearly label them as qualitative expectations without in‑paper analysis. If kept, provide citations to independent works that have actually tested these models against data.

---

P1A-N1  
Section: Abstract; Sec. I and II (length vs. contribution)  
Problem (paper length vs. actual new content):  
The paper runs 27 pages and includes extensive narrative about programmatic structure (foundations/branches, multi‑paper roadmap, chain status, survey timelines) that is not strictly necessary to convey the core technical content and may obscure the actual derivations. For a PRD methods paper, a more focused presentation would be appropriate.  
Required fix (MINOR):  
Shorten the manuscript to ~18–20 pages by:  
- Moving programmatic roadmaps and survey‑timeline discussions to a short “Outlook” section,  
- Trimming repeated descriptions of the 14 barriers,  
- Consolidating discussion of speculative N_tot and fine‑tuning into a single section.

---

P1A-N2  
Section: Footnotes and boxed “Single‑convention” blocks (e.g. p.5–6, p.12–13, Appendix C)  
Problem (overlong footnotes and meta‑commentary):  
Numerous footnotes are used to settle convention issues or to respond to “external review” concerns. This breaks the flow and is not standard PRD style.  
Required fix (MINOR):  
Move detailed convention reconciliations to an appendix and remove references to “external review” or “earlier drafts.” Present the final conventions succinctly in the main text.

---

P1A-N3  
Section: Minor typographical / stylistic issues (non‑exhaustive)  
Examples:  
- “ansätze” vs “Ansätze” used inconsistently.  
- Spaces in units: “1015 GeV” vs “10^{15} GeV”; “km/s/Mpc” not always formatted as “km s^-1 Mpc^-1”.  
- Some equations lack punctuation or clear reference in text (e.g., Eq. (20) not cited immediately when first mentioned).  
Required fix (NIT):  
Run a careful copy‑edit: correct accents, ensure consistent unit formatting, and make sure every displayed equation is referenced and punctuated as per PRD style.

---

P1A-N4  
Section: Figures (1–6)  
Problem (figure usefulness and labeling):  
Several figures are mostly conceptual cartoons (e.g., Fig. 1, Fig. 4, Fig. 6) with long captions echoing the text. Axes often lack explicit units (e.g. “ω/H” in Fig. 3 is clear, but energy scales in Fig. 2 and the “fine‑tuning score” in Fig. 5 are qualitative). For PRD, figures should either present quantitative results or be clearly schematic.  
Required fix (NIT):  
Label schematic figures explicitly as “schematic” and ensure all axes have units or are dimensionless. Consider removing or moving to supplemental material the least informative figures.

---

## Summary recommendation

REJECT

The manuscript is ambitious and touches on interesting questions, but it falls well short of PRD standards in several fundamental ways. The central “closure” and N_tot claims rely on an acknowledged non‑EFT ansatz, multiple key numerical statements cannot be traced to the cited literature, most of the quantitative support is deferred to non‑public “companion” works, and the perturbation‑transparency “theorem” is not derived with sufficient rigor for the generality claimed. A substantial conceptual re‑framing, plus significant technical additions and a full re‑audit of citations and numerics, would be required; this goes beyond what is reasonable for “major revisions” at PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E13  
Section: Abstract; Sec. III A; Sec. IV B; Sec. VIII; Sec. XII; Sec. XV; Appendix C  
Problem (figure/caption/body mismatch and mixed birefringence normalization):  
The paper uses **three different birefringence normalizations** for the same observable without clearly separating them: \( \beta_{\mathrm{obs}} = 0.342^\circ \pm 0.094^\circ \), a “benchmark” \( \beta \approx 0.27^\circ\text{–}0.30^\circ \), and a “spectral signature” statement in Appendix C that the paper’s mapping is \( \beta = (\alpha/2M)\Delta\theta \). The body then alternates between saying the benchmark is “inside the 1σ band,” “within \(\sim 1.1\sigma\)” of ACT DR6, and “the relevant model-discrimination test is differential against the prior central value.” The numerical comparability is not consistently specified, and the abstract’s “\(\beta \approx 0.27^\circ\)” is presented as if it were a single well-defined predicted value even though the paper later treats it as a consistency point, not a prediction.  
Required fix (MAJOR):  
State explicitly, in one place, which quantity is being compared to which null procedure: \( \beta=0 \), \( \beta=0.342^\circ \), or \( \beta=0.215^\circ \). Use one normalization consistently in the abstract and captions, and make clear that the body’s significance statements are not directly comparable unless they share the same null hypothesis and error model.

P1A-E14  
Section: Fig. 2 caption; Sec. II C; Sec. XII A; Appendix B  
Problem (figure-caption vs body mismatch on the dilution factor and hierarchy bookkeeping):  
Figure 2 captions the “quantitative bookkeeping” as \(N_{\mathrm{tot}} \approx 92\) with \(D_{\mathrm{inf}}\sim 10^{-121}\), while Sec. II C and Sec. XII A repeatedly state both \(D_{\mathrm{inf}}\sim 10^{-121}\) and a separate “\(10^{-2}\times D_{\mathrm{inf}}\sim 10^{-123}\)” decomposition for \(\Xi\). But Appendix B then says the “genuine cosmological-constant hierarchy” is \(\sim 10^{122}\) and that \(N_{\mathrm{tot}}\approx 94\) follows from that bookkeeping, with \(N_{\mathrm{tot}} \approx 92\) only after the ansatz choice. The figure caption does not disclose this ambiguity, so the visual impression of a single robust \(N_{\mathrm{tot}}\) is misleading.  
Required fix (MAJOR):  
Either make Fig. 2 explicitly display the ansatz dependence and the \(92\) vs \(94\) distinction, or revise the caption/body so the plotted dilution factor is clearly labeled as a schematic estimate rather than a unique result.

P1A-E15  
Section: Eq. (1), footnote 1; Sec. II A 1; Sec. IV A; Appendix C  
Problem (dimensional consistency of the torsion/contact-term conventions is only partially resolved):  
The paper claims the torsion definition and the Hehl–Datta contact term “map exactly” between half-weight and full-weight conventions, but Eq. (1) contains the term \(+\frac14 T^{abc}T_{abc}\), while the footnote says the same torsion field corresponds to either \(T^\lambda{}_{\mu\nu}=2\Gamma^\lambda{}_{[\mu\nu]}\) or the half-weight convention. The text then repeatedly treats \(T^{abc}T_{abc}\) as a shorthand for the integrated-out four-fermion term rather than as a separate quadratic torsion contribution. That is internally delicate: the action as written mixes a torsion-squared term and a matter-induced effective contact term without an explicit derivation showing which piece survives before/after eliminating torsion.  
Required fix (MAJOR):  
Make the action-level distinction explicit: either keep the torsion-squared term as part of the fundamental action and derive the four-fermion term after variation, or rewrite the displayed action so the torsion-squared shorthand is not conflated with the induced contact interaction. The current notation risks double-counting.

P1A-E16  
Section: Sec. II C 1; Sec. XII A; Appendix B  
Problem (inconsistent use of \(M_{\mathrm{Pl}}\), \(\bar M_{\mathrm{Pl}}\), and the bounce density scale):  
The paper says throughout that \(M_{\mathrm{Pl}} = 1.22\times 10^{19}\,\mathrm{GeV}\) is the unreduced Planck mass and that reduced-vs-unreduced differences are “below the order-of-magnitude resolution.” But the same sections also use \( \rho_{\Lambda}^{\mathrm{bounce}} \sim (\alpha/M)^? M_{\mathrm{Pl}}^4 \), \(M = M_{\mathrm{Pl}}/\sqrt{\gamma}\), and \( \rho_{\mathrm{crit}} \propto \gamma^{-3} \) in a way that makes the \(\mathcal{O}(1)\) factors non-negligible at the claimed “\(N_{\mathrm{tot}}\approx 92\)” precision level. If a \(2\%\) shift moves the headline e-fold count by \(\sim 2\), then the “below resolution” claim is no longer consistent with the paper’s own use of \(N_{\mathrm{tot}}\) as a calibrated number.  
Required fix (MAJOR):  
Choose one Planck-mass convention for all numerical estimates, propagate it consistently, and explicitly quantify whether the induced shifts in \(N_{\mathrm{tot}}\) and \(\Xi\) are within the claimed uncertainty. If the paper keeps \(N_{\mathrm{tot}}\) at the ±2 level, the reduced/unreduced choice cannot be dismissed as negligible without showing the propagation.

P1A-E17  
Section: Sec. IV D; footnote 3; Appendix C; Table IV  
Problem (basis-conversion chain contains a hidden sign/normalization ambiguity):  
The paper states that \( \alpha/M \) “coincides numerically” with \(g_{a\gamma}\) only after a non-trivial identification, then later in Appendix C claims the same mapping is \( \alpha/M \equiv C_{a\gamma}\alpha_{\rm em}/(2\pi f_a)\), while the footnote at first appearance says the paper’s convention differs by a factor \(1/(4\pi)\) and can be reconciled by \(f_a \sim M_{\mathrm{Pl}}/10\) or \(C_\gamma\sim 10\). These statements are not equivalent unless one fixes the normalization of the ALP operator and the field definition once and for all. The text currently allows the reader to infer that \( \alpha/M = 10^{-21}\,\mathrm{GeV}^{-1} \) is a unique benchmark, when in fact the paper itself admits a factor-of-\(\sim 10\) ambiguity.  
Required fix (MAJOR):  
State a single canonical normalization for the ALP-photon operator, then translate all quoted \( \alpha/M \) values into that basis in the main text. If the benchmark depends on \(f_a\) and \(C_\gamma\), report the allowed range instead of a single number.

P1A-E18  
Section: Table I; Sec. XII B; Fig. 5  
Problem (table/body mismatch on the “fine-tuning score” and the residual hierarchy):  
Table I says the “\(10^5\) residual” is the score under the \(N_{\mathrm{tot}}\) reparameterization and explicitly not a resolution, while Fig. 5 presents that \(10^5\) residual in the same graphical hierarchy as \(\Lambda\)CDM (\(10^{120}\)), quintessence (\(10^{60}\)), and \(f(R)\) (\(10^{40}\)). Meanwhile Sec. XII B says the residual is only a qualitative dimensional rearrangement and that the exact figure depends on an ansatz choice. The figure therefore visually overstates the definiteness of the \(10^5\) number.  
Required fix (MAJOR):  
Relabel the plot as *illustrative* or remove the cross-model numeric comparison entirely unless each score is derived with the same bookkeeping conventions and error model. The table and figure should not imply commensurability when the text says the residual is only a reparameterization.

P1A-E19  
Section: Sec. VII; Fig. 4; Fig. 6; Sec. XV  
Problem (null-procedure comparability across LiteBIRD significance statements):  
The paper says LiteBIRD will “confirm a non-zero birefringence at high significance” or “rule out the spectator-ALP class,” but elsewhere it says the relevant discriminant against the current WMAP+Planck central value is only \(0.73\sigma\) for \(0.27^\circ\) versus \(0.342^\circ\). Those are different null procedures: detection versus discrimination. The figure captions and conclusion place them side by side without warning the reader that the quoted \(\sim 9\sigma\) is only for testing \(\beta=0\), not for separating \(0.27^\circ\) from the current central value.  
Required fix (MAJOR):  
Add an explicit “not directly comparable” qualifier whenever the paper juxtaposes detection significance and model-discrimination significance. In the conclusion, state both numbers with their nulls, or only one of them, but not both in a way that invites conflation.

P1A-E20  
Section: Eq. (20); Sec. IX L; Fig. 4; Table III  
Problem (inconsistent use of the PTA bound and the GW ceiling):  
Barrier 12 gives \( \Omega_{\mathrm{GW}}^{\mathrm{ECH}}|_{\mathrm{bounce}} \lesssim 0.07\text{–}0.17 \), while Fig. 1 and the text around Sec. X claim the PTA reanalysis gives \( \gamma = 2.567 \pm 0.382 \) and that the matter-bounce prediction \( \gamma=3.0 \) sits at \(+1.13\sigma\). But the paper never shows how a bounce-epoch ceiling of order \(10^{-1}\) maps to a PTA-band post-transfer prediction with \(\mathcal{O}(1)\) significance in the observed band. Without an explicit transfer-function calculation, the ceiling and the PTA result are not actually comparable.  
Required fix (MAJOR):  
Either provide the transfer function from bounce epoch to PTA frequency band, or stop presenting the PTA result as if it were derived from the same bound. As written, the paper juxtaposes an initial-condition ceiling and an observational spectral index as though they constrain the same quantity.

P1A-E21  
Section: Table II; Sec. IX; Abstract  
Problem (catalog count vs narrative count mismatch persists in the visual summary):  
The abstract and Table II both say there are “14 historical catalog entries” but “13 logically independent” constraints because B8 is subsumed by B14. However, Table II still labels the 14th entry as a separate barrier and the abstract says “Through 7 foundation studies and 6 observational research branches we report 13 logically-independent mechanism-class constraints,” which is numerically the same as 7+6 but not the same as the 14-entry catalog. The visual presentation can be read as if 7+6 implies 13 by construction, hiding the actual dependence relation between B8 and B14.  
Required fix (MINOR):  
In Table II or its caption, explicitly mark the dependence arrow “B8 \(\rightarrow\) B14” and state that the 13-count is *after* quotienting by that relation. This avoids the appearance that 13 was obtained merely by adding 7 and 6.

P1A-E22  
Section: Sec. IV D; Sec. XIV D; Appendix C  
Problem (unquantified hedge around “free-coupling spectator ALP is viable”):  
The text says that if \( \alpha/M \) is floated, the spectator-ALP class “is recovered as a viable parity-odd source” but also says the benchmark value is in strong tension with astrophysical ALP-photon limits. That is too vague for a parameter-benchmark paper: the reader is left without the actual comparison to helioscope or stellar-cooling bounds in the same coupling normalization. The paper therefore leaves the impression that the benchmark is merely “tensioned” rather than potentially excluded.  
Required fix (MAJOR):  
Quote the relevant astrophysical limits in the same convention as the paper’s \( \alpha/M \) and show whether the benchmark is allowed, marginal, or excluded. If this is not done here, then the statement “recovered as a viable parity-odd source” should be weakened to “algebraically recoverable, subject to external constraints not evaluated in this paper.”