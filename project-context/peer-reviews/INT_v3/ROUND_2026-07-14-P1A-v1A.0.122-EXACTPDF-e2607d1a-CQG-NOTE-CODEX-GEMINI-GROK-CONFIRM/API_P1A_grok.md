# INT API Review — P1A v1A.0.122 — grok (grok-4.3)
paper: P1A  version: v1A.0.122  model: grok-4.3
provenance: commit=0bb7fddf231f8dfb2778f332e2500d618fb6339e  pdf=arxiv/paper1a_ech_nogo.pdf  sha256=e2607d1a8476aa8df9e5e89b04595655b81048be34cabb4bec273e59c4c87e04
packet: key=4a524fea329a0876445de2742fd098471d3b1ef40f9344a6f0ced30920e12a34  profile=CQG-NOTE
modality: native-PDF (/v1/files file_id)
UTC: 2026-07-14T20:37:08.643290Z  |  latency: 13.5s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 13.5, "modality": "native-PDF (/v1/files file_id)", "provider": "xai", "provider_reported_cost": "unavailable", "request_id": "6833e91e-7fca-9970-a789-b2ee69dd5298", "requested_model": "grok-4.3", "resolved_model": "grok-4.3", "response_id": "6833e91e-7fca-9970-a789-b2ee69dd5298", "usage": {"context_details": {"input_tokens": 13760, "output_tokens": 1418}, "cost_in_usd_ticks": 205409000, "input_tokens": 13760, "input_tokens_details": {"cached_tokens": 192}, "num_server_side_tools_used": 0, "num_sources_used": 0, "output_tokens": 1417, "output_tokens_details": {"reasoning_tokens": 766}, "total_tokens": 15177}}
PARSED VERDICT: ACCEPT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: ACCEPT
(2) ISSUES: None.
(3) CENTRAL CLAIM: The narrow central claim—that algebraic elimination of the nondynamical connection in minimal ECH yields the sourced axial–axial contact coefficient −(3κ/16)[γ²/(1+γ²)]J₅² on the spin branch while the zero-spin scalar branch reduces exactly to the Einstein–scalar theory—is supported.
(4) CLOSURE CHECK:
1. CLOSED (explicitly labeled “coefficient-one dimensional benchmark” and “not a constraint” on pp. 1, 3);
2. CLOSED (explicitly “deliberately elevated for illustration; it is neither a cosmological-density estimate nor a preferred state” on p. 3);
3. CLOSED (Eq. (6) on p. 2 supplies the exact bridge 4πG=κ/2 and −(3/2)πG=−3κ/16 linking to the cited conventions);
4. CLOSED (κn², 3/16 factor, finite-Holst factor, and state-dependent ⟨J₅J₅⟩ kept conceptually separate on pp. 1, 3);
5. CLOSED (Λ=M_Pl called “bookkeeping ceiling only” and R_A labeled “coefficient-magnitude benchmark, not a derived axial condensation threshold” on p. 7);
6. CLOSED (matched background/initial/boundary data, “usual falloff,” and vanishing first-order surface term specified on p. 4);
7. CLOSED (main-text NJL check on p. 3 explicitly points to “exchange ordering and Grassmann sign fixed in Appendix A”);
8. CLOSED (limitation stated narrowly as “missing matched physical Lorentzian cosmological stress tensor and observable” on pp. 3, 5, without inventing a Wick-rotation defect);
9. CLOSED (TB/EB expanded as “temperature–B-mode (TB) and E-mode–B-mode (EB) CMB cross-power spectra” on p. 4);
10. CLOSED (explicit statement “No alternate regulator is evaluated here, so we make no claim” on p. 7);
11. CLOSED (no PACS; reproducibility links pinned to immutable commit b587cb7bb8e0 on p. 6).
(5) EXTERNAL GATES:
- alternate-regulator calculation: disclosed as open; blocks any stability claim beyond the stated NJL truncation;
- matched physical Lorentzian cosmological stress tensor/observable for the cited Euclidean running: disclosed as open; blocks any dark-energy or birefringence claim;
- state-specific renormalized axial-current expectation value: disclosed as open; blocks any equation-of-state or vacuum-stress inference;
- remote resolution of commit-pinned reproducibility URLs: disclosed as open; blocks only release/journal status;
- immutable archive/DOI packaging: disclosed as open; blocks only release/journal status;
- actual independent human CQG review/editorial decision: disclosed as open; blocks only release/journal status.
(6) INSPECTION: Full text of the exact seven-page PDF supplied in the query (pages 1–7 inclusive) was read directly; no model-access limitation.