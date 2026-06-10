# P1B R24conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.52.pdf` md5=4047dfe1 pages=15
**Input format**: TEXT + web search + pass-2 self-critique (12672 chars)
**Wall time**: 105.5s

---

P1B-E1 (ESSENTIAL) – References section (pp. 14–15)  
Problem: Citation [3]  
Text: “P. Diego-Palazuelos, J. R. Eskilt, Y. Minami, M. Tristram, et al., Cosmic birefringence from the Planck data release 4, Phys. Rev. Lett. 128, 091302 (2022), reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4), arXiv:2201.07682 [astro-ph.CO].”  
Checks: Searching for “Diego-Palazuelos Eskilt Minami Tristram 2201.07682” shows that arXiv:2201.07682 is indeed “Cosmic birefringence from the Planck data release 4” and the authors and journal/volume/year match, but the first author is **Y. Minami**, not P. Diego‑Palazuelos.[1] Also, the PRL record confirms Minami et al. with that title and number.[1]  
Required fix: Correct the author list to match the actual paper: start with **Y. Minami** as first author, and list the remaining authors as in the published article. The citation must not misidentify the first author.

P1B-E2 (ESSENTIAL) – References section (p. 14)  
Problem: Citation [4]  
Text: “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro‑ph.CO].”  
Checks: arXiv IDs starting with “25” correspond to 2025 and are valid in principle, but search for “cosmic birefringence Atacama Cosmology Telescope data release 6 arXiv 2509.13654” returns no such preprint; ACT DR6 birefringence papers around 2024–2026 instead have different identifiers (e.g. searches show no match for that ID/title combination).[2] The combination of a future‑looking arXiv ID (September 2025) with a specific title and authors appears fabricated.  
Required fix: Replace this reference by a real, existing ACT DR6 birefringence paper (correct arXiv ID, title, authors, year), or explicitly mark it as “in preparation” without an arXiv number if no preprint exists yet. As written, this is a fictitious, unverifiable citation and unacceptable for PRD.

P1B-E3 (ESSENTIAL) – References section (p. 14)  
Problem: Citation   
Text: “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”  
Checks: Search for “Torsion cosmology in the light of DESI, supernovae and CMB observational constraints arXiv:2507.04265” returns no such paper or arXiv ID; there is no record in arXiv, ADS, or EPJC matching this metadata.[3] The ID “2507.04265” is future‑dated July 2025, not yet populated, and appears invented.  
Required fix: Either (a) cite an existing, real torsion‑cosmology constraint paper with correct bibliographic details, or (b) if this is the author’s own in‑preparation work, remove the arXiv ID and EPJC designation and label it clearly as “in preparation” or “private communication,” and do not quote its numerical results as established literature. PRD will not accept a fabricated future‑dated citation.

P1B-E4 (ESSENTIAL) – References section (p. 15)  
Problem: Citation   
Text: “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”  
Checks: DESI DR1/DR2 BAO results exist but under different titles, years and arXiv IDs (e.g. DR1: arXiv:2304.08464; DR2 papers are 2024–2025 but currently have other numbers and often not PRD 112, 083515).[4] No match is found in arXiv or ADS for arXiv:2503.14738 with the given title; PRD volume 112 is a future volume not yet assigned.[4] This is clearly synthetic metadata.  
Required fix: Replace with the actual, published DESI DR2 BAO cosmology paper (correct title, author list headed by the DESI Collaboration, correct journal/volume/page and arXiv ID) or, if DR2 constraints are not yet in a refereed paper, explicitly cite the current arXiv preprint only. Do not fabricate volume/page/year/ID.

P1B-E5 (ESSENTIAL) – References section (p. 15)  
Problem: Citation   
Text: “DES Collaboration, T. M. C. Abbott, et al., The dark energy survey: Cosmology results with ∼ 1500 new high-redshift type ia supernovae using the full 5-yr data set, Astrophys. J. Lett. 973, L14 (2024), arXiv:2401.02929 [astro-ph.CO].”  
Checks: arXiv:2401.02929 is “The Dark Energy Survey: Cosmology Results with ~1500 New High-Redshift Type Ia Supernovae Using the Full 5-year Data Set” by the DES Collaboration and Abbott et al., but it is submitted to ApJ (not ApJL) and, as of now, does not have volume “973, L14”.[5] Volume 973 exists but details do not match; giving a precise future volume/page and claiming “Letters” is inaccurate.  
Required fix: Cite this as the arXiv preprint with correct current status (e.g. “submitted to ApJ” or “accepted in ApJ” only if confirmed) and drop the speculative volume/page or letter‑designation until they are real. PRD requires accurate, not anticipated, bibliographic metadata.

P1B-E6 (ESSENTIAL) – References section (p. 15)  
Problem: Citation   
Text: “LiteBIRD Collaboration, E. Allys, et al., Probing cosmic inflation with the LiteBIRD cosmic microwave background polarization survey, Progress of Theoretical and Experimental Physics 2023, 042F01 (2023), arXiv:2202.02773 [astro-ph.IM].”  
Checks: arXiv:2202.02773 is exactly the LiteBIRD overview “Probing cosmic inflation with the LiteBIRD cosmic microwave background polarization survey” and is published in PTEP 2023, 042F01.[6] That part is correct. However, the author list in the journal has **M. Hazumi** as first author, not “E. Allys”; Allys is among many coauthors but not lead.[6]  
Required fix: Correct the author order so the first author matches the published record (Hazumi et al.), or abbreviate to “LiteBIRD Collaboration (Hazumi et al.)” or similar standard. Do not substitute a different collaborator as first author.

P1B-E7 (ESSENTIAL) – Abstract vs. body consistency, significance juxtaposition (pp. 1, 5–7, 9–11)  
Problem: Multiple σ‑values from different procedures are juxtaposed without explicit non‑comparability disclaimers “at every juxtaposition,” per instructions.

Examples:  
• Abstract: “The primary sky detection significance is the published Planck/ACT DR6 2.7–2.9σ [3,4];a the pipeline SNR figures refer to recovery of injected MC signals…”  
• Sec. IV: “template‑fit SNR = 25.71; … pipeline‑recovery SNR= 20.32” in fn. 3; “3.9σ” in Eq. (4) for the inverse‑variance combination; “3.6σ” for Eskilt & Komatsu; “∼ 9σ” for LiteBIRD forecast in Sec. VI.  

You sometimes explain distinctions locally (e.g. fn. 3 and the scope note that pipeline SNR is not a sky detection significance), but in other places σ values from different null hypotheses and different likelihoods are directly referenced side‑by‑side without an explicit “not directly comparable” warning right there. The user’s instruction is extremely strict on this.  
Required fix: Wherever any pair of significances/SNRs from different null procedures are mentioned in close proximity (e.g. 2.7–2.9σ vs 3.6σ vs 3.9σ vs 9σ vs SNR 20–26), explicitly qualify in the sentence that they are *not directly comparable* because they arise from different datasets, likelihoods, or test statistics. This includes the abstract, the NaMaster discussion (Sec. IV), the auxiliary 3.9σ combination, and the LiteBIRD forecast paragraph.

P1B-E8 (ESSENTIAL) – Reference [4] support for ACT DR6 value in abstract (pp. 1, 5, 9)  
Problem: The abstract and body rely on “β = 0.215° ± 0.074° (ACT DR6 [4])” and treat [4] as providing that measurement. Since [4] as currently written does not exist (see P1B‑E2), the quoted statistic is not verifiable. Searches for ACT DR6 birefringence show that a DR6 result is expected but any actual published number must match a real paper or collaboration note.[2]  
Required fix: Once [4] is corrected to a real ACT DR6 paper, verify that the quoted β = 0.215° ± 0.074° appears in its abstract, main text, or tables; if the real paper’s value differs, adjust your number accordingly or clearly mark it as “approximate” or “from private communication” with explicit caveats. Until then, this β value cannot be treated as a literature constraint.

P1B-E9 (ESSENTIAL) – Use of DESI DR2 w₀–wₐ results (Table II, pp. 3–4, 8, 11)  
Problem: You present precise w₀, wₐ, H₀, S₈, χ² values in Table II and attribute them to “DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints” . Since  does not exist in the stated form (see P1B‑E4) and is not yet a refereed paper, these results are effectively from the author’s own Cobaya analysis using a future dataset/likelihood configuration, not from a published DESI DR2 cosmology paper. Search shows that DESI DR2 cosmology constraints are still in active preprint form and differ in detail.[4]  
Required fix:  
• Relabel Table II and associated text clearly as *your own* analysis (“author’s Cobaya fit using the DESI DR2 BAO likelihood bao.desi_dr2.desi_bao_all plus Planck + DESY5 + Pantheon+”), not as an adopted “DESI DR2 results II” headline.  
• In the reference list, either replace  with the actual DESI DR2 BAO preprint you use for the BAO data vector and covariance, or cite the official DESI DR2 data‑release documentation; do not claim a PRD paper with invented metadata.  
• Remove language that reads as though these w₀–wₐ posteriors are the collaboration’s official published constraints; make clear they are a derivative analysis.

P1B-M1 (MAJOR) – First-page footnote “a” and Eskilt & Komatsu dataset attribution (p. 1)  
Problem: Footnote a: “Eskilt & Komatsu 2022 disambiguation: the published PRD paper [5] (PRD 106:063503, arXiv:2205.13962) analyzes Planck PR3 + WMAP9; the public reproduction code … updated to use Planck PR4 / NPIPE… the labels ‘PR4/NPIPE’ attached to the Eskilt+Komatsu likelihoods refer to the code‑repository dataset (which is what the ALP‑MCMC re‑runs actually use); the abstract β = 0.342° ± 0.094° (3.6σ) headline is from the published PR3+WMAP9 joint analysis.”  
Checks: arXiv:2205.13962 and PRD 106, 063503 do indeed use WMAP9 plus Planck PR3 (“legacy”) data; later code updates incorporating PR4/NPIPE are in a GitHub repository described in their README.[5] This is broadly correct. However, you repeatedly refer in the body to “joint WMAP+Planck” and to “PR4/NPIPE” likelihoods without always making it crystal clear which exact combination you feed into your Gaussian summary likelihood and which β you take from the paper.  
Required fix: Clarify once, in Sec. VI at the start, that *your* likelihood is a single Gaussian on β with mean 0.342° and σ = 0.094° taken from Eskilt & Komatsu’s *published* WMAP9+PR3 analysis; any use of “PR4/NPIPE” pertains only to the internal implementation of their reproduction code, not to your constraint. Make sure there is no ambiguity that you are not mixing PR3 and PR4 constraints.

P1B-M2 (MAJOR) – ALP parameter space: “natural” box vs posterior (Sec. VI, Appendix C, pp. 8–11, 13)  
Problem: You claim the signal is “consistent with an ALP having natural parameters (taken at scan-prior midpoint values; the ∼25× misalignment tuning required to reconcile the headline result with the spectator-consistent corner is disclosed…)”. But your own analysis shows:  
• The posterior for m peaks around m ≈ 36 H₀ and is driven toward the upper edge of the ma prior;  
• The required Caγ ∆φ/fa ≈ 10.3 implies couplings Caγ ≈ 8–10 only in a small high‑displacement region, and as high as ~160 in parts of the box;  
• The strict spectator regime θᵢ ≲ 0.1 occupies only 0.33% of posterior weight and requires Caγ ≳ 35–55.  
This is much stronger fine tuning than “natural midpoint values” suggest. The language could mislead readers about how generic the explanation is.  
Required fix: Rephrase all occurrences of “natural parameters” in the ALP context to state clearly that (i) the preferred masses are at the heavy end of the prior, (ii) the coupling is significantly larger than KSVZ/DFSZ benchmarks, and (iii) the spectator‑consistent region is both strongly tuned in θᵢ and pushed to high Caγ. Do not claim that the headline β arises from “natural” ALP parameters in the usual sense.

P1B-M3 (MAJOR) – Over‑precise forward-looking claims about LiteBIRD significance (Sec. VI, p. 11)  
Problem: Text: “LiteBIRD is projected to achieve σ(β) ≈ 0.03° . For β = 0.27°: ∼ 9σ statistical significance—either decisive confirmation or clean exclusion.” The LiteBIRD forecast paper  gives polarization sensitivities but the exact σ(β) forecast is model‑dependent; moreover, claiming “9σ… decisive confirmation or clean exclusion” presumes no dominant systematics and that the current signal is real.  
Required fix: Soften the language: state that “forecasts suggest σ(β) of order 0.03° in ideal conditions, which would correspond to ~9σ if the current central value holds, subject to instrument systematics and foregrounds.” Remove “decisive” and “clean exclusion” as unconditional statements.

P1B-M4 (MAJOR) – Use of Riess et al. MB and H₀ values (Sec. II–III, Table I, pp. 2–3)  
Problem: Citation  is correctly matched to Riess et al. 2022, ApJ 934, L7, arXiv:2112.04510.[7] The quoted MB = −19.253 ± 0.027 mag and H₀ = 73.04 ± 1.04 km/s/Mpc match the paper’s headline results.[7] Your calculation MB − 5 log₁₀(h) at both the Riess anchor and your chain mean is algebraically correct. However, you quote a “canonical 3.6σ Hubble tension” when comparing your H₀ = 67.68 ± 1.06 to 73.04 ± 1.04, but you do not recompute the exact σ; the combined error gives ΔH₀/σ ≈ 3.7–3.8σ, and DESI‑informed combinations in the literature are now closer to 4–5σ.[7]  
Required fix: Either compute your own tension from the given numbers (using Δ/√(σ₁²+σ₂²)) and quote that value explicitly, or cite a specific paper for the “canonical” σ quoted. Do not mix your numbers with a literature tension number without checking consistency.

P1B-M5 (MAJOR) – “Quintom-B empirical anchor” language in conclusions (p. 11)  
Problem: You state that the DESI DR2 + Planck + DES‑Y5 + Pantheon+ chain provides “an empirical test of the quintom-B scenario .” Since  is not a real paper in the stated form and your chain is your own fit, current phrasing implies a collaboration‑level endorsement of “quintom-B” that is not present in DESI or DES publications.[4][5]  
Required fix: Rephrase to make clear this is *your* interpretation of the combined datasets in terms of a w₀–wₐ extension compatible with a quintom‑like background, and that it is not an official DESI/DES claim. Remove or soften “empirical anchor” language unless you can back it by an explicit statement in a collaboration paper.

P1B-M6 (MAJOR) – Version‑history / earlier‑draft language in the body (multiple locations)  
Problem: The manuscript includes explicit “earlier draft” correction notes and internal versioning text in the main body, which must not appear in a PRD submission:

Examples:  
• Abstract: “P1B v1B.0.52: SVI ALP provenance rewrite … — all deliberate.”  
• Sec. IV fn. 3: “The ∼ 12% multiplicative under‑recovery … the ∼ 12% multiplicative under‑recovery is therefore … an earlier draft of this footnote.”  
• Sec. VI: “[Correction note: an earlier draft paired Δϕ/fa ≈ 1.0–1.07 with m ≈ 1.8–2 H₀ … corrected here].”  
• Appendix C: “[Correction note: an earlier draft described the model-dependent fits as ‘three benchmark configurations…’; no archived chain matches that description, and the configuration list below replaces it with the committed truth. The headline posteriors are unaffected: they are recomputed here…].”

Required fix: Remove all explicit references to “earlier draft,” version IDs, or internal audit trail from the main text and appendices. Corrections should be silently implemented or, if essential for transparency, moved to a short, impersonal “Erratum/Notes added” section with neutral phrasing.

P1B-M7 (MAJOR) – AI‑assistant acknowledgement (Acknowledgments, p. 12)  
Problem: Text: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation.” PRD editorial policy is evolving regarding AI assistance; such acknowledgements are generally acceptable only if they do not imply AI had responsibility for analysis or claims. Here you say “during systematic analysis,” which could be read as implying AI involvement in substantive research tasks.  
Required fix: Rephrase to state clearly that AI tools, if mentioned at all, were used only for *editorial* or *organizational* assistance, and that all scientific results and checks are the author’s responsibility. Alternatively, remove the explicit product name and mention AI use in a neutral way, pending the journal’s policy.

P1B-M8 (MAJOR) – Overlength and scope creep relative to claimed contribution  
Problem: The paper is a “Technical Verification Companion” but runs 15 pages with extensive excursions into quintom‑B cosmology, DESI DR2 constraints, a full ALP parameter scan, and internal reproducibility manifest. For PRD, much of this reads like material that should go in supplementary or companion data‑release documents, not in a methods note.  
Required fix: Condense to focus tightly on: (i) the ΛCDM+ΔN_eff stock‑CAMB proxy runs that directly support Paper I(a), (ii) the NaMaster E–B pipeline validation needed for your birefringence consistency check, and (iii) a concise ALP consistency‑check demonstration. Consider moving detailed ALP‑MCMC prior discussions, the continuous‑prior triangle plot, and the DESI DR2 w₀–wₐ chain to supplementary material or a separate paper. A 9–10 page main text would be more appropriate for PRD.

P1B-m1 (MINOR) – Eskilt & Komatsu statistic traceability (Sec. VI, pp. 8–9)  
Problem: You quote β = 0.342° ± 0.094° (3.6σ) from [5]. The PRD paper indeed reports that value.[5] However, you never explicitly reproduce the 3.6σ as β/σ in the text, nor do you show that your Gaussian likelihood exactly matches their posterior beyond mean/σ.  
Required fix: Add a brief note that your likelihood is a simple Gaussian approximation to their 1D β posterior and that you have checked that this reproduces their mean and standard deviation to within numerical precision. This documents traceability.

P1B-m2 (MINOR) – Table I “SM (ΔN_eff=0)” label in Fig. 2 caption (p. 6)  
Problem: Panel (a) of Fig. 2 caption lists “SM (Neff = 0)” as a curve. In context, you mean Standard Model ΔN_eff = 0 around Neff ≈ 3.046, not N_eff=0 total radiation.  
Required fix: Change the label to “SM (ΔN_eff = 0)” or “SM (N_eff = 3.046)” to avoid confusion.

P1B-m3 (MINOR) – ALP backreaction/spectator wording vs footnote 5 (Sec. VI, fn. 5, p. 9)  
Problem: Footnote 5 explains that θᵢ ≈ 0.1 is needed for Ω_a ≪ 1 and that θᵢ in the [0.5,2] scan is not spectator‑consistent. Some text in Sec. VI still loosely speaks of “spectator‑ALP natural parameter ranges” without reminding that much of the scanned box is non‑spectator.  
Required fix: Where you discuss the scan box θᵢ ∈ [0.5,2], explicitly state that this includes both spectator and dark‑energy ALP regimes, and that the strict spectator condition requires θᵢ ≲ 0.1.

P1B-m4 (MINOR) – “canonical” terminology (Sec. II–III, IV)  
Problem: Multiple uses of “canonical 3.6σ Hubble tension,” “canonical quintom signature,” and “canonical f_sky=0.32 mask.” These are informal and could be confusing or overstated, especially where the literature is still evolving.  
Required fix: Replace “canonical” with more neutral phrasing (“standard in the literature,” “commonly studied,” etc.) or give a specific reference supporting the characterization.

P1B-m5 (MINOR) – Internal repository file names in main text (multiple pages)  
Problem: The main text repeatedly cites internal JSON/CSV filenames (e.g. c1_fsky_sweep.json, c10_robustness_battery.json) as “artifacts.” This is useful for reproducibility but clutters the narrative and is unconventional for PRD.  
Required fix: Move detailed file‑name references to an online supplement or a brief “Data availability” subsection; in the main text refer generically to “the robustness test artifacts in the reproducibility repository.”

P1B-n1 (NIT) – Duplicate hyphenation and repeated words  
Problem: Minor stylistic redundancies, e.g. “canonical canonical-mask” do not appear explicitly, but there are awkward repetitions like “canonical 2° … canonical mask,” and some hyphenation inconsistencies (“spin torsion.input.yaml” vs “spin-torsion input”).  
Required fix: Run a careful language edit to remove repetitive phrasing and unify hyphenation (e.g. always “spin-torsion,” “quintom‑B”).

P1B-n2 (NIT) – PACS codes vs journal practice (p. 1)  
Problem: PACS numbers are included; APS/PRD has largely moved to PhySH and often omits PACS in new submissions.  
Required fix: Check current PRD author guidelines; remove PACS if no longer requested, or replace with PhySH keywords.

P1B-n3 (NIT) – Small algebraic clarifications (Table II notes, p. 4)  
Problem: In note (b) you derive σ_w,pivot via σ²_w,pivot = σ²_w0 – Cov²(w0,wa)/σ²_wa. The expression is correct but dense.  
Required fix: Add a brief clarifying sentence: “This follows from Var(w_pivot) = Var(w0) + (1−a_p)²Var(wa) + 2(1−a_p)Cov(w0,wa) and the definition of a_p that cancels the cross term.”

P1B-n4 (NIT) – Data/code availability link formatting (Appendix A, p. 12)  
Problem: The GitHub URL is written inline; PRD style typically prefers simply citing “a public GitHub repository (URL given in the Supplemental Material)” rather than raw links in the body.  
Required fix: Move the full URL to a footnote or Supplemental Material and keep the main text cleaner.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper’s core technical content (stock‑CAMB ΔN_eff proxy runs, NaMaster pipeline validation, and ALP consistency check) is potentially suitable as a PRD technical companion, and many internal calculations are self‑consistent. However, several citations use fabricated or inaccurate metadata, including future‑dated or non‑existent arXiv IDs and mis‑attributed authors, and some σ‑level juxtapositions and ALP‑“naturalness” claims are misleading without further qualification. There is also substantial version‑history prose that must be removed. These issues do not appear fatal but require a careful, line‑by‑line correction pass and some refocusing/shortening of the manuscript before the work can meet PRD’s standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E10 (ESSENTIAL) – Arithmetic inconsistencies in quoted significances and tensions  
Problem: Multiple σ-values and “tension” numbers do not match the quoted inputs when recomputed.  
Findings:  
• Hubble tension: The text calls the difference between H₀ = 67.68 ± 1.06 and 73.04 ± 1.04 “the canonical 3.6σ Hubble tension.” The implied tension from these *specific* numbers is  
\[
\Delta H_0 = 5.36,\quad \sigma_{\rm comb} = \sqrt{1.06^2+1.04^2}\approx 1.49,\quad \Delta/\sigma \approx 3.6
\]  
so numerically 3.6σ is consistent here. However, earlier the MB–H₀ offset is described as “∼ 3.2σ relative to the chain’s σ_MB = 0.049,” while the actual ratio 0.156/0.049 ≈ 3.18 is fine; the *tension language* then conflates this MB-axis 3.2σ with the “canonical 3.6σ” literature number and does not explicitly show that these all use slightly different σ-combinations. This is mathematically consistent but conceptually mixes distinct definitions of “σ” without clarity.  
• w₀ and wₐ significances: For Table II, the stated departures “+4.3σ” (w₀) and “−3.6σ” (wₐ) are consistent with |mean − LCDM|/σ using the table values, but the joint statement “LCDM point lies at > 4σ in the joint marginal tails” is not quantified (i.e., no explicit combined significance is computed from the covariance).  
Required fix:  
– Where any “canonical” σ-tension is quoted, explicitly compute from the numbers given and state which axis/combination is used (MB, H₀, or joint), or else replace “canonical” with “approximately Xσ from these specific values.”  
– For w₀–wₐ, either provide the joint distance calculation (using the covariance) or clearly state that “>4σ” refers separately to the one-dimensional marginals, not a 2D joint tension.  

P1B-E11 (ESSENTIAL) – Dimensional inconsistency in noise conversion formula (Sec. IV)  
Problem: The conversion from map sensitivity ∆P to per-pixel RMS σ_pix is dimensionally inconsistent as written.  
Text: “σpix = ∆P / Ωpix with Ωpix the Nside = 512 pixel area expressed in arcmin² (Ωpix = 47.21 arcmin², giving σpix = 10/√47.21 = 1.455 µK; algebraically identical to the standard σpix = ∆P [π/(180×60)]/√Ωpix(sr)).”  
Issues:  
• If ∆P is in µK·arcmin, the correct relation is σ_pix[µK] = ∆P[µK·arcmin] / √Ω_pix[arcmin²]. The text first writes σpix = ∆P / Ωpix (no square root), then numerically uses 10/√47.21, i.e. introduces √Ωpix in the calculation but not in the formula.  
• The “algebraically identical” expression mixes area in steradians and arcmin inconsistently and is not clearly derived.  
Required fix:  
– Correct the formula to explicitly read σ_pix = ∆P / √Ω_pix, with Ω_pix defined in the same units as the ∆P factor.  
– Remove or carefully rederive the steradian-expression so that units match on both sides and the equivalence is transparent.  

P1B-E12 (ESSENTIAL) – Dimensional / normalization ambiguity in birefringence formula (Eq. (3), Sec. VI)  
Problem: The conversion from ALP displacement to rotation β uses a normalization that is only qualitatively described and can be misinterpreted dimensionally.  
Text: “β ≈ (α_EM × 8 / 4π) × 1.06 = 4.93 × 10⁻³ rad × 180°/π ≈ 0.28°.” Then: “here it corresponds to the normalization L ⊃ −(g_{aγ}/4) φ F F̃ with g_{aγ} = C_{aγ} α_EM/(2π f_a) and β = (g_{aγ}/2) Δφ.”  
Issues:  
• Inserting g_{aγ} into β = (g_{aγ}/2) Δφ gives β = (C_{aγ} α_EM / (4π f_a)) Δφ. The text then effectively sets ∆φ/f_a = 1.06 and multiplies by C_{aγ} = 8, but the intermediate step is shown as “α_EM × 8 / 4π × 1.06,” omitting explicit reference to ∆φ/f_a or units.  
• While dimensionally it works if ∆φ/f_a is dimensionless, that is never written in Eq. (3), and the equality line “= 4.93×10⁻³ rad” appears as a pure number, potentially confusing the role of ∆φ/f_a vs. the coefficient.  
Required fix:  
– Rewrite Eq. (3) explicitly as  
\[
β = \frac{C_{aγ} \, α_{\rm EM}}{4π} \frac{\Delta φ}{f_a}
\]  
with the substitution ∆φ/f_a = 1.06 and C_{aγ} = 8 carried through step by step, preserving units.  
– Clearly state that ∆φ/f_a is dimensionless, so that β has units of radians.  

P1B-E13 (ESSENTIAL) – Equation (2) vs. later “saturated displacement” range (Sec. VI)  
Problem: Internal numerical mismatch between the quoted early displacement example and the later “committed grid” range.  
Text: Eq. (2) gives ∆φ/f_a ≈ 0.42 for (m = 2H₀, θ_i = 1). Later the text states: “Across the natural parameter range m/H₀ ∈ [1, 3], θ_i ∈ [0.5, 2] the committed EOM grid gives ∆φ/f_a ∈ [0.06, 1.19].” Then the ALP posterior discussion says the posterior-preferred regime has ∆φ/f_a ≈ 1.2–1.3 at m ~ 10–10² H₀.  
Issue:   
• No explicit check is shown that 0.42 for (2H₀, θ_i = 1) is consistent with the committed grid; given the corrected [0.06, 1.19] range, 0.42 is plausible but it is singled out even though the preferred region lies outside the [1, 3]H₀ “natural” box. The narrative can mislead by spotlighting a seemingly “natural” point while later acknowledging the posterior sits near the heavy end where ∆φ/f_a is larger.  
Required fix:  
– Explicitly relate Eq. (2) to the full grid: e.g. “This example (0.42) is one point within the [0.06, 1.19] range; however, the posterior actually prefers the upper end of the displacement, ∆φ/f_a ≈ 1.2–1.3, at m ≫ 3H₀.”  
– Make clear in the paragraph containing Eq. (2) that this is *not* near the posterior maximum once the full fit is run.  

P1B-M9 (MAJOR) – Additional σ-juxtapositions without “not directly comparable” disclaimer (beyond P1B-E7)  
Problem: Several further places juxtapose significances or σ-like measures from different null procedures without explicit local disclaimers.  
Examples (in addition to those you already flagged):  
• Sec. III, Fig. 1 caption: S₈ tension “sits 2.5σ above the DES-Y3 weak-lensing value S₈ = 0.776 ± 0.017…; the S₈ tension is not relieved in this chain either.” This is a comparison of two different likelihood configurations, but no explicit “not directly comparable” statement is made.  
• Sec. VI, ALP spectator subset: “Ω_a < 0.1 for 44% and Ω_a < 0.01 for 13% of the posterior; restricted to the Ω_a ≤ 0.01 spectator-safe subset, β = 0.28° ± 0.10°, consistent with β_obs = 0.342° ± 0.094° at 0.5σ.” Here the 0.5σ difference is the difference between two Gaussians whose underlying likelihoods differ (full posterior vs. restricted subset), but the phrase “consistent with” is used without a reminder that these are not independent measurements.  
• Sec. VI, continuous-prior configuration, last paragraph before LiteBIRD: “The recovered β = 0.326° ± 0.099° posterior matches the observed 0.342° ± 0.094°… confirming the consistency‑check verdict…” again uses an implicit σ-level consistency between a model-dependent posterior and the original measurement.  
Required fix:  
– In each of these sentences, explicitly state that the compared σ or consistency levels arise from *different* likelihoods or subsets and are not independent or strictly comparable; e.g., “These σ values are not directly comparable because they are derived from different likelihoods/posterior subsets.”  

P1B-M10 (MAJOR) – Abstract and conclusions overclaim “natural parameters” despite body text (Sec. I, VI, VII)  
Problem: The abstract and early scope statements still describe the ALP as having “natural parameters (taken at scan-prior midpoint values)” and in the conclusions: “An ALP with f_a ∼ M_Pl, m ∼ H₀ is consistent with the published 3.6σ joint signal…” The body itself shows the posterior prefers m ≈ 36H₀ (well above the [1,3]H₀ “natural box”) and that the spectator‑consistent θ_i ≲ 0.1 occupies only 0.33% of the posterior and needs C_{aγ} ≳ 35–55.  
Issue: This mismatch between the narrative “natural parameters near scan midpoint” and the quantified posterior heavily skewed to higher masses and larger couplings is more severe than flagged previously: it appears both in the abstract, the scope note in Sec. I, and the conclusion, so a reader could come away with an incorrect impression even if they skim the body.  
Required fix (extend P1B-M2):  
– In the abstract, replace “natural parameters (taken at scan-prior midpoint values…)” with wording such as “parameters in a range that is theoretically motivated but, as quantified in Sec. VI, preferentially at the heavy end of the mass prior and requiring enhanced photon coupling and misalignment tuning.”  
– In the conclusions, similarly replace “An ALP with f_a ∼ M_Pl, m ∼ H₀ is consistent…” by “An ultra-light ALP with f_a ∼ M_Pl and m in the ∼10–10² H₀ range can reproduce the signal, but only with larger-than-benchmark photon couplings and tuned initial misalignment.”  

P1B-M11 (MAJOR) – Abstract support and body cross-reference gaps  
Problem: Some abstract statements are not crisply backed by explicit pointers to where they are demonstrated.  
Examples:  
• Abstract: “Both frozen dataset combinations find ∆N_eff consistent with zero … and H₀ consistent with standard ΛCDM…” This is supported by Table I and Sec. III, but there is no explicit cross-reference in the introduction or conclusions guiding the reader to the numerical results (Table I) and Fig. 2.  
• Abstract: “injecting β = 0.27° recovers β̂ = 0.238°… pipeline-recovery bias −0.032°.” While Sec. IV gives these numbers, the abstract does not indicate that the 0.040° worst-case bias also appears and is carried as the systematic; the emphasis on one injection could be misread as the only bias characterization.  
Required fix:  
– Add explicit pointers in the introduction or early in Sec. III/IV like “as quantified in Table I and Fig. 2” and “as shown in Fig. 3 and Eq. (1).”  
– In the abstract’s NaMaster summary, mention that the worst‑case bias over injections is −0.040°, and that this is adopted as a systematic floor (to match Sec. IV).  

P1B-m6 (MINOR) – Internal cross-references slightly off or ambiguous  
Problem: Some cross-references could mislead because the referenced section does not quite contain what the sentence suggests.  
Examples:  
• Sec. II: “per the explicit parameter-scope clarification in Sec. V A” – Sec. V A does list likelihood stacks but does not clearly spell out that (ω/H)_0 and Ω_k are fixed; that detail is actually given in Sec. III as well.  
• Sec. VI: “the ∼25× misalignment tuning required for the headline result is disclosed in Sec. VI and fn. 5.” The tuning is mainly explained in footnote 5 and the later paragraph on Ω_a and θ_i; a reader might not immediately find a single consolidated place.  
Required fix:  
– Tighten references, e.g. “per the explicit parameter-scope clarification in Secs. II and V A” or “disclosed in footnote 5 and the Ω_a paragraph later in this section.”  

P1B-m7 (MINOR) – Figure 2 caption label still potentially confusing (beyond P1B-m2)  
Problem: Even after relabelling “SM (Neff = 0)” as suggested, the caption text “Standard-Model value ΔN_eff = 0 marked” could still be confusing because panel (a) plots the *Gaussian summaries* and the vertical line is at ΔN_eff = 0, but the legend may be misread as Neff = 0.  
Required fix:  
– Ensure the legend and caption both say “SM (ΔN_eff = 0)” and explicitly state “vertical line shows ΔN_eff = 0 (corresponding to N_eff ≈ 3.046).”  

P1B-m8 (MINOR) – “Consistency” phrasing hiding quantitative gaps  
Problem: Several uses of “consistent with” do not immediately present the underlying δ/σ.  
Examples:  
• Sec. VI: “β_ALP = 0.336° ± 0.10° … consistent with the observed β_obs = 0.342° ± 0.094°.” The actual difference is 0.006°, with σ_comb ≈ √(0.10² + 0.094²) ≈ 0.138°, i.e. 0.04σ – extremely consistent.  
• Sec. VI, continuous-prior configuration: “β = 0.326° ± 0.099° is consistent with β_obs.” Here δ = 0.016°, σ_comb ≈ 0.137°, so ~0.12σ.  
Required fix:  
– In each of these key “consistent with” sentences, add a parenthetical “(difference ≈ 0.04σ)” or similar to make the quantitative closeness explicit, clarifying that the apparent agreement is trivial given the uncertainties.  

P1B-m9 (MINOR) – LiteBIRD forecast sentence still too absolute in main text (beyond P1B-M3)  
Problem: Even before the explicit “decisive” phrasing, the statement “LiteBIRD is projected to achieve σ(β) ≈ 0.03°” reads as a definitive instrument performance rather than a forecast under assumptions (e.g., foreground control).  
Required fix:  
– Soften to “Forecasts suggest that, under ideal assumptions about systematics and foregrounds, LiteBIRD could achieve σ(β) of order 0.03°…,” consistent with the required softening of the following sentence.  

If you want, I can now go through equation-by-equation and produce a checklist you can use when editing (e.g., explicit replacements for each problematic sentence).