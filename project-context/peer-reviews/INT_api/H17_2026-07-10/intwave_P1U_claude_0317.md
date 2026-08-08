# INT Claude-subscription Review — P1U v1U.0.17 — claude-opus-4-8
paper: P1U  version: v1U.0.17  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T10:17:57Z
context-note: wave on v1U.0.17: NJL leg-B AA-channel bound added (worst-case 0.31, sub-critical; PP-only coverage overstatement fixed — DP1U-NJ4-01)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've verified the genuinely-new content of this wave (the NJL leg-B AA-channel bound) against the committed artifacts by recomputation. Summary of what I checked:

- **eq:AAdecomp** `(J5·J5) → +¼SS + ½VV − ½AA − ¼PP` — confirmed it is column-A of the machine-derived Fierz matrix in `fierz_lemma_check.py` (textbook Itzykson-Zuber/Nieves-Pal, F²=1 involution). Correct.
- **G_scalar** = (−3/16)(+¼)κ = **−3/64 κ** (repulsive) ✓; **G_AA** = (−3/16)(−½)κ = **+3/32 κ** ✓; **G_PP** = (−3/16)(−¼)κ = **+3/64 κ** ✓ — all match `njl_gap_equation_route1_results.json`.
- **|G_eff|/G_crit** at Λ=M_Pl: (3/64)(N_fN_c)/π² = 4.7e-3 (N_fN_c=1), 4.3e-2 (=9); worst scan 0.156 at Λ_strong=M_Pl/√γ_BI, N_fN_c=9 — recomputed 0.04275/0.274 = 0.156 ✓.
- **AA worst-case** = 2×0.156 = **0.31** ✓ (factor G_AA/|G_scalar| = 2 exact). The PP-only overstatement (`|G_PP|=|G_scalar|`) is now correctly replaced by the explicit AA ×2 statement in both the appendix (L5128-5132) and main-text mirror (L2704-2710); "far sub-critical" → "sub-critical" alignment confirmed in abstract (L1244) and appendix.

The genuinely-new leg-B fix is correct, honest, and fully closes the overstatement. Residual minors below.

---

(1) **VERDICT: MINOR REVISIONS**

(2) ISSUES:

1. **[MINOR]** App `njl_gap`, `arxiv/paper1_unified.tex:5128-5132` (and main-text mirror `:2709-2710`): the AA/PP "magnitude check" divides by the **scalar-channel** critical coupling `G_crit = π²/(N_fN_c Λ²)` derived from the *scalar* gap-equation slope (`eq:gcrit`, L5104). The axial-vector (AA) channel's own criticality (order parameter ⟨ψ̄γ^μγ5ψ⟩, a Lorentz-violating vacuum) has a different loop structure and is not separately derived, so `|G_AA|/G_crit ≈ 0.31` is a proxy, not a like-for-like criticality ratio. This does not threaten the conclusion (the *decisive* leg is the channel-independent scalar sign, and AA/PP are explicitly noted as not the w=−1 object), but a one-line caveat that `G_crit` here is the scalar-channel value used as a rough yardstick would make the belt-and-suspenders check precise.

2. **[MINOR]** `eq:ratio`, `:5137-5147`: the flavor scan tops out at `N_fN_c = 9` ("QCD-like") and reports "worst case 0.156," but the Hehl–Datta torsion contact term couples to *all* fermion species. For realistic SM matter (N_fN_c ≈ 24) the magnitude ratio at Λ_strong is ≈0.156×(24/9) ≈ 0.42 — still sub-critical (crossing 1 needs N_fN_c ≈ 210), so the conclusion is safe, but the headline "worst scanned 0.156" understates the physically-relevant maximum. Either extend the scan to full-SM multiplicity or state that 0.156 is the worst case *within the scanned N_fN_c ≤ 9* and that the sub-critical result is monotone and survives to N_fN_c ≈ 210.

3. **[MINOR]** `:5149-5159` (Verdict) and abstract `:1243-1245`: the vacuum-condensate exclusion is load-bearing on the "standard mean-field NJL framework" assumption (beyond-mean-field strong coupling explicitly out of scope, L5156-5159). This is honestly disclosed and the abstract keeps the "mean-field NJL framework" qualifier — no change required; flagged only to confirm the qualifier must not be dropped in any future abstract tightening, since without it "condensate-excluded" would read as unconditional.

(3) The central claim — the four minimal-ECH dark-energy routes are closed at the channel/amplitude level (R1–R3) and by naturalness (R4), with the Route-1 vacuum condensate now additionally excluded by a repulsive scalar channel plus sub-critical coupling — **is supported under the paper's explicitly stated assumptions** (mean-field NJL, minimal ECH single-species field content, single-scale NDA), and the leg-B AA-channel numbers I recomputed match the committed script/JSON exactly with no fabrication.
