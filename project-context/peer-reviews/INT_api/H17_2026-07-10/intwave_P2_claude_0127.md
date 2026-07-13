# INT Claude-subscription Review — P2 v1.7.116 — claude-opus-4-8
paper: P2  version: v1.7.116  tex: research/focused_paper_source_integration/02_full_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-13T08:27:14Z
context-note: M19

======================================================================
RAW RESPONSE (verbatim):
======================================================================

All load-bearing numbers verify. Summary of my verification:

- **c15 channel-native Fisher** (`outputs/c15_channel_native_fisher.json`): bounce-template ρ(f_NL,A_GR) = −0.425 (2×2) / −0.494 (3×3), σ_marg(b_φ 30%) = 0.9417 → 2.32σ, α = 0.9916, cosine 0.9998, proxy floor 1.30σ — **all match the text**.
- **Vertex certification** (`scripts/p2_vertex_check.py`): code faithfully implements Table tab:vertices row-for-row; per-vertex squeezed sum −25/16 − 5/32 + 0 − 15/32 = **−35/16** ✓; equilateral −35/32 − 5/32 − 5/8 − 15/128 = **−255/128** ✓; ε-order group −5/2 + 5/16 + 0 = −35/16 ✓; Li −165/16 + 65/8 = −35/16 at c_s=1 ✓.
- **Significance/Bayes arithmetic** (hand-checked): 2.1875·0.84/0.7 = 2.63σ ✓; ·0.876 = 2.74σ ✓; /√(0.7²+1²) = 1.5σ ✓; 0.7/√(1−0.868²) = 1.41 → 1.30σ ✓; dualnorm 5.25σ = 2× ✓; 30/(√2π·0.7) = 17.1 ✓; exp[(35/16)²/(2·0.7²)] = 132 ≈ 1.4×10² ✓; σ_GR=1.0 → 5.0 ✓; −305/64 = −35/16 − (10/3)(99/128) ✓.

No fabrication or arithmetic error found. My review:

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MAJOR] Scope/novelty for PRD (whole paper; abstract L975, Scope L984, Caveats(i) L1512).** The paper's deliverable is two things, both honestly labeled: a literature-error correction of the matter-bounce amplitude (−35/8 → −35/16), and a sensitivity *recast* of a single external forecast (Heinrich et al., σ=0.7) whose per-triangle covariance is not public. The resulting headline is a sub-3σ, ~1.3–2.75σ forecast that "cannot discriminate" at any decisive level. The correction is a genuine, citable contribution and the recast is validated by the in-house c13/c15 Fisher — but the editor needs a sharper, up-front statement of *what is new and why it clears PRD's significance bar*, given that the central number rides on one un-released external covariance. Not an error; a venue-fit judgment that must be made explicit.

2. **[MAJOR] Excessive length and pervasive redundancy (throughout).** Despite the v1.7.116 consolidation, the same four caveats — "recast, not independent," the proxy-based ρ=−0.868 floor, the r=0.84 vs r_eff=0.99 reconciliation, and "additive-quadrature is a heuristic, not a joint covariance" — are each restated 4–6 times (e.g. proxy floor at L975, L984, L1332, L1409, L1434, L1512). The prose reads defensively, like an accumulated rebuttal record rather than a primary manuscript. This needs substantial cutting; each load-bearing caveat should appear once at its canonical home with cross-references only (the paper already claims this structure but does not achieve it).

3. **[MINOR] "Resolution" framing slightly overreaches what is shown (§title L1541; admission L1556).** The section claims to *resolve* the Cai–Li factor of two by identifying an arithmetic error, yet the paper explicitly "do[es] not claim a complete term-by-term reconstruction of Cai's published −35/8": the transcribed printed polynomial reduces to a *third* value (−305/64), not −35/8. The re-summation robustly certifies −35/16; but a reader is left with three numbers and no reproduction of the −35/8 the "error" supposedly produced. Retitle to reflect that −35/16 is *certified* (and matches Li), while −35/8 is *unreproduced*, rather than that the specific error is fully diagnosed.

4. **[MINOR] Disconnected auxiliary appendix (app:birefringence, L1712).** The cosmic-birefringence appendix is, by the paper's own repeated statement, independent of every result. Relegating it to an appendix rather than removing it reads as scope-padding; recommend deletion (or a one-line outlook sentence with no appendix).

5. **[MINOR] Citation-year inconsistency for the load-bearing reference.** The Heinrich forecast — the single source the entire recast rests on — is keyed `\cite{Heinrich:2023}` (L984 et seq.) but referred to in prose as "Heinrich et al. 2024" (e.g. L1224, L1459). Reconcile the bib entry year with the prose so the paper's most-cited external anchor is unambiguous.

6. **[MINOR] Abstract is a single ~330-word hedge-dense paragraph (L975).** It should state the corrected value, the headline significance and its dominant uncertainty crisply; several of the nested proxy/edge disclosures belong in the body, not the abstract.

**(3)** Yes — the central claim (matter-bounce f_NL = −35/16, certified four independent ways, and a validated SPHEREx sensitivity recast of ~1.3–2.75σ) is supported: every load-bearing number reproduces from the committed vertex-certification code and the c15 Fisher JSON, and the limitations are disclosed honestly; the required revisions are editorial (scope framing, length, minor consistency), not corrections to the science.
