# P4P INT_v3/ROUND_2026-09-18-P4P-v4P.0.7-EXACTPDF-7eb1f99e-CONFIRM/API — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `pipelines/p4prime_chirality_test/paper/main.pdf` sha256=7eb1f99ecc5e3d50a90457997e075873750eff0902ac95eadf9e430d27729a9d pages=13
**Review packet(s)**: `643b08c58a602932cd2d30b5e2e3c2539a4b4211ee223e1bed3c0a84b899bc44, b81b798b9b5ccf79d46b040a5f102808a5f5eae5146e2573d6dc6bd114316de3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 89.2s

---

**Referee Report**

**P4P-E1 (ESSENTIAL, p.1, header + §1)**  
"DRAFT VERSION SEPTEMBER 5, 2026" and "(Dated: September 5, 2026; Version v4P.0.7)" appear in the submitted PDF. These are internal bookkeeping tags.  
Fix: Remove every draft/version string; resubmit with only journal-standard metadata.

**P4P-E2 (ESSENTIAL, pp. 4–5, 8 and multiple figure captions)**  
Internal script paths and repository strings remain in the body and captions, e.g. `research/bh_universe_dipole/a95_null_cl_2026_09_02.py`, `pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.json`, `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py`. These are not acceptable in a journal submission.  
Fix: Excise every filesystem path, commit hash, and internal filename; replace with stable Zenodo DOIs or remove.

**P4P-E3 (ESSENTIAL, abstract + §3, p.4)**  
Abstract states \(A_{95}^{\rm obs} \simeq 0.98\%\) and \(A_{95}^{\rm CL} \simeq 0.75\%\) as the sensitivity floor. The body (Eq. 1, Fig. 2, p.5) shows these are derived from a 2 000-injection campaign on the exact committed pipeline. No independent verification of the 0.98 % / 0.75 % numbers is supplied, and the Neyman construction is only sketched.  
Fix: Provide the exact committed script + seed list + output table that produces both numbers; recompute and tabulate the 5th-percentile recovered amplitude for every injected \(A\).

**P4P-E4 (ESSENTIAL, §5.2, p.8)**  
The quantitative exclusion \(\eta > A_{95}^{\rm obs} \simeq 0.98\%\) rests on an illustrative bridge factor \(g=0.398\) that is explicitly “not an established calibration.” The paper therefore converts an observed-label sensitivity floor into a physical-amplitude statement without a validated transfer function.  
Fix: Either (a) remove the physical-amplitude claim or (b) supply a morphology-transfer calibration with quoted uncertainty.

**P4P-M1 (MAJOR, Table 5 + §5.1)**  
Literature amplitudes are listed as 2–20× above the floor, yet the model papers (Popławski 2010, 2012, 2016, 2020) supply no computed dipole amplitude. The “exceeds by 2–20×” statement is therefore an unquantified comparison between an observed-label floor and uncomputed theoretical numbers.  
Fix: Replace the ratio column with a clear statement that the cited works contain no numerical prediction, or retract the factor-of-X claim.

**P4P-M2 (MAJOR, §2.3 + §3)**  
The primary null (\(z_{\rm mom}=+0.635\), one-sided \(p=0.238\)) and the FSC harmonic diagnostic (\(\ell=1\), \(z=+6.923\)) are presented side-by-side without an explicit statement that they are not directly comparable (different supports, different estimators).  
Fix: Add a one-sentence qualifier at every juxtaposition of the two statistics.

**P4P-M3 (MAJOR, Fig. 1 caption + §3)**  
The Mollweide map is described as showing “no coherent large-scale structure.” Visual inspection of the rendered figure shows only pixel-scale noise; no quantitative test of residual power at \(\ell>1\) is reported.  
Fix: Add the \(\ell=2\)–\(\ell=5\) power spectrum of the map or state that it was computed and is consistent with noise.

**P4P-N1 (MINOR, p.1, abstract)**  
The phrase “8.47-Million-Galaxy DESI Chirality Catalog” rounds 8 474 531 to two significant figures while every other number is given to three or more.  
Fix: Use consistent significant-figure policy.

**P4P-N2 (MINOR, Table 2)**  
Footnote “† Not separately quoted in the archived release” is attached to a purity number that is used in the text.  
Fix: Either quote the number in the release or remove the claim that relies on it.

**P4P-N3 (NIT)**  
Multiple instances of “committed” as a verb (“the committed null”, “committed 10 000-draw null”) are non-standard statistical English.  
Fix: Replace with “fixed-occupancy label-randomization null” or equivalent.

**Summary recommendation**  
REJECT

The submitted PDF contains multiple internal versioning strings, draft markers dated in the future, and embedded filesystem paths to analysis scripts. These alone violate ApJS submission standards. In addition, the central quantitative exclusion of the rotating-black-hole-universe model rests on an uncalibrated conversion from an observed-label sensitivity floor to a physical spin-axis amplitude, and the literature comparison in Table 5 asserts numerical factors that the cited model papers do not supply. Until the internal artifacts are removed and the sensitivity-to-physical-amplitude step is either eliminated or rigorously calibrated, the manuscript does not meet the acceptance bar for ApJS.