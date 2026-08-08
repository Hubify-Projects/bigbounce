# INT Claude-subscription Review — P4 v1.0.237 — claude-opus-4-8
paper: P4  version: v1.0.237  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T16:21:50Z
context-note: directive-M presentation overhaul answering the recurring ChatGPT/OpenAI 'excessively long, repetitive, internally self-justifying' MINOR + PRD single-paragraph abstract ask (DP4-13). Abstract collapsed from 5 dense paragraphs (~430w) to ONE ~230-word PRD paragraph, byte-preserving every number/claim (detail relocated to Sec.notation / Sec.monopole_mask_null / Appendix B/D which already carry it). De-duplicated the 'sigma values not directly comparable' caveat: removed 4 redundant per-figure parentheticals + trimmed 2 table captions to one statement each, cross-ref'd to canonical Sec.notation. ZERO content/number change.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have verified all load-bearing numbers against the committed artifacts by recomputation. Here is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

The science is sound and every headline number I checked reproduces exactly from the committed artifacts. The remaining issues are presentation-level — including a partial-only closure of the very concern this revision targeted.

**Verification performed (all pass):**
- Catalog counts 1,592,107 CW + 1,609,053 CCW = 3,201,160 spirals; total 8,474,688−157 = 8,474,531 (`catalog_c_post_tta_dipole_summary.json`, `class_pie`). ✓
- Primary dipole +0.41σ, rank-p=0.31, ampl 4.4×10⁻³, (l,b)=(293°,12°), 2-sided 0.62 (`catalog_c_post_tta_dipole_summary.json`). ✓
- Monopole-mask leakage 99.32% (0.016846/0.016961), residual +1.69σ, hemisphere +4.42σ (`monopole_mask_null_results.json`). ✓
- GZ1 human-only null z=−0.54 (rank-p 0.666), N=46,017, CW-frac 0.4836, ampl 0.0546 (`gz1only_fullN_dipole_result.json`). ✓
- Injection recovery P(σ>3)=0.59/0.91/1.0 at 0.75/1.0/1.5%; A₅₀≈0.75%, A₉₅ log-interp 1.20%; full-sample A₅₀≈0.36%/A₉₅≈0.63%; canonical z=+7.93 (`c16_r24conf_pod_batch.json`). ✓
- WLS best-fit 0.455% A_p, σ_boot=1.63×10⁻³, A_ref=0.017, z=−7.64 (`joint_nuisance_bootstrap_sigma.json`). ✓ — the previously-contested factor-of-2 is now correctly resolved and consistently propagated (abstract + Sec. notation + Sec. IV.D + conclusions all use A_ref=0.017 → z≈−7.6; the artifact explicitly documents the superseded doubled z≈−18).

**(2) ISSUES:**

1. **[MINOR]** *Redundancy — the DP4-13 target — is only partially closed.* The overhaul correctly collapsed the abstract and trimmed 4 figure captions, but the body still carries ~30 restatements of the "not directly comparable / not a frequentist exclusion / systematics-attributed" caveat family (`chirality_catalog_paper.tex:706,733,757,828,831,962,990,…`). The worst offender is the Sec. IV.D forward-model paragraph (`chirality_catalog_paper.tex:1032`), which states the a-fortiori "entire ℓ=1 residual < A₅₀ < A₉₅, so it does not affect the exclusion" argument ~4 times in a single paragraph. Recommend applying the same canonical-statement-plus-cross-reference treatment used for the abstract to Sec. IV.D and the two table captions (`tab:decision_tree` L733, `tab:headline_summary` L757), which restate the caveat already given in Sec. notation (L706).

2. **[MINOR]** *Abstract density.* The single-paragraph abstract (`chirality_catalog_paper.tex:637`) is PRD-compliant and byte-preserves every number, but at ~230 words with deeply nested semicolon/parenthetical clauses (e.g. the mid-sentence Shamir "maps to our A_p=2(f_CW−½) without rescaling" aside) it is hard to parse in one pass — arguably still "self-justifying" in tone. Consider two clean lead sentences (result, then method) before the caveat cascade.

3. **[MINOR]** *WLS bootstrap mask vs. stated canonical mask.* The text states the block-bootstrap WLS fit operates on "the canonical-mask A_p field" (N_spiral≥10, f_sky=0.49005; `chirality_catalog_paper.tex:716,763`), but the committed artifact `joint_nuisance_bootstrap_sigma.json` uses a `(|b_gal|>15°)&(n_total>0)` galactic-latitude mask (440 super-pixels). The artifact self-documents that both masks agree to 4 sig figs (A_dip 4.55×10⁻³, z≈−7.6), so the result is unaffected — but a one-line footnote acknowledging the two mask definitions would forestall a reproducibility flag from any referee who opens the artifact.

**(3)** Yes — the central claim (a chirality dipole consistent with null at sub-percent sensitivity, with the two primary estimators returning +0.41σ and z≈−7.6 and every quoted number reproducing from committed artifacts) is fully supported.
