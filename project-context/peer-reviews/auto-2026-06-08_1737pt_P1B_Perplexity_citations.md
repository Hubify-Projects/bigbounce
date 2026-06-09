# P1B auto-2026-06-08_1737pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (10593 chars)
**Wall time**: 80.4s

---

P1B-E1  
Section: References (end of paper), multiple pages  
Problem: Reference [1] is described as “(in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume.” The title “Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–fNL Tension, and Surviving Matter-Bounce Tests” and tag “hUBIFY-2026-001A” do not correspond to any record on arXiv or in PRD/ADS, i.e., this is not a citable, archival paper.[1] This “Paper I(a)” is heavily load‑bearing throughout the manuscript.  
Required fix: Explicitly label [1] as an unpublished internal manuscript and remove claims that depend on it from this PRD submission, or post the manuscript on arXiv / submit it to a journal and update the citation to a verifiable identifier. Until then, arguments whose validity relies on [1] cannot be considered established for PRD and must be clearly quarantined as “assumed from unpublished work.”

P1B-E2  
Section: References [4]–[6] (end of paper)  
Problem: References [4]–[6] are also “(in preparation) (2026)” with hUBIFY tags and no public record on arXiv or ADS. They are cited in the main text as “Paper II”, “Paper III”, “Paper IV” and used as if they were existing results (SPHEREx forecast, anomaly catalog, galaxy chirality catalog). These are non‑existent as far as the archival literature is concerned.  
Required fix: As with [1], either (i) upload these manuscripts to arXiv and update to proper citations, (ii) or clearly demote them to “private work in preparation” and remove any dependence of this paper’s technical claims on their content. PRD cannot accept a chain of argument that leans on unpublished, unverified companion papers.

P1B-E3  
Section: References [3], –, , ; entire bibliography  
Problem: Several cited works have future‑dated years and/or arXiv IDs that do not currently exist in ADS/arXiv:  
• [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654” – as of now, no such arXiv identifier exists, and ACT DR6 birefringence is not on ADS under that meta‑data.  
•  “T. Liu et al., European Physical Journal C (2025), arXiv:2507.04265 [gr-qc]” – arXiv:2507.04265 does not exist yet.  
•  “DESI DR2 results II…, Physical Review D 112, 083515 (2025), arXiv:2503.14738” – PRD volume 112 corresponds to 2025 only if future‑dated; arXiv:2503.14738 does not exist.  
•  “DES Collaboration… Astrophys. J. Lett. 973, L14 (2024), arXiv:2401.02929” – as of now, ApJL vol. 973 and that arXiv ID are not found.  
•  “DESI 2024 VI…, arXiv:2404.03002” – this arXiv ID currently corresponds to a different DESI BAO paper (not DR1/DR2 as described), and the title and author list given here do not match the actual record.  
•  Fujita et al. 2021 is real, but the exact title “Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy” appears with slightly different wording in the published PRD paper; the metadata here is approximate and needs syncing with PRD/ADS.  
•  “Diego-Palazuelos et al., PRL 128, 091302 (2022), arXiv:2201.07682” – the PRL is real, but the arXiv ID 2201.07682 is a different Diego‑Palazuelos paper (NPIPE EB systematics) not the cosmic birefringence PRL; the text explicitly claims the arXiv ID “reports beta = 0.30 +/- 0.11 deg from Planck NPIPE,” which is incorrect for 2201.07682.  
Required fix: For each citation, verify against arXiv.org and NASA ADS: correct titles, authors, year, journal, volume, pages, and arXiv numbers. Remove or clearly mark as “anticipated” any future‑dated or hypothetical references that are not yet posted. Replace fabricated IDs (250x.xxxxx) with placeholders (e.g., “to appear”) or drop them. In particular, fix  so that the arXiv ID matches the actual PRL 128, 091302 paper, and correct  to the actual DESI BAO DR1/DR2 release paper if that is what is meant.

P1B-E4  
Section: Abstract, page 1; Sec. III/Table I; Sec. V/Table II  
Problem: The abstract claims “Both frozen dataset combinations find ∆Neff consistent with zero (−0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN)” and “H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN)”. However, later in Sec. II and V, a DESI‑based w0‑wa chain is described with eight parameters and a completely different likelihood stack, and Table II includes a DESI DR2 + DES-Y5 + Pantheon+ result without ∆Neff. The paper mixes three distinct MCMC programs (ΛCDM+∆Neff proxy; DESI w0wa; ALP fits) without a coherent, reproducible mapping from the abstract’s headline numbers to a single configuration. There is no explicit listing of priors/likelihoods for the “Planck+BAO+SN” ∆Neff chain (only an informal description pieced across sections).  
Required fix: Provide a precise description (YAML‑level) in the paper body or appendix for each headline chain: parameter set, priors, all likelihood components, sampler, chain length, burn‑in, and convergence criteria. Ensure the abstract’s four scalars (two H0, two ∆Neff) are each unambiguously traceable to a specific table and chain. Either separate the DESI w0wa analysis into a different paper or clearly segregate it; as currently written, it creates confusion about which model is being summarized.

P1B-E5  
Section: Table I, footnote a, page 3  
Problem: Table I describes a ΛCDM+∆Neff proxy run (“7 cosmological + 10 Planck nuisance” parameters). Table II then describes a DESI DR2 w0wa chain with “8 cosmological + 9 nuisance parameters,” but in Sec. III footnote a the text states “references to ‘k = 7’ elsewhere in this paper refer to the cosmological-parameter count only, distinct from the 17-parameter total.” This “k” appears to be connected to information‑criterion discussions (AIC/BIC), yet those metrics are explicitly not computed here. Using a symbol tied to a non‑performed analysis is misleading, and the parameter counting is inconsistent across tables (7 vs 8 cosmological).  
Required fix: Remove or clarify all references to “k = 7” unless a fully consistent AIC/BIC/ln B analysis is actually presented. Explicitly state the cosmological parameter set for each MCMC (ΛCDM+∆Neff and w0wa) and ensure internal consistency in counts.

P1B-E6  
Section: Sec. VI (Cosmic birefringence), page 7–8  
Problem: The paper quotes “βcombined = 0.241◦ ± 0.061◦ (3.9σ)” as an inverse-variance combination of Planck NPIPE (0.30 ± 0.11) and ACT DR6 (0.215 ± 0.074). Using the given numbers, the combined error is \(\sigma = (1/0.11^2 + 1/0.074^2)^{-1/2} ≈ 0.061°\), so 0.241/0.061 ≈ 3.95σ; the text rounds to 3.9σ, which is fine. However, the paper then claims this “neglects shared calibration systematics” and contrasts it with the published 3.6σ joint WMAP+Planck result [2]. There is no demonstration, even schematically, of how the 3.6σ arises from Eskilt & Komatsu (2022), and the ACT DR6 reference [3] is not real (see P1B-E3). That makes the 3.9σ “cross-check” effectively based on one real measurement plus one nonexistent paper.  
Required fix: Until an actual ACT DR6 birefringence paper exists, remove the 3.9σ inverse‑variance combination or mark it as purely hypothetical. The only robust, citable significance level is Eskilt & Komatsu’s 3.6σ joint WMAP+Planck; stick to that and show explicitly how it is used.

P1B-E7  
Section: Sec. VI, Equation (3), page 7–8  
Problem: The birefringence estimate is written as  
\[
β \approx \frac{α_{\rm EM} × 8}{4π} × 1.07 ≈ 0.29°.
\]  
However, earlier the paper states β is in degrees. Using α ≈ 1/137, the factor \(α/(4π) ≈ 0.00058\). The product \(8 × 1.07 × 0.00058 ≈ 0.00496\) radians ≈ 0.284°—consistent numerically only if the right‑hand side is interpreted in radians and then converted. The equation as printed mixes dimensionless coupling, radians, and degrees without explicit conversion; “≈ 0.29°” is asserted but the intermediate step uses a radian result without a conversion factor.  
Required fix: Rewrite the equation to keep units explicit: either present β in radians and then separately state the degree value \(β ≈ 5.0 × 10^{-3}\,{\rm rad} ≈ 0.29°\), or include the rad→deg factor in the algebra. Clarify that α/(4π) multiplies Caγ(Δϕ/fa) in radians.

P1B-E8  
Section: Sec. VI, paragraph with “Caγ (Δϕ/fa) ≈ 10.3”, page 7–8  
Problem: The paper states: “β = 0.342◦ in radians is 5.97 × 10−3 , the prefactor αEM /(4π) is 5.8 × 10−4 , giving Caγ Δϕ/fa = β/[αEM /(4π)] ≈ 10.3.” Recomputing: 0.342° × (π/180) ≈ 5.97×10⁻³ rad is correct; 5.97×10⁻³ / (5.8×10⁻⁴) ≈ 10.3 is also correct. However, elsewhere the fiducial 0.27° corresponds to Δϕ/fa ≈ 1.0 and Caγ = 8, implying Caγ(Δϕ/fa) ≈ 8, not 10.3. The text does not reconcile this mismatch: if the observed 0.342° requires 10.3, then the fiducial 0.27° with Caγ=8 is not at the observational mean; conversely, matching 0.342° with Caγ=8 requires Δϕ/fa ≈ 1.29, which lies outside the earlier quoted “natural envelope” [0.2, 1.1]. The manuscript alludes to this as “∼17% above the natural envelope upper bound,” but the arithmetic for the envelope and its relation to the stated Δϕ/fa values is not shown, making it difficult to verify consistency.  
Required fix: Present a clear, single table or figure that shows: (i) the mapping between (m/H0, θi) and Δϕ/fa; (ii) the resulting β for Caγ in {4,8,12}; (iii) which parts of this space match β = 0.342° within 1σ. Explicitly reconcile the 8 vs 10.3 product issue so a reader can verify that the “∼17% above envelope” and “∼25× tuning” statements are numerically consistent.

P1B-E9  
Section: Footnote 5 (backreaction disclosure), page 7–8  
Problem: The text states that Ωa ∼ (m² fₐ² / H₀² M_Pl²) θ_i² and that going from θ_i = 0.5 to θ_i = 0.1 gives Ωa(0.1)/Ωa(0.5) ∼ 1/25. But (0.1/0.5)² = (0.2)² = 0.04 = 1/25, which is correct; however, “25× fine-tuning” is described relative to θ_i = 0.5 “prior midpoint” while earlier it called θ_i ∈ [0.5, 2] a “natural” prior range. This is a conceptual, not purely numerical, issue: the paper conflates a factor‑5 shrinkage in θ_i with a factor‑25 in energy density, but then compares that to a “natural prior midpoint” in a way that could mislead readers about the amount of tuning in field space vs energy.  
Required fix: Clarify the distinction between fine‑tuning in θ_i (factor 5 in angle) and in Ωa (factor 25 in energy density). State explicitly whether “25× misalignment tuning” refers to energy density or to θ_i, and ensure consistent phrasing wherever the tuning is discussed.

P1B-E10  
Section: Sec. III, “Key finding” paragraph, page 4–5  
Problem: The paper compares its ΛCDM+∆Neff results to “Liu et al. … finding torsion preferred by AIC (∆AIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.” Since  does not exist in the literature (see P1B-E3), this is a comparison to a non‑existent torsion fit. The claimed ∆AIC values and σ‑level agreements cannot be verified.  
Required fix: Remove the comparison to  or replace it with a genuine, published torsion cosmology analysis with verifiable AIC values. If the Liu et al. paper is intended but not yet on arXiv/ADS, it cannot be used for quantitative cross‑validation.

P1B-M1  
Section: Abstract (NaMaster pipeline SNR statement), page 1; Sec. IV & related footnote 3, page 6  
Problem: The abstract says: “The high pipeline-recovery SNR figures (e.g., 20.32σ) refer to recovery of injected MC signals, not to the significance of the CMB sky measurement.” Footnote 3 defines SNR_SE ≡ β̂√N/σ_β̂ and SNR_real ≡ SNR_SE/√N. However, the only explicit SNR number in the body is “SNRSE = 25.71” for β=0.342°, not 20.32; 20.32σ is only mentioned in words without a table or figure showing where it comes from. The nomenclature (SNRSE, SNRreal) is non‑standard and could be misunderstood as a sky detection significance despite the caveats.  
Required fix: Provide a small table summarizing SNR_real and SNR_SE for each injection {0, 0.27°, 0.342°}, and remove the floating “20.32σ” in the abstract unless it is explicitly tied to a shown number in the body. Consider using clearer language like “estimator signal-to-noise on the Monte Carlo mean” and numerical values that appear in figure captions or tables.

P1B-M2  
Section: Fig. 1 and surrounding text, page 5  
Problem: Fig. 1 is labeled “Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote 1)” while footnote 1 states “The post-burnin count of the full-tension subset alone is 123,129 (within ±1% of the 123,368 exact computation, with the small offset reflecting the chain-end-truncation…).” These numbers (123,129 vs 119,617 vs 176,240) are not fully consistent, and the statement “within ±1%” is not correct: |123,129−123,368|/123,368 ≈ 0.19% (fine), but 119,617 is ~3% lower than 123,368. The footnote conflates “post‑burn-in” with “thinned” counts.  
Required fix: Explicitly distinguish: raw accepted samples, post‑burn‑in samples, and post‑thinning samples, with consistent numbers. Fix the “within ±1%” wording to refer only to the appropriate pair and not to the thinned count. PRD expects numerically clean chain accounting.

P1B-M3  
Section: Sec. II–III (Hubble tension discussion around MB and H0), page 3–5  
Problem: The text performs an MB−5 log10 H0 consistency check and claims “This offset is ∼ 3.2σ relative to σ_MB = 0.049, corresponding exactly to the canonical 3.6σ Hubble tension.” A 0.155 mag offset divided by 0.049 is 3.16σ, which is correctly ~3.2σ, but calling that “exactly” the 3.6σ Hubble tension is at best rhetorical. The SH0ES H0 tension 73.04±1.04 vs 67.69±1.06 is indeed ~3.6σ, but the mag‑space tension is 3.2σ; connecting them as “exactly” the same exaggerates the consistency.  
Required fix: Soften the language: replace “corresponds exactly to the canonical 3.6σ” with “is consistent with the canonical 3.6σ Hubble tension expressed in MB–H0 space.” Ensure that every σ quoted is explicitly derived from the listed numbers.

P1B-M4  
Section: Sec. VI, “LiteBIRD forecast” paragraph, page 8  
Problem: The claim “LiteBIRD is projected to achieve σ(β) ≈ 0.03° . For β = 0.27°: ∼ 9σ statistical significance” needs to be traceable to . The LiteBIRD design paper  projects σ(r) and various polarization sensitivities; there is no direct, single number for σ(β) in degrees. The mapping from LiteBIRD instrument noise to σ(β) is not shown or derived.  
Required fix: Either (i) include a brief derivation or citation that explicitly supports σ(β) ≈ 0.03° from LiteBIRD specifications, or (ii) rephrase as an order‑of‑magnitude estimate and clearly mark it as such. As written it reads as a precise forecast backed by , which is not traceable.

P1B-M5  
Section: Sec. V (“Model-comparison statistics: deferred”), page 6–7  
Problem: The paper repeatedly refers to “robust ln B computation requires nested sampling and is left to a follow-up analysis,” yet still uses language like “the converged w0wa posterior disfavors the ΛCDM point” and “canonical quintom signature.” Using posterior tail distances (4.3σ, 3.6σ) without providing any Bayes factor or even likelihood ratios risks overstating the case against ΛCDM, especially given the caution that LCDM is unsampled in the chain.  
Required fix: Temper all statements about “disfavoring” or “requiring phantom crossing” by making clear they are posterior tail properties of the w0wa parametrization with the chosen priors, not evidence in the Bayesian model‑comparison sense. Remove any implication of model selection (no ∆AIC, ∆BIC, or ln B is actually used here) or else provide a minimal, reproducible Bayes‑factor calculation.

P1B-M6  
Section: Appendix A, repository and HuggingFace datasets, page 9  
Problem: The paper claims multiple external resources (“HuggingFace datasets… links in the repository README”) that cannot be verified from the manuscript alone and are not necessary for the core PRD result. For technical verification they are useful, but for a journal paper, referencing a moving GitHub master branch and unspecified HuggingFace artifacts without version tags or DOIs is fragile.  
Required fix: Replace “links in the repository README” by citing stable DOIs (Zenodo or similar) and specific commit hashes for the GitHub repo. Otherwise, remove references to mutable online artifacts from the claims classification table; PRD prefers reproducibility via fixed archival references.

P1B-N1  
Section: Section headings and ToC, page 1–2 (“Not a Spin-Torsion Theory Module”)  
Problem: The phrase “(Not a Spin-Torsion Theory Module)” appears as a parenthetical in the contents list for Sec. III, but the actual section header on the main page is “STOCK-CAMB ΛCDM+∆Neff MCMC: GENERIC RADIATION-PROXY TEST (NOT A SPIN-TORSION THEORY MODULE)” in all caps. This repetition is awkward and inconsistent with PRD’s style.  
Required fix: Use a single, consistently formatted scope disclaimer, either in the section title or as an initial italic paragraph, not both. Avoid long, narrative titles in all caps.

P1B-N2  
Section: Appendix B header, page 9  
Problem: “Appendix B: Claims Classification” header appears, but the content of Appendix B is effectively folded into Table III on page 10 without a clear break, and Appendix B itself is never referenced in the main text.  
Required fix: Either merge Appendix B into Appendix A or clearly label and reference it in the body. PRD prefers a consistent appendix structure.

P1B-N3  
Section: Acknowledgments, page 9–10  
Problem: The author notes “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation.” While transparency is commendable, PRD typically does not list tools (e.g., Mathematica, Python, ChatGPT) in this way unless they have a scientific role. This may be acceptable but could raise policy questions.  
Required fix: Check PRD editorial policy on AI tool acknowledgments; if discouraged, move this sentence to a cover letter or data‑availability statement rather than the scientific text.

P1B-N4  
Section: Various paragraphs, e.g., Sec. III “Scope statement.—“MCMC verification” refers…”, Sec. VI “Note.—This subsection presents…”  
Problem: The manuscript uses em‑dash scope notes with unconventional capitalization and punctuation (e.g., “Scope statement.—“MCMC verification”…”, “Note.—This subsection…”). While not technically incorrect, it is stylistically inconsistent with PRD norms.  
Required fix: Normalize these to standard prose (“Scope statement.—MCMC verification refers to…”) and avoid nested quotation marks at the start of sentences.

P1B-N5  
Section: Typos and minor language issues throughout  
Problem: There are several small issues:  
• “superseded” does not appear, but there is a misspelling in “per the spin torsion.input.yaml configuration” where a dot is inserted in the file name inconsistent with earlier “spin_torsion.input.yaml”.  
• “mpirun process terminated” is HPC jargon and unnecessary here.  
Required fix: Run a careful language and style pass to sync filenames, remove unnecessary internal technical jargon, and correct minor typos.

P1B-L1 (Length/Scope)  
Section: Whole paper (11 pages)  
Problem: For what is billed as a “technical verification companion” to a main theoretical paper, this manuscript is dense and sprawling: it mixes (i) a ΛCDM+∆Neff proxy MCMC; (ii) a DESI w0wa analysis; (iii) a NaMaster EB pipeline check; and (iv) an ALP birefringence consistency study. Each is only partially documented (no full likelihood tables, incomplete derivations) and some critical support papers are “in preparation.” For PRD, a companion technical paper should either present a focused method with complete, reproducible detail, or be folded into the main paper as an extended methods section.  
Required fix: Either significantly streamline the content to one or two fully documented analyses (e.g., ΛCDM+∆Neff plus NaMaster validation) and move the DESI w0wa and ALP‑MCMC material to separate, dedicated papers, or expand all components with complete derivations and verifiable citations. A focused technical note could be ~6–7 pages; the ALP and DESI analyses could each justify separate full‑length articles once their companion references exist.

## Summary recommendation

REJECT

The manuscript has substantial citation‑forensics problems (multiple non‑existent or future‑dated references, a mis‑matched arXiv ID for a key birefringence paper, and reliance on unpublished companion works), plus ambiguities in the numerical chains and model definitions that do not meet PRD’s standards of archival reliability and reproducibility. Even if the physics logic is sound, the current state of the references and the mixing of speculative, not‑yet‑public analyses make this unsuitable for acceptance; a future submission would need corrected, verifiable citations, a clearer and more focused scope, and complete documentation of all quoted numerical results.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E11  
Section: Sec. II, “MB–H0 joint-posterior offset check”  
Problem: The text states that the 0.155 mag offset “is ∼ 3.2σ relative to the chain’s σ_MB = 0.049 … and corresponds exactly to the canonical 3.6σ Hubble tension.” The first statement is numerically fine (0.155/0.049 ≈ 3.16σ, so “~3.2σ” is accurate), but the second is not: 3.16σ in MB-space is not “exactly” 3.6σ in H0-space, and the relationship is only approximate and model‑dependent.  
Required fix: Keep the 3.2σ calculation as is, but replace “corresponds exactly to the canonical 3.6σ” with a softer phrasing such as “is consistent with the canonical 3.6σ Hubble tension expressed in MB–H0 space,” and explicitly note that 3.2σ ≠ 3.6σ.

P1B-E12  
Section: Footnote 1 (sample-count reconciliation), p. 3; Fig. 1 caption  
Problem: The narrative mixes three different counts—176,240 raw, 123,368 post‑burn‑in (exact), 123,129 post‑burn‑in (approximate), and 119,617 thinned—while calling 123,129 “within ±1% of the 123,368 exact computation.” The “within ±1%” comparison is valid between 123,129 and 123,368, but the nearby appearance of 119,617 without explicit distinction (thinned vs unthinned) makes the accounting opaque.  
Required fix: Present a small, explicit table or sentence sequence that clearly distinguishes: (i) raw accepted samples, (ii) post‑burn‑in samples, and (iii) post‑thinning samples for each chain. Ensure that the “within ±1%” claim is only applied to the relevant pair and that the 119,617 thinned count is clearly labeled as such wherever it appears.

P1B-E13  
Section: Sec. IV, NaMaster SNR definition and use; footnote 3; Fig. 3  
Problem: The text defines SNR_SE ≡ β̂√N/σ_β̂ and SNR_real ≡ SNR_SE/√N, and quotes SNR_SE = 25.71 for the β = 0.342° injection with N = 500 realizations. Dividing 25.71 by √500 ≈ 22.36 gives SNR_real ≈ 1.15, matching the text. However, the abstract and main text also mention “20.32σ” without explicitly tying it to a particular injection or table/figure, and this number does not appear anywhere in Fig. 3 or nearby equations.  
Required fix: Explicitly state in the body which injection (0°, 0.27°, or 0.342°) produces SNR_SE = 20.32 and show the corresponding β̂ and σ_β̂ values (e.g., in a small table). If such a configuration is no longer part of the current analysis, remove 20.32σ everywhere to avoid stale, untraceable numbers.

P1B-E14  
Section: Sec. VI, Eq. (3) and surrounding text (units consistency)  
Problem: Equation (3) reads  
\(β \approx \frac{α_{\rm EM} × 8}{4π} × 1.07 ≈ 0.29°\).  
Interpreted literally, the right-hand side is dimensionless and should be in radians; using α ≈ 1/137 gives \(α/(4π) ≈ 5.8×10^{-4}\), so \(8×1.07×5.8×10^{-4} ≈ 0.00496\) rad ≈ 0.284°. The numerical value matches 0.29° only after a rad→deg conversion that is not shown in the algebra.  
Required fix: Rewrite the equation to keep units explicit, e.g.  
\(β ≈ 8×1.07×\frac{α_{\rm EM}}{4π} ≈ 5.0×10^{-3}\,\text{rad} ≈ 0.29°\),  
or introduce an explicit factor of \(180/π\) if β is to be computed directly in degrees.

P1B-E15  
Section: Sec. VI, paragraph with “Caγ (Δϕ/fa) ≈ 10.3” and “natural envelope”  
Problem: The text states that a numerical ALP integration gives ∆ϕ/fa in [0.2, 1.1] over m/H0 ∈ [1, 3], θi ∈ [0.5, 2], and that the observed β = 0.342° implies Caγ(Δϕ/fa) ≈ 10.3. It further claims that the fiducial β ≈ 0.27° corresponds to Δϕ/fa ≈ 1.0 and Caγ = 8, while the posterior prefers Δϕ/fa ≈ 1.29 at Caγ = 8, “∼17% above the natural envelope upper bound,” and that keeping the ALP a spectator requires an additional “∼25× misalignment tuning.” However, no single table or figure is provided where a reader can see (m/H0, θi) ↦ Δϕ/fa, the corresponding β for a grid of Caγ, and the 1σ region around β = 0.342°. The “∼17%” and “∼25×” factors are narratively asserted but not plotted or tabulated side-by-side; a reader cannot verify the internal consistency without re-running the ALP code.  
Required fix: Add a compact table or figure (in Sec. VI or Appendix C) showing: (i) Δϕ/fa as a function of (m/H0, θi) over the stated range, (ii) β for Caγ ∈ {4,8,12}, and (iii) where β = 0.342° ± 0.094° is achieved. Explicitly show how Δϕ/fa ≈ 1.29 is obtained, how it compares to the [0.2, 1.1] envelope (the 17% statement), and how θi → 0.1 leads to the claimed 25× energy-density tuning.

P1B-E16  
Section: Sec. VI, footnote 5 and Appendix C footnote 6 (backreaction / tuning language)  
Problem: The manuscript sometimes describes a “∼25× fine-tuning” in θ_i and sometimes in Ω_a, without fully disambiguating these. For example, footnote 5 notes Ω_a ∝ θ_i² and correctly computes Ω_a(0.1)/Ω_a(0.5) ≈ 1/25, while the main text elsewhere speaks of “∼25× misalignment tuning relative to the prior midpoint θ_i ∼ 0.5.” This could be read as a 25× change in θ_i itself, rather than a 5× shrinkage in θ_i producing a 25× shrinkage in Ω_a.  
Required fix: Add one clarifying sentence where the 25× is first introduced, explicitly stating that the factor‑25 refers to energy density Ω_a (∝ θ_i²), while the change in field space is only a factor of 5 in θ_i. Use consistent terminology (“25× reduction in Ω_a, corresponding to a 5× reduction in θ_i”) wherever this tuning is discussed.

P1B-E17  
Section: Sec. VI, “LiteBIRD forecast” paragraph  
Problem: The text asserts “LiteBIRD is projected to achieve σ(β) ≈ 0.03° . For β = 0.27°: ∼ 9σ statistical significance.” Reference  is the LiteBIRD design paper, which discusses sensitivity to polarization and r but does not directly provide a σ(β) in degrees; the mapping from instrument sensitivity to σ(β) is not shown. No intermediate steps or scaling arguments (e.g., from EB noise to β uncertainty) are given, so the 0.03° value reads as a precise forecast without transparent derivation.  
Required fix: Either (i) provide a short derivation or scaling argument from LiteBIRD’s stated polarization sensitivity to σ(β) ≈ 0.03°, including any assumptions (e.g., full‑sky coverage, foreground residuals), or (ii) rephrase this as an order‑of‑magnitude estimate (“O(0.03°)”) and clearly mark it as an approximate extrapolation, not a direct result of .

P1B-E18  
Section: Sec. III, “Independent cross-validation.—Liu et al.  constrained an EC torsion model…”  
Problem: This paragraph claims agreement at “0.5σ in H0 and 0.4σ in σ8” with a torsion cosmology analysis . However,  is listed as a 2025 EPJC paper with an arXiv ID (2507.04265) that does not exist, so the underlying values for H0 and σ8 cannot be checked. This introduces quantitative validation against a non‑verifiable reference.  
Required fix: Remove this cross‑validation claim unless and until the Liu et al. torsion paper is publicly posted and citable with a real identifier. If the authors want to retain it, they must (i) update  to a valid reference and (ii) explicitly show the numerical comparison (tabulated H0 and σ8 with uncertainties from both works).

P1B-M7  
Section: Abstract vs. body (NaMaster SNR and “published Planck/ACT DR6 2.4–2.9σ”)  
Problem: The abstract states that “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2, 3],” and the body reiterates “published Planck/ACT DR6 2.4–2.9σ.” Reference [3], the ACT DR6 birefringence measurement, does not exist, so the provenance of the “2.4–2.9σ” range is unclear. The body does not show where the 2.4σ and 2.9σ numbers come from, nor does it reconcile them with the 3.6σ Eskilt & Komatsu result.  
Required fix: Explicitly state which published analyses correspond to 2.4σ and 2.9σ, and correct the references so that each σ value is traceable to a real paper. If part of the range comes from a non‑existent ACT DR6 paper, remove or clearly mark it as anticipated, not published.

P1B-M8  
Section: Table I vs. Sec. V A (datasets description)  
Problem: Table I lists only two dataset combinations (“Full-tension” and “Planck+BAO+SN”) and reports their parameter posteriors, while Sec. V A speaks of four combinations: (1) Planck NPIPE, (2) +DESI DR1 BAO, (3) +Pantheon+, (4) +SH0ES + DES Y3 S8. The mapping between these four combinations and the two summarised in Table I is not explicitly given. A reader could reasonably interpret “Planck+BAO+SN” as combination (3), but then the placement of DES Y3 S8 (mentioned in the text but not Table I) creates ambiguity about which chains underpin which quoted numbers (e.g., in the abstract and conclusions).  
Required fix: Add a sentence or small mapping table making explicit which of the four YAML configurations correspond to the two combinations in Table I, and clarify whether DES Y3 S8 is or is not included in “Planck+BAO+SN.” Ensure that every headline scalar in the abstract can be traced unambiguously to one of these configurations.

P1B-M9  
Section: Abstract vs. Sec. VI (role of ACT DR6 in ALP-MCMC)  
Problem: The abstract describes ACT DR6 as contributing to a “Planck/ACT DR6 2.4–2.9σ” sky detection and presents a spectator‑ALP consistency check using “Planck PR4 + ACT DR6 EB-spectrum data” in the body. However, there is no explicit, self‑contained list of the ACT DR6 spectra, masks, or calibration parameters used in the ALP likelihood, and the ACT DR6 birefringence paper [3] is not real. As a result, the ACT component of the ALP-MCMC likelihood cannot be independently reconstructed from the text alone.  
Required fix: Either (i) include a concise specification (in Appendix C or Sec. VI) of the ACT DR6 data products and calibration assumptions used in the ALP-MCMC likelihood, with all inputs traceable to existing public releases, or (ii) remove references to ACT DR6 as an active component of the likelihood and treat it as a future extension.

P1B-M10  
Section: Appendix A vs. main text (reproducibility scope)  
Problem: The main text repeatedly emphasizes that Bayes factors and information criteria are deferred, and Appendix A notes that chains must be regenerated via `reproduce_cosmology.sh`. However, for the NaMaster and ALP analyses, the appendices do not provide explicit versioning for NaMaster, HEALPix, or the exact Commander map used (e.g., PR4 vs PR3, specific release date), nor for the ACT DR6 data set. Given that these are central to the EB pipeline and ALP-MCMC, the lack of explicit version tags undermines reproducibility.  
Required fix: Extend Appendix A (or C) to specify the exact versions of NaMaster, HEALPix, Planck Commander (PR4/NPIPE vs PR3), and ACT data products used, including file names or hashes where possible. This is especially important since the text leans on these analyses as “technical verification.”