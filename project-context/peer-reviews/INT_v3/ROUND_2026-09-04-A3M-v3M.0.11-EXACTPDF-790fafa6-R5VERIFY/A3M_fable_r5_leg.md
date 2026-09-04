# INT referee report — A3-Multichannel v3M.0.11 — R5 — Claude (Fable 5.1) leg

- **PDF reviewed:** `site/public/papers/a3_multichannel_arxiv_v3M.0.11.pdf`
- **sha256:** `790fafa691e1a6ef0c476309d8224c5f2af2a59e4a3966f6afa0cf9d9dff4105`
- **Pages:** 14
- **Date:** 2026-09-04
- **Venue standard:** Physical Review D (regular article), independent skeptical referee
- **Reviewer model:** Claude Fable 5.1 (Claude Code subagent), exact-PDF-bound; no prior boards, SSOT, dispositions, or referee reports read.

(Report appended per section below as the read proceeds.)

## Summary

1. The paper re-derives the matter-contraction local amplitude f_NL = −35/16 vertex-by-vertex (Table I sums correctly; Eq. (A3) reduces correctly at ε = 3/2), localizes Cai et al.'s factor of 2 to their Eqs. (38)–(40), and relates the δN and in-in variables by a linear identity δN_c = (1−ε/3)ζ.
2. It then bounds/computes transmission through three bounce backgrounds in two schemes (S1: f_after ∈ [−0.65,−0.50]; S2: ≈ −1.25 on one background) and carries the result through PTA, PBH and LSS channels, reporting three nulls and one non-discriminating channel.
3. The arithmetic I re-checked (Table I sum, Eq. (4) monopole/quadrupole, the S1 per-background table from Eqs. (6)–(7), every entry of Table IV, all z-values in Table II and the refit/official 1.20σ) reproduces. The paper is unusually candid about what is and is not established.
4. However, the abstract's linear "bound" 0 ≤ T_fNL < 1/2 is contradicted by the paper's own S2 result (λ_ζ = 0.97 ⇒ T ≈ 1.03); §III and §V C make incompatible statements about the LQC exact-mode bispectrum at kη_B ~ 1–3; a headline NANOGrav amplitude is misprinted; the §II D variable accounting leaves the normalization of the δN f_NL values undefined; and a sign disagreement with the only reference implementation of the compaction criterion is left open.
5. These are fixable, but as it stands the transmission and PBH sections would not survive a PRD referee without revision.

## Verdict

**major-revisions**

## MAJOR findings

**M1. (Abstract; §III p. 4 Eq. (6) and the text after it; §III A "Scheme S2, resolved", p. 5.)** The abstract states "a linear handoff bound (0 ≤ T_fNL < 1/2, 0.165–0.409)" and p. 4 says "within this handoff scheme, linear transfer can only suppress the amplitude", "T_fNL = 1/λ_ζ". But p. 5 reports that in scheme S2 on the Quintin-type background "S2 transmits the growing mode almost unsuppressed (|λ_ζ| = 0.97)", i.e. T_fNL = 1/0.97 ≈ 1.03 > 1/2 — and the paper's own decomposition (T·(−2.1875) ≈ −2.25, net cubic +1.0, f_after = −1.25) uses exactly that T. So the "< 1/2" bound is an S1-only statement, the quoted range 0.165–0.409 (advertised on p. 4 as "the full set of three backgrounds and two conventions") omits the S2/Quintin-type value ≈ 1.03, and the sentence "linear transfer can only suppress the amplitude, never invert or amplify its sign" is false in S2 as computed. Either |r| ≫ 1 fails for S2 modes or (A4) does not apply there; the paper does not say which. *Resolves it:* a 3-background × 2-scheme table of (λ_ζ, T_fNL, Δf^bounce, f_after) with "not computed" cells explicit; restate the bound as "0 ≤ T < 1/2 in scheme S1"; rewrite the abstract sentence accordingly.

**M2. (§III item (3), p. 4, vs §V C, pp. 9–10.)** §III states the exact-mode LQC-dust bispectrum across kη_B ∈ [0.1, 10] "shows no counterpart of the literature's order-10³ plateau … it sits 2.1–4.4 decades below that plateau". §V C then reports, from "that scan", "the largest number produced anywhere in that scan (equilateral configuration, |f_NL| ≈ 1.2 × 10³)". A value of 1.2×10³ is at the level of the order-10³ plateau, not 2–4 decades below it. Unless the two statements refer to different configurations/normalizations (squeezed vs equilateral, f_NL vs a shape-normalized bispectrum), they contradict each other; if they do refer to different things, the §III sentence must say which configuration the "2.1–4.4 decades" applies to and must acknowledge the O(10³) equilateral value. *Resolves it:* one table (configuration, kη_B, initial state, |f_NL|) for the exact-mode scan, cited from both sections.

**M3. (§IV D p. 7; Fig. 1 caption; abstract "10^14.3".)** The text reads "predicted amplitude Ω_GW h²(f_yr) = 1.45 × 10⁻²³ … against NANOGrav's power-law value 6.3 × 10⁻¹⁰ at f_yr – fourteen orders of magnitude below". log10(6.3e−10 / 1.45e−23) = 13.6, not 14.3, and for the dust bracket log10(6.3e−10/5.88e−23) = 13.0, not 13.7. I checked the committed output `research/track_a3_multichannel/outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json`: it uses `nanograv_reference/Omega_GW_h2_at_f_yr = 3.62e−9` (from A = 2.4e−15, γ = 3.2, which I reproduce analytically) and records `log10_amplitude_shortfall = 14.34` / `13.74`. Fig. 1's dashed NANOGrav line also sits at ~3×10⁻⁹ at 30 nHz. The printed 6.3 × 10⁻¹⁰ is therefore unsupported by the paper's own artifact; the 14.3/13.7 gaps are supported. *Resolves it:* replace 6.3×10⁻¹⁰ by 3.6×10⁻⁹ (state the h² convention) or, if 6.3×10⁻¹⁰ is Ω_GW at some other frequency/convention, say so and recompute the gap consistently in text, abstract, and caption.

**M4. (§II D pp. 2–3, Eq. (5); Appendix A.1–A.2, p. 12.)** The δN values f^ρ_NL = 5(ε−7)/8 and f^c_NL = −5 "for all ε" are compared with the in-in monopole −15/8 and the gap "−25/8" is accounted for term by term ([X]_mono 5/4 + ([L] − δN_c) 15/8). But the paper never states what these δN f_NL's are normalized against. If δN_c = (1−ε/3)ζ_Mald at linear order (Eq. (5)), then a bispectrum of δN_c normalized by P²_{δN_c} differs from one normalized by P²_ζ by the factor 1/(1−ε/3) = 2 at ε = 3/2 — i.e. a pure linear rescaling already maps −15/8 ↔ −15/4 — and at ε → 3 the linear map vanishes, so an ε-independent "f^c_NL = −5" cannot be a properly normalized f_NL of δN_c on that branch. The gap accounting on p. 12 ("−15/8 − (−5) = 25/8") mixes a ζ-normalized number with a δN number without saying so. Appendix A.1 is a four-sentence sketch of the identity that the abstract calls "derived"; the expansion of the comoving-normal congruence, K = (1/N)(3H + 3ζ̇ − ∂²ψ/a² + …), and the step ψ ⊃ a²ε∂⁻²ζ̇ ⇒ δ(K/3) = (1−ε/3)ζ̇ should be written out. *Resolves it:* define f^ρ_NL, f^c_NL (which variable, which power spectrum); redo the [L]/[K]/[X]/[S] accounting in one normalization; show the ε → 3 limit is sensible; expand A.1 into an actual derivation.

**M5. (§V B, p. 8, last paragraph.)** The paper reports that for γ_cr ≲ 0.85 "our implementation instead finds enhancement relative to Gaussian where they [Choudhury et al.] report suppression, a genuine discrepancy left unresolved". Channel II's only quotable output (the amplitude ratio, Eq. (12), and the −35/8 > −35/16 ordering) rests on this implementation, and the sign of the non-Gaussian correction relative to Gaussian is the central physical claim of the cited reference. A sign disagreement with the reference implementation cannot be left open in a section that adopts that reference's criterion. The itemized deviations (single horizon mass M_H = 10²⁰ g vs their mass-integrated Eq. 66, width factor, lognormal stand-in) are candidates; one of them presumably flips the sign. *Resolves it:* run the paper's code at Choudhury et al.'s stated parameter set (their γ_cr, C_th, Δ, M-integration) and report whether the sign agrees there; if not, identify the responsible step; if it cannot be reproduced, say the ratio 1.7–1.9 is conditional on this unresolved discrepancy in the abstract, not only in §V B.

## Minor findings

1. Abstract: "combining power spectrum and bispectrum widens the separation to 0.5–1.1σ." From the S1 table, |Δf_after| = 0.36–0.55; /0.5 gives 0.7–1.1σ (P+B) and /0.7 gives 0.5–0.8σ (B only). The 0.5 belongs to the bispectrum-only case. §VI and §VII B also say "under 1σ" while the top of the range is 1.1σ.
2. Abstract: the band "[−1.25, −0.50]" is quoted without the qualifiers the body attaches (S2 on Quintin-type only, −35/16 only). Add "(S2 on one background)".
3. Abstract "0.165–0.409" and p. 4 "the full set of three backgrounds and two conventions": only four (background, scheme) pairs are evaluated at that point, and the S2/Quintin-type value (≈1.03, see M1) is not in the range.
4. §II A/Table I count five cubic pieces; §III A says "all six cubic attachments and boundary terms". State which sixth operator appears at the bounce (ε_eff = 1/2, z = a) and why it is absent from Table I.
5. The per-background table in §III A (p. 5) has no number or caption, yet Table IV refers to it as "Table in Sec. III A". Number it.
6. p. 4: the poly-background power ratio 0.058 at kη_B ≈ 0.7 is a factor-17 suppression, not an "O(1) excursion". Also, state where kη_B ~ 1 falls in physical k for the T_B range allowed in §V C (k_B ≈ 1.7×10¹⁵ Mpc⁻¹ at T_B = 10⁸ GeV per the committed JSON) so the reader can see whether the feature is observable anywhere.
7. §V C: "at kη_B ≈ 3, the extreme small-scale end of the PBH band". With the §V C requirement T_B ≳ 10⁸–10¹⁰ GeV, the 10¹⁵ g scale has kη_B ≲ 10⁻² by construction; kη_B ≈ 3 at k ~ 10¹⁶ Mpc⁻¹ corresponds to T_B ~ 10⁶ GeV, which §V C excludes. Say which bounce scale this evaluation assumes.
8. §V B footnote: knowingly propagating Ω_DM = 0.674 (which is h, not Ω_DM) into Eq. (13), Table III's f_PBH columns and Fig. 2 is not acceptable in a journal article; use 0.264 (or Ω_DM h² = 0.12) and note the ×2.55 rescale. The ratio is unaffected, as stated.
9. Table II / §IV B: B_{13/3/free} = 5×10⁻⁴ from 9 chain samples, and the derived B_MB/SMBHB ≈ 7×10³ "stable in 7–9×10³ (±0.2 dex)": a KDE density evaluated at a point supported by 9 samples has far larger uncertainty than ±0.2 dex. Quote as a bound or drop.
10. §IV D / abstract: a "5.1σ" slope tension for a signal 14 decades below NANOGrav's amplitude is not a test of anything (NANOGrav's slope is not measuring this signal). Report the amplitude shortfall as the null and drop the σ language, or say explicitly that the σ number is hypothetical.
11. §III item (2): the Quintin Eq. (79) amplification factor is "constant on the Quintin-type background by construction" — then it is not a check on that background. Say so, or evaluate it on a background where the velocity dip exists.
12. §VII A: "not the 3.13σ apparent tension with the pre-bounce amplitude" — 3.13σ (Table IV) is a bare forecast detection significance, not a tension.
13. Eq. (8) and §IV A: γ definition via h_c ∝ f^{(3−γ)/2} is fine; note that Table II's z_off for γ = 5 (4.9σ) coincides with the model's own γ_pred to 1 decimal, so "prim. tensors" and "this model" rows are visually confusable; label.
14. Fig. 1: title carries the internal label "A3-3"; legend entries are code identifiers ("MB_anchored_ns0.9649", "pure_dust_ns1"). Fig. 2: the f_PBH > 1 region (up to 10⁸) is unphysical and should be shaded or capped; the caption's "uncapped" is not on the plot.
15. Typos/style: "isoceles" (p. 5); "(below). so |f_after|" and "−5/24. a closed-form" (p. 5, sentence breaks); "”moderate tension" (p. 6, quote marks); "Papanikolaou [8] derive" (single author); "correcting an earlier statement in this program" (p. 4) and "An earlier version of this program reported" (p. 5) are internal-history remarks that do not belong in the article.
16. First-order primordial tensors: a matter bounce produces a scale-invariant tensor spectrum with r typically O(0.1–1); Channel I compares only the induced (second-order) background. State the model's own first-order Ω_GW at nHz (also a null, but it is the model's channel, and the γ = 5 row of Table II is presented as generic).

## Reference spot-check (5 + 3)

- [1] Cai, Xue, Brandenberger, Zhang, JCAP 0905, 011 (2009), arXiv:0903.0631 — correct; the −35/8 quoted amplitude is as printed there.
- [4] Li, Quintin, Wang, Cai, JCAP 1703, 031 (2017), arXiv:1612.02036 — correct.
- [6] Namjoo, Firouzjahi, Sasaki, EPL 101, 39001 (2013), arXiv:1210.3692 — correct; f_NL = 5/2 USR value as used in §II A.
- [11] Agazie et al., ApJL 951, L8 (2023), arXiv:2306.16213 — correct; γ = 3.2 ± 0.6 is median and 90% CI there, consistent with the paper's "5–95%".
- [17] Young, Byrnes, Sasaki, JCAP 07, 045 (2019), arXiv:1904.00984 — correct.
- [10] Kohri & Terada PRD 97, 123532 (2018) and [9] Cai, Pi, Sasaki PRD 102, 083528 (2020) — correct; the 0.8222 flat-spectrum coefficient the JSON validates against is the Kohri–Terada value.
- [8] Papanikolaou arXiv:2504.11641 and [16] Choudhury et al. EPJC 85, 472 (2025) — not independently verifiable here; flagged as unverified, not wrong.
- Missing: δN formalism originals (Sasaki–Stewart 1996; Lyth–Malik–Sasaki 2005), gradient expansion (Salopek–Bond 1990), anisotropic/Bianchi-I separate universe (Talebian, Ashoorioon, Firouzjahi 2019 or Tanaka–Urakawa), a matter-bounce review (Brandenberger & Peter 2017), and the source of the SPHEREx P+B σ = 0.5 (Table IV cites [20, 21]; [21] is the 2014 mission paper, which does not give 0.5).

## Questions to the authors

Q1. In S2 the growing mode passes through the bounce with λ_ζ = 0.97 while in S1 it grows by 6.06 on the same background: does the post-bounce power-spectrum amplitude then differ by ~39 between schemes? If so, CMB normalization fixes a different pre-bounce amplitude per scheme; does anything in §§IV–VI depend on which one is used?
Q2. What is f^c_NL = −5 normalized against (see M4), and what does the comoving-slice δN give at ε = 3 where (1−ε/3) = 0?
Q3. Which boundary/field-redefinition terms are kept in Table I's first row? In a non-attractor phase with ζ' = −3ζ/η the ζ̇ζ² boundary terms do not vanish; is the "−25/16 − (15/16)μ²" entry the total of all of them?
Q4. Is the kη_B ≈ 0.6–0.8 transfer excursion (×2.24, ×0.058) ever at an observable k for any T_B allowed by §V C? A one-line k_feature(T_B) would settle it.
Q5. What is the model's own first-order tensor spectrum at nHz, and why is it not Channel I's primary comparison?
Q6. §III A: how is Eq. (7)'s evaluation window [−η_B, η_B] chosen when S2's analogous integral is stated to be window-dependent at O(1)? Is S1's window-independence demonstrated or assumed?

## Integrity note

One printed number is not supported by the paper's own artifact: §IV D's "NANOGrav's power-law value 6.3 × 10⁻¹⁰ at f_yr". The committed JSON (`research/track_a3_multichannel/outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json`) uses 3.62 × 10⁻⁹, which is what A = 2.4×10⁻¹⁵, γ = 3.2 gives, and which is required for the quoted 10^14.3 / 10^13.7 gaps (which are themselves supported). No other number I re-derived (Table I, Eqs. (4)/(A3), Eqs. (6)–(7) table, Tables II and IV, the 1.20σ refit offset, FIRAS μ) failed.
