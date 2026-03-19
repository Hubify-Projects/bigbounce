# Low-k / Transfer / IR Opening Assessment

**Created:** 2026-03-19
**Status:** COMPLETE
**Classification:** CLOSED (NOT_WORTH_IT)

---

## The Question

Could LQC formalism differences show up at low-k (infrared) scales and affect observable predictions?

---

## Analysis

### The IR Terminology Mismatch

The 2024 comparison paper (arXiv:2405.12296) shows that dressed-metric and hybrid differ in "IR" regimes. This sounds relevant to low-ell CMB observations. But their definition of "IR" and ours refer to completely different scales:

- **Their IR:** modes near the bounce scale k_LQC, specifically the regime k slightly below k_LQC where the quantum corrections transition from significant to negligible.
- **Our IR:** CMB low-ell modes at k ~ 10^{-4} Mpc^{-1}, or LSS modes at k ~ 10^{-2} Mpc^{-1}.

These are separated by an unbridgeable hierarchy.

### The Scale Hierarchy

```
k_CMB       ~ 10^{-4} Mpc^{-1}    (observable low-ell, ell ~ 2-30)
k_LSS       ~ 10^{-2} Mpc^{-1}    (large-scale structure)
k_pivot     ~ 0.05 Mpc^{-1}       (Planck pivot scale)
             ...
             (60 orders of magnitude)
             ...
k_LQC       ~ 10^{56} Mpc^{-1}    (bounce scale)
```

The ratio k_CMB/k_LQC ~ 10^{-60}. Any formalism-dependent correction scales as (k/k_LQC)^n for some positive n (the leading correction must vanish as k/k_LQC --> 0 by the correspondence principle). Even for the slowest possible falloff (n = 1):

```
Correction ~ (k_CMB / k_LQC) ~ 10^{-60}
```

For the more physical expectation (n = 2, from the Bogoliubov analysis):

```
Correction ~ (k_CMB / k_LQC)^2 ~ 10^{-120}
```

These are not numbers that can be overcome by clever analysis techniques, multi-tracer methods, or future detector improvements. They are structural zeros.

### What About Anomaly-Scale Modes (ell < 10)?

The CMB anomalies (low quadrupole, hemispherical asymmetry, cold spot) are at ell ~ 2-10, corresponding to k ~ 10^{-4} Mpc^{-1}. These are sometimes invoked as possible LQC signatures (Agullo et al. 2013, 2015).

Same argument applies: these modes are still 60 orders below k_LQC. The LQC corrections cannot reach these scales through formalism differences.

The only way LQC could affect these scales is through the initial-state prescription (what vacuum to choose at the bounce). But:
1. Our modes are set during contraction, not at the bounce.
2. Initial-state effects at the bounce affect only modes with k ~ k_LQC.
3. For k << k_LQC, the initial state is irrelevant -- the modes are already classical.

### The Only Exception: Scale-Independent Modifications

If LQC produced a modification that is SCALE-INDEPENDENT (affects all k equally), it could reach observable scales. But:

1. A scale-independent modification would not distinguish between formalisms -- it would affect dressed-metric and hybrid equally (since both have the same background evolution).
2. A scale-independent shift to P(k) is absorbed into the normalization A_s, which is a fitted parameter.
3. A scale-independent shift to f_NL is an O(1) renormalization that depends on bounce details (rho_c, gamma) but not on formalism choice.

Scale-independent modifications exist but are formalism-universal. They do not help discriminate between dressed-metric and hybrid.

---

## Classification: NOT_WORTH_IT

The low-k/transfer/IR opening is closed by the same scale hierarchy that makes the bounce transparent to CMB modes. There is no realistic path from LQC-specific IR structure to observable signals.

The terminology mismatch between "IR in the LQC literature" and "IR in observational cosmology" creates a false sense of overlap. When the LQC community says their formalisms differ in the IR, they mean at k ~ k_LQC. When we look at the CMB IR (k ~ 10^{-4} Mpc^{-1}), we are 60 orders below where the differences live.

---

## Implication

This closes the last potential escape route for formalism sensitivity at observable scales. The argument is complete:

1. **f_NL:** Generated during contraction (formalism-insensitive) + transmitted trivially through the bounce (O(10^{-112}) correction).
2. **n_s:** Generated during contraction (formalism-insensitive).
3. **r:** Formalism-sensitive but undetectable (r ~ 10^{-4}).
4. **Low-k structure:** 60 orders below the formalism-difference region.
5. **Initial state:** Irrelevant for modes set during contraction.

No observable window remains.
