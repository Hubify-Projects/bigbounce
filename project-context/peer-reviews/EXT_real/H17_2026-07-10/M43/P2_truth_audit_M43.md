# P2 truth-audit — M43 EXT (2026-07-13)

**Paper:** P2 (matter-bounce f_NL = −35/16 SPHEREx forecast), byte-unchanged **v1.7.116**
(served md5-current; no edit this wave). Legs recovered after the headless
false-FAILED-dead incident (commit f797cbde). Raws read verbatim before any verdict:
`M43/P2_grok_M43.md` (+ `.png`) and `M43/P2_chatgpt_M43.md` (+ `.png`).

## Verdicts (from raw line 1, verified)
- **Grok = MINOR REVISIONS** (2 in-MINOR MAJ-tag / 3 MINOR under a MINOR-REVISIONS
  header — in-MINOR emphasis, pattern-066). Closing sentence AFFIRMS the corrected
  prediction: "The central claim—that the corrected matter-bounce prediction
  f_NL = −35/16 yields a SPHEREx detection significance of ∼2.6–2.75σ … is supported
  by the internal consistency checks, independent tree-level multi-tracer Fisher
  validation …, closed-form Bayes-factor derivation … and transparent disclosure of
  all assumptions and proxy limitations."
- **ChatGPT = REJECT** (11 MAJOR / 2 MINOR) — maximal-harsh floor (DP2-24). Its own
  point (3) CONCEDES: "the contraction-phase algebra provides some support for a
  squeezed-limit value f_NL = −35/16." REJECT rests on survival-through-bounce +
  forecast-scope (disclosed venue DP2-13/-17/-29). Structural harsh-referee floor
  (directive-H).

## Provenance (recovered legs — confirmed real assistant content, correct paper)
Both raws review the correct f_NL forecast paper: −35/16 vs −35/8 factor-of-two /
Cai et al. Eq. (37) / vertex sum / degree-9 polynomial null-space / r=0.84 template /
SPHEREx / Heinrich et al. Fisher 0.73 / ρ=−0.868 GR systematic / Bayes factor 9–14 /
Wilson-Ewing LQC all present. Neither is a truncation or wrong-paper.

## Per-finding disposition (ledger_match draft + Opus adjudication)
ledger_match: Grok 5/6 auto (#1 = "REVISIONS ISSUES:" scaffold-header non-finding),
ChatGPT 11/12 auto; UNMATCHED items Opus-adjudicated below. All source-cited standing
DP2 re-flags.

**Grok (2 MAJ-tag / 3 MINOR under MINOR-REVISIONS header):**
- Central f_NL: four verification methods cited but per-vertex squeezed-limit
  contributions (L_redef, L_ζζ̇², L_ζ̇∂ζ∂χ, L_ζ(∂i∂jχ)²) not tabulated side-by-side;
  discrepancy traced to −(99/128)∑k_i³ in Cai Eq.(37) → **DP2-02/-01/-16**
  (−35/16-vs-−35/8 / +99/128 convention disposition; deliberately disclosed,
  re-falsified by re-running committed p2_vertex_check.py + Li c_s=1 formula. ledger
  0.67).
- 1.3σ floor transfers proxy ρ=−0.868 across channels into bispectrum Fisher (Cov_B
  not public); channel-native ρ≈−0.42 cross-check heuristic; quantify sensitivity →
  **DP2-34/-14/-22** (RE-FLAG-DISCLOSED; channel-native ρ≈−0.42 → floor 2.32σ retained
  as conservative cross-check; ρ-transfer heuristic explicitly disclosed. ledger 0.75).
- (MINOR) null-space 6-coeff basis underdetermined → r=0.85±0.13 uniform vs 0.84±0.02
  noise-weighted; state whether ±0.02 folds representation uncertainty → **DP2-15**
  (reparametrization caveat verbatim in-paper. ledger 1.00).
- (MINOR) multiple significance endpoints from different procedures → single fiducial
  recast + summary table → **DP2-04** (presentation OPINION; distinctions already
  explained in-text).
- (MINOR) 37-page length; move coefficient tables / MC / surrogate Fisher to
  Supplement → **DP2-04/-31** (cosmetic OPINION).

**ChatGPT (11 MAJOR / 2 MINOR):**
- #1 App-A Eq.(A4) fixes coefficients (3,1,−9,5,−33,9) not adopted (2,7,3,−12,−69,19);
  null-space = deformations of a known shape; discard/recompute → **DP2-15/-01**
  (task-crux; the (5,2,2)-orbit ordered-vs-unique convention is deliberately disclosed,
  re-falsified by committed p2_vertex_check.py; headline −35/16 unaffected. ledger 0.82).
- #2 App-A factor-of-two diagnosis internally contradictory (Cai (34)-(37) already
  full-commutator; −2Im double-counts; −(99/128) is the same convention question) →
  **DP2-01/-16** (DP2-01 −35/16-vs-−35/8 disposition; the algebra ChatGPT itself
  displays "gives evidence for −35/16"; the specific spurious-term identification is a
  disclosed convention note, headline unaffected. ledger 0.64).
- #3 cubic transmission through bounce "not closed"; δf_NL≲10⁻³ an unsupported
  dimensional estimate not a theorem → **DP2-13** (load-bearing disclosed OOM caveat;
  Wilson-Ewing linear-transfer scope stated in-paper. ledger 0.38).
- #4 different bounce models/quantizations conflated (dressed-metric vs holonomy-
  corrected; c_s=1 vs c_s≪1 splice) → **DP2-19/-02** (RE-FLAG-DISCLOSED; c_s=1 canonical
  branch is the headline, c_s≪1 an explicitly-flagged alternative. ledger 0.33).
- #5 r=0.84 template correction not the SPHEREx Fisher cross-response (survey-weighted
  ≈0.99); ad hoc grid weights → **DP2-14** (RE-FLAG-DISCLOSED; 0.84 conservative
  cross-check vs 0.99 survey-weighted both reported. ledger 0.76).
- #6 independent Fisher (0.42–0.45) ≠ Heinrich (0.73) reproduction; missing RSD/
  photo-z/marginalization → **DP2-22** (RE-FLAG-DISCLOSED; in-house Fisher not
  end-to-end, disclosed. ledger 1.00).
- #7 GR systematic quadrature ≠ ρ=0 Fisher marginalization; ρ=−0.868 from SDB not
  bispectrum → **DP2-07** (RE-FLAG-DISCLOSED; channel-native ρ≈−0.42 retained as
  conservative. ledger 0.90).
- #8 **UNMATCHED (0.18)** b_φ degradation σ(f_NL)=0.7→0.9→1.0 asserted not calculated;
  Heinrich imposes universal-mass-function relations → **Opus RE-FLAG: DP2-22/-04**
  (b_φ-prior degradation asserted-not-recomputed = the standing DP2-04/-34 systematic-
  budget disposition + DP2-22 independent-Fisher-not-end-to-end; identical to the M41
  audit's "b_φ prior asserted → DP2-04/-34" mapping). NOT genuinely-new.
- #9 Bayes factors are prior-volume constructions (BF ∝ width W); no physical
  curvaton/QSFI likelihood → **DP2-18** (RE-FLAG-DISCLOSED; BF illustrative, disclosed.
  ledger 0.44).
- #10 quasi-dust κ_ε=2.8–40 + consistency relation not derived → **DP2-20/-19**
  (disclosed OOM caveat. ledger 0.78).
- #11 (MINOR) uncertainties propagated inconsistently (2.38–2.72σ vs 2.6–2.75σ) →
  **DP2-04/-19** (disclosed endpoint-provenance, re-flag).
- #12 (MINOR) scope/observable language (gauge-frame, MegaMapper, Einstein-Cartan,
  birefringence appendix peripheral) → **DP2-21/-30** (scope OPINION; disclosed
  supplementary material).

## Genuinely-new count: 0
Every finding fingerprint-matches a canonical DP2 disposition. The ChatGPT #1/#2
App-A crux is the standing DP2-01/-15 convention disposition, re-falsified by
re-running the committed p2_vertex_check.py derivation + the convention-free Li c_s=1
formula — headline −35/16 unaffected. ChatGPT's own conclusion concedes the −35/16
algebra. The one ledger_match UNMATCHED item (b_φ #8) is the standing DP2-22/-04
systematic-budget disposition, re-worded. No fabrication used to make any finding go
away.

## Recording
- clean-wave streak **16 → 17** (seventeenth consecutive clean wave on byte-unchanged
  v1.7.116).
- No bump (byte-unchanged v1.7.116); directive_g.sh NOT run.
- cap HOLDS **74** = 50 + Grok MIN 12 + ChatGPT REJECT 0 + latest-Gemini MIN 12
  (post_verdict.sh recomputed, verified in Convex).
- post_verdict.sh: `M43-Grok` minor-revisions, `M43-ChatGPT` reject (EXT bare labels).
- record_wave.sh P2 M43: genuinelyNew 0, streak 17, openCompute 4, openVenue 2.

## Integrity
No ACCEPT faked; no ChatGPT MAJOR/REJECT dismissed without a source-cited verdict;
no math fabricated — the App-A crux is falsified by re-running the committed derivation,
not by asserting a value. Recovered legs verified as real, on-paper assistant content
before any verdict recorded.
