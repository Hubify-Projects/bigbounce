# P4 auto-2026-06-06_0004pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13626 chars)
**Wall time**: 69.4s

---

Below is a citation-forensics audit of the **bibliography and in-text load-bearing claims that can be checked from the provided paper text plus the supplied web results**. I cannot truthfully claim to have verified every reference against arXiv/ADS in real time because only one search batch was provided here, but I can still flag clear mismatches, internal inconsistencies, and unsupported or incorrectly attributed claims.

- **P4-E1 — References  / pp. 9–10**  
  **Problem:** The citation text is fused and incomplete:  
  > “J. Hou, Z. Slepian, and R. N. Cahn, ‘Measurement of parity-odd modes in the large-scale 4-point correla- tion function of SDSS BOSS DR12 CMASS and LOWZ galaxies,’ Mon. Not. R. Astron. Soc. 522, 5701 (2023), arXiv:2206.03625.”  
  The supplied web results show this is indeed the MNRAS 522, 5701 paper, but the paper title in the bibliography is line-broken awkwardly and the citation omits the DOI that is present in the journal record.  
  **Required fix:** Normalize the entry formatting; ensure the full title is reproduced exactly and add the DOI if journal style requires it.

- **P4-E2 — References  / p. 10**  
  **Problem:** The bibliography entry  
  > “R. N. Cahn, Z. Slepian, and J. Hou, ‘A test for cosmological parity violation using the 3D distribution of galaxies,’ Phys. Rev. Lett. 130, 201002 (2023), arXiv:2110.12004.”  
  is plausibly correct in substance, but it is not verifiable from the provided search batch. More importantly, the in-text discussion later uses this literature to support a claim about **“parity-odd signal lives in the ℓ = 0 monopole and even-ℓ multipoles”**; that is not a citation-forensics issue by itself, but the paper does not adequately distinguish this from the cited 3D parity-odd observable.  
  **Required fix:** Verify the citation against arXiv/ADS and explicitly state what aspect of the cited work is being used.

- **P4-E3 — References  / p. 10**  
  **Problem:**  
  > “DESI Collaboration, A. Aghamousa, J. Aguilar et al., ‘The DESI Experiment Part I: Science, Targeting, and Survey Design,’ arXiv:1611.00036 (2016).”  
  This is a **fused metadata** style entry: the DESI Collaboration is not properly formatted as an author list, and the citation is missing a journal publication status/venue.  
  **Required fix:** Replace with the canonical bibliographic form for the DESI design paper, including correct first authorship and venue information if available in the paper’s reference style.

- **P4-E4 — References – / p. 10**  
  **Problem:** These entries are incomplete or malformed:  
  -  gives only “A. Zonca, L. Singer, D. Lenz et al., J. Open Source Softw. 4, 1298 (2019).” with no title.  
  -  gives only “C. R. Harris, K. J. Millman, S. J. van der Walt et al., Nature 585, 357 (2020).” with no title.  
  -  gives no title at all, only conference proceedings.  
  -  gives no paper title, only proceedings.  
  -  is a software repository citation, but the manuscript mixes this with journal-style references.  
  **Required fix:** Use a consistent reference format; include titles for all software/software-proceedings citations or convert them to a consistent software-citation style.

- **P4-M1 — Abstract / p. 1**  
  **Problem:** The paper states:  
  > “The post-MASTER canonical-mask direct-MC residual is +3.64σ … (empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent; 500-MC binomial per-pixel-shuffle null)”  
  This is **mathematically inconsistent** as written. A two-sided Gaussian-equivalent of \(p=0.030\) is about \(2.17σ\), not \(1.9σ\); a one-sided equivalent is about \(1.88σ\), but the paper does not specify one-sidedness at that sentence.  
  **Required fix:** State clearly whether the p-value is one-sided or two-sided and recompute the Gaussian-equivalent accordingly.

- **P4-M2 — Abstract / p. 1 vs Table I / p. 4**  
  **Problem:** The abstract says  
  > “the canonical-mask direct-MC residual is +3.64σ … (500-MC binomial per-pixel-shuffle null)”  
  while Table I labels the same estimator simply as “pp-shuffle” and Table IV separately reports  
  > “Pre-MASTER pseudo-Cℓ (canonical mask) ... +1.68”  
  for a different null.  
  The manuscript repeatedly juxtaposes different null procedures without always restating non-comparability at every comparison point, despite its own warning.  
  **Required fix:** Add explicit “not directly comparable” qualification at each side-by-side σ comparison involving different nulls.

- **P4-M3 — Abstract / p. 1**  
  **Problem:**  
  > “The headline scientific result is a null ℓ = 1 chirality-dipole observable on the analysis subsample mask: the MASTER-deconvolved single-mode pseudo-C1 on the strict-superset subsample mask (n = 5,547,858, fsky = 0.659) yields −0.122σ (500-MC label-shuffle null)”  
  This is fine internally, but the phrase “strict-superset subsample mask” is unexplained and appears to be a bespoke analysis mask not defined mathematically in the main text.  
  **Required fix:** Define the mask construction precisely and give the relation to the canonical mask.

- **P4-M4 — Abstract / p. 1**  
  **Problem:**  
  > “The +3.64σ canonical-mask residual is consistent with monopole leakage through survey geometry … and is not interpreted as a cosmological signal.”  
  Yet later the paper still phrases this residual as a “non-headline” result in a way that risks overstating physical content.  
  **Required fix:** Keep interpretation language consistent throughout: systematic artifact, not signal.

- **P4-M5 — Abstract / p. 1**  
  **Problem:**  
  > “a future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null.”  
  The falsification threshold is presented as a hard criterion, but the paper’s own sensitivity discussion later gives a different “true-underlying threshold” of about 1.88% after dilution.  
  **Required fix:** Resolve whether the falsification threshold is on observed amplitude, intrinsic amplitude, or catalog-measured amplitude.

- **P4-M6 — p. 2, Introduction**  
  **Problem:**  
  > “Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries on DESI Legacy samples (‘nearly 1.3 × 10^6 spiral galaxies’ per the published abstract).”  
  This is not a direct quote from the cited papers as written here; the manuscript merges multiple claims and rounds the sample size.  
  **Required fix:** Quote exact numbers from the cited abstracts or tables, or remove the parenthetical if it cannot be traced verbatim.

- **P4-M7 — p. 2, Introduction**  
  **Problem:**  
  > “Jia et al. [7] introduced CE-ResNet … yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.”  
  The citation text in [7] says the paper is “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network.” The manuscript’s “cw/ccw = 0.998” is not obviously traceable to the citation text provided here.  
  **Required fix:** Verify this statistic against the cited paper’s abstract or tables and specify the sample and metric definition.

- **P4-M8 — p. 2, Data / Training Labels**  
  **Problem:**  
  > “The independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy 69.91% (Cohen’s κ = 0.40).”  
  This is a critical quantitative claim, but the paper gives no contingency table, no baseline, and no derivation of κ.  
  **Required fix:** Provide the confusion matrix or a derivation showing how 69.91% and κ = 0.40 were computed.

- **P4-M9 — p. 3, Methods III.C / equation (2)**  
  **Problem:** The equation typesetting is visibly corrupted:  
  > \(P^{eq}_{CW}= \frac12 P^{orig}_{CW} + P^{flip}_{CCW}\), etc.  
  The displayed line breaks and parentheses are malformed, and the equation as rendered is ambiguous.  
  **Required fix:** Reformat the equation cleanly and verify that the averaging weights are exactly \(1/2\).

- **P4-M10 — p. 3, Methods III.D**  
  **Problem:**  
  > “All three tiers share 8,474,531 rows in Apache Parquet format.”  
  This number is one less than the final catalog count in the abstract’s parent sample discussion, but the manuscript never explains the one-row discrepancy except by saying 157 of 8,474,688 failed quality checks. The arithmetic is consistent only if 8,474,688 − 157 = 8,474,531, which is true; however, this should be explicit because the same section also states the full dataset contains 8,474,688 images.  
  **Required fix:** Add the explicit subtraction in the text or a table footnote.

- **P4-M11 — p. 4, Table I**  
  **Problem:** Table I’s header and footnote are internally confusing:  
  > “Nmap weighted = p∈mask Wp where Wp = Nall(p) is the total classified-galaxy count in pixel p (CW+CCW+NS), used as a survey-depth weight…”  
  This is malformed notation. The summation index is missing proper sigma notation, and the description says “Nmap weighted exceeds Ncatalog spiral because Wp includes non-spiral galaxies,” but \(W_p\) is a pixel weight, not a galaxy count.  
  **Required fix:** Rewrite the definition using clear sum notation and state whether \(W_p\) is normalized per pixel or raw count.

- **P4-M12 — p. 4, Table II**  
  **Problem:** The “Dev. (σ)” entries are numerically inconsistent with standard binomial deviations if interpreted naively. For example, with \(N=3{,}201{,}160\) and \(f_{CW}=0.5079\), the stated +28.8σ is plausible, but the table does not show the exact \(σ\) used beyond a generic binomial formula.  
  **Required fix:** Provide the full calculation for each row or a worked example in the caption.

- **P4-M13 — p. 4, Results IV.B**  
  **Problem:**  
  > “The Catalog C residual (9.5σ from 0.5000, Table II) is spatially uniform across 7 equatorial coordinate slabs and does not produce a dipole.”  
  This is a strong inference from a slab test, but the manuscript gives no statistical test of uniformity across slabs.  
  **Required fix:** Add the slab-by-slab values and a formal homogeneity test.

- **P4-M14 — p. 4, Results IV.C and Table III**  
  **Problem:** The paper calls the \( \ell=1 \) estimate the “primary isotropy-breaking dipole observable,” but Table III mixes \(C_\ell\) values and “significance” values from different procedures.  
  **Required fix:** Separate the raw spectrum from the null-significance calculation and label the null model for each row.

- **P4-M15 — p. 4, Table III**  
  **Problem:**  
  > “ℓeff = 4 (ℓ ∈ [2, 6]) 3.210 … +6.097 Mask-coupled monopole leakage”  
  The table shows a positive “significance” for a negative physical quantity in some rows later, but the sign convention is not explained.  
  **Required fix:** Define the sign convention for \(\sigma\) in the table caption and keep it consistent.

- **P4-M16 — p. 4, Results IV.D**  
  **Problem:**  
  > “The monopole-only null reproduces 99.3% of the observed pre-MASTER pseudo-Cℓ(ℓ=1) power.”  
  The manuscript does not show the arithmetic connecting 99.3% to the listed values in Table IV. If the data are \(1.696\times10^{-2}\) and null mean \((1.685\pm0.007)\times10^{-2}\), the ratio is about 99.4%, not exactly 99.3%.  
  **Required fix:** Recompute the percentage from the displayed numbers and state whether the reported figure is rounded or estimated differently.

- **P4-M17 — p. 5, Section IV.E**  
  **Problem:**  
  > “The +3.3σ signal in the 1.87M-galaxy [0.5, 0.6) confidence bin does not survive … cutting to peq > 0.6 gives −0.03σ.”  
  These two numbers are not shown anywhere in a supporting table in the main paper.  
  **Required fix:** Include the bin counts and null values in the appendix table or main text.

- **P4-M18 — p. 5, Section V.A**  
  **Problem:**  
  > “Shamir’s claimed ∼ 3% signal by a factor of ∼ 6–12 under the present pipeline”  
  This is a loose claim that depends on whether one compares 3% to 0.43%, 0.75%, or 0.26%. The factor is not stable.  
  **Required fix:** Specify exactly which amplitude is being compared and avoid range inflation.

- **P4-M19 — p. 5, Section V.B**  
  **Problem:**  
  > “CE-ResNet [7] achieves cw/ccw = 0.998 with architectural equivariance on 1.95 million galaxies.”  
  This is presented as if it were a directly comparable statistic to the present paper’s \(0.4974\), but the definitions are not aligned: one is a class ratio, the other a CW fraction after TTA.  
  **Required fix:** Define identical metrics or explicitly state why they are not comparable.

- **P4-M20 — p. 6, Discussion VI.A**  
  **Problem:**  
  > “The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).”  
  The derivation is not shown, and \(f_{sky}=0.46\) conflicts with earlier masks of 0.659 and 0.49005.  
  **Required fix:** Show the full Fisher calculation and identify which mask fraction is used.

- **P4-M21 — p. 6, Discussion VI.A**  
  **Problem:**  
  > “g = 2a − 1 ≈ 0.398 for a = 0.6991”  
  This arithmetic is incorrect if \(a=0.6991\): \(2a-1 = 0.3982\), yes, but the implied “true-underlying threshold ∼ 1.88%” is not derived transparently from the preceding 0.75% sensitivity floor.  
  **Required fix:** Show the exact mapping from observed threshold to intrinsic threshold.

- **P4-M22 — p. 6, Discussion VI.B**  
  **Problem:**  
  > “The parity-odd signal lives in the ℓ = 0 monopole and even-ℓ multipoles.”  
  This statement is physically suspect as written and appears to conflate the paper’s observable with different parity-odd constructions in the cited literature.  
  **Required fix:** Rewrite this sentence with a precise theoretical basis and a citation that directly supports it.

- **P4-M23 — p. 7, Appendix A**  
  **Problem:**  
  > “nmt.NmtBin.from lmax linear(lmax=191, nlb=1)”  
  This is malformed code-like text; it is not valid NaMaster syntax as written.  
  **Required fix:** Replace with proper function syntax or pseudocode in a code block.

- **P4-M24 — p. 7, Appendix B**  
  **Problem:**  
  > “Headlines 93.7% three-class accuracy … post-hoc eval without augmentation yields 94.9%.”  
  The manuscript does not clarify what dataset split, class balance, or metric averaging is used.  
  **Required fix:** State whether the accuracy is top-1, macro, micro, or weighted and give the confusion matrix.

- **P4-M25 — p. 8, Appendix C**  
  **Problem:**  
  > “The +3.3σ in the 1.87M-galaxy [0.5, 0.6) bin does not survive … peq > 0.6 gives −0.03σ.”  
  The appendix repeats the unsupported headline numbers without tabulation.  
  **Required fix:** Provide the full table with bin edges, counts, and null definitions.

- **P4-M26 — p. 8, Appendix C**  
  **Problem:**  
  > “The direct-MC look-elsewhere test (N = 10,000 random-label shuffles) gives pLEE ≤ 10−4”  
  But the same paragraph says Bonferroni/BH across ∼ 650 directions reduces the result to < 1σ. These two statements are not inherently contradictory, but they are juxtaposed without explicit warning that they are different null procedures.  
  **Required fix:** State that the p-values are not directly comparable and identify which is primary.

- **P4-M27 — p. 8, Appendix D**  
  **Problem:**  
  > “Block-bootstrap at NSIDE = 8 (Nboot = 1000) inflates σ(Adipole) by 14.7×, reducing z to ≈ −18.1”  
  This is numerically and conceptually problematic: inflating \(\sigma\) by 14.7× should reduce \(|z|\) substantially, but the manuscript does not show the original z-value or how \(-18.1\) was computed.  
  **Required fix:** Give the before/after values and derive the post-bootstrap z-score explicitly.

- **P4-M28 — p. 8, Appendix D**  
  **Problem:**  
  > “WLS posterior (far-tail)” and “zboot ≈ −18”  
  These are statistical claims without sufficient explanation of the likelihood model or the meaning of “far-tail.”  
  **Required fix:** Define the WLS objective, prior assumptions, and posterior interpretation.

- **P4-M29 — p. 9, Appendix E**  
  **Problem:**  
  > “65.7% of visually identified edge-on systems (b/a < 0.3) receive CW or CCW classifications rather than not spiral.”  
  This is a meaningful contamination statistic but the paper does not show the sample size or denominator.  
  **Required fix:** Provide the raw counts and uncertainty.

- **P4-M30 — p. 9, Appendix E**  
  **Problem:**  
  > “the equivariant averaging … for any galaxy whose mirror image is morphologically indistinguishable from the original (as for edge-on disks) the ensemble-mean CW and CCW probabilities are flip-symmetric.”  
  This is an inference, not a demonstrated theorem in the paper.  
  **Required fix:** Mark it as a model assumption or support it with a proof/validation.

- **P4-M31 — p. 9, Appendix E**  
  **Problem:**  
  > “The Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict)”  
  These values are not tabulated in the paper text provided.  
  **Required fix:** Add a supporting table and define “monopole-preserving dipole.”

- **P4-M32 — p. 9, Appendix E**  
  **Problem:**  
  > “The spiral fraction is uniform across the DESI Legacy footprint at the ≲ 2% level across 7 equatorial coordinate slabs”  
  As with earlier slab claims, no statistical test is shown.  
  **Required fix:** Provide slab values and the test statistic.

- **P4-M33 — p. 9, Data Availability**  
  **Problem:**  
  > “https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog”  
  The rendered text contains broken URL tokens and line-break artifacts.  
  **Required fix:** Clean the data availability formatting. Even if URLs are omitted in the journal version, the manuscript should not contain broken hyphenation in the body.

- **P4-M34 — p. 9, Acknowledgments**  
  **Problem:**  
  > “Software: Astropy , HEALPix/healpy [34, 35], NumPy , pandas , PyTorch , timm , NaMaster/pymaster.”  
  The software citations are incomplete or inconsistent with journal citation norms, and NaMaster/pymaster is uncited here despite being central to the analysis.  
  **Required fix:** Add proper software citations and ensure the core analysis package is cited consistently.

- **P4-M35 — p. 1–9, internal consistency / load-bearing scalars**  
  **Problem:** The manuscript repeatedly alternates between **0.26%**, **0.4%**, **0.79%**, **0.75%**, **1.88%**, **2.05%**, **3.2 M**, and **3,201,160** as if these were directly interchangeable measures of the same phenomenon. They are not.  
  **Required fix:** Introduce a single notation table defining raw CW excess, calibrated excess, equivariant CW fraction shift, and intrinsic underlying threshold; then keep each quantity separate everywhere.

- **P4-M36 — p. 1–9, unsupported novelty claims**  
  **Problem:**  
  > “largest galaxy chirality catalog to date,” “bias-hardening audit suite,” “quantifiable monopole-mask leakage channel”  
  The first claim may be true, but it is not demonstrated against the literature cited here; the second and third are author-coined descriptions rather than established results.  
  **Required fix:** Either document the comparison set for “largest” or remove the superlative.

- **P4-M37 — p. 1–9, duplicate/overlapping presentation**  
  **Problem:** Several sections repeat the same result sets in different words: the headline null dipole, canonical-mask residual, and leakage interpretation are restated across abstract, results, discussion, and conclusions without adding new evidence.  
  **Required fix:** Compress redundant prose and keep each result stated once with its supporting table/figure.

- **P4-M38 — p. 9–10, reference hygiene**  
  **Problem:** The bibliography includes older Shamir references [1], [3], [4] and a 2022 PASJ item [2], but the in-text chronology and reference numbering are awkward, and some claims about Shamir’s sample sizes are paraphrased rather than directly traceable to the cited abstracts.  
  **Required fix:** Audit every Shamir-related numerical claim against the cited paper abstracts/tables and correct any mismatched sample sizes or amplitudes.

## Summary recommendation
**REJECT**

The manuscript contains multiple load-bearing statistical claims that are either internally inconsistent, insufficiently derived, or presented without the necessary qualification when switching null models. The bibliography also has malformed and incomplete entries, and several important numerical statements cannot be traced cleanly to the cited papers’ abstracts/tables from the information provided here. For a Physical Review D submission, the paper needs a major reconstruction of its statistical reporting, citation hygiene, and result bookkeeping before it could be considered for acceptance.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-M39 — Arithmetic / σ from binomial error (Table II, Sect. IV.B)  
**Problem:** The “Dev. (σ)” entries in Table II do not match the quoted binomial uncertainties. For Catalog C, the table lists \(f_{CW}=0.4974\pm0.000279\) and Dev. \(=9.5σ\). Using the stated \(\sigma=0.000279\), the deviation from 0.5 is \((0.4974-0.5)/0.000279 \approx -9.35σ\), which rounds to 9.4, not 9.5. For Catalog A, \(0.5079-0.5=0.0079\); with \(\sigma=0.000279\), this is \(28.3σ\), not 28.8. Analogous small mismatches appear for Tier B.  
**Required fix:** Either recompute Dev. using exactly the quoted \(\sigma\), or explicitly state that a different effective \(\sigma\) (e.g. from a slightly different \(N\)) is used and adjust the tabulated uncertainty accordingly.

P4-M40 — Arithmetic / CW excess vs stated “−0.53%” (Sect. IV.B)  
**Problem:** The text describes “equivariant −0.53%” asymmetry-suppression from “raw +2.05% to equivariant −0.53%,” but Table II gives Catalog C excess as −0.26%. With the listed fraction 0.4974, the full-amplitude difference from 0.5 is −0.26%, not −0.53%. The factor-of-3.86 “asymmetry-suppression” (2.05% → 0.53%) is likewise inconsistent with 2.05% → 0.26% (suppression factor ≈7.9).  
**Required fix:** Bring the prose and Table II into numerical agreement: either correct the Catalog C excess and Dev. or update the “−0.53%” and “3.86×” factors to match the 0.4974 value.

P4-M41 — Arithmetic / “99.3%” leakage fraction (Abstract, Sect. IV.D, Table IV)  
**Problem:** The leakage description claims “99.3% of its observed amplitude” is reproduced. Table IV lists data \(1.696\times10^{-2}\) and null mean \(1.685\times10^{-2}\). The ratio \(1.685/1.696\approx0.9945\), i.e. 99.45%, not 99.3%. The stated z=+1.68 from \((1.696-1.685)/0.007 \approx 1.57σ\) also does not match exactly using the printed numbers.  
**Required fix:** Recompute the ratio and z from the actual simulation outputs and either (i) change the text to “≈99.4%” and update the z-value, or (ii) adjust the table entries so that the displayed numbers are internally consistent with 99.3% and z=1.68.

P4-M42 — Arithmetic / “z = Δ/σnull moment-ratio” versus MC rank (Abstract, Table III)  
**Problem:** The abstract defines z as “∆/σnull moment-ratio,” but for the canonical-mask residual it simultaneously quotes “+3.64σ (… empirical rank pMC = 0.030).” A one-sided Gaussian \(p=0.030\) corresponds to \(z≈1.88\), while two-sided corresponds to \(z≈2.17\); neither matches 3.64. In Table III, the ℓeff=4 entry has Cℓ=3.210, σnull=0.804, Significance=+6.097, but their ratio \(3.210/0.804≈3.99\), not 6.10. This shows z is not consistently “∆/σnull” in the table either.  
**Required fix:** State explicitly how z is defined for each case (raw Cℓ/σnull, tail probability mapped to σ, or higher-moment ratio) and ensure the quoted σ values are consistent with that definition; otherwise, the same symbol “σ” is being used for inequivalent statistics.

P4-M43 — Arithmetic / Fisher floor and “σ(A/2) ≈ 0.048%” (Sect. VI.A)  
**Problem:** With \(N_{\text{spiral}}=3{,}201{,}160\), the binomial standard deviation of the CW fraction is \(\sigma(p)\approx\sqrt{0.25/N}\approx 0.000279\) (0.0279%), so \(\sigma(A/2)\) (half-amplitude) should be ≈0.028%, not 0.048%. A 3σ full-amplitude floor would therefore be about 0.17%, not 0.29%. The numbers 0.048% and 0.29% appear stale or derived from a smaller effective \(N\) or different \(f_{\rm sky}\) than quoted.  
**Required fix:** Re-derive the Fisher sensitivity using the exact \(N_{\text{spiral}}\) and \(f_{\rm sky}\) (and any dilution factor) and update both 0.048% and 0.29% so they are traceable from the displayed inputs.

P4-M44 — Arithmetic / g-factor and “true-underlying threshold ∼1.88%” (Sect. VI.A)  
**Problem:** The text states “g = 2a − 1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ∼ 1.88%” from an observed 0.75%. If the observed amplitude is diluted by g, the intrinsic amplitude is \(A_{\rm true} = A_{\rm obs}/g ≈ 0.75\% / 0.398 ≈ 1.88\%\), which is consistent. However, earlier prose associates the empirical 0.75% threshold with a 3σ recovery and elsewhere uses different amplitude numbers (0.26%, 0.4%, 0.79%). The mapping is never written explicitly as a formula, and the 0.75% used here conflicts with the Fisher floor numerics above.  
**Required fix:** Present the full equation \(A_{\rm true} = A_{\rm obs}/g\) with the exact numbers plugged in, and ensure all amplitude thresholds (0.26%, 0.4%, 0.75%, 1.88%) are tied consistently to either observed, diluted, or intrinsic quantities.

P4-M45 — Arithmetic / “maximum regional asymmetry is 0.32%” (Sect. V.A)  
**Problem:** The text claims “maximum regional asymmetry is 0.32%,” but no table gives the regional CW fractions, and 0.32% is not obviously derivable from any previously quoted numbers (e.g., the global −0.26% or earlier asymmetries). Without the underlying counts or regions, this number cannot be recomputed or checked.  
**Required fix:** Add a table or figure listing the per-region CW fractions and counts from which 0.32% is derived, or remove the numerical value if it cannot be supported.

P4-M46 — Arithmetic / “2.31σ real-space; +6.48σ pre-MASTER” vs given amplitudes (Sect. VI, VII.c)  
**Problem:** The raw Catalog A dipole is quoted as 2.31σ and the pre-MASTER pseudo-Cℓ as +6.48σ, but the underlying amplitudes and null dispersions are not shown anywhere (no entries in Tables I–IV for the raw tier). Without the base numbers, these σ-values cannot be recomputed, and their consistency with the stated +0.79% monopole is unclear.  
**Required fix:** Provide the raw Catalog A dipole amplitude, its bootstrap uncertainty, the pre-MASTER Cℓ values, and their null dispersions so that 2.31σ and 6.48σ can be independently verified.

P4-M47 — Figure-caption vs body-claim / ℓ = 1 “primary observable” vs Table III interpretation (Sect. IV.C, Table III)  
**Problem:** Sect. IV.C calls the MASTER ℓ=1 value “the primary isotropy-breaking dipole observable,” while Table III’s caption highlights ℓeff=4 as “Mask-coupled monopole leakage,” and the abstract emphasizes that the canonical-mask residual is a systematic. The table combines the subsample-mask ℓ=1 single mode (fsky=0.659) with canonical-mask bandpowers (fsky≈0.49) and then uses a joint χ²/dof to argue for mask-coupled leakage. The body text does not clearly restate that the ℓeff rows and ℓ=1 row are from different masks/nulls, despite the mixed presentation in one table.  
**Required fix:** Add explicit statements in both the text and the Table III caption that the ℓ=1 single-mode entry (subsample mask) and the ℓeff bandpowers (canonical mask) are based on different sky masks and nulls and are not directly comparable without that caveat.

P4-M48 — Equation dimensional consistency / asymmetry map definitions (Eq. (3), Appendix A)  
**Problem:** Eq. (3) defines \(A_p=(N_{CW}^{(p)}-N_{CCW}^{(p)})/(N_{CW}^{(p)}+N_{CCW}^{(p)})\). Appendix A later defines “asymmetry field” as \(A_p=(N_{CW}^{(p)}-N_{CCW}^{(p)})/N_{total}^{(p)}\) and separately mentions a monopole-subtracted “CW-deficit map \(f_{CW}(n̂)-0.5\).” These are three different normalizations (spiral-only fraction, all-class fraction, and CW-0.5) all called “A” or “asymmetry,” with no explicit mapping between them. Units are dimensionless in each case, but the normalization choice materially affects the power spectrum normalization and any Fisher-sensitivity arguments.  
**Required fix:** Choose a single canonical definition for the analysis field (e.g. spiral-only asymmetry) and explicitly show how the other two are related or used in cross-checks; otherwise, the MASTER Cℓ units and inferred amplitudes are ambiguous.

P4-M49 — Null procedure comparability / Abstract vs Sect. IV vs Appendix C (E)  
**Problem:** Although there is one prominent warning that σ values are “not directly comparable across estimators,” the paper repeatedly compares: (i) the canonical +3.64σ (pp-shuffle null), (ii) the hemisphere 3.05σ (max-stat null with LEE correction), (iii) the real-space +0.43σ (bootstrap null), and (iv) various bandpower σ’s (from different NaMaster nulls) in close succession without explicit per-instance reminders. For example, Sect. IV.D narrates the 3.64σ residual and the 3.05σ hemisphere maximum in the same paragraph as if they were on a common scale; Sect. VI restates 2.31σ, 0.43σ, −0.122σ, and 3.05σ together.  
**Required fix:** At each juxtaposition where two or more σ’s from different nulls appear in the same sentence or paragraph, add a brief parenthetical (“different null procedures; not directly comparable”) and specify the null used.

P4-M50 — Abstract faithfulness / “99.3%” and “1.7% clean dipole” interpretations (Abstract, Sect. IV.D, Appendix D)  
**Problem:** The abstract and conclusions state that a monopole-only null “reproduces 99.3% of the observed pre-MASTER … power” and treat “a clean real cosmological dipole at amplitude ∼1.7%” as disfavored. In the body, the 1.7% comes from a “reference amplitude” used in a WLS template fit (Appendix D), where the estimated best-fit dipole is 0.23% and the “1.7% at z=−264.5” appears to be a hypothetical point in the posterior far tail, not an actual measured amplitude. The leap from a hypothetical 1.7% to “interpretation (i) as a clean dipole-only explanation” being disfavored is conceptually confusing, and the abstract makes it sound as if a 1.7% signal were directly tested.  
**Required fix:** Clarify in the abstract and main text that 1.7% is a hypothetical amplitude used for comparison, not a measured value, and that the monopole-only null explains ≈99% of the pre-MASTER power with a much smaller effective dipole (0.23%).

P4-M51 — Abstract faithfulness / “sub-percent sensitivity” vs injection threshold (Abstract, Sect. VI.A, VII.d)  
**Problem:** The abstract claims a “sub-percent sensitivity” chirality dipole null, and Sect. VI.A gives an empirical 50%-recovery-at-3σ threshold of 0.75% and a Fisher floor of 0.29%. The use of “sub-percent” is technically compatible with 0.75%, but readers might infer sensitivity approaching the Fisher 0.29% limit, which the paper does not achieve in practice due to systematics. The body text acknowledges this only briefly.  
**Required fix:** Rephrase the abstract to indicate that the *practical* sensitivity floor is ≈0.75%, clearly distinguished from the formal Fisher 0.29% limit, and avoid implying that the analysis is sensitive to all sub-percent amplitudes.

P4-M52 — Appendix vs main-text mismatch / hemisphere LEE numbers (Sect. IV.E, Appendix C)  
**Problem:** Sect. IV.E states that the hemisphere maximum is 3.05σ and that Bonferroni/BH correction across ∼650 directions downgrades this to <1σ, while Appendix C quotes a direct-MC look-elsewhere \(p_{LEE}\le 10^{-4}\) and again refers to Bonferroni/BH reducing post-LEE significance to <1σ. The explicit corrected σ-equivalent for the direct-MC p-value is never given, and the relation between the MC rank test and the Bonferroni/BH counting is not quantified; a naive translation of \(p_{LEE}=10^{-4}\) would still be ≈3.9σ before any further penalty.  
**Required fix:** Provide the exact σ-equivalent for the direct-MC \(p_{LEE}\) and show how the ∼650-direction trials factor leads to the claimed <1σ corrected significance, or state unambiguously that the Bonferroni/BH correction is being applied to a pre-LEE local σ, not to the \(p_{LEE}\) itself.

P4-M53 — Appendix vs main-text mismatch / HC cuts and “+4.31σ monopole-preserving dipole” (Appendix E vs main text)  
**Problem:** Appendix E mentions “The Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict),” while the main text’s primary real-space dipole is given as +0.43σ (Sect. IV.C) and there is no explanation of what “monopole-preserving dipole” means or how 4.31σ relates to 0.43σ. The apparent change of reference estimator (or null) between main text and appendix is not flagged.  
**Required fix:** Define “monopole-preserving dipole” in the main text, specify its null procedure, and explain the relation between its 4.31σ value and the +0.43σ headline real-space dipole, including why the latter is taken as primary.

P4-M54 — Stale numbers / pixel threshold and Nmap,weighted (Sect. III.A, Table I, Appendix A)  
**Problem:** The paper repeatedly uses “n = 5,547,858, fsky=0.659” as both the number of spirals on the subsample mask and the “Nmap,weighted” sum of weights, but Appendix A clarifies that \(N_{\text{map,weighted}} = Σ_{p}W_p\) where each Wp includes non-spirals; this should exceed the spiral count. Table I lists Ncatalog_spiral=3,201,160 and Nmap_weighted=5,547,858 for the subsample, but the abstract refers to “MASTER-deconvolved … on the strict-superset subsample mask (n=5,547,858, fsky=0.659)” as though n were the number of galaxies, not the weighted sum. The dual use strongly suggests n=5,547,858 originated as a galaxy count in an earlier version and was later repurposed as a weight sum without consistently updating the text.  
**Required fix:** Distinguish clearly between (i) the number of spirals on the subsample mask and (ii) the sum of per-pixel weights, giving separate symbols and values. Correct the abstract and any other places where n=5,547,858 is described as a galaxy count if it is in fact a weighted sum.

If you want, I can next go equation by equation and reconstruct the implied units and normalization for each Cℓ and dipole amplitude, but that will require you to supply the actual numeric scripts or additional tables with the unrounded values.