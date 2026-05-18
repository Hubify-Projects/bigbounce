# P3_v3149_R11 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1330pt
**Wall time**: 24.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=63133, completion=1496, total=64629

---

## PAPER-PER-B1 — Nicolaou et al. 2026 looks confabulated (BLOCKER)

Section: Introduction, paragraph 2 (“Nicolaou et al. 2026 … Astronomaly … on 208,000 EDR spectra”).  

Issue: I cannot find any arXiv or journal paper matching “Nicolaou et al. 2026” doing a DESI EDR anomaly search with a variational autoencoder and Astronomaly on 208k spectra; the combination of author, year, method, dataset, and framework appears fabricated rather than pointing to a real, citable work.[1]  

Fix: Either (a) replace this with a real, verifiable reference (with correct authors, year, arXiv ID, title, and a brief description that matches the actual paper), or (b) delete the sentence and drop the citation entirely to avoid citing a non‑existent study.

---

## PAPER-PER-M1 — Liang et al. metadata slightly off (minor)

Section: Introduction, paragraph 2; Abstract (Liang et al. citation and numbers).  

Issue: The paper correctly cites Liang et al. as “Liang et al. 2023” with arXiv:2307.07664 and the DESI Early Data Release BGS outlier search, which is real and matches the description.[1] However, the text attributes “approximately 250,000 DESI EDR spectra” and “1.07% rate, 2,685 anomalies” whereas Liang et al. 2023 describes outlier detection in the DESI Bright Galaxy Survey EDR sample without using exactly those rounded numbers in the abstract; the numbers are plausible but should be explicitly checked against the body of Liang et al. (rather than inferred) to avoid subtle drift.  

Fix: Verify the exact EDR sample size and outlier count from Liang et al. (table or methods section) and adjust the text so the numbers and survey description match the paper exactly, or else phrase them explicitly as approximate (“of order 2.7k outliers out of ≈2.5×10^5 BGS spectra”) and keep the BGS qualifier.

---

## PAPER-PER-M2 — SPHEREx / Heinrich et al. description needs tightening (major)

Section: Introduction, paragraph 2; §5 cosmology discussion.  

Issue: The text attributes to “Heinrich et al. 2023” and “Heinrich+2024” a SPHEREx multi‑tracer bispectrum forecast with σ(fNL) ≈ 0.7, and contrasts it with Muenchmeyer et al. SPHEREx-class forecasts; while Heinrich–Doré–Krause do exist and study multi‑tracer / bispectrum constraints for SPHEREx‑like surveys, the exact chain “Heinrich+2024 σfNL ≈ 0.7 bispectrum‑only headline; internal Fisher σ ≈ 0.07–0.12 using special kernels, 3–10× tighter than Muenchmeyer 0.4–0.9” is not stated this way in any single published paper and risks over‑specific, fused metadata.[1]  

Fix: Re‑read the relevant Heinrich, Muenchmeyer, and SPHEREx forecast papers and rewrite this paragraph so that (i) each σ(fNL) value and quoted range is directly present in the cited source, (ii) “internal Fisher” numbers that are not in a publication are clearly labeled as “our internal computation” rather than attributed to Heinrich et al., and (iii) any comparison to Muenchmeyer et al. uses their stated σ(fNL) ranges, not a compressed “consensus” band.

---

## PAPER-PER-m3 — SPHEREx 2014 white paper citation is okay but loosely framed (minor)

Section: Introduction, cosmology paragraph (SPHEREx satellite).  

Issue: The SPHEREx 2014 white paper (Doré et al. 2014, arXiv:1412.4872) is real and correctly described as outlining SPHEREx’s ability to test local fNL at a few‑σ level; however, the phrase “testable … at 3–5σ realistic significance” reads as if it were an explicit quoted performance number rather than an interpretation of the forecast curves.[1]  

Fix: Rephrase to make clear that “3–5σ” is your interpretation of the forecasted σ(fNL) range (e.g. “SPHEREx forecasts suggest that |fNL| ≈ 4 could be probed at several‑σ significance”), and ensure the actual σ(fNL) values you imply are present in the SPHEREx paper or in a correctly cited forecast.

---

## PAPER-PER-m4 — Citation coverage for NANOGrav / PTA work incomplete (minor)

Section: §5.2 / Appendix PTA MCMC (NANOGrav 15‑year HD‑correlated KDE likelihood and “new physics” paper).  

Issue: The text refers to the NANOGrav 15‑yr GWB detection paper and the KDE free‑spectrum likelihood, as well as to the “new‑physics companion paper,” and attributes detailed data‑release identifiers and spectral‑index expectations; multiple real NANOGrav 15‑yr papers exist (Agazie et al. 2023 detection, Agazie et al. 2023 new‑physics constraints, etc.), but the current text does not give explicit arXiv IDs or titles, which makes it hard to verify that each quoted result (HD‑correlated KDE pack, γ ranges, and model roster) is actually present in the cited work.[1]  

Fix: Add explicit citations with arXiv IDs for (a) the main NANOGrav 15‑yr stochastic background detection paper and (b) the 15‑yr new‑physics paper that surveys cosmological backgrounds, and ensure that any quoted numbers (posterior γ ranges, model lists) are traceable to those papers; if some numbers come from your own re‑analysis, label them as such instead of implying they are verbatim from the NANOGrav publications.

---

## PAPER-PER-n1 — General arXiv ID hygiene suggestion (nit)

Section: Global bibliography and text (all external works).  

Issue: Many external references (e.g., DESI DR1 documentation, eROSITA DR1 release, ACT DR6, some Gaia/NEOWISE documentation) are given as descriptive citations without explicit arXiv IDs or DOIs; while this is not wrong, it makes forensic verification harder and increases the risk of subtle metadata drift in future drafts.[1]  

Fix: For every paper‑like citation that has an arXiv entry or DOI, add the arXiv ID (and DOI if available) into the bibliography, and check that titles, author lists, and years match the corresponding arXiv or publisher landing pages; this will also make it easier to detect and avoid fused‑metadata errors in later revisions.


