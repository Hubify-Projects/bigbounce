# P1A auto-2026-06-05_1418pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15894 chars)
**Wall time**: 107.1s

---

P1A-E1  
Section: Abstract, p.1  
Problem: The paper claims WMAP+Planck birefringence “first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]” with βobs = 0.342° ± 0.094° and cites [3] and [4]. The Eskilt & Komatsu PRD paper indeed quotes β = 0.342° ± 0.094° as its *own* combined WMAP+Planck constraint; Minami & Komatsu (PRL 125, 221301 (2020)) report a *different* value (β ≈ 0.35° ± 0.14°) and are not the source of the quoted numbers.[3][4] The wording “βobs = 0.342° ± 0.094° … first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]” is historically inaccurate: that specific central value and error bar come only from Eskilt & Komatsu.  
Required fix: Rewrite the sentence to attribute β = 0.342° ± 0.094° explicitly to Eskilt & Komatsu [4] and give Minami & Komatsu’s value separately if desired, e.g. “a WMAP+Planck constraint β = 0.35° ± 0.14° from Minami & Komatsu [3], updated to β = 0.342° ± 0.094° by Eskilt & Komatsu [4].”  

P1A-E2  
Section: Abstract, p.1; Sec. I, p.3–4; Sec. IV, Scope paragraph, p.8–9; throughout  
Problem: Multiple references are cited as “(in preparation)” companion papers with internal identifiers and described as “this volume” or “companion work” but do not correspond to any public arXiv or published entry:

- [2] “H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (in preparation) (2026), HUBIFY-2026-002; companion paper, this volume.”  
- [6] “H. Golden, Cobaya MCMC + NaMaster … (in preparation) (2026), HUBIFY-2026-001B; companion paper, this volume.”  
-  “H. Golden, Galaxy Chirality at Scale: 8.47M Galaxies Classified … (in preparation) (2026), HUBIFY-2026-004; companion paper, this volume.”  
-  “H. Golden, Spectrally Unusual Sources at Scale … (in preparation) (2026), HUBIFY-2026-003; companion paper, this volume.”  

A search on arXiv and NASA ADS yields no such entries; they are not citable in their current form and many key numerical inputs (MCMC posteriors, spin null results, PTA γ) are only documented there. This is below PRD standards for reproducibility.  
Required fix: Either (a) post all four companion works on arXiv (or submit them to a journal) and update the references with proper arXiv IDs/DOIs, or (b) remove the reliance on these internal documents, moving any essential methods and numerical results into the present manuscript (data vector, priors, convergence diagnostics, pipeline details for NaMaster, classifier validation, etc.). Remove “this volume” language unless there is a simultaneously submitted PRD companion and the editor agrees to linked treatment.

P1A-E3  
Section: Abstract, p.1; Sec. I A (point 1), p.3–4; Table I caption, p.4; Sec. IX intro and Table II, p.12–13  
Problem: The paper states it reports “14 constraints (Sec. IX, 13 logically-independent with B8 subsumed by B14)” and calls them “logically-independent mechanism-class constraints” in several places, while also explicitly acknowledging that Barrier 8 is not independent of Barrier 14. This is internally inconsistent language.  
Required fix: Use consistent counting everywhere: e.g. “We catalog 14 barriers, of which 13 are logically independent; Barrier 8 is observationally equivalent to Barrier 14.” Avoid calling all 14 “logically independent” anywhere in the text.

P1A-E4  
Section: Abstract, p.1; Sec. I A point 2 / Sec. XIV D, p.3 and p.17; Appendix B last paragraph, p.19  
Problem: The structural tension result Ntot ≈ 92 post-bounce e-folds is presented in the abstract as if it were a relatively precise requirement (“requires Ntot ≈ 92 post-bounce e-folds”), but the body admits:  

- The parity-odd operator is dimensionally inconsistent off-shell and the ρΛ mapping is a phenomenological ansatz, not an EFT derivation (Appendix B).  
- The dilution factor Dinf and the prefactor (Treh/MGUT)^{3/2} are based on heuristic dimensional arguments and are explicitly called “order-of-magnitude” and “not calculated from a thermal partition function.”  
- Appendix B notes that a rigorous treatment gives Ntot ≈ 94 and the quoted “92” differs by ~2%, tied to the chosen ansatz and prefactor.  

Given this, stating “requires Ntot ≈ 92” in the abstract overstates the quantitative robustness; it is an O(1–few e-fold) order-of-magnitude result, not a sharply determined requirement.  
Required fix: Downgrade the quantitative strength consistently, especially in the abstract: e.g. “requires of order Ntot ≈ 90–95 post-bounce e-folds under our phenomenological scaling ansatz” and explicitly mention in the abstract that the dark-energy mapping is only phenomenological, as you already do but less prominently than the sharp number.

P1A-E5  
Section: Abstract, p.1; Sec. III A, p.7; Sec. VI–VII, p.11; Table I, p.4  
Problem: The paper quotes observational birefringence significances and SPHEREx fNL forecast significances that depend on external literature and its own unpublished forecasting:

- βobs = 0.342° ± 0.094° “(∼ 3.6σ from β = 0)” is consistent with Eskilt & Komatsu [4] (3.6σ), but the ACT DR6 value “β = 0.215° ± 0.074° at ∼ 2.9σ” is not checked for σ directly in the cited paper here; however, Diego-Palazuelos & Komatsu indeed report ~2.9σ, so this is acceptable.  
- “Heinrich+2024 σ(fNL) ≈ 0.7” for SPHEREx multi-tracer forecast is supported by Heinrich, Doré, & Krause (JCAP 2024) who find similar values for local-type fNL forecast using SPHEREx-like survey assumptions.  
- The claimed 3–5σ realistic significance range is partly based on an unpublished “Paper II [2]” Fisher forecast and ad hoc degradations (GR projection, bϕ, photo-z). Since Paper II is not public and no tables are given here, the 3–5σ statement is not reproducible or verifiable.  

Required fix: (i) For birefringence, add a short explicit citation of the significance from [4] and [5] and avoid rephrasing it as “∼3.6σ” or “∼2.9σ” without referencing the exact numbers used in those papers. (ii) For fNL forecasts, either present enough Fisher matrix inputs and degradation factors in this paper to reproduce the 3–5σ figure, or remove that quantitative claim and only quote the Heinrich et al. σ(fNL) ≈ 0.7 (which is externally verifiable) plus a qualitative comment that systematics will degrade it.

P1A-E6  
Section: Sec. I, “Companion paper”, p.5; Sec. II C 2, p.7; Sec. III B, p.8; Sec. VI, p.11; Table IV, p.20  
Problem: The paper repeatedly relies on internal MCMC results “documented in companion work in preparation [6]” to support H0, ∆Neff, σ8, ΛCDM consistency, and ALP parameter fits, but does not provide the chains, priors, likelihoods, or convergence diagnostics in the present manuscript. For PRD it is not acceptable for central cosmological numbers to rely only on inaccessible internal documents.  
Required fix: Either (a) make the MCMC chains, likelihood setup, and priors publicly available (arXiv or data repository) and give a precise citation/DOI, or (b) move a concise but complete description of the MCMC configurations into this paper (datasets used, likelihoods, prior ranges, sampler settings, R̂, effective sample sizes) and treat [6] as “to be published” only for extended details. Until (a) or (b) is done, the cosmological parameter values should be treated as illustrative and not used to support any substantive claims.

P1A-E7  
Section: Sec. II B, equations (8)–(9), p.6; text surrounding ρcrit values  
Problem: The paper quotes ρcrit ≃ 0.27–0.41 ρPl, attributing 0.41 ρPl to Ashtekar & Singh’s LQC value and deriving 0.27 ρPl by substituting γSU(2) ≈ 0.274 into the LQC formula. Ashtekar & Singh  do indeed quote ρcrit ≃ 0.41 ρPl for the standard area gap; the value 0.27 ρPl is not a published LQC number but an internal extrapolation across Barbero–Immirzi choices, as the author admits. However, the abstract states “LQC: ρc ≃ 0.27–0.41 ρPl” as if this were a published window.  
Required fix: In the abstract, clearly distinguish: “LQC predicts ρc ≃ 0.41 ρPl for the canonical area gap; using alternative black-hole entropy motivated γ values gives an internal extrapolation ρc ≃ (0.27–0.41)ρPl which we treat as a scheme-dependent range, not as a published LQC interval.” Do not present “0.27–0.41” as an external LQC result.

P1A-E8  
Section: Sec. II A 2, Eq. (5)–(7), p.5–6; Appendix B, p.19  
Problem: The “parity-odd term” S_eff with coupling α/M is justified via one-loop estimates from Freidel et al.  and Shapiro & Teixeira , but those papers do not present the specific operator in Eq. (5)–(7) with the quoted coefficient; the current paper acknowledges that the one-loop structure is an ansatz and that the operator has incorrect mass dimension off shell. Nonetheless, phrases like “motivating the order of magnitude [(α/M) MPl] ∼ 10−2” could be misread as a real one-loop computation. The underlying sources  do compute loop corrections in Einstein–Cartan/Holst setups, but not this exact structure or the numerical 10−2.  
Required fix: Sharpen the attribution: clearly state that Eq. (7) is an *order-of-magnitude ansatz*, not taken from a specific loop calculation in ; explicitly say something like “we introduce Eq. (7) as a phenomenological parametrization, loosely inspired by one-loop structures in , but not equal to any published result. The estimate [(α/M) MPl] ∼ 10−2 is a choice, not a prediction.” Ensure no wording suggests that 10−2 comes directly from Shapiro & Teixeira or Mercuri & Capozziello.

P1A-E9  
Section: Sec. IV B, Eq. (15), p.9–10  
Problem: The paper compares ∆θ_one-loop / ∆θ_obs and mentions that an earlier draft missed an H0/MPl factor; the current derivation uses a dimensionless ratio but intermixes quantities in eV and GeV heuristically. The claim that the ratio is ∼10−58–10−60 is plausible given H0/MPl ~ 10−61 and αem/4π ~ 10−3, but it is not derived from a precise operator in the literature and relies on an ad hoc matching to “the R4-fitted coupling α/M ∼ 10−21 GeV−1.” There is no explicit check against Mercuri & Capozziello , which compute one-loop corrections to the Holst term but not a cosmological birefringence amplitude.  
Required fix: Clarify that this is an internal consistency estimate given the assumed operator normalization, not a cross-check against . Add a sentence stating that no published calculation currently derives the late-time birefringence amplitude from Holst one-loop corrections; your ∼10−60 suppression is an EFT-level scaling argument rather than a direct reproduction of a known result.

P1A-E10  
Section: Sec. IV D, Eq. (17), p.10–11; reference   
Problem: Lue, Wang & Kamionkowski  analyse cosmological signature of parity-violating interactions with a generic ϕ F F̃ term; they do not define α/M exactly as in Eq. (17). The current paper correctly notes that  “work with a generic pseudoscalar-photon Chern–Simons coupling … not with the specific −¼ (α/M) normalization adopted here” and that it uses them as an “early example,” which is acceptable. However, stating that “Setting the rotation-rate amplitude equal to the published WMAP+Planck cosmological-birefringence measurement … bounds α/M at ∼10−21 GeV−1” implicitly treats β–θ normalization as fully standard; different conventions in the literature could shift that number by factors of order unity or more.  
Required fix: Add an explicit note that the bound α/M ∼ 10−21 GeV−1 depends on your chosen normalization of the Chern–Simons term and that other conventions differ by factors of O(1). This does not change the naturalness conclusion but avoids over-precision.

P1A-E11  
Section: Sec. VIII, p.12; references , , , ,   
Problem: Several “recent” works are cited with future-dated years (2025–2026) and arXiv numbers not currently existing, e.g.:

-  “Legner et al. 2025, arXiv:2507.09228”  
-  “Alam et al. 2025, arXiv:2509.03508”  
-  “Cai & Zhu 2026, arXiv:2603.13924”  

Searches on arXiv.org and ADS currently find no entries with these IDs or matching titles. Future-dated arXiv IDs are not permissible; this is fabricated or at best speculative metadata.  
Required fix: Remove all future-dated or non-existent arXiv identifiers and publication years. If these are genuinely ongoing works, refer to them generically (“in preparation” or “private communication”) without precise arXiv IDs or years, or better, omit them entirely until they exist. PRD cannot accept invented arXiv numbers.

P1A-E12  
Section: References [1], [3], [4], [5], [7], , , , , , –, , , , , , , , , , , , , , , , ,   
Problem: For all these references, the metadata (authors, titles, journals, years) match known arXiv or journal entries as far as can be checked quickly:

- [1] Cai et al. (JCAP 2009) fNL = −35/8 matter bounce, correctly cited.[1]  
- [3] Minami & Komatsu PRL 125 (2020); [4] Eskilt & Komatsu PRD 106 (2022); [5] Diego-Palazuelos & Komatsu (ACT DR6 birefringence) match.[3][4][5]  
- [7] Planck 2018 parameters, Aghanim et al. (A&A 641, A6) correct.[7]  
-  Ashtekar & Singh (Class. Quant. Grav. 28, 213001) correct.  
-  Hehl et al. Rev. Mod. Phys. 48 (1976), Einstein–Cartan, correct.  
-  Poplawski papers exist with matching titles and venues.  
-  Freidel, Minic & Takeuchi PRD 72, 104002 (2005) correct.  
-  Mercuri and Mercuri & Capozziello papers on Holst term and loop corrections exist with matching metadata.  

However, some references are given in hybrid, semi-commentary style with embedded interpretive comments in the reference text (e.g.  includes an explanatory sentence about Quintom-B used in “P1A Sec. VI”), which is non-standard for PRD bibliographies.  
Required fix: Clean the reference list to standard PRD format: author(s), title, journal, volume, page, year, and arXiv ID, without commentary sentences inside the bib entries. Keep interpretive notes in the main text, not inside the reference.

P1A-M1  
Section: Sec. I A, point 1, p.3–4 (“14-constraint catalog and perturbation-transparency observation”)  
Problem: The paper claims novelty for several barriers (mass-coupling lock, topological-shift duality, scalar-tensor universality, Planck suppression, etc.) but does not systematically assess prior literature on Einstein–Cartan cosmology and torsion dark energy. Some aspects—e.g. Planck suppression of torsion couplings, vanishing torsion in absence of spin—are standard textbook conclusions (Hehl et al. ; Shapiro & Teixeira ). The claim “novel results (Barriers 1, 2, 3, 4, 8, 10, 11, 12, 14)” risks overstating originality where at least part is elaboration of established facts.  
Required fix: Rephrase to make clear which barriers are genuinely new structural combinations or cross-channel arguments, vs. which are re-statements or straightforward applications of known EC/PGT results. Avoid implying that Planck suppression or scalar-tensor universality per se are novel discoveries.

P1A-M2  
Section: Sec. X, “The perturbation-transparency result”, p.14  
Problem: The main “perturbation transparency” theorem is stated in words with a short chain of reasoning, but there is no explicit, fully written equation-level derivation for scalar and tensor perturbations, no decomposition of the connection into Levi-Civita plus contorsion, and no explicit variation of the Holst action showing that the Pontryagin density contributes only boundary terms even in the perturbed FRW background. The paper also points to Hehl et al. 1976 , but that reference does not address the Holst term or all-order cosmological perturbations. For a central claim in a PRD theory paper, this level of detail is insufficient.  
Required fix: Provide a complete derivation. At minimum: (i) write Γ = Γ̊ + K, (ii) show the torsion equation of motion algebraically sets K = 0 in the scalar-only matter case at all orders; (iii) show explicitly that the Holst term reduces to ∇μK^μ with K^μ built from the Levi-Civita curvature and that its variation vanishes up to boundary terms; (iv) derive the quadratic and cubic actions for scalar and tensor modes to demonstrate the absence of γ-dependent terms. Alternatively, give a precise reference where exactly this all-order result is already proven and align your notation with it.

P1A-M3  
Section: Sec. IV Scope paragraph, p.8; Sec. XI, p.15; Sec. XIV E, p.17  
Problem: The paper asserts “channel-level closure of four enumerated minimal-ECH dark-energy routes” and distinguishes this from an “operator-level basis closure,” but in several places the language may mislead readers into thinking a stronger no-go theorem has been proven, especially when combined with phrases like “systematic closure of minimal first-principles routes.” Given that Jackiw–Pi R∧R̃ and parity-odd four-fermion terms are explicitly excluded, and that other torsion dynamics (propagating modes, non-minimal couplings) are not considered, one must be careful that the claim is not overinterpreted as a general theorem about ECH and dark energy.  
Required fix: Tighten the claims. Explicitly state in the introduction and conclusions that this is *not* a general no-go theorem for Einstein–Cartan–Holst dark energy, but a closure of four specific channels under restrictive assumptions (canonical scalar matter, non-propagating torsion, minimal coupling, etc.). Replace phrases like “systematic closure of minimal first-principles routes to dark energy in ECH” by “systematic closure of four minimal channels we consider.” 

P1A-M4  
Section: Sec. III B, p.8; Sec. V, p.11; references –;   
Problem: The paper states that an independent ViT-Small classifier applied to DESI Legacy DR8 finds a null galaxy spin dipole and “refutes Shamir’s claimed 3% asymmetry at high significance,” citing a companion “Paper IV  (in preparation)” plus external critiques . Shamir’s ApJ and arXiv works are cited correctly, but without access to  one cannot verify classifier architecture, training set, debiasing, or the exact p-values. This is again a reproducibility problem: a primary empirical claim in this paper (galaxy spin channel is null) depends on inaccessible work.  
Required fix: Either provide a concise summary of the classifier, sample selection, null tests, and the main quantitative result (A0, its uncertainty, and the statistical test used) in this paper, or remove the claim that the null has been *established* by your pipeline, instead citing Patel & Desmond  and Philcox & Ereza  as the current external null results.

P1A-M5  
Section: Sec. XIII, Table III, p.16  
Problem: Table III lists various models and attributes like “Quintom-B … consistent†” with DESI w0wa, while other entries state “not tested‡” referencing an ongoing MCMC chain. This looks more like an internal project status note than a finished scientific result, and the “†/‡” footnote includes detailed text about chain convergence. This is inappropriate for PRD and confusing to readers: it mixes in-progress chain status with a published table.  
Required fix: Remove the chain-status commentary from the table. Restrict Table III to statements that are supported by completed, reproducible analyses. For ongoing chains, simply state in the text that fits including w0wa are under investigation and omit any “consistent” or “not tested” labels.

P1A-M6  
Section: Data and Code Availability, p.18  
Problem: The GitHub link and repository description are given, but PRD policy requires that data/code availability statements are accurate and that the repository contains everything necessary to reproduce key results. Given that significant results are in companion works [2], [6], , , it is currently unclear whether this repository actually suffices.  
Required fix: Make sure that the repository truly contains all scripts and configuration files needed to reproduce the calculations in *this* paper (not just those in the companions). Explicitly list which figures/tables/sections are reproducible from that repo. If some require the companion papers’ code/data, state that transparently and adjust claims of reproducibility.

P1A-N1  
Section: Abstract, p.1; throughout  
Problem: The paper frequently uses internal project labels (“Foundations A–G”, “Branches H, J, L, M, N, O”, “Paper I(b)”, “Paper II”, “Paper III”, “Paper IV”) without always explaining their content in this paper. While not strictly prohibited, this internal bookkeeping style increases cognitive overhead and can make the narrative hard to follow.  
Required fix: Provide a brief glossary or a compact summary of what each Foundation/Branch actually corresponds to physically, and avoid referencing internal paper numbering unless those manuscripts are simultaneously submitted. At minimum, when a Foundation/Branch is first mentioned, summarize its content in one or two sentences.

P1A-N2  
Section: Sec. II C 1, paragraph “Reheating thermal-reset barrier”, p.6–7  
Problem: The phrase “this is bookkeeping, not progress” and similar self-commentary are stylistically informal for PRD. While it conveys skepticism, it is better expressed in a more neutral, impersonal style.  
Required fix: Rephrase such sentences to neutral, descriptive language (e.g. “This reparametrization does not solve the cosmological constant problem; it simply shifts the fine tuning into the choice of Ntot.”).

P1A-N3  
Section: References , , p.20–21  
Problem: Reference  includes an embedded note “Used in P1A Sec. VI to point readers…” and  is labeled “companion technical note, available upon request from the author.” This is unorthodox for reference formatting.  
Required fix: Strip these notes from the bibliography. If you want to comment on how a reference is used, do so in the main text or a footnote, not inside the bib entry. For , either provide a stable public identifier (arXiv, DOI) or remove it; “available upon request” is generally discouraged in PRD references.

P1A-N4  
Section: Sec. XV, Acknowledgments, last paragraph, p.18  
Problem: The author explicitly acknowledges the use of “Claude (Anthropic) as an AI research assistant” and asserts that “All scientific claims … were independently verified by the author.” While such acknowledgments are increasingly common, PRD currently does not have a settled policy on AI co-authorship/acknowledgement; this may need to be discussed with the editor.  
Required fix: At minimum, move any AI-tool description to a short, neutral note if the editor allows it, and clarify precisely which tasks were AI-assisted (e.g., “text editing” vs “derivation checking”). Be prepared to remove this line if the journal requests it.

P1A-Length-1  
Problem: The manuscript runs 21 pages, plus dense notation, and covers: conceptual framework, 14-barrier catalog, four route-by-route closures, perturbation-transparency result, galaxy spin analysis, birefringence, structural tension with fNL, and extensive internal project management notes. For the claimed contribution—a channel-level closure of four ECH dark-energy routes under relatively restrictive assumptions—the paper is arguably overlong and partially obscured by project-internal commentary.  
Required fix: Streamline. Focus on (i) a clean, detailed derivation of the perturbation-transparency theorem; (ii) a concise but rigorous analysis of each of the four routes; (iii) a clear statement of the limitations. Move project logistics (chain status, future surveys, “this volume” remarks) and some of the barrier catalog discussion to an appendix or to a genuinely separate companion paper.

## Summary recommendation

REJECT

The paper mixes an interesting conceptual program (channel-level closure of several Einstein–Cartan–Holst dark-energy routes and a perturbation-transparency observation) with extensive reliance on unpublished “companion” works, future-dated/arXiv-fabricated references, and heuristic dimensional ansätze. The main claimed theorem (perturbation transparency) is not derived at a level of rigor suitable for PRD. Key empirical and forecasting claims hinge on inaccessible internal analyses, violating reproducibility expectations. The citation metadata is generally correct for established works but includes several non-existing/future arXiv IDs and non-standard bibliographic commentary. Rectifying all essential issues would require substantial restructuring, additional derivations, and public release of the companion material; this goes beyond “major revisions” and is best addressed in a fresh, more focused submission.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E13  
Section: Abstract, p.1; Sec. II C 1, p.6–7; Sec. XII A, p.15–16; Appendix B, p.19  
Problem (arithmetic + consistency): The paper repeatedly quotes a “fine‑tuning reduction from \(10^{122}\) to \(10^5\)” (or equivalently \(N_{\text{tot}} \approx 92\) e‑folds) as if these numbers are mutually consistent, but the internal arithmetic and cross‑referenced values do not match. In Appendix B the genuine hierarchy is correctly identified as \(M_{\rm Pl}^4 / \rho_\Lambda^{\rm obs} \sim 10^{122}\) and the required dilution factor is \(D_{\rm inf} \sim e^{-3N_{\text{tot}}} \sim 10^{-122}\), giving \(N_{\text{tot}} \approx 122 \ln 10 / 3 \approx 94\).[B] In the main text, however, the structural tension section and abstract state \(N_{\text{tot}} \approx 92\) and describe this as “reparameterizing” the fine‑tuning hierarchy to a sensitivity of order \(10^5\) in \(\Delta N_{\text{tot}}\) (Sec. II C 1, Sec. XII A) even though \(e^{3\times 4} \approx e^{12} \sim 10^5\) would correspond to a *residual* sensitivity around a chosen \(N_{\text{tot}}\), not to the original \(10^{122}\) hierarchy, and this is not clearly separated in the abstract. There is also an explicit admission in Appendix B that the 92 vs 94 difference is a ∼2% artifact of the chosen on‑shell ansatz, but the abstract still presents “requires \(N_{\text{tot}} \approx 92\)” without any range or uncertainty.  
Required fix:  
• Make the arithmetic transparent and consistent in all places: explicitly state that the *true* hierarchy is \(\sim10^{122}\) and that \(N_{\text{tot}} \approx 94\) e‑folds follows from that when using the on‑shell scaling ansatz, with “92” identified as an ansatz‑dependent rounded value.  
• In the abstract and Sec. I A point 2, replace “requires \(N_{\text{tot}} \approx 92\)” and “reparameterizes the \(10^{122}\) hierarchy to \(\sim 10^5\)” by something like “corresponds to \(N_{\text{tot}} \sim 90\!-\!95\) e‑folds, so that the residual sensitivity to \(\Delta N_{\text{tot}}\) is of order \(e^{3\Delta N_{\text{tot}}}\sim10^5\) for \(\Delta N_{\text{tot}}\sim4\); this is a bookkeeping reparameterization, not a reduction of the underlying \(10^{122}\) hierarchy.”  
• Ensure Appendix B, Sec. II C 1, Sec. XII A, and the abstract all quote the same \(N_{\text{tot}}\) range and clearly distinguish between (i) the genuine \(10^{122}\) ratio and (ii) the derived \(10^5\) *sensitivity* to a few e‑folds around that value.  

P1A-E14  
Section: Sec. II B, Eq. (9), p.6; Sec. II B text, p.6; Table I, p.4; Sec. IX L, Eq. (20), p.13  
Problem (dimensional + arithmetic + consistency): The paper gives the critical density as  
\[
\rho_{\rm crit} = \frac{3}{8\pi G \gamma^2 \Delta} = \frac{3}{32\pi^2 \gamma^3} \rho_{\rm Pl}
\]  
with \(\Delta = 4\sqrt{3}\pi\gamma \ell_P^2\). Using \(\gamma = 0.2375\) gives the standard LQC value \(\rho_{\rm crit}\simeq 0.41\rho_{\rm Pl}\). However:  
• In the text the second equality is written as \(3/(32\pi \gamma^3)\rho_{\rm Pl}\); with only one power of \(\pi\) this does not match the definition \(\Delta = 4\sqrt{3}\pi\gamma \ell_P^2\) and is inconsistent with the 0.41 numerical value.  
• Later, the paper uses \(\gamma_{\rm SU(2)} \approx 0.274\) to infer \(\rho_{\rm crit} \simeq 0.27\rho_{\rm Pl}\) and then quotes a “0.27–0.41” window as if both endpoints came from the same published formula. The author notes in passing that 0.27 is an “internal extrapolation” but still uses “0.27–0.41” in Table I and Barrier 12 (Eq. 20) as if it were a single LQC window.  
• Barrier 12 then squares this range to state \(\Omega_{\rm GW}^{\rm ECH}|_{\rm bounce} \lesssim ( \rho_{\rm crit}/\rho_{\rm Pl})^2 \approx 0.07–0.17\), but if \(\rho_{\rm crit}/\rho_{\rm Pl}=0.27–0.41\), the square is \(0.073–0.168\); this is numerically consistent, yet it implicitly treats 0.27–0.41 as a uniform LQC band rather than as “one published value plus one internal extrapolation,” which is stated more carefully earlier.  
Required fix:  
• Correct the algebraic form of Eq. (9) so the second expression matches the stated \(\Delta\) and produces the canonical 0.41 value for \(\gamma=0.2375\); explicitly carry the \(\sqrt{3}\) and \(\pi\) factors or drop the second equality if you do not intend to present a simplified analytic coefficient.  
• Throughout (abstract, Table I, Sec. II B, Sec. IX L), explicitly label 0.41 \(\rho_{\rm Pl}\) as the published Ashtekar–Singh value and 0.27 \(\rho_{\rm Pl}\) as an internal extrapolation obtained by substituting \(\gamma_{\rm SU(2)}\) into the same formula, not as a published “LQC range.” Ensure Barrier 12’s ceiling is described as using “\(\rho_{\rm crit}\in[0.27,0.41]\rho_{\rm Pl}\) when varying \(\gamma\) across schemes,” not as an observationally or theoretically established interval.  

P1A-E15  
Section: Sec. III A, Eq. (12), p.7; Sec. II A 2, Eq. (7), p.6; Sec. IV B, Eq. (15), p.9–10; Sec. X D, Eq. (23), p.14; Appendix B, Eq. (B1)–(B2), p.19  
Problem (dimensional consistency): Several displayed equations mix conventions and units in ways that are likely to confuse readers or are dimensionally incomplete given the paper’s own definitions. Specifically:  
• Eq. (7) writes \(\alpha/M \sim (g^2 \gamma)/(32\pi^2 M)\,\ln(\Lambda_{\rm UV}^2/\mu^2)+\delta_{\rm NY}\) and then “motivates” \([(\alpha/M)M_{\rm Pl}] \sim 10^{-2}\). However, no explicit choice of \(g,\Lambda_{\rm UV},\mu,\delta_{\rm NY}\) is given and the underlying loop papers cited do not compute this operator with this normalization. Since \(M\sim M_{\rm Pl}/\gamma\), the claim \((\alpha/M)M_{\rm Pl}\sim10^{-2}\) implicitly fixes the product \(g^2 \ln(\Lambda_{\rm UV}^2/\mu^2)+\dots\) without stating it, and the dimensional analysis is obscured by mixing the phenomenological \(M\) with the loop‑level quantities.  
• Eq. (12) uses \(C_\ell^{EB} \simeq 2\beta C_\ell^{EE}-C_\ell^{BB}\), but in the small‑angle regime the usual relation is \(C_\ell^{EB} \simeq 2\beta\, C_\ell^{EE}\) if intrinsic \(BB\) is negligible; the extra “\(-C_\ell^{BB}\)” term is not justified and is dimensionally inconsistent with the rest of the paper’s use (since both \(C_\ell^{EE}\) and \(C_\ell^{BB}\) are power spectra while \(\beta\) is dimensionless; it is unclear what approximation is being made).  
• Eq. (15) constructs \(\Delta\theta_{\rm one\mbox{-}loop}/\Delta\theta_{\rm obs} \sim \frac{\alpha_{\rm em}}{4\pi}\frac{H_0/M_{\rm Pl}}{(\alpha/M)\beta_{\rm obs}}\), with \(H_0\) in eV and \(M_{\rm Pl}\) presumably in GeV, then asserts the ratio is \(\sim10^{-58}-10^{-60}\). The text acknowledges a past missing \(H_0/M_{\rm Pl}\) factor and a “naive” mixing of eV and GeV, but the current derivation still does not clearly spell out the unit conversion or where the single power of \(M_{\rm Pl}\) comes from in the effective operator.  
• Eq. (23) writes \(R(\bar\Gamma)=\tfrac12\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\bar\Gamma)=\tfrac12\,{}^\ast RR\equiv\partial_\mu K^\mu\), using \(R\) both for the Ricci scalar (earlier) and for the dual contraction, making dimensional tracing non‑transparent.  
• Appendix B, Eq. (B2) writes \(\rho_\Lambda^{\rm bounce}\sim (\alpha/M)M_{\rm Pl}^5\) and then states this is \(\sim 10^{-2}M_{\rm Pl}^4\), which only works if \((\alpha/M)M_{\rm Pl}\sim10^{-2}\); that assumption is taken from Eq. (7) but not repeated here, so Eq. (B2) as written appears to have dimension +5 until the hidden substitution is made.  
Required fix:  
• For Eq. (7) and Appendix B, explicitly factor out all mass scales: write \((\alpha/M)M_{\rm Pl} = (g^2\gamma/32\pi^2)\,(M_{\rm Pl}/M)\ln(\Lambda_{\rm UV}^2/\mu^2)+\dots\) and then state clearly that you *choose* \((\alpha/M)M_{\rm Pl}=10^{-2}\) as a phenomenological parameter, rather than presenting it as “motivated” by the loop papers. Repeat this assumption immediately before Eq. (B2) so the dimensionality is transparent.  
• For Eq. (12), either (i) drop the “\(-C_\ell^{BB}\)” term and stick to the standard small‑angle formula \(C_\ell^{EB}\simeq 2\beta C_\ell^{EE}\), or (ii) derive and explain the origin of the \(-C_\ell^{BB}\) contribution, and state clearly in the text under what conditions that form is valid.  
• For Eq. (15), carry units explicitly: define all mass scales in a single unit system, show how \(H_0/M_{\rm Pl}\sim10^{-61}\) arises, and justify the single power of \(M_{\rm Pl}\) in the denominator from the operator in Eq. (14) rather than as an ad hoc plug‑in; alternatively, rewrite the estimate using fully dimensionless quantities to avoid unit mixing.  
• For Eq. (23), use distinct notation for the Pontryagin density (e.g. \(P\equiv \tfrac12\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}\)) to avoid overloading \(R\) and make clear that the Holst term reduces to \(\int d^4x\,\sqrt{-g}\,P\), a total derivative, with dimensions matching the action.  
• In Appendix B, immediately after Eq. (B2), add a sentence such as “Here we have assumed \((\alpha/M)M_{\rm Pl}\simeq10^{-2}\), so that \((\alpha/M)M_{\rm Pl}^5\simeq 10^{-2}M_{\rm Pl}^4\); this is a phenomenological choice rather than a loop prediction.”  

P1A-E16  
Section: Abstract, p.1; Sec. VII and footnote 1, p.11–12; Sec. XIII, p.16–17; Table I caption, p.4  
Problem (arithmetic + comparability of σ; null-procedure comparability): The paper’s quoted “3–5σ realistic” SPHEREx detection significance for \(f_{\rm NL}=-35/8\) is not consistently traceable from the numbers given, and different σ values derived from different null procedures are juxtaposed without explicit comparability caveats. Specifically:  
• Footnote 1 defines a “Fisher‑ideal” regime with \(\sigma(f_{\rm NL})\approx0.7\), giving \(|f_{\rm NL}|/\sigma \approx 4.375/0.7 \approx 6.25\sigma\), then states this is “degraded to \(\sim5–5.5\sigma\) optimistic” after a template‑overlap factor \(r\approx0.84\) but does not show how the degradation is computed (multiplying 6.25 by 0.84 gives 5.25, but that assumes a particular way of folding \(r\) into σ).  
• The same footnote then introduces an “after GR‑projection and photo‑z marginalization” regime with \(\sigma(f_{\rm NL})\approx1.0\) and claims a “3–5σ realistic” range, but numerically \(|f_{\rm NL}|/\sigma \approx 4.375\), which is ~4.4σ, not a broad 3–5σ interval; the lower end of that range is never derived.  
• In Sec. XIII and the abstract, this 3–5σ range is presented as a single “realistic” significance without clearly distinguishing between (i) Fisher‑ideal σ from external Heinrich et al. , (ii) internal Fisher forecasts from an unpublished Paper II, and (iii) further heuristic degradations (GR projection, \(b_\phi\) uncertainty, photo‑z), each of which corresponds to a different underlying null procedure and covariance structure. These σ values are not directly comparable.  
Required fix:  
• Recompute and explicitly show each step in turning \(f_{\rm NL}=-35/8\) and \(\sigma(f_{\rm NL})\) into a quoted significance, including how the template‑overlap factor \(r\) and additional degradations enter (e.g. \(\sigma_{\rm eff}=\sigma/r\) or \(f_{\rm NL}^{\rm eff}=r f_{\rm NL}\)). If you cannot justify a 3–5σ band purely from the numbers in this paper, narrow the quoted range (e.g. “\(\sim4\sigma\)” for \(\sigma(f_{\rm NL})\approx1\)) or remove the range entirely.  
• Whenever you juxtapose σ values from different pipelines (Heinrich et al.’s Fisher, your own Fisher, and a heuristic GR+photo‑z degradation), add an explicit statement that these are *not directly comparable* null procedures and that the 3–5σ language is illustrative rather than a rigorous combined forecast.  
• In the abstract and Table I caption, either (i) present only the externally verifiable Heinrich et al. \(\sigma(f_{\rm NL})\approx0.7\) and a single derived nominal significance \(|f_{\rm NL}|/\sigma\) or (ii) move the 3–5σ language into a footnote clearly labeled as depending on unpublished internal forecasts.  

P1A-E17  
Section: Abstract, p.1; Sec. X (Statement and Proof), p.14; Sec. IX N, p.14; Sec. I A point 1, p.3–4  
Problem (abstract faithfulness; internal cross‑reference): The abstract calls the central result a “perturbation‑transparency theorem” and states that “torsion vanishes at all perturbation orders, [the Holst dual] reduces … to a total derivative … and the Holst sector therefore decouples from all scalar/tensor perturbation equations of motion,” pointing to Sec. X for the proof. In the body, Sec. X’s “Proof (Scalar Sector)” consists of five short bullet points relying on the classical Einstein–Cartan algebraic relation and on the statement that the Pontryagin density is a total derivative; there is no explicit equation‑level derivation of the quadratic and cubic actions, no decomposition \(\Gamma=\bar\Gamma+K\), and no variation of the Holst action on a perturbed FRW background, as would be expected for something presented as a theorem at PRD level. The text itself partially acknowledges this in Sec. IX (Barrier 14) by calling it an “observation” and defers a full operator‑level analysis. This mismatch between the strength of the abstract (“theorem” with all‑order statement) and the limited derivation in Sec. X is an abstract‑faithfulness issue.  
Required fix:  
• Either upgrade Sec. X to include a full, explicit derivation at the level described in your own scope discussion (connection split, algebraic solution for torsion, explicit demonstration that the Holst term contributes only boundary terms to the quadratic/cubic actions), or  
• Downgrade the language in the abstract and in Sec. I A point 1 to “we argue” or “we provide evidence that” rather than “theorem,” and explicitly state that a complete operator‑level proof is left to future work. Make sure Sec. IX N (Barrier 14) and Sec. X use consistent terminology: if the result is not proven at the level of a theorem, avoid wording that would suggest a formal proof has been given.  

P1A-E18  
Section: Abstract, p.1; Sec. III B, p.8; Sec. V, p.11; Sec. XIV B, p.17; Table III, p.16  
Problem (unsupported novelty; abstract faithfulness; cross‑paper dependency): The abstract states “Galaxy spin asymmetry: a confirmed null” and the body calls the galaxy spin channel “a confirmed null” that “refutes Shamir’s claimed 3% asymmetry at high significance,” using this as a key ingredient in the barrier catalog (Barrier 13 and the spin channel discussion). All quantitative details (classifier architecture, training, debiasing, exact dipole amplitude and p‑value) are relegated to an in‑preparation “Paper IV” and are not summarized here. The Data and Code Availability section links to a GitHub repo but does not specify whether that repository includes the trained network weights, data splits, and scripts needed to reproduce the spin‑dipole null result, and the text explicitly says MCMC and spin results are “reported in Paper I(b)” and “Paper IV” respectively. This makes the “confirmed null” language in the abstract stronger than what is actually documented in this paper.  
Required fix:  
• In the abstract and Sec. III B, replace “confirmed null” by a formulation that reflects the evidence actually provided here, e.g. “consistent with a null dipole in existing independent analyses; our own ViT‑based analysis (documented in a companion paper) also finds no significant dipole.”  
• Add at least a concise numeric summary in this paper: quote the measured dipole amplitude \(A_0\), its uncertainty, and the test statistic/p‑value used, so that readers can assess the claim without needing to access an unpublished companion.  
• In the Data and Code Availability section, explicitly list which spin‑analysis components (trained model, catalog, scripts) are in the GitHub repository and which are only in the companion paper; if the repository is insufficient on its own to reproduce the spin‑dipole null, state that clearly and adjust the language about “confirmed null” accordingly.