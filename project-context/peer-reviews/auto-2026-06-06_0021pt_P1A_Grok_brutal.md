# P1A auto-2026-06-06_0021pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 101.1s

---

**Referee Report**

**P1A-E1 (ESSENTIAL, p. 1, abstract block + Sec. I, p. 3)**  
The manuscript states: “ACDM+ΔN_eff MCMC verification … are documented separately in companion work in preparation [6]” and repeatedly defers Fisher forecasts, NaMaster validation, and ALP parameter fitting to “Paper I(b)”, “Paper II”, etc. Core numerical claims (ΔN_eff = −0.020 ± 0.169, σ(f_NL) ≈ 0.7, 3–5σ separation) are therefore unverifiable from the submitted text. A PRD paper must be self-contained.

**P1A-E2 (ESSENTIAL, p. 1, abstract + Sec. IV, p. 8)**  
The title and abstract assert “Channel-Level Closure of Four Minimal … Routes”. The text immediately qualifies: “we do not claim a full operator-basis closure” and explicitly excludes the Jackiw–Pi term R∧R̃ and the parity-odd four-fermion partner of Route 1. The central claim is therefore false on its face; the paper demonstrates only a partial amplitude-level no-go under stated assumptions.

**P1A-E3 (ESSENTIAL, p. 1 header)**  
“(Dated: June 2, 2026 PDT)” appears in the title block. This is an internal draft artifact inconsistent with a submitted manuscript.

**P1A-E4 (ESSENTIAL, Sec. X, p. 14 and abstract)**  
The “perturbation-transparency theorem” is derived only for canonical scalar matter; the tensor-sector extension is stated without proof (“the same five steps apply”). All claims about primordial GW chirality and TB/EB vanishing rest on an unproven step.

**P1A-M1 (MAJOR, Sec. II C, p. 6 and Appendix B, p. 19)**  
The parity-odd operator (Eq. 6) is assigned off-shell mass dimension +1. The authors treat ρ_Λ ∼ (α/M)M_Pl^5 as a “phenomenological on-shell scaling ansatz, not a derivation.” All subsequent N_tot ≈ 92 bookkeeping and the 13-barrier catalog inherit this uncontrolled ansatz; the entire structural-tension argument collapses without it.

**P1A-M2 (MAJOR, Sec. IV, pp. 8–11)**  
Routes R1–R4 are declared “closed at channel-amplitude level.” Each closure invokes either Planck suppression (M_Pl^−1 or M_Pl^−2), mass-dimension mismatch, or an external spectator field. No route is closed by an internal ECH inconsistency alone; the “no-go” is therefore an artifact of the chosen truncation, not a theorem about minimal ECH.

**P1A-M3 (MAJOR, Table II, p. 13 and Sec. IX, p. 12)**  
Fourteen “logically independent” barriers are listed. Barrier 8 (parity-even interaction) and Barrier 14 (transparency) are direct consequences of the same Holst-term evaluation; they are not independent. The count of 13/14 is inflated.

**P1A-M4 (MAJOR, Fig. 1 caption + Sec. XIII, p. 16)**  
The figure and text juxtapose σ(f_NL) values obtained under different null hypotheses and different systematics budgets without the required qualifier that they are “not directly comparable.” This violates the explicit instruction in the review criteria.

**P1A-N1 (MINOR, p. 1 and throughout)**  
Dozens of forward references to “Paper I(b)”, “Paper II”, “Paper III”, “Paper IV” (all “in preparation”) render the manuscript unreadable as a standalone document.

**P1A-N2 (MINOR, Sec. II A 2, p. 5)**  
Eq. (7) quotes an one-loop coefficient whose numerical prefactor is scheme-dependent (γ_SU(2) ≈ 0.274 with ±0.020 “scheme range”). The text never propagates this uncertainty into the quoted N_tot = 92 or the 13-barrier catalog.

**P1A-N3 (NIT)**  
Table I and the abstract list β_obs = 0.342° ± 0.094° as a “benchmark consistency point.” The value is taken from external literature; the paper’s own prediction is only that any spectator ALP can reproduce it. The phrasing is therefore misleading.

**Summary recommendation**  
REJECT

The manuscript is not self-contained, its central “closure” claim is explicitly disclaimed in the text, the key numerical results reside in unpublished companion papers, and the manuscript contains an obvious future-date draft artifact. These are not cosmetic issues; they are fatal to a first-read acceptance at Physical Review D.