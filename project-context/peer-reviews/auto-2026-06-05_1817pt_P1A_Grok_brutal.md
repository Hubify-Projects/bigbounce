# P1A auto-2026-06-05_1817pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 116.1s

---

**Referee Report**

**Paper:** P1A — Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes… (Houston Golden)

**Journal:** Physical Review D (adversarial first-read audit)

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P1A-E1**  
Section I (p. 3), abstract, and Sec. IV (p. 8): The central claim is a “channel-level closure” of four enumerated minimal-ECH routes “at the amplitude level.” The text explicitly states this is *not* an operator-level theorem and that the Jackiw–Pi term and the parity-odd four-fermion partner of Route 1 are “excluded from the enumeration” and “left to a follow-up operator-level analysis.”  
**Required fix:** Either (a) perform the operator-level closure or (b) remove every sentence that presents the result as a no-go theorem for minimal ECH. The present wording is false advertising.

**P1A-E2**  
Abstract, Table I (p. 4), and Sec. XIII (p. 16): The headline numbers \(f_{\rm NL}=-35/8\) and \(\beta\approx0.27^\circ\) are advertised as “surviving predictions” of the ECH framework. Both are explicitly identified in the body as properties of the *matter-bounce class* or of a generic spectator ALP, not as outputs of the ECH action. The paper never derives either number from the Holst term or from the four enumerated routes.  
**Required fix:** Remove both numbers from the abstract and from all summary tables/figures that label them “ECH predictions.”

**P1A-E3**  
Throughout (especially Secs. II C, IV, IX–XI and Appendix B): Every load-bearing step (the \(\rho_\Lambda\) scaling ansatz Eq. (B2), the \(\mathcal{D}_{\rm inf}\) dilution factor, the one-loop coefficient \(\alpha/M\), the \(N_{\rm tot}\approx92\) bookkeeping) is introduced with the explicit disclaimer “we treat this as an ansatz, not a derivation.” The 13 “logically independent barriers” are therefore conditional on unproven phenomenological inputs. A PRD paper cannot claim a structural no-go theorem whose premises are admitted ansätze.

**P1A-E4**  
References and text (pp. 3, 6, 15, 18): The MCMC verification, NaMaster pipeline validation, ALP parameter fitting, and the \(\sigma(f_{\rm NL})\) forecast are all relegated to “companion papers in preparation” ([2], [6], Paper I(b), Paper II, Paper III, Paper IV). A standalone submission to PRD must contain, or have already published, the statistical evidence for its headline claims.

**P1A-E5**  
Sec. X (p. 14) and abstract: The “perturbation-transparency theorem” is stated only for *canonical scalar matter*. The paper never demonstrates that the same decoupling holds once the omitted parity-odd operators or non-minimal fermion couplings are restored. The theorem as written therefore does not close the routes it claims to close.

### MAJOR findings (significant revision required)

**P1A-M1**  
Dimensional analysis (Appendix B, p. 19): The parity-odd operator (Eq. 6) is assigned off-shell mass dimension +1. The text acknowledges that a local Lagrangian density must have dimension +4. The subsequent claim that the operator “acquires its \(\rho_\Lambda\) mapping only through on-shell evaluation” is an evasion, not a resolution.

**P1A-M2**  
Fig. 1 and Table II (pp. 4, 13): The diagram and the 14-barrier catalog mix ECH-specific barriers with generic statements true of any bounce cosmology (e.g., “attractor-sensitivity dilemma,” “parameter immunity”). The figure caption does not distinguish the two classes.

**P1A-M3**  
Sec. III B and Paper IV citation (p. 8): The galaxy-spin “null result” is presented as supporting the ECH framework. The same section notes that the observed dipole is >100 orders of magnitude below the ECH prediction. A null result that falsifies the model’s amplitude by 100 orders cannot be advertised as supportive.

**P1A-M4**  
Sec. II A 2 (p. 6) and Eq. (7): The one-loop estimate for \(\alpha/M\) is taken from an SU(2) scheme whose uncertainty is stated to be “scheme dependence rather than a statistical or theoretical error.” Using a scheme-dependent number as the sole justification for a \(10^{-21}\,{\rm GeV}^{-1}\) coupling is not rigorous.

### MINOR / NIT findings

**P1A-m1** (MINOR)  
Date on title page: “Dated: June 2, 2026 PDT.” A submission containing a future date is an administrative red flag.

**P1A-m2** (MINOR)  
Repeated self-citation to “Paper I(b)”, “Paper II”, etc., without arXiv numbers or DOIs makes the reference list non-self-contained.

**P1A-m3** (NIT)  
Several figure captions (Fig. 1, Fig. 2) contain parenthetical asides that belong in the main text or footnotes.

**P1A-m4** (NIT)  
Inconsistent use of “we do not claim a full operator-basis closure” (abstract) versus “the four enumerated channels … close” (abstract and Sec. IV). The wording should be uniform.

### Summary recommendation

**REJECT**

The manuscript advertises a “channel-level closure” theorem whose central steps are explicitly labeled ansätze, whose headline numerical predictions are not derived from the ECH sector, and whose statistical support resides entirely in unpublished companion papers. Until the operator-level calculation is performed, the ansätze are replaced by derivations, and the statistical evidence is made self-contained and published, the paper does not meet the standards of Physical Review D.