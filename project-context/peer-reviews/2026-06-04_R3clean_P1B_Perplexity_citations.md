# P1B 2026-06-04_R3clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 18.8s

---

I can’t complete the requested citation-forensics audit to the standard you asked for because the prompt does not include the actual web search results from arXiv/NASA ADS, and I do not have live browsing access in this environment. The only “search results” attached are generic journal-information pages that do not verify any of the paper’s citations, arXiv IDs, titles, authors, venues, or quoted statistics.

What I *can* do from the manuscript text itself is flag several **internal consistency and citation-risk problems** that would need checking with real arXiv/ADS lookups:

- **ESSENTIAL**: The manuscript claims [2] is “J. R. Eskilt and E. Komatsu, Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data, Phys. Rev. D 106, 063503 (2022), arXiv:2205.13962,” and then repeatedly attributes the same source to “PR3 + WMAP9,” “PR4/NPIPE,” and “published joint WMAP+Planck value.” The footnote says the repository code was updated to PR4/NPIPE but the headline \(0.342^\circ \pm 0.094^\circ\) is from the published PR3+WMAP9 analysis. This is a **metadata/attribution fusion** that must be separated cleanly. Required fix: distinguish the published paper from the repository implementation dataset in every place that cites [2], and verify whether the “PR4/NPIPE” label is a code-repo artifact rather than a bibliographic fact.

- **ESSENTIAL**: Reference [3] is cited as “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654.” That arXiv ID format suggests a **future-dated preprint** relative to the paper date and must be checked for validity/resolution. Required fix: verify the arXiv identifier resolves to the stated ACT DR6 birefringence paper and correct the year/metadata if not.

- **MAJOR**: The manuscript repeatedly states published birefringence values “\(2.4–2.9\sigma\)” and “3.6\sigma” as if they are interchangeable. They are not. The paper uses a **published joint WMAP+Planck value** and also an **auxiliary inverse-variance combination** in a way that can blur what is actually measured versus what is an internal recombination. Required fix: explicitly label which significance belongs to the published result and which belongs to the author’s auxiliary combination.

- **MAJOR**: The manuscript says the NaMaster pipeline recovery “recovers \(\hat\beta = 0.238^\circ\)” with “pipeline-recovery SNR = 20.32,” then elsewhere states “high pipeline-recovery SNR figures (e.g., 20.32, 25.71) refer to recovery of injected MC signals and must not be conflated with the published Planck/ACT DR6 2.4–2.9σ sky detection.” This is a necessary caveat, but the text still mixes them in proximity and risks reader confusion. Required fix: move all injected-signal SNR statements into a strictly separate validation subsection and avoid any phrasing that could be read as observational significance.

- **MAJOR**: The manuscript states that “the same β ≈ 0.27° arises in standard GR with an identical ALP Lagrangian and natural parameters,” and then says it is “not derived from minimal ECH.” That is a scope statement, but it also undermines the paper’s framing as an ECH companion. Required fix: state more sharply in the abstract and conclusions that the birefringence section is not an ECH prediction at all, only an external consistency check.

- **MAJOR**: The paper says “the stock-CAMB ΛCDM+∆Neff proxy run does not test the ECH spin-torsion sector directly” and later “current data neither require nor exclude a small positive ∆Neff from the spin-torsion sector.” These are compatible only if the proxy interpretation is treated as strictly heuristic. Required fix: avoid phrasing that suggests the proxy constrains ECH itself; it constrains only a standard \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) extension.

- **MAJOR**: The paper contains multiple “version-history / internal-audit” artifacts in body prose: “earlier internal bookkeeping (corrected fire #25),” “stale mid-burn-in diagnostic,” “repository README is the authoritative source,” “alias failure,” “queued,” “verification,” “transparency artifact,” “audit,” “direct .input.yaml inspection,” and similar operational comments. Required fix: remove all review-log and internal debugging language from the manuscript body or relegate it to a reproducibility appendix with neutral wording.

- **MAJOR**: The manuscript reports a sequence of posterior summaries across different dataset combinations while also deferring model-comparison statistics. In particular, \(\sigma\)-level departures from LCDM in the \(w_0\)–\(w_a\) chain are presented alongside statements that LCDM is unsampled and that Bayes factors are unavailable. This is fine only if clearly framed as posterior-tail distance, not model rejection significance. Required fix: ensure every \(\sigma\) statement about \(w_0\) and \(w_a\) is explicitly labeled as a marginal-tail extrapolation, not an exclusion level.

- **MAJOR**: The manuscript states that the ALP scan uses \(C_{a\gamma}\in\{4,8,12\}\), \(m/H_0\in[1,3]\), and \(\theta_i\in[0.5,2]\), but also says the “spectator-consistent regime” requires \(\theta_i\sim 0.1\). That means the scan prior does not actually cover the claimed spectator-consistent corner. Required fix: either expand the scan to include the spectator-consistent region or stop claiming the scan supports spectator consistency.

- **MAJOR**: The paper gives a “published joint WMAP+Planck value \(\beta = 0.342^\circ \pm 0.094^\circ\)” and then computes \(\beta_{\rm combined}=0.241^\circ\pm0.061^\circ\) by inverse-variance weighting of two values. That combination is not the published headline result and should not be presented as a corroborating observational number without qualification. Required fix: mark it clearly as an author-constructed auxiliary combination, not a literature result.

- **MAJOR**: The citation  is annotated in the reference list with “reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B,” which is not bibliographic metadata. Required fix: remove line-level internal cross-references from the reference list and keep only the publication details.

- **MINOR**: The paper uses “Planck 2018 NPIPE,” “PR4/NPIPE,” “Planck NPIPE CamSpec,” and “Planck PR4 + ACT DR6 EB-spectrum likelihoods” as if these are interchangeable. They are not. Required fix: standardize the dataset nomenclature and specify which products are actually used.

- **MINOR**: The paper says “CAMB v1.6.5, stock; no torsion modifications” and elsewhere “Cobaya v3.5 original; v3.6.1 verification.” That is potentially fine, but it should state exactly which version generated the reported chains. Required fix: identify the single version used for the published results and the role of any verification rerun.

- **MINOR**: The manuscript says “the 13 logically-independent structural barriers (14 historical catalog entries)” and elsewhere “14 independent structural constraints.” This may be consistent but reads as a numbers mismatch. Required fix: define the counting convention once and use it consistently.

- **MINOR**: The manuscript says “canonical canonical-mask” is not present, but it does contain repeated near-duplicate phrases like “Not a competitive sky detection” and “not a distinctive ECH prediction” in adjacent sections. Required fix: trim repetitive scope disclaimers.

- **MINOR**: The paper’s abstract says the NaMaster validation “confirms the algebraic pseudo-Cℓ E→B deconvolution under MASTER mode coupling, NOT the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α.” That is accurate as a scope statement, but the abstract should not foreground results that are merely methodological. Required fix: reduce the amount of validation-detail in the abstract.

- **MINOR**: The reference  appears to be a generic quintom review, but the body uses it as support for “the bounce / pre-Big-Bang scenario discussed in Paper I(a)” and “canonical quintom signature.” Required fix: check that  actually supports those specific claims; if not, cite a more direct source for the quintom-bounce connection.

- **MINOR**: The reference  (“Torsion cosmology in the light of DESI, supernovae and CMB observational constraints,” arXiv:2507.04265) is future-dated relative to the manuscript date and must be checked for existence and exact title/venue. Required fix: verify whether it is truly an arXiv preprint or a placeholder/in-preparation citation that should not appear as a finished reference.

- **MINOR**: The reference  “DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations, arXiv:2404.03002” needs verification of exact title, author list, and whether the manuscript’s “DR1” label matches the cited paper. Required fix: ensure the dataset label in the text matches the reference metadata.

- **MINOR**: The manuscript says “LiteBIRD will settle this at ∼9σ in the early 2030s.” That is a forecast and should be labeled as such rather than written in the same register as measured results. Required fix: mark forecast language as forecast language.

- **NIT**: The text contains awkward fused notation such as “\(\beta = 0.27^\circ , \beta = 0.342^\circ ,\) and \(\beta = 0\) injections” and “Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native”. Required fix: normalize notation and capitalization.

- **NIT**: The paper says “The same birefringence arises in standard GR with an identical ALP; it is not a distinctive ECH prediction,” which is repeated several times. Required fix: state it once.

- **NIT**: The conclusions section is unusually long for an 11-page methods companion and contains detailed restatements of prior sections. If the paper’s contribution is mainly verification, the recommended maximum length is **8–10 pages** excluding appendix. Required fix: tighten the conclusions and move operational detail to appendices.

I cannot honestly provide a complete citation audit of every reference without the actual arXiv/ADS lookups. Several of the listed citations, especially the future-dated arXiv IDs and the PR4/NPIPE vs PR3+WMAP9 attribution for the birefringence paper, need live database verification before this manuscript can be deemed publication-ready.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript’s technical content is framed as verification, but it currently mixes published results with repository-specific dataset labels, internal audit language, auxiliary combinations, and posterior-tail extrapolations in ways that would mislead readers if left uncorrected. The biggest issues are citation/metadata integrity for the birefringence references, the overstatement risk around \(\sigma\)-levels and injected-signal SNRs, and the failure to cleanly separate what is a method-validation exercise from what is an observational or theory claim.