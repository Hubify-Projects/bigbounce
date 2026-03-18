# 01: Distinctiveness Audit

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Models Under Review

From the first-pass analysis (project_viable_bounce_model/), three candidate models emerged:

| Model | Label | First-Pass Status |
|-------|-------|------------------|
| LQC Matter Bounce + Partial Curvaton (alpha ~ 0.3) | Model A | "Viable" — but curvaton tilt sign error discovered |
| Wilson-Ewing Quasi-Dust (w = -0.003) + LQC | Model B | Not fully analyzed in first pass |
| Ekpyrotic Slow Contraction (ILS 2014 mechanism) | Model C | Identified as next direction |

---

## Model A: LQC Matter Bounce + Partial Curvaton

### What the bounce does:
- Replaces the singularity with a regular bounce (background)
- LQC dressed-metric corrections suppress r to ~10^-4 (perturbation level)
- Matter contraction generates scale-invariant adiabatic spectrum with f_NL = -35/8

### What the curvaton does:
- Provides spectral tilt (n_s departure from 1)
- Partially dilutes the matter-bounce f_NL

### Critical finding from first-pass correction:
**The curvaton tilt is BLUE in matter contraction** (n_sigma = 1 + 2m^2/(3H^2) > 1). The curvaton makes n_s WORSE, not better. This kills Model A as described.

### Distinctiveness test:

**Even setting aside the tilt sign error:**

| Observable | Set by bounce? | Set by curvaton? |
|-----------|---------------|-----------------|
| n_s = 0.965 | NO — bounce gives n_s = 1 | YES (supposed to, but wrong sign) |
| r ~ 10^-4 | YES — LQC dressed-metric | NO |
| f_NL ~ -3.7 | PARTIALLY — base value -35/8 from matter contraction | PARTIALLY — curvaton dilutes to -3.7 |
| alpha_s | NO — comes from curvaton mass running | YES |

The bounce sets r (via LQC) and provides the base f_NL (via matter contraction dynamics). The curvaton was supposed to set n_s and alpha_s.

**But r ~ 10^-4 is not testable** (below LiteBIRD sensitivity). So the only bounce-controlled testable observable would be f_NL, which is partially diluted by the curvaton.

### Verdict: **MODEL DEAD** (curvaton tilt sign kills it)

Even if it weren't dead: BOUNCE_AS_BACKGROUND_ONLY for n_s; bounce contributes to f_NL but through an intermediate value (-3.7) that depends on the curvaton fraction alpha. The f_NL prediction is no longer parameter-free — it depends on alpha.

---

## Model B: Wilson-Ewing Quasi-Dust (w = -0.003) + LQC

### Key correction from agent research:

The Wilson-Ewing (2013) model uses P = -epsilon * rho, giving w = -epsilon = -0.003 (NEGATIVE). This was misunderstood in the first pass as w = +0.003.

The correct formulas:
- n_s = 1 - 12*epsilon = 1 - 0.036 = 0.964 (RED tilt, matches Planck)
- r ~ 9 x 10^-4 (from LQC, numerical estimate)
- f_NL: the standard matter bounce value (convention-dependent: -35/8 in Bardeen or 5/12 in zeta)

### What the bounce does:
- Provides the bounce itself (LQC)
- Sets n_s via the slightly negative EOS (n_s = 1 - 12*epsilon)
- Sets r via LQC corrections
- Sets f_NL via matter contraction dynamics

### What extra ingredients are needed:
- A matter field with w = -0.003 < 0 during contraction
- This means slightly more potential than kinetic energy — like dust with a tiny cosmological-constant-like component

### Physical plausibility of w = -0.003:

The agent research found a critical caveat: "It is physically implausible that a canonical scalar field can allow w < 0, leading to obvious instabilities." A canonical scalar with w < 0 requires potential domination — the field behaves like dark energy, not dust.

**Wilson-Ewing's resolution:** In the LCDM bounce (arXiv:1412.2914), a cosmological constant Lambda provides exactly this. The effective EOS becomes slightly negative when Lambda contributes. This is physical and motivated.

### Distinctiveness test:

| Observable | Set by bounce? | Set by extra ingredients? |
|-----------|---------------|--------------------------|
| n_s = 0.964 | YES — from w = -epsilon during contraction | The value of epsilon comes from Lambda/matter ratio |
| r ~ 10^-4 | YES — LQC dressed-metric | NO |
| f_NL = -35/8 or 5/12 | YES — matter contraction dynamics | NO |
| alpha_s > 0 | YES — Lehners & Wilson-Ewing (2015) | NO |

**THIS IS MUCH CLEANER.** All observables are set by the bounce sector. The only "extra ingredient" is Lambda, which already exists in standard cosmology.

### But wait — the f_NL convention problem:

The first-pass analysis found confusion between:
- f_NL = -35/8 = -4.375 (Bardeen convention, Cai et al. 2009)
- f_NL = 5/12 = 0.42 (zeta convention, other references)

**This distinction is CRITICAL.** If f_NL = -4.375, the model has a sharp negative prediction distinguishable from inflation. If f_NL = +0.42, the model is practically indistinguishable from single-field inflation (which predicts f_NL ~ 0).

**The agent research confirmed:** f_NL = -35/8 is from arXiv:0903.0631 (Cai, Xue, Brandenberger, Wilson). This must be verified to determine whether this is the Planck-observable f_NL or a different convention.

### Verdict (conditional on f_NL convention):

**If f_NL = -4.375 (Planck convention):** DISTINCTIVE_BOUNCE_MODEL
- All observables set by bounce physics
- f_NL is a fixed, parameter-free prediction
- Only Lambda is added (already in standard cosmology)
- Minimal parameter count

**If f_NL = +0.42 (or ~0):** BOUNCE_AS_BACKGROUND_ONLY
- n_s and r are set by bounce, but n_s = 0.964 is also predicted by Starobinsky
- r ~ 10^-4 is untestable
- f_NL is too small to be a discriminator
- The model survives but has nothing to say that inflation can't also say

---

## Model C: Ekpyrotic Slow Contraction (ILS 2014)

### What the model does:
- Slow contraction with w >> 1 (ekpyrotic)
- Two scalar fields with non-minimal kinetic coupling
- Entropy perturbation converts to adiabatic before/during bounce
- n_s set by kinetic coupling function Omega(phi)
- f_NL ~ +5 (from conversion dynamics only)
- r ~ 0 (tensor modes not amplified during ekpyrosis)
- BKL resolved automatically (w >> 1)

### Distinctiveness test:

| Observable | Set by bounce? | Set by entropy/conversion? |
|-----------|---------------|---------------------------|
| n_s = 0.965 | NO — set by Omega(phi) engineering | YES |
| r ~ 0 | NO — set by ekpyrotic suppression during contraction | YES (ekpyrosis, not bounce) |
| f_NL ~ +5 | NO — set by entropy-to-adiabatic conversion | YES |
| alpha_s | NO — set by Omega(phi) corrections | YES |

**NOTHING is set by the bounce.** The bounce is purely a non-singular connector between contraction and expansion. All observables are determined by the contracting phase dynamics (ekpyrosis) and the conversion mechanism.

If I remove the word "bounce" and replace it with "a non-singular transition mediated by [Horndeski/DHOST/Cuscuton gravity]," nothing changes about the predictions.

### Additional problem: f_NL = +5 is POSITIVE

This is the same sign as many inflationary multifield models. It is NOT distinctive compared to inflation. The sign of f_NL was supposed to be the bounce's trump card (negative for matter bounce, positive for inflation). The ILS mechanism gives POSITIVE f_NL, erasing this advantage.

### Verdict: **GENERIC_MULTIFIELD_MODEL_DISGUISED_AS_BOUNCE**

The bounce does zero predictive work. It is a background regulator only. The observables are entirely controlled by the two-field ekpyrotic sector and the conversion dynamics. The f_NL is positive (same sign as inflationary curvaton). The n_s is tuned via a function (comparable to choosing V(phi) in inflation). This is a multifield contraction model that happens to include a bounce.

---

## Summary

| Model | Verdict | Notes |
|-------|---------|-------|
| A: LQC + Curvaton | **MODEL DEAD** | Curvaton tilt is blue; cannot fix n_s |
| B: Wilson-Ewing Quasi-Dust | **DISTINCTIVE_BOUNCE_MODEL** (if f_NL = -4.375) or **BOUNCE_AS_BACKGROUND_ONLY** (if f_NL ~ 0) | Convention check is THE critical question |
| C: ILS Ekpyrotic | **GENERIC_MULTIFIELD_MODEL_DISGUISED_AS_BOUNCE** | Bounce does no predictive work |

**The entire second-pass analysis hinges on resolving the f_NL convention for the matter bounce.**
