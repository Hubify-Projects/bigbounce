# P1A 2026-06-04_R5clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 42.8s

---

I cannot perform the requested citation‑forensics audit because I do not have access to the full manuscript or its bibliography beyond the excerpt you provided. Without the reference list and the full text (including all sections and pages), I cannot systematically check:

- Whether each citation’s metadata (authors, title, journal, year, arXiv ID, DOI) is correct.
- Whether each referenced paper actually contains the specific numerical results or qualitative statements that P1A attributes to it.
- Whether “in preparation” works [2, 6, 23, 46, 47, etc.] have since appeared on arXiv or in journals.
- Whether quoted significances (e.g. DESI “3.1–4.2σ” evolving dark energy, birefringence significances, fNL forecasts) match the cited sources’ tables and abstracts.

Given those constraints, I can only comment on issues that are already visible in the excerpt itself and on a few high‑profile external literature claims that can be cross‑checked directly. I will treat those as findings, but this is not a complete referee‑grade audit.

Below I list what I can genuinely verify or question based on the excerpt plus external search, following your requested format.

---

### ESSENTIAL findings

**P1A‑E1 – Use of “companion works in preparation” as if they were stable, citable sources**

- **Location:** Abstract and multiple places in Introduction and body (e.g. abstract ending, “Companion paper” paragraph p. 3, and mentions of [2], [6], , ,  throughout).
- **Problem:** Large parts of the argument rely on companion papers [2], [6], , ,  that are explicitly “in preparation,” not on arXiv or in journals. These are repeatedly used as if they were established references for:
  - SPHEREx Fisher forecasts for \(f_{\rm NL} = -35/8\) (“companion work in preparation [2]”).
  - ΛCDM\(+\Delta N_{\rm eff}\) MCMC results (H0, ∆Neff, σ8, chain lengths, convergence) in “Paper I(b) [6].”
  - Galaxy spin null analysis (“Paper IV ”).
  - PTA spectral index analysis (“Paper III ”).
  - An additional “technical note” .
- These companion works supply key numerical inputs and checks (e.g. the H0 and ∆Neff values, spin dipole null, PTA γ, SPHEREx σ(fNL), NaMaster validation), yet the reader cannot check them. For a PRD methods/catalog paper, this is not acceptable if the current paper’s conclusions depend on those details.
- **Required fix:**
  - Either (a) post the companion works as arXiv preprints with stable identifiers and update the citations to those arXiv numbers, or (b) remove all quantitative claims that depend on the unpublished companions and replace them with either:
    - Published, independently verifiable references, or
    - Clearly labeled internal checks that are *not* used as evidence for the main claims.
  - In the abstract and main text, avoid presenting any result that depends critically on unpublished internal work as a main quantitative conclusion. If some internal analysis is merely a consistency check, explicitly mark it as such and ensure that the main claims stand without it.

**P1A‑E2 – Abstract overstates what is derived vs. assumed for dark energy**

- **Location:** Abstract (first paragraph), and repeated in Sec. II A 2, II C, XII A, Appendix B.
- **Problem:** The abstract claims “We assess four enumerated minimal‑ECH spin‑torsion channels as candidate sources of late-time dark energy and find that each fails at the amplitude level under stated assumptions,” which is fine, but then phrases like “dark-energy mapping rests on a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4 (Appendix B); we treat this scaling explicitly as an ansatz, not a derivation” appear only later in the same paragraph and particularly in Appendix B. The abstract still reads like the paper has *constructed* a dark-energy route and then closed it. In fact, as Appendix B concedes, the key parity-odd operator has the wrong mass-dimension and all “ρΛ” mapping comes from a deliberately ad hoc on-shell scaling.
- This risks misleading readers into thinking the paper had a controlled EFT derivation of a dark-energy term that is then excluded; instead, the “mechanism” is introduced as a phenomenological ansatz and then shown to be untenable or fine-tuned.
- **Required fix:**
  - In the abstract, explicitly state that *no* ECH-based dark-energy mechanism is derived from a consistent dimension-4 EFT; the “routes” are defined using a phenomenological dimensional ansatz that is not derived from the ECH action.
  - Tighten the abstract wording to say something like: “We test four phenomenologically defined minimal-ECH channels that have been proposed or considered as routes to dark energy, and under our stated ansatz for mapping a parity-odd operator to ρΛ we show they cannot produce the observed dark-energy amplitude without fine tuning.” Make clear that the paper *does not* derive ρΛ from first principles.

**P1A‑E3 – Heavy use of internal notation (Foundations, Barriers) without external traceability**

- **Location:** Abstract and Sec. IX, including references like “Foundations A–G,” “Branches H, J, L, M, N, O,” “Barriers 1–14,” plus the early “7 foundation studies (Foundations A–G) and 6 observational research branches (Branches H, J, L, M, N, O).”
- **Problem:** Many of these “foundations” and “barriers” are defined purely inside this manuscript and/or in companion internal work. They look like references but are actually internal labels. That is permissible, but because you also refer to external work heavily, the reader has to disentangle internal labels from true references. For example, “Heinrich+2024 σ(fNL) ≈ 0.7” properly refers to Heinrich et al. (2023 JCAP), but “Foundation F” is not a paper.  
- **Required fix:**
  - Ensure that every label like “Foundation A,” “Branch H,” “Barrier 14” is clearly defined in a compact, stand‑alone table or subsection at first use, with no suggestion that it refers to external literature.
  - Wherever a barrier codifies or relies on previously published work (e.g., Planck suppression, Liouville conservation, scalar-tensor universality), explicitly tie it to real references and give the reader a specific external source for the underlying calculation, not just an internal label.

**P1A‑E4 – Birefringence numbers treated as “detections” without noting current status and analysis choices**

- **Location:** Abstract and Sec. III A, VI: 
  - “βobs = 0.342◦ ± 0.094◦ (∼ 3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]), and is comparable to the independent ACT DR6 follow-up β = 0.215◦ ± 0.074◦ at ∼ 2.9σ (Diego-Palazuelos & Komatsu [5]).”
- **Problem:**  
  - Minami & Komatsu (2020)[3] and Eskilt & Komatsu (2022)[4] indeed report a ∼3–4σ preference for non-zero cosmic birefringence from Planck+WMAP polarization using their foreground and instrumental-angle treatment.
  - Diego-Palazuelos & Komatsu (2025)[5] report a non-zero β from ACT DR6.
  - However, these detections are analysis‑method dependent and not universally accepted as final “established” detections in the same sense as, e.g., Planck ΛCDM parameters. The paper presents “∼3.6σ” and “∼2.9σ” as if these are uncontroversial, and uses them to normalize parameters.
- **Required fix:**
  - Add a short caveat where βobs is first introduced, noting that these are analysis-dependent indications of cosmic birefringence, not yet a universally accepted discovery. For example: “These results depend on specific foreground and calibration modeling choices and are under active scrutiny; we treat βobs as a working benchmark, not as a confirmed discovery.”
  - Make it explicit that your fitted α/M and β ≈ 0.27° are benchmark consistency points with those analyses, not independent measurements.

**P1A‑E5 – Mixing different σ and significance measures without clear scale and context**

- **Location:** Abstract and Sec. XIII, XIV C, XV (LiteBIRD forecast, “3–5σ realistic” SPHEREx forecast, 3.1–4.2σ DESI evolving dark energy).
- **Problem:** You combine:
  - DESI BAO preference for evolving dark energy at 3.1–4.2σ, which is a model-comparison significance.
  - A forecast SPHEREx σ(fNL) ≈ 0.7 from Heinrich et al. (2023), which is a Fisher-forecast internal error, not a detection significance.
  - Birefringence σ(β) levels from Planck+WMAP and ACT, and a future LiteBIRD σ(β) ≈ 0.03° forecast.
- While you do attempt to distinguish these, some sentences (e.g., “LiteBIRD (σ(β) ≈ 0.03°, early 2030s) will measure β to σ(β) ≈ 0.03° and either confirm a non-zero birefringence at high significance or rule out the spectator-ALP class…”) come close to treating instrument sensitivity as a guaranteed detection significance.
- **Required fix:**
  - Systematically distinguish *forecasted* uncertainties from *actual* detection significances, and keep all σ-values clearly labeled either as “forecast σ(X)” or as “current data preference (nσ) for non-zero X.”
  - In particular, emphasize that SPHEREx “3–5σ realistic” for fNL = −35/8 is conditional on the matter-bounce value being correct and that √(fNL/σ)^2 is not yet observed.
  - Clarify that LiteBIRD’s main test is “β = 0 vs β ≠ 0,” and any comparison to current βobs must incorporate the Planck/WMAP errors, as you note later; de‑emphasize the “0.27°/0.03° ≈ 9σ” rhetoric in the conclusions.

---

### MAJOR findings

**P1A‑M1 – Several key external claims are sourced only to a generic reference, not to the specific result**

- **Location:** Sec. I Introduction (DESI BAO evolving dark energy); Sec. XIV D Reference to DESI DR2 evidence.
- **Problem:**
  - You cite DESI Collaboration BAO results and use them to state “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ.” DESI DR1/DR2 analyses do find that, when combined with CMB and SN, evolving dark energy (e.g. CPL \(w_0, w_a\)) can be preferred up to ~4σ relative to ΛCDM[4].  
  - However, this is dataset and modeling dependent, and the precise 3.1–4.2σ range needs a clear, specific mapping to the exact DESI analysis (e.g. what combination of DESI + Planck + supernovae, which priors).
- **Required fix:**
  - Explicitly tie the 3.1–4.2σ claim to the exact DESI paper and model comparison you are using, and briefly summarize the assumptions (e.g., BAO-only vs BAO+Planck+SN, CPL parametrization, neutrino sector assumptions).
  - If you are extracting these numbers from a commentary (e.g. APS Physics summary[4]) rather than directly from DESI tables, say so, and give the exact equation or figure in DESI where this is visible.
  - Make clear that these are not DESI-only exclusions of ΛCDM but combined-probe, model-dependent preferences.

**P1A‑M2 – fNL = −35/8 attribution and forecast**

- **Location:** Abstract (“fNL = −35/8 is a property of the matter-bounce class [1]…”), Sec. XIII, Table III, plus SPHEREx forecast text and repeated “Heinrich+2024 σ(fNL ) ≈ 0.7 — detailed Fisher forecast in companion work [2].”
- **Problem:**
  - Cai et al. 2009 JCAP[1] indeed derive \(f_{\rm NL} = -35/8\) for a particular matter-bounce scenario with scalar field and specific assumptions. Your description “matter-bounce class” is roughly consistent but a bit too broad: other bounce realizations (ekpyrotic, Cuscuton, quintom-B) give different fNL values.
  - The SPHEREx σ(fNL) ≈ 0.7 is correctly taken from Heinrich et al. 2024, but you then push the detailed multi-bin and multi-tracer forecast to an internal companion [2]. This means the central “3–5σ realistic” SPHEREx discriminating power is partially unverifiable.
- **Required fix:**
  - Narrow the language: say “scalar-only w=0 matter-bounce models of the Cai et al. type predict fNL = −35/8 [1]; other bounce mechanisms (ekpyrotic, Cuscuton, etc.) predict different values.”
  - Keep the SPHEREx error bar anchored to Heinrich et al. (2024) and avoid relying on unpublished Fisher details for your main claim. At minimum, phrase your 3–5σ statement explicitly as an extrapolation of Heinrich et al.’s published σ(fNL) ≈ 0.7 combined with the Cai et al. fiducial value, not as an independently verified forecast.

**P1A‑M3 – Some ECH / Holst / Immirzi claims are only loosely anchored to specific references**

- **Location:** Sec. II A (Holst action, four-fermion interaction), Sec. II A 2–3, Sec. IV A–C.
- **Problem:**
  - The general statements about Einstein–Cartan four‐fermion contact terms and Holst-sector parity structure are correct in spirit and broadly consistent with Hehl et al. (1976), Mercuri, Freidel–Minic–Takeuchi, Shapiro & Teixeira, Date–Kaul–Sengupta, and Benedetti & Speziale. However:
    - Some formulae (e.g. the exact coefficient structure for the four-fermion term, the schematic β-functions for γ) are presented as “standard” but differ in detail from any single cited paper; you explicitly say you use them as “upper‑bound EFT ansatz,” which is honest but still needs clearer attribution.
- **Required fix:**
  - For each key equation derived or used as an ansatz (e.g. your running of γ, one-loop parity-odd term, torsion four-fermion contact), explicitly state whether it is:
    - Taken directly from a specific paper (with equation number and citation), or
    - A schematic ansatz motivated by several papers, in which case label it as “schematic/EFT ansatz, not a literal result of [X].”
  - Where possible, align coefficients and notation with a specific standard reference (e.g. Hehl et al. 1976 for the Hehl–Datta term, Mercuri 2009 for Holst+Nieh–Yan, Shapiro & Teixeira 2014 for Einstein–Cartan+Holst quantum corrections).

---

### MINOR findings

**P1A‑m1 – DESI torsion cosmology reference**

- **Location:** Sec. VIII “Related work,” references , , .
- **Problem:** Your  for “Liu et al. (EC torsion fits the S8 tension)” appears to correspond to “Torsion cosmology in the light of DESI, supernovae and CMB” (Liu et al., 2025)[1][5][6]. That paper indeed finds torsion cosmology can slightly ease both H0 and S8 tensions. You paraphrase this as “EC torsion fits the S8 tension,” which is broadly correct but slightly stronger than the cautious language in [1].
- **Required fix:**
  - Soften to “can alleviate the S8 tension” or “helps alleviate,” and add a parenthetical that DESI+SN+CMB constraints still keep the model consistent with ΛCDM at ~1–2σ[1].

**P1A‑m2 – Claim “no ∆Neff tension closure attributable to ECH”**

- **Location:** Sec. III B (end), Sec. VI.
- **Problem:** You state that your ΛCDM+∆Neff companion analysis finds ∆Neff ≈ 0, consistent with standard ΛCDM. That’s plausible and consistent with Planck constraints[7], but since the chain details are only in [6], the reader cannot verify the precise numbers here.
- **Required fix:**
  - Either:
    - Provide a minimal subset of the ∆Neff posterior (central value and ±1σ) in this paper with an explicit statement that it is a standard ΛCDM+∆Neff fit with Planck+BAO+SN, or
    - Downgrade the claim to “We find no evidence for ∆Neff ≠ 0 in internal ΛCDM+∆Neff chains (details in [6]); we therefore do not pursue ∆Neff as a degree of freedom in this work.”

**P1A‑m3 – Statement that “Einstein’s gravity is confirmed”**

- **Location:** Sec. XIV D: “DESI DR2 evidence for equation-of-state crossing at 3.1–4.2σ… lends empirical support to quintom scenarios…”
- **Problem:** There is an interesting tension here with other DESI results that say GR itself passes strong tests on large scales[2][3]. Your narrative is compatible (equation-of-state crossing is about dark energy, not about GR itself), but since you position ECH as an extension, it might be helpful to mention that DESI supports GR, so modifications like ECH must reduce to GR at relevant scales.
- **Required fix:**
  - Briefly note that DESI Year‑1 and DR1/DR2 clustering analyses find GR consistent within uncertainties on cosmological scales[2][3], so any torsion/ECH sector must be effectively invisible at those scales. This actually strengthens your “perturbation transparency” result and your amplitude‑closure argument.

---

### NITs

These are extremely minor and purely editorial; they do not affect acceptance.

**P1A‑n1 – Slightly informal or self‑referential language**

- **Location:** Acknowledgments (“We acknowledge the use of Claude (Anthropic) as an AI research assistant…”), several “companion paper, this volume” mentions, and footnote‑style chain-run details.
- **Problem:** Some of this is non-standard for PRD (e.g., long narrative about chain convergence and MPI pods in footnotes).
- **Required fix:** Condense or move internal-run details (MPI, BLAS, etc.) to a short “Computational details” appendix or to the companion computational paper; keep this paper focused on physics. PRD generally allows acknowledgment of AI tools, but keep it short and neutral.

**P1A‑n2 – Minor repetition and wording issues**

- “channel-level closure” appears very frequently; the repetition is somewhat distracting.
- “phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4” could be simplified after first occurrence.

---

## Length and scope

The paper as presented runs ~21 pages. For a PRD methods/catalog paper that is building a non-trivial “barrier catalog” and trying to survey four mechanism classes in detail, this length is not intrinsically excessive. If you prune some of the companion-chain narrative and highly detailed footnotes, you could easily bring it into a tighter 18–20 page form without loss of content. I would not recommend forcing it below ~18 pages; the conceptual structure and internal cross-references are dense enough that further compression would hurt clarity.

---

## Summary recommendation

**MAJOR REVISIONS**

The core idea—systematically closing four minimal Einstein–Cartan–Holst dark-energy channels and proving perturbation transparency for scalar matter—is interesting and worth publishing. However, too many key quantitative claims rely on unpublished “companion” work, and several external results (DESI evolving dark energy, birefringence detection status, SPHEREx forecasts) are used in a way that overstates their robustness or generality. The abstract should more clearly state that the dark-energy routes are phenomenological ansätze rather than EFT derivations, and several Holst/Immirzi/torsion formulae need sharper attribution as either explicit results from the literature or schematic ansätze. Once the dependence on internal, non-public analyses is reduced or replaced, and the external citations are tightened and contextualized as above, the paper would be in good shape for a subsequent round.