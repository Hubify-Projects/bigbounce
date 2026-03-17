# Model Reconsideration Memo

**Date:** 2026-03-13
**Author:** Houston Golden
**Purpose:** Conceptual bridge between Paper 1.01 and Paper 1.2
**Status:** Internal working document

---

## 1. Structural Lessons from Failed Routes

Four minimal routes were tested and closed. The branch-by-branch results are
documented in the companion technical note. Here we extract the deeper structural
lessons — what they collectively teach about the model class itself.

### Lesson 1: Algebraic torsion washes out after elimination

In minimal Einstein-Cartan-Holst (ECH) gravity, torsion is non-propagating.
Solving its algebraic equation of motion exactly eliminates all Holst-sector
structure from the reduced action. What remains is standard GR + standard
minimally-coupled fermions + a constrained four-fermion contact interaction.

This is not a failure of any particular calculation. It is a structural property
of the model class. Any mechanism that relies on torsion carrying information
into the infrared will fail in the minimal setup, because torsion does not
propagate — it is integrated out at arbitrarily high energies.

**Implication:** A viable geometric dark-energy mechanism must involve a degree
of freedom that *survives* reduction, not one that is eliminated by it.

### Lesson 2: Fixed gamma leaves no robust IR fingerprint

The Barbero-Immirzi parameter gamma enters the reduced action only through the
four-fermion coupling constants. At gamma = 0.274 (LQG value), the
scalar/pseudoscalar channel is repulsive (Track B). At any gamma, the one-loop
fermion determinant is gamma-independent (Branch G v1). The parameter affects
UV-scale contact interactions but leaves no distinctive infrared trace.

**Implication:** The Barbero-Immirzi parameter, as a fixed constant, is not the
engine for late-time physics. It sets UV-scale details of the torsion-fermion
interaction but does not generate low-energy structure.

### Lesson 3: Dynamical gamma reduces to generic ALP

Promoting gamma to a dynamical field theta(x) was the most natural structural
extension. But the Nieh-Yan 4-form is exact (a total derivative) in four
dimensions. Its topological nature ensures that after torsion elimination,
theta(x) behaves as a standard axion-like particle. The four-fermion interaction
becomes theta-independent. No mechanism generates V(theta) ~ Lambda. The
cosmological dynamics give w = +1 (stiff matter), the opposite of dark energy.

**Implication:** Repackaging the same algebraic degrees of freedom in a
different form does not generate new physics. The Nieh-Yan density's
topological nature is the structural reason. Any successor model must
introduce genuinely new degrees of freedom, not rephrase old ones.

### Lesson 4: Minimal matter couplings produce no distinctive signals

The parity-odd operator in ECH gravity is purely gravitational. It does not
couple to photons. Any photon coupling must be assumed (not derived), and the
resulting birefringence prediction is constant-beta — identical to generic ALP
phenomenology. The framework has no distinctive observable signature in the
minimal setup.

**Implication:** Observational distinctiveness requires either (a) new couplings
that arise from the model itself, not from external assumptions, or (b) a
mechanism that produces a non-generic spectral shape, cross-correlation, or
scale dependence.

### Lesson 5: No scale protection exists in the minimal model

None of the tested routes address the central naturalness question: why should
the dark-energy scale be O(10^{-122} M_Pl^4)? The condensate route produces
exponentially suppressed scales but the wrong sign. The one-loop route has
standard cosmological-constant renormalization with no new structure. The
dynamical Immirzi route requires V(theta_0) = Lambda_obs by hand.

**Implication:** Any serious successor model must confront scale naturalness
from the start, not treat it as a downstream detail. If the small scale is not
protected by a symmetry or dynamical mechanism, the model just relocates the
cosmological constant problem.

### Lesson 6: The discipline works; the model class doesn't (yet)

The canonical problem statements, gates, failure modes, and freeze logs
prevented waste. Each closure was clean, documented, and useful. The methodology
is a genuine asset. The model class — minimal ECH+Dirac — is what needs
upgrading, not the scientific process.

---

## 2. Assumptions to Retire

The following assumptions, which were central or implicit in Paper 1.01, should
not be carried forward as foundational in Paper 1.2:

### R1: "Minimal EC+Holst+Dirac is enough for late-time dark energy"

This was the implicit foundational assumption. Four independent routes show it
is false at the tested approximation orders. The minimal model does not generate
a late-time vacuum term, does not produce distinctive observables, and does not
address scale naturalness. Paper 1.2 must not center on this model class as if
it is sufficient.

### R2: "The Barbero-Immirzi parameter (fixed or dynamical) is the main engine"

gamma enters only through UV-scale four-fermion couplings (fixed case) or
reduces to a generic ALP (dynamical case). It is not the engine of late-time
physics. Paper 1.2 should not present gamma as the primary source of dark
energy, acceleration, or distinctive signatures.

### R3: "Parity language alone generates distinctive physics"

The parity-odd operator in ECH is real, but without a derived coupling to
observable sectors (photons, matter), it produces no testable prediction that
distinguishes the framework from generic alternatives. Parity is a structural
property of the theory, not by itself a mechanism or signal. Paper 1.2 should
not treat parity as a substitute for a mechanism.

### R4: "The inflationary dilution scaling story is a derivation"

The scaling rho_Lambda = Xi * M_Pl^4 with Xi ~ (alpha/M)^2 * D_inf is a
motivated parametric story, not a derivation. It does not explain why the
parity-odd operator's VEV persists at late times (the operator source vanishes),
and it does not address scale naturalness (why Xi ~ 10^{-122}). Paper 1.2 may
reference this scaling as phenomenological motivation but must not present it
as a first-principles result.

### R5: "Delta N_eff is a testable signal of this framework"

The framework's Delta N_eff contribution is phenomenological (a free parameter
in the MCMC), not derived from the spin-torsion sector. Observationally,
Delta N_eff is consistent with zero. This is not a distinctive signal.

---

## 3. Assumptions and Insights Worth Keeping

### K1: Geometry + parity structure may matter in a stronger model

The ECH action's parity-odd sector is real physics. The Holst term, the
Nieh-Yan density, and the torsion-fermion interaction are legitimate
ingredients. They just don't, by themselves, in the minimal setup, generate the
needed physics. In a richer model — one with propagating geometric degrees of
freedom, non-minimal couplings, or new symmetries — these ingredients could
play a role. Do not discard them; reposition them as building blocks.

### K2: The direct dark-energy derivation goal remains allowed

Nothing in the closures rules out a geometric origin of dark energy in
principle. The closures rule out specific minimal routes. The goal of deriving
rho_Lambda from geometry is still scientifically legitimate — it just requires
stronger ingredients than minimal ECH+Dirac.

### K3: The research discipline is a major asset

Canonical problem statements, gates, failure modes, freeze logs, and clean
closure documents are not common in theoretical physics. This methodology
produced four clean negative results in ~2 weeks. It should be preserved and
applied to any successor model.

### K4: Phenomenological consistency checks survive

The MCMC fits (H_0, sigma_8, S_8) are standard LCDM-extension analyses with
Delta N_eff as a free parameter. They don't depend on the spin-torsion
derivation. The fine-tuning reduction argument (10^{120} to 10^5) is a valid
parametric observation if properly framed. The observational comparison with
Planck, DESI, ACT data is competent work. These survive as phenomenology.

### K5: The failed routes themselves are publishable

A systematic closure of minimal first-principles routes is valuable in its own
right. It maps the landscape, prevents duplication, and establishes boundary
conditions for future work. The companion technical note is a real contribution.

---

## 4. Candidate Next-Generation Foundations

Three candidate foundation directions are identified below. Each is assessed
against the structural lessons from Section 1.

### Foundation A: Propagating Torsion / Metric-Affine IR Sector

**Core idea:** Replace algebraic torsion (which washes out) with a genuinely
propagating geometric degree of freedom in the connection sector. In
metric-affine gravity, torsion and/or non-metricity can be dynamical.

**Why it avoids old failure modes:**
- Lesson 1 (wash-out): If torsion propagates, it is not integrated out. It
  carries information into the IR.
- Lesson 3 (ALP collapse): A propagating spin-2 or spin-3 torsion mode is
  structurally different from a scalar ALP.

**Key requirements for viability:**
- Ghost-freedom: the Poincare gauge theory literature (Blagojevic, Hehl, Yo,
  Nester) has extensive no-ghost analyses. Many propagating-torsion theories
  have ghost instabilities. A viable candidate must pass these constraints.
- Mass generation: a propagating torsion mode needs a mass. What sets it?
  Is it protected?
- Late-time relevance: if the torsion mass is at or near the Planck scale,
  the mode decouples at late times. It must be light enough to matter
  cosmologically.

**Biggest risk:** Ghost instabilities in the massive torsion sector. The
Poincare gauge theory literature has many pathological theories and few
healthy ones. Finding a ghost-free, phenomenologically viable propagating
torsion sector is an unsolved problem.

**Assessment:** Structurally well-motivated but technically difficult.
Requires serious engagement with the Poincare gauge theory ghost literature
before any cosmological modeling.

### Foundation B: Symmetry-Protected Geometric Pseudoscalar Sector

**Core idea:** The dynamical Immirzi field failed because it collapsed to a
generic ALP. But what if a geometric pseudoscalar had a symmetry that
(a) protects its mass and (b) preserves a geometric fingerprint after
reduction? This would require either a new symmetry not present in minimal
ECH, or a non-minimal coupling that is symmetry-motivated.

**Why it avoids old failure modes:**
- Lesson 3 (ALP collapse): If the symmetry imposes specific coupling
  structures that are not generic ALP couplings, the reduction does not
  collapse to generic phenomenology.
- Lesson 5 (no scale protection): A shift symmetry, discrete symmetry, or
  gauge symmetry could protect the pseudoscalar mass.

**Key requirements for viability:**
- Identify the symmetry explicitly. "Protected" is meaningless without
  specifying what protects it.
- Show that the symmetry survives quantum corrections (i.e., is not anomalous
  in a way that defeats the purpose).
- Show that the remaining couplings after reduction are non-generic — they
  must produce at least one observable or mechanism that a standard ALP
  cannot reproduce.

**Biggest risk:** This may be the dynamical Immirzi route in disguise. If the
"symmetry-protected geometric pseudoscalar" turns out to be just an ALP with
extra words, it fails for the same reasons Route T1 failed. The burden is on
the model to demonstrate structural novelty, not just terminological novelty.

**Assessment:** Conceptually attractive but requires an explicit symmetry
proposal. Without one, this is aspirational, not a foundation.

### Foundation C: Vacuum Relaxation / Sequestering Geometric Mechanism

**Core idea:** Instead of generating a vacuum energy of the right magnitude
(which requires explaining 10^{-122}), cancel or sequester vacuum energy
dynamically. The geometric sector provides constraints (topological, gauge,
or gravitational) that enforce cancellation or relaxation to a small residual.

**Why it avoids old failure modes:**
- Lesson 5 (no scale protection): Sequestering addresses the scale problem
  directly. Instead of deriving Lambda from first principles, it explains
  why Lambda is small.
- Lesson 1 (wash-out): If the sequestering mechanism is built into the
  gravitational action's global structure (e.g., topological constraint,
  unimodular gravity, or non-local gravitational mechanism), it does not
  require a propagating degree of freedom that might wash out.

**Key requirements for viability:**
- Must not be equivalent to simply setting Lambda = 0 by hand.
- Must leave a cosmological imprint — either a small but nonzero Lambda,
  or a dynamical dark energy with specific equation of state.
- Must be radiatively stable: quantum corrections should not spoil the
  mechanism.

**Biggest risk:** The Weinberg no-go theorem (1989) constrains many
adjustment mechanisms. Any serious proposal must explicitly address how it
evades Weinberg's argument. Additionally, many sequestering mechanisms
(e.g., Kaloper-Padilla) have been criticized for fine-tuning in their
initial conditions.

**Assessment:** Addresses the deepest problem (why Lambda is small) but is
the hardest to construct. Requires engagement with the no-go literature.
If successful, it would be the most significant result.

---

## 5. Decision Rules for Any New Model

Before opening any new foundational direction, it must satisfy all four
criteria:

### DR1: Survives reduction without washing out

The model must contain at least one degree of freedom or structural feature
that is present in the full theory AND in the reduced/effective theory after
all algebraic constraints are solved. If torsion is algebraic and gets
eliminated, nothing that depends on it survives. The candidate mechanism must
not depend on variables that are integrated out.

**Test:** Write down the reduced action. Does the mechanism's key ingredient
still appear? If not, stop.

### DR2: Addresses tiny-scale naturalness explicitly

The model must contain an explicit statement of why the relevant scale is
small. Acceptable answers include: shift symmetry, discrete symmetry, gauge
symmetry, radiative stability argument, dynamical relaxation, sequestering.
Unacceptable answers include: "we just set it to the observed value" or
"the scale is a free parameter."

**Test:** If someone asks "why is this scale 10^{-122}?", does the model
have a structural answer, or does it just punt? If it punts, it has not
addressed the problem.

### DR3: Offers either unique mechanism or distinctive observable

The model must produce at least one of:
- A vacuum/dark-energy mechanism that is not reproducible by LCDM + generic ALP
- An observable prediction (spectral shape, cross-correlation, amplitude
  constraint) that distinguishes it from LCDM + generic ALP

If the model is observationally identical to LCDM + ALP, it has no
scientific value regardless of its theoretical motivation.

**Test:** Name the distinctive prediction. Can a generic ALP reproduce it?
If yes, stop.

### DR4: Fails cleanly if it doesn't work

The model must be testable within a defined scope. It must have a canonical
problem statement with gates and failure modes BEFORE computation begins.
If it fails, the failure must be documentable as a clean negative result.

**Test:** Can you write the gate structure and kill criteria before doing
any calculation? If not, the model is not well-defined enough to pursue.

---

## 6. Ranking and Recommendation

### Ranking

| Rank | Foundation | Promise | Risk | Readiness |
|------|-----------|---------|------|-----------|
| 1 | C: Vacuum relaxation/sequestering | Highest if viable | Weinberg no-go, fine-tuning displacement | Needs serious theoretical groundwork |
| 2 | A: Propagating torsion/metric-affine | Structurally motivated | Ghost instabilities | Large existing literature to engage |
| 3 | B: Symmetry-protected pseudoscalar | Conceptually natural | May collapse to ALP again | Needs explicit symmetry proposal |

### Recommendation

**Do not open any foundation direction until the negative-results paper is
finalized.** The strongest immediate scientific output is the four-route
closure paper. It is nearly complete and is a publishable, useful
contribution on its own.

**After the closure paper:** Foundation C (sequestering) addresses the deepest
problem but requires the most theoretical development. Foundation A
(propagating torsion) is the most concrete — the Poincare gauge theory
literature provides a clear starting point, and ghost-freedom analyses are
well-defined technical problems with known methods.

**Recommended first move:** A focused literature review (1-2 weeks) of
ghost-free propagating torsion models in Poincare gauge theory, with the
specific question: "Is there a ghost-free massive torsion mode that is light
enough to be cosmologically relevant?" This is a well-defined question with
a checkable answer.

**If that review is negative:** Shift to Foundation C and engage with the
Kaloper-Padilla sequestering literature and its geometric/torsion
generalizations.

**Foundation B should be pursued only if** a specific symmetry proposal
emerges naturally from A or C, not as a standalone direction.

---

## Summary

The minimal ECH+Dirac model is a useful phenomenological starting point but
not a viable foundation for deriving late-time dark energy. Paper 1.2 must
acknowledge this honestly, preserve the useful phenomenological work, and
redirect the theoretical program toward foundations that address the
structural failures identified by the four-route closure program.

The path forward is not to polish the old model but to upgrade the
foundations while maintaining the discipline that made the closures clean.
