# P1A R35conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.64.pdf` md5=03392974 pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 104.8s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Physical Review D

**Overall assessment:** The manuscript does not meet PRD standards. It is a heavily qualified “channel-level amplitude closure” argument resting on 14 explicitly labeled assumptions, multiple phenomenological ansätze that are never derived, and repeated citations to unpublished companion papers for all quantitative results. The central claims are therefore not self-contained and cannot be evaluated on the submitted text alone.

**ESSENTIAL findings (any one is sufficient for rejection)**

**P1A-E1**  
**Section:** Abstract (p. 1) and Sec. I (p. 3)  
**Problem:** Abstract states “the central result is a perturbation-transparency result: for canonical scalar matter, torsion vanishes at all classical metric/scalar perturbation orders.” The body (Sec. X, p. 18–19) proves this only after imposing the on-shell Bianchi identity on a torsion-free Levi-Civita connection and after restricting to canonical scalar matter with no non-minimal couplings. The abstract omits every qualifier.  
**Required fix:** Rewrite abstract to match the final calibrated statement in Sec. X exactly, including the scope restrictions.

**P1A-E2**  
**Section:** Throughout (explicitly pp. 2, 4, 6, 13, 20, 24)  
**Problem:** Every numerical claim that would allow a reader to judge significance (f_NL = −35/8 at 2.6–5σ, β ≈ 0.27°, ΔN_eff ≈ 0, H_0 = 67.68 ± 1.06, N_tot ≈ 92, etc.) is imported from “companion work in preparation [2,6]”, “Paper I(b)”, or “Paper II”. No standalone derivation or table of inputs exists. Violates PRD requirement that the paper be self-contained.  
**Required fix:** All load-bearing numbers must be recomputed and tabulated inside the present manuscript with explicit assumptions stated.

**P1A-E3**  
**Section:** Sec. IV (pp. 10–14) and Table II (p. 16)  
**Problem:** The four-route “closure” is performed at the amplitude-budget level under explicitly labeled scaling ansätze (e.g., ρ_Λ = Ξ M_Pl^4 with Ξ treated as a free parameter, off-shell mass dimension +1 for the parity-odd operator). The text repeatedly states this is “not an operator-level theorem.” The abstract and introduction nevertheless present the result as a structural no-go for minimal ECH dark energy.  
**Required fix:** Remove all language implying a general theorem; restrict title, abstract, and conclusions to the precise scope stated in Sec. IV “Scope” paragraph.

**P1A-E4**  
**Section:** Sec. X (p. 18) and Fig. 3 caption (p. 7)  
**Problem:** The perturbation-transparency proof uses the first (algebraic) Bianchi identity on a torsion-free connection. The text acknowledges this is “distinct from the Pontryagin density” but then uses the result to claim the Holst sector “decouples cleanly.” The logical step from “vanishes on the Levi-Civita connection” to “no observable ECH signature at any order” is not demonstrated for the actual dynamical connection that includes torsion before the on-shell limit.  
**Required fix:** Provide an explicit off-shell calculation or retract the “all orders” claim.

**MAJOR findings**

**P1A-M1**  
**Section:** Sec. II C and Appendix B (pp. 7–8, 25)  
**Problem:** The mapping ρ_Λ = Ξ M_Pl^4 is introduced as a “phenomenological on-shell scaling ansatz, not a derivation.” All subsequent fine-tuning comparisons (10^5 vs 10^120) rest on this ansatz. No justification is given for why the same ansatz is not applied to the competing models in Fig. 5.  
**Required fix:** Either derive the scaling or remove all quantitative fine-tuning comparisons.

**P1A-M2**  
**Section:** Table I (p. 4) and footnotes  
**Problem:** Multiple entries are labeled “not a distinctive ECH prediction” or “recovers ΛCDM.” The table is presented as an “executive summary” of the paper’s results.  
**Required fix:** Remove or clearly segregate non-distinctive entries.

**P1A-M3**  
**Section:** Sec. XIII and Fig. 4 (pp. 21, 15)  
**Problem:** The two “surviving ECH-independent class tests” (f_NL = −35/8 and spectator-ALP β) are stated to be mechanism-independent. The paper therefore does not claim a unique ECH signature even if those signals are detected.  
**Required fix:** Revise all language that presents these tests as tests of the ECH framework itself.

**MINOR / NIT findings (selected)**

**P1A-N1** (p. 1) Future date “June 12, 2026” in the dateline.  
**P1A-N2** (p. 2) “v1A.0.64” version tag left in the published header.  
**P1A-N3** (multiple) Inconsistent use of “parity-odd” vs “CP-odd” for the same operator.  
**P1A-N4** (Fig. 3) Lower panel y-axis label “ΔH/H_ΛCDM (%)” but caption claims it reflects the Ξ M_Pl^4 term; the plotted curve is actually the rotation contribution, which is stated to be negligible.

**Summary recommendation: REJECT**

The manuscript is not a self-contained scientific argument. Every quantitative result required to assess the claimed closures and the perturbation-transparency statement is deferred to unpublished companions. The actual content that remains is a set of amplitude-budget arguments under a long list of explicitly acknowledged phenomenological assumptions. This does not constitute a theorem or a robust no-go result at the level expected by Physical Review D.