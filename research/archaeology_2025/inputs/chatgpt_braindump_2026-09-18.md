# ChatGPT brain-dump on the 2025 pre-BigBounce exploratory notes (received 2026-09-18)

**Provenance:** Houston Golden shared this verbatim on 2026-09-18 in a Claude Code session in
`~/Desktop/CODE_YOU`. It is the output of a ChatGPT session that reviewed Houston's March–July 2025
Notion notes (White Hole Sponge / Black Hole Sponge / ICBC / Omega Black Hole / "Born in a black hole")
against the live BigBounce site and current literature. It is **provenance, not science**. Nothing in
it is authoritative; every citation must be resolved independently (see `../bibliography/`).

Houston's framing when sharing it: "without affecting any current on-going research ... historical
context from my initial idea exploration before realizing i needed a proper scientific setup which is
what led me to create hubify and the bigbounce projects ... don't destroy my good research."

Director's corrections (Claude, 2026-09-18) before any worker used this document:
- "Lane 18/19/20" do not exist as free slots; `project-context/NEXT_SCIENCE_LEDGER.md` already runs to item 19. New items are #20, #21, #22.
- Popławski's rotating-black-hole-universe spin-axis prediction was already confronted with the DESI A95 upper limit on 2026-09-02 (`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py`, Track C1 / P4′). That route is closed; only the mass/energy/entropy bookkeeping question is open.
- There are at least three historical `M_crit` definitions (Notion-era Λc²r³/3G; the retired parent-BH threshold `(M_Pl⁴/ρ_vac)^{1/3} ≈ 10⁻³ M_☉` in `research/paper_1_01_archive/`; a Horndeski braiding scale in `research/branch_I_bounce_compatible_DE/`). Never reuse the symbol.
- The site already has `/speculations` and `/learn`; the missing surface is a genealogy / retired-hypotheses page.
- `research/branch_I_bounce_compatible_DE/` overlaps the cosmic-fate lane; check it before deriving.
- Citations [2], [3], [8] and the 2026-07-30 DESI post are UNVERIFIED as of receipt.

---

## Verbatim dump

Yes. I found substantially more than the three pages you remembered, and there is a useful scientific story buried in it.

I recovered what is available from our older conversation context, your Notion tree and nested pages, current BigBounce artifacts/library, the active GitHub repository and SSOT, the live site, and current literature. I can't guarantee verbatim recovery of every old chat message that is no longer indexed, but the conceptual lineage is surprisingly complete.

### The big picture

Your BigBounce work has effectively gone through **four generations**:

| Era | What you were exploring | What survived |
|---|---|---|
| **Mar 2025 — White Hole Sponge / ICBC** | Universe ending in a giant black hole, white-hole rebirth, ICBC, QGBW, Omega Black Hole, VCA | The intuition that **gravitational collapse might terminate in a nonsingular new expanding spacetime** |
| **Mar 25–27, 2025 — Black Hole Sponge pivot** | Reframed from "white-hole universe" to **our universe as the interior/daughter of a parent black hole** | Much stronger conceptual direction; less dependence on literal white holes |
| **Jul 2025 — "Born in a black hole"** | Einstein–Cartan spin-torsion + LQC-like bounce + rotating parent BH + inherited observables | The legitimate **ECSK nonsingular black-hole/bounce literature** and parent→daughter-universe question |
| **2026 BigBounce** | Derivations, reproducibility, adversarial peer review, DESI, actual falsification | A much narrower, substantially more defensible program: bounce phenomenology, ECH/torsion, DESI tests, with failed routes openly published as nulls. ([BigBounce][1]) |

And that fourth generation is important. The live site now explicitly says the ECH derivation retains the positive torsion-bounce mechanism while closing four candidate dark-energy routes, and your DESI spin-axis test is a null. That's exactly the kind of pruning the early material needed. ([BigBounce][1])

The old work should therefore **not be restored as a theory**. It should be mined for questions.

### 1. The Big Crunch deserves a serious new BigBounce research lane

**Can a Big Crunch actually happen?** Yes. Absolutely, as a physically legitimate cosmological possibility. But not because gravity will simply "eventually overpower dark energy," and not because black holes will inevitably merge until there is one Omega Black Hole.

Under ordinary flat ΛCDM with a truly positive, constant cosmological constant, expansion does not reverse. The far-future extrapolation is instead approximately asymptotic de Sitter/heat death: matter becomes increasingly isolated, black holes eventually evaporate, and the local spacetime approaches an extremely dilute equilibrium state. ([arXiv][2])

A genuine turnaround from expansion to contraction requires something to change the Friedmann dynamics. Schematically, H² = (8πG/3)ρ − kc²/a². A turnaround occurs at some finite a_t when H(a_t)=0 and expansion actually transitions to contraction when Ḣ(a_t)<0.

That can happen through scientifically respectable mechanisms including: a scalar/dark-energy field whose potential eventually becomes **negative**; an effectively negative cosmological constant; sufficiently important positive spatial curvature if the accelerating component decays; interacting dark-sector models that change the future effective energy density; particular modified-gravity scenarios. There are published models in which a presently accelerating universe later reaches a turnaround precisely because a scalar potential becomes negative. ([APS Journals][3])

**But DESI does not currently imply a future Big Crunch.** The July 30, 2026 DESI DR2 Lyα full-shape result actually moved its central value **toward ΛCDM**, and DESI explicitly says this could mean the evolving-dark-energy hints eventually fade, although a more complicated model remains possible. ([DESI][4])

So a strong new BigBounce lane would ask: **Given all current cosmological constraints, what physically complete classes of dark-energy models permit our currently accelerating universe to undergo a future turnaround, and what observable present-day signatures distinguish them?**

Your preference for a regenerative universe is completely reasonable as **motivation for asking the question**. It should simply never enter the likelihood function, priors, derivation, or model selection.

### 2. A Big Crunch and a Big Bounce are two separate questions

Even if the universe turns around and contracts, vanilla GR does **not** automatically produce a new universe. Classical GR drives the contraction toward a singularity. You need a second mechanism: expansion → turnaround → contraction → **then what?**

Possible nonsingular answers include: **Einstein–Cartan / ECSK** (fermionic spin sources torsion, producing an effective repulsive interaction at enormous densities; Popławski explicitly derived a Big Bounce from this mechanism ([arXiv][5])); **Loop quantum cosmology** (quantum geometry modifies the high-curvature Friedmann dynamics and generically replaces certain classical singularities with a bounce ([Penn State][6])); and numerous other nonsingular/bounce constructions.

Clean chain: **Fate problem** (can our universe ever recollapse?) → **Singularity problem** (if it contracts, does high-density physics terminate contraction in a bounce?) → **Inheritance problem** (what information/perturbations/entropy/rotation survive the bounce?) → **Observability** (would any of those leave something measurable today?). Each is independent.

### 3. The "baby universe can be vastly larger than the parent black hole" idea is much more legitimate than expected

Popławski's published Einstein–Cartan black-hole cosmology explicitly proposes that a black hole avoids a singularity through spin-torsion repulsion and forms a closed daughter universe beyond its horizon, and further argues that **quantum particle production can drive an exponential expansion and create an enormous amount of matter in the daughter universe.** ([arXiv][7])

The scientifically precise version is not "a bounce can create infinite energy from nothing." It is: **In some black-hole baby-universe models, the proper matter content and spatial volume of the daughter cosmology can grow dramatically through particle production and/or inflation-like expansion, and there is no generic requirement that a naive integrated daughter-universe mass equal the parent black hole's asymptotic mass.**

**What does "mass of the parent" versus "mass of the child" even mean?** Those aren't automatically comparable quantities in GR. The parent may have an ADM/Bondi or quasi-local black-hole mass. A closed FLRW child may have E_child = ∫_Σ ρ dV on some chosen spatial slice. GR enforces local covariant conservation ∇_μ T^{μν} = 0, but an expanding FLRW spacetime generally lacks the global time-translation symmetry needed to define one universally conserved global total energy. ([DOI][8])

**Parent–Child Mass & Energy Bookkeeping lane:** compare, in actual published baby-universe models: (1) parent ADM/Bondi/quasi-local mass; (2) mass at the throat/horizon; (3) child-universe proper matter energy; (4) gravitational binding energy; (5) particle-production contribution; (6) vacuum energy/inflationary contribution; (7) entropy before and after the bounce; (8) dependence on spatial slicing; (9) whether an "amplification factor" is invariant or merely coordinate/model dependent. Then actually reproduce Popławski's calculation numerically.

### 4. A cleaner version of the "hope after the Big Freeze" idea

Two independent reproductive routes. **Route A — global reproduction:** expand → future turnaround → Big Crunch → nonsingular bounce → new expansion (requires both recollapse physics and bounce physics). **Route B — local reproduction:** star/galaxy → black hole → nonsingular interior → daughter cosmology; the parent universe could continue expanding toward heat death while some of its black holes had already generated causally disconnected daughter universes. Popławski's model explicitly adopts essentially this second picture. ([arXiv][7])

Reformulated carefully: **A heat-death future for our observable universe would not logically exclude reproductive cosmologies in which black holes formed during its finite astrophysical era seed daughter spacetimes.** We have **no observational evidence that this actually happens**, but it is a coherent theoretical distinction. It connects to Smolin-style cosmological natural selection without requiring BigBounce to adopt it.

### 5. The old M_crit was not entirely nonsense — it was misinterpreted

March 2025 notes had M_crit = Λc²r³/(3G), interpreted as "enough mass within a cosmic radius to overcome dark energy and initiate universal collapse." Too sweeping. But rearranged, r = (3GM/Λc²)^{1/3} is the established **maximum turnaround radius** relation in ΛCDM for a bound structure; Pavlidou & Tomaras derive exactly this scale. ([arXiv][9]) Old idea (universal critical collapse mass): ❌. Real physics hiding inside it (maximum scale at which a mass concentration can remain gravitationally bound against positive Λ): ✅.

**P_crit:** no evidence of a consistently defined physical P_crit that should be preserved. Memory is blending M_crit (in at least two unrelated meanings), ρ_crit in LQC-like bounce equations, Planck density/curvature, and pressure in early ICBP/QGBW brainstorming. Retire P_crit unless a buried source turns up with an actual derivation; use model-specific ρ_bounce, curvature threshold, or torsion density instead.

### 6. "Einstein–Rosen bridge / white-hole side" needs a terminology cleanup

Three things got merged: (A) classical Einstein–Rosen bridge in maximally extended Schwarzschild; (B) black → white hole transition (Haggard & Rovelli ([arXiv][10])); (C) black hole → separate daughter universe (Popławski-type ECSK ([arXiv][7])). Not synonyms. Draw Penrose diagrams side by side; stop using "Einstein–Rosen bridge" as shorthand unless the spacetime analyzed has one.

### 7. Drop immediately: "central black holes make galaxies spiral"

SMBHs are extremely common in massive galaxies of different morphologies ([NASA][11]). Morphology depends on stellar orbital structure, gas, angular momentum, star-formation history, merger history and environment. Retire.

### The Notion archaeology

| Page | What it represents | Recommendation |
|---|---|---|
| [Interior Black Hole Sponge Multiverse Theory — 3/20/25](https://app.notion.com/p/1bdb98b1bcf880129099fc15b7ec47f8) | Giant master tree; Omega BH, Mcrit, Crunch/Freeze, BHCP, UMPBHs | Preserve as historical source |
| [NEW BEST VERSION — White Hole Sponge Multiverse / ICBC](https://app.notion.com/p/1bdb98b1bcf880e29985f23647d55e33) | Peak ICBC/QGBW/Omega synthesis | Archive, do not revive |
| [Born in a black hole](https://app.notion.com/p/238b98b1bcf880df81daebb496bc5869) | Later ECSK/LQC/rotating-black-hole version | Mine carefully — strongest old scientific base |
| [Refining ICBC / replacing dark energy](https://app.notion.com/p/1bdb98b1bcf880f8bf46fde4675069af) | β=l_P/L_cosmic², boundary acceleration | Retire |
| [Black Hole Sponge — Equations Part 1](https://app.notion.com/p/1c1b98b1bcf8806b9bc8ea3b65f43898) | CTEF, ICBP, GGSC, BCR, WHCIF, SBA equations | Raw archive only |
| [Black Hole Sponge Cosmology — official outline](https://app.notion.com/p/1c1b98b1bcf88025a0ecceb6076b920d) | Pivot from white-hole framing to BH-interior framing | Historical genealogy |
| [Grok — Black Hole Inverted Cosmology](https://app.notion.com/p/1c2b98b1bcf88095957be3661fbb69ea) | Maximum AI overreach: invented parameters/equations/citations | Do not use as science |
| [White Holes — book outline](https://app.notion.com/p/1bdb98b1bcf8807dac02c79c10e52538) | Big Freeze → BH era → Omega → rebirth narrative | Useful history/philosophy |

The "Equations Part 1" page literally has the AI introducing "truly original and novel theories and equations" such as CTEF, GGSC, BCR, WHCIF and SBA without deriving them from an action, symmetry, EFT, field equations, or prior literature. Preserve internally as a provenance artifact; zero authority in present-day physics.

### Complete idea triage

| Old concept | Disposition | What to do now |
|---|---|---|
| Big Crunch → possible bounce | 🟢 PURSUE | New rigorous cosmic-fate lane |
| Big Freeze / heat death | 🟢 DOCUMENT | Proper comparison baseline |
| Parent BH → daughter universe | 🟢 PURSUE | Literature + mathematical taxonomy |
| Daughter contains much more matter than parent BH | 🟢 PURSUE, REFRAME | Reproduce particle-production / mass-bookkeeping results |
| Local black holes reproduce even if parent freezes | 🟡 CONCEPTUAL SYNTHESIS | Ideas/learn page; theoretical implication, not fact |
| Mcrit = Λc²r³/3G | 🟢 SALVAGE | Reidentify as turnaround-radius relation |
| Pcrit | 🔴 DROP | No consistent recovered definition |
| ρ_crit high-density bounce | 🟢 KEEP MODEL-SPECIFIC | ECSK/LQC etc.; don't universalize |
| Omega Black Hole | 🟡 ARCHIVE AS THOUGHT EXPERIMENT | May represent global recollapse endpoint, but not inevitable |
| All black holes inevitably merge into Omega BH | 🔴 RETIRE | False under an eternally accelerating Λ universe |
| BHCP | 🟡 HISTORICAL | Descriptive speculative phase only |
| UMPBH as required cosmic era | 🔴 RETIRE | Unsupported |
| White-hole Big Bang language | 🟡 USE ONLY WITH SPECIFIC GEOMETRY | Otherwise say daughter/bounce spacetime |
| ICBC replaces dark energy | 🔴 RETIRE PUBLICLY | Modern ECH work has already closed dark-energy routes |
| β=l_P/L_cosmic² | 🔴 DROP | Dimensional construction, not a derived coupling |
| ICBP | 🔴 DROP | Ad hoc pressure profile |
| QGBW/QGIW literal walls | 🔴 DROP AS MECHANISM | "nonsingular transition surface" only after deriving it |
| VCA triggers collapse | 🔴 DROP | No established mechanism |
| CTEF | 🔴 RAW ARCHIVE ONLY | AI-created ansatz |
| GGSC equation | 🔴 RAW ARCHIVE ONLY | Current DESI spin-axis test is null anyway |
| BCR extra redshift mechanism | 🔴 RAW ARCHIVE ONLY | No derived geodesic mechanism |
| WHCIF/BHCIF entropy-flow equation | 🔴 RAW ARCHIVE ONLY | Holographic language without actual theory |
| SBA field | 🔴 RAW ARCHIVE ONLY | Equation not derived from a consistent field theory |
| Parent angular momentum inherited by child | 🟡 CONSTRAINED / OPTIONAL | Theoretical initial-condition problem; current observed spin-axis route is null |
| Bounce-generated stochastic GW spectrum | 🟡 POSSIBLE BUT START OVER | Derive from a real bounce background, never reuse guessed spectrum |
| PBHs inherited from parent universe | 🟡/🔴 VERY SPECULATIVE | Keep only if causal/topological mechanism can be derived |
| Bounce resets entropy | 🟡 REAL PROBLEM, OLD SOLUTION INVALID | Study entropy transfer separately |
| Central SMBH → spiral morphology | 🔴 DROP | Not supported |
| JWST/CMB cold spots/H0 "confirm" BHS-MC | 🔴 DROP | Those old claims were unjustified |
| Smolin-style cosmological reproduction | 🟡 COMPARE | Literature/context, not evidence |

### What to expose publicly

Three layers: **Current Science** (exactly as the site works now; no 2025 exploratory equation enters without independent re-derivation); **Research Ideas / Open Questions** (Big Crunch, cosmic fate, black-hole daughter universes, parent-child energy bookkeeping, entropy; every item marked "Open question · Literature review · Not a claim"); **Research Genealogy / Retired Hypotheses** (curated, not exhaustive: White Hole Sponge → ICBC → Black Hole Interior → Einstein–Cartan → current falsifiable program, plus ~4 retired examples: ICBC as dark energy; inevitable Omega Black Hole; inherited galaxy-spin alignment; PBH/GW routes that later produced nulls). Microscopic AI-generated debris (CTEF, SBA, WHCIF, placeholder citations, arbitrary parameter ranges) stays in archival source material.

Suggested disclaimer: "These early AI-assisted exploratory notes predate the project's current derivation, reproducibility and adversarial-review standards. They are preserved for provenance. Historical hypotheses are not current claims; several were subsequently retired, reformulated, or falsified."

### The strongest new lanes

**Cosmic Fate: Can an Accelerating Universe Recollapse?** — derive turnaround conditions → classify viable physical models → run current observational constraints → avoid invalid w0,wa extrapolation → quantify which allowed models Crunch → only then connect to bounce physics.

**Black-Hole Daughter Universes: Mass, Energy & Entropy Across a Bounce** — reproduce Popławski → compare ECSK, LQC/Planck-star/black-to-white, false-vacuum baby-universe mechanisms → define mass rigorously on both sides → determine exactly what "matter amplification" means → ask what observable consequences survive.

**Reproductive Cosmology Fate Tree** — formalizes global recollapse/bounce vs local black-hole reproduction vs heat death without reproduction; Learn page, not a paper.

### Master prompt (as delivered; numbering of "lanes 18/19/20" is WRONG for this repo, see director's corrections above)

MISSION: rigorous scientific archaeology of the 2025 pre-BigBounce work. Old material is NOT authoritative. Job: (1) recover every distinct idea; (2) locate its scientific kernel, if any; (3) compare against current literature and current BigBounce; (4) explicitly retire bad ideas; (5) identify worthwhile unanswered questions; (6) launch new rigorous lanes where justified; (7) document the genealogy without contaminating the current record; (8) update the public site only where evidence level warrants. Houston's preference for a regenerative universe motivates QUESTIONS only; never evidence, prior, model-selection criterion. Nulls are first-class.

§0 Read AGENTS.md, project-context/AGENT_ONBOARDING.md, CLAUDE.md, AGENT_RULES.md, SSOT index/queue, PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md, FUTURE_PAPERS.md, site architecture, current tracks/nulls/ledger first. SSOT is authoritative. Do NOT edit active manuscripts for this archaeology.

§1 Archaeology search terms (rg + git log -S/-G, archived/deleted files): "White Hole Sponge", "Black Hole Sponge", "Omega Black Hole", "Omega Singularity", "Big Crunch", "Big Freeze", "heat death", "Big Rip", "ICBC", "Inverse/Inverted Cosmic Boundary Curvature", "ICBP", "QGBW", "QGIW", "VCA", "Vacuum Collapse Anomaly", "UMPBH", "BHCP", "CTEF", "GGSC", "BCR", "WHCIF", "BHCIF", "SBA", "Mcrit", "M_crit", "Pcrit", "P_crit", "rho_crit", "critical density", "Einstein-Rosen", "white hole", "baby universe", "daughter universe", "universe in a black hole", "Planck star", "particle production", "matter amplification", "entropy reset", "cosmic natural selection". Produce a source map: first appearance; later mutations; whether Houston proposed the kernel or an AI manufactured the math; whether it survived; whether current BigBounce already tested/closed it.

§2 Legacy Notion sources: the eight pages above and their subpages, if Notion access exists. Resolve EVERY citation; a non-resolving citation is evidence of a historical hallucination — never silently replace it.

§3 Legacy-hypothesis ledger statuses: A ESTABLISHED FOUNDATION; B ACTIVE RESEARCH QUESTION; C HISTORICAL/SPECULATIVE; D SUPERSEDED; E FALSIFIED/CLOSED BY BIGBOUNCE; F RETIRED — NO SCIENTIFIC BASIS; G TERMINOLOGY CONFLATION. Each row: name; exact historical claim; source(s); closest legitimate literature; mathematical status; observational status; current BigBounce relationship; disposition; public/private recommendation; successor question (may be "none").

§4 Omega BH / Big Crunch: derive turnaround conditions from Friedmann + Raychaudhuri; distinguish flat ΛCDM, positive curvature, transient DE, quintessence with negative potentials, negative Λ, interacting dark sector, phantom/quintom, modified gravity. Require finite a_turn, H(a_turn)=0, correct sign of Ḣ, energy conditions/stability. Do NOT extrapolate CPL w0–wa to a→∞. Use newest DESI DR2 as of Sept 2026. Posterior fractions only within explicit model classes; never a model-independent "probability of a Big Crunch".

§5 Crunch ≠ Bounce: compare classical GR, ECSK, ECH limits from current BigBounce, LQC, other nonsingular effective models; state precisely what causes contraction, singularity avoidance, H=0, Ḣ>0 at the bounce.

§6 Parent BH → daughter universe literature: Popławski EC black-hole universe; spin-torsion nonsingular interiors; particle production; false-vacuum baby universes; Planck stars; Haggard–Rovelli; recent LQG BH singularity resolution; Smolin CNS (comparison only); rebuttal literature. Do NOT conflate: eternal ER bridge; black-to-white transition in same asymptotic region; causally disconnected baby universe; closed FLRW inside/behind horizon; false-vacuum bubble.

§7 Parent–child bookkeeping: parent ADM/Bondi/Misner–Sharp/horizon mass; stress-energy entering collapse; child ρ(t), V(t), ∫ρdV; vacuum, gravitational/constraint, particle-production contributions; entropy; slicing dependence; causal relation. Audit ∇_μT^{μν}=0; whether a global conserved energy is definable. Reproduce Popławski's particle-production/matter claim independently (equations, units, assumptions, ICs, fermion content, production model, whether exponential expansion is essential, what "amplification" means). Numerical examples for stellar, intermediate, SMBH, very massive SMBH parents. Compute an invariant amplification ratio if definable; otherwise say why and replace with correct invariants. NEVER write "infinite energy" without a derived divergence.

§8 M_crit/P_crit: reidentify Λc²r³/3G as the turnaround-radius relation; repo-wide symbol audit; if no coherent P_crit exists say so and do not manufacture one.

§9 Untrusted historical equations (ICBC, ICBP, QGBW, QGIW, VCA, CTEF, GGSC, BCR, WHCIF/BHCIF, SBA; e.g. `P_ICBP(r,t) = -(ħcΛ_ICBC)/(8πGr²) exp(-t/t_boundary)`, `E_CT = ∫ R T Ψ_ent dV`, `N_CW/N_CCW ∝ exp(∫ κ_ICBC s·dA)`): for each ask derivable from a covariant action? valid indices? dimensionally consistent? symmetries? known theory already covers it? independently predictive? already closed by BigBounce data? If no → retire; do not "fix".

§10 Dispositions to test (not accept): LIKELY RETIRE the whole red list above plus "infinite energy"; POTENTIALLY SALVAGE turnaround conditions, nonsingular completion, BH daughter universes, spin-torsion singularity avoidance, particle-production amplification, entropy across a bounce, inherited angular momentum as bounded IC problem, bounce GWs from a real derived background, M_crit→turnaround-scale, local vs global reproduction. Compare every one with current nulls first; closed stays closed unless the new mechanism is mathematically distinct.

§11 Galaxy morphology sidebar: resolve from literature quickly; document the correction; move on.

§12 Cosmic reproduction fate tree (taxonomy, NOT a probability ranking): A eternal expansion/heat death, no daughter mechanism; B eternal expansion + local BH daughter universes; C global turnaround → Crunch → classical singularity; D global turnaround → contraction → nonsingular bounce → new expansion; E other model-specific endpoint. For each: required physics, present constraints, falsifiability, unknowns, relation to BigBounce results.

§13 New lanes only after triage; numbering follows the current ledger.

§14 Public-site IA: three evidence layers (Current Science / Open Questions / Research Genealogy); no raw 2025 notes on the main site; suggested disclaimer above.

§15 Required outputs: (1) Historical Research Archaeology; (2) Cosmic Fate Technical Memo; (3) Black-Hole Daughter Universe Technical Memo; (4) Parent–Child Energy & Entropy Memo; (5) Retired Hypotheses Ledger; (6) Verified Bibliography; (7) Site-copy draft (only after memos); (8) Science ledger entries (only for genuinely active questions).

§16 Source quality: peer-reviewed > official collaboration release > arXiv > review > institutional. Never cite AI prose, blogs, or old Notion/BigBounce text as evidence for itself.

§17 Scientific rules: never invent an equation or citation; no arbitrary parameter ranges called predictions; no novelty by absence of prior art; derive from action/field equations; dimensional checks; state assumptions; toy vs physical; possibility vs plausibility; present data vs far-future extrapolation; preserve negatives; no cherry-picking; preference is not evidence; do not blend speculation into accepted results; existing nulls remain nulls.

§18 Synthesis must answer: (1) Can our universe Crunch despite accelerating? (2) What physical changes are required? (3) What do Sept 2026 observations permit? (4) Does Crunch imply Bounce? (5) Which nonsingular mechanisms could convert one to the other? (6) Can an ordinary astrophysical BH generate a daughter universe in any serious published model? (7) Can the daughter contain vastly more proper matter than the parent's mass? (8) Where does the additional matter come from mathematically? (9) Does that violate local conservation? (10) Is there a meaningful invariant amplification ratio? (11) Can a heat-death-bound universe have produced daughters via its BHs? (12) Was historical M_crit meaningful? (13) Did P_crit ever exist coherently? (14) Which old ideas deserve public retired-hypothesis documentation? (15) Which stay archival? (16) Do any surviving ideas yield a genuinely new falsifiable prediction not already tested?

§19 Gate: archaeology + literature FIRST; per lane: literature → derivation/reproduction → independent calculation → adversarial review → truth-audit → decision (CLOSED/OPEN/PROMISING/RESULT) → only then site/SSOT integration. Explanatory-only output → Learn/Ideas artifact, not a paper.

DEFINITION OF DONE: lineage reconstructed; every major concept dispositioned; fake citations quarantined; M_crit/P_crit resolved; Crunch vs Bounce separated; recollapse constraints documented; daughter-universe literature mapped; Popławski amplification reproduced or shown not to; bookkeeping in defensible GR quantities; current nulls intact; new lanes only where warranted; public copy distinguishes current science / open questions / retired history; site + SSOT synchronized; committed per normal workflow.

### Citation list as delivered (UNVERIFIED until `../bibliography/VERIFIED_BIBLIOGRAPHY.md` says otherwise)

[1] https://bigbounce.hubify.app/
[2] https://arxiv.org/abs/1201.1298
[3] https://journals.aps.org/prd/abstract/10.1103/PhysRevD.69.063511
[4] https://www.desi.lbl.gov/2026/07/30/new-desi-dr2-lyman-alpha-results-shed-light-on-dark-energy/
[5] https://arxiv.org/abs/1105.6127
[6] https://pure.psu.edu/en/publications/loop-quantum-cosmology-a-status-report/
[7] https://arxiv.org/abs/1410.3881
[8] https://doi.org/10.3390/galaxies14010008
[9] https://arxiv.org/abs/1310.1920
[10] https://arxiv.org/abs/1407.0989
[11] https://www.nasa.gov/universe/new-simulation-sheds-light-on-spiraling-supermassive-black-holes/
