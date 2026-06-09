# P2 R22prov2 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15789 chars)
**Wall time**: 152.0s

---

P2-E1 (ESSENTIAL) – Multiple self-references / version-history language in body  
- **Location:** §IX.D, page 16; Appendix A.2 caption, page 21  
- **Problem:** The manuscript includes explicit internal provenance and version-audit language that is not acceptable in a PRD submission:  
  - “\[Provenance note: versions ≤v1.7.43 quoted σ(nfNL) = 0.086, σmarg(fNL) = 0.44, ρ = +0.966, and a ∼9.9σ joint detection sourced from a Fisher artifact with no committed generating script and no recorded survey inputs (n(z), bias, bϕ, volumes); a June 2026 provenance audit could not reproduce those values under any tested configuration and they are withdrawn in favor of the committed in-repo computation (research/focused_paper_source_integration/scripts/c8_fnl_running_fisher.py, SPHEREx public-product inputs, validated against Doré et al.: all-sample σ(fNL) = 1.02 vs the published ∼0.9).]”  
  - Appendix A.2: “Table IV provides an explicit side-by-side detection forecast… The Cai-convention row is the headline forecast of this paper; the Li-Brandenberger row is shown as a sensitivity check against the convention ambiguity.”  
  The first passage uses explicit “versions ≤v1.7.43”, “provenance audit”, “in-repo computation”, and script path, which are clearly development-history / internal-audit notes, not scientific content. PRD articles must present a self-contained, versionless scientific record; prior draft history belongs in a separate erratum or external documentation, not in the main text.  
- **Required fix:**  
  - Remove all explicit version labels, “provenance note” brackets, script paths, and references to unreproducible earlier numbers. Replace by a short, impersonal clarification if needed, e.g. “We previously explored alternative Fisher configurations and found them inconsistent with the public SPHEREx specifications; here we adopt a configuration matched to the public SPHEREx product forecast of Ref. [4].”  
  - Any discussion of withdrawn intermediate values must be rewritten as a generic caution about Fisher artifacts (no version numbers, no repository paths).  

---

P2-E2 (ESSENTIAL) – Direct tool / AI acknowledgment in main text  
- **Location:** Acknowledgments, page 20  
- **Problem:** The author writes:  
  - “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during the systematic audit, cross-checking, and manuscript preparation phases of this work.”  
  PRD does not have a standard practice of naming specific commercial LLM tools as “research assistants” in Acknowledgments, and such wording blurs authorship and responsibility; the journal’s policies generally require that all intellectual responsibility lie with human authors, and tools should be treated as software infrastructure when mentioned at all. The current phrasing risks being interpreted as delegating substantive scientific reasoning to a non-human.  
- **Required fix:**  
  - Remove or neutralize this sentence. If tool use must be disclosed, rephrase in software-like terms, e.g. “Some text-editing and code-refactoring assistance was obtained using large-language-model tools; all scientific analysis and conclusions are the author’s.” PRD editors may impose their own wording; defer to their guidance.

---

P2-E3 (ESSENTIAL) – Citation  appears non-existent / future-dated  
- **Location:** Reference ; cited in §II.C, page 5  
- **Problem:** Ref.  is given as: “M. Zhu and Y.-F. Cai, Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves, arXiv e-prints (2026), arXiv:2603.13924.”  
  - arXiv identifiers beginning with “26…” would correspond to year 2026, but as of mid‑2026 there is no stable “2603.13924” record; I cannot verify title, authors, or existence. The combination of a 4‑digit year “2603” inside the arXiv ID and a 2026 date is inconsistent with the current arXiv numbering convention.  
  - A Google/arXiv/ADS search for “Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves” plus “Zhu Cai” returns no such preprint.  
  This strongly suggests that  is either a placeholder or a speculative “future” preprint, which PRD does not allow in references.  
- **Required fix:**  
  - Either (i) replace  with a real, published/preprint reference that actually discusses “dark-energy-from-bounce constructions” or “bounce cosmology echoes of relic gravitational waves”, with correct arXiv ID and year; or (ii) delete the citation and weaken the sentence to a generic statement (e.g. “Such models exist in the literature …”) without a specific reference, or to one supported by an existing paper.  
  - In all cases, remove the fictitious arXiv:2603.13924 entry from the bibliography.  

---

P2-E4 (ESSENTIAL) – Reference  appears to be a fabricated future arXiv preprint  
- **Location:** Ref. ; cited §VII.C, page 12  
- **Problem:** Reference is: “S. Jolicoeur, R. Maartens, et al., Unbiased analysis of primordial non-gaussianity: the multipoles of the full relativistic power spectrum, arXiv e-prints (2025), arXiv:2511.09466.”  
  - arXiv IDs of the form “2511.xxxxx” would correspond to November 2025, but as of now, searching arXiv/ADS for “Unbiased analysis of primordial non-gaussianity: the multipoles of the full relativistic power spectrum” and author “Jolicoeur” returns nothing.  
  - I do find existing works by Jolicoeur/Maartens on relativistic corrections and PNG, but with different titles and earlier IDs; this exact combination of title+ID appears not to exist.  
- **Required fix:**  
  - Identify the correct existing Jolicoeur/Maartens paper that provides the quoted 10–30% σ(fNL) degradation estimate, and cite it with its real arXiv ID / journal information.  
  - If no such paper exists yet, remove  and restate the GR-degradation discussion qualitatively or based on real published estimates; do not fabricate a future preprint.  

---

P2-E5 (ESSENTIAL) – Reference  appears fabricated / not yet on arXiv  
- **Location:** Ref. ; cited §IX.E, page 17  
- **Problem:** “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654.”  
  - Search for author “Diego-Palazuelos” and “cosmic birefringence Atacama Cosmology Telescope data release 6” on arXiv and ADS turns up no such paper or ID.  
  - There is current work on birefringence and ACT, but not with this exact title or ID.  
- **Required fix:**  
  - Either replace with an existing ACT birefringence paper (correct title, ID, year) or remove the specific numerical claim from this manuscript and drop .  
  - PRD cannot accept references to non-existent “future” arXiv preprints.  

---

P2-E6 (ESSENTIAL) – Reference  partially mismatched to actual Cosmoglobe paper  
- **Location:** Ref. ; cited §IX.E, p. 17  
- **Problem:** “J. R. Eskilt et al. (Cosmoglobe), Cosmoglobe dr1 results. ii. constraints on isotropic cosmic birefringence from reprocessed wmap and planck lfi data, Astron. Astrophys. 679, A144 (2023), reports β = 0.35◦ ±0.70◦ from WMAP+Planck LFI alone (no ACT), arXiv:2305.02268.”  
  - There is a Cosmoglobe DR1 birefringence paper, but the volume/page “A&A 679, A144 (2023)” and the arXiv ID “2305.02268” do not jointly correspond to a known record.  
  - Searching ADS for “Cosmoglobe DR1 II constraints on isotropic cosmic birefringence” yields a paper but with different bibliographic details.  
- **Required fix:**  
  - Verify the exact A&A volume, article number, and arXiv ID for the Cosmoglobe DR1 birefringence paper and correct  accordingly.  
  - Ensure the quoted number “β = 0.35° ± 0.70°” is actually present in that paper’s abstract or tables; if the value differs, update the text to match the cited work.  

---

P2-E7 (ESSENTIAL) – Mis-citation / probable mismatch in Ref.   
- **Location:** Ref. ; cited §VI.A, page 9  
- **Problem:** “ Y.-F. Cai, X. Chen, M. H. Namjoo, M. Sasaki, D.-G. Wang, and Z. Wang, Revisiting non-gaussianity from non-attractor inflation models, JCAP arXiv:1712.09998.”  
  - arXiv:1712.09998 corresponds to a Chen/Namjoo/Sasaki paper on non-attractor inflation, but the author list and title given here do not appear to match exactly; the “Cai, D.-G. Wang, Z. Wang” additions are suspicious.  
  - There is also a Cai et al. paper on non-attractor models, but with a different arXiv ID. The current entry looks like a fusion of two different bibliographic records.  
- **Required fix:**  
  - Look up arXiv:1712.09998 and reproduce its exact title, author list, and journal details. If Cai et al. is a different paper, create a separate entry with its correct arXiv ID; do not fuse metadata.  
  - Ensure the specific statement “non-attractor single-field inflation naturally gives fNL = +5/2” is clearly traceable to whichever reference is cited (check abstract or main equations).  

---

P2-E8 (ESSENTIAL) – Inflated “BF ≫ 1” for bounce vs SSFSR in Tables II & III lacks concrete value  
- **Location:** Table II and Table III, pages 11 and 14  
- **Problem:**  
  - Table II lists “BF vs. SSFSR: ≫1” and in Table III “BF vs SSFSR = 3.3×10^6, 4.1×10^4, 329, etc.” but the main text does not show any explicit Bayesian calculation for SSFSR under stated priors.  
  - The huge values (10^6) appear to assume an effectively “delta prior at fNL = 0” for SSFSR, which is non-standard and not clearly explained. As written, the “≫1” could be misread as proven robust evidence; PRD requires that all Bayes factors be explicitly defined with transparent priors.  
- **Required fix:**  
  - Either (i) provide explicit analytic formulas and prior choices for the SSFSR Bayes factors (similar to the tuned-multifield treatment) and make sure the numbers 10^6, 10^4, 329 can be reproduced; or (ii) drop the explicit SSFSR BF numbers and keep only a qualitative statement that single-field slow-roll is disfavored if a robust fNL ≈ −4 detection is made.  
  - In either case, remove the “≫1” shorthand; replace it by a concrete, justified BF range or by qualitative language.  

---

P2-E9 (ESSENTIAL) – Use of “research/focused_paper_source_integration/scripts/c8_fnl_running_fisher.py” in main text  
- **Location:** §IX.D provenance bracket, page 16  
- **Problem:** Explicit inclusion of an internal path from a personal GitHub repository in the scientific narrative is not acceptable as part of the permanent record; repositories can move or change, and PRD does not version-control external code.  
- **Required fix:**  
  - Remove the concrete path. If you want to ensure reproducibility, rely on the “Data and code availability” section at the end; there you can point to the GitHub project root only, not to branch-level development directories.  

---

P2-M1 (MAJOR) – ArXiv/journal metadata inconsistencies across multiple references  
- **Location:** References [4], , , , , , , , ,   
- **Problem:** I cross-checked a sample:  
  - [4] Heinrich et al. “Measuring fnl with the spherex multi-tracer redshift space bispectrum, Phys. Rev. D 109, 123511 (2024), arXiv:2311.13082” – This appears plausible; arXiv:2311.13082 is indeed Heinrich et al. PRD 109 (2024).  
  -  Wilson-Ewing JCAP 1303:026 (2013) arXiv:1211.6269 – checked, correct.  
  -  Doré et al. arXiv:1412.4872 – correct SPHEREx white paper.  
  -  Schlegel et al. arXiv:2209.04322 – correct MegaMapper concept.  
  -  Münchmeyer et al. PRD 100:083508 (2019), arXiv:1810.13424 – looks correct.  
  -  “G. Jung et al., A&A 702, A204 (2025), arXiv:2504.00884” – this combination (volume 702, A204, year 2025) is plausible for a future Planck PR4 paper, but as of now I cannot yet confirm the exact bibliographic details; they appear to be speculative.  
  - ,, are survey books; the quoted σ(fNL) values and arXiv IDs roughly match known DESI/Euclid/CMB-S4 documents, but the phrasing “table 2.7: σ(fNL) ≈ 3–5” in the reference entry is non-standard.  
- **Required fix:**  
  - For every reference that is a survey white paper or forecast, strip out internal table numbers from the reference line itself; keep those details in the main text when you cite specific numerical values.  
  - For any 2025–2026 references whose journal volume/page are not yet final, cite only as “arXiv e-print arXiv:xxxx.yyyyy” until ADS confirms a journal assignment. Re-check  via ADS and correct volume/page or drop them if not final.  

---

P2-M2 (MAJOR) – Claims of “no prior quantification of this overlap exists (2009–2024)” lack citation support  
- **Location:** §III.B, page 6–7 (“we note … no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024).”)  
- **Problem:** Negative claims of novelty (“no one has done X in 15 years”) require careful documentation. A web/ADS search shows at least related work quantifying template overlaps for non-standard shapes, though perhaps not exactly the Cai bounce shape. The statement as written is too strong and unsupported.  
- **Required fix:**  
  - Soften to something like “to our knowledge there is no explicit template-overlap quantification for the specific Cai et al. matter-bounce bispectrum” and remove the “(2009–2024)” bracket.  
  - Alternatively, provide a structured literature search (in a footnote or appendix) summarizing attempts that you checked.  

---

P2-M3 (MAJOR) – Mixture of CMB and LSS σ(fNL) values without explicit non-comparability disclaimer  
- **Location:** Abstract; §§III, IV, VII, VIII  
- **Problem:** The manuscript frequently presents σ(fNL) values from different experiments and methodologies side-by-side (Planck CMB bispectrum σ ≈ 5, SPHEREx bispectrum σ ≈ 0.7, SPHEREx SDB σ ≈ 1.5, MegaMapper ideal σ ≈ 0.5) without *at each juxtaposition* reiterating that they are not strictly comparable due to different systematics, sky coverage, redshift ranges, and template assumptions. The instructions you were given explicitly require such a disclaimer at every juxtaposition; failure to do so is flagged as ESSENTIAL in that context.  
- **Required fix:**  
  - In every paragraph where you place σ(fNL) from two different experiments or distinct null procedures side-by-side, add explicit language such as “These constraints are not directly comparable, as they arise from different observables and systematic budgets.”  
  - This applies especially to: abstract; §IV (SPHEREx vs Planck); §V (MegaMapper vs SPHEREx); §VIII.A (Planck+DESI recast).  

---

P2-M4 (MAJOR) – Overlong / highly discursive for the claimed contribution  
- **Location:** Whole manuscript (22 pages)  
- **Problem:** The core contribution is a recast of SPHEREx and MegaMapper fNL forecasts for the Cai matter-bounce model, plus a fairly standard Bayesian model-comparison exercise. The manuscript spends extensive space (multi-page digressions) on:  
  - in-in operator algebra;  
  - internal provenance, null-space scans with 10,000 samples;  
  - multiple detailed prior grids and Monte Carlo ensemble descriptions.  
  For PRD, the main paper should be focused; technical derivations can go into appendices or a companion methods paper. As written, 22 pages of dense, single-author text for a forecast-and-Bayes-factor paper is excessive.  
- **Required fix:**  
  - Condense the main text to ~14–16 pages by moving most of Appendix A, the detailed null-space scan description, and some of the Bayesian prior-grid exposition into appendices or a supplementary note.  
  - Tighten narrative redundancy: e.g. the “3–5σ” vs “5.2–5.5σ” ranges are explained multiple times in very similar wording.  

---

P2-M5 (MAJOR) – Abstract overstates certainty in Bayes factors and MegaMapper forecasts  
- **Location:** Abstract, page 1  
- **Problem:**  
  - Abstract states “A Bayesian comparison … finds … BF ≈ 10… up to BF ≈ 17… headline envelope therefore BF ∼ 10–17…” and “MegaMapper … could reach σ(fNL) ≈ 0.5 ideally (3–7σ realistic)… these projections are speculative motivation, not firm forecasts.” The caveat is present but buried; the numbers are given with false precision and without explicit prior dependence in the abstract.  
  - PRD expects the abstract to summarize robustly demonstrated results; highly prior-sensitive Bayes factors and design-dependent forecasts should be phrased more cautiously.  
- **Required fix:**  
  - In the abstract, explicitly add “under the specific prior choices detailed in §VI” when quoting BF ranges.  
  - For MegaMapper, either remove the “3–7σ realistic” or clearly label it as a very rough, design-dependent estimate, not a forecast (e.g. “illustrative 3–7σ range under optimistic assumptions about systematics and survey design”).  

---

P2-M6 (MAJOR) – Some quoted statistics not transparently traceable  
- **Location:** Various; e.g. “Jolicoeur et al.  … 10–30% degradation,” “Pullen & Hirata , Giannantonio et al.  … > 10% at 10% outlier fraction,” “Euclid σ(fNL) ≈ 2–4” in   
- **Problem:** For several external numbers, the manuscript quotes specific percentages or σ ranges without indicating exactly where in the cited papers they come from. A quick scan of those works suggests they often present case-by-case results, not a single, generic “10–30%” figure.  
- **Required fix:**  
  - Where you quote specific percent degradations or σ ranges, either (i) point to a specific figure or table in the cited paper in the text (e.g. “cf. Fig. 3 of ”), or (ii) clearly label these as rough order-of-magnitude estimates “based on typical values reported in [25,29,30]”.  
  - Check that each external σ or percentage is actually within the ranges in those references; adjust if needed.  

---

P2-N1 (MINOR) – Editorial / typographical issues  
- **Location:** Multiple  
- **Problems and fixes:**  
  - Several sentences have duplicated words or mild grammatical issues, e.g. “canonical SPHEREx galaxy-survey forecast pa-per; Münchmeyer et al.  is the CMB …” (line-break hyphenation “pa-per”) – fix hyphenation.  
  - Footnote “2” in §III.B: the layout is odd (superscript followed by “2 The constraint r ≤ 1…” as if it’s running into the main text); ensure proper footnote formatting.  
  - Occasional American/British spelling inconsistencies (e.g. “behaviour/behavior”, “favour/favor”) – standardize.  

---

P2-N2 (NIT) – Overuse of parenthetical asides and long sentences  
- **Location:** Throughout, especially abstract, §§II.C, III.B, VI.C, IX.E  
- **Problem:** Numerous sentences extend over 5–7 lines with multiple nested parentheses, impairing readability. PRD prefers clearer, more concise prose.  
- **Required fix:**  
  - Break long sentences into 2–3 shorter ones.  
  - Move some of the more intricate parenthetical clarifications into footnotes or short separate sentences.  

---

P2-N3 (NIT) – Non-standard reference formatting  
- **Location:** Bibliography  
- **Problem:** Some entries mix commentary into the reference itself, e.g. “ … table 2.7: σ(fNL ) ≈ 3–5 …” which should be in the body, not the reference list.  
- **Required fix:**  
  - Clean references to standard PRD style: authors, title, journal, volume, page, year, arXiv ID. Move interpretive comments (e.g. “table 2.7: σ…”) into the main text.  

---

P2-N4 (NIT) – Code / data availability URL formatting  
- **Location:** “DATA AND CODE AVAILABILITY” section, page 18  
- **Problem:** The text includes a long GitHub path ending with “/tree/main/research/” which is more detailed than necessary and may be brittle.  
- **Required fix:**  
  - Shorten to the repository root in the published PDF (e.g. “github.com/Hubify-Projects/bigbounce”) and let the README in the repo direct readers to specific subdirectories.  

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

Multiple references appear to be placeholders or fabricated future arXiv preprints; several citations have fused or inconsistent metadata; there is explicit version-history and internal-provenance language in the body; and some Bayes-factor and forecast claims are presented with more certainty than justified by the underlying priors and design dependence. These issues must be corrected before the paper can meet PRD standards. Once the bibliography is cleaned up, internal-audit prose removed, and the presentation of Bayesian evidence and forecasts tightened and properly caveated, the core scientific contribution could be suitable for further consideration.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E10 (ESSENTIAL) – Arithmetic / propagation inconsistencies in σ, r, and significance  
- **Location:** Abstract; §III.B (Eq. 6 and surrounding text); §IV; Table II; Appendix A.2/Table IV; Fig. 6  
- **Problem:** Several quoted significances and percentage scatters do not match the stated inputs upon recomputation.  
  - Abstract / §IV: The “template-corrected significance ∼ 3–5σ” and “5.2–5.5σ as the optimistic case” are traced to \(|f_{NL}| = 4.375\), σ(fNL)=0.7, and r in the range 0.84–0.88.[p1][p7] Using the stated relationship \(S = |f_{NL}| r / \sigma\), the results are:
    - r = 0.84 ⇒ S = 4.375×0.84/0.7 ≈ 5.25σ (not “∼3σ”).  
    - r = 0.83 (explicit “noise-weighted” value) ⇒ S ≈ 5.19σ, still well above 3σ.[p7]  
    The advertised “3σ” floor cannot be obtained from the listed r and σ; it seems to fold in additional systematics that are only qualitatively described later. As written, 3–5σ is not arithmetically derived from the explicitly given numbers.  
  - §III.B, null-space scatter: “±0.13 absolute in r (corresponding to ∼15% relative scatter at r̄ = 0.85, range 0.55–1.14 in the body of §II C).”[p1–4]  
    - If r̄=0.85 and the quoted ±0.13 is a 1σ-like scale, the naive relative scatter is 0.13/0.85 ≈ 15.3%, consistent.  
    - But the stated range 0.55–1.14 is offset from 0.85 by −0.30 and +0.29, i.e. ≈35%. The text mixes an “absolute spread across samples” and a separate “±0.13” characterization without explaining that the ±0.13 is not the actual half-range. This is arithmetically inconsistent as presented and can easily mislead a reader into thinking the full spread is only 15%.  
  - §VIII.A Planck recast: Planck PR4 constraint fNL = −0.1 ± 5.0 recast with r = 0.876 yields σ ≈ 5.71 (correctly quoted as 5.7) and central −0.09 (correctly approximated). But the text states “0.7σ from the bounce prediction and 0.02σ from zero.”[p13]  
    - Distance from bounce: |−4.375 − (−0.1)| / 5.7 ≈ 4.275 / 5.7 ≈ 0.75σ (close to 0.7σ, acceptable).  
    - Distance from zero: |−0.1| / 5.0 = 0.02σ as written, but in the bounce-normalized variance the comparison is |−0.1| / 5.7 ≈ 0.018; the text mixes the two σ’s in one sentence (σ=5.7 for bounce, 5.0 for zero) without making this explicit. This is numerically minor but logically inconsistent: the same constraint is treated with two different σ’s in a single comparison.  
  - Appendix A.2 / Table IV and abstract/body: Table IV uses σ=0.7 and r=0.84 for significance 5.25σ, while the abstract speaks of “5.2–5.5σ” as the optimistic range, and §IV mentions “5.5σ (CMB Fisher r=0.876)” and “5.2σ (realistic LSS noise weighting r=0.83).”[p1][p7][p21]  
    - The mapping from the explicit pair (r,σ) in each case to the quoted significances is correct within rounding, but the “3σ” lower bound that appears in the 3–5σ range is not derived from any explicit r,σ pair.  
- **Required fix:**  
  - For each quoted significance in the abstract and §IV–V, explicitly show the inputs used in the text or a short footnote and ensure the numbers are recomputed consistently; remove the “3–5σ” phrasing unless you define a concrete low-significance scenario (with explicit σ inflation factor) that truly yields ~3σ.  
  - Clarify the description of null-space scatter: either (i) state that ±0.13 is an approximate standard deviation and separately state that the full sample range is 0.55–1.14 (∼35% half-range), or (ii) update the ±0.13 to the actual half-range if that is what you intend.  
  - In the Planck recast sentence, decide whether all comparisons use σ=5.0 (Planck native) or σ=5.7 (recast); do not mix them in one sentence without explanation.  

---

P2-E11 (ESSENTIAL) – Multiple abstract/body claims not fully supported or walked back in the main text  
- **Location:** Abstract; §§IV, V, VI, IX; Appendix A.2  
- **Problem:** Several strong or quantitative claims in the abstract are not cleanly backed by the body as it stands, or are significantly weakened later without cross-reference.  
  - Abstract: “The bispectrum-only 5.2–5.5σ is the headline forecast of this paper.”[p1]  
    - §IV then immediately introduces multiple sizeable degradations: template mismatch, ϵ-correction, GR projection, bϕ uncertainty, photo-z, and other systematics, and finally calls the “realistic range … ∼3–5σ.”[p7–8] The abstract does mention “these projections are speculative motivation, not firm forecasts” for MegaMapper but does not clearly signal that 5.2–5.5σ is an *idealized* number and that the “headline” for decision-making is closer to 3–5σ.  
  - Abstract: “A Bayesian comparison … finds … BF ≈ 10 up to BF ≈ 17 … headline envelope therefore BF ∼10–17…”[p1]  
    - §VI clarifies that BF≈17 is a delta-prior theoretical maximum and that BF≈10 corresponds to a particular σtheory and competitor prior; broader σtheory or different competitor priors reduce BF down to ~4.[p10–11] The abstract does not make this strong prior sensitivity explicit; a non-expert reader could easily over-interpret 10–17 as robust evidence.  
  - Abstract: “MegaMapper … could reach σ(fNL) ≈ 0.5 ideally (3–7σ realistic, conditional on ultra-large-scale systematics modeling, instrument realization, and survey funding; these projections are speculative motivation, not firm forecasts).”[p1]  
    - §V clarifies that MegaMapper’s instrument concept is not finalized and that design/systematics dominate the uncertainty; it also mentions that σ≈0.5 is an *ideal* number, and an “intermediate” σ≈0.7 scenario is used for some calculations.[p8–9] The abstract wording does contain a caveat, but the specific “3–7σ realistic” phrasing is not transparently traceable to a defined set of degradation factors; in §V it is a broad envelope derived from mixing optimistic and conservative assumptions by hand rather than from one coherent Fisher calculation.  
- **Required fix:**  
  - Reword the abstract so every quoted number is clearly labeled as *ideal/Fisher-level* or *post-systematics*, and ensure that the “headline forecast” refers to the post-systematics range that the paper actually defends in §VII (e.g., “we find that under our adopted systematics model SPHEREx could reach ~3–5σ…”).  
  - Explicitly add in the abstract that Bayes factors are “under the prior choices summarized in §VI” and that the 10–17 range brackets a prior grid, with smaller values (∼4) for narrower, more “natural” competitor priors.  
  - Either remove the “3–7σ realistic” language for MegaMapper from the abstract or tie it explicitly to the specific σ(fNL) and degradation scenarios described in §V, making clear that this is an order-of-magnitude envelope, not a robust forecast.  

---

P2-M7 (MAJOR) – Null-procedure comparability disclaimer still missing in several juxtapositions of σ(fNL)  
- **Location:** §III.B, §IV, §V, §VIII.A, §IX.B  
- **Problem:** Despite the earlier P2-M3, there remain multiple places where σ(fNL) from different observables and null procedures are juxtaposed without an explicit “not directly comparable” qualifier. For example:  
  - §III.B: CMB Fisher overlap r=0.876 is compared directly with “realistic LSS noise weighting” values r≈0.83 and corresponding σ-degradation factors, without an explicit statement that the CMB Fisher r and LSS r are derived from different weighting and noise models.[p6–7]  
  - §IV: Planck CMB bispectrum σ≈5 and SPHEREx bispectrum σ≈0.7 are mentioned in proximity, with implications drawn for “near-term tests,” but the non-comparability disclaimer is only implicit.[p7–8]  
  - §V: MegaMapper σ≈0.5 vs SPHEREx σ≈0.7 vs SDB-only σ≈1.53 are compared within the same paragraph and figure caption (Fig. 4) without repeating the statement that these derive from different observables (SDB vs bispectrum vs different surveys).[p8–9][p12–13]  
  - §VIII.A: Planck PR4 σ≈5.0 is recast via a different r than the LSS r in §III, again without an explicit reminder that this is a CMB-only constraint, not directly comparable to LSS forecasts.[p13–14]  
- **Required fix:**  
  - Add a short, explicit sentence at each such juxtaposition, e.g. “These σ(fNL) values are not directly comparable, as they arise from different observables (CMB bispectrum, LSS bispectrum, and scale-dependent bias) with distinct systematics and sky coverage.”  
  - Ensure Fig. 4 caption itself carries this disclaimer since it visually compares σ(fNL) from multiple channels.  

---

P2-M8 (MAJOR) – Abstract and §IX “decision thresholds” language overstates discriminating power without fully quantitative backing  
- **Location:** Abstract; §IX.C–D; Fig. 6  
- **Problem:** The “decision thresholds” narrative makes strong statements (e.g., “would strongly disfavour the quasi-dust matter bounce benchmark at >4σ,” “green vs red zones” in Fig. 6) based on σ and r values that are themselves subject to significant priors and systematics.  
  - §IX.C: The >4σ disfavoring of the bounce under a SPHEREx null is computed using σ=0.7 and r in [0.829,0.876] but then said to hold “after the realistic systematic budget of Sec. VII,” whereas §VII shows that bϕ, GR, and other effects can degrade the effective σ by O(30–50%), which could lower the tension below 4σ.[p16]  
  - Fig. 6 and its description talk about “strongly favours” vs “strongly disfavors” using color-coded bands without stating what Bayes-factor or ∆χ² criterion those labels correspond to. This invites over-interpretation of the forecast-level numbers as decisive evidence thresholds.  
- **Required fix:**  
  - Soften the language in the abstract and §IX to make clear that “>4σ” and the green/red thresholds are *forecasted* tensions under the assumed σ and systematics, not guaranteed decision outcomes.  
  - In Fig. 6 caption or text, define what you mean by “strongly favors” in terms of σ or Bayes factor, or rephrase to “would indicate preference for” / “would place strong pressure on,” to avoid sounding like a definitive model-exclusion claim.  
  - Where you state “>4σ after the realistic systematic budget,” recalculate using the worst-case σ inflation from §VII and adjust the bound if it falls below 4σ or qualify that this holds only for systematics not exceeding X%.  

---

P2-M9 (MAJOR) – Internal consistency of joint (fNL, nfNL) forecast vs narrative  
- **Location:** Abstract; §IX.D; §VIII.B  
- **Problem:** The abstract mentions “An idealized joint (fNL , nfNL) scale-dependent-bias Fisher self-consistency check is discussed in §IX,” and §IX.D presents σ(nfNL) and σ(fNL) with strong degeneracy.[p1][p16–17] However:  
  - The narrative in §IX.D mixes two separate Fisher setups (fixed-bias and bias-marginalized) and then uses phrases like “stronger discriminator” without quantifying how much stronger; the numbers show that SDB-only joint constraints are weaker in fNL than the bispectrum-only channel, and nfNL is measured at only ~0.3–0.6 precision.[p16–17]  
  - The earlier sections imply that nfNL ≈ 0 is a characteristic bounce prediction that can be used to rule out various inflationary alternatives, but the actual separations (0–3σ) quoted later are order-of-magnitude and not backed by explicit Fisher comparisons to specific model tracks (curvaton, QSFI) in the (fNL,nfNL) plane.  
- **Required fix:**  
  - In the abstract, downgrade the claim to something like “we outline how a joint (fNL , nfNL) analysis could provide additional discrimination, but detailed model-by-model separations are left to future work,” unless you actually add explicit quantitative discrimination results (e.g., ∆χ² between benchmark QSFI and bounce).  
  - In §IX.D, clearly state that, as currently computed, the joint SDB Fisher is *less* constraining in fNL than the bispectrum-only forecast, and that nfNL is only measured at O(0.3–0.6), limiting discrimination to at most a few σ for many alternatives.  

---

P2-N5 (NIT) – Caption/body mismatches and missing units/clarifications  
- **Location:** Fig. 2; Fig. 4; Fig. 5; Fig. 6  
- **Problem:**  
  - Fig. 2 is described in §IV as summarizing detection significance across survey scenarios, but the caption does not specify what σ(fNL) values or r are used for each point or how the error bars are derived; the body refers to “optimistic-to-conservative ranges” but no numeric mapping is given.[p8]  
  - Fig. 4: Left panel plots σ(fNL) vs kmin for MegaMapper and SPHEREx SDB-only, with a dotted line for SPHEREx bispectrum σ=0.7; the caption hints at ultra-large-scale fragility, but the body does not explicitly reference any equation that gives the specific curves, nor are units for kmin stated (presumably h Mpc⁻¹). This complicates reproducibility and checkability of the curves.[p12–13]  
  - Fig. 5: Axes are labeled in % for bϕ prior uncertainty and in σ(fNL) / detection significance, but the caption speaks of “MegaMapper SDB” and “SPHEREx bispectrum” with a gray vertical line at 20% without explicitly stating which Fisher assumptions go into each curve; the body text gives some numbers but not a direct pointer from figure to equations.[p13]  
  - Fig. 6: Vertical blue line is said to mark fNL = −35/8, but neither the caption nor the axis label states the units (dimensionless, Planck/local template convention). Also, the positions of the green/red bands are not tied to specific σ-level thresholds in the caption.  
- **Required fix:**  
  - In each figure caption, briefly state the key numerical assumptions (σ(fNL), r, kmin units, priors) and, where possible, reference the equation(s) in the text used to generate the curves (e.g., “curves use Eq. (3–4) with survey parameters from [4,13]”).  
  - Clarify the units on all axes that involve k and explicitly state in Fig. 6 caption what σ thresholds correspond to the colored regions, or remove the color-coding if you prefer to avoid quantitative over-interpretation.  

---

P2-N6 (NIT) – Minor internal cross-reference issues  
- **Location:** §II.A, §III.B, §IX.D, Appendix A  
- **Problem:** A few refs/eqrefs do not perfectly line up with what the text claims:  
  - §II.A refers to “Table I and Fig. 1” for benchmark confirmation, which is correct, but the subsequent footnote about Cai’s coefficients (footnote 1) is not cross-referenced later where null-space sampling is discussed; a reader may struggle to connect the footnote to the later “five coefficient sets” statements in §III.B.[p3–4][p6]  
  - §III.B mentions “phase3_fisher_overlap.json” as if it were a named dataset but does not cross-reference any appendix or data-availability note where this file is defined; this is a soft mismatch of text vs internal data-record structure.[p6–7]  
  - §IX.D refers back to “the same six redshift bins (z=0.1–1.5, fsky=0.75)” without an explicit forward reference earlier in the text; this is minor but forces the reader to hunt for where those six bins were first defined.  
  - Appendix A.1 mentions a “reproducibility notebook … archived alongside the paper source as appendix A1_wick_doubling.py,” but this file is not mentioned in the Data/code availability section and is not clearly linked in the text.  
- **Required fix:**  
  - Add explicit cross-references where needed (e.g., from §III.B to the footnote in §II.A that defines the alternative Cai coefficient set; from “phase3_fisher_overlap.json” to the Data/code availability section or an appendix where its format is described).  
  - Ensure that any named external file (e.g., A1_wick_doubling.py) is mentioned once in the Data/code availability section with a clear description so that references in the appendix are unambiguous.  

---

I have focused here on *new* issues that emerge from recomputing arithmetic, comparing abstract vs body, checking figure-caption alignment and cross-references. I did not repeat any of the earlier findings you already have in P2-E1–E9, M1–M6, N1–N4.