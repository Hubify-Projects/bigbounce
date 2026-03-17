# 05: Observable-First Ranking

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Scoring Matrix

Each candidate scored 1–5 on six dimensions. Higher is better.

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Observable chance | 3× | Likelihood of producing a real, computable, measurable signal |
| Novelty chance | 3× | Likelihood of surviving a novelty audit |
| Existing strengths | 1× | How much of our current codebase/knowledge transfers |
| Low machinery | 2× | Inverse of new theoretical overhead required |
| Not-generic risk | 2× | Chance of NOT collapsing into prior literature |
| Positive paper | 2× | Chance of a publishable positive result (not just a no-go) |

---

## Scores

| Class | Observable (×3) | Novelty (×3) | Strengths (×1) | Low machinery (×2) | Not-generic (×2) | Positive paper (×2) | **TOTAL** |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A. Curvaton | 4 | 1 | 3 | 4 | 1 | 2 | **30** |
| **B. Chiral GW** | **4** | **5** | **4** | **3** | **5** | **4** | ****55**** |
| C. Dissipative | 3 | 3 | 2 | 2 | 4 | 3 | **38** |
| D. PBH | 4 | 2 | 2 | 3 | 1 | 3 | **33** |
| E. SIGW kernel | 3 | 3 | 3 | 4 | 3 | 3 | **41** |
| F. Phase transition | 3 | 4 | 1 | 1 | 4 | 3 | **38** |
| G. GW memory | 2 | 4 | 3 | 3 | 5 | 2 | **39** |
| H. Non-transparent | 3 | 3 | 3 | 3 | 3 | 3 | **39** |

---

## Scoring Justification

### B. Chiral GW (TOTAL: 55) — CLEAR WINNER

- **Observable (4):** Circular polarization of SGWB is a real observable. LISA, ET, and cross-correlation techniques can detect it. PTA circular polarization searches are active. Not a hypothetical.
- **Novelty (5):** Nobody has computed the chiral GW spectrum from a torsion bounce. Zhu & Cai (2023) show the enhancement but don't compute the circular polarization spectrum. This is a genuine gap.
- **Strengths (4):** We already have the ECH bounce background, the Holst/parity-odd gravitational structure, the Barbero-Immirzi parameter, and the ALP–photon coupling. The parity-violating sector is native to ECH.
- **Low machinery (3):** Requires deriving the tensor perturbation equation with a Chern-Simons or Nieh-Yan parity coupling and solving through the bounce. Non-trivial but bounded — one new coupling, one modified tensor equation.
- **Not-generic (5):** The specific prediction — circular polarization fraction V/I from a torsion bounce with Barbero-Immirzi–determined coupling — is not generic. It is specific to the ECH/Holst parity structure. It cannot be reproduced by inflation or by a generic bounce without parity violation.
- **Positive paper (4):** Even a null result ("torsion bounce chirality is unobservably small") is publishable as a constraint. A positive result ("torsion bounce produces V/I ~ X at frequency f, testable by LISA") is a major contribution.

### E. Modified SIGW kernel (TOTAL: 41) — SECOND

- Strong on low machinery (uses existing bounce background + second-order perturbation theory)
- Moderate novelty (nobody has done it, but it may be a small correction)
- Risk: if the modification is negligible for observable modes, the paper is "we checked and it's the same" — not flagship-worthy

### G/H. GW memory / Non-transparent bounce (tied at 39) — THIRD

- GW memory: high novelty but low observable chance (signal at Planck frequencies)
- Non-transparent: moderate novelty with recent competition (Zhu & Cai 2026)

### A. Curvaton (TOTAL: 30) — LAST

- Good observable chance but zero novelty. Would reproduce Cai & Brandenberger (2011).

---

## Clear Ranking

1. **B. Bounce + Sourced Parity/Chiral GW** — 55 points
2. **E. Bounce + Modified SIGW Kernel** — 41 points
3. **G/H. GW Memory / Non-Transparent** — 39 points (tie)
4. **C/F. Dissipative / Phase Transition** — 38 points (tie)
5. **D. PBH** — 33 points
6. **A. Curvaton** — 30 points
