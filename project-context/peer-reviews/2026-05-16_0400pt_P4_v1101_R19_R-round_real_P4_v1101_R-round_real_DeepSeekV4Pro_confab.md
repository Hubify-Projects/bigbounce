# P4_v1101 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0400pt_P4_v1101_R19_R-round_real
**Wall time**: 345.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=79083, completion=9552, reasoning=8291, total=88635

---

# Adversarial Peer Review — Findings

## PAPER-ADV-B1 (BLOCKER): Headline post-MASTER $\ell{=}1$ null ($-0.12\sigma$) and raw pseudo-$C_\ell$ bandpower ($+6.48\sigma$) lack guaranteed public provenance.

**Location:** Abstract; Sec.~II.D (Dipole Analysis); Conclusions.  
**Issue:** The two most load-bearing scalars in the abstract and conclusions — the MASTER‑deconvolved $\ell{=}1$ dipole $-0.12\sigma$ (primary cosmological null) and the pre‑MASTER pseudo‑$C_\ell$ bandpower $+6.48\sigma$ (mask‑leakage demonstration) — are computed from JSON artifacts (`master_power_spectrum.json` and `wave11c_nspiral_recompute_…/results.json`) that reside in directories (`master_results/`, `h200_results/`) **not** covered by the paper’s data‑availability guarantee. The footnote on reproducibility explicitly lists only `r42_results/*.json` and `outputs/canonical_provenance/` as deposited under the release tag; neither of the cited files falls within those described locations. A reader following the paper’s own provenance instructions cannot confirm these numbers without guessing whether the repository maintainer separately committed those paths.  
**Fix:** Either move both JSON files into `outputs/canonical_provenance/` and update the data‑availability statement, or add an explicit sentence that the release DOI also encompasses the `master_results/` and `h200_results/` subdirectories, and verify they are indeed present in the tagged archive.

---

## PAPER-ADV-M1 (MAJOR): Real‑space dipole artefact also falls outside the documented provenance tree.

**Location:** Abstract; Sec.~II.D; Conclusions; `\artifact{pipelines/p2_chirality/outputs/dipole/summary.json}`.  
**Issue:** The $0.43\sigma$ real‑space dipole is repeatedly presented as a primary cosmological estimator, yet its JSON artefact lives in `outputs/dipole/` — another directory not mentioned in the data‑availability section. The same holds for the hemisphere scan artefact (`h200_results/wave12_hemi_…`) that supplies the $3.05\sigma$ local maximum. This pattern leaves three of the paper’s stated “primary” and “secondary” estimators without a verifiable on‑disk source.  
**Fix:** Consolidate all estimator artefacts in `outputs/canonical_provenance/` with clear, literal filenames, and ensure the release note lists every file that backs a headline figure.

---

## PAPER-ADV-m1 (minor): The residual global monopole of the asymmetry map is ambiguously documented across the paper.

**Location:** Abstract (“$2\langle p_{\rm CW}\rangle-1\!\approx\!-0.0053$ at $\langle p_{\rm CW}\rangle\!=\!0.4974$”); Sec.~IV.B; Table~V; Table~VI.  
**Issue:** The abstract derives $-0.0053$ from $p_{\rm CW}=0.4974$, yet the per‑leg summary (Table~VI) and the canonical‑$N$ MASTER discussion use $0.49735$. The difference is only $1.5\times10^{-4}$, but it propagates into the stated monopole amplitude, and the text never clarifies which fraction is the official canonical value. A reader attempting to reproduce the asymmetry map’s mean subtraction cannot know which number to adopt.  
**Fix:** Adopt one value (e.g. the $0.49735$ from the per‑leg table, as it matches the 3,201,160 spiral total) consistently in the abstract, tables, and body, and recalculate derived quantities from that single seed.

---

## PAPER-ADV-m2 (minor): The $9.5\sigma$ monopole significance is quoted without an $N_{\rm eff}$‑corrected counterpart, even though the paper acknowledges that spatial correlations likely reduce the effective sample size.

**Location:** Abstract; Sec.~IV.B; Conclusions.  
**Issue:** The paper states that the $9.5\sigma$ deviation uses the naïve binomial uncertainty $\sigma=0.000279$ and then notes that the true $N_{\rm eff}$ may be smaller, which would lower the significance, but no corrected significance is provided. No JSON artefact or on‑disk computation of $N_{\rm eff}$ (e.g. via pixel‑to‑pixel variance) is cited. The headline “$9.5\sigma$” therefore remains an upper bound whose actual level is unknown, yet it is presented as a precise measurement.  
**Fix:** Either compute $N_{\rm eff}$ from the HEALPix CW‑fraction map (a trivial extra column in an existing script) and report the corrected significance, or explicitly downgrade the $9.5\sigma$ to “$<9.5\sigma$ after accounting for spatial oversampling” and note that no corrected value is available.

---

## PAPER-ADV-n1 (nit): The “99.3%” reproduction ratio in the abstract could be misread without the immediate table reference.

**Location:** Abstract sentence beginning “A controlled monopole‑only $N=500$ generative null … reproduces $\mathbf{99.3\%}$ of the observed pre‑MASTER pseudo‑$C_1$ power”.  
**Issue:** The number $99.3\%$ is a simple division of two numbers from Table~I ($1.6846/1.696$), but the abstract does not cite the table in the same sentence. A reader scanning for provenance may momentarily wonder if the ratio comes from a separate, uncited calculation.  
**Fix:** Append “(Table~I)” immediately after the percentage to link it to the displayed values that back it.

---
