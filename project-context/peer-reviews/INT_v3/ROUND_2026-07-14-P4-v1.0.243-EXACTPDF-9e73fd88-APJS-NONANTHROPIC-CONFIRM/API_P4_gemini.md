# INT API Review — P4 v1.0.243 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.243  model: gemini-3.1-pro-preview
provenance: commit=36badcbdf498123413031aa0a9504127d48f2054  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=9e73fd888699058d421043b0dd2de5d37d2aeb36fe37e8dd1c0bf5409e947d19
packet: key=329883ec9a15e7ba0512bd0fefc8fe757eb4fb2cc236cfe4e9865eeb5391fe37  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-14T19:08:18.457131Z  |  latency: 61.6s  |  attempt: 1
usage: {"promptTokenCount": 14151, "candidatesTokenCount": 496, "totalTokenCount": 16700, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 14040}, {"modality": "TEXT", "tokenCount": 111}], "thoughtsTokenCount": 2053, "serviceTier": "standard"}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**
1. [MINOR] Abstract & Section VI.D / Throughout: The manuscript frequently references "DP4-15", "DP4-16", "DP4-17", and "DP4-21" to denote open analytical gates/future work. The prefix "DP4" is never explicitly defined in the text (presumably an internal project tracker, "Data Paper 4", or "Decision Point"). Please define this acronym on first use or replace the alphanumeric codes with descriptive text. 
2. [MINOR] Formatting / Throughout: The continuous embedding of literal JSON and script file paths (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/...`) directly within the main text paragraphs interrupts the reading flow. While the commitment to absolute reproducibility is highly commendable and well-suited for ApJS, consider moving these specific paths to footnotes, or replacing them with brief citation keys that point to a consolidated provenance table in the Appendix.
3. [MINOR] Section IV.A (Catalog Statistics): The text notes that "The mean classification confidence (0.951) far exceeds the independent GZ1 three-class accuracy (58.7%)." It would be beneficial to explicitly remind the reader here that modern deep neural networks (including ViTs) are famously miscalibrated and tend toward extreme overconfidence on raw softmax outputs prior to temperature scaling. This well-known phenomenon perfectly contextualizes and justifies your robust methodological choice to treat these outputs strictly as monotonic ranking scores rather than true frequentist probabilities.
4. [MINOR] Section VI.B: In Equation 4, the idealized full-sky variance is given without the dilution factor $g$, yielding an observed-label precision floor. While the text later explains the $g=0.398$ scalar transfer, explicitly stating immediately below Eq. 4 that this is the *observed-label* variance (and that the physical variance would scale by $1/g$) will prevent readers from conflating the idealized observed floor with the physical sensitivity floor.

**ONE SENTENCE:** 
The central claim that the previously reported spiral galaxy chirality dipole is a spurious artifact of classifier bias coupled with the survey footprint—and that it vanishes into a statistically null result under rigorous equivariant test-time post-processing—is convincingly supported by exceptional systematic controls.