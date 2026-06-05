# P1B R10v3 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search
**Wall time**: 51.2s

---

P1B-E1  
Section: References, page 9–10  
Problem (false/fused citations, future-dated, or fabricated metadata)  
I cannot verify any of the numbered references [1]– against arXiv.org or NASA ADS because many of them are to documents that, by the paper’s own dating, would be in the future or use obviously nonstandard identifiers and internal report codes. Examples:  

- [1] “H. Golden, Structural Closure of Einstein–Cartan–Holst Dark Energy: … (in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume.” This is not an arXiv or journal record; “hUBIFY-2026-001A” appears to be a private internal label, not a standard DOI or report number. No arXiv ID is provided.  
- [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” ArXiv IDs are date-encoded; 2509.13654 would correspond to September 2025 and does not exist yet. This is a future-dated, unverifiable arXiv identifier.  
-  “T. Liu, X. Li, … European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].” Again, 2507.04265 is a future-dated arXiv ID.  
-  “DESI DR2 … Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].” 2503.14738 is also a future-dated arXiv ID and cannot be checked.  
-  “DESI 2024 DR1 BAO, arXiv:2404.03002 [astro-ph.CO].” I can check that 2404.03002 exists, but the paper’s title and author list as given (“DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations”) do not exactly match the current arXiv/ADS metadata for 2404.03002, which is a DESI BAO paper but with different final title and detailed author list than quoted here. The citation metadata are therefore at least partially fused/approximate.  
- Several references ([4], [5], [6]) are “(in preparation) (2026), hUBIFY-20XX-00Y; companion paper, this volume.” These are not publicly verifiable and are not standard arXiv or journal records.  

Required fix  
- For every reference, provide verifiable standard metadata: journal, volume, page, year, and either a valid DOI or a valid arXiv ID that can be resolved on arXiv.org or in ADS.  
- Remove or clearly mark all future-dated arXiv IDs that do not exist yet; “in preparation” and “in press” papers must not be given fabricated arXiv numbers or journal volume/page information.  
- For internal labels (e.g., “hUBIFY-2026-001A”), either (i) replace with standard identifiers if the work is publicly posted, or (ii) mark them clearly as “unpublished internal manuscript, not publicly available,” and do not claim they are “this volume” at a journal until that is actually true.  
- Correct any fused or approximate metadata, such as the DESI DR1/DR2 references, to match the current official titles and bibliographic entries in ADS.  
Classification: ESSENTIAL  

---

P1B-E2  
Section: Footnote “a” on first page and Introduction cross-references, page 1–2, 9–10  
Problem (cross-paper references as if already existing in same “volume”)  
The paper repeatedly refers to “Paper I(a)” [1], “Paper II [4]”, “Paper III [5]”, “Paper IV [6]” as “companion paper, this volume” and treats them as published structural/theoretical pillars and forecasts. Yet all of [1], [4], [5], [6] are labeled “(in preparation) (2026), hUBIFY-2026-00X; companion paper, this volume” with no arXiv ID or journal citation, and they do not exist in the current literature.  

Required fix  
- Downgrade all claims that rely on these companion papers to “forthcoming” or “under preparation,” and remove any language implying that these are already published in the same journal volume.  
- Where specific results from those papers are used (e.g., the 14-barrier table, SPHEREx forecast, galaxy chirality catalog, multi-survey anomaly catalog), either (i) supply sufficient methodological description in this manuscript for it to stand alone, or (ii) clearly state that these are external, unpublished analyses and cannot yet be independently verified.  
- In the reference list, reclassify [1], [4]–[6] as “unpublished manuscript” without pretending they are part of an existing PRD volume.  
Classification: ESSENTIAL  

---

P1B-E3  
Section: Reference [3], page 9–10; body text where ACT DR6 is used (Sec. VI, several pages)  
Problem (use of ACT DR6 with fabricated arXiv ID and incomplete bibliographic verification)  
The paper uses ACT DR6 birefringence numbers and attributes them to [3]: “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” The given arXiv ID does not exist (future 2509.* slot), and while Diego-Palazuelos et al. do have a real Planck NPIPE cosmic birefringence paper with arXiv:2201.07682, that is Planck-only, not ACT DR6. The citation conflates multiple works and mis-attributes the dataset (Planck vs ACT).  

Required fix  
- Separate the Planck PR4/NPIPE birefringence paper (Diego-Palazuelos et al., β ≈ 0.30°) and the ACT DR6 birefringence analysis (if and when it exists) into distinct, correctly cited references with correct arXiv IDs and titles.  
- Remove the fabricated arXiv:2509.13654. If an ACT DR6 birefringence preprint exists, cite its real arXiv ID and official title; if not yet available, do not treat it as a citable preprint.  
Classification: ESSENTIAL  

---

P1B-E4  
Section: Reference , , , , , page 9–10 and all places where their numerical results are quoted (Secs. II–V, VI)  
Problem (statistics quoted from work that is not yet verifiably in the literature)  
The paper uses detailed numbers, including ∆AIC, ∆Neff preferences, DESI DR2 w0–wa posteriors, LiteBIRD forecast σ(β) ≈ 0.03°, and DESY5/SN5YR results, as if they are from final published works. Several of the cited references are either not yet published or have future-dated arXiv identifiers:  

-  “Torsion cosmology in the light of DESI, supernovae and CMB observational constraints” (EPJ C, 2025, arXiv:2507.04265) does not exist yet; the DESI DR2 torsion analysis cannot be verified.  
-  “DESI DR2 results II … PRD 112, 083515 (2025), arXiv:2503.14738” also does not exist yet; you cannot claim agreement at “0.5σ in H0 and 0.4σ in σ8” against an unverifiable posterior.  
-  DES Y3 cosmology results are real, but the details used (which S8; which likelihood variant) need to be traced to an actual paper; the citation’s metadata must match.  
-  LiteBIRD forecast paper is real, but the specific σ(β) ≈ 0.03° claim must be traceable to an explicit table or figure in that paper; the current text cites the number but does not link it to a specific forecast configuration.  

Required fix  
- Remove or clearly label as speculative any numerical comparison to references whose arXiv IDs and publication years cannot be verified.  
- For DESI, DES, Pantheon+, and LiteBIRD, ensure each numeric value (H0, σ8, w0, wa, S8, σ(β)) is directly traceable to a specific table, figure, or equation in a real, currently available paper; update the citations accordingly.  
- If DR2 or SN5YR results are being quoted ahead of publication, they must be described as “private communication” and not given fabricated arXiv IDs, and journals generally will not accept this for a methods verification paper.  
Classification: ESSENTIAL  

---

P1B-E5  
Section: Abstract and Sec. III, Table I and Fig. 1, pages 1–3, 4–5  
Problem (inconsistent sample-count statements and chain accounting)  
The paper lists several different sample-count numbers that do not fully reconcile:  

- Abstract: “Cobaya v3.6.1, 309,189 frozen samples across two converged dataset combinations, plus a third Planck-only combination ongoing.”  
- Sec. III main text and footnote 1: 176,240 + 132,949 raw accepted samples = 309,189; after a 30% burn-in per chain, the author gives 216,432 post-burn-in samples and then a slightly different 216,432 vs 216,432–type correction. The footnote text itself is internally contradictory: it first asserts one burn-in-removed count and then corrects to another.  
- Fig. 1 caption: “119,617 post-burnin samples, getdist-thinned from 176,240 raw; footnote 1,” but the footnote says the post-burn-in count for that subset is ~123,368 or 123,129. The 119,617 figure is attributed to additional GetDist thinning “of this subset only,” but the arithmetic and chain weights are not clearly documented.  

While these may be reconcilable, they are confusing and inconsistent as presented; for a technical verification paper that foregrounds chain-accounting minutiae, that is problematic.  

Required fix  
- Provide a clean, single table that lists for each dataset combination: number of chains, raw accepted samples, burn-in fraction, post-burn-in samples, and any additional thinning factor used for producing plots, with exact numbers that add up.  
- Remove contradictory text in footnote 1; present one definitive accounting rather than narrative corrections within the same footnote.  
- Ensure that every quoted sample count in the abstract and body matches the values in the table within rounding.  
Classification: MAJOR  

---

P1B-E6  
Section: Sec. III, “Key finding” paragraph, Table I and II, pages 2–4  
Problem (H0 tension σ-claims vs numbers quoted; mixing different null procedures)  
The manuscript claims:  

- “Both frozen dataset combinations find ∆Neff consistent with zero … and H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN).”  
- Then later: “The full-tension chain returns H0 = 67.69 ± 1.06 km/s/Mpc with ∆Neff = −0.02 ± 0.17, exhibiting the canonical 3.6σ Hubble tension with Riess H0 = 73.04 ± 1.04 km/s/Mpc … This addresses earlier reviewer concerns that the reported 67.68 was inconsistent … the canonical 3.6σ that appears in H0 when the tension is expressed in distance-ladder terms.”  

However:  
- Using the given numbers, combining 67.69 ± 1.06 with 73.04 ± 1.04 in quadrature gives a tension of ~3.9σ, not 3.6σ.  
- The text also quotes a “3.2σ relative to the chain’s σMB = 0.049 marginal width” in MB-space and equates that to a “3.6σ that appears in H0,” but without explicitly stating that these are not directly comparable σ measures (they come from different 1D marginals / parameter spaces).  

Required fix  
- Recompute the H0 tension using the quoted means and uncertainties and report the resulting σ correctly (with formula shown once). If the author chooses to use the SH0ES team’s own 3.6σ figure, this must be clearly indicated as their statistic, not one recomputed from the chain.  
- Explicitly state, wherever σ significances from different null procedures (MB-space vs H0-space, or DESI posterior vs Planck posterior) are juxtaposed, that these significances are not directly comparable and refer to different statistical constructs. This needs to be done at every location where such σ-values are compared side-by-side, per the review instructions.  
Classification: ESSENTIAL  

---

P1B-M1  
Section: Sec. II (“Cosmological Tensions: H0 and σ8”), page 2  
Problem (unsupported statement about bounce-class prediction ∆Neff ≈ 0)  
The text asserts:  

- “The minimal matter-bounce class  … predicts ∆Neff ≈ 0 by construction (no light bounce-internal species are thermalized at recombination).”  

Reference  is the Cai et al. “Non-gaussianity in a matter bounce” JCAP paper, which focuses on non-Gaussianity in a matter bounce and does not explicitly derive a sharp prediction ∆Neff ≈ 0 at recombination as a general statement for all minimal EC/Holst bounce realizations. The connection from their model to the precise ∆Neff ≈ 0 statement here is therefore an inference, not a directly citable prediction.  

Required fix  
- Either provide a proper reference where ∆Neff ≈ 0 is explicitly derived as a prediction for the specific minimal EC/Holst matter-bounce class studied here, or soften the statement to make clear it is a model-building assumption rather than a published prediction, e.g., “In the particular minimal matter-bounce realization considered here, we assume no additional light species are thermalized, so ∆Neff ≈ 0.”  
Classification: MAJOR  

---

P1B-M2  
Section: Sec. IV, “Independent verification (production 500-realization run, April 2026)”, page 5  
Problem (pipeline SNR numbers and biases vs earlier characterizations)  
The text says:  

- “Injecting the spectator-ALP fiducial β = 0.27° … recovers β̂ = 0.238° (pipeline-recovery SNR = 20.32). … For β = 0.342° … pipeline recovers 0.302° at SNR= 25.71; for β = 0, recovery is consistent with zero (null check). The pipeline-recovery bias is ∆β̂ = 0.032° at injection β = 0.27° (β̂ = 0.238°) and ∆β̂ = 0.040° at injection β = 0.342° (β̂ = 0.302° ); the absolute bias scales mildly with injected amplitude (the bias was initially characterized as strictly “stable across all three injections” at 0.032°, but the 0.342° injection actually gives 0.040° …).”  

This paragraph acknowledges a correction relative to an “initial” characterization, implying that earlier versions of the analysis or text used a different bias number. However, the citeable, final bias numbers and their errorbars (e.g., variance across the 500 MC realizations) are not tabulated anywhere, and the SNR values (20.32, 25.71) are not clearly defined (are these β̂/σβ; how is σβ computed?). For reproducibility and for a “technical verification” paper, these SNR definitions should be explicit and checkable from tables or code.  

Required fix  
- Provide a small table listing, for each injection (0, 0.27°, 0.342°): mean recovered β̂, its MC standard deviation, bias ∆β, and SNR ≡ β̂/σβ (or whatever exact definition is used).  
- Make explicit that the stated SNR values refer to MC-recovery of injected signals in the NaMaster pipeline, not to sky-detection significance, as you already partially note; this should be stated adjacent to the SNR numbers themselves.  
Classification: MAJOR  

---

P1B-M3  
Section: Sec. VI (“Birefringence value” and “Summary-likelihood combination”), pages 6–7  
Problem (consistency and traceability of quoted β values and σ’s to literature)  
The manuscript quotes several β values and σ’s:  

- “β = 0.30° ± 0.11° (Planck NPIPE )”  
- “β = 0.215° ± 0.074° (ACT DR6 [3])”  
- “β = 0.342° ± 0.094° (3.6σ) [2]” as the primary WMAP+Planck joint value.  
- An inverse-variance combination giving “βcombined = 0.241° ± 0.061° (3.9σ).”  

From the real Diego-Palazuelos et al. Planck NPIPE paper (arXiv:2201.07682), the reported β is indeed ~0.30° ± 0.11°, and from Eskilt & Komatsu (arXiv:2205.13962) the joint WMAP+Planck value β ≈ 0.342° ± 0.094° is also correct. However, the ACT DR6 β = 0.215° ± 0.074° figure and its 2.4–2.9σ significance are not traceable to any currently available ACT DR6 birefringence paper with the given (future) arXiv ID [3]. The combination βcombined = 0.241° ± 0.061° is then numerically correct given the input numbers but depends on an ACT result that is not currently documented.  

Required fix  
- Either (i) provide a correct, verifiable citation for the ACT DR6 birefringence result with β = 0.215° ± 0.074°, including a real arXiv ID and demonstrate that this number matches that paper; or (ii) remove the ACT DR6 value and the inverse-variance combination, retaining only the Planck and WMAP+Planck numbers that can be verified.  
- If you keep the inverse-variance combination, explicitly include the formula and show the arithmetic once, so a reader can check the calculation straightforwardly.  
Classification: MAJOR  

---

P1B-M4  
Section: Sec. VI, equations around β ≈ 0.29°, eq. (3), page 6  
Problem (arithmetic and parameter mapping in ALP birefringence formula)  
The text writes:  

- “For Caγ = 8, θi = 1, m ≈ 2H0:  
  β ≈ (αEM × 8)/(4π) × 1.07 ≈ 0.29°.”  

The birefringence formula for an ALP with coupling Caγ/fa is β ≈ (αEM/(4π)) Caγ ∆ϕ/fa. The text asserts ∆ϕ/fa ≈ 1.07 for m ≈ 2H0 and θi = 1 (by referring to “field displacement from recombination to today”), but the derivation is not shown, and 1.07 seems slightly inconsistent with the trajectory range ∆ϕ/fa ∈ [0.2, 1.1] quoted just above. Also, the numeric conversion from radians to degrees is not made explicit.  

Required fix  
- Show the explicit step from β (in radians) to degrees:  
  βdeg = (αEM/(4π)) Caγ (∆ϕ/fa) × 180/π, and plug in αEM ≈ 1/137, Caγ = 8, and the chosen ∆ϕ/fa = 1.07 to produce βdeg numerically.  
- Clarify how ∆ϕ/fa = 1.07 is obtained from the ODE integration (eq. (2)), and ensure that this is consistent with the stated envelope [0.2, 1.1]. If 1.07 is at the high end, the midpoint value used for the “fiducial” 0.27° should be explicitly noted.  
Classification: MINOR  

---

P1B-N1  
Section: Abstract and Sec. VII (“Conclusions”), multiple pages  
Problem (length vs contribution; excessive forward-looking narrative for a technical companion)  
For a technical verification companion, the manuscript is quite long and narrative-driven for the actual contribution: verification of a stock ΛCDM+∆Neff MCMC run; NaMaster pseudo-Cℓ pipeline test; and a consistency check of a simple ALP-birefringence model. A significant fraction of the text is meta-discussion about future nested-sampling runs, forward-looking DESI DR2 analyses, and references to other papers “in preparation,” which do not yet exist.  

Required fix  
- Compress sections that describe future or external work (e.g., the long “Forward” paragraph in Conclusions and much of Appendix A’s narrative) and focus on the technical, currently reproducible verification content.  
- A reasonable page target for this companion paper would be ~6–7 journal pages rather than 10, assuming figures and tables are used efficiently.  
Classification: MINOR  

---

P1B-N2  
Section: Throughout the text (e.g., Introduction, Sec. III, Sec. VI)  
Problem (version-history and internal bookkeeping language)  
The manuscript contains several pieces of internal-history language that should not appear in a final PRD submission, e.g.:  

- “earlier count erroneously quoted ‘98.6% quintom-B’ weight”  
- “initially characterized as strictly ‘stable across all three injections’ at 0.032°, but the 0.342° injection actually gives 0.040°”  
- “promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal”  
- “addresses earlier reviewer concerns that the reported 67.68 was inconsistent …”  
- Reference labels like “P1A Sec. VI”, “P1B” within the text and in tables.  

These are all signs of draft version history and prior reviews that should not be included in the final paper.  

Required fix  
- Remove all references to “earlier” miscounts, promises to reviewers, or prior audit logs; keep only the final, corrected statements.  
- Where necessary, simply present the corrected value; do not describe its evolution through drafts.  
Classification: MINOR  

---

P1B-N3  
Section: “Claims classification” table (Table III), page 10  
Problem (internal audit artifact)  
Table III is a self-referential “Claims classification for this companion paper” with columns “Type / Status / Notes,” including entries such as “Model-comparison ∆AIC/BIC/ln B – Numerical – Omitted – Follow-up nested-sampling analysis.” This is an internal QA artifact, not standard material for a PRD article, and it does not cite external literature.  

Required fix  
- Remove the claims-classification table from the main text. If the author wishes to keep such a QA checklist, it can be provided as supplementary material or maintained privately.  
Classification: NIT  

---

P1B-N4  
Section: Acknowledgments, page 8  
Problem (AI-use note potentially not aligned with journal policy)  
The paper states: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation.” Different journals have different requirements on how AI tools are disclosed; PRD has specific policies that may differ from this phrasing.  

Required fix  
- Check PRD’s current AI-use policy and adjust the acknowledgment accordingly, ensuring that it complies with the journal’s required wording and clarifies that the author is responsible for all content.  
Classification: NIT  

---

P1B-N5  
Section: Minor stylistic duplication and awkward phrases, various pages  
Problem (repeated phrases / near-duplicate wording)  
Although I did not find egregious duplicated phrases like “canonical canonical-mask,” there are a number of slightly awkward repetitions, e.g.:  

- “We report this as a ΛCDM+∆Neff null-consistency test: the data are consistent with ∆Neff = 0 in stock CAMB.1” followed almost immediately by “The proxy run … confirms ∆Neff is consistent with zero.”  
- Multiple reiterations that the NaMaster pipeline “is not a competitive sky measurement” and that “the primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ,” sometimes within the same paragraph.  

Required fix  
- Edit for concision, removing redundant statements while preserving the necessary scope clarifications.  
Classification: NIT  

---

## Summary recommendation

MAJOR REVISIONS  

The core numerical work (ΛCDM+∆Neff MCMC verification, NaMaster pipeline test, ALP-birefringence consistency check) is potentially useful, but the bibliography and citation practice are not acceptable in their current form: multiple references use fabricated or future-dated arXiv IDs, several key comparisons rely on papers that do not yet exist or are only “in preparation,” and some quoted significances and tensions are not recomputed or clearly defined. The paper also includes internal audit artifacts and version-history language. A thorough clean-up of all references to ensure that every cited statistic maps to a real, verifiable paper, plus removal or clear labeling of all speculative future work, is required before this manuscript can be considered for publication.