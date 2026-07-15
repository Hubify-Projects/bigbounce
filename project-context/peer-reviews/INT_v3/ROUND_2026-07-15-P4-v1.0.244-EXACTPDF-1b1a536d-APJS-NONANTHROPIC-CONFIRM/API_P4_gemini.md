# INT API Review — P4 v1.0.244 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.244  model: gemini-3.1-pro-preview
provenance: commit=bbdc79db20500e6aa64f2d6f246120a01c53d2bb  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=1b1a536dfbd7d07ea4958304d6694582ce3b5ec7d6ce16b08b5d17fdefc15669
packet: key=2e327bb11dbebac205d03a017b8eb2a15cd18aab05813ac2feb163c2db068a07  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-15T08:57:37.534491Z  |  latency: 58.5s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 58.5, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "nEtXaoObEv-rqtsPlMTr8As", "usage": {"candidatesTokenCount": 672, "promptTokenCount": 13631, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 13520}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 1578, "totalTokenCount": 15881}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**

1. **[MINOR] Inline File Paths and Provenance Clutter:** The manuscript embeds dozens of long literal file paths (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/c12_r24conf_local_batch.json`) directly within the main text paragraphs. While the dedication to exact reproducibility and provenance is exemplary and highly suited for ApJS, this practice severely disrupts the readability of the scientific narrative. *Recommendation:* Move these artifact paths to a unified provenance table in the Appendix, or use numbered footnotes/references that point to a directory tree in the Data Availability section.
2. **[MINOR] Undefined Internal Nomenclature ("DP4-XX"):** The text frequently refers to "open gates" such as DP4-15, DP4-16, DP4-17, and DP4-21 (e.g., "The missing joint covariance is open gate DP4-17" in Sec III.B and Sec VI.D). These appear to be internal project-tracking acronyms and are never explicitly defined in the text. *Recommendation:* Define this acronym upon first use, or simply replace it with descriptive text (e.g., "Open Problem 1" or "Future Work: Joint Covariance"). 
3. **[MAJOR] Path to Closing the Transfer Function Gap:** The author is appropriately careful to state that without a physical morphology transfer function (the aforementioned "DP4-15"), the observed-label null cannot be translated into a rigorous primordial parity bound. However, since this is a methods-and-catalog release intended for downstream use, the manuscript must explicitly outline *what specific data, simulations, or calibration procedures* are required for the community to close this gap. *Recommendation:* Expand Section VI.D to specify how a user of this catalog should go about deriving $g$ (the transfer slope) beyond the illustrative scalar dilution estimate provided, perhaps via matched image simulations or future spectroscopic cross-matches. 
4. **[MINOR] Overloaded Captions and Footnotes:** The captions for Tables VI and VII, as well as Footnote 1, contain extensive, load-bearing physical analysis regarding the monopole-mask leakage generative null (specifically the 99.32% vs 99.33% reproduction fraction discussion). *Recommendation:* Move the substantive interpretation of the generative null diagnostics into the main text of Section IV.D to ensure it is not missed by readers skimming the tables.
5. **[MINOR] Table XIII (Bias-hardening test results):** The table states that "All 7 tabulated tests pass" but lists T1, T2, T3, T4, T6, T7, T8. The text explains that T5 (Linear Pearson RA) was removed, which explains the numbering jump. *Recommendation:* Briefly note the omission of T5 in the table caption itself so the reader does not assume a formatting error.

**One sentence:** The central claim of a null chirality dipole in the equivariant, high-confidence observed-label sample is robustly supported by an exceptionally rigorous suite of systematics, masking, and bias-hardening diagnostics.