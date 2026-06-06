# P1B auto-2026-06-06_0021pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (16707 chars)
**Wall time**: 80.4s

---

P1B-E1 (ESSENTIAL)  
Section: References, page 9  
Problem: Multiple references are non‑existent or future‑dated, which is unacceptable for a PRD submission. Specifically:  
- Ref. [3] “P. Diego‑Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro‑ph.CO].” There is currently no arXiv:2509.13654, and ACT DR6 is not yet on arXiv with that identifier. The year 2025 and arXiv ID combination is speculative.  
- Ref.  “Y.-F. Cai, W. Xue, R. Brandenberger, and X. Zhang, Non-gaussianity in a matter bounce, JCAP 0905, 011, arXiv:0903.0631.” The correct arXiv ID is arXiv:0903.0631 [astro‑ph.CO]; the journal metadata is broadly right, but the style is incomplete and not checked vs ADS (minor).  
- Ref.  “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr‑qc].” arXiv:2507.04265 does not exist; this is again speculative future metadata.  
- Ref.  “DESI Collaboration, M. Abdul‑Karim, et al., DESI DR2 results II... PRD 112, 083515 (2025), arXiv:2503.14738 [astro‑ph.CO].” arXiv:2503.14738 does not exist, and DR2 cosmology results are currently 2024/early 2025 with different IDs. The full combination of volume/page/year looks invented.  
- Ref.  “DESI 2024 DR1 BAO, arXiv:2404.03002 [astro‑ph.CO].” This is close to reality but the internal citation elsewhere calls it “DESI 2024 DR1 BAO ” while the reference  text is “DESI 2024 VI: cosmological constraints from BAO” (actual title differs slightly). The authors/et al. list and title need to be matched exactly to ADS/arXiv.  
Required fix:  
- Remove or replace all speculative future references. Every reference must correspond to an actually existing arXiv entry or journal article, with correct year, volume, page, title, and author list. Do not cite non‑existent arXiv IDs or future‑dated ACT DR6 / DESI DR2 / torsion papers. If these results are genuinely “in preparation,” they must be cited as such without fabricated arXiv numbers or journal metadata, and they cannot be used as authoritative constraints. For ACT DR6 cosmic birefringence, either (a) cite a real ACT paper or (b) treat it as private communication / internal analysis, clearly labeled and not treated as a published 2.4–2.9σ sky detection.  

P1B-E2 (ESSENTIAL)  
Section: Abstract, page 1; Sec. IV, page 5; Sec. VI, pages 6–7  
Problem: The claimed ACT DR6 birefringence measurement “β = 0.215° ± 0.074°, 2.4–2.9σ [3]” is attributed to a future paper (ref. [3]) with a non‑existent arXiv ID and unspecified journal. The abstract and body treat this as a published sky detection, yet the cited work does not exist.  
Required fix:  
- Either remove the ACT DR6 numeric result entirely or re‑anchor it to an actually published paper with correct metadata. Until there is a real, citable ACT DR6 birefringence paper, ACT DR6 numbers cannot be quoted as “published Planck/ACT DR6 2.4–2.9σ [2,3]”. At minimum, clearly reclassify any such result as preliminary / internal if it truly exists, and do not use it as a published constraint or as part of the “primary sky detection significance.”  

P1B-E3 (ESSENTIAL)  
Section: Abstract, page 1; Sec. III/Table I, page 3; Sec. II, page 2  
Problem: Load‑bearing ΛCDM+ΔNeff numbers are given (e.g. “H0 = 67.68 ± 1.06 km s−1 Mpc−1,” “ΔNeff = −0.020 ± 0.169”; “309,189 frozen samples across two converged dataset combinations”) and used as if final, but no underlying chains or numerical outputs are provided in the submission and several internal numbers are internally inconsistent:  
- Footnote 1 and surrounding text attempt to reconcile 309,189 total samples with per‑combo counts and burn‑in, but there are multiple, slightly different numbers (“123,368 exact computation,” “123,129,” “119,617 in Fig. 1”), indicating bookkeeping errors.  
- The text claims “Planck-only run (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating,” yet Table I lists the Planck+BAO+SN combination as having 132,949 samples while that same table is also used for the Planck‑only run elsewhere in the narrative. This creates ambiguity about what actually went into Table I.  
Required fix:  
- Provide a consistent, audited set of chain statistics: for each dataset combination, give raw sample count, burn‑in fraction, post‑burn‑in count, and thinning strategy, and ensure these match both Table I and the corner plot. Eliminate contradictory numbers (e.g. 123,368 vs 123,129 vs 119,617). PRD will require that the quoted H0 and ΔNeff values be traceable to a clearly defined chain.  

P1B-E4 (ESSENTIAL)  
Section: Sec. II, page 2; Sec. III/Table I, page 3; Sec. V/Table II, page 4  
Problem: σ‑values and “nσ” distances are presented from different analyses without systematic caveats, and some of these numbers are not re‑derived or traceable:  
- The text states “w0 departs by +4.3σ and wa departs by −3.6σ” relative to ΛCDM for the DESI DR2 w0wa chain, with a footnote that LCDM is unsampled. These “σ” values are posterior‑tail extrapolations, not straightforward mean/σ distances; PRD standards require very clear caveats at every use.  
- In the DESI DR2 table, “w0 = −0.8122 ± 0.0436” vs LCDM w0 = −1 indeed gives (−0.8122 + 1)/0.0436 ≈ 4.3, and “wa = −0.6666 ± 0.1864” vs 0 gives ~3.6. However, this table is labeled “DESI DR2,” yet the same chain is also described as Planck+DESI+DES‑Y5+Pantheon+, so the reference  (DESI DR2 cosmology) cannot account for the quoted σ‑values alone.  
Required fix:  
- Explicitly label in the text, each time such “nσ” distances are quoted, that they are *posterior‑tail extrapolation distances along a Gaussian approximation*, not direct sampled significances or Bayes factors. Ensure the “DESI DR2” label is not misleading; clarify that this is a combined DESI+Planck+DES+Pantheon+ chain, and that the 4.3σ, 3.6σ numbers are not traceable to any single cited external paper but are internal to this work.  

P1B-E5 (ESSENTIAL)  
Section: References, page 9; refs. [1], [4]–[6]  
Problem: The author cites their own papers as “[in preparation] (2026), hUBIFY‑2026‑00x; companion paper, this volume,” with no arXiv IDs or DOIs. For PRD, using “in preparation” work as a core structural foundation (Paper I(a) is repeatedly cited as establishing the main physics) is only acceptable if those companion papers are simultaneously submitted and independently refereed. In addition, the “hUBIFY‑2026‑00x” labels are clearly internal report codes, not established identifiers.  
Required fix:  
- Clarify the status of these works: if they are simultaneously submitted to PRD, state “submitted to PRD” (with manuscript IDs once assigned) and remove internal report codes from the formal reference list. If they are not yet submitted, they should not be used as the primary basis for claims like “The main paper establishes 14 independent structural constraints,” except as “private communication” or speculative. For this paper to stand on its own, its conclusions must not rely critically on unreviewed, unavailable manuscripts.  

P1B-E6 (ESSENTIAL)  
Section: Abstract, page 1; Sec. VI, pages 6–7; Appendix C, page 9  
Problem: The ALP birefringence consistency calculation uses the equation  
\(\beta \approx \frac{\alpha_{\rm EM}}{4\pi} \times 8 \times 1.07 \approx 0.29^\circ\)  
but dimensional and numerical consistency is not properly justified:  
- 8 is described as \(C_{a\gamma}\); 1.07 is apparently \(\Delta\phi/f_a\), but the text gives \(\Delta\phi/f_a \approx 0.65\) for m=H0, θi=1 and “midpoint m≈1.8H0, Δφ/f_a≈1.0.” There is a mismatch between 1.07 and the earlier range; 1.07 is not derived anywhere.  
- In radians, β=0.29° ≈ 5.06×10^{-3}. The prefactor \(\alpha_{\rm EM}/(4\pi) \approx 5.8\times 10^{-4}\) is correct, so the required product \(C_{a\gamma} (\Delta\phi/f_a) ≈ β / [\alpha_{\rm EM}/(4\pi)] ≈ 8.7\), not “≈10.3” as claimed later. The text alternates between 10.3 and numbers consistent with ≈8.7 without recalculating.  
Required fix:  
- Re‑derive the ALP birefringence expression explicitly, with all dimensionless factors stated and a single consistent value for \(C_{a\gamma} \Delta\phi/f_a\). Correct either the 1.07 factor, the 10.3 product, or the β value so that all are self‑consistent. PRD will not accept “hand‑waved” dimensionless products that don’t match the printed numbers.  

P1B-E7 (ESSENTIAL)  
Section: Appendix C, page 9; footnotes 4–5  
Problem: The constraints on the ALP misalignment angle θi and the “spectator” status are internally inconsistent. The main text states “spectator‑consistent corner θi ∼ 0.1 (fn. 4) requires ∼25× misalignment tuning,” but the MCMC explicitly uses a prior θi∈[0.5,2] and does not sample θi∼0.1 at all, while still quoted as supporting spectator consistency.  
Required fix:  
- For a referee‑grade technical paper, you must clearly separate parameter regions that are actually sampled vs those extrapolated. Either (a) rerun the ALP MCMC including θi∈[0.1,0.5] so that the “spectator‑consistent” region is genuinely sampled, or (b) explicitly state that the MCMC does *not* probe the spectator‑consistent region and that any statements about θi∼0.1 are analytical extrapolations, not MCMC‑based. The current text blends these.  

P1B-E8 (ESSENTIAL)  
Section: Sec. IV, pages 5–6; Eq. (1)  
Problem: The NaMaster pipeline “SNR=20.32” and “25.71” numbers for injected signals are presented without sufficient definition of the underlying σ, and the connection between the bias (0.032–0.040°) and the stated SNR is unclear. There is no explicit formula given for SNR nor a table of per‑realization dispersion.  
Required fix:  
- Provide a precise definition: e.g., SNR = β̂/σ(β̂) from the scatter of the 500 MC realizations. Then tabulate the mean β̂ and σ(β̂) for each injection (0, 0.27°, 0.342°), verifying that 0.238° / σ ≈ 20.32 etc. Without this, the reader cannot verify the SNR claims from the information in the PDF, which is required by your own “recompute every quoted σ” standard.  

P1B-M1 (MAJOR)  
Section: Throughout; multiple pages  
Problem: Time‑evolution language and internal bookkeeping labels appear in the body, not only in the references or appendices. Examples:  
- “An earlier count erroneously quoted ‘98.6% quintom‑B’ weight; in the actual converged chain there are zero free‑w0 wa samples at the LCDM point...”  
- “This addresses earlier reviewer concerns that the reported 67.68 was inconsistent...”  
- “the small offset reflecting the chain‑end‑truncation of partial samples at the burn‑in cut” is fine, but “earlier count erroneously quoted…” reads like version history.  
Required fix:  
- Remove all explicit references to “earlier reviewer concerns,” “earlier count erroneously quoted,” etc. PRD manuscripts must read as standalone papers, not internal review logs. If corrections are needed, simply present the corrected values without narrating prior mistakes.  

P1B-M2 (MAJOR)  
Section: Abstract, page 1; Sec. II–III, pages 2–4  
Problem: The abstract claims precise numerical values (H0 and ΔNeff) and sample counts as if they are the final, definitive results. However, the body admits that Bayes factors, AIC/BIC, and the Planck‑only chain are incomplete/missing, and some chain diagnostics (R̂–1) are marginal:  
- The Planck‑only chain is stated to be at R̂−1≈0.05 (non‑converged).  
- DESI DR2 w0wa chain has R̂−1=0.00820, just below the 0.01 target; that is acceptable, but the model‑comparison diagnostics (lnB, ΔAIC, ΔBIC) are explicitly not computed.  
Required fix:  
- Adjust the abstract language to emphasize the *technical verification* nature of the results and their limited statistical status. Make clear that you do not present model‑selection conclusions, only parameter constraints; and that one of the dataset combinations is not fully converged and is not used in headline numbers.  

P1B-M3 (MAJOR)  
Section: Figures and Tables (Fig. 1, Table I, Table II, Table III), pages 3–5, 10  
Problem: Figure and table captions are not always consistent with the body text, and some table entries mix internal narrative comments with numerical results (e.g., Table II’s “canonical quintom signature,” “phantom‑crossing required” within the table). PRD expects tables to be strictly numerical or clearly structured.  
Required fix:  
- Cleanly separate numerical content from interpretive commentary. In Table II, put interpretation in the caption or text, not in the “vs LCDM” column. Ensure Fig. 1’s caption states clearly which dataset combination is shown and how many samples it uses (post‑burn‑in and whether thinned), in a way that matches the numbers given in Sec. III.  

P1B-M4 (MAJOR)  
Section: Data and Code Availability, Appendix A, pages 8–9  
Problem: The paper heavily relies on a GitHub repository and HuggingFace datasets for reproducibility, but PRD will not referee a paper based on external, mutable code repositories that are not archived. Some of the key results (e.g., cosmic birefringence likelihoods) are only referenced as being in scripts and not described in enough detail in the paper itself.  
Required fix:  
- Ensure that all essential analysis steps (likelihood definitions, priors, and main results) are fully specified in the paper or in a stable auxiliary material file, not just by pointing to GitHub. Consider depositing fixed versions of chains and scripts as PRD supplemental material with version tags.  

P1B-M5 (MAJOR)  
Section: Acknowledgments, page 8  
Problem: The acknowledgments explicitly state “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation. All scientific claims… were independently verified by the author.” For a methods‑heavy cosmology paper in PRD, this raises a process concern: you claim independent verification but also heavy AI involvement, yet no details are provided on which steps were AI‑assisted and how you verified them.  
Required fix:  
- Provide a short, clear statement in the cover letter (not necessarily in the paper) explaining how AI tools were used and what safeguards ensured mathematical and bibliographic correctness. In the paper, keep the acknowledgment concise without implying that critical derivations may have been outsourced. Given the citation and numeric inconsistencies described above, I recommend re‑auditing all AI‑assisted content manually.  

P1B-N1 (MINOR)  
Section: Title, page 1  
Problem: The title is extremely long and mixes three distinct topics (“ΛCDM+ΔNeff MCMC Proxy,” “NaMaster Pipeline Recovery,” “Birefringence Consistency Check”) in one line. For PRD, this is borderline unwieldy.  
Required fix:  
- Consider splitting into a main title and a concise subtitle, or narrowing the title to the main technical focus (e.g., “Technical verification of ΛCDM+ΔNeff MCMC and EB pseudo‑Cℓ pipeline for ECH spin‑torsion cosmology”).  

P1B-N2 (MINOR)  
Section: Abstract and Sec. II, page 1–2  
Problem: The paper is explicit about the spin‑torsion module *not* being implemented (stock CAMB; no torsion in the Boltzmann hierarchy). This is good, but the repeated “not a spin‑torsion theory module” language in headings is idiosyncratic.  
Required fix:  
- Streamline phrasing: one clear scope statement early in the paper is sufficient, rather than repeating “NOT a SPIN‑TORSION THEORY MODULE” in multiple headings.  

P1B-N3 (MINOR)  
Section: Throughout  
Problem: Some stylistic elements are non‑standard for PRD (e.g., all caps “RETAINED,” “NOT,” heavy use of em‑dashes, very long parenthetical asides).  
Required fix:  
- Edit for a more conventional PRD style: reduce all‑caps, shorten parentheticals, and move extended discussion into footnotes or appendices.  

P1B-N4 (MINOR)  
Section: Claims Classification Table III, page 10  
Problem: Table III is meta‑text (“claims classification for this companion paper”), which is useful for the author but not typical in published physics articles.  
Required fix:  
- Decide whether this is intended as part of a “reproducibility manifesto.” If PRD editors accept it, fine; but otherwise it might be better moved to supplemental material or removed.  

P1B-N5 (NIT)  
Section: Typographical, several pages  
Problem: A few minor issues:  
- “mbirfringence” typos not observed, but there are repeated “retained RETAINED,” “canonical quintom signature” twice in quick succession, etc.  
- Units “km s−1 Mpc−1” sometimes lack spacing consistency.  
Required fix:  
- Run a thorough copy‑edit and consistency check on units, capitalization, and duplicated phrases.  

P1B-N6 (NIT)  
Section: PACS numbers, page 1  
Problem: PACS numbers are included; PRD is transitioning away from PACS in favor of more modern classification schemes, but this is minor.  
Required fix:  
- Check current PRD author guidelines; remove or update PACS if no longer required.  

---

## Summary recommendation

REJECT  

The manuscript contains serious citation forensics issues (non‑existent or speculative future references, inaccurate ACT/ DESI/ torsion cosmology metadata), internal numerical inconsistencies in key ALP and MCMC results, and an over‑reliance on unreviewed companion papers and external code repositories. While some of these problems are in principle fixable, collectively they fall well below Physical Review D’s standards for bibliographic accuracy, statistical transparency, and reproducibility. A thorough rewrite and re‑audit—both of the physics and of all citations—would be required before a version of this work could be considered.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E9 (ESSENTIAL)  
Section: Abstract, page 1; Sec. III/Table I, page 3; Sec. V A, page 6; Appendix A, page 8  
Problem: The abstract headline “309,189 frozen samples across two converged dataset combinations” is mathematically inconsistent with the chain accounting in footnote 1 and Table I, and the bookkeeping is still not clean. Specifically:  
- Footnote 1 gives “two frozen combinations (176,240 + 132,949 raw accepted samples),” whose sum is 309,189, but Table I’s “Total samples” row lists 176,240 and 132,949 as if each were the total for a *single* combination, while the text elsewhere also uses “309,189 raw samples across 2 frozen dataset combinations.” This mixes “per‑combo total” and “combined total” without ever stating explicitly that 309,189 = 176,240 + 132,949; the wording “across two converged dataset combinations” in the abstract reads as if *each* combination had 309,189 samples.  
- The post‑burn‑in numbers are internally inconsistent: footnote 1 claims 176,240×0.7 ≈ 123,368 post‑burn‑in, but later in the same footnote it states “The post-burnin count of the full-tension subset alone is 123,129 (within ±1% of the 123,368 exact computation, with the small offset reflecting the chain‑end‑truncation…)”. A truncation effect cannot be described as “within ±1% of the exact computation” and simultaneously used as if 123,368 were the correct value.  
- Figure 1’s caption uses “119,617 post-burnin samples, getdist‑thinned from 176,240 raw,” which contradicts both 123,368 and 123,129 as the effective post‑burn‑in size before thinning; the paper never supplies a clear, audited mapping from 176,240 → (burn‑in removal) → (thinning) → 119,617.  
Required fix:  
- Present a simple, audited chain accounting table: for each dataset combination list (i) raw accepted samples, (ii) burn‑in fraction and resulting post‑burn‑in count, (iii) thinning factor and final effective sample count used in figures. Ensure the abstract’s “309,189 frozen samples” language is unambiguous (e.g., “309,189 raw samples in total = 176,240 + 132,949”) and eliminate the 123,368 vs 123,129 vs 119,617 triad of inconsistent numbers.

---

P1B-E10 (ESSENTIAL)  
Section: Sec. III/Table I, page 3; Sec. V A, page 6; Appendix A, page 8  
Problem: Dataset‑combination bookkeeping is still ambiguous and internally inconsistent. It is unclear how many dataset combinations were actually analyzed, which chains are “frozen,” and which combinations correspond to the Table I columns.  
- Sec. III (“The proxy run… has produced two frozen dataset combinations with publication‑quality convergence, plus a third Planck-only run…”) clearly states there are two frozen combinations and one ongoing Planck‑only run.  
- Table I, however, labels the columns only as “Full-tension” and “Planck+BAO+SN,” with no explicit Planck‑only column, yet footnote 1 refers to “The third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating samples, is reported separately in Table I, and is not aggregated into the 309,189-sample headline anywhere in this paper.” There is no third column in Table I, so the Planck‑only chain is not, in fact, “reported separately in Table I.”  
- Sec. V A introduces “four dataset combinations: (1) Planck 2018 NPIPE; (2) +DESI 2024 DR1 BAO; (3) +Pantheon+; (4) +SH0ES H0 prior + DES Y3 S8,” while the abstract lists only “two converged dataset combinations, plus a third Planck-only combination ongoing.” The paper never clearly maps which of these four conceptual combinations correspond to the two columns in Table I and which correspond to the ongoing third chain.  
Required fix:  
- Provide a precise mapping between (Planck, Planck+BAO, Planck+BAO+SN, full‑tension with SH0ES+S8) and the chains actually run. Clarify in a single place: which combinations are converged/frozen, which are still running, and exactly which combinations Table I summarizes. Remove or correct the incorrect statement that the Planck‑only run is “reported separately in Table I.”

---

P1B-E11 (ESSENTIAL)  
Section: Sec. VI, pages 6–7; Appendix C, page 9  
Problem: The ALP birefringence arithmetic and dimensionless products remain inconsistent even beyond the issues already noted in P1B‑E6.  
- Eq. (3) uses “β ≈ [αEM/(4π)] × 8 × 1.07 ≈ 0.29°.” Converting 0.29° to radians gives β ≈ 5.06×10⁻³, while αEM/(4π) ≈ 5.8×10⁻⁴, so the required product Caγ(Δϕ/fa) is β/[αEM/(4π)] ≈ 8.7, not 8×1.07 ≈ 8.56, and certainly not 10.3 as quoted later. The text claims both “≈ 0.29°” and “Caγ(Δϕ/fa) ≈ 10.3,” which cannot both be true for the same β.  
- Later in Sec. VI the paper states: “β = 0.342° in radians is 5.97×10⁻³, the prefactor αEM/(4π) is 5.8×10⁻⁴, giving CaγΔϕ/fa = β/[αEM/(4π)] ≈ 10.3.” This is arithmetically correct for β = 0.342°, but it is inconsistent with Eq. (3), which uses β ≈ 0.29° and 1.07 as the Δϕ/fa factor.  
- The text claims “The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8H0, Δϕ/fa ≈ 1.0,” yet Eq. (3) uses 1.07 instead of 1.0, and Eq. (2) gives Δϕ/fa ≈ 0.65 for m = H0, θi = 1, with no derivation of 1.07 anywhere. The sequence 0.65 → 1.0 → 1.07 is never justified numerically.  
Required fix:  
- Choose a single fiducial benchmark and recompute all numbers self‑consistently. If βfid = 0.342° is used to define CaγΔϕ/fa ≈ 10.3, then Eq. (3) must reflect that, and the 0.29° and 1.07 factors must be corrected. If βfid = 0.27° is used, recompute CaγΔϕ/fa and use that everywhere. Remove the unexplained 1.07 factor or derive it explicitly from the ALP ODE solution, and ensure that Eq. (2), Eq. (3), and the later “10.3” product all correspond to the *same* parameter point.

---

P1B-E12 (ESSENTIAL)  
Section: Sec. VI, page 7; Appendix C, page 9  
Problem: The stated ALP parameter ranges and derived β‑range envelope are not fully consistent or properly justified.  
- Sec. VI states: “Across the natural parameter range m/H0 ∈ [1, 3], θi ∈ [0.5, 2]: Δϕ/fa ∈ [0.2, 1.1].” This gives CaγΔϕ/fa between (4×0.2=0.8) and (12×1.1=13.2). Plugging this into β = [αEM/(4π)]CaγΔϕ/fa yields β ∈ [0.8×5.8×10⁻⁴, 13.2×5.8×10⁻⁴] rad ≈ [0.026°, 0.44°]. The text indeed notes this “wider naive envelope [0.027, 0.44]°.”  
- However, the paper then asserts a narrower “prediction spans β ≈ 0.17–0.43° over Caγ ∈ [4, 12], m/H0 ∈ [1, 3], θi ∈ [0.5, 2]… obtained from a joint-trajectory scan,” without giving any justification of why the lower range 0.027–0.17° is excluded other than a qualitative statement. No plot, table, or quantitative condition (e.g., cuts in likelihood or physicality) is given to support this narrower envelope.  
- The text later treats “CaγΔϕ/fa ≈ 10.3” as a central value with Δϕ/fa ∈ [0.2, 1.1] implying Caγ ∈ [9, 51]. For Δϕ/fa = 1.1 this gives Caγ ≈ 9.3 (consistent with the stated “∼9”), but for Δϕ/fa = 0.2 it gives Caγ ≈ 51.5. The lower edge of β ≈ 0.17° used in the “0.17–0.43°” envelope corresponds roughly to CaγΔϕ/fa ≈ 5, which is inconsistent with the central “10.3” product.  
Required fix:  
- Provide a quantitative description of the “joint-trajectory scan” that yields β ∈ [0.17, 0.43]°: what grid or MCMC was run, what (m/H0, θi, Caγ) points were sampled, and what criterion defines the envelope. If the narrower range is meant to correspond to a particular confidence region (e.g. 68% or 95%), state this and show at least a summary table. Otherwise, retain only the mathematically correct envelope [0.027, 0.44]° or clearly state that 0.17–0.43° is an illustrative subset, not a rigorous prediction band.

---

P1B-E13 (ESSENTIAL)  
Section: Sec. VI, page 7; Appendix C footnotes 4–5, page 9  
Problem: The quantitative “∼25× misalignment tuning” claim is only loosely justified and conflates multiple ratios.  
- Footnote 4 states: “at θi = 0.1 vs the scan-midpoint θi = 0.5 the backreaction is Ωa(0.1)/Ωa(0.5) ∼ 1/25 (i.e., a ∼25× fine-tuning of the misalignment initial condition).” This follows from ρa ∝ θi² and is correct for the *energy-density ratio*.  
- But θi itself is only a factor of 5 smaller (0.1 vs 0.5), so the “25× tuning” is in Ωa, not in θi. Elsewhere the text speaks of “the ∼25× misalignment tuning required for the headline result,” which is potentially misleading: the tuning in *angle* is 5×, while the tuning in *energy density* is 25×.  
Required fix:  
- Distinguish clearly between tuning in θi and tuning in Ωa. For example: “a factor 5 reduction in θi (from 0.5 to 0.1) implies a 25× reduction in Ωa.” Do not describe this as “25× misalignment tuning” without specifying whether the tuning refers to the angle or the energy density.

---

P1B-M6 (MAJOR)  
Section: Sec. II, page 2; Sec. III/Table I, page 3; Sec. VII, page 7  
Problem: Some “consistency” statements about H0 and ΔNeff are not numerically quantified where they are first used, making it hard for the reader to verify them.  
- Sec. II states that “Both frozen dataset combinations find ΔNeff consistent with zero … and H0 consistent with standard ΛCDM (67.68 ± 1.06 …; 67.79 ± 1.09 …),” but the baseline Planck ΛCDM value to which “consistent” refers is nowhere given numerically in this paper.  
- Similar language appears in Sec. VII (“consistent with standard Planck ΛCDM”) without quoting the reference value or the delta/significance.  
Required fix:  
- Whenever “consistent with standard ΛCDM” is used in a load‑bearing way, provide the reference Planck ΛCDM values (e.g., H0 = 67.4 ± 0.5 km s⁻¹ Mpc⁻¹) and state the numerical difference and its significance (e.g., 0.3σ). This avoids unquantified hedging.

---

P1B-M7 (MAJOR)  
Section: Fig. 1 and caption, page 5; Sec. III/Table I, page 3  
Problem: Figure 1 caption vs body text mismatch in sample counts and dataset labeling.  
- Fig. 1 is captioned as “Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote 1) over Planck+BAO+SN+H0+S8,” implying it corresponds to the “full-tension” combination that includes SH0ES and S8.  
- Table I labels the first column as “Full-tension” and lists “Total samples 176,240,” but gives no post‑burn‑in or thinning numbers. Footnote 1 attempts to explain post‑burn‑in and thinning but introduces additional numbers (123,368, 123,129, 119,617) that do not clearly map onto Fig. 1 or Table I.  
- The text in Sec. III discusses both a “full-tension subset specifically, 176,240×0.7 ≈ 123,368 post-burnin” and a “post-burnin count … 123,129 … the 119,617 figure in Fig. 1 reflects additional getdist effective-sample weight-based thinning,” but this chain of transformations is not visible to the reader in any table or figure.  
Required fix:  
- In the Fig. 1 caption, explicitly state the burn‑in fraction and thinning procedure that lead from 176,240 to 119,617. In Table I (or a new table), provide the same numbers so the reader can verify that the figure and table refer to the same chain with consistent statistics.

---

P1B-M8 (MAJOR)  
Section: Sec. IV, page 5–6; Eq. (1); Table III, page 10  
Problem: The NaMaster SNR definition remains underspecified, and the numerical SNR claims still cannot be independently recomputed from the text.  
- Eq. (1) states: “Injecting … β = 0.27° … recovers β̂NaMaster = 0.238° (pipeline-recovery SNR = 20.32),” and later: “for β = 0.342° … the pipeline recovers 0.302° at SNR = 25.71; for β = 0, recovery is consistent with zero.”  
- The text mentions 500 MC realizations but does not present the sample standard deviation σ(β̂) for each injection, nor an explicit formula SNR = β̂/σ(β̂) or SNR = (β̂−βtrue)/σ(β̂). Without σ(β̂), the values 20.32 and 25.71 cannot be independently checked.  
- Table III lists “β̂NaMaster = 0.238° (500-MC) — Numerical, Verified, Pipeline; MC bias table,” yet no such “MC bias table” appears in the manuscript.  
Required fix:  
- Include a small table giving, for each injection βtrue ∈ {0, 0.27°, 0.342°}, the mean recovered β̂ and the standard deviation σ(β̂) across the 500 realizations, and explicitly define SNR in terms of these quantities. Ensure that the numbers in Eq. (1) and in any claims in Sec. IV correspond exactly to this table.

---

P1B-M9 (MAJOR)  
Section: Abstract, page 1; Sec. IV, page 5; Sec. VI, pages 6–7  
Problem: Some abstract statements about the status and role of the birefringence measurements are not fully faithful to the body.  
- The abstract says: “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2,3]; the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements.” This is consistent with Sec. IV’s scope note, but Sec. VI also describes an “internal model-independent MCMC fit… with β as a free parameter,” which yields βfree = 0.344° ± 0.096°. The abstract does not mention this internal sky fit at all, even though it contributes to the interpretation of the ALP model.  
- Sec. VI additionally gives an auxiliary combined value “βcombined = 0.241° ± 0.061° (3.9σ)” from Planck NPIPE and ACT DR6. The abstract does not mention that this 3.9σ figure exists but is explicitly *not* used as the headline, which could be confusing when readers compare abstract and body.  
Required fix:  
- Either mention briefly in the abstract that internal β fits are performed but that the headline sky significance remains the published 3.6σ result, or ensure that all sky‑significance numbers mentioned in the abstract (2.4–2.9σ, 3.6σ) are clearly traceable to the body without omission that could mislead readers about what was actually fit in this work.

---

P1B-M10 (MAJOR)  
Section: Appendix A (“What is NOT included”), page 8  
Problem: The data/code‑availability narrative introduces potential ambiguity about which results are reproducible from the paper alone.  
- The NaMaster and ALP likelihood configurations are described as being in scripts and repositories, but the paper itself does not provide enough detail (e.g. the exact ℓ‑binning, noise spectra, or likelihood functional forms) to reproduce the key numerical SNR and βALP results without access to the mutable GitHub/HuggingFace resources.  
- Appendix A states “No CMB polarization map analysis code is provided beyond the NaMaster driver script; all published birefringence values are literature citations,” but Sec. VI describes *new* internal MCMC fits to EB spectra (βfree, βALP). The paper does not specify the likelihood function for these fits (e.g., which EB bandpowers, covariance treatment, and calibration nuisance parameters), only that “Planck PR4 + ACT DR6 EB-spectrum likelihoods … with shared calibration covariance” are used.  
Required fix:  
- For the ALP and model‑independent EB fits, provide at least a schematic likelihood definition in the paper (e.g., χ²(β) in terms of EB bandpowers and covariance) and the exact ℓ‑range and binning used. This is necessary so that PRD readers can understand and, in principle, reproduce the fits independently of the external code repository.

---

P1B-N7 (MINOR)  
Section: Sec. III, page 3; Sec. V, page 6; Sec. VII, page 7  
Problem: Some “headline” language around the w0–wa results and “canonical quintom signature” is repeated in both table commentary and body text in a way that is more rhetorical than necessary for PRD style.  
- Table II already carries interpretive phrases in the “vs ΛCDM” column (“phantom-crossing required,” “canonical quintom signature”), and similar phrases appear in the main text. This blends numerical reporting and interpretation.  
Required fix:  
- Remove interpretive labels from the table body, keeping only numerical distances (e.g. “4.3σ from −1,” “3.6σ from 0”), and reserve commentary like “canonical quintom signature” for the text or caption.

---

P1B-N8 (MINOR)  
Section: References, page 9–10  
Problem: The reference list still mixes informal explanatory commentary with formal citations in a way that is atypical for PRD.  
- Examples: Ref.  includes an extended explanatory clause about how the value “used at L256/L416 of P1B” was chosen; Ref.  contains a long parenthetical description of how the paper is “used in P1A Sec. VI to point readers to the bounce-class alternative…” This is meta‑commentary about how the author uses the references rather than bibliographic information.  
Required fix:  
- Move such usage notes to the main text or a footnote and keep the reference entries themselves in standard bibliographic form (authors, title, journal, volume, year, arXiv).

---

Overall, the additional pass reveals several still‑unresolved arithmetic and bookkeeping inconsistencies (especially in the ALP section and MCMC chain accounting) and some abstract/body mismatches and under‑specified likelihood definitions that would require correction for PRD‑level rigor.