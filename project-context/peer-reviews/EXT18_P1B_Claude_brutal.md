# EXT18 — P1B Brutal Referee Report

- **Reviewer:** Claude_brutal (Claude Code sub-agent, Anthropic)
- **Paper:** P1B — "Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model"
- **Round:** EXT18 (cross-vendor; Anthropic leg, run as Claude Code sub-agent — the API leg failed with a credit-balance 400, so this report replaces that stub)
- **Version:** v1B.0.73 (commit b22f8cc9)
- **Pages read:** 1–21 (full PDF, every page, all equations + Tables I–V + Figs 1–4)
- **Read type:** confirmation read of the EXT18 Ω_a relic-density correction + full brutal pass

---

## CONFIRMATION: corrected Ω_a / relic-density arithmetic

**The EXT18 correction is internally consistent. Recomputed independently and all fixed numbers check out:**

1. **ρ_crit,0 = 3H₀²M_Pl² ≈ 3.7×10⁻¹¹ eV⁴ (p13, Eq. 9 text).**
   H₀ = 67.68 km/s/Mpc = 2.193×10⁻¹⁸ s⁻¹ = 1.443×10⁻³³ eV (matches the paper's own 1.44×10⁻³³ eV on p13/p14).
   M_Pl (reduced) = 2.44×10¹⁸ GeV = 2.44×10²⁷ eV (stated in the same equation).
   3 × (1.443×10⁻³³)² × (2.44×10²⁷)² = **3.72×10⁻¹¹ eV⁴** ✓.
   The old erroneous 8.1×10⁻¹¹ corresponds to using the *non-reduced* Planck mass; the fix to the reduced M_Pl is now self-consistent with the M_Pl value printed in the same equation. CONFIRMED.

2. **Eq. (9) small-angle denominator 6H₀² (p13).**
   Ω_a ≈ m_a²f_a²[1−cos θ_i]/[ρ_crit,0(1+z_osc)³]; small θ_i ⇒ 1−cos θ_i ≈ θ_i²/2; f_a=M_Pl ⇒
   Ω_a ≈ m_a²M_Pl²(θ_i²/2)/[3H₀²M_Pl²(1+z_osc)³] = m_a²θ_i²/[6H₀²(1+z_osc)³] ✓.
   The factor of 3 from ρ_crit and the ½ from the cosine expansion combine to 6. The old 2H₀² omitted the relic-density factor-3. CONFIRMED.

3. **fn. 6 backreaction θ_i² scaling.** Ω_a(0.1)/Ω_a(0.5) = (0.1/0.5)² = 0.04 = 1/25 ⇒ the stated ~25× misalignment tuning. ✓ Consistent with the corrected θ_i² law.

4. **H₀-marginalization ≤3% (p13).** Ω_a ∝ H₀⁻² (from 1/ρ_crit,0 ∝ 1/H₀²); the Planck 1σ on H₀ is ±1.06/67.68 ≈ 1.57%, doubled by the square ⇒ ≈3.1% shift. The "≤3%" (corrected from ≤1%) is the right order and correctly stated as below the Ω_a<0.01 cut's statistical uncertainty. ✓

5. **S₈ harmonization to 2.6σ.** Abstract (p1) and p5 caveat (d) both now read 2.6σ; Table II iter2 S₈=0.8245±0.0089; Table I full-tension S₈=0.814±0.008 with the posterior-overlap-integral 2.6σ vs DES-Y3 0.776±0.017 (the 2.0σ "from the prior" figure is separately and correctly labeled a within-stack readout). The headline 2.6σ is now consistent across abstract/body/tables. ✓

**Verdict on the correction: the Ω_a arithmetic is now internally consistent.** No residual factor errors in the relic-density subsection.

Cross-check on Eq. (4) (recomputed): α_EM/(4π)=1/137.036/(4π)=5.81×10⁻⁴ ✓; ×8×1.06=4.93×10⁻³ rad ✓; ×180/π=0.282° ✓.

---

## ESSENTIAL findings

None.

## MAJOR findings

None. The paper is unusually disciplined for its claim register: every potentially-overclaimed quantity (NaMaster template-fit SNR 20.32/25.71, the 3.9σ inverse-variance combination, the w₀wₐ +4.3σ/−3.6σ tails, the LiteBIRD 9σ) is explicitly down-graded in place to a pipeline-validation / posterior-tail-extrapolation / forecast-not-discrimination statement. The central framing — "technical verification companion, not a sky detection, not a distinctive ECH prediction" — is honestly matched between abstract and body. Headline numbers are earned at the (deliberately modest) level claimed.

## MINOR findings

1. **MINOR — Eq. (4) "0.28°" vs Eq. (3)/abstract "0.27°" benchmark (p11, p1).**
   The abstract and §VI use β≈0.27°; Eq. (4)'s worked example lands on 0.28° (from Δφ/f_a=1.06 at the C_aγ=8/θ_i=1/m≈3.9H₀ corner). This is correct and self-consistent, but a skimming reader sees 0.27°/0.28°/0.342° within one column. *Suggested fix (optional):* add a clause at Eq. (4) — "0.28° here vs the 0.27° headline reflects Δφ/f_a=1.06 vs 1.0 grid point." Non-blocking; the distinction is already explained two sentences down.

2. **MINOR — Table II χ²_total rounding artifact (p20, fn. c).**
   The 0.1 mismatch between χ²_total (14037.4) and the channel sum (10.6+10983.9+3043.0=14037.5) is honestly footnoted as a GetDist weighted-sample vs channel-sum rounding artifact with the correct non-independence caveat. Fine to keep; quoting both to one decimal consistently would make the 0.1 gap visibly a rounding tie. Non-blocking.

3. **MINOR — heavy footnote load in §VI.**
   The load-bearing spectator caveats (25× tuning, Ω_a<0.01 = 13% of posterior mass) are correctly elevated into main text (p12, p14) per the EXT directive, but fns 5/6 still carry the quantitative backreaction algebra a reader must follow to trust the spectator label. Acceptable for a verification companion; a PRD referee may ask fn. 6's Ω_a(0.1)/Ω_a(0.5) algebra into the body. Editorial, non-blocking.

**No leftover audit tags, no `\todo`/`XXX`/placeholder strings, no duplicated sentences, no hedges-masquerading-as-conclusions detected.** The "consistency check, not a prediction" / "pipeline validation, not a detection" hedges are correctly load-bearing scope statements, not disguised positive claims.

---

## FINAL VERDICT: ACCEPT

The EXT18 relic-density correction is verified internally consistent (ρ_crit,0=3.7×10⁻¹¹ eV⁴, Eq. 9 denominator 6H₀², ≤3% H₀-marginalization, 1/25 backreaction, 2.6σ S₈ all recomputed and confirmed). Table arithmetic (Tables I, II, IV) and Eq. (4) birefringence chain recompute correctly. Abstract matches body. Claims are honestly scoped and not overstated. The three MINOR items are editorial polish, not correctness issues, and do not gate acceptance.
