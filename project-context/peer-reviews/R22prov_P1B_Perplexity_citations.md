# P1B R22prov — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (10953 chars)
**Wall time**: 88.8s

---

P1B-E1 (ESSENTIAL)  
Section: References, p. 11–12  
Problem: Self-citation [1] “H. Golden, Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–fNL Tension, and Surviving Matter-Bounce Tests, (in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume.” is listed as an in-preparation manuscript with an internal report number but no arXiv ID, DOI, or journal info. It is heavily relied upon (main structural result, 14-barrier table, predictions) and is treated as “this volume,” i.e., as if formally published. Similar issues for [4]–[6], all “(in preparation)” Golden papers in the same “this volume” bundle.  
Required fix: Either (i) provide public identifiers (arXiv IDs or journal references) and update metadata accordingly, or (ii) explicitly mark these as *unpublished internal companion manuscripts*, remove “this volume,” and sharply limit any load-bearing use of their results in the present paper. PRD does not accept essential claims supported only by inaccessible “in preparation” self-citations; the main ECH results and all cross-paper claims that depend on [1], [4]–[6] must be either removed or supported by published / publicly available arXiv work.

---

P1B-E2 (ESSENTIAL)  
Section: Sec. VI, Spectator ALP consistency check, p. 8  
Problem: The paper claims “69% of the posterior mass falls inside the EOM-required band [9, 51]” for the continuous Caγ prior Caγ ∈ [4, 60] and then uses that to argue consistency between the ALP model and the EOM requirement. However, the text only gives the marginal Caγ statistics “median Caγ = 20.7 with 16–84% range [7.3, 45.6]” and does not show or tabulate the actual fraction of posterior samples in [9, 51]. There is no explicit evidence this 69% number is correctly computed; it is a nontrivial probability statement used to support the main interpretation of the ALP fit.  
Required fix: Add a quantitative check (e.g., a small table or explicit statement) showing the posterior fraction in the Caγ interval [9, 51] from the continuous-prior chain (total samples, count in-band, resulting fraction). If the recomputed value differs from 69%, correct the number and any downstream interpretation.

---

P1B-E3 (ESSENTIAL)  
Section: Sec. III & Table I, p. 3  
Problem: The text states “Both frozen dataset combinations find ∆Neff consistent with zero (−0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN) and H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN…)” while Table I lists “H0 [km/s/Mpc] 67.68 ± 1.06 (full-tension), 67.79 ± 1.09 (Planck+BAO+SN)” and “∆Neff −0.020 ± 0.169, +0.065 ± 0.17.” However, earlier in Sec. III it is said that the Planck-only combination is still sub-converged and *not* included in the 309,189 headline samples. The wording “Both frozen dataset combinations” plus a “third Planck-only combination ongoing” is confusing and risks miscount: the 309,189 number must be strictly the sum of only the two frozen combinations. Footnote 1 tries to clarify but includes multiple inconsistent sample totals (e.g., 176,240 vs 175,545 vs 176,240×0.7 ≈ 123,368 vs 123,129; 119,617 in Fig. 1). As written, a reader cannot unambiguously reconstruct the exact sample counts or verify the chain composition underlying the quoted ∆Neff and H0 means.  
Required fix: Provide a single, internally consistent accounting of chain lengths: list, for each dataset combination, the raw samples, burn-in fraction, post-burn-in samples, and any thinning used for figures. Ensure 309,189 and all other sample counts are arithmetically consistent with these numbers. Remove or correct any conflicting figures (e.g., 175,545 vs 176,240) so that a reader can reproduce the sample-count arithmetic exactly.

---

P1B-E4 (ESSENTIAL)  
Section: Sec. IV, NaMaster pipeline validation & Figure 3 caption, p. 5–6  
Problem: The text states “NaMaster pseudo-Cℓ pipeline validation on the Planck Commander CMB polarization map (Nside = 512, ℓmax = 1024, fsky = 0.32, 500 Monte Carlo realizations): injecting the spectator-ALP fiducial value β = 0.27◦ recovers β̂ = 0.238◦ (pipeline-recovery bias 0.032◦ ).” Later it clarifies “The pipeline-recovery bias is ∆β̂ = 0.032◦ at injection β = 0.27◦ (β̂ = 0.238◦ ) and ∆β̂ = 0.040◦ at injection β = 0.342◦ (β̂ = 0.302◦ ).” The notation “bias 0.032◦” is used for both positive and negative differences (some lines say “0.032◦,” others say “−0.033◦ to −0.034◦”). But the figure caption says “Bias β̂ − βinj is below 0.04◦ …” without specifying sign or direction. This is ambiguous: a bias of +0.032◦ vs −0.032◦ is materially different for an estimator, and the text alternates between absolute magnitude and signed difference.  
Required fix: Make the definition of bias explicit and consistent. For all statements, use either β̂ − βinj or βinj − β̂ with sign, and remove ambiguous references like “0.032◦ bias” that do not specify sign. Update Figure 3 caption to specify, e.g., “|β̂ − βinj| < 0.04◦” if magnitude is intended, and correct the text in the sky-fraction sweep subsection to consistently distinguish between “−0.033◦ to −0.034◦” and “0.032◦” biases.

---

P1B-E5 (ESSENTIAL)  
Section: Abstract & Sec. I/III/V, H0 tension and σ8/S8, p. 1–4  
Problem: The abstract states “Both frozen dataset combinations find ∆Neff consistent with zero … and H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN…)” and that the “stock-CAMB ΛCDM+∆Neff MCMC proxy … is reported as a null-consistency test … not as evidence for or against the ECH spin-torsion framework.” However, in Sec. II the paper states that “The spin-torsion framework alone does not resolve cosmological tensions at the present data precision,” and in Sec. III and V there are multiple qualitative statements about the Hubble tension and σ8/S8 consistency, yet no explicit reconstruction or numeric quantification of σ8/S8 tensions versus key external datasets (e.g., DES Y3, KiDS) is given in this paper beyond the proxy chain means and quoted σ8/S8 errors in Table I/II. The abstract claims are borderline interpretive without the explicit tension statistics (e.g., σ-level discrepancies computed from the presented numbers).  
Required fix: For each tension claim mentioned in the abstract (H0 consistency with ΛCDM, inability to resolve H0 tension, statements about σ8/S8), include in the body a clear numerical comparison (difference in units of combined σ) derived solely from the numbers given in this paper and the cited external values (e.g., Riess H0, DES Y3 S8), with explicit formulas. If such calculations are not provided, the abstract must be rephrased to remove or soften tension claims to purely descriptive statements of the measured parameters.

---

P1B-E6 (ESSENTIAL)  
Section: Global – versioning/round language, p. 1–12  
Problem: The paper repeatedly refers to “Paper I(a) [1]”, “Paper II [4]”, “Paper III [5]”, “Paper IV [6]”, “this volume,” internal IDs “hUBIFY-2026-00x,” and uses “companion paper” language. There is also a “Forward.—A DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR cobaya chain … has converged…” paragraph in the Conclusions that reads like a “current work status” note rather than a completed result. PRD requires the submission to stand alone without reliance on unpublished “companion” manuscripts or internal report labels, and discourages forward-looking version-log prose.  
Required fix: Remove or substantially minimize forward-looking/version-history language (“this volume,” “companion paper” when unpublished, “has converged” future-use statements). Reframe any necessary cross-references to other works as standard citations only when they exist in the public literature (arXiv or journal). Delete internal report numbers (hUBIFY-2026-001A, etc.) unless they correspond to public DOIs or arXiv IDs clearly identifiable by readers.

---

P1B-M1 (MAJOR)  
Section: Sec. VI, eqs. (2)–(3), p. 7–8  
Problem: Equation (3) states “For Caγ = 8, θi = 1, m ≈ 2H0: β ≈ αEM × 8/(4π) × 1.07 ≈ 0.29◦.” The numerical factor 1.07 is not defined in the equation; from context it is apparently ∆ϕ/fa in radians (≈1.07) obtained from the ODE integration (or some averaged value such that Caγ ∆ϕ/fa ≈ 8×1.07 ≈ 8.56). Equation (2) just above quotes “∆ϕ/fa ≈ 0.65 (m = H0 , θi = 1). Across the natural parameter range m/H0 ∈ [1, 3], θi ∈ [0.5, 2]: ∆ϕ/fa ∈ [0.2, 1.1].” The jump from 0.65 to 1.07 for m ≈ 2H0 is plausible but not documented; the reader cannot reconstruct the factor 1.07 from any numbers shown.  
Required fix: Explicitly define and justify 1.07 in eq. (3). Either show an additional line or small table giving ∆ϕ/fa at the benchmark (m ≈ 2H0 , θi = 1) or replace “1.07” with “∆ϕ/fa|m≈2H0 ≈ 1.07” and add a sentence indicating how this value was obtained (numerical integration details or reference to an online table in the repository). This is necessary for dimensional and numerical transparency.

---

P1B-M2 (MAJOR)  
Section: Table II and surrounding text, p. 3–4  
Problem: The text claims “w0 departs by +4.3σ and wa departs by −3.6σ, with w0 + wa = −1.48 ± 0.15 requiring phantom crossing.” Using the quoted means and σ in Table II:  
- For w0: (−0.8122 − (−1))/0.0436 ≈ +4.3, consistent.  
- For wa: (−0.6666 − 0)/0.1864 ≈ −3.6, consistent.  
However, the table and footnote a emphasize that LCDM is *unsampled*, and the 4.3σ and 3.6σ are “marginal-tail posterior-extrapolation” only. The main text, including in the “Physics interpretation” paragraph and Abstract, gives these σ departures in a way that can be easily misread as robust exclusion significances.  
Required fix: At every place where “4.3σ” and “3.6σ” appear in the main text, explicitly qualify them as “posterior tail distances (LCDM point unsampled), not Bayes factors or frequentist significances,” as you already do in Table II’s footnote. The current mixture where some mentions carry the caveat and others do not is inadequate for PRD level clarity.

---

P1B-M3 (MAJOR)  
Section: Sec. II & III, H0 tension discussion, p. 2–4  
Problem: The chain-level explanation for the SH0ES + Pantheon+ + Planck interplay uses the combination “MB − 5 log10(H0) ≈ const” with a numeric evaluation. At the Riess anchor they get −28.571; at the chain mean they get −28.416, difference 0.155 mag. They then assert “This offset is ∼ 3.2σ relative to the chain’s σMB = 0.049 marginal width and corresponds exactly to the canonical 3.6σ Hubble tension.” If you compute 0.155/0.049 ≈ 3.16, so the 3.2σ relative to σMB is fine, but to state that this “corresponds exactly” to the 3.6σ H0 tension is an over-interpretation: the combined-tension significance depends on both σMB and σH0 and their covariance from the full fit, not just σMB.  
Required fix: Rephrase to say that the 0.155 mag difference *is of order* the canonical ~3–4σ Hubble tension, or explicitly demonstrate (using the reported chain H0 constraints and covariance) that this projection into the MB–H0 combination yields 3.6σ. Without that, drop the word “exactly” and soften the identification.

---

P1B-M4 (MAJOR)  
Section: Sec. VI, “EOM-required band [9, 51]” and Caγ prior, p. 8  
Problem: The text states that the “EOM-required coupling-displacement product … gives Caγ ∆ϕ/fa ≈ 10.3 … with ∆ϕ/fa ∈ [0.2, 1.1] from numerical integration, the required Caγ spans ∼ 9 to ∼ 51,” and that this EOM-required band motivates expanding the prior from Caγ ∈ [1,30] to [4,60]. However, the derivation of [9,51] depends sensitively on the range [0.2,1.1]; the paper only describes that range qualitatively as a “joint-trajectory scan” and does not show the mapping between (m/H0 , θi ) and ∆ϕ/fa. Without at least a brief tabulation or figure, the claimed [9,51] looks like an internal calculation that cannot be checked.  
Required fix: Add a small table or figure showing ∆ϕ/fa at the corners of the natural prior box (m/H0 = 1,3; θi = 0.5,2) and the resulting implied Caγ bounds for β = 0.342◦. Alternatively, provide explicit values for ∆ϕ/fa min and max used in the [9,51] derivation (not just the bracket [0.2,1.1]) and a line that computes Caγ,min = 10.3/∆ϕ,max and Caγ,max = 10.3/∆ϕ,min numerically so the reader can verify the 9–51 range.

---

P1B-M5 (MAJOR)  
Section: Global – unsupported novelty/“not distinctive” claims, p. 1, 7–9  
Problem: The paper repeatedly asserts that certain effects are “not a distinctive ECH prediction” and “the same β ≈ 0.27◦ arises in any GR+ALP setup with the same parameters; no ECH-specific derivation connects the Holst action to the photon-torsion coupling required.” It also states that standard-ECH dark-energy routes via extra relativistic species are “not viable as an amplitude-level explanation” etc. These claims of non-uniqueness and non-viability are at the level of novelty/exclusion but are not systematically supported by a survey of competing theories or by citations beyond , . PRD requires that statements of “not distinctive,” “not viable,” etc., be either demonstrably derived in the paper or clearly framed as scope statements rather than general conclusions.  
Required fix: Either (i) soften the language to clearly indicate these are *scope statements for this specific model setup* (“in the specific GR+ALP realization studied here, the same β arises irrespective of torsion; we do not derive a unique ECH signature”), or (ii) provide additional references and/or explicit arguments demonstrating that no currently known torsion model yields a distinguishable birefringence signal for the same ALP parameters.

---

P1B-M6 (MAJOR)  
Section: Sec. IV, “Scope note” and footnote 3, p. 5–6  
Problem: Footnote 3 explains SNRSE and SNRreal for β injections. It defines SNRSE ≡ β̂/SE(β̂) = 25.71 and SNRreal ≡ β̂/σβ̂ ≈ SNRSE/√N. With β̂ ≈ 0.238◦ and N = 500, σβ̂ ≈ 0.026◦, SNRreal ≈ 9.1, not 0.91. However, the text claims “SNRreal ≈ 0.91 (and ≈ 1.15 for the β = 0.342◦ injection).” This is off by a factor of ~10 if SNRSE is indeed 25.71; either the formula or the numeric is inconsistent.  
Required fix: Recompute SNRSE and SNRreal from the MC statistics and correct the numerical values in the footnote. If SNRSE is defined as √N times SNRreal or vice versa, clearly state and consistently apply the convention. At minimum, reconcile the given numbers with the given formula.

---

P1B-M7 (MAJOR)  
Section: Appendix C, “ALP-MCMC results … 9,720 total accepted samples across 3 configurations,” p. 10–11  
Problem: The appendix says “9,720 total accepted samples across 3 configurations,” each with Caγ fixed at {4,8,12} and “3,240 samples per configuration.” 3×3,240 = 9,720, consistent. But in Sec. VI the description of the ALP MCMC and continuous-prior run uses slightly different accepted counts (“9,720 total accepted samples across the 3 ALP-MCMC configurations … 8,955 accepted samples” for the continuous-prior run) without making clear which results in Sec. VI are derived from which of these chains. For example, βALP = 0.336◦ ± 0.107◦ is said to be from “Caγ = 8 fixed,” but it is not explicit if that uses all 3,240 samples or a subset.  
Required fix: Clarify explicitly: for each quoted ALP result (βALP, βfree, Caγ ranges, 69% fraction), specify which chain(s) they are derived from (benchmark fixed-Caγ vs continuous-prior chain) and the exact sample counts used. This level of bookkeeping is expected for MCMC-based papers in PRD.

---

P1B-M8 (MAJOR)  
Section: References [3], , , , p. 11–12  
Problem: Several references are clearly future-dated relative to their nominal arXiv IDs and likely do not exist at the time of writing:  
- [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” arXiv IDs beginning with 2509 correspond to Sept 2025 and cannot currently be verified.  
-  “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang… European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].” Similar issue: 2507 is a future-month arXiv identifier.  
-  “DESI Collaboration… Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].” Again 2503 is a future date; PRD vol. 112 in 2025 is speculative.  
-  “DES Collaboration… Astrophys. J. Lett. 973, L14 (2024), arXiv:2401.02929” – here 2401.* exists as a real arXiv month, but ApJ Letters vol. 973 is far in the future; ApJ volumes are currently much lower.  
These look like speculative future references or placeholders that cannot be verified in arXiv/ADS now. PRD requires references to be to existing, citable works.  
Required fix: Replace these with existing, verifiable references (arXiv IDs that actually exist, volumes/pages that match current journal status) or mark them clearly as “private communication” / “in preparation” and remove volume/page numbers and arXiv IDs that do not yet exist. Any key results that depend on these references must be re-checked against currently published data.

---

P1B-M9 (MAJOR)  
Section: References , p. 11  
Problem:  is “P. Diego-Palazuelos, J. R. Eskilt, Y. Minami, M. Tristram, et al., Cosmic birefringence from the Planck data release 4, Phys. Rev. Lett. 128, 091302 (2022), reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B, arXiv:2201.07682 [astro-ph.CO].” The additional clause “reports beta = …; the value used at L256/L416 of P1B” is internal cross-paper chatter and not standard reference formatting. It also implies dependence on another paper (“P1B”) which may not be accessible.  
Required fix: Remove the internal-commentary part from the reference entry. Leave this as a standard literature citation giving only authors, title, journal, volume, page, year, and arXiv. Any mention of P1B page numbers belongs only in the body text, if at all.

---

P1B-M10 (MAJOR)  
Section: Data and Code Availability & Appendix A, p. 10–11  
Problem: The text points to a GitHub repository and independent HuggingFace datasets as reproducibility material. PRD policies allow code/data repositories but do not recognize them as peer-reviewed sources. However, in this paper, some numerical results (e.g., NaMaster fsky sweep, exact ODE-derived ∆ϕ/fa values) are only described in words and rely on “artifacts” references such as “artifact: reproducibility/p1_namaster_500mc/results/c1_fsky_sweep.json” for verification. This makes it hard to fully verify the quoted numbers solely from the PDF, as required by the instructions.  
Required fix: For every load-bearing numerical statement that is not trivially reproducible from numbers printed in the paper, include enough detail in the manuscript itself to allow independent verification (e.g., give summary tables of key derived quantities, not just mention JSON files). The repository can remain as a supplement, but the paper must be self-contained for numerical checks.

---

P1B-N1 (MINOR)  
Section: Title, Abstract, and throughout, p. 1–2, 7–9  
Problem: The phrase “Spectator-ALP consistency check” and variants are used repeatedly without an explicit definition of “spectator” in the early sections. The true technical condition (Ωa ≪ 1 requiring θi ≪ 1) only appears in Sec. VI and appendix footnotes, not in the abstract or early overview, which could mislead less technical readers.  
Required fix: Add a brief formal definition of “spectator ALP” in the introduction (e.g., a sentence spelling out the Ωa ≪ 1 condition and its relation to θi) and cross-reference the detailed discussion in Sec. VI/Appendix C.

---

P1B-N2 (MINOR)  
Section: Sec. VI, “Caveats” paragraph, p. 8–9  
Problem: The paper states “LiteBIRD is projected to achieve σ(β) ≈ 0.03◦ . For β = 0.27◦: ∼ 9σ statistical significance.” 0.27/0.03 = 9 exactly, but the interpretation “∼ 9σ” assumes Gaussian statistics and negligible systematics;  gives an instrument-noise-level forecast, not including, e.g., foreground systematics. For PRD-level precision this is fine but should be explicitly acknowledged as assuming Gaussian errors.  
Required fix: Add “assuming Gaussian statistics and systematics at or below the forecast level” or similar qualification.

---

P1B-N3 (MINOR)  
Section: Acknowledgments, p. 10  
Problem: The phrase “The author acknowledges the use of Claude (Anthropic) as an AI research assistant…” is fine as transparency, but PRD generally expects acknowledgments to focus on scientific and funding contributions, not product naming. This is not fatal but somewhat nonstandard.  
Required fix: Consider rephrasing to a more generic statement (“… acknowledges assistance from large-language-model tools during analysis; all scientific claims were independently verified by the author.”) if the journal or editors prefer product-neutral wording.

---

P1B-N4 (MINOR)  
Section: Appendix B: Claims Classification, p. 11  
Problem: Table III includes a “Claims classification for this companion paper” with categories “MCMC verified,” “Lit. cited,” “Scope Defn.,” etc., which is internal QA language unusual for PRD articles and may confuse readers (it reads like an internal audit or review log).  
Required fix: Either remove the claims-classification table or move it to a supplementary note, clearly framed as an internal checklist rather than part of the scientific argument.

---

P1B-N5 (MINOR)  
Section: Sec. IV, “Foreground and noise model,” p. 5–6  
Problem: The text says “The Commander map is a foreground-cleaned CMB-only product; no separate foreground component is included.” This is technically imprecise: Commander maps are *component-separated* products and typically retain residual foreground contamination. While the analysis is a pure pipeline validation and not a sky measurement, the “CMB-only” wording is stronger than warranted.  
Required fix: Rephrase to “CMB-dominated component-separated product with residual foregrounds” or similar.

---

P1B-N6 (MINOR)  
Section: Sec. V A, “Reproducibility materials at https://github.com/…”, p. 6  
Problem: The URL is given as a raw full path inline. Some PRD formatting guidelines prefer to avoid full URLs in the main text, using references or footnotes instead.  
Required fix: Move the URL into a footnote or into the Data Availability section only, and make the main text simply refer to “the public repository (see Data and Code Availability).”

---

P1B-N7 (MINOR)  
Section: PACS numbers, p. 1  
Problem: PACS codes are formally deprecated in many journals, including APS, which now prefers keywords. This is a minor style issue.  
Required fix: Check PRD’s current style guide; if PACS are no longer requested, remove or replace with appropriate keywords.

---

P1B-N8 (MINOR)  
Section: Sec. V B, first paragraph, p. 6–7  
Problem: The phrase “The two posterior parameter measurements that remain are ∆Neff = …” is slightly confusing: many more parameters are measured (H0, σ8, etc.) as shown in Table II.  
Required fix: Rephrase to “The two extended-parameter measurements central to this paper are…” to avoid implying that all other parameter results are somehow discarded.

---

P1B-N9 (MINOR)  
Section: Abstract & Sec. III, “null-consistency test” language, p. 1–3  
Problem: “Null-consistency test” is nonstandard jargon; some readers may confuse it with a formal null-test (e.g., χ² of zero signal). Here it just means “posterior consistent with zero.”  
Required fix: Add a brief clarification the first time this phrasing appears, e.g., “by ‘null-consistency’ we simply mean that the posterior for ∆Neff includes zero within 1σ.”

---

P1B-N10 (MINOR)  
Section: Appendix A, “What is NOT included,” p. 10  
Problem: The capitalized NOT and emphasis on missing Bayes factors could be perceived as informal; PRD usually prefers neutral phrasing.  
Required fix: Replace with neutral language (“Bayes factors and information criteria are not computed in this work; they are deferred to future work using nested sampling.”).

---

P1B-N11 (MINOR)  
Section: Eq. labeling, p. 7–8  
Problem: Equations (2) and (3) are presented inline with text and described in words, but the dependence on θi, m/H0, and Caγ is not made explicit in the equation notation.  
Required fix: Consider adding a short explicit expression, e.g., “β(Caγ , m/H0 , θi) = (αEM/4π) Caγ [∆ϕ/fa](m/H0, θi)” to make the parameter dependence transparent.

---

P1B-N12 (MINOR)  
Section: Figure 4 caption, p. 9  
Problem: The caption uses internal code-branch names (“research/branch_R_alp_birefringence/phase2_mcmc/chains/c5_continuous/”) which are meaningless to readers and look like internal bookkeeping.  
Required fix: Remove such paths from the caption; keep only scientific information and, if necessary, a reference to the public repository.

---

P1B-N13 (MINOR)  
Section: Global – length vs contribution  
Problem: For a “technical verification companion” paper whose main ECH theory results are in Paper I(a), this manuscript is relatively long (12 pages) yet still defers core model-comparison metrics (Bayes factors) and lacks some explicit numerical derivations. The contribution is mainly diagnostic and consistency checks.  
Required fix: Consider condensing descriptive prose and internal process commentary (e.g., “earlier reviewer concerns,” “promised a Savage-Dickey ratio,” etc.) to bring the paper to ~8–9 pages. Keep only the essential numerical results, their methods, and key caveats.

---

## Summary recommendation

MAJOR REVISIONS

The manuscript shows care in caveating its claims and attempts to provide reproducibility, but there are multiple essential and major issues: speculative/future-dated references, heavy reliance on unpublished companion papers, ambiguous or internally inconsistent numerical statements (sample counts, SNR, bias sign), and overinterpretation of some σ-level “departures” without fully transparent derivations. These must be corrected and the referencing cleaned up before the paper can meet PRD’s standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E7 (ESSENTIAL)  
Section: Sec. VI, “Birefringence value” paragraph and surrounding text, p. 7–8  
Problem: The numerical envelope and its interpretation are internally inconsistent. The text states that the “prediction spans β ≈ 0.17–0.43° over Caγ ∈ [4, 12], m/H0 ∈ [1, 3], θi ∈ [0.5, 2]” and that this envelope “comfortably” brackets the observed βobs = 0.342°. But a few lines later it says the MCMC posterior “pulls (θi, m/H0) toward the upper edge of the natural-prior box” and implies an effective ∆ϕ/fa ≈ 1.29, which is explicitly above the stated “natural” upper bound 1.1 and described as a 25× fine-tuning regime. As written, the reader cannot reconcile (i) a “natural” theoretical envelope [0.17, 0.43]° supposedly bracketing the observation with (ii) the statement that the data-preferred configuration lies outside the same natural ∆ϕ/fa range and requires fine-tuning.  
Required fix: Explicitly separate (a) the purely prior-driven “natural envelope” for β (derived only from m/H0, θi ranges and Caγ ∈ [4, 12]) from (b) the *posterior-preferred* region once the βobs constraint is imposed. Quantify the fraction of posterior mass that lies outside the stated “natural” ∆ϕ/fa ∈ [0.2, 1.1] band, and revise the wording to make clear that bracketing βobs within [0.17, 0.43]° is a prior-envelope statement, not a data-preferred, naturally realized configuration. Remove or qualify “comfortably” accordingly.

---

P1B-E8 (ESSENTIAL)  
Section: Appendix C & Sec. VI, ALP priors vs. “spectator” definition, p. 7–8, 10–11  
Problem: The introduction and abstract describe the ALP as a “spectator” field and emphasize the Ωa ≪ 1 condition. However, the *actual* sampled prior for θi is uniform on [0.5, 2] in the ALP-MCMC chains, i.e., centered in the regime where Ωa ∼ 1 and the field is not a spectator. The spectator-consistent region θi ∼ 0.1 is not sampled in the model-dependent chains at all and is only discussed in footnotes as a “sliver” requiring 25× tuning. Yet Sec. VI and the Conclusions repeatedly present results under “spectator-ALP consistency,” blurring this important distinction.  
Required fix: Make it explicit in Sec. VI and in the abstract that the *MCMC results* are obtained with a prior that does not enforce spectator status (θi ∈ [0.5, 2]) and thus correspond to a DE‑ALP regime for most of the posterior. Clearly separate (i) the spectator-consistent analytic check at θi ∼ 0.1 (not directly sampled in the benchmark chains) from (ii) the MCMC-based consistency demonstration, and avoid using “spectator” for the latter unless the prior is modified and the chains are recomputed with θi restricted to a genuinely spectator range.

---

P1B-M11 (MAJOR)  
Section: Sec. II, “MB–H0 joint-posterior offset check,” p. 4–5  
Problem: The text claims the 0.155 mag offset “corresponds exactly to the canonical 3.6σ Hubble tension manifesting in the MB axis,” equating 0.155/σMB ≈ 3.2 with the often-quoted 3.6σ tension. The wording “exactly” is too strong: the chain’s σMB includes the full joint fit and covariance structure, and the canonical 3.6σ discrepancy refers to a specific tension computation between SH0ES and Planck H0 constraints. Treating 3.2σ in MB as *exactly* 3.6σ in H0 is not justified without an explicit covariance-based mapping.  
Required fix: Replace “corresponds exactly to the canonical 3.6σ Hubble tension” with wording such as “is of the same order as the canonical ∼3–4σ Hubble tension.” Alternatively, provide an explicit calculation (using the full covariance of MB and H0 from the chain) showing that the joint discrepancy projected along the MB–H0 degeneracy indeed yields 3.6σ.

---

P1B-M12 (MAJOR)  
Section: Sec. II, “Independent cross-validation” paragraph, p. 4–5  
Problem: The cross-validation with Liu et al. is stated as “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8,” but the paper does not provide the Liu et al. central values and uncertainties or show the arithmetic. Without explicit numbers, the claimed σ-level agreement is opaque and cannot be independently checked.  
Required fix: Add the H0 and σ8 mean ±σ values from Liu et al. and from the present work in the text or a small table, and explicitly show the σ-difference calculation (e.g., |H0,this − H0,Liu| / √(σ²this + σ²Liu)). If this information is not added, soften the statement to a qualitative “numerically close” without specific σ values.

---

P1B-M13 (MAJOR)  
Section: Sec. V B “Results” and Table II, σ8/S8 tensions, p. 3–4  
Problem: The Conclusions and Sec. II discuss σ8/S8 in the context of “cosmological tensions,” and Table II gives σ8 and S8 values with small errors. However, nowhere in the body is there an explicit numerical comparison of these σ8/S8 values to external probes (DES Y3, KiDS, etc.) in σ units, nor a clear statement of whether the tension is increased, decreased, or unchanged. This leaves phrases like “cosmological tensions” under-quantified.  
Required fix: For at least one key external dataset (e.g., DES Y3 S8), add a short quantitative comparison: compute the difference between this paper’s S8 and the cited external S8 in units of the combined error and state the corresponding σ-level. Clarify in text whether this represents a significant tension, a mild pull, or consistency.

---

P1B-M14 (MAJOR)  
Section: Sec. IV, Figure 3 vs. main text, p. 5–6  
Problem: The caption for Fig. 3 states, “Bias β̂ − βinj is below 0.04° across the natural resolution range; this is the NaMaster systematic floor adopted in Eq. 1–3.” In the body, however, the sky-fraction sweep paragraph describes the fsky variations as giving “a recovery bias of −0.033° to −0.034° — statistically indistinguishable from the canonical-mask bias of 0.032°,” i.e., mixing signed and unsigned bias. The caption speaks purely about magnitudes, while the text emphasizes signed values without ever clearly fixing a convention. This inconsistency makes it unclear whether the systematic floor used later is an absolute value or a signed offset.  
Required fix: Amend the Figure 3 caption to specify that the 0.04° “systematic floor” is an *absolute* bias, e.g., “|β̂ − βinj| < 0.04°,” and add a one-sentence explicit statement in the body (at the start of Sec. IV or the validation subsection) defining bias as either β̂ − βinj or βinj − β̂, with sign conventions consistent throughout.

---

P1B-M15 (MAJOR)  
Section: Sec. VI, “Summary-likelihood combination (auxiliary cross-check)” and eq. (4), p. 8  
Problem: Equation (4) defines βcombined = 0.241° ± 0.061° (3.9σ) by inverse-variance combining Planck and ACT measurements. The text notes that this neglects shared calibration systematics and overestimates the significance, but then calls 3.9σ an “upper bound on the true significance.” Strictly, ignoring positive correlations does make the combined σ too small, but characterizing the resulting significance as an “upper bound” is ambiguous without specifying what is being bounded (the true detection significance for cosmic birefringence, or the value in a specific covariance model).  
Required fix: Clarify that 3.9σ is an *over-optimistic* significance in a toy model with uncorrelated errors, and that the physically relevant value is the published 3.6σ which uses a joint covariance. Suggested wording: “…the naive 3.9σ is an over-optimistic estimate obtained under the assumption of independent errors and should not be interpreted as a bound on the true significance; the headline value is the 3.6σ joint analysis.”

---

P1B-M16 (MAJOR)  
Section: Appendix C vs. Sec. VI, ALP MCMC “benchmark” vs. “continuous-prior” chains, p. 8, 10–11  
Problem: The main text says “Dedicated MCMC sampling … (3 configurations, 9,720 total accepted samples) yields βALP = 0.336° ± 0.107° (Caγ = 8 fixed) … consistent with βfree = 0.344° ± 0.096°,” and later describes a continuous-prior run with Caγ ∈ [4, 60] (8,955 accepted samples). The appendix lists priors and notes 3,240 samples per fixed-Caγ configuration, but it never explicitly confirms which of these chains underpin each quoted β result, nor how burn-in and thinning were handled in the ALP context.  
Required fix: In Appendix C, add a short mapping table or bullet list explicitly stating, for each quoted number in Sec. VI (βALP, βfree, continuous-prior median Caγ and its credible interval, “69% in-band” fraction), (i) which chain(s) they come from, (ii) the number of post–burn-in samples used, and (iii) whether any thinning was applied. This mirrors the level of bookkeeping already provided for the cosmology chains and removes any ambiguity.

---

P1B-M17 (MAJOR)  
Section: Sec. III, footnote 1 vs. Table I and Fig. 1 sample counts, p. 3–5  
Problem: Footnote 1 attempts to reconcile sample-count stratification and gives multiple approximate numbers: 176,240 raw samples for full-tension and 132,949 for Planck+BAO+SN, with 30% burn-in and an effective-thinning explanation for Fig. 1’s 119,617 samples. However, the footnote oscillates between approximate (“≈ 123,368”) and precise (“123,129”) counts and uses different effective-sample notions (raw post–burn-in vs. getdist-thinned), making it difficult to reconstruct exact counts from the text. For a verification paper, this is unnecessarily opaque.  
Required fix: Replace the mixture of approximations with a clear, single table (in Sec. III or as a small addition to Table I) listing, for each dataset combination: raw samples, burn-in fraction, exact post–burn-in sample count, and any additional thinning used for figures (with the resulting effective count). Remove approximate “≈” figures where exact integers are available.

---

P1B-N3 (MINOR)  
Section: Sec. IV, “Independent verification (production 500-realization run, April 2026),” p. 5–6  
Problem: The definition of the “ACT-level noise” used in the NaMaster MC test is given as ∆P = 10 µK·arcmin, but this is not tied to any specific ACT DR6 reference or channel. For a technical-verification paper, this leaves the exact realism of the noise model under-specified.  
Required fix: Add a parenthetical citation to the ACT DR6 reference [3] or a short phrase specifying which ACT DR6 frequency/multipole range the 10 µK·arcmin figure is meant to approximate (e.g., “comparable to the ACT DR6 combined polarization noise at ℓ ≈ …”). This makes the “ACT-level” label quantitatively grounded.

---

Reason for no further issues in other categories  
I re-scanned the abstract vs. body mapping, dimensional consistency of displayed equations, and figure–caption vs. text consistency beyond what is flagged above. Eq. (2) and Eq. (3) are dimensionally consistent once αEM/(4π) and ∆ϕ/fa are understood as dimensionless; the main remaining issues are numerical transparency and prior vs. posterior interpretation, which are covered in P1B-M1 and P1B-M11–M16. I did not find additional arithmetic mismatches in the tables beyond those already identified in the earlier review and in the new items above.