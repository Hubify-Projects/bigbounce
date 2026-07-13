# M34-EXT truth-audit — P2 (v1.7.116, byte-unchanged)

**Raws READ verbatim before any verdict:** `P2_grok_M34.md` (MINOR REVISIONS, 1 MAJ-tagged/4 MIN),
`P2_chatgpt_M34.md` (REJECT, 10 MAJ/1 MIN). Verdict lines literal in each raw.

**Provenance:** Both raws review the f_NL SPHEREx-forecast paper (−35/16 squeezed vertex sum, r=0.84
template overlap, Heinrich covariance, Bayes factor, δf_NL≲10⁻³ transmission) → correct paper. ✓

## Grok (MINOR, 1 MAJ-tagged/4 MIN) — ledger_match 5/6; #1 header non-finding
Lone [MAJOR]-tag sits under a MINOR-REVISIONS header = in-MINOR emphasis, not reject-tier. Closing
CREDITS the central claim ("robustly supported … once the proxy nature of the lowest edge is caveated").
- [MAJOR-tag] conservative 1.3σ floor uses proxy ρ=−0.868 vs channel-native surrogate ρ≈−0.42/~2.3σ;
  elevate proxy-floor to a numbered limitation → **DP2-33** (proxy-vs-channel-native; channel-native bug
  fixed v1.7.115 DP2-CN1-01, σ_marg=0.94→2.32σ; both labeled marginal-sensitivity estimates).
- [MINOR] six-coefficient null-space underdetermined, r=0.85±0.13 broad vs 0.84±0.02 headline → **DP2-15**
  (amplitude-invariant null-space stress band; ref vector present, never enters σ_eff).
- [MINOR] cubic transmission δf_NL≲10⁻³ rests on single-clock ζ-conservation + gradient estimate → **DP2-13**
  (Wilson-Ewing scope, six-assumptions caveated).
- [MINOR] 1.3–2.75σ envelope mixes heterogeneous null procedures → **DP2-04** (disclosed non-comparable
  endpoints; abstract note present).
- [MINOR] BF≈9–14 prior-choice dependent (drops to ~4 for [−5,+5]) → **DP2-14** (prior-sensitivity disclosed).
**0 genuinely-new.** Grok MINOR↔MAJOR band across M15/M25/M28/M31 = documented pattern-066; every closing
AFFIRMS −35/16.

## ChatGPT (REJECT, 10 MAJ/1 MIN) — ledger_match 9/10; #10 UNMATCHED Opus-adjudicated
CRUX #1 (numerical analysis "doesn't use the appendix bispectrum"; proposes distinct-monomial coeffs
(3,1,−9,5,−33,9); "internal contradiction invalidates conclusions") = **NON-REAL re-flag of DP2-01/-15/-16/-25**,
already FALSIFIED in M31 by re-running the committed `p2_vertex_check.py`: the paper's 6-perms convention
yields squeezed −35/16 (= Li c_s=1, convention-FREE) + equilateral −255/128 (= Table I benchmark);
ChatGPT's proposed convention yields −285/128 / −65/32 which CONTRADICTS both independent cross-checks.
ChatGPT's own raw concedes "−35/16 may nevertheless be correct—particularly because Li et al.'s independent
formula gives it at c_s=1." Headline UNAFFECTED under any Li-consistent convention.
- #2 four-way-certification time-ordering incoherence → **DP2-01/-16** (quadruple-certified; ChatGPT concedes −35/16 favored).
- #3 δf_NL≲10⁻³ not derived (Wilson-Ewing) → **DP2-13/-19** (scope caveated, assumption disclosed).
- #4 r=0.84 not the SPHEREx estimator response (α=…) → **DP2-14/-34** (surrogate r_eff≈0.99 disclosed; 0.84 labeled conservative).
- #5 in-house Fisher tree-level / doesn't validate imported forecast → **DP2-22** (channel-native surrogate, DP2-CN1-01).
- #6 1.3–2.75σ mixes constructions → **DP2-04/-07/-26** (heterogeneous-endpoint disclosure).
- #7 Bayes factors = prior-volume ratios, non-invariant rebooking → **DP2-18** (prior-sensitivity + Jacobian caveat).
- #8 f_NL–n_s "consistency relation" not derived, κ_ε order-of-magnitude → **DP2-20** (schematic ansatz, disclosed).
- #9 gauge-frame +0.015 "on-sky" mislabel / factor-146 → **DP2-21** (gauge-invariant-observable disclosure).
- #10 (UNMATCHED 0.22) radical compression + "reviewers' expectations"/artifact-IDs/"archive to be minted" →
  **DP2-02/-11/-27/-30** + PROCESS-NIT (no reset): scaffolding-phrase cleanup + Zenodo-DOI = OPEN-VENUE / editorial nit.
**0 genuinely-new.** ChatGPT REJECT on byte-unchanged v1.7.116 = maximal-harsh structural floor (DP2-24);
item set 1:1 with M15/M23/M31.

## Verdict
- **0 genuinely-new across both legs** → no bump (v1.7.116 stands), directive_g.sh NOT run.
- **Clean-wave streak 13→14.**
- **Cap = 74** (post_verdict.sh computed, latest-per-reviewer by _creationTime: Grok MIN 12 +
  ChatGPT REJ 0 + latest-Gemini [M19-INT] MIN 12 = 50+24=74). ChatGPT REJECT contributes 0; the M34
  Grok MINOR is the latest Grok row (+12). Authoritative computed value.
- Crux #1 falsified by RE-RUNNING the committed derivation + convention-free Li formula, NOT hand-waving.
- No ACCEPT faked, no finding dismissed without a source-cited verdict, no math fabricated.
