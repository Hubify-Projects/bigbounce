# EXT10 Harvest — P1B — ChatGPT
- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5cf-db00-83e8-b824-21b626a0d9ab
- PDF md5: 06410d7c
- Harvested: 2026-06-13 15:16 PDT

---

## Referee report — MNRAS/PRD/JCAP style

**Manuscript:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Version reviewed:** Paper 1B v1B.0.68, 20-page PDF dated 13 June 2026.

---

**Recommendation: MINOR REVISIONS**

This is a careful technical companion paper documenting three limited-scope checks: a stock-CAMB ΛCDM+ΔNeff MCMC proxy, a NaMaster pseudo-Cℓ injection-recovery validation, and a spectator-ALP consistency exercise for cosmic birefringence. The manuscript is unusually explicit about what the analyses do not establish. I do not find a publication-blocking flaw in the headline numerical claims. The paper should be publishable after a small number of clarifying corrections, mainly to remove two remaining wording inconsistencies that could otherwise be misread as stronger claims than the computations support.

---

**1. Recommendation**

**MINOR REVISIONS.** No new MCMC production run, NaMaster production run, or ALP MCMC run is required for publication, provided the textual inconsistencies below are corrected.

---

**2. BLOCKERS — must fix before publication**

None. I found no load-bearing unsupported claim that would require rejection or major scientific rework.

---

**3. MAJORS — should fix**

**Major 1 — The "same likelihood stack" phrase is factually inconsistent with Table III**
Location: Sec. V.B, "Independent re-run cross-check"; PDF p. 10; .tex line 317.
Issue: Table III defines the frozen ΛCDM+ΔNeff Planck block as planck_2018_lowl.EE + planck_2018_lensing.clik, whereas line 317 describes the independent rerun as the "same likelihood stack" but lists planck_2020_lollipop.lowlE + planckpr4lensing. The rerun is useful (reproduces ΔNeff within 0.04σ), but it is not literally the same likelihood stack as Table III.
Proposed fix: Replace "same likelihood stack" with "A dedicated near-stack re-run / release-pairing robustness re-run of the Planck+BAO+SN ΛCDM+ΔNeff configuration…" or correct the listed likelihood names to match Table III exactly.

**Major 2 — The conclusion still says "m∼H0" immediately after giving a spectator-safe median m≃40.5H0**
Location: Sec. VII, "Spectator-ALP consistency"; PDF p. 14; .tex line 377.
Issue: Table IV gives the Ωa<0.01 spectator-safe subset as 13% posterior mass with m/H0 = 6.0/40.5/238. The conclusion then states that "an ALP with fa∼MPl, m∼H0" is consistent, despite the median being 40.5H0.
Proposed fix: Replace the sentence with: "Within the Ωa<0.01 spectator-safe subset (13% of the posterior mass; m/H0 = 6.0/40.5/238 at 16/50/84%; θi = 0.15/0.21/0.27), an ALP with fa∼MPl can accommodate the published 3.6σ joint birefringence signal, but the posterior-supported spectator-safe region lies at m≫H0 and requires both misalignment tuning and enhanced photon coupling. The m∼H0 statement should be reserved for the broader scan-prior envelope, not the posterior median."

**Major 3 — The spectator criterion should be stated as an operational cut, not only as θi≪1**
Location: Abstract; Sec. VI; Table IV.
Issue: The paper alternates between three related but not identical spectator descriptions: θi≪1, θi∼0.1, and the actual chain-derived cut Ωa<0.01. Table IV is the clearest and most defensible statement.
Proposed fix: Add one sentence near the start of Sec. VI: "In the quantitative readout below, 'spectator-safe' means the derived chain-level condition Ωa<0.01; the θi∼0.1 language is an approximate misalignment-scale diagnostic, while the actual subset used for the quoted β=0.28°±0.10° result is the Ωa<0.01 cut in Table IV."

**Major 4 — The w0wa cross-check should remain clearly secondary**
Location: Sec. III caveat (e), Sec. V.C, Table II.
Issue: Phrases such as "phantom crossing required" can sound stronger than warranted for an overlap-uncorrected product likelihood (DES-SN5YR × Pantheon+ share ~20% of raw supernova events).
Proposed fix: Change "phantom-crossing required" to "phantom crossing favoured in this overlap-uncorrected product likelihood."

---

**4. MINORS — polish**

- Minor 1: Add a short "reader's map" at the end of the Introduction pointing to Table I (ΔNeff), Fig. 3 (NaMaster), Table IV/Fig. 4 (ALP), Table II (secondary w0wa diagnostic).
- Minor 2: In the abstract, shorten the NaMaster caveat without weakening it: "The MC SNR is a template-recovery SNR for injected signals, not a sky-detection significance."
- Minor 3: Use "pipeline-recovery bias floor" consistently instead of "systematic floor."
- Minor 4: Add one sentence: "We do not apply the inverse-variance estimator as a correction to any sky measurement; it is used only to diagnose the source of the synthetic-pipeline under-recovery."
- Minor 5: Pin the exact version tag/commit SHA and Zenodo/HuggingFace DOI in Data and Code Availability before submission.
- Minor 6: Remove PACS for MNRAS/JCAP submission.
- Minor 7: Move the internal audit history out of the arXiv source preamble to a repository changelog.

---

**5. Strengths**

- The scope discipline is strong. The paper repeatedly distinguishes a stock-CAMB ΔNeff proxy from an actual ECH/torsion Boltzmann calculation.
- The MCMC sample accounting is unusually transparent: the two frozen chains sum to 309,189 raw samples, with separate treatment of the accumulating Planck-only chain and clear convergence/ESS reporting.
- The ΔNeff result is clean and appropriately interpreted as null: both frozen combinations are consistent with zero, and the paper avoids claiming tension resolution.
- The NaMaster section carefully separates injected-signal recovery from sky-detection significance and explicitly discloses the β–α degeneracy limitation.
- The ALP section is candid about non-uniqueness, non-minimal photon coupling, and spectator misalignment tuning; Table IV is a valuable restricted-posterior summary.
- The paper's reproducibility culture is strong: it names code paths, YAML likelihood blocks, corrected diagnostic files, and known gaps.

---

**6. Specific scrutiny requested**

**6.1 MCMC: 309,189 samples across two converged combinations**
The two frozen dataset combinations are listed as 176,240 full-tension samples and 132,949 Planck+BAO+SN samples, summing exactly to 309,189. Table I reports worst R̂⁻¹ = 0.001 and 0.003, and minimum ESS values of 4,744 and 4,692, respectively. Assessment: Acceptable. No re-run required.

**6.2 ΔNeff ≈ 0 result: +0.058±0.179 for Planck+BAO+SN**
The Planck+BAO+SN result is 0.32σ from zero. The independent rerun gives +0.0514±0.171, in 0.04σ agreement with the frozen result. The null-consistency conclusion is robust at the precision claimed.

**6.3 NaMaster pseudo-Cℓ: 500 MC recovery at SNR = 20.32σ**
The manuscript correctly states that 20.32 is a matched-template recovery SNR for injected MC signals, not a sky-detection significance. The 500-MC recovery values are coherent: β̂=0.238° for βinj=0.27°, β̂=0.302° for βinj=0.342°, and a worst-case empirical under-recovery of 0.040°. Assessment: Acceptable as a pipeline validation.

**6.4 Spectator-ALP carved-out regime**
Table IV is the strongest formulation: Ωa<0.01, 13% posterior mass, β=0.28°±0.10°, m/H0=6.0/40.5/238, θi=0.15/0.21/0.27, Caγ=29.9/43.3/54.1. The strict θi≤0.1 sliver is only 0.33% by MC weight and has too few samples for a stable marginal. Assessment: Scientifically acceptable as a consistency carve-out, not a prediction.

---

**Final verdict**

Minor revisions. The manuscript's numerical core is publishable after correcting the likelihood-stack wording, tightening the ALP conclusion around the actual Ωa<0.01 restricted posterior, and preserving the secondary status of the w0wa cross-check.
