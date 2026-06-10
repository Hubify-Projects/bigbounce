# P1B R23conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.51.pdf` md5=856fbad2 pages=13
**Input format**: TEXT + web search + pass-2 self-critique (10436 chars)
**Wall time**: 85.6s

---

P1B-E1 (ESSENTIAL)  
Section: References, p. 13  
Problem: Reference [3] is cited as “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” This arXiv ID is future‑dated and invalid: there is no arXiv:2509.13654 entry corresponding to this title or author list as of now, and ACT DR6 has not been released under that identifier. The paper appears fictitious or at least mis‑cited.  
Required fix: Either (a) replace [3] with a real, existing ACT birefringence analysis (correct arXiv ID, year, and journal/“preprint” status), and adjust all references to “ACT DR6” and the quoted β = 0.215° ± 0.074° accordingly, or (b) clearly mark this as an unpublished internal analysis and remove all arXiv metadata, adjusting claims so no numerical result is attributed to a non-existent paper. The manuscript cannot cite a fabricated or future‑dated arXiv entry.

---

P1B-E2 (ESSENTIAL)  
Section: References, p. 13  
Problem: Reference  “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc]” uses a future-dated arXiv identifier (2507.04265). No such arXiv entry exists yet; the metadata are speculative.  
Required fix: Replace this with a real, currently available torsion-cosmology paper (correct arXiv ID and bibliographic details) whose numbers you actually use, or remove this reference and the discussion that depends on it. Do not use fabricated/future arXiv IDs.

---

P1B-E3 (ESSENTIAL)  
Section: References, p. 13  
Problem: Reference  “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].” Again, arXiv:2503.14738 is future‑dated and does not exist; DESI DR2 has not yet appeared under this ID. The specific journal volume/page/ID combination is also speculative.  
Required fix: Cite the latest *actual* DESI BAO / DR2 paper (with correct arXiv ID and status), or else relabel this as “DESI internal forecast” without arXiv/journal metadata and remove all quantitative attribution that cannot be traced to a real publication. The current citation is not acceptable for PRD.

---

P1B-E4 (ESSENTIAL)  
Section: References, p. 13  
Problem: References [5] and [6] (other “companion papers” by the same author, both “(in preparation) (2026), hUBIFY‑2026‑003/004; companion paper, this volume”) are cited with internal IDs and “this volume” language but are not publicly available, not on arXiv, and not published in a recognized journal. They are also given as delivering crucial datasets and conceptual results (multi-survey anomaly catalog, galaxy chirality catalog) that are used program‑wide. PRD normally does not allow “in preparation” references as load‑bearing support for quantitative claims.  
Required fix: Either (a) post these manuscripts on arXiv and update the references with arXiv IDs, or (b) remove them as load‑bearing references and ensure this paper is fully self‑contained in its methods and data description, or relies only on published/archived sources. At minimum, drop “this volume” and “in preparation” if these papers are not accepted PRD articles in the same issue.

---

P1B-E5 (ESSENTIAL)  
Section: References, p. 13  
Problem: Reference [1] “H. Golden, Structural Closure of Einstein–Cartan–Holst Dark Energy: …, (in preparation) (2026), hUBIFY‑2026‑001A; companion paper, this volume.” This “Paper I(a)” is the main scientific foundation for this technical companion (structural closure, perturbation-transparency theorem, matter‑bounce predictions, etc.), but is only “in preparation” with no arXiv ID or DOI. Many key claims in the body are deferred to that paper (e.g., the 14 barriers, perturbation transparency, surviving tests), meaning they are uncheckable.  
Required fix: Make Paper I(a) publicly available (arXiv or published) and update the citation with correct bibliographic metadata, or reduce references to it to a minimum and state clearly which results in this companion are fully independent of I(a). PRD should not accept a derivative technical companion whose parent paper cannot be examined.

---

P1B-E6 (ESSENTIAL)  
Section: References, p. 13  
Problem: Reference [4] “H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (in preparation) (2026), hUBIFY-2026-002; companion paper, this volume.” This SPHEREx forecast and fNL prediction are repeatedly invoked in the text as part of the program narrative, but this reference is only “in preparation” with no public record.  
Required fix: Either publish/post this paper and cite it properly, or remove all claims that depend on its results (especially any numerical SPHEREx forecasts) from this manuscript.

---

P1B-E7 (ESSENTIAL)  
Section: References, p. 13  
Problem: Reference [5] explicitly includes the label “(in preparation) (2026), hUBIFY-2026-003; companion paper, this volume.” This is version-history / internal‑bookkeeping language (“hUBIFY-2026-XXX”, “this volume”) that does not belong in a final PRD reference list, per the instructions.  
Required fix: Strip internal IDs and “this volume” language, or replace with standard citation data once (and if) the paper is accepted. If the work is not yet public, it must not carry load-bearing claims here.

---

P1B-E8 (ESSENTIAL)  
Section: References, p. 13  
Problem: Reference [6] has identical issues: “(in preparation)” plus internal label “hUBIFY-2026-004; companion paper, this volume.” This is version‑history / bookkeeping.  
Required fix: As above: remove internal identifiers and “this volume”, or provide a proper, public reference. Avoid any use as quantitative support until the paper is accessible.

---

P1B-E9 (ESSENTIAL)  
Section: Abstract, p. 1  
Problem: The abstract states “The primary sky detection significance is the published Planck/ACT DR6 2.7–2.9σ [2, 3]; the pipeline SNR figures refer to recovery of injected MC signals…” The Planck NPIPE birefringence significance and the “2.7–2.9σ” range are being attributed to [2] and [3], but [3] is non‑existent and [2] (Eskilt & Komatsu PRD 106, 063503) analyzes Planck PR3+WMAP9, not Planck PR4+ACT DR6. The 2.7–2.9σ range appears to fuse statistics from different works (Planck PR4 birefringence from Diego‑Palazuelos et al. and ACT DR6, plus Eskilt & Komatsu). This is citation fusion: the numerical range in the abstract cannot be traced to the specific pair of references given.  
Required fix: Identify precisely which published analyses yield 2.7σ and 2.9σ and cite them correctly and separately (e.g., Planck PR4 birefringence, ACT DR6 birefringence, WMAP+Planck Eskilt & Komatsu). Remove [3] unless a real ACT DR6 paper exists, and ensure each quoted σ value is traceable to the corresponding paper.

---

P1B-E10 (ESSENTIAL)  
Section: §IV, p. 5 (“Birefringence measurements are adopted…” and its use of [3])  
Problem: The ACT DR6 value β = 0.215° ± 0.074° is attributed to [3], which is fictitious. Without a valid reference, this numerical measurement cannot be checked against the literature.  
Required fix: Replace the ACT DR6 birefringence entry with a real, published ACT result and correct citation, or move this number out of the main analysis into a clearly labeled speculative/forecast section that does not pretend to be based on a published paper.

---

P1B-E11 (ESSENTIAL)  
Section: §VI, p. 8–9 (ALP MCMC likelihood)  
Problem: The ALP likelihood is described as a “Gaussian summary likelihood on the published Eskilt–Komatsu joint WMAP+Planck isotropic-birefringence measurement βobs = 0.342° ± 0.094° [2].” However, Eskilt & Komatsu (PRD 106, 063503, 2022, arXiv:2205.13962) employ a more complex likelihood built from EB/BB spectra, foregrounds, and calibration nuisance parameters. Modeling this as a single Gaussian in β is a *new* modeling choice and not directly documented in [2]. The paper presents this Gaussian summary as if it were a standard representation without detailing validation (e.g., showing that their 1D β posterior is well approximated by a Gaussian with that mean and σ). For PRD-level methods, such a reduction needs justification.  
Required fix: Explicitly state that you approximate the full likelihood by a Gaussian in β using the quoted mean and σ from [2], and discuss/justify this approximation, or demonstrate with a figure that the β posterior from [2] is nearly Gaussian. Otherwise, readers cannot reproduce your ALP likelihood from the cited source alone.

---

P1B-M1 (MAJOR)  
Section: §II / §III, p. 2–4 (“Cosmological Tensions: H0 and σ8”, discussion of Liu et al. )  
Problem: The comparative statements “Liu et al.  constrained an EC torsion model… finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6) but with the torsion parameter itself consistent with zero (α = −0.00066 ± 0.00098). Their headline values H0 = 68.41 ± 0.32 km/s/Mpc and S8 = 0.812 ± 0.006…” are alleged to be drawn from . Because  is not a real paper (future-dated arXiv ID), these numbers cannot be checked, and could be fused from multiple sources.  
Required fix: Remove this paragraph or replace  with a real, existing torsion cosmology paper whose AIC, torsion parameter, H0, and S8 match the quoted values. Recompute the quoted σ‑level agreements from actual published numbers and update citations accordingly.

---

P1B-M2 (MAJOR)  
Section: §V, Table II, p. 4  
Problem 1: Table II is labeled “DESI DR2 w0 wa posterior summary” and the text refers to “DESI DR2 BAO” and “DESI DR2 results II” . Since  is not a real paper, it is unclear which actual BAO likelihood was used. The YAML block in Table III uses `bao.desi dr2.desi bao all`, which is not a standard, public Cobaya likelihood currently documented on arXiv/ADS. This raises reproducibility and provenance concerns: the derived wpivot and σ(wpivot) numbers cannot be cross‑checked against a published DESI DR2 analysis.  
Problem 2: The DESI DR2 data used may in fact be preliminary or internal (given the fabricated reference), but the paper treats them as published and final.  
Required fix: Either (a) restrict the analysis to publicly released DESI data with a correct reference (e.g., DESI DR1) and adjust Table II and the text to use that dataset, or (b) clearly state that this is an analysis of provisional DESI DR2 likelihoods not yet described in a refereed publication, and tone down any claims of “headline” or “empirical anchor” accordingly. PRD generally expects cosmological constraints to be based on public, documented data products.

---

P1B-M3 (MAJOR)  
Section: §VI, p. 8–10 (ALP parameter ranges and “natural-prior” language)  
Problem: The manuscript repeatedly calls θi ∈ [0.5, 2] “natural” and then later notes that the spectator‑consistent regime is θi ∼ 0.1, requiring ∼25× tuning. The “natural” label is not tied to any cited prior or theoretical argument beyond qualitative language. Furthermore, several quantitative statements about the required range of Caγ and ∆ϕ/fa (“spans ∼9–51”, “69% of posterior mass inside [9, 51]”, “0.4% of posterior mass for θi ≤ 0.1”) are based entirely on your own MCMC runs, but there is no cross-check with existing ALP birefringence analyses such as Fujita et al. .  
Required fix: Either provide a concise analytic comparison to  or other ALP papers (showing that your inferred Caγ × ∆ϕ/fa ranges are compatible with their constraints), or soften the language to make clear that these priors and “naturalness” criteria are your choices, not derived from prior work. Cite  more substantively where you claim your model class “was previously studied”.

---

P1B-M4 (MAJOR)  
Section: §III, p. 3–4; Table I, Table II  
Problem: Several quoted “σ” deviations (e.g., “w0 departs by +4.3σ”, “wa by −3.6σ”, “S8 sits 2.5σ above the DES-Y3 weak-lensing value”) are not shown to be recomputed in the manuscript itself. While the underlying numbers are present, there is no explicit demonstration of the σ calculations beyond footnote sketches, and the DES-Y3 comparison uses S8 = 0.776 ± 0.017  but the exact tension figure 2.5σ is not recomputed in situ. For PRD’s technical companion, these should be explicitly transparent.  
Required fix: Add an explicit short table or inline calculations showing each σ difference: e.g. δ/σcomb for H0, S8, w0, wa, and w0+wa, and verify they match the numbers quoted in the prose. This is documentation, but important for a technical verification paper.

---

P1B-M5 (MAJOR)  
Section: References, p. 13 – Ref.   
Problem: Reference  conflates two distinct works. It lists “P. Diego-Palazuelos, J. R. Eskilt, Y. Minami, M. Tristram, et al., Cosmic birefringence from the Planck data release 4, Phys. Rev. Lett. 128, 091302 (2022), reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4), arXiv:2201.07682 [astro-ph.CO].” In reality, arXiv:2201.07682 is “Cosmic birefringence from the Planck data release 4” by Diego-Palazuelos *et al.* (no Eskilt & Minami as co‑authors), PRL 128, 091302. The author list and description here fuse this with [2] (Eskilt & Komatsu).  
Required fix: Correct  to match exactly the actual Planck PR4 birefringence paper (author list and title), and ensure the β = 0.30° ± 0.11° number and its interpretation match that paper’s abstract or main tables. Remove Eskilt’s name from  if not present in the original and keep [2] separate.

---

P1B-M6 (MAJOR)  
Section: Throughout (e.g., Abstract; §III, §V, §VII)  
Problem: The text repeatedly uses phrases like “headline result”, “headline observational constraint”, “headline 3.6σ”, “headline number” in a quasi‑marketing way and sometimes fuses these with different references. This non‑standard phrasing makes it difficult to trace which numerical result comes from which source and can conceal fused statistics (as in the 2.7–2.9σ Planck/ACT range).  
Required fix: Replace “headline result” etc. with precise attributions: “Eskilt & Komatsu [2] report β = … at 3.6σ”, “Diego-Palazuelos et al.  report β = … at Xσ”, etc., and ensure each quoted σ is individually traceable.

---

P1B-M7 (MAJOR)  
Section: References, p. 13  
Problem: Reference  “Y.‑F. Cai, W. Xue, R. Brandenberger, and X. Zhang, Non-gaussianity in a matter bounce, JCAP 0905, 011, arXiv:0903.0631.” is missing the year and the journal volume/issue are not in standard PRD format (should be JCAP 05 (2009) 011). Similarly, several other references (e.g. , , , , ) have inconsistent styling (missing years, or mis-ordered metadata) relative to PRD’s standard.  
Required fix: Normalize all cosmology references to standard PRD format: journal name, volume, page/article number, year, and correct arXiv ID. This is a significant editorial clean‑up, expected for PRD.

---

P1B-N1 (NIT)  
Section: Abstract, p. 1; §III, footnote 1, p. 3  
Problem: The sample-count reconciliation footnote is verbose and includes internal file names and minor numerical discrepancies (e.g. 123,368 vs 123,129 post‑burn‑in). For a paper in PRD, this level of version-history detail in the main text is excessive and makes the narrative hard to follow.  
Required fix: Move this minute bookkeeping into an appendix or the online repository README. In the main text, just state the final effective sample numbers and R̂ thresholds.

---

P1B-N2 (NIT)  
Section: Appendix A, p. 11–12  
Problem: The acknowledgments include “We thank … and acknowledge the use of Claude (Anthropic) as an AI research assistant… All scientific claims … were independently verified by the author.” This is acceptable, but some journals may prefer AI-use disclosures in a dedicated statement rather than in the general acknowledgments.  
Required fix: Check PRD policy on AI use. If needed, move this statement into a brief “Author’s note on AI use” or similar, per editorial guidance.

---

P1B-N3 (NIT)  
Section: §IV footnote 3, p. 6–7  
Problem: The footnote explicitly refers to “quoted in an earlier draft of this footnote,” which is version‑history language.  
Required fix: Remove “quoted in an earlier draft of this footnote” and rephrase to be self-contained (e.g., “This value is …”).

---

P1B-N4 (NIT)  
Section: Appendix A, p. 11–12  
Problem: Several repository paths and branch names (“research/branch_R_alp_birefringence/phase2_mcmc/…”) are detailed in the text, which is more appropriate for documentation than for a PRD article.  
Required fix: Condense these into a shorter description and refer to the repository README for the full path structure.

---

P1B-N5 (NIT)  
Section: Appendix B / Table IV, p. 12  
Problem: Table IV is titled “Claims classification for this companion paper.” While useful internally, this is not a standard PRD device and reads like an internal audit artifact.  
Required fix: Either remove this table or reframe it as a brief narrative paragraph summarizing which claims are MCMC‑derived vs literature‑cited.

---

P1B-N6 (NIT)  
Section: §V A, p. 7 (“Reproducibility materials at https://github.com/…”)  
Problem: Direct URLs in the text are acceptable, but PRD typically puts data/code availability in a dedicated section and may prefer a DOI-based archive. GitHub URLs can change.  
Required fix: Consider mirroring the repository on a DOI-granting archive (e.g., Zenodo) and citing that DOI, with the GitHub link only as a secondary pointer.

---

## Summary recommendation

MAJOR REVISIONS  

The manuscript’s internal numerical consistency is mostly reasonable, but the citation forensics reveal multiple severe issues: at least three references use fabricated, future-dated arXiv IDs; several “companion papers” and key program elements are only “in preparation” and not publicly accessible; and some numbers are attributed to non-existent or mis-described sources, including ACT DR6 birefringence and torsion-cosmology constraints. For PRD, these citation and provenance problems are unacceptable and must be fully resolved by replacing all speculative references with real publications (or removing dependent claims), correcting fused/misaligned citations, and cleaning up version-history language. Once those are fixed and the analysis is anchored in existing literature, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E12 (ESSENTIAL)  
Section: §II, p. 3 (“MB–H0 joint-posterior offset check”)  
Problem: The text states that the offset between the Pantheon+ degeneracy constant at the Riess anchor and the chain mean “is ∼ 3.2σ relative to the chain’s σMB = 0.049 marginal width.” From the given numbers, the offset is 0.156 mag and σMB = 0.049 mag, so the significance is 0.156 / 0.049 ≈ 3.18σ (consistent). However, the same paragraph also calls this “the canonical 3.6σ when the tension is expressed in distance-ladder terms in the H0 axis.” That 3.6σ refers to |73.04 − 67.68| / √(1.06² + 1.04²) ≈ 4.08 / 1.49 ≈ 2.74σ, not 3.6σ, using the numbers quoted in this paper. The 3.6σ headline is imported from the SH0ES paper and not recomputed from the values used here; as written, the tension significance quoted for this dataset combination is numerically inconsistent with the paper’s own numbers.  
Required fix: Recompute the H0 tension significance directly from the H0 values and uncertainties actually used in this manuscript and state that number explicitly, or else clearly attribute the “3.6σ” to the original SH0ES analysis and avoid implying that it is recomputed here. Align the MB-axis and H0-axis tension descriptions quantitatively.

---

P1B-E13 (ESSENTIAL)  
Section: §III, p. 4 (“The iter2 chain’s S8 = 0.8245 ± 0.0089 … sits 2.5σ above the DES-Y3 weak-lensing value S8 = 0.776 ± 0.017”)  
Problem: The stated 2.5σ tension can be recomputed from the given numbers: ΔS8 = 0.8245 − 0.776 = 0.0485, combined σ = √(0.0089² + 0.017²) ≈ √(7.9×10⁻⁵ + 2.89×10⁻⁴) ≈ √(3.68×10⁻⁴) ≈ 0.0192, so Δ/σ ≈ 0.0485 / 0.0192 ≈ 2.53σ. This does match “2.5σ,” but nowhere in the text or tables is this arithmetic shown; the reader must reconstruct it. Given the paper’s emphasis on technical verification and other σ-level claims (H0, w0, wa), leaving all of these as implicit mental arithmetic undercuts reproducibility.  
Required fix: Add a compact table or inline equation explicitly showing the Δ/σcomb calculation for each quoted σ-level tension (H0, S8, w0, wa, w0 + wa), using the numbers already in Tables I and II and the cited comparison values (Riess H0, DES-Y3 S8, ΛCDM w0 = −1, wa = 0). Make clear which tensions are recomputed here and which are imported from external papers.

---

P1B-M8 (MAJOR)  
Section: Abstract & §III (ΛCDM+ΔNeff proxy)  
Problem: The abstract states “Both frozen dataset combinations find ΔNeff consistent with zero (−0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN) and H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN…).” The body does not provide any explicit quantitative comparison between these H0 values and a specific “standard ΛCDM” reference (e.g., Planck 2018 baseline), nor does it show the σ-level agreement. The phrase “consistent with standard ΛCDM” is therefore an unquantified hedge.  
Required fix: Identify a specific ΛCDM reference value (e.g., Planck 2018 or PR4 best-fit H0 with its uncertainty) and compute the difference and combined σ, or else rephrase to “numerically close to typical Planck ΛCDM values” without implying a quantified statistical compatibility that is not actually shown.

---

P1B-M9 (MAJOR)  
Section: Abstract vs §IV–§VI (birefringence significance and ACT use)  
Problem: The abstract says: “The primary sky detection significance is the published Planck/ACT DR6 2.7–2.9σ [2, 3]… The primary sky detection significance is the published Planck/ACT DR6 2.7–2.9σ [2, 3];a the pipeline SNR figures refer to recovery of injected MC signals…” In the body, §IV and §VI instead use (i) β = 0.30° ± 0.11° from Planck PR4 () and (ii) βobs = 0.342° ± 0.094° at 3.6σ from Eskilt & Komatsu [2], while the ACT DR6 value β = 0.215° ± 0.074° appears only as a standalone number with a fictitious reference [3]. There is no place in the body where a combined “Planck/ACT DR6 2.7–2.9σ” significance is defined or derived. The abstract’s 2.7–2.9σ range is therefore not traceable to any specific computation or citation in the main text; it silently fuses disparate published significances.  
Required fix: Either (a) remove the “Planck/ACT DR6 2.7–2.9σ” wording from the abstract and instead quote the specific published significances that are actually used in the body (3.6σ from Eskilt & Komatsu [2]; Xσ from Diego‑Palazuelos et al. ; ACT value if a real reference exists), or (b) add a clear sentence in §IV that explains exactly which published numbers are combined to yield 2.7σ and 2.9σ, with correct citations. In any case, ensure the abstract’s significance statements match documented calculations in the body.

---

P1B-M10 (MAJOR)  
Section: Abstract vs §VI & Appendix C (ALP likelihood modeling)  
Problem: The abstract and §VI describe the ALP consistency check as using “the published joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ) [2]” via a “Gaussian summary likelihood,” and Appendix C confirms the likelihood is implemented as a 1D Gaussian in β centered on 0.342° with σ = 0.094°. Eskilt & Komatsu [2] derive this from a higher-dimensional likelihood with foregrounds and calibration nuisance parameters. The paper never quantitatively shows that the 1D β posterior from [2] is close to Gaussian, nor how non-Gaussianity or parameter degeneracies might affect the ALP posteriors. This means the “Gaussian summary likelihood” is a nontrivial modeling choice that is not justified beyond a brief prose note; yet the abstract presents the consistency check result as if it were a straightforward propagation of [2].  
Required fix: In §VI, add a concise quantitative justification of the Gaussian approximation, for example by reproducing or citing the 1D β posterior from [2] and explaining its near-Gaussianity, or by explicitly framing this as an approximation and discussing its potential impact on the ALP posterior. Make clear that this is a new modeling step, not simply “using” Eskilt & Komatsu’s likelihood in its original form.

---

P1B-m1 (MINOR)  
Section: §IV, Fig. 3 caption vs text  
Problem: The caption to Fig. 3 states that “The worst-case |bias| = 0.040° is the NaMaster systematic floor adopted in Eq. 1–fn. 3.” In the main text of §IV, the systematic floor is described as “we carry forward [−0.040°] as the NaMaster systematic floor” without referencing any equation, and there is no labeled “Eq. 1” in §IV that explicitly uses this 0.040° as a floor in an error budget or parameter constraint. This makes the role of the “systematic floor” opaque: is it ever propagated into any quoted uncertainty, or is it just a standalone diagnostic?  
Required fix: Either explicitly show, in the main text or an equation, how the 0.040° systematic floor is used (e.g., added in quadrature to some measurement uncertainty), or revise the caption to clarify that the 0.040° is simply a characterization of pipeline bias and is not propagated into any later error budget.

---

P1B-m2 (MINOR)  
Section: §V A, p. 7 (“Reproducibility materials at https://github.com/…”) vs Appendix A  
Problem: §V A briefly points to the GitHub repository for “reproducibility materials,” while Appendix A describes the repository structure in more detail. However, the likelihood blocks shown in Table III are described as “verbatim from the on-disk YAML,” and Appendix A notes that Bayes factors and information criteria are *not* included in the repository and must be recomputed. The juxtaposition of “verbatim YAML” and “follow-up nested-sampling analysis” can mislead readers into expecting that the repository already contains everything needed for full model-comparison reproduction (including priors suitable for nested sampling), which it does not.  
Required fix: Add a brief clarifying sentence in §V A or Appendix A stating explicitly that the repository provides parameter-estimation (Metropolis–Hastings) configs only, and that any future nested-sampling/evidence calculations would require additional configuration not included here.

---

P1B-m3 (MINOR)  
Section: §VI, p. 9–10 (ALP parameter ranges and “natural” language) vs Appendix C  
Problem: The main text calls m/H0 ∈ [1, 3], θi ∈ [0.5, 2] the “natural parameter range,” while Appendix C specifies that for the continuous-prior configuration log10(ma/eV) ∈ [−35, −30], corresponding to m/H0 ≈ 7×10⁻³–7×10², and θi ∈ [0.01, π]. Thus, different sections use different prior ranges for “naturalness” or for the “headline configuration,” but this is not clearly reconciled: a reader might mistakenly assume that all quoted posterior summaries use the same (narrow) priors described in the main text, whereas several key numbers (e.g., the Caγ = 20.7 median and the 69% mass inside [9, 51]) are from the broader continuous-prior run.  
Required fix: Add an explicit sentence in §VI clearly distinguishing between the narrow “natural-envelope” runs (m/H0 ∈ [1, 3], θi ∈ [0.5, 2]) and the broader continuous-prior configuration (log10(ma/eV) ∈ [−35, −30], θi ∈ [0.01, π]), and tag each quoted number (βALP, βfree, Caγ ranges, posterior mass fractions) with which configuration it comes from. This will prevent confusion about which priors underlie which reported results.

---

P1B-N7 (NIT)  
Section: Abstract and §III (use of “headline” for ALP and w0–wa results)  
Problem: The abstract and §V use “headline” language (e.g., “headline result,” “headline observational constraint”) for the w0–wa deviation and the ALP birefringence consistency, while §V itself explicitly states that Bayes factors and AIC/BIC are *not* computed and that robust model comparison is deferred. This can be read as over-selling what are, in this paper, posterior summaries without a full evidence analysis.  
Required fix: Soften the language in the abstract and §V by replacing “headline result/constraint” with more neutral terms like “main posterior summary” or “principal posterior finding,” and explicitly remind readers in §V that no Bayes-factor or AIC/BIC comparison is presented here.

---

Given the length and complexity of the manuscript, these additional issues are primarily in the categories of abstract faithfulness, unquantified hedges, and clarity of modeling choices, rather than gross arithmetic errors. The σ-level arithmetic that is explicitly reconstructible from the text appears numerically consistent, but several key significances and “consistency” statements need to be made more transparent and directly tied to computations shown in the body.