# paper1b R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R23_P1B_v1B_0_20
**Wall time**: 23.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=19188, completion=1130, total=20318

---

## PAPER-PER-M1 — Mis-cited Planck NPIPE birefringence paper

**Issue (MAJOR).** In Sec. \ref{sec:data_cmb} and Eq. \eqref{eq:beta_combined} the Planck NPIPE measurement is cited as “DiegoPalazuelos2022” but the value quoted, \(\beta = 0.30^\circ \pm 0.11^\circ\), corresponds to Eskilt’s Planck DR4/NPIPE analysis, not a Diego-Palazuelos paper; Diego-Palazuelos leads an ACT DR6 birefringence analysis instead.[2] The “DiegoPalazuelos2022” key is therefore mismatched to the Planck result and likely points to the wrong arXiv ID / metadata in the .bib.

**Fix.** Re-point the Planck NPIPE birefringence citation to Eskilt’s Planck DR4 frequency-dependent birefringence paper (correct authors, title, arXiv:2201.13347, A&A 662 A10) and reserve “Diego Palazuelos” for ACT-only work.[2] Check the .bib entry to ensure the title, arXiv ID, authors, and journal all match Eskilt’s paper rather than the ACT DR6 paper.

---

## PAPER-PER-M2 — Ambiguous / likely fused Eskilt joint Planck+ACT reference

**Issue (MAJOR).** The joint Planck+ACT value \(\beta = 0.342^\circ \pm 0.094^\circ\) is attributed to “Eskilt 2022b” / “Eskilt \etal” without a clear, unique bibliographic mapping to the actual joint-analysis paper; the only Eskilt Planck DR4 birefringence paper readily identifiable is the Planck-only DR4 analysis.[2] This raises a risk that the “Eskilt2022b” entry in the .bib fuses Eskilt’s Planck-only paper metadata with a different arXiv ID (or an as‑yet-unverified joint Planck+ACT preprint).

**Fix.** Explicitly identify and verify the joint Planck+ACT birefringence paper (correct arXiv ID, title, author list, and journal) and ensure “Eskilt2022b” points to it, not to the Planck‑only DR4 paper.[2] If no such peer‑reviewed joint paper exists yet, relabel the reference as an internal or in‑prep analysis and avoid treating it as a published journal result.

---

## PAPER-PER-m1 — Check ACT DR6 birefringence metadata for Diego Palazuelos

**Issue (minor).** The ACT DR6 birefringence value \(\beta = 0.215^\circ \pm 0.074^\circ\) is cited as “DiegoPalazuelos2025”, but ACT DR6 cosmology papers currently visible on arXiv and ADS (ACT DR6 lensing, power spectra, etc.) are 2023–2024 and must be carefully matched for title and arXiv ID once the EB‑birefringence paper is public.[1] Without explicit verification, there is a risk of using a placeholder key whose year or arXiv ID does not match the eventual ACT DR6 birefringence publication.

**Fix.** Once the ACT DR6 birefringence paper is available, update “DiegoPalazuelos2025” to match its actual bibliographic details (title, arXiv ID, year, journal) and confirm that the quoted value \(\beta = 0.215^\circ \pm 0.074^\circ\) is taken directly from that source.[1] If the result is currently from an internal or conference proceeding, label it accordingly rather than as a generic 2025 journal citation.

---

## PAPER-PER-m2 — Eskilt 2022 Planck DR4 result should be explicitly cross-checked

**Issue (minor).** The text uses a Planck NPIPE value \(\beta = 0.30^\circ \pm 0.11^\circ\) as an input to an auxiliary inverse-variance combination, but Eskilt’s Planck DR4 analysis quotes \(\beta = 0.33^\circ \pm 0.10^\circ\) for the frequency‑independent case and closely related numbers for specific foreground treatments.[2] The paper does not state which exact configuration of Eskilt (sky fraction, foreground model, or frequency selection) is being mapped to the 0.30° ± 0.11° figure, which can create confusion about what is actually being combined.

**Fix.** Add a parenthetical specifying which Eskilt DR4 configuration is used (e.g., “Planck DR4 nearly full‑sky, no foreground EB modeling, \(\beta = 0.29^\circ\pm 0.11^\circ\)” or similar) and verify that the 0.30° ± 0.11° number matches that particular table or figure.[2] If it does not, adjust the quoted value to exactly match the chosen configuration or change the configuration to one that yields the cited number.
