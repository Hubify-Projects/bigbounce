# P1B 2026-06-04_R6clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 45.4s

---

P1B-E1 (ESSENTIAL) – References section, throughout  
Problem: Several key references are listed as “(in preparation)” or have nonstandard internal report IDs rather than established bibliographic metadata, and there is no evidence they currently exist on arXiv or in journals. Specifically:  
- [1] “H. Golden, Structural Closure of Einstein–Cartan–Holst Dark Energy: … (in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume.”  
- [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].”  
- [4] “H. Golden, fNL = −35/8 Forecast: SPHEREx … (in preparation) (2026), hUBIFY-2026-002; companion paper, this volume.”  
- [5] “H. Golden, Spectrally Unusual Sources at Scale… (in preparation) (2026), hUBIFY-2026-003; companion paper, this volume.”  
- [6] “H. Golden, Galaxy Chirality at Scale… (in preparation) (2026), hUBIFY-2026-004; companion paper, this volume.”  
-  “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”  
-  “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: … Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”  

arXiv identifiers starting with “25” (e.g., 2503.*, 2507.*, 2509.*) correspond to future years and do not resolve on arXiv at present; likewise there are no EPJC or PRD entries with these exact metadata yet. These are forward‑projected citations, not real, citable literature. For the “hUBIFY-2026-00x” series, there is no evidence on arXiv or ADS yet; they function as internal report IDs, but the paper relies on them as if they were public.  

Required fix:  
- Replace all “in preparation” / forward‑dated / non‑resolving arXiv and journal placeholders with actual public references (arXiv IDs, DOIs, or journal info) that can be verified, or clearly mark them as unpublished internal manuscripts that are not used as empirical evidence.  
- For results crucial to this paper that depend on these companion papers (especially [1]), either (a) provide real, accessible preprints, or (b) confine claims to what is actually shown in the present manuscript and remove cross‑paper dependence for load‑bearing statements.  
- Remove speculative arXiv IDs (e.g., arXiv:2509.13654, 2507.04265, 2503.14738) and replace with correct IDs once those preprints exist; until then, cite only the collaboration names plus “in preparation” without fake identifiers, and do not base quantitative statements on them.  

---

P1B-E2 (ESSENTIAL) – Abstract, p.1, claims tied to non‑public Paper I(a)  
Problem: The abstract begins: “We report the technical verification material for the Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program of Paper I(a) [1]. The main paper establishes 14 independent structural constraints… The present paper documents the three numerical analyses that support and contextualize those results.” The structural closure theorem, “14 independent structural constraints,” and “perturbation-transparency theorem” are all in Paper I(a), which is only cited as “(in preparation)” and appears not to be publicly available. Yet the present paper presents itself as a “Technical Verification Companion” giving numerical support to that non‑public work.  

Required fix:  
- Revise the abstract and Introduction to ensure all *load‑bearing* claims are either proved in this paper or supported by published, verifiable references.  
- If Paper I(a) is not yet publicly available, remove language implying that this paper completes or “supports” established structural results. Instead, present the analyses as self‑contained methods / tests, with only minimal forward‑looking reference to a forthcoming theoretical paper.  
- Alternatively, ensure Paper I(a) is on arXiv or accepted in a journal with stable metadata, and update the citation accordingly.  

---

P1B-E3 (ESSENTIAL) – Birefringence statistics and quoted σ values  
Problem: The manuscript repeatedly mixes significance levels from different sources and procedures and occasionally presents them in a way that risks treating them as comparable:

- Abstract: “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2, 3];a the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements.”  
- Sec. IV (Data Methods: CMB E-B Analysis): “The high pipeline-recovery SNR figures (e.g., 20.32, 25.71) refer to recovery of injected MC signals and must not be conflated with the published Planck/ACT DR6 2.4–2.9σ sky detection.”  
- Sec. VI: “β = 0.342◦ ± 0.094◦ (3.6σ) [2]”, “βcombined = 0.241◦ ± 0.061◦ (3.9σ).”  

The author does state in several places that the pipeline SNR is *not* a sky detection, which is good. However, no explicit check is provided that the quoted “2.4–2.9σ” for Planck/ACT, “3.6σ” for Eskilt & Komatsu, and “3.9σ” for the combined Planck NPIPE + ACT DR6 value are directly traceable to the cited papers and use consistent conventions (e.g., treatment of systematics, joint likelihood vs approximate inverse‑variance combination). In particular:  
- Eskilt & Komatsu (PRD 106, 063503; arXiv:2205.13962) does report β ≈ 0.342° ± 0.094° and 3.6σ, so that part is consistent.  
- Diego-Palazuelos et al. (arXiv:2201.07682) report β = 0.30° ± 0.11° from Planck PR4, but the text here also refers to ACT DR6 results [3] with 2.4–2.9σ; the claimed future reference arXiv:2509.13654 cannot be checked.  
- The “3.9σ” combined value is explicitly described as a simple inverse‑variance combination that neglects shared systematics; it is not in the cited literature. That is a derived quantity in this paper, not a “published” σ, and could easily be misread as a literature number.

Required fix:  
- Explicitly distinguish in the text between σ values taken directly from published fits (with appropriate references whose IDs are real) and σ values computed in this paper (e.g., the 3.9σ inverse‑variance combination).  
- Clarify that the 3.9σ is a *naive* combination done here, not a result from [2] or [3], and that the headline 3.6σ WMAP+Planck value is the only one used as the observational benchmark.  
- Once ACT DR6 birefringence results are actually public (with real arXiv ID), update the references and check that the quoted 2.4–2.9σ range matches their abstract or tables.  
- Maintain and possibly strengthen the existing warnings that pipeline SNRs are of a different nature and not comparable to sky detection σ-values.  

---

P1B-E4 (ESSENTIAL) – Citing future DESI DR2 results with fake arXiv IDs  
Problem: The paper makes substantive claims based on DESI DR2 and connects them to forward‑projected references:

- Sec. III, “Independent cross-validation”: “Liu et al.  constrained an EC torsion model using DESI DR2  + Pantheon+  + DES-SN5YR  + Planck 2018, finding torsion preferred by AIC (∆AIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.”  
- Reference : “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”  

As of now, the DESI collaboration has a DR1 BAO cosmology paper (Adame et al., arXiv:2404.03002), not DR2 with the quoted metadata. The arXiv ID 2503.14738 is not valid yet. The comparative numbers “0.5σ in H0 and 0.4σ in σ8” cannot be verified because the referenced Liu et al. torsion paper and DESI DR2 summary do not exist.  

Required fix:  
- Remove or substantially soften any quantitative cross‑validation claims against nonexistent DESI DR2 / Liu et al. results. At most, these can be presented descriptively as “anticipated” comparisons, not as established agreement at “0.5σ.”  
- Once actual DESI DR2 and torsion papers are available, insert correct citations and re‑compute the comparison to ensure the quoted σ offsets match the published numbers. Until then, those comparisons should not appear in a PRD article.  

---

P1B-M1 (MAJOR) – Over‑reliance on “companion” papers for methodology and interpretation  
Section: Introduction and multiple sections referencing Papers I–IV  

Problem: This “companion” article frequently refers to other works by the same author (Papers I–IV) as already‑established and uses them to motivate the choice of tests and their interpretation—for example:  

- “The main paper establishes 14 independent structural constraints closing minimal-ECH dark-energy routes and proves a perturbation-transparency theorem…”  
- “The SPHEREx multi-tracer Fisher forecast is in Paper II [4]. The multi-survey anomaly catalog is in Paper III [5]. The galaxy chirality catalog is in Paper IV [6].”  
- The DESI DR2 w0–wa chain and “quintom-B” interpretation are tied back to Paper I(a) (§ Structural Tension).  

However, all of [1], [4], [5], [6] are described as “in preparation” with only internal IDs. The present paper is nominally about technical verification, but some of the interpretive weight (e.g. “canonical quintom signature,” “bounce-class compatibility”) rests on those unpublished analyses. This creates a situation where important context and tests are effectively inaccessible to the reader.  

Required fix:  
- Make the present paper self‑contained: either provide enough methodological detail and derivations here to justify the cosmological interpretations (quintom vs ΛCDM, bounce‑class connection, etc.) or explicitly label those interpretations as speculative and not central to this companion.  
- Treat all “in preparation” companion papers as *unpublished* background; do not rely on them for claims that go beyond what is clearly demonstrated in this manuscript’s own tables and figures.  

---

P1B-M2 (MAJOR) – Mis‑cited Planck reference and NPIPE usage  
Section: Sec. IV, Sec. V, References ,   

Problem: The paper distinguishes correctly between Planck 2018 legacy (PR3) and NPIPE (PR4) in words, but the Planck cosmology reference  is:  

-  “Planck Collaboration, N. Aghanim, et al., Planck 2018 results. VI. cosmological parameters, Astronomy & Astrophysics 641, A6 (2020), arXiv:1807.06209 [astro-ph.CO].”  

That is the PR3 parameters paper (A&A 641 A6), not the PR4/NPIPE temperature–polarization data products used for birefringence and, in some places, for cosmological likelihoods. For cosmic birefringence, the relevant Planck PR4 paper is Diego-Palazuelos et al. (arXiv:2201.07682), which is indeed cited as , but the text sometimes describes “Planck 2018 NPIPE” as though  were the source.  

Required fix:  
- Ensure references cleanly distinguish between:  
  - Planck 2018 base cosmology (Aghanim et al., 2018, arXiv:1807.06209),  
  - Planck PR4/NPIPE birefringence analysis (Diego-Palazuelos et al., arXiv:2201.07682), and  
  - Any Planck PR4/NPIPE parameter products or likelihoods actually used in Cobaya.  
- Where “Planck 2018 NPIPE” is mentioned, cite the appropriate NPIPE data paper(s) in addition to or instead of .  

---

P1B-M3 (MAJOR) – Length and scope relative to contribution  
Section: Entire paper (10 pages)  

Problem: For a “Technical Verification Companion,” the paper is quite dense and long relative to what is actually contributed: three null / consistency‑check analyses, largely using stock codes and literature datasets, plus extensive narrative around convergence counts, YAML details, and internal audit logs. Some of this belongs in supplementary material or the GitHub documentation rather than in a PRD article. There is also an entire “Claims Classification” table (Table III) and large blocks in Appendix A/C that mainly restate repository contents.  

Required fix:  
- Condense the main text by removing or moving to Supplemental Material:  
  - Detailed chain‑length arithmetic and burn‑in reconciliation,  
  - Implementation‑map descriptions,  
  - HuggingFace dataset logistics,  
  - Internal claims classification table.  
- Focus main sections on: (i) precise definitions of the tests, (ii) key numerical outputs, and (iii) how these support or constrain the theoretical program. A reasonable target would be ≤6–7 pages for the main text plus a short appendix.  

---

P1B-M4 (MAJOR) – Use of “verified,” “confirmed” language for internal computations  
Section: Multiple places including Table III and text around MCMC runs  

Problem: The paper repeatedly uses terms like “Verified,” “confirmed,” “we report this as a null-consistency cross-check,” “confirms the algebraic pseudo-Cℓ E → B deconvolution” when describing the author’s own code runs. Table III labels internal numbers as “Verified” in a way that mimics an external audit, but they are simply the author’s own reproducible computations. This type of terminology risks over‑selling the level of validation from independent literature.  

Required fix:  
- Reserve “verified” or “confirmed” for statements that are explicitly checked against external, published results (e.g., reproducing Planck ΛCDM parameters within stated uncertainties).  
- For purely internal diagnostics (e.g., NaMaster recovery of injected β, ALP MCMC), describe them as “obtained,” “computed,” or “we find,” not “Verified.”  
- In Table III, either remove the “Status” column or change “Verified” to something more neutral like “Computed in this work” and only mark entries as “External” for literature values.  

---

P1B-M5 (MAJOR) – Abstract accuracy and emphasis  
Section: Abstract  

Problem: The abstract is mostly accurate about what is *done* (three analyses; null ∆Neff; pipeline recovery of β; ALP consistency). However, it frames these as “technical verification material for the ECH spin-torsion cosmology no-go program of Paper I(a),” which is not publicly available, and thus suggests that a major no‑go theorem is “supported” here. In reality, all three analyses are either null tests (ΛCDM+∆Neff), code validation, or non‑distinctive consistency checks (ALP birefringence). No numerical result in this paper uniquely supports or falsifies the ECH framework relative to standard GR+ALP or ΛCDM.  

Required fix:  
- Rephrase the abstract to clearly present the work as:  
  - a stock ΛCDM+∆Neff check that finds consistency with ΛCDM and does not resolve tensions,  
  - a NaMaster pipeline validation on Planck Commander, and  
  - an ALP model whose parameters can accommodate observed cosmic birefringence but are not unique to ECH.  
- Explicitly state in the abstract that these are *non‑diagnostic* for ECH itself and that the structural no‑go result is presented elsewhere and not proved here.  

---

P1B-M6 (MAJOR) – “Quintom-B” and “98.6%” correction referencing non‑verifiable earlier counts  
Section: Sec. III, around “Physics interpretation (Table II)”  

Problem: The text says: “An earlier count erroneously quoted ‘98.6% quintom-B’ weight; in the actual converged chain there are zero free-w0 wa samples at the LCDM point, the chain is centered well into quintom-B territory at w0 + wa ≈ −1.48.” This references an earlier internal error, but that earlier work is not accessible and the origin of the “98.6%” figure is not documented in a citable way. The current paper also uses that chain to argue for a canonical “quintom-B” signature as part of the bounce / pre‑Big‑Bang scenario, again tying interpretation to a non‑public structural analysis.  

Required fix:  
- Remove internal history (“earlier count erroneously quoted…”) from the main text; just present the current chain properties and uncertainties.  
- If the “quintom-B” interpretation is important for the ECH program, either briefly summarize the theoretical mapping from w0, wa to the bounce model here with proper references, or move the interpretive language to the forthcoming theoretical paper.  

---

P1B-m7 (MINOR) – Stock codes and versions vs cited papers  
Section: Throughout, especially ΛCDM+∆Neff description, NaMaster section, Cobaya references ,   

Problem: The paper states specific versions (Cobaya v3.6.1, CAMB v1.6.5, NaMaster as per ) but the Cobaya and CAMB references are generic. It is not strictly wrong, but for reproducibility the mapping between the cited Cobaya paper  and the version used should be clear. Similarly, NaMaster  is cited but the text uses some newer options (e.g., purification flags) that may have been introduced after the publication.  

Required fix:  
- Add explicit version numbers in the data‑methods section where first citing Cobaya and CAMB, and clarify that the implementations follow the published code but with these particular versions.  
- Optional but helpful: mention the NaMaster git commit or release tag used for the pseudo-Cℓ runs in Appendix A.  

---

P1B-m8 (MINOR) – Internal audit and AI‑assistant acknowledgments in body  
Section: Acknowledgments  

Problem: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation.” This kind of statement is increasingly common, but journals differ in how they want AI assistance documented. PRD’s policies may require specific wording or placement (often in acknowledgments or a separate authorship statement), but not typically the level of detail given here (naming a particular model and implying “systematic analysis” assistance).  

Required fix:  
- Check PRD’s policy on AI tools and rephrase the acknowledgment to conform, e.g., “The author used AI‑assisted tools for editing and code‑debugging; responsibility for all scientific content rests with the author.”  
- Remove implication that an AI assistant played an independent role in “systematic analysis.”  

---

P1B-m9 (MINOR) – Forward-looking statements about CMB-S4 / LiteBIRD  
Section: Abstract, Conclusions, Sec. VI  

Problem: Statements like “CMB-S4 (σ(Neff ) ∼ 0.03) will provide the first precision test” and “LiteBIRD is projected to achieve σ(β) ≈ 0.03°” are drawn from other forecast papers (e.g., LiteBIRD ). They appear reasonable, but the text sometimes interpolates them into the narrative as if they are guaranteed rather than forecast.  

Required fix:  
- Ensure each such claim explicitly references the forecast source and uses language like “is projected to,” “is forecast to,” not “will provide” without qualification. E.g., “According to , LiteBIRD is projected to reach σ(β) ≈ 0.03°.”  

---

P1B-n1 (NIT) – Redundant / inconsistent capitalization and notation  
Section: Throughout  

Problems:  
- Mixed “ΛCDM+∆Neff” vs “LCDM+∆Neff” (e.g., “LCDM point” in Table II caption).  
- Occasional inconsistent spacing in equations and variables, e.g., “H0 km/s/Mpc” vs “km s−1 Mpc−1”, and “w0 wa” vs “w0, wa”.  

Required fix:  
- Standardize on a single notation: ΛCDM everywhere, and consistent units formatting for H0.  
- Ensure parameters like w0, wa, S8, σ8 are consistently formatted and spaced.  

---

P1B-n2 (NIT) – Duplicate or awkward phrases  
Section: Several places  

Examples:  
- “What is NOT in this paper.—The 13 logically-independent structural barriers, the perturbation-transparency theorem, the 14-barrier table…” awkwardly repeats “barriers.”  
- “Stock CAMB proxy ̸= ECH theory module” in Table III is clear but informal.  

Required fix:  
- Tighten wording for clarity, e.g., “What is not in this paper.—The 13 structural barriers, the perturbation-transparency theorem, and the 14-barrier summary table…”  
- Consider slightly more formal phrasing in the claims table, e.g., “Stock CAMB proxy distinct from full ECH theory module.”  

---

P1B-n3 (NIT) – Claims Classification table placement  
Section: Table III  

Problem: The claims classification table is unusual for a PRD paper and duplicates text already present in the conclusions and abstract. It is not wrong but somewhat out of place.  

Required fix:  
- Consider moving Table III to an appendix or to the repository documentation instead of the main body.  

---

P1B-n4 (NIT) – Clarify that some arXiv numbers are placeholders  
Section: References [1], [3]–[6], ,   

Problem: If the author insists on including future‑work references before public release, the current formatting (e.g., “arXiv:2509.13654”) strongly suggests these IDs already exist.  

Required fix:  
- Until actual submissions are made, remove all speculative arXiv identifiers and replace with neutral text like “preprint in preparation (not yet on arXiv).” This will prevent confusion and failed lookups.  

---

## Summary recommendation

MAJOR REVISIONS

Core issues are the use of non‑existent / forward‑projected references (including fabricated arXiv IDs), the dependence of this “verification companion” on an unpublished main theoretical paper, and the way some quoted σ‑level claims and cross‑validations cannot currently be checked against the cited literature. Once the citations are grounded in actual public papers (or appropriately downgraded), and the manuscript is streamlined and made more self‑contained, it could be a solid methods note; but in its current form it does not meet PRD standards for citation accuracy and verifiability.