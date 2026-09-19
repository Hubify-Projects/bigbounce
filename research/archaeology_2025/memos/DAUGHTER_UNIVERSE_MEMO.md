# Black-Hole Daughter-Universe Technical Memo

**Worker:** W4 (2025 legacy-archaeology campaign) · **Date:** 2026-09-18 · **Status:** literature memo, not a claim
**Campaign plan:** `research/archaeology_2025/PLAN.md` · **Provenance input:** `research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md`

> **Evidence layer:** Open Questions / Research Genealogy. Nothing in this memo is a BigBounce
> result, a prediction, or a claim. Houston's preference for a regenerative universe is motivation
> for asking the questions below; it is **never** evidence, a prior, or a model-selection criterion.
>
> **Citation policy:** every reference below was resolved by W4 this session by fetching its arXiv
> abstract page or DOI landing page, and then cross-checked against W2's independently produced
> `research/archaeology_2025/bibliography/VERIFIED_BIBLIOGRAPHY.md` +
> `archaeology_2025.bib` (28 resolved entries). Where W2 and W4 agree, the entry is marked
> **[W4+W2]**. Items still unresolved by either worker are tagged `[UNVERIFIED]` and are **not**
> relied on for any statement. W2's two standing corrections are carried here: the dump's NASA
> citation `[11]` is a **MISMATCH** and must not be used for the morphology claim (§6), and the
> Popławski PLB pairing is corrected in §2.6 / §9.

---

## 1. Scope, and what BigBounce has already tested

### 1.1 What this memo is

A causal/topological taxonomy of the constructions that the 2025 Notion-era notes collapsed into
the single phrase "born in a black hole", a mechanism table, a literature map including the known
objections, and three narrow side-questions (Smolin CNS as context, galaxy morphology, the §18
synthesis questions). It is a **literature and terminology memo**. It contains no new derivation and
proposes no new observable.

### 1.2 What BigBounce already tested — and why this memo does not reopen it

Two distinct, already-closed results bound this memo:

**(a) The Popławski rotating-BH-universe spin-axis dipole is EXCLUDED (2026-09-02).**
`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` (Track C1 / P4′,
`NEXT_SCIENCE_LEDGER` item #5) confronted the one qualitative observable the rotating-parent model
offers — a preferred axis inherited from the parent black hole's spin, producing clockwise /
counter-clockwise galaxy-spin asymmetry — against P4's coverage-calibrated observed-label
sensitivity. The script's own finding, reproduced verbatim from its output JSON, is that
**Popławski's papers contain no derived dipole amplitude, alignment fraction, or timescale**:
arXiv:1910.10819 states only that "galaxies tend to align their axes of rotation with the preferred
axis, resulting in clockwise-counterclockwise asymmetry". Under the explicit toy closure
`observed dipole amplitude = alignment efficiency η` (adopted because the literature supplies no
closure), the DESI Legacy DR8 catalog excludes `η > 0.98%` at ≥95% coverage on the primary
high-confidence real-space channel, while every amplitude in the model's own observational
motivation (Longo 2011 ~7%; Shamir 2012/2020/2022 ~2–20%; Shamir 2025 JWST/JADES ~20–33%, N=263)
sits 2–30× above that floor. Five numbered assumptions are attached to that statement in the
script and travel with it — notably that `A_95^obs` is an **observed-label** sensitivity floor, not
a physical parity-amplitude bound, and that the preferred axis itself is a free direction that was
*not* searched for by direction-matching.

**(b) The galaxy spin-dipole itself is NULL (P4, P5).**
- P4 (`pipelines/p2_chirality/chirality_catalog_paper.tex`, abstract): 887,472 quality-controlled
  DESI Legacy DR8 rows enter the supported-pixel fit and fixed-occupancy label-randomization null;
  the primary high-confidence observed-label dipole is **consistent with zero**
  (`z_mom = +0.635`, one-sided rank `p = 0.23768`), with `A_95^obs ≃ 0.98%`.
  `research/bh_universe_dipole/outputs/a95_null_cl_2026_09_02.json` adds the complementary genuine
  CL statement: the 95th percentile of the committed 10,000-draw null is 0.669%, and the observed
  `A_dip = 0.467%` lies below it.
- P5 (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, abstract): the void / non-void
  environment contrast in DESI DR1 is a **non-detection**
  (`Δf_CW = +0.00145442`, 95% CI `[−0.00504290, +0.00795174]`, two-sided `p = 0.66085`;
  wild-cluster `p = 0.67345`), explicitly "a catalog-specific non-detection for classifier labels,
  not a physical-handedness, real-space, or cosmological constraint."

**Consequence for this memo.** Per campaign hard-constraint #2, *existing nulls stay nulls*. This
memo does **not** revisit the spin-axis route, does not propose a re-analysis of P4/P5, does not
soften either null, and does not treat the absence of a derived Popławski amplitude as an opening.
The only live question left on this lane, per the director's corrections, is the **mass / energy /
entropy bookkeeping** across the bounce — which is W5's memo, not this one. What W4 supplies is the
causal taxonomy W5 needs in order to know *which* spacetime he is doing bookkeeping on.

### 1.3 Provenance: the retired paper_1_01

`research/paper_1_01_archive/main.tex` (archived 2026-03-13; see its `ARCHIVAL_NOTE.md`) is the
**retired** early BigBounce paper and is cited here as provenance only, never as a source. It framed
dark energy as "emerging from quantum gravitational effects in a rotating universe born from a black
hole interior" (§I), asserted that "a rotating parent black hole spawns a non-singular baby universe
beyond its event horizon through torsion-regulated gravitational collapse" and that "the baby
universe inherits angular momentum, establishing a preferred cosmic axis" (§I, §II), and defined a
parent-BH threshold `M_BH > M_crit = (M_Pl^4/ρ_vac)^{1/3} ≈ 10⁻³ M_☉` (§, near line 228). Its own
claims table lists "Parent rotating black hole origin" as **Assumed**, not derived. Three
independent reasons it is provenance and not science here: the four-route ECH derivation program
closed negative (`ARCHIVAL_NOTE.md`); its `N_tot ≈ 92` is a fitted parameter by its own admission;
and its central observable — the inherited preferred axis — is the route excluded in §1.2(a).
Per the director's corrections, the symbol `M_crit` now has at least three mutually unrelated
historical meanings across this repo and **must not be reused**.

---

## 2. Causal / topological taxonomy — five constructions the 2025 notes conflated

Each entry gives the geometry, an ASCII Penrose sketch, the asymptotic regions, and the decisive
question: **is the "child" causally connected to the parent's exterior?**

Sketch legend: `ℐ⁺`/`ℐ⁻` null infinity · `i⁰` spatial infinity · `~~~` singularity ·
`═══` horizon · `≈≈≈` non-singular bounce / transition surface · `‖` region boundary.

---

### (i) Eternal Einstein–Rosen bridge (maximally extended Schwarzschild)

The vacuum Kruskal extension contains two exterior asymptotically flat regions joined by a throat.

```
            ~~~~~~~~~~~~~~~~   (future singularity r=0)
           /                \
          /   black-hole     \
     ℐ⁺  /        region       \  ℐ⁺
        ‖ ═══              ═══ ‖
   i⁰   ‖  EXTERIOR I   EXTERIOR II  ‖  i⁰      <-- two distinct asymptotic regions
        ‖ ═══              ═══ ‖
     ℐ⁻  \   white-hole      /  ℐ⁻
          \    region       /
           \               /
            ~~~~~~~~~~~~~~~~   (past singularity r=0)
```

- **Asymptotic regions:** two, both asymptotically flat, both eternal.
- **Causally connected?** **No — and there is no child.** Exterior II is not a "daughter universe";
  it is a second asymptotic region of the *same* vacuum solution, present for all time, not created
  by anything. Fuller & Wheeler, *Phys. Rev.* **128**, 919 (1962), DOI 10.1103/PhysRev.128.919,
  showed the Schwarzschild throat "pinches off in finite time", trapping any signal, so the bridge
  is **non-traversable** and causality is preserved. Nothing is born; nothing crosses.
- **Additional disqualifier:** the eternal Kruskal extension is not the spacetime of a star that
  collapses. A realistic collapse spacetime has *one* exterior and no white-hole region at all.

---

### (ii) Black-to-white-hole transition in the same asymptotic region

Quantum-gravitational tunneling converts the trapped region into an anti-trapped region; the matter
re-emerges into the **same** exterior universe, after a very long exterior time.

```
                 ℐ⁺
                /
       ═══════ /          anti-trapped (white-hole) region
        \  ≈≈≈≈≈≈≈≈  <-- quantum region replaces the singularity
         \ ═══════            trapped (black-hole) region
   i⁰ ---‖   SINGLE EXTERIOR   ‖--- i⁰      <-- one asymptotic region, same one
         /  (collapsing star)  \
       ℐ⁻                       ℐ⁻
```

- **Verified sources.** Haggard & Rovelli, arXiv:1407.0989, *Phys. Rev. D* **92**, 104020 (2015),
  DOI 10.1103/PhysRevD.92.104020: "there is a classical metric satisfying the Einstein equations
  outside a finite spacetime region where matter collapses into a black hole and then emerges from
  a white hole … A black hole can thus quantum-tunnel into a white hole." Rovelli & Vidotto,
  *Planck stars*, arXiv:1401.6562, DOI 10.1142/S0218271814420267: "quantum-gravitational pressure
  counteracts weight … yielding a bounce", short in star proper time but "extremely long seen from
  the outside, because of the huge gravitational time dilation", with the onset governed by energy
  density not size. Bianchi, Christodoulou, D'Ambrosio, Haggard & Rovelli, *White holes as
  remnants*, arXiv:1802.04264, *Class. Quantum Grav.* **35**, 225003 (2018),
  DOI 10.1088/1361-6382/aae550: the white hole "acts as a long-lived remnant", is a "white hole with
  small mass but large finite interior", and the full cycle "form[s] a unitary process that does not
  violate any known physics."
- **Asymptotic regions:** **one** (plus, in the remnant scenario, a large finite interior volume
  that is *not* a new asymptotic region).
- **Causally connected?** **Yes.** This is the defining feature: the emergent matter/radiation
  returns to the parent's own exterior. There is **no daughter universe here at all.** Anyone who
  cites Haggard–Rovelli or Planck stars in support of "our universe was born inside a black hole"
  has cited the wrong construction.

---

### (iii) Closed FLRW region behind the horizon ("universe inside a black hole")

Collapse is halted by new interior physics and the interior continues as a closed cosmology on the
far side of a spacelike bounce surface, with no return to the parent exterior.

```
                 ‖  CHILD: closed FLRW, no ℐ, no i⁰  ‖
                 ‖  (compact spatial slices, expands) ‖
      ═══════════ ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ ═══════════   <-- bounce surface replaces r=0
                    trapped region
   i⁰ ------------‖  PARENT EXTERIOR  ‖------------ i⁰
                   (collapsing matter)
                 ℐ⁻                      ℐ⁻
```

- **Verified sources.**
  - Frolov, Markov & Mukhanov, *Black holes as possible sources of closed and semiclosed worlds*,
    *Phys. Rev. D* **41**, 383 (1990), DOI 10.1103/PhysRevD.41.383: under a **limiting-curvature**
    assumption, "the Schwarzschild metric inside the black hole can be attached to the de Sitter one
    at some spacelike junction surface" (Israel thin-shell), and a closed universe can develop
    inside the black hole. This is the **de Sitter-core** route.
  - Popławski, *Universe in a black hole in Einstein–Cartan gravity*, arXiv:1410.3881,
    *Astrophys. J.* **832**, 96 (2016), DOI 10.3847/0004-637X/832/2/96: spin–torsion coupling
    "generates gravitational repulsion at extremely high densities in fermionic matter, approximated
    as a spin fluid, and thus avoids the formation of singularities"; the matter "should therefore
    bounce at a finite density and then expand into a new region of space on the other side of the
    event horizon, which may be regarded as a nonsingular, closed universe", with quantum particle
    production able to "create enormous amounts of matter, produce entropy, and generate a finite
    period of exponential expansion (inflation)". This is the **Einstein–Cartan / torsion** route.
    Anisotropic version: Popławski, arXiv:2007.11556, *Gen. Relativ. Gravit.* **53**, 18 (2021),
    DOI 10.1007/s10714-021-02790-7.
  - Earliest statements of the "our universe is the interior of a black hole" idea: Pathria,
    *The Universe as a Black Hole*, *Nature* **240**, 298 (1972), DOI 10.1038/240298a0 —
    bibliographic record resolved this session via DOI-keyed metadata; the Nature landing page is
    authentication-walled and **the abstract was not retrieved**, so the record is cited for
    priority only and its content is `[UNVERIFIED]`.
    Good, *Chinese universes*, *Physics Today* **25**(7), 15 (1972) —
    `[UNVERIFIED]` (AIP landing page returned 403 this session).
- **Asymptotic regions:** parent has one (or more); the **child has none** — a closed FLRW has
  compact spatial slices and therefore no `ℐ`, no `i⁰`, and no ADM or Bondi mass. This is the single
  most important structural fact for W5's bookkeeping.
- **Causally connected?** **One-way, then not at all.** The parent's infalling matter reaches the
  child (so the child's initial data is causally determined by the parent), but no signal from the
  child ever reaches the parent's exterior. In Popławski's construction the child is "on the other
  side of the event horizon"; to the parent's exterior observer the object remains, in every
  respect, a black hole.

---

### (iv) False-vacuum bubble that pinches off into a causally disconnected baby universe

A region of false vacuum bounded by a domain wall inflates. Seen from outside it is a black hole;
seen from inside it is a closed universe that disconnects from the original spacetime.

```
       ‖ CHILD: inflating closed universe ‖
       ‖   (disconnects; own ℐ⁺)          ‖
        \_______  wormhole throat  _______/      <-- throat pinches off
       ═══════════════════════════════════      <-- horizon (parent sees a black hole)
   i⁰ -----------‖ PARENT EXTERIOR ‖----------- i⁰
                   (true vacuum)
```

- **Verified sources.**
  - Blau, Guendelman & Guth, *Dynamics of false-vacuum bubbles*, *Phys. Rev. D* **35**, 1747 (1987),
    DOI 10.1103/PhysRevD.35.1747: "An observer in the exterior true-vacuum region will describe the
    system as a black hole, while an observer in the interior will describe a closed universe which
    completely disconnects from the original spacetime."
  - Farhi & Guth, *An obstacle to creating a universe in the laboratory*, *Phys. Lett. B* **183**(2),
    149 (1987), DOI 10.1016/0370-2693(87)90429-1 **[W4+W2]**. Pre-arXiv; the Elsevier landing page
    returned 403 to W4, so W4's confirmation is of the DOI-keyed bibliographic record only, but W2
    independently resolved both the record and its content via ScienceDirect indexing:
    *"any false-vacuum bubble growing beyond a critical size in asymptotically flat space traces
    back to an initial singularity."* That is the obstacle. No verbatim abstract is quoted here
    because neither worker retrieved one.
  - Farhi, Guth & Guven, *Is it possible to create a universe in the laboratory by quantum
    tunneling?*, *Nucl. Phys. B* **339**, 417 (1990), DOI 10.1016/0550-3213(90)90357-J **[W4+W2]**:
    a bubble *can* be produced without an initial singularity, but classically it collapses; the
    paper investigates quantum tunneling as the mechanism that would let it expand into a universe,
    using canonical and functional-integral semiclassical methods in the thin-wall limit — with the
    functional integral yielding a non-manifold solution that required introducing a
    "pseudomanifold" prescription to estimate the tunneling probability.
- **Asymptotic regions:** parent one; child acquires its own, after the throat pinches off.
- **Causally connected?** **Briefly one-way, then fully disconnected.** This is the only
  construction in the list where the child ends up with its own asymptotic structure.

---

### (v) Regular / non-singular black-hole interiors with **no** new universe

Singularity resolution without any daughter cosmology: the interior is simply regular.

```
                 ℐ⁺
       ═══════════════════       outer horizon
        \    regular core     /
         \   (no r=0 sing.)  /   <-- de Sitter-like core; inner horizon
       ═══════════════════       (Hayward: forms, is quiescent, evaporates)
   i⁰ ---------‖ SINGLE EXTERIOR ‖--------- i⁰
                 ℐ⁻
```

- **Verified sources.**
  - Hayward, *Formation and evaporation of non-singular black holes*, gr-qc/0506126,
    *Phys. Rev. Lett.* **96**, 031103 (2006), DOI 10.1103/PhysRevLett.96.031103: "Regular
    (non-singular) space-times are given which describe the formation of a (locally defined) black
    hole from an initial vacuum region, its quiescence as a static region, and its subsequent
    evaporation to a vacuum region. The static region is Bardeen-like … behaving as a cosmological
    constant at small radius." The black hole is "a compact space-time region of trapped surfaces"
    with inner and outer boundaries joining as a single smooth trapping horizon. **No child.**
  - Bardeen (1968), the original regular-black-hole metric — `[UNVERIFIED]`: a conference
    proceeding (GR5, Tbilisi) with no DOI, no landing page resolvable by W4, and not in W2's
    resolved set. Hayward's own description of his static region as "Bardeen-like" is
    the verified attribution used here.
  - Ashtekar, Olmedo & Singh, *Quantum transfiguration of Kruskal black holes*, arXiv:1806.00648,
    *Phys. Rev. Lett.* **121**, 241301 (2018), DOI 10.1103/PhysRevLett.121.241301, and the companion
    *Quantum extension of the Kruskal space-time*, arXiv:1806.02406, *Phys. Rev. D* **98**, 126003
    (2018), DOI 10.1103/PhysRevD.98.126003: LQG quantum-geometry corrections cover both the
    "interior" region containing classical singularities and the exterior asymptotic region;
    "singularities are naturally resolved by the quantum geometry effects of loop quantum gravity",
    and the quantum extension features "an infinite number of trapped, anti-trapped and asymptotic
    regions" with curvature scalars bounded above uniformly.
    *Precision note:* the widely used phrase "transition surface" does **not** appear in either
    verified abstract; the anti-trapped regions in the quantum-extended Kruskal spacetime are
    white-hole-type in the sense of (ii)/(i), **not** closed daughter cosmologies. Any stronger
    statement about a named transition surface is `[UNVERIFIED]`.
- **Asymptotic regions:** one (Hayward); infinitely many in the AOS quantum extension, which is an
  eternal-Kruskal-type structure, not a reproduction mechanism.
- **Causally connected?** **N/A — there is no child.** This class exists in the taxonomy precisely
  because "the singularity is avoided" does **not** imply "a universe is born." Most singularity
  resolution in the literature is of this type.

---

### 2.6 Terminology ruling (binding for this project)

When BigBounce, or any BigBounce-adjacent copy, says **"born in a black hole"**, it can only mean
**(iii)** — a closed FLRW region behind the horizon — or, in a different and much stronger-assumption
model, **(iv)** — a false-vacuum bubble that pinches off. It can **never** mean (i), (ii), or (v):

- **(i) is not a birth.** The second exterior of maximally extended Schwarzschild is eternal,
  vacuum, present in the solution from the start, and unreachable (Fuller & Wheeler 1962). Nothing
  is created and nothing is transmitted.
- **(ii) is not a child.** The black-to-white-hole transition returns matter to the **same**
  asymptotic region. Citing Haggard–Rovelli or Planck stars for a daughter universe is a category
  error.
- **(v) contains no child by construction.**


#### 2.6.1 The one published paper that *does* use the bridge language — and exactly what it costs

Honesty requires flagging the source of the 2025 conflation, because it is not purely an
error of the notes. Popławski, *Radial motion into an Einstein-Rosen bridge*, arXiv:0902.1994,
*Phys. Lett. B* **687**, 110–113 (2010), DOI 10.1016/j.physletb.2010.03.029 **[W4+W2]**, argues
that "observed astrophysical black holes may be Einstein-Rosen bridges, each with a new universe
inside that formed simultaneously with the black hole. Accordingly, our own Universe may be the
interior of a black hole existing inside another universe."

**Citation correction (W2, carried here):** this paper is *Phys. Lett. B* **687**, 110 (2010) —
**not** *Phys. Lett. B* **694** (2010) 181, which is the *different* Popławski paper
*Cosmology with torsion* (arXiv:1007.0587). The two were conflated in the campaign's own task
framing; both papers are real and both are verified, but the pairing must be used correctly.

What that paper needs, from its own verified abstract, in order to say "bridge" and "new universe
inside" at the same time: the black hole is read in **isotropic coordinates**; the interior is
declared "regular and physically equivalent to the asymptotically flat exterior of a white hole";
geodesic completeness is obtained because "the expansion scalar in the Raychaudhuri equation has a
discontinuity at the horizon"; and the bridge is "represented by the Kruskal diagram with
**Rindler's elliptic identification of the two antipodal future event horizons**." That elliptic
identification is a non-standard topological identification imposed on the Kruskal manifold — it is
an assumption, not a consequence of Einstein's equations, and it is what manufactures the
"new universe" on the far side. Three consequences for BigBounce:

1. This is a **different construction** from the one BigBounce's lineage actually rests on.
   Popławski's later and far more developed line — arXiv:1410.3881 (ApJ 832, 96), arXiv:2007.11556
   (GRG 53, 18) — is construction **(iii)**: a torsion bounce producing a **closed** daughter FLRW
   with no asymptotic region and no bridge. The 2009 paper is a vacuum-geometry/identification
   argument; the 2016 paper is a matter-collapse argument. They should never be cited as one idea.
2. Even in the 2009 paper the child is **not** causally connected to the parent's exterior; the
   "bridge" is not traversable in the ordinary sense, and the paper's own framing is that distant
   observers cannot distinguish the two solutions.
3. Therefore the ruling below stands unchanged, with one amendment: *if* a BigBounce document ever
   uses "Einstein–Rosen bridge", it must cite arXiv:0902.1994 specifically, state the elliptic
   identification as an assumption, and say explicitly that it is **not** the construction behind
   the torsion-bounce line.

**"Einstein–Rosen bridge" must not be used as shorthand for (iii) or (iv).** The term denotes a
specific vacuum geometry — the Kruskal throat connecting two asymptotically flat exteriors of one
eternal Schwarzschild solution. Construction (iii) has **no** second asymptotic region at all (the
child is closed: no `ℐ`, no `i⁰`, no ADM mass), so there is literally nothing for a bridge to
connect to. Construction (iv) does eventually produce a second asymptotic region, but only *after*
the throat pinches off, and the pinch-off is the event that makes the child a separate universe —
the opposite of a persisting bridge. Using "Einstein–Rosen bridge" for either one imports
(a) two eternal exteriors, (b) a vacuum solution, and (c) a traversability question that Fuller &
Wheeler settled negatively in 1962 — none of which apply. The 2025 notes' merging of these is a
**class-G terminology conflation** in the ledger's own scheme, and it is the single most consequential
error in the recovered material: it is what made "our universe is on the white-hole side of an
Einstein–Rosen bridge" sound like a statement about a spacetime, when no spacetime in the cited
literature has that structure. Preferred neutral language: **"daughter cosmology"**, **"closed
interior universe"**, or **"bounce spacetime"**, with the construction number attached.

---

## 3. Mechanism table

| | (i) Eternal ER bridge | (ii) Black→white, same region | (iii) Closed FLRW behind horizon | (iv) False-vacuum baby universe | (v) Regular interior, no child |
|---|---|---|---|---|---|
| **What avoids the singularity** | **Nothing** — both singularities are present in the maximal extension | Quantum-gravity effects accumulating over long times; quantum-gravitational pressure at high *energy density*, not small size (1401.6562) | **Torsion** from fermionic spin (ECSK; 1410.3881) **or** a limiting-curvature de Sitter core (PRD 41, 383) | **Nothing about singularities** — the mechanism is false-vacuum repulsion + a domain wall; Farhi–Guth 1987 finds an initial singularity is required unless one tunnels | Quantum-geometry corrections (LQG; 1806.00648 / 1806.02406) or an assumed regular matter core behaving as a cosmological constant at small radius (gr-qc/0506126) |
| **Can an ordinary astrophysical BH (stellar / SMBH, formed by collapse) produce it, in the published model?** | **No** — realistic collapse has one exterior and no white-hole region | **Yes**, in principle: the published scenario is the end state of ordinary collapse + evaporation | **Yes** in the published models: 1410.3881 applies to collapsing fermionic matter generally; PRD 41, 383 attaches de Sitter to Schwarzschild inside a black hole | **No** — requires a pre-existing false-vacuum region; ordinary collapse of Standard-Model matter does not supply one | **Yes** (that is the point) — and it yields **no** child |
| **Required assumptions** | Only that one takes the eternal vacuum solution seriously as physics | Quantum gravity affects the metric in a small region **outside** the horizon (1407.0989 argues this is not forbidden by causality); a tunneling amplitude; a bounce timescale | ECSK torsion is real and unsuppressed at high density; fermions averaged as a **spin fluid** (Weyssenhoff-type, Frenkel condition); a **particle-production ansatz** whose rate is a free input (1410.3881: "depending on the particle production rate…"); for the anisotropic case, particle production must **dominate over shear** (2007.11556) | A false-vacuum region exists; a thin domain wall; a semiclassical tunneling prescription — FGG 1990 needed a "pseudomanifold" action prescription because the functional integral gave a non-manifold solution | Either LQG effective dynamics (canonical LQC bounce review: Ashtekar & Singh, *Class. Quantum Grav.* **28**, 213001 (2011), arXiv:1108.0893, DOI 10.1088/0264-9381/28/21/213001 **[W2]**), or a phenomenological regular metric with matter of "finite density and pressures" (energy-condition-violating in the core) |
| **Does any observable survive to the parent's exterior?** | No (throat pinches off; Fuller–Wheeler) | **Yes by construction** — the matter/radiation re-emerges into the same exterior; 1401.6562 even proposes "a detectable signal, of quantum gravitational origin, around the 10⁻¹⁴ cm wavelength" | **No signal.** The only claimed exterior-facing handle is the *reverse* direction — the child inheriting the parent's spin axis (1910.10819) — and that route is EXCLUDED for BigBounce (§1.2) | **No.** Once the throat pinches off, the child is causally disconnected; the parent sees only a black hole | N/A — the observables are black-hole observables (evaporation, horizon structure), not cosmological ones |

**Reading of the table.** Only construction (ii) offers an exterior observable, and (ii) has no
child. Only (iii) and (iv) have children, and neither transmits anything to the parent's exterior.
That asymmetry — *reproduction is unobservable from the parent side, by construction* — is the
central structural fact of this entire lane and is the reason §7/Q16 below answers as it does.

---

## 4. Literature map with rebuttals and limitations

Each objection below was verified this session at the cited abstract or landing page.

### 4.1 Singularity theorems constrain, but do not forbid, these constructions
Penrose, *Gravitational collapse and space-time singularities*, *Phys. Rev. Lett.* **14**, 57 (1965),
DOI 10.1103/PhysRevLett.14.57 (record verified; the APS landing page does not display an abstract,
so the theorem's exact hypotheses are cited from the paper's standing role, not quoted). The theorem
assumes a trapped surface, global hyperbolicity conditions, and an energy condition. Every
construction in §2 evades it by violating one hypothesis — (iii) and (v) by violating an energy
condition at high density (torsion repulsion, de Sitter core), (iv) by false-vacuum repulsion, (ii)
by quantum-gravitational modification of the metric. **This is not a loophole in the pejorative
sense; it is exactly what "new high-density physics" means.** But it does mean that *none of these
constructions follows from general relativity plus ordinary matter* — each one is a statement about
physics we have not measured.

### 4.2 The spin-fluid averaging step in the Einstein–Cartan route is contested
The ECSK daughter-universe result depends on approximating fermions as a macroscopic spin fluid,
usually Weyssenhoff-type with the Frenkel condition. Independent kinematic treatments exist:
Pasmatsiou, Tsagas & Barrow, *Kinematics of Einstein-Cartan universes*, arXiv:1611.07878,
*Phys. Rev. D* **95**, 104007 (2017), develop the evolution equations "without initial restrictions
on material content or torsion-spin couplings" and recover Weyssenhoff results only as a special
case; de Berredo-Peixoto & de Freitas, arXiv:0907.1701, *Int. J. Mod. Phys. A* **24**, 1652 (2009),
emphasise that in Einstein–Cartan "torsion is not dynamical and is completely expressed by means of
the spin sources", so every conclusion is only as good as the assumed spin source. Popławski himself
concedes the limitation, writing in arXiv:2007.11556 that "this scenario is only approximate: the
Kantowski-Sachs metric is never reached and should be replaced with a more general metric that
tends to that of a 3-sphere." **Limitation, not refutation** — but it means the spin-fluid step is
a modelling choice, not a derivation.

### 4.3 The same ECSK collapse has been published with a *different* endpoint — dispersal, not a daughter
Hashemi, Jalalzadeh & Ziaie, *Collapse and dispersal of a homogeneous spin fluid in Einstein–Cartan
theory*, arXiv:1407.4103, *Eur. Phys. J. C* **75**, 53 (2015),
DOI 10.1140/epjc/s10052-015-3276-1, run the Oppenheimer–Snyder collapse with a homogeneous
Weyssenhoff fluid and find that "the collapse process halts at a finite radius" and "the spacetime
singularity that occurs in the OS model is replaced by a non-singular bounce **beyond which the
collapsing cloud re-expands to infinity**." That is construction (ii)-like behaviour — return to the
parent's asymptotic region — **not** a closed daughter universe. Same theory, same matter model,
published in EPJC, opposite topological conclusion. **This is the sharpest literature-level
limitation on the "universe in a black hole" claim and W5 must confront it directly.**

### 4.4 Torsion's coupling strength is unmeasured
There is no measured spin–torsion coupling. Trukhanova, Andreev & Obukhov, *Search for manifestations
of spin-torsion coupling*, arXiv:2212.13871, *Universe* **9**(1), 38 (2023),
DOI 10.3390/universe9010038, derive torsion-induced polarization rotation and "establish the strong
bound on the possible cosmic axial torsion field from the astrophysical data" — i.e. the state of the
art is **bounds, not detections** (the numeric bound was not displayed on the abstract page and is
`[UNVERIFIED]`). Consequently every ECSK daughter-universe statement is
conditional on unmeasured physics, and BigBounce should never present it otherwise.

### 4.5 The Farhi–Guth "obstacle" and what FGG 1990 did and did not rescue
The false-vacuum route (iv) carries an explicit published obstacle: Farhi & Guth 1987 **[W4+W2]**
find that a bubble growing past a critical size in asymptotically flat space must have emerged from
an initial singularity. FGG 1990
(verified) does **not** remove the obstacle by classical means — it shows the bubble collapses
classically and investigates **quantum tunneling** as the escape, using a semiclassical thin-wall
treatment whose functional-integral version produced a non-manifold solution requiring an *ad hoc*
"pseudomanifold" action prescription to even estimate the probability. Any BigBounce text that
presents laboratory/false-vacuum universe creation as established is wrong on the published record.

### 4.6 Criticism of the Haggard–Rovelli timescales
Barceló, Carballo-Rubio, Garay & Jannes, *The lifetime problem of evaporating black holes: mutiny or
resignation*, arXiv:1409.1501, *Class. Quantum Grav.* **32**, 035012 (2015),
DOI 10.1088/0264-9381/32/3/035012, object that regularised black holes generically "present
long-lived trapping horizons, with absolutely enormous evaporation lifetimes in whatever measure",
and propose instead a genuinely time-symmetric bounce lasting "fractions of milliseconds for
neutron-star-like collapses" — explicitly comparing their proposal to Haggard & Rovelli in an
epilogue. Christodoulou & D'Ambrosio, arXiv:1801.03027, compute the transition from Lorentzian LQG
spinfoam amplitudes and **distinguish two different timescales**: a crossing time linear in the mass,
versus the *lifetime*, for which they "recover the exponential scaling of the lifetime in the mass",
i.e. a very long-lived, low-probability tunneling. Martin-Dussaud, arXiv:2504.05492 (2025), argues
that the resulting white-hole remnant lifetime is `M⁵` rather than the previously estimated `M⁴`.
**Net:** the timescale in this scenario is unsettled across roughly linear-in-M, `M⁴`, `M⁵`, and
exponential-in-M estimates in the published literature. This is a live dispute, not a solved number,
and it is another reason (ii) supplies no usable prediction for BigBounce.

### 4.7 "What does 'inside' mean for a realistic, rotating collapse?"
Every construction in §2 that produces a child is presented in spherical symmetry or in a homogeneous
interior model. Popławski's own rotating extension, arXiv:1910.10819, is filed as **physics.pop-ph**
and has **no journal reference**; its content is qualitative (a preferred axis, "small" non-inertial
forces, an alignment *tendency*) with no derived amplitude — the finding already recorded in
`poplawski_dipole_exclusion_2026_09_02.py`. The anisotropic follow-up arXiv:2007.11556 uses
Kantowski–Sachs and self-flags that the metric "is never reached." There is at present **no published
treatment of a realistic Kerr collapse producing a daughter universe**, and BigBounce must not imply
otherwise.

### 4.8 Bounces generically require energy-condition violation
Stated for completeness and consistency with W3's lane: a non-singular bounce requires violating an
energy condition (or replacing GR). In (iii) this is supplied by torsion, in (iv) by false vacuum,
in (v) by a de Sitter-like core with "finite density and pressures" (gr-qc/0506126). None of these
violations has been observed. This is a shared limitation across the whole family, not a defect of
any one model.

---

## 5. Smolin cosmological natural selection — **comparison only, not a BigBounce claim**

Smolin, *Did the universe evolve?*, *Class. Quantum Grav.* **9**, 173–191 (1992),
DOI 10.1088/0264-9381/9/1/016 (verified): universes with collapsing singularities "bounce" into new
universes with slightly altered parameters, producing an evolutionary pressure toward parameter
values that maximise black-hole production; if our universe is typical of that ensemble, its
parameters should be near-optimal for black-hole production. Methodological defence:
Smolin, *The status of cosmological natural selection*, hep-th/0612185 (verified).

**The falsifiable prediction, and its current status.** CNS is falsifiable through the maximum
neutron-star mass, because a higher `M_max` would open channels that change black-hole production.
The version tied to kaon condensation is stated precisely by Brown, Lee & Rho, *Kaon condensation,
black holes and cosmological natural selection*, arXiv:0802.2997, *Phys. Rev. Lett.* **101**, 091101
(2008), DOI 10.1103/PhysRevLett.101.091101 (verified): "a massive neutron star with mass
M > 2 M_sun would put in serious doubt or simply falsify the following chain of predictions:
(1) nearly vanishing vector meson mass at chiral restoration, (2) kaon condensation at a density
n ~ 3 n_0, (3) the Brown-Bethe maximum neutron star mass M_max ~ 1.5 M_sun and (4) Smolin's
'Cosmological Natural Selection' hypothesis."

**Current tension.** Romani, Kandel, Filippenko, Brink & Zheng, *PSR J0952−0607: the fastest and
heaviest known Galactic neutron star*, arXiv:2207.05124, *Astrophys. J. Lett.* **934**, L17 (2022),
DOI 10.3847/2041-8213/ac8007 (verified), report "a pulsar mass M_NS = 2.35 ± 0.17 M_⊙, the largest
well-measured mass found to date", and from reanalysis of black-widow and redback systems
"M_max > 2.19 M_⊙ (2.09 M_⊙) at 1σ (3σ) confidence." **Taken at face value this sits well above the
2 M_⊙ falsification threshold Brown–Lee–Rho named**, and the ~2.35 M_⊙ measurement is model-dependent
on the light-curve/heating fit (the paper's own framing is that "modeling uncertainties are small,
since the heating is not extreme", but it is still a fit). The 3σ statement `M_max > 2.09 M_⊙` from
the same paper is the more conservative quantity and already exceeds the threshold.

**BigBounce's position:** CNS is **context**. BigBounce does not adopt it, does not test it, and
gains nothing from it. It is listed here because the 2025 notes reached for it, and because it is the
one place in this literature where a reproduction hypothesis was made falsifiable at all — which is
precisely the standard §7/Q16 applies to the rest of the lane.

---

## 6. Galaxy-morphology sidebar — "does a central SMBH make a galaxy spiral rather than elliptical?"

1. **No.** Supermassive black holes are ubiquitous in massive galaxies of **both** classes; the most
   massive SMBHs sit in giant **ellipticals**, not spirals (Kormendy & Ho, *Coevolution (or not) of
   supermassive black holes and host galaxies*, arXiv:1304.7762, *Annu. Rev. Astron. Astrophys.*
   **51**, 511 (2013), DOI 10.1146/annurev-astro-082708-101811 — verified).
2. Kormendy & Ho further verify the reverse of the old intuition: "BHs are found in pure-disk
   galaxies, so classical (elliptical-galaxy-like) bulges are not necessary to grow BHs. But BHs do
   not correlate with galaxy disks."
3. Correlations with pseudobulges or halo dark matter "are so weak as to imply no close coevolution"
   — so BH presence is not the parameter that sorts morphology.
4. Morphology is set by **angular momentum, gas fraction, merger history, and environment**, not by
   whether a nucleus hosts a black hole.
5. AGN feedback *is* real and *does* matter — but for **quenching and bulge/elliptical assembly**:
   Kormendy & Ho's regimes 2 and 3 tie quasar-mode feedback in wet major mergers to making
   "classical bulges and coreless-rotating ellipticals", and maintenance-mode feedback into X-ray gas
   to keeping baryons hot in "giant, core-nonrotating ellipticals."
6. If anything, the verified causal arrow runs **toward** ellipticals, the opposite of the 2025 claim.
7. The 2025 note therefore inverted both the direction and the mechanism.
8. **Verdict: RETIRE.** Class F (no scientific basis). Recommended for the public Retired-Hypotheses
   page as a clean, teachable correction with the Kormendy & Ho citation attached.

**Citation warning (W2, carried here).** The dump's supporting citation `[11]`
(`nasa.gov/universe/new-simulation-sheds-light-on-spiraling-supermassive-black-holes/`) is a
**MISMATCH**: the URL resolves, but the page is a 2018 NASA/Goddard press release about the
*electromagnetic signatures of two merging SMBHs* (circumbinary disk + mini-disks) and says nothing
about SMBH prevalence across galaxy morphologies. **Do not cite `[11]` for this claim.** The
morphology sidebar above rests solely on Kormendy & Ho 2013 **[W4+W2]**. If a lay-audience source
is wanted for the public page, one must be found and verified independently.

---

## 7. Explicit answers to §18 synthesis questions 6, 11, 14, 15, 16

**Q6 — Can an ordinary astrophysical black hole generate a daughter universe in any serious
published model?**
Yes, in two peer-reviewed lines, both for construction (iii): Popławski's Einstein–Cartan model
(arXiv:1410.3881, ApJ 832, 96) applies to ordinary collapsing fermionic matter and produces "a
nonsingular, closed universe" beyond the horizon, and Frolov–Markov–Mukhanov (PRD 41, 383) attach a
de Sitter interior to the Schwarzschild interior under a limiting-curvature assumption. Both require
unmeasured high-density physics, and the ECSK line's spin-fluid step has published counter-results
in which the same collapse re-expands to infinity instead (EPJC 75, 53). Construction (iv) is
**not** available to an ordinary black hole, because it requires a pre-existing false-vacuum region.

**Q11 — Can a heat-death-bound universe have produced daughters via its black holes?**
Logically yes, and this is the one structurally clean point in the whole 2025 file. Daughter
formation in (iii) and (iv) is a **local** event behind a horizon whose causal past is the collapsing
matter, not the parent's global future; a parent that expands forever toward heat death can still
contain black holes that formed during its finite astrophysical era. There is **no observational
evidence that this happens**, and by §3 there cannot be any from the parent side. It is a coherent
theoretical distinction — a Learn-page taxonomy item — and nothing more.

**Q14 — Which old ideas deserve public retired-hypothesis documentation?**
Three, because each teaches something: (a) "a central SMBH makes a galaxy spiral" — retired against
Kormendy & Ho 2013 (§6); (b) "Einstein–Rosen bridge / white-hole side" as shorthand for a daughter
universe — a class-G terminology conflation with a crisp correction (§2.6); (c) "our universe
inherited its parent black hole's spin axis, observable as a galaxy-spin dipole" — retired by
**BigBounce's own** P4/P5 nulls and the 2026-09-02 exclusion, which makes it the strongest public
item: a hypothesis the lab itself tested and closed.

**Q15 — Which stay archival?**
Everything with no derivation behind it and nothing to teach: CTEF, GGSC, BCR, WHCIF/BHCIF, SBA,
ICBP, the `β = l_P/L_cosmic²` construction, "White Hole Sponge", "Omega Black Hole", UMPBH-as-a-
cosmic-era, and the ICBC-replaces-dark-energy route. Also archival, as retired-project provenance:
the `research/paper_1_01_archive/` parent-BH threshold `M_crit = (M_Pl⁴/ρ_vac)^{1/3}` — kept in the
genealogy record only, with the standing instruction that the symbol `M_crit` is never reused.

**Q16 — Do any surviving daughter-universe ideas yield a genuinely new falsifiable prediction the
project has not already tested?**
**None currently identified.** The taxonomy makes the reason structural rather than provisional:
the only construction that returns anything to the parent's exterior is (ii), which has no child;
the constructions that have children — (iii) and (iv) — are causally sealed by definition, so no
signal from the daughter can reach us. The one exterior-facing handle anyone has proposed for (iii)
runs the other way (the *child* inheriting the *parent's* spin axis), and BigBounce has already
tested and excluded it. The nearest thing to a live observable in this whole family is Planck-star
burst radiation (1401.6562), which belongs to (ii), is a black-hole-evaporation signature rather
than a reproduction signature, and rests on a bounce timescale that §4.6 shows is disputed across
four different scalings. **If a new prediction is ever to come from this lane, it will have to come
from the mass/energy/entropy bookkeeping (W5), not from the causal structure.**

---

## 8. Handoff notes for W5 (parent–child bookkeeping + Popławski reproduction)

**8.1 Which paper and which equations define the closed daughter FLRW and the particle-production
rate.**
The canonical source is **Popławski, arXiv:1410.3881 = *Astrophys. J.* 832, 96 (2016)**,
DOI 10.3847/0004-637X/832/2/96 — that is the paper whose abstract states the bounce, the closed
daughter universe, the particle production creating "enormous amounts of matter", the entropy
production, and the finite period of exponential expansion. **Pin the version**: the arXiv record
shows v1 submitted 14 Oct 2014 and **v2 last revised 26 May 2026**, so "arXiv:1410.3881" without a
version is ambiguous; reproduce against the published ApJ text and record the arXiv version used.
Supporting mechanism papers, all verified: arXiv:1007.0587 = *Phys. Lett. B* **694**, 181 (2010),
Erratum **701**, 672 (2011), DOI 10.1016/j.physletb.2010.09.056 (ECKS bounce; torsion density
parameter `Ω_S ≈ −10⁻⁶⁹`); arXiv:1105.6127 = *Gen. Relativ. Gravit.* **44**, 1007 (2012),
DOI 10.1007/s10714-011-1323-2 (bounce density `∝ n²/m_Pl²`, bounce at ~15× Planck energy density,
minimum scale factor ~10³² smaller than today); arXiv:1111.4595 = *Phys. Rev. D* **85**, 107502
(2012), DOI 10.1103/PhysRevD.85.107502 (cusp-like bounce at finite minimum scale factor).
Anisotropic / Kantowski–Sachs version with particle production: arXiv:2007.11556 =
*Gen. Relativ. Gravit.* **53**, 18 (2021), DOI 10.1007/s10714-021-02790-7.

**8.2 The mass-amplification claim has a closed form — and it is in a different paper.**
**Popławski, arXiv:1103.4192**, *On the mass of the Universe born in a black hole* (arXiv only; no
journal reference shown on the abstract page), states: ECSK collapse of spin-fluid fermionic matter
**with a stiff equation of state** in a black hole of mass `M` "forms a new universe of mass
`M_* = M² m_n / m_Pl²`", where `m_n` is the neutron mass; setting `M_*` to ~10²⁶ M_⊙ gives
`M ≈ 10³ M_⊙`. This is the single most reproducible quantitative statement in the whole lane.
W5 should: (a) dimension-check it (`M² · m_n / m_Pl²` → mass ✓); (b) establish how sensitive it is to
the stiff-EOS assumption; (c) evaluate it for stellar, intermediate, SMBH, and very-massive-SMBH
parents as §7 of the master prompt asks; and (d) determine whether the ratio `M_*/M = M m_n/m_Pl²`
is an **invariant** or an artifact of comparing two non-comparable mass definitions — see 8.3.

**8.3 Which quasi-local mass is appropriate on each side (this is the crux).**
- **Parent side:** the parent exterior is asymptotically flat, so **ADM** (at spatial infinity) and
  **Bondi** (at null infinity) are both defined, and for a spherically symmetric configuration the
  **Misner–Sharp** mass is the right quasi-local quantity to track through the collapse and evaluate
  at the horizon. Canonical sources, both resolved by W2 and present in
  `bibliography/archaeology_2025.bib`: Misner & Sharp, *Phys. Rev.* **136**, B571 (1964),
  DOI 10.1103/PhysRev.136.B571 **[W2]**; and, for the covariant spherically symmetric energy
  formalism, Hayward, *Gravitational energy in spherical symmetry*, gr-qc/9408002,
  *Phys. Rev. D* **53**, 1938–1949 (1996), DOI 10.1103/PhysRevD.53.1938 **[W2]**.
- **Child side:** the child in construction (iii) is a **closed FLRW** — compact spatial slices,
  **no `ℐ`, no `i⁰`, therefore no ADM mass and no Bondi mass at all**. Any statement of the form
  "the child's mass exceeds the parent's ADM mass" is comparing a quantity that exists to one that
  does not. The defensible child-side quantities are the **Misner–Sharp mass of a compact region**
  on a chosen slice, or `E = ∫_Σ ρ dV` on an explicitly named slicing — with the slicing dependence
  reported, not hidden. Note also the standard result that a closed universe has vanishing total
  Hamiltonian/constraint energy; W5 should state whether the reproduction he performs respects that,
  and if the "amplification" survives it.
- **Therefore:** the honest framing is not "energy was created" but "two different, non-equivalent
  mass functionals were evaluated on two spacetime regions with different asymptotic structure."
  Per §17 of the master prompt: **never write "infinite energy" without a derived divergence**, and
  do not report an amplification ratio as invariant until it is shown to be.

**8.4 What looks like it will not reproduce.**
1. **The particle-production rate is a free parameter, not a derived number.** 1410.3881's own
   abstract says "**depending on the particle production rate**, such a universe may undergo several
   nonsingular bounces until it has enough matter…". W5 should expect a **one-parameter family of
   histories**, not a unique prediction, and should report it that way. If a specific rate is used,
   its provenance must be traced to an equation, not inferred from a plot. The upstream
   gravitational-particle-creation formalism the rate must ultimately reduce to is
   Parker, *Phys. Rev.* **183**, 1057 (1969), DOI 10.1103/PhysRev.183.1057 **[W2]**, and — for the
   anisotropic case relevant to the Kantowski–Sachs interior — Zel'dovich & Starobinsky,
   *Sov. Phys. JETP* **34**, 1159 (1972) **[W2, lower confidence: no primary APS/ADS record reached;
   W2 recommends an ADS bibcode check before load-bearing use]**.
2. **The anisotropic version self-flags as unreached.** 2007.11556: "This scenario is only
   approximate: the Kantowski-Sachs metric is never reached and should be replaced with a more
   general metric that tends to that of a 3-sphere." It also requires **particle production to
   dominate over shear** for the bounce to occur at all — an inequality W5 should check numerically
   rather than assume.
3. **A published counter-result with the same ingredients.** Hashemi, Jalalzadeh & Ziaie,
   arXiv:1407.4103, *Eur. Phys. J. C* **75**, 53 (2015), DOI 10.1140/epjc/s10052-015-3276-1, run
   ECSK Oppenheimer–Snyder collapse with a homogeneous Weyssenhoff fluid and get a bounce whose
   cloud **"re-expands to infinity"** — back into the parent's asymptotic region, i.e. construction
   (ii)-like, **no daughter universe**. Same theory, same matter model, opposite topology. If W5's
   reproduction cannot say why the two differ (matching conditions at the surface? trapped-surface
   formation? equation of state? the stiff-EOS assumption in 1103.4192?), the bookkeeping result is
   not yet meaningful.
4. **The spin-fluid averaging is a modelling choice.** Weyssenhoff + Frenkel is not derived from a
   Dirac-field treatment; see arXiv:1611.07878 (PRD 95, 104007) for the unrestricted kinematics and
   arXiv:0907.1701 (IJMPA 24, 1652) for the point that Einstein–Cartan torsion is non-dynamical and
   entirely determined by the assumed spin source. The `⟨s²⟩` that sets the bounce density depends
   on the averaging prescription; W5 should report which prescription he used and how the bounce
   density moves under a reasonable alternative.
5. **Numbers to sanity-check against, from the verified abstracts:** bounce density `∝ n²/m_Pl²`,
   bounce at ~15× Planck energy density for Standard-Model content, minimum scale factor ~10³²
   smaller than today (1105.6127); torsion density parameter `Ω_S ≈ −10⁻⁶⁹` (1007.0587). If the
   reproduction lands far from these, something is wrong in the reproduction, not in the paper.
6. **Do not import the spin-axis observable.** It is excluded (§1.2). Bookkeeping only.

---

## 9. Reference list

**Cross-worker status.** Entries marked **[W4+W2]** were resolved independently by W4 (this session,
by fetching the arXiv abstract page or DOI landing page) **and** appear as resolved entries in W2's
`research/archaeology_2025/bibliography/VERIFIED_BIBLIOGRAPHY.md` / `archaeology_2025.bib`.
Entries marked **[W4]** were resolved by W4 only (they are outside the set W2 was asked to resolve).
Entries marked **[W2]** come from W2's verified `.bib` and were not independently re-fetched by W4.
For BibTeX keys, cite from `bibliography/archaeology_2025.bib`.

Verified by arXiv abstract page or DOI landing page on 2026-09-18:

- Fuller & Wheeler, *Phys. Rev.* **128**, 919 (1962) — DOI 10.1103/PhysRev.128.919 **[W4]**
- Penrose, *Phys. Rev. Lett.* **14**, 57 (1965) — DOI 10.1103/PhysRevLett.14.57 **[W4]** *(record verified; no abstract displayed)*
- Blau, Guendelman & Guth, *Phys. Rev. D* **35**, 1747 (1987) — DOI 10.1103/PhysRevD.35.1747 **[W4]**
- Farhi & Guth, *Phys. Lett. B* **183**(2), 149 (1987) — DOI 10.1016/0370-2693(87)90429-1 **[W4+W2]** *(pre-arXiv; no abstract retrieved by either worker; content per W2's ScienceDirect check)*
- Frolov, Markov & Mukhanov, *Phys. Rev. D* **41**, 383 (1990) — DOI 10.1103/PhysRevD.41.383 **[W4+W2]**
- Farhi, Guth & Guven, *Nucl. Phys. B* **339**, 417 (1990) — DOI 10.1016/0550-3213(90)90357-J **[W4+W2]**
- Smolin, *Class. Quantum Grav.* **9**, 173 (1992) — DOI 10.1088/0264-9381/9/1/016 **[W4+W2]**
- Hayward, *Phys. Rev. Lett.* **96**, 031103 (2006) — gr-qc/0506126, DOI 10.1103/PhysRevLett.96.031103 **[W4]**
- Smolin, hep-th/0612185 (2006) **[W4]**
- Brown, Lee & Rho, *Phys. Rev. Lett.* **101**, 091101 (2008) — arXiv:0802.2997, DOI 10.1103/PhysRevLett.101.091101 **[W4]**
- de Berredo-Peixoto & de Freitas, *Int. J. Mod. Phys. A* **24**, 1652 (2009) — arXiv:0907.1701 **[W4]**
- Popławski, *Cosmology with torsion*, *Phys. Lett. B* **694**, 181–185 (2010); Erratum **701**, 672 (2011) — arXiv:1007.0587, DOI 10.1016/j.physletb.2010.09.056 **[W4+W2]**
- Popławski, *Radial motion into an Einstein-Rosen bridge*, *Phys. Lett. B* **687**, 110–113 (2010) — arXiv:0902.1994, DOI 10.1016/j.physletb.2010.03.029 **[W4+W2]** *(W2 correction: this is B **687**:110, NOT B 694:181 — see §2.6.1)*
- Popławski, arXiv:1103.4192 (2011) **[W4]** *(arXiv only; no journal ref on the abstract page)*
- Popławski, *Gen. Relativ. Gravit.* **44**, 1007 (2012) — arXiv:1105.6127, DOI 10.1007/s10714-011-1323-2 **[W4+W2]**
- Popławski, *Phys. Rev. D* **85**, 107502 (2012) — arXiv:1111.4595, DOI 10.1103/PhysRevD.85.107502 **[W4]**
- Kormendy & Ho, *Annu. Rev. Astron. Astrophys.* **51**, 511 (2013) — arXiv:1304.7762, DOI 10.1146/annurev-astro-082708-101811 **[W4+W2]**
- Rovelli & Vidotto, *Planck stars*, *Int. J. Mod. Phys. D* (2014) — arXiv:1401.6562, DOI 10.1142/S0218271814420267 **[W4+W2]**
- Haggard & Rovelli, *Phys. Rev. D* **92**, 104020 (2015) — arXiv:1407.0989, DOI 10.1103/PhysRevD.92.104020 **[W4+W2]**
- Hashemi, Jalalzadeh & Ziaie, *Eur. Phys. J. C* **75**, 53 (2015) — arXiv:1407.4103, DOI 10.1140/epjc/s10052-015-3276-1 **[W4]**
- Barceló, Carballo-Rubio, Garay & Jannes, *Class. Quantum Grav.* **32**, 035012 (2015) — arXiv:1409.1501, DOI 10.1088/0264-9381/32/3/035012 **[W4]**
- Popławski, *Astrophys. J.* **832**, 96 (2016) — arXiv:1410.3881, DOI 10.3847/0004-637X/832/2/96 **[W4+W2]**
- Pasmatsiou, Tsagas & Barrow, *Phys. Rev. D* **95**, 104007 (2017) — arXiv:1611.07878 **[W4]**
- Christodoulou & D'Ambrosio, arXiv:1801.03027 (2018) **[W4]**
- Bianchi, Christodoulou, D'Ambrosio, Haggard & Rovelli, *Class. Quantum Grav.* **35**, 225003 (2018) — arXiv:1802.04264, DOI 10.1088/1361-6382/aae550 **[W4]**
- Ashtekar, Olmedo & Singh, *Phys. Rev. Lett.* **121**, 241301 (2018) — arXiv:1806.00648, DOI 10.1103/PhysRevLett.121.241301 **[W4+W2]**
- Ashtekar, Olmedo & Singh, *Phys. Rev. D* **98**, 126003 (2018) — arXiv:1806.02406, DOI 10.1103/PhysRevD.98.126003 **[W4]**
- Popławski, arXiv:1910.10819 (2019) **[W4]** *(physics.pop-ph; no journal reference)*
- Ashtekar & Olmedo, *Int. J. Mod. Phys. D* **29**, 2050076 (2020) — arXiv:2005.02309, DOI 10.1142/S0218271820500765 **[W4]**
- Popławski, *Gen. Relativ. Gravit.* **53**, 18 (2021) — arXiv:2007.11556, DOI 10.1007/s10714-021-02790-7 **[W4]**
- Romani, Kandel, Filippenko, Brink & Zheng, *Astrophys. J. Lett.* **934**, L17 (2022) — arXiv:2207.05124, DOI 10.3847/2041-8213/ac8007 **[W4]**
- Trukhanova, Andreev & Obukhov, *Universe* **9**(1), 38 (2023) — arXiv:2212.13871, DOI 10.3390/universe9010038 **[W4]**
- Martin-Dussaud, arXiv:2504.05492 (2025) **[W4]**
- Ashtekar & Singh, *Loop quantum cosmology: a status report*, *Class. Quantum Grav.* **28**, 213001 (2011) — arXiv:1108.0893, DOI 10.1088/0264-9381/28/21/213001 **[W2]** *(canonical LQC bounce review; cited in §3)*
- Misner & Sharp, *Phys. Rev.* **136**, B571 (1964) — DOI 10.1103/PhysRev.136.B571 **[W2]** *(quasi-local mass; §8.3)*
- Hayward, *Phys. Rev. D* **53**, 1938–1949 (1996) — gr-qc/9408002, DOI 10.1103/PhysRevD.53.1938 **[W2]** *(spherically symmetric gravitational energy; §8.3)*
- Parker, *Phys. Rev.* **183**, 1057 (1969) — DOI 10.1103/PhysRev.183.1057 **[W2]** *(gravitational particle creation; §8.4)*
- Zel'dovich & Starobinsky, *Sov. Phys. JETP* **34**, 1159 (1972) **[W2, lower confidence]** *(anisotropic particle production; §8.4)*

**Still unresolved after both workers — do not cite as evidence:**

- Bardeen (1968), regular black hole, GR5 Tbilisi proceedings — `[UNVERIFIED]`. No DOI; not in W2's
  resolved set. The attribution used in §2(v) rests only on Hayward's verified description of his
  own static region as "Bardeen-like".
- Pathria, *The Universe as a Black Hole*, *Nature* **240**, 298 (1972), DOI 10.1038/240298a0 —
  bibliographic record resolved by W4 via DOI-keyed metadata; **abstract not retrieved** (Nature
  auth-wall) and not in W2's resolved set. Cite for **priority only**; content `[UNVERIFIED]`.
- Good, *Chinese universes*, *Physics Today* **25**(7), 15 (1972) — `[UNVERIFIED]` (AIP landing page
  returned 403 to W4; not in W2's set).
- The numeric cosmic-axial-torsion bound inside arXiv:2212.13871 — `[UNVERIFIED]` (the paper is
  verified; the specific number is not displayed on the abstract page and was not retrieved).
- *Recommendation to the director:* these four are the only open citation items on this lane. They
  are all provenance/priority items, none is load-bearing for any statement in this memo, and none
  blocks W5.

Repo artifacts referenced (read-only):
`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` and its
`outputs/poplawski_dipole_exclusion_2026_09_02.json`;
`research/bh_universe_dipole/outputs/a95_null_cl_2026_09_02.json`;
`pipelines/p2_chirality/chirality_catalog_paper.tex`;
`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`;
`research/paper_1_01_archive/main.tex` + `ARCHIVAL_NOTE.md` (**retired**; provenance only).
