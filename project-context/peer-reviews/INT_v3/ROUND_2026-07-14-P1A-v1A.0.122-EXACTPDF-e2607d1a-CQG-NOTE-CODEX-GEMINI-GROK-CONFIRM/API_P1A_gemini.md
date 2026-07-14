# INT API Review — P1A v1A.0.122 — gemini (gemini-3.1-pro-preview)
paper: P1A  version: v1A.0.122  model: gemini-3.1-pro-preview
provenance: commit=0bb7fddf231f8dfb2778f332e2500d618fb6339e  pdf=arxiv/paper1a_ech_nogo.pdf  sha256=e2607d1a8476aa8df9e5e89b04595655b81048be34cabb4bec273e59c4c87e04
packet: key=3770aa1afdbef47012b9062db257d441502a015274766ec854a31e66020457e9  profile=CQG-NOTE
modality: native-PDF (inline_data base64)
UTC: 2026-07-14T20:37:09.324262Z  |  latency: 31.3s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 31.3, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "9p1WatH0Av7fz7IPoYmhyQ0", "usage": {"candidatesTokenCount": 912, "promptTokenCount": 4498, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 3640}, {"modality": "TEXT", "tokenCount": 858}], "serviceTier": "standard", "thoughtsTokenCount": 2950, "totalTokenCount": 8360}}
PARSED VERDICT: ACCEPT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: ACCEPT

(2) ISSUES:
None.

(3) CENTRAL CLAIM:
The narrow central claim—that minimal Einstein–Cartan–Holst gravity algebraically reduces to a classically equivalent zero-spin branch with a vanishing Holst anomaly, and a spin-sourced branch characterized by a well-normalized axial–axial contact interaction that lacks a nonzero real homogeneous scalar condensate in the standard hard-cutoff mean-field NJL truncation—is technically sound, logically bounded, and fully supported.

(4) CLOSURE CHECK:
1. CLOSED. Page 3 explicitly states the benchmark is "not a constraint on the actual composite expectation" and restricts it to a "coefficient-scale comparison".
2. CLOSED. The abstract and Page 3 precisely declare that $100\text{ cm}^{-3}$ is "deliberately elevated for illustration; it is neither a cosmological-density estimate nor a preferred state."
3. CLOSED. Page 2, Eq. (6) provides the correct algebraic bridge mapping Freidel–Minic–Takeuchi to the text's conventions ($4\pi G = \kappa/2$, $-(3/2)\pi G = -3\kappa/16$).
4. CLOSED. The abstract and text distinguish the coefficient-one benchmark ($\kappa n_\psi^2$) from the $3/16$ factor, finite-Holst factor $\gamma^2/(1+\gamma^2)$, and state-dependent composite.
5. CLOSED. Table I's caption explicitly confirms $\Lambda = M_\text{Pl}$ is "only as a bookkeeping ceiling" and defines $R_A$ as a "coefficient-magnitude benchmark, not a derived axial-vector condensation threshold."
6. CLOSED. Section IV.A cleanly specifies "matched background, initial, and boundary data", defining boundary data as "usual falloff conditions with the boundary contribution to the first-order variation set to zero."
7. CLOSED. Section III.B directly references "the exchange ordering and Grassmann sign fixed in Appendix A" for the Fierz projection.
8. CLOSED. Section IV.E states the limitation precisely as the absence of a "matched physical Lorentzian cosmological stress tensor and observable", avoiding unevidenced speculation on Wick rotation.
9. CLOSED. Page 5 defines TB as "temperature–B-mode" and EB as "E-mode–B-mode" CMB cross-power spectra.
10. CLOSED. Page 7 unequivocally states, "No alternate regulator is evaluated here, so we make no claim about how one would change the stability condition."
11. CLOSED. Old PACS codes are removed from the metadata (Page 1) and reproducibility links reference a specific immutable commit hash (`b587cb7bb8e0`, Page 6).

(5) EXTERNAL GATES:
1. **Alternate-regulator calculation:** Adequately disclosed as unevaluated (Page 7). Blocks broader claims about universal nonperturbative vacuum stability, but does not block the narrow stated mean-field no-go result.
2. **Matched physical Lorentzian cosmological stress tensor/observable:** Adequately disclosed as an unresolved bridge in the literature (Page 4, Page 6). Blocks phenomenological extensions equating Euclidean running with observable dark energy, but does not block the local classical transparency theorem.
3. **State-specific renormalized axial-current expectation value:** Adequately disclosed as unevaluated/undetermined (Page 3). Blocks any genuine equation-of-state or physical vacuum stress prediction, but does not block the dimensional scale benchmark.
4. **Remote resolution of commit-pinned URLs:** Disclosed effectively. Blocks permanent archival validation if external hosts rot, but does not block scientific verification since the core algebraic manipulations are text-complete.
5. **Immutable archive/DOI packaging:** Pending. Blocks official journal publication status, but does not block peer-review validation of the manuscript's physics content.
6. **Actual independent human CQG review/editorial decision:** Acknowledged limitation of this AI review. Blocks final administrative acceptance to the journal.

(6) INSPECTION:
I used simultaneous visual inspection of the provided screenshots and textual analysis of the provided OCR text covering all exactly rendered 7 pages of the provided PDF. No external models, earlier drafts, or inferred materials were substituted.
