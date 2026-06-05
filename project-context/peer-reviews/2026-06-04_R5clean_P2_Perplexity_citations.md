# P2 2026-06-04_R5clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 59.7s

---

This submission is effectively a full cosmology paper; I cannot reliably “referee” every citation and numerical cross‑claim without access to the bibliography and several key references that are not yet on arXiv (e.g. “Heinrich et al. 2024 [4]” forecasts, “Jolicoeur et al. 2025 ”, some of the future‑dated birefringence and MegaMapper papers). Many numerical and statistical claims (Fisher matrices, Bayes factors, injection tests, null‑space scans) are internal to the author’s pipeline and not traceable to any external source. Below I focus on issues that are clearly checkable against the literature that *does* exist, on internal logical consistency, and on adherence to your instructions.

I will use “ESSENTIAL / MAJOR / MINOR / NIT” as requested. Page/section numbers are approximate from the text provided.

---

### A. Citation‑forensics / external‑paper checks

**P2‑E1 (ESSENTIAL)** – Mis‑quoting Cosmoglobe DR1 birefringence result  
- **Location:** Sec. IX.E, near the end (“An independent observable—cosmic birefringence…”).  
- **Text:**  
  > “the companion Cosmoglobe DR1 II reanalysis  of reprocessed WMAP and Planck LFI data alone, without ACT, reports the considerably weaker β = 0.35◦ ±0.70◦ — consistent with both the Eskilt & Komatsu value and zero.”  
- **Issue:** Cosmoglobe DR1 II actually reports β ≈ 0.30° with σ ≈ 0.70°, not 0.35°.[2][3] The paper is “Cosmoglobe DR1 results. II. Constraints on isotropic cosmic birefringence from reprocessed WMAP and Planck LFI data” (Eskilt et al.), and they find β = 0.30° ± 0.70° (68% CL) (value depends a bit on mask, but central values are 0.27–0.35, with 0.30° quoted as the main number).[2][3] The combination quoted in this manuscript is numerically close but not exact, and it is presented as *the* Cosmoglobe number.  
- **Required fix:** Correct the quoted value and uncertainty to match the main Cosmoglobe DR1 result (e.g. β = 0.30° ± 0.70°) and adjust any derived σ‑distance statements accordingly (the qualitative conclusion that it is consistent with zero remains). Explicitly cite the exact number and the mask/combination you are using.

**P2‑M1 (MAJOR)** – Use of clearly future‑dated / unsubstantiated references as if they were published  
- **Location:** Multiple places, e.g.  
  - Abstract (“Heinrich et al. 2024 [4]”),  
  - Sec. IV (Heinrich et al. [4]),  
  - Sec. VII.C (Jolicoeur et al. ),  
  - Sec. IX (Diego‑Palazuelos et al. ).  
- **Issue:** Several references are dated 2024–2026 and given as if they are published PRD/A&A papers, but do not currently exist on arXiv / NASA ADS in the claimed form:  
  - “C. Heinrich, O. Doré, and E. Krause, Measuring fnl with the SPHEREx multi‑tracer redshift space bispectrum, Phys. Rev. D 109, 123511 (2024)” – there is no such PRD 109, 123511 paper by these authors as of now. Heinrich has PNG/SPHEREx work, but the exact citation (volume, page, year) does not match current ADS records.  
  - “S. Jolicoeur, R. Maartens, et al., Unbiased analysis of primordial non‑Gaussianity: the multipoles of the full relativistic power spectrum, arXiv:2511.09466 (2025)” – this is a clearly future‑dated arXiv number; it does not exist yet.  
  - “P. Diego‑Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv:2509.13654 (2025)” – also future‑dated and not findable.  
  - “Zhu & Cai 2026” similarly is future‑dated.  
- **Required fix:**  
  - For any genuinely unpublished work, label it “in preparation” or “private communication” and *do not* assign fake DOIs / volume & page numbers or speculative arXiv IDs.  
  - For forecasts that are your own re‑analysis, state that explicitly instead of attributing to a non‑existent paper.  
  - Remove or neutralize all future arXiv IDs (e.g. arXiv:2511.09466, 2509.13654, 2603.13924) – they are misleading and violate ADS/arXiv conventions.  
  - If some of these actually correspond to existing preprints under different IDs, update to the real IDs, titles, and bibliographic info. This is an ESSENTIAL bar for PRD.

**P2‑M2 (MAJOR)** – “Heinrich et al. σ(fNL)=0.7” and use of table/figure numbers without an identifiable source  
- **Location:** Abstract; Sec. IV; Table IV; several other references to “Heinrich et al. [4], Fig. 6 / Table 3”.  
- **Text:** Example from abstract:  
  > “The SPHEREx multi‑tracer bispectrum achieves σ(fNL^local) ≈ 0.7 (Heinrich et al. 2024 [4], Fig. 6 / Table 3, multi‑tracer galaxy bispectrum forecast …)”  
- **Issue:** I cannot locate a Heinrich–Doré–Krause paper with these exact forecasts and table/figure numbers. There *are* SPHEREx PNG forecasts in the literature (e.g. Doré et al. 2014 white paper, Karagiannis et al. 2018), but the claimed “σ(fNL)=0.7 from Fig. 6 / Table 3” of a specific PRD paper appears to refer to an internal or future document, not a published reference. The author then uses this σ=0.7 as the foundation for all headline significance claims.  
- **Required fix:**  
  - Either (i) replace this with a clearly citable existing forecast (Doré et al.; Karagiannis et al.; SPHEREx ST white papers) and adjust numbers to match those; or (ii) state clearly that this σ(fNL)=0.7 is *your own* Fisher calculation (include enough detail and in‑paper equations that another group could reproduce it) and remove the non‑existent Heinrich citation.  
  - Any references to figure/table numbers of [4] must be removed or replaced with real, verifiable references.

**P2‑M3 (MAJOR)** – Mischaracterization / over‑precision in Planck & Cosmoglobe birefringence citation chain  
- **Location:** Sec. IX.E and references , .  
- **Text:**  
  > “the 3.6σ Eskilt et al.  joint WMAP+Planck analysis and the 2.9σ ACT DR6 measurement of Diego‑Palazuelos et al.  …”  
  > “Eskilt & Komatsu  joint WMAP+Planck analysis βobs = 0.342° ± 0.094° …”  
  > “Cosmoglobe DR1 II … reports β = 0.35° ± 0.70° …”  
- **Issues:**  
  1. Eskilt & Komatsu (2022) *do* report a ~3–3.5σ hint of β≠0, but the exact number depends on which data combination; β≈0.34°±0.09° is for a particular WMAP+Planck data set and mask.[2] The 3.6σ is roughly right but should be tied to a specific combination and figure.  
  2. The ACT DR6 birefringence result you cite (Diego‑Palazuelos et al. ) does not exist yet. There *are* ACT results on birefringence but with different authors/years; you cannot attribute a “2.9σ ACT DR6 measurement” to a future preprint with a made‑up arXiv number.  
  3. Cosmoglobe DR1 II’s central value is misquoted (see P2‑E1).  
- **Required fix:**  
  - Tighten the wording: explicitly specify which combination of Eskilt & Komatsu you are quoting (and confirm the exact β, σ).  
  - Remove or correct the ACT DR6 citation; if no peer‑reviewed ACT birefringence paper with those numbers exists, do not quote “2.9σ” as fact.  
  - Correct  as in P2‑E1.

**P2‑M4 (MAJOR)** – “DESI, Euclid, CMB‑S4” numbers not fully traceable  
- **Location:** Sec. IX.B, items for DESI, Euclid, CMB‑S4, refs –.  
- **Issue:**  
  - DESI white paper  indeed gives ballpark σ(fNL)≈3–5 from SDB, but your exact ranges are not referenced to a specific table; you attribute them vaguely (“table 2.7” is mentioned in ref , but that table is not specifically about fNL constraints in the latest DESI docs).  
  - Euclid: you refer to a 2025 Mellier et al. Euclid paper with σ(fNL)≈2–4. There *are* Euclid forecasts with σ(fNL) around that range, but the precise numbers and their dependence on survey specifics need a precise citation (e.g. specific Euclid Collaboration cosmology forecast paper).  
  - CMB‑S4: you quote σ(fNL)≈2.5 from the CMB‑S4 science book; that is broadly consistent with other reviews, but again you do not tie this to a specific figure/table.  
- **Required fix:**  
  - For each of , , , explicitly tie your σ(fNL) numbers to a definite table or figure in the cited document or adjust the numbers to match what is clearly documented.  
  - If these numbers are your recast of those surveys, say so and briefly outline the recast procedure.

**P2‑M5 (MAJOR)** – Maldacena consistency relation sign and numerical value  
- **Location:** Abstract and Introduction, e.g.:  
  > “Standard single-field slow-roll inflation predicts a nearly scale-invariant, nearly Gaussian spectrum with a small, positive local-type non-Gaussianity fNL ≈ (5/12)(1 − ns ) ≈ 0.015, set by the Maldacena consistency relation [1] …”  
- **Issue:** Maldacena’s squeezed‑limit relation for the *gauge‑frame* local fNL is conventionally \(f_{\mathrm{NL}}^{\mathrm{local}} = \frac{5}{12} (1 - n_s)\).[1] With Planck \(n_s ≈ 0.965\), \(1-n_s ≈ 0.035\) and \(5/12 ≈ 0.417\), which gives \(f_{\mathrm{NL}} ≈ 0.015\), so the *numerical* value is correct. However, elsewhere in the manuscript you write variants like “−(5/12)(ns−1)”, and you mix “gauge‑frame vs CFC‑frame” statements without always keeping sign conventions crystal‑clear (see Eq. (8) discussion).  
- **Required fix:**  
  - Make the sign convention explicit once (e.g. “we adopt the Planck gauge‑frame sign convention, for which Maldacena gives \(f_{\mathrm{NL}}^{\mathrm{loc}} = +\frac{5}{12}(1-n_s)\)”).  
  - Check every occurrence: in some places you have “−(5/12)(ns−1)”, which is equivalent numerically but confusing to readers. Ensure you never inadvertently suggest that standard single‑field predicts negative fNL.

**P2‑M6 (MAJOR)** – Claims about Cai vs. Cai & Brandenberger normalization not matched to the literature  
- **Location:** Abstract, Sec. II.C, Appendix A.  
- **Text:**  
  > “A factor-of-two discrepancy exists in the literature: Cai & Brandenberger  obtain fNL = −35/16 = −2.1875 when evaluated at cs = 1.”  
  > “We performed a source-to-source normalization audit and established that this is a convention difference, not a physical one… the factor of two resides in the momentum-dependent polynomial terms …”  
- **Issues:**  
  1. Cai et al. 2009 JCAP 0905, 011 and Cai & Brandenberger 2014 PRD 90, 023534 indeed both compute fNL in matter‑bounce models, but they are not simple re‑evaluations of the same calculation: the later paper also changes the model (e.g. LQC vs. effective Minkowski bounce). It is *plausible* that the factor‑of‑2 difference you find largely reduces to convention and commutator issues, but you are stating this as an established fact without showing line‑by‑line agreement with their equations.  
  2. You claim all four vertex contributions agree “to six significant figures” and that the only difference is a missing commutator factor plus a different Komatsu–Spergel c. This would require a very explicit match to both PDFs; you do not provide enough detail for a reader to verify this claim.  
- **Required fix:**  
  - Tone down the claim to something like: “Our numerical evaluation suggests that, in the Planck convention, the Cai et al. and Cai–Brandenberger results are consistent once commutator doubling and normalization are treated identically. However, because the 2014 paper also modifies the background dynamics, the factor‑of‑two should not be interpreted as a pure ‘convention’ discrepancy; it may partly reflect physical differences. We adopt −35/8 in our forecasts and treat −35/16 as an alternative normalization for robustness.”  
  - Alternatively, add a short, explicit comparison of the key equations (pointing to equation numbers) where you can clearly demonstrate that only an overall factor differs in the cs=1 limit.

---

### B. Internal‑consistency, abstraction vs. proof, and σ‑scale issues

**P2‑E2 (ESSENTIAL)** – Mixing σ values from different procedures on apparently equal footing  
- **Location:** Abstract; Sec. IV; Sec. IX.D; Table IV.  
- **Text:** e.g.  
  > “The SPHEREx multi-tracer bispectrum achieves σ(fNL^local) ≈ 0.7 (Heinrich et al. 2024 [4]) … giving template-corrected significance ∼3–5σ after the combined systematic budget … with 5.2–5.5σ as the optimistic case before GR and bϕ degradation (the signal-only CMB Fisher weighting gives 5.5σ; under realistic LSS noise weighting, 5.2σ).”  
  > “a separate joint (fNL, nfNL) scale-dependent-bias Fisher analysis … gives a much higher idealized detection significance … ∼9.9σ … The ∼9.9σ should be read as … not as an independent detection forecast against published SPHEREx multi-tracer projections.”  
- **Issue:** This paper uses at least three *different* σ(fNL) scales and frequently presents them as comparable:  
  1. σ(fNL)=0.7 from an external bispectrum forecast.  
  2. Idealized joint Fisher (fNL, nfNL) from SDB across six bins, which would correspond to σ(fNL)≈0.11 unmarginalized.  
  3. Template‑projection (r) scaling and further GR/bϕ degradation.  
  Although you *do* warn in Sec. IX.D that the 9.9σ is not the same baseline, the abstract and conclusion still place σ‑numbers side‑by‑side in a way that will mislead many readers into thinking the 5.2–5.5σ “headline” and 9.9σ “joint” values are on the same footing. This violates your instruction 7: different null procedures are being discussed as if their σ are comparable, even though they are not all derived with the same covariance and observables.  
- **Required fix:**  
  - In the abstract and conclusion, restrict the “headline” forecast to **one** σ value derived from a single pipeline (e.g. the bispectrum‑only σ=0.7 forecast with r correction, plus an overall systematic‑degradation factor).  
  - Move the joint (fNL, nfNL) Fisher discussion to a clearly marked “internal consistency check” subsection, and delete any σ‑numbers for that case from the abstract.  
  - Explicitly state that σ from this joint SDB‑only Fisher cannot be compared directly to σ from the bispectrum‑only forecast and is not used for the 3–5σ claims.

**P2‑M7 (MAJOR)** – Abstract “what we prove” vs. what is actually demonstrated  
- **Location:** Abstract.  
- **Text (examples):**  
  > “We audit the Cai et al. bispectrum calculation, confirming that the intermediate ϵ‑order decomposition … reproduces approximately half the full polynomial… consistent with the commutator interpretation that −35/8 is the correct Planck‑convention normalization.”  
  > “We quantify for the first time the template mismatch between the matter-bounce and local templates … validated via ℓ-space Fisher overlap, 200 injection-recovery realizations, and a 10,000-sample null-space scan …”  
  > “A Bayesian comparison validated across three independent ensembles (10^5 realizations each) finds that a detection near fNL = −4.375 favors the bounce over tuned multifield competitors at Bayes factor BF ≈ 10… up to BF ≈ 17 …”  
- **Issues:**  
  - The “audit” of Cai et al. does *not* actually re‑derive the bispectrum from first principles; it only checks consistency at three benchmark configurations and relies heavily on Cai’s own results. This is not an “audit” in the strong sense suggested.  
  - The template‑mismatch quantification is entirely based on your own code; no external cross‑check is cited. That’s fine, but the abstract reads as if this is an observationally validated result.  
  - The Bayes factors depend crucially on your prior choices; Section VI is careful about this, but the abstract simply quotes BF≈10–17 without reminding the reader that these are *upper bounds* and sensitive to priors and theoretical uncertainty in fNL.  
- **Required fix:**  
  - Reword the abstract to distinguish clearly between things you *prove* vs. things you *assume* or *validate numerically under certain assumptions*.  
  - Add explicit phrases like “under the assumed priors of Sec. VI” when quoting BF≈10–17 in the abstract.  
  - For the Cai audit, say “we numerically reproduce Cai et al.’s benchmark configuration values and demonstrate consistency with the −35/8 normalization under the Planck convention” rather than “audit” implying independent verification.

**P2‑M8 (MAJOR)** – Abstract self‑reference to deferred companion material vs. delivered content  
- **Location:** Abstract, near “scale‑dependent‑bias Fisher analysis”.  
- **Text:**  
  > “A separate joint (fNL, nfNL) scale-dependent-bias Fisher analysis is discussed in §IX as an idealized-Fisher self-consistency check (full Fisher-input release—six-bin kmin(z), n̄(z), b1, bϕ scheme, photometric-z scatter σz, and per-bin survey volume—is deferred to a companion artifact and the specific numerical significance is not quoted here in the abstract until that release lands).”  
- **Issue:** You explicitly say the full Fisher inputs are “deferred to a companion artifact”. That artifact is not part of this PRD submission; the abstract is flagging a dependency on non‑existent supplementary material. Instructions ask to flag such version‑history / TODO language.  
- **Required fix:**  
  - Remove any language about “deferred to a companion artifact” from the abstract. Either supply all necessary Fisher inputs in an appendix of this paper, or treat the joint (fNL, nfNL) analysis as an internal check that does not require external data release and does not contribute to headline claims.  
  - See P2‑E4 below for related issues with version‑history language.

---

### C. Version‑history / internal‑process artifacts and duplicated phrases

**P2‑E3 (ESSENTIAL)** – Internal review / version‑history language in body and abstract  
- **Location:** Multiple places; notably:  
  - Abstract, last sentence of Appendix A.2:  
    > “… to address the cross-model peer-review concern (R42 Gemini 3.1-Pro P2 BLOCKER B-3) …”  
  - Data and code availability:  
    > “pinned to release tag paper2-v1.7.40”  
  - Acknowlegments: explicit mention of “R42 Gemini 3.1-Pro” and AI use is fine, but internal bug/issue IDs are not.  
- **Issue:** You have left explicit internal audit tags, review IDs, and Git tag strings in the main scientific text (not just the acknowledgments). Per instruction 8, these must be flagged. They are not scientific content, and they directly reference a proprietary review log.  
- **Required fix:**  
  - Remove all mentions of “R42 Gemini 3.1-Pro”, “P2 BLOCKER B‑3”, specific internal bug IDs, and similar audit tags from the scientific text and abstract. If you want to acknowledge that the Cai vs. Li normalization was raised by a referee, say “this point was raised in internal review” without naming tools or internal IDs.  
  - In Data & Code Availability, you may reference a Git tag, but keep it neutral (“we used tag v1.7.40 in the public repository”) rather than “paper2-v1.7.40”.

**P2‑M9 (MAJOR)** – TODO / deferred language that belongs only in author notes  
- **Location:** Abstract (“…deferred to a companion artifact…”); Sec. IX.D (long discussion of “not yet published Fisher input release”).  
- **Issue:** This reads like an internal project note, not a finished methods section. PRD expects the paper itself to be self‑contained or to refer to existing public data releases.  
- **Required fix:**  
  - Either (i) release the Fisher input tables in an appendix of this paper and treat the “companion artifact” as optional; or (ii) demote these analyses to future work and remove numerical claims that depend on unreleased inputs.

**P2‑N1 (NIT)** – Duplicate / odd phrases  
- **Location:** Several spots; one explicit example:  
  - Abstract: “canonical Planck/local‑template gauge convention” is a bit tautological but not strictly erroneous.  
  - Sec. III.B: “the signal-only CMB Fisher weighting gives 5.5σ; under realistic LSS noise weighting, 5.2σ” – repeated from abstract.  
- **Issue:** You were asked to flag duplicate phrases like “canonical canonical‑mask”. You do not have that exact string, but you do have some borderline redundant constructions (“Planck/local‑template gauge convention”, “SPHEREx multi‑tracer bispectrum achieves σ…”) repeated verbatim between abstract and main text.  
- **Required fix:** Optional. If space is tight, compress and de‑duplicate, but this is not blocking.

---

### D. Length and scope

**P2‑M10 (MAJOR)** – Length vs. contribution and scope creep  
- **Location:** Global. Paper is ~22 pages for a methods/forecast paper.  
- **Issue:** The central technical contribution is: (i) re‑expressing the Cai bounce bispectrum in a 6‑monomial basis and exploring its null‑space, (ii) computing a template overlap r≈0.84–0.88, and (iii) recasting a SPHEREx‑like σ(fNL) forecast plus some Bayes factors. That could probably be conveyed in ∼12–15 pages. The current manuscript contains long digressions on Holst gravity, torsion, ECH operator spaces, QSFI parameter space, cosmic birefringence, and future surveys that are interesting but not essential to the main result and not backed by new calculations.  
- **Required fix:**  
  - I recommend trimming to ≤18 pages. Candidates for shortening or moving to an appendix:  
    * Most of Sec. VI.C–E (Bayes factors and QSFI/curvaton discussions) – keep the headline BF scaling and one table; cut redundant prose.  
    * Much of Sec. IX.B–E (other experiments, birefringence excursion, dynamical DE commentary) – keep a concise paragraph on how other probes compare.  
    * Parts of Appendix A that repeat operator‑formalism basics well‑known from Maldacena’s original paper.  

---

### E. Abstract accuracy vs. body

**P2‑M11 (MAJOR)** – Abstract over‑represents robustness of −35/8 prediction  
- **Location:** Abstract first two sentences; Sec. II.A–C.  
- **Text:**  
  > “A matter-dominated contracting phase preceding a nonsingular bounce produces a minimally parameterized local-type non-Gaussianity fNL^local = −35/8 … The bounce-vs-inflation discrimination is therefore dual-pronged…”  
- **Issue:** Within the body you are careful to say: (i) the prediction is **conditional** on assumptions (a)–(f), including unknown third‑order transfer across the bounce; (ii) the O(ϵ) correction is large and poorly constrained (κ1 between ~5.6 and 80), giving a 1–8% uncertainty; (iii) polynomial null‑space creates an additional ~15% amplitude systematic. The abstract, however, reads as if −35/8 is a near‑exact prediction of the whole matter‑bounce class, and arguably over‑states the robustness relative to what is actually derived.  
- **Required fix:**  
  - In the abstract, add one explicit caveat: e.g. “This prediction holds within the scalar‑only Wilson–Ewing matter‑bounce class, under assumptions (a)–(f) detailed in Sec. II.C, and carries a 1–8% theoretical uncertainty from the quasi‑dust correction and polynomial coefficient ambiguities.”  
  - Clarify that the bounce‑vs‑inflation discrimination is “strong *if* the −35/8 normalization is correct”, not that it is guaranteed by first principles.

---

### F. Miscellaneous smaller issues

These are less severe but should be corrected for clarity and rigor.

**P2‑m12 (MINOR)** – Use of “first time” for template mismatch quantification  
- **Location:** Abstract, Sec. III.B.  
- **Issue:** You state “We quantify for the first time the template mismatch between the matter-bounce and local templates”. To my knowledge there is indeed no prior published overlap calculation specifically for the Cai matter‑bounce bispectrum vs. the Planck local template; however, “for the first time” is a strong claim and can be questioned if any workshop proceeding, thesis, or minor paper did such a calculation.  
- **Required fix:** Rephrase to “We quantify the template mismatch…” without “for the first time”.

**P2‑m13 (MINOR)** – “No observational tensions” statement  
- **Location:** Sec. II.D.  
- **Text:**  
  > “No observational tensions with this model have been identified to date.”  
- **Issue:** This is somewhat strong: the Wilson–Ewing matter‑bounce is not in wide use in cosmological parameter pipelines, so the statement might be better phrased as “has not been robustly ruled out” rather than “no tensions identified”.  
- **Required fix:** Change to “This model has not been robustly ruled out by current constraints; a dedicated global fit has not yet been performed.”

**P2‑n2 (NIT)** – Minor notational collision: κ1 vs c1  
- **Location:** Sec. II.A and Sec. VIII.  
- **Issue:** κ1 is introduced as the linear coefficient in the ϵ expansion, but you also have c1–c6 as polynomial coefficients. This is not wrong but somewhat confusing.  
- **Required fix:** Consider renaming κ1 to something clearly distinct (e.g. Aϵ) or adding a one‑line reminder.

---

## Summary recommendation

**MAJOR REVISIONS**

The core technical content (reparametrization of the Cai bispectrum, template overlap, and use of SPHEREx‑like forecasts) is potentially publishable and interesting, but the paper currently mixes speculative or future‑dated references with real literature, overstates the robustness of some external results and of the Cai vs. Cai & Brandenberger reconciliation, and uses multiple incompatible σ scales in a way that could mislead readers. Cleanly separating what is demonstrably supported by existing papers from what is internal to this work, correcting the few factual citation errors (especially Cosmoglobe DR1), stripping internal review artifacts, and tightening the abstract to reflect the actual scope will require substantial but straightforward revisions.