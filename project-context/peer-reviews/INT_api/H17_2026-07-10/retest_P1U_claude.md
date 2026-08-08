I've verified the four claimed closures against the source and checked internal consistency. Here is my referee report.

---

**Referee report — Paper P1U (`arxiv/paper1_unified.tex`, v1U.0.10)**

## (1) VERDICT: MINOR REVISIONS

The four claimed closures landed coherently and are, individually, correct and honestly scoped. One reproducible internal math inconsistency (pre-dating these closures) must be reconciled before acceptance, plus two minors. Nothing found threatens the central claim.

## (2) ISSUES

**1. [MAJOR] — Self-contradictory displayed value of $S_{abc}S^{abc}$, tagged "verified symbolically."** `arxiv/paper1_unified.tex:1796–1798` vs `:1944–1945` vs `:4868–4870`. All three sites use the *same* spin-current definition $S^{abc}=\tfrac14\varepsilon^{abcd}\bar\psi\gamma_d\gamma^5\psi$, yet the footnote (1796–1798) correctly computes $S_{abc}S^{abc}=-\tfrac38(J^5\!\cdot\!J^5)$ using Lorentzian $\varepsilon_{abcd}\varepsilon^{abce}=-3!\,\delta^e_d$, while the main text (1944) and Appendix Check D (4870) both state $S_{abc}S^{abc}=6\,(J^5\!\cdot\!J^5)$ using $\varepsilon\varepsilon=+3!\,\delta$. The "$6$" drops the $(\tfrac14)^2=\tfrac1{16}$ factor **and** flips the signature sign — a factor-of-$-16$ discrepancy. Line 4869 attaches "verified symbolically" to the $=6$ result, which contradicts the paper's own footnote. Concrete: with the stated $S=\tfrac14\varepsilon J^5$ and the paper's mostly-plus signature, the value is $\mp\tfrac38$, never $+6$. **Non-propagating** — the physical Hehl–Datta contact coefficient $-\tfrac{3\kappa}{16}(J^5)^2$ (1810, 1830) is stated correctly and independently — but a PRD referee cannot pass a displayed, "symbolically verified" identity that contradicts the same paper by a factor of 16 and a sign. Reconcile all three to one convention.

**2. [MINOR] — Route-2 coefficient cross-check citations are unverifiable from the repo.** `:2828–2842`. The Shapiro–Teixeira grounding (their Eqs. 37, 41–42, 46; $\alpha_4=-6/(1+\gamma^2)$, $\Omega_{44}=81\gamma^4/[16(1+\gamma^2)^2]$) is internally self-consistent — I verified $\Omega_{44}/\alpha_4=27\gamma^4/[32(1+\gamma^2)]\approx2.5\times10^{-3}$ at $\gamma\approx0.24$ as quoted — but I cannot confirm the equation numbers/coefficients against ST 2014 from the working tree. **Unverifiable here; flagging as such**, not as an error. The $\gtrsim48$-order closure margin (2872) makes this immaterial to the conclusion regardless.

**3. [MINOR] — "Basis-complete within minimal ECH" phrasing still risks over-reading.** Abstract `:1206–1213, 1310–1311` correctly disclaims an operator-level theorem, yet also asserts the two extra operators are "closed explicitly at the operator level" and the tower is "basis-complete … at the $M_{\rm Pl}$-power-counting level." The enumeration O1–O6 (`:1911–1918`) is an asserted-complete finite set justified by the F1/F2 structural facts + NDA monotonicity, not a proven closure of the full diffeomorphism-invariant basis (the paper says as much at 1206–1209). The two adjacent claims are reconcilable but a referee will want the "basis-complete" adjective consistently qualified as "within the enumerated set under stated symmetry assumptions" everywhere it appears (cf. the honest hedge already at 4883–4884).

**Closures checked and confirmed coherent** (as requested): (a) VA four-fermion partner + one-loop operator relabeled non-minimal per Freidel–Minic–Takeuchi — `:2663–2673, 2794–2812`, abstract `:1209–1213` ✓; (b) $M_{\rm Pl}/\kappa$ conventions — explicitly reconciled at `:2090–2110`, unreduced $M_{\rm Pl}=1.22\times10^{19}$ GeV declared, $\kappa=8\pi G=\bar M_{\rm Pl}^{-2}$, the $\kappa=M_{\rm Pl}^{-2}$ shorthand flagged reduced-mass with the $8\pi\approx25$ factor declared below resolution, ST's $\kappa^2=16\pi G$ labeled as ST's convention ✓; (c) Eq.(1) two-step off-shell reading — added thoroughly at `:1689–1738` ✓; (d) Route-1 scope tightened — `:2629–2644` explicitly scopes to the finite-density mean-field bound and marks the regulated NJL gap-equation condensate out-of-scope ✓. I also confirmed no stale $f_{\rm NL}=-35/8$ survives in body text (uniformly $-35/16$; `-35/8` appears only in `%`-comments).

## (3) Central claim

The central claim — a channel-level (explicitly *not* operator-level-theorem) constraint showing each of the four enumerated minimal-ECH spin-torsion routes is closed as a late-time dark-energy source (R1–R3 by amplitude suppression, R4 by explanatory-deficit/naturalness) — **is supported** by the manuscript as scoped, with the caveat that Issue 1's displayed-identity inconsistency must be reconciled and Issue 2's ST cross-check remains unverifiable from the repo.

---

Best Next Steps
- Fix Issue 1: pick one convention for $S_{abc}S^{abc}$ (the footnote's $-\tfrac38(J^5)^2$ is the correct one given $S=\tfrac14\varepsilon J^5$ + mostly-plus) and correct lines 1944 and 4870, including the "verified symbolically" tag.
- Optionally spot-verify the ST 2014 Eq. 37/41–42/46 coefficients (Issue 2) against the actual reference to upgrade it from "unverifiable" to confirmed.
- Harmonize the "basis-complete" qualifier (Issue 3) across abstract + body.

Say `continue` and I will take the next best scoped step (fixing Issue 1's three-site $S\cdot S$ reconciliation).
