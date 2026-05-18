# P1B_v1B019_R15 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1600pt
**Wall time**: 33.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=18804, completion=2385, total=21189

---

## Finding 1 — PAPER-CITE-B1 (MAJOR)

Section: Spectator-ALP consistency check, citations to Eskilt cosmic-birefringence work (e.g., “Eskilt2022”, “Eskilt2022b”).

Issue: The manuscript attributes the joint Planck+ACT cosmic birefringence result \(\beta = 0.342^\circ \pm 0.094^\circ\) at \(3.6\sigma\) to Eskilt et al. under a 2022 label, but the only Planck DR4 birefringence paper by Eskilt in 2022 is arXiv:2201.13347 (“Frequency-Dependent Constraints on Cosmic Birefringence from the LFI and HFI Planck Data Release 4”), which reports Planck-only constraints (e.g., \(\beta = 0.33^\circ \pm 0.10^\circ\) assuming no frequency dependence) and does not contain any joint Planck+ACT measurement or the specific \(\beta = 0.342^\circ \pm 0.094^\circ\) joint value cited here.[1] This indicates that either the arXiv ID / year / title for the joint Planck+ACT analysis are wrong, or the quoted joint value actually comes from a different paper (potentially 2023–2025) and is being fused with the 2201.13347 metadata.

Fix (1–2 sentences): Identify the correct publication that reports the joint Planck+ACT DR4/DR6 analysis with \(\beta = 0.342^\circ \pm 0.094^\circ\) (check arXiv and journal metadata for an Eskilt et al. paper explicitly combining Planck and ACT) and update the BibTeX entry so that its authors, year, title, journal, and arXiv ID match that work exactly. If instead the quoted number is a private or internal fit based on combining Planck DR4 with public ACT EB spectra, relabel it as such and remove the “Eskilt et al.” attribution and external-citation styling.


## Finding 2 — PAPER-CITE-B2 (MAJOR)

Section: Data Methods: CMB E–B Analysis (“Birefringence measurements are adopted from the published literature: \(\beta = 0.30^\circ\pm 0.11^\circ\) (Planck NPIPE) and \(\beta = 0.215^\circ\pm 0.074^\circ\) (ACT DR6). The spectator ALP analysis (Sec. 6) uses these published values.”).

Issue: The Planck DR4 frequency-dependent birefringence paper arXiv:2201.13347 (Eskilt 2022) reports Planck-only results (e.g., \(\beta = 0.33^\circ \pm 0.10^\circ\) under a frequency-independent assumption) but does not quote the specific pair of values \(\beta = 0.30^\circ \pm 0.11^\circ\) (NPIPE) and \(\beta = 0.215^\circ \pm 0.074^\circ\) (ACT DR6) as a standard pair to be directly combined; these look like they may be drawn from later, separate NPIPE-focused and ACT DR6-focused analyses, not both from arXiv:2201.13347.[1] Without explicit, correctly-identified references for each of these central numbers, the bibliography currently underspecifies their provenance and risks implying that 2201.13347 alone is their source.

Fix (1–2 sentences): For each of the two “headline” birefringence values (\(0.30^\circ \pm 0.11^\circ\) NPIPE and \(0.215^\circ \pm 0.074^\circ\) ACT DR6), add a dedicated bibliographic entry pointing to the exact arXiv ID and journal paper that reports that measurement (Planck NPIPE-focused paper and ACT DR6 birefringence paper, respectively), and ensure that the in-text citations next to each number point to these specific references rather than generically to a single Eskilt 2022 Planck-DR4 paper.[1]


## Finding 3 — PAPER-CITE-B3 (MAJOR)

Section: “Independent cross-validation” paragraph in the MCMC verification section (reference “ECTorsionDESI2025”).

Issue: The text claims that “Liu et al. [ECTorsionDESI2025] constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (\(\Delta\mathrm{AIC}=-5.7\) to \(-6.6\)).” A search of arXiv around “Einstein–Cartan torsion DESI DR2 Pantheon+ DES-SN5YR Planck 2018” and likely author combinations (including “Liu”) does not reveal any paper that exactly matches this description, and no such title appears in common bibliographic indices (ADS/arXiv) for 2024–2025; instead, the arXiv IDs checked (sample cosmology and astroph papers with similar time stamps) correspond to completely unrelated topics.[2][3] This strongly suggests that “ECTorsionDESI2025” is either not yet a real public paper or is being used as a placeholder with invented metadata (author, dataset list, AIC numbers) that do not correspond to a verifiable publication.

Fix (1–2 sentences): Remove the “Liu et al. [ECTorsionDESI2025]” cross-validation claim unless you can supply a real, publicly available reference (with correct arXiv ID, title, and authors) that actually reports an EC torsion analysis on DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018 with the stated \(\Delta\mathrm{AIC}\) preference; if such a paper is still in preparation or under review, label it explicitly as “in prep.” or “private communication” and strip out the quantitative AIC statement until it can be backed by a citable source.


## Finding 4 — PAPER-CITE-M1 (minor)

Section: “LiteBIRD forecast” in the ALP/birefringence section (“LiteBIRD is projected to achieve \(\sigma(\beta)\approx 0.03^\circ\) [LiteBIRD2023].”).

Issue: The LiteBIRD collaboration forecast papers (e.g., “LiteBIRD: A Satellite for the Studies of B-Mode Polarization and Inflation from Cosmic Microwave Background Radiation,” and follow-up design/forecast papers) provide sensitivity forecasts on tensor-to-scalar ratio \(r\), polarization noise, and generalized cosmic birefringence constraints, but the quoted \(\sigma(\beta)\approx 0.03^\circ\) number is not trivially traceable to a single “LiteBIRD 2023” paper upon inspection of recent arXiv entries; the arXiv IDs checked around 2023 for LiteBIRD are broader CMB-forecast discussions and do not show that precise scalar constraint in an obvious form.[4] As written, this looks more like a distilled secondary estimate than a directly lifted headline number, and the paper does not specify exactly which LiteBIRD document it comes from or the underlying assumptions (sky fraction, frequency coverage, systematics model).

Fix (1–2 sentences): Either (a) replace the single \(\sigma(\beta)\approx 0.03^\circ\) statement with a range explicitly tied to a specific LiteBIRD forecast paper and cite that paper by correct arXiv ID and title, or (b) keep the central value but add an explicit reference to the exact figure/table and forecast assumptions in the LiteBIRD publication from which it is derived, so that a reader can verify the number directly.


## Finding 5 — PAPER-CITE-N1 (nit)

Section: Reproducibility materials and claims classification (discussion of HuggingFace datasets containing “NaMaster pipeline artifacts (mask, MC seeds, output spectra)” and ALP MCMC chains).

Issue: The text treats the existence of specific HuggingFace datasets with detailed cosmology content as established fact but does not provide dataset DOIs, dataset IDs, or URLs, and a search on HuggingFace for obvious name patterns (e.g., “bigbounce NaMaster Houston Golden ALP MCMC”) does not readily surface a matching public dataset.[5] This is a reproducibility-citation nit rather than a physics error, but the current wording makes these artifacts sound already-published and easily discoverable when they may still be private or named differently.

Fix (1–2 sentences): Either add explicit dataset identifiers (e.g., “huggingface.co/datasets/Hubify-Projects/bigbounce-namaster-artifacts”) for each referenced HuggingFace dataset, or soften the language to “will be released” / “planned” if they are not yet public, so that readers are not misled into expecting currently non-discoverable resources.


## Finding 6 — PAPER-CITE-N2 (nit)

Section: Global bibliography expectations vs. in-text shorthand names (e.g., “DESI2025DR2”, “DESI2024”, “DESI2025DR2” cited in connection with DESI BAO and \(w_0w_a\) results).

Issue: The manuscript uses compact keys like “DESI2024”, “DESI2025DR2” for major DESI releases and also refers to “DESI 2024 DR1 BAO” and “DESI DR2 \(w_0w_a\)” in the prose, but the arXiv entries checked for DESI BAO releases around 2024–2025 often have more detailed titles (“DESI 2024 results: baryon acoustic oscillations from…”) and the exact year/release mapping is easy to get wrong.[6] Without seeing the actual BibTeX file, there is a low-level risk of fused or off-by-one metadata (e.g., DR1 numbers cited as “DR2 2025” or vice versa), especially because the text predicts 2025-era DR2 results while we are still in 2026.

Fix (1–2 sentences): Perform a pass over the DESI citations to ensure that each in-text “DESI 2024 DR1 BAO” / “DESI2025DR2” label maps to the correct arXiv ID and official title (“DESI 2024 results: …”, “DESI 2025 results: …”) and that the release number (DR1 vs DR2) and year in the key match the actual paper; adjust the shorthand keys or in-text years if they do not align with the official DESI publication metadata.[6]


---

Do you want me to also sanity-check a sample of the DES, Pantheon+, and DES-SN5YR citation tuples (author–year–arXiv ID–journal) for fused or mismatched metadata? 


