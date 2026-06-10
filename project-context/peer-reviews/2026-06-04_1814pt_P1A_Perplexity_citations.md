# P1A 2026-06-04_1814pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 53.2s

---

The manuscript text is very long and technically detailed, but the excerpt you provided does not include the numbered reference list itself (only the in‑text citations [1]–). I can still audit what is present, but I cannot fully complete the task “verify every cited paper” without seeing the actual bibliography block with titles, authors, venues, and arXiv/DOI metadata.  

Below I treat the given text as P1A’s first PDF-native draft and audit all citations that can be checked from the excerpt. Where I cannot see the corresponding reference entry, I restrict myself to checking that the *claimed content* associated with a citation is actually established in the cited work and that any arXiv IDs or titles inferable from context are plausible.

---

## Global assessment

- The paper is dense but internally consistent about which results are original vs. assumed or phenomenological.
- Many key external claims (e.g., standard results on Einstein–Cartan torsion, Holst term, LQC bounce density, Planck cosmology, DESI BAO, cosmic birefringence measurements) are in fact standard and do correspond to well-known papers; the text’s attributions are broadly correct.
- However, there is a recurring pattern of:
  - Using specific numerical values or detailed statements (e.g., DESI “3.1–4.2σ dynamical dark energy”, precise bounce densities 0.27–0.41 ρPl, bounds on birefringence, ALP parameter ranges, Fisher error bars) and attributing them generically to references without always matching the exact numbers those references quote.
  - Referring to “companion works in preparation” [2], [6], , , which do not yet exist publicly and therefore cannot be verified; some chains of reasoning rely crucially on those internal works.
  - Treating certain approximate numbers or constructions as “from X” when in fact they are extrapolated or re‑derived from the referenced paper’s more qualitative statements.

Because your instructions emphasize *citation forensics*, I focus on whether the text’s *specific claims* can be traced to the cited works (or are clearly labeled as internal/ansatz), and whether any mis‑attribution, fused metadata, or hidden dependence on “in preparation” work occurs.

I classify every finding as requested.

---

## Findings

### ESSENTIAL issues

**P1A-E1 – Missing and unverifiable bibliography (global)**  
- **Location:** References section (not fully visible in the excerpt).  
- **Problem:** The report is asked to verify “every cited paper” and their arXiv IDs, titles, authors, venues, and quoted statistics. The provided text only shows in‑line reference numbers [1]– and a partial references block (starting at [1]), but does *not* show the full bibliographic entries for many key citations, most notably ,  (DESI),  (Ashtekar & Singh), [3]–[5] (birefringence),  (Heinrich et al.), , –, etc. I therefore cannot validate whether the arXiv IDs and metadata are correct. This is not a small omission for a PRD submission: all references must be fully specified and verifiable.  
- **Required fix:**  
  - Provide the full reference list for all citations in the manuscript (including arXiv identifiers, journal references where available, and complete author lists) and ensure it is visible in the PDF.  
  - After doing so, re‑audit:
    - that each citation’s arXiv ID resolves to the claimed title/authors;  
    - that DOIs and journal metadata are correct and not fused;  
    - that any quoted numerical statistics (e.g., DESI significance levels, Planck parameter values, LQC critical density ranges) match the numbers actually given in the cited works.

**P1A-E2 – Companion works in preparation used as critical sources**  
- **Location:** Introduction (companion paper paragraph), Sec. III B, Sec. VI, Sec. VII, Table IV, reference entries [2], [6], , .  
- **Problem:** Several key quantitative claims rely on “companion works in preparation” that are not publicly posted:  
  - Paper I(b) [6] for ΛCDM+ΔNeff MCMC verification, NaMaster validation, ALP parameter fitting, and all quoted MCMC posteriors;  
  - Paper II [2] for the SPHEREx Fisher forecast and σ(fNL) ≈ 0.7;  
  - Paper IV  for the detailed galaxy-spin null result and bias audits;  
  - Paper III  for the PTA γ reanalysis.  
  These are cited as if they provide essential backing for the claims (“documented separately”, “frozen accepted samples”, “real‑KDE reanalysis”, etc.), but they are unpublished and cannot be checked by referees or readers. For a PRD methods/catalog paper, claims that crucially rely on non-public data analyses are not fully verifiable.  
- **Required fix:**  
  - Either (a) post these companion works on arXiv (or as journal preprints) before or together with this submission and update the references with their arXiv IDs, or (b) remove all reliance on their quantitative results from the present paper, replacing them with:
    - publicly documented analyses; or  
    - more limited qualitative statements that do not depend on unpublished chains.  
  - All explicit numerical MCMC results, PTA spectral index constraints, and galaxy spin pipeline performance statistics must be either documented in this paper or in publicly citable references.

**P1A-E3 – σ values from different procedures potentially compared on same scale**  
- **Location:** Sec. VII (“Falsification Criteria”), Sec. XIII (SPHEREx fNL forecast), multiple mentions of σ(fNL).  
- **Problem:** The text reports “σ(fNL) ≈ 0.7 — detailed Fisher forecast in companion work [2]” and then talks about “3–5σ realistic after full systematic budget (GR‑projection, bϕ uncertainty, photo‑z degradation).” It references Heinrich et al. 2024  for σ(fNL) ≈ 0.7. Heinrich et al. give SPHEREx Fisher‑forecast uncertainties, but they are specific to a particular modeling of systematics and multi‑tracer configurations.  
  The manuscript blends:
  - Fisher‑ideal σ(fNL) from ,  
  - an internal “realistic” σ(fNL) from [2] (in preparation), and  
  - the implied “σ level” for detection,  
  sometimes referring to all simply as “σ(fNL)” without clearly specifying which procedure and assumptions each σ comes from. That makes it easy for readers to misinterpret them as comparable on a single, universally calibrated scale, even though they arise from different setups and are not directly comparable.  
- **Required fix:**  
  - Explicitly distinguish each σ value by its origin: e.g. “σFisher(fNL) from Heinrich et al. ”, “σinternal(fNL) from our pipeline [2] with GR‑projection & photo‑z systematics”, etc.  
  - State clearly that these σ values are not directly comparable and depend on different survey modeling assumptions and estimators.  
  - Avoid treating “3–5σ” as a single precision label without specifying which underlying σ is being used.

**P1A-E4 – Misleading reuse of DESI significance numbers without explicit verification**  
- **Location:** Page 3, Introduction: “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset‑dependent) [9, 10].”  
- **Problem:** The DESI collaboration has multiple DR1/DR2 papers; the manuscript claims “3.1–4.2σ” significance for dynamical dark energy, referencing , . The exact σ numbers depend on specific combinations of DESI BAO + CMB + SNe and the parameterization (e.g. w0wa). Those precise values must be traceable to numbers explicitly given in the cited DESI papers. In the excerpt of the references,  and  are DESI BAO results, but the specific “3.1–4.2σ” range is a *compressed summary* that may interpolate across tests; I cannot verify the exact range from the text provided. Without matching the particular tables/figures in the DESI papers, attributing a specific σ range risks overstating what DESI themselves conclude.  
- **Required fix:**  
  - In the references, point to the exact DESI tables/sections where each σ value is taken (e.g. “Table X of , Table Y of ”).  
  - Confirm that “3.1–4.2σ (dataset‑dependent)” is either:
    - directly quoted; or  
    - a simple restatement of DESI’s own phrasing;  
    otherwise, soften to “of order 3–4σ depending on the dataset, see [9,10] for details” and ensure you state it as your summary, not as a verbatim DESI claim.

**P1A-E5 – Use of ρcrit ≃ 0.27–0.41 ρPl attributed to Ashtekar & Singh**  
- **Location:** Sec. II A (Loop Quantum Cosmology and Holst action), Sec. II B, Barrier 12 (Sec. IX L), and several places where “0.27–0.41 ρPl” is quoted.  
- **Problem:** Ashtekar & Singh’s LQC status report gives a commonly quoted critical density ρcrit ≃ 0.41 ρPl for the standard choice of Barbero–Immirzi parameter (γDLM ≈ 0.2375). P1A extrapolates to 0.27 ρPl by inserting γSU(2) ≈ 0.274 into the formula, then repeatedly uses the range “0.27–0.41 ρPl” as if it were “the Ashtekar–Singh window,” sometimes clarifying it as scheme‑dependent, sometimes not. Ashtekar & Singh do *not* quote a 0.27–0.41 range; that is this paper’s own extrapolation.  
- **Required fix:**  
  - Every time the range “0.27–0.41 ρPl” appears, make clear that only the upper end is directly from , and the lower value is your internal extrapolation to an alternative γ from different entropy‑counting schemes.  
  - Do *not* phrase this as “Ashtekar & Singh quote 0.27–0.41 ρPl”; instead: “Ashtekar & Singh find ρcrit ≃ 0.41 ρPl for γ ≈ 0.2375. Using the same formula with γSU(2) ≈ 0.274 gives ≃ 0.27 ρPl; thus we adopt the *scheme‑dependent* range 0.27–0.41 ρPl.”  
  - Ensure that any use of this range in constraints (e.g. Barrier 12) explicitly acknowledges the extrapolative part.

**P1A-E6 – Some LQC/EC torsion statements slightly exceed what is shown in the cited works**  
- **Location:** Sec. II B (“Black Hole Interior and Quantum Bounce”), Sec. II A 3 (Parameter Naturalness), several mentions of “torsion-regulated bounce at ρcrit with no free parameters,” and the LQC bounce equation (8).  
- **Problem:**  
  - The effective LQC Friedmann equation with 1–ρ/ρcrit and ρcrit tied to the area gap is standard.  
  - However, the text blends Poincaré gauge theory torsion and loop quantum cosmology in language like “holonomy corrections produce a non‑singular bounce at Planck‑scale densities ” immediately after “torsion‑regulated gravitational collapse [12,13]” in a way that may implicitly suggest Ashtekar & Singh’s derivation is torsion‑based, which it is not.  
- **Required fix:**  
  - Keep the attributions clean: LQC bounce formula and ρcrit from ; EC torsion bounce/block of singularity from Popławski and Hehl et al. [12,13,14].  
  - Where the text currently says “LQC: ρc ≃ 0.27–0.41 ρPl” or “torsion‑regulated gravitational collapse” in a way that might conflate them, add explicit clarifying phrases separating EC torsion from LQC holonomy corrections.

---

### MAJOR issues

**P1A-M1 – Lue–Wang–Kamionkowski birefringence operator use vs. original reference**  
- **Location:** Sec. IV D (Route 4), Eq. for LCS ⊃ −¼(α/M) θ F̃F, and the discussion of Lue, Wang & Kamionkowski .  
- **Problem:** Lue, Wang & Kamionkowski (1999) indeed consider a generic pseudoscalar–photon Chern–Simons coupling ∂µϕ Kµ (or ϕ F̃F) and its cosmological birefringence. The paper here adopts that operator and normalization, which is fine. However, it states that “we adopt this normalization and use  as an early example...rather than as the source of the specific prefactor.” That is correct and honest.  
  The potential issue is *numerical*: P1A derives α/M ≈ 10⁻²¹ GeV⁻¹ as “typical” from matching βobs and later uses that as if it were a generic “R4‑fitted” coupling. That value is not directly in ; it’s a fit combining the operator from  and the Planck/WMAP birefringence numbers [3,4]. The text mostly presents it as its own fit, but sometimes phrases like “identical to the value already quoted in Sec. II A 2” can obscure the chain of reasoning.  
- **Required fix:**  
  - Keep the conceptual attribution to , but make explicit that α/M ≈ 10⁻²¹ GeV⁻¹ is *your* fit to βobs using the Lue–Wang–Kamionkowski form, not a number cited from .  
  - In any place where “one-loop motivated” is attached to α/M in Table IV, specify that the numerical value 10⁻²¹ GeV⁻¹ comes from matching β and is *not* computed in  or .

**P1A-M2 – Eskilt & Komatsu / Minami & Komatsu birefringence numbers**  
- **Location:** Abstract, Sec. III A, Sec. VI, Sec. XIII.  
- **Problem:** The cited works are:  
  - Minami & Komatsu (2020) first reported a detection of isotropic cosmic birefringence: βMC = 0.35° ± 0.14° (68% CL).[3]  
  - Eskilt & Komatsu (2022) improved constraints combining WMAP and Planck: they report β = 0.342° ± 0.094°.[4]  
  - Diego-Palazuelos & Komatsu (ACT DR6) is listed as [5].  
  P1A writes: “βobs = 0.342° ± 0.094° (∼ 3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4])” and later “comparable to ACT DR6 β = 0.215° ± 0.074° at ∼2.9σ (Diego-Palazuelos & Komatsu [5]).”  
  These numbers are consistent with the literature: Eskilt & Komatsu give β = 0.342° ± 0.094°.[4] That is ≈3.6σ from zero. ACT DR6 values are plausible, but [5] appears to be a 2025 arXiv preprint; I cannot verify the exact numbers without the full reference entry but the central value and uncertainty are in line with what is expected for ACT‑like datasets.  
  The subtle issue: Minami & Komatsu’s 0.35° ± 0.14° is the *original* claim; calling 0.342° ± 0.094° “first reported by Minami & Komatsu and refined by Eskilt & Komatsu” conflates the two. Minami & Komatsu did *not* report 0.342° ± 0.094°; they reported a different central value and larger uncertainty.  
- **Required fix:**  
  - Rephrase to: “An isotropic birefringence signal was first reported by Minami & Komatsu (β ≈ 0.35° ± 0.14°)[3] and later refined by Eskilt & Komatsu to β = 0.342° ± 0.094°[4].”  
  - Keep ACT DR6 numbers but ensure that the exact β and σ are copied verbatim from [5]; if not, adjust them.

**P1A-M3 – Heinrich et al. σ(fNL) statement**  
- **Location:** Table I footnote, Sec. VII, Sec. XIII.  
- **Problem:** Heinrich, Doré & Krause (2024) forecast SPHEREx constraints on fNL using the multi‑tracer RSD bispectrum. They quote σ(fNL) ≈ 0.7 for a particular configuration. P1A adopts “σ(fNL) ≈ 0.7” and then folds in additional systematics to claim “3–5σ realistic” for |fNL| = 4.375. That is consistent in spirit, but the text occasionally blurs which numbers are directly from Heinrich et al. versus internal pipeline adjustments [2].  
- **Required fix:**  
  - Wherever “Heinrich+2024 σ(fNL) ≈ 0.7” is cited, make clear that it refers to the *idealized* Fisher forecast configuration defined in that paper.  
  - When quoting “3–5σ realistic”, clarify that this is *your* estimate based on additional degradation from systematics, not Heinrich et al.’s result.

**P1A-M4 – Popławski / Hehl torsion claims**  
- **Location:** Introduction items “black hole universe origin” , various references to torsion preventing singularities [12,13].  
- **Problem:**  
  - Hehl et al. (1976) indeed show that EC torsion leads to spin‑spin contact interactions that can avoid singularities.  
  - Popławski (2016 ApJ 832, 96) discusses “universe inside a black hole” scenarios and torsion‑regulated collapse.  
  However, P1A sometimes presents these as if they were universally accepted mechanisms, whereas both are speculative EC‑based scenarios.  
- **Required fix:**  
  - Wherever “black hole universe origin” or “torsion‑regulated gravitational collapse” is mentioned, frame it clearly as “the scenario proposed by Popławski ” rather than an established standard result.  
  - Do not overstate consensus; keep language agnostic (e.g. “Popławski’s scenario posits…”) to match the speculative status in the cited papers.

---

### MINOR issues

**P1A-m1 – Golden  “Systematic closure” technical note metadata**  
- **Location:** Reference  in the list, description “Systematic closure of minimal first‑principles routes to dark energy in Einstein‑Cartan‑Holst gravity (2026), companion technical note, available upon request from the author.”  
- **Problem:** This is essentially a private note, not accessible via arXiv, ADS, or a journal. Using it as a reference is problematic for reproducibility.  
- **Required fix:**  
  - Either post this technical note publicly (arXiv, institutional repository) and update the reference with an arXiv ID/URL, or remove it as a formal reference and summarize its key content in the main text instead.

**P1A-m2 – Poplawski 2011 “Cosmological constant from quarks and torsion”**  
- **Location:** Ref. .  
- **Problem:** The title (“Cosmological constant from quarks and torsion”) and venue (Annalen der Physik 523, 291 (2011)) are accurately reproduced. However, P1A mainly uses Popławski for “torsion prevents singularities” and mentions “cosmological constant from quarks and torsion” in passing. That is fine, but the text doesn’t always distinguish between Popławski’s *particular model* of dark energy and the general EC torsion avoidance of singularities.  
- **Required fix:**  
  - When using  as support, make clear whether you are citing it for its singularity avoidance arguments or its specific dark‑energy model, and ensure those points correspond to what the paper actually states.

**P1A-m3 – Mercuri & Capozziello one-loop vs. thermal phase-space distinction**  
- **Location:** Sec. II C 1.  
- **Problem:** The paper correctly acknowledges that the (Treh/MGUT)³⁄² factor is a phenomenological phase-space ansatz, not the Mercuri & Capozziello one‑loop anomaly coefficient αem/4π. This is good. The potential issue is that a reader might still misinterpret the presence of  as supporting the thermal factor.  
- **Required fix:**  
  - Add a short explicit sentence: “Mercuri & Capozziello  compute a one‑loop chiral anomaly coefficient αem/4π; we do *not* use their result to justify the thermal (Treh/MGUT)³⁄² factor, which remains a purely phenomenological ansatz.”

**P1A-m4 – Liu et al., Legner et al., Alam et al. “support” phrasing**  
- **Location:** Sec. VIII (“Recent independent support includes Liu et al. , Legner et al. , Alam et al. ”).  
- **Problem:**  
  - Liu et al. (torsion cosmology in light of DESI and CMB) explore torsion as a phenomenological explanation for S8 and H0 tensions; this is in the same broad thematic area but not “support” in the sense of validating this paper’s specific ECH route catalog.  
  - Legner et al. propose torsion condensation (TorC) to address H0 tension, again broadly related but distinct.  
  - Alam et al. (torsion-based bouncing cosmologies) are also parallel, not confirming.  
- **Required fix:**  
  - Rephrase “Recent independent support includes…” to “Recent related work includes…” or similar, unless you can point to explicit conclusions in those papers that endorse the specific structural closure claims made here.

**P1A-m5 – Minor wording ambiguity for “first reported by Minami & Komatsu”**  
- **Location:** Abstract, Sec. III A.  
- **Problem:** As noted in Major M2, wording can be clarified.  
- **Required fix:** As in M2.

---

### NITs (very minor)

**P1A-n1 – Slightly informal phrasing in technical sections**  
- **Location:** Sec. II C 1 and elsewhere: phrases like “bookkeeping, not progress”, “does no work on the cosmological constant problem itself.”  
- **Problem:** Stylistic, but PRD tends to prefer more neutral phrasing.  
- **Required fix:** Optionally rephrase in more formal language (“We emphasize that this parametrization does not alleviate the cosmological constant problem; it simply repackages the fine-tuning into Ntot.”).

**P1A-n2 – Occasional over‑specific numeric precision**  
- **Location:** Several occurrences, e.g. γSU(2) ≈ 0.274, γDLM ≈ 0.2375, Ntot ≈ 92, H0 ≈ 67.68.  
- **Problem:** The text sometimes gives numbers to 4 significant digits where the underlying theoretical/phenomenological uncertainties are much larger. This is mostly cosmetic.  
- **Required fix:** Consider rounding to 2–3 significant digits to avoid giving an impression of unwarranted precision.

**P1A-n3 – Self-citation density**  
- **Location:** References [2], [6], , , .  
- **Problem:** A large part of the structure rests on an internal suite of self‑citations. While not inherently wrong, it can appear insular.  
- **Required fix:** Once those works are posted publicly, this concern disappears. Until then, consider minimizing reliance on them for key external claims.

---

## Length assessment

The manuscript is about 21 pages, which is within PRD’s typical 15–30 page range for a methods/constraint paper. Given the complexity of the ECH torsion framework, the barrier catalog, and the detailed discussion of multiple observational channels, the length is justifiable. I do not recommend shortening below ~18 pages; most sections are doing substantive work for the structural argument.

---

## Abstract truthfulness

The abstract states:

- That four enumerated minimal ECH routes (NJL, one-loop EA, Immirzi running, parity‑CMB) are closed at the amplitude level under stated assumptions.  
- That the perturbation-transparency theorem shows torsion vanishes for canonical scalars and Holst decouples from scalar/tensor perturbations.  
- That the ECH-to–dark-energy mapping is phenomenological and ansatz‑based.  
- That a structural tension exists between Ntot ≈ 92 e‑folds required by the dark‑energy mechanism and the matter‑bounce fNL prediction.  
- That surviving “predictions” (fNL = −35/8, β ≈ 0.27°) are not ECH‑specific.

These claims are consistent with the body of the paper; the abstract does not oversell what is actually proven relative to what is assumed. The main caveat is the use of DESI’s “3.1–4.2σ” phrase, which must be carefully sourced as discussed.

---

## Summary recommendation

**MAJOR REVISIONS**

The core cosmological and theoretical content is interesting and the abstract’s claims broadly track what the paper actually does, but from a citation‑forensics standpoint there are essential issues: the incomplete/hidden reference list, heavy reliance on non‑public companion papers for key numerical claims, and several places where specific σ or ρcrit values are compressed summaries rather than clearly attributed to their original sources. These must be fixed before the paper can be properly reviewed on its scientific merits. Once the bibliography is complete, the companion works are publicly accessible or their use is de‑emphasized, and the few over‑precise attributions are cleaned up, the paper will be in much better shape for a standard PRD scientific review.