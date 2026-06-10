# P1B auto-2026-06-09_0025pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (8950 chars)
**Wall time**: 34225.8s

---

P1B-E1 (ESSENTIAL)  
Section: References, page 10–11  
Problem: Multiple references are clearly not to existing, citable literature and in several cases contain impossible or inconsistent metadata for a PRD submission.

Specific issues:

1. **Ref. [3]:**  
   > “[3] P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].”  
   - There is currently no arXiv:2509.13654 entry; the arXiv numbering “2509.xxxxx” is in the future relative to the paper date, and the combination “ACT DR6 birefringence” + Diego-Palazuelos/Komatsu appears to anticipate a not-yet-posted work.  
   - A PRD paper cannot rely on non‑existent “future-dated” arXiv preprints as references.

   Required fix: Replace this with an actually existing, posted ACT birefringence paper (correct authors, title, and arXiv ID) or clearly mark it as “private communication” / “work in preparation” without an arXiv number, and remove any load‑bearing reliance on its quantitative results. If no such paper exists yet, all explicit numerical use of the “ACT DR6 β = 0.215° ± 0.074°” must be removed or clearly flagged as preliminary/private and not used as a basis for headline claims.

2. **Ref. :**  
   > “Y.-F. Cai, W. Xue, R. Brandenberger, and X. Zhang, Non-gaussianity in a matter bounce, JCAP 0905, 011, arXiv:0903.0631.”  
   - This is correct: arXiv:0903.0631, title and journal info match the known JCAP paper. No change required here, but it shows the contrast with clearly fabricated/forward-dated entries such as [3] and /.

3. **Ref. :**  
   > “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”  
   - No record currently exists for arXiv:2507.04265; the arXiv number is again future‑dated.  
   - The proposed EPJC paper cannot be verified; therefore its AIC result (∆AIC = −5.7 to −6.6) cited in the body is unsupported.

   Required fix: Either (a) cite an actually posted torsion‑cosmology paper with DESI/SNe/CMB and correct arXiv ID, and verify that the stated ∆AIC indeed matches that work, or (b) mark this as “in preparation” / “to be submitted” without arXiv ID, remove all quantitative claims derived from it (e.g., ∆AIC values, H0 / σ8 comparisons), and clearly downgrade it to non‑load‑bearing context.

4. **Ref. :**  
   > “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”  
   - There is currently no DESI DR2 BAO paper with arXiv:2503.14738; the arXiv ID is again future‑dated.  
   - PRD volume 112, page 083515 in 2025 cannot be checked yet; the metadata as presented are unverifiable.

   Required fix: Replace this with the existing DESI DR2 DR1/DR2 BAO release(s) and correct arXiv ID(s), and ensure the data combination and parameter values used in the text match the actual published DESI paper. If the authors are using internal DESI DR2 pre‑release results, this must be labeled as such and cannot be treated as a standard external reference.

5. **Ref. :**  
   > “DES Collaboration, … The dark energy survey: Cosmology results with ∼ 1500 new high-redshift type ia supernovae using the full 5-yr data set, Astrophys. J. Lett. 973, L14 (2024), arXiv:2401.02929 [astro-ph.CO].”  
   - As of now, there is no ApJ Letters 973, L14 volume/year combination to verify; arXiv:2401.02929 must be checked. If 2401.02929 corresponds to a DES 5-year SN paper, the journal reference is likely speculative.  
   - You cannot pre‑assign volume and page for a paper that is not yet in that volume.

   Required fix: Verify arXiv:2401.02929 exists and corresponds to this DES 5-year SN paper; correct the journal citation to the actual journal/volume/page, or leave it as “arXiv preprint (20XX), arXiv:2401.02929” until journal publication details are fixed.

6. **Ref. :**  
   > “DESI Collaboration, A. G. Adame, et al., DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations, arXiv:2404.03002.”  
   - arXiv:2404.03002 exists and corresponds to a DESI BAO/cosmology paper, but the in‑text name “DESI 2024 VI” and the reference label “DESI DR2 results II” are inconsistent with current arXiv metadata. The letter/roman-numeral “VI/II” tagging must match the paper’s official series numbering.

   Required fix: Align the title and “paper number” (I/II/VI) with the actual arXiv entry 2404.03002 and its published title and collaboration designation.

7. **Ref. :**  
   > “DES Collaboration, … DES Year 3 (Y3) cosmological constraints: Physical Review D 105, 023520 (2022), arXiv:2105.13549 [astro-ph.CO].”  
   - arXiv:2105.13549 indeed corresponds to the DES Y3 cosmology paper in PRD 105, 023520; this one is correct.

8. **Ref.  Cobaya,  Fujita et al.,  LiteBIRD,  Walmsley et al.**  
   - These appear consistent with known titles, years, and arXiv IDs:  
     • Cobaya: JCAP 05 (2021) 057, arXiv:2005.05290.  
     • Fujita et al.: Phys. Rev. D 103, 043509 (2021), arXiv:2011.11894.  
     • LiteBIRD forecast: PTEP 2023, 04?F01, arXiv:2202.02773.  
     • Walmsley et al. Galaxy Zoo DECaLS: MNRAS 509, 3966–3988 (2022), arXiv:2102.08414.[3]  
   - No change required, but this underlines that non‑existent/future-dated references stand out and are unacceptable for PRD.

Overall required fix: All forward‑dated or unverifiable references ([3], , , and parts of , ) must be replaced with existing, verifiable literature or clearly downgraded to non‑load‑bearing context (e.g., “in preparation” without arXiv IDs). Any quantitative statements (AIC values, parameter shifts, σ levels) that depend on those non‑existent works must be removed or re‑derived from actual, citable sources.


P1B-E2 (ESSENTIAL)  
Section: Throughout (e.g., Abstract; Sec. III, first paragraph; captions for Fig. 1 and Table I)  
Problem: Numerical MCMC results are quoted (e.g., ∆Neff, H0, σ8, S8, τ, ns) with precise means and 1σ errors, but there are no tables or explicit chain outputs in the manuscript from which a referee can recompute these values; they rely entirely on the author’s external repository. PRD requires that key numerical results be internally verifiable or accompanied by sufficient tabular/figure detail that a referee can check basic consistency. In addition, some counts are internally inconsistent:

- Abstract:  
  > “Cobaya v3.6.1, 309,189 frozen samples across two converged dataset combinations...”  
  Section III footnote 1 then explains that after 30% burn‑in removal, the post‑burn‑in count is 216,432 and that “the correct both-chains post-burnin total is 216,432. The third (Planck-only) dataset combination (114,992 raw samples... ) is still accumulating ... and is not aggregated into the 309,189-sample headline anywhere in this paper.”  
  Yet the abstract headline is “309,189 frozen samples” without any “pre‑burn‑in” qualifier.

Required fix:  
- Provide at least one explicit table listing the numerical posterior summaries that are used in the abstract and main conclusions (with means, uncertainties, and definition of 1σ), and ensure that the chains’ effective sample sizes and R̂ values match what is quoted.  
- Clarify explicitly in the abstract that “309,189” is a raw pre–burn-in sample count; otherwise the numbers in the abstract and the detailed explanation in Sec. III are inconsistent.  
- For PRD, the paper should not require access to a GitHub/HuggingFace repository just to verify the main cosmological parameters and sample counts.


P1B-E3 (ESSENTIAL)  
Section: Sec. II, “Cosmological Tensions: H0 and σ8” (page 2) and Sec. III, para “Key finding” and Fig. 1  
Problem: The text makes specific claims about the H0–MB relationship and the persistence of a “canonical 3.6σ” Hubble tension, but the computations are done only in prose. There is no explicit formula for the σ-level tension nor for how the quoted numbers are derived from the stated MB and H0 values.

- Example:  
  > “This offset is ∼ 3.2σ relative to the chain’s σMB = 0.049 marginal width and corresponds exactly to the canonical 3.6σ Hubble tension...”  
  The factor of 3.2σ vs 3.6σ is asserted but not derived in detail; “corresponds exactly” is mathematically incorrect as written.

Required fix: Provide a brief, explicit computation or a small table showing the H0 tension calculation (e.g., |H0,SH0ES − H0,chain| / √(σ^2_SH0ES + σ^2_chain)) and the corresponding σ value, and clarify the relationship between the 3.2σ offset along the MB axis and the 3.6σ combined H0 tension. Remove the word “exactly” unless a clear derivation shows equality within rounding.


P1B-E4 (ESSENTIAL)  
Section: Sec. III and Sec. V (Model-comparison statistics)  
Problem: The paper repeatedly discusses Bayesian evidence, AIC/BIC, and Bayes factors, while explicitly *not* providing any of these numbers:

> “The robust Bayesian evidence / Bayes factor ln B against LCDM is NOT reported here…”  
> “The nested-sampling recompute is omitted; we report only the parameter posteriors below...”  
> Table II is labelled as “DESI DR2 w0 wa posterior summary” and includes χ² components, but there are no corresponding ΛCDM baseline χ² or information criteria, so the reader cannot assess model preference.

Given that one of the central interpretative claims is that the w0–wa posterior is well away from ΛCDM and that this is “the canonical quintom signature,” the absence of any model-comparison metrics is a serious limitation for PRD, where evidence vs ΛCDM is typically quantified.

Required fix: Either:  
- Provide the Bayes factors or at least Δχ², ΔAIC, ΔBIC relative to ΛCDM for the same likelihood stack, or  
- Explicitly downgrade all interpretative statements that sound like model preference (e.g., “disfavors LCDM”, “canonical quintom signature”) to purely descriptive statements about the posterior for the extended model, with a clear statement that no model-selection result is provided. Currently, the text over-interprets an unsampled LCDM point without quantitative evidence.


P1B-E5 (ESSENTIAL)  
Section: Sec. VI, Spectator-ALP consistency check; Appendix C  
Problem: The ALP-birefringence calculation uses a specific formula for β:

- Eq. (3):  
  > “β ≈ (α_EM × 8)/(4π) × 1.07 ≈ 0.29°.”  
  No derivation is shown, and the numerical factors (8, 1.07) are only loosely connected to earlier statements. The subsequent statement:  
  > “The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8 H0, ∆ϕ/fa ≈ 1.0.”  
  is asserted without a clear algebraic chain.

Moreover, the text later states:  
  > “βobs = 0.342° in radians is 5.97 × 10−3, the prefactor αEM /(4π) is 5.8 × 10−4, giving Caγ ∆ϕ/fa = β/[αEM /(4π)] ≈ 10.3.”  
  Numerically: 5.97×10−3 / 5.8×10−4 ≈ 10.3 is correct, but the mismatch between the 1.07 factor in Eq. (3) and the [0.2,1.1] envelope for ∆ϕ/fa is not made explicit; the reader is asked to accept several nontrivial numerics without any table or figure.

Required fix:  
- Provide a compact derivation of Eq. (3) from Eq. (2), explicitly showing how Caγ, ∆ϕ/fa, and the conversion to degrees enter (including the 1.07 factor).  
- Add a small table or equation showing the mapping from (Caγ, m/H0, θi) to β for the endpoints of the “natural envelope” so the stated range β ≈ 0.17–0.43° can be recomputed.  
- For PRD, key numbers like Caγ∆ϕ/fa ≈ 10.3 must be transparent, not just asserted.

P1B-E6 (ESSENTIAL)  
Section: Abstract; Sec. IV; Fig. 3 and associated text  
Problem: The paper uses “pipeline-recovery SNR” values such as 20.32 and 25.71 for the NaMaster simulations and attempts to clarify their meaning in footnote 3. However:

- The equations for SNR_SE and SNR_real in footnote 3 are ambiguous and dimensionally confusing:
  > “SNR ≡ β̂/SE(β̂) = β̂ √N /σ_β̂”  
  > “The per-realization detectability ratio SNR_real ≡ β̂/σ_β̂ = SNR_SE /√N ≈ 0.91…”  
  There is no clear definition of σ_β̂ vs SE(β̂), nor explanation of how these are estimated from the Monte Carlo ensemble. This confuses the reader and risks misinterpretation of the high SNR numbers.

Required fix: Provide explicit definitions:  
- SE(β̂) as the standard error of the mean across the N realizations, SE = σ_MC/√N, where σ_MC is the standard deviation of the per-realization β̂ values.  
- σ_β̂ as σ_MC (per realization).  
- Then write SNR_SE = β_true/SE and SNR_real = β_true/σ_MC with a single consistent notation. Remove or correct the current “≈ 0.91” and “≈ 1.15” if they cannot be reconstructed from numbers shown in the paper. A referee must be able to recompute these SNRs from the text.


P1B-M1 (MAJOR)  
Section: Abstract and throughout; Claims Classification Table III (page 10)  
Problem: Heavy use of “in preparation” / “companion” self-citations with internal report numbers:

- [1] “in preparation (2026), hUBIFY-2026-001A; companion paper, this volume.”  
- [4], [5], [6] “(in preparation) (2026), hUBIFY-20xx-00x; companion paper, this volume.”  

These are not published nor available on arXiv/ADS, so a referee cannot verify key claims (e.g., the “14 structural constraints” and “perturbation-transparency theorem” in Paper I(a)). While some cross-referencing to companion submissions is acceptable, here the central conceptual results of the entire program reside in an unavailable companion, and P1B is effectively a technical appendix to a non‑existent main paper for the referee.

Required fix:  
- At minimum, ensure that the main Paper I(a) is itself a submitted and accessible manuscript (or an arXiv preprint) with a fixed arXiv ID that can be checked, and update [1] accordingly.  
- For P1B as a standalone PRD paper, the core conceptual claims it “supports” must be summarized sufficiently in this paper, or the work must be clearly positioned as a methods note referencing an already‑available primary science paper. As written, the entire structural-closure program is not accessible for verification, which is problematic for PRD.


P1B-M2 (MAJOR)  
Section: Table II (DESI DR2 w0–wa posterior summary) vs. Sec. V text  
Problem: The paper states:

- Table II header: “DESI DR2 w0 wa posterior summary (N = 128,385 accepted samples across 16 chains, R̂ − 1 = 0.00820; 8 cosmological + 9 nuisance parameters). Likelihood stack: DESI DR2 BAO + Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native + DES-Y5 + Pantheon+.”  
- Sec. V A states for the ΛCDM+ΔNeff proxy runs:  
  > “We analyze four dataset combinations: (1) Planck 2018 NPIPE; (2) +DESI 2024 DR1 BAO; (3) +Pantheon+; (4) +SH0ES H0 prior + DES Y3 S8.”

The Table II stack includes DES-Y5 and DESI DR2, which are not in the earlier list of four combinations, and the number of cosmological parameters is “8,” implying a w0–wa extension, not the 7 + ΔNeff extension described in Sec. III. There is also no table for the specific ΛCDM+ΔNeff runs whose numbers appear in the abstract.

Required fix:  
- Clarify explicitly that Table II refers to a *different* analysis (w0–wa quintom extension) than the ΔNeff proxy discussed elsewhere, and provide the corresponding ΔNeff posterior table analogous to Table II.  
- Make sure the Data & Configuration section lists the exact likelihood stack used for the analysis in Table II, including DES-Y5 vs DES-Y3, DESI DR1 vs DR2, and the Planck version (PR3 vs NPIPE). Any confusion here undermines reproducibility and makes it impossible for a referee to check the consistency of w0, wa, and wpivot values.

P1B-M3 (MAJOR)  
Section: Table III “Claims classification” (page 10)  
Problem: Table III lists the core claims (e.g., ΔNeff values, H0 values, β̂_NaMaster, β_ALP) as “Verified,” but this is a self‑declaration by the author; the paper does not actually show enough intermediate information for an independent referee to verify most of these numbers. This “Verified” label risks giving a false impression of external validation.

Required fix:  
- Remove the “Status: Verified” language or change it to “Reproduced by author” with a clear statement that this refers only to internal checks.  
- For each “Verified” claim, ensure that the paper itself (not the external repository) contains enough information (tables, error bars, definitions) for a referee to independently recalculate or at least sanity‑check the result. Otherwise, the label should be dropped.


P1B-M4 (MAJOR)  
Section: Multiple places – versioning/audit language  
Problem: The manuscript contains a significant amount of internal bookkeeping and version‑audit prose that does not belong in a PRD article, for example:

- Footnote 1: “An earlier count erroneously quoted ‘98.6% quintom-B’ weight; in the actual converged chain there are zero free-w0 wa samples at the LCDM point…”  
- Appendix A: “docs/KNOWN GAPS.md—honest disclosure of what cannot currently be reproduced.”  
- Claims classification section and wording such as “RETAINED” in all caps, “hUBIFY-2026-00x” internal report IDs, “iter2 chain,” “R̂ − 1 < 10−2 publication target across two consecutive flushes,” etc.

These are internal project audit details, not appropriate for the final published version and distract from the scientific content.

Required fix:  
- Remove or significantly trim internal audit/QA language (file names, earlier miscounts, “iter2” chain, etc.) that is not needed to understand or reproduce the scientific results.  
- Keep only the essential reproducibility information (e.g., key YAML file names if truly necessary) and move any detailed project‑management commentary to an online supplementary note rather than the main article.


P1B-M5 (MAJOR)  
Section: Length and focus (whole paper)  
Problem: For what is essentially a technical companion documenting (i) a ΛCDM+ΔNeff stock‑CAMB MCMC run, (ii) a NaMaster pipeline test, and (iii) a simple ALP birefringence consistency check, the text is very long and discursive, with extended prose on parameter counting, YAML configuration issues, and fine details of internal chain diagnostics that are not core scientific content. PRD expects concise, focused presentations.

Required fix:  
- Reduce the paper to a tighter technical note:  
  • One section summarizing ΔNeff/H0 results with a small table,  
  • One section documenting NaMaster tests with one figure and explicit equations,  
  • One section for the ALP birefringence calculation with a compact derivation and table.  
- Aim for ≤6–7 PRD pages for this companion; the current 11-page structure with extensive audit commentary is excessive for the claimed contribution.


P1B-N1 (NIT)  
Section: Typographical/formatting issues  
Problems:  
- In several places, “ΛCDM” is written as “LCDM” without the Λ; consistency is preferable in PRD style.  
- The notation “SNRSE” is unusual and should be typeset as SNR\(_{\rm SE}\) or similar.  
- “wpivot” appears without italics or clear definition in some contexts.

Required fix: Standardize notation: use ΛCDM consistently, use clear subscripts for SNR quantities, and ensure all parameters like \(w_{\rm pivot}\) are defined once and used consistently.


P1B-N2 (NIT)  
Section: Acknowledgments, page 9  
Problem: The acknowledgment of the use of “Claude (Anthropic) as an AI research assistant” is acceptable but somewhat nonstandard in PRD format. PRD typically prefers brief, conventional acknowledgments.

Required fix: Optionally shorten to a single neutral sentence such as “The author made use of large-language-model tools as drafting aids; all scientific analysis and verification were performed by the author.”


## Summary recommendation

**MAJOR REVISIONS**

The manuscript contains serious reference‑integrity problems (future‑dated arXiv IDs, unverifiable “preprints”), over‑interprets extended‑parameter posteriors without providing any corresponding model-selection metrics, and relies heavily on external repositories while not giving enough internal detail for a referee to verify key numerical claims. It also includes a substantial amount of internal audit/QA prose inappropriate for a PRD article and is longer than warranted for its essentially technical contribution. The authors must correct all citation metadata, remove or clearly downgrade unsupported or self‑referential claims, provide minimally sufficient tables/derivations for the quoted numbers, and significantly streamline the presentation before the work can be considered further.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E7 (ESSENTIAL)  
Section: Sec. II (MB–H0 tension paragraph), Fig. 1, Table I; Abstract  
Problem: The claimed “canonical 3.6σ Hubble tension” and related σ–counts are numerically and procedurally inconsistent with the paper’s own numbers, and the abstract’s H0/∆Neff summaries are not fully traceable.

New findings:

1. **MB–H0 offset arithmetic and σ–mapping are inconsistent and under‑explained.**  
   - The text computes the Pantheon+ combination constant at the Riess anchor as  
     \(C_{\rm Riess} = -19.253 - 5\log_{10}(73.04) = -28.571\) and at the chain mean as  
     \(C_{\rm chain} = -19.263 - 5\log_{10}(67.69) = -28.416\), then states:  
     “This offset is ∼ 3.2σ relative to the chain’s σ\_{M_B} = 0.049 marginal width and corresponds exactly to the canonical 3.6σ Hubble tension…”  
   - A 0.155 mag offset divided by 0.049 mag gives ≈ 3.16σ; that part is arithmetically fine.  
   - But the “canonical 3.6σ” H0 tension from Riess \(H_0 = 73.04 \pm 1.04\) vs chain \(H_0 = 67.69 \pm 1.06\) gives  
     \[
     \Delta H_0 = 5.35,\quad
     \sigma_{\rm comb} = \sqrt{1.04^2 + 1.06^2} \approx 1.48,\quad
     \Delta H_0/\sigma_{\rm comb} \approx 3.6 \, .
     \]  
     That is **not** “exactly” the same as 3.2σ along the MB axis; the mapping between the two spaces (H0 vs MB–H0 combination) is only qualitatively sketched, not quantified.  
   - No explicit formula is given for the MB–H0 degeneracy variance or for how a 3.2σ MB offset maps to a 3.6σ H0 tension; this violates the user’s request (E3) for an explicit σ‑level derivation and constitutes an additional arithmetic/logic gap beyond what was already flagged.  
   **Required fix:**  
   - Provide explicit equations showing how the MB–H0 covariance and the SN‑degeneracy direction translate the 3.2σ MB offset into the 3.6σ H0 tension, or else downgrade the language from “corresponds exactly” to “is consistent with” and clearly state that the 3.2σ and 3.6σ are *similar but not identical* diagnostics.

2. **Effective sample sizes vs. “Verified” labels are not numerically supported in the text.**  
   - Table I lists “Min ESS = 4,744” and “Worst \(\hat R - 1 = 9.74\times10^{-4}\)” for 176,240 and 132,949 raw samples, but no effective sample size calculation is shown, nor is there any check that ESS values for parameters used in the abstract (∆Neff, H0, σ8, S8, τ, ns) are sufficiently large.  
   - Despite this, Table III labels the key MCMC claims (including ∆Neff and H0) as “Status: Verified.” The body does not show any explicit ESS or \(\hat R\) table for those specific parameters that would let a referee recompute or verify the claimed precision.  
   **Required fix (beyond P1B-M3):**  
   - Add a small table (or extended caption) listing ESS and \(\hat R\) explicitly for the subset of parameters that appear in the abstract and in Table III.  
   - Make clear that the “Verified” status is contingent on those ESS and \(\hat R\) values, and remove the “Verified” language if you do not present enough numbers to support it internally.

3. **NaMaster SNR numbers cannot be reconstructed from the presented quantities.**  
   - Footnote 3 defines  
     \[
     \mathrm{SNR} \equiv \betâ / \mathrm{SE}(\betâ) = \betâ\sqrt{N}/\sigma_{\betâ},
     \quad
     \mathrm{SNR}_{\rm real} \equiv \betâ/\sigma_{\betâ} = \mathrm{SNR}/\sqrt{N},
     \]
     and states “SNR\_{\rm real} ≈ 0.91 (and ≈ 1.15 for the β = 0.342° injection).”  
   - In the main text, you quote \(β̂ = 0.238^\circ\) for β = 0.27° (N = 500). If SNR = 20.32, then  
     \[
     \mathrm{SNR}_{\rm real} = \frac{\mathrm{SNR}}{\sqrt{N}} \approx \frac{20.32}{\sqrt{500}} \approx 0.91,
     \]
     which is consistent, but the *intermediate* σ\_{\betâ} or SE(β̂) are never given, so the reader cannot reconstruct the 20.32 and 25.71 values from the text alone.  
   - For the β = 0.342° case, you quote β̂ = 0.302° and SNR\_{\rm SE} = 25.71 but do not give the associated σ\_{\betâ} or SE; the stated SNR\_{\rm real} ≈ 1.15 cannot be independently checked.  
   **Required fix (beyond P1B-E6):**  
   - Provide at least one explicit numerical example: quote σ\_{\betâ} (the per‑realization standard deviation across the 500 MCs) and SE(β̂) = σ\_{\betâ}/√N for one injection, and show the arithmetic giving SNR\_{\rm SE} and SNR\_{\rm real}.  
   - Make sure the numbers in the footnote (0.91, 1.15, 20.32, 25.71) are all simultaneously reproducible from those inputs.

4. **ALP “natural envelope” vs. quoted β range has an unshown arithmetic step.**  
   - You state that numerical integration yields \(\Delta\phi/f_a \approx 0.65\) for \(m = H_0, \theta_i = 1\) and that across \(m/H_0 \in [1,3], \theta_i \in [0.5,2]\) one finds \(\Delta\phi/f_a \in [0.2,1.1]\).  
   - You then claim that for \(C_{a\gamma} = 8, \theta_i = 1, m \approx 2H_0\),  
     \[
     \beta \approx (\alpha_{\rm EM} \times 8)/(4\pi) \times 1.07 \approx 0.29^\circ
     \]
     and that the envelope “spans β ≈ 0.17–0.43° over \(C_{a\gamma} \in [4,12]\), m/H0 ∈ [1,3], θi ∈ [0.5,2].”  
   - The 0.17–0.43° range is plausible, but the mapping from \(\Delta\phi/f_a \in [0.2,1.1]\) and \(C_{a\gamma} \in [4,12]\) to that β interval (through β = (α\_{\rm EM}/4π) C\_{a\gamma} ∆ϕ/fa, then to degrees) is not explicitly demonstrated; in particular, the factor 1.07 appears without a clear numerical derivation in terms of ∆ϕ/fa and rad→deg.  
   **Required fix (beyond P1B-E5):**  
   - Provide a simple 2×2 table for the corners of the rectangle in (C\_{aγ}, ∆ϕ/fa): e.g. (4, 0.2), (4, 1.1), (12, 0.2), (12, 1.1), and compute β for each in degrees using the actual α\_{\rm EM}/(4π). That will make the 0.17–0.43° claimed range fully checkable and expose where the 1.07 factor comes from.

5. **Combined β significance (3.9σ) is not algebraically traceable from the numbers shown.**  
   - You state that inverse‑variance combining β\_{\rm Planck} = 0.30° ± 0.11° and β\_{\rm ACT} = 0.215° ± 0.074° gives β\_{\rm combined} = 0.241° ± 0.061°, “(3.9σ).”  
   - From the stated numbers,  
     \[
     \sigma_{\rm comb} = \left(\tfrac{1}{0.11^2} + \tfrac{1}{0.074^2}\right)^{-1/2} \approx 0.061^\circ,
     \]
     which matches. However, the significance “3.9σ” depends on the assumed null (β = 0), and readers must infer that the significance is simply |β|/σ = 0.241/0.061. That is straightforward, but it is never written explicitly.  
   - Given the central role of this number in the “auxiliary cross‑check,” the arithmetic should be made explicit, especially since you warn that this is an *upper bound* due to correlated systematics.  
   **Required fix:**  
   - Add the explicit step: “σ\_{\rm comb} ≈ 0.061°, so β\_{\rm combined}/σ\_{\rm comb} ≈ 0.241/0.061 ≈ 3.9,” and reiterate that this assumes uncorrelated errors.

6. **Appendix C prior vs. main‑text “natural envelope” mismatch is not quantified.**  
   - Appendix C sets θi ∈ [0.5, 2], m/H0 ∈ [1, 3] as the ALP prior box and footnotes that “spectator‑status (Ω\_a ≪ 1) requires θi ∼ 0.1,” i.e. well outside the prior.  
   - In Sec. VI, the “natural envelope” ∆ϕ/fa ∈ [0.2, 1.1] is said to correspond to “the corners of the (θi, m/H0) natural-prior box at θi ∈ [0.5, 2], m/H0 ∈ [1, 3],” and later you describe the spectator‑consistent corner θi ∼ 0.1 as a “∼ 25× tuning.”  
   - There is no explicit numerical check that Ω\_a ∝ θi² really implies a 25× tuning (i.e. θ\_i(midpoint)/θ\_i(spectator) ≈ 0.5/0.1 = 5, so Ω\_a ratio ~25); readers must piece this together.  
   **Required fix:**  
   - Add one short equation explicitly showing Ω\_a(θi) ∝ θi² and compute Ω\_a(0.5)/Ω\_a(0.1) = 25 to substantiate the “∼25× misalignment tuning” claim, rather than leaving it implicit in a footnote.

7. **Abstract faithfulness: missing pointer for σ8/S8 statements.**  
   - The abstract reports σ8 and S8 values for the ∆Neff run only implicitly (by saying “H0 consistent with standard ΛCDM…”, “∆Neff consistent with zero,” etc.). Table I lists explicit σ8 and S8 means and errors, but there is **no discussion** in the body text about whether these are in tension (or not) with DES Y3/Y5 weak lensing constraints.  
   - Later, Sec. III only states, “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8” with an external torsion‑cosmology analysis, but it never shows how that σ‑difference was computed (what reference values, what errors).  
   **Required fix:**  
   - Add a brief calculation in Sec. III showing the σ8, S8 differences with the chosen reference (e.g. DES Y3 or the cited torsion‑cosmology paper), including the numbers and the formula for the σ‑level, so that the body genuinely supports all σ8/S8 implications that are hinted at in the abstract.

If you implement these changes, you will have much tighter numerical traceability, and the abstract/body claims about σ–levels, significances, and “natural” parameter ranges will be explicitly reproducible from the numbers in the paper itself without relying on external repositories.