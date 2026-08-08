# P1A R40 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=f1eab008 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 151.7s

---

**Referee Report: P1A (PRD submission)**

**P1A-E1** (Abstract, p. 1)  
The abstract states “the four enumerated routes … are not proven to be a complete diffeomorphism-invariant operator basis” yet simultaneously claims “channel-level closure.” This internal contradiction is load-bearing.  
**Required fix**: Rewrite the abstract to state only what is actually demonstrated (a set of amplitude-budget arguments under explicit ansätze) and remove the word “closure.”

**P1A-E2** (Abstract + Sec. I, p. 3)  
Abstract claims \(f_{NL}=-35/8\) as a “surviving testable prediction.” Body text (p. 4, Table I footnote c; Sec. XIII) repeatedly qualifies it as “class-level: scalar-only \(w=0\) matter-bounce … not a distinctive ECH prediction.” The abstract version is stronger than the calibrated body statement.  
**Required fix**: Remove \(f_{NL}\) from the abstract or qualify it identically to the body.

**P1A-E3** (Abstract, p. 1; Sec. IV D, p. 13)  
Abstract presents \(\beta\approx0.27^\circ\) as a benchmark consistency point. Body states it is “not an ECH prediction” and arises from a free spectator-ALP fit. This is an unsupported claim of ECH relevance.  
**Required fix**: Delete the \(\beta\) sentence from the abstract.

**P1A-E4** (Throughout, e.g. p. 2, 4, 6, 10, 24)  
Dozens of load-bearing results are imported from “Paper I(b)”, “Paper II”, “in preparation [2,6]”, and “companion paper.” No arXiv numbers or DOIs are supplied. The manuscript fails the standalone-reader test.  
**Required fix**: Either make the present paper self-contained or withdraw it until the companions are public.

**P1A-E5** (p. 1)  
Paper dated “June 13, 2026.” A submission carrying a future date is procedurally invalid.  
**Required fix**: Correct the date or explain the anomaly.

**P1A-M1** (Sec. X, pp. 19–20)  
The “perturbation-transparency” theorem is proved only for canonical scalar matter on a torsion-free Levi-Civita background after the algebraic torsion has already been integrated out. The actual ECH action contains dynamical torsion sourced by fermions; the proof therefore does not apply to the theory advertised in the title.  
**Required fix**: Either restrict the claim to the reduced theory or supply the missing dynamical-torsion calculation.

**P1A-M2** (Table II, p. 17; Sec. IX)  
Fourteen “barriers” are listed; only seven are derived in the present work. The remainder are re-labeled historical arguments or observational nulls. The table heading “14 mechanism-class structural constraints” is therefore inaccurate.  
**Required fix**: Reclassify and renumber; move non-original items to a separate “related constraints” table.

**P1A-M3** (Fig. 1 caption & Sec. IV, p. 10)  
The figure asserts that the four routes are “structurally closed (this paper).” The text immediately qualifies that R1–R3 closures rest on “explicitly-labeled scaling ansätze” and R4 on a “naturalness objection.” The figure caption is therefore false.  
**Required fix**: Redraw or relabel the figure to reflect the actual status of each route.

**P1A-M4** (Sec. II C 1, p. 7; Eq. 10)  
The identification \(\rho_\Lambda=\Xi M_{Pl}^4\) is introduced as an on-shell scaling ansatz, yet is later treated as a derived mapping. No derivation from the ECH action is supplied.  
**Required fix**: Label every occurrence of this relation as an ansatz and propagate the caveat through all numerical claims.

**P1A-M5** (Sec. XIV D, p. 24)  
The structural-tension argument between \(N_{tot}\approx92\) and the \(f_{NL}\) prediction is presented as model-independent. It is derived under the specific assumption that the bounce-era physical scale maps to \(k_{phys}^{bounce}\sim10^{-1}h\,{\rm Mpc}^{-1}\). No robustness test against other mappings is shown.  
**Required fix**: Supply the missing sensitivity analysis or downgrade the claim.

**P1A-N1** (p. 2)  
PACS numbers include “95.36.+x” (dark energy) but the paper concludes that minimal ECH cannot source dark energy. The classification is therefore misleading.  
**Required fix**: Replace with the appropriate “alternative gravity” or “cosmological models” code.

**P1A-N2** (multiple equations, e.g. Eq. 4, 13)  
Inconsistent use of half-weight vs. full-weight torsion conventions is acknowledged in footnotes but never unified. Readers must constantly track which convention is active.  
**Required fix**: Adopt one convention throughout or add a single global conversion table.

**Summary recommendation**  
**REJECT**

The manuscript is not self-contained, relies on a future date, presents stronger claims in the abstract than the body supports, and advertises a “channel-level closure” whose central technical result (perturbation transparency) is proved only after the dynamical content of ECH has been removed. These are not cosmetic defects; they are fatal to a first-read PRD evaluation. A substantially rewritten, fully standalone version limited to the actual derived results (approximately 12–14 pages) could be reconsidered, but the present submission does not meet PRD standards.