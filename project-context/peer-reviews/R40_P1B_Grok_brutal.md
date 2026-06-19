# P1B R40 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 118.3s

---

**Referee Report**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program… (P1B)

**Journal:** Physical Review D (adversarial first-read audit)

**Finding P1B-E1 (ESSENTIAL, Abstract + §I p.2)**  
The abstract states three headline results (ΔN_eff = −0.020 ± 0.169, NaMaster recovery bias −0.032° to −0.040°, spectator-ALP consistency at 3.6σ) without the explicit scope qualifiers that appear on every page of the body (“NOT a spin-torsion theory module”, “not a distinctive ECH prediction”, “pipeline-validation figure, not a sky-detection significance claim”). Abstract claims are stronger than, and ordered differently from, the body’s final calibrated statements. Required fix: rewrite abstract to match the body’s repeated scope limitations verbatim.

**Finding P1B-E2 (ESSENTIAL, §III p.3–5, Fig. 2, Table I)**  
ΔN_eff posteriors from two frozen dataset combinations are presented side-by-side with a single 1σ interval; the text states they are “not directly comparable to each other’s published sky significances” yet supplies no explicit “not directly comparable” qualifier at every juxtaposition of the two σ values. Violates instruction 7. Required fix: insert the qualifier at every numerical comparison or remove the joint presentation.

**Finding P1B-E3 (ESSENTIAL, §VI p.10–13, Fig. 4, Table IV)**  
The birefringence signal is recovered only inside a spectator-ALP model whose photon-torsion coupling is inserted by hand (C_aγ fixed at 8, misalignment tuned by ~25×). The paper repeatedly states this is “not derived from minimal ECH” and “not a distinctive ECH prediction”. The central claim of the section is therefore unsupported by the ECH framework itself. Required fix: either derive the coupling from the Holst action or re-title the section as a generic ALP consistency check.

**Finding P1B-E4 (ESSENTIAL, §IV p.6–8, Fig. 3)**  
NaMaster pipeline bias (−0.032° to −0.040°) is presented as a “validation figure” while the published Planck/ACT 3.6σ value is quoted in the same paragraph. The text admits the two numbers “are not directly comparable”. No effect-size or practical-significance statement accompanies the χ²-based SNR figures (20.32, 25.71). Required fix: remove all side-by-side numerical comparison or supply the missing effect-size qualifier and explicit incomparability statement at every occurrence.

**Finding P1B-M1 (MAJOR, entire manuscript length vs. contribution)**  
21 pages of heavily caveated verification material whose principal conclusions are negative or null (“does not resolve the Hubble tension”, “not a distinctive ECH prediction”). PRD methods papers of this type are routinely ≤10–12 pages. Required fix: condense to ≤12 pages or justify the length.

**Finding P1B-M2 (MAJOR, §V p.9–10, Table II)**  
w0wa posterior is reported with marginal-tail distances (+4.3σ, −3.6σ) from the Metropolis-Hastings chain while the text states the Savage-Dickey ratio is “not viable” because the ACDM point lies >4σ in the tails. The quoted significance is therefore an extrapolation artifact, not a controlled posterior odds. Required fix: replace with nested-sampling evidence or remove the numerical σ claims.

**Finding P1B-M3 (MAJOR, Data Availability p.15)**  
Frozen-chain DOIs and commit hashes are listed as “pending” or “v1B.0.74”. Several artifact URLs point to directories whose contents (mask, burn-in, N_side) are described inconsistently with the body text. Required fix: supply immutable frozen-release DOIs and verify every artifact matches the exact configuration used for the quoted numbers.

**Finding P1B-N1 (MINOR, multiple locations)**  
Duplicate phrasing (“canonical canonical-mask”, “the the”) and internal round markers (“R40”, “this version”) appear in the rendered PDF. Required fix: clean copy-edit.

**Finding P1B-N2 (NIT)**  
Several axis labels in Fig. 1–4 omit units or use non-standard abbreviations (e.g., “deg” vs. “°”). Minor but inconsistent with PRD style.

**Summary recommendation**  
**REJECT**

The manuscript is a 21-page technical appendix whose central results are either null or explicitly stated to be outside the ECH framework. Every load-bearing numerical claim is hedged by scope limitations that are omitted from the abstract, and the birefringence “consistency check” relies on an ad-hoc spectator field whose coupling is not derived from the theory being tested. These defects are structural and cannot be repaired by minor revision.