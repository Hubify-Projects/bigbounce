# Portfolio decision — 2026-09-02 (orchestrator synthesis, on Houston's request to challenge the architecture)

**Inputs:** `PAPER_GENEALOGY_2026-09-02.md` (dated lineage, 2025-07 → today),
`PORTFOLIO_SCIENTIFIC_VALUE_ASSESSMENT_2026-09-02.md` (literature-anchored
per-work verdicts + three literature sub-searches), the March-2026 lab audits
(`research/final_novelty_and_paper_audit/`, `research/remaining_live_paths_audit/`,
`research/project_nextgen_bounce_signals/`), `bounce_portfolio_strategy.md`
(2026-03-24 mission statement), and first-hand checks recorded below.
Facts are cited; judgments are marked as mine.

## 1. How we got here (facts)
- **2025-07:** one paper — spin-torsion dark energy resolving H₀/σ₈, citing a
  JWST spin asymmetry as evidence. **2026-03-17:** the lab's own salvage cut
  about half of it. **2026-03-20/24:** the most vision-aligned lineup we ever
  had — three papers (framework + 14 barriers; ALP birefringence; the f_NL
  forecast as "the decisive test") — and a written mission: *bounce cosmology
  vs inflation via a portfolio of testable channels*, with ranked next
  science: LQC formalism audit, independent f_NL derivation, PBH + induced GW,
  NANOGrav γ=3, chiral GWs from the torsion bounce.
- **2026-04 → 07:** the lineup grew by split and rescue (4 → 5 → 6), not by
  new results. The birefringence paper dissolved into supporting material.
  P3 collapsed from a 268k-object discovery claim to a provenance note. The
  flagship amplitude was corrected −35/8 → −35/16 (halving the signal — the
  scenario the March audit called "weakened but alive"). A merge into one
  58-page paper lasted six days.
- **2026-08-03:** "six papers" declared a residue; three research programs
  adopted. **2026-08-05 → 09-02:** P1C resurrected and driven through 13
  review boards; the anomaly scan re-run under a sealed contract.
- **Drift is monotone** (genealogy §3): every surviving paper claims less
  than its origin, and half the portfolio (P4/P5, anomaly/P3) is DESI
  data-mining with no bounce content by its own admission.
- **Two process errors surfaced today:** (a) `arxiv/main.tex` is a stale
  June monolith (v2.3.18, still −35/8) that this session's P1C reviewer
  prompts cited as "P1A"; the registered P1A is `arxiv/paper1a_ech_nogo.tex`.
  (b) The one genuinely on-vision positive result — the NANOGrav 15-yr
  free-spectrum MCMC, γ = 2.57 ± 0.38 vs the matter-bounce prediction 3
  (Savage–Dickey B ≈ 3.2 for matter bounce over free) — is filed as "P3
  support" and appears in no paper.

## 2. Verdict on the three-program architecture (judgment)
It was an honest filing system and a necessary correction to "six equal
papers," but it is the **wrong publication structure**: it grants program
status to two lines that are not bounce science, and it dilutes the one
line that is. Houston's instinct is right. The structure should follow the
original question, not the inventory.

## 3. The ideal structure: one flagship line, one closed-line note, data products
**Track A — Bounce vs inflation (the vision; the only line that earns the lab's name).**
- **A1 · P2′** — short Letter (≤6 pp, PRD-L/JCAP): the exact matter-contraction
  amplitude f_NL = −35/16, correcting Cai et al. 2009's −35/8. *Gate before
  submission (hardest path first):* an independent second-method derivation
  (Salopek–Bond gradient expansion or δN) that reproduces −35/16 — the March
  #2 item, never done by an independent route; the assessor could not verify
  the factor-2 and neither can a referee without it.
- **A2 · Transmission paper** — nonlinear transmission of f_NL through an
  explicit nonsingular bounce (LQC dressed-metric/hybrid, and one non-LQC
  bounce), turning the contraction coefficient into an observable
  prediction. This is the paper every P2 reviewer asked for and the March #1
  item.
- **A3 · Multi-channel consistency paper** — the portfolio paper the March
  strategy envisioned, redone at −35/16: NANOGrav γ (reclaim the orphaned
  MCMC), PBH abundance (Choudhury+ 2025 at −35/16), and SPHEREx/MegaMapper
  reach. This is where a *positive*, distinctive, near-term test lives.
- **A4 (contingent)** — chiral GWs / birefringence from the torsion bounce
  only if a bounce-specific, distinctive prediction survives the four-question
  gate; the generic ALP birefringence content stays an appendix/dataset (the
  field — Fujita, Obata, Eskilt — already owns the generic result).

**Track B — The closed ECH dark-energy line (service to the community).**
- **B1 · One structural note** — merge P1A into P1C: ≤12 pp, gr-qc/CQG Note,
  "which minimal spin-torsion routes to dark energy are structurally closed,"
  with the transparency theorem as the positive result. Stop the P1C review
  churn now (R10–R13 rejections are about genre and length, not errors); one
  INT board on the merged note, then submit. MCMC companion → Zenodo dataset.
  Stale `arxiv/main.tex` → `arxiv/_retired/`.

**Track C — DESI data products (program-agnostic; say so).**
- **C1 · P4′** — catalog + dipole null, ≤15 pp, P5 folded in as one section
  (a 46-pp post-hoc null no model predicts is not a paper). Framed as
  confirming the independent reanalyses (Iye+, Patel & Desmond), not as
  bounce physics — P1A's own transparency result already kills the
  bounce–chirality link.
- **C2 · Anomaly catalogue (earned, not assumed)** — publishable only if the
  S>8 taxonomy validates real objects with known-object recovery benchmarks
  and closes the loop to at least one confirmed class; otherwise a data
  release with P3 as its provenance layer. Priors: Liang & Melchior 2023,
  the 2025 DESI VAE paper.
- **C3 · namaster-proof** — optional JOSS note.

**Count:** publishable now **2** (P2′ after its derivation gate; P4′);
**1** note (B1); **2 contingent new science papers that ARE the vision**
(A2, A3); **1 contingent data paper** (C2); **1 optional** (C3). The
scientifically valuable *new* work — A2/A3 and the independent derivation —
does not exist yet. That is the honest state.

## 4. What restores the vision (judgment)
Stop spending sessions on review rounds of closed material; spend them on
A1's gate and A2/A3's computations — positive-discovery directions per the
repo's research directive. Keep the review loop as a gate, not a product.

## 5. Decisions taken under delegation (to be executed next session)
1. Adopt the Track A/B/C structure above; retire "three research programs"
   as the public framing (site copy: "flagship line + data products").
2. Freeze P1C at v1C.0.16; merge P1A into it; one INT board; submit.
3. Fold P5 into P4′; retire the MCMC companion to Zenodo; retire
   `arxiv/main.tex`.
4. Reclaim the NANOGrav MCMC into Track A3.
5. Independent second-method f_NL derivation before any P2 submission.
6. INT-only reviews for the next leg (Houston, 2026-09-02).

## Addendum — 2026-09-02, after Houston's response (corrections to §3, adopted)
- **P4′ is on-vision.** The chirality survey was designed to test the
  "universe born in a rotating black hole" claim (Popławski's Einstein–Cartan
  black-hole cosmology; Shamir's JWST rotation-direction result). P4′ is
  therefore framed as **the largest test of that hypothesis's galaxy-spin
  prediction** (null so far), with the model's predicted dipole derived and
  confronted (ledger #5) — not as a detached data product. Scale (8.47M
  galaxies; 27.5M spectra with sealed provenance) and the receipted
  methodology are genuinely new even where the questions are not.
- **The ECH Note is on-vision.** Popławski's bounce is torsion-induced
  spin–spin repulsion in Einstein–Cartan gravity — the contact term P1A/P1C
  derive. The Note is repositioned as "what minimal ECH does for the bounce
  and cannot do for dark energy," bridging Track B to the black-hole-cosmology
  test.
- **The anomaly line is redirected**, not retired: an early-universe anomaly
  map from public data (z>10 massive galaxies, PNG in clustering, isolated
  early SMBHs, asymmetries/voids), each paired with an explicit
  bounce-vs-inflation discriminator (ledger #4, #6, #8). The autoencoder
  catalogue is one instrument of that map, publishable when earned.
- **Publication cadence.** Continuous, never for its own sake. Near-term
  milestone: the first 1–3 genuinely valuable papers out soon. Fastest
  honest candidates: (i) P4′ (condensed, model-tested null), (ii) the ECH
  Note (P1A+P1C merged), (iii) P2′ once ledger #1 passes.
- **Governance:** directive R added to `CLAUDE.md`; `VISION.md`,
  `NEXT_SCIENCE_LEDGER.md`, and `HUBIFY_RESEARCH_GOVERNANCE_2026-09-02.md`
  created.
