# INT Claude-subscription Review — P1U v1U.0.20 — claude-opus-4-8
paper: P1U  version: v1U.0.20  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-13T12:39:40Z
context-note: M28

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've read the full manuscript, verified the load-bearing numbers against the committed artifacts (NJL script/JSON, figure generator), and checked the core derivations. Here is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

The science is sound and every load-bearing number I independently recomputed checks out (NJL density estimate ρ_NJL ≈ 4×10⁻⁸¹ eV⁴ ≈ 1.4×10⁻⁷⁰ ρ_Λ; Fierz couplings G_scalar=−3/64 κ, G_AA=+3/32 κ, G_PP=+3/64 κ, |G_AA|/|G_scalar|=2; worst-case |G_eff|/G_crit=0.156; MCMC sample bookkeeping 176,240+132,949=309,189, ×0.70=216,432; the perturbation-transparency proof is a correct standard Bianchi-identity argument). The remaining items are presentation and bookkeeping, not correctness — hence MINOR, though a stricter PRD referee could plausibly return MAJOR on length/repetition alone.

**(2) ISSUES**

1. **[MAJOR] Over-hedging and length materially impede evaluation.** The "channel-level, not operator-level" caveat and scope disclaimers are restated at least five times: abstract (L1273–1274), intro scope paragraph (L1317–1345), the boxed "does and does not establish" figure (L1347–1382), the §IV Scope paragraph (L2395–2436), and the completeness paragraph (L2438–2490). At 6898 lines with ~10 appendices (MCMC, NaMaster, ALP, Fierz, NJL, dimensional), the manuscript reads as defensive rather than authoritative. The v1U.0.19 pass helped but did not resolve it; further consolidation (one canonical scope statement + cross-refs) is needed for a PRD-length article.

2. **[MINOR] Physical justification of the exp[−3 N_tot] dilution is thin.** Sec. II (L2172, L2177) matches ρ_Λ ≈ (2.3 meV)⁴ by diluting a Planck-scale density as exp[−3 N_tot] — i.e. like non-relativistic (w=0) matter, not like the w=−1 vacuum component it is meant to become. It is honestly flagged as a fitted, non-load-bearing reparameterization, but one explicit sentence justifying why the eventual ρ_Λ inherits a w=0 dilution law (rather than staying constant) would close an obvious referee question.

3. **[MINOR] Reproduce the 10⁻¹²² convention.** D_inf ≈ 4×10⁻¹²² (L1744) versus the direct ρ_Λ/M_Pl⁴ with unreduced M_Pl≈1.22×10²⁸ eV gives ≈1.3×10⁻¹²³ — a factor ~30 that presumably reflects reduced-vs-unreduced M_Pl or the ρ_Λ definition. State the convention inline so the number is reproducible from the paper alone.

4. **[MINOR] Changelog/version hygiene gap.** `\paperVersion` is `v1U.0.20` (L54) but the header changelog block's most recent entry is `v1U.0.19` (L56); there is no v1U.0.20 entry documenting what changed (directive-G hygiene). Add the entry or confirm it is a bare restamp.

5. **[MINOR] Cited "self-verifying" script has a mislabeled verdict string.** The appendix text (L5042–5044) correctly attributes the worst case 0.156 to Λ_strong=M_Pl/√γ_BI, but the committed artifact `arxiv/scripts/njl_gap_equation_route1.py` (verdict string ~line 249) states that worst case is "at Lambda=M_Pl" and comment [6] (~L233) asserts the ratio *shrinks* at Λ_strong — contradicting its own JSON (0.156 occurs at Λ_strong, not M_Pl). Numerics and paper are correct; fix the script comment/string since the artifact is cited as machine-checked.

6. **[MINOR] Title is unusually long and defensive** (L1248–1251): the double parenthetical plus "Under Stated Assumptions" reads as a hedge chain; a sharper title would serve the (genuinely correct) core results better.

**(3)** Yes — the central claims (the perturbation-transparency theorem and the channel-level amplitude closure of the four enumerated minimal-ECH routes under explicitly stated assumptions) are supported by correct derivations whose load-bearing numbers I recomputed and confirmed against the committed scripts.
