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

---

## Section 3 — no-go / null-result lane (candidates 4–6)

### C4 — Row 14: the joint (r, f_NL) no-go with the 296× disjoint windows

**Claimed.** For a dust contraction with constant scalar sound speed,
r = 16ε c_s = 24 c_s (two independent symbolic routes) and
f_NL^squeezed = −165/16 + 65/(8c_s²). r < 0.036 needs c_s < 1.5e−3, where
f_NL^after ≈ 6e5–9e5 (~10⁵σ over Planck); |f_NL| ≤ 5.1 needs c_s ≥ 0.444, i.e.
r ≥ 10.7. The windows are disjoint by ~296× in c_s. The bounce transfer is
c_s-independent (to 4e−11) and cannot help.

**Prior art.** This *is* Li, Brandenberger et al.'s extended no-go
(**arXiv:1612.02036**, verbatim abstract: "it does not seem possible to suppress
the tensor-to-scalar ratio without amplifying the production of
non-Gaussianities beyond current observational constraints (and vice versa)"),
itself extending Quintin, Sherkatghanad, Cai & Brandenberger
(**arXiv:1508.04141**). Li+2016 states it *qualitatively*, with no numeric
window and at the then-current r < 0.07.

**Verdict: N2.** Type = *derivation / no-go, quantitative strengthening*. The
theorem is not the lab's; what is the lab's is (a) an independent re-derivation
of both legs, (b) the first explicit **numerical** statement of the disjointness
(296× in c_s, a factor 3.8 tighter at r < 0.036), and (c) the demonstration that
the bounce transfer cannot bridge the gap. That is a novel quantification of a
known theorem, not a new direction. **Lift to N3:** nothing on this row alone —
the theorem already exists. The N3-adjacent move is C5 (below): showing the
*standard cure* to the theorem also fails.

### C5 — Row 15: the curvaton matter bounce, and the dilution of the flagship signal

**Claimed.** (i) A light spectator obeys the same MS operator, so n_s = 0.9649
is **inherited** unchanged — a curvaton mass cannot supply it (blue,
n_σ−1 = +8m²/3H²; CXB11's 2m²/3H² is the de Sitter value). (ii) r is free:
r = 24/[1 + (4/3) r_dec²(M_pl/σ_*)²], so r < 0.036 needs only
r_dec M_pl/σ_* > 22.35. (iii) f_NL is O(1) and Planck-compatible; CXB11 Case 1
collapses to the parameter-free −320/π⁴ = −3.29. (iv) **The cure destroys the
signal:** the adiabatic power fraction is exactly r/24, so the intrinsic −35/16
enters weighted by (r/24)² = 1.5e−6 at r = 0.036, giving
f_NL^bounce,eff ≈ 1e−6 — above SPHEREx σ=0.5 only for r ≥ 22.95, the
tensor-excluded branch.

**Prior art.** Cai, Xue & Brandenberger (**arXiv:1101.0822**) introduce the
mechanism qualitatively ("a mechanism for … suppressing the ratio of tensor to
scalar perturbations … new sources of non-Gaussianity"); the standard curvaton
f_NL formula is Lyth–Ungarelli–Wands (**astro-ph/0208055**) and
Sasaki–Väliviita–Wands (**astro-ph/0607627**). The ekpyrotic analogue
("naturally suppressing the intrinsic amount of non-Gaussianity") is known.
What the literature does **not** state, as far as this audit could find: that
in the *matter-bounce* curvaton the intrinsic contraction amplitude is diluted
by exactly (r/24)², i.e. that curing the tensor problem removes the
matter-bounce non-Gaussian signature from observational reach — the closing of
the last single-field-adjacent escape route from the C4 no-go.

**Verdict: N2 now, N3-eligible with bounded work.** Type = *derivation / null
result*. Point (iv) is a genuinely new structural statement and, combined with
C4, constitutes a **new constraint on a model class**: "no single-field or
matter-bounce-curvaton realisation is simultaneously CMB-tensor-viable and
observably non-Gaussian." **Lift to N3:** (a) extend the dilution argument
beyond the specific CXB11 conversion to a general spectator-conversion
parametrisation, (b) add the ekpyrotic-contraction branch so the statement
covers the two standard contraction classes rather than one, and (c) publish C4
+ C5 as one no-go paper whose *claim is the closure*, not the amplitude. That is
a first-of-kind negative result about a model class — the lab's clearest,
cheapest N3.

### C6 — The three multi-channel nulls (PTA γ_pred = 5.07; PBH 7-dex deficit; PNG high-z)

**Claimed.** For the lab's own spectrum: γ_pred = 5.035–5.07 with
Ω_GW h² (f_yr) = 1.7e−14, ~10^5.3 below NANOGrav; a PBH deficit with the
compaction-function sign resolved (negative f_NL *suppresses*, Choudhury+2025
correct, the lab's earlier enhancement an IR-divergent cutoff artefact); and a
5–15% *suppression* of the z=10–12 M*>1e10 M⊙ abundance — wrong sign for the
JWST anomaly and 10–30× below its systematic floor.

**Prior art.** Induced GWs and PBHs in non-singular matter bouncing cosmology
are treated directly by **arXiv:2404.03779** (JCAP 2024/06/066), including the
low-frequency Ω_GW ∝ f² slope the lab reproduces; NANOGrav 15 yr is
**arXiv:2306.16213**; the PBH compaction-function f_NL response is
Choudhury et al. **2025**; the high-z abundance response to local PNG is
LoVerde et al. (**arXiv:0711.4126**) Eq. (45).

**Verdict: N2.** Type = *null result / multi-channel consistency test*. Each
individual channel has published prior treatment; the lab's contribution is
applying all three to **one internally consistent spectrum with its own
transmitted amplitude**, and publishing the three as honest nulls. The
sign-resolution of the compaction response (candidate row 11a) is a genuine
correction of the lab's own earlier claim, not of the literature —
Choudhury+2025 was already right. **Lift to N3:** the multi-channel *map* is N2
by nature (combination). The one N3-shaped piece inside it is the
**JWST-anomaly exclusion stated as a constraint**: "a matter bounce with
|f_NL| ≲ 5 cannot explain the z>10 over-massive-galaxy abundance; explaining it
requires |f_NL| ~ 32, excluded by Planck at ~6σ" — that is a *new constraint on
a proposed explanation*, and if written as such (with the systematic floor
budget), it is defensibly N3. Bounded work: one short note, $0 compute.
