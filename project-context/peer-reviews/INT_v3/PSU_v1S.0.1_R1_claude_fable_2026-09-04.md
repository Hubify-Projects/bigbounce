# PSU v1S.0.1 — R1 independent referee report (Claude Fable 5.1, INT leg)

- PDF: site/public/papers/paper_su_criterion_v1S.0.1.pdf
- sha256: cc0dfb84a232967c45ea359d5de18f642af0727c2907512b289931854ed7c48e
- Pages: 4
- Date: 2026-09-04
- Venue standard: Physical Review D (Letter / short-note)
- Reviewer stance: independent, skeptical; no review history / SSOT / dispositions / source notes consulted; claims verified by own derivation (sympy where noted).

## Summary

1. The note states an exact linear "threading identity" delta N_c = zeta - (1/3) int d_i N^i dt along fluid worldlines, reduces it on super-Hubble scales (d_i N^i = (eps/c_s^2) zeta-dot, which I confirm from the Maldacena/Chen et al. constraint lap chi = a^2 (eps/c_s^2) zeta-dot) to delta N_c = lambda zeta, lambda = 1 - <eps/c_s^2>_zeta / 3, and adds a second-order map f_map = -(5 eps/4)(1 - mu^2) at constant eps, c_s = 1.
2. Algebra I could check passes: lambda(w) = (1-w)/2, f_map^mono = -(5/4)(1+w), lambda_USR = 1 + eps_f/3 - sqrt(eps_s eps_f)/3 (sympy), the dust growing mode zeta ∝ 1/t, and the 8/3 = (-5)/(-15/8) headline ratio (angle-averaged in-in monopole).
3. The load-bearing content -- the isotropic-delta N value f_dN = -5 and the in-in input -35/16 + (15/16) mu^2 -- is not derived in the note; both are imported from two unpublished self-citations ([18], [19], GitHub markdown). The published matter-contraction in-in result (Cai, Xue, Brandenberger, Zhang 2009, f_NL = -35/8 squeezed) is neither cited nor reconciled; it differs by a factor of 2 from the input used here, and the entire O(1) claim (gap 25/8, factor 8/3) depends on that input.
4. The stated second-order composition f_dN = f_inin/lambda + f_map is contradicted by the note's own numbers at the quadrupole: for dust it evaluates to -25/4 + (15/4) mu^2, whereas the delta N value is the isotropic -5. Only the angle average agrees. The identity is therefore a monopole statement, not the mu-resolved identity written in Sec. II.
5. Novelty is real but narrower than claimed: the shift-divergence term in the local expansion is the O(k^0) piece of the gradient expansion that the "beyond delta N" gradient-expansion literature (Takamizu-Mukohyama-Kobayashi-Tanaka 2010; Naruko-Takamizu-Sasaki 2013) already tracks; the note's contribution is the observation that it is unsuppressed when zeta grows with eps = O(1). The USR statement is consistent with NFS (agreement at leading order, correction O(eps)).

## Verdict

**major-revisions**

## MAJOR findings

**M1 (p.1 Sec. I; p.2 Table I; abstract) -- the O(1) failure rests on an uncited, unpublished in-in input that disagrees by a factor 2 with the published result.**
The in-in squeezed bispectrum of zeta in a matter-dominated contraction is taken as -35/16 + (15/16) mu^2 "[18]", where [18] is the author's own GitHub markdown. The peer-reviewed calculation for exactly this background (Cai, Xue, Brandenberger, Zhang, JCAP 0905:011, arXiv:0903.0631) reports f_NL = -35/8 in the squeezed/local limit. If -35/8 is the monopole, the "gap" becomes -5 - (-35/8) = -5/8 and the "factor 8/3" becomes 8/7, i.e. the headline collapses from an O(1) failure to a ~14% effect. The note must (a) cite Cai et al. 2009, (b) state the normalisation/convention that maps their -35/8 to the note's -15/8 monopole, and (c) either reproduce the -35/16 + (15/16) mu^2 kernel in an appendix or in a peer-reviewable form. A PRD referee cannot accept an O(1) claim whose sole numerical input is a self-cited markdown file.

**M2 (p.2 Eq. (3) and the sentence "f_dN = f_inin/lambda + f_map") -- the second-order composition is false at the quadrupole; it only holds angle-averaged.**
Own check (sympy): with lambda = 1/2, f_inin = -35/16 + (15/16) mu^2, f_map = -(15/8)(1 - mu^2): f_inin/lambda + f_map = -25/4 + (15/4) mu^2. The isotropic separate-universe value in Table I is -5 with no mu dependence. The mu^2 coefficients (15/8 from the in-in, +15/8 from the map) add rather than cancel; only the angle average (-5) matches. Either (i) the in-in quadrupole sign/magnitude is wrong, (ii) f_map's angular structure is wrong, or (iii) the composition is only meant for the monopole (as the Fig. 1 caption's "f_map^mono" hints). The text must say which, and Eq. (3) must not be presented as a mu-resolved identity if it is (iii). As written, the note's own numbers refute its own equation.

**M3 (p.1 Sec. II, one sentence: "The zero-shift threading computed by the separate universe is the fluid (normal) congruence") -- the central identification delta N_c = separate-universe delta N is asserted, not derived, and the "-5 (initial-position label)" is convention-dependent and undefined.**
Eq. (1) is a correct identity for the volume e-fold count along fluid worldlines (I agree: with x-dot^i = -N^i the worldline-total derivative absorbs N^i d_i zeta, and the -(1/3) d_i N^i is the trace of the shift's strain on the volume element). But the claim that the isotropic delta N(phi, pi) computes *this* quantity rather than Maldacena's zeta is the whole content of the note and is supported by one sentence. My own attempt at the separate-universe count for the constant-eps contraction growing mode (which at k -> 0 is exactly the time-shift solution, delta phi = phi-dot delta t, zeta = -H delta t ∝ 1/t, verified to solve zeta'' + 2(z'/z) zeta' = 0) gives delta N = -ln[a(t_i + delta t)/a(t_i)] = zeta(t_i): the result depends on the initial-slice time and has no quadratic term in delta phi at fixed t_i -- i.e. the "isotropic delta N" value for this background depends entirely on the labelling convention ("initial-position label" is named but never defined). The note must define the label, derive delta N_c = delta N(phi, pi) explicitly (not by citation to [19]), and show why the -5 is label-independent -- or state that it is not.

**M4 (abstract "exact for any history"; p.1 Eq. (1)-(2) lower limit -infinity, zeta_L(-infinity) = 0) -- the linear criterion is not exact for any history; it drops the horizon-crossing contribution and is ill-defined for attractors.**
The full super-Hubble reduction is d_i N^i = -(1/a^2 H) lap zeta + (eps/c_s^2) zeta-dot. Eq. (2) keeps only the second term. The first term integrates to int (k^2/a^2 H^2) zeta dN, which is O(1) x zeta over the ~1 e-fold of horizon crossing, exactly where zeta grows from zero to its frozen value. Started from zeta_L(-infinity) = 0, the attractor case is therefore *not* the identity map at O(1); it is the identity only if the count starts from a super-Hubble flat slice t_i after crossing (the standard delta N convention), with <X>_zeta normalised by zeta(t_f) - zeta(t_i). For the attractor and ekpyrotic rows of Table I the definition <X>_zeta = int X d zeta / zeta(t_f) with d zeta = 0 and zeta(-infinity) = 0 is 0/0 as written. Fix: define the map from a super-Hubble initial slice, state "exact on super-Hubble scales for any history", and rewrite the normalisation.

**M5 (Sec. III/IV framing vs. Sec. II content) -- "failure" vs "explicit exact map" are mutually exclusive framings; abstract claims the former, body delivers the latter.**
If delta N_c and zeta are related by an explicit, exact, invertible map (Eqs. (2)-(3)), the separate universe does not "fail" -- it computes a different, equally well-defined variable, and the physics (which variable is conserved/observable through the bounce) is untouched. The abstract ("fails by a factor of 8/3", "second, independent failure mode") and the title assert a failure; the body's Eq. (2) makes it a change of variable. The note should state which variable is physical for the contraction-to-expansion observable and *why* delta N_c is the wrong one, or retitle as a threading map.

**M6 (Sec. IV novelty vs. Refs. [11,12] and uncited gradient-expansion work) -- the shift-divergence term in the local expansion is not new; the novelty is only its non-suppression when eps zeta-dot = O(1).**
The term -(1/3) d_i N^i in theta is the standard next-to-leading gradient-expansion term already carried by "beyond delta N" (Takamizu, Mukohyama, Kobayashi, Tanaka, JCAP 1006:019, arXiv:1004.1870; Naruko, Takamizu, Sasaki, JCAP 1304:037, arXiv:1210.6525) and by the Hamiltonian separate-universe treatment of Artigas-Grain-Vennin [11]. What is new here is the statement that with zeta ∝ growing and eps = O(1) this term is O(k^0). Sec. IV must cite the gradient-expansion literature and position the claim as "the known NLO term is LO in a non-attractor contraction", not as a newly identified failure mode.

## Minor findings

m1. Abstract "factor of 8/3" is never derivable from the body: the body prints -5 and -35/16 + (15/16) mu^2 but never the angle-averaged monopole -15/8. Print it (Table I column "f_inin^mono").
m2. p.2 Fig. 1 caption / Sec. II: "at w = 1 (kination) ... the in-in monopole itself vanishes" -- unsupported, no citation or derivation; either cite or drop.
m3. Sec. II: lambda_USR = 1 + eps_f/3 - sqrt(eps_s eps_f)/3 assumes zeta ∝ a^3 from zeta = 0 at a_s; in a slow-roll -> USR transition zeta_L(a_s) is the frozen slow-roll value, not zero. State the assumption (pure USR / a^3-mode dominance) explicitly.
m4. Table I "USR: f_inin = 5/2, f_dN = 5/2, agree to O(eps)": NFS's 5/2 is itself leading order in eps, so O(eps) agreement is a statement about the map, not a test against NFS -- say so; it is currently phrased as if NFS constrained the correction.
m5. Ekpyrosis row: "passes (zeta on constant mode)" -- with zeta-dot = 0 the criterion is trivially satisfied; the row tests the definition, not the criterion. The genuinely non-trivial ekpyrotic test is the two-field/entropic case where zeta is sourced on super-Hubble scales; either add it or mark the row as a consistency check.
m6. Sec. II "every one of the five geometric contributions to f_map carries an explicit overall factor of eps [19]" -- the five contributions are not listed in the note; a PRD reader cannot audit this. One equation or a footnote listing them is needed.
m7. Reproducibility statement: file paths break mid-token ("secon d order", "experim ents") and the script name in Sec. III breaks across three lines with stray spacing. Use \url{} / \path{} with allowed breaks or a footnote.
m8. Ref. [12] "M. G. Jackson et al., arXiv:2311.03281" -- give the full author list and journal (JCAP 2024) per PRD style; Refs. [18],[19] are GitHub blobs and should be labelled as unpublished notes with a commit hash, not as citable works.
m9. The AI-usage disclosure says "all physics content ... verified by the author against the committed script output"; scripts verify algebra, not the identification in M3. Rephrase honestly.
m10. Dimensions/notation: <eps>_zeta is defined as the mean of eps/c_s^2 in Table I caption but written <eps/c_s^2>_zeta elsewhere; unify. Theta in Sec. IV is defined only in passing.

## Questions to authors

Q1. What exactly is the "initial-position label", and does f_dN = -5 change under the "final-position" or "N(phi,pi)-at-fixed-t_i" labels? If it does, which one is the isotropic separate universe of the title?
Q2. How do you reconcile -35/16 + (15/16) mu^2 with Cai et al. 2009's -35/8? Same normalisation of f_NL (B = (6/5) f_NL P P)? Same sign convention for zeta?
Q3. Is Eq. (3)'s composition meant to hold at each mu or only after angle averaging? If the former, which term supplies the missing -(15/4) mu^2?
Q4. Does the c_s != 1 fluid case change lambda? Eq. (2) claims exactness for any c_s, but the momentum constraint d_i N^i = (eps/c_s^2) zeta-dot assumes the P(X) form; a genuine fluid with non-adiabatic pressure would add a term. State the class of matter for which Eq. (2) holds.
Q5. For the attractor row, from which slice is <X>_zeta counted (see M4)?

## Integrity note

Independent review of the exact PDF (sha256 above); no repo history, SSOT, dispositions or source notes read; every checked equation re-derived here with sympy (lambda(w), f_map^mono, lambda_USR, dust growing mode, f_inin/lambda + f_map composition); the Cai et al. 2009 value and the gradient-expansion references are from the reviewer's own literature knowledge and should be confirmed against the papers before closure.
