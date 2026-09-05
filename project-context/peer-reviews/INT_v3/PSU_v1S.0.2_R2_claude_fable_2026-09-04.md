# INT referee report — PSU (separate-universe criterion note) v1S.0.2, round R2

- Reviewer: Claude (Fable 5.1) INT leg, independent skeptical PRD short-note referee
- Date: 2026-09-04
- Artifact reviewed: `arxiv/paper_su_criterion/main.pdf` (== `site/public/papers/paper_su_criterion_v1S.0.2.pdf`)
- SHA-256: `812dbaf1af7e8eafa5769730fed55c81cfa8b429fbeab022d1125be1527aca31`
- Pages: 4 (all read: text extracted + rendered to PNG for figure/table inspection)
- Method: no repo review history, SSOT, dispositions or prior reports consulted; claims re-derived independently (sympy) where checkable; not told an expected verdict.
- Venue bar: Physical Review D, short note (Brief Report length).

## Summary (5 lines)

1. The note claims the isotropic separate universe returns the fluid-worldline e-fold count δN_c (initial-position label), related to Maldacena's comoving ζ by δN_c = ζ_L,f[1 − I/3] + O(k_L²/a²H²); at second order a label-dependent map (Eqs. 3–5) composes the from-scratch in-in bispectrum into the separate-universe value −5.
2. I re-derived Eq. (1) exactly from θ = ∇_μ u^μ for u^μ = (1/N, −N^i/N) on h_ij = a²e^{2ζ}δ_ij, and confirmed the linear map by an independent route (Friedmann on uniform-φ slices with lapse 1 + ζ̇/H gives δH_loc/H = −(ε/3)ζ̇/H, matching H + ζ̇ − ∂_iN^i/3 with ∂_iN^i = εζ̇). The linear content is correct and, in my judgement, a genuinely useful clarification.
3. The composition algebra (Eqs. 3, 5; the −5 for every constant ε; λ_USR; the general-ε monopole) checks in sympy — but Eq. (4)'s second equality has a sign error, and the second-order kernels themselves are not derivable from the manuscript (they live in an unpublished GitHub note).
4. The load-bearing inputs (from-scratch in-in −35/16 + (15/16)μ², the separate-universe −5, the factor-2 claim against Cai et al. 2009) are all the author's unpublished notes; the manuscript contradicts a published result without showing why, and its own robustness sentence is arithmetically inconsistent.
5. Abstract misstates the headline number (calls −5 "the in-in monopole"); references [6], [11], [12] contain errors, and the most relevant prior work on the validity of the separate universe (Dai–Pajer–Schmidt, "On separate universes") is mis-cited rather than engaged.

## Verdict

**MAJOR REVISIONS.** The core identity and linear criterion are right and worth publishing as a short note; the second-order/validation layer and the literature layer are not yet at PRD standard.

## MAJOR

**M1 — Abstract misstates the headline number (p.1, abstract, sentence 4).** "the initial-position label ... reproduces the in-in monopole exactly, −5, for every constant ε". −5 is the *separate-universe* value (Sec. I, Sec. III, Table I: f_δN^init = −5); the in-in monopole is −(5/18)(ε−3)(ε−6) = −15/8 at ε = 3/2 (p.2 col.2, p.3). The abstract therefore asserts the opposite of the body on the one number the note is about. *Resolves:* "reproduces the isotropic separate-universe value, −5, for every constant ε, from the in-in bispectrum and the map".

**M2 — Sign error in Eq. (4), second equality (p.2).** With Eq. (3) f_map^init = 5ε/(4(3−ε))[(ε−2) − εμ²] and f_map^fin = −(5ε/4)(1−μ²), direct subtraction gives f_map^fin − f_map^init = −5ε/(4(3−ε))(1−3μ²), not +5ε/(4(3−ε))(1−3μ²) as printed (check at ε=3/2: f^fin − f^init = −5/4 + (15/4)μ² = −(5/4)(1−3μ²)). The zero-monopole conclusion and the ε=3/2 numbers (−25/4 + (15/4)μ²) are unaffected, but a printed closed form must be right. *Resolves:* flip the sign; re-run the sympy gate on the printed Eq. (4) itself (the script asserts the composed totals, not this displayed difference).

**M3 — The second-order content is not derivable from the manuscript; "identity vs fit" cannot be judged by a reader (p.2, Eqs. 3–5; p.3 Reproducibility).** Eqs. (3)–(4) are stated as results of "solving the exact ADM constraints to O(ζ_Lζ_S) and integrating Eq. (1)", with the derivation only in an unpublished GitHub note [22]. The "for every constant ε" isotropy of f_δN^init additionally requires the general-ε in-in *shape* (5/12)(ε²μ² − ε² + 6ε − 12) — the μ² coefficient 5ε²/12 — which the note never prints (only its monopole appears, p.2). I verified that the composition f^{in-in}/λ + f_map^init ≡ −5 holds *given* those two inputs; I could not verify the kernels themselves. As written, a referee cannot distinguish an independently derived map from one tuned to the lab's own −5. *Resolves:* an appendix with (i) the second-order lapse/shift solution used, (ii) the five kernel contributions listed in footnote 1 with their closed forms, (iii) the general-ε in-in shape with its source, and (iv) an explicit statement that the map derivation uses no in-in or δN input.

**M4 — Factor-2 dispute with Cai et al. 2009 asserted without evidence, later literature uncited, and the robustness sentence is arithmetically inconsistent (p.1 col.2).** (a) The note states the published −35/8 is "uniformly a factor of 2 smaller" in the from-scratch calculation and that [21] "locates the slip in their amplitude step" — a claim that a published PRD/JCAP result is wrong, supported only by the author's unpublished note. The later recomputation by Li, Quintin, Wang & Cai (arXiv:1612.02036, JCAP 2017), which reproduces the canonical-limit squeezed value, is not cited or addressed. (b) "Were −35/8 the correct in-in monopole instead of −15/8, the gap ... would be −5/8, a factor of 8/7": this treats −35/8 as a *monopole*; but if the from-scratch shape were uniformly ×2 the monopole would be −15/4, gap −5/4, ratio 4/3 (sympy-checked). (c) "the headline O(1) statement of this note rests on the from-scratch value" is wrong in the other direction: the linear criterion λ = 1 − ε/3 = 1/2 is independent of any bispectrum; only the exact −5 composition depends on the in-in input. *Resolves:* either present the located error in Cai et al. (equation-level) in an appendix, or downgrade the statement to "differs from [18]"; cite and address 1612.02036; fix the arithmetic; separate the linear (bispectrum-independent) claim from the second-order composition claim.

**M5 — Validation claims exceed what was computed (abstract; Sec. III; Table I).** Of the four rows, attractor and ekpyrosis have I = 0 by definition (the note concedes the ekpyrotic row "is a consistency check on the definition of I rather than a nontrivial test"); the USR row lists f_δN^init = 5/2 "agree to O(ε)" although Sec. V admits no time-dependent-ε second-order calculation was attempted and the linear correction is O(√(ε_sε_f)), not computed or tabulated; the sole nontrivial row (dust) validates the composition against the lab's own unpublished δN number. "We validate on four backgrounds" should become "one nontrivial check plus three consistency limits". *Resolves:* reword abstract/Sec. III; in Table I replace the USR f_δN^init entry by the note's own prediction 5/2 + O(√(ε_sε_f)) with the leading coefficient, or mark it "not computed here (NFS value)".

**M6 — Reference errors on the most relevant prior work; novelty section built on a mis-citation (p.3 Sec. IV; refs [6], [11], [12]).** [6] pairs "JCAP 1511, 043" with arXiv:1504.00351; to my knowledge 1504.00351 is Dai–Pajer–Schmidt "On separate universes" (JCAP 1510, 059) while the conformal-Fermi-coordinate paper the text describes is arXiv:1502.02011 (JCAP 1511, 043). "On separate universes" is precisely the paper that states when a long mode is a local FRW (curvature + time shift, with the tidal/anisotropic remainder), and the note's Sec. IV neither cites nor engages it. [11] should read D. Artigas, J. Grain, V. Vennin; [12] first author is J. H. P. Jackson (with Assadullahi, Gow, Koyama, Vennin, Wands). *Resolves:* correct all three; add a paragraph in Sec. IV placing the I-criterion against DPS "On separate universes" (which of their assumptions fails when I = O(1)?).

## Minor

1. p.2 col.1: "I = 1 − λ reduces to ε/3 for constant ε" contradicts Eq. (2) and Table I (I = ε, 1 − λ = I/3 = ε/3). Rewrite as "1 − λ = I/3 reduces to ε/3".
2. "dust" (Table I, Sec. I, Sec. III) is used for a c_s = 1 scalar-field w = 0 background; for a true dust fluid c_s → 0 and the printed I = ζ^{-1}∫(ε/c_s²)ζ̇ dt diverges. Label the row "w = 0 scalar field (c_s = 1)" and say what the criterion predicts for genuine dust, which is the case Cai et al. also discuss.
3. Abstract: "an exact, invertible change of variable" — Eq. (2) is linear order, super-Hubble, and by the note's own companion the second-order map is non-local and time-dependent. Say "exact at linear order on super-Hubble scales".
4. Eq. (2) is claimed "exact ... for any single-field history from a flat, super-Hubble initial slice"; the split at the comoving slice through x_i is exact at linear order for any history (the flat→comoving leg contributes ζ_L,i + O(ζ²)) but the second-order treatment assumes ζ_L(t_i) = 0 (pure growing mode from −∞). State this explicitly.
5. p.3: "the two coincide only in the limit ε → 0" applies the growing-mode formula −(5/18)(ε−3)(ε−6) (→ −5 at ε → 0) outside its domain; in the attractor limit the in-in value is Maldacena's (5/12)(1−n_s), not −5. Delete or qualify.
6. Kination statements (Fig. 1 caption, p.2 col.2): at ε = 3 the constant-ε "growing" mode has m = 3/ε − 1 = 0, i.e. it is the constant mode with ζ̇_L = 0 and I = 0, so λ → 0 is a formal limit of the ε-formula, not a property of δN_c. Qualify or drop.
7. Θ ≡ εζ̇_L/(Hζ_L) appears first in Sec. IV without definition; define it or remove.
8. Fig. 1 plots two straight lines that coincide after axis rescaling (λ = (1−w)/2, f^mono = −(5/4)(1+w)); it conveys nothing beyond Eq. (5). Replace with something informative (e.g. λ_USR(ε_s, ε_f) or I(t) along the four histories) or drop.
9. State explicitly that the final slice is uniform-φ (= comoving) and that it differs from the uniform-density slice at O(k⁰) whenever I = O(1) (δρ_c ∝ ∂_iN^i), so Lyth–Malik–Sasaki's δN = ζ_ud theorem is not the object being compared. This is a second O(1) slice ambiguity the text currently leaves implicit.
10. Table I, ekpyrosis row: "attractor-like" is not a value; give the Creminelli–Nicolis–Zaldarriaga statement (constant mode, blue spectrum) or mark "not applicable".
11. USR: "I = O(ε)" — the exact result is I = √(ε_sε_f) − ε_f, which is ≫ ε_f; say O(√(ε_sε_f)).
12. Reproducibility paragraph: file paths break mid-word across lines ("...criterion_2026_09_04.p / y", "...secon / d_order..."); use \url or a macro with allowed breaks.
13. Eq. (1): note that ∂_iN^i is the coordinate divergence of the contravariant shift and that "fluid (normal) congruence" presumes u^μ ∥ n^μ (true for a single scalar field, not for a general fluid with vorticity).

## Questions for the author

Q1. In [21], to which final slice (uniform φ or uniform ρ) is the −5 computed, and is it the same number on both? The two slices differ at O(k⁰) here.
Q2. Does f_map^init change if ζ_L carries a constant piece in addition to the growing mode (I < ε)? The general-history statement in Sec. III suggests it should; the kernels are only given at constant ε with a pure power law.
Q3. Can λ_USR be checked against an exact numerical USR δN(φ, π) at finite ε_s (e.g. ε_s = 10⁻², ε_f = 10⁻⁶ gives λ − 1 ≈ −3×10⁻⁵)? That would turn the USR row into a real validation.
Q4. Was the second-order map derivation performed without any in-in or δN input (the script comment "read only now" suggests yes) — please state so in the paper.

## Integrity note

- Reviewed exactly `arxiv/paper_su_criterion/main.pdf`, SHA-256 812dbaf1…aca31, byte-identical to the served v1S.0.2 copy; all 4 pages read (text + rendered images for Fig. 1 and Table I).
- No prior referee reports, SSOT, dispositions or review history consulted; no expected verdict was given to me.
- To decide "identity vs fit" I inspected the cited reproducibility artifacts `research/theory_audit/threading_map_second_order_2026_09_04.py`, `separate_universe_failure_criterion_2026_09_04.py`, and grep-level excerpts of the cited note [21] — as a referee would open a cited supplement. I did not run the (slow) second-order solve; I did not re-derive the kernels.
- My own sympy checks (scratchpad `ref_check.py`): composition f^{in-in}/λ + f_map^init = −5 ∀ε; final-label composition and its −5 monopole; monopoles −5ε/6; Eq. (5); λ_USR; the Eq. (4) sign; the "×2" robustness arithmetic. Hand derivations: Eq. (1) from ∇_μu^μ; linear map from Friedmann on uniform-φ slices.
- Reference-detail claims in M6 are from memory of the arXiv listings and should be confirmed against the arXiv records before closure.
- Nothing in this report was written to a git commit.
