# Referee Handoff — P2 (Matter-Bounce f_NL + SPHEREx Sensitivity Recast)

`research/focused_paper_source_integration/02_full_draft.tex` · slug `paper-2` · **current version: v1.7.98 (2026-07-06)**

## Headline result

The matter-bounce local non-Gaussianity is **f_NL = −35/16 = −2.1875**. P2's
central original contribution is to **resolve** the long-standing Cai et al. 2009
(−35/8, arXiv:0903.0631) vs Li et al. 2017 (−35/16, arXiv:1612.02036) factor-of-2
discrepancy in favor of −35/16, by re-summing Cai et al.'s own four cubic-action
vertices at ε=3/2 (exact symbolic computation) and tracing the printed −35/8 to a
spurious local-shaped +(99/128)Σk_i³ term in their final polynomial (their Eq. 37).
Li et al.'s independent general-c_s derivation gives −35/16 at c_s=1, corroborating
the correction. The vertex-by-vertex certification is in **Appendix A**.

**Certification scripts are now committed** at
`research/focused_paper_source_integration/scripts/caili_certification/`
(vertex extraction, exact vertex sum + squeezed/equilateral limits, the +(99/128)Σk³
discrepancy, and the Li c_s=1 cross-check; see the directory README). A smoke-run
reproduces −35/16 (squeezed), −255/128 (equilateral), and the +(99/128)Σk³ residual.
The arXiv source tarballs of the two cited papers are fetched at run time (not
redistributed).

Secondary contribution: a SPHEREx/MegaMapper sensitivity **recast** onto this
prediction — an honest **conditional ~1.3–2.75σ envelope** plus illustrative Bayes
factors ~9–14.

## Convergence status

P2 has reached the LLM-refereeing floor: **0 genuinely-new real findings** across the
FINAL (2026-07-05) and POSTPOLISH (2026-07-06) truth-audited EXT+API rounds
(`project-context/peer-reviews/FINAL_SIGNOFF_AUDIT_2026-07-05.md`). On the identical
v1.7.98 PDF: **Grok MINOR / Gemini MINOR** ("publish with minor polish"); **ChatGPT
REJECT and openai gpt-5.5 REJECT** — the maximally-harsh-referee structural floor
(directive H), consistent across every paper in the program. No reviewer identified a
correctness defect that survives truth-audit.

## Recurring objections a human referee should adjudicate

1. **The Cai–Li factor-of-2 resolution — the sole substantive technical residue.**
   - Status: **resolved by our computation to −35/16** (vertex-certified, Appendix A;
     scripts committed). ChatGPT + openai independently RE-RAISE it at every round,
     arguing the +(99/128)Σk³ term "alone has the wrong sign/magnitude to explain the
     doubling." The paper's v1.7.95 changelog already reconciled that point: adding
     +(99/128)Σk³ *alone* gives the wrong sign (+2.58) — the correct statement is that
     Cai's final printed polynomial *differs from the vertex sum by* +(99/128)Σk³, and
     it is the vertex sum (not the mis-extracted polynomial) that gives −35/16. Grok +
     Gemini (EXT) rate P2 MINOR and call the resolution "fully supported" / "settles the
     arithmetic error definitively."
   - Honest framing: this is dispositioned as "resolved by our from-scratch vertex
     re-summation, re-corroborated as *disputed* by the harshest referees, handed off to
     a human expert." It is an honest but **live** disagreement, not "resolved and
     everyone agrees."
   - Judgment call: **is the vertex-level re-derivation in Appendix A sufficient to
     publicly assert the correction of Cai et al.'s printed −35/8, and is the
     presentation appropriately respectful of the original work?** (Cai is a coauthor on
     both the 2009 and correcting-2017 papers.)

2. **Single-source (Heinrich recast) vs independent forecast.**
   - Concern: every SPHEREx significance rescales one external Heinrich et al. 2023
     Fisher σ≈0.7 through a computed shape-overlap; it is not an independent
     bispectrum Fisher.
   - Disclosed: abstract *Scope* sentence + signpost (i) state "no independent
     bispectrum Fisher is constructed here." The one remaining external input — the
     Heinrich per-triangle bispectrum covariance Cov_B — is explicitly named and
     documented as not publicly available (`DATA_UNLOCK_2026-07-05.md`).
   - Judgment call: **is a clearly-labeled single-source sensitivity recast publishable
     as-is, or does PRD want an independent bounce-fiducial multi-tracer Fisher re-run
     before the significance envelope can appear as a headline?**

3. **Cubic-order bispectrum transmission through the bounce.**
   - Concern: f_NL = −35/16 assumes faithful cubic-order transfer through the bounce.
   - Now **derived to a bounded systematic** (transmission = 1 ± O((kη_B)²) ≈ 1 ± 1e-4)
     via single-clock degree-of-freedom counting + nonlinear superhorizon ζ-conservation
     on the single-clock LQC background (signpost (ii)). Grok EXT: "one of the strongest
     technical sections … upgrades this from a scaling estimate to a derived bounded
     systematic." ChatGPT calls it not-demonstrated.
   - Judgment call: **is the single-clock ζ-conservation derivation solid, or is it the
     weakest technical link?**

4. **Additive-quadrature systematic budget.**
   - Concern: systematics combined heuristically in quadrature (σ_eff = √(σ_base² + Σσ_i²)),
     not via a joint multi-tracer nuisance Fisher.
   - Disclosed: §VII up-front heuristic banner + signpost (v); the budget is presented as
     a **computed-degeneracy bracket**, and a joint SDB Fisher cross-check bounds the
     heuristic's direction. Gemini rates this MINOR.
   - Judgment call: **heuristic budget with a cross-check — acceptable for a recast, or
     must it be replaced by a full joint covariance?**

## What is NOT in question

No genuinely-new correctness defect remains. The −35/16 resolution is vertex-certified
with committed reproducing scripts. A ChatGPT claim that the paper quotes "BF ≈ 10⁸/>10⁵"
was **FALSIFIED against source** — the paper quotes BF ≈ 9–14 (and labels them
illustrative, not definitive model-selection evidence); the only "10⁵" in P2 is a
Monte-Carlo realization count. The fig1–fig5 PNG legends that previously carried a baked-in
−35/8 were regenerated to −35/16 at v1.7.97 (a cosmetic label-sync of already-corrected
headline numbers; captions already reconciled the values).

## Recommended venue / next step

Submit to **PRD** as an explicitly-scoped sensitivity recast, with the single-source
Heinrich recast and the Cai–Li factor-of-2 flagged to the editor. Recommended collegial
step before/at submission: **email Cai (and Li/Quintin)** the vertex re-summation +
+(99/128)Σk³ trace, asking them to confirm or refute — this de-risks the single
highest-stakes claim in the program at the cost of one email.
