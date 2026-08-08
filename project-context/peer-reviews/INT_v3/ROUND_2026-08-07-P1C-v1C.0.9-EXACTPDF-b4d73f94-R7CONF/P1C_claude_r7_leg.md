# P1C v1C.0.9 — Claude INT leg, R7 confirmation round

- **Role:** Independent skeptical journal referee (CQG calibre), Claude leg of the R7 confirmation board. Fresh review; no prior-round context consulted.
- **Manuscript:** `arxiv/paper1c_nogo_survey/main.pdf` (20 pp., "A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and Bounce Phenomenology", dated August 6, 2026, v1C.0.9)
- **SHA-256 (verified before reading):** `b4d73f94621035ebf5f2e724e714c2f19283835748c7c577905a4e02cf890c47` — MATCH
- **Review date:** 2026-08-06 (round label 2026-08-07)
- **Scope reviewed:** mathematical correctness of every checkable displayed equation (incl. Appendices A–E derivation chains), internal consistency, scope honesty, citation integrity, presentation blockers.

## VERDICT: MINOR-REVISIONS (0 MAJOR / 8 MINOR — all findings are wording, notation, or presentation; every independently recomputable equation and numeric checked out)

---

## Independent verification log (what was recomputed and confirmed)

All of the following were recomputed from scratch and **agree** with the manuscript:

1. **Eq. (2) Route-2 budget (p. 7).** α_em/4π = 5.81×10⁻⁴ ("more precisely 5.8×10⁻⁴", rounded up to 10⁻³ — conservative direction correctly identified); H₀/M_Pl ≈ 1.2×10⁻⁶¹; M_Pl·(α/M) = 1.22×10¹⁹ GeV × 10⁻²¹ GeV⁻¹ ≈ 10⁻²; β_obs = 0.342° = 5.97×10⁻³ rad ✓. Canonical contraction 10⁻³·10⁻⁶¹/(10⁻²·6×10⁻³) = 1.7×10⁻⁶⁰ ✓; direct contraction (α_em/4π)(H₀/M_Pl)/β_obs ≈ 2×10⁻⁶² ✓ (two additional orders; quoting 10⁻⁶⁰ is indeed the conservative side). 60−2 = 58 (≥58 claim) ✓; "inflate ten orders → ≳48" ✓.
2. **Eq. (3) chiral-count integration (p. 8).** 12π² = 118.4; ln 10¹⁶ = 36.8, ln 10¹³ ≈ 30 ✓; Δγ/γ = 30–36.8/118.4 = 0.253–0.311 ✓; 32/(12π²) = 0.270 ✓.
3. **Eq. (4) Benedetti–Speziale flow integration (p. 8).** Integrating μ∂γ²/∂μ = −(γ²−1)(μ²κ̃²/(8π)²)(23γ²+5) with κ̃² = 16π/M_Pl², γ = 0.24, μ_UV = 10¹⁶ GeV, full M_Pl = 1.22×10¹⁹ GeV: Δγ² = [(1−γ²)(23γ²+5)/(64π²)]·(16π μ_UV²/M_Pl²)/2 = 1.6×10⁻⁷, so |Δγ/γ| = Δγ²/2γ² = **1.38×10⁻⁶** — matches the quoted 1.4×10⁻⁶ exactly. Frozen-coefficient (μ_UV/M_Pl)² = 6.7×10⁻⁷ same order ✓. γ² = 1 zeroes the RHS (fixed point) ✓; UV-attractive for γ²<1 given the −(γ²−1) sign ✓.
4. **Route-3 margins.** 0.3×1.2×10⁻⁶¹ ≈ 3.6×10⁻⁶² ("≈3×10⁻⁶²") → ~61 orders; 1.4×10⁻⁶×1.2×10⁻⁶¹ = 1.7×10⁻⁶⁷ → ~67 orders. Abstract's "61–67, ~67 from derived flow / ~61 from pessimistic bound" endpoint attribution is the right way round ✓.
5. **Shapiro–Teixeira ratio (p. 6).** |Ω₄₄/α₄| = [(378+783γ²)/20(1+γ²)²]/[6/(1+γ²)] = (378+783γ²)/[120(1+γ²)] ✓; at γ = 0.24 evaluates to 3.33 ("≈3.3") ✓. (4π)² = 16π² ✓.
6. **B12 LQC endpoints (p. 5).** ρ_crit = √3/(32π²γ³)ρ_Pl: γ = 0.2375 → 0.409 ("0.41") ✓; γ = 0.274 → 0.267 ("0.27") ✓; squares 0.073–0.168 ("0.07–0.17") ✓.
7. **Appendix A arithmetic.** [α/M] = −1, [εeeF] = +2 → +1, three units short of +4 ✓ (consistent with Eq. (6) discussion p. 10–11). (α/M)M_Pl⁵ = 1.22×10⁻² M_Pl⁴ ✓ (Eq. A2). M_Pl⁴/ρ_obs = (1.2209×10²⁸ eV / 2.25×10⁻³ eV)⁴ = 8.65×10¹²² ("8.7×10¹²² ≈ 10¹²³") ✓. N_tot = 122 ln10/3 = 93.6 ("≈94") ✓; 10¹²² vs 10¹²³ shift = ln10/3 ≈ 0.77 e-folds ("≈0.8") ✓; Case-II 10⁻² endpoint → 92.1 (the disclosed 92-vs-94 spread) ✓.
8. **Appendix C Fierz.** Eq. (C1) is the standard normalized Fierz matrix; I verified F_c² = 𝟙 by direct row-column multiplication (rows 1, 3, 4 checked; diagonal 1, off-diagonal 0) ✓. Fourth row ¼(−4,−2,0,−2,4) = (−1,−½,0,−½,1) ✓; F_op = −F_c row (1,½,0,½,−1) reproduces Eq. (C2) (J⁵·J⁵) → SS + ½VV + ½AA − PP ✓. Cross coefficients F_VA^op = F_AV^op = ½ ✓. (F_c)_AS = −1 → (F_op)_AS = +1 → G_s = −3κ/16 ✓.
9. **Appendix E.** Eq. (E1): (⋆+γ⁻¹𝟙)·γ²/(1+γ²)(γ⁻¹𝟙−⋆) = γ²/(1+γ²)·(γ⁻²−⋆²) = 𝟙 using ⋆² = −𝟙 ✓. Eq. (E3): κ = 8πG ⇒ 4πG = κ/2 and (3/2)πG = 3κ/16 ✓; γ→∞ recovers −3κ/16 ✓. Eq. (E4) matches the Sec. II operator −(3κ/16)[γ²/(1+γ²)](J⁵)² ✓. Eq. (E5): n = 100 cm⁻³×(1.9733×10⁻⁵ eV·cm)³ = 7.68×10⁻¹³ eV³; κ = 8π/(1.2209×10²⁸ eV)² = 1.69×10⁻⁵⁵ eV⁻²; κn² = 9.96×10⁻⁸⁰ ≈ 1.0×10⁻⁷⁹ eV⁴ ✓; /(2.3 meV)⁴ = 2.80×10⁻¹¹ eV⁴ → 3.6×10⁻⁶⁹ (68.4 orders) ✓; ×3/16 → 1.9×10⁻⁸⁰, 6.7×10⁻⁷⁰ ✓; under (2.25 meV)⁴ → 3.9×10⁻⁶⁹ ✓ — all three cross-quotes (Sec. II p. 2, Table II R1, App. E) mutually consistent.
10. **Torsion-square identity (pp. 12, 16).** S_abc S^abc = (1/16)ε_abcd ε^abce J⁵ᵈJ⁵ₑ = −(3/8)(J⁵·J⁵) using ε_abcd ε^abce = −3!δ_d^e (mostly-plus) ✓. Nieh–Yan identity d(e_I∧T^I) = T_I∧T^I − e_I∧e_J∧R^IJ ✓ standard. Check A (ε^μνρσ R_μνρσ = 0 from R_μ[νρσ] = 0) ✓ standard.
11. **Dimension bookkeeping Eq. (1) (p. 6).** [ϑ_NY] = +1, [∂ϑ] = +2, [J⁵] = +3, prefactor −1: −4−1+2+3 = 0 ✓. ∂ϑ ~ H₀² ≈ 2×10⁻⁶⁶ eV² ✓. Table III prefactor/bare-dimension ledger (O1–O6) internally consistent; M_Pl²κ² = κ in the reduced-mass convention ✓.
12. **Counting consistency.** 14 entries = 7 foundations (B1–B7) + 7 branch entries (B8–B14); B8 subsumed → 13 distinct ✓ (abstract, Sec. I, Sec. III, Table I, Fig. 1, Conclusions all agree). Novel/known/structural split 9+4+1 = 14 ✓ and "eight of the nine ECH-specific, B10 excepted" ✓. Barrier→route tags in text (B1,B2,B8,B14→R1; B3,B4,B9→R2; B5,B6,B10,B11,B12→R3; B7,B13→R4; B14→all) match Fig. 1 and Table I ✓.
13. **App. D proof chain.** Zero spin density → T = 0 via invertible Q_γ (1+γ² > 0) → Levi-Civita → Holst term killed pointwise by algebraic Bianchi. Steps standard and correct; scope exclusions explicitly listed ✓.
14. **Significances.** 0.342/0.094 = 3.64 ("≈3.6σ") ✓; 0.215/0.074 = 2.91 ("≈2.9σ") ✓; α/M ~ 2β_obs/M_Pl = 9.8×10⁻²² ≈ 10⁻²¹ GeV⁻¹ ✓.
15. **Citation spot-checks (bibliographic).** Refs [2] (CQG 31 185002, arXiv:1402.4854), [3] (JPCS 360 012011, 1111.0884), [4] (CQG 28 213001, 1108.0893), [5] (PRD 53 5966), [6] (PRD 72 104002, hep-th/0507253; the −(3/2)πG γ²/(1+γ²) J₅² result is indeed FMT's published coefficient), [7] (PRL 103 081302), [8] (PRD 79 044008), [9] (JHEP 2011(6)107, 1104.4028), [10] (PRD 106 063503, 2205.13962, β = 0.342°±0.094° correct), [11] (PRL 125 221301, 0.35°±0.14° correct), [16]–[24] — all match known bibliographic records. Self-archive refs [1],[13] are candidly labeled not-peer-reviewed.

## MAJOR findings

**None.** Every displayed equation I could independently recompute is correct; internal cross-references of every headline number (58/60/61/67/68/92/94/122/123, 3.6 vs 3.9×10⁻⁶⁹) are mutually consistent; the tier-classification scope statements (Sec. III, Table II, Sec. VI) honestly bound what is claimed, and the "What is not established" section is exemplary.

## MINOR findings

- **MIN-1 (B1, p. 4, Found. A).** The tuning ratio as literally written is inverted: "the required tuning δm_T²/m_T² ~ (H₀/M_Pl)² ~ 10⁻¹²²". With radiative δm_T² ~ M_Pl² and target m_T ~ H₀, the ratio δm_T²/m_T² as defined evaluates to (M_Pl/H₀)² = 10⁺¹²². The intended statement (cancellation to one part in 10¹²², i.e. m_T²/δm_T² ~ 10⁻¹²²) should be written that way.
- **MIN-2 (p. 12, Sec. V main-text closure item (b)).** "reduce under T = κS … to the parity-odd four-fermion contact operator κ²(J⁵·J⁵)" — per the paper's own B8 (p. 5) and App. B (p. 16), (J⁵·J⁵) is parity-even; the parity-odd label belongs to the pre-reduction ε-contracted densities O4/O5, not their Fierz image. One-word fix ("the four-fermion contact operator") removes the internal contradiction.
- **MIN-3 (p. 6, Route 2).** "|Ω₄₄/α₄| = (378+783γ²)/[120(1+γ²)] … ≈3.3 at γ≈0.24 and O(1)–O(5) across γ ≲ O(1)": the ratio is bounded below by 378/120 ≈ 3.15 for all real γ, so the stated range floor "O(1)" understates it; "O(3)–O(5)" is what the formula gives.
- **MIN-4 (Eq. (1) → Eq. (2) step, pp. 6–7).** The numerator Δθ_one-loop ~ (α_em/4π)(H₀/M_Pl) is asserted ("is stated as the dimensionless budget ratio") rather than exhibited: the accumulation step (Hubble-amplitude ϑ_NY of dimension +1, division by M_Pl, anomaly chain of App. B, and the silently dropped — conservative — factors 1/16π² and β(γ)) should appear as one explicit intermediate line. The Tier-III labeling covers the logic, but the referee currently has to reconstruct the numerator from prose on p. 6.
- **MIN-5 (Ref. [12]).** The ACT DR6 birefringence citation (Diego-Palazuelos & Komatsu, arXiv:2509.13654, β = 0.215°±0.074°) could not be verified from this manuscript/environment; confirm the author list, identifier, and quoted value against the published record before submission. (All other quoted observational numbers verified.)
- **MIN-6 (presentation).** The abstract (~450 words, single block, with inline notation like "≥58" and tier vocabulary) exceeds typical CQG limits and reads as a summary section; the tier-status disclaimers are repeated near-verbatim in ≥5 places (Abstract, Sec. I Contributions, Sec. III preamble, Sec. IV closures, Table II caption, Sec. VI, App. A). Compress; keep Table II as the single authority.
- **MIN-7 (layout).** p. 19 left column carries a large vertical whitespace gap before App. E.2 ("The R1 finite-density benchmark"); p. 13 Data-and-Code block centers raw repository paths with awkward mid-path line breaks (`fierz_adjudication_2026_\\08_05.py`). Cosmetic, but visible.
- **MIN-8 (App. A / p. 15 dilution bookkeeping).** The 10¹²²-vs-10¹²³ and N = 92-vs-94 accounting is internally consistent (verified) but is spread over three passages (Eq. (A2) paragraph, "Inflationary dilution" paragraph, "Sharper dependency statement") with partially overlapping caveats; consolidating into one dependency statement would remove the need for the reader to re-derive which endpoint pairs with which convention.

## Scope-honesty assessment

Exceptional. The three-tier evidentiary classification is applied uniformly (only B14 claimed Tier-I; R2 explicitly Tier-III and "not load-bearing"; completeness of {O1–O6} explicitly asserted-not-proved in five places); Sec. VI "What is not established" enumerates the genuine escape routes; the companion's not-peer-reviewed status is disclosed in the reference list itself; load-bearing derivations are carried self-contained (Apps. D, E) so the Tier-I leg is refereeable from this manuscript alone. No overclaim identified.

## Verdict rationale

No mathematical error found in any checkable equation or numeric chain; all findings are notation (MIN-1, MIN-2, MIN-3), one missing intermediate display line (MIN-4), one unverifiable citation (MIN-5), and presentation (MIN-6–8). MINOR-REVISIONS; acceptable after these fixes.

*Claude (Fable 5) INT leg — exact-PDF-bound b4d73f94 — raw report saved before any verdict recorded.*
