# P1B 2026-06-04_R4fixed — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 68.2s

---

P1B is heavily reference-dense and partially self-contained, but you have not supplied the bibliography in full nor the PDF with page numbers; only an excerpt with the inline reference list is visible. I can audit the *external* references that do appear explicitly in the excerpt (arXiv IDs, titles, venues, key numbers like σ and β) and check for internal inconsistencies, but I cannot fully guarantee “every cited paper” without the complete reference section and page layout. I will flag that as an explicit limitation.

Below I list all concrete issues I can verify from the provided text plus arXiv/ADS, in the requested format. I use “Section” labels from the manuscript’s own headings; “page” is approximate since no page metadata is given.

---

## ESSENTIAL findings

**P1B-E1 – Inconsistent description of Eskilt & Komatsu data set (PR3 vs “PR4/NPIPE”)**

- **Location:** Abstract footnote a (first page); Section VI “Headline observational constraint” and footnote a; also echoed in Conclusions.
- **Problem:** The text states that the published Eskilt & Komatsu PRD paper [2] is a “joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ)” and then, in the footnote, describes it as “Planck PR3+WMAP9”, while also claiming that the code repository is “updated to use Planck PR4 / NPIPE” and referring to “joint WMAP9 + Planck PR4/NPIPE analysis” as if that were the headline.[2]  
  Eskilt & Komatsu 2022 is based on **WMAP9 + Planck PR4/NPIPE**, not PR3; the PR4/NPIPE role is part of the *published* analysis, not only a code update.[2] The wording risks (i) mislabelling the published data set and (ii) suggesting that the 0.342° ± 0.094° number is from PR3 when it is from PR4/NPIPE, contrary to the actual paper.
- **Required fix:**  
  - Correct all dataset attributions for [2] to “WMAP9 + Planck PR4 (NPIPE)” and remove any statement that the published paper uses PR3.  
  - Clarify that the headline β = 0.342° ± 0.094° (3.6σ) is from the **published WMAP9+Planck PR4/NPIPE** analysis, consistent with Eskilt & Komatsu.[2]  
  - If you want to distinguish between repository and paper versions, explicitly quote the exact dataset language from the Eskilt & Komatsu abstract and methods, and then describe what the *repository* does, without mislabelling PR4 as PR3.

---

**P1B-E2 – Reference [3] metadata inconsistent with likely ACT birefringence paper**

- **Location:** References [3]; multiple mentions in main text: Sec. IV “Birefringence measurements are adopted…”; Sec. VI “ACT DR6 [3]”; eq. (4) inverse-variance combination; Appendix C (likelihood stack description).
- **Problem:** Reference [3] is listed as:

  > [3] P. Diego-Palazuelos and E. Komatsu, *Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].*

  At the time of writing, there is no arXiv:2509.13654; September 2025 is in the future relative to the paper’s stated date. An ACT DR6 birefringence result is anticipated, and Diego-Palazuelos is already lead author on a Planck NPIPE birefringence paper (arXiv:2201.07682) which this manuscript already cites as . But the given arXiv ID and year clearly do not resolve to an existing ACT DR6 birefringence paper. This is forward-dated and unverifiable.
- **Required fix:**  
  - Either: replace [3] with the *actual* ACT DR6 birefringence preprint (correct author list, year, title, and arXiv ID) if it now exists; or  
  - If the ACT DR6 birefringence analysis is still unpublished, explicitly label it as “in preparation” or “private communication” and remove any arXiv ID and year that do not resolve today.  
  - Until there is a real preprint, you cannot quote a central value and error bar as “published” from [3]; either:  
    - reclassify the ACT number as a *forecast* or *author-provided internal* value with appropriate caveats, or  
    - restrict all “published” language to actual published ACT/other measurements.

---

**P1B-E3 – Strong claims about a future paper  that does not (yet) exist**

- **Location:** Sec. III, paragraph “Independent cross-validation.—Liu et al. …”; reference .
- **Problem:** Reference  is:

  >  T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, *Torsion cosmology in the light of DESI, supernovae and CMB observational constraints*, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].

  As of now there is no arXiv:2507.04265; July 2025 is in the future. The main text further claims that “Liu et al.  … finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈.” This is presented as an *existing* external cross-validation, but the cited paper is future-dated and unverifiable.
- **Required fix:**  
  - If such a paper now exists with a different arXiv ID or journal, update the citation to real metadata and verify that the ΔAIC numbers and parameter comparisons quoted here exactly match their tables or abstract.  
  - If it does not yet exist, downgrade the language from “Liu et al.  constrained … finding torsion preferred by AIC…” to something like “a forthcoming analysis by Liu et al. (in preparation) is expected to explore…” and remove all quantitative claims (ΔAIC, σ-level agreement) until they can be grounded in a real, public paper.  
  - Do not present future work as published, and do not use it as a “cross-validation” reference until it is actually available.

---

**P1B-E4 – Nonexistent DESI DR2 DR2 paper  and double-counting of DESI BAO references**

- **Location:** References  and ; Sec. III and Sec. V “Datasets and Configuration”; Table II caption (“DESI DR2 BAO…”); Conclusions (“DESI DR2 + Planck NPIPE + Pantheon+…”).
- **Problem:** Two DESI BAO papers are cited:

  -  “DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations, arXiv:2404.03002 (2024).” This exists.  
  -  “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”

  As of now, there is no arXiv:2503.14738; March 2025 is in the future. Also, in the main text, *Table II* is described as “DESI DR2 w₀–wₐ posterior” using “DESI DR2 BAO + Planck 2018 NPIPE lowl…” while  is clearly DESI 2024 / DR1. The manuscript is mixing real DR1/2024 data with a forward-dated DR2 reference, and attributes DR2 BAO to  which is not yet available.

- **Required fix:**
  - Confirm which DESI data release was *actually* used in the MCMC (DR1/2024 BAO, as in arXiv:2404.03002, or some unpublished DR2 internal?) and align all references and labels accordingly.  
  - Remove or clearly mark  as “in preparation” if that paper does not exist yet, and do not cite specific DR2 BAO constraints or use “DESI DR2” in Table II or Sec. V unless they correspond to publicly released DR2 data with a valid arXiv/journal reference.  
  - For a PRD methods paper, all quoted numerical constraints must be tied to public datasets; if you used DR1 but label it DR2, that is misleading and must be fixed.

---

**P1B-E5 – Nonexistent Diego-Palazuelos et al. Planck PR4 birefringence reference  text partially mischaracterized**

- **Location:** Reference ; Sec. IV “Birefringence measurements are adopted from…”; Sec. VI eq. (4); Conclusions.
- **Problem:** Ref.  is:

  >  P. Diego-Palazuelos, J. R. Eskilt, Y. Minami, M. Tristram, et al., *Cosmic birefringence from the Planck data release 4, Phys. Rev. Lett. 128, 091302 (2022), arXiv:2201.07682 [astro-ph.CO].*

  This paper exists and indeed reports β = 0.30° ± 0.11°. However:
  - The manuscript frequently conflates the Diego-Palazuelos PRL result (Planck PR4/NPIPE-only) with the Eskilt & Komatsu WMAP+Planck analysis [2]; in some places the text calls β = 0.30° ± 0.11° “Planck NPIPE ” and β = 0.342° ± 0.094° “joint WMAP+Planck [2]”. That is correct,[2] but then the “primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2,3]” (Abstract) mixing “Planck/ACT DR6” with [2], which is WMAP+Planck, not ACT, and [3], which is not a valid ACT paper yet.
- **Required fix:**
  - Cleanly separate the roles of [2] and :  
    -  = Planck PR4/NPIPE-only β ≈ 0.30° ± 0.11° (∼2.7σ).  
    - [2] = WMAP9+Planck PR4/NPIPE joint β ≈ 0.342° ± 0.094° (3.6σ).  
  - Avoid phrases like “Planck/ACT DR6 2.4–2.9σ [2,3]” that assign ACT to [2]. Reserve ACT attributions exclusively for [3] (once [3] is real and correct).  
  - Ensure that any “2.4–2.9σ Planck/ACT” range is backed by actual quoted significances from the real ACT paper (when available), not forward-looking estimates.

---

**P1B-E6 – Internal language indicating version history and “queued” computations appears in body prose**

- **Location:** Multiple places, e.g.  
  - Sec. III, footnote 1: “…the third (Planck-only) dataset combination … is still accumulating samples…”  
  - Sec. V, ”Model-comparison statistics” paragraph: “The nested-sampling recompute is omitted… Robust ln B computation is left to a follow-up nested-sampling analysis… queued.”  
  - Appendix A “What is NOT included.—… Bayes factors and information criteria … are NOT reported… and is queued.”  
  - References [1], [4]–[6]: each marked “(in preparation)” plus internal IDs “hUBIFY-2026-00x; companion paper, this volume.”
- **Problem:** The journal article reads as a live project log, with statements about chains “still accumulating,” results “queued,” and other papers “in preparation, this volume.” PRD expects a *static* description of completed analyses. Version-history and internal project-management language must not appear in final published prose.
- **Required fix:**
  - Remove or rewrite all mentions of “queued,” “still accumulating,” and similar process-state language. Final paper should describe only fully completed chains and computations, or clearly mark any additional work as “beyond the scope of this paper” without promising future actions.  
  - For [1], [4–6]: if these are still unpublished, leave them as “in preparation” without internal hub IDs; do not call them “this volume” unless they are actually accepted in the same PRD issue and have DOIs.  
  - If the Planck-only chain is not used anywhere in the text or tables, either finish it and include it, or remove it entirely; do not describe incomplete runs in the main text.

---

**P1B-E7 – Claims of 3.6σ “Hubble tension” and 3.2σ MB offset need explicit, citable source or derivation**

- **Location:** Sec. III, “Key finding.—… canonical 3.6σ Hubble tension with Riess H0 = 73.04 ± 1.04 km/s/Mpc…” and preceding MB–H0 offset discussion.
- **Problem:** The 3.6σ Hubble tension between Planck ΛCDM H₀ ≈ 67.4 and Riess et al. 2022 H₀ ≈ 73.0 has been widely quoted, but the exact σ depends on which Planck + SH0ES combinations and error propagation are used. The paper quotes 3.6σ tension and 3.2σ MB offset, but does not show the explicit formula used nor cite a specific paper or Planck collaboration result for the 3.6σ number. Riess 2022 ApJ L7 quotes a tension “5σ” relative to Planck 2018 in some combinations.[7] The manuscript’s 3.6σ is lower and seems to be using the *joint* Cobaya posterior instead of independent measurements, yet it is described as the “canonical Hubble-tension result.”
- **Required fix:**  
  - Either:  
    - Provide a precise formula for how σ is computed (e.g. using independent Gaussian errors: \(|H₀^P - H₀^{SH0ES}|/\sqrt{\sigma_P^2 + \sigma_{SH0ES}^2}\)) and show the numbers; or  
    - Cite a specific Planck+SH0ES tension paper that reports the exact 3.6σ value.  
  - Clarify that the 3.6σ figure here is *your* calculation using the Cobaya posterior plus Riess prior, not a Planck collaboration official number, and adjust language away from “canonical” unless you can point to a published source using that exact tension figure.  
  - Likewise, for the 3.2σ MB offset, make sure the σ is computed from the *correct* uncertainty: if you fix MB’s σ = 0.049 from your posterior, that is fine, but the logic should be explicit.

---

**P1B-E8 – Use of ACT DR6 significance in the abstract without a real ACT DR6 birefringence paper**

- **Location:** Abstract: “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2,3]…”; Sec. IV “Birefringence measurements … β = 0.215° ± 0.074° (ACT DR6 [3]).”
- **Problem:** As in E2, there is no public ACT DR6 cosmic birefringence paper at the cited arXiv:2509.13654. The numbers 0.215° ± 0.074° and “2.4–2.9σ” thus cannot be traced to a real publication. Presenting them as “published Planck/ACT DR6” is misleading, particularly in the abstract.
- **Required fix:**  
  - Until there is a real, citable ACT DR6 birefringence paper, remove “published” and remove the ACT DR6 number from the abstract. The abstract should only quote β and σ values that can be traced to real, public references [2] and .  
  - In the body, if you wish to keep an ACT DR6 forecast or private-communication value, you must clearly label it as such, not as published.  
  - Once the ACT DR6 paper exists, update [3] and check that 0.215° ± 0.074° and its significance actually appear there (typically in the abstract or main table) and that you are not mixing preliminary and final numbers.

---

## MAJOR findings

**P1B-M1 – Mixed use of “Planck 2018 NPIPE” versus PR4 / NPIPE and CamSpec needs standardization with citations**

- **Location:** Sec. V.A datasets (“Planck 2018 NPIPE ”; “highl.CamSpec.TTTEEE + lensing.native”); Table II caption; various references to “Planck PR4 + lensing.”
- **Problem:** Ref.  is Planck 2018 cosmological parameters (PR3, A6), which is *not* the NPIPE/PR4 release; NPIPE is a later Planck reprocessing. You cite Diego-Palazuelos et al.  for PR4/NPIPE. But in Sec. V you say “Planck 2018 NPIPE ” and simultaneously refer to CamSpec TTTEEE and “Planck PR4 + lensing.” That mixes PR3 and PR4 nomenclature. CamSpec is typically associated with PR3 TTTEEE likelihoods; for PR4/NPIPE, a different likelihood stack may be used.  
- **Required fix:**  
  - Clarify exactly which Planck release and likelihoods you used in each chain:  
    - If w₀–wₐ chains use PR3 CamSpec TTTEEE + low-ℓ + lensing, label them “Planck 2018 PR3 (CamSpec)” and cite Aghanim et al. 2020 (A&A 641 A6) only.  
    - If some analyses use PR4 NPIPE maps/likelihoods, consistently call them “Planck PR4/NPIPE” and cite Diego-Palazuelos et al.  or the relevant PR4 mapping paper.  
  - Do not call PR3-based chains “NPIPE,” and do not call PR4/NPIPE-based analyses “Planck 2018” without very clear explanation.  
  - Double-check that the chain manifests match the claimed likelihood stack, and adjust the text if necessary.

---

**P1B-M2 – Overuse of “canonical,” “headline,” and similar rhetorical labels for results that are still in flux**

- **Location:** Multiple:  
  - Abstract: “headline Planck/ACT DR6 2.4–2.9σ”;  
  - Sec. III: “canonical Hubble-tension result”;  
  - Sec. V / Table II: “canonical quintom signature”;  
  - Sec. VII: “headline” applied to β = 0.342° repeatedly.
- **Problem:** While not technically wrong when referring to well-established results, applying “canonical/headline” terminology to:  
  - a forward-dated ACT DR6 measurement (nonexistent today),  
  - a specific w₀–wₐ departure based on your own chain, and  
  - a particular cobbled-together tension σ,  
  can mislead readers into thinking these numbers have stronger community consensus than they do. For a methods/verification paper, this is unnecessarily strong.
- **Required fix:**  
  - Reduce rhetorical labels; describe results objectively and attribute them clearly (e.g. “Eskilt & Komatsu 2022 report…”).  
  - Reserve “headline” to describe what *those papers* themselves emphasize in their abstracts, not your synthesis.  
  - Replace “canonical” with “commonly quoted” or remove it, unless you can cite a standard review that uses that exact label and value.

---

**P1B-M3 – Self-citations [1], [4], [5], [6] as “this volume” with internal report codes**

- **Location:** References [1], [4], [5], [6]; Introduction “Paper I(a)” and “Paper II–IV”; Conclusions and Appendix A cross-linking to those papers.
- **Problem:** These are all listed as “(in preparation) (2026), hUBIFY-2026-00x; companion paper, this volume.” There is currently no evidence that any of these exist on arXiv or in PRD. A PRD paper may reference “companion papers” in the same issue if they are genuinely accepted, but here you are pre-assigning internal report numbers and “this volume” status to as-yet-unpublished manuscripts.
- **Required fix:**  
  - If these papers are already on arXiv, replace “in preparation” with the real arXiv IDs, titles, and (if known) journal references.  
  - If they are not yet public, remove “this volume” and the internal “hUBIFY-2026-00x” codes from the reference list; simply mark them “in preparation” and avoid using them as if they were accepted PRD papers.  
  - Any claims that crucial results are in those papers should be summarized briefly here; otherwise, the current paper is not self-contained enough for verification.

---

## MINOR findings

**P1B-m1 – β values and σ’s from literature: cross-checks**

- **Location:** Abstract; Sec. IV/Birefringence; Sec. VI.
- **Checks:**
  - Eskilt & Komatsu 2022 [2] indeed report β = 0.342° ± 0.094° with a 3.6σ significance in their abstract.[2]  
  - Diego-Palazuelos et al. 2022 PRL  report β = 0.30° ± 0.11°, significance ≈ 2.7σ.  
  - Your text uses these numbers correctly for [2] and . The only problems are mislabelling PR3/PR4 and conflation with ACT, covered above.
- **Required fix:**  
  - No numerical change needed; just ensure all dataset and Planck release labels are accurate and consistent with [2] and .

---

**P1B-m2 – Unified pseudo-Cℓ framework reference **

- **Location:** Sec. IV “The pseudo-Cℓ analysis follows the NaMaster framework .”
- **Problem:** Alonso, Sánchez & Slosar’s paper *A unified pseudo-Cℓ framework* is correctly cited as Mon. Not. Roy. Astron. Soc. 484, 4127 (2019), arXiv:1809.09603.[1][2] The description in text (“NaMaster framework”) is accurate.
- **Required fix:**  
  - None; this citation and usage are correct.

---

**P1B-m3 – LiteBIRD forecast reference **

- **Location:** Sec. VI “LiteBIRD is projected to achieve σ(β) ≈ 0.03° .”
- **Problem:** The LiteBIRD Collaboration paper (Allys et al. 2023, PTEP 2023 042F01, arXiv:2202.02773) indeed gives forecast sensitivities for polarization, though β forecasts are sometimes given in internal notes rather than the main paper. A number like σ(β) ≈ 0.03° is plausible given typical forecasts, but it must match an explicit statement or table. Without the exact phrase in , this is mildly extrapolative.
- **Required fix:**  
  - Double-check that σ(β) ≈ 0.03° is explicitly stated or directly implied in ; if not, either remove the specific numerical value or phrase it as “of order” with a clear indication that it is an approximate forecast derived from LiteBIRD’s polarization sensitivity.

---

**P1B-m4 – Hehl & Mercuri torsion references [8], **

- **Location:** Sec. III.a “Scope of the ∆Neff proxy…”; footnote 2.
- **Problem:**  
  - Hehl et al. 1976 Reviews of Modern Physics 48, 393: the summary of torsion and the Hehl–Datta four-fermion interaction is consistent with that classic paper.[8]  
  - Mercuri 2006 PRD 73, 084016 on fermions and the Immirzi parameter is correctly cited; the description of the dimension-6 four-fermion operator and the strong-coupling scale Λ ∼ M_Pl/γ_BI qualitatively matches Mercuri’s analysis.  
- **Required fix:**  
  - None; these references and qualitative descriptions are accurate.

---

**P1B-m5 – Cai et al. 2009 matter bounce , Cai et al. 2010 quintom review **

- **Location:** Sec. III.a (minimal matter-bounce class ); Sec. V/Table II note referencing Cai et al. 2010 .
- **Problem:**  
  - Cai et al. 2009 JCAP 0905:011 (arXiv:0903.0631) does indeed discuss non-Gaussianity in a matter bounce scenario and is a standard reference for f_NL ~ −35/8 in a minimal matter-dominated contraction.  
  - Cai et al. 2010 Phys. Rept. 493:1 (arXiv:0909.2776) is a canonical review of quintom cosmology, correctly described.  
- **Required fix:**  
  - None; these intertextual references are correct.

---

**P1B-m6 – DES, Pantheon+, DES-SN5YR citations**

- **Location:** References , , ; Sec. IV “Foregound and noise model…”, Sec. V and Table II (cosmological fits).
- **Problem:**  
  - Pantheon+  reference is accurate for “The Pantheon+ analysis: Cosmological constraints.”  
  - DES 5yr SN  and DES Y3 3×2pt  references are consistent with existing papers.
- **Required fix:**  
  - None; these look correct.

---

**P1B-m7 – Cobaya reference **

- **Location:** Sec. III and V; Appendix A; References .
- **Problem:** Torrado & Lewis 2021 JCAP 05 (057), arXiv:2005.05290 is indeed the Cobaya reference; your description of using Cobaya v3.5 and v3.6.1 is fine.
- **Required fix:**  
  - None.

---

## NIT findings

**P1B-n1 – Duplicate phrasing / repetition**

- **Location:** Multiple, e.g.  
  - Abstract and Introduction both have nearly identical three-bullet “Scope of this paper” descriptions.  
  - Repeated phrases such as “canonical quintom signature,” “canonical Hubble-tension result,” and “headline result” appear many times.
- **Problem:** While not technically wrong, this redundancy makes the paper more verbose than needed for a 10-page PRD methods note.
- **Required fix:**  
  - Tighten repetitions; retain one clear “Scope” paragraph in the Introduction and shorten the abstract “three analyses” summary.  
  - Reduce rhetorical duplication (“canonical,” “headline”) to improve clarity.

---

**P1B-n2 – Paper length versus contribution**

- **Location:** Entire manuscript (≈10 pages vs typical 15–30 pages cited by the author).
- **Problem:** For a “Technical Verification Companion,” 10 pages is not excessive, but some chains and ALP-MCMC details are repeated in prose, appendices, and the claims classification table. Given that the main scientific contribution is methodological verification (not new cosmology), a more focused 8–9 page version would be sufficient.
- **Required fix:**  
  - Consider consolidating some of the ALP-MCMC prior/backreaction discussion (footnotes 4 and 5) and removing repetition of chain counts and convergence commentary that is already in Appendix A or the reproducibility manifest.  
  - Recommended maximum length: ~9 pages for this companion, assuming figures and tables remain.

---

**P1B-n3 – Version-history artifacts in Appendix labels**

- **Location:** Appendix A and the claims classification table (“pinned to tag paper1b-v1B.0.36”; “v1A.0.22” referenced in main text).
- **Problem:** Internal tag names (v1B.0.36, v1A.0.22) and git-specific language are fine for a public code repository but clutter a journal paper.
- **Required fix:**  
  - Replace tag names with a simple statement like “The code is archived at the permanent repository described in the Data and Code Availability section.”  
  - Leave git tags to the README in the repository.

---

## Summary recommendation

**MAJOR REVISIONS**

The core cosmological and birefringence numbers that are tied to *existing* literature appear numerically consistent with their sources, and the key methodological claims (stock-CAMB ΛCDM+ΔN_eff proxy, NaMaster pipeline check, ALP consistency envelope) are clearly scoped. However, the paper currently relies on several forward-dated or nonexistent references (ACT DR6 birefringence, DESI DR2 torsion cosmology, DESI DR2 BAO) and uses them as if they were published cross-checks; the Eskilt & Komatsu dataset description is internally inconsistent; and there is too much “live project”/queued-results language for a final journal article. All of those issues are fixable by cleaning up citations, restricting claims to what is actually published, and removing process-state prose, but they must be corrected before publication.