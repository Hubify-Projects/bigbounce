# INT API Review — P3APJS v3.1.161-apjs — gemini (gemini-3.1-pro-preview)
paper: P3APJS  version: v3.1.161-apjs  model: gemini-3.1-pro-preview
provenance: commit=913f5033  pdf=pipelines/p3_anomaly_engine/paper3_apjs.pdf  sha256=ef7065b05badbdfe8bbeaf44f04895bccbc06354044a63c1651a4a8e5d5b56d1
modality: native-PDF (inline_data base64)
UTC: 2026-07-14T09:24:52.097858Z  |  latency: 34.7s  |  attempt: 1
usage: {"promptTokenCount": 15754, "candidatesTokenCount": 618, "totalTokenCount": 18711, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 15600}, {"modality": "TEXT", "tokenCount": 154}], "thoughtsTokenCount": 2339, "serviceTier": "standard"}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: REJECT

ISSUES:
1. [MAJOR] DESI Catalog Usability and Provenance: Section 2.2 explicitly states that "the released tid column mixes real DESI TARGETIDs (26,218; 13.4%) with internal hashed identifiers (169,611; 86.6%)," and notes that "only ≈1.3% of the released rows resolve... and are re-pullable." The author admits this is "structurally bounded by pod-lost input linkage." Because the vast majority of the anchor DESI anomaly catalog cannot be traced back to actual astronomical coordinates or public spectra, the catalog is scientifically unusable for downstream follow-up. 
2. [MAJOR] Unrecoverable Code, Models, and Data: The manuscript repeatedly acknowledges that primary models, checkpoints, and output tables were lost due to an "exited compute node" or "never committed" code. This includes the entire native Planck model and top-200 table (Section 3.6), the LAMOST per-object table (Section 3.4), and the eROSITA production scoring code and canonical score axis (Section 3.5). A data-catalog paper cannot be published in ApJS if the core data products and generating code are admittedly permanently lost and irreproducible.
3. [MAJOR] Inclusion of Synthetic Data: Section 3.7 discloses that the released Gaia DR3 parquet file contains "synthetic-placeholder fallback" data rather than real Gaia data, complete with "magnitudes outside the physical Gaia range." While the author "quarantines" this in the text, publishing an immutable data release repository that contains known fake/synthetic data as part of an astronomical catalog is unacceptable for a journal standard.
4. [MAJOR] Publication of Failed Diagnostic Data: Section 3.6 states that because the native Planck results were lost on a pod, the released Planck table is instead drawn from an early cross-transfer scan that "fails the Path-C gate" and has a massive validation loss. Releasing a known-failed diagnostic artifact in place of the validated science product undermines the scientific validity of the catalog.
5. [MAJOR] Methodological Flaws (Data Leakage): Section 2.2 notes that for the tabular catalogs (NEOWISE, eROSITA, Gaia), the feature normalization scalers were "fit on the full sample rather than the training split alone," admitting that "validation-set (including tail) information enters the normalization constants." The author acknowledges this is bad practice but leaves the pipeline uncorrected, relying on unverified assumptions that it does not reorder the anomaly tail.

The central claim of a validated multi-survey anomaly catalog is not supported and is inappropriate for ApJS, as the underlying data release suffers from catastrophic provenance failures, including pod-lost linkage for 86% of the anchor DESI targets, unrecoverable code and models, and the inclusion of synthetic placeholder data.