# INT API Review — P1A v1A.0.120 — gemini (gemini-3.1-pro-preview)
paper: P1A  version: v1A.0.120  model: gemini-3.1-pro-preview
provenance: commit=438ce8ec  pdf=arxiv/paper1a_ech_nogo.pdf  sha256=6472db7741deebd4100fe3191d5ef23a9b0b7960c4284cf53e9e4761f62f535b
modality: native-PDF (inline_data base64)
UTC: 2026-07-14T18:06:11.459957Z  |  latency: 24.1s  |  attempt: 1
usage: {"promptTokenCount": 4309, "candidatesTokenCount": 374, "totalTokenCount": 6805, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 149}, {"modality": "IMAGE", "tokenCount": 4160}], "thoughtsTokenCount": 2122, "serviceTier": "standard"}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MAJOR] In the Abstract, the phrase "those Route-2/3 identifications therefore remain unresolved" uses terminology ("Route-2/3") that is completely undefined anywhere in the manuscript. This jargon must be removed or explicitly defined, as a CQG Note must be entirely self-contained. 
2. [MINOR] The abstract and Introduction explicitly reference a companion computational paper ("Paper I(b)") involving CAMB, NaMaster, and spectator-ALP fits, while simultaneously stating these pipelines are not inputs to the analytical proofs presented here. To improve focus and readability, these references should be minimized or removed, as they distract from the exact, self-contained analytic results that form the core of this Note.
3. [MINOR] The homogeneous density benchmark $n_\psi = 100 \text{ cm}^{-3}$ in Section III.A is introduced somewhat abruptly. While the text correctly notes that this is artificially elevated compared to the cosmic mean baryon density, adding a brief sentence justifying why this specific arbitrary value was chosen (e.g., as a conservative local overdensity or simple numerical baseline) would clarify the physical context.
4. [MINOR] Table I in Appendix B lists threshold scan values to five decimal places (e.g., $0.23873$ and $7.84158$). This implies a level of precision that is physically meaningless for a rough mean-field NJL magnitude estimate. The author should consider rounding these values to two or three significant digits.

The central claims are robustly supported by standard algebraic torsion elimination, a strict Fierz projection in the mean-field NJL framework, and the exact vanishing of the Holst term on the torsion-free branch via the first algebraic Bianchi identity.