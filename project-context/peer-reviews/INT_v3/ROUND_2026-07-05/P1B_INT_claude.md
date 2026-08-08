# INT (Claude Code, full-source) referee review — P1B v1B.0.99
Paper: arxiv/paper1b_mcmc_companion.tex · Round 2026-07-05 · leg: Claude Code (Houston subscription, NOT Anthropic API)
Reviewer stance: PRD referee, source-of-truth complement to EXT. Claims verified against .tex + chains + scripts. No fabrication.

## Verdict: MINOR REVISIONS

Central claim — that P1B supplies correct, reproducible methodological/consistency material for the ECH program — is SUPPORTED. The three headline results (stock-CAMB ΔN_eff consistent with zero, NaMaster synthetic-sky bias/SNR, ALP posterior accommodation) all reproduce from committed artifacts. The §III.A dimensional fix is correct. One real internal numeric inconsistency and one missing diagnostic artifact keep it from a clean ACCEPT.

## Dimensional / arithmetic verification (§III.A, the recently-touched section)

- **§III.A four-fermion coefficient IS now dimensionally consistent.** Eq.(eq:fourfermion), L1558-1560: `L_4f = -(3κ²/16)[γ²/(γ²+1)](ψ̄γ⁵γ^μψ)²`, with `κ²=8πG_N=M_Pl⁻²`. Check: [κ²]=M⁻²; dim-6 four-fermion operator (ψ:M^{3/2} → bilinear M³ → squared M⁶); M⁻²·M⁶=M⁴ = Lagrangian density. ✓. The γ→∞ ECSK limit reducing to `-(3/2)πG_N(...)²` (L1567) is consistent (κ²/16·1 → with 8π: (8πG/16)·(3)=(3/2)πG). ✓. The v1B.0.98 fix (κ→κ²) is genuine and correct.
- **Thermal-average intermediate step (v1B.0.99) is reasonable.** L1576-1585: `⟨(ψ̄γ⁵γ^μψ)²⟩_T ~ n_f² ~ (g_*T³)²`, Kapusta-Gale cited. This is a heuristic factorization (dimensionally n_f²~T⁶ ✓) presented with "~", not a rigorous NJL thermal computation — acceptable at the order-of-magnitude level the section claims.

- **[MAJOR-1 candidate / firm MINOR] Reduced-vs-non-reduced Planck-mass inconsistency in Eq.(eq:neff_bound).**
  Eq.(eq:torsion_ratio) L1587-1589 writes `ρ_tor/ρ_rad ~ G_N T² = (T/M_Pl)²`, and the paper defines `M_Pl = (8πG)^{-1/2} ≈ 2.44×10¹⁸ GeV` (REDUCED) at L1301, L1378, L2767 — the SAME M_Pl as κ⁻¹ in L1560. But the numerical values in Eq.(eq:neff_bound) L1600-1603 (7×10⁻⁴⁵ at T=1 MeV; 5×10⁻⁵⁸ at T=0.26 eV) correspond to the **non-reduced** Planck mass 1.22×10¹⁹ GeV, not the reduced one the equation actually uses:
    - reduced (self-consistent w/ eq): (1 MeV/2.44e21 MeV)² = **1.7×10⁻⁴³**; (0.26 eV/M_Pl)² = **1.1×10⁻⁵⁶**
    - non-reduced: (1/1.22e22)² = **6.7×10⁻⁴⁵** ✓ matches 7e-45; recomb = **4.5×10⁻⁵⁸** ✓ matches 5e-58
  So the quoted numbers are internally inconsistent with the equation that generates them (and with the reduced-M_Pl definition used everywhere else in the paper) by a factor ~24 (1.4 dex). EXT would not catch this. NOT fatal — the physics claim is only "~40 orders below any sensitivity," which holds under either convention — but it is a REAL source/arithmetic inconsistency that must be fixed: either switch these two numbers to the reduced-M_Pl values (1.7e-43, 1.1e-56) OR state that Eq.(eq:neff_bound) plugs in the non-reduced Planck mass while Eq.(eq:torsion_ratio) is written with the reduced one. As written the reader cannot reproduce the boxed numbers from the boxed equation. Downgraded from MAJOR to firm MINOR only because the load-bearing conclusion is convention-independent.

## Chain / data verification (VERIFIED against committed artifacts)

- **[VERIFIED] ΔN_eff MCMC / SH0ES tension unreduced.** parameter_summary_CORRECTED.json (frozen full_tension + planck_bao_sn dirs): ΔNeff = −0.0196±0.169 and +0.0578±0.179 → paper's −0.020±0.169 / +0.058±0.179 (L1268, L1806) MATCH. H0 = 67.68 / 67.78 in both — stays ~67.7, NOT ~73; "SH0ES tension unreduced / consistent with zero / stock CAMB" claim is honestly represented. ✓
- **[VERIFIED] Sample counts.** 176,240 + 132,949 = 309,189 (L1649-1650) matches committed diagnostics exactly. ✓
- **[VERIFIED] NaMaster.** summary.json: bias β̂−β_inj = −0.032° / −0.040°, template-fit SNR 20.32 / 25.71 (§IV) MATCH committed JSON. Synthetic-ΛCDM-sky / ACT-like-mask / pipeline-recovery framing (not sky detection) is correctly scoped. ✓

## Issues

**[MINOR-1] (= the reduced/non-reduced M_Pl issue above)** Eq.(eq:neff_bound) L1600-1603 numbers use non-reduced M_Pl; Eq.(eq:torsion_ratio) + all M_Pl definitions use reduced (2.44e18). Factor ~24 internal inconsistency. Fix the numbers or add a one-line convention note. VERIFIED (arithmetic recomputed).

**[MINOR-2] ALP posterior-mass fractions not backed by a committed diagnostic.** Table IV (tab:alp_restricted_subsets) claims 44%/13% mass at Ω_a<0.1/<0.01, β|Ω_a≤0.01=0.28±0.10, ESS values, and 9,720 accepted samples. Unlike the MCMC runs, there is NO committed `alp_parameter_summary.json`; raw chain line-counts (c5_continuous 8,959 + run3_baseline 721 = 9,680) fall ~40 short of the quoted 9,720. The ~25×/>100× fine-tuning is an in-paper analytic calc, fine. But the mass-fraction/ESS numbers are not machine-verifiable from committed artifacts, and the 9,680-vs-9,720 sample count needs a recount or correction. Recommend committing an ALP summary JSON + the reduction script. VERIFIED-as-gap (artifact absent).

**[MINOR-3] Thermal factorization is heuristic.** L1580-1583 `⟨(A^μ)²⟩_T ~ n_f²` is stated as "factorizes at leading order" but is really a parametric estimate, not a derived NJL finite-T result. Acceptable given "~" throughout, but a one-clause "(parametric estimate; O(1) coefficients dropped)" would prevent an EXT referee re-flagging it as an unjustified equality.

**[MINOR-4 / noted, not blocking] Venue.** Companion-vs-standalone question is real but out of content scope; framing ("consistency-check companion, self-contained + reproducible") is already handled honestly across abstract + §I. No action required on content grounds.

## Is the content error-clean?
Nearly. The §III.A dimensional bug is genuinely fixed and the three data-backed results reproduce from committed chains/JSON. Remaining defects are ONE real internal numeric inconsistency (reduced vs non-reduced M_Pl in Eq. neff_bound — must fix or annotate) and ONE reproducibility gap (ALP fractions/ESS lack a committed diagnostic + a ~40-sample miscount). Both are MINOR, both are the kind of source/arithmetic issue EXT cannot see. No fabricated derivation, no chain-vs-paper mismatch on the load-bearing ΔNeff/NaMaster results, no overclaim on the tension.
