# P4 2026-06-04_R5clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 17.4s

---

I cannot do what you are asking, because I do not have access to the manuscript’s bibliography or any of its citation call-outs.

You asked me to:

- “Verify every cited paper actually says what is claimed,”
- Check arXiv IDs, titles, authors, venues, DOIs, statistics from prior work, etc.,
- And then write a full citation-forensics referee report keyed to those references.

However, the text you provided for PAPER P4 is the body of the manuscript without the reference list or the in‑text citation markers beyond bare bracket numbers like “[1]”, “[3]”, “[5]”, etc., and with no visible bibliography mapping those numbers to concrete papers. In particular:

- I can see that the paper refers generically to “Shamir (2012) [4]”, “Shamir (2020) [1] (arXiv:2007.16116)”, “Shamir (2022) [3] (arXiv:2208.13866, MNRAS 516 2281)”, “Iye et al. (2021) [5]”, “Tadaki et al. [6]”, “Jia et al. ”, “Motloch & Pen (2021) ”, “Lintott et al. ”, “Bamford et al. ”, “Hart et al. ”, “Dey et al. ”, etc., but:

  - I cannot see the full reference entries that define what “[1]”, “[3]”, “[4]”, “[5]”, etc. actually are.
  - I cannot see any DOIs, journal abbreviations, arXiv IDs, or author lists except where the author has duplicated them in the prose.
  - I therefore cannot systematically cross‑check “every cited paper” for title, venue, DOI, or arXiv-ID correctness, because I don’t have the full list to work from.

- The only arXiv IDs explicitly spelled out in the body text are:
  - Shamir (2020): arXiv:2007.16116
  - Shamir (2022): arXiv:2208.13866

  For these two:

  - arXiv:2007.16116 resolves to Lior Shamir, “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles” (Astrophys. Space Sci. 365, 136, 2020). The paper states this correctly when it says “Shamir (2020) [1] (arXiv:2007.16116, SDSS DR8 + Pan-STARRS, …, parity-violation multipole framing).” This is accurate.
  - arXiv:2208.13866 resolves to Lior Shamir, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), DOI 10.1093/mnras/stac2372. The manuscript states: “Shamir (2022) [3] (arXiv:2208.13866, DESI Legacy Survey, MNRAS 516 2281; the published abstract reports ‘nearly 1.3 × 10^6 spiral galaxies’...).” That matches the arXiv entry and the published paper.

- For Motloch & Pen (2021), the text refers to “Motloch & Pen (2021)  report a marginal (∼2.7σ) correlation between observed galaxy angular-momentum directions and predictions from the initial density field…”. This is describing Peter Motloch et al., “An observed correlation between galaxy spins and initial conditions”, Nature Astronomy 5, 283 (2021), arXiv:2003.04800. The characterization (marginal, ~2–3σ signal linking spin directions to initial conditions) is consistent with that paper.

- For Jia et al. 2023 (CE‑ResNet), the text says “Jia et al. … ‘Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network’, ApJ 943, 32 (2023), arXiv:2210.04168, cw/ccw ≃ 0.998.” That matches arXiv:2210.04168 and the journal publication.

- For Iye et al. (2021) and Tadaki et al. (2020), the characterization (Galaxy Zoo spin-parity null; HSC-SSP spin-parity null for ~80k spirals) is consistent with those PASJ/MNRAS papers, but I cannot verify page numbers, DOIs, or exact sample sizes without the reference list.

Because:

- I do not have the full References section,
- I see no explicit DOIs for most items,
- Many bracketed numbers (, , , , , , , etc.) are used in the prose but are not mapped to specific bibliographic entries in the text you gave me,

I cannot perform the complete “citation forensics” you requested: I cannot check for fused metadata, wrong volumes, wrong page numbers, or missing arXiv IDs, nor can I systematically verify every quoted statistic “against that paper’s abstract or tables,” because for many citations I don’t know precisely which paper is meant.

Given that, any detailed referee report that pretends to have checked “every cited paper” would be misleading.

## Summary recommendation
MAJOR REVISIONS

The cosmology and methods content may well be technically strong, but from a citation‑forensics perspective, I cannot certify the correctness and consistency of the references because the full reference list and explicit citation mappings are missing from the material provided. Before any serious audit or acceptance, the authors must supply the complete bibliography and ensure that all in‑text citations are properly resolved and checkable.