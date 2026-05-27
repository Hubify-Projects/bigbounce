# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v63verify-v2_P3_v3_1_63
**Wall time**: 26.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=68932, completion=1372, total=70304

---

## PAPER-PER-B1 — Mis-citation of “Heinrich+2024” bispectrum forecast

The paper cites “Heinrich+2024 sigfnl ≈ 0.7 bispectrum-only forecast” as an external benchmark and attributes it to Heinrich et al. with the same citation key as Heinrich et al. (2023) in the bibliography, but there is no separate 2024 Heinrich et al. paper with a bispectrum-only \(\sigma(f_{\rm NL})\approx 0.7\) forecast on arXiv or ADS; the only widely cited work in this line is Heinrich et al. (2023) on SPHEREx multi-tracer forecasts, not a distinct “Heinrich+2024” publication.[1]  
**Fix:** Rephrase all references to “Heinrich+2024” as “the Heinrich et al. (2023) SPHEREx multi-tracer forecast (bispectrum component \(\sigma(f_{\rm NL})\sim\) few-tenths)” and ensure the bibliography has a single, correctly dated entry; if the 0.7 number is from internal calculations, label it explicitly as an internal estimate rather than an external “+2024” paper.

---

## PAPER-PER-B2 — Overstated claim about “Münchmeyer et al. consensus” range

The introduction claims “Münchmeyer et al. (2019) consensus \(\sigma_{f_{\rm NL}}\approx 0.4–0.9\) for SPHEREx-class surveys,” but Munchmeyer et al. (2019) study kSZ tomography with CMB-S4 and LSST, and do not provide a community “consensus” range for SPHEREx-class local \(f_{\rm NL}\); the 0.4–0.9 interval is not stated in that paper.[2]  
**Fix:** Replace the “Münchmeyer … consensus 0.4–0.9 for SPHEREx-class surveys” wording with a neutral description of their actual result (kSZ constraints with CMB-S4 + LSST), and if a 0.4–0.9 range is desired, either (a) justify it by explicit citation to a paper that actually quotes that range for SPHEREx, or (b) label it clearly as the author’s own synthesized estimate rather than a Münchmeyer “consensus.”

---

## PAPER-PER-M1 — Liang et al. (2023) data volume and anomaly count phrasing

The paper states that Liang et al. (2023) apply an autoencoder+flow to “approximately 250,000 DESI Early Data Release (EDR) spectra, finding 2,685 anomalies at a 1.07% rate,” whereas the Liang et al. paper describes operating on the DESI BGS sample from DESI EDR and quotes the BGS size and outlier fraction in that specific context, not a generic “DESI EDR 250k” corpus.[0]  
**Fix:** Tighten the wording to “Liang et al. (2023) apply an autoencoder plus normalizing flow to the DESI BGS sample in DESI Early Data Release, finding 2,685 outliers in the BGS subset (≈1% of that sample)” to match the actual sample definition and avoid implying they ran over an arbitrary 250k “EDR” spectra.

---

## PAPER-PER-M2 — Planck citation mismatch for “Planck 2018” vs. Planck 2015 parameters

The text cites “Planck (2018)” generically for CMB and cosmology context but then effectively uses standard \(\Lambda\)CDM numbers (e.g., \(H_0\approx 68\), \(\Omega_m\approx 0.31\)) that correspond numerically to the Planck 2015 cosmological-parameter paper (Planck 2015 results XIII, arXiv:1502.01589) rather than clearly linking to the 2018 legacy parameter release; the bibliography entry for Planck appears to be a generic 2018 overview, not the 2015 parameter paper actually providing those numbers.[3]  
**Fix:** Either (a) explicitly cite the 2018 parameters paper and update quoted numbers/uncertainties to its values, or (b) if using the 2015 values, change the in-text reference to “Planck 2015” and add the Planck 2015 XIII cosmological-parameters paper as a distinct reference keyed accordingly.

---

## PAPER-PER-m3 — eROSITA DR1 citation slightly underspecified

The eROSITA DR1 reference is given as “eROSITA DR1” with a generic description of “930,203 X-ray sources across the western Galactic hemisphere,” but the canonical eROSITA DR1 paper (Merloni et al. 2024, first all-sky survey) explicitly describes four- or eight-pass all-sky coverage with particular footprint and depth, and does not describe itself as a “western hemisphere only” catalog.[4]  
**Fix:** Align the footprint description with the DR1 paper: state that eROSITA DR1 covers the full-sky eRASS1 survey (with appropriate qualifiers about exposure depth and any actual mask you applied) and, if you internally limited to a western hemisphere subcatalog, say so explicitly as a selection made in this work rather than as a property of the DR1 release.

---

## PAPER-PER-n1 — Ambiguous SPHEREx reference metadata

The SPHEREx mission is cited via “SPHEREx 2014” as a single reference for both mission description and sensitivity to local \(f_{\rm NL}\), but the 2014 Doré et al. white paper focuses on mission concept and broad science case and does not by itself give the specific \(3–5\sigma\) detection significance for the matter-bounce \(f_{\rm NL} = -35/8\) quoted here.[5]  
**Fix:** Keep Doré et al. (2014) as the mission description, but add an explicit citation to a forecast paper that actually computes SPHEREx \(f_{\rm NL}\) sensitivity (e.g., Heinrich et al. 2023) when quoting a \(3–5\sigma\) figure, and make clear which numbers are drawn from which paper.
