# P1A R40conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1a_ech_nogo.pdf` md5=fd4707e3 pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 101.3s

---

**Referee Report**

**Paper**: P1A — Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes… (Houston Golden)

**Journal target**: Physical Review D

**Date of review**: 2025 (paper dated June 13, 2026 — already anomalous)

I have examined every rendered page, equation, table, figure, caption, and the abstract. The paper fails PRD standards on multiple independent grounds.

### ESSENTIAL findings (any one sufficient for rejection)

**P1A-E1** (Abstract, p. 1; Sec. I, p. 3)  
Abstract states “14 constraints map minimal-ECH route space” and presents \(f_{NL}=-35/8\) and \(\beta\approx0.27^\circ\) as surviving predictions. Body (Sec. IX, Table II, p. 17; Sec. IV, pp. 11–13) shows all 14 barriers are either (a) already known in the literature or (b) conditional on the explicit on-shell scaling ansatz of Appendix B that is “not a derivation.” The abstract claim is therefore stronger than the calibrated body statement.  
**Required fix**: Remove or qualify every quantitative claim in the abstract that rests on the ansatz; add the explicit caveat that appears only in Sec. XIV.

**P1A-E2** (Abstract, p. 1; Sec. I, p. 3; Sec. XV, p. 24)  
Abstract and conclusion present a “channel-level closure” of four routes. The text repeatedly states (Scope paragraph, p. 3; Sec. IV opening, p. 10) that this is *not* an operator-level theorem and that the Jackiw–Pi term and the parity-odd four-fermion partner of Route 1 are omitted. A PRD paper cannot title and abstract a result as “closure” while the body disclaims exactly that scope.  
**Required fix**: Retitle and rewrite abstract/conclusion to “amplitude-budget assessment under stated ansatz” or perform the missing operator-basis analysis.

**P1A-E3** (Multiple locations)  
The paper is not standalone. Load-bearing results are deferred to “Paper I(b) [6] (in preparation)”, “Paper II [2] (in preparation)”, and “companion MCMC verification (in preparation)”. Examples: all MCMC posteriors, NaMaster pipeline validation, ALP parameter fitting, and the numerical value of \(\sigma(f_{NL})\) after GR-projection. PRD requires a self-contained argument; citation to unpublished works for central numerical claims violates this.  
**Required fix**: Either include the missing calculations or remove all quantitative claims that depend on them.

**P1A-E4** (Sec. X, pp. 19–20; abstract)  
The “perturbation-transparency result” (Holst term vanishes identically on the Levi-Civita connection by the algebraic Bianchi identity) is presented as novel. It is a direct, one-line consequence of the first Bianchi identity on a torsion-free connection, already used in the same context by Hehl et al. (1976) and subsequent ECKS literature. The paper’s own footnote a (p. 2) acknowledges the distinction from the Pontryagin term but still advertises the result as central.  
**Required fix**: Remove the claim of novelty; reduce Sec. X to a single paragraph.

**P1A-E5** (Sec. IV D, p. 13; abstract)  
Route 4 is declared closed by a “naturalness objection rather than amplitude no-go.” The abstract nevertheless lists the spectator-ALP channel as one of the four “enumerated minimal-ECH dark-energy routes” that are closed. This is a direct contradiction.  
**Required fix**: Either drop Route 4 from the enumerated set or change the abstract language.

### MAJOR findings

**P1A-M1** (Fig. 1, p. 5; Table I, p. 4)  
Fig. 1 and Table I juxtapose \(\sigma(f_{NL})\) values and \(\beta\) significances from different null procedures without the explicit “not directly comparable” qualifier required by instruction 7 at every such juxtaposition. The single footnote on p. 4 is insufficient.

**P1A-M2** (Sec. II C, p. 7; Eq. 10)  
The identification \(\rho_\Lambda=\Xi M_{Pl}^4\) is introduced as a “phenomenological on-shell scaling ansatz.” All subsequent closure statements rest on this ansatz. No first-principles derivation or renormalization-group justification is supplied. The paper therefore does not demonstrate that the four routes are closed inside the minimal ECH theory; it shows they are closed inside a particular truncation.

**P1A-M3** (Sec. XIV A, p. 23)  
The author explicitly lists “Phenomenological \(\alpha/M\): Not derived from first principles” as a current limitation, yet the abstract and conclusion present the four-route closure as a robust result. Internal contradiction.

**P1A-M4** (Bibliography & text)  
Multiple citations to “in preparation” works are used as load-bearing evidence for numerical claims (e.g., LiteBIRD forecast, SPHEREx Fisher matrix). These cannot be verified by a standalone reader.

### MINOR / NIT findings (selected)

**P1A-N1** Future date “June 13, 2026” on title page.  
**P1A-N2** Inconsistent use of “we” vs. single-author byline.  
**P1A-N3** Fig. 5 bottom panel mixes orders-of-magnitude scales without stating the precise \(M_{Pl}\) convention used for each bar.  
**P1A-N4** Repeated phrase “not a distinctive ECH prediction” appears in Table I and Sec. XIII but is never quantified as an effect-size statement.

### Summary recommendation

**REJECT**

The manuscript is a programmatic position paper whose central claims rest on (i) an explicit phenomenological ansatz that is never derived, (ii) results deferred to unpublished companion manuscripts, and (iii) a scope that the abstract and title misrepresent. Even after the requested fixes the work would remain a methods note rather than a completed PRD article. The perturbation-transparency observation is correct but trivial; the “channel-level closure” is an assessment under stated assumptions, not a no-go theorem. The paper does not meet the standards of Physical Review D.