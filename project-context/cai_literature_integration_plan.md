# Cai Literature Integration Plan

**Date:** 2026-03-24
**Trigger:** Literature audit of Yi-Fu Cai's 44 recent papers (2024-2026) revealed 4 actionable tracks
**Source:** `research/lit_audit/cai_recent_relevance_audit.md`

---

## Context

The literature audit found that our f_NL = -35/8 lane is clear — no one has published competing work. But it identified 4 papers that can actively **strengthen** our research program: one provides a discrimination table entry, one provides a PBH/second-observable framework, one proposes a new GW channel to test against our barriers, and one offers quintom bounce comparison models.

---

## Track 1: Cuscuton Bounce Contrast (Discrimination Table)

**Paper:** Dehghani, Geshnizjani & Quintin (2025), arXiv:2503.01992
"Cuscuton Bounce Beyond the Linear Regime: Bispectrum and Strong Coupling"

**What to extract:**
- Exact f_NL value for the Cuscuton bounce
- Bispectrum shape function
- Strong coupling analysis (does our matter bounce have the same protection?)
- How they avoid the no-go theorem (Quintin+ 2015)

**Integration targets:**
- Paper 2: Add Cuscuton bounce to discrimination/comparison table
- Paper 2: Cite in introduction as evidence that f_NL discriminates between bounce models
- `index.html`: Update claims table if discrimination argument strengthens
- `contributions.html`: Add to prior art context
- `research/lit_audit/`: Save detailed analysis

**Key question:** Does the Cuscuton bounce produce f_NL ~ 0, making it degenerate with inflation? If so, SPHEREx detection of f_NL = -4.375 would simultaneously confirm matter bounce AND rule out Cuscuton bounce.

---

## Track 2: PBH Channel Assessment (Second Observable)

**Paper:** Papanikolaou, Banerjee, Cai, Capozziello, Saridakis (2024), arXiv:2404.03779
"Primordial black holes and induced gravitational waves in non-singular matter bouncing cosmology"

**What to extract:**
- Their parametrization of the bounce-to-radiation transition
- Transfer function T(k) calculation methodology
- PBH mass function mapping
- Induced GW spectrum calculation
- What bounce energy scale and transition sharpness they assume

**Integration targets:**
- Paper 2: If viable, add as "second independent observable" in discussion
- `research/lqc_specific_openings_audit/`: Update Channel A assessment
- `activity.html`: Log as new research direction if channel opens
- Define the quick-kill computation: solve Mukhanov-Sasaki through Wilson-Ewing bounce for k ~ k_bounce, check T(k)

**Key question:** Is the LQC effective bounce (Wilson-Ewing parametrization) sharp enough to produce T(k) >> 1? If T(k) ~ 1, channel is dead. If T(k) >> 1, we get asteroid-mass PBHs + induced GWs detectable by LISA.

---

## Track 3: GW Echo Barrier Analysis

**Paper:** Cai & Zhu (2026), arXiv:2603.13924
"Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves"

**What to extract:**
- The Fabry-Perot transfer matrix formalism
- What bounce energy scale they assume
- Whether echoes provide amplitude enhancement or only shape modulation
- The double-peaked V_eff structure and whether it applies to our LQC/ECH bounce

**Integration against our barriers:**
- Run the GW echo mechanism through Barrier 12: vacuum amplification ceiling
  - H_bounce/M_Pl ~ 10^-3 to 10^-6 depending on model
  - GW amplitude suppressed by (H_bounce/M_Pl)^2
  - Does the Fabry-Perot resonance provide multiplicative enhancement that could overcome this?
- Check against Barrier 11 (decoupling universality)
- Determine if the echo spacing/amplitude encodes gamma = 0.274 (ECH-specific)

**Integration targets:**
- `research/lit_audit/`: Full barrier analysis of GW echoes
- Paper 1 or 2: Cite as complementary test if viable, or document as closed channel if not
- `activity.html`: Log the analysis result
- If viable: new research branch candidate

**Key question:** Does the Fabry-Perot resonance provide **amplitude** enhancement (viable) or only **spectral shape** modulation at an already-unmeasurable amplitude (dead)?

---

## Track 4: Quintom Bounce f_NL Comparison

**Paper:** Cai (2025), arXiv:2511.19994
"A focused review of quintom cosmology: from quintom dark energy to quintom bounce"

**What to extract:**
- The three quintom bounce examples (Quintom-A, -B, -C)
- Whether any computes f_NL (likely not — quintom papers rarely do bispectra)
- How the quintom bounce relates to DESI DR2 w-crossing evidence
- Whether quintom-B (phantom-to-quintessence) applies to our barrier landscape
- Whether the cyclic universe example has distinct observables

**Integration targets:**
- Paper 2: Add quintom bounce models to discrimination table (if f_NL values available)
- `index.html`: Note DESI DR2 quintom context if it affects our framing
- `research/lit_audit/`: Document comparison results
- Barrier analysis: Do our 14 barriers constrain quintom bounces? (They probably don't — different mechanism)

**Key question:** Does the quintom bounce predict a specific f_NL? If same as -35/8, that's a universality result strengthening our prediction. If different, it goes in the discrimination table. If uncomputed, flag as future work.

---

## Bibliography Additions Required

These papers need to be added to `arxiv/references.bib`:

1. **Cai:2014dxa** — Cai & Wilson-Ewing (2014), arXiv:1412.2914, "A ΛCDM bounce scenario"
2. **Li:2016xjb** — Li, Quintin, Wang & Cai (2017), arXiv:1612.02036, "Matter bounce with generalized single field"
3. **Quintin:2015rta** — Quintin, Sherkatghanad, Cai & Brandenberger (2015), arXiv:1508.04141, "No-go theorem"
4. **Cai:2026echoes** — Cai & Zhu (2026), arXiv:2603.13924, "GW echoes"
5. **Papanikolaou:2024pbh** — Papanikolaou+ (2024), arXiv:2404.03779, "PBH in matter bounce"
6. **Dehghani:2025cusc** — Dehghani+ (2025), arXiv:2503.01992, "Cuscuton bounce bispectrum"

---

## Success Criteria

- [x] Cuscuton f_NL extracted and added to Paper 2 discrimination table — **DONE: negligible f_NL, novel shape, validates our discrimination argument**
- [x] PBH channel viability assessed — **DONE: downgraded to <1% for LQC bounce (energy scale mismatch, symmetric bounce, EOS transition timing)**
- [x] GW echo mechanism tested against Barrier 12 — **DONE: CONDITIONAL, requires GUT-scale + ekpyrotic. Does NOT apply to our ECH/LQC/matter bounce models. Barrier 12 holds.**
- [x] Quintom bounce f_NL status determined — **DONE: ZERO computed f_NL in any quintom bounce model. No head-to-head comparison possible.**
- [x] All 6 bibliography entries added to references.bib — **DONE**
- [x] Website updated — **DONE: contributions.html author fix (3 instances), distinctiveness_audit fix, 06_fNL_estimate fix**
- [x] Activity page updated with literature audit event — **DONE**

---

## Results Summary (2026-03-24)

### Track 1: Cuscuton Bounce (Dehghani+ 2025)
- f_NL is **essentially zero** on observable scales (suppressed by ~50 orders of magnitude)
- Bispectrum has a novel shape (not local, equilateral, or folded)
- Strong coupling is controlled (c_s >= 1 through bounce)
- Evades no-go theorem because cuscuton is non-dynamical
- **Footnote 26 explicitly supports our perturbation-transparency claim**
- **Strategic value: HIGH** — ideal foil for Paper 2 discrimination table

### Track 2: PBH Channel (Papanikolaou+ 2024)
- Uses generic LOW-ENERGY parametrized bounce (H ~ 10^{-10} M_Pl), not LQC
- Three fatal incompatibilities with our Model B:
  1. Energy scale: Planck-scale bounce -> Planck-mass PBHs (evaporate in 10^{-43} s)
  2. Bounce symmetry: symmetric bounce -> T(k) ~ 1 (no enhancement)
  3. EOS transition: must occur DURING bounce, ours occurs AFTER
- **Channel A downgraded from 30-50% to <1%**
- Program remains single-point-of-failure: f_NL = -35/8 only

### Track 3: GW Echoes (Cai & Zhu 2026)
- Echoes provide ZERO amplitude enhancement — purely spectral shape modulation
- Detectable signal requires: GUT-scale contraction + ekpyrotic EOS + tachyonic amplification
- ECH bounce: NO (radiation contraction w=1/3 -> single-peak potential, no echoes)
- Matter bounce (Branch V): NO (w_c=0 fails ekpyrotic requirement)
- **Barrier 12 holds for all our models**

### Track 4: Quintom Bounce (Cai 2025 review)
- Three quintom bounce examples + cyclic universe, NONE compute f_NL
- None of our 14 barriers apply (all ECH-specific, quintom uses phantom fields)
- Quintom advantage: bounce-DE unification (DESI DR2 supports w-crossing at 4+ sigma)
- Our advantage: parameter-free early-universe prediction
- **Strategic: complement with competitive asymmetry, not direct competitor**
