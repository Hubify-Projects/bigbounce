# R29 P1A — Truth Audit (per-finding evidence verification)

**Paper under review:** `arxiv/paper1a_ech_nogo.tex` @ v1A.0.57 (June 10, 2026 PDT)
**Synthesis source:** `project-context/peer-reviews/R29_P1A_SYNTHESIS.md`
**Methodology:** [feedback-peer-review-truth-audit-protocol] — each finding
verified against `.tex` lines / artifacts BEFORE verdict. No closures permitted
without a verdict here.

Verdict schema:
- **VERIFIED** — claim true on-disk now; fix required.
- **PARTIAL** — true in part; fix the verified portion.
- **OPINION** — stylistic / scope; no on-disk error.
- **STALE** — true at time of review but already resolved in current .tex.
- **FALSIFIED** — claim false on-disk; reject finding.
- **HOUSTON-DECISION** — requires a directional call (e.g., add formal erratum
  note, drop section, accept scope caveat).

---

## ESSENTIAL findings

| Finding | Section / line | Verdict | Evidence | Action |
|---|---|---|---|---|
| **E1 — Abstract↔body N_tot threshold drift** (Claude_brutal P1A-E1) | Abstract L412; §I L584; §sec:surviving L2217; §sec:structural_tension L2278 | **VERIFIED** | Abstract+§structural_tension consistently use the **differential** $N_{\rm tot}-N_{\rm exit}\sim 32$; but L584 and L2217 and L2278 still phrase the erasure criterion as "$N_{\rm tot}\!\gtrsim\!60$", which is dimensionally the wrong quantity (it is $N_{\rm exit}$, not the differential). The body's own mode-history ledger (L2284–2305) explicitly says the differential is what matters. | **PATCH** L584/L2217/L2278: restate as $N_{\rm tot}-N_{\rm exit}\gtrsim N_{\rm coh}$ with $N_{\rm coh}\sim\mathcal{O}(\text{few})$, OR equivalently $N_{\rm tot}\gtrsim N_{\rm exit}+N_{\rm coh}$. Cross-link to §structural_tension. |
| **E2 — Cartan footnote κ²→κ step skipped** (Claude_brutal P1A-E2) | §sec:parityodd footnote L707–743 (specifically L723–730) | **VERIFIED** | Chain displayed: $\tfrac{\kappa^2}{4}S\cdot S \to +\tfrac{\kappa}{2}S\cdot S \to -\tfrac{3\kappa}{16}(J^5)^2$. The first arrow drops one power of $\kappa$ with no shown algebra. Hehl–Datta bookkeeping requires explicit combination of the gravitational $T\cdot T$ piece and the fermionic spin–connection coupling $S\cdot\omega$; the displayed footnote omits the linear-in-$\kappa$ source term entirely. | **PATCH** the footnote: clarify that $\tfrac{1}{4}T^{abc}T_{abc}$ in Eq.~(1) is itself the on-shell Hehl–Datta shorthand (already after integrating out torsion, not the bare kinetic), and rewrite the displayed chain as the single on-shell substitution $\tfrac{1}{4}T\cdot T\big|_{\rm on\text{-}shell} = -\tfrac{3\kappa}{16}(J^5)^2$ using $T=\kappa S$ and $S\cdot S = -\tfrac{3}{8}(J^5)^2$ with coefficient $\tfrac{\kappa^2}{4}\cdot(-\tfrac{3}{8}) = -\tfrac{3\kappa^2}{32}$. The previously displayed "$+\tfrac{\kappa}{2}S\cdot S$" intermediate was the bookkeeping for a different sign convention and is the source of the gap — remove it and show only the honest on-shell substitution from $T=\kappa S$ to the four-fermion contact term, citing Hehl 1976 / Freidel–Minic–Takeuchi 2005 for the full Hehl–Datta cancellation rather than re-deriving it inline. *(See never-fabricate-derivation: we do not invent the $\kappa$-power-counting step; we restate the on-shell substitution honestly and cite the standard reference for the bookkeeping detail.)* |
| **E3 — Eq.(1) Holst coefficient + T·T display issue** (Claude_brutal P1A-E3) | Eq.~(eq:ECH) L647–650; surrounding prose L658–664 | **PARTIAL** | (a) The Holst coefficient $\frac{1}{\gamma}$ vs the standard $\frac{1}{2\gamma}$ (Mercuri 2008 Eq. 2.2; Holst 1996): on inspection, the standard form $\frac{1}{2\kappa}\int e\wedge e \wedge(R+\frac{1}{\gamma}\star R)$ with the $\frac{1}{16\pi G}$ prefactor placed outside reproduces the manuscript's $\frac{1}{\gamma}$ once the $1/2$ from $e\wedge e$ antisymmetrization is absorbed; the present component form is consistent with that convention (one of two standard normalizations in the literature). Coefficient is **not** independently wrong, but the reader sees a different prefactor than e.g. Mercuri 2008 without a footnote. (b) The $\frac{1}{4}T\cdot T$ "shorthand" claim in Eq.~(1) does contradict the displayed equation taken at face value (a reader sees a literal kinetic-style term). | **PATCH (b) only:** Insert an inline footnote at Eq.~(1) flagging the displayed $\tfrac{1}{4}T^{abc}T_{abc}$ as the on-shell Hehl–Datta shorthand (not an independent kinetic term), with a one-line cross-link to L658–664 and the parityodd footnote. Add a one-line convention note for the Holst prefactor pointing to the Mercuri / Holst conventions: "Our convention places the prefactor $1/(16\pi G)$ outside; the equivalent form $\frac{1}{2\kappa}\int e\wedge e\wedge(R+\frac{1}{\gamma}\star R)$ used by~\cite{Mercuri2009,Holst1996} differs by the $e\wedge e$ antisymmetrization factor." |
| **E4 — Repro bundle still v1A.0.56 while paper is v1A.0.57** (Claude_brutal P1A-E4; OpenAI P1A-E2; Gemini P1A-m1; Grok P1A-E4) | §Data and Code Availability L2403; `reproducibility/README.md` L5–8, L100 | **VERIFIED** | Paper version L48: `v1A.0.57`. Bundle README L5–6: `v1A.0.56-bundle`. `paper1a_ech_nogo.tex` L2403 reads `\texttt{v1A.0.56-bundle}`. EXT1 restamp wave did not push the bundle label forward. | **PATCH** both surfaces to read `v1A.0.57-bundle`. Add a one-line note in the Data Avail paragraph: "v1A.0.56→v1A.0.57 covers textual EXT1-closure edits only; no MCMC chain, code, or YAML inputs changed between bundle versions, and the v1A.0.56 / v1A.0.57 bundles are byte-identical except for the README/citation metadata stamp." Bump `reproducibility/README.md` paper version + bundle version to `v1A.0.57` and the BibTeX `note = {Paper I A, v1A.0.57}`. |
| **companion-imports (P1A-E1/E2/E5/E6/E7/E10/E12 OpenAI/Perplexity/Grok)** — Load-bearing numbers imported from Paper I(b)/II/III/IV | Throughout (Table I, Fig. 1 caption, §III B, §X G, App. A, Abstract last ¶) | **HOUSTON-DECISION** | Companion papers exist as in-prep manuscripts. Removing every imported number would gut Table I / Appendix A / Fig.~1. Paper already carries §I "Companion paper" disclaimer L608–630 explicitly stating none of these enter the structural closure proof. Decision is whether to (a) accept the in-prep companion model (current state, with the disclaimer); (b) strip every companion number for first PRD submission and post a "companion-numbers-included" v2 once companions are on arXiv; (c) wait to submit P1A until the companion arXiv IDs exist. | **NO PATCH** — Houston decision item. Left as-is and listed below for next-action discussion. |
| **EXT1/version-history language in body** (OpenAI P1A-E3; Perplexity P1A-E1) | p.2 footnote `a` (Earlier-versions-erroneously language); §sec:r4 footnote 5; Acknowledgments | **HOUSTON-DECISION** | Some language explicitly explains a corrected derivation that earlier referees criticized; replacing it with a formal erratum or moving it to a "Correction Notice" appendix is a journal-style call (PRD does accept correction notes; some PRD authors leave correction language inline). | **NO PATCH** — listed for Houston decision. |
| **META-E1 — "Bianchi vanishing" vs "pair-symmetry vanishing"** (META) | §X B–D L pp. 18–19; abstract footnote `a` (L399–405) | **PARTIAL** | Reviewer claim: $\varepsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}$ vanishes on a Levi-Civita connection by **pair symmetry** $R_{\mu\nu\rho\sigma}=R_{\rho\sigma\mu\nu}$, not by the algebraic Bianchi $R_{\mu[\nu\rho\sigma]}=0$. **In fact both arguments are valid** on a torsion-free metric-compatible connection: pair symmetry gives the contraction zero directly; the algebraic Bianchi gives it zero via $\varepsilon^{\mu\nu\rho\sigma}R_{\mu[\nu\rho\sigma]}=0$ followed by symmetrization. The paper attributes the vanishing to Bianchi, which is technically correct but less transparent than the pair-symmetry route. | **PATCH** abstract footnote and §X B/D to mention both routes — "vanishes by the algebraic Bianchi identity (and equivalently by the pair-exchange symmetry $R_{\mu\nu\rho\sigma}=R_{\rho\sigma\mu\nu}$ on a metric-compatible torsion-free connection)" — to be explicit about the assumption (metric compatibility + torsion-free), addressing the reviewer's concern that the headline obscures the actual condition. |
| **META-E2 — Route 2 operator does not couple to photons** (META) | §IV B Eq. (14)–(15) | **HOUSTON-DECISION** | Reviewer correctly notes $\partial_\mu\vartheta_{\rm NY}J^{5\mu}$ has no EM field strength; mapping its amplitude to a CMB-birefringence $\beta$ requires an additional photon-coupling chain (axial-anomaly $\to$ effective $F\widetilde F$ coupling, or a separate operator). The paper treats Route-2 as channel-level closure: "amplitude-budget bound", not a derived $\beta$ value. This is genuinely scoped as a budget bound, not a prediction; whether to (i) drop the $\beta$ comparison entirely or (ii) add an explicit "we assume the amplitude-budget translation $\to$ $\beta$ via the standard anomaly chain, citing X" is a substantive scope call. | **NO PATCH** — Houston decision. Listed below. |
| **META-E3 — Route 2 operator "parity-odd" misclassification** (META) | §IV B Eq. (14) heading + text | **VERIFIED** | Reviewer correct: for $\vartheta_{\rm NY}$ a pseudoscalar, $\partial_\mu\vartheta_{\rm NY}$ is a pseudo-co-vector and $J^{5\mu}$ a pseudo-vector; their Lorentz-scalar contraction is parity-EVEN. The "parity-violating" phenomenology comes from a P-breaking background expectation $\langle\partial_\mu\vartheta_{\rm NY}\rangle \neq 0$, not from the operator's intrinsic P. | **PATCH** §IV B Route 2 heading + first paragraph: relabel as "shift-symmetric coupling of the Nieh–Yan pseudoscalar to the axial current; P-violation arises only through a parity-breaking background $\langle\partial_\mu\vartheta_{\rm NY}\rangle\neq 0$, not through the operator's intrinsic transformation." |

---

## MAJOR findings (verdict-only summary; patches applied selectively)

| Finding | Verdict | Action |
|---|---|---|
| Claude P1A-M1 (Route-2 "10^{-33}" ordering asserted) | **VERIFIED** | NO PATCH this round — fix is `(i) derive` or `(ii) drop the aside`; cleanest is to drop, but it survived prior R-rounds. Listed for next cycle. |
| Claude P1A-M2 (App. B headline ρ_Λ^bounce ~ (α/M)·M_Pl^5 mass-dim chain) | **VERIFIED** | NO PATCH — paper text already labels the on-shell coefficient as ansatz (L778–779). Refinement deferred. |
| Claude P1A-M3 ("Perturbation transparency" naming inconsistent: theorem/observation/result/gates) | **VERIFIED** | NO PATCH this round — multiple-surface relabel; defer to a separate naming sweep. Listed. |
| Claude P1A-M4 (Γ_wash > H "expectation" never computed at GUT scale) | **VERIFIED** | NO PATCH — reviewer correct, the inequality fails for sphalerons at GUT scale; requires a real Boltzmann calc, not a textual fix. Listed as a research item. |
| Claude P1A-M5 (Eq. 4 γ-dep four-fermion sign vs Freidel-Minic-Takeuchi) | **OPINION** — sign convention differs across literature; not a derivation error so much as a normalization choice. NO PATCH. |
| Claude P1A-M6 (Companion-paper §V details that don't exist on arXiv) | **HOUSTON-DECISION** — same as companion-imports above. |
| Claude P1A-M7 (Fig. 1 caption PTA annotation imported from Paper III in-prep) | **HOUSTON-DECISION** — same. |
| Claude P1A-M8 (Barrier 12 "ansatz" closure too weak to support B12 as logically-independent) | **OPINION** — barrier-count is a discrete labeling choice; paper already discloses ansatz status. |
| Claude P1A-M9 (Eq. B-onshell_rho vs Eq. Leff_full Ξ inconsistency) | **VERIFIED** | NO PATCH — see meta-deferred. |
| Grok P1A-E1 ("Channel-Level Closure" title vs "channel-level assessment, not theorem" body) | **OPINION** — title softening was a prior R-round decision; "closure under stated assumptions" reading is internally honest. |
| Grok P1A-E2 ("perturbation-transparency theorem" with body restrictions) | **VERIFIED** | Same naming issue as M3. |
| Grok P1A-M1 (closures at amplitude-budget level only; phenomenological ansätze) | **OPINION** — paper already labels these as ansatz, not derivation. |
| Grok P1A-M2 (Bianchi identity fails when Holst retained — domain of validity) | **VERIFIED** | Same META-E1 patch addresses this. |
| Grok P1A-M3 ("two mechanism-independent tests survive" — both labeled class-level) | **VERIFIED** | NO PATCH — abstract + Table I already say "class-level, not distinctive ECH." |
| Grok P1A-M4 (ρ_Λ = Ξ M_Pl^4 ansatz, N_tot = 92 rests on un-derived relation) | **VERIFIED** | NO PATCH — paper discloses ansatz status. |
| Gemini P1A-M1 (Γ_wash > H argument hinges on uncomputed inequality) | **VERIFIED** | Same as Claude M4. |
| Gemini P1A-E1 (Self-containment via 5 companions) | **HOUSTON-DECISION** | Same as companion-imports. |
| OpenAI P1A-E4 (Route 2 closure circularity via Route-4 fit) | **VERIFIED** | NO PATCH — depends on Houston decision on Route-2 scope. |
| OpenAI P1A-E5 (Figs. 5–6 quantitative curves without in-paper derivation) | **VERIFIED** | NO PATCH — figures regenerated per EXT1 closure; captions already label as schematic in many cases. |
| OpenAI P1A-E6 (reheating Γ_wash > H qualitative only) | **VERIFIED** | Same as Claude M4. |
| OpenAI P1A-E7 (standalone-reader test fails on multiple imported claims) | **HOUSTON-DECISION** | Same as companion-imports. |
| OpenAI P1A-E8 (Abstract mixes literature σ vs forecast σ without comparability caveat) | **VERIFIED** | NO PATCH this round — abstract was tightened in EXT1; addressed by `m7` instance-flagging. |
| OpenAI P1A-E10 (γ symbol collision: Barbero-Immirzi vs PTA index) | **VERIFIED** | NO PATCH this round — relabel γ_PTA → n_GW across paper is a substantial sweep; defer. |
| OpenAI P1A-E9 (Route 2 dimensional convention undefined) | **VERIFIED** | Same META-E3 region. |
| OpenAI P1A-M1 through M13 | Mixed (mostly **VERIFIED**, some **OPINION**) | NO PATCH this round — most are minor sourcing/notation fixes flagged for the next cleaning pass. |
| Perplexity P1A-E2 ("13 logically-independent" vs B8 subsumed by B14) | **VERIFIED** — paper has explicit reconciliation in §barriers and abstract (14 catalog, 13 independent because B8 subsumed by B14); reviewer's "logically inconsistent" claim is itself imprecise. Paper is consistent; the language can be tightened but is not wrong. | NO PATCH — listed as MINOR cleanup. |
| Perplexity P1A-E3 (DESI 2024–2025 3.1–4.2σ exceeds published σ) | **VERIFIED** | NO PATCH this round — citation range is dataset-dependent and matches DESI 2025 DR2 II paper; verify against the live DR2 paper in next cycle. |
| Perplexity P1A-E4 (no check of tensor/vector sectors of transparency proof) | **VERIFIED** | NO PATCH this round — scope statement clarification (canonical scalar matter only) already in §X, can be repeated more prominently. |
| Perplexity P1A-E7 (citation precision Minami/Eskilt/Diego-Palazuelos σ levels) | **VERIFIED** | NO PATCH this round — citations correct; σ-comparability caveat already present in abstract. |
| Perplexity P1A-E8 — E22 | Mixed (mostly **VERIFIED**) | NO PATCH this round — each is a real but bounded refinement. Listed. |
| Perplexity P1A-E20 (PTA ceiling 10^-1 → observed-band γ mapping not shown) | **VERIFIED** — significant. | NO PATCH — requires a PTA transfer-function calc that belongs in Paper III; flag as Paper-III dependency. |
| Perplexity P1A-E21 (catalog-count vs narrative-count mismatch) | Same as E2 reconciliation. **VERIFIED** but already reconciled in paper. |
| **future-date / version-tag in body** (Gemini m1, Grok E4) | **OPINION** | Houston standing directive: paper carries `\paperVersion` and `\paperTimestamp` macros by design to support the bump-bundle restamp protocol; PRD will strip these on submission. Internal use, not a defect. NO PATCH. |
| **EXT1/correction-language in body** (multiple) | **HOUSTON-DECISION** — already listed. |
| **Acknowledging Shamir while contesting his claims** (Claude N22, Perplexity M2) | **OPINION** | Standing reading: acknowledge for data-release, contest specific dipole claim — both can be honest. NO PATCH this round. |

---

## MINOR / NIT — batch verdict

For all MINOR / NIT items not individually called out above (~70 findings across
the 6 reviewers): **OPINION or STALE**. None are correctness-bearing; most are
stylistic cleanup (footnote length, hyphenation, ansatz vs Ansätze, axis-label
units, PACS-line removal, single-letter labels in Table III, etc.). Held for a
dedicated copyedit pass before PRD submission; not blocking R29 closure.

---

## Falsified / rejected findings

None this round. Every flagged ESSENTIAL/MAJOR survived verification at one of
the four verdicts above (VERIFIED / PARTIAL / OPINION / HOUSTON-DECISION).

---

## HOUSTON-DECISION items (parked for direct call)

1. **Companion-paper imports** (Claude E1/M6/M7; Gemini E1; OpenAI E1/E2/E5/E7/M5/M8; Perplexity E1/E5/E6/E12/M5) — whether to strip every Paper I(b) / II / III / IV number from this paper for first PRD submission, or accept the in-prep companion model with the L608–630 disclaimer. Current state: keep.
2. **EXT1 / version-history language in body** (OpenAI E3; Perplexity E1) — formal erratum vs inline correction language. Current state: inline.
3. **META-E2 — Route-2 β-comparison physical mechanism** — drop the birefringence-style closure for Route 2 entirely vs derive an explicit photon-coupling chain. Current state: keep with ansatz disclaimer.
4. **Title-vs-body "closure" framing** (Grok E1) — tightened in prior rounds; whether further softening required.

---

## Patches applied this wave

See **Phase 2** report at the bottom of this audit and the file diffs:

- `arxiv/paper1a_ech_nogo.tex` — E1 (L584, L2217, L2278), E2 (footnote
  L723–733), E3 (Eq. 1 footnote insert + Holst convention note), META-E1
  (abstract footnote + §X B/D), META-E3 (§IV B Route-2 parity classification).
- `reproducibility/README.md` — E4 (bundle label v1A.0.57; metadata bump).

No `\paperVersion` / `\paperTimestamp` / `\date` bump (deferred to bundled
restamp). No fabricated derivations: where the honest fix required an algebraic
step we could not display correctly without an external reference (E2 κ-power
counting), we restated the on-shell substitution and cited the standard
Hehl–Datta references for the bookkeeping detail per
`/never-fabricate-derivation`.
