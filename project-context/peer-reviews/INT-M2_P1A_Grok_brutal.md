# P1A INT-M2 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=a80102d5 pages=32
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 78.0s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Physical Review D

**Date of report:** Current submission

### ESSENTIAL findings

**P1A-E1**  
**Section:** Abstract (p. 1) + Sec. I (p. 3) + Scope paragraph (p. 11)  
**Problem:** The abstract states that the four routes “are closed” and that the perturbation-transparency result holds, yet the body repeatedly qualifies every closure as holding only “under the stated assumptions,” only at “channel-level amplitude-budget granularity,” only for a “phenomenological on-shell scaling ansatz” that is “not a derivation,” and only after excluding the Jackiw–Pi term and the parity-odd four-fermion partner of Route 1. No sentence in the abstract carries these caveats.  
**Required fix:** Rewrite the abstract so that every quantitative claim is no stronger than the final calibrated statement in Sec. IV and Sec. X.

**P1A-E2**  
**Section:** Entire manuscript (multiple locations, e.g., p. 2, p. 6, p. 15, p. 16)  
**Problem:** Every load-bearing numerical result (MCMC posteriors, Fisher forecasts, \(\sigma(f_{NL})\) values, \(\beta\) measurements, \(\gamma_{PTA}\)) is imported from “Paper I(b) [6]”, “Paper II [2]”, or works “in preparation.” The paper is not self-contained; a standalone reader cannot audit the central claims.  
**Required fix:** Either absorb the essential numerical content or remove all quantitative headline numbers that rest on unavailable companions.

**P1A-E3**  
**Section:** p. 1 (date line)  
**Problem:** The paper is dated “June 28, 2026.” This is chronologically impossible for a current submission.  
**Required fix:** Correct the date.

**P1A-E4**  
**Section:** Sec. II A 2 (p. 7) and Appendix B (referenced p. 25)  
**Problem:** The parity-odd operator (Eq. 6) is assigned off-shell mass dimension +1 by an explicit scaling ansatz that the author states is “not a derivation.” All subsequent amplitude-budget closures and the “+1 vs +4” counting rest on this ansatz. The paper nevertheless presents the closures as structural results.  
**Required fix:** Either promote the ansatz to a controlled EFT calculation with explicit power counting or downgrade every closure claim to “conditional on the ansatz.”

### MAJOR findings

**P1A-M1**  
**Section:** Sec. IV Scope paragraph (p. 11) and Sec. IX (p. 16)  
**Problem:** The title and abstract speak of “closure,” yet the text explicitly disclaims operator-level closure and leaves the Jackiw–Pi term and the leading four-fermion partner of Route 1 for “a follow-up operator-level analysis.” The mismatch between title language and actual scope is material.

**P1A-M2**  
**Section:** Sec. X (p. 19–21)  
**Problem:** The Bianchi-identity argument that the Holst dual contraction vanishes is performed only on a torsion-free Levi-Civita connection (\(T=0\)). The paper then claims the Holst sector “decouples from all scalar/tensor perturbation equations of motion.” This is true only inside the torsion-free sector; the claim is not demonstrated for the dynamical-torsion case that defines ECH.

**P1A-M3**  
**Section:** Table I (p. 5) and abstract  
**Problem:** The entry “Testable prediction? Yes, class-level” for \(f_{NL}=-35/8\) is sourced from a companion Fisher forecast whose systematics budget is not reproduced here. The 2.6–5\(\sigma\) range quoted cannot be recomputed from any table or equation in the present manuscript.

**P1A-M4**  
**Section:** Sec. IV D (p. 14) and Sec. IV Scope (p. 11)  
**Problem:** Route 4 is declared closed by a “naturalness/explanatory-deficit objection rather than amplitude no-go.” This is an aesthetic argument, not a dynamical obstruction. Treating it as equivalent to the amplitude-suppression closures of Routes 1–3 is inconsistent.

### MINOR findings

**P1A-m1**  
**Section:** Multiple figure captions (e.g., Fig. 1 p. 6)  
**Problem:** Several arrows labeled “structurally closed (this paper)” point to routes whose closure is only at channel level under the scaling ansatz. Caption language is therefore stronger than the text.

**P1A-m2**  
**Section:** p. 2 (PACS numbers)  
**Problem:** The PACS line contains a typographical artifact (“95.36.+x” with a stray “x”).

### NIT findings

None that rise above cosmetic.

### Summary recommendation

**REJECT**

The manuscript cannot be evaluated as a standalone contribution. Its headline results rest on (i) an explicit phenomenological scaling ansatz that is never promoted to a controlled calculation, (ii) multiple “in-preparation” companion papers that supply every numerical claim, and (iii) an abstract whose quantitative assertions are materially stronger than the qualified statements in the body. In addition, the paper carries an impossible future date. These defects are structural; they are not remediable by minor revision. The work may become publishable only after the ansatz is either justified or removed, the numerical content is made self-contained, and the abstract is rewritten to match the actual scope and limitations demonstrated in the text.