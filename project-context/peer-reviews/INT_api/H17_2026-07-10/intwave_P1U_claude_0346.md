# INT Claude-subscription Review — P1U v1U.0.17 — claude-opus-4-8
paper: P1U  version: v1U.0.17  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T10:46:52Z
context-note: confirm wave 2/2 on v1U.0.17; no changes since NJ5 (0-new, AA-bound recompute-verified)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've read the full manuscript structure, the abstract, the Route-1 NJL section, the Fierz lemma and gap-equation appendices, and verified the numbers against the committed artifact `njl_gap_equation_route1_results.json`.

**Verification of the NJ4→NJ5 AA-bound fix (v1U.0.17):**
- `G_scalar/κ = -3/64 = -0.046875` (repulsive) ✓ (JSON line 5)
- Worst scanned `|G_eff|/G_crit = 0.15600` ✓ (JSON verdict, Λ_strong, N_fN_c=9)
- `G_crit = π²/(N_f N_c Λ²)`, symbolic_match: true ✓
- Holst factor `γ²/(γ²+1) = 0.0698` (γ_BI=0.274); EC/Holst ratio 0.042745/0.002985 = **14.3×** ✓
- AA-bound: `G_AA = (-3/16)(-1/2)κ = +3/32κ`, `|G_scalar| = 3/64κ` → exact factor `G_AA/|G_scalar| = 2`; `|G_AA|/G_crit = 2×0.156 = 0.31` ✓ (hand-recomputed; 0.31 < 1 = sub-critical)
- `G_PP = +3/64κ = |G_scalar|` → `|G_PP|=|G_scalar|` ✓

The leg-(B) magnitude bound now genuinely covers the attractive AA/PP channels (the NJ4 gap), not just the PP-only equality. This closes the gap that the NJ4 finding raised.

---

(1) **VERDICT: MINOR REVISIONS**

(2) **ISSUES:**

1. **[MINOR]** App.~njl_gap leg (B), `arxiv/paper1_unified.tex:5133` — leg (B) still reads "the coupling is **far** sub-critical," but the v1U.0.17/NJ5 tempering pass deliberately aligned the abstract (`:1245`, "the coupling is sub-critical") and the main-text mirror (`:2711`, "**comfortably** sub-critical") to drop "far" so the language matches the tempered worst-case (scalar 0.156, only a factor ~6.4 below critical; AA 0.31, only ~3.2× below). The appendix's own verdict (`:5151`) also uses "comfortably." The single surviving "far sub-critical" at :5133 is now internally inconsistent with both the tempered claims and the appendix's own concluding wording — a residual of the same tempering the header comment describes. Purely editorial; change "far" → "comfortably"/"sub-critical" for consistency. Conclusion unaffected.

(3) **Central claim supported:** Yes — the channel-level closure of all four minimal-ECH dark-energy routes, and specifically the R1 vacuum-condensate exclusion (repulsive scalar channel plus sub-critical AA/PP magnitudes, worst scanned 0.156/0.31, Holst-dressed 14× smaller), is fully supported and recompute-verified against the committed script; only the one-word "far"/"comfortably" wording inconsistency remains.

**Wave 2/2 confirmation:** The AA-bound and all NJL numbers recompute-verify against the committed artifact; no changes since NJ5. The single item above is a residual wording nit from the NJ5 tempering pass (an editorial-consistency miss, not new physics) — the substance is 0-genuinely-new and the v1U.0.17 leg-(B) AA-coverage fix holds.
