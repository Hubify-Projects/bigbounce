# arXiv endorser outreach — 2026-09-02 lineup (refresh of ENDORSER_SHORTLIST_2026-07-22 / ENDORSEMENT_REQUEST_DRAFTS_2026-07-24)

## CLICK-LIST (ordered) — everything Houston must click/send, nothing agent-doable left

**Refreshed 2026-09-02** against the final manuscripts (P4′ v4P.0.5, ECH
Note v1N.0.5 — both APPROVE at agent gates, readiness 95; P2′ DEFERRED, its
content lives in the not-yet-reviewable A3 paper). Both abstracts were
trimmed 2026-09-02 (final-review REVISE) to satisfy their venue word caps —
presentation-only, no science change.

1. **Mint the Zenodo new-version DOI for the ECH Note** (P1C survey +
   theory-audit artifacts) via the Zenodo UI "New version" on the published
   P1A record (`10.5281/zenodo.21481838`), then run
   `tools/zenodo_deposit.py --deposition-id <new draft id>` per
   `PORTAL_KITS_2026-09-02.md` §5a. Insert the resulting DOI link into the
   ECH Note endorsement email template (§1 below) in place of the
   `[DOI/PDF link]` placeholder.
2. **Mint the Zenodo new-version DOI for P5** (folded into P4′) via the
   Zenodo UI "New version" on the published P4 record
   (`10.5281/zenodo.21461899`), then run `tools/zenodo_deposit.py
   --deposition-id <new draft id>` per `PORTAL_KITS_2026-09-02.md` §5a.
   Insert the resulting DOI link into the P4′ endorsement email template
   (§2 below).
3. **Send the ECH Note endorsement emails first** (§1 below): Popławski,
   then Iosifidis or Agullo in parallel — from Houston's own mail client,
   subject/body as drafted, DOI link from step 1 pasted in.
4. **Send the P4′ endorsement emails second** (§2 below): Desmond first,
   then Smethurst — from Houston's own mail client, DOI link from step 2
   pasted in.
5. **Do NOT send any P2′-framed email** (§3 is archived/deferred). **Do NOT
   send any A3 email yet** (§3a) — A3's PBH compaction-function row and its
   pending INT board must close first; this file will be refreshed with a
   go-ahead when that happens.
6. Once each endorsement clears and arXiv admin confirms submission
   eligibility, proceed to the portal-kit click-list in
   `PORTAL_KITS_2026-09-02.md`.

---

**Why this file exists.** The 2026-09-02 portfolio decision
(`project-context/PORTFOLIO_DECISION_2026-09-02.md` + Addendum, `INTENT.md`)
retired "six equal papers" for Track A/B/C. Three works are now the near-term
submission set: the **ECH Note** (P1A merged into P1C), **P4′** (P5 folded
in), and **P2′ Letter**. The four arXiv codes Houston already generated are
unchanged — they clear by **archive**, not by paper title, so the 2026-07-22
eligibility facts and the 2026-07-24 confirmed addresses below are reused
verbatim, not re-verified from scratch (arXiv eligibility rarely changes
inside 6 weeks; anyone who wants a harder re-check should re-open
`arxiv.org/auth/show-endorsers/<paper>` before sending). What changed here:
the draft framing per paper (ECH Note / P4′ / P2′ language, not the old P1A/
P1B/P2/P3/P4/P5 six-way framing) and confidence labels per person, tightened
to the archive they'd actually be asked to clear now.

**Codes:** gr-qc `HYEJ7S` (ECH Note) · astro-ph.IM `L8TIPN` (retained,
secondary — not the active route for any of the three near-term works) ·
astro-ph.CO `LRZHC4` (P2′; ECH Note cross-list) · astro-ph.GA `CLVMAQ` (P4′;
cross-list astro-ph.CO covered by the same person if they also clear
`LRZHC4`).

**Integrity boundary — unchanged.** Endorsement asks are scientist-to-
scientist. No agent contacts an endorser. Houston sends every email himself,
from his own mail client, under his own name. Nothing below has been sent.

---

## 1. ECH Note — gr-qc `HYEJ7S` (cross-list astro-ph.CO `LRZHC4`)

**FINAL manuscript** (`arxiv/paper1bc_ech_note/main.tex`, v1N.0.5,
2026-09-02, ApproveD at agent gates, readiness 95): title **"What Minimal
Einstein–Cartan Torsion Does for the Bounce and Cannot Do for Dark Energy."**
Tarball `SSOT/arxiv_tarballs/paper1bc_ech_note_arxiv_v1N.0.5.tar.gz` sha256
`26f215d6…`; residual before submission: no Zenodo DOI yet for the P1C
survey / theory-audit artifacts (mint a new version under the P1A concept
DOI `21481837` — click-list item below).

> FINAL abstract (v1N.0.5, trimmed to 298 words for the 300-word cap —
> verbatim from the compiled manuscript; no science change from v1N.0.4,
> presentation-only trim):
> Popławski's Einstein–Cartan black-hole cosmology replaces the classical
> singularity with a torsion-supported bounce: eliminating the
> non-propagating spin connection from the minimal Einstein–Cartan–Holst
> (ECH) action generates a spin–spin four-fermion contact term that, in
> the Einstein–Cartan limit γ→∞, reduces to the Hehl–Datta term underlying
> that bounce mechanism. We ask whether the same mechanism can also
> source late-time dark-energy density and answer, systematically, no.
> We (i) derive the minimal axial–axial contact interaction
> −(3κ/16)[γ²/(1+γ²)]J₅², show its direct-channel, hard-cutoff,
> mean-field NJL scalar projection is repulsive,
> G_s = −(3κ/16)[γ²/(1+γ²)], so the gap equation for this condensate
> channel has no nonzero solution; (ii) prove a perturbation-transparency
> theorem: torsion vanishes at every classical perturbation order and the
> Holst sector decouples identically via the algebraic Bianchi identity;
> and (iii) catalog fourteen mechanism-class constraints — two derived
> here, the rest argued or self-labelled heuristics — jointly bounding
> four channels (NJL contact, one-loop Holst correction, Immirzi running,
> parity-odd CMB coupling) by which minimal ECH could connect bounce-scale
> torsion to a late-time Λ-like density, rebutting Popławski's own
> proposed mechanism. A six-member generating list of dimension-four,
> rule-admitted local densities (mixed parity, five distinct densities at
> rank four) is either an exact total derivative on the torsion-free
> branch, a Fierz-closed M_Pl⁻²-suppressed contact term on-shell, or
> identically vanishing; the on-shell trace-vector irrep is the larger
> contribution (β/α = 1/(2γ) ≃ 2.11 at benchmark γ=0.2375), the tensor
> irrep vanishing identically. The result is a structural dichotomy: the
> same contact term supplying Popławski's bounce mechanism as γ→∞ is, at
> finite physical γ, parity-even, Planck-suppressed, and classically
> transparent to perturbations — unable to generate late-time
> acceleration. No ECH dark-energy or birefringence prediction is made;
> this is a channel-level, not operator-level, closure.

### Endorsers (2 needed max; several submissions in gr-qc in the last 5 years required by arXiv rule)

**Superseded note:** the table below replaces the 2026-07-22 gr-qc shortlist
with a 2026-09-02 verification pass checked against current primary-category
gr-qc arXiv submission counts (2021–2026) plus a second API-corroboration
pass. **Robert Brandenberger is downgraded off the gr-qc list**: the 2026-09-02
count found **zero** gr-qc-primary submissions from him since 2021 (his
matter-bounce work files as astro-ph.CO/hep-th-primary) — he remains a
strong astro-ph.CO ask (§3 below) but is not a safe gr-qc endorser choice
despite the 2026-07-22 shortlist listing him there; that entry is now
believed stale. Counts are primary-category floors (cross-lists add more).

| # | Name / affiliation | gr-qc eligibility evidence | Contact | Confidence |
|---|---|---|---|---|
| 1 | **Nikodem J. Popławski** (Univ. of New Haven) | 7 gr-qc-primary since 2021 (2509.11468, 2501.06631, 2211.03234, 2101.04212, +3 more). Author of the Einstein–Cartan spin-torsion "universe in a black hole" program the ECH Note and P4′ both directly engage. Strongest single gr-qc ask — the paper is literally about the mechanism his cosmology depends on. | `NPoplawski@newhaven.edu` — **CONFIRMED** (newhaven.edu faculty profile, verified 2026-09-02). | **High/High.** |
| 2 | **Damianos Iosifidis** (Scuola Superiore Meridionale & INFN Napoli) | ≥7 gr-qc-primary (2608.07386, 2506.04738, 2604.03343, +more). Holst-action / Nieh–Yan torsion-sector specialist — directly on the ECH Note's algebraic-torsion-elimination content. | `d.iosifidis@ssmeridionale.it` — **CONFIRMED** (read from arXiv:2510.01777 HTML header, verified 2026-09-02). | **High/High.** |
| 3 | **Jérôme Quintin** (ÉTS / McGill) | gr-qc submissions 2503.19955, 2403.15205, 2109.11701 (API-corroborated count: 4 gr-qc-primary). NEC-violation / bounce-construction theorist; also the co-author of the general-c_s formula P2′ cross-checks against — a genuine dual-paper contact (list him for both this Note and P2′, §3, if convenient). | `jquintin@physics.mcgill.ca` — **CONFIRMED** (jerome-quintin.github.io/about, verified 2026-09-02). | **High/High.** |
| 4 | **Edward Wilson-Ewing** (Univ. of New Brunswick) | 13 gr-qc-primary (API-corroborated), incl. 2604.06480, 2408.16533, 2301.10215. LQC bounce specialist — the Wilson-Ewing nonsingular-transition construction P2′'s own transmission caveat cites by name. | `edward.wilson-ewing@unb.ca` — **UNCONFIRMED** (sourced from a CAP lecture listing; his UNB page 404'd). Verify via a recent PDF corresponding-author line before sending. | High eligibility, Medium address. |
| 5 | **Ivan Agullo** (Louisiana State) | 15 gr-qc-primary (API-corroborated), incl. 2512.18354, 2511.17382, 2409.16366. LQC / Einstein-Cartan bounce phenomenology, high submission cadence. | `agullo@lsu.edu` — **CONFIRMED** (LSU physics faculty page, verified 2026-09-02). | **High/High.** |
| 6 | **Christian Böhmer** (UCL Mathematics) | gr-qc 2605.18203, 2605.14479, 2507.00503 — Einstein–Cartan cosmology specifically. | `c.boehmer@ucl.ac.uk` — **UNCONFIRMED** (sourced from profiles.ucl.ac.uk/7350; verify via a recent PDF). | High eligibility, Medium address. |

**Backups (Medium confidence, thinner or unconfirmed-contact record):**
Parampreet Singh (LSU; gr-qc 2603.18175, 2505.14784, 2502.09718, 2501.09151 —
no email collected); Simone Speziale (CPT Marseille; 8 gr-qc-primary since
2021 incl. 2508.21817, 2409.06698, 2405.08808 — Holst/first-order-gravity
expert, no email collected).

**Explicitly NOT gr-qc-eligible — do not send `HYEJ7S` to these:** Robert
Brandenberger (zero gr-qc-primary submissions since 2021; use astro-ph.CO
`LRZHC4` instead, §3); Fabio Bombacigno (only 1 gr-qc-primary submission —
below the "several" bar).

**Recommendation:** send **Popławski first** (exact topical match — the Note
explains what does and doesn't work for the mechanism his own cosmology
program depends on) and **Iosifidis or Agullo** in parallel (both
confirmed address + eligibility). Quintin is attractive as a dual-purpose
contact if a single person clearing both the Note and P2′ is preferred. Do
not send `HYEJ7S` to Brandenberger under this framing — send him `LRZHC4`
instead (§3).

### Draft email (send from Houston's own account; DO NOT SEND until manuscript is merged/compiled)

**Subject:** `arXiv endorsement request — Einstein–Cartan–Holst structural no-go (gr-qc)`

> Dear Professor ⟨Name⟩,
>
> I'm an independent researcher in Los Angeles — unaffiliated, single-author —
> asking whether you'd be willing to endorse me to submit to gr-qc.
>
> The paper is a structural transparency theorem inside minimal
> Einstein–Cartan–Holst gravity: it shows what the standard torsion-elimination
> algebra does and does not deliver for late-time dark energy, closing four
> candidate routes (amplitude-budget arguments against the observed
> birefringence amplitude and the observed dark-energy density, among others)
> without excluding Einstein–Cartan torsion as a bounce mechanism more
> generally. [If sending to Popławski: I'd be glad to hear where you think
> the catalog under- or over-states a route relevant to your own
> spin–spin-repulsion cosmology.]
>
> [DOI/PDF link — insert once the merged manuscript compiles; do not send
> without it.]
>
> Endorsing is a short form at arxiv.org/auth/endorse with the code in the
> forwarded message below — arXiv states it attests only that I'm a
> legitimate researcher in the area, not support for the results.
>
> With thanks for your time,
> Houston Golden
> Independent Researcher, Los Angeles, California
> houston@hubify.com · ORCID 0009-0008-5616-5994

**Gate before sending:** the manuscript now exists and compiles clean
(v1N.0.5, APPROVE at agent gates, readiness 95) — insert the final PDF/DOI
link once the Zenodo new-version mint completes (click-list item below);
do not send with the `[DOI/PDF link]` placeholder still in place.

---

## 2. P4′ — astro-ph.GA `CLVMAQ` (cross-list astro-ph.CO `LRZHC4`)

**FINAL manuscript** (`pipelines/p4prime_chirality_test/paper/main.tex`,
v4P.0.5, 2026-09-02, APPROVE at agent gates, readiness 95; P5 folded in as
the void-environment cross-check section per Track C1): title **"The
Largest Test of a Preferred Galaxy-Spin Axis: An 8.47-Million-Galaxy DESI
Chirality Catalog, a Void-Environment Contrast, and a Sensitivity
Confrontation with the Rotating-Black-Hole-Universe Prediction."** Tarball
`SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.5.tar.gz` sha256
`fbab0380…`; residual before submission: P5 has no Zenodo DOI (mint a new
version under the P4 concept DOI `21461898` or as its own record — click-list
item below).

> FINAL abstract (v4P.0.5, trimmed to the ApJS 250-word single-paragraph
> cap — 246 words, verbatim from the compiled manuscript; no science
> change from v4P.0.4, presentation-only trim):
> Two literatures motivate a search for a preferred axis in galaxy spin
> directions: handedness-dipole claims from Longo and from Shamir, and
> Popławski's rotating black-hole-universe model, in which Einstein-Cartan
> torsion halts a collapsing black hole's singularity, bouncing into a
> daughter universe that inherits a preferred axis from the parent's spin,
> toward which galaxies are predicted to align. We report the largest test
> of that claim to date: an 8,474,531-galaxy DESI Legacy DR8 chirality
> catalog and two independent null tests. The primary, quality-controlled
> real-space dipole (N_support=887,472 of 890,069 rows) is null-consistent
> (z_mom=+0.635, one-sided p=0.238), with a 95% sensitivity floor
> A₉₅^obs≃0.98% (Neyman 95% CL limit A₉₅^CL≃0.75%, the floor used below).
> A companion DESIVAST void/non-void contrast on 145,766 classifier-labelled
> galaxies likewise finds no significant effect (ΔfCW=+0.00145, two-sided
> p=0.66). We derive the model's spin-axis-dipole implication; the cited
> mechanism papers give only a qualitative tendency, not a computed
> amplitude, so under the minimal closure needed to quantify the claim, our
> floor disfavors a dipole above ~1% at ≥95% power, 2–20× below the
> ~2–33% literature amplitudes, though under an illustrative,
> not-adopted-for-strengthening bridge the two largest comparison samples
> drop below this floor. This null is measured on 887,472 primary-channel
> spirals, 4–3,400× larger than every comparison catalog except Shamir's
> DESI Legacy sample (N=1.3 million), and confirms independent reanalyses
> by Iye et al. and Patel & Desmond finding no significant galaxy-spin
> anisotropy.

### Endorsers (astro-ph.GA; several submissions in astro-ph.GA in the last 5 years required)

**Superseded note:** the table below replaces the 2026-07-22 GA shortlist
(Shamir/Martini/Elbers/Suárez-Pérez) with a fresh 2026-09-02 verification
pass specifically checked against current (2025–2026) primary-category
astro-ph.GA arXiv submission counts. **Lior Shamir is deliberately excluded
this round** — the 2026-09-02 pass found his spin-direction work files as
astro-ph.CO-primary, not GA, and, more importantly, P4′'s own result is a
**null** that does not confirm his reported asymmetry — asking the person
whose claim your paper fails to reproduce is a materially weaker opening
line than asking someone whose own null result you *do* confirm (Desmond).
Masanori/Michael Iye is also dropped from this GA list: no verified
astro-ph submission found after 2018 (emeritus, inactive on arXiv) — do not
send to him without first finding a live counter-example. Counts below are
**primary-category** GA submissions (cross-lists would add more); emails
marked UNCONFIRMED must be recovered from a recent paper's
corresponding-author footnote or ADS, never guessed from a name pattern.

| # | Name / affiliation | astro-ph.GA eligibility evidence | Contact | Confidence |
|---|---|---|---|---|
| 1 | **Harry Desmond** (ICG, Univ. of Portsmouth) | ≥4 GA-primary submissions 2025–26 (2608.03576, 2605.06659, 2601.07799, 2510.01112). Co-author of **Patel & Desmond 2024**, the exact independent non-detection P4′ now cites as one of the two confirming nulls. Strongest single ask on this list — P4′ confirms his own result. | `Harry.Desmond@port.ac.uk` — **CONFIRMED** (port.ac.uk staff page, verified 2026-09-02). | **High/High.** |
| 2 | **Rebecca Smethurst** (Oxford) | GA-primary 2604.03389, 2603.17778, 2509.22311, 2503.21869 (2025–26). Galaxy Zoo / galaxy-morphology author, directly on-topic for a large-sample chirality catalog. | `rebecca.smethurst@physics.ox.ac.uk` — **CONFIRMED** (physics.ox.ac.uk/our-people/smethurst, verified 2026-09-02). | **High/High.** |
| 3 | **Karen Masters** (Haverford, Galaxy Zoo PI) | GA-primary 2504.00103, 2503.21869, 2503.15310, 2502.03532. Galaxy Zoo PI — as topical an authority as exists for a crowd/ML-labeled chirality catalog. | `klmasters@haverford.edu` (from her own site snippet) — **UNCONFIRMED**, verify against a recent PDF corresponding-author line before sending. | High eligibility, Medium address. |
| 4 | **Brooke Simmons** (Lancaster) | GA-primary 2606.16507, 2603.17778, 2505.01421, 2412.14502. Galaxy Zoo team, morphology-classification methods overlap with P4′'s classifier-injection/retrain controls. | `b.simmons@lancaster.ac.uk` — **UNCONFIRMED** (her page is JS-gated; verify via a recent arXiv PDF). | High eligibility, Medium address. |
| 5 | **Mike Walmsley** (Dunlap Institute, Toronto) | GA-primary 2606.16507, 2603.28208, 2509.22311, 2505.01421 — Galaxy Zoo DESI + Zoobot (the ML morphology-classification pipeline most directly comparable to P4′'s classifier). **Also eligible for astro-ph.IM** (2512.23691, 2512.11957, 2412.02527) — a genuine dual-archive contact if `L8TIPN` is ever needed alongside `CLVMAQ`. | No public email found (personal site `walmsley.dev`, Dunlap directory) — **UNCONFIRMED**, recover from a recent paper's footnote. | High eligibility (both archives), Medium address. |
| 6 | **Tobias Géron** (Toronto) | First-author GA submissions 2505.01421, 2405.05960 — thinner record than the five above; backup only. | No public email found — **MEDIUM** confidence overall (fewer confirmed submissions than the others). | Medium/Low. |

**Recommendation:** send **Desmond first** — the paper's headline framing
now explicitly confirms his own 2024 non-detection, which is the strongest
possible "why I'm writing to you" sentence on this entire outreach effort.
Smethurst second (confirmed address, confirmed eligibility, directly
on-topic). Masters/Simmons/Walmsley as the bench if either is slow; Walmsley
specifically if a dual GA+IM endorser becomes useful. Do not send to Shamir
or Iye under this framing without a fresh, specific reason to reconsider.

**Reference — full DESI-provenance bench carried forward unchanged from
2026-07-22** (still valid as GA/CO/IM-eligible backups, lower topical fit
than the six above since none of them work on chirality/morphology
specifically): Paul Martini (Ohio State, astro-ph + CO/HE/GA/IM/SR),
Violeta Gonzalez-Perez, Claire Lamman, Willem Elbers, John F. Suárez-Pérez.

### Draft email

**Subject:** `arXiv endorsement request — 8.47M-galaxy chirality catalog vs. the rotating-black-hole-universe spin prediction (astro-ph.GA)`

> Dear Professor ⟨Name⟩,
>
> I'm an independent researcher in Los Angeles — unaffiliated, single-author —
> asking whether you'd be willing to endorse me to submit to astro-ph.GA.
>
> The paper releases observed chirality labels for 8,474,531 DESI Legacy DR8
> galaxies and tests the galaxy-spin-axis dipole predicted by the
> rotating-black-hole-universe hypothesis, framing the result explicitly
> against [Iye et al. 2021's / your and Desmond's 2024 / your own
> rotation-direction] independent non-detection: on 890,069
> quality-controlled high-confidence spirals the primary dipole test is
> null (z=+0.635, p=0.238), and a DESI DR1 void/non-void environment
> cross-check is likewise null. This is the largest sample yet applied to
> this specific prediction.
>
> [DOI/PDF link — insert once the P5-folded-into-P4 merge compiles.]
>
> Endorsing is a short form at arxiv.org/auth/endorse with the code below —
> arXiv states it attests only that I'm a legitimate researcher in the area,
> not support for the results.
>
> With thanks,
> Houston Golden
> Independent Researcher, Los Angeles, California
> houston@hubify.com · ORCID 0009-0008-5616-5994

**Gate before sending:** the manuscript now exists and compiles clean
(v4P.0.5, APPROVE at agent gates, readiness 95, P5 folded in) — insert the
final PDF/DOI link once the Zenodo new-version mint for P5 completes
(click-list item below); do not send with the `[DOI/PDF link]` placeholder
still in place. The pre-merge ApJS staging kit
(`pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md`) is superseded by
`PORTAL_KITS_2026-09-02.md` §2 — do not paste its old abstract into an
endorsement email.

---

## 3. P2′ Letter — astro-ph.CO `LRZHC4` (cross-list gr-qc `HYEJ7S`) — **DEFERRED — no submission planned; the astro-ph.CO endorsement will be used for the A3 multi-channel paper instead**

**Status (2026-09-02 final-review recommendation):** P2′
(`arxiv/paper2prime_fnl_letter/main.tex`, v2L.0.2) is an **archived theory
record**, not a submission candidate. The R1 board + truth-audit found the
Letter's −35/16 result is already printed by Li et al. (2016, Eq. 4.19) and
quoted by Quintin et al. (2015); its genuine contribution (independent
from-scratch confirmation, locating the ×2 discrepancy in Cai et al. 2009,
the δN reconciliation) is a confirmation, not a standalone Letter's worth of
new science. This scope decision is recorded in `PAPER_LINEAGE`. **P2′'s
content is now §II–III of the A3 multi-channel paper** (§3a below) — do
**not** send any P2′-framed endorsement email, and do not use codes
`LRZHC4`/`HYEJ7S` under the P2′ framing below. The astro-ph.CO endorsement
ask for these same recipients (Brandenberger, Cai, Meerburg, Chaussidon,
Ferraro, Quintin, Ross, Noriega — table retained below since the eligibility
research is still valid and reusable) is redirected to the **A3 paper**
once it clears its remaining INT board (see §3a).

**Retained below for reference only** — the eligibility/contact research in
the table and the draft framing that follows describes what P2′ *was*; do
not act on it as a live outreach plan.

**Superseded draft framing (archived, condensed from
`research/focused_paper_source_integration/02_full_draft.tex`; P2′ is now
folded into A3, §3a below, not submitted standalone):**

> ARCHIVED draft abstract (P2′, not submitted — superseded by A3 §3a):
> A matter-dominated contracting phase gives a local-type non-Gaussian
> amplitude f_NL^local = −35/16 = −2.1875 before the nonsingular
> transition, correcting the unreproduced printed −35/8 in Cai, Xue,
> Brandenberger & Zhang (2009). We derive the coefficient by re-summing all
> four cubic vertices for the ε=3/2 background, cross-checked against Cai
> et al.'s order-grouped expressions and Li et al.'s general-c_s formula.

### Endorsers (astro-ph.CO; several submissions in astro-ph.CO in the last 5 years required)

**Superseded note:** the table below replaces the 2026-07-22 CO list with a
2026-09-02 verification pass. Both Cai and Brandenberger are confirmed here
with counts and CONFIRMED emails (correcting the 2026-07-22 "unconfirmed
address" status for Cai) — but both are **the authors of the paper whose
printed value P2′ corrects**, so lead with the diplomatic framing already in
the draft below (refinement, not "your paper is wrong"), or open with
Meerburg/Chaussidon/Ferraro/Ross instead if a less loaded first ask is
preferred.

| # | Name / affiliation | astro-ph.CO eligibility evidence | Contact | Confidence |
|---|---|---|---|---|
| 1 | **Robert Brandenberger** (McGill) | 10 of last 15 submissions CO-primary (2607.26174, 2602.16963, 2503.17659). Co-author of arXiv:0903.0631, the paper whose printed −35/8 P2′ does not reproduce. **Not gr-qc-eligible** (see §1) — use `LRZHC4` here, not `HYEJ7S`. | `rhb@hep.physics.mcgill.ca` — **CONFIRMED**. | **High/High.** |
| 2 | **Yi-Fu Cai** (USTC) | ~120 CO-primary submissions — extremely active. Lead/corresponding author of the corrected paper. | `yifucai@ustc.edu.cn` — **CONFIRMED** (read as corresponding-author address off arXiv:2603.13924 HTML, verified 2026-09-02 — supersedes the 2026-07-22/07-24 "unconfirmed" status). | **High/High.** |
| 3 | **P. Daniel Meerburg** (Univ. of Groningen) | CO-primary 2502.11846, 2412.12377, 2303.00916. Primordial non-Gaussianity forecaster — not an author being corrected, a clean topical ask on the PNG-forecast half of P2′. | `p.d.meerburg@rug.nl` — **CONFIRMED** (rug.nl staff page, verified 2026-09-02). | **High/High.** |
| 4 | **Edmond Chaussidon** (LBNL) | CO-primary 2604.05213, 2512.17865, 2411.17623. Runs the DESI f_NL measurement pipeline — directly relevant to P2′'s SPHEREx/DESI-adjacent sensitivity mapping. | `echaussidon@lbl.gov` — **CONFIRMED** (echaussidon.github.io/portfolio, verified 2026-09-02). | **High/High.** |
| 5 | **Simone Ferraro** (LBNL) | CO-primary 2608.11296, 2607.02498, 2604.14327. SPHEREx/DESI PNG lead — the closest topical match to P2′'s SPHEREx-mapping section. | `sferraro@lbl.gov` — **CONFIRMED** (sferraro.lbl.gov/people, verified 2026-09-02). | **High/High.** |
| 6 | **Jérôme Quintin** (ÉTS/McGill) | See §1 — 4 gr-qc-primary + active CO submissions; co-author of the general-c_s formula P2′ cross-checks its coefficients against. Dual-purpose contact (Note + P2′). | `jquintin@physics.mcgill.ca` — **CONFIRMED**. | **High/High.** |
| 7 | **Ashley J. Ross** (Ohio State CCAPP) | CO-primary 2606.24852, 2603.25693, 2511.15354. | `ross.1333@osu.edu` — **UNCONFIRMED**, verify before sending. | High eligibility, Medium address. |
| 8 | **Hernán E. Noriega** (UNAM) | Verified 2026-07-22, carried forward: clears CO (+gr-qc/IM/GA). DESI DR1 author. | `henoriega@icf.unam.mx` — **CONFIRMED** 2026-07-24. | High/High. |

**Not recommended:** Mehdi Rezaie — last arXiv submission 2501.10759,
appears to have left academia; do not send.

**Recommendation:** to avoid the "I'm correcting your own paper" framing as
the very first contact, lead with **Meerburg, Chaussidon, or Ferraro**
(confirmed, on-topic, not authors of the corrected value) and send
Cai/Brandenberger in the same or next batch using the diplomatic
"refinement of your calculation" framing already in the draft below — never
send Cai/Brandenberger a version that reads as "your paper is wrong."
Quintin is worth sending regardless, since he can clear the Note (§1) and
P2′ (§3) with one endorsement each.

### Draft email — ARCHIVED, DO NOT SEND (P2′ deferred; use §3a's A3 framing instead)

**Subject:** `arXiv endorsement request — exact matter-contraction f_NL correction (astro-ph.CO)`

> Dear Professor ⟨Name⟩,
>
> I'm an independent researcher in Los Angeles — unaffiliated, single-author —
> asking whether you'd be willing to endorse me to submit to astro-ph.CO.
>
> The paper re-derives the matter-contraction local non-Gaussian amplitude
> for the ε=3/2 background by re-summing all four cubic vertices, obtaining
> f_NL^local = −35/16 = −2.1875. I do not reproduce the −35/8 printed in Cai,
> Xue, Brandenberger & Zhang (arXiv:0903.0631); the coefficients are
> cross-checked against that paper's own order-grouped expressions and
> against Li, Quintin et al.'s general-c_s formula. [If sending to Cai or
> Brandenberger: I'd rather you saw the discrepancy directly than hear about
> it secondhand.]
>
> [DOI/PDF link — insert once the independent second-method derivation gate
> closes and the manuscript is condensed to Letter form; do not send before
> then per the portfolio decision's submission gate.]
>
> Endorsing is a short form at arxiv.org/auth/endorse with the code below —
> arXiv states it attests only that I'm a legitimate researcher in the area,
> not support for the results.
>
> With thanks,
> Houston Golden
> Independent Researcher, Los Angeles, California
> houston@hubify.com · ORCID 0009-0008-5616-5994

**Gate — superseded, do not act on this section:** P2′ is DEFERRED per the
2026-09-02 final-review recommendation (above) — no gate closes it into a
submission because no submission is planned. Route the astro-ph.CO
endorsement ask to A3 instead (§3a).

---

### 3a. A3 multi-channel paper — astro-ph.CO `LRZHC4` (cross-list gr-qc `HYEJ7S`) — **DRAFT, not yet submission-ready**

**Status (2026-09-02, updated after R2 verification closure):**
`research/track_a3_multichannel/paper/main.tex` v3M.0.5 is the Track-A
flagship absorbing P2′'s content (§II–III) plus pulsar-timing, PBH, and
LSS/SPHEREx channel confrontations. Automated review has converged: R2
verification (Fable minor-revisions / Grok reject / Gemini major-revisions)
closed 16 items, including a real 30-bin injection-recovery test; per
directive R2's convergence budget (2/2 rounds consumed), review rounds now
STOP on this paper. **Final author review (Houston's personal sign-off) is
still pending — do not send any A3 endorsement email yet.** This entry
documents the current, real abstract so the ask is ready the moment final
author review clears.

> Abstract (v3M.0.5, current manuscript text — automated review converged;
> final author review pending, do not treat as submission-authorized):
> A dust-dominated contracting phase preceding a nonsingular bounce predicts
> a parameter-free local non-Gaussianity of the primordial curvature
> perturbation. We report a from-scratch, vertex-by-vertex in-in
> computation of this amplitude, validated against the de Sitter and
> ultra-slow-roll limits before use. It independently confirms
> f_NL^local = −35/16 = −2.1875, the value printed by Li et al. (2017) and
> by Quintin et al. (2015), exactly half the value originally printed by
> Cai et al. (2009), f_NL^local = −35/8; we locate Cai et al.'s factor of
> two at their amplitude-normalization step, and show the squeezed limit is
> orientation dependent, −35/16+(15/16)μ². This from-scratch computation,
> agreeing with two independent published results, is what adjudicates the
> factor of two within the in-in method; a method-independent
> (gradient-expansion or Bianchi-I separate-universe) confirmation remains
> open. Survival of this amplitude through an explicit nonsingular bounce
> is bounded, not resolved: within a handoff scheme that freezes the
> contraction-phase bispectrum at the NEC boundary and evolves it linearly
> thereafter, transfer across three bounce backgrounds obeys
> 0<T_fNL≤1/2 (scheme-dependent, 0.165–0.409), while the bounce's own
> cubic term — found in the loop-quantum-cosmology literature to
> potentially enhance non-Gaussianity by orders of magnitude — is not
> computed here, so no bound on the physical post-bounce f_NL follows. We
> then take the exact amplitude through three observational channels,
> stated at exactly the strength their evidence supports. (i) Pulsar
> timing. Refitting the NANOGrav 15-yr Hellings–Downs free-spectrum
> posteriors (30 bins) gives γ=2.567±0.382, consistent with the
> matter-bounce induced-GW prediction γ=3 at 1.14σ (refit) and 0.55σ
> (against NANOGrav's official 14-bin posterior, γ_HD=3.2⁺⁰·⁶₋₀·₆, 5–95%).
> The supermassive-black-hole-binary value γ=13/3 is disfavoured at 3.1σ
> against the official posterior (matching NANOGrav's own characterization
> of "moderate tension ... at the 99% credible boundary") and more
> strongly by the refit. A scale-invariant primordial-tensor slope (γ=5)
> has no posterior support: zero of 320,000 chain samples reach γ≥5. This
> channel measures a slope common to any scalar-induced background and is
> insensitive to f_NL. (ii) Primordial black holes. Replacing a truncated
> Press–Schechter map with the compaction-function formation criterion of
> Choudhury et al. (2025) gives a reproducible amplitude ratio,
> A(−35/16)/A(−35/8) = 1.732 [1.610, 1.809] across a 27-point grid, within
> a quadratic local map that is not always perturbatively controlled at the
> curvature excursions formation requires (1.2|f_NL|σ_r≈0.5–2); f_PBH(f_NL)
> at fixed amplitude is itself strongly non-monotonic (a ~55-decade minimum
> near f_NL≈−0.35, with both candidate values on the rising,
> anti-correlated branch beyond it) and is not quotable because the
> primordial spectrum shape it depends on is not reconstructible from the
> published source. (iii) Large-scale structure. The prediction is
> consistent with the DESI DR1 constraint under either of its two mutually
> exclusive theoretical priors on the quasar response: f_NL^local =
> −3.6⁺⁹·⁰₋₉·₁ (merger model) at 0.16σ, or +3.5⁺¹⁰·⁷₋₇·₄ (universality) at
> 0.77σ; the two are not directly comparable to each other. Large-scale
> structure is the only channel that both discriminates the two candidate
> amplitudes and depends on which is correct: SPHEREx reaches 3.13σ at its
> bispectrum-only forecast σ_fNL=0.7, pending a shape-overlap projection
> this paper has not yet re-derived at the −35/16 fiducial. No channel is
> in tension with another.

**Endorsers for A3** (astro-ph.CO `LRZHC4`, cross-list gr-qc `HYEJ7S`):
reuse the table above (Brandenberger, Cai, Meerburg, Chaussidon, Ferraro,
Quintin, Ross, Noriega) — the eligibility/contact research was verified
2026-09-02 and is unaffected by the P2′→A3 fold-in (same archive, same
authors, expanded content). **Recommendation unchanged:** lead with
Meerburg, Chaussidon, or Ferraro (not authors of the value under
discussion), send Cai/Brandenberger with the diplomatic "independent
confirmation, not correction" framing (A3 confirms Li et al. 2016's value
rather than disputing Cai et al. 2009's, a softer opening than P2′'s
framing was). Quintin remains a dual-purpose contact (Note §1 + A3 §3a).

**Gate before sending:** automated review is now converged (R2 verification
closed, rounds stopped per directive R2). Do not send any A3 endorsement
email until (1) final author review (Houston's personal sign-off, per
directive P) is recorded, (2) a method-independent f_NL check, the bounce
cubic term, and a real NANOGrav KDE-grid injection (the science gate items
below) are addressed or explicitly disclosed as open, and (3) a DOI/PDF
link exists to paste. This entry is prepared-ahead, not a go-ahead.

---

## Cross-cutting notes

- **ORCID.** `0009-0008-5616-5994` was independently confirmed public
  (`pub.orcid.org` HTTP 200) 2026-07-24. Re-check whether works have since
  been added — the 2026-07-24 draft found 0 linked works, which is still a
  minor credibility gap for a cold ask to a senior researcher; adding the
  Zenodo DOIs as ORCID "Works" costs ~2 minutes and is worth doing before
  the first send under this refreshed framing.
- **No sends without a link.** Every draft above intentionally has a
  `[DOI/PDF link — insert once...]` placeholder rather than a real URL,
  because none of the three merged/condensed manuscripts exist yet on disk
  in their new framing. Sending any of these emails before the gated
  manuscript compiles would ask an endorser to evaluate a paper that
  doesn't exist in the form described.
- **Reused facts vs. new facts.** All four archives (gr-qc `HYEJ7S`,
  astro-ph.GA `CLVMAQ`, astro-ph.CO `LRZHC4`, astro-ph.IM `L8TIPN`) were
  re-verified in a 2026-09-02 research pass against **current
  primary-category arXiv submission counts (2021–2026)**, superseding the
  2026-07-22/07-24 shortlist for the two archives where it conflicted:
  Brandenberger moved off gr-qc onto astro-ph.CO only (zero gr-qc-primary
  submissions since 2021); Shamir and Iye dropped from the GA list (Shamir's
  spin work files CO-primary and, more importantly, P4′'s null does not
  confirm his claim; Iye has no post-2018 activity found). Counts are
  **primary-category floors** — cross-lists would add more. Emails marked
  UNCONFIRMED were sourced from a directory page or search summary and must
  be recovered from a recent paper's corresponding-author footnote or ADS
  before sending — never guessed from a name pattern (e.g. never assume
  `first.last@lbl.gov`). No endorser was contacted in this research pass.
- **astro-ph.IM (`L8TIPN`).** Not the active submission route for any of the
  three near-term works (the Note is gr-qc-primary, P4′ is GA-primary, P2′
  is CO-primary), so no dedicated IM outreach section exists above — but if
  a future work needs it, the 2026-09-02 pass verified: **David Alonso**
  (Oxford, `David.Alonso@physics.ox.ac.uk` CONFIRMED, NaMaster author,
  IM-primary 2601.16761/2406.04725/2304.08995/2108.13418, HIGH); **Dustin
  Lang** (Perimeter, IM-primary 2607.09374/2603.03520/2503.07923/2306.11784/
  2305.16630, email UNCONFIRMED, HIGH); **Stephen Bailey** (LBNL DESI data
  systems, IM-primary 2405.19288/2311.04272/2311.04855/2208.08518, email
  UNCONFIRMED — desi.lbl.gov 403'd, HIGH); **Anand Raichoor** (LBNL,
  IM-primary 2504.06870/2503.07923/2306.11784/2208.08518, email
  UNCONFIRMED — profiles.lbl.gov JS-gated, HIGH); **Adam D. Myers**
  (Wyoming, IM-primary 2507.12784/2306.11784/2209.14482, email UNCONFIRMED
  — UW page 500'd, HIGH); **Mike Walmsley** (Toronto/Dunlap — dual GA+IM,
  see §2 row 5). Backups (MEDIUM, only 2 IM-primary each): Julien Guy,
  Carlos García-García.
