# INT API Review — P4 v1.0.265 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.265  model: gemini-3.1-pro-preview
provenance: commit=e0faf5c1fcf48c67e20e596aaba64f49379255de  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=67a08a4d3255a6fab0eadacd96580491ac20ae77abda50c55847506f49c16fc5
packet: key=729464bef7f84a5540c7459643e7a0102ca02751528871ee191f8f875b8fc75d  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-17T21:54:19.248027Z  |  latency: 47.8s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 47.8, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "naRaatKTBZboz7IPmcqAaQ", "usage": {"candidatesTokenCount": 548, "promptTokenCount": 14671, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 14560}, {"modality": "TEXT", "tokenCount": 111}], "serviceTier": "standard", "thoughtsTokenCount": 2026, "totalTokenCount": 17245}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MINOR] Section 4 / Main Text Flow: The manuscript embeds numerous SHA-256 hashes, HuggingFace commit IDs, and JSON artifact filenames directly into the prose of the main text (e.g., Sections 4.1, 4.3, 4.5). While this level of strict provenance and computational closure is outstanding for an ApJS methods/catalog paper, it severely impedes readability. Suggest moving the explicit hash strings and filenames to footnotes, a dedicated Data/Software appendix table, or the Data Availability section, allowing the main text to focus on the astrophysical and statistical narrative.
2. [MINOR] Section 6.2 / Physical Transfer Function: The careful distinction between the rigorous "observed-label limit" (0.98%) and the open "physical parity-amplitude bound" is methodologically correct. However, it leaves the reader without an order-of-magnitude sense of the true physical constraint. The author provides an illustrative dilution factor $g=0.398$; the text would benefit from a brief expanded discussion estimating how much realistic unmodeled imaging systematics (spatially varying PSF, depth, seeing) might reasonably degrade this physical bound (e.g., by a factor of 2? 5?) to contextualize the scientific limit.
3. [MINOR] Figures 7 & 9 / Formatting: Figure 7 contains a massive caption that functions as main text methodology. Please move the detailed procedural descriptions and pipeline artifact references to the relevant main text sections (e.g., Section 4) and keep the caption focused on the visual takeaway. In Figure 9, the plot contains colloquial text/arrows ("$z \simeq -7.6$") embedded in the data area; please formalize the plot aesthetics to match standard ApJS publication quality.
4. [MINOR] Section 3.1 & Table 5: The variable $z_{mom}$ is explicitly defined as a moment-ratio $(x - \langle x \rangle_{null})/\sigma_{null}$ on line 150, but its presentation directly alongside $p$-values frequently risks reader confusion (as $z$ universally implies a Gaussian standard score). Please add a brief reminder in the Table 5 and Table 6 captions that $z_{mom}$ does not map to the empirical rank $p$ via a standard normal distribution.

The central claim that the observed galaxy chirality dipole is consistent with zero, and that previously reported signals are artifacts mitigated by equivariant test-time averaging and footprint-systematic controls, is rigorously supported by exceptional methodological auditing.