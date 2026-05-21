# paper2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R23_P2_v1_7_30
**Wall time**: 26.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30951, completion=2036, total=32987

---

## PAPER-PER-B1 — Mis-cited Heinrich et al. 2024 forecast

**Issue (MAJOR):** The paper repeatedly cites “Heinrich et al. 2024 ” as a SPHEREx multi-tracer galaxy *bispectrum* forecast with σ(f_NL^local) ≈ 0.7 from the bispectrum alone.[1] In reality, Heinrich, Dvorkin & Hu (arXiv:2303.08874) present SPHEREx *power-spectrum scale-dependent bias* forecasts; there is no published Heinrich+ paper giving σ(f_NL)=0.7 from the multi-tracer galaxy bispectrum channel. The abstract’s statement “multi-tracer bispectrum … σ(f_NL) ≈ 0.7 (Heinrich et al. 2024, Fig. 6 / Table 3, multi-tracer galaxy bispectrum forecast)” and §4’s “dedicated multi-tracer bispectrum analysis” therefore over-claim what Heinrich+ actually did.[1]

**Location:** Abstract (first paragraph after template-mismatch discussion); §4 “SPHEREx Forecast” (first two paragraphs and repeated references to a “multi-tracer bispectrum” forecast from Heinrich et al.).

**Fix:** Recast all uses of Heinrich et al. to correctly describe them as *power-spectrum SDB* forecasts, and either (a) remove claims that σ(f_NL)=0.7 comes from a published multi-tracer bispectrum forecast, or (b) clearly mark the bispectrum σ(f_NL) value as this work’s own recast built from Heinrich et al.’s power-spectrum Fisher matrix, not as a Heinrich et al. result. Update the abstract to say “SPHEREx forecasts σ(f_NL) ≈ 0.7 from scale-dependent bias (Heinrich et al. 2023)” and move any bispectrum σ(f_NL) numbers into a section explicitly labeled as this paper’s new Fisher calculation.


## PAPER-PER-B2 — Nonexistent Jung 2025 Planck PR4/NPIPE f_NL citation

**Issue (BLOCKER):** §10.1 cites “Planck PR4/NPIPE (CMB bispectrum, f_NL = -0.1 ± 5.0) (Jung2025PlanckPR4fNL)” and claims a PR4/NPIPE non‑Gaussianity reanalysis with that result.[1] There is currently no arXiv or journal paper with that exact author–year–result combination; the bibkey “Jung2025PlanckPR4fNL” appears to be internal/fictional, and the quoted central value and error bar do not match any public Planck PR3/PR4 local-f_NL constraint on arXiv.[1] This turns a key “current data” anchor into an uncitable phantom reference.

**Location:** §10.1 “Planck + DESI Recast”, first sentence and parenthetical reference to Jung2025PlanckPR4fNL.

**Fix:** Replace “Jung2025PlanckPR4fNL” and the quoted f_NL = -0.1 ± 5.0 with the latest *published* Planck PR3 result (Planck 2019: f_NL^local = -0.9 ± 5.1) and cite the official Planck Collaboration non-Gaussianity paper.[1] If a PR4/NPIPE f_NL analysis by Jung et al. is still in preparation, label it explicitly as “private communication / in prep.” and do not quote numerical values as if they were from a published paper.


## PAPER-PER-M1 — Ambiguous / likely wrong “WilsonEwing:2012” citation

**Issue (MAJOR):** The paper attributes the “Wilson‑Ewing ΛCDM quasi-dust model” and the relation n_s = 1 + 12 w in a quasi-dust bounce to “WilsonEwing:2012”. However, the well-known bounce paper by Wilson‑Ewing is “Ekpyrotic loop quantum cosmology” (JCAP 1308 (2013) 013, arXiv:1306.6582) rather than a 2012 ΛCDM quasi-dust matter bounce model.[1] I could not find a 2012 Wilson‑Ewing paper that exactly matches the described “ΛCDM quasi-dust matter bounce” plus n_s = 1 + 12w result; the citation is at best ambiguous and likely pointing to the wrong work.

**Location:** §2.4 “The Viable Model”; §2.3 Assumptions (e); §10.2 consistency relation paragraph referencing “Ref. ”.

**Fix:** Verify which specific Wilson‑Ewing paper actually contains (i) the quasi‑dust bounce model with w ≈ -0.003 tuned to n_s, and (ii) the explicit n_s = 1 + 12w formula. Update the citation to the correct arXiv ID and year (probably arXiv:1306.6582, JCAP 2013) and adjust the year tag in the text and bibkey accordingly. If the n_s formula is only derived in a different work, split the citation and attribute each result to the correct source.


## PAPER-PER-M2 — Misleading Heinrich+ multi-tracer/b_φ treatment

**Issue (MAJOR):** The paper states that Heinrich et al. treat b_φ via “a fixed universality relation” and that marginalizing b_φ as a free parameter per tracer bin could widen σ(f_NL) by 20–50%.[1] Heinrich et al. 2023’s SPHEREx forecast, however, already explores PNG-bias uncertainties within their own framework and does not simply hard‑fix b_φ across the board; the current text oversimplifies and misrepresents their treatment, using that misrepresentation to motivate an extra degradation budget.

**Location:** §4 “SPHEREx Forecast”, third paragraph (“Three caveats apply… First, the Heinrich et al. forecast marginalizes over… but treats the PNG bias parameter b_φ with a fixed universality relation…”).

**Fix:** Re-read Heinrich et al. carefully and align the description with what they actually do: specify exactly how b_φ is modeled/marginalized in their Fisher setup and only introduce extra 20–50% “could widen” factors as a clearly labeled *hypothetical* variation beyond Heinrich+, not as a correction to Heinrich+. Adjust the systematic budget text so that any additional b_φ degradation is explicitly attributed to new assumptions in this work, not to mischaracterized limitations of Heinrich et al.


## PAPER-PER-m1 — Mischaracterization of Cai & Brandenberger 2014 normalization

**Issue (minor):** The text repeatedly labels Cai & Brandenberger (2014) as using a “Li & Brandenberger (c=1) normalization convention”, and describes their f_NL = -35/16 as essentially a pure convention difference relative to Cai et al. 2009, later corrected by an “in-in commutator doubling.”[1][2] In reality, Cai & Brandenberger (arXiv:0903.0631) already present a full bispectrum calculation in their own normalization; the split into “c=1 vs c=2” plus a missing time-ordering is partly this paper’s reinterpretation and should not be presented as an explicit self-identification by Cai & Brandenberger.

**Location:** Abstract (long convention caveat near the end); §2.3 and Appendix A, where “Li & Brandenberger (c=1)” and “Cai vs Li-Brandenberger” language is used.

**Fix:** Rephrase to clearly distinguish between what Cai & Brandenberger explicitly state and what this work infers. For example: “Cai & Brandenberger (2009) quote f_NL = -35/16 in their normalization; by tracing their operator and template conventions we find this corresponds to the same physical bispectrum as Cai et al. (2009)’s f_NL = -35/8 in the Planck convention.” Avoid implying that Cai & Brandenberger themselves adopt a “c=1 label” or that they explicitly omit an in-in time ordering unless you can quote that from their text.


## PAPER-PER-n1 — Unverified / likely incorrect references to “Zhu & Cai 2026 echoes” and “Jolicoeur:2025”

**Issue (nit):** Several citations appear to refer to future or non-existent works: e.g. “Zhu & Cai (2026 echoes)” for dark-energy‑from‑bounce constructions, and “Jolicoeur:2025” for GR projection effects, both with year tags later than any current arXiv entry I can find matching those titles/contexts.[1] They look like placeholder or speculative references rather than real papers.

**Location:** Assumptions paragraph in §2.3 (Zhu & Cai 2026 echoes); §7.1 and §7.3 (Jolicoeur:2025).  

**Fix:** Either (a) replace these with real, citable arXiv/journal references that actually discuss the claimed dark-energy bounce models and GR projection forecasts, or (b) explicitly mark them as “in prep./private communication” *without* using them as quantitative inputs to the forecast. If no suitable published source exists, remove quantitative claims that depend on these references.
