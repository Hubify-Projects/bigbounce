# FR1b ChatGPT-retry — EXT truth-audit (2026-07-11)

Recovers the FR1-round EXT ChatGPT rate-limit GAP (FR1 recorded ChatGPT + Gemini as
chart GAPs; FR1b re-ran the ChatGPT leg). Reviewed the July-11 restamped versions
(P1U v1U.0.13 · P2 v1.7.113 · P3 **v3.1.153, PRE-NANOGrav-fix** · P4 v1.0.236 · P5 v0.1.121).
Raws + screenshots in `FR1b/{P1U,P2,P3,P4,P5}_chatgpt_FR1b.md`; each raw's verbatim
`VERDICT:` line READ before any verdict recorded. Pre-triage: `tools/ledger_match.py`
per raw (drafts saved as `FR1b/{P}_ledger_match.md`); every UNMATCHED finding Opus-adjudicated
verdict-first + source-cited against the paper `.tex` + `DISPOSITIONS/*.md`.

## Verdict matrix (EXT ChatGPT, FR1b)

| paper | ChatGPT FR1b | maj/min | ledger_match | UNMATCHED → disposition | genuinely-new |
|-------|--------------|---------|--------------|--------------------------|---------------|
| P1U   | **REJECT**   | 14/1    | 9/15         | #3,#4→DP1U-07; #9,#10,#15→DP1U-12; #11→DP1U-14; #13→DP1U-13 (+ -20/-22) | **0** |
| P2    | **REJECT**   | 9/1     | 9/10         | #3 viable-model (c_s) → DP2-02/-19 | **0** |
| P3    | **REJECT**   | 13/2    | 14/17        | #10 novelty→DP3-07/-09; #15 PRD-scope→DP3-10; #16 spatial MINOR→DP3-09 | **0** |
| P4    | **REJECT**   | 11/3    | 10/14        | #7 A50/A95→DP4-17; #8 MASTER→DP4-16; #10 GZ1→DP4-09; #14 MC-precision→DP4-09/PROCESS-NIT | **0** |
| P5    | **MAJOR REVISIONS** | 12/2 | 14/16 | #1 parser-noise header; #9 covariate→DP5-19/-10 | **0** |

**NET: 0 genuinely-new reader-visible editable findings across all 5 papers.** Every
ChatGPT FR1b finding is a source-cited RE-FLAG of a standing D-id (or PROCESS-NIT /
OPEN-COMPUTE / OPEN-VENUE). No resets. No version bumps. `directive_g.sh` not run (no edit).

## Per-paper

- **P1U — REJECT (14 MAJ / 1 MIN).** All re-flags: variational-hybrid Eq(1)/Cartan→DP1U-03;
  dim+1→+4 no-go→DP1U-08; O1–O6 basis-completeness/Nieh–Yan + Fierz mixed V⊗A→DP1U-07/-20;
  R1 NJL condensate (⟨J5⟩=0 ⇏ ⟨J5 J5⟩=0)→DP1U-05; R2 one-loop/∂ϑ bookkeeping→DP1U-09;
  R3 Δγ→dark-energy mapping→DP1U-10; R4 ALP free-coupling→DP1U-11/-05; dynamical-CS
  transparency-misapplication + Sec-X overuse→DP1U-12; D_inf/N_tot≃92/matter-bounce-erasure→DP1U-14;
  13-barrier independence→DP1U-13; App E–G don't test ECH→DP1U-15; global-restructure/repetition
  MINOR→DP1U-22 (PROCESS-NIT / OPINION). Streak HOLDS at 3.

- **P2 — REJECT (9 MAJ / 1 MIN).** Re-flags: artificial polynomial null-space→DP2-15;
  −35/16 vs Cai −35/8→DP2-01; no-consistent-viable-model / c_s tension (−165/16+65/8c_s²)→DP2-02/-19;
  cubic-transmission δf_NL≲10⁻³→DP2-13; template-mismatch estimator response→DP2-14;
  Heinrich Fisher not like-for-like→DP2-22; 1.3σ/0.8σ ρ=−0.868 floor→DP2-07; Bayes-factor
  prior-volume→DP2-18; quasi-dust κ_ε / f_NL–n_s relation→DP2-20; observer-frame MINOR→DP2-21.
  Streak HOLDS at 4.

- **P3 — REJECT (13 MAJ / 2 MIN).** Reviewed v3.1.153 (pre-fix). Re-flags: validated-catalog-grade
  268,519→DP3-07; DESI population/SPECTYPE accounting→DP3-11; Liang like-for-like→DP3-07;
  arbitrary 77,905 SDSS tier + cross-transfer/native conflation→DP3-14; score/validation gates→DP3-06;
  DESI generalization (fold val_loss 1.91)→DP3-12; Planck tier→DP3-06; novelty-fraction 58.8%→DP3-07/-09;
  f_NL forecast→DP3-10; reproducibility/provenance→DP3-08; 37.3M scale→DP3-04; PRD-split→DP3-10;
  spatial-diagnostics + superseded-figures MINORs→DP3-09/-07 (PROCESS-NIT).
  **NANOGrav §V A/App E finding → DP3-18/-10 SCOPE RE-FLAG:** the ChatGPT finding critiques the
  γ=3 mapping / KDE-product covariance / "density ratio is not evidence" / catalog-disconnect —
  it does **NOT** re-surface the +4.61σ arithmetic. That specific mis-round (+4.61→+4.63σ) was
  already caught (Claude-INT, FR1) and **CLOSED-BY-EDIT in v3.1.154** (correct +4.63σ, DP3-18).
  Cite the existing v3.1.154 fix — **not** a new closure and **not** a new reset. Streak stays 0
  (from the prior FR1 DP3-18 reset).

- **P4 — REJECT (11 MAJ / 3 MIN).** Re-flags: p_eq>0.6 post-selection→DP4-07; classifier-validation
  GZ1 69.91%/κ=0.40→DP4-15; z≃−7.6 vs 1.7% dilution model + block-bootstrap WLS→DP4-01;
  47% residual + A50/A95-not-upper-limit→DP4-17 (OPEN-COMPUTE); MASTER +3.64σ vs +7.93σ→DP4-16
  (OPEN-COMPUTE); hard-argmax/flip-equivariance→DP4-08; GZ1-under-powered→DP4-09; DOI-pending→DP4-21;
  interpretation + sample-size + MC-precision MINORs→DP4-12/-13/-09 (last = disclosed future-work
  L1091, PROCESS-NIT). Streak HOLDS at 5.

- **P5 — MAJOR REVISIONS (12 MAJ / 2 MIN) — FLOOR-CRACK HOLDS.** ChatGPT's first non-REJECT tier-lift
  on P5 persists on the restamp (NOT REJECT). Re-flags: same-footprint estimand→DP5-06;
  volume-limited BGS anchor→DP5-07; V2 sphere-membership→DP5-16; Bonferroni-5 family + non-rejection≠
  equivalence→DP5-04; 0.9-pp quadrature→DP5-11; two-proportion SE spatial-covariance→DP5-10;
  covariate-adjustment-in-lieu→DP5-19/-10 (OPEN-COMPUTE); de-attenuated 2.26-pp→DP5-08; RSD
  fixed-geometry→DP5-12; T-Web→DP5-14; PRD-relevance toy-EFT→DP5-20; Paper-IV dependency→DP5-21;
  presentation + QSO-in-primary MINORs→DP5-17/-09. (Raw finding #1 = a parser-noise "REVISIONS ISSUES:"
  header fragment, not a finding.) **Cap effect:** latest-per-EXT-reviewer ChatGPT MAJOR (6) replaces
  the prior REJECT (0) → P5 readiness cap **74→80** (50 + grok-MIN 12 + chatgpt-MAJ 6 + gemini-MIN 12).
  Streak HOLDS at 3.

## Caps (post-FR1b, Convex-synced)

P1A 62 · P2 74 · P3 62 · P4 74 · **P5 74→80**. Only P5 changed (the ChatGPT floor-crack). All
other papers' latest ChatGPT was already REJECT, so their caps are unchanged.

## Integrity

Every verdict READ from the raw's verbatim `VERDICT:` line before recording. No ACCEPT faked;
no finding dismissed without a source-cited verdict; no math fabricated. P5's REJECT→MAJOR tier-lift
recorded honestly (it lifts the cap by the standing formula but does not by itself alter any
clean-wave streak — the 0-genuinely-new count governs streaks). The FR1 EXT ChatGPT/Gemini GAPs
were honestly recorded as failures (never zeros); FR1b closes the ChatGPT GAP only (Gemini EXT
remains a GAP this round).
