# P1B R-CONFIRM-2026-09-22 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `arxiv/paper1b_namaster_proof.pdf` sha256=c7cac6c9f16ca00d6494f6108f0d80c925c074596277cce7e1be6f70d3334a22 pages=16
**Review packet(s)**: `2c215b0161d83d325fb87753aff27384deb3a2cb3fbd3a963da88ed2a2d74a5c, 31da4caf401d047a59b8e075bdfe4bd8d692c55e58448e43448b1611dee80d88`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (1686 chars)
**Wall time**: 110.2s

---

**Referee Report — P1B (JORS-SOFTWARE)**

**P1B-E1 (ESSENTIAL)** — Section 1 (p. 2) and Scope limits (p. 9): The paper states “namaster-proof is deliberately not an installation dependency: window functions require a workspace exposing get_bandpower_windows()… The first must return a finite [4, n_b, 4, n_ℓ] tensor…” yet immediately concedes “the blind test exercises this repository’s own spin-0 MASTER estimator rather than NaMaster/PyMaster itself” and “an equivalent instrumental hook has not been added inside NaMaster”. The core software claim is therefore untested on the artefact it purports to verify. Required fix: either integrate the hook into PyMaster/NaMaster or remove every sentence that presents the package as a detector for the public NaMaster pipeline.

**P1B-E2 (ESSENTIAL)** — Abstract (p. 1) vs. §6 and Table 3 (p. 5): Abstract asserts “All detection claims are reported as class-level counts, never as run-level probability intervals”. Table 3 and the surrounding text report exactly that (class-level 20/20, 4/4, 0/5 etc.) while simultaneously publishing per-arm n=5 counts and Clopper–Pearson bounds. The abstract claim is false on its face. Required fix: delete the sentence or rewrite the abstract to match the actual reporting practice.

**P1B-E3 (ESSENTIAL)** — Abstract (p. 1) and §6 (p. 4–5): Abstract claims the package “establishes the primitive as a detector of structural shortcuts in instrumental steps, not of forged metadata or of value-level shortcuts taken downstream of a declared intermediate”. Body shows S5 (metadata forgery) escapes every rule in all four batches and S6 (effective-multipole) is only caught by a rule (R7) that was pre-registered against that exact class. The abstract statement is therefore unsupported by the evidence presented.

**P1B-E4 (ESSENTIAL)** — Entire §6 and Tables 2–4: The decision rules R0–R8, the four-batch sealed protocol, the “pre-declared success criterion”, the “pilot, rule-development round”, and the repeated use of internal labels (“R7”, “R8”, “batch 2 is the primary result”) constitute internal audit bookkeeping, not a reusable software contribution. JORS software metapapers must describe a general tool; this is a lab notebook of one researcher’s threat model.

**P1B-M1 (MAJOR)** — Length: 16 pages for a JORS software paper. JORS guidelines and comparable submissions (e.g., reprozip, signac, datalad metapapers) are 4–8 pages. The excess is almost entirely narrative of the blind-test protocol rather than API, usage, or architectural description.

**P1B-M2 (MAJOR)** — §11 Limitations (p. 12) and Scope limits (p. 9): The paper itself lists that it does not create masks, estimate covariances, choose likelihoods, or infer cosmological parameters, and that the blind test never ran on NaMaster. These are not minor caveats; they remove the claimed use case.

**P1B-M3 (MAJOR)** — Abstract quantitative claims vs. body: Abstract states “the mode-coupling matrix and decoupled bandpowers agree with NaMaster to round-off (≲5×10^{-13} and ≲2×10^{-12} relative difference)”. Table 5 (p. 9) gives exactly those numbers, but only for the in-house estimator vs. PyMaster 3.0 on N_side=64, ℓ_max=95. No equivalent table exists for the production NaMaster 2.6 / PyMaster 2.6 configuration used in the CAMB campaign described two paragraphs earlier. The abstract number is therefore not traceable to the claimed production artefact.

**P1B-M4 (MAJOR)** — §7 (p. 10): The provenance discussion cites in-toto, SLSA, Sigstore, ReproZip, etc., but never demonstrates that namaster-proof produces any of those attestations. It only produces JSON receipts with SHA-256. The section is therefore unsupported marketing.

**P1B-N1 (NIT)** — Future date on title page: “September 5, 2026 — manuscript revision v2B.0.23(2026-09-05 12:00 PT)”. This is internal versioning language that should not appear in a submitted manuscript.

**P1B-N2 (NIT)** — Multiple instances of internal tags (“R0–R6”, “R7”, “R8”, “S1–S6”, “batch 1 pilot”, “wall-clock-would-fire”) remain in the body text. These must be removed.

**P1B-N3 (NIT)** — Table 1 caption and header use “namaster-proof” in lowercase while the package name is consistently title-cased elsewhere; trivial inconsistency.

**Summary recommendation: REJECT**

The manuscript is an internal verification log of a single-researcher cosmology workflow, not a reusable software artefact suitable for JORS. It fails the venue’s requirement that the described software be the primary contribution, that claims be substantiated on the target system (NaMaster), and that the narrative be free of lab-notebook bookkeeping. The abstract contains multiple statements that are directly contradicted by the body. Even after removing the internal-audit prose, the remaining software contribution is too narrow and the central claim (receipts detect structural shortcuts in the public NaMaster pipeline) is untested.

---

## PASS 2 — self-critique findings (what initial review missed)

**P1B-E5 (ESSENTIAL)** — §6 (p. 5) and Table 3: The text states “20/20 runs (one-sided 95% Clopper–Pearson lower bound 0.473 on the class-level detection rate”. The quoted bound 0.473 is exactly the Clopper–Pearson one-sided 95% lower limit for 4/4 successes (0.05^{1/4}≈0.4729), not for 20/20 (which is ≈0.832). The reported numerical claim is therefore arithmetically false; the authors appear to have used the number of classes rather than the number of runs.

**P1B-M5 (MAJOR)** — Abstract (p. 1) vs. Table 5 (p. 9) and §6 (p. 9): The abstract asserts agreement “with NaMaster to round-off (≲5×10^{-13} and ≲2×10^{-12} relative difference)” for the production configuration. Table 5 and the surrounding paragraph give those exact figures only for the in-house spin-0 MASTER vs. PyMaster 3.0 on an N_side=64, ℓ_max=95 test set. No equivalent matrix or band-power comparison is supplied for the actual NaMaster 2.6 / PyMaster 2.6 + CAMB campaign (N_side=512, ℓ_max=1024) described two paragraphs earlier. The abstract quantitative claim is therefore not supported by the data shown for the stated production artefact.

**P1B-N4 (NIT)** — §6 (p. 5): The sentence “one-sided 95% Clopper–Pearson lower bound 0.473 on the class-level detection rate, the only i.i.d. unit available” is internally inconsistent: the parenthetical already concedes that the inferential unit is the class, yet the preceding clause treats 20/20 runs as the sample size for the bound. The statistical wording is therefore self-contradictory even before the numerical error in E5.

No other new arithmetic, cross-reference, dimensional, or faithfulness discrepancies were identified beyond the three items above.