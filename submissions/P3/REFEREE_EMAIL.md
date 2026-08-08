# Referee-Routing Email — P3

**Subject:** Expert read requested: a 268k-source multi-survey anomaly catalog — a scope/venue judgment call

---

Dear [RECIPIENT NAME / astrostatistics or multi-survey anomaly detection],

I'm writing to ask for a short expert read on a submission-ready paper before I finalize the venue.

The paper (v3.1.140, 2026-07-06) presents a validated catalog-grade subset of 268,519 unique anomalies — obtained by applying an autoencoder framework to 37.3 million sources and CMB map patches across seven surveys (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, NEOWISE), with per-survey native retraining and 7-way positional deduplication. The four injection-recovery-passing components form the headline; exploratory tiers are labeled and sequestered separately.

In this revision, two items were closed: (1) **DESI injection-recovery is now real and committed** — a full 5σ test on real DESI-DR1 spectra produced broad-class recovery 99–100% across 3 validation gates, at parity with SDSS and Planck injection-recovery; narrow-line injection floor ≥15σ is disclosed. (2) **Scaler-leakage audit is complete** — the spectroscopic path (DESI/SDSS/LAMOST/Planck) normalizes per-spectrum and is split-independent; the J=0.862/J=0.732 headline Jaccard gates are confirmed leak-free. The tabular tiers (eROSITA/NEOWISE/Gaia) do use a full-sample scaler, already disclosed and bounded by a committed train-split-only refit control, and those tiers are not headline-load-bearing.

On status: the paper has been through a multi-model LLM-referee process (browser-tier ChatGPT/Grok/Gemini plus API-tier reviews), with raw review text archived in the public repository. On the identical PDF the verdicts span the full range: grok-4.3 (API) MINOR REVISIONS ("central claim supported"); Grok (EXT) / Gemini MAJOR REVISIONS (Gemini recommends a catalog venue, ApJS/MNRAS); ChatGPT and openai REJECT (a structural floor the harshest referees apply to any real manuscript). The recurring flags — eROSITA score-axis irreproducibility, the lineage-inferred Gaia preprocessing script — are disclosed as exploratory-tier limitations excluded from the 268,519 validated headline. The paper carries zero genuinely-new correctness defects. The open questions are matters of human expert judgment: **(1) is a disclosed, sequestered, exploratory-tier score-axis non-reproducibility (eROSITA production threshold not recoverable across 16 monotone rescalings — tier excluded from the validated headline) acceptable in a catalog paper, or does a catalog require every tier fully reproducible?** And **(2) is this an ApJS/MNRAS catalog/data-release paper or a PRD paper — the recurring venue question, given the cosmology sections are non-detections?**

Three low-pressure options, whichever fits: (a) a brief opinion on either of those scope calls; (b) if the eROSITA reproducibility or Gaia provenance recovery interests you, I'd welcome you as a co-author; or (c) a pointer to the right referee or venue.

Program site: https://bigbounce.hubify.app · Code: https://github.com/Hubify-Projects/bigbounce

The full PDF and a one-page referee-concern summary are attached.

With thanks,
Houston Golden — houston@hubify.com

---

**[ATTACH]** paper3_draft.pdf + REFEREE_HANDOFF.md (one-page referee-concern summary)
