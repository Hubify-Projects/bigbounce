# R53 P1A — Truth Audit (per-paper convergence pass)

**Date:** 2026-06-26
**Paper:** P1A — Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes
**Source:** `arxiv/paper1a_ech_nogo.tex` (compiled v1A.0.79, PDF md5=1996d408, 29 pp)
**Vendor legs returned:** Grok 4.3 (REJECT), Gemini 2.5 Pro (MAJOR), OpenAI gpt-5 high+pass2 (MAJOR), Claude/Opus reviewer leg (this audit). **Failed:** Perplexity (quota-dead 401, expected).

Prior state: R52+EXT21/22 polish-tier, 0 BLOCKER / 0 genuine MAJOR. Calibration applied: pattern-061 (judge by in-text recommendation), -063 (math/extraction-artifact default FALSIFIED until checked vs .tex), -062 (already-fixed checks), -064 (Grok harsh-outlier per-reason audit); June-2026 dating valid; arXiv 25xx/26xx valid; companion placeholders + DOI deferral deliberate (HOUSTON-DECISION).

## Independent arithmetic re-verification (Claude leg + gpt-5 leg, concur)
All recomputed and CONSISTENT: NJL ρ≈4e-81 eV⁴ ≈ 4e-69 ρΛ (~69 OOM below); R2 ratio ≈10⁻⁶⁰; R4 ρθ=1.6e-10 eV⁴ ≈ 6 ρΛ at mθ=H0 (α/M=10⁻²¹ GeV⁻¹=10⁻³⁰ eV⁻¹); overshoot 22/36 OOM; ACT-vs-WMAP+Planck 1.06σ; γ_PTA offset 1.13σ; f_NL/σ=6.25; LiteBIRD 0.73σ/0.77σ/2.4σ; Barrier-12 ceiling 0.07–0.17; N_tot=92 vs App-B 94 (~2%); e³²≈7.9e13; ρcrit 0.27/0.41 ρPl at γ=0.274/0.2375; App-C WKB (α/M)φ'~10⁻³⁵ eV vs k~6e-4 eV (~30 OOM). **Zero arithmetic/derivation defects** (gpt-5's high-effort methodology leg explicitly confirms each).

## Verdicts

### VERIFIED (closed this round)
- **R53-V1 (MINOR, internal inconsistency; Gemini E3 + gpt-5 E8, convergent).** Abstract (L710-711) and Conclusions (L2938) grouped "R1–R3 ... under explicitly-labeled scaling ansätze," contradicting body §IV intro (L1545: "standard torsion-elimination derivation for R1 ... ansatz-level amplitude budgets for R2–R3") and Theoretical Implications (L2696: "R1 closes via the standard published derivation; R2–R3 close ... under explicitly-labeled scaling/ansatz assumptions"). Pattern-008 downstream-prose-after-physics class.
  - **Closure:** abstract L710-711 → "R1 (NJL contact) is amplitude-suppressed by a standard torsion-elimination derivation, while R2–R3 ... under explicitly-labeled scaling ansätze"; conclusions L2938 → "Route R1 closes at the amplitude level via a standard torsion-elimination derivation; Routes R2–R3 close ... under explicitly-labeled scaling ansätze." Grounded in existing body text; no fabrication; makes abstract MORE accurate (R1 closure is standard, not ansatz-dependent).

### FALSIFIED (training-prior / extraction / already-present)
- Grok E2, Gemini m1, gpt-5 (implicit): "future date June 19 2026" — FALSE POSITIVE, June 19 is 7 days BEFORE today (2026-06-26). Training-cutoff prior.
- Gemini N2: "arXiv 2603.13924 future date" — FALSIFIED, 2603 = 2026-03, before today. Gemini self-corrects 2509→2025 mid-finding.
- gpt-5 m3/m10: "Domaga la / Pop lawski spacing" — extraction artifact (pattern-063); source uses `\l{}` (Polish ł); renders correctly in PDF.
- gpt-5 E9: "Eq.(1) action mathematically inconsistent (T² + variation double-counts)" — FALSIFIED; footnote+body (L1019-1044) state T·T is on-shell Hehl–Datta shorthand, NOT independently varied; connection variation on EC-Holst+Dirac alone. Standard, correct.
- gpt-5 E10: "App C cross-refs companion §VI, unverifiable" — FALSIFIED; L3252-3253 footnote: "self-contained within App. mcs_derivation; no companion result is required." β mapping derived in-paper (Eq. beta_derived).
- gpt-5 M6: "add explicit ε^μνρσR_μνρσ=0 contraction" — already present L2451-2453.
- gpt-5 M2: "Fig 3 ΔH/H is parameter-choice not ECH" — already disclosed in caption (L1230-1255, EXT7 F67-B1 closure).
- gpt-5 M8: "consolidate N_tot 92 vs 94" — already done, App-B "Sharper dependency statement" L3116-3134 (N_tot=92±2).
- gpt-5 m5: "cω ω² conversion not shown" — present in Fig-5 caption L1242-1244.
- gpt-5 m1: "n_psi=10² cm⁻³ exceeds cosmic mean" — FALSIFIED; n_b at z~1100 ≈ 270 cm⁻³, so ~10² is correct post-recombination baryon density; also valid dense-ISM. Strengthens bound regardless.

### STALE / HOUSTON-DECISION (deliberate design)
- Grok E1, Gemini E2, gpt-5 E1/E4/E5/E6: "in-prep companions load-bearing, not self-contained" — STALE; abstract+§I (L985-993) explicitly: "none of these companion-imported numerical values is used in the channel-level closure proof or the 13 barriers; the structural closure rests on dimensional/operator-counting/perturbation-transparency arguments alone." Deliberate companion-placeholder design, closed repeatedly EXT1–EXT22.
- gpt-5 E3, Gemini m4, gpt-5 m4 (PACS): Zenodo DOI / "will pin" / PACS removal — HOUSTON-DECISION submission-prep (HD-4/HD-11); DOI inserted at submission.

### OPINION (framing/polish; no correctness defect)
- Grok E3/M3/M4, Gemini E1/M1: abstract conditional/ansatz framing, title rewrite, "define channel-level closure," barrier classification — already extensively caveated in abstract/§I/§IX/App-B; requested content present. Title change subjective.
- Grok M1, gpt-5 M10/m11: "7 Foundations are modeling assumptions, classify barriers" — §IX "Constraint classification" para (Novel/Known/Structural) already does this.
- Grok M2, Gemini E3(p2), gpt-5 M12: Fig 4/7 ρ-family covariance — ρ defined in captions; ρ=0 baseline + ρ>0 sensitivity bands ARE the requested sensitivity; joint forecast is companion's.
- gpt-5 E2/M1: Route-2 derivation step-by-step / SPHEREx degradation table — anomaly chain in footnote, degradation chain in fn:spherex_range; labeled amplitude-budget bound, not derived prediction.
- gpt-5 E7/M13: R4 error propagation / Δφ–ρθ derivation — regime of validity (mθ≲H0) stated L1914-1916; central value confirmed by gpt-5's own recompute.
- gpt-5 E8/E11, Gemini M2: "definitively erased" / mark theorem-vs-heuristic in abstract — "definitively" is defensible on the e³² scale-history argument and the body consistently qualifies it as "scale-history bookkeeping, not the transfer-function calculation" (L2900); the theorem/ansatz/heuristic split exists in body §IV/§IX/§XII. R1/R2-R3 sub-point closed as R53-V1.
- gpt-5 M3: Barrier-12 ceiling — explicitly labeled "order-of-magnitude ceiling ansatz (not derived); used only as a global ceiling."
- gpt-5 M4/M11/m7: cal-F vs F_μν — disambiguation note already at L1162-1164.
- gpt-5 M5/M7: one-loop α/M numeric steps / M=MPl/√γ constant — steps shown L1181-1185; M is OOM-labeled "up to numerical constants."
- gpt-5 M9: Fig-5 RG-running panel looks computed — figure-presentation; α/M treated phenomenological throughout; would need figure regen (OUT-OF-SCOPE for text round).
- gpt-5 M14: reheating washout "instantaneously ≃0" too strong — already fully conditionalized ("if Γ_wash>H ... then"; "a condition rather than a result"; Boltzmann calc deferred).
- Grok N1/N2, gpt-5 m2/m6/m9/n1/n2: glossary, fine-tuning convention footnote, Fig-1 PTA "external" tag, WKB mθ≪H0 clause, caption cross-ref phrasing — optional polish; content present or non-load-bearing.

### OUT-OF-SCOPE (needs new compute/data — TRULY-BLOCKED)
- Gemini M2, gpt-5 E11: full 4-epoch transfer-function suppression calc — deferred to Paper II; paper explicitly presents "scale-history bookkeeping, not the transfer-function calculation" (L2900). New forecast compute.

## Net verdict
**P1A CONVERGED.** 1 NEW VERIFIED item this round (MINOR, abstract/conclusions R1-grouping internal inconsistency), closed by surgical body-grounded edit. 0 BLOCKER, 0 genuine MAJOR survive truth-audit. Grok REJECT = pattern-064 harsh-outlier (future-date false positive + already-addressed companion concern). Gemini/gpt-5 MAJOR verdicts driven entirely by the recurring (deliberate) companion-in-prep + DOI-deferral theme + framing opinions; gpt-5's high-effort arithmetic recomputation confirms zero numerical defects.
