# P1A R37conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.68.pdf` md5=0de277bf pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 79.4s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Physical Review D

**Finding classification key**  
- ESSENTIAL: blocks acceptance  
- MAJOR: requires substantial revision  
- MINOR: addressable without re-review  
- NIT: cosmetic

**P1A-E1** (ESSENTIAL)  
Section: Title page (rendered p. 1)  
Problem: Header contains “Dated: June 13, 2026 PDT — v1A.0.68”. This is internal versioning / future-date artifact language.  
Required fix: Remove all version strings and future dates from the manuscript.

**P1A-E2** (ESSENTIAL)  
Section: Abstract + p. 3–4 (multiple citations to [2,6] and “Paper I(b)”)  
Problem: Core numerical results (MCMC posteriors, Fisher forecasts, \(\sigma(f_\text{NL})\approx0.7\), LiteBIRD \(\sigma(\beta)\approx0.03^\circ\)) and the claim that \(\Delta N_\text{eff}\approx0\) are imported from “companion work in preparation.” The paper is not standalone.  
Required fix: All load-bearing quantitative claims must be either reproduced or removed; placeholder arXiv IDs or “in preparation” citations are unacceptable for PRD.

**P1A-E3** (ESSENTIAL)  
Section: Abstract (first paragraph) + p. 10–14 (Route 4 closure)  
Problem: Abstract states that Route 4 is closed “by a naturalness/explanatory-deficit objection rather than amplitude mismatch.” The body (p. 13–14) shows that closure occurs only after treating \(\alpha/M\) as a free phenomenological parameter and imposing an external ultralight-mass tuning \(m_\theta\sim H_0\). The abstract claim is stronger than the calibrated body statement.  
Required fix: Rewrite abstract sentence to match the body’s final, assumption-tagged conclusion.

**P1A-E4** (ESSENTIAL)  
Section: Table I (p. 4) + footnote a  
Problem: Footnote states “Reparameterized as sensitivity to \(N_\text{tot}\); not solved.” The table headline nevertheless lists “\(H_0=67.68\pm1.06\), \(\Delta N_\text{eff}\approx0\)” as a result. This is an internal contradiction on whether the cosmological-constant problem is solved.  
Required fix: Remove or clearly qualify the \(H_0\) and \(\Delta N_\text{eff}\) entries.

**P1A-E5** (ESSENTIAL)  
Section: p. 19 (Barrier 14) + Sec. X  
Problem: The central “perturbation-transparency” theorem is proved only for canonical scalar matter; the tensor-sector extension (p. 19) is stated without derivation. The abstract presents the result as general.  
Required fix: Either restrict the abstract claim or supply the missing tensor proof.

**P1A-M1** (MAJOR)  
Section: p. 1–2 (length)  
Problem: 28-page manuscript whose principal result is a channel-level enumeration under 14 explicitly labeled assumptions. PRD norm for a closure argument of this type is \(\leq18\) pages.  
Required fix: Reduce to \(\leq18\) pages or justify length.

**P1A-M2** (MAJOR)  
Section: Fig. 3 caption (p. 8)  
Problem: Caption quotes specific ECH parameters (\(H_0=69.2\), \(\Omega_m=0.310\)) and \(\Lambda\)CDM reference values but does not state the exact \(\Xi\) or \(\mathcal{D}_\text{inf}\) values used to generate the orange curve. Numbers cannot be recomputed from displayed inputs.  
Required fix: Supply the numerical inputs that produce the plotted curve.

**P1A-M3** (MAJOR)  
Section: p. 14 (Route 4) + p. 4 (Table I)  
Problem: Multiple \(\sigma\) values from different null procedures (WMAP+Planck vs. ACT DR6 vs. LiteBIRD forecast) are juxtaposed without the explicit qualifier “not directly comparable” at every instance.  
Required fix: Add the qualifier wherever values from distinct pipelines appear side-by-side.

**P1A-M4** (MAJOR)  
Section: p. 5 (Fig. 1) + p. 20 (Sec. XI)  
Problem: The figure and hybrid-loophole discussion rely on the unproven assumption that adding \(w_0w_a\) does not change the structural-tension verdict. No quantitative test is supplied.  
Required fix: Provide the explicit test or remove the claim.

**P1A-N1** (MINOR)  
Section: p. 2 (PACS numbers)  
Problem: PACS line contains “95.36.+x” (obsolete).  
Required fix: Update to current scheme.

**P1A-N2** (MINOR)  
Section: Multiple figure captions  
Problem: Axis labels omit units on several derived quantities (e.g., \(\Delta H/H_\text{ACDM}\) panel of Fig. 3).  
Required fix: Add units.

**P1A-NIT1** (NIT)  
Section: Throughout  
Problem: Repeated use of “channel-level” vs. “operator-level” phrasing without a one-sentence definition on first use.  
Required fix: Add definition.

**Summary recommendation**  
REJECT

The manuscript is not self-contained, contains internal versioning artifacts, presents abstract claims stronger than the body’s final calibrated statements, and relies on “in-preparation” companions for every quantitative result that would normally be required for a PRD closure paper. Even after those issues are set aside, the 28-page length is disproportionate to a channel-level enumeration under 14 labeled assumptions. The work would require a complete rewrite and substantial new derivations before it could be considered at PRD standards.