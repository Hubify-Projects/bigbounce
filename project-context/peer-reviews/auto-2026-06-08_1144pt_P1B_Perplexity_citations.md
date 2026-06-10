# P1B auto-2026-06-08_1144pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (17062 chars)
**Wall time**: 98.7s

---

P1B-E1  
Section: Abstract, page 1  
Problem: The abstract cites “Planck/ACT DR6 2.4–2.9σ [2,3]” as the primary sky-detection significance. Reference [3] is listed as “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” That arXiv identifier is future‑dated (2509.x) and does not exist; no ACT DR6 birefringence paper with that exact metadata is currently on arXiv or ADS. The only firmly established CMB birefringence result consistent with the quoted values is Eskilt & Komatsu 2022 (Planck/WMAP), not ACT DR6.  
Required fix: Either (a) replace [3] with a real, published or at least existing arXiv ACT birefringence reference whose σ and β match the quoted numbers, or (b) remove all claims tied to ACT DR6 and future‑dated arXiv:2509.13654, restricting the “2.4–2.9σ” range to documented literature with correct citation. Clarify explicitly which published results are used, with correct arXiv IDs and journal info.

P1B-E2  
Section: Abstract, page 1  
Problem: The abstract states: “Spectator-ALP consistency check: a field with fa ∼ MPl, m ∼ H0 is consistent with the published joint WMAP+Planck value β = 0.342◦ ± 0.094◦ (3.6σ) [2].” While β = 0.342° ± 0.094° (3.6σ) does appear in Eskilt & Komatsu 2022 (PRD 106, 063503; arXiv:2205.13962), that paper uses WMAP9 + Planck PR3/PR4 NPIPE; the wording “joint WMAP+Planck” is fine, but later in the footnote and body the text conflates PR3 and PR4/NPIPE attribution in a way that is not faithful to the published paper: the published 3.6σ headline corresponds to PR3+WMAP9, whereas the PR4/NPIPE analysis in that work gives different numbers.  
Required fix: Precisely align the cited 3.6σ value with the configuration actually used in Eskilt & Komatsu (PR3+WMAP9) and state clearly that the 0.342° ± 0.094° comes from that dataset combination. Any use of PR4/NPIPE code or repository spin-offs must be described as re-analysis, not as the published PRD result.

P1B-E3  
Section: Section III, Table I and surrounding text, pages 2–3  
Problem: The paper describes “ΛCDM+∆Neff proxy MCMC results from frozen Cobaya v3.6.1 chains (CAMB v1.6.5, stock; no torsion modifications)” and gives precise numerical posteriors for H0, ∆Neff, σ8, etc., but no external reference is cited for these numbers (they are internal). That is fine; however, the chain sizes and R̂–1 values are load‑bearing. In footnote 1 the text attempts to reconcile 309,189 total raw samples, a 30% burn‑in, and the post‑burn‑in counts (e.g. 123,129 vs 123,368) and claims this matches “convergence summary.json.” These numbers are mutually inconsistent in the text as written (123,129 vs 123,368 for the same subset, 216,432 vs the implied 216,432.3) and cannot be independently checked by the reader because the chains are not provided.  
Required fix: Provide the actual post‑burn‑in sample counts and show a consistent calculation once, without approximate back‑of‑the‑envelope numbers that differ at the percent level. If the exact counts are, e.g., 176,240 raw → 123,368 post‑burn‑in, use that value consistently and drop the conflicting “123,129” and “within ±1%” language. For PRD standards, either include a machine‑readable R̂ and ESS table in the ancillary files or remove the unnecessary internal numerology.

P1B-E4  
Section: Section III, paragraph beginning “a. Scope of the ∆Neff proxy”, page 3  
Problem: The text asserts that the minimal matter bounce “predicts ∆Neff ≈ 0 by construction (no light bounce‑internal species are thermalized at recombination)” with reference  (Cai et al. 2009, matter bounce non‑Gaussianity). That paper does not state a sharp prediction ∆Neff ≈ 0; it is about primordial non‑Gaussianity and does not construct or classify relativistic degrees of freedom at recombination. The quoted “prediction” is an inference about a specific model choice, not something that can be traced to .  
Required fix: Rephrase to make clear that “∆Neff ≈ 0” is the author’s definition of a “minimal matter bounce” scenario rather than a prediction proved or stated in . Remove any implication that  itself derives this ∆Neff statement.

P1B-E5  
Section: Section III, Independent cross-validation, page 4; References , ,   
Problem: References , ,  are claimed as DESI DR2 and DES Y3/5 publications with specific years (2025, 2024, 2022) and arXiv IDs indicated only generically (e.g., arXiv:2507.04265, arXiv:2503.14738). These arXiv IDs are future‑dated relative to the 2026‑06‑03 manuscript date; there is no confirmable DESI “DR2 results II: BAO and cosmological constraints” with the exact title, author list, and arXiv:2503.14738 on arXiv/ADS, nor a torsion cosmology paper with arXiv:2507.04265. The metadata for these citations appears to be fabricated or anticipatory.  
Required fix: Replace , ,  with existing, verifiable DESI and DES references (e.g., current DR1/2024 BAO main cosmology paper, DES Y3 cosmology paper) with correct authors, titles, years, and arXiv IDs. Do not cite future, non‑existent arXiv numbers or DR2 cosmology results as if they were published.

P1B-E6  
Section: Section V, Table II and paragraph “DESI DR2 w0 wa posterior summary”, pages 4–5  
Problem: Table II claims “DESI DR2 w0 wa posterior summary (N = 128,385 accepted samples across 16 chains… Likelihood stack: DESI DR2 BAO + Planck 2018 NPIPE … + DES-Y5 + Pantheon+).” The cited DESI DR2 BAO and DES‑SN5YR / DES‑Y5 references in the bibliography do not exist with the given metadata; DR2 cosmology and DES‑SN5YR (2024 ApJ 973, L14, arXiv:2401.02929) are not yet combined in any published w0–wa cosmology analysis matching the quoted numbers. Because there is no externally available analysis with these exact inputs, the reader cannot verify the DESI DR2/“DES-Y5” association nor the χ² components. The “DESI DR2 BAO” paper  itself is non‑existent.  
Required fix: Either (a) replace the DR2/“DES‑Y5” inputs with real public data and cite the corresponding, correct references, or (b) clearly label this analysis as purely internal and exploratory, remove explicit mention of DR2/“DES‑Y5” papers and arXiv IDs, and refrain from presenting it as a cross‑validation of external published results. For PRD, if “DESI DR2” is used, only datasets and references that actually exist at submission time are acceptable.

P1B-E7  
Section: Section V.B, “Key finding” paragraph, page 5; Figure 1 caption, page 5  
Problem: The key finding restates that ∆Neff = −0.020 ± 0.169 and +0.065 ± 0.17 are “consistent with zero” and that CMB‑S4 will reach σ(Neff) ~ 0.03. CMB‑S4 projections are not cited; there is no reference in the bibliography for this σ(Neff) ≈ 0.03 forecast. That forecast value is non‑trivial and should be traceable to a design or forecast paper (e.g., a CMB‑S4 science book).  
Required fix: Add a proper CMB‑S4 reference for the σ(Neff) ≈ 0.03 forecast and verify that the forecast number matches what that reference states (or correct the number and wording). If no such citation is included, remove the quantitative σ(Neff) claim and keep only a qualitative statement that next‑generation CMB experiments will improve Neff constraints.

P1B-E8  
Section: Section IV, “Birefringence measurements are adopted from the published literature”, page 5; References  and [3]  
Problem: The text quotes β = 0.30° ± 0.11° (Planck NPIPE ) and β = 0.215° ± 0.074° (ACT DR6 [3]). Diego‑Palazuelos et al. (arXiv:2201.07682) indeed report a Planck NPIPE birefringence measurement ~0.30° ± 0.11°, but that’s Planck only; ACT DR6 birefringence results and their precise 0.215° ± 0.074° value, attributed to a 2025 ACT DR6 paper, cannot be checked because the ACT DR6 birefringence paper [3] does not exist with the given ID. Thus only the Planck value is traceable; the ACT DR6 number is not verifiable by source.  
Required fix: For the ACT DR6 number, either (a) cite a real ACT DR6 birefringence analysis with matching β and σ (once it exists) or (b) remove the 0.215° ± 0.074° claim and any derived combinations that treat it as published. Do not mix a verifiable Planck NPIPE result with a speculative ACT DR6 value under “published literature.”

P1B-E9  
Section: Section VI, “Summary-likelihood combination (auxiliary cross‑check)”, page 7  
Problem: The paper combines β = 0.30° ± 0.11° and β = 0.215° ± 0.074° using inverse‑variance weighting to get βcombined = 0.241° ± 0.061° (3.9σ). Given that only the Planck number is backed by a real paper, while the ACT DR6 number is not traceable, this combined “3.9σ” statistic cannot be verified from the literature and is effectively built on an unverified input.  
Required fix: Until a real ACT DR6 measurement with β = 0.215° ± 0.074° is published and cited properly, remove the numerical combined 3.9σ result and discussion. If retained, it must be clearly described as a hypothetical what‑if combination, not as “auxiliary cross‑check” of published data.

P1B-E10  
Section: Section VI, “MCMC parameter estimation” and Appendix C (ALP‑MCMC), pages 7 and 9  
Problem: The text claims to use “Planck PR4 + ACT DR6 EB-spectrum likelihoods (the same observables used by Refs. [2,3]) combined with shared calibration covariance” for the ALP and βfree fits. Eskilt & Komatsu [2] use Planck+WMAP (and related calibration), not ACT DR6 EB spectra; the ACT DR6 likelihood and shared calibration covariance as described here are effectively unverified because the ACT DR6 birefringence paper [3] is non‑existent. Thus the statement “the same observables used by Refs. [2,3]” is inaccurate for [2] and unverifiable for [3].  
Required fix: Correct the description of the likelihoods: specify exactly what EB spectra and calibrations are used, and do not attribute “same observables” to papers that use different data. Remove or modify references to ACT DR6 until an appropriate, verifiable reference exists.

P1B-E11  
Section: References [1], [4], [5], [6], ; multiple pages  
Problem: The bibliography lists several of the author’s own works as “(in preparation)” with internal tags “hUBIFY‑2026‑00x; companion paper, this volume” (e.g., [1] through [6]). These are not yet published or on arXiv, and thus cannot be examined by the referee or a PRD reader. Some claims in the current paper rely on results from these in‑preparation works (e.g., structural closure, multi‑survey anomaly catalog, galaxy chirality results). PRD generally expects load‑bearing claims to be supported by published or at least publicly accessible preprints.  
Required fix: For any statement in this paper that depends critically on results in [1], [4], [5], [6], , either (a) move the essential content into this manuscript (or its openly available supplementary material) or (b) ensure those companion papers are available on arXiv with stable identifiers and update the references accordingly. If that is not feasible, remove such dependence from this paper or flag clearly that such results are not yet verifiable.

P1B-E12  
Section: Abstract and Section VII (Conclusions), pages 1 and 7–8  
Problem: The paper repeatedly states that “the same birefringence arises in standard GR with an identical ALP; it is not a distinctive ECH prediction” and that the ALP with fa ~ MPl, m ~ H0 gives β in the observed range. While Fujita et al. 2021 (PRD 103, 043509; arXiv:2011.11894) indeed study axion‑like particles and birefringence, the specific numerical ranges given in this paper for Caγ, ∆ϕ/fa, and resulting β are internal to this work and do not directly trace to . The wording could suggest that  guarantees the precise parameter combinations cited, which it does not.  
Required fix: Make explicit that the ALP parameter ranges and Caγ ∆ϕ/fa ~ 10.3 come from the author’s own numerical scans, not directly from Fujita et al. Clarify that  is cited only as prior work on ALP‑induced birefringence, not as the source of the numerical values used here.

P1B-E13  
Section: Reference , page 10  
Problem: Reference  is “Planck Collaboration, N. Aghanim, et al., Planck 2018 results. VI. cosmological parameters, Astronomy & Astrophysics 641, A6 (2020), arXiv:1807.06209 [astro-ph.CO].” This is Planck PR3, not PR4/NPIPE. In several places the text claims to use “Planck 2018 NPIPE” and “PR4/NPIPE” likelihoods, but the only Planck reference given is PR3 cosmological parameters. Diego‑Palazuelos et al.  is a PR4/NPIPE birefringence analysis, but not the main PR4 parameter paper. There is no reference for the PR4/NPIPE cosmological likelihoods actually used.  
Required fix: Add a correct reference for Planck PR4/NPIPE (e.g., the corresponding Planck NPIPE data release or analysis paper) if those likelihoods are indeed used. Distinguish clearly between PR3 and PR4 in all dataset descriptions and ensure the citations line up with the data actually used in the MCMC runs.

P1B-M1  
Section: Section III, paragraph “Key finding”, Figure 1 caption, pages 4–5  
Problem: The paper juxtaposes different σ significances and constraints (e.g., ∆Neff posteriors, H0 tension “3.6σ”, τ constraints) without always stating when these significances are derived from different null procedures or different datasets. In some cases (e.g., H0 tension between SH0ES and Planck) the underlying null hypotheses differ, yet the σ language is used in a single narrative. The instructions specify that σ values from different null procedures appearing side‑by‑side require explicit “not directly comparable” qualifications at each juxtaposition.  
Required fix: Wherever multiple σ values from distinct tensions or null hypotheses are mentioned in the same paragraph (e.g. H0 tension vs. ∆Neff consistency, β significance vs. pipeline SNR), explicitly state that these are not directly comparable significances and explain their distinct origins (posterior deviation, inverse‑variance combination, frequentist tension across experiments, etc.).

P1B-M2  
Section: Abstract, Section II, Section V, page 1–2, 6  
Problem: The abstract and body claim that this is purely a “technical verification companion,” yet substantial new cosmological claims are made (e.g., w0 = −0.812 ± 0.044, wa = −0.667 ± 0.186, phantom crossing with w0 + wa = −1.48 ± 0.15) for a novel dataset combination (“DESI DR2 BAO + Planck NPIPE + DES-Y5 + Pantheon+”) whose exact composition is not referenced to a published analysis and whose robustness cannot be independently checked. This is more than “technical verification” and amounts to a full cosmological analysis; yet the description, validation against the literature, and systematics discussion are minimal.  
Required fix: Either (a) substantially expand the methodological and validation discussion for the w0–wa analysis (data vetting, comparison to existing w0–wa constraints, systematics treatment) to meet PRD standards for a new cosmology result, or (b) significantly down‑scope these results, treating them as internal test runs and moving detailed numerical claims to supplementary materials or a future dedicated paper.

P1B-M3  
Section: Section IV, “Pipeline configuration” and “Independent verification”, pages 5–6  
Problem: The NaMaster setup is described qualitatively, but no specific numerical values are cited for several configuration details that materially affect the pseudo‑Cl bias: e.g., the exact mask, apodization function parameters beyond “C2 apodization at 2° scale,” the ℓ range and binning are only roughly given, and there is no plot or table of recovered spectra, only the β̂ numbers. The text states that the bias of 0.032–0.040° is “consistent with the apodized‑mask bias expected from a 2° apodization scale” without providing a reference or calculation for this expectation.  
Required fix: Provide concrete details (e.g., mask description, apodization kernel definition, numerical form of the pixel window; show a representative EB spectrum with and without injected rotation and bias subtraction). Either cite existing NaMaster literature that quantifies this sort of bias or provide an explicit check, so that the claimed “consistent with mask bias” is verifiable.

P1B-M4  
Section: Section VI, equations (2) and (3), page 6  
Problem: The ALP evolution equation is written as ϕ̈ + 3H ϕ̇ + m² fa sin(ϕ/fa) = 0, then used to derive ∆ϕ/fa ≈ 0.65 and β ≈ (αEM × 8)/(4π) × 1.07 ≈ 0.29°. Dimensional consistency is marginally described: fa and ϕ are dimensionful, but the textual derivation glosses over the normalization conventions (e.g., is the Lagrangian normalized with ϕ/fa or θ = ϕ/fa). The numerical factor “1.07” in equation (3) appears without derivation or citation; its origin (time integral of the field trajectory, choice of redshift range, normalization) cannot be checked.  
Required fix: Provide a brief but explicit derivation or a reference for the 1.07 factor and the ∆ϕ/fa ≈ 0.65 estimate, including the assumed initial conditions and background cosmology, so that the reader can reproduce the β ≈ 0.29° calculation. At minimum, specify the normalization conventions clearly and show that the dimensions cancel properly.

P1B-M5  
Section: Appendix A, “What is NOT included”, page 8  
Problem: The paper emphasizes “reproducibility manifest” and a GitHub repository, but key numerical results in this companion paper (MCMC chains, NaMaster outputs) are not actually present and must be recomputed by the reader. For a “technical verification” companion in PRD, it is more appropriate to provide at least the main chains and pipeline outputs as archived ancillary files, not only scripts to regenerate them.  
Required fix: Either deposit the actual MCMC chains and NaMaster outputs in a stable repository (Zenodo or similar) and cite that archive, or reduce the reliance on external code and long‑runtime MCMC runs by presenting sufficient summary diagnostics in the paper (full parameter covariance matrices, detailed R̂ and ESS tables, more extensive diagnostic plots).

P1B-M6  
Section: Acknowledgments, page 8  
Problem: The author states: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation. All scientific claims, derivations, numerical results, and bibliographic attributions were independently verified by the author.” While transparency about AI use is commendable, PRD standards require that bibliographic and numerical claims be independently and rigorously checked; this statement is at odds with the numerous citation and metadata inconsistencies already identified (non‑existent arXiv IDs, fused datasets).  
Required fix: After correcting all citation and data‑attribution errors, this statement should be updated to be accurate. Alternatively, remove the assurance of independent verification and replace it with a more modest acknowledgment of AI assistance without claiming flawless verification that is not borne out.

P1B-Minor1  
Section: Abstract, Section IV, page 1 and 5–6  
Problem: The abstract and body correctly state that pipeline SNR values (e.g., 20.32σ, 25.71σ) refer to recovery of injected MC signals, not sky detections; however, the notation “σ” for these SNR values is potentially confusing given the simultaneous use of σ for statistical significance of sky measurements elsewhere.  
Required fix: Consider using “SNR=20.3 (MC recovery)” rather than “20.32σ” to prevent misinterpretation and maintain clear separation between pipeline SNR and sky‑measurement significance.

P1B-Minor2  
Section: Various footnotes (fn. 4, fn. 5), pages 7 and 10  
Problem: Several footnotes use uppercase emphasis (“RETAINED”) and informal phrasing (“PROMISED a Savage‑Dickey ratio”, etc.) that are stylistically inconsistent with PRD’s formal style.  
Required fix: Rephrase the footnotes in neutral, formal language, removing emphatic capitalization and conversational tone.

P1B-Minor3  
Section: Table III “Claims classification”, page 10  
Problem: The table classifies various claims as “Verified,” “Omitted,” “Scope Defn.,” etc., including internal assertions such as “Model-comparison ∆AIC/BIC/ln B – Omitted.” This is not standard content for a PRD paper and risks confusing readers; moreover, it does not correspond to any external verification process.  
Required fix: Remove Table III or move it to supplementary material, and ensure that the paper itself clearly states which claims are load‑bearing and which are scope statements, without implying an external verification status.

P1B-Nit1  
Section: Table II and its caption, page 4  
Problem: Minor typographical issues: the table uses “lcdm” in one place and “LCDM” elsewhere; spacing in “w0 wa” vs “w0wa” is inconsistent; and the subscript “pivot” appears without definition in the table caption.  
Required fix: Standardize capitalization (ΛCDM), notation for w0–wa, and define wpivot clearly in the caption or text.

P1B-Nit2  
Section: PACS numbers, page 1  
Problem: PACS is deprecated; most PRD papers now use keywords and subject classification instead.  
Required fix: Update to the current PRD subject classification scheme if requested by the editors.

P1B-Nit3  
Section: References , , , , , page 10  
Problem: Minor formatting inconsistencies: some references include subtitles and journal names in non‑standard capitalization; abbreviations (e.g. “Phys. Rev. D”, “JCAP”) should follow PRD style.  
Required fix: Normalize all references to PRD’s bibliographic style.

## Summary recommendation

REJECT

The manuscript contains multiple serious citation‑forensics failures: non‑existent arXiv IDs and future‑dated references, misattribution of dataset combinations and result provenance, and unverifiable ACT DR6 birefringence inputs used in key quantitative claims. Several cosmological results are presented as if they cross‑validate external work but are actually based on internal, uncheckable analyses. Combined with stylistic and methodological issues for a “technical verification” companion, the paper does not meet PRD’s standards of rigor and verifiability in its current form; the required corrections amount to a substantial restructuring and replacement of core external inputs rather than routine revisions.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E14  
Section: Section III, “MB–H0 joint-posterior offset check”, page 4  
Problem: The text claims the offset between the Pantheon+ combination “MB − 5 log10(H0)” at the Riess anchor versus the chain mean is “∼3.2σ relative to the chain’s σMB = 0.049” and “corresponds exactly to the canonical 3.6σ Hubble tension.” Numerically, the difference is 0.155 mag and dividing by 0.049 gives ≈3.16σ, which matches “∼3.2σ” but not “exactly” 3.6σ. Moreover, the 3.6σ H0 tension quoted elsewhere uses the Riess and Planck H0 uncertainties, not σMB, so there is no direct σ-for-σ equivalence.  
Required fix: Clarify that the 0.155 mag offset corresponds to ≈3.2σ in MB-space and is qualitatively consistent with (but not “exactly” equal to) the ∼3.6σ H0 tension. Remove the “corresponds exactly” language and explain that these σ values arise from different variables and error budgets.

P1B-E15  
Section: Table II, rows “χ²total” and “χ²BAO/CMB/SN”, page 4  
Problem: The caption notes that χ²total = 14037.4 differs from the sum 10.6 + 10983.9 + 3043.0 = 14037.5 by “0.1-unit arithmetic-rounding artifact; the two are formally identical to within sampling precision.” The arithmetic difference is 0.1, but the rounding explanation is incomplete: the quoted component χ² means are themselves rounded to 0.1 precision, so the exact unrounded values could sum to 14037.4, 14037.5, or something close. As written, “formally identical” is too strong; the user cannot check that the decomposition and total are consistent beyond the quoted rounding.  
Required fix: Rephrase to say that the 0.1 difference is within the rounding precision of the reported component means and is not statistically meaningful, rather than “formally identical.” Optionally add the unrounded χ² component values in an ancillary file if this decomposition is load-bearing.

P1B-E16  
Section: Figure 1 caption vs. Table I and surrounding text, pages 3–5  
Problem: Figure 1’s caption states “119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote 1,” while footnote 1 and Table I give different post-burn-in numbers (123,129 vs. 123,368 vs. 216,432) for the same chain subsets. Your earlier review already flagged the numerical inconsistency in footnote 1; the new issue is that the figure-caption chain length (119,617) is neither equal to the explicit post-burn-in count (123,129) nor derived by any clearly documented thinning factor. The reader cannot reconstruct how 176,240 raw → 119,617 appears here, and the mismatch between figure and table suggests stale or partially updated numbers.  
Required fix: Choose one consistent set of numbers for raw, post-burn-in, and thinned sample counts and use them in Table I, footnote 1, and the Figure 1 caption. Explicitly state the thinning factor (e.g., “thinned by factor 0.97 to 119,617 samples”) or provide the exact GetDist effective-sample computation so the chain lengths across text, table, and figure are self-consistent.

P1B-E17  
Section: Section III, “Key finding” paragraph, page 5; Section II H0–σ8 discussion, page 2; Table I  
Problem (arithmetic and σ-procedure comparability):  
– The “Key finding” states that both frozen datasets “find ∆Neff consistent with zero and H0 consistent with Planck ΛCDM at 0.3σ,” referring to Table I’s H0 values (67.68 ± 1.06 and 67.79 ± 1.09). Planck PR3’s base-ΛCDM H0 = 67.4 ± 0.5 km/s/Mpc is not explicitly cited in this context, and the 0.3σ figure is not recomputed in the text. Using 67.4 ± 0.5 as the reference, the offset 67.68 – 67.4 ≈ 0.28 divided by the combined error \(\sqrt{1.06^2 + 0.5^2}\) ≈ 1.17 gives ≈0.24σ, so “0.3σ” is only an approximate statement and the reference error model is unstated. A similar ambiguity exists for linking the ∆Neff posterior widths to “current data neither require nor exclude” language without showing an explicit 95% or 3σ interval.  
– These σ values (0.3σ off ΛCDM, 3.6σ H0 tension, 4.3σ and 3.6σ departures of w0, wa, etc.) are juxtaposed in the H0/σ8 discussion and in Section V without consistently flagging that they arise from different null procedures (comparison to a Planck base-ΛCDM mean, SH0ES–Planck discrepancy, posterior distance from a model point). Some of this was addressed in prior comments, but new juxtapositions appear in the MB–H0 consistency paragraph on page 4, where the 3.2σ MB offset and the 3.6σ H0-tension are again placed in one narrative without a fresh “not directly comparable” reminder.  
Required fix:  
(a) Explicitly define the reference “Planck ΛCDM” values and uncertainties used to obtain the 0.3σ H0 consistency, and either show the small calculation or acknowledge that “≈0.2–0.3σ” is an approximate consistency statement, not a precise derived significance.  
(b) In every paragraph where a new σ value is introduced next to existing ones (e.g., the MB–H0 check, the “Key finding” paragraph), add a brief clause clarifying that they come from distinct null procedures and are not directly comparable, as required by the instructions you quote.

P1B-E18  
Section: Section IV, “Independent verification (production 500-realization run)”, page 5; equation (1)  
Problem (arithmetic / notation): The text reports “β̂NaMaster = 0.238° (pipeline-recovery SNR = 20.32)” for a β = 0.27° injection and describes a “pipeline-recovery bias 0.032°,” later noting a 0.040° bias at β = 0.342°. The implied SNR definition is not stated. If SNR ≡ β̂/σβ, then σβ ≈ 0.238°/20.32 ≈ 0.0117°, which is a perfectly plausible MC uncertainty but is never made explicit nor cross-checked. Because “σ” is also used for sky-significance elsewhere, the lack of a precise SNR definition here increases the risk of confusion. This is related to, but distinct from, the Minor2 issue about notation.  
Required fix: Define explicitly how “SNR = 20.32” and “25.71” are computed (e.g., β̂ divided by the standard deviation of the MC β̂ distribution), and where possible quote the implied σβ once to make the arithmetic traceable. Consider replacing “20.32” with “SNR ≈ 20” and explicitly state it is a pipeline MC SNR, not a sky-detection σ, to reinforce the distinction.

P1B-E19  
Section: Section VI, equation (3) and surrounding text, page 6  
Problem (dimensional consistency and missing derivation details, beyond prior comments): Equation (3) writes  
β ≈ (αEM × 8)/(4π) × 1.07 ≈ 0.29°,  
and then states that the fiducial β ≈ 0.27° corresponds to m ≈ 1.8 H0, ∆ϕ/fa ≈ 1.0. Earlier, equation (2) gives ∆ϕ/fa ≈ 0.65 for m = H0, θi = 1, and the text then quotes ∆ϕ/fa ∈ [0.2, 1.1] for m/H0 ∈ [1, 3], θi ∈ [0.5, 2]. However, the connection between the 1.07 factor in equation (3) and any particular value of ∆ϕ/fa is not shown: if αEM/(4π) ≈ 1/137/(4π) ≈ 5.8×10⁻⁴, then βrad ≈ 8×5.8×10⁻⁴×1.07 ≈ 0.00496, i.e. ≈0.284°, so 1.07 implicitly plays the role of an effective Caγ×(∆ϕ/fa). Yet the text separately quotes Caγ = 8 and ∆ϕ/fa ≈ 1.0, whose product is 8, not 1.07. That is, equation (3) appears to bake Caγ into the αEM×8 factor and then insert another, dimensionless 1.07 whose origin (Δϕ/fa trajectory integral, normalization conventions, limits of integration) remains opaque. This makes it difficult to judge whether the numerical computation of β is dimensionally and conceptually consistent with the earlier ∆ϕ/fa results.  
Required fix: Explicitly write the standard birefringence relation (e.g. β = (αEM/4π) Caγ Δϕ/fa), then show step-by-step how Caγ, Δϕ/fa, and any additional numerical factors combine to give the specific 1.07 used in equation (3). Clarify whether 1.07 is Δϕ/fa, an integral of the field trajectory normalized to θi = 1, or something else. Ensure that the text uses the same normalization consistently between equations (2) and (3), or correct the numbers if they are inconsistent.

P1B-E20  
Section: Section VI, “Birefringence value” paragraph, page 6; Appendix C  
Problem (arithmetic / stale numbers): The text states that the “prediction spans β ≈ 0.17–0.43° over Caγ ∈ [4, 12], m/H0 ∈ [1, 3], θi ∈ [0.5, 2]” and that the simple independent-extremes estimate would give a wider “naive envelope [0.027, 0.44]°.” Given the quoted Caγ ∈ [4, 12] and Δϕ/fa ∈ [0.2, 1.1], the naive product Caγ Δϕ/fa ranges from 0.8 to 13.2. Using β ≈ (αEM/4π) × Caγ Δϕ/fa with αEM/(4π) ≈ 5.8×10⁻⁴, the corresponding β range is roughly 0.026°–0.76°. The lower end (0.026°) matches the quoted 0.027°, but the upper naive β≈0.76° is significantly higher than 0.44°. This indicates that either the ∆ϕ/fa range, the Caγ range, or the naive-envelope number has been partially updated without re-deriving all dependent quantities.  
Required fix: Recompute the full β range from the stated Caγ and Δϕ/fa envelopes and update the quoted “naive” and “trajectory-scan” β intervals accordingly. If the trajectory scan never reaches the maximal product Caγ×Δϕ/fa, make that explicit and show (briefly) how the true scan-based 0.17–0.43° interval is obtained. Remove or correct the “[0.027, 0.44]°” naive-envelope numbers if they no longer reflect the current parameter ranges.

P1B-E21  
Section: Table III “Claims classification”, page 10  
Problem (unsupported classification / internal consistency): Table III labels “Published 3.6σ (β = 0.342 ± 0.094°)” as “Lit., Cited, Eskilt et al.” and “βALP = 0.336° ± 0.107°” as “MCMC, Verified.” However, as the body now stands, the ALP fits use “Planck PR4 + ACT DR6 EB-spectrum likelihoods” and “the same observables used by Refs. [2,3]” (Appendix C), while reference [3] is a non-existent ACT DR6 birefringence paper and the precise EB likelihood configuration is not documented in any public source. This makes the “Verified” tag for βALP incomplete: the statistical convergence may be checked internally, but the observational inputs are not yet independently verifiable by a reader, especially given the undefined ACT DR6 likelihood.  
Required fix: Downgrade the classification of βALP to reflect its dependence on internally-configured, non-public likelihoods (e.g., “MCMC, Internal-only (unverifiable ACT DR6 likelihood)” or similar), or else remove ACT DR6 from the ALP-likelihood stack and re-run the fit with fully documented, public likelihoods so that “Verified” is a fair characterization. Also clarify in the notes column that the 3.6σ value is strictly a literature result from Eskilt & Komatsu, whereas the combined or ALP-derived values are internal.

P1B-E22  
Section: Section VII (Conclusions), “Forward.” paragraph, page 7; Table II  
Problem (abstract faithfulness / scope): The “Forward” paragraph states that a DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR w0–wa chain “has converged (128,385 accepted samples across 16 MPI chains; R̂ − 1 = 0.00820, below the standard R̂ − 1 < 10−2 publication target)” and that “GetDist posteriors on w0 wa are available as an empirical test of the quintom-B scenario .” Earlier, Table II gives detailed w0–wa numbers for this same combination, and the abstract and Section V use those as quasi-results, while also asserting that “this is a technical verification companion” and that model-comparison metrics and robust ln B are deferred. This mixture of language effectively promotes the w0–wa constraints to headline cosmology results in the body (with explicit σ significances and phantom crossing) while describing them only as “empirical test” and “Forward” outlook at the end. That disconnect between how prominently the numbers are used and how cautiously they are framed makes the abstract and conclusions less than fully faithful to the body’s content.  
Required fix: Align the conclusions with the actual usage of the w0–wa results in the body. Either (a) clearly label the Table II constraints as exploratory internal fits and adjust Section II/III/V text to avoid presenting them as load-bearing cosmological claims, or (b) explicitly acknowledge in the conclusions that this companion paper does report a substantial new w0–wa result (with its limitations) rather than leaving it in a “Forward” paragraph that understates its role.

P1B-E23  
Section: Appendix C, “Likelihood stack.”, page 9; main text Section VI and Section IV  
Problem (internal cross-references / data-description mismatch): Appendix C states that the ALP and βfree fits use “the Planck PR4 + ACT DR6 EB-spectrum likelihoods (the same observables used by Refs. [2,3]) combined with shared calibration covariance.” In the main text, Section VI’s “Headline observational constraint” instead focuses on the joint WMAP+Planck Eskilt & Komatsu result and treats ACT DR6 mainly as an auxiliary measurement. The data-methods section (Section IV) describes only the NaMaster pseudo-Cl pipeline on Planck Commander maps, not the exact EB-spectrum likelihoods used in the ALP-MCMC. Thus, there is no location in the body where the “Planck PR4 + ACT DR6 EB-spectrum likelihoods” are actually defined, referenced, or cross-checked, despite Appendix C asserting their use. This is a new internal cross-reference problem: the main text never shows or quantifies the likelihood ingredients that Appendix C claims are central to the ALP fits.  
Required fix: Add a subsection in Section VI (or earlier in Section IV) that explicitly describes the EB-spectrum likelihoods used in the ALP and βfree fits: which Planck PR4/NPIPE products, what ACT DR6 spectra (if any public ones), how calibration covariance is modeled, and how this differs from the Eskilt & Komatsu WMAP+Planck analysis. Cross-reference that subsection from Appendix C so that readers can actually understand and (in principle) reproduce the likelihood stack.

P1B-M7  
Section: Throughout, especially Sections II, III, V, VI, VII  
Problem (hedges and quantitative backing): Numerous phrases such as “consistent with zero,” “consistent with ΛCDM,” “consistent with the minimal matter-bounce prediction,” “comfortably bracketing the observed value,” “neither require nor exclude,” and “not a discriminator” are used without always giving the explicit numerical deviations and error bars in the same sentence or paragraph. While some of these are backed elsewhere (e.g., Table I for ∆Neff and H0), in several spots—especially in the bounce-class discussion at the end of Section III and the ALP parameter discussion in Section VI—the hedge language could obscure how close to the boundaries these constraints actually lie.  
Required fix: For each use of “consistent with,” “no significant tension,” or similar in Sections II, III, V, and VI, ensure that the associated numerical difference and uncertainty (or a reference to the specific table/figure where they are given) appears nearby. This makes the qualitative hedges quantitatively grounded and prevents them from hiding potentially important tensions or boundary cases.

P1B-M8  
Section: Section III, “Independent cross-validation.”, page 5; References ,   
Problem (figure-caption vs body-claim analogue for literature comparison): The text states, “Liu et al.  constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (∆AIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.” While your earlier review already flagged that these DESI “DR2” references are future-dated and non-existent, this new issue is arithmetic: the “0.5σ” and “0.4σ” agreement claims are not backed by any explicit numbers from Liu et al. or from this paper’s posteriors. The reader cannot check whether the 0.5σ/0.4σ figures are correctly computed or simply illustrative.  
Required fix: Once the DESI/DES references are corrected to existing literature, explicitly quote the H0 and σ8 values and uncertainties from Liu et al. and from your own chains, and show the simple σ-calculation (difference divided by combined error) that leads to 0.5σ and 0.4σ. If these numbers change after correcting the references/datasets, update the σ-agreement figures accordingly.

P1B-Minor4  
Section: Section VI, footnotes 4 and 5 referenced in the text, pages 6 and 9  
Problem: The main text references “fn. 4” and “fn. 5” as disclosing misalignment tuning and backreaction details, and the footnotes themselves contain terms like “RETAINED” in all caps and informal parenthetical explanations. Your earlier review already flagged style issues in some footnotes, but this new observation is that some of these footnote clarifications (e.g., that θi ∈ [0.5, 2] is not spectator-consistent and that θi ~ 0.1 is required) carry scientifically important caveats that should arguably appear in the main text rather than in informal footnotes.  
Required fix: Promote the core scientific content of these footnotes (spectator-status backreaction scaling, required fine-tuning factor, distinction between DE-ALP and spectator ALP) into the main body of Section VI in a formal tone, and leave the footnotes, if kept at all, for genuinely ancillary remarks. This improves both clarity and stylistic alignment with PRD norms.

If you want, I can now go through each table line-by-line and recompute every σ and percentage explicitly, but that will be a longer, more mechanical pass.