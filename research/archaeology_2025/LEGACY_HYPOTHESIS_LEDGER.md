# Legacy Hypothesis Ledger — 2025 pre-BigBounce archaeology (worker W6)

**Inputs:** `PLAN.md`; braindump director's-corrections/triage/§9/§10
(`inputs/chatgpt_braindump_2026-09-18.md`); `SOURCE_MAP.md` §§1–6 (canonical,
per director note — the W1 addendum at §6 corrects/supersedes §§1–5 on
pre-campaign-vs-campaign-only provenance) and `SOURCE_MAP_git_history_W1.md`
(full git-history sweep, preferred for first-appearance facts, flagged where
it disagrees with the working-tree-only `rg` pass); `bibliography/VERIFIED_BIBLIOGRAPHY.md`
+ `archaeology_2025.bib`; `memos/COSMIC_FATE_MEMO.md` (W3), `memos/DAUGHTER_UNIVERSE_MEMO.md`
(W4), `memos/PARENT_CHILD_BOOKKEEPING_MEMO.md` (W5).

**Provenance discipline (per director's mid-task correction).** `SOURCE_MAP.md`'s
completed git-history sweep (§6) shows that of the ~40 search terms, only **2**
(Omega Black Hole, Inverse Cosmic Boundary) have zero hits in git history ever,
but **21 more** have **zero hits before 2026-09-18** — i.e. they entered the
repo only via this campaign's own provenance files (the braindump-ingestion
commit `95affd13`, the ledger-item commit `6fd06cdb`, the genealogy-page
commit `ddf40b75`, and the memo commits). Below, any row whose only repo
"evidence" is one of those campaign artifacts is marked **"Notion/ChatGPT
provenance only (no pre-2026-09-18 repo presence)"** in the Source(s) column —
the genealogy page and this ledger are today's *output*, not yesterday's
*evidence*, and must not be cited as if they were pre-existing repo history.
Two further terms (BCR, SBA) show only coincidental substring collisions in
unrelated commit messages pre-campaign (confirmed false positives, not real
historical usage) and are marked accordingly rather than "zero hits."
`research/paper_1_01_archive/main.tex` and `arxiv/_retired/main.tex` share
**one** origin commit, `b4d4c601` (2026-02-26) — one lineage, not two — per
W1's cross-checked `git log --follow --diff-filter=A` result; cited that way
throughout.

**Disposition legend:** A ESTABLISHED FOUNDATION · B ACTIVE RESEARCH QUESTION ·
C HISTORICAL/SPECULATIVE · D SUPERSEDED · E FALSIFIED/CLOSED BY BIGBOUNCE ·
F RETIRED — NO SCIENTIFIC BASIS · G TERMINOLOGY CONFLATION.

Existing BigBounce nulls (Popławski spin-axis dipole exclusion, galaxy-spin
dipole null, ECH dark-energy closures) are treated as nulls throughout, not
reopened.

---

## 1. Ledger

| # | Name | Exact historical claim | Source(s) | Closest legitimate literature | Mathematical status | Observational status | Current BigBounce relationship | Disposition | Public/private rec | Successor |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Big Crunch (global recollapse) | The universe's expansion will eventually reverse and it will recollapse into a Big Crunch. | Braindump §1; `status.html`, `speculations.html`, `research/branch_V_bounce_evidence/05_top3_candidates.md` (pre-campaign, generic term); `COSMIC_FATE_MEMO.md` (this campaign) | Garriga2004; KalloshLinde2003; Kallosh2003b | Derived turnaround condition (§2–3 of memo); impossible under constant Λ>0, any curvature, at Ω_m<1 (Eq. 3.5) | DESI DR2 BAO+Lyα (arXiv:2503.14738, arXiv:2607.27410) prefer evolving DE but do not forecast a turnaround; CPL→a→∞ extrapolation is invalid | Not yet a BigBounce claim; new open lane | B | Open Questions (`/speculations`) | ledger #20 |
| 2 | Big Freeze / heat death | The far future is an asymptotically dilute, cold, expanding de Sitter-like equilibrium. | Braindump §1; `speculations.html`, `status.html`; `COSMIC_FATE_MEMO.md` | Lundgren2012 | Standard ΛCDM flat-space asymptotics; no turnaround (§3a) | Consistent with all current data; the default reading of flat ΛCDM | Documented as the comparison baseline for the cosmic-fate lane | A | Current Science (baseline, not a BigBounce result) | none |
| 3 | Big Rip | Phantom dark energy (w<−1) drives a future finite-time curvature singularity. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) — braindump search-term list; addressed in `COSMIC_FATE_MEMO.md` §3(f) | none in `archaeology_2025.bib` (Caldwell–Kamionkowski–Weinberg, PRL 91:071301 (2003), cited in memo References but not in the campaign .bib) | Distinguished from a Crunch: CPL a→∞ with w_a<0 gives ρ_DE→0⁺, not a Rip (Eq. 4.1) | Not favored or excluded by current DESI data; a separate model class from the Crunch question | Not a BigBounce claim; one branch of the fate taxonomy (Branch E) | C | Genealogy page (taxonomy context only) | none |
| 4 | Omega Black Hole (thought-experiment entity) | A single, universal terminal black hole representing a hypothetical global-recollapse endpoint. | Notion/ChatGPT provenance only — **zero hits in git history ever**, including this campaign's own commits (exact phrase never literally committed) | none | No defining equation anywhere in the recovered material | Not observationally addressable; not a physical model | Archived as a thought-experiment label inside the fate taxonomy (Branch C/E), not a mechanism | C | Genealogy page | none |
| 5 | "All black holes inevitably merge into an Omega Black Hole" | Cosmic evolution inevitably drives every black hole to merge into one final black hole. | Notion/ChatGPT provenance only (same zero-hit status as row 4) | none | No merger mechanism ever derived | False under an eternally accelerating, constant, positive Λ: causally disconnected regions never merge (`COSMIC_FATE_MEMO.md` §3a, §8 Branch A) | Contradicted by BigBounce's own accepted ΛCDM-consistent fate baseline | F | Retired-Hypotheses page | none |
| 6 | Parent black hole → daughter universe ("baby universe", "universe in a black hole") | An ordinary astrophysical black hole's interior can non-singularly become a new, closed expanding universe. | Real pre-campaign lineage: repo's first commit `36cfb8d7` (2025-07-22, `bigbounce.md`) through `research/paper_1_01_archive/main.tex` (origin `b4d4c601`, 2026-02-26) to active P4′ (`ac065a61`, 2026-09-02); `DAUGHTER_UNIVERSE_MEMO.md` (this campaign) | Poplawski2016; Poplawski2010torsion; Poplawski2012; FrolovMarkovMukhanov1990 | Five causal constructions taxonomized (§2 of memo); only (iii) closed-FLRW-behind-horizon and (iv) false-vacuum bubble produce a genuine child, both require unmeasured high-density physics, and a published counter-result (Hashemi et al. 2015) gets the *same* theory to re-expand into the parent instead | The one exterior-facing observable this construction offers (inherited spin axis) is EXCLUDED (row 30); no signal from a genuine daughter can otherwise reach the parent, by causal construction | B | Open Questions (`/speculations`) | ledger #21 |
| 7 | Daughter can contain vastly more matter than the parent's mass ("matter amplification") | Particle production and/or inflation-like expansion inside the daughter can make its matter content dramatically exceed the parent black hole's mass. | "Matter amplification" as an exact phrase: Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence); the underlying question has real pre-campaign lineage via "particle production"/"daughter universe" (row 6); `PARENT_CHILD_BOOKKEEPING_MEMO.md` (this campaign, independent numerical reproduction) | Poplawski2016; Poplawski2010torsion; Poplawski2012 | Reproduced at the equation level to ≤0.3% (T_max, τ, H_max, bounce density 15.37 ρ_Pl); but the "amplification" is set by a free production coefficient β (or an assumed energy→rest-mass conversion), not by the parent mass; the child's total Misner–Sharp mass is exactly zero regardless (§2.2, §4.7 of memo) | Not tested against BigBounce data; a bookkeeping/definitional result, not an observable | B | Open Questions (`/speculations`) | ledger #22 |
| 8 | Local black-hole reproduction survives even if the parent freezes | A parent universe heading to heat death can still have spawned daughter universes via black holes formed during its finite astrophysical era. | Braindump §4 ("hope after the Big Freeze"); `DAUGHTER_UNIVERSE_MEMO.md` §7 (Q11) | Poplawski2016; Smolin1992 (comparison only) | A structurally clean logical point, not a derivation: daughter formation is local and behind a horizon, causally decoupled from the parent's global future | No observational evidence this happens, and by causal construction there cannot be any from the parent side | Coherent theoretical distinction; a Learn-page taxonomy item, not a testable claim | C | Learn page / Open Questions (context only, not a standalone question) | none |
| 9 | M_crit — Notion-era `Λc²r³/(3G)` ("universal collapse mass") | Enough mass within a cosmic radius r would overcome dark energy and trigger universal collapse once M exceeded this value. | Notion-era only; not found verbatim anywhere in the repo or git history (predates the repo) — braindump §5; `COSMIC_FATE_MEMO.md` §6 (re-derivation, this campaign) | PavlidouTomaras2014 | Correctly rearranges to `r_ta = (3GM/Λc²)^{1/3}`, the established maximum-turnaround-radius relation for one bound structure (verified against Pavlidou & Tomaras); applied globally, the criterion reduces identically to the ordinary deceleration condition `ρ_m>2ρ_Λ`, satisfied by the real universe at all z>0.6323 without any recollapse | Not a global fate criterion; a real, existing ΛCDM structure-scale test | D | Retired-Hypotheses page (salvaged relation renamed `r_ta`) | none |
| 10 | M_crit — retired parent-BH naturalness threshold `(M_Pl⁴/ρ_vac)^{1/3}≈10⁻³M_☉` | Any astrophysical black hole's mass naturally exceeds the threshold needed for its interior vacuum energy to source the Einstein-Cartan bounce mechanism. | `research/paper_1_01_archive/main.tex:228` and `arxiv/_retired/main.tex:246` — byte-identical, **both trace to the single origin commit `b4d4c601`** (2026-02-26; corrected from an earlier two-lineage hedge, `SOURCE_MAP.md` §6(iii)); deleted from the active `arxiv/paper1a_ech_nogo.tex` | none | No derivation or citation for this sentence exists anywhere in the repo; deriving one now would be fabrication (pattern-036) per `project-context/peer-reviews/R23conf_P1A_TRUTH_AUDIT.md` finding META-m1; also flagged earlier by `2026-06-04_R4fixed_P1A_DeepSeek_confab.md` (P1A-N1) and `2026-06-01_R-multi-true95..._GPT5_methodology.md` | N/A | Deleted from the live paper at R23conf; survives only in archived/retired copies as a provenance artifact | F | Genealogy page (provenance record only; symbol never reused) | none |
| 11 | M_crit — Horndeski braiding scale | Cubic Horndeski dark energy with braiding scale M below M_crit develops a ghost instability at the bounce. | `research/branch_I_bounce_compatible_DE/horndeski_bounce_stability/01_problem_statement.md` (dated 2026-03-16 in-file); live, unrelated research branch, not a Notion-era item | none assigned a number yet | Stated as a hypothetical "strong success" placeholder criterion, not a derived value or number | Untested; part of an active, not-yet-executed derivation | Unrelated to the 2025 archaeology; a live BigBounce research question already tracked outside this campaign | B | Not a public item (internal research branch) | none (already tracked in `research/branch_I_bounce_compatible_DE/`; no new ledger item needed) |
| 12 | P_crit | A critical pressure scale, blended across Notion notes with M_crit, ρ_crit, Planck density/curvature, and an ICBP/QGBW pressure ansatz. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) — braindump §5; `COSMIC_FATE_MEMO.md` §7 | none | No derivation, no defining equation, no dimensionally consistent usage found anywhere in the recovered material or the repo | N/A | No coherent historical referent recoverable; must not be reconstructed or assigned a value | F | Retired-Hypotheses page (name only, no physics) | none |
| 13 | ρ_crit (model-specific bounce density) | A critical density at which a nonsingular bounce occurs, in a specific model (LQC, ECSK). | `research/paper_1_01_archive/main.tex` (~L232, origin `b4d4c601`, 2026-02-26); `horndeski_bounce_stability/01_problem_statement.md` — real, continuous pre-campaign usage | AshtekarSingh2011; Poplawski2012 | Well-defined per model: `ρ_c=3/(κγ²λ²)≈0.41ρ_Pl` (LQC); torsion bounce density `∝n²/m_Pl²` (ECSK) — braindump's own recommended usage | Active, legitimate physics in the current P1A-lineage Friedmann equation | Correctly used as a model-specific quantity, never universalized | A | Current Science (as used in active papers, not a genealogy item) | none |
| 14 | BHCP | An era/phase label within the March-2025 Black Hole Sponge cosmology notes; descriptive, no attached equation. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) | none | No mathematical content of its own | N/A | Not engaged by current BigBounce work | C | Genealogy page (provenance list) | none |
| 15 | UMPBH as a required cosmic era | Ultra-massive primordial black holes are a mandatory intermediate era of cosmic evolution. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) | none | No supporting derivation anywhere in the recovered material | Unsupported; not observationally required | Not engaged by current BigBounce work | F | Retired-Hypotheses page | none |
| 16 | White-hole Big Bang language | The Big Bang can be described, narratively, as a "white hole" event. | Braindump §"Complete idea triage"; generic term "white hole" has real pre-campaign hits (2026-02-18 site regenerations onward), but this specific narrative usage is Notion-era framing | HaggardRovelli2015 (for the distinct, unrelated black-to-white transition construction) | Not a derived statement; a narrative label that risks importing construction (ii)'s physics (same-asymptotic-region return) into a Big Bang context where it does not apply | N/A | Not current BigBounce usage; `DAUGHTER_UNIVERSE_MEMO.md` §2.6 requires precise construction-numbered language instead | C | Learn page (use only with specific geometry named) | none |
| 17 | "Einstein–Rosen bridge" / white-hole side, as shorthand for a daughter universe | The classical Einstein–Rosen bridge, the black-to-white-hole transition, and a causally disconnected daughter universe were treated as interchangeable. | "Einstein-Rosen" as a named term: Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence); the underlying Popławski bridge paper is real and independently verified | Poplawski2010ER (arXiv:0902.1994, PLB 687:110 — corrected pairing, W2); HaggardRovelli2015 | Three distinct constructions with incompatible geometry: (i) eternal ER bridge has two eternal exteriors and nothing transmitted (Fuller & Wheeler 1962); (ii) black-to-white returns matter to the *same* asymptotic region; (iii) closed-FLRW daughter has no second asymptotic region at all, so there is nothing for a "bridge" to connect to (`DAUGHTER_UNIVERSE_MEMO.md` §2.6) | N/A — a language error, not a tested claim | Memo's own characterization: "the single most consequential error in the recovered material" | G | Retired-Hypotheses/Genealogy page (as a named terminology correction) | none |
| 18 | ICBC (Inverted/Interior Cosmic Boundary Curvature) replaces dark energy | A cosmic-boundary curvature mechanism was proposed to source late-time acceleration instead of a cosmological constant. | One coincidental, unconfirmed pre-campaign git hit (`f11eb418`, spot-checked as a binary byte-match artifact, **not** the ICBC concept, per `SOURCE_MAP_git_history_W1.md`); otherwise Notion/ChatGPT provenance only | none | No covariant action, no dimensional derivation anywhere in the recovered material | N/A | BigBounce's own ECH derivation already closed four candidate dark-energy routes independently, without invoking ICBC | F | Retired-Hypotheses page | none |
| 19 | β = l_P/L_cosmic² (boundary-acceleration coupling) | A dimensionless ratio of the Planck length to a cosmic length scale was proposed as a physical coupling constant. | Notion/ChatGPT provenance only; not separately git-searched as a term — Notion page "Refining ICBC / replacing dark energy" | none | A dimensional construction, not a derived coupling from any action or field equation | N/A | Not engaged by current BigBounce work | F | Retired-Hypotheses page | none |
| 20 | ICBP (ad hoc pressure profile, e.g. `P_ICBP(r,t)=-(ħcΛ_ICBC)/(8πGr²)exp(-t/t_boundary)`) | A boundary-pressure profile was proposed as a physical mechanism without derivation. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) | none | Fails braindump §9's own test: not derivable from a covariant action, no established symmetry justification | N/A | Not engaged by current BigBounce work | F | Retired-Hypotheses page (raw archive) | none |
| 21 | QGBW / QGIW as a literal nonsingular-transition "wall" | A literal quantum-gravity boundary/interior wall was proposed as the physical mechanism terminating collapse. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence), both acronyms | none | No derivation of the "wall" as a specific transition surface; braindump itself allows the *phrase* "nonsingular transition surface" only after an actual derivation is supplied | N/A | Not engaged by current BigBounce work | F | Retired-Hypotheses page (raw archive; door not closed to a future derivation under different naming) | none |
| 22 | VCA (Vacuum Collapse Anomaly) triggers collapse | An anomalous vacuum-collapse mechanism was proposed to trigger cosmic collapse. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) | none | No established mechanism; no equation with a stated derivation | N/A | Not engaged by current BigBounce work | F | Retired-Hypotheses page (raw archive) | none |
| 23 | CTEF (equation, e.g. `E_CT=∫RTΨ_ent dV`) | An AI-generated ansatz combining curvature, temperature, and an entropy field was presented as an original theory. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) — "Black Hole Sponge — Equations Part 1" Notion page | none | Not derived from an action, symmetry, EFT, or field equations; the source page itself introduces it as "truly original and novel" without derivation | N/A | Not engaged by current BigBounce work | F | Archival only (raw archive; zero present-day authority) | none |
| 24 | GGSC equation | An AI-generated equation, unrelated to any derived spin-axis mechanism, associated with the galaxy-spin dipole narrative. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) — same "Equations Part 1" source | none | Not derived from an action or field theory | The DESI spin-axis test (rows 30) is null regardless of whether this equation is retired | Same-family speculative equation as CTEF/BCR/WHCIF/SBA | F | Archival only | none |
| 25 | BCR (extra redshift mechanism) | An additional redshift mechanism was proposed without a derived geodesic origin. | No genuine pre-campaign presence; only coincidental substring collisions in unrelated commit messages (P3 R33conf, EXT3-stamp, P4 pod-session commits) — confirmed false positives, not real historical usage (`SOURCE_MAP_git_history_W1.md`) | none | No derived geodesic mechanism anywhere in the recovered material | N/A | Not engaged by current BigBounce work | F | Archival only | none |
| 26 | WHCIF / BHCIF entropy-flow equation | An entropy-flow equation using holographic-sounding language (e.g. `N_CW/N_CCW∝exp(∫κ_ICBC s·dA)`) was proposed without a defined theory. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence), both acronyms — "Equations Part 1" page | none | Holographic language without an actual underlying theory; fails the covariant-action test of braindump §9 | N/A | Not engaged by current BigBounce work | F | Archival only | none |
| 27 | SBA field | An AI-generated field, not derived from a consistent field theory. | No genuine pre-campaign presence; only coincidental substring collisions in unrelated commit messages (P4 R23conf, arxiv-kit tarball commits) — confirmed false positives (`SOURCE_MAP_git_history_W1.md`) | none | No derivation from any consistent field theory | N/A | Not engaged by current BigBounce work | F | Archival only | none |
| 28 | White Hole Sponge (Mar 2025 umbrella hypothesis) | The universe ends in a giant black hole and is reborn through a literal white hole, with ICBC/QGBW/Omega BH/VCA as its supporting apparatus. | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence); Notion page "NEW BEST VERSION — White Hole Sponge Multiverse/ICBC" recommended "archive, do not revive" | none | The apparatus (ICBC, QGBW, VCA, Omega BH) has no derivation (rows 4–5, 18, 20–22); as a specific physics package it has zero scientific content | N/A | Not restored as theory (per Houston's own framing and hard constraint #2); only the general intuition ("collapse might terminate nonsingularly") survives, and that intuition is carried forward by row 6, not by this package | F | Genealogy page (era label, explicitly retired as a physics package, not merely archived) | none |
| 29 | Black Hole Sponge (Mar 25–27, 2025 pivot) | A reframing from "white-hole universe" to "our universe as the interior/daughter of a parent black hole." | Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence); Notion pages "Black Hole Sponge Cosmology — official outline" and "Black Hole Sponge — Equations Part 1" (the latter's equations are rows 23–27, separately retired) | Poplawski2016 (retrospectively, this pivot's conceptual seed) | The pivot itself is a reframing, not an equation; its supporting equations (CTEF/GGSC/BCR/WHCIF/SBA) are separately retired (rows 23–27) | N/A | This is the genuine conceptual seed of row 6 (parent→daughter framing), which is what survived and became scientifically tractable | C | Genealogy page (era label; conceptual seed preserved, apparatus not) | none |
| 30 | Inherited galaxy-spin-axis dipole (rotating parent → observable child dipole) | A rotating parent black hole imprints a preferred spin axis on its daughter universe, observable today as a dipole in galaxy chirality/spin alignment. | Real pre-campaign lineage: Popławski citation chain from `f6669470` (2026-02-15) onward; `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` (2026-09-02, pre-campaign); `pipelines/p2_chirality/chirality_catalog_paper.tex` | none in `archaeology_2025.bib` (Popławski arXiv:1910.10819 is physics.pop-ph, no journal reference, qualitative only) | No published Popławski paper gives a derived dipole amplitude; the exclusion runs on an explicit toy closure (dipole amplitude ≡ alignment efficiency η), not a literal model prediction | **Closed.** DESI Legacy DR8 (N=887,472) gives a dipole consistent with zero (z_mom=+0.635, p=0.23768); the 2026-09-02 exclusion shows literature amplitudes (Longo ~7%, Shamir 2-20%, Shamir 2025 20-33%) sit 2-30x above the A₉₅ᵒᵇˢ=0.98% sensitivity floor | This is an **existing BigBounce null and stays a null** per the hard constraints; not reopened by this campaign | E | Genealogy/Retired-Hypotheses page (BigBounce's own tested-and-closed result) | none |
| 31 | Bounce-generated stochastic gravitational-wave spectrum | A stochastic GW background with a specific spectral shape was guessed as a signature of the bounce. | Braindump §"Complete idea triage" only; not independently git-searched as a distinct term | none | No derivation from a real bounce background exists; the guessed spectrum has no stated derivation | Untested; not currently a BigBounce analysis | Not currently pursued; would require deriving from an actual bounce background, never reusing the guessed spectrum | C | Not public (no lane exists; flagged, not opened) | none |
| 32 | Primordial black holes (PBHs) inherited from the parent universe | Black holes formed in the parent universe could be inherited by, or seed, the daughter universe's PBH population. | Braindump §"Complete idea triage" only; not independently git-searched as a distinct term | none | No causal/topological mechanism derived anywhere in the recovered material | Untested | Very speculative; kept only conditionally on a future derived mechanism | C | Not public | none |
| 33 | Bounce resets entropy | The bounce mechanism resets or discards the universe's entropy, allowing a fresh start. | "Entropy reset": Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence) — braindump §5, §"idea triage" | Poplawski2016 (partial; §4.8 entropy discussion) | Old proposed "reset" is invalid: in the reproduced Popławski model entropy is conserved through a bounce absent production and only ever increases with it (dS/dt∝K≥0); there is no reset, only ordinary dilution at late times (`PARENT_CHILD_BOOKKEEPING_MEMO.md` §4.8) | Untested; a genuine open bookkeeping question distinct from the closed "reset" framing | Real problem, old solution invalid; entropy-transfer study proposed as a separate question, not yet formalized into a lane | B | Not public (no lane/method exists yet; flagged for future work, not opened this campaign) | none |
| 34 | Central supermassive black hole causes spiral galaxy morphology | A galaxy's central black hole determines whether it forms a spiral rather than an elliptical shape. | Braindump §7; `DAUGHTER_UNIVERSE_MEMO.md` §6 (this campaign) | KormendyHo2013 | Directly contradicted: the most massive SMBHs sit in giant ellipticals, not spirals; morphology tracks angular momentum, gas fraction, merger history, and environment | Verified against Kormendy & Ho (2013) ARA&A review; the dump's own supporting NASA citation [11] is a MISMATCH (resolves, but supports nothing about morphology) | Retired; recommended as a public teachable correction | F | Retired-Hypotheses page | none |
| 35 | JWST/CMB cold spots/H0 tension "confirm" Black-Hole-Sponge multiverse cosmology (BHS-MC) | Various independent anomalies (JWST early-galaxy results, CMB cold spots, the H0 tension) were claimed as confirming evidence for the 2025 black-hole-sponge framework. | Braindump §"Complete idea triage" | none | No derivation connecting BHS-MC to any of these anomalies exists anywhere in the recovered material | Those old claims were unjustified: each anomaly has its own independent, unrelated literature explaining it | Not engaged by current BigBounce work; would be a severe overreach if revived | F | Retired-Hypotheses page | none |
| 36 | Smolin-style cosmological natural selection | Universes reproduce through black holes with mutation of physical constants, and constants we observe are selected for maximizing black-hole production. | "Cosmological natural selection": Notion/ChatGPT provenance only (no pre-2026-09-18 repo presence); `DAUGHTER_UNIVERSE_MEMO.md` §5 (comparison only, this campaign) | Smolin1992 | A real, independently published, and internally coherent mechanism — not itself flawed — but BigBounce does not adopt it | Untested by BigBounce; comparison literature only | Context/comparison, not evidence; connects to but is independent of row 8 | C | Learn page (comparison context only) | none |
| 37 | Planck star | A quantum-gravity bounce inside gravitational collapse produces a "Planck star" with an observable burst signature. | Weak pre-campaign presence: `2b0b0086` (2026-03-03, 148-paper literature sweep) only; `DAUGHTER_UNIVERSE_MEMO.md` mechanism table (this campaign) | RovelliVidotto2014 | A real published mechanism (construction (ii) in the causal taxonomy); belongs to the black-to-white transition family, not to a genuine daughter universe | Proposed detectable signal near 10⁻¹⁴ cm wavelength (literature claim); not independently tested by BigBounce; timescale disputed across roughly linear-in-M, M⁴, M⁵, and exponential-in-M estimates in the literature (§4.6 of memo) | Literature-mapped comparison; not tested against BigBounce data | C | Learn page / genealogy page (literature-map context) | none |

---

## 2. Disagreements with the ChatGPT triage

Six rows where this worker's disposition or framing differs from the dump's
"Complete idea triage" table (or its narrative text), with reasons:

1. **Row 7 — "daughter contains vastly more matter than parent" (matter
   amplification).** The dump headlines this as "much more legitimate than
   expected" and dispositions it 🟢 PURSUE, REFRAME. W5's actual numerical
   reproduction (`PARENT_CHILD_BOOKKEEPING_MEMO.md`) found the specific claim
   the dump was excited about — an invariant parent-to-child amplification
   ratio — **does not exist**: every reproducible number is set by a free
   production coefficient β (or an assumed energy→rest-mass conversion), not
   by the parent mass, and two Popławski papers give amplification factors
   with *opposite* dependence on M for the same parent (∝M vs independent of
   M). This worker keeps the row as B (the bookkeeping question is still a
   legitimate open lane, per ledger #22) but disagrees with the dump's framing
   that this idea turned out "more legitimate than expected" — the naive
   version of the claim is now closed-negative, not merely reframed.
2. **Row 10 vs. row 9 — the dump never distinguishes the three M_crit
   definitions in its formal triage table** (it lists only one row, "Mcrit =
   Λc²r³/3G 🟢 SALVAGE"). This worker, following the director's correction and
   `SOURCE_MAP.md`/`COSMIC_FATE_MEMO.md` §6, treats the Notion-era relation
   (row 9, disposition D, salvaged), the retired parent-BH threshold (row 10,
   disposition F, fabrication risk) and the Horndeski braiding scale (row 11,
   disposition B, unrelated live research) as three separate rows with three
   different dispositions, because conflating them — exactly what the dump's
   single triage row risks — is the error the director's correction #3
   explicitly warns against.
3. **Row 17 — Einstein–Rosen bridge / white-hole-side terminology.** The dump
   frames this narratively as needing "a terminology cleanup" (§6 of the
   verbatim dump), a comparatively mild framing, and does not give it its own
   triage-table row or color. `DAUGHTER_UNIVERSE_MEMO.md` §2.6 calls this "the
   single most consequential error in the recovered material" and gives it
   the ledger's most severe non-retirement category, G (TERMINOLOGY
   CONFLATION), because it made a category error — "our universe is on the
   white-hole side of an Einstein–Rosen bridge" — sound like a statement about
   a real spacetime when no cited construction has that structure. This
   worker follows the memo's stronger assessment over the dump's softer one.
4. **Row 28 vs. row 29 — White Hole Sponge and Black Hole Sponge.** The dump's
   "big picture" narrative table treats both eras uniformly as contributing to
   "the intuition that gravitational collapse might terminate in a nonsingular
   new expanding spacetime," without dispositioning either individually. This
   worker splits them: Black Hole Sponge (row 29) gets C (historical/
   speculative) because it is the genuine conceptual seed of the still-live
   parent→daughter question (row 6); White Hole Sponge (row 28) gets **F**
   (no scientific basis) because its specific supporting apparatus — ICBC,
   QGBW, Omega Black Hole, VCA — has zero derivation (rows 4–5, 18, 20–22), and
   its own Notion page was explicitly recommended "archive, do not revive,"
   which is a retirement-strength verdict on the physics package, not merely
   an archival label. The dump's narrative blends these two eras into one
   undifferentiated "intuition survived" story; this worker disagrees with
   collapsing them.
5. **Row 30 — inherited galaxy-spin-axis dipole.** The dump's triage table
   marks this 🟡 CONSTRAINED/OPTIONAL ("theoretical initial-condition problem;
   current observed spin-axis route is null"), which frames the observational
   route as merely one still-open consideration among others. This worker
   dispositions the observable claim as **E — FALSIFIED/CLOSED BY BIGBOUNCE**,
   full stop, per the director's own correction #2 ("That route is closed;
   only the mass/energy/entropy bookkeeping question is open") and hard
   constraint #2 (existing nulls stay nulls). The deeper theoretical
   initial-condition question the dump also gestures at is a different,
   still-open question already covered by row 6/33, not a reason to soften
   the observational disposition.
6. **Row 33 — "bounce resets entropy."** The dump frames this as 🟡 REAL
   PROBLEM, OLD SOLUTION INVALID and implicitly treats it as ready for a
   dedicated study. This worker agrees the underlying question is legitimate
   (disposition B) but disagrees that it is ready to become a formal ledger
   item alongside #20–#22: no lane, method, or derivation path has been
   proposed anywhere in the recovered material or the memos, unlike #20–#22
   which each have a stated research program. See §3 of this document's report
   for the skeptical read on new B items.

No disagreement is recorded merely because this worker used a different label
than the dump's colored badge (e.g. 🟢 SALVAGE ≈ D; 🔴 RETIRE ≈ F; 🟡 COMPARE ≈
C) where the underlying verdict is the same.

---

## 3. M_crit / P_crit resolution

**Three M_crit definitions, confirmed distinct, no fourth found** (matches
Director's correction #3 exactly):

1. **Notion-era `M_crit = Λc²r³/(3G)`** ("universal collapse mass"). Rearranges
   exactly to `r_ta = (3GM/Λc²)^{1/3}`, the established ΛCDM maximum-
   turnaround-radius relation (Pavlidou & Tomaras, arXiv:1310.1920, verified).
   `COSMIC_FATE_MEMO.md` §6 shows the historical global-collapse reading is
   wrong on three independent grounds, including that applied to a homogeneous
   sphere the criterion reduces identically to the ordinary deceleration
   condition `ρ_m>2ρ_Λ` — satisfied by the real universe at all z>0.6323
   without any recollapse. **Salvage the relation as `r_ta`; retire the symbol
   and the "collapse mass" interpretation** (row 9, disposition D).
2. **Retired parent-black-hole naturalness threshold, `M_crit=(M_Pl⁴/ρ_vac)^{1/3}≈10⁻³M_☉`.**
   `research/paper_1_01_archive/main.tex:228` / `arxiv/_retired/main.tex:246`
   (single origin commit `b4d4c601`, 2026-02-26). No derivation or citation
   ever existed in the repo; deleted from the active paper at R23conf as a
   fabrication risk (pattern-036). **Retired, no scientific basis** (row 10,
   disposition F).
3. **Horndeski braiding scale, `M_crit`** in
   `research/branch_I_bounce_compatible_DE/horndeski_bounce_stability/01_problem_statement.md`.
   A hypothetical "strong success" placeholder for a not-yet-executed
   derivation, never assigned a number. A live, unrelated research question
   (row 11, disposition B) — not part of this archaeology campaign's ledger.

**Recommendation (per `COSMIC_FATE_MEMO.md` §6.4, adopted here): never reuse
the bare symbol `M_crit` in any BigBounce artifact.** Use `r_ta` for definition
1, and give definitions 2 and 3 explicit subscripted names at their point of
use if they are ever referenced again.

**P_crit: no coherent historical definition was recovered.** Expected answer
confirmed: **no.** `COSMIC_FATE_MEMO.md` §7 finds no derivation, no defining
equation, and no dimensionally consistent usage for the symbol anywhere in the
recovered material or the repo. The historical usage blended at least four
distinct quantities — a mass threshold (M_crit), the LQC bounce density, the
Planck density/curvature scale, and an ad hoc pressure ansatz from ICBP/QGBW
brainstorming. Correct, well-defined, model-specific substitutes already exist
and should be used by name instead: `ρ_c≈0.41ρ_Pl` (LQC), the torsion/spin-
density bounce scale (ECSK), curvature invariants generally, and the
turnaround density `ρ_tot(a_t)=3kc²/(8πGa_t²)` for the fate problem
specifically (row 12, disposition F — retired, not manufactured).

---

## 4. Hallucination quarantine

Every fabricated, invented, or non-resolving citation/equation identified by
W2 or the memo workers, with where it appeared:

1. **Retired parent-BH `M_crit≈10⁻³M_☉` sentence** (row 10). No
   derivation/citation anywhere in the repo; identified as a fabrication risk
   by `project-context/peer-reviews/R23conf_P1A_TRUTH_AUDIT.md` (finding
   META-m1), and flagged earlier (without yet calling it fabrication) by
   `2026-06-04_R4fixed_P1A_DeepSeek_confab.md` (P1A-N1) and
   `2026-06-01_R-multi-true95..._GPT5_methodology.md`. Deleted from the live
   paper at R23conf.
2. **CTEF, GGSC, BCR, WHCIF/BHCIF, SBA equations** (rows 23–27). The Notion
   page "Black Hole Sponge — Equations Part 1" has an AI "introducing 'truly
   original and novel theories and equations'... without deriving them from
   an action, symmetry, EFT, field equations, or prior literature" (braindump
   §"The Notion archaeology"). The companion page "Grok — Black Hole Inverted
   Cosmology" is independently flagged by the dump itself as "maximum AI
   overreach: invented parameters/equations/citations." Preserved only as
   provenance artifacts; zero present-day authority.
3. **Master-prompt §9 untrusted equations** (`P_ICBP(r,t)=-(ħcΛ_ICBC)/(8πGr²)exp(-t/t_boundary)`,
   `E_CT=∫RTΨ_ent dV`, `N_CW/N_CCW∝exp(∫κ_ICBC s·dA)`) — the same class as item
   2, quarantined as archival, never "fixed" (rows 20, 23, 26).
4. **Dump citation [11]** (NASA SVS press release on spiraling supermassive
   black holes): resolves (HTTP 200) but supports nothing about SMBH
   prevalence across galaxy morphology — a clean MISMATCH, not a fabrication,
   but flagged by W2 as a citation that must not be reused for the claim it
   was attached to (`VERIFIED_BIBLIOGRAPHY.md` Quarantined #1; row 34).
5. **The task's own citation pairing error**: "Popławski, Phys. Lett. B 694
   (2010) 181, 'Radial motion into an Einstein–Rosen bridge'" conflates two
   real but distinct Popławski papers — the volume/page belongs to
   arXiv:1007.0587 ("Cosmology with torsion"), and the title belongs to
   arXiv:0902.1994 (actually Phys. Lett. B 687, 110 (2010)). Both underlying
   papers are real and verified; the pairing in the *request itself* was
   wrong. Corrected, not silently substituted (`VERIFIED_BIBLIOGRAPHY.md`
   Quarantined #2; row 17).
6. **Unverified, unfetched sources used as inputs by Popławski's own papers**
   (not fabricated by this campaign, but never independently verified and
   explicitly flagged as such): Beilin et al., Sov. Phys. JETP 51, 1045
   (1980) [his ref. 34, particle-production rate source]; Lord, *Tensors,
   Relativity and Cosmology* (1976) [his ref. 5, escape-condition source];
   Rich, *Fundamentals of Cosmology* (2001) [his ref. 18, thermal-input
   source] — all flagged `[UNVERIFIED]` in `PARENT_CHILD_BOOKKEEPING_MEMO.md`
   §4.2–4.3 and §8, none load-bearing in the reproduction because the
   dependent quantities were independently re-derived or flagged as PAPER
   inputs.
7. **Non-reproducing quantitative claims in the Popławski/Desai–Popławski
   literature** (not hallucinations in the invented-from-nothing sense, but
   documented as non-resolving under independent reproduction, per
   `PARENT_CHILD_BOOKKEEPING_MEMO.md` §7 Part D items 14, 20, 21): the ApJ
   text's `t_infl∝τ(β_cr−β)^(−1)` scaling (reproduces as exponent −0.52±0.02,
   not −1); Desai–Popławski's "about 60 e-folds" (reproduces as 97.9 e-folds;
   the elapsed time matches to 0.1%); Desai–Popławski's Table I bounce counts
   (reproduce as 2,3,4,7,13 against a stated stellar initial condition where
   they print 1,2,3,5,10 against an unstated one).
8. **Zeldovich & Starobinsky 1972** (Sov. Phys. JETP 34, 1159): not a
   hallucination — content is corroborated across 3+ independent secondary
   sources — but no primary APS/ADS bibcode was independently reached this
   session. Flagged lower-confidence, not load-bearing anywhere in this
   ledger (`VERIFIED_BIBLIOGRAPHY.md` Quarantined #3).

No dump citation ([1]–[11]) was fully UNRESOLVED with no recoverable identity;
the worst case is [11] above (item 4), a MISMATCH rather than a broken link.
