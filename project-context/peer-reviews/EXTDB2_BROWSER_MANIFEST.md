# EXTDB2 Browser Sweep Manifest
Round: EXTDB2 (de-biased, rebuttal/prominence edits + P2 joint-Fisher)
Started: 2026-06-28
Completed: 2026-06-28
Tiers: ChatGPT Instant | Grok Expert | Gemini Flash (regular)
Budget: hard ~45 min cap (exceeded; sweep completed all 18 legs)

## MD5s (staged PDFs)
- P1A: 1d9ef1b1ad113e150e156b4aa772036f (/tmp/EXTDB2_P1A.pdf)
- P1B: dbf1d9d374f4923fd33c7e30cbd36ad5 (/tmp/EXTDB2_P1B.pdf)
- P2:  1da0518fa79894dfd68bbed7f93efc75 (/tmp/EXTDB2_P2.pdf)
- P3:  d3d662cb8d0c737032580465397911f2 (/tmp/EXTDB2_P3.pdf)
- P4:  342597924827541af63ee00bff1aa1af (/tmp/EXTDB2_P4.pdf)
- P4_grok: d7185fce3bf73a03db391ce1dc586e57 (/tmp/EXTDB2_P4_grok.pdf)
- P5:  9bdaf560d853e074a58071ae41e3e07a (/tmp/EXTDB2_P5.pdf)

## Submission Log (all 18 legs)

| # | Paper | Provider | Verdict | Chat URL | Notes |
|---|-------|----------|---------|----------|-------|
| 1 | P1A | ChatGPT | MINOR REVISIONS | https://chatgpt.com/c/6a40e2ce-3c30-83e8-aeb2-183f6b1f1988 | 0 blockers, 1 major (Route 2/3 ansatz labeling), 5 minors |
| 2 | P1A | Grok | LEG FAILED | — | "Grok was unable to finish replying" twice; transient Grok error |
| 3 | P1A | Gemini | MAJOR REVISIONS | https://gemini.google.com/u/0/app/a17541ad0b2b0a0a | 3 majors: Fig 3 H0 baseline shift artifact, cross-channel param contamination, un-converged MCMC chains |
| 4 | P2 | ChatGPT | MINOR REVISIONS | https://chatgpt.com/c/6a40e7c9-d96c-83e8-9699-61a3f730002c | 0 blockers, 4 majors (recast framing, cubic-order transfer, heuristic systematics, BF over-elaboration) |
| 5 | P2 | Grok | MINOR REVISIONS | https://grok.com/c/d7a34289-69e5-42ef-867f-b55a3e260340?rid=921b1959-9c8c-4ea7-8a55-136df6e4dbd3 | 0 blockers, 2 majors (third-order transmission prominence, heuristic quadrature) |
| 6 | P2 | Gemini | MAJOR REVISIONS | https://gemini.google.com/u/0/app/66d335cf3319eed5 | 2 BLOCKERS: asymmetrical tabular rebooking; uncontrolled MegaMapper systematics |
| 7 | P3 | ChatGPT | MAJOR REVISIONS | https://chatgpt.com/c/6a40ea1a-5318-83e8-91a6-c942129721cd | 3 BLOCKERS: headline catalog size overstated; eROSITA score non-reproducible; DESI catalog dominated by non-primary spectra |
| 8 | P3 | Grok | MAJOR REVISIONS | https://grok.com/c/3a2cbba3-7b6a-4d31-a352-490dacd06c32?rid=7966e7ac-af4a-4ad1-a8ac-d699dddfd47c | 2 BLOCKERS: irreproducible eROSITA scores; DESI headline framing mismatch |
| 9 | P3 | Gemini | MAJOR REVISIONS | https://gemini.google.com/u/0/app/0b65c78f2b735200 | 0 blockers, 5 majors (DESI framing, selection functions, SIMBAD novelty, noise bias in Fisher, irreproducible eROSITA) |
| 10 | P4 | ChatGPT | MINOR REVISIONS | https://chatgpt.com/c/6a40ecf1-fd44-83e8-afda-98afbe430794 | 0 blockers, 5 majors (abstract overloaded, "largest" qualifier, CE-ResNet dependence, peq>0.6 provenance, MASTER residual) |
| 11 | P4 | Grok | MAJOR REVISIONS | https://grok.com/c/57ca399e-20c0-4e79-b144-4aa880bfd637?rid=4a29cf0d-f0d2-4372-9d1c-84f386a4e2e1 | grok-specific PDF; 0 blockers, 4 majors (Appendix D dependence, dipole axis vs systematics map, template-fit exclusion detail, edge-on contamination) |
| 12 | P4 | Gemini | MAJOR REVISIONS | https://gemini.google.com/u/0/app/aa598a88983e1c28 | 0 blockers, 2 majors: circularity (66.5% CE-ResNet pseudo-labels); inconsistent σ reporting |
| 13 | P5 | ChatGPT | MINOR REVISIONS | https://chatgpt.com/c/6a40efbb-4790-83e8-be54-8a22f50f5893 | 0 blockers, 4 majors (headline scope, post-hoc primary, T-Web instability framing, RSD limitation) |
| 14 | P5 | Grok | MINOR REVISIONS | https://grok.com/c/db4b189d-050a-49b3-a0df-98ab9a91e40e?rid=3e86ccbe-9676-47d2-ad8c-e484ae47d501 | 0 blockers, 2 borderline-majors (post-hoc primary, anisotropic RSD) |
| 15 | P5 | Gemini | MAJOR REVISIONS | https://gemini.google.com/u/0/app/91b1ac3f34526e2c | 0 blockers, 4 majors incl. EFT operator breaks rotational invariance (must formalize or remove) |
| 16 | P1B | ChatGPT | MINOR REVISIONS | https://chatgpt.com/c/6a40f191-d698-83e8-9590-5b1ba5db56b1 | 0 blockers, 0 majors, 6 minors (w0wa prominence, release-pairing, NaMaster floor, ALP tuning, repro recipe, title) |
| 17 | P1B | Grok | MINOR REVISIONS | https://grok.com/c/2a3cddfc-4561-48a0-8667-8655b3fdb99c?rid=29fc075a-ec23-4393-8f0c-3b862eb07427 | 0 blockers, 0 majors, 3 minors (w0wa SN-overlap framing, P1a linkage, presentational tightenings) |
| 18 | P1B | Gemini | MAJOR REVISIONS | https://gemini.google.com/u/0/app/51ccd47a75973156 | 1 BLOCKER: w0wa product likelihood double-counts SNe; 2 majors (ALP fine-tuning, Savage-Dickey breakdown) |

## Verdict Summary

| Paper | ChatGPT | Grok | Gemini |
|-------|---------|------|--------|
| P1A | MINOR | FAILED | MAJOR |
| P1B | MINOR | MINOR | MAJOR |
| P2 | MINOR | MINOR | MAJOR |
| P3 | MAJOR | MAJOR | MAJOR |
| P4 | MINOR | MAJOR | MAJOR |
| P5 | MINOR | MINOR | MAJOR |

**Counts (17 valid legs):**
- ACCEPT: 0
- MINOR REVISIONS: 8
- MAJOR REVISIONS: 9
- FAILED: 1 (P1A-Grok, transient error)

## Notable cross-leg findings

**P1B blocker (Gemini):** w0wa product likelihood double-counting ~20% overlapping DES-SN5YR + Pantheon+ SNe — must either supply joint covariance or remove σ-tail headline values. ChatGPT and Grok flagged the same issue as a MINOR/presentation fix; Gemini elevated to BLOCKER.

**P2 blocker (Gemini):** Asymmetrical tabular rebooking (tables show r→1 entries but text uses r=0.84 rebooking).

**P3 blockers (ChatGPT × 3, Grok × 2):** Headline catalog size overstated; eROSITA scores irreproducible; DESI catalog dominated by non-primary-science spectra (only 2,468 science-target clusters vs 195,829 headline).

**P4 circularity (Gemini):** 66.5% CE-ResNet pseudo-labels means label-shuffle null cannot detect inherited survey-correlated structures. First identified this round.

**P5 EFT operator (Gemini):** Appendix A parity-violating operator L_parity ∝ gϕ(∇ϕ)(∇ρ/ρ_bg)(L̂·ẑ) explicitly breaks rotational invariance because of fixed coordinate ẑ. Must be formalized into a rotationally invariant form or removed.

**P1A H0 baseline (Gemini):** Fig 3 2.5% CMB deviation is almost entirely artifact of different H0 values (69.2 vs 67.36 km/s/Mpc), not a genuine bounce signal.
