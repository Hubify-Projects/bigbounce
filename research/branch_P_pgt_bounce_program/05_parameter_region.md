# PGT Bounce Parameter Region

**Date:** 2026-03-16

---

## 1. Ghost-Free Constraints

### Sector II (spin-0^-): the only viable sector

```
t_2 = -2 t_1,    t_3 < 0
```

The propagating mode is a massive pseudoscalar (odd parity, spin-0).

Sector I (spin-0^+) is rejected: it develops a ghost instability at
the target mass scale (m_T << M_Pl). Only Sector II is considered.

### Torsion mass

```
m_T = M_Pl / (2 sqrt(|t_3|))
```

where t_3 is the dimensionless PGT coupling. Since t_3 < 0:

```
|t_3| > 0   =>   m_T < infinity
|t_3| -> infinity   =>   m_T -> 0
|t_3| = 1/4   =>   m_T = M_Pl  (EC limit)
```

The PGT extension is parametrized by a single physical parameter m_T
(or equivalently |t_3|).

---

## 2. Bounce Scale

### Critical density

```
rho_crit = m_T^2 M_Pl^2
```

### Bounce temperature (radiation dominated)

```
T_bounce = (30 rho_crit / (pi^2 g_*))^{1/4}
         = (30 m_T^2 M_Pl^2 / (pi^2 g_*))^{1/4}
```

For g_* = 106.75:

```
T_bounce ~ 0.6 x (m_T M_Pl)^{1/2}
```

| m_T (GeV) | |t_3| | rho_crit (GeV^4) | T_bounce (GeV) |
|-----------|-------|------------------|----------------|
| M_Pl = 1.22 x 10^{18} | 1/4 | M_Pl^4 = 2.2 x 10^{72} | ~10^{18} |
| 10^{15} | 3.7 x 10^5 | 10^{66} | ~5 x 10^{16} |
| 10^{12} | 3.7 x 10^{11} | 10^{60} | ~5 x 10^{14} |
| 10^{9} | 3.7 x 10^{17} | 10^{54} | ~5 x 10^{12} |
| 10^{6} | 3.7 x 10^{23} | 10^{48} | ~5 x 10^{10} |
| 10^{3} | 3.7 x 10^{29} | 10^{42} | ~5 x 10^{8} |
| 1 | 3.7 x 10^{35} | 10^{36} | ~5 x 10^{6} |
| 10^{-3} | 3.7 x 10^{41} | 10^{30} | ~5 x 10^{4} |

### Bounce frequency (GW characteristic scale)

```
f_b = 2.6 x 10^{10} x (m_T/M_Pl)^{1/2} Hz
```

| m_T (GeV) | f_b (Hz) | Relevant detector band |
|-----------|---------|----------------------|
| 10^{18} (M_Pl) | 2.6 x 10^{10} | None (above all bands) |
| 10^{15} | ~7 x 10^{8} | None |
| 10^{12} | ~2 x 10^{7} | None |
| 10^{9} | ~7 x 10^{5} | None (above LIGO) |
| 10^{7} | ~2 x 10^{4} | ET upper edge |
| 10^{5} | ~2 x 10^{3} | LIGO/ET |
| 10^{3} | ~2 x 10^{2} | LIGO/ET |
| 1 | ~7 | ET |
| 10^{-3} | ~0.2 | DECIGO |
| 10^{-7} | ~2 x 10^{-3} | LISA |

---

## 3. Torsion Decay Properties

### Decay rate (gravitational coupling to SM fermions)

```
Gamma_T ~ m_T^5 / (8 pi M_Pl^4)
```

### Decay temperature

```
T_decay ~ (Gamma_T M_Pl^2 / (1.66 sqrt(g_*)))^{1/2}
        ~ m_T^{5/2} / (few x M_Pl^{3/2})
```

### Lifetime

```
tau_T = 1/Gamma_T ~ 8 pi M_Pl^4 / m_T^5
```

| m_T (GeV) | tau_T (s) | T_decay (GeV) | Decays before BBN? |
|-----------|---------|---------------|:------------------:|
| 10^{18} | 10^{-43} | ~10^{18} | YES |
| 10^{15} | 10^{-28} | ~10^{10} | YES |
| 10^{12} | 10^{-13} | ~10^{3} | YES |
| 10^{10} | 10^{-3} | ~3 | MARGINAL |
| 10^{9} | 10^{2} | ~0.03 | MARGINAL |
| 10^{8} | 10^{7} | ~10^{-4} | NO |
| 10^{6} | 10^{17} | ~10^{-8} | NO |
| 10^{3} | 10^{32} | ~10^{-14} | NO |

### BBN constraint (preliminary)

BBN requires that any massive relic with significant energy fraction
decays before T ~ few MeV (t ~ 1 s):

```
tau_T < 1 s   =>   m_T > ~3 x 10^{9} GeV
```

**This is the BBN lower bound on m_T, ASSUMING the torsion carries
O(1) energy fraction at the bounce (Scenario A from the calculation).**

If the torsion energy fraction is (m_T/M_Pl)^2 (Scenario B), the
constraint weakens drastically.

---

## 4. Signal Expectations by Mass Region

### Region I: m_T > 10^{15} GeV (near Planck)

- Bounce scale near Planck: indistinguishable from EC
- Torsion decays instantly
- No observable consequence beyond EC
- **Status: Viable but uninteresting (equivalent to EC)**

### Region II: 10^{10} < m_T < 10^{15} GeV

- Bounce below Planck but well above BBN
- Torsion decays before BBN
- GW spectrum at f_b ~ 10^5 -- 10^8 Hz (above all detectors)
- If torsion energy fraction ~ O(1): safe (decays before BBN)
- **Status: Viable. No positive signal, no exclusion.**

### Region III: 10^{9} < m_T < 10^{10} GeV (BBN boundary)

- Torsion decay temperature ~ MeV scale
- Marginal BBN compatibility
- If torsion energy fraction ~ O(1): CONSTRAINED by BBN
- Torsion decay products may contribute to N_eff
- GW spectrum at f_b ~ 10^5 Hz (above detectors, gap ~ 10^{19})
- **Status: THE MOST INTERESTING REGION if f_T ~ O(1)**

### Region IV: 10^{6} < m_T < 10^{9} GeV

- Torsion too long-lived: decays after BBN
- If f_T ~ O(1): EXCLUDED by BBN
- f_b ~ 10^3 -- 10^5 Hz (in detector bands but 10^{17}+ gap)
- **Status: Excluded if f_T ~ O(1). Allowed if f_T << 1.**

### Region V: m_T < 10^{6} GeV

- Torsion extremely long-lived
- If f_T ~ O(1): EXCLUDED (would dominate universe, spoil BBN + CMB)
- f_b < 10^3 Hz (in detector bands but 10^{21}+ gap)
- **Status: Excluded if f_T ~ O(1).**

---

## 5. Observational Constraints That Already Apply

### 5.1 BBN (conditional on torsion energy fraction)

If f_T ~ O(1): m_T > ~3 x 10^9 GeV (from tau_T < 1 s)
If f_T ~ (m_T/M_Pl)^2: no meaningful constraint

### 5.2 CMB N_eff

N_eff = 2.99 +/- 0.17 (Planck 2018)
Delta N_eff < 0.3 (95% CL)

Torsion decaying to relativistic particles after neutrino decoupling
but before recombination contributes:

```
Delta N_eff ~ (7/8) (4/11)^{4/3} x (g_T/g_nu) x f_T x (T_decay/T_nu_dec)^p
```

The precise formula depends on decay epoch. For m_T in Region III, this
gives Delta N_eff ~ O(f_T), which is constrained.

### 5.3 Gravitational wave bounds

Current LIGO O4 upper limit on stochastic background: Omega_GW h^2 < 10^{-9}
at f ~ 25 Hz.

For any m_T: the PGT bounce signal is at least 10^{17} below this.
**No constraint from GW observations.**

### 5.4 Primordial scalar spectrum

The bounce is transparent (T(k) = 1). No constraint on PGT from
scalar observations. The pre-bounce mechanism is unconstrained.

### 5.5 Tensor-to-scalar ratio

r ~ 10^{-55}: trivially compatible with r < 0.03 (BICEP/Keck).
No constraint.

---

## 6. Summary: Viable Parameter Space

### If f_T ~ O(1) (Scenario A):

```
VIABLE:     m_T > ~3 x 10^9 GeV   (Region II + III)
EXCLUDED:   m_T < ~3 x 10^9 GeV   (Regions IV + V, by BBN)
TRIVIAL:    m_T > ~10^{15} GeV     (Region I, indistinguishable from EC)
INTERESTING: 10^9 < m_T < 10^{10} GeV (Region III, BBN boundary)
```

### If f_T ~ (m_T/M_Pl)^2 (Scenario B):

```
VIABLE:     all m_T
EXCLUDED:   none (all constraints too weak)
INTERESTING: none (no observable consequence)
```

**The parameter space structure depends entirely on the torsion energy
fraction. This is why the calculation in 04_best_next_calculation.md
is the gating step for the entire program.**

---

## 7. Parameter Space Figure (ASCII)

```
log10(m_T/GeV)
  18 |  EC limit -------- Region I (trivial, = EC) ------->
     |
  15 |  ................ Region II (viable, no signal) ....
     |
  12 |  ....................................................
     |
  10 |  ===== Region III (BBN boundary, INTERESTING) =====
     |  <--- f_T=O(1) boundary
   9 |  xxxxx (EXCLUDED if f_T~O(1)) xxxxxxxxxxxxxxxxxxxxxx
     |
   7 |  xxxxx Region IV (excluded if f_T~O(1)) xxxxxxxxxx
     |
   5 |  xxxxx Region V (excluded if f_T~O(1)) xxxxxxxxxxx
     |
   0 |  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     |
     +-------------------------------------------------------->
                    Observable consequences

KEY:  .... = viable, no signal
      ==== = potentially constrained (interesting)
      xxxx = excluded if f_T ~ O(1)
```
