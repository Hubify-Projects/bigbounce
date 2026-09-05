# Novelty audit — what is honestly N3-eligible (2026-09-04)

**Asked by Houston (2026-09-04):** "what we can do to get to an N3-level claim …
our contributions are all N2 … Research what's novel here … better labeling of
what type of contribution it is."

**Ladder** (`~/.claude/skills/never-claim-n4/SKILL.md`, canonical):

| Tier | Bar |
|------|-----|
| N1 | Incremental refinement / replication |
| N2 | Novel application or combination |
| N3 | First-of-kind demonstration / new constraint / new direction — **self-claim ceiling** |
| N4 | Paradigm-shifting — **never self-claimed** |

**Method.** For each of 11 candidate contributions: state exactly what is
claimed; find prior work by literature search (arXiv/ADS/INSPIRE, ids cited);
decide whether it is first-of-kind / a new constraint / a new direction; assign
an honest tier with a one-line justification; name the concrete bounded work
that would lift it to N3, or state "nothing — N2 by nature."

**Integrity stance.** Never inflate. A lab's first year producing mostly N2
(novel application/combination) contributions is the normal, healthy case; N3
is earned by being demonstrably *first* at something a referee can check.

**Sections** (filled in below, committed per section):
1. Plan + ladder (this header)
2. Candidates 1–3 — theory/derivation lane
3. Candidates 4–6 — no-go / null-result lane
4. Candidates 7–9 — data lane
5. Candidates 10–11 — method + note lane
6. Summary table (candidate | contribution type | current site tier | honest tier | lift-to-N3)
7. Top-3 nearest-to-N3 with exact work; site labelling recommendation

---

## Section 2 — theory / derivation lane (candidates 1–3)

### C1 — From-scratch in-in confirmation of f_NL = −35/16 and the located ×2 in Cai+2009

**Claimed.** An independent from-scratch in-in computation (independently fixed
commutator/Wick/orbit multiplicities; machinery validated on Maldacena dS and
Namjoo USR 5/2) reproduces the comoving-gauge squeezed matter-contraction
amplitude −35/16, and locates the ×2 in Cai, Xue, Brandenberger & Zhang
(**arXiv:0903.0631**, JCAP 0905:011) to a uniform factor in their amplitude
step, their Eq. (37) being correct monomial-by-monomial. Cross-checked against a
δN/separate-universe route (row 1) and the c_s→1 limit of Li et al.
(**arXiv:1612.02036**, Eq. 4.19), which returns −35/16 exactly.

**Prior art.** The *correct value* is already in the literature: Quintin,
Sherkatghanad, Cai & Brandenberger (**arXiv:1508.04141**) quote −35/16; Li,
Brandenberger et al. (**1612.02036**) reuse Cai's rows rather than recomputing.
The orientation dependence f(μ) = −35/16 + (15/16)μ² is contained in
**1612.02036** Eq. (4.19) at c_s=1 (the lab's own Fable referee leg established
this, commit 66cf1cb0) — so it is a confirmation, not a new result.

**Verdict: N2.** Type = *derivation / verification*. It is a replication by an
independent method that corrects the literature record on a published
coefficient — genuinely valuable, and exactly what "novel combination of
methods" means, but not first-of-kind: the number it confirms was already
published in 2015. Lift to N3: **nothing — N2 by nature.** (A standalone
erratum-style note is publishable and citable; it does not change the tier.)

### C2 — The threading map: δN_c vs ζ in a non-attractor contraction (row 11c)

**Claimed.** The exact map along the fluid worldline
δN_c = ζ − ⅓∫∂_iN^i dt; at linear order δN_c = (1−ε/3)ζ; at second order the gap
to the naive isotropic δN answer is 5ε/3 (linear rescaling) + 5ε(3−ε)/18 (from
the e^{−2ζ} factor in N^i); the in-in −35/16 + (15/16)μ² maps to δN = −5
exactly; the "5ε/4 = pair translation" reading is refuted. Consequence: the
**isotropic separate-universe / δN construction fails at O(1), not O(k²), in a
matter-dominated (non-attractor, ε = 3/2) contraction.**

**Prior art.** The non-attractor consistency-relation violation is Namjoo, Chen
& Sasaki (**arXiv:1211.0083**) and follow-ups; the soft-limit/separate-universe
correspondence is Kenton & Mulryne (**arXiv:1605.03435**) and Dai, Pajer &
Schmidt (conformal Fermi coordinates, **arXiv:1504.00351**); the *breakdown* of
separate universe is established for **inflationary** ultra-slow-roll: Artigas,
Grain & Vennin (**arXiv:2110.11720**), Jackson, Assadullahi, Gow, Koyama, Vennin
& Wands (**arXiv:2311.03281** — failure on a finite range of super-Hubble scales
at a sudden SR→USR transition), and **arXiv:2506.23571** (validity in transient
USR). δN in Bianchi-I is Abolhasani et al. (**arXiv:1302.6986**), where δN and
in-in agree exactly. What is **not** in that literature: the same analysis for a
*contracting* non-attractor background, with an explicit ε-dependent threading
map that reconciles in-in and δN at second order.

**Verdict: N2 today, the strongest N3 candidate in the theory lane.** Type =
*derivation / method*. It is currently an internal reconciliation note
(`research/theory_audit/threading_map_second_order_2026_09_04.md`) tied to one
background. **Lift to N3:** generalise the map to arbitrary constant ε (and
c_s), state the failure condition of isotropic δN as a criterion rather than an
anecdote, demonstrate it on ≥2 backgrounds (dust contraction + ekpyrotic, plus
the USR inflationary case as the known control where the literature answer is
reproduced), and publish as a standalone methods note. That would be a
first-of-kind demonstration ("separate-universe δN fails at O(1) in
non-attractor *contractions*, here is the exact correction") — bounded work,
weeks of symbolic + numerical effort, $0 compute.

### C3 — The T ≤ 1/2 linear transfer bound and the S1/S2 scheme dependence

**Claimed.** (a) Linear transfer of the non-Gaussian amplitude through the
modelled bounces obeys T_fNL = (1−ρ_B)/2 ≤ 1/2. (b) The S2 (effective-fluid MS
variable) "divergence" is a total-derivative pole introduced by the Maldacena
integration-by-parts steps, which use 1/H across H = 0; the raw ADM cubic
Lagrangian is finite on exact S2 modes and gives f_NL^after ≈ −1.25 vs S1's
−0.50 — a factor 2.5 traced to the linear MS-variable choice (|λ_ζ| 0.97 vs
6.06), reported as a scheme band (decision D-A3-9).

**Prior art.** The 1/H-in-the-cubic-action question at a bounce is **already
treated**: Battarra, Koehn, Lehners & Ovrut and, explicitly, *Non-singular
bouncing cosmology: consistency of the effective description*
(**arXiv:1512.03807**) argue the 1/H terms are only *apparent* singularities
(each inverse power multiplies ζ̇, keeping the product finite); non-perturbative
transfer through a bounce is Xue, Garfinkle, Pretorius & Steinhardt
(**arXiv:1308.3044**); linear transfer/ matching is Durrer–Vernizzi,
Allen–Wands and Cai et al. (**arXiv:1106.1416**). The bound T ≤ 1/2 for this
background class and the *quantified* factor-2.5 S1/S2 band are the lab's own.

**Verdict: N2.** Type = *derivation*. The qualitative "the divergence is an IBP
artefact, not physics" is a rediscovery of **1512.03807**'s point in a different
variable; the new content is the quantified scheme band and the explicit bound,
i.e. a novel application of known machinery to a specific background family.
**Lift to N3:** prove (or bound) the scheme dependence *away* — i.e. exhibit a
variable choice that is regular through H = 0 and show the transmitted amplitude
is unique in it, turning "we report a band because the answer is
scheme-dependent" into "the scheme-independent answer is X." That is exactly the
"remaining theory problem" ledger row 9 already names, and it is the single
highest-value bounded theory task the lab has open.
