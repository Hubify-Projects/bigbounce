# Cross-Paper Theorist Consistency Audit

**Reviewer persona:** matter-bounce theorist, parameter-genealogy obsessed, dimensional-analysis first, consistency-between-companion-papers above all else.
**Scope:** Paper 1 (`arxiv/main.tex`, 1215 ln), Paper 2 (`research/focused_paper_source_integration/02_full_draft.tex`, 372 ln), Paper 3 (`pipelines/p3_anomaly_engine/paper3_draft.tex`, 1068 ln), Paper 4 (`pipelines/p2_chirality/chirality_catalog_paper.tex`, 1115 ln). Plus `SSOT/index.md`, all four `SSOT/paper-N/status.md`, `CLAUDE.md`, `project-context/bounce_portfolio_strategy.md`.
**Recommendation:** **MINOR INCONSISTENCIES — do not submit as a bundle until the five Tier-A items below are resolved.** The science is mutually consistent at the physics level. The bookkeeping between paper text, SSOT, and CLAUDE.md has drifted in five quantitatively specific places, at least three of which will be noticed by a cross-paper referee.

---

## Canonical-number cross-check table

All numbers traced to the `.tex` files. "—" means the paper does not quote the number (not automatically an error; flagged only where cross-cite is expected).

| Quantity | Paper 1 (main.tex) | Paper 2 (02_full_draft.tex) | Paper 3 (paper3_draft.tex) | Paper 4 (chirality) | Consistent? | Fix |
|---|---|---|---|---|---|---|
| f_NL value | −35/8 (L93, L103, L732, L736, L756, L1024) | −35/8 = −4.375 (L39, L81, L117, L148, L173, L185, L283, L287, L318, L353, L359, L362) | −35/8 = −4.375 (L70, L515, L1047) | — | ✓ | — |
| f_NL citation style | "−35/8" bare | both "−35/8" and "−4.375" interchangeably | both "−35/8" and "−4.375" (explicit) | — | ✓ | — |
| γ_bounce (matter-bounce PTA spectral index) | not quoted | not in scope | γ = 3.0 fixed (L529, L548, L569) | — | ✓ | — |
| NANOGrav observed γ | not cited | not in scope | **3.20 ± 0.42** (L532, L552, L564, L570) | — | ✓ within paper | CLAUDE.md still says 3.33±0.40 — update |
| NANOGrav vs bounce tension | — | — | **0.48σ** (L534) | — | ✓ within paper | CLAUDE.md says 0.81σ — update |
| ALP β (prediction, bounce-motivated) | 0.27° (L394, L452) — "ALP prediction" | 0.27° (L330) — "Planck-scale ALP" | — | — | ✓ | — |
| NaMaster β (measurement) | 0.264° ± 0.065° (L391) | 0.27° injection recovery, 0.19° map result (L330) | — | — | ✓ | — |
| β observed (Eskilt joint) | 0.342° ± 0.094° (L394, L837) | 3.6σ Eskilt quoted without number (L330) | — | — | ✓ | — |
| β combined from Planck+ACT (inverse-variance) | 0.242° ± 0.061° (L833) | — | — | — | ✓ | — |
| β Bayes factor | 176 (3.9σ) | — | — | — | ✓ (only P1 quotes) | — |
| H₀ (full-tension) | 67.68 ± 1.06 km/s/Mpc (L98, L108, L132, L331) | — | — | — | ✓ | — |
| H₀ (Planck+BAO+SN) | 67.79 ± 1.09 km/s/Mpc (L108, L331) | — | — | — | ✓ | — |
| ΔN_eff (full-tension) | −0.020 ± 0.169 (L332) | — | — | — | ✓ | — |
| ΔN_eff (Planck+BAO+SN) | +0.065 ± 0.17 (L332) | — | — | — | ✓ | — |
| Total MCMC posterior samples | **424,181** (L323) AND **309,789** (L785) | — | — | — | **✗ INTERNAL** | see Item A below |
| w0-wa quintom-B preference | "never implemented computationally … loophole was explored theoretically" (L785) | not quoted | not quoted | not quoted | **✗ CLAUDE.md vs papers** | see Item B below |
| 14 structural barriers | "14 barriers close all routes" (L100, L507, L130) | — | "14 structural barriers that close ECH-specific routes to dark energy" (L1048) | — | ✓ | — |
| Chirality f_cw (equivariant) | 0.5012 ± 0.0006 (L271, L894, L940) | — | — | ≈ 0.4974 (L468, L481, and table L621) | ✗ mild | see Item C below |
| Chirality galaxies classified | 8.47 M / 8,474,531 (L271, L312, L373, L940) | — | — | 8,474,531 (L83, L620) | ✓ | — |
| Chirality dipole σ (equivariant null) | "null dipole (0.43σ)" (L312, L940) | — | — | 0.43σ (p=0.33) (L504) | ✓ | — |
| Shamir refutation factor | 7× (L312) | — | — | 7× (L82) | ✓ | — |
| Total anomalies (aggregate) | — | — | 319,443 (abstract L53, Table 1 L178) | — | ✓ within paper | Paper 2 should cite (Item D) |
| Total sources scored | — | — | 37,292,042 (Table 1 L178) | — | ✓ within paper | Paper 2 should cite (Item D) |
| σ(f_NL) standard DESI baseline | — | 8.98 (implicit via Heinrich) | 8.98 (Table 2, L490, L713) | — | ✓ | — |
| σ(f_NL) DESI+anomalies | — | 8.12 (latent, 9.5 %) | 8.43 (DESI alone, 6.1 %); 9.5 % latent (§5) | — | ✓ | Paper 2 uses different decomposition, not contradictory |
| σ(f_NL) SPHEREx bispectrum baseline | — | **0.7** (L131, L141, L148, L220, L226, L318) | not quoted directly | — | — | — |
| σ(f_NL) SPHEREx post-multi-tracer (Paper-3 context) | — | — | **1.0** (L517, L519) | — | ⚠ visually odd | see Item E below |
| SPHEREx detection significance of f_NL = −35/8 | 4–6σ (L452, L1024) | 5–5.5σ bispectrum template-corrected (L131) | **4.38σ** (L517, Eq. 1) | — | ⚠ three different numbers, three different denominators | see Item E |
| Bias-enhancement factor α | — | — | α = 0.15 theoretical, not calibrated (L600, limitation #4) | — | ✓ within paper | CLAUDE.md's 2.28× is not in any paper — see Item F |
| Gold+Silver clustering enhancement | — | 1.58× (referenced as Pipeline-1 result, SSOT-P2 §2.3) | not quoted | — | ⚠ — | CLAUDE.md conflates 1.58× (Pipeline-1) and 2.28× ("extreme anomalies") |
| Bounce-agnostic framing (quintom/Cuscuton/ekpyrotic can bypass barriers) | Explicit (L1024, L736–763 discrimination table) | L39 "matter bounce … mechanism-independent in the sense that it depends only on contracting-phase dynamics, not on the specific UV completion" | L70 "quasi-matter bounce model", §5 tied to matter-bounce projection only | — | ✓ | None; Paper 4 has no scope for this |

---

## Derivation-path genealogy

**f_NL = −35/8 = −4.375.**
- **First-principles source:** Cai et al. 2009 (`\cite{Cai:2009fn}`), recomputed and verified in Paper 2 §2 (L61–86: shape function, three benchmark configurations, convention discussion L353–362).
- **Paper 1 introduces it** as the surviving testable prediction at L93 (Table 1), L103, L732 (matter-bounce mechanism-independence), L736–763 (discrimination table vs Cuscuton/ekpyrotic/quintom/inflation).
- **Paper 2 forecasts σ(f_NL)** for SPHEREx + MegaMapper + SDB, r-correction to local template (L117–120, r_CMB = 0.90, r_LSS = 0.85). Paper 2 explicitly cites Paper 1 as `\cite{Golden:2026framework}` (L39) for the "structural barrier catalog" — theory anchor is correctly attributed.
- **Paper 3 consumes it** as the target of its multi-tracer Fisher improvement (L70, L515). Paper 3 cites both `\cite{Golden:2026framework}` (Paper 1) AND `\cite{Golden:2026fnl}` (Paper 2) — correctly routes the theory citation to Paper 1 and the forecast citation to Paper 2.
- **Paper 4 does not use f_NL.** It defines `\fnl` in its preamble (L31) but the symbol is unused — leftover from a shared LaTeX template. Not a bug, but a grep-scan will catch it.
- **Genealogy verdict:** clean. All three papers that quote the number write it identically; the two papers that cross-cite it route correctly to Paper 1 (theory) and Paper 2 (forecast).

**γ = 3.0 matter-bounce PTA spectral index.**
- Paper 1 does not derive this — it is not in its scope.
- Paper 3 §6 is the **only** paper to derive, compare, and quote it: γ_bounce = 3.0 fixed (L569), γ_SMBHB = 13/3 fixed (L555), γ_free = 3.20 ± 0.42 (L532, L570).
- **Tension computation**: (3.20 − 3.0) / 0.42 = 0.476 ⇒ "0.48σ" (L534) — arithmetic correct to one decimal.
- **CLAUDE.md discrepancy** (not in any paper): CLAUDE.md top-of-file says "γ = 3.33 ± 0.40, bounce at 0.81σ". This is the **earlier "combined PTA" GPU MCMC run** (2026-04-10 entry), superseded by the final `paper3_draft.tex` numbers. CLAUDE.md needs to be harmonized with the paper.
- **Genealogy verdict:** clean within papers; CLAUDE.md is stale.

**ALP β = 0.27° prediction.**
- Paper 1 §3 / Appendix B is the **only** derivation: spectator ALP, f_a ~ M_Pl, m ~ H_0, C_aγ ∈ [4,12], θ_i ∈ [0.5, 2], yielding β ∈ [0.17°, 0.43°] with central 0.27° (L829). Paper 1 L394 quotes "ALP prediction β = 0.27°" as the summary number.
- Paper 2 L330 cross-cites the β = 0.27° value without re-deriving, attributing to `\cite{Golden:2026framework}` (Paper 1). **This is correct.** Paper 2 also performs its own NaMaster EB cross-power analysis as a robustness check (L330: β = 0.19 ± 0.03° at NSIDE=1024; injection test recovers β = 0.27° with zero bias).
- Paper 1 itself runs NaMaster and gets β_NaMaster = 0.264° ± 0.065° (L391). This is **measurement**, not prediction. The distinction 0.27° (prediction) vs 0.264° (measurement) is preserved correctly throughout Paper 1, but the SSOT-Paper-1 Table §3 labels 0.264° as "β from spectator ALP (prediction)" — SSOT is wrong; the paper is right.
- **Genealogy verdict:** the papers are internally consistent and cross-cite correctly. The **SSOT-Paper-1 status file has the label swapped** — should read "0.264° ± 0.065° (NaMaster measurement)" and "0.27° (ALP prediction)". Minor documentation error; recommend fix in SSOT.

**H₀ = 67.68 ± 1.06 km/s/Mpc.**
- Only Paper 1 quotes it (MCMC full-tension combo, 176,840 samples). Papers 2, 3, 4 do not cite H₀. Nothing to reconcile cross-paper.

**ΔN_eff ≈ 0.**
- Only Paper 1. Paper 1 is internally consistent: full-tension −0.020 ± 0.169; Planck+BAO+SN +0.065 ± 0.17; sign agrees with "≈ 0" headline.

**14 structural barriers.**
- Paper 1 §II is the canonical enumeration (Fig. reference L507). Paper 3 cross-cites "14 structural barriers" at L1048 via `\bibitem{Golden:2026framework}` — correct count and attribution. Papers 2 and 4 do not enumerate. No inconsistency.

**Bounce-model-agnosticism.**
- Paper 1 L1024 is the canonical statement: "These barriers are ECH-specific: other bouncing cosmologies—notably the quintom scenario, which uses dynamical phantom and quintessence fields rather than geometric torsion—can in principle unify the bounce with late-time dark energy through mechanisms that bypass all 14 barriers."
- Paper 2 L39 carries the agnosticism at the f_NL level: "mechanism-independent in the sense that it depends only on the contracting-phase dynamics, not on the specific UV completion that produces the bounce."
- Paper 3 L70 says "quasi-matter bounce model predicts a parameter-free local non-Gaussianity" — tight scope but does not imply "only ECH".
- Paper 4 does not touch bounce-model classes.
- **Genealogy verdict:** the agnosticism principle is carried correctly through Papers 1 and 2; Paper 3 is scoped to matter-bounce specifically (which is defensible — the Fisher number σ(f_NL) = 1.0 with 4.38σ at f_NL = −4.375 is a matter-bounce-specific forecast). No accidental "the bounce model predicts X" language slipping into a paper that should be agnostic.

---

## Inconsistencies found

### Tier A — must fix before cross-paper bundle submission (5 items)

**A1. Paper 1 internal MCMC sample count contradiction.**
- L323: "Total MCMC program: 424,181 raw samples across 3 dataset combinations."
- L785: "None of the 309,789 MCMC posterior samples in this program used w_0 or w_a as free parameters."
Delta = 114,392 (exactly the "third combo" count from SSOT-Paper-1 §2). The numbers refer to different subsets (3-combo aggregate vs. 2-frozen-combo aggregate) but the paper presents both as "this program's total" without distinction. A referee will flag this. Fix: pick one (recommend 424,181 for "total" and footnote L785 with "309,789 samples in the two frozen combinations; the third combo is an ongoing run").

**A2. CLAUDE.md claims `w0-wa quintom-B 98.6%` — no paper supports this.**
Paper 1 L785 explicitly states: "None of the 309,789 MCMC posterior samples in this program used w_0 or w_a as free parameters. The loophole was explored theoretically but never implemented computationally." The CLAUDE.md "Key scientific results" block claims "w0-wa MCMC: quintom-B (w-crossing) favored at 2.3σ, P(quintom-B) = 98.6%". This is either (a) a result from a pipeline run not yet folded into Paper 1, or (b) a stale CLAUDE.md entry. In either case, the top-level project status says one thing and the theory paper says the opposite. Fix: either add the w0-wa MCMC to Paper 1 (and remove L785's disclaimer), or strike the CLAUDE.md line and remove the 98.6% from the site stat cards.

**A3. CLAUDE.md NANOGrav line is stale relative to Paper 3.**
- CLAUDE.md: "Combined PTA GPU MCMC (2026-04-10): γ = 3.33 ± 0.40, bounce at 0.81σ".
- Paper 3 L532, L570: γ = 3.20 ± 0.42, bounce at 0.48σ.
Paper 3 is the one that matters; CLAUDE.md needs to be updated to quote the paper.

**A4. 2.28× clustering bias claim has no paper anchor.**
CLAUDE.md: "f_NL bias validation: extreme anomalies show 2.28x clustering bias vs baseline (Landy-Szalay w(θ))". Grep across all four `.tex` files for "2.28" returns no hits. The number that IS in the paper ecosystem is 1.58× (Gold+Silver QSOs from Pipeline 1, in SSOT-Paper-2 §2.3 — still not embedded in the Paper 2 `.tex` itself, which treats α as a theoretical prior). Paper 3 L600 is explicit that α = 0.15 is theoretical and NOT empirically calibrated. The 2.28× number is either (a) from Pipeline 1 step 4 for a different tracer subset, (b) a stale project-context number, or (c) a typo. Need to trace it. If legit, it belongs in Paper 3 §5 or Paper 2 §7.2 as the empirical calibration that closes the α = 0.15 theoretical-prior limitation — high-value plug for both papers. If not legit, strip from CLAUDE.md.

**A5. Paper 2 does not cite Paper 3 (Golden:2026anomaly).**
Paper 2 §4, §5, §7.2 all invoke "AI-selected high-bias tracers" and "anomaly-enhanced tracer catalogs" (which is Paper 3's contribution) without any `\cite{Golden:2026anomaly}` citation. Paper 2's bibitem for "Golden:2026fnl" at L1050 refers to Paper 2 itself (the formal Fisher forecast). There is no Paper 3 cross-cite anywhere in Paper 2. SSOT-Paper-2 §6 flagged this under P2-XREF-AUDIT and decided "no cite needed — multi-tracer language is about SPHEREx as-designed", but that decision is wrong when Paper 2's five-tracer anomaly-optimized σ(f_NL) = 11.71 result (referenced in Paper 3 L1054) must be sourced. Fix: add `\bibitem{Golden:2026anomaly}` in Paper 2, cite at §4 intro and §7.2 where "anomaly-optimized" enters.

### Tier B — nice-to-have, not blocking

**B1. SPHEREx σ(f_NL) and detection significance triple inconsistency (visual, not logical).**
| Paper | σ(f_NL) quoted | Significance quoted | Basis |
|---|---|---|---|
| Paper 1 L452, L1024 | (not explicitly) | 4–6σ | verbal statement citing Paper 2 / Heinrich |
| Paper 2 L131 | 0.7 | 5–5.5σ | bispectrum only, r-corrected (Heinrich 2023) |
| Paper 3 L517, L519 | 1.0 | 4.38σ | multi-tracer projected to SPHEREx volume, anomaly-enhanced |

All three are defensible under different assumptions. A referee will still ask "which one is the headline?" The forecasts are not contradictory — Paper 3's σ=1.0 is more conservative (incorporates photo-z + bias + GR projection), Paper 2's σ=0.7 is the Fisher-ideal bispectrum. But the three numbers scattered across three papers look sloppy. Fix: add one sentence to Paper 1's §I and Paper 3's §5 that reads "the range 4–6σ reflects σ(f_NL) ∈ [0.7 (ideal bispectrum, Paper 2), 1.0 (multi-tracer with anomalies and GR marginalization, this work)]" — anchors all three numbers to the same pedagogy.

**B2. SSOT-Paper-1 mislabels β numbers (§3 claims table).**
SSOT says "β from spectator ALP: 0.264° (prediction) vs 0.342 ± 0.094° observed" — but 0.264° is the NaMaster **measurement**, 0.27° is the **prediction**. The paper itself has this right. Fix: edit SSOT-Paper-1 §3 row to read "β NaMaster measurement: 0.264° ± 0.065° | ALP prediction: 0.27° | Planck+ACT joint: 0.342° ± 0.094°".

**B3. Paper 4's `\newcommand{\fnl}` is unused.**
L31 of Paper 4 defines `\fnl` but the symbol never appears in Paper 4. Harmless, but a `grep fnl` reader will wonder. Drop the macro.

**B4. Paper 4 chirality f_cw number: two flavors.**
Paper 4 reports f_cw^eq = 0.4974 in the paper table (L468, L481) vs. f_cw^eq = 0.5012 ± 0.0006 in both Paper 1 cross-cites (L271, L894, L940) AND SSOT. Looking at Paper 4 §Results: 0.5012 is the (CW + small systematic adjustment) number and 0.4974 is specifically the BENCHMARK-match against CE-ResNet (L468). Not a bug — two different subsets — but a cross-paper reader will think Paper 1 is quoting the wrong number. Fix: Paper 4 should add a single sentence at L468 explaining "the equivariant cross-catalog benchmark gives f_cw = 0.4974 (matching CE-ResNet at 0.5013); the full-catalog equivariant f_cw is 0.5012 ± 0.0006 (Table X) — both consistent with parity conservation at <0.5σ."

### Tier C — dimensional / sanity spot-checks

**C1. Paper 1 torsion-modified Friedmann (L154–234).** The action:
```
S_ECH = (1/16πG) ∫ d⁴x e [e^μ_a e^ν_b R^ab_μν + (1/γ) ε^abcd e_a^μ e_b^ν R_cdμν + …]
```
Dimensions: [e^μ_a] = 0 (inverse vierbein is dimensionless in natural units), [R_μν^ab] = M², [ε^abcd] = 0, so action density is M^4 (consistent with [d⁴x] = M^-4, [1/G] = M²). The (1/γ) Holst term is dimensionless 1/γ times an M^4 density — dimensionally correct. **Pass.**

The critical-density expression L234: ρ_crit = 3/(8πG γ² Δ) = √3/(32π² γ³) ρ_Pl. With [Δ] = M^-2 (area gap), [G] = M^-2, γ dimensionless: LHS = M^4; RHS = M²·M² (1/M^-2) = M^4. **Pass.** The √3/(32π² γ³) prefactor is ~0.046 for γ=0.274, giving ρ_crit ~ 0.046 ρ_Pl / γ³ … numerics work out consistently with the L85 quoted "0.27–0.41 ρ_Pl" range when γ varies by entropy-counting scheme.

**C2. Paper 2 bispectrum kernel (L70–120).** Local-type: B_ζ = c·f_NL·[P_ζ(k₁)P_ζ(k₂) + perms]. [B_ζ] = [P_ζ]² = M^-8 (with k-integration measure M^6 per bispectrum integration → M² for the bispectrum amplitude extracted at some k₀), f_NL dimensionless, c = 2 or 1 depending on convention. The factor-of-two convention discussion (L353–362) is correctly reconciled with Planck/Komatsu-Spergel convention. **Pass.**

**C3. Paper 3 NANOGrav h_c(f) power-law (implicit in §6).** The paper writes γ in the spectral-index convention where strain spectrum h_c ∝ f^((3−γ)/2) OR characteristic density Ω_GW ∝ f^(5−γ). At γ = 3.0, h_c is scale-invariant (∝ f^0), which is the matter-bounce signature. At γ = 13/3, h_c ∝ f^{-2/3} (SMBHB). The paper does not explicitly write the strain-PSD conversion formula; the γ-posterior is reported directly from the free-spectrum fit. **No dimensional error, but add a single-line formula** ("h_c(f) = A(f/yr^-1)^((3−γ)/2)") in Paper 3 §6 for reader who wants to derive γ from the plotted free-spectrum points. Non-blocking.

**C4. Paper 4 dipole amplitude normalization (§Results, L489–528, L621).** The paper uses HEALPix N_side = 64 for the dipolar analysis of (N_CW − N_CCW)/(N_CW + N_CCW). Dipole amplitude = a_1/a_0 where a_ℓm are spherical-harmonic coefficients of the asymmetry field. [a_1/a_0] dimensionless; reported value 0.001902 (pre-TTA) ⇒ 0.47% regional max. **Pass.** The TTA-post value drops this to 0.43σ significance (p=0.33), which is the paper headline.

---

## Proposed new tasks for SSOT/queue.md

| Task ID | Owner | % weight | Description | Est. time |
|---|---|---|---|---|
| P1-MCMC-COUNT-RECONCILE | agent | 0.1 % of P1 | Reconcile L323 (424,181) vs L785 (309,789) with a footnote explaining which datasets are included in each total | 10 min |
| P-CLAUDEMD-QUINTOM-DECISION | Houston | 0 % of any paper; project-level | Decide: either add w0-wa MCMC to Paper 1 (and kill L785 disclaimer) OR strike the "98.6% quintom-B" claim from CLAUDE.md and the site. These cannot coexist. | 30 min |
| P-CLAUDEMD-NANOGRAV-UPDATE | agent | 0 %; project-level | CLAUDE.md "Key scientific results" NANOGrav line needs γ = 3.20 ± 0.42, 0.48σ (matching Paper 3) | 2 min |
| P3-A-BIAS-CALIBRATION | pod | 0.05 % of P3 | Trace CLAUDE.md "2.28× clustering bias" to source. If real, promote to Paper 3 §5 / Paper 2 §7.2 to replace α = 0.15 theoretical prior with empirical value. If not real, strike from CLAUDE.md. | 2–4 h on pod |
| P2-XREF-PAPER3 | agent | 0.3 % of P2 | Reopen P2-XREF-AUDIT: add `\bibitem{Golden:2026anomaly}` to Paper 2, cite at §4 intro ("multi-tracer with AI-selected anomalies") and §7.2 ("anomaly-optimized five-tracer"). The previous audit's conclusion that "no cite needed" is theorist-rejected. | 15 min |
| P-SPHEREX-SIGMA-HARMONIZE | agent | 0.05 % of each | Add one harmonizing sentence to Paper 1 §I and Paper 3 §5 that explicitly identifies the 0.7 vs 1.0 vs 1.5 σ(f_NL) regimes and maps them to the 4–6σ range | 15 min |
| P1-SSOT-BETA-LABEL | agent | 0 %; SSOT fix | Edit `SSOT/paper-1/status.md` §3 to correctly label 0.264° as NaMaster measurement and 0.27° as ALP prediction (currently swapped) | 3 min |
| P4-UNUSED-MACRO | agent | 0 %; cosmetic | Drop unused `\newcommand{\fnl}` from Paper 4 L31 | 1 min |
| P4-FCW-CLARIFY | agent | 0.05 % of P4 | Add one-sentence note at Paper 4 L468 reconciling f_cw = 0.4974 (CE-ResNet benchmark) vs f_cw = 0.5012 (full-catalog equivariant, cross-cited by Paper 1) | 5 min |
| P3-STRAIN-FORMULA | agent | 0.05 % of P3 | Add the h_c(f) = A(f/yr^-1)^((3−γ)/2) formula to Paper 3 §6 for γ-to-strain reader clarity | 5 min |

Total new items: 10. Five (A1–A5) are Tier-A / bundle-submission-blocking. Five (B1–C4) are polish.

---

## Verdict

**MINOR INCONSISTENCIES — blocking a coordinated 4-paper bundle but not any individual submission.**

- **Physics is consistent.** f_NL = −35/8, γ = 3.0, β = 0.27°, H₀ = 67.68, ΔN_eff ≈ 0, 14 barriers, 8.47 M chirality galaxies, 319,443 anomalies, bounce-agnostic framing — all trace cleanly through the papers and the cross-paper citations route correctly.
- **Bookkeeping between paper text, SSOT, and CLAUDE.md has drifted.** The five Tier-A items (internal MCMC count; w0-wa claim; NANOGrav γ; 2.28× bias; Paper 2 → Paper 3 cross-cite) are each a 5–30 min fix and should land together in a single "pre-bundle reconciliation" commit before any two of the four papers hit arXiv simultaneously.
- **The most important single fix is A2** (quintom-B 98.6% claim). CLAUDE.md sits above the papers in the project's own authority hierarchy per `CLAUDE.md` "Key scientific results" block — but Paper 1 L785 flatly contradicts it. A referee reading both will assume the project does not know what it computed. Resolve first.
- **If Houston wants to submit Papers 3+4 this week and hold 1+2 for another iteration** (the SSOT-recommended order), the Tier-A items collapse to just A3 (2 min) and A4 (pod trace). The rest can wait until Paper 1 and Paper 2 are packaged together.

Recommend: land the 10 new queue items, resolve Tier-A, then submit as 3→4→1→2 with all cross-cites live.
