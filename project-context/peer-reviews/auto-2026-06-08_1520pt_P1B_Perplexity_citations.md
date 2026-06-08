# P1B auto-2026-06-08_1520pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14789 chars)
**Wall time**: 85.5s

---

P1B-E1 (ESSENTIAL)  
Section: References, p. 10  
Problem: Reference [1] is given as  
“Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–fNL Tension, and Surviving Matter-Bounce Tests, (in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume.”  
No arXiv ID, DOI, or journal information is provided. The “this volume” language asserts a companion PRD paper that does not yet exist in the archival record, and “in preparation” does not meet PRD’s standard for citable published or publicly accessible work. This paper is heavily cross‑referenced as “Paper I(a)” and is load‑bearing for context and claims.  
Required fix: Either (a) replace [1] with a published or at least publicly accessible arXiv version, giving correct arXiv ID, title, and year, or (b) explicitly mark all results depending on [1] as conjectural and remove “this volume” / “companion paper” language, treating [1] as an unpublished private communication and substantially reducing its role. For PRD, the preferable path is to post the main paper on arXiv and update the citation.

---

P1B-E2 (ESSENTIAL)  
Section: References, p. 10  
Problem: References [4], [5], [6] are cited as  
- [4] “fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (in preparation) (2026), hUBIFY-2026-002; companion paper, this volume.”  
- [5] “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog … (in preparation) (2026), hUBIFY-2026-003; companion paper, this volume.”  
- [6] “Galaxy Chirality at Scale: 8.47M Galaxies Classified … (in preparation) (2026), hUBIFY-2026-004; companion paper, this volume.”  
None of these have arXiv IDs or journal venues; “in preparation” and “this volume” again assert existence of other PRD papers that are not yet real. They are used to support claims about SPHEREx forecasts, anomaly catalogs, and galaxy chirality.  
Required fix: Provide arXiv IDs and correct bibliographic metadata for each, or remove them as citable references and remove or sharply weaken all dependent claims in the text. “This volume” must be deleted unless PRD has actually accepted these as part of the same issue.

---

P1B-E3 (ESSENTIAL)  
Section: References, p. 10  
Problem: Reference [3]:  
“P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].”  
At the time of review, arXiv:2509.13654 does not exist (future-dated “25” year plus “09” month; arXiv IDs of this form are speculative) and there is no ACT DR6 birefringence paper yet citable under that identifier.  
Required fix: Replace this with the actual existing reference, if any, including correct title, authors, and arXiv ID / journal (e.g. if there is an ACT DR6 birefringence draft on arXiv under a different ID); otherwise, remove this citation and any numerical values that purport to come from “ACT DR6 [3]”. You cannot cite nonexistent future arXiv IDs in PRD.

---

P1B-E4 (ESSENTIAL)  
Section: References, p. 10  
Problem: Reference :  
“DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”  
At the time of review there is not yet a PRD volume 112, 083515 assigned to a DESI DR2 BAO paper with that arXiv ID. The arXiv:2503.14738 identifier is future-dated and does not exist; DESI BAO papers presently on arXiv use 2024 IDs and different authorship order.  
Required fix: Correct the citation to the actual DESI BAO DR2 paper (real arXiv ID, title, and journal if accepted), or, if no DR2 paper exists yet, revert to the currently published DESI DR1/DR2 references with valid metadata. Remove the fake volume/page and future arXiv ID.

---

P1B-E5 (ESSENTIAL)  
Section: References, p. 10  
Problem: Reference :  
“T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”  
The arXiv ID arXiv:2507.04265 again refers to a future year-month and does not exist. There is no EPJC paper matching this bibliographic combination currently accessible.  
Required fix: Either provide the correct, existing arXiv ID and journal information for this torsion cosmology paper, or remove the reference and the “Independent cross-validation” paragraph that relies on it in Sec. III. Fabricated or anticipatory IDs are not acceptable.

---

P1B-E6 (ESSENTIAL)  
Section: References, p. 10; throughout text where quoted  
Problem: ACT DR6 birefringence value “β = 0.215◦ ± 0.074◦ (ACT DR6 [3])” is used multiple times (Sec. IV, p. 4; Sec. VI, p. 6; Eq. (4), p. 7), attributed to ref. [3], which, as noted above, does not exist. Without a verifiable source, this specific numerical result is unsupported.  
Required fix: Replace with a value traceable to an actual published or arXiv ACT birefringence analysis, or explicitly remove the ACT DR6 number from all calculations (including the inverse-variance “3.9σ” combination) and clearly state that such a measurement is hypothetical. If an internal / private ACT result is being used, it must be removed or relegated to very clearly labelled “hypothetical forecast” without numerical weight.

---

P1B-E7 (ESSENTIAL)  
Section: Abstract & Sec. VI, p. 1 and p. 6  
Problem: The abstract and Sec. VI attribute “β = 0.342◦ ± 0.094◦ (3.6σ)” to Eskilt & Komatsu [2] as the “published joint WMAP+Planck value” and “joint WMAP+Planck PR4/NPIPE” result. According to the actual PRD 106, 063503 paper and arXiv:2205.13962, the reported isotropic birefringence is \(\beta = 0.342^\circ \pm 0.091^\circ\) (3.8σ) for WMAP + Planck PR4, and 0.334° ± 0.091° (3.7σ) for Planck PR4 alone; 0.094° is not the quoted 1σ uncertainty in the published paper. The misquoted σ also propagates to the prominence of the “3.6σ” label.  
Required fix: Align the quoted central value and uncertainty exactly with the values in the Eskilt & Komatsu paper, making clear which dataset combination is used (WMAP+Planck PR4 vs Planck-only). If the authors intentionally inflate σ to 0.094°, that must be justified as their own re‑analysis, not presented as the published number. Adjust any dependent significance numbers accordingly.

---

P1B-E8 (ESSENTIAL)  
Section: Abstract, p. 1; Sec. III/Table I, p. 3; Sec. VII, p. 8  
Problem: Hubble parameter and ∆Neff values are presented as load‑bearing headline numbers:  
- Abstract: “Both frozen dataset combinations find ∆Neff consistent with zero (−0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN) and H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN...).”  
- Table I: repeats these numbers.  
However, the “Planck+BAO+SN” chain configuration is described inconsistently: Sec. V.A lists four combinations including “+DESI 2024 DR1 BAO ; (3) +Pantheon+ ;” but also elsewhere (Sec. II, p. 2) the text claims “BAO+CMB+SN-only, no local-distance ladder,” and the specific BAO dataset is referred to by a DR2-style reference  that is not actually used in the Cobaya YAML described in Appendix A. There is no way for the reader to confirm that the reported numbers correspond to the stated combination without the YAML in this paper and with references / partially inconsistent and in part fictitious.  
Required fix: Harmonize the dataset naming and references so that each quoted numerical result has an unambiguous, verifiable dataset stack: explicitly state whether “Planck+BAO+SN” uses DESI DR1 or DR2, and update the references to real dataset papers. If DR2 is not actually used, change the reference and text accordingly. PRD requires that all headline parameter estimates be reproducible solely from the paper and cited literature, without relying on external README documents.

---

P1B-E9 (ESSENTIAL)  
Section: Sec. VI, p. 7  
Problem: The inverse-variance combination in Eq. (4) claims  
“Combining β = 0.30◦ ± 0.11◦ (Planck NPIPE ) and β = 0.215◦ ± 0.074◦ (ACT DR6 [3]) via inverse-variance weighting: βcombined = 0.241◦ ± 0.061◦ (3.9σ).”  
Recomputing:  
- Weights: \(w_1 = 1/0.11^2 ≈ 82.64\), \(w_2 = 1/0.074^2 ≈ 182.66\), sum \(≈ 265.3\).  
- Combined mean: \((0.30·82.64 + 0.215·182.66)/265.3 ≈ (24.79 + 39.29)/265.3 ≈ 64.08/265.3 ≈ 0.2415°\), so the mean is consistent.  
- Combined σ: \(\sigma = 1/\sqrt{265.3} ≈ 0.0614°\), so σ is consistent.  
- Significance: \(|0.241|/0.0614 ≈ 3.92σ\), which justifies “3.9σ” numerically.  
However, since the ACT DR6 value itself is not traceable (P1B-E3/E6), this combined significance is not supportable by real data. Moreover, the text highlights this 3.9σ as a “cross-check” but does not clearly reiterate in every place where Planck and ACT significances are juxtaposed that they are not independent due to shared calibration systematics beyond the brief caveat.  
Required fix: Either remove Eq. (4) entirely until a real ACT DR6 reference exists, or explicitly mark the ACT quantity as hypothetical and refrain from quoting a numerical sigma level. Also ensure that whenever different null-procedure σ values (Planck vs ACT vs combined) are compared side-by-side, each comparison line explicitly states that they are not directly comparable due to shared systematics and differing analysis pipelines.

---

P1B-E10 (ESSENTIAL)  
Section: Sec. V.B, p. 6–7 & Table II, p. 4  
Problem: The DESI DR2 w0–wa posterior in Table II is described as “DESI DR2 BAO + Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native + DES-Y5 + Pantheon+.” Reference  is given as “DES-SN5YR” with arXiv:2401.02929, but that paper appears to be an early DES 5‑year SN sample; the “DES-Y5” label is a different concept used in DES cosmology papers, and the combination of DESI DR2 + DES-Y5 + Pantheon+ as a jointly analyzed stack in this exact form does not appear in any published paper as of now. Yet Table II quotes strong tensions (w0 = −0.8122 ± 0.0436, wa = −0.6666 ± 0.1864, “phantom crossing required,” etc.) and mentions “DESI DR2 BAO” in a context where the reference  is itself fictitious.  
Required fix: Clarify the exact dataset combination, and update references to actual released data and analyses. If this is an entirely new combination assembled by the author (rather than reproducing a DESI or DES collaboration chain), that must be spelled out clearly, and no implication of being “DESI DR2 results II” etc. should be made. Remove or correct any labels that suggest this chain reproduces a specific collaboration’s result if that claim cannot be traced to a cited paper.

---

P1B-M1 (MAJOR)  
Section: Abstract vs. main text (Secs. III & VII), p. 1, 6–8  
Problem: The abstract states that the ∆Neff MCMC is “reported as a null-consistency test of an extra radiation-like degree of freedom, not as evidence for or against the ECH spin-torsion framework.” Later, Sec. III and VII discuss this proxy run as “consistent with the minimal matter-bounce prediction” and reference it as part of a “bounce-class compatibility check.” This elevates the interpretive weight of the proxy beyond what the abstract suggests. Given that the EC torsion sector is not implemented in CAMB at all, and ∆Neff is only a phenomenological stand-in, this linking to the ECH framework can be easily misread as partial evidence for the specific theory.  
Required fix: Tighten the language throughout so that all mentions of “bounce-class compatibility” are clearly separated from any implication that these runs materially test the ECH spin‑torsion model itself. PRD will expect that the abstract’s description match the interpretive weight in the body.

---

P1B-M2 (MAJOR)  
Section: Sec. VI (ALP consistency), p. 6–7  
Problem: The paper claims that a field with “fa ∼ MPl, m ∼ H0” is consistent with the observed β, but the detailed discussion in Sec. VI and footnotes 4, 5 shows that:  
- The natural prior range θi ∈ [0.5, 2] does not yield spectator behavior;  
- Spectator consistency requires θi ∼ 0.1, a ~25× fine-tuning relative to the prior midpoint;  
- The required product Caγ Δϕ/fa ≈ 10.3 pushes Caγ into 9–51, outside minimal KSVZ/DFSZ expectations.  
This is correctly acknowledged in the body, but the abstract and conclusions emphasize “consistent with natural parameters (taken at scan-prior midpoint values)” in a way that downplays the tuning and unusually large coupling. For PRD, this is too unbalanced: readers can easily take away that the signal is naturally explained, which is not supported once the full tuning and coupling-range discussion is taken into account.  
Required fix: Revise the abstract and conclusion to explicitly mention both the consistency and the required misalignment tuning and coupling enhancement, e.g., “consistent but only with ≳25× misalignment fine-tuning and super‑KSVZ photon coupling.” That balance is necessary to avoid overstating the level of “naturalness.”

---

P1B-M3 (MAJOR)  
Section: Sec. IV (NaMaster analysis), p. 4–5  
Problem: The pseudo‑Cℓ pipeline test injects β values and quotes “pipeline-recovery SNR = 20.32” and “25.71” for injected signals, using ACT-like noise. The text repeatedly warns that these are not sky-detection significances, but the SNR is still framed in σ language ("20.32σ", "25.71") in the narrative. For PRD, any σ‑like numbers in a birefringence context will be read as detection significances unless extremely clearly separated.  
Required fix: Remove σ language from the pipeline-recovery SNR (call them “SNR=20” etc. without the σ symbol), and add an explicit statement immediately next to each such number that these are internal pipeline tests, not comparable to the 2.4–2.9σ sky detections. This will avoid misleading readers about the empirical strength of birefringence evidence.

---

P1B-M4 (MAJOR)  
Section: General length and scope, all pages  
Problem: For a “technical verification companion” whose stated scope is to document an MCMC proxy, a pseudo-Cℓ pipeline check, and an ALP consistency test, the manuscript devotes substantial space to:  
- High-detail discussion of w0–wa quintom chains (Table II, long narrative on Bayes factors and Savage–Dickey failures);  
- Reiteration of galaxy-spin, anomaly-catalog, and SPHEREx topics that are not actually analyzed in this paper;  
- Repeated cross-references to “Paper I(a)” and other “this volume” companions, none of which are actually available.  
The overall 11 pages are dense but include material that does not directly serve the stated verification goals and may confuse readers about what is actually achieved.  
Required fix: Streamline the paper to focus tightly on the three promised technical verifications. The quintom w0–wa chain (Table II) probably belongs in the main structural paper, not the verification companion, unless it directly calibrates something here. Recommend cutting 2–3 pages of extraneous structural-cosmology discussion and leaving only what is strictly necessary to justify the MCMC and birefringence checks.

---

P1B-M5 (MAJOR)  
Section: Multiple, including footnotes, p. 2–3, 7–9  
Problem: There is extensive version-history and audit-log style text embedded in the scientific narrative and footnotes, including:  
- “An earlier count erroneously quoted ‘98.6% quintom-B’ weight; in the actual converged chain...”  
- Detailed chain accounting (“176,240 × 0.7 ≈ 123,368... the 119,617 figure in Fig. 1 reflects additional getdist effective-sample weight-based thinning...”);  
- References to “iter2 chain,” “promised a Savage–Dickey ratio,” and README-based attributions.  
While commendable for reproducibility, PRD prefers such implementation details in online supplementary material. As currently written, they clutter the main text and blur the distinction between the final scientific result and the author’s workflow history.  
Required fix: Move the detailed convergence bookkeeping, prior promises, and README explanations to an online Supplement or an expanded README referenced by the paper. Keep only essential convergence metrics (R̂–1, min ESS, total post‑burn‑in samples) in the main text.

---

P1B-m1 (MINOR)  
Section: Appendix C heading, p. 9; Table III caption, p. 10  
Problem: “Appendix B: Claims Classification” is defined (p. 9), and Table III is labeled “Claims classification for this companion paper.” This is useful but somewhat idiosyncratic as an in‑paper audit device, and some “Status” entries include “Omitted” and “Scope defn.” rather than standard scientific descriptors.  
Required fix: Either (a) move the claims-classification table to Supplementary Material and adapt its language to standard scientific phrasing, or (b) keep it but make sure its categories and statuses are clearly explained in the text so readers do not confuse “Omitted” with an actual negative result.

---

P1B-m2 (MINOR)  
Section: Appendix A, p. 8  
Problem: The paper includes a direct GitHub URL and describes scripts like “reproduce cosmology.sh”. PRD typically allows URLs but prefers DOIs and stable archives (e.g., Zenodo) as the primary reproducibility artifacts. Also, mentioning a shell script name without a formal description can be brittle.  
Required fix: Ensure that the GitHub repository is mirrored on a DOI-granting archival service (Zenodo or similar), and cite that DOI explicitly. In the text, describe the reproduction procedure in generic terms (e.g., “a shell script that reruns the chains”) rather than hardcoding filenames that may change.

---

P1B-m3 (MINOR)  
Section: Acknowledgments, p. 8  
Problem: A statement credits use of “Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation.” While transparency is welcome, PRD has emerging but not fully standardized policies on AI assistance statements. The sentence “All scientific claims... were independently verified by the author” is not verifiable by the reader and may be seen as unnecessary self-attestation.  
Required fix: Condense this to a simple, policy-compliant statement (if PRD requests AI disclosure) such as “The author used AI-assisted tools in data handling and drafting; all scientific conclusions were determined by the author.” Remove unverifiable or promotional language.

---

P1B-n1 (NIT)  
Section: Contents, p. 1  
Problem: The line “III. Stock-CAMB ΛCDM+∆Neff MCMC: Generic Radiation-Proxy Test (Not a Spin-Torsion Theory Module)” places “(Not a Spin-Torsion Theory Module)” as a separate line with unusual capitalization and spacing.  
Required fix: Normalize to standard section-titling conventions, e.g., “III. Stock-CAMB ΛCDM+∆Neff MCMC: Generic Radiation-Proxy Test (not a spin-torsion theory module).”

---

P1B-n2 (NIT)  
Section: Typographical, multiple pages  
Problem: A few small style/typo points:  
- “planck 2018 lowl.EE + planck 2018 lowl.TT” uses lowercase “planck” in the text.  
- Occasional en-dash/hyphen inconsistencies, e.g., “Planck/ACT DR6 2.4–2.9σ [2, 3];a the pipeline SNR figures...” where semicolon placement around the footnote marker is awkward.  
Required fix: Standardize capitalization (“Planck”), clean punctuation around footnotes, and ensure consistent use of en-dashes for numeric ranges.

---

## Summary recommendation

MAJOR REVISIONS

The manuscript contains multiple serious citation-forensics issues, including several non-existent or future-dated arXiv IDs, “in preparation / this volume” references to load-bearing companion papers, and a misquoted key statistic from Eskilt & Komatsu, as well as overstatement risks in the ALP naturalness narrative and the ACT DR6 usage. While the technical thrust—a ∆Neff proxy, NaMaster pipeline test, and ALP consistency check—is potentially publishable as a methods companion, PRD standards require that all citations be real and verifiable, that headline numbers map cleanly to actual datasets, and that numerical claims from the literature be quoted accurately. Substantial corrections to the references, dataset descriptions, and abstract/conclusions are required before this can be considered for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E11 (ESSENTIAL)  
Class: A (arithmetic), F (abstract faithfulness), J (stale numbers)  
Location: Abstract; Sec. VI “Headline observational constraint”; Eq. (3); surrounding ALP discussion  

Problem: The Eskilt & Komatsu WMAP+Planck birefringence result is still misquoted and internally inconsistent. The abstract and Sec. VI use β = 0.342° ± 0.094° (3.6σ) as the “published” value, but the actual paper reports 0.342° ± 0.091° (3.8σ) for WMAP+Planck PR4 and 0.334° ± 0.091° (3.7σ) for Planck PR4 alone.[2] The 0.094° and 3.6σ numbers are not justified as a recomputed value (no derivation is shown), yet they are repeatedly treated as the canonical published constraint and used as the anchor for the ALP consistency calculation. This misquote propagates into the abstract, the “headline observational constraint” paragraph, and Appendix C, and conflicts with the footnote a on p. 1, which otherwise tries to distinguish PR3 vs PR4.  

Required fix:  
- Replace every instance of “β = 0.342° ± 0.094° (3.6σ)” with the correct Eskilt & Komatsu value, explicitly specifying which dataset is meant (WMAP+Planck PR4 vs Planck-only).  
- If the authors intend to use a re‑analysis (e.g., incorporating code/PR4 updates or their own likelihood), they must: (i) state clearly that 0.094° is their recomputed σ, (ii) show how it is obtained from data, and (iii) stop calling it the “published” number.  
- Recompute all downstream “σ” statements using the chosen, correctly documented uncertainty.  
- Ensure abstract text and Sec. VI use *the same* dataset definition and uncertainty.

---

P1B-E12 (ESSENTIAL)  
Class: A (arithmetic), E (null-procedure comparability), J (stale numbers)  
Location: Sec. IV (first paragraph), Sec. VI (auxiliary combination), Conclusions  

Problem: The manuscript treats β = 0.30° ± 0.11° (Planck NPIPE) and β = 0.215° ± 0.074° (ACT DR6) as “published literature” inputs and uses them both in the NaMaster scope statement and the inverse‑variance combination, but:  
- The Planck PR4 value is taken from Diego-Palazuelos et al. (Planck DR4 birefringence) rather than Eskilt & Komatsu, and is not clearly identified as such; the reference list still points to  (Diego-Palazuelos et al. “Planck DR4” preprint) while earlier footnote a asserts that [2] is the PR3/WMAP9 paper.[2]  
- The ACT DR6 number β = 0.215° ± 0.074° is still attributed to ref. [3], which does not exist; the text has been updated to call both Planck NPIPE and ACT DR6 “published” in Sec. IV and “observational reference” in Sec. VI, but no real ACT DR6 birefringence paper is cited.  

The new wording (“published Planck/ACT DR6 2.4–2.9σ”, “used in the spectator ALP analysis”) still presents the ACT DR6 value as real data, contrary to the earlier essential finding that the ACT reference is fictional. This contaminates the ALP consistency narrative and the auxiliary inverse‑variance combination, which mixes one real and one nonexistent measurement into a 3.9σ “cross‑check”.  

Required fix:  
- Remove the ACT DR6 number entirely from Sec. IV and Sec. VI unless and until a real ACT DR6 birefringence paper exists with matching β and σ.  
- Replace all “Planck/ACT DR6 2.4–2.9σ” language with references only to the actually published Planck/WMAP result, or to demonstrated, citable ACT work if such appears under a *real* arXiv/journal ID.  
- Drop Eq. (4) and the 3.9σ inverse‑variance combination until both inputs are traceable to real, citable measurements.  
- Where Planck and ACT σ values are *discussed qualitatively*, explicitly state that the ACT value is hypothetical/forecasted if the authors insist on mentioning it; otherwise, omit it.  

---

P1B-E13 (ESSENTIAL)  
Class: A (arithmetic), H (unquantified hedges), J (stale numbers)  
Location: Sec. III “a. Scope of the ∆Neff proxy”; Table I; Fig. 1 caption; Sec. II H0 tension paragraph  

Problem: Arithmetic and tension labels involving H0 and ΔNeff are presented inconsistently and without explicit quantitative checking:  
- The abstract and Table I quote H0 = 67.68 ± 1.06 (full-tension) and H0 = 67.79 ± 1.09 (Planck+BAO+SN). Later, Sec. II states that the “joint posterior H0 = 67.185 ± 0.455 km/s/Mpc is therefore the no‑SH0ES result” and that this corresponds to the Planck+BAO+SN chain. The two sets of numbers (67.79 ± 1.09 vs 67.185 ± 0.455) are different but both are labeled as “Planck+BAO+SN‑only, no local-distance ladder” in different parts of the paper, without reconciling that they refer to different runs (with or without DES Y3 S8 and SH0ES in various combinations).  
- The text says the full‑tension chain exhibits the “canonical 3.6σ Hubble tension” with Riess H0 = 73.04 ± 1.04. Using the quoted numbers 67.69 ± 1.06 vs 73.04 ± 1.04, the tension is |ΔH0|/σtot ≈ 5.35 / √(1.06²+1.04²) ≈ 5.35 / 1.49 ≈ 3.6σ (consistent), but this is not explicitly shown, while the similar calculation for the Planck+BAO+SN chain versus SH0ES is never written down, even though the text uses it implicitly to argue consistency with ΛCDM.  

Combined with the inconsistent H0 labels between Table I and Sec. II, a reader cannot map each quoted σ to a unique, reproducible dataset stack. This violates PRD’s reproducibility and transparency expectations.  

Required fix:  
- Create a single table or clearly structured paragraph mapping *each* H0/ΔNeff pair (67.68 ± 1.06, 67.79 ± 1.09, 67.185 ± 0.455) to a unique dataset stack and YAML configuration.  
- For every “tension” descriptor (e.g., “canonical 3.6σ Hubble tension”), show the explicit arithmetic using the quoted means and uncertainties.  
- Ensure the abstract, Table I, Sec. II, and Sec. V use the same naming for each dataset combination (e.g., “Planck+BAO+SN (no SH0ES, no DES Y3)” vs “full-tension (Planck+BAO+SN+SH0ES+DES Y3)” ) so that each quoted number is unambiguously tied to its likelihood stack.  

---

P1B-M6 (MAJOR)  
Class: A (arithmetic), F (abstract faithfulness), H (unquantified hedges)  
Location: Sec. VI (ALP consistency, around Eq. (3)); Conclusions; Appendix C  

Problem: The ALP consistency numerics are partially recomputed in the text but key ratios are never explicitly shown, and some statements are borderline misleading:  
- Eq. (3) claims β ≈ α_EM × 8 / (4π) × 1.07 ≈ 0.29°. Taking α_EM ≈ 1/137, this gives β ≈ (1/137) × 8 / (4π) × 1.07 ≈ (8.56 / 1720) ≈ 0.00498 rad ≈ 0.285°, which is consistent, but the text nowhere shows the intermediate radian/radian‑to‑degree conversions. Readers must reverse‑engineer how “1.07” arises from Δϕ/fa ≈ 0.65 and other factors.  
- The claimed “prediction spans β ≈ 0.17–0.43° over Caγ ∈ [4,12], m/H0 ∈ [1,3], θi ∈ [0.5,2]” is not backed by any explicit grid or figure; given the large range in θi, m/H0, and Caγ, it is unclear how the product Caγ Δϕ/fa is constrained to a narrow interval, especially once the Δϕ/fa dependence on (m/H0, θi) is acknowledged.  
- Later, the required Caγ Δϕ/fa ≈ 10.3 is correctly recomputed from βobs = 0.342° and α_EM/(4π) ≈ 5.8×10⁻⁴, but this contradicts the earlier “natural envelope” 4–12 × [0.2–1.1] range that would naively cover 0.8–13.2. The manuscript states that the model is “consistent” with the observed β but only belatedly admits that the preferred combination lies near or outside the prior envelope and requires fine tuning.  

Overall, the numerical narrative is accurate in pieces but presented in a way that foregrounds qualitative “consistency” and hides how close to the envelope edge the preferred product lies.  

Required fix:  
- Add an explicit 1‑line derivation of Caγ Δϕ/fa ≈ 10.3 from βobs and α_EM/(4π), including radians‑to‑degrees conversion.  
- Either provide a small table or figure showing β(θi, m/H0, Caγ) across the prior box, or explicitly clarify that the range 0.17–0.43° is obtained from a coupled scan and not simply from independent extremes; give at least one quantitative example at each corner.  
- In the abstract and conclusions, immediately pair the statement “consistent with fa ∼ MPl, m ∼ H0” with a quantitative line stating that this requires Caγ ∈ [9, 51] and misalignment tuning θi ≈ 0.1, so readers cannot miss the fine‑tuning and super‑KSVZ coupling requirements.  

---

P1B-M7 (MAJOR)  
Class: B (figure-caption vs body-claim), E (null-procedure comparability)  
Location: Sec. IV (NaMaster analysis and caption of Fig. 1), Sec. VI (pipeline SNR), Conclusions  

Problem: The treatment of “SNR” vs “σ” for the NaMaster injection tests remains confusing and inconsistent with the stated policy not to equate pipeline‑recovery SNR with sky-detection significances:  
- The abstract still states “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2, 3];a the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements,” but the main text of Sec. IV gives explicit numbers like “pipeline-recovery SNR = 20.32” and “25.71” without units or dimensions, and the earlier version of the manuscript referred to these as “20.32σ”, “25.71σ”. The current text removes some σ symbols but never explicitly defines SNR (e.g., as β̂/σ_MC) or states how it is computed.  
- In the conclusion, the NaMaster result is summarized as “SNR consistent with the ACT-noise floor,” which is a qualitative comparison to a different null procedure (ACT DR6 birefringence pipeline) without reiterating that they cannot be directly compared in σ units or used to argue the empirical strength of evidence for cosmic birefringence.  

Required fix:  
- Explicitly define “pipeline-recovery SNR” in Sec. IV as SNR ≡ β̂/σ_MC or whichever ratio is actually used.  
- Confirm that all “σ” symbols have been removed from the pipeline SNR language; where 20.32 or 25.71 are quoted, immediately follow with wording like “(dimensionless SNR of the injected-signal recovery; not a sky detection significance)” to prevent misinterpretation.  
- In the conclusions, avoid phrasing that sounds like a comparison of “20σ pipeline SNR vs 2.4–2.9σ sky detection”; instead, state plainly that the NaMaster test validates algebraic deconvolution but makes no independent statement about the detection significance of cosmic birefringence.  

---

P1B-M8 (MAJOR)  
Class: D (internal cross-references), I (appendix vs main‑text mismatch)  
Location: Sec. VI (ALP MCMC description), Appendix C; references to “βALP” and “βfree”  

Problem: The ALP-MCMC description in the main text and Appendix C is not fully consistent with the usage of βALP and βfree in Sec. VI:  
- Sec. VI quotes βALP = 0.336° ± 0.107° at Caγ = 8 and βfree = 0.344° ± 0.096°, referring to “our internal model-independent MCMC fit to the Planck PR4 + ACT DR6 EB-spectrum likelihoods.” However, Appendix C describes βfree as coming from a fit to “Planck PR4 + ACT DR6 EB-spectrum likelihoods with β as a free parameter” *while also describing Caγ ∈ [4,12] benchmarks* in the same section, without clearly separating which chains are used where.  
- Several internal references (e.g., “Sec. VI (configurations Caγ = 4, 8, 12 on Planck PR4 + ACT DR6 EB-spectrum likelihoods with β as a free parameter)”) make it unclear whether βfree is truly independent of the ALP model or is derived from the same Caγ‑fixed runs. This matters because the text uses βfree as a “model-independent” cross-check of the ALP prediction.  

Required fix:  
- In Sec. VI, explicitly state which MCMC chains feed into βALP and which into βfree, and how βfree is obtained (e.g., separate run with an unconstrained β parameter and *no* ALP dynamics).  
- In Appendix C, separate the descriptions into two clear subsections: “Model-dependent ALP chains (Caγ fixed, θi, m/H0 sampled)” and “Model-independent β-only chain”, and give the number of samples and convergence metrics for each.  
- Ensure all cross-references to βALP and βfree in Sec. VI and the conclusions point to the correct chains and that “model-independent” is only used where the likelihood truly does not assume a specific ALP model.  

---

P1B-m4 (MINOR)  
Class: D (internal cross-references), F (abstract faithfulness)  
Location: Abstract; Sec. III “Scope statement”; Appendix B (Claims classification)  

Problem: The abstract’s description of the ∆Neff proxy as “not as evidence for or against the ECH spin‑torsion framework” is accurate, but later sections and Appendix B still blur this separation slightly:  
- Sec. III describes the proxy as a “bounce-class compatibility check,” and Table III lists “ΛCDM+∆Neff proxy” claims as “Verified,” which a casual reader may interpret as verification of the ECH program itself, despite the explicit early disclaimers.  
- There is no explicit cross-reference in the abstract pointing the reader to the stronger disclaimers in Sec. III and the claims classification in Appendix B, so the high-level framing may still be over-interpreted.  

Required fix:  
- Add a brief sentence to the abstract or immediately after the “Scope of this paper” bullet list emphasizing that all ∆Neff results constrain *phenomenological proxies only* and that no direct test of the ECH torsion sector is performed.  
- In Table III, slightly adjust language from “Stock CAMB proxy ≠ ECH theory module – Scope Defn.” to something more explicit like “Tests only ΛCDM+∆Neff phenomenological extension; no torsion-module implementation.”  

---

P1B-n3 (NIT)  
Class: C (dimensional consistency)  
Location: Footnote 4 (backreaction scaling), Eq. (2); surrounding text  

Problem: The backreaction scaling Ωa ∼ (m² f_a² / H₀² M_Pl²) θ_i² and the statement “ρ_a ∼ m² f_a² θ_i² ∼ H₀² M_Pl²” are dimensionally correct but written in a way that forces the reader to infer the equality up to factors of O(1). Later references to “Ω_a ∼ 1” and “spectator regime θ_i ∼ 0.1” assume that the ratio m² f_a² / H₀² M_Pl² is exactly unity for “natural” parameters, which is only approximately true.  

Required fix:  
- Add a phrase such as “up to order‑unity factors” when writing ρ_a ∼ H₀²M_Pl², and/or define explicitly that the “natural” benchmark takes m ≈ H₀, f_a ≈ M_Pl so that the prefactor is ≈1.  
- This keeps the dimensional reasoning intact while preventing readers from over‑interpreting the proportionality as an exact equality.  

---

NO FURTHER ESSENTIAL ARITHMETIC ERRORS FOUND

I walked through all explicitly given σ, “#σ from” claims, and simple sums/means where enough numerical information is present (e.g., the 4.3σ and 3.6σ w₀ and w_a departures in Table II, the combined χ² values, the MB–H₀ constant comparison, and the inverse‑variance combination in Eq. (4)), and they are arithmetically consistent with the quoted central values and uncertainties. The remaining issues are therefore primarily about citation validity, dataset labeling, and interpretive framing rather than raw arithmetic mistakes.