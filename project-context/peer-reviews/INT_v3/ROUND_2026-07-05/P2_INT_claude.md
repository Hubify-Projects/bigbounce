# P2 INT full-source referee review — v1.7.92 (2026-07-05)

**Leg:** Claude Code INT (Houston subscription, NOT Anthropic API — correct routing per directive I1).
**Paper:** `research/focused_paper_source_integration/02_full_draft.tex` (1345 lines, PDF dated Jul 6, 0 undef-refs).
**Method:** Full .tex read + independent symbolic re-derivation (sympy) of the vertex sum, marginalized-σ arithmetic, and the c11 non-local projection verified against the committed script/JSON.

---

## VERDICT: MINOR REVISIONS

The central claim — matter-bounce `f_NL = -35/16` detectable at ~1.3–2.6σ by SPHEREx — **is supported**. The five session upgrades are correctly and honestly implemented, with honest caveats intact and no fabricated numbers. One genuinely-new internal issue found that EXT (PDF-only) cannot catch: the "spurious term → −35/8" traceability sub-claim is not self-verifying from the stated equation.

---

## Verification of this session's 5 P2 upgrades

### 1. Factor-of-2 RESOLVED to −35/16 (App. A vertex certification) — VERIFIED (with one MINOR)
Independent sympy re-summation of the four cubic vertices in Table `tab:vertices` (rows L1230–1235) at ε=3/2, forming `f_NL=(10/3)A/Σk³`, gives:
- **squeezed limit `k1≪k2=k3`: `-35/16 + (35/64)(k1²/k²) + …` → −35/16`** — matches Eq.(vertexsum) L1241 and Eq.(decisive_sqz) L1213 **exactly**, including the +35/64 subleading coefficient.
- **equilateral: `-255/128`** — matches L1216 exactly.
This is the load-bearing positive result and it is **certified correct**, not fabricated. The Li Eq.(5.1) cross-check `-165/16+65/(8c_s²)→-35/16` at c_s=1 is trivially correct.

### 2. Cubic transmission derived (single-clock LQC ζ-conservation, 1±10⁻⁴) — VERIFIED / HONEST
Abstract L655 states it as *derived to a bounded systematic* via single-clock field content (no new scalar dof; WilsonEwing:2012, Cailleteau:2011kr), transmission `1±O((kη_B)²)≈1±10⁻⁴`, δf_NL≲10⁻³. The one model-choice input (subleading gradient sign, dressed-metric Lorentzian c_s²=1) is honestly flagged as a *citable quantization choice, not an open computation*. Not overclaimed — the residual is disclosed. Write-up `INT_v3/P2_cubic_adiabaticity_2026-07-05.md` present.

### 3. Systematic budget marginalized (~1.3σ, proxy ρ=−0.868, missing ∂B/∂A_GR flagged) — VERIFIED, arithmetic correct
- `σ_marg = 0.7/√(1−0.868²) = 1.41` (paper says 1.42 — 0.7% rounding, acceptable).
- floor `|−35/16|·0.84/1.41 = 1.30σ` (paper ~1.3σ). ✓
- tab:systematics row L1094 + caption L1097 **explicitly label ρ=−0.87 as a PROXY** "transferred pending the channel-native ∂B_g/∂A_GR derivative." The deferred derivative is disclosed, not hidden; the marginalized floor honestly *worsens* the number (correct direction). Not overclaimed.

### 4. r=0.84 shown robust (non-local template projection δr≤0.002) — VERIFIED against committed code
`scripts/c11_nonlocal_template_projection.py` is a **genuine vectorized computation** (eval_monomials/perm6_sum/cosine/joint_projection over the 23,098-triangle grid), not hardcoded. JSON `c11_nonlocal_template_projection.json`:
- uniform LOCAL cosine −0.98495 → reproduces the paper's r_cos=0.985 **exactly** (L806).
- LOCAL/EQUIL/ORTHO −0.985/−0.45/+0.94 match body L811–812.
- joint frac_full 0.9737 vs frac_local 0.9701 → raised by ≤0.004 → **δr≤+0.0018 ≤ 0.002** (L808–810). ✓
- The high ORTHO cosine is correctly explained as **collinearity** (ortho ≡ −3·local+…), removed by the joint fit (L811–815). Honest scope caveat (geometry-only, full-3D estimator-mismatch variance out of scope) intact L819–820.

### 5. Central-value consistency (no stale −35/8 headline) — VERIFIED
All body `-35/8` occurrences are explicitly labeled *"erroneous published / reference only"* (L1209, L1331, L1335) or appear in captions that headline the *corrected* −35/16 (L752, L862, L1097). Eq.(2) squeezed limit reads −35/16 (v1.7.90 fix). No active headline uses −35/8. Planck recast arithmetic checks: `|−2.1875+0.1|/5.71 = 0.37σ` (L1107). ✓

---

## Issue list

### [MINOR] App. A (Eq. `spurious`, L1218–1221): the "+(99/128)Σkᵢ³ pushes −35/16→−35/8" traceability is NOT self-verifying from the stated equation.
The vertex sum → −35/16 is airtight. But the claim that Cai's *printed* Eq.(37) exceeds the vertex sum by exactly `+(99/128)Σᵢkᵢ³` **and** that this term is "exactly what pushes −35/16→−35/8 in the squeezed limit" cannot be reproduced from Eq.(spurious) alone. A local-shaped positive `+(99/128)Σk³` added to A contributes `+(10/3)(99/128)=+2.578` to the squeezed f_NL (→ +0.39), whereas reaching −35/8 requires a **negative** −2.1875 shift. To flip −35/16→−35/8 the extra term's squeezed-limit reduction must be negative, which the stated positive local term does not obviously produce. The −35/8 origin therefore rests on Cai's full (unstated-here) printed-polynomial permutation reduction, not on the isolated Eq.(spurious). **Fix (no number change):** either (a) show the squeezed reduction of `A_T^printed` end-to-end so the −35/8 is reproducible, or (b) soften L1221 from "is exactly what pushes −35/16→−35/8" to "is the discrepancy between the printed polynomial and the vertex sum; the printed polynomial's own squeezed reduction gives −35/8" — i.e. attribute −35/8 to Cai's printed reduction, not to a naive add of Eq.(spurious). EXT (PDF-only) cannot catch this; the −35/16 headline is unaffected either way.

### [MINOR] Consistency: σ_marg rounding 1.41 vs stated 1.42 (tab:systematics L1094, changelog).
`0.7/√(1−0.868²)=1.409`. Paper rounds to 1.42 in the table row while ρ is stated as −0.87 (which does give 1.42). Harmless but internally the changelog cites ρ=−0.868 (→1.41) and the row cites ρ=−0.87 (→1.42). Pick one ρ for reproducibility. No downstream number affected (floor is 1.3σ either way).

### [MINOR/OPINION] Length + recast framing.
28pp; the recast-vs-independent-forecast framing is now hoisted to abstract sentence 1 and repeated. This is a deliberate, honestly-labeled scope; no science error. Recurring EXT MAJORs on this are already dispositioned (signpost L1175).

---

## Bottom line
Central claim supported. Five upgrades correctly + honestly implemented — no fabrication, honest caveats (proxy degeneracy, deferred ∂B/∂A_GR derivative, single-clock model choice, geometry-only projection) all intact and not overclaimed. The one real source-level catch EXT would miss: the −35/8 *origin* attribution to Eq.(spurious) is not self-verifying (the −35/16 result itself is independently certified 3 ways and stands).
