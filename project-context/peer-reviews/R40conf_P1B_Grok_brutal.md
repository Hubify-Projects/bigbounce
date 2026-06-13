# P1B R40conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1b_mcmc_companion.pdf` md5=62374add pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 83.7s

---

**Referee Report**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program… (P1B)

**Journal target:** Phys. Rev. D (high bar for methods/verification papers)

**Findings (adversarial read)**

**P1B-E1 (ESSENTIAL)**  
Section I, p. 2 and abstract: The paper is explicitly framed as a “technical verification companion” whose three analyses are all null or negative (“does not reduce the residual…”, “not a sky detection significance claim”, “not a distinctive ECH prediction”). No positive, falsifiable prediction of the ECH framework is tested. PRD does not publish 21-page verification-only manuscripts whose sole conclusion is “our pipeline recovers injected signals and our proxy extension is consistent with zero.” Required fix: either convert to a concise Methods Note (≤6 pages) or withdraw.

**P1B-E2 (ESSENTIAL)**  
Abstract + §III (p. 3–5) and Table I: The headline ΔN_eff values (−0.020 ± 0.169 and +0.058 ± 0.179) are presented as the central result, yet the text repeatedly states this is “NOT a spin-torsion theory module” and “does not test the ECH spin-torsion sector directly.” The abstract therefore advertises a number whose physical interpretation the authors themselves disclaim. This is a direct violation of the “abstract accurately summarizes what the paper PROVES” rule.

**P1B-E3 (ESSENTIAL)**  
§IV (p. 6–8) and Fig. 3: The NaMaster pipeline-recovery bias is reported as Δβ̂ = −0.032° to −0.040° (worst-case). The published observational value β = 0.342° ± 0.094° is juxtaposed without the explicit qualifier “these two numbers are not directly comparable” at every occurrence. The 3.6σ claim is therefore presented next to a pipeline artifact whose magnitude is ~40 % of the reported signal. This is an ESSENTIAL sigma-mixing violation.

**P1B-E4 (ESSENTIAL)**  
§VI (p. 10–13) and abstract: The birefringence “consistency check” uses a spectator-ALP model whose authors admit produces the identical β ≈ 0.27° in ordinary GR. The section is therefore a test of standard axion physics, not of ECH. The abstract lists it as one of the three main results. Required fix: remove from abstract and re-title the paper.

**P1B-M1 (MAJOR)**  
The manuscript is 21 pages (including appendices) for a purely technical verification exercise. PRD page limits and scope for companion/methods papers are routinely enforced at ≤10–12 pages when no new physics result is claimed. Recommend immediate reduction to a focused Methods Note.

**P1B-M2 (MAJOR)**  
Multiple load-bearing statements (“the 3.6σ tension persists”, “consistent with zero”) rely on the frozen chains and YML files whose exact commit hashes and burn-in cuts are only referenced via an external GitHub repo that post-dates the stated paper version (v1B.0.69). Standalone-reader test fails.

**P1B-M3 (MAJOR)**  
Table II reports w0 + wa = −1.4788 ± 0.1485 and claims a “+2.5σ” phantom-crossing departure. No effect-size measure (Cramér’s V, fractional deviation from ΛCDM, or Bayes factor) is supplied. The 4.3σ / 3.6σ tail-distance language is therefore unaccompanied by practical significance.

**P1B-N1 (MINOR)**  
Fig. 2 caption and text use “full-tension” and “Planck+BAO+SN” interchangeably without a one-sentence definition on first use.

**P1B-N2 (NIT)**  
Minor axis-label font inconsistency in Fig. 1 corner plot (H0 units appear as “km s^{-1} Mpc^{-1}” in one panel and abbreviated in another).

**Summary recommendation**  
**REJECT**

The manuscript is a 21-page technical verification document whose three headline results are (1) a null extension test the authors themselves label “not a spin-torsion module,” (2) a pipeline bias measurement whose magnitude is comparable to the claimed sky signal without repeated explicit non-comparability warnings, and (3) a birefringence exercise performed in ordinary GR+ALP. No distinctive ECH prediction is confronted with data. The length, framing, and abstract–body mismatch place the paper well below the Phys. Rev. D threshold for a full article.