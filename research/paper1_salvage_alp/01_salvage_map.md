# Paper 1 Salvage Map

**Date:** 2026-03-17

---

## Methodology

Every major section of Paper 1 (`arxiv/main.tex`, 1680 lines, v1.6.0) is classified into one of three buckets based on the new salvage frame: spin-torsion bounce cosmology + spectator ALP birefringence + dark energy treated as Lambda (not derived from ECH).

---

## A. KEEP (use as-is or with minor edits)

| Section/Content | Lines | Reason |
|----------------|-------|--------|
| **ECH action derivation** (Sec 2.1.1) | 155-175 | Clean math. Still the starting Lagrangian. |
| **Torsion activation + four-fermion interaction** (Steps 1-2) | 180-191 | Standard EC result, textbook-level. |
| **Modified Friedmann equation / quantum bounce** (Sec 2.2) | 231-251 | Core bounce physics, well-established. |
| **Bounce critical density from gamma** | 237-241 | Clean derivation, no overclaim. |
| **CMB E-B cross-correlations** (Sec 3.1, Eq 14) | 344-373 | Standard birefringence formula. Needed for ALP prediction. |
| **Birefringence measurements from literature** (Sec 5.1) | 654-673 | Data citations. Keep and update (add Eskilt 2025 combined). |
| **Bayesian model comparison methodology** (Sec 6.3) | 715-740 | Standard statistical methods. Reusable for ALP MCMC. |
| **Falsification criteria structure** (Sec 8) | 901-947 | Framework for testability. Revise content for ALP model. |
| **Notation appendix** (App A) | 1256-1282 | Keep, add ALP notation. |
| **Dimensional analysis appendix** (App H) | 1523-1607 | Keep as pedagogical material. |
| **Reproducibility appendix** (App I) | 1608-1631 | Update for new MCMC runs. |

---

## B. KEEP BUT REFRAME

| Section/Content | Lines | Current framing | Required reframing |
|----------------|-------|----------------|-------------------|
| **Introduction** (Sec 1) | 78-149 | "dark energy from quantum gravity" | "bounce cosmology + parity phenomenology; DE as open question" |
| **Original Contributions list** (Sec 1.2) | 124-140 | 6 contributions, most about DE derivation | Rewrite: (1) bounce, (2) parity, (3) ALP birefringence prediction, (4) MCMC, (5) closure assessment |
| **Parity-odd term derivation** (Steps 3-4) | 193-223 | "origin of dark energy" | "motivation for Planck-scale pseudoscalar coupling; does NOT derive DE" |
| **Parity-odd coefficient** (Eq 8) | 213-223 | alpha/M as DE parameter | alpha/M as theoretical motivation for ALP coupling scale; explicitly not fitted to DE |
| **Cosmic rotation subsection** (Sec 2.3) | 253-310 | "rotation + dark energy" with Lambda_eff | Keep rotation-as-axis-origin; remove DE derivation claim; state Lambda is added separately |
| **Inflationary suppression** (Sec 2.3.2) | 287-307 | "DE scale from dilution" | Reframe as "illustrative chain showing how Planck-scale effects could in principle map to late-time scales; this chain does NOT constitute a derivation" |
| **Birefringence consistency check** (Sec 10.4) | 1032-1063 | f_photon x C_0 = O(1) compatibility | Replace with actual ALP prediction: beta = C alpha theta_i / (4 pi); spectator ALP; MCMC posterior |
| **Discussion: inflationary suppression** (Sec 10.1) | 985-1015 | Central theoretical claim | Downgrade to "illustrative fine-tuning reduction argument; not a derivation" |
| **Discussion: theoretical implications** (Sec 10.3) | 1016-1031 | Broad claims | Narrow to: bounce is well-defined; DE is separate; ALP birefringence is the testable prediction |
| **Limitations** (Sec 11) | 1064-1199 | "future directions to complete the derivation" | Reframe: "the derivation program is closed (see companion note); remaining open questions are ALP model selection and LiteBIRD forecasts" |
| **Conclusions** (Sec 12) | 1200-1221 | DE framework + tensions + birefringence as secondary | ALP birefringence as primary result; bounce as theoretical context; DE as separate |
| **Executive summary table** (Tab 1) | 94-110 | "H_0 tension reduced", "geometric origin DE" | Remove DE and tension claims; replace with ALP birefringence prediction |
| **MCMC verification** (Sec 3.4) | 435-536 | Delta-Neff as key test | Reframe: verification that ECH sector does not conflict with standard cosmology; Delta-Neff consistent with zero is the correct finding |
| **Cosmological fits** (Sec 6) | 689-826 | Tension reduction narrative | Reframe as "standard LCDM fit with additional spectator ALP sector" |
| **Parameter summary** (App B) | 1285-1326 | alpha/M, Xi, D_inf as fitted | Add ALP parameters (theta_i, m_a, C_{agamma}); demote alpha/M to "theoretical motivation" |
| **Claims appendix** (App J) | 1632+ | Mixed derived/assumed/fit | Complete rewrite with honest status |

---

## C. REMOVE / RETIRE

| Section/Content | Lines | Reason |
|----------------|-------|--------|
| **"Geometric origin" DE claim in executive table** | 102 | Dead. Seven barriers closed all routes. |
| **"Fine-tuning from 10^120 to 10^5" as achievement** | 72-73, 102, 1210 | The chain is illustrative, not a derivation. Cannot be listed as an achievement. Mention as motivation only. |
| **H_0 = 69.2 +/- 0.8 tension reduction claim** | 74, 98-99, 1206 | Driven by SH0ES prior, not by the model. The MCMC verification proved this. Remove from abstract and executive summary entirely. |
| **sigma_8 = 0.785 tension reduction claim** | 75, 99 | Same issue. Model does not predict sigma_8 reduction. |
| **"Simultaneous tension reduction" as original contribution** | 131 | Not a contribution. It's LCDM + Delta-Neff with a SH0ES prior. |
| **Galaxy spin alignment mechanism** (Sec 2.3.3) | 311-336 | 9-12 orders of magnitude gap. The mechanism does not work. Mentioned as "open question" at most. |
| **Galaxy spin asymmetry data** (Sec 3.2) | 374-405 | Based on contested Shamir dipole. Not supported by framework's own coupling. |
| **Galaxy spin data methods** (Sec 4) | 613-651 | Entire section on analyzing a signal the framework cannot produce. |
| **Galaxy spin hierarchical Bayesian appendix** (App C) | 1329-1383 | Supporting material for a claim that must be removed. |
| **Galaxy spin null tests** (Sec 7.1.1) | 847-857 | Tests for a signal that is not predicted. |
| **Galaxy spin falsification criteria** (Sec 8.2) | 911-916 | Cannot falsify a claim you are not making. |
| **A(z) = A_0(1+z)^{-p}e^{-qz} functional form** | 322-325 | Empirical fit to a dipole the framework cannot source. |
| **"Correlated axes" prediction** | 65-66, abstract | Requires galaxy spin dipole to be real AND framework-produced. Neither is established. |
| **"Rotating BH origin" as parity violation source** | 104, abstract | The BH-universe scenario is speculative and not needed for the ALP model. Mention as one possible motivation only. |
| **Black hole interior numerical relativity** (Sec 11.5.5) | 1161-1170 | Future direction for a dead program direction. |
| **Vacuum energy from fermion condensates** (Sec 3.2) | 571-583 | NJL condensate route is closed (Branch Q result). |
| **Joint likelihood analysis appendix** (App D) | 1385-1411 | Galaxy spin + CMB joint likelihood for signals the framework cannot produce. |
| **Rotation framework appendix** (App F) | 1442-1485 | Keep only as background context, not as DE-relevant. Trim heavily. |
| **100,000-sample Monte Carlo sensitivity scan language** | 1210 | Part of the fine-tuning narrative. Illustrative only. |
| **Delta-Neff as "predicted by bounce"** | 75, 131, 1317 | Delta-Neff is consistent with zero. Not a prediction. |

---

## Summary Counts

| Bucket | Sections/items | Approximate lines |
|--------|---------------|------------------|
| A. KEEP | 11 items | ~350 lines |
| B. REFRAME | 17 items | ~650 lines |
| C. REMOVE | 21 items | ~400 lines |
| Total Paper 1 | | ~1680 lines |

**Net effect:** Paper 1 shrinks by ~25% and shifts from "DE framework paper" to "bounce + ALP birefringence phenomenology paper."
