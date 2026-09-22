# P2 R-CONFIRM-2026-09-22 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `research/focused_paper_source_integration/02_full_draft.pdf` sha256=d3afe79fe70ce13cee5ec8149e84c4b42c78224ca6a90569058ec501222f5c2f pages=12
**Review packet(s)**: `e5d8c38a5b2aeb63d0c17441d3565ed2aad8e357c83f25ea232f32f4bcfb0409, 9855179ad492425310bfadf9939d048952cd246bbc61fc9ce8393bd61e0f2333`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 109.5s

---

**Referee Report for P2 (PRD Research Article)**

**P2-E1 (ESSENTIAL)** — Abstract (p.1) and Sec. I (p.1): The abstract states “Its flat-grid amplitude recovery is r = 0.8354 … the corresponding mapping map … is 2.63σ before additional nuisance marginalization. A channel-native surrogate-covariance check spans 3.5σ … 3.1σ … 2.3σ … and 0.4σ”. These headline σ values are presented without the explicit qualifier that appears only later in the body (Sec. IV, p.4–5 and Sec. VII, p.6): “illustrative conditional diagnostics, not an observational headline”. The abstract therefore over-claims a detection-level result. Required fix: either remove all numerical σ claims from the abstract or prepend the identical “illustrative … not an observational headline” sentence that appears in the body.

**P2-E2 (ESSENTIAL)** — Abstract (p.1) and title page (p.1): The manuscript is dated “July 24, 2026, 18:35 PDT” and carries the internal tag “v1.7.130”. A submission to PRD cannot carry a future calendar date or a version string that belongs to an internal Git/Zenodo log. Required fix: replace with the actual submission date and remove the version tag from the title page.

**P2-E3 (ESSENTIAL)** — Sec. VIII (p.6) and Appendix (p.7–8): The paper contains an “AI USAGE DISCLOSURE” section and repeated provenance language (“R-CONFIRM-2026-09-22”, “v1.7.125”, “scripts/p2_vertex_check.py”, “research/cubic_bounce_transmission/g1_dressedmetric_ic.close.json”). These are internal review artifacts, not part of a PRD research article. Required fix: delete the entire disclosure section and all script/version strings from the body and appendices.

**P2-E4 (ESSENTIAL)** — Abstract (p.1) vs. Sec. IV B (p.4) and Table III (p.6): The abstract quotes a single “2.63σ” number obtained with the adopted r = 0.84 convention. The body shows that the exact-shape recovery is r = 0.83542294 and that the 2.63σ figure is produced only after the ad-hoc rounding 0.8354 → 0.84. No propagation of the 0.0046 difference into the Fisher matrix is shown. The quoted significance is therefore not reproducible from the displayed numbers. Required fix: recompute and report the exact r = 0.8354 significance (or remove the rounded value).

**P2-M1 (MAJOR)** — Sec. II–III (pp.2–5): The paper is 12 pages long. The sole rigorous, self-contained result is the four-vertex algebraic identity that yields f_NL = −35/16 (Eq. (3)–(4) and Appendix B). All SPHEREx forecasts, channel-native ladders, redshift-space extensions, and torsion estimates are explicitly labeled “illustrative” and rest on unverified assumptions (d)–(f) of Sec. II C. The manuscript therefore violates PRD’s length guideline for a narrow algebraic correction. Required fix: reduce to a 4–5 page Letter focused on the vertex sum; move all conditional LSS mappings to a separate, fully justified forecast paper.

**P2-M2 (MAJOR)** — Sec. II C (p.3) and Eq. (5): The torsion correction bound |δf_NL^tor| ≲ 0.022–0.21 is derived under the explicit assumption that n_ψ,c is “not fixed by any committed artifact”. No numerical integration of the four-fermion operator with the actual bounce mode functions is supplied; the inequality is therefore an uncomputed claim. Required fix: either perform the integral or replace the inequality with a clear statement that the coefficient remains uncalculated.

**P2-M3 (MAJOR)** — Fig. 1 (p.2) and Table I (p.2): The plotted curve and the three tabulated B_NL values are stated to come from the exact vertex sum, yet the caption and table do not display the intermediate K_9 polynomial evaluated at the three benchmark triangles. A reader cannot verify the plotted numbers without the companion script. Required fix: add the explicit numerical evaluation of Eq. (3) at the three configurations.

**P2-N1 (MINOR)** — Sec. I (p.1): The sentence “the result corrects the unreproduced printed −35/8 literature value” appears before any derivation. The claim is repeated in the abstract. While factually correct after Appendix B, the placement constitutes forward-referencing. Required fix: move the statement to after Eq. (4).

**P2-N2 (MINOR)** — Bibliography (pp.11–12): Ref. [7] is cited as “arXiv:0903.0631v2” with retrieval date “July 14, 2026”. The date is again in the future and the version string is unnecessary. Required fix: standardize to the published JCAP reference without internal retrieval metadata.

**P2-N3 (NIT)** — Multiple locations: The phrase “the exact matter-bounce amplitude derivation” is used repeatedly as a section heading and in the abstract. It is slightly redundant (“exact derivation”). Cosmetic only.

**Summary recommendation: REJECT**

The manuscript’s sole rigorous contribution—an algebraic re-summation of four cubic vertices that replaces the historically printed −35/8 with −35/16—is a narrow correction that belongs in a 3–4 page erratum or short note, not a 12-page PRD article. The remainder of the text consists of explicitly labeled “illustrative” forecasts whose numerical significances are presented in the abstract without the body’s essential caveats, while the manuscript itself is riddled with internal versioning tags, future dates, and an AI-usage disclosure section that have no place in a journal submission. Until the paper is stripped to its algebraic core and the abstract is rewritten to match the body’s calibrated language, it does not meet PRD’s acceptance bar.