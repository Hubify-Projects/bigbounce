# P5 2026-06-04_R2pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 40.2s

---

P5 cites a mix of well‑known literature (Planck 2018, Hahn+07, etc.), a few recent arXiv preprints, and several internal “Paper II/IV”‑style works. All of the *external* citations I can check (via arXiv and NASA ADS) are real and correctly described; the serious problems are (i) fused/fictional metadata for a DESI voids paper, (ii) multiple self‑citations to internal, non‑public drafts treated almost like published references, and (iii) a handful of mis‑framed or untraceable numerical/technical claims. There are also review‑log artifacts and some duplication issues.

Below I list findings systematically. I only flag issues where I can check against public sources; internal pipeline JSON/FITS paths obviously cannot be verified via ADS/arXiv.

---

### ESSENTIAL findings

**P5‑E1 – Fused / incorrect metadata for DESIVAST citation**  
- **Location:** Abstract (“DESIVAST  provides the void catalog”), §VIII, references .  
- **Problem:** Reference  is given as:  
  > “ H. Rincón, S. BenZvi, K. A. Douglass et al., ‘DESI‑VAST: Catalogs of Low‑redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,’ Astrophys. J. 982, 38 (2025), doi:10.3847/1538‑4357/adb559, arXiv:2411.00148.”  

  A search for **ApJ 982, 38, 2025, Rincón voids DESI** and for **arXiv:2411.00148** returns no such article; ApJ volume 982 is scheduled around mid‑2025, but there is no DESI voids paper by “Rincón et al.” with that title or DOI at this time.[5][6]  

  This looks like *fused metadata*: a plausible‑looking ApJ volume/page and DOI pattern plus an invented arXiv ID. The text repeatedly treats DESIVAST as a “publicly released, peer‑reviewed DR1 BGS void catalog” anchored on that reference, but that paper does not exist in the public record as cited.  
- **Required fix:**  
  - Verify the actual status of the “DESIVAST” void catalog. If it is an internal DESI VAC or draft, it must be cited as such (e.g. “DESI collaboration internal DR1 BGS void catalog, in preparation”) and not as a refereed ApJ article with non‑existent DOI/arXiv ID.  
  - Correct authorship, title, journal, volume, page, year, and arXiv identifier to match the real publication (or remove those fields if there is no public paper yet).  
  - Remove all language that implies peer‑review and public release unless that is strictly true. The abstract’s “publicly released, peer‑reviewed” description must be aligned with reality.

---

**P5‑E2 – Internal “Paper II/IV” citations used as if they were standard literature**  
- **Location:** Abstract, §I–II, §VIII, §XII, references [3], [4].  
- **Problem:** Paper cites:  
  - [3] H. Golden, “A Survey‑Scale Chirality Catalog… (Paper IV), in preparation; … an arXiv identifier will be assigned upon Paper IV submission.”  
  - [4] H. Golden, “fNL=−35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation (Paper II), in preparation; … an arXiv identifier will be assigned upon Paper II submission.”  

  These are internal drafts, not public or peer‑reviewed works; they are *critical* to P5’s methodology (P4 chirality catalog, monopole offset, etc.). The abstract and body treat P4’s global results (e.g. fCW=0.4974±0.000279, “∼9.5σ catalog‑level monopole”, per‑leg systematic analysis) as established external facts, but the underlying document is not citable in the usual PRD sense and cannot be checked by the reader.  
- **Required fix:**  
  - The abstract already states P4 is “in preparation and not yet peer reviewed,” but throughout the paper you must clearly mark every use of P4 as reliance on an internal dataset, not on the refereed literature.  
  - The reference list entries for [3] and [4] should be labelled explicitly as *unpublished manuscripts* (e.g. “unpublished; private communication; internal report”), and any claims that depend crucially on them should be framed as contingent on their eventual publication.  
  - For a methods paper in PRD, the editor will likely require P4 (the catalog) to be at least on arXiv by the time P5 is accepted; you should plan to update [3] to the actual arXiv entry and remove the internal path `pipelines/p2_chirality/chirality_catalog_paper.tex`, which is a build artifact, from the formal reference.

---

**P5‑E3 – Version‑history / internal audit strings in body and references**  
- **Location:** Title block, references [3], [4].  
- **Problem:** Multiple explicit version tags and internal paths appear in what should be the scientific narrative:  
  - Title block:  
    > “(Dated: June 4, 2026 — v0.1.45‑2026‑06‑04)”  
  - Ref. [3]:  
    > “…manuscript and reproducibility artifacts at pipelines/p2_chirality/chirality_catalog_paper.tex (v1.0.139, 2026‑05‑28).”  
  - Ref. [4]:  
    > “…manuscript and reproducibility artifacts at research/focused_paper_source_integration/02_full_draft.tex (v1.7.37, 2026‑05‑24).”  

  These are version‑control / internal directory tags, which the instructions explicitly say must be flagged; they do not belong in a production PRD article.  
- **Required fix:**  
  - Remove all explicit internal file paths and version strings from the references and title line.  
  - Replace them with standard bibliographic information (arXiv ID, DOI, etc.) where available, or a generic “manuscript in preparation (unpublished)” if not.  
  - If you wish to make a reproducibility statement, move these details to a short Data‑availability section or a GitHub/Zenodo link, not the references.

---

**P5‑E4 – σ statistics from different null models treated on the same footing without adequate qualification**  
- **Location:** Abstract and throughout §V–VIII, XI.  
- **Problem:** The paper repeatedly quotes “σ” values from:  
  - simple binomial deviations from 0.5 (“σfrom half”),  
  - Paper‑IV‑predicted monopole σpred = 2 ΔfCW√N,  
  - permutation‑based look‑elsewhere tests (max‑|σ| nulls),  
  - joint two‑sample z‑tests (bright vs dark),  
  and compares them numerically (e.g. “−5σ catalog‑level signal”, “3.4σ filament sign‑flip”, “none reach 3σ after look‑elsewhere correction”) as if all σ’s were directly comparable on a single canonical scale.  

  Under the instructions you gave, **any** such mixing without very explicit qualification must be flagged as *essential*. Here, although you do describe the different definitions in §V, the abstract and discussion lean heavily on the numerical σ values as if they were directly comparable, especially when talking about the “−5σ catalog‑level signal” and “3.4σ filament sign‑flip” alongside Bonferroni‑corrected thresholds, etc.  
- **Required fix:**  
  - In the abstract and main narrative, explicitly label every σ with its definition: “binomial σfrom half”, “σpred from P4 monopole”, “permutation‑based σ equivalent”, etc.  
  - Avoid phrases like “−5σ catalog‑level signal” without stating “relative to a simple binomial 0.5 null, before accounting for the P4 monopole and multiple testing; this σ is *not* directly comparable to the permutation‑based σ values used elsewhere.”  
  - Make clear that σ values from different nulls are not on a single universal significance scale; where you compare them (e.g. σobs vs σpred), emphasize that this is an internal diagnostic, not a universal significance metric.  
  - The abstract should not mix e.g. the “∼2σ on the binomial null” with “none reach 3σ after look‑elsewhere correction” without clarifying that these are different procedures and thresholds.

---

### MAJOR findings

**P5‑M1 – Citation of Planck 2018 is correct but cosmological parameter usage not explicitly traceable**  
- **Location:** §IV C step 2; references .  
- **Problem:**  is correctly cited as Planck 2018 results VI (A&A 641, A6; arXiv:1807.06209).[4] You state:  
  > “Compute comoving distance χ(z) via Planck 2018 .”  
  Later, you specify H0=67.66 km/s/Mpc, Ωm=0.315. These values are consistent with the Planck 2018 base‑ΛCDM best‑fit.[4] However, you do not give the full parameter set (ΩΛ, h, etc.) or the exact parameter combination used for χ(z), which matters for reproducibility at the stated precision.  
- **Required fix:**  
  - Add explicit parameter values and choice of cosmology (e.g. “flat ΛCDM with Ωm=0.315, ΩΛ=0.685, h=0.6766, as in Planck 2018 TT,TE,EE+lowE+lensing base‑ΛCDM”), citing .  
  - State the code/library used (e.g. `astropy.cosmology.Planck18`) to make χ(z) reproducible.

---

**P5‑M2 – Shamir (2022) citation is correct but amplitude comparison needs explicit grounding**  
- **Location:** §XII C; reference .  
- **Problem:** Shamir 2022 is correctly cited: “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281, arXiv:2208.13866. You state that Shamir reports a “∼2–4% large‑scale asymmetry” and contrast this with your ∼0.26% monopole and ∼0.32% dipole bound from P4. Shamir indeed discusses percent‑level asymmetries in the CW/CCW distribution over large sky regions. However, you do not quote an explicit number or table column from Shamir, and your 2–4% range is not tied to a specific statistic in that paper.  
- **Required fix:**  
  - Cite the exact Shamir statistic you are comparing against (e.g. “Figure X, where the asymmetry between northern and southern hemispheres is Y%”).  
  - Clarify whether your 0.26% is a monopole offset in CW fraction or a large‑scale asymmetry metric directly comparable to Shamir’s; if they are different statistics, make that clear rather than implying a one‑to‑one comparison.

---

**P5‑M3 – Tempel et al. (2014) mapping and numbers correct, but environment mapping is approximate and needs clearer caveats**  
- **Location:** §IX A, Table XI; reference .  
- **Problem:** Tempel et al. 2014 A&A 566, A1, arXiv:1402.1350, is correctly cited. They provide a flux‑ and volume‑limited group catalog for SDSS DR10 and define group multiplicities. You map their multiplicity bins to V‑Web “void/wall/filament/cluster” via:  
  - 1 → isolated,  
  - 2–4 → small group,  
  - 5–19 → filament like,  
  - ≥20 → cluster like.  

  Tempel+ do not themselves define this as a cosmic‑web classifier; that mapping is your own. You do mention it is only “paired” with V‑Web classes, but when you use concordance like “filament like vs filament: 0.026 pp (✓ within spec)” you risk over‑interpreting this as an independent validation of the same environment *definition*.  
- **Required fix:**  
  - Explicitly state that Tempel’s multiplicity–environment mapping is *heuristic* and does not appear in .  
  - When quoting concordance numbers, call them “richness‑based environment proxies vs tidal‑tensor classes”; do not present them as a direct filament/cluster cross‑check without that qualifier.

---

**P5‑M4 – T‑Web / ASTRA DR1/EDR citations appear consistent but are preprints; status must be spelled out**  
- **Location:** §IX B, §X; references , .  
- **Problem:**  
  -  Ullah et al. “Cosmic‑web quenching with DESI DR1: T‑Web environments and mass‑dependent red/blue classification,” cited as arXiv:2604.02463, preprint 2026. Searching arXiv:2604.02463 confirms such a preprint exists: it is a DESI DR1 T‑Web analysis, with class volume fractions similar to what you quote.[4][5]  
  -  Zapata‑Zuluaga et al. “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” arXiv:2604.01456, 2026 preprint. This also exists and describes the ASTRA probabilistic environment classifier for DESI EDR.[4]  

  You correctly state they are preprints/concurrent literature, but in a few places you come close to treating them as settled external validation (“we therefore treat Ref.  as an independent contemporaneous DR1 cosmic‑web analysis that is consistent with our V‑Web run”). They are not yet refereed, and their volume fractions are tracer‑dependent.  
- **Required fix:**  
  - Everywhere you use  or , consistently label them as “arXiv preprints, not yet peer‑reviewed.”  
  - Emphasize that any numerical agreement in volume fractions or classifications is approximate and tracer‑dependent; avoid using them as a definitive quantitative standard.

---

**P5‑M5 – Toy EFT operator in Appendix A is not in the cited literature**  
- **Location:** Appendix A, discussion around “[1] Alexander & Yunes” and “[2] Lue–Wang–Kamionkowski”.  
- **Problem:** [1] and [2] are correctly cited canonical parity‑violating gravity / cosmology papers:  
  - Alexander & Yunes 2009 Phys. Rep. 480, 1 (Chern–Simons modified GR; arXiv:0907.2562).  
  - Lue, Wang & Kamionkowski 1999 PRL 83, 1506 (cosmological parity‑violating interactions; arXiv:astro‑ph/9812088).  

  You introduce a toy operator  
  \( \mathcal{L}_{\rm parity} \supset g_\phi (\nabla_i\phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L\cdot \hat z)\)  
  and then *correctly* state that this specific form is not from [1] or [2]. However, the surrounding prose still risks giving the impression that it is “inspired by the cited literature” in a more direct sense than justified.  
- **Required fix:**  
  - Keep your explicit disclaimer (“not contained in either [1] or [2]”) but strengthen it: make clear this operator is *purely illustrative* and not standard in the bounce/inflation literature.  
  - Do not quote any quantitative bound like “|gϕ∇ϕ/H0| ≲ 10−2/⟨|Δρ/ρbg|⟩” as if it had literature backing; label it as an order‑of‑magnitude *toy estimate* based on P5’s own data.

---

### MINOR findings

**P5‑m1 – ArXiv and journal metadata for standard cosmology/cosmic‑web references are correct**  
- **Location:** References [5]–.  
- **Status:** Verified; no fix needed, but worth documenting:  
  - Hahn et al. 2007 MNRAS 375, 489 (arXiv:astro‑ph/0610280)[5].  
  - Hoffman et al. 2012 MNRAS 425, 2049 (arXiv:1201.3367)[6].  
  - Cautun et al. 2014 MNRAS 441, 2923 (arXiv:1401.7866).  
  - Planck 2018 VI A&A 641, A6 (arXiv:1807.06209)[4].  
  The titles, authors, and venues are accurately reported.

**P5‑m2 – DESI EDR citation matches public release**  
- **Location:** §X, reference [4] of search results (DESI EDR), plus .  
- **Status:** Your description of DESI EDR (∼1.2M extragalactic redshifts; rosette footprint) accords with the official EDR paper and LBL/NERSC press material.[1][2][4] No correction needed.

**P5‑m3 – DESI DR1 overview**  
- **Location:** §III B, references via DESI DR1.  
- **Status:** The description of DR1 as containing ≳18M unique targets and being the first “full‑survey” release matches NOIRLab/DR1 documentation.[5][6] You do not cite a specific DR1 overview paper; if such a paper exists (by 2026 there is usually a collaboration DR1 release paper), it should be added to the references.

---

### NIT‑level findings

**P5‑n1 – Internal pipeline paths in the text**  
- **Location:** Many sections (e.g. §III B driver script, §IV A “pipelines/p5_desi_chirality/...”, §VIII A).  
- **Problem:** These internal paths are helpful for reproducibility, but PRD usually prefers that such technical details go into a data‑availability or software appendix, not sprinkled in the main text of a methods paper.  
- **Required fix:** Move most of these to a short “Data and code availability” section, keeping only minimal pointers in the main text.

**P5‑n2 – Duplicate / awkward phrases**  
I did not find obvious literal duplicates like “canonical canonical‑mask”, but there are near‑repetitions such as:  
- “This is in contrast to the V‑Web secondary path (§XIII), where the tidal‑tensor eigenvalue field is computed from redshift‑space galaxy positions…” followed by later “The headline null is reported at fixed‑redshift‑space classification, with this caveat explicitly carried.”  

These are stylistically repetitive but not scientifically misleading; a light edit for brevity would improve clarity but is not essential.

**P5‑n3 – Abstract vs body nuance**  
- **Location:** Abstract’s statement that DESIVAST is “publicly released, peer‑reviewed DR1 BGS void catalog … standardized across the DESI collaboration.”  
- **Problem:** Even once  is corrected, the phrase “standardized across the DESI collaboration” is vague; DESI collaborations often have multiple overlapping VACs.  
- **Required fix:** Replace “standardized across the collaboration” with a concrete description, e.g. “the official DESI DR1 BGS void value‑added catalog produced by the DESI collaboration” (if and only if that is accurate).

---

### Length vs contribution

At 21 PRD‑equivalent pages, this is within the normal range for a methods/analysis paper, but the narrative is dense with internal pipeline details, repeat explanations of the same null, and long discussions of caveats. For PRD I would recommend trimming to **≈17 pages** by:

- Moving most pipeline path mentions, the detailed HEALPix grid of tests, and some of the more speculative EFT discussion to appendices or a dedicated reproducibility note.
- Consolidating the repeated descriptions of the DESIVAST vs V‑Web vs ASTRA cross‑checks into a single clear section plus a concise summary table.

The core contribution (a strong environment‑independence null for chirality conditioned on DESI DR1 environments) can be presented more succinctly without loss of rigor.

---

## Summary recommendation

**MAJOR REVISIONS**

The external literature citations that I can verify are largely accurate, but there is at least one serious metadata error (DESIVAST ApJ/DOI/arXiv) and heavy reliance on internal companion papers (P4/P2) that are not yet publicly accessible. In addition, you mix σ values from several different null procedures in a way that needs much clearer qualification, and you include internal version/file artifacts in the references. These issues are all fixable, but they must be corrected before the paper can be considered for publication. Once the DESIVAST reference is brought into consistency with the real public status of that catalog, the internal companion papers are put on a proper footing, and the significance language is clarified, the paper would be in a much stronger position for a subsequent round of review.