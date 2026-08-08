# INT API Review — P5 v0.1.138-2026-07-16 — gemini (gemini-3.1-pro-preview)
paper: P5  version: v0.1.138-2026-07-16  model: gemini-3.1-pro-preview
provenance: commit=68d7e2541aa48de03c15133f7aa9f3b8e1cce5ac  pdf=pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf  sha256=3c47ccf75da20653c463557fc54fff50da01e1e6bde43a225f61c46cd50baaf0
packet: key=01bd66f3fff0d483410e960e76603225d72922d899cf69b685ec2423be61d54e  profile=AJ-OBSERVATIONAL
modality: native-PDF (inline_data base64)
UTC: 2026-07-16T08:29:12.032741Z  |  latency: 32.1s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 32.1, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "WpZYapGVLu-sz7IPibbS8AI", "usage": {"candidatesTokenCount": 499, "promptTokenCount": 21425, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 105}, {"modality": "IMAGE", "tokenCount": 21320}], "serviceTier": "standard", "thoughtsTokenCount": 1883, "totalTokenCount": 23807}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**

1. [MAJOR] **Reliance on Unpublished Companion Paper**: The manuscript depends critically on the per-galaxy chirality labels and the global monopole calibration from "Paper IV," which is cited as an in-preparation companion manuscript. While hosting the catalog publicly on HuggingFace and providing Appendix A is highly commendable for transparency, *AJ* standards generally require that load-bearing companion papers be submitted concurrently, accessible to reviewers, or already accepted. The author must clarify the publication status of Paper IV. If Paper IV undergoes structural changes during its own peer review, it could impact the baseline metrics used here.
2. [MINOR] **Manuscript Readability and Artifact IDs**: The author’s commitment to reproducibility is exceptional; however, the narrative flow is frequently disrupted by the inline embedding of artifact IDs, paths, and script names (e.g., "[A10]", "[A43–A44]"). The manuscript currently reads somewhat like software documentation. Consider removing these inline brackets from the main prose and instead linking claims to their reproducibility artifacts via footnotes or relying entirely on the mapping in Appendix D. 
3. [MINOR] **Disproportionate Focus on the Secondary T-Web Analysis**: The author transparently notes that the T-Web tidal-tensor analysis was demoted to a secondary/diagnostic role after review, favoring the DESIVAST catalog for the focal estimate. Despite this, the T-Web methodology and its associated null tests (Sections IV, VI.B–E, VII, and IX) dominate the page count. The author should consider streamlining the T-Web discussion to improve the paper's focus on the primary DESIVAST-anchored results.
4. [MINOR] **Defensive Tone in Unit Conversions**: Footnote 1 provides a lengthy derivation of $D [h^{-1}\text{Mpc}] = D [\text{Mpc}] \times h$. This is mathematically standard and trivial in cosmological literature. The defensive phrasing ("The incorrect divide-by-$h$ operation... is not a valid alternative") is unnecessary and should be condensed to a simple statement of the applied cosmological parameters and unit convention.

**One sentence:** The central claim—that there is no statistically significant, environment-dependent preferred handedness for spiral galaxies in DESI DR1 once catalog-wide classifier systematics are marginalized—is rigorously and convincingly supported by the data.