# INT referee report — A3M v3M.0.13 (R6, Claude Fable 5.1 leg)

- **PDF:** site/public/papers/a3_multichannel_arxiv_v3M.0.13.pdf
- **sha256:** c6f9bb57f9acb755dfe6a3bda12955038ffcf46c86a5cea9809dabff5031a34c
- **Date:** 2026-09-04
- **Venue standard:** Physical Review D, regular article
- **Reviewer:** independent skeptical referee (Claude Fable 5.1, INT leg); no prior reports, SSOT, or dispositions consulted
- **Status:** COMPLETE — verdict major-revisions (5 MAJOR, 15 minor, 7 questions)


## Reading notes — pp. 1–5 (abstract, §I, §II, §III through Table III)

Arithmetic checked by hand (all pass):
- Table I column sum: −25/16 − 5/32 + 0 + 0 − 15/32 = −35/16; μ² sum −15/16 + 15/8 = +15/16. Eq. (3)/(4) consistent.
- Angular average of −35/16 + (15/16)μ² = −15/8; P₂ coefficient (15/16)(2/3) = 5/8. Matches text p.2.
- Cai et al. quoted amplitudes (−35/8, −255/64, −9/4) are exactly 2× (−35/16, −255/128, −9/8). Consistent.
- Separate-universe: 5(ε−7)/8 at ε=3/2 = −55/16. Consistent.
- Eq. (7) + linear transfer: f_after = −(35/16)T − (5/24)(1−2T) = −(85/48)T − 5/24. Table III: T=0.165→−0.501, Δ=−0.140; T=0.250→−0.651, Δ=−0.104; T=0.196→−0.555, Δ=−0.127. All reproduce. 19–39% ratio reproduces.
- T = 1/λ_ζ with λ = 6.06, 4.0, 5.12 → 0.165, 0.250, 0.195. Consistent with T=(1−ρ)/2 (ρ=1−2/λ).
- S2: −2.187×1.03 + 1.0 ≈ −1.25. Consistent.

Concerns logged for the findings section:
- (C1) Abstract: "5.1σ off NANOGrav's γ_HD = 3.2" — NANOGrav 15-yr HD-correlated γ = 3.2 ± 0.6; (5.07−3.2)/0.6 ≈ 3.1σ. Verify in §IV what σ is used.
- (C2) Abstract: "amplitude ∼10^14 below NANOGrav" for induced GWs from a scale-invariant A_s≈2.1e−9 spectrum: Ω_GW ∼ O(1–10)·A_s² ∼ 10^−17 vs NANOGrav Ω_GW h² ∼ 10^−9 → ∼10^8–10^9, not 10^14. Verify §IV definitions.
- (C3) §II.D: identity δN_c = (1−ε/3)ζ_Mald (Eq. 5) is asserted as "derived"; check Appendix A for the derivation and its validity for the growing (non-attractor) mode ζ' = −3ζ/η where the gradient expansion fails.
- (C4) §III.A: scheme S1 uses Maldacena's cubic action with constant ε_eff = 1/2, c_s = 1 *through H = 0*; Eq. (7) then depends on the background only through ρ_B. This is flagged by the authors as an assumption, but the abstract's "transmitted band" is built on it.
- (C5) p.4: "n_s = 0.9649 in Sec. VI is not in tension with this section" while Δ² is computed flat to 1.2–4.2%: a dust-contraction gives n_s = 1, which Planck excludes at ≳8σ. Check how §VI justifies inserting n_s = 0.9649.
- (C6) p.4 direction-of-kη_B paragraph: no mapping from physical k [Mpc⁻¹] to kη_B is given here; the validated band kη_B ≲ 10⁻² is a condition on η_B (bounce energy) — check §V.C states the number.
- (C7) Table II: equilateral |f^bounce| = 112, 1216 at kη_B = 3, 10. The claim "None of the three mechanisms re-opens the PBH null" depends on the PBH-scale modes satisfying kη_B ≲ 10⁻²; check.
- (C8) "2.1–4.4 dex" deficit vs ABS plateau: not reproducible from Table II without the ABS plateau values, which are not tabulated.

## Reading notes — pp. 6–10 (§IV Channel I, §V Channel II)

Arithmetic checked (pass):
- Table IV z_off with σ=0.365: (3.2−2)/0.365=3.29; (3.2−3)/0.365=0.55; (4.333−3.2)/0.365=3.10; (5−3.2)/0.365=4.93; (5.07−3.2)/0.365=5.12 → "5.1σ". Refit with σ=0.382, γ=2.567: 1.48, 1.13, 4.62, 6.37. All reproduce.
- Ω_GW h²(f_yr)=1.45e−23 vs 3.6235e−9 → 10^14.4. Order-of-magnitude sanity: Ω_GW,rad ≈ 0.82·A_s² ≈ 3.6e−18, ×Ω_r h²·g-factor ≈ 1.7e−5, × tilt suppression from k=0.05 to k≈2e7 Mpc⁻¹ ((4e8)^{−2×0.0351} ≈ 0.25) ≈ 1.5e−23. Plausible; concern C2 from the abstract WITHDRAWN.
- r<0.036 → Ω^(1)h² < 2.5e−17 vs 1.45e−23: "six decades" reproduces.
- NANOGrav band k ≈ 2π f/c: 60 nHz → 3.9e7 Mpc⁻¹; with k_B(10^8 GeV)=1.714e15 Mpc⁻¹ (p.10) → kη_B ≈ 2.3e−8. Reproduces.
- Eq. (11): ζ_max = −5/(12 f_NL) + (3/5)|f_NL|σ²; 0.09524 / 0.19048; with σ=0.1: 0.1215 / 0.2036. Reproduce.
- Table V ratio column: 1.767, 1.673, 1.734, 1.809, 1.677 lie within [1.610,1.809] stated.
- PBH scale: M_H ∝ k⁻²; 10^15 g ↔ k ≈ 5e15 Mpc⁻¹. Consistent with "10^15–10^16".

Concerns:
- (C1, refined) The 5.1σ uses σ≈0.6/1.645=0.365, i.e. it reads NANOGrav's "3.2 ± 0.6" as a 90% (5–95%) interval and then extrapolates a Gaussian to 5σ. If NANOGrav's ±0.6 is a 68% interval the tension is 3.1σ. The paper must cite the exact sentence/table of Ref. [11] that fixes the convention, and should not quote 5.1σ to two figures from a Gaussian tail of an asymmetric posterior (its own refit paragraph makes the same point about tails).
- (C9) BOUNCE ENERGY INCONSISTENCY (p.10 vs p.10): "Requiring kη_B ≲ 10⁻² at k ~ 10^15–10^16 Mpc⁻¹ needs a_B H_B ≳ 10^17–10^18 Mpc⁻¹, i.e. T_B ≳ 10^8–10^10 GeV" — but the paper's own mapping two paragraphs later gives k_B = a_B H_B = 1.714×10^15 Mpc⁻¹ at T_B = 10^8 GeV. With k_B ∝ T_B (radiation scaling, up to g_* factors), a_B H_B = 10^17–10^18 requires T_B ≳ 10^10–10^11 GeV, not 10^8–10^10 GeV. Two-decade internal inconsistency in a condition quoted in the abstract ("bounce-energy condition"). Also §IV.D uses "T_B ≳ 10^8 GeV" as the threshold. Needs one explicit k_B(T_B) formula and consistent numbers.
- (C10) TENSOR SECTOR: §IV.D quotes "the unresolved r = 0.84 matter-bounce scenario (open item, not adopted)" and instead uses the observational bound r < 0.036. If the same dust-contraction background that fixes f_NL = −35/16 predicts r ≈ 0.84, it is excluded by BICEP/Keck+Planck at enormous significance; a "multi-channel consistency assessment" that omits the tensor channel while calling three nulls "honest" is incomplete. Same for n_s: the paper inserts n_s = 0.9649 via w ≈ −0.003 (n_s−1 = 12w/(1+3w)) but Eq. (1) is the w=0 value; the general-ε formula (Appendix) should be used to state f_NL at the n_s-matched w, or the O(w) shift quantified.
- (C11) PBH headline "shape-robust ratio 1.7–1.9": Table V caption states the model's own spectrum has γ_cr ∈ [0.27,0.63], OUTSIDE the scanned grid [0.766,0.968], and p.9 states that for γ_cr ≲ 0.85 the implementation finds ENHANCEMENT where Choudhury et al. report SUPPRESSION ("a genuine discrepancy left unresolved"). So the model-spectrum value 1.85–1.89 lies precisely in the regime where the implementation disagrees in sign with the calculation it claims to reproduce. Abstract says "shape-robust" without this conditionality.
- (C12) Table IV "Prim. tensors" row is labelled n_T=0/γ=5 while the model's own tensor tilt n_T = n_s − 1 gives γ = 5.035; harmless but the row label and text should match.
- Note: §V footnote 1 correctly flags Ω_DM = 0.674 in Choudhury Eq. (66) as coinciding with h — good catch by the authors, but a 2.55× normalization ambiguity in the tabulated f_PBH should be stated in Table V's caption too.

## Reading notes — pp. 11–15 (§VI, §VII, Appendix A, reproducibility, references)

Arithmetic checked (pass):
- §VI.A: (−2.19+3.6)/9.0 = 0.16σ; (3.5+2.19)/7.4 = 0.77σ; 2.19/9 = 0.24. Reproduce.
- Table VI: all 15 significance entries reproduce from |f_after| bands ÷ σ (e.g. 0.50–0.65/0.7 = 0.71–0.93; 1.25/0.5 = 2.49; 4.375/0.7 = 6.25). −35/8 S1 row: −4.375T + Δf_bounce → [−1.20, −0.86]. Reproduces.
- §VI.B separation: |Δf_after| = 1.20−0.65 = 0.55, 0.86−0.50 = 0.36; ÷(0.5–0.7) → 0.5–1.1σ. Reproduces.
- Appendix A3 general-ε: monopole −5(ε−3)(ε−6)/18 → −15/8; isosceles −5(ε²−6ε+12)/12 → −35/16; μ² coeff 5ε²/12 → 15/16; Eq. (A3) angular average reproduces the monopole formula. Decomposition 5ε(9−ε)/18 = 5ε(9−2ε)/36 + 5ε/4 verified algebraically; 25/8 = 5/4 + 15/8.
- Appendix A1 sketch of Eq. (5): with N = 1 + ζ̇/H and ∂²ψ/a² ⊃ εζ̇, θ/3 = H − (ε/3)ζ̇; integrating along proper time gives δN_c = (1−ε/3)ζ for constant ε and ζ(initial)=0. The sketch is internally consistent, but only a sketch.

Source-script verification (ONE claim, as permitted): the bounce-temperature ↔ k_B mapping of §V.C.
- File: research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.py (lines 243–254) and outputs/inlab_delta2_zeta_2026-09-03.json (a2_validity/k_B_Mpc-1_if_T_B_GeV).
- Committed output: k_B = 1.714e17 Mpc⁻¹ at T_B = 1e10 GeV; 1.714e21 at 1e14; 1.714e23 at 1e16 (k_B ∝ T_B, k_B ≈ 1.714e7·T_B[GeV] Mpc⁻¹). This matches the paper's p.10 statement "k_B ≈ 1.714×10^15 Mpc⁻¹ at T_B = 10^8 GeV".
- Consequence: "a_B H_B ≳ 10^17–10^18 Mpc⁻¹, i.e. T_B ≳ 10^8–10^10 GeV" (p.10, §V.C) is WRONG by two decades on both ends: 10^17–10^18 Mpc⁻¹ ⇔ T_B ≳ 10^10–10^11 GeV per the paper's own committed script. ("Eleven decades above BBN" ⇒ 10^8 GeV is likewise inconsistent: k_B(1 MeV) ≈ 1.7e4 Mpc⁻¹ by the same formula, so 10^17 Mpc⁻¹ is thirteen decades above BBN.) The script's own JSON note "For any bounce above the BBN scale, k_B >= 1e17 Mpc^-1" is also incorrect by the same formula. The null verdict is unaffected (the true condition is stronger), but the stated condition is not.

Reference spot-check (5+): [1] Cai–Xue–Brandenberger–Zhang JCAP 0905:011 arXiv:0903.0631 — correct. [3] Quintin et al. PRD 92, 063532, arXiv:1508.04141 — correct. [4] Li–Quintin–Wang–Cai JCAP 1703:031, arXiv:1612.02036 — correct. [7] Agullo–Bolliet–Sreenath PRD 97, 066021, arXiv:1712.08148 — correct. [11] NANOGrav 15-yr ApJL 951 L8, arXiv:2306.16213 — correct. [24] BICEP/Keck PRL 127, 151301 — correct. [8] Papanikolaou arXiv:2504.11641 (single author) — could not verify from memory; the known NANOGrav/matter-bounce SIGW work by this author is multi-author; authors should double-check the author list and identifier.

Figures vs text: Fig. 1 caption/legend consistent with §IV.D numbers; Fig. 2 consistent with Table V row (0.5, 1.0, 0.5) and A_* = 0.131446. One mismatch: Fig. 1 legend "NANOGrav 15yr (A = 2.4×10⁻¹⁵, γ = 3.2)" — A = 2.4e−15 is NANOGrav's γ = 13/3-fixed amplitude; the free-γ (γ = 3.2) median is A ≈ 6.4e−15, which raises Ω_GW h²(f_yr) from 3.6e−9 to ≈2.6e−8 (the "10^14.4" would become ≈10^15.2). Null unaffected; numbers inconsistent.

## Summary (5 lines)

1. The paper re-derives the matter-bounce local amplitude f_NL = −35/16 vertex-by-vertex (in-in), localizes Cai et al.'s factor of 2 to their normalization step, adds a classical O(k⁰) cross-check and a general-ε formula, and then propagates the value through three observational channels (PTA slope, PBH compaction abundance, LSS bispectrum) plus a scheme-qualified bounce transmission (S1/S2).
2. Every number I could recompute from the paper's own inputs reproduces (Tables I, III, IV, V ratios, VI; Eqs. 3–4, 7, 11–12, A2–A3); the arithmetic hygiene is excellent.
3. The scientific content of the channel sections is three honest nulls and one non-discriminating channel; that is publishable at PRD only if the consistency assessment is complete — and it omits the tensor channel (r), where the same background is quoted at r = 0.84 "open item, not adopted".
4. Two headline numbers are not yet defensible as stated: the "5.1σ" PTA tension (depends on reading NANOGrav's ±0.6 as 90% and on a Gaussian tail; amplitude taken from the wrong fit) and the "shape-robust 1.7–1.9" PBH ratio (model spectrum lies outside the scanned grid, in the regime where the implementation disagrees in sign with Choudhury et al.).
5. One quantitative condition (§V.C bounce temperature) is inconsistent with the paper's own committed script by two decades; several presentation items (S1/S2 "band" framing, §II.D "resolved" vs Appendix "identity not mechanism", thin Appendix) need work.

## Verdict: **major-revisions**

## MAJOR findings

**M1 — The tensor sector is omitted from a "multi-channel consistency assessment" of a background it would most strongly constrain (p.7 §IV.D; §I; §VII).** §IV.D writes "the unresolved r = 0.84 matter-bounce scenario (open item, not adopted)" and instead computes the first-order tensor background from the *observational* bound r < 0.036. If the dust contraction that fixes f_NL = −35/16 (Eq. 1; z ∝ a, ε = 3/2, c_s = 1 — the same background used for the S1 transmission) predicts r = O(1), BICEP/Keck+Planck [24] excludes it far more decisively than any of the three channels, and a reader is entitled to know that before the three "honest nulls". Likewise n_s = 0.9649 is inserted from Planck via w ≈ −0.003 while Eq. (1) is evaluated at w = 0. *Resolves it:* (a) state the model's own r for each of the three backgrounds (or for the dust contraction with the scheme used), compare with r < 0.036, and state the outcome as a fourth channel (even if it is "excluded unless tensors are suppressed by a mechanism outside this paper"); (b) evaluate Eq. (A3) at the ε corresponding to n_s = 0.9649 and quote the shift in f_NL (expected O(1%) but must be stated), so that the propagated spectrum and the propagated f_NL come from the same background.

**M2 — The headline PBH amplitude ratio "shape-robust 1.7–1.9" (abstract; §VII) is quoted for a regime the calculation does not cover and where it contradicts the reference calculation (pp. 8–9, Table V caption).** Table V's caption states the model's own spectrum has γ_cr ∈ [0.27, 0.63], outside the scanned grid [0.766, 0.968], and p.9 states that for γ_cr ≲ 0.85 "our implementation instead finds enhancement relative to Gaussian where they report suppression, a genuine discrepancy left unresolved". The model-spectrum value 1.85–1.89 therefore sits precisely where the implementation and Choudhury et al. [16] disagree in sign. "Shape-robust" and "reproducible" are then not established for the model's own spectrum; the abstract carries none of this conditionality. *Resolves it:* either resolve the sign discrepancy (reproduce one of Choudhury et al.'s γ_cr < 0.85 points to stated precision or identify the differing ingredient), or restrict the headline ratio to the covered grid and state in the abstract that the model-spectrum value is outside coverage and conditional on an unresolved disagreement.

**M3 — The "5.1σ" PTA slope tension (abstract; Table IV; Fig. 1) rests on three unstated or inconsistent choices (pp. 6–8).** (i) σ ≈ 0.6/1.645 = 0.365 reads NANOGrav's "γ = 3.2 ± 0.6" as a 5–95% interval; if [11] quotes a 68% interval the tension is 3.1σ. The paper must cite the exact statement in [11] fixing the convention. (ii) A Gaussian is extrapolated to a 5σ tail of a non-Gaussian, asymmetric posterior — the paper's own refit paragraph explains why such tail statements are unreliable ("extrapolating into an unsampled tail"), yet the abstract quotes 5.1 to two figures. (iii) The NANOGrav amplitude used, 3.6235e−9 (A = 2.4e−15), is the γ = 13/3-fixed fit, while the slope compared against is the free-γ posterior (A ≈ 6.4e−15). *Resolves it:* quote the tension from the actual posterior (e.g. the posterior mass beyond γ_pred from the public chain, or a tail-safe statement such as "> 4σ"), fix the convention with a citation, and use A and γ from the same NANOGrav fit (this changes "10^14.4" to ≈10^15.2).

**M4 — §V.C bounce-temperature condition is inconsistent with the paper's own mapping and committed script (p.10).** "a_B H_B ≳ 10^17–10^18 Mpc⁻¹, i.e. T_B ≳ 10^8–10^10 GeV — eleven decades above the BBN scale" conflicts with the paper's own "k_B ≈ 1.714×10^15 Mpc⁻¹ at T_B = 10^8 GeV" two paragraphs later and with `inlab_delta2_zeta_2026-09-03.py` (k_B = 1.714e17 Mpc⁻¹ at 10^10 GeV). The correct condition is T_B ≳ 10^10–10^11 GeV (thirteen decades above BBN). The null is unaffected, but a stated quantitative condition is wrong by 100×. *Resolves it:* print the k_B(T_B) formula once (k_B ≈ 1.7×10^7 T_B[GeV] Mpc⁻¹ with the g_* factors used) and recompute every T_B statement in §IV.D, §V.C, and the reproducibility JSON note.

**M5 — The "two-scheme transmitted band" (abstract; §III.A; §VII) is presented as if it bracketed an uncertainty, whereas §III.A establishes that S1 and S2 are "genuinely physically inequivalent continuations through H = 0" and §VII.C(i) admits which is physical is an unresolved theory question (pp. 4–5, 12).** In addition, scheme S1 substitutes constant ε_eff = 1/2, c_s = 1 into Maldacena's cubic action *at and through H = 0*, where ε is not defined; Eq. (7) then depends on the background only through ρ_B, which is a consequence of that assumption rather than a result. *Resolves it:* rewrite the abstract/§VII so that [−1.25, −0.50] is described as two scheme-dependent answers, not a band; give a physical argument (or a reference) for why the dressed-metric prescription with fixed ε_eff is a controlled treatment of the cubic action at H = 0; and either compute S2 on the LQC and poly backgrounds or state explicitly in the abstract that S2 exists on one background only.

## Minor findings

1. Abstract, last sentences: "SPHEREx bispectrum-only reaches 0.7–0.9σ … combining power spectrum and bispectrum widens this to 0.5–1.1σ" conflates *detection* significance with *candidate-separation* significance; as written it reads as if adding P lowers the significance. Reword.
2. §II.D says the quadrupole gap is "resolved rather than merely bounded" and "corrects it to the in-in coefficient exactly", while the abstract and Appendix A2 say the second-order piece is "recorded as … a computed identity, not a claimed mechanism". Harmonize to the Appendix's (weaker, honest) wording.
3. Appendix A "transcribes, without new science, the derivation archived in the … adjudication note": for PRD the derivation of Eq. (5) and the evaluation of boundary term (A1) must be in the paper (or a supplement), not in a repository markdown file.
4. Table IV: "Prim. tensors" row is γ_* = 5 (n_T = 0) while the model's own n_T = n_s − 1 gives 5.035; label the row as the reference case and add the model row, or use one consistently.
5. Table II: "2.1–4.4 dex" deficit cannot be checked because the ABS plateau values at each k are not tabulated; add a column.
6. The refit γ = 2.57 ± 0.38 sits 1.2σ below the official posterior; using all 30 bins (the upper bins are white-noise dominated) is a known way to bias γ low. Say so, or drop the refit columns from Table IV's headline.
7. Fig. 1 legend amplitude/slope mismatch (see M3(iii)).
8. Table V: nominal f_PBH values of 3.5×10³ and 2.2×10⁸ are unphysical (f_PBH ≤ 1); say "uncapped nominal" in the column header, not only in the caption. Also put the Ω_DM = 0.674 vs 0.264 (×2.55) normalization caveat from footnote 1 in the caption.
9. p.4 "a background-dependent excursion, a factor 0.06–2.2 (not order-unity in the strict sense)": a factor 0.058 is a 17× suppression, not an "excursion"; describe the poly result honestly.
10. p.4 vs p.5: the linear S2 transfer on LQC (T = 0.409) exists but the cubic S2 does not; the sentence "S2 has no computable post-bounce f_after on the LQC background" should say "cubic".
11. p.5, ¶ after Eq. (7): sentence beginning "so |f_after| ∈ [0.50, 0.65] …" is a fragment following "(below)." — fix.
12. Equilateral/folded values (−255/128, −9/8) and the Legendre ℓ = 2 coefficient are asserted; give the full shape function (the (5,2,2) monomial sum) in Appendix A.
13. Code is pinned to a git hash, not a DOI (authors' own note); PRD will expect a frozen archive at acceptance.
14. Ref. [8]: verify author list/identifier.
15. §VI.B: the shape-overlap r < 1 between the μ²-dependent squeezed shape and the local template is acknowledged but not computed; since it can only *reduce* every Table VI entry, label Table VI values as upper bounds in the caption.

## Questions to authors

Q1. Which statement in Ref. [11] fixes "3.2 ± 0.6" as a 90% (5–95%) interval? If it is 68%, all Table IV z_off entries change.
Q2. Which variable — ζ_Mald or δN_c — matches onto the post-bounce conserved curvature perturbation that the CMB/LSS channels measure, and is the answer scheme-dependent? Eq. (5) implies a factor-2 ambiguity in the propagated amplitude if the answer is δN_c.
Q3. What is r for each of the three backgrounds under the same S1 prescription used for f_NL, and is any of them below 0.036?
Q4. What is f_NL from Eq. (A3) at the ε that gives n_s = 0.9649 via n_s − 1 = 12w/(1+3w)?
Q5. Is the Table V mean ratio 1.732 = √3 a coincidence, or does the truncated-map structure predict √(35/8 ÷ 35/16)·(something)? A one-line explanation, if one exists, would strengthen the "robust" claim.
Q6. Table II is "lab vacuum" initial state only; the abstract says "three choices of initial vacuum state" — give the other two rows or drop the phrase.
Q7. Why is the direct-collapse PBH channel during contraction (§VII.C(v)) listed as future work when it is the one channel where the kη_B ≳ 1 enhancement of Table II (equilateral |f_NL| ≈ 10³) would operate?

## Integrity note

Reviewed only the exact PDF (sha256 c6f9bb57…1a34c) plus one committed script/JSON to verify one numerical claim (§V.C T_B↔k_B mapping); no prior reports, SSOT, dispositions, or boards were read; no verdict was suggested to me.
