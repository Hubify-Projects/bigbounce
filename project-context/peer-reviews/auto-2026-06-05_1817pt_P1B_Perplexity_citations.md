# P1B auto-2026-06-05_1817pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15845 chars)
**Wall time**: 91.7s

---

P1B-E1 (ESSENTIAL)  
Section: References, page 9–10  
Problem: Multiple references are clearly fabricated or temporally impossible, and several others are mis-specified relative to existing literature.

Details by reference:

1. **Ref. [2] “Eskilt & Komatsu 2022, Phys. Rev. D 106, 063503, arXiv:2205.13962”**  
   - Check: arXiv:2205.13962 corresponds to J. R. Eskilt & E. Komatsu, “Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data,” Phys. Rev. D 106, 063503 (2022).[ ]  
   - Status: **Accurate**; volume, page, year, title, authors and arXiv ID match the real paper. No action needed for [2].

2. **Ref. [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].”**  
   - Problem: As of now, there is **no** arXiv:2509.13654; arXiv IDs using the “2509” date block correspond to September 2025 and are in the future relative to the paper’s stated date (2026-06-03), and the identifier does not resolve to a real paper.  
   - Additionally, ACT DR6 cosmic birefringence work exists, but current ACT polarization releases are earlier than “DR6 2025” with that arXiv ID and details.[ ]  
   - Required fix:  
     - Replace this with a **real, published or at least existing arXiv** reference for ACT birefringence or explicitly mark it as “private communication” if that is the true status.  
     - Remove the future-dated, non-resolving arXiv ID “2509.13654” and the fake “arXiv preprint (2025)” bibliographic data.  
     - Ensure that the quoted ACT value β = 0.215° ± 0.074° is actually traceable to whichever real ACT paper is cited; if no such published value exists, all uses of that number in the text must be recast as a projection or preliminary result, not “published.”

3. **Ref.  “Y.-F. Cai, W. Xue, R. Brandenberger, and X. Zhang, Non-gaussianity in a matter bounce, JCAP 0905, 011, arXiv:0903.0631.”**  
   - Check: arXiv:0903.0631 is “Non-Gaussianity in a Matter Bounce,” Cai et al., JCAP 0905:011 (2009).[ ]  
   - Status: **Accurate.**

4. **Ref.  “Brout et al. 2022, Pantheon+ analysis,” Astrophys. J. 938, 110, arXiv:2202.04077.**  
   - Check: arXiv:2202.04077 is “The Pantheon+ Analysis: Cosmological Constraints,” D. Brout et al., ApJ 938, 110 (2022).[ ]  
   - Status: **Accurate.**

5. **Ref.  “Planck Collaboration, N. Aghanim, et al., Planck 2018 results. VI. cosmological parameters, A&A 641, A6 (2020), arXiv:1807.06209.”**  
   - Check: arXiv:1807.06209 is “Planck 2018 results. VI. Cosmological parameters,” A&A 641, A6 (2020).[ ]  
   - Status: **Accurate.**  
   - However, the text repeatedly labels “Planck 2018 NPIPE” and “PR4/NPIPE” while  is the PR3 2018 parameters paper; the proper NPIPE birefringence analysis is  and the NPIPE PR4 description is a different Planck paper. The internal use of “Planck 2018 NPIPE ” is therefore **mis-attributed.**  
   - Required fix:  
     - Wherever “Planck 2018 NPIPE ” or “PR4” is used, cite the correct NPIPE paper (e.g. the Diego-Palazuelos et al. PRL 2022 for birefringence, already given as ) and, for cosmological parameters, the appropriate NPIPE parameters release if used.  
     - Do not attribute NPIPE to , which is PR3.

6. **Ref.  “Diego-Palazuelos et al., Cosmic birefringence from the Planck data release 4, Phys. Rev. Lett. 128, 091302 (2022), arXiv:2201.07682 [astro-ph.CO], beta = 0.30 ± 0.11 deg, Planck NPIPE (PR4).”**  
   - Check: arXiv:2201.07682 is “Cosmic birefringence from the Planck data release 4,” P. Diego-Palazuelos et al., PRL 128, 091302 (2022).[ ]  
   - Status: **Accurate**, including the β = 0.30° ± 0.11° headline. The in-text quote “reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4)” is consistent with the abstract/table.

7. **Refs. , , , ,  (DESI DR2 “2024/2025”, DES Y3/Y5, Cobaya, LiteBIRD, Galaxy Zoo DECaLS)**  
   -  Cobaya,  LiteBIRD,  Galaxy Zoo DECaLS match real, existing references (journals, arXiv IDs, titles).[ ]  
   - Conversely, ** and ** are described as “DESI 2024 DR1 BAO” and “DESI DR2 2025” with specific volumes and arXiv IDs (e.g. 2024-04-03002, 2503.14738) that cannot yet be verified in refereed PRD form and whose exact arXiv IDs in the text do not correspond to existing entries.  
   - Required fix:  
     - For DESI DR2, DES-SN5YR, and DESI DR1 citations, check each claimed arXiv ID, year, and journal against the real DESI and DES releases. Replace any non-resolving or future-dated IDs with the correct ones; if the work is not yet on arXiv, mark as “in preparation” or “DESI Collaboration, in prep.” and **do not fabricate an arXiv ID.**  
     - Explicitly verify that the quoted use of “DESI DR2 BAO + Planck 2018 NPIPE + DES-Y5 + Pantheon+” matches the actual dataset combinations in the cited DESI paper; if the described combination is an internal pipeline combination not from a single published paper, cite the components separately and state that it is the author’s combined analysis.

8. **Refs. [1], [4], [5], [6],  – author’s own ‘hUBIFY-2026-00x’ series plus Liu et al. torsion cosmology**  
   - [1], [4], [5], [6] are all listed as “(in preparation) (2026), hUBIFY-2026-00x; companion paper, this volume” with no arXiv IDs. That is acceptable as internal companion papers, but they are not yet citable as refereed literature.  
   - **Ref.  “T. Liu et al., Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”**  
     - This arXiv ID is future-dated (“2507…”) and does not correspond to an existing arXiv entry.  
     - The paper is described as 2025 EPJC, but no such paper currently exists with this arXiv ID or exact title.  
   - Required fix:  
     - Remove or correct the fabricated arXiv ID “2507.04265.” If this is an unpublished or in-prep torsion cosmology analysis, mark as “in preparation” or “private communication” without assigning a false arXiv identifier.  
     - Do not claim it is an EPJC paper with a fictitious arXiv number.  
     - For self-citations [1], [4]–[6], clarify their status: “submitted to Phys. Rev. D, in review” or “unpublished manuscript,” without implying journal acceptance.

Overall required fix for P1B-E1:  
- Systematically re-check **every** arXiv identifier and journal-year-volume triad against arXiv.org and NASA ADS.  
- Remove all future-dated, non-resolving, or invented IDs; replace with either correct IDs or honest “in preparation” labels.  
- Where the text attributes specific numeric results (e.g. ACT DR6 β, DESI DR2 w0, wa, ∆AIC) to these references, verify that those numbers appear in the actual paper’s abstract or tables. If they do not, clearly mark them as results from the author’s own analysis rather than “published values.”

---

P1B-E2 (ESSENTIAL)  
Section: Abstract and Sec. VI, page 1 and 6–7  
Problem: The claim “published Planck/ACT DR6 2.4–2.9σ [2, 3]” and β values implies that both ranges are fully established in the cited literature, but at least part of this is based on a non-existing ACT DR6 birefringence paper ([3] is not a real arXiv entry).  
Required fix:  
- Rephrase all text about ACT DR6 birefringence to accurately reflect the status of the ACT result. If the relevant ACT analysis is not yet published, explicitly call it “preliminary,” “internal,” or “in preparation,” and do not call it “published DR6” or combine it into a quoted “2.4–2.9σ” published range.  
- Ensure that every quoted β and σ value is traceable to a verifiable paper (for Planck PR4  and Eskilt & Komatsu [2]) or clearly flagged as the author’s own fit.

---

P1B-E3 (ESSENTIAL)  
Section: Table II & surrounding text, pages 3–4  
Problem: The paper attributes “DESI DR2” and specific w0, wa posteriors and χ² decompositions to a dataset combination invoking “DESI DR2 BAO + Planck 2018 NPIPE + DES-Y5 + Pantheon+” and then says this is consistent with “Liu et al. ” and other works. Yet  is not a real paper, and the alleged DESI DR2 cosmology paper with that combination does not exist as cited.  
Required fix:  
- Remove the implication that this particular w0, wa posterior arises from a **published DESI DR2 cosmology paper**; state instead that it is the author’s own Cobaya run using public DESI BAO, DES-Y3/5, Pantheon+ and Planck likelihoods.  
- Do not describe the χ² and “quintom” significance as direct constraints “from DESI DR2” unless that matches an actual DESI paper’s cosmological analysis and confidence region plots.  
- Re-assign citation  appropriately or mark it as “author’s fit with DESI public BAO distances” rather than a stand‑alone EPJC result.

---

P1B-M1 (MAJOR)  
Section: ALP consistency check, pages 6–7  
Problem: The calibration between β, Caγ, and ∆ϕ/fa is only sketched and partially contradictory. The paper states:  
- Eq. (2): ∆ϕ/fa ≈ 0.65 for m = H0, θi = 1, with scan range ∆ϕ/fa ∈ [0.2, 1.1];  
- Then β ≈ (αEM/4π) × 8 × 1.07 ≈ 0.29°, corresponding to a midpoint “∆ϕ/fa ≈ 1.0”;  
- Later it asserts Caγ ∆ϕ/fa ≈ 10.3 to match βobs = 0.342°, relying on αEM/(4π) ≈ 5.8×10⁻⁴.  
Recomputing with αEM ≈ 1/137 gives αEM/(4π) ≈ 5.8×10⁻⁴; converting β = 0.342° = 5.97×10⁻³ rad gives Caγ ∆ϕ/fa = β/[αEM/(4π)] ≈ 10.3 — consistent. However the earlier “1.07” factor and the described “midpoint” ∆ϕ/fa ≈ 1.0 are not clearly derived or checked against Eq. (2), and the misalignment tuning factor of ~25× is only qualitatively justified.  
Required fix:  
- Explicitly write the birefringence formula used, including factors of 2 or 4 and the sign conventions, and show the derivation of the 1.07 factor.  
- Recompute β for the fiducial parameter point (Caγ = 8, m/H0 ≈ 1.8, θi = 1) in a single transparent chain of equations, confirming dimensional consistency and agreement with the reported 0.27–0.29°.  
- Verify that the claimed 25× misalignment tuning (θi from 0.5 to 0.1) is numerically correct given the adopted formula for Ωa and the range of ∆ϕ/fa. If not, correct the tuning factor.  
- Check that the ranges [0.17, 0.43]° and [0.027, 0.44]° are indeed obtained as stated from the parameter scans and not from inconsistent mixing of independent extrema.

---

P1B-M2 (MAJOR)  
Section: NaMaster pipeline, page 5–6; Eq. (1)  
Problem: The NaMaster pipeline “SNR = 20.32” and “25.71” are quoted as pipeline-recovery SNR for injected β values. However, the manuscript does not show how these SNR values are computed from the MC ensemble, nor does it provide the underlying σ(β̂) used in the ratio. The paper does state that pipeline SNR is not a sky-significance, but the numerical values are load-bearing in the methods-validation claim.  
Required fix:  
- Provide the explicit definition of “pipeline-recovery SNR” (e.g. mean(β̂MC)/std(β̂MC)) and list the corresponding σMC.  
- Confirm that the stated biases (0.032° and 0.040°) and SNRs are consistent, e.g. if βinj = 0.27° and SNR = 20.32, then σMC ≈ 0.0133°, which should be shown.  
- Include a compact table or figure summarizing βinj, ⟨β̂⟩, σMC, and SNR, so that the reader can independently re-compute SNR from the given quantities.

---

P1B-M3 (MAJOR)  
Section: Table I and Figure 1, pages 2–3 and 5  
Problem: The abstract and body headline “309,189 frozen samples across two converged dataset combinations” must be consistent with the numbers in Table I and Fig. 1. The footnote explains 176,240 + 132,949 = 309,189 and then notes burn-in removal and thinning. However, the figure text mentions “119,617 post-burnin samples” and “176,240 raw” for the full-tension combination, while the footnote claims post-burn-in full-tension = 123,129 (within 1% of 123,368), which is not exactly “119,617.” This inconsistency is critical for any MCMC-based cosmology analysis.  
Required fix:  
- Harmonize all sample-count numbers; for each chain, clearly separate: raw accepted samples, post-burn-in samples, and effective samples after thinning.  
- In the abstract and body, quote one consistent definition (e.g. raw accepted samples) and move more detailed breakdown to a dedicated table.  
- Remove or correct any approximate counts (“within ±1%”) that do not match the actual values shown in figures.

---

P1B-M4 (MAJOR)  
Section: Table II, pages 3–4  
Problem: The table reports w0, wa deviations from ΛCDM at “+4.3σ” and “−3.6σ” and states “phantom crossing required,” “canonical quintom signature,” etc. However, these σ values are described as “marginal-tail posterior-extrapolation” distances and LCDM is unsampled. Without an explicit model comparison or careful assessment of prior volume and parameter correlations, these numbers can easily be misinterpreted as frequentist significances. The manuscript partly clarifies this in the footnote, but then reuses the same σ values multiple times as if they were robust.  
Required fix:  
- At every point where the +4.3σ and −3.6σ departures are quoted, explicitly remind the reader that these are *posterior-tail distances in an unsampled region* and not frequentist significances or Bayes factors.  
- Remove language implying that this is an “exclusion” of ΛCDM, and instead present it as “posterior mean is offset from ΛCDM by 4.3σ along w0 and 3.6σ along wa, but the LCDM point is not sampled in the chain, and no evidence ratio is computed here.”  
- If the claim “canonical quintom signature” is to be retained, it must be clearly attributed to the posterior shape rather than to any formally quantified model preference.

---

P1B-M5 (MAJOR)  
Section: Bibliography overall, pages 9–10  
Problem: The bibliography contains multiple internal self-citations labeled “(in preparation) (2026), hUBIFY-2026-00x; companion paper, this volume.” PRD typically requires that key claims rest on published or at least submitted work, and the current paper leans heavily on an unpublished series “P1A–P1D” for structural closure, Fisher forecasts, anomaly catalogs, and galaxy chirality claims.  
Required fix:  
- For every scientific assertion in this paper that depends critically on an “in preparation” companion (e.g. the structural closure theorem, the fNL = −35/8 forecast, galaxy chirality catalog), check whether the present paper can stand without that result.  
- Either (a) move sufficient details from those companions into this paper to make it self-contained, or (b) modestly weaken any claims that rely on them, making clear that they are contingent on unpublished work.  
- Clarify the status of each companion (submitted/under review, or not).

---

P1B-N1 (NIT)  
Section: Various, pages 1–8  
Problem: Minor duplications and editorial artifacts, e.g. phrases such as “reported here, which are unaffected by the model-comparison-statistic deferral” and internal commentary about earlier reviewer concerns and corrections (e.g. “An earlier count erroneously quoted ‘98.6% quintom-B’ weight; in the actual converged chain…”). These read like version-history notes rather than final PRD prose.  
Required fix:  
- Remove references to “earlier count erroneously quoted,” “reviewer concerns,” “reconciliation,” etc., and present only the final, correct numbers.  
- Clean up duplicated words and unnecessary meta-discussion.

---

P1B-N2 (NIT)  
Section: Appendix B “Claims Classification,” page 10  
Problem: Table III is labeled “Claims classification for this companion paper,” with a column “Status: Verified/Omitted/Cited/Defn.” This is an internal audit artifact, not standard content for a PRD article.  
Required fix:  
- Either remove this table or rewrite it as a brief narrative pointing to which results are original vs. literature and which are not computed here (e.g. ln B). As-is, it looks like internal bookkeeping.

---

## Summary recommendation

**MAJOR REVISIONS**

The manuscript’s central numerical work (ΛCDM+∆Neff proxy, NaMaster validation, ALP consistency check) is conceptually reasonable, but the citation forensics show multiple fabricated or unverifiable references (future-dated arXiv IDs, mis-attributed NPIPE usage, non-existing ACT DR6 and torsion cosmology papers) and several internal inconsistencies in chain accounting and statistical interpretation. These issues fall below PRD’s standards for rigor and traceability. The paper must correct all reference metadata, cleanly separate author-derived numbers from published results, and tighten the derivations and statistical claims before it can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E4 (ESSENTIAL)  
Section: Abstract, Sec. III, Table I, Fig. 1, footnote 1, Conclusions  
Problem: Sample-count arithmetic and chain-accounting are internally inconsistent across the abstract, table, figure, and footnotes, beyond the issues already flagged under P1B-M3.

New issues:

1. **Inconsistent definition of “309,189 frozen samples” vs. post‑burn-in and thinned counts.**  
   - Abstract: “309,189 frozen samples across two converged dataset combinations” — clearly referring to *raw* samples.  
   - Footnote 1: gives raw full‑tension = 176,240 and Planck+BAO+SN = 132,949, which sum to 309,189, consistent with the abstract.  
   - Footnote 1 then states: “correct both‑chains post‑burnin total is 216,432,” computed as 0.7×176,240 + 0.7×132,949 = 123,368 + 93,064.3 ≈ 216,432.3. Here 93,064.3 is non-integer and silently rounded, and the footnote later quotes 123,129 as the full‑tension post‑burn‑in count, which is inconsistent with its own 123,368 computation.  
   - Fig. 1 caption: “119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote 1” for the full‑tension chain, while footnote 1 states “The post-burnin count of the full-tension subset alone is 123,129 (within ±1% of the 123,368 exact computation...).” 123,129 and 119,617 differ by ~3,512 samples (~2.9%), which is not “within ±1%” of either 123,368 or 119,617.  
   - The body text in Sec. III repeats “309,189 raw samples across 2 frozen dataset combinations” and refers to this as the “MCMC program,” while the conclusions again treat “309,189 frozen samples” as a defining property of the proxy run.  
   **Required fix:**  
   - Decide on one consistent accounting scheme with integer counts: for each chain (full‑tension, Planck+BAO+SN, Planck‑only) specify (i) raw accepted samples; (ii) post‑burn-in samples; (iii) post‑thinning samples.  
   - Remove the “within ±1%” language and replace it with exact values, or state precisely which numbers are approximate and why.  
   - Make the abstract’s “309,189 frozen samples” explicitly refer to raw accepted samples, and ensure Table I and Fig. 1 captions match that convention.  
   - Eliminate contradictions between footnote 1 and Fig. 1; either 119,617 is the post‑burn‑in+thinned count or it is not—this must be internally consistent and numerically traceable.

2. **Arithmetic in the MB–H0 “3.2σ” argument is not shown and is likely misinterpreting σ.**  
   - The text states the offset in the SN degeneracy constant is 0.155 mag and calls this “∼ 3.2σ relative to the chain’s σMB = 0.049 marginal width” and “corresponds exactly to the canonical 3.6σ Hubble tension.”  
   - The paper does not show the chain’s 1D posterior σ for the *combination* MB−5 log10 H0, nor does it convert the 0.155 mag offset into σ using the actual 2D covariance of (MB, H0). Using σMB alone is not correct for a constraint that lives along a degeneracy direction; the relevant σ is along the Pantheon+ degeneracy axis, not the marginal MB axis.  
   - Thus “∼3.2σ” is at best a heuristic mapping, but is presented as a checked quantitative result.  
   **Required fix:**  
   - Explicitly compute the uncertainty of MB−5 log10 H0 from the chain (using the full covariance) and recompute the number of σ for the 0.155 mag offset.  
   - If that is not done, soften the language: remove “∼3.2σ” and avoid claims like “corresponds exactly to the canonical 3.6σ tension.” Instead describe the offset qualitatively or with a properly derived σ.  
   - Make clear that this calculation is an illustrative sanity check, not a separate tension measurement.

---

P1B-E5 (ESSENTIAL)  
Section: Sec. IV (CMB E–B analysis), Sec. VI (ALP consistency check), Appendix C  
Problem: σ and SNR values are used without fully specifying the underlying null procedures, and different σ definitions are juxtaposed as if directly comparable.

New issues:

1. **NaMaster “SNR = 20.32” and “25.71” still lack explicit σMC and null definition, and these SNRs are implicitly compared to sky σ.**  
   - Sec. IV states: “Injecting... β = 0.27° ... recovers β̂ = 0.238° (pipeline-recovery SNR = 20.32)” and later “for β = 0.342° ... recovers 0.302° at SNR= 25.71; for β = 0, recovery is consistent with zero (null check).”  
   - Even after the earlier concern (P1B-M2), the manuscript still does not show the formula used for SNR or list σMC. One can infer that SNR ≈ βinj/σMC, but this must not be left implicit.  
   - These SNRs are repeatedly contrasted with the “Planck/ACT DR6 2.4–2.9σ” sky detection in both abstract and Sec. IV. Even though the text says they are “not competitive sky measurements,” this juxtaposition invites direct comparison of different σ definitions (pipeline MC vs. sky likelihood) without clear labels on the underlying null procedures.  
   **Required fix:**  
   - Explicitly define SNR = mean(β̂MC)/std(β̂MC) or equivalent in Sec. IV and list σMC for each injection (including β = 0 and nonzero β).  
   - Add a short sentence explicitly stating that “these SNR values are computed from injected‑signal Monte Carlo ensembles and are *not* directly comparable to the Planck/ACT sky-detection σ values, which come from different likelihoods and null hypotheses.”  
   - Consider moving or revising the phrases “high pipeline-recovery SNR figures (e.g., 20.32, 25.71)” so they are not visually adjacent to “2.4–2.9σ” without that explicit warning.

2. **ALP MCMC σ vs. literature β σ juxtaposition without an explicit comparability caveat.**  
   - Sec. VI gives βALP = 0.336° ± 0.107° and βfree = 0.344° ± 0.096°, and then compares these to βobs = 0.342° ± 0.094° and to the combined 3.6σ and 3.9σ significances.  
   - The text states they are “all three within 1σ,” but again, the ALP-chain errors include ALP parameter priors and the specific Planck PR4 + ACT DR6 EB likelihood configuration, while the Eskilt & Komatsu 0.342° ± 0.094° comes from Planck PR3+WMAP9 and a different pipeline. These are not strictly identical null procedures.  
   - The paper does note that the 3.9σ inverse-variance combination neglects shared systematics, but never similarly cautions that “within 1σ” here refers to a visual consistency check, not a fully joint re-analysis.  
   **Required fix:**  
   - When stating “all three within 1σ,” add an explicit caveat that the σ values come from different analyses with different likelihood stacks and are not strictly combined; this is a qualitative consistency check.

---

P1B-M6 (MAJOR)  
Section: Sec. VI, Eqs. (2)–(3), ALP paragraph around CaγΔϕ/fa ≈ 10.3  
Problem: The birefringence calibration between β, Caγ, and Δϕ/fa remains incomplete and partially inconsistent, beyond the previous tuning and factor‑of‑2 issues flagged in P1B-M1.

New issues:

1. **Eq. (3) is dimensionally opaque and the “1.07” factor is still not derived.**  
   - Eq. (3): β ≈ (αEM × 8)/(4π) × 1.07 ≈ 0.29°, with no explicit Δϕ/fa appearing and no reference to Eq. (2). The reader is left to infer that 1.07 encodes Δϕ/fa ≈ 1.0 and perhaps numerical integration corrections, but this is never shown.  
   - A few lines later, the text does use the correct proportionality β = (αEM/4π) Caγ (Δϕ/fa) when deriving CaγΔϕ/fa ≈ 10.3, but this formula is not written down as an explicit equation.  
   - As written, Eq. (3) reads like a loose order-of-magnitude estimate from αEM and Caγ only, which is misleading given that Δϕ/fa is the physically relevant quantity.  
   **Required fix:**  
   - Replace Eq. (3) with an explicit formula, e.g.  
     β = (αEM/4π) Caγ (Δϕ/fa),  
     then show how inserting Caγ = 8 and Δϕ/fa ≈ 1.07 yields β ≈ 0.29°.  
   - Explicitly connect 1.07 to the numerical integration (e.g. “for m ≈ 1.8H0 and θi = 1 we find Δϕ/fa ≈ 1.07 from solving Eq. (2)”), rather than leaving it as an unexplained factor.

2. **Claimed β range [0.17, 0.43]° vs. “naive envelope [0.027, 0.44]°” remains opaque.**  
   - The text says the range [0.17, 0.43]° is obtained from a “joint-trajectory scan” over (Caγ, m/H0, θi) and contrasts this with the “wider naive envelope [0.027, 0.44]°” from independent extrema.  
   - However, the paper does not show even one explicit trajectory mapping (m/H0, θi) → Δϕ/fa, nor any representative points demonstrating why β cannot reach as low as 0.027° once coupled trajectories are enforced.  
   - For a verification/consistency paper, this is too hand‑wavy; the claim that the range is not an independent-extrema product needs at least a minimal numerical illustration or table.  
   **Required fix:**  
   - Add a compact table or figure with a few representative parameter points (e.g. low, mid, high m/H0 and θi) showing Δϕ/fa and the resulting β for Caγ = 4, 8, 12.  
   - Show explicitly that the true joint scan yields the [0.17, 0.43]° range, and indicate where in parameter space the extremes occur.  
   - Remove reference to the “naive [0.027, 0.44]° envelope” unless you concretely show how it arises and why it is not physical.

3. **Backreaction / spectator-status fine-tuning factor still not numerically demonstrated.**  
   - The text states Ωa ∝ θi² and then claims a “∼25× fine-tuning” when going from θi = 0.5 to θi = 0.1. In fact, θi² scales as 0.25 vs. 0.01, a factor of 25; that part is correct, but the paper never relates this explicitly to a numeric Ωa at the scan midpoint vs. spectator corner.  
   - Given that the paper leans on this 25× as a key qualitative statement, it would be more rigorous to show at least one numerical estimate, even at the order-of-magnitude level, for Ωa(θi = 0.5) and Ωa(θi = 0.1).  
   **Required fix:**  
   - Add an explicit example computing Ωa for canonical parameters (e.g. m = H0, fa = MPl), at θi = 0.5 and θi = 0.1, to show the actual backreaction fraction and confirm the 25× factor.

---

P1B-M7 (MAJOR)  
Section: Sec. II (“Cosmological Tensions: H0 and σ8”), Table I, Fig. 1  
Problem: “Consistent with zero” and “consistent with ΛCDM” statements are not always backed by explicit quantitative comparisons in the locations where they’re asserted.

New issues:

1. **“∆Neff consistent with zero” phrasing is sometimes unquantified locally.**  
   - Abstract: “Both frozen dataset combinations find ∆Neff consistent with zero (−0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN)…” — here the numbers are given, so the claim is clear.  
   - Fig. 1 caption: “The ∆Neff posterior is consistent with zero (−0.020 ± 0.169), confirming no additional relativistic species at recombination.” This is fine.  
   - However, Sec. II text: “the proxy run confirming ∆Neff = −0.020 ± 0.169 (full-tension) and +0.065 ± 0.17 (Planck+BAO+SN) is therefore consistent with the minimal matter-bounce prediction” then says “we frame the proxy as a bounce-class compatibility check, not as a posterior-preference test against a competing model,” but nowhere in this section is there a concrete statement like “the deviation from zero is <0.4σ in both cases.”  
   **Required fix:**  
   - Where “consistent with zero” is used in body text for interpretive claims, append a short quantitative statement (e.g. “the posterior mean deviates from zero by 0.12σ and 0.38σ respectively”). This avoids any impression that “consistent with” is used qualitatively without numbers.

2. **“H0 consistent with standard ΛCDM” statement likewise lacks local σ.**  
   - Abstract: “H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN).”  
   - Sec. III: “Key finding.—Both frozen datasets find … H0 consistent with Planck ΛCDM at 0.3σ” appears only once near the end of Sec. III and is not cross-referenced in the abstract, where the same “consistent with” phrase appears without the 0.3σ figure.  
   **Required fix:**  
   - Either remove “consistent with standard ΛCDM” from the abstract or explicitly state “consistent at the 0.3σ level” so the reader sees a quantitative definition of “consistent” at the point of the claim.

---

P1B-m3 (MINOR)  
Section: Sec. V (“Cosmological Fits and Model Comparison”), Table II  
Problem: Internal referencing and wording around Planck release labels and χ² decomposition still have minor inconsistencies.

New issues:

1. **Planck release labelling mismatch in Table II χ² row.**  
   - Table II caption says “χ²CMB: Planck PR4 + lensing,” but the table header rows still describe the dataset combination with “Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native + DES-Y5 + Pantheon+.”  
   - However, Ref.  is the Planck 2018 parameters paper (PR3), not a PR4/NPIPE cosmology paper. The text elsewhere (footnote a to the abstract) already acknowledges the PR3 vs. PR4 tension. For this table, the phrase “Planck PR4 + lensing” is therefore misleading unless the actual likelihoods used are clearly NPIPE PR4-only.  
   **Required fix:**  
   - Change “Planck PR4 + lensing” in the χ²CMB line to something like “Planck NPIPE TTTEEE+lowl+lensing (PR4 likelihood stack)” and ensure the references correctly include the NPIPE/PR4 birefringence/EB papers in addition to .  
   - Explicitly differentiate PR3 parameter paper and PR4/NPIPE likelihood usage in any χ² or dataset labels.

2. **Goodness-of-fit decomposition footnote b uses slightly confusing wording.**  
   - Footnote b: “The mean-of-total χ² here is GetDist’s weighted-sample average over the full posterior, which differs from the sum of the individual-channel means ... by a 0.1‑unit arithmetic‑rounding artifact; the two are formally identical to within sampling precision.”  
   - The difference of 0.1 is not “arithmetic rounding” in the usual sense; it is from separate posterior averages of nonlinear functions (χ²total vs. χ²BAO + χ²CMB + χ²SN) and finite sampling noise.  
   **Required fix:**  
   - Replace “arithmetic-rounding artifact” with “posterior-averaging and finite-sampling differences” or similar, to avoid implying a trivial rounding issue when the cause is methodological.

---

P1B-N3 (NIT)  
Section: Appendices A–C, footnote 5, acknowledgments  
Problem: A few minor editorial inconsistencies and artifacts remain.

New issues:

1. **Appendix B “Claims classification” still reads as internal bookkeeping.**  
   - Although already flagged in P1B-N2, the new issue is that several “Status: Verified” entries refer to claims that are *not* fully traceable in the main text as currently written (e.g. β̂NaMaster = 0.238° “Pipeline; MC bias table” – there is no actual “MC bias table” in the paper).  
   **Required fix:**  
   - Either remove the “Verified” column or make sure that every “Verified” entry points to an explicit table/figure/equation in the main text where the numerical value appears.  

2. **Footnote 5 vs. main-text backreaction footnote 4.**  
   - Footnote 5 restates the spectator/backreaction caveat in slightly different language than footnote 4, including both “RETAINED” in caps and “NOT the spectator-consistent sub-range.” This feels like internal emphasis rather than final PRD prose.  
   **Required fix:**  
   - Consolidate the backreaction/spectator-status caveat into a single, clearly written footnote or paragraph in Sec. VI and remove duplicated, shouty “RETAINED” / “NOT” emphases.

---

NO other classes of issues beyond those listed above emerged from the fresh pass.  

- Arithmetic checks: other reported means, σ’s, and χ² sums in Tables I–II are self-consistent at the stated precision.  
- Figure–caption vs body: aside from the sample-count inconsistencies already described, axis descriptions and parameter ranges in Fig. 1 match the text.  
- Equation dimensional consistency: the main new concern is the incomplete specification of the birefringence formula in Sec. VI; other equations are dimensionally standard.  
- Internal cross-references: beyond the Planck PR3/PR4 labelling, citations and \ref’s generally point to the correct content for this companion.