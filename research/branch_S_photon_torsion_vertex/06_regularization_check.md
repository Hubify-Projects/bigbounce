# Branch S: Regularization Check

**Date:** 2026-03-16

---

## 1. The Question

The ABJ anomaly is famously regularization-independent: it is a genuine
quantum anomaly, not an artifact of any particular regularization scheme.
Does the same robustness hold for the torsion-photon triangle?

---

## 2. Why This Matters

If the VVA triangle result were regularization-dependent, there would be
an ambiguity: different regulators could give different answers, and one
might argue that the "physical" regulator gives a larger (or zero) result.
We need to establish that the result is unambiguous.

---

## 3. The Standard ABJ Anomaly: Regularization Independence

The ABJ anomaly for the VVA triangle is determined by the
Adler-Bardeen theorem (1969):

**Theorem:** The axial anomaly receives contributions ONLY from the
one-loop triangle diagram. Higher-loop corrections do not modify the
anomaly coefficient. The one-loop coefficient is exact.

This was proven using:
- Dimensional regularization (where gamma_5 requires careful treatment
  via the 't Hooft-Veltman-Breitenlohner-Maison scheme)
- Pauli-Villars regularization (where the anomaly arises from the
  regulator mass)
- Point-splitting regularization
- Fujikawa's path integral method (where the anomaly arises from the
  non-invariance of the fermion measure)

All methods give the SAME coefficient:

```
partial_mu J^{5 mu} = (e^2 / 16 pi^2) * Q_f^2 * F_{mu nu} F-tilde^{mu nu}
```

(per fermion species with charge Q_f).

---

## 4. Application to the Torsion-Photon Triangle

### 4.1 The torsion vertex is an axial vector coupling

The torsion-fermion vertex S_mu * psi-bar gamma^mu gamma_5 psi has
EXACTLY the same Lorentz and gamma-matrix structure as any axial
vector current coupling. The anomaly calculation proceeds identically.

### 4.2 Dimensional regularization

In dim-reg, the torsion-photon triangle gives:

```
Gamma^{mu nu rho}_{VVA} = standard ABJ result * (g_axial / g_A^{standard})
```

The ratio of couplings is trivially regularization-independent (it is
the tree-level vertex ratio). The anomaly coefficient itself is the
standard ABJ coefficient, which is regularization-independent.

The well-known subtlety with gamma_5 in dimensional regularization
(the 't Hooft-Veltman prescription) affects the definition of the
axial current in d != 4. This introduces evanescent operators and
finite renormalizations. However, these affect only the DEFINITION
of the renormalized axial current, not the physical anomaly coefficient.

For our purposes: the effective operator L = S_mu K^mu_{CS} with the
ABJ coefficient is unambiguous in dimensional regularization.

### 4.3 Pauli-Villars regularization

In PV, a massive regulator fermion is introduced. The anomaly arises
from the regulator mass term, which violates axial symmetry. The
triangle with the regulator gives a finite, regulator-mass-independent
contribution that equals the anomaly.

For the torsion vertex: the PV regulator couples to torsion in the
same way as the physical fermion (since the regulator has the same
spin-connection coupling). The result is identical to the standard
ABJ calculation with the torsion coupling constant.

### 4.4 Fujikawa method

In the path integral, the anomaly arises from the non-invariance of
the fermion measure under axial transformations:

```
D psi-bar D psi -> D psi-bar D psi * exp(2i integral alpha(x) A(x))
```

where A(x) = (1/16 pi^2) F F-tilde is the anomaly density and alpha(x)
is the axial transformation parameter.

For the torsion coupling: the axial torsion S_mu acts as a BACKGROUND
GAUGE FIELD for the axial U(1) symmetry. The anomaly in this background
is:

```
partial_mu J^{5 mu} = (1/16 pi^2) [e^2 Q_f^2 F F-tilde + gravitational terms]
```

The electromagnetic anomaly term is INDEPENDENT of S_mu (it depends
only on the photon field). The gravitational anomaly term (proportional
to R R-tilde) is also independent of S_mu and vanishes on FRW.

**Key point:** The anomaly is in the DIVERGENCE of J^5, not in J^5
itself. The torsion coupling probes J^5 directly, not its divergence.
The effective operator S J^5 -> S K_{CS} comes from inverting the
anomaly relation, which is a valid manipulation only for the transverse
(non-anomalous) part.

Actually, this requires more care. Let me separate:

```
J^{5 mu} = J^{5 mu}_{transverse} + J^{5 mu}_{longitudinal}
```

The anomaly determines the longitudinal part:

```
partial_mu J^{5 mu}_{longitudinal} = anomaly
```

The VVA triangle determines the FULL amplitude Gamma^{mu nu rho},
including both transverse and longitudinal parts. The longitudinal
part gives the anomaly. The transverse part is regularization-dependent
in general (it can be shifted between the vector and axial Ward
identities by local counterterms).

However, the PHYSICAL requirement is that the vector Ward identities
are preserved (electromagnetic gauge invariance). This UNIQUELY fixes
the transverse part. The result is the standard ABJ amplitude.

### 4.5 Conclusion on regularization

```
+--------------------------------------------------+
|                                                    |
|  The torsion-photon triangle amplitude is          |
|  REGULARIZATION-INDEPENDENT.                       |
|                                                    |
|  It is the standard ABJ anomaly with a different   |
|  coupling at the axial vertex. The anomaly          |
|  coefficient is universal and exact (Adler-Bardeen  |
|  theorem). No scheme ambiguity.                     |
|                                                    |
+--------------------------------------------------+
```

---

## 5. Non-Renormalization

### Does the Adler-Bardeen non-renormalization theorem apply?

YES. The theorem states that the axial anomaly receives no corrections
beyond one loop. This applies regardless of:
- The source of the axial coupling (torsion, Z boson, ALP, etc.)
- The presence of other interactions (QCD, weak, gravitational)
- The regularization scheme

The proof relies on:
1. The anomaly is topological (related to the index theorem)
2. Higher-loop corrections would require additional divergences that
   are absent by power counting
3. The BPHZ forest formula shows that subdivergences do not modify
   the anomaly coefficient

For the torsion-photon vertex: the Adler-Bardeen theorem guarantees
that the one-loop result is EXACT. Higher-order corrections (from QCD,
electroweak, or gravitational interactions) do not modify the coefficient
(3 e^2 / 32 pi^2) sum Q_f^2.

---

## 6. Curved Spacetime Corrections

### Does curvature modify the anomaly?

In curved spacetime, the axial anomaly acquires an additional term:

```
partial_mu (sqrt{g} J^{5 mu}) = (e^2 / 16 pi^2) sqrt{g} F F-tilde
                                + (1/384 pi^2) sqrt{g} R R-tilde
```

The gravitational contribution R R-tilde (Pontryagin density) is:
- Independent of the photon field (does not affect F F-tilde coefficient)
- Zero on FRW backgrounds (as established in Branch H)
- A higher-order effect in kappa (graviton loops)

The electromagnetic anomaly coefficient (e^2 / 16 pi^2) Q_f^2 is
UNCHANGED by curvature. This is guaranteed by the Atiyah-Singer index
theorem, which determines the anomaly in terms of topological invariants
that are insensitive to the metric.

### Does torsion modify the anomaly?

In spacetime with torsion, the anomaly equation acquires corrections
from the Nieh-Yan topological invariant:

```
partial_mu J^{5 mu} = (e^2/16pi^2) F F-tilde + (1/384pi^2) R-tilde R
                       + c_NY * N_4
```

where N_4 = d(e^I T_I) is the Nieh-Yan four-form and c_NY is a
coefficient that depends on the regularization.

This Nieh-Yan contribution to the anomaly is CONTROVERSIAL in the
literature (Nieh-Yan 1982, Obukhov et al. 1997, Chandia-Zanelli 1997,
Peeters-Waldron 1999, Hughes et al. 2013). Different regularization
schemes give different values of c_NY. This is because the Nieh-Yan
term is UV-sensitive (it depends on the cutoff scale squared).

HOWEVER: this controversy affects the anomaly equation (divergence of J^5),
NOT the VVA triangle amplitude directly. The VVA triangle with two
photon legs and one torsion leg is determined by the electromagnetic
anomaly, not the gravitational/torsional anomaly. The Nieh-Yan ambiguity
enters only when computing the torsional contribution to the divergence
of J^5 — which is a different diagram (torsion-torsion-axial, or the
gravitational anomaly).

For our calculation: the Nieh-Yan ambiguity is IRRELEVANT. We compute
the VVA triangle (two photons, one torsion), which is determined by
the electromagnetic anomaly coefficient. This is unambiguous.

---

## 7. Summary

| Issue | Resolution |
|-------|-----------|
| Regularization dependence | NONE. Standard ABJ anomaly, universal coefficient. |
| Non-renormalization | Adler-Bardeen theorem applies. One-loop is exact. |
| Curved spacetime | Electromagnetic anomaly coefficient unchanged. R R-tilde = 0 on FRW. |
| Torsion corrections | Nieh-Yan ambiguity is irrelevant (affects divergence of J^5, not VVA triangle). |
| Scheme dependence | Physical requirement of electromagnetic gauge invariance uniquely fixes the amplitude. |

```
+--------------------------------------------------+
|                                                    |
|  The VVA triangle result is ROBUST:                |
|  - Universal anomaly coefficient                   |
|  - Exact at one loop (Adler-Bardeen)              |
|  - Unaffected by curvature, torsion, or scheme     |
|                                                    |
|  This robustness means the result CANNOT be         |
|  evaded by a clever choice of regularization.       |
|  The operator exists with the coefficient we        |
|  computed. The problem is not the coefficient —     |
|  it is the cosmological irrelevance (J^5 = 0,      |
|  Planck suppression).                               |
|                                                    |
+--------------------------------------------------+
```
