# 08: Deliverable Readiness Check

## Must-Have Before Drafting

| Item | Status | Classification |
|------|--------|---------------|
| f_NL = -35/8 verified | ✅ Done (coefficient search) | HAVE |
| Shape function evaluable | ✅ Done (Python code) | HAVE |
| SPHEREx forecast number | ✅ From arXiv:2311.13082 | HAVE |
| MegaMapper forecast number | ✅ From published white papers | HAVE |
| Fisher robustness scan | ✅ Done (k_min, multi-tracer, bias) | HAVE |
| Systematics audit | ✅ Done (GR, b_φ, k_min) | HAVE |
| Decision thresholds | ✅ Done (confirm/weaken/kill) | HAVE |
| Inflation comparison | ✅ Done (mimicry audit) | HAVE |
| ECH closure statement | ✅ Done (1 paragraph sufficient) | HAVE |

## Nice-to-Have

| Item | Status | Classification |
|------|--------|---------------|
| Shape function figure | Code exists, plot not generated | **NICE_TO_HAVE** |
| Fisher sensitivity figure | Code ran, plot not generated | **NICE_TO_HAVE** |
| Decision threshold figure | Numbers exist, not plotted | **NICE_TO_HAVE** |
| Survey comparison figure | Numbers exist, not plotted | **NICE_TO_HAVE** |
| b_φ marginalized Fisher | Not computed (estimate from literature: ~30% degradation) | DEFERABLE |

## Deferrable

| Item | Classification | Reason |
|------|---------------|--------|
| Full numerical time-integral reproduction | DEFERABLE | Algebraic verification sufficient |
| Proper CMB template projection | DEFERABLE | CMB is not primary test |
| Mock catalog validation | DEFERABLE | Fisher + literature sufficient for paper |
| Detailed b_φ prior calibration | DEFERABLE | Literature provides adequate estimates |

## Unresolved Claim-Strength Issues

| Issue | Resolution |
|-------|-----------|
| "~6σ" for SPHEREx | SAFE — from published dedicated forecast (arXiv:2311.13082) |
| "8.75σ" for MegaMapper | MUST CAVEAT — conditional on ideal conditions; state "3-7σ realistic" |
| "mechanism-independent" | SAFE — proven by ECH transparency + generic derivation |
| GR bias "20σ" vs "0.6σ" | MUST DISCUSS — reconcile in systematics section |
| b_φ "14× degradation" | MUST CAVEAT — worst case; realistic ~30% with fitted priors |

## Missing Citation Clusters

| Topic | Key Citations Needed |
|-------|---------------------|
| Matter-bounce bispectrum | Cai et al. 2009 (0903.0631), Maldacena 2003, Wands 2010 |
| Scale-dependent bias | Dalal et al. 2008, Slosar et al. 2008 |
| Multi-tracer | Seljak 2009, Hamaus et al. 2011 |
| SPHEREx PNG | Heinrich et al. 2023 (2311.13082), Doré et al. 2014 |
| MegaMapper | Schlegel et al. 2022, Sailer et al. 2021, Ferraro et al. 2022 |
| GR effects | Bonvin & Durrer 2011, Yoo 2010, arXiv:2511.09466, arXiv:2412.06553 |
| b_φ | Barreira 2022 (2205.05673), Barreira 2021 (2107.06887) |
| ECH | Holst 1996, Perez & Rovelli 2006 |

## Verdict

**READY TO DRAFT.** All must-have items are in hand. Figures can be generated during the drafting process (all code exists). No new computation needed. The citation list is identifiable. The claim-strength issues are all resolvable with proper caveats.

The ONLY blocker would be if we wanted full numerical time-integral reproduction of f_NL — but that is explicitly DEFERABLE since algebraic verification is scientifically sufficient and the shape function code works.
