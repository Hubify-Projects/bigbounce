# Referee Report — R52 (Claude/Opus leg)

**Recommendation: MINOR REVISIONS**

Paper: P1A v1A.0.78 — "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst
Dark-Energy Routes and Perturbation Transparency for Scalar Matter" (Golden).
PDF reviewed end-to-end (29 pp.); load-bearing numbers truth-audited against
`arxiv/paper1a_ech_nogo.tex`.

**Summary judgment.** The paper's actual thesis — a *channel-level* closure of
four enumerated minimal-ECH dark-energy routes under explicitly-labeled scaling
ansätze, plus an analytic perturbation-transparency theorem for canonical scalar
matter — rests on self-contained, correct content. The transparency result
(Sec. X) is right and cleanly argued, and the dark-energy mapping's status as an
*ansatz, not a derivation* is disclosed to an unusually high standard. No
load-bearing claim of *this* paper is broken, and no new analysis is required.
The remaining items are framing, one arithmetic coefficient, and the fact that
several prominently-displayed discrimination significances live in in-preparation
companion papers. Hence MINOR REVISIONS, not MAJOR.

---

## 1. BLOCKERS (must fix before publication)

None. The central theorem is correct and the no-go closures are honestly scoped
to their stated assumptions.

---

## 2. MAJORS (should fix)

**M1 — "13 logically-independent barriers" overstates independence (Abstract;
Sec. IX; Table II; Secs. I, XII, XIV, XV).**
The headline count of 13 logically-independent constraints (14 catalog entries)
is in tension with the body's own characterization of two of them. Barrier 9
(Liouville Conservation) is explicitly "a heuristic closure under explicit
assumptions … *not used as a stand-alone closure of any route*" (Sec. IX.I), and
Barrier 13 (Gravitational Democracy) is labeled a "structural/philosophical
observation … included for completeness" (Sec. IX, Table II). Two of the 13 are
therefore not load-bearing independent closures by the authors' own admission.
*Proposed fix:* either (a) relabel the headline as "14 catalog entries, of which
~11 are load-bearing independent closures (B9 heuristic, B13 philosophical, B8
subsumed by B14)," or (b) add a one-line independence ledger in Sec. IX stating
which barriers are stand-alone closures vs. catalog/heuristic entries. The
abstract should not lead with a count the body partially retracts.

**M2 — Headline discrimination significances are not reproducible from the
committed bundle (Abstract; Table I; Sec. XIII; Figs. 4, 6; Table III/IV).**
The "surviving testable predictions" carry quantitative significances —
SPHEREx σ(f_NL) ≈ 0.7–1.0 → "2.6–5σ", γ_PTA = 2.567 ± 0.382 with the
matter-bounce γ = 3.0 at "+1.13σ", and the ALP β analysis — that are sourced
entirely to companion papers marked *in preparation* ([2] Paper II, [6] Paper
I(b), [46] Paper III). The Data/Code Availability section confirms these
analyses are *not* in the committed reproducibility bundle. A referee cannot
verify the load-bearing observational discrimination numbers that the paper
displays in four figures/tables and the abstract. The paper does disclose this
and (correctly) excludes these numbers from the core closure proof, which is why
this is a MAJOR rather than a BLOCKER. *Proposed fix:* either post the companion
analyses (or their frozen chains/Fisher matrices) to the bundle/arXiv before or
at submission, or downgrade the in-text significances to clearly-flagged
forecasts pending companion release and remove the precise σ figures from the
abstract/Table I until the supporting analysis is citable.

---

## 3. MINORS (polish)

**m1 — ρ_NJL/ρ_Λ coefficient is off (Sec. IV.A, .tex line 1663).**
Text states ρ_NJL ≈ 4×10⁻⁸¹ eV⁴ "i.e. roughly 4×10⁻⁶⁹ ρ_Λ." With
ρ_Λ = (2.3 meV)⁴ = 2.8×10⁻¹¹ eV⁴, the ratio is 4×10⁻⁸¹ / 2.8×10⁻¹¹ ≈
1.4×10⁻⁷⁰ ρ_Λ — i.e. ~10⁻⁷⁰, not 4×10⁻⁶⁹ (coefficient off by ~28×, exponent
off by one). The "~69 orders below" phrasing elsewhere is fine at OOM, but the
displayed coefficient should read ~1.4×10⁻⁷⁰ ρ_Λ. Does not affect the
suppression conclusion. *(Truth-audit note: the upstream n_ψ ≈ 7.66×10⁻¹³ eV³
and 4×10⁻⁸¹ eV⁴ are correct in the .tex; only the final ρ_Λ-normalized
coefficient is slipped.)*

**m2 — Abstract length/density (p. 1).** The abstract is a single ~¾-page block
of tightly-packed qualifications. MNRAS readability would benefit from splitting
into (i) result, (ii) scope/assumptions, (iii) surviving tests. Content is fine;
the wall-of-text presentation buries the genuine result.

**m3 — Fig. 1 / Table III–IV PTA annotation.** The γ_PTA vs. Barbero–Immirzi γ
disambiguation is handled well, but "γ = 3.0 … +1.13σ above posterior mean …
consistent within standard frequentist tolerance" should state the tolerance
explicitly (1.13σ is "consistent" only loosely). Minor wording.

**m4 — Companion-citation placeholders.** [2], [6], [23], [46] are "in
preparation / posted concurrently." Ensure live arXiv IDs are inserted at
submission so the surviving-tests section is not left with dangling references.

**m5 — Reference [1] dependence.** The surviving f_NL = −35/8 prediction is
attributed to Cai et al. [1]; the paper leans on this exact value as its
strongest discriminator. Confirm at proof that −35/8 is the precise quantity in
[1] under the matching scalar-only w = 0 assumptions cited (could not be verified
from the PDF alone).

---

## 4. Strengths

- **The perturbation-transparency theorem (Sec. X) is correct and well-argued.**
  The Holst dual ½ε^μνρσR_μνρσ vanishing identically on the Levi-Civita
  connection by the first (algebraic) Bianchi identity at T = 0 is sound, and the
  extension to all scalar/tensor perturbation orders for canonical (spinless)
  matter is a clean, defensible generalization of Hehl et al. (1976).
- **Exceptional and rare transparency about ansatz vs. derivation.** The
  dimension-+1 → +4 on-shell scaling is labeled as a phenomenological ansatz
  consistently (abstract, Sec. IV scope, Sec. II A 2, Appendix B), with an
  explicit dimensional-counting appendix. The paper does not overclaim an
  operator-level theorem.
- **The Holst-dual vs. Pontryagin-density distinction (title-page footnote a,
  Sec. X.D, footnote 7) is a genuinely valuable clarification** that many
  treatments conflate; the e∧e∧R = −NY + T∧T decomposition is correctly used to
  pinpoint *why* the Holst sector decouples (Bianchi, not total-derivative).
- **Statistical honesty is a model of restraint.** The Sec. XIII discussion
  separating the naive 2.4σ from the heuristic 0.73σ LiteBIRD-vs-central
  discrimination, and the repeated insistence that β ≈ 0.27° is a "consistency
  point, not an ECH prediction," resist the usual significance inflation.

---

*Referee: Claude/Opus leg, internal review round R52, 2026-06-26.*
