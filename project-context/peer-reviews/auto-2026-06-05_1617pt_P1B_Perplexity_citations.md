# P1B auto-2026-06-05_1617pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12628 chars)
**Wall time**: 85.2s

---

P1B-E1 (ESSENTIAL)  
Section: References, p. 9–10  
Problem: Multiple references are labeled “(in preparation)” with internal report IDs (e.g. “[1] H. Golden, Structural Closure of Einstein–Cartan–Holst Dark Energy: …, (in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume.”; similarly [4]–[6]). These do not correspond to any public arXiv entry, DOI, or accepted PRD article as of now, and “this volume” is internally referential rather than a real journal citation. They are being used as if they are established literature (e.g. Paper I(a) is the main physics paper underlying the present “verification companion”). This is not acceptable for PRD: the main claims the companion is supposed to “verify” rest on a non‑public, non‑archived manuscript.  
Required fix: Either (i) ensure that each of these “in preparation” companion papers is publicly available in a stable form (arXiv or accepted journal) and update the references with correct bibliographic metadata (journal, year, arXiv ID) or (ii) remove all dependence on unpublished work from the claims in this paper and rewrite to stand on peer‑accessible, archived references only. The companion paper here cannot be published as a freestanding PRD article if its primary target (“Paper I(a)”) is not simultaneously accessible.

---

P1B-E2 (ESSENTIAL)  
Section: References –, p. 9–10  
Problem: Reference  “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].” and reference  “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].” both cite 2025 papers with arXiv IDs starting “2507…” and “2503…”. These IDs are not yet assigned and cannot be verified on arXiv or NASA ADS. They are effectively future‑dated placeholders.  
Required fix: Replace these entries with real, verifiable references. If these are intended to cite private drafts or anticipated DESI DR2 papers, they must not be given fabricated arXiv identifiers or journal/volume/page information. Either cite the actual current DESI DR2 papers (with correct arXiv IDs and journal metadata) or clearly mark them as “private communication” without arXiv/volume/page, and do not quote numerical results unless they can be traced to publicly available documents.

---

P1B-E3 (ESSENTIAL)  
Section: References [3], p. 9–10  
Problem: Reference [3] is “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” This again uses a future‑dated arXiv ID “2509.13654” and year 2025. There is no such arXiv entry or ADS record as of now; the only ACT DR6 birefringence paper currently present is a 2024/2025‑era draft without that ID, so this is fabricated metadata.  
Required fix: Correct this entry to the actual ACT DR6 birefringence preprint (use its real arXiv:YYMM.NNNNN and year) once it exists, or remove claims that rely on it. You cannot fabricate a future arXiv ID, year, and title and present them as a reference.

---

P1B-E4 (ESSENTIAL)  
Section: References , p. 9–10  
Problem: Reference  “DESI Collaboration, A. G. Adame, et al., DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations, arXiv preprint (2024), arXiv:2404.03002 [astro-ph.CO].” partially matches the real DESI 2024 BAO paper, but the title is altered (“DESI 2024 VI” instead of the actual numbering in the DESI series) and the authorship string is incomplete/incorrect compared with the arXiv version. The paper cited in Table II as “DESI DR2 BAO” is also not yet the 2025 DR2 paper but DR1/2024‑era; there is a mismatch between the “DR2” wording in the body and DR1 metadata in the reference.  
Required fix: Correct the title, collaboration tag, and series numbering to match the actual arXiv:2404.03002 paper as on arXiv.org, and make the DR1/DR2 status consistent between body and bibliography. If the cosmological results in Table II are claimed to be DESI DR2, they must correspond to a specific, public DR2 paper; otherwise rename to DR1 and adjust the text accordingly.

---

P1B-E5 (ESSENTIAL)  
Section: Abstract, p. 1; Sec. III/Table I, p. 3; Sec. V A, Table II, p. 4  
Problem: The abstract claims “Cobaya v3.6.1, 309,189 frozen samples across two converged dataset combinations” and quotes H0 and ΔNeff errors. In footnote 1, the chain accounting is convoluted and internally inconsistent: the text variously states 176,240 + 132,949 raw samples, 216,432 post‑burn‑in, “119,617 post‑burnin samples” in Fig. 1, and “123,129” vs “123,368” for the full‑tension subset, with admission of earlier miscounts. These numbers do not line up cleanly, and there is no check that the reported posterior means/σ are unaffected by the inconsistent effective sample counts.  
Required fix: Provide a clear, single accounting of the raw, post‑burn‑in, and effectively thinned sample sizes for each chain and for the combination, and verify (with a simple calculation) that the quoted means and standard deviations in Table I are stable to thinning and burn‑in choice. Remove contradictory numbers (e.g. 119,617 vs 123,129 vs 123,368) and state one consistent set. The abstract’s “309,189 frozen samples” must match the internal accounting exactly.

---

P1B-E6 (ESSENTIAL)  
Section: Table II caption and body, p. 4  
Problem: The w0, wa “σ” values and the significance statements: the table gives w0 = −0.8122 ± 0.0436 and claims “(marg.-tail, +4.3σ)” departure from w0 = −1. For a Gaussian, \(|-0.8122+1|/0.0436 ≈ 4.3\), so this is arithmetically fine. However, the text then uses the same σ language to describe joint departures, “w0 + wa = −1.4788 ± 0.1485 phantom-crossing required”, and says “w0 departs by +4.3σ and wa departs by −3.6σ, with w0 + wa = −1.48 ± 0.15 requiring phantom crossing.” There is no explicit statement that the 1D “σ” distances and the “phantom crossing required” phrasing are not a Bayes factor or frequentist p‑value; the notation “σ” is used in a way that could be read as a statistical significance test against ΛCDM. PRD generally requires extreme clarity when σ is used for posterior distances versus hypothesis rejection.  
Required fix: Explicitly state, in the caption or immediately adjacent text, that these “σ” values describe 1D posterior means relative to ΛCDM under an approximate Gaussian assumption and are *not* to be interpreted as Bayes-factor or frequentist hypothesis‑test significances. Clarify that “phantom crossing required” is a descriptive statement about the posterior mean trajectory and not a high‑significance detection of w < −1 at any particular redshift.

---

P1B-E7 (ESSENTIAL)  
Section: Sec. VI, Eq. (3) and surrounding text, p. 6–7  
Problem: The birefringence calculation uses \( \beta ≈ (α_{\rm EM} C_{aγ}/(4π)) (Δϕ/f_a)\). The text plugs in “For Caγ = 8, θi = 1, m ≈ 2H0: β ≈ (αEM×8)/(4π) × 1.07 ≈ 0.29°.” The units are inconsistent: αEM, C_aγ are dimensionless, Δϕ/f_a dimensionless, so β should be dimensionless (radians). The conversion to degrees (0.29°) is not shown and the factor 57.295… is not present in the equation. Similar numeric claims “β ≈ 0.17–0.43°” and the derived Caγ ∆ϕ/f_a ≈ 10.3 are not explicitly derived step‑by‑step, making it impossible to verify quickly from the printed numbers.  
Required fix: Rewrite the birefringence formula explicitly in radians, including the conversion to degrees: e.g. \(\beta_{\rm deg} = (180/π) (α_{\rm EM} C_{aγ}/(4π))(Δϕ/f_a)\). Show the arithmetic for the fiducial case and for the conversion from β = 0.342° (i.e. 5.97×10⁻³ rad) to Caγ ∆ϕ/f_a = β / (αEM/(4π)). Confirm that the intervals quoted (0.17–0.43°; 9–51 for Caγ) are computed from *correlated* samples of (Caγ, m/H0, θi) rather than by independent extrema, and document that explicitly.

---

P1B-E8 (ESSENTIAL)  
Section: Sec. VI, footnotes 4–5 and main text, p. 7–8  
Problem: The spectator‑status discussion states that “the spectator-consistent corner θi ∼ 0.1 … requires a ∼ 25× fine-tuning of the misalignment initial condition relative to the natural prior midpoint θi ∼ 0.5”, but in the body the envelope scan is reported over θi ∈ [0.5, 2], and the MCMC prior is uniform over this range. The text thus references a spectator‑consistent θi ≈ 0.1 that lies outside the prior range actually used in the ALP‑MCMC. Yet statements such as “the model accommodates the observed signal for natural parameter values (taken at scan-prior midpoint values; the ~25× misalignment tuning required for the headline result is disclosed…)” conflate results from the θi ∈ [0.5, 2] prior with hypothetical θi ~ 0.1 points never sampled.  
Required fix: Make the distinction between the scanned prior range and the hypothetical spectator‑consistent region explicit. You must not imply that the MCMC posterior supports θi ∼ 0.1 if the prior was θi ∈ [0.5,2] and the sampler never explores θi = 0.1. Either (i) rerun the ALP‑MCMC with a prior that includes θi ∈ [0.1, 2] and report the resulting posterior constraints, or (ii) restrict statements about “spectator‑consistent corners” to analytic back‑of‑envelope estimates, clearly separated from the sampled posterior results.

---

P1B-E9 (ESSENTIAL)  
Section: Sec. IV “Data Methods: CMB E-B Analysis”, p. 5  
Problem: The pipeline SNR numbers (20.32, 25.71) are introduced as “pipeline‑recovery SNR,” and earlier disclaimers emphasize that these do not represent sky measurement significance. However, later summary language (“SNR consistent with the ACT-noise floor”) risks conflating them with real data SNR, and their computation is not shown (e.g. is SNR = β̂/σ_β_MC? how is σ_β_MC estimated across 500 realizations?). Without explicit definition, these σ numbers are not reproducible or verifiable from the text.  
Required fix: Define the SNR explicitly (e.g. SNR = β̂_injected / σ_β from MC ensemble) and provide the numeric σ_β values used to obtain 20.32 and 25.71. Clarify again, where the numbers appear, that these are *purely* MC pipeline‑validation SNR values and not sky detection significances. Ideally, add a small table listing β_inj, mean β̂, scatter, and SNR so they can be recomputed by a reader.

---

P1B-E10 (ESSENTIAL)  
Section: References [2], , , p. 9–10  
Problem: Several quoted statistics must be traceable to the cited papers’ abstract or tables:

- [2] Eskilt & Komatsu PRD 106, 063503, arXiv:2205.13962: The paper’s joint WMAP+Planck value is indeed β = 0.342° ± 0.094° (3.6σ), but the footnote and text describe this as “Planck PR4/NPIPE + WMAP9,” whereas the published PRD paper actually uses Planck PR3 + WMAP9; the PR4/NPIPE likelihood code is in a later GitHub update.[2] This mixes pipeline versioning with the peer‑reviewed publication; the PDF text is ambiguous on what dataset the 3.6σ value corresponds to.  
-  Diego‑Palazuelos et al. (Planck PR4 NPIPE) is correctly cited for β = 0.30° ± 0.11° but described as “Planck NPIPE (PR4)” whereas the original abstract’s language and naming convention should be matched exactly.  
-  Fujita et al. 2021 (PRD 103, 043509) has specific ALP parameter choices; the current paper references them but does not clearly map the chosen (m/H0, fa, Caγ) envelope to the examples in Fujita et al.  

Required fix:  
– For [2], clearly separate the published 3.6σ result (Planck PR3+WMAP9) from any internal re‑runs using a PR4/NPIPE likelihood code, and ensure all references to “PR4/NPIPE joint WMAP+Planck value” are corrected to match what is actually published. If you use PR4/NPIPE internally, report those as independent reanalyses, not as the “published PRD value.”  
– For , ensure title, dataset description, and β value exactly match the journal article’s abstract and main result.  
– For , either specify the exact parameter choices you took from Fujita et al., or remove the suggestion that the current ALP parameter range is directly “studied by Fujita et al.” unless you can point to explicit ranges in their paper.

---

P1B-M1 (MAJOR)  
Section: Entire manuscript; Figures (corner plot) and Tables I–II  
Problem: No explicit units on axes in the rendered corner plot (Fig. 1) are visible in the provided text; “H0” is plotted but the caption only states “H0 [km/s/Mpc]” in Table I, not on the figure itself. For parameters like ΔNeff, σ8, S8, ns there is no unit, which is acceptable, but for H0, Ωm, etc., PRD typically expects an explicit unit on the figure axis, not only in a caption elsewhere. Furthermore, Fig. 1’s sample count “119,617 post-burnin samples” conflicts with the footnote 1 chain accounting (see P1B‑E5).  
Required fix: Ensure that every axis in Fig. 1 includes units where relevant (e.g. “H0 [km/s/Mpc]”), and correct the sample count in the caption to be consistent with the clarified chain accounting. If the figure is generated via GetDist, add explicit axis labels in the plotting script.

---

P1B-M2 (MAJOR)  
Section: Sec. V “Cosmological Fits and Model Comparison”, p. 6  
Problem: The paper sets up a w0–wa quintom analysis based on a DESI DR2 + Planck + SN likelihood stack and reports Table II with detailed numbers, but the main focus of the manuscript is ostensibly “technical verification” of an ECH spin‑torsion program and a ΛCDM+ΔNeff MCMC proxy. The w0–wa analysis is only tangentially related and is not fully documented (e.g. no priors, no full parameter list in the main text, and only a brief pointer to “companion data repository”). For PRD, a 2‑page‑equivalent w0–wa result set without model‑comparison metrics (ΔAIC, ΔBIC, ln B) feels partially developed and may distract from the paper’s stated aims.  
Required fix: Either significantly expand the w0–wa analysis to meet PRD standards for a cosmological DE constraints paper (full parameter list, priors, robustness checks, model comparison statistics) or trim this section down to a brief pointer and move the full results to another dedicated paper. For a “technical companion” focused on spin‑torsion and ΔNeff, the present level of detail on quintom DE is not well balanced.

---

P1B-M3 (MAJOR)  
Section: Abstract and Sec. I “Introduction”, p. 1–2  
Problem: The abstract claims “Three analyses are documented” and then lists (1) ΛCDM+ΔNeff proxy, (2) NaMaster pipeline validation, (3) ALP consistency check. However, the body of the paper also incorporates substantial material on a w0–wa quintom posterior (Table II, Sec. V) and on a DESI DR2 cosmology chain, which are not mentioned in the abstract’s “three analyses” enumeration. This makes the abstract incomplete: key results appearing later (phantom crossing, tension with ΛCDM) are not summarized or even acknowledged in the abstract.  
Required fix: Update the abstract so that it accurately reflects all major analyses and results contained in the paper, including the w0–wa DESI DR2 + Planck + SN fit, or else move that material out. PRD expects the abstract to summarize the main scientifically substantive contributions, not just a subset.

---

P1B-M4 (MAJOR)  
Section: Sec. VII “Conclusions” and Appendices, p. 7–9  
Problem: The paper uses substantial internal “project” language: “P1A”, “Paper II [4]”, “Paper III [5]”, “P1B” (in Table III), “this volume”, “companion paper,” and internal report IDs like “hUBIFY-2026-002”. This is internal‑project bookkeeping, not standard PRD referencing. For a standalone journal article, every reference must be a conventional literature citation (journal or arXiv), and cross‑references to other papers must use their actual bibliographic info, not internal code names.  
Required fix: Remove P1A/P1B/Paper II–IV internal tags and replace them with standard citations (journal, year, arXiv ID). Do not refer to “this volume” unless this is a confirmed PRD special issue and you have precise bibliographic details. Internal report IDs (hUBIFY‑…) should not appear in the published reference list.

---

P1B-M5 (MAJOR)  
Section: Acknowledgments, p. 8  
Problem: The acknowledgment explicitly notes “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation. All scientific claims, derivations, numerical results, and bibliographic attributions were independently verified by the author.” This is informative but raises a verifiability concern for a “technical verification companion” whose primary role is to provide independent audit. Given the demonstrated problems in chain accounting and references in this very draft, the claim of “independent verification” is not supported. PRD will expect greater care in describing the role of AI assistants.  
Required fix: Clarify the specific tasks performed by the AI tool (e.g. code scaffolding, plotting) and state clearly that all numerical and bibliographic claims have been cross‑checked by the author using primary sources. Remove global statements of “independent verification” unless they can be defended (which the current citation errors contradict).

---

P1B-M6 (MAJOR)  
Section: Appendix C: ALP-MCMC Sampled Parameters, p. 9  
Problem: The ALP‑MCMC description gives only a sketch of the priors and likelihoods. For example, Caγ is held fixed at {4, 8, 12} in three separate runs, but it is not clear how these runs are combined to produce the quoted βALP = 0.336° ± 0.107°; likewise, the total “9,720 accepted samples” are mentioned without stating the burn‑in fraction, sampler configuration, or convergence diagnostics beyond a single R̂ threshold. For a cosmology methods paper in PRD, this is marginal: a reader should be able to reproduce the MCMC numerically from the description alone, without relying on external code.  
Required fix: Provide explicit details of the ALP‑MCMC: priors with exact numerical ranges, sampler step sizes or covariance adaptation, burn‑in length, how the three Caγ runs are aggregated (or not), and how βALP and βfree statistics are estimated (e.g. from posterior histograms vs. Gaussian fits). Consider adding a small table summarizing each configuration separately.

---

P1B-M7 (MAJOR)  
Section: Length and scope of the paper  
Problem: For a paper that is explicitly a “technical verification companion,” the manuscript is relatively long and includes multiple side‑tracks (quintom w0–wa results, future DESI DR2 data, ALP forecasts) that partially duplicate or anticipate material meant for “companion papers” [1], [4]–[6]. Many of these topics are not essential to a narrow verification of the ΔNeff proxy run and the NaMaster pipeline.  
Required fix: Tighten the manuscript significantly. A focused PRD “methods/verification” companion could be kept to roughly 6–7 journal pages (excluding appendices), concentrating on: the ΔNeff proxy MCMC (setup, validation, corner plots), the NaMaster pipeline bias characterization, and a *brief* ALP consistency check. Remove forward‑looking or speculative material that is primarily relevant to other companion papers.

---

P1B-N1 (NIT)  
Section: Title page and Section headings, p. 1–2  
Problem: Section headings include parenthetical clarifications like “(Not a Spin-Torsion Theory Module)” embedded in the Contents block in a visually awkward way; the “Contents” list also appears slightly corrupted (“Contents (Not a Spin-Torsion Theory Module) 2”). This looks like a typesetting artifact.  
Required fix: Clean up the Contents and section headings so that only section titles appear there, and scope clarifications appear in the body text rather than inside the table of contents.

---

P1B-N2 (NIT)  
Section: Main text, multiple locations  
Problem: Some phrases are slightly awkward or repetitive, for example: “This is a methodology cross-check, not a competitive sky measurement; the primary observational evidence for cosmic birefringence remains the published Planck/ACT DR6 2.4–2.9σ measurements. The pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements.” Similar clarifications are repeated many times.  
Required fix: Streamline the prose by consolidating repeated caveats into a single, clear statement in each section and avoiding redundant reiteration.

---

P1B-N3 (NIT)  
Section: Table III “Claims classification”, p. 10  
Problem: Table III mixes “Claim type” entries such as “Scope” and “Defn.” with “MCMC” and “Lit.” without explaining the taxonomy. For a PRD reader, a “claims classification” table is unusual and the categories are not self‑explanatory.  
Required fix: Either remove the table (its content is mostly redundant with the text), or add a brief legend explaining what “MCMC”, “Lit.”, “Scope”, “Defn.” mean, and ensure that every classification is clearly motivated.

---

P1B-N4 (NIT)  
Section: Various footnotes, p. 2–8  
Problem: Some footnotes are written in an informal, conversational tone (“reviewer concerns,” “catastrophically fails,” “canonical Hubble-tension result,” capitalization like “RETAINED” in all caps). This is stylistically out of step with PRD norms.  
Required fix: Edit footnote language to standard formal scientific prose, remove conversational asides, and avoid all‑caps emphasis.

---

## Summary recommendation

REJECT

The manuscript exhibits multiple serious issues in citation integrity (fabricated/future arXiv IDs, “in preparation” anchor papers, inconsistent mapping between dataset descriptions and published references) and internal numerical accounting (inconsistent chain sample counts, incomplete definition of pipeline SNR and ALP parameter ranges). Since this is explicitly a “technical verification companion,” such problems are particularly problematic: the paper does not yet meet PRD standards for reproducibility, bibliographic rigor, or scope focus. Substantial re‑structuring and clarification, plus replacement of all future/placeholder references with real, verifiable literature, would be required before reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E11 (ESSENTIAL)  
Section: Sec. III, footnote 1; Fig. 1 caption; Abstract; Table I  
Problem: The chain accounting is still internally inconsistent even after the attempted reconciliation. The footnote claims “176,240 × 0.7 ≈ 123,368 post‑burnin (the 119,617 figure in Fig. 1 reflects additional getdist effective-sample weight-based thinning…); the post-burnin count … is 123,129 (within ±1% of the 123,368 exact computation, with the small offset reflecting chain-end-truncation…).” These numbers cannot all be true simultaneously: 176,240 × 0.7 = 123,368 exactly, so “123,129” is not “within ±1% of 123,368” (it differs by ~0.19%; that is within 1% but then “exact computation” is misused). More importantly, the Abstract’s claim “309,189 frozen samples across two converged dataset combinations” conflates “raw accepted samples” (176,240 + 132,949) with “post‑burn‑in” counts used in Fig. 1, and the Planck‑only run (114,992 samples) is inconsistently described: the paragraph says “reported separately in Table I, and is not aggregated into the frozen headline,” yet Table I has only two combos and no Planck‑only column. The reviewer cannot reconstruct a single coherent set of: (i) raw samples per chain, (ii) burn‑in fraction applied, (iii) post‑burn‑in counts used in any posterior.  
Required fix: Do a single pass, from the actual chain files, to produce a small table listing for each dataset combination: number of chains, raw samples, burn‑in fraction, post‑burn‑in samples, and (if applicable) any extra thinning in GetDist. Ensure that: (a) the Abstract’s “309,189 frozen samples” corresponds exactly to a particular stage (raw or post‑burn‑in) and combination; (b) the numbers quoted in footnote 1 and Fig. 1 match this accounting exactly; (c) the Planck‑only run either appears in Table I with its real sample count or is removed from that table description. Remove the “≈… within ±1%… exact computation” language and replace with the exact counts you actually used.

---

P1B-E12 (ESSENTIAL)  
Section: Sec. III (MB–H0 joint‑posterior check), p. 4  
Problem: The H0 tension significance is numerically inconsistent. You state that the full‑tension chain returns “H0 = 67.69 ± 1.06 km/s/Mpc … exhibiting the canonical 3.6σ Hubble tension with Riess H0 = 73.04 ± 1.04 km/s/Mpc,” but computing the discrepancy gives  
\[
\Delta H_0 = 73.04 - 67.69 = 5.35\ \text{km/s/Mpc},\quad
\sigma_{\rm comb} = \sqrt{1.06^2 + 1.04^2} \approx 1.49,
\]
so \(\Delta H_0/\sigma_{\rm comb} \approx 3.6\) is fine.  
However, the MB–H0 constant offset is described as “0.155 mag … ∼3.2σ relative to the chain’s σ_MB = 0.049,” but 0.155 / 0.049 ≈ 3.16, which would indeed be ~3.2σ, yet you then state this “corresponds exactly to the canonical 3.6σ Hubble tension.” The 3.2σ vs 3.6σ discrepancy is non‑trivial: these are different numbers and cannot both be “exactly” the same canonical tension.  
Required fix: Recompute both significances in a single consistent way and report both with correct values. Either: (i) drop the “exactly” language and state that the MB offset corresponds to ~3.2σ while the H0 discrepancy is ~3.6σ; or (ii) recompute using a single joint‑parameter significance definition that yields the same σ for both and document the method. Do not assert exact equality between σ values that are numerically different.

---

P1B-E13 (ESSENTIAL)  
Section: Sec. IV “Data Methods: CMB E–B Analysis”; Equation (1) and surrounding text  
Problem: The SNR numbers (20.32 and 25.71) remain arithmetically opaque. You now state “Injecting … β = 0.27° … recovers β̂NaMaster = 0.238° (pipeline-recovery SNR = 20.32)” and for β = 0.342° “recovers 0.302° at SNR = 25.71,” but you never define σ_β numerically, and a reader cannot verify how 20.32 or 25.71 arise from these numbers. If SNR were defined as β_inj / σ_β, then σ_β would have to be ~0.0133° and ~0.0133° respectively; if instead SNR = (β̂ – 0)/σ_β or (β̂ – β_inj)/σ_β the implied σ_β would differ. Currently the SNRs are just asserted.  
Required fix: Provide the explicit definition SNR = X / σ_β and the numeric σ_β used for each injection, and verify that the numbers 20.32 and 25.71 follow directly from the listed β_inj and β̂. Add a small table in Sec. IV (or Appendix) with columns (β_inj, mean β̂, σ_β, SNR) so a reader can recompute and confirm the SNR values from the printed numbers alone.

---

P1B-E14 (ESSENTIAL)  
Section: Sec. VI, Eq. (3) and adjacent paragraph (birefringence arithmetic)  
Problem: The birefringence arithmetic is still not fully explicit or dimensionally transparent. You now state “For Caγ = 8, θi = 1, m ≈ 2H0: β ≈ (α_EM × 8)/(4π) × 1.07 ≈ 0.29°” and then later compute Caγ(Δφ/fa) ≈ 10.3 using β = 0.342° and α_EM/(4π) = 5.8×10⁻⁴. The intermediate steps are still partly implicit: you never write explicitly that β here is in radians in the formula, then converted to degrees by multiplying by 180/π, and the origin of “1.07” is unclear (Δφ/fa ≈ 1.07 from the ODE, but that is not spelled out). A reader cannot verify that 0.29° follows from the given constants without reconstructing the whole chain themselves.  
Required fix: Rewrite the birefringence part so that:  
– The fundamental formula is clearly in radians, e.g. \(\beta_{\rm rad} = (\alpha_{\rm EM} C_{a\gamma}/(4\pi)) (\Delta\phi/f_a)\), followed by \(\beta_{\rm deg} = (180/\pi)\,\beta_{\rm rad}.\)  
– Show the explicit numeric evaluation for the fiducial benchmark: plug α_EM ≈ 1/137, C_{aγ}=8, Δφ/fa=1.07 and produce β_rad and β_deg step‑by‑step.  
– For the inversion to CaγΔφ/fa ≈ 10.3, explicitly show β_rad = 0.342° × (π/180), then divide by α_EM/(4π).  
This removes any unit ambiguity and allows the reader to verify each quoted number.

---

P1B-M8 (MAJOR)  
Section: Sec. V A vs Table II vs Abstract/Conclusions (dataset naming and DR1/DR2 status)  
Problem: There is a residual inconsistency in how the DESI dataset is described. Sec. V A lists “+DESI 2024 DR1 BAO ” in the dataset combinations, while Table II and multiple places in the prose refer to “DESI DR2 BAO”, “DESI DR2 w0 wa posterior”, and “DESI DR2 + Planck + SN” even though the reference  is the DR1 / 2024 BAO paper (arXiv:2404.03002) with a specific internal series number. The table caption says “DESI DR2 BAO + Planck 2018 NPIPE…” but the bibliography is DR1. This is exactly the DR1/DR2 mismatch your earlier review flagged, but the main text and table have not been fully aligned.  
Required fix: Decide what you are actually using: if the chains in Table II were run with the DR1 BAO likelihood, then all occurrences of “DR2” in Sec. V, Table II caption, and Conclusions must be changed to “DR1” (and the “DR2 results II” reference  updated or removed accordingly). If instead these chains genuinely use a DR2 likelihood, you must point to the real DR2 paper once it exists and correct the reference list; until then, do not label the dataset as “DR2” or cite a DR1 paper as if it were DR2.

---

P1B-M9 (MAJOR)  
Section: Abstract vs Sec. V vs Conclusions (quintom analysis visibility)  
Problem: The Abstract still says “Three analyses are documented” and lists only the ΛCDM+ΔNeff proxy, NaMaster validation, and ALP consistency check. The w0–wa “DESI DR2 w0 wa posterior” analysis, including the 4.3σ and 3.6σ departures and “phantom-crossing required” language in Table II, is now substantial (a full table, detailed discussion, conclusions paragraph), but is still omitted from the Abstract and only briefly telegraphed as “Forward.—A DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR chain has converged…” in the Conclusions. This under‑describes a major result set and misleads readers as to the scope of the paper.  
Required fix: Either (i) treat the w0–wa analysis as a full fourth analysis and summarize its main quantitative result (including the nature of the “quintom-B” preference and the caveat that no ln B is provided) explicitly in the Abstract, or (ii) sharply demote it to a short forward‑looking note (no table, minimal numbers) and remove the strong σ claims from the body. As written, the Abstract is not faithful to the actual content.

---

P1B-M10 (MAJOR)  
Section: Sec. VI vs Appendix C (ALP-MCMC sample accounting and aggregation)  
Problem: Sec. VI states “Dedicated MCMC sampling … (3 configurations, 9,720 total accepted samples) yields: βALP = 0.336° ± 0.107° (Caγ = 8 fixed), consistent with the model-independent fit βfree = 0.344° ± 0.096° (… 9,720 accepted samples across the 3 ALP‑MCMC configurations described in Sec. VI).” Appendix C then clarifies that Caγ is fixed to {4, 8, 12} across three configurations with 3,240 samples each. It is still not clear:  
– How the 9,720 samples across three values of Caγ are used to construct a single βfree constraint.  
– Whether βALP = 0.336° ± 0.107° is obtained from only the Caγ = 8 configuration (3,240 samples) or from some weighted combination of all three.  
– How burn‑in, thinning, and convergence differ, if at all, between the three runs.  
The phrase “9,720 total accepted samples across 3 configurations” is ambiguous about whether those samples are pooled.  
Required fix: Explicitly state, in Sec. VI and Appendix C, for each of the three configurations (Caγ = 4, 8, 12): the number of post‑burn‑in samples, the resulting β posterior mean and σ, and whether they are combined or kept separate. If βALP is quoted specifically for Caγ = 8, state that clearly and give the sample count for that configuration alone. For βfree, clarify whether you reran a separate single-chain fit or pooled the three ALP runs; if the latter, justify that pooling is statistically consistent given Caγ is actually different in each run.

---

P1B-m1 (MINOR)  
Section: Fig. 1 (corner plot) and Table I; axis units  
Problem: While the caption references “H0 [km/s/Mpc]” in Table I, the reproduced Fig. 1 axes as embedded here show only parameter symbols (e.g. “H0”, “Ωm”, “σ8”) with no explicit unit on the H0 axis itself. PRD typically expects units on the figure axis, not only in tables elsewhere. You partly acknowledged this in your previous draft, but the current text still does not confirm that the actual submitted figure has the units embedded in the axis labels.  
Required fix: Ensure the plotting script sets the H0 axis label explicitly to “H0 [km/s/Mpc]” (and any other dimensional quantities as needed) on the figure itself, not just in tables and captions. Update the manuscript to note that units are given directly on the axes.

---

P1B-m2 (MINOR)  
Section: Sec. VI, “Summary-likelihood combination (auxiliary cross‑check)”, Eq. (4)  
Problem: The inverse‑variance combination β_combined = 0.241° ± 0.061° from 0.30° ± 0.11° and 0.215° ± 0.074° is arithmetically correct, but the phrase “(3.9σ)” is ambiguous: it is not stated explicitly whether this is β_combined / σ_combined or some other definition, nor is it contrasted numerically with the 3.6σ headline PR4+WMAP result. A careful reader can infer that 0.241 / 0.061 ≈ 3.95, but the text does not make that clear or explain the slight difference vs 3.6σ.  
Required fix: Add a clarifying sentence such as “The 3.9σ figure is simply |β_combined|/σ_combined and should not be interpreted as a corrected global significance; it differs slightly from the published 3.6σ joint WMAP+Planck value because it ignores shared calibration systematics.” This makes the calculation and its limitations explicit.

---

P1B-m3 (MINOR)  
Section: Appendix C, priors and spectator‑status caveat  
Problem: Appendix C adds clarifications that the θi ∈ [0.5, 2] prior is a “numerical envelope” and that spectator status requires θi ~ 0.1, but the main text of Sec. VI still contains statements like “Across the natural parameter range m/H0 ∈ [1, 3], θi ∈ [0.5, 2]: Δϕ/fa ∈ [0.2, 1.1]” and “the spectator-consistent corner of this envelope (θi ~ 0.1…) requires a ~25× tuning” that may confuse readers about what was actually sampled vs analytically extrapolated. The appendix and main text are now closer, but the main narrative still risks implying that θi ~ 0.1 was part of the sampled posterior.  
Required fix: In Sec. VI, add an explicit pointer to the Appendix C note, and insert one sentence directly after the “spectator-consistent corner θi ~ 0.1” remark stating that θi = 0.1 lies outside the MCMC prior range and that any statements about that corner come from analytic rescaling, not from sampled posterior points.

---

If you address these additional items along with the previously flagged issues, the manuscript will be much closer to PRD’s standards of internal numerical consistency, clarity of scope, and reproducibility.