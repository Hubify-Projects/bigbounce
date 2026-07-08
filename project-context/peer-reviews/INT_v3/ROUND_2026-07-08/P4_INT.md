# P4 INT — full-source regression check (v1.0.223)

**Reviewer:** Claude Code INT (subscription subagent, full-source read — CLAUDE.md I1)
**Scope:** closure-wave regression check only (§IV.D bound-first lead + "not reliably recovered"/A_95 language vs abstract falsification criterion). No new-finding hunt.
**File:** `pipelines/p2_chirality/chirality_catalog_paper.tex`

## Verdict: CLOSURE WAVE CLEAN — no regressions

### Abstract falsification criterion (L584)
"Falsification criterion: a future real-space dipole detection at ≥5σ … with amplitude A ≳ A_95, where injection–recovery brackets **A_95 in (1.0%,1.5%]** (**A_50≈0.75%**), would be in tension with this null." Harmonic-channel completeness (P(≥3σ)≥0.999 at A_p=0.75%) explicitly labeled a separate property.

### Bound-first / null-first framing consistent everywhere
- Abstract L578: "find it consistent with null"; primary real-space dipole +0.41σ (p=0.31); WLS disfavors a clean 1.7% dipole at z≈−18. Parity-EVEN axial-vector channel disclosed.
- Intro L601: "measured dipole is consistent with null"; empirical 50%-recovery-3σ injection floor at |A_dipole|≥0.75% — matches abstract A_50≈0.75%.
- §Dipole body (L884+): injection-recovery floors A_50≈0.75% / A_95 used consistently; the unthresholded full-sample excess (A_p=0.57%, z≈4.2–4.4) is stated to sit **between** the full-sample A_50≈0.36% and A_95≈0.63% and is dispositioned as residual depth-correlated classifier systematic, "not a detection." The a-fortiori residual-bound-first ordering (from v1.0.222) is preserved and coherent with the A_95 criterion — the paper never claims a signal it did not reliably recover; below A_95 is explicitly "not reliably recovered / bounded null."
- A_95,nq null-quantile (6.8×10⁻³ A_p) is carefully labeled "NOT a signal-injected limit, carrying no frequentist coverage guarantee" — distinct object, no conflation with the injection A_95. No contradiction.

### v1.0.223 closure edits (commit d3941cf4)
Diff shows version bump + additive content only:
- GZ1 human-only independence cross-check (N=4.60×10⁴, z=−0.54σ) — reinforces null.
- Pre-registration of the 0.6 cut (commit 94113e5, 2026-06-09) — reinforces no-forking-paths.
- Selection-function note distinguishing HC-subsample test from WLS fit — both return null.
None alters the abstract's falsification criterion or the A_50/A_95 numbers.

### Number integrity
A_50≈0.75% (HC broad), A_95∈(1.0%,1.5%], full-sample A_50≈0.36%/A_95≈0.63%, +0.41σ primary, N_HC=949,584, 3,201,160 spirals — all consistent between abstract, intro, and body. No headline number changed in v1.0.223 (diff = title/version + additive prose).

Regressions: **none**.
