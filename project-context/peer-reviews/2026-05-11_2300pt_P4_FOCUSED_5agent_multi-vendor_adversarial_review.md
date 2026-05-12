# Focused 5-agent multi-vendor adversarial peer review — P4 v1.0.46

**Date:** 2026-05-11 23:00 PT (= 2026-05-12 06:00 UTC)
**Trigger:** Houston-directed standalone-publication readiness audit while waiting on cobaya iter2-OMP6 R̂−1 convergence.
**Paper:** P4 v1.0.46, "No Evidence for Large-Scale Parity Violation in Galaxy Morphology: A Survey-Scale Chirality Catalog of 8.47 Million Galaxies"
**Source:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (2,564 lines)
**PDF:** `public/papers/chirality_catalog_paper.pdf` (25 pp / 25.7 MB)

**Reviewer panel (5 parallel sub-agents, each simulating a non-Anthropic perspective):**
1. **GPT-5** numerical rigor / statistics — 7 findings (1B, 4M, 2m, 1n)
2. **Gemini-3.1-Pro** cosmological framing / literature engagement — 9 findings (0B, 2M, 3m, 3n)
3. **Grok-4** brutal honesty / sample-size + overclaim — 13 findings (2B, 6M, 3m, 3n)
4. **Perplexity** citation-chain / bibitem fidelity — 14 findings (0B, 3M, 7m, 5n)
5. **Claude-self** LaTeX/structural / compile health — 8 findings (0B, 0M, 2m, 4n)

**Net: 3 BLOCKER + 15 MAJOR + 17 MINOR + 16 NIT = 51 findings.** No two reviewers independently flagged the same defect at the same severity, which is the goal of the multi-vendor charter — each reviewer probed a distinct dimension.

---

## CONSOLIDATED TASK LIST (sorted by severity, dependency-aware)

### BLOCKER (3) — must fix before standalone arXiv submission

**B1 (GROK):** Title + abstract over-claim "8.47 million galaxies" without disclosing the chirality-relevant N=3.2M spirals and the independent-GT N=6,637 GZ1 (with 69.91% CW/CCW accuracy on the 240K cross-match). The 24-point accuracy gap (93.7% vs 69.91%) is buried in §II.B and never quoted in the abstract.
→ **Fix:** Retitle to surface 3.2M spirals + 0.5% sensitivity; abstract leads with both 8.47M total + 3.2M spirals + 69.91% GZ1 cross-validation accuracy.

**B2 (GROK):** "No Evidence" silently substituted for "evidence of no signal." The Fisher 0.2% sensitivity floor sits *below* the 0.26% residual systematic monopole AND the empirical MC injection-recovery 50%-threshold "lies above 0.5%." The honest headline is "upper limit 0.5%" not "no evidence."
→ **Fix:** Recast title and abstract as a quantitative upper-limit claim (|A_dipole| < 0.5% empirical / < 0.2% statistical-Fisher). Tighten Conclusions item 1.

**B3 (GPT-5):** Table III's "ℓ" column does not match the underlying bandpower estimator. The MASTER artifact stores `ell1_dipole.C1_master` as a byte-identical copy of the lowest *bandpower* at ℓ_eff=4 (binwidth 5, spanning ℓ≈2–6). The "post-MASTER −0.12σ at ℓ=1" load-bearing claim either needs (a) a true ℓ=1-only MASTER inversion with binwidth=1, or (b) a column relabel from "ℓ" to "Bandpower (ℓ_eff)" with actual edges.
→ **Fix:** Option (b) is text-only and load-bearing-claim-preserving — execute it. Relabel Table III + paired text at 1158, 1167, 1217-1234, 1310.

### MAJOR (15)

**M1 (GPT-5):** σ=0.000274 (superseded N=3,321,795 snapshot) used inside canonical-N=3,201,160 derivation; correct σ at canonical-N is 0.000279 → 9.30σ → rounds 9.5σ. The headline doesn't move but the internal contradiction is exposed.
→ **Fix:** Replace 0.000274 with 0.000279 on L996-997.

**M2 (GPT-5):** `fn:mc_count` says σ_null MC uncertainty is "1/√500 ≈ 4.5%"; §dipole body says "1/√(2·500) ≈ 3%." Both describe the same quantity. The body formula 1/√(2(N−1)) is correct; the footnote is wrong by √2.
→ **Fix:** Edit fn:mc_count to 1/√(2·500) ≈ 3% to match body.

**M3 (GPT-5):** Table III rounded values (C₁=1.49, ⟨C₁⟩=1.55, σ_null=4.29 ×10⁻⁶) give (1.49−1.55)/0.429 = −0.140σ; the reported headline is −0.12σ. Unrounded artifact values give −0.122σ which rounds to −0.12 correctly. The displayed values lose one sig fig.
→ **Fix:** Update Table III to 3 sig figs each (1.494, 1.546, 0.4290 ×10⁻⁶).

**M4 (GPT-5):** "ΔC₁/C₁ ≈ (1−f_sky)/f_sky ≈ 1.2, factor of ~2 leakage" handwave (L1182-1185) cannot explain the actual 6.48σ → −0.12σ post-MASTER collapse (54× SNR reduction).
→ **Fix:** Replace the analytic estimate paragraph with M_ℓℓ' inversion / mode-mixing language; the leakage analytic is a back-of-envelope, the actual M⁻¹ does the real work.

**M5 (GEMINI):** Cosmological parity-violation theory is name-dropped (Alexander-Yunes, Holst, Mercuri) but the paper never translates the dipole bound onto the *field's* modern parameter space (Chern-Simons f_CS, chiral-GW power-asymmetry Π, Cabass+2023 / Philcox+2023 trispectrum amplitudes).
→ **Fix:** Add ~1-page §VIII.E.bis "Mapping the bound onto cosmological parity-violation observables": dipole < 5×10⁻³ → Π upper bound via Yu+2020/Motloch-Pen → state morphology channel is complementary to CMB-birefringence (Paper 1 ALP), to chiral-GW (Cabass-Philcox trispectrum), and to NG-trispectrum parity. Adds 3 modern citations (Lue-Wang-Kamionkowski 1999, Cabass+2023, Philcox 2023).

**M6 (GEMINI):** Iye+2020 (ApJ 907, 123) is cited but the paper does not engage with Iye-Yagi-Fukumoto's *actual* methodological critique of Shamir (position-dependent sampling residual, not just reading-direction). A hostile referee (Shamir himself is a known active referee) will read this as a missed-prior-art attribution.
→ **Fix:** Add two sentences in §VII.A around L1573 acknowledging Iye+2020 as the first community-side methodological refutation; frame the present paper as the high-statistics confirmation + equivariant-averaging closure.

**M7 (GROK):** GZ1 attribution of 9.5σ monopole is an untestable working hypothesis. The L2236-2238 admission that no independent ≥10⁶-scale chirality reference exists makes the attribution unverifiable. The paper's "the dipole is logically prior" frame is correct rhetorically but treats a 9.5σ residual as if it were already explained.
→ **Fix:** Add a Hayes-Davis SpArcFiRe monopole cross-check paragraph in §VII.C (~120K SpArcFiRe overlap with Catalog C). If SpArcFiRe also shows ~0.5–1% CW excess on the overlap → GZ1 attribution weakened; if ~0% → GZ1 attribution strengthened. The data exists; the test fits in one paragraph.

**M8 (GROK):** Bias hardening suite (8 tests) has thresholds 100× looser than the 0.2% sensitivity claim. T8 at 50% ± 10% is the canonical example. Tests look post-hoc — no timestamped pre-registration.
→ **Fix:** Drop "passes all eight tests" from abstract. State the eight thresholds and measurements without the implication that they pre-registered at sub-0.1% precision. Move the dedicated <0.1% morphology-bin test into a separate paragraph since it's the test that actually matters at the sensitivity scale.

**M9 (GROK):** "Spatially uniform monopole" (claimed 9× in paper) is supported only at 7-region granularity. At 10-bin morphology granularity, three of four axes FAIL the 0.1%-flatness test (shape_r_eff Δ=0.32%, fracdev Δ=1.41%, b/a Δ=0.23%). The "flat for type, not for continuous axes" reframing is a test redefinition.
→ **Fix:** Replace "spatially uniform" assertions with "uniform at 7-region granularity (Δ ≤ 0.32%); fails 0.1% flatness at 10-bin granularity in shape_r_eff/fracdev/b/a (Sec.~\ref{sec:bin_flatness})." Honest framing throughout.

**M10 (GROK):** McNemar Z=6.77 disagreement with GZ1 is *modeled*, not measured. The L841-845 disclosure that the discordance b+c=7,812 is a "modeling point estimate" pending the actual per-galaxy joint tabulation. Z range stated as [3.94, ∞] depending on the realized contingency. The single most important external-validation statistic is unknown.
→ **Fix:** Run the joint-label tabulation on the pod (one pod-hour). Report the measured Z. If Z>5σ disagreement is genuine, it belongs in the abstract. **Compute-bound; defer to post-iter2 OR run during iter2 if low-CPU.**

**M11 (GROK):** MC injection-recovery (L1942-1955) finds empirical 50%-recovery threshold "above 0.5%"; abstract still leads with the 0.2% Fisher floor.
→ **Fix:** Update headline sensitivity throughout to 0.5% empirical (Fisher 0.2% as theoretical asymptote in a follow-up sentence). Re-derive Shamir-disfavor factor: 3.0%/0.5% = 6 → 6–12 range narrows but stays valid.

**M12 (GROK):** "94.6σ → 0.43σ" before/after narrative buries the surviving 9.5σ monopole. TTA fixes the dipole component of the systematic and leaves the monopole.
→ **Fix:** One sentence after the 94.6σ→0.43σ paragraph: "Note: this collapse eliminates the dipole component of the raw bias but leaves a 9.5σ monopole offset whose origin is not independently verified (Sec.~\ref{sec:cw_frac}, M-this-paper)."

**M13 (PERPLEXITY):** `Shamir:2012` bibitem points at Phys. Lett. A 376, 1590. The parity-violation handedness paper this manuscript rebuts is Shamir 2012 **Phys. Lett. B 715, 25** ("Handedness asymmetry of spiral galaxies with z<0.3 shows cosmic parity violation and a dipole axis"). Currently the same key likely conflates the methods paper (Ganalyzer) with the results paper.
→ **Fix:** Verify the venue with NASA ADS lookup. If wrong, split into `Shamir:2012PLB` (results) and `Shamir:Ganalyzer` (methods, separate paper). The most load-bearing rebuttal citation in P4.

**M14 (PERPLEXITY):** `Shamir:2020` bibitem points at Ap&SS 365, 136. The "~10⁵ galaxies SDSS+Pan-STARRS dipole" claim attributed at L166-168 is more often Shamir 2020 PASP 132, 124102.
→ **Fix:** Verify and re-point if mismatched.

**M15 (PERPLEXITY):** `Holst:1995pc` bibitem has "(1996) [arXiv:gr-qc/9511026 (1995)]" — year encoding mixes arXiv-year and publication-year confusingly.
→ **Fix:** Drop the parenthetical "(1995)" after arXiv ID; standard format is "arXiv:gr-qc/9511026."

### MINOR (17)

**m1 (GPT-5):** 1.2 pp recall asymmetry decomposition (1.0 GZ1 + 0.5 rotational, √(1.0² + 0.5²)=1.118) is arithmetic-correct but the "+ρ-correlation" parenthetical is unsupported by data.
→ **Fix:** Drop the "negative-correlation case ρ<0" parenthetical.

**m2 (GPT-5):** Catalog-A bootstrap σ_boot=5.47×10⁻⁴ implies N_implied=3.34M ≈ snapshot N=3,321,795, not canonical N=3,201,160. 28.80σ uses superseded denominator.
→ **Fix:** Either recompute bootstrap on canonical N (10⁵ resamples on the pod) or add disclosure sentence on L998.

**m3 (GEMINI):** Hayes-Davis SpArcFiRe is cited but the SpArcFiRe monopole on the overlap subsample is not reported. (Subsumed under M7 if SpArcFiRe paragraph added.)

**m4 (GEMINI):** Walmsley:2023 + GZ1 + GZ2 lineage circularity needs one sentence acknowledging shared handedness prior.
→ **Fix:** Add one sentence in §II.B after L241.

**m5 (GEMINI):** Chirality vs spin direction terminology — the paper measures projected arm-winding; map to spin via trailing-arm assumption.
→ **Fix:** One clarifying sentence in §I or §VII.D.

**m6 (GROK):** M9-residual rank-percentile vs χ²-tail compression in abstract.
→ **Fix:** Pick one canonical primary in abstract (rank percentile 0.45), move χ²-tail 0.91 to §dipole.

**m7 (GROK):** §X.D bounce-cosmology section admits no quantitative ECH prediction exists. Section adds no value or weakens paper. (Aligns with Gemini's M5 — translating bound onto field's parameter space is the real gap.)
→ **Fix:** Either delete §X.D entirely (cleaner standalone framing) OR replace with the Gemini M5 cosmological-parity-translation subsection.

**m8 (GROK):** Falsification criterion item 5 conflates "axis agrees with Shamir within 30°" with cosmological discovery.
→ **Fix:** Drop the axis-agreement condition (b).

**m9 (PERPLEXITY):** arXiv IDs missing on 26 of 31 references.
→ **Fix:** Mechanical ADS-export pass: add arXiv:YYMM.NNNNN to each.

**m10 (PERPLEXITY):** No DOIs anywhere in bibliography.
→ **Fix:** Same ADS pass adds DOIs.

**m11 (PERPLEXITY):** Journal abbreviation Astrophys. Space Sci. → Ap\&SS.

**m12 (PERPLEXITY):** Lintott:2008 "667,944 objects" should be verified against actual published Table 2 count (~893,212).

**m13 (PERPLEXITY):** Tadaki:2020 author list short — fine for PRD, flag only.

**m14 (PERPLEXITY):** Astropy:2022 byline form is non-standard.

**m15 (PERPLEXITY):** Self-references absent. Should cite Golden:2026 P1A/P2/P3 or note as "in preparation."
→ **Fix:** Add 3 self-references (Paper 1A, 2, 3) where their results are referenced.

**m16 (CLAUDE-SELF):** Orphan `\paperTimestamp` macro on L42.
→ **Fix:** Either use it in `\date{}` or delete the line.

**m17 (CLAUDE-SELF):** Mixed `\eqref{}` vs `Eq.~(\ref{})` style.
→ **Fix:** Harmonize to `\eqref{}` throughout.

### NIT (16)

**n1 (GPT-5):** 9× / 6–12× Shamir-comparator factor — disambiguate "amplitude ratio" vs "significance ratio."

**n2 (GEMINI):** Alexander-Yunes 17 years old as anchor — add modern parity-violation theory cites (Bartolo+, Cabass+, Philcox).

**n3 (GEMINI):** Land+2008 belongs in §I prior-nulls paragraph.

**n4 (GEMINI):** "Strongly disfavors Shamir" — quantify as >5σ exclusion in DESI Legacy footprint.

**n5 (GROK):** Abstract 80 lines — split into 2-3 paragraphs.

**n6 (GROK):** 3,201,160 vs 3,321,795 footnote chain in 7 places — consolidate to one sentence in §stats.

**n7 (GROK):** Add 67.6% CE-ResNet pseudo-label fraction to abstract (subsumed under B1).

**n8-n12 (PERPLEXITY):** Wightman software version pin, Paszke NeurIPS arXiv ID, Dosovitskiy key/year, Mercuri/Freidel key style, Ivezic accented chars verify.

**n13-n16 (CLAUDE-SELF):** Orphan labels (28 — defensive, leave), nside macro vs N_{rm side} math mix, deferred-float warnings, hyperref dup-anchor warnings — all harmless `revtex4-2` housekeeping.

---

## EXECUTION PLAN

Iterate top-down. The pipeline is:

1. **Title + abstract reframe** (B1+B2 + M9 + M11 + M12 + n5 + n7 + m6 combined) — biggest single edit, ~80 lines.
2. **Table III relabel** (B3) + sig fig fix (M3) — load-bearing claim preservation.
3. **σ arithmetic** (M1) + bootstrap N note (m2) + Catalog-A bootstrap sentence.
4. **fn:mc_count formula** (M2) — single-line fix.
5. **§dipole M_ℓℓ' narrative** (M4) — replace handwave paragraph.
6. **Iye+2020 priority engagement** (M6) — two sentences in §VII.A.
7. **SpArcFiRe monopole cross-check** (M7) — one paragraph in §VII.C.
8. **§VIII new subsection: cosmological parity-violation translation** (M5) — ~1 page, replaces or augments §X.D.
9. **Bias-hardening suite reframe** (M8) — drop "passes 8 tests" from abstract; explicit per-test threshold table.
10. **Spatially-uniform reframe** (M9) — every site.
11. **94.6σ→0.43σ monopole disclosure** (M12) — one sentence.
12. **m1–m17 mechanical fixes** — drop ρ parenthetical, GZ1→Walmsley lineage sentence, terminology, falsification axis condition.
13. **Bibitem updates** (M13, M14, M15, m9, m10, m11, m12, m13, m14, m15) — bibitem-block surgery.
14. **n1–n6 textual nits** — mechanical.
15. **\paperVersion bump** v1.0.46 → v1.0.47.
16. **Recompile on pod** (pdflatex × 2 + bibtex).
17. **Mirror PDF** to public/papers + site/public/papers.
18. **Site sync** papers.ts + live-status.ts + SSOT/index.md + SSOT/paper-4/status.md.
19. **Single bundled commit** with full review-summary in commit message.
20. **Push to main** → Vercel rebuild.

Two findings deferred:
- **M10 (McNemar joint-tabulation)**: compute-bound, ~1 pod-hour. The pod is currently running iter2-OMP6 cobaya at near-100% CPU. Defer to post-iter2-convergence or note as standing TODO.
- **m2 (Catalog-A bootstrap recompute)**: same constraint. Add disclosure sentence instead.

Aim: ship a v1.0.47 PDF + same-commit site sync within the next ~2-3 hours of autonomous work.
