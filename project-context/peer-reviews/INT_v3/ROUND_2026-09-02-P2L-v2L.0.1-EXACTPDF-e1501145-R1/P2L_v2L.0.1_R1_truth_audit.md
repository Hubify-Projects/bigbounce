# P2L v2L.0.1 — R1 truth audit (Opus, independent)

- **Manuscript:** `arxiv/paper2prime_fnl_letter/main.pdf`, v2L.0.1, 4 pp, dated September 2, 2026
- **sha256 (verified this session):** `e1501145bd314f85e54c928c579ec1e3ceb96bbdf078ba15ab02e2bb40ca4d12` ✓ matches every leg's binding
- **Round:** `ROUND_2026-09-02-P2L-v2L.0.1-EXACTPDF-e1501145-R1`
- **Legs audited:** Claude/Fable INT (`P2L_fable_r1_leg.md`, MAJOR REVISIONS, 5 MAJOR / 13 MINOR); Grok API (`..._P2L_Grok_brutal.md`, REJECT, 4 ESSENTIAL / 4 MAJOR / 2 MINOR / 1 NIT / 1 STALE / 1 ARITH); Gemini API (`..._P2L_Gemini_cosmology.md`, MAJOR REVISIONS, 4 ESSENTIAL / 4 MAJOR / 3 MINOR). **Perplexity: ABSENT** (not run; recorded absent, never as zero-findings — Rule 4).
- **Item extraction:** mechanical, per-item tags, per Rule 8 — leg verdict words are diagnostic only. 42 tagged items total; 42 dispositioned. Gap: **no**.
- **Auditor stance:** skeptical in both directions; every verdict below is decided from source (tex lines, committed artifact JSON/markdown, my own sympy runs, arXiv metadata fetched this session), never from a leg's verdict word.

## 0. What I recomputed myself (nothing taken on trust)

1. **Fixed-angle squeezed limit, from the committed total shape polynomial.** Loaded
   `A_total_times_256_prodk2` from `research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.json`,
   set `k_{2,3}=sqrt(k^2+k_1^2/4 ∓ k k_1 μ)`, and took `k_1→0` of `(10/3)A/Σk_i^3`:
   **`−35/16 + (15/16)μ²`** (spot values: μ=0 → −35/16; μ=1/2 → −125/64; μ=1 → −5/4).
   Eq. (3) of the Letter and Table I's total row are **confirmed**.
2. **M1 arithmetic (sympy):** `(5ε−7)·5/8` at ε=3/2 = **+5/16**; `5(ε−7)/8` = `(5ε−35)/8` = **−55/16**.
   The committed script prints `f_rho = 5*(epsilon - 7)/8` (line 537 + JSON
   `uniform_density_slicing_fNL_general_eps`) and the brief line 33 prints `f_ρ=5(ε−7)/8`.
   The Letter prints the other, inequivalent expression.
3. **Li Eq. (4.19) at c_s=1:** the script's transcription (lines 454–461) gives
   `A_total − A_Li = 0` and `li_eq51_at_cs1 = −35/16`; combined with (1), the μ² structure is
   **entirely inside the published 2009/2016 shape function**. (Caveat: I verified the identity
   against the repo's transcription of Eq. (4.19) and the Fable leg's independent extraction from
   Li's arXiv source; I did not re-key Eq. (4.19) from the published PDF myself.)
4. **Cai factor of two:** JSON `cai_eq37_minus_total_distinct_monomial_reading = 0`,
   `cai_quoted_over_from_scratch = {local: 2, equilateral: 2, folded: 2}` — the uniform ×2 between
   Cai's *printed polynomial* and Cai's *quoted amplitudes* is confirmed in all three configurations.
5. **Forecast provenance:** `research/track_a3_multichannel/outputs/survey_reach_fnl.json` —
   Table II's "2.6–3.1" is (r-projected 2.625, bare 3.125) and "3.7–4.4" is (3.675, 4.375), with
   `bounce_to_local_template_overlap_r = 0.84`, `r_source = "this lab's P2 forecast"`. The A3 brief's
   own ledger item **A3-4** flags that r must be re-derived at the −35/16 fiducial. DESI: brief §3.2
   gives σ ≈ 9.0/9.1 (Chaussidon+2024, arXiv:2411.17623), tension 0.16σ (merger model) / 0.77σ
   (universality), discriminating power 0.24.
6. **Transmission:** A2 brief lines 119–125 — `T ∈ {0.250 (LQC/S1), 0.165 (Quintin-type/S1), 0.409 (LQC/S2)}`;
   the 1.64× is `0.409/0.250` **on the same LQC background**; the full-range spread is 2.48×.
7. **arXiv metadata fetched live** for 1612.02036, 0903.0631, 1301.5699, 1210.3692, 1712.08148,
   1508.04141, 2311.13082, 2504.11641, 2409.18983.
8. **New supporting fact (mine, not in any leg):** Quintin *et al.* 2015 (ar5iv 1508.04141, §III.3)
   states verbatim *"for the local shape, the authors of [Cai 2009] found f_NL^local = −35/16"* —
   i.e. the corrected value is already in circulation in the literature, **mis-attributed to Cai**.
   This **verifies** the Letter's claim about Quintin *et al.*, and it is directly relevant to venue
   (see §4).

## 1. Per-finding table

Verdicts: **GNR** = GENUINELY-NEW-REAL · **RFD** = RE-FLAG-OF-DISCLOSED · **FAL** = FALSIFIED ·
**OPN** = OPINION/GENRE · **OOS** = OUT-OF-SCOPE.

| # | Leg / id | Claim | Location | Verification (source) | Verdict | Sev | Closure |
|---|---|---|---|---|---|---|---|
| 1 | Fable M1 | `f^ρ=(5ε−7)·5/8` contradicts its own −55/16 | main.tex L170 | my sympy §0.2: +5/16 vs −55/16; script L537 + JSON print `5(ε−7)/8` | **GNR** | MAJOR | Replace with `f_{\rm NL}^\rho=5(\epsilon-7)/8` (= `(5\epsilon-35)/8`) |
| 2 | Gemini E1 | same algebraic contradiction | §III p.2 | same | **GNR** (dup of 1) | MAJOR | → C1 |
| 3 | Fable M2 | "new result" for μ² overstated; it is in Li Eq. (4.19)/Cai Eq. (37) | abstract L46–48, §III, Summary | §0.1 + §0.3: my own expansion of the total polynomial gives −35/16+(15/16)μ²; `li_eq419_minus_total_at_cs1 = 0` | **GNR** | MAJOR | Reframe as *previously unremarked property of the published (correct) shape function*; state the one-line route from Eq. (4.19)/Eq. (37) |
| 4 | Grok M2 | μ²→shear algebra asserted, not derived | §III Eq. (3) | table + script reproduce it, but the Letter shows no step | **GNR** (same defect, cheaper fix via #3) | MAJOR | → C2; one sentence deriving it from Eq. (4.19) answers both |
| 5 | Grok M4 | 15/16 prefactor not independently reproducible from the Letter | §III | as #4 | **GNR** dup | MAJOR | → C2 |
| 6 | Fable M3 | Letter never says which amplitude a survey tests; r=0.84 absent | Table II, §V, abstract | §0.5 — 2.6/3.7 are r-projected, 3.1/4.4 bare; r defined only in the A3 brief; A3-4 says r is not yet re-derived at this fiducial | **GNR** | MAJOR | State per row: isoceles vs monopole vs template projection; define r and its provenance/limitation |
| 7 | Gemini M1 | 2.1875/0.7=3.125 matches only the upper end; 2.6 unexplained | Table II | same — 2.6 = 3.125×0.84 | **GNR** dup | MAJOR | → C3 |
| 8 | Grok M3 | σ separations quoted without Fisher/covariance/mask information | Table II | the σ are **cited** (Heinrich+2023 abstract: 0.7 bispectrum, 0.5 P+B target — verified live); no in-house Fisher is claimed | **OPN** in part / **GNR** in part | MINOR→ | Say explicitly that σ are quoted from Heinrich+2023 and that the separation is `Δf_NL(×r)/σ`, not a new Fisher |
| 9 | Grok A1 | 0.16σ implies σ_fNL ≈ 13.67 | Table II | **FAL** — 0.16σ is tension of −2.1875 with DESI central −3.6 (σ≈9.0), not a separation; brief §3.2 | **FAL** (arithmetic) / defect real | MINOR | → C9 (print σ≈9, cite Chaussidon+2024, print 0.24σ) |
| 10 | Fable m4 | DESI row: σ blank, uncited, "≲0.2σ" understates 0.24 | Table II | brief §3.2 | **GNR** | MINOR | Fill σ≈9.0, cite arXiv:2411.17623, print 0.24 |
| 11 | Fable M4 | Refs [2] and [6] do not exist as cited | references.bib L56–66, L104–114 | **live arXiv:** 1612.02036 = Yu-Bin Li, Quintin, Dong-Gang Wang, Yi-Fu Cai, *Matter bounce cosmology with a generalized single field…*, **JCAP 03 (2017) 031** — bib has wrong authors, wrong title, wrong volume/year. 1301.5699 = Chen, Firouzjahi, Namjoo, Sasaki, *A single field inflation model with large local non-Gaussianity*, EPL 102 59001 — **not** *Quantum Primordial Standard Clocks* (that is 1411.2349, JCAP 02 (2015) 006) | **GNR** | MAJOR | Correct both entries; decide which Chen paper supports the non-attractor-clock sentence and cite that one |
| 12 | **auditor (new)** | Ref [12] Choudhury given names wrong | references.bib L139 | live arXiv 2409.18983: Kritartha Dey, Siddhant Ganguly, Ahaskar Karde, Swapnil Kumar Singh, Pranjal Tiwari — bib says Sudhakar/Nilanjandev/Purnendu/Nisha/Abhishek | **GNR** | MINOR | Fix author list |
| 13 | **auditor (new)** | `CaiEassonBrandenberger:2012` present in .bib, cited 0 times | references.bib L80 | `grep -c` on main.tex = 0 | **GNR** | NIT | Remove or cite |
| 14 | Grok N2 | "cited works carry 2026 dates / placeholder arXiv IDs that post-date the manuscript" | references | **FAL** — 2311.13082, 2409.18983, 2504.11641, 1712.08148 all fetched live and real; the only 2026 entries are the author's own repo/Zenodo items. Known future-date-confab class (SKILL Rule 3) | **FAL** | — | None |
| 15 | Fable M5 | Load-bearing statements rest on mutable `blob/main` links | §III, §IV, refs [13]–[15] | refs L158–177 are all `blob/main` URLs; `ζ_ρ=2ζ_c` and `T=[1−ρ]/2` appear with no derivation and no published citation | **GNR** | MAJOR | Give the one-line gauge argument and the two-line origin of T; pin [13]–[15] to a commit hash or Zenodo DOI |
| 16 | Gemini E3 | mutable branch pointers violate reproducibility | Data Availability + [13]–[15] | same | **GNR** dup | MAJOR | → C5 |
| 17 | Gemini E4 | §IV imports load-bearing physics from a GitHub markdown | §IV | same | **GNR** dup | MAJOR | → C5 |
| 18 | Gemini M2 | `ζ_ρ=2ζ_c` quantitative claim, no derivation/citation | §III | value itself correct (brief §5 table, all ε) — the *presentation* is the defect | **GNR** dup | MAJOR | → C5 |
| 19 | Grok M1 | no per-vertex integrands; independent verification impossible | §I + Table I | **FAL as MAJOR** — Table I gives per-vertex squeezed values and full μ-dependence, and the committed script prints every integrand; the real residual is the mutable link | **FAL**(severity) → **C5** | MINOR | Pin the artifact to a DOI |
| 20 | Grok E1 | abstract claims an observable; bounce vertex uncomputed → remove claims or compute it | abstract + §IV | **FAL** — abstract L53–57 states transmission is "bounded, not resolved", `0<T≤1/2`, and that the bounce cubic term "is not computed here"; title scopes to the contraction. "Compute the bounce vertex" is a new-research demand | **FAL** / **OOS** (the demand) | — | None |
| 21 | Grok E4 | same, restated in pass 2 | abstract | same | **FAL** dup | — | None |
| 22 | Grok E2 | "the exact local non-Gaussianity" is stronger than the body | title/abstract | **partly real**: the number is exact; "local" is imprecise once the squeezed limit is μ-dependent | **GNR** (as wording) | MINOR | → C16 (retitle) |
| 23 | Fable m11 | title "exact local" mildly overstated | title | same | **GNR** dup | MINOR | → C16 |
| 24 | Grok J1 | abstract "2.6–3.7σ" is a stale composite of two channels' lower bounds | abstract L59 + Table II | Table II rows are 2.6–3.1 and 3.7–4.4; brief §3.1 confirms the four numbers | **GNR** | MINOR | Write "2.6–4.4σ depending on channel and shape projection", or name the channel |
| 25 | Gemini E2 | same | abstract | same | **GNR** dup | MINOR | → C6 |
| 26 | Fable m1 | same | abstract | same | **GNR** dup | MINOR | → C6 |
| 27 | Gemini M3 | "This supersedes an earlier, narrower statement…" is drafting prose | §IV L195–196 | present verbatim at main.tex L195 | **GNR** | MINOR | Delete |
| 28 | Fable m5 | same + the "not an artifact of this one" tone | §III–IV | L166, L195 | **GNR** dup | MINOR | → C10 |
| 29 | Gemini M4 | "1.64×" contradicts 0.409/0.165 = 2.48 | §IV L194 | **FAL as an error** — A2 brief L125: 1.64 = 0.409/0.250 on the *same* LQC background, exactly as the parenthesis says. Ambiguity of juxtaposition is real | **FAL** / clarity **GNR** | MINOR | Give both numbers: full-range 2.48×, same-background scheme 1.64× |
| 30 | Fable m2 / Gemini N2 | "isoceles" → "isosceles" (×4–5) | abstract, §I, §III, Table I caption | `grep -c isoceles main.tex` | **GNR** | MINOR | Spelling |
| 31 | Fable m3 / Gemini N1 | "(§ 2311.13082, abstract)" | §V L227–228 | L228 verbatim | **GNR** | MINOR | → "arXiv:2311.13082, abstract" |
| 32 | Fable m6 | μ²-vertex attribution ("two vertices … through ∂χ̃") disagrees with Table I | §III L160–161 vs Table I | Table I: μ² sits in the field-redefinition row (−15/16 μ²) and ζ′∂ζ·∂χ̃ (+15/8 μ²); ζ(∂∂χ̃)² has none though it contains χ̃. Brief line 96 words it correctly | **GNR** | MINOR | Name the two contributions explicitly |
| 33 | Fable m7 | "their amplitude-normalization step" over-localises the factor 2 | abstract, §III, Summary | JSON only establishes *printed polynomial = our sum* and *quoted = 2× that*; the location inside Cai Eqs. 38–40 is inferred | **GNR** | MINOR | "between their printed shape function and their quoted amplitudes" / "presumably in" |
| 34 | Fable m8 | δK sign/convention | §III L157 | brief §6 L119–124 gives K^i_j = Hδ − ∂∂ψ/a²; trace is −εζ̇ in this convention | **GNR** | MINOR | State the convention or write \|δK\| |
| 35 | Fable m9 | "Li et al. … inherit … not an independent check" is unfair | §III L149–150 | Li+2016 redo the in-in for general c_s and recover Cai at c_s=1; and they **print** the corrected −35/16 | **GNR** | MINOR | Reword; say plainly that Li *et al.* already print −35/16 |
| 36 | Fable m10 / Grok NIT1 | `f^sq(μ)` undefined in Table I caption | Table I caption L124–125 | caption verbatim | **GNR** | MINOR | Define it; note μ=0 = isoceles |
| 37 | Grok E3 / N1 / Fable m12 | "v2L.0.1" preprint tag and "(Dated: …)" author block | p.1 header | main.tex L19–24, L34 — these are directive-G internal stamps | **OPN/GENRE** (house style; required internally) | NIT | Strip in the journal-submission build only; keep in the repo/arXiv build |
| 38 | Gemini N3 / Fable m13 | ref titles carry "Track a2/a3:", "Adjudication:" project tags; [9] casing | references.bib | L160–176, L38 | **GNR** | NIT | Clean up |
| 39 | Grok NIT1 (2nd half) | no figures | — | 4-page Letter, one table + one table | **OPN** | — | None |
| 40 | Fable §C cross-checks | (13 rows adjudicating Grok/Gemini) | — | independently re-derived above; I agree with every row of Fable §C except that I upgrade its "Grok M1 refute" to a partial (the DOI pin is the real residual) | — | — | — |
| 41 | Grok summary REJECT | verdict word | — | Rule 6/8: its three "essentials" are #20/#22/#37 — one FALSIFIED, one MINOR wording, one house style. REJECT is not supported by its own body | **FAL** (as a verdict) | — | Record verdict verbatim; do not treat as a science blocker |
| 42 | Gemini overall | "core physics excellent, presentation blocks" | — | consistent with my findings | — | — | — |

**Completeness check (Rule 8):**

| Paper | Leg | Verdict word | Tagged items in raw | Dispositioned | Gap |
|---|---|---|---|---|---|
| P2L | Claude/Fable INT | MAJOR REVISIONS | 18 (5 MAJOR, 13 MINOR) | 18 | no |
| P2L | Grok API | REJECT | 13 (4 E, 4 M, 2 N, 1 NIT, 1 STALE, 1 ARITH) | 13 | no |
| P2L | Gemini API | MAJOR REVISIONS | 11 (4 E, 4 M, 3 N) | 11 | no |
| P2L | Perplexity | — | **ABSENT** (leg not run) | — | n/a |

**BLOCKERs in the round: 0** (observed, not assumed). No leg was faked, downgraded, or read from a label.

## 2. Canonical (fingerprint-deduped) list

| id | severity | canonical item |
|---|---|---|
| **DP2L-01** | MAJOR | `f^ρ_NL` printed as `(5ε−7)·5/8`; correct committed value is `5(ε−7)/8 = (5ε−35)/8 = −55/16` |
| **DP2L-02** | MAJOR | μ² orientation dependence is **not new**: it is the fixed-angle squeezed limit of the published Cai Eq. (37) / Li Eq. (4.19) shape function (`A_total − A_Li = 0` at c_s=1). Novel content is the observation, the per-vertex attribution, and the shear interpretation |
| **DP2L-03** | MAJOR | Table II never states which amplitude each survey row tests (isoceles −35/16 / monopole −15/8 / template projection); r=0.84 is undefined and unsourced in the Letter, and is flagged not-yet-re-derived at this fiducial by A3-4 |
| **DP2L-04** | MAJOR | Reference metadata: [2] Li+2016 (authors/title/journal all wrong), [6] Chen 1301.5699 mis-titled as *Quantum Primordial Standard Clocks*, [12] Choudhury given names wrong, [8] uncited |
| **DP2L-05** | MAJOR | Load-bearing statements (`ζ_ρ=2ζ_c`, `T=[1−ρ]/2`, `0<T≤1/2`, 0.165–0.409) carry no derivation and only mutable `blob/main` links |
| **DP2L-06** | MINOR | Abstract "2.6–3.7σ" is a cross-channel composite; Table II gives 2.6–3.1 and 3.7–4.4 |
| **DP2L-07** | MINOR | DESI DR1 row: σ_fNL blank, no citation, "≲0.2σ" vs the brief's 0.24σ |
| **DP2L-08** | MINOR | "isoceles" → "isosceles" throughout |
| **DP2L-09** | MINOR | "(§ 2311.13082…)" → "arXiv:2311.13082" |
| **DP2L-10** | MINOR | Version-history prose ("This supersedes an earlier, narrower statement…") |
| **DP2L-11** | MINOR | μ²-source sentence disagrees with Table I's own rows |
| **DP2L-12** | MINOR | "amplitude-normalization step" over-localises Cai's factor 2 beyond what is observed |
| **DP2L-13** | MINOR | δK sign/convention unstated |
| **DP2L-14** | MINOR | "Li et al. … inherit … not an independent check" — unfair, and buries that Li *et al.* already print −35/16 |
| **DP2L-15** | MINOR | Table I caption does not define `f^sq(μ)` |
| **DP2L-16** | MINOR | Title/abstract "the exact **local**" is imprecise given the μ-dependence |
| **DP2L-17** | MINOR | 1.64× (same-background scheme) vs 2.48× (full range) needs both numbers |
| **DP2L-18** | NIT | House-style: preprint version tag, dated author block, project tags in ref titles — strip in the journal build only |
| **DP2L-F1** | FALSIFIED | "Abstract asserts a post-bounce observable" (Grok E1/E4) — abstract explicitly bounds transmission and disclaims the bounce cubic term |
| **DP2L-F2** | FALSIFIED | "Placeholder / future-dated arXiv IDs" (Grok N2) — all nine fetched live and real (SKILL Rule 3 class) |
| **DP2L-F3** | FALSIFIED | "0.16σ implies σ≈13.7" (Grok A1) — 0.16σ is a tension against DESI's central value, σ≈9.0 |
| **DP2L-F4** | FALSIFIED | "1.64 contradicts 0.409/0.165" (Gemini M4) — 1.64 = 0.409/0.250 on one background, as stated |
| **DP2L-F5** | FALSIFIED (severity) | "No per-vertex integrands; unverifiable" (Grok M1) — Table I + committed script supply them; residual is the DOI pin (→ DP2L-05) |
| **DP2L-O1** | OUT-OF-SCOPE | "Compute the bounce cubic vertex or remove the observational section" (Grok E1) — a new-research demand against a scope the Letter states honestly |

**Class counts — GENUINELY-NEW-REAL 18 (5 MAJOR, 12 MINOR, 1 NIT) · FALSIFIED 5 · OPINION/GENRE 2 · OUT-OF-SCOPE 1 · RE-FLAG-OF-DISCLOSED 0** (P2L is a new work; no prior P2L round exists, and none of the parent P2 fingerprints in `DISPOSITIONS/P2.md` matches an item in this round — the Letter's scope, headline, and forecast construction are all different from the 37-page parent).

## 3. Closure plan (no manuscript edits made by this audit)

**(a) Restate the contribution honestly.** The Letter's defensible claims, in order:
   1. an **independent from-scratch in-in computation** confirming `f_NL^local = −35/16`, with a
      per-vertex table and two literature validations (de Sitter, USR `5/2`) run before use;
   2. **locating** the long-standing `−35/8` discrepancy: Cai *et al.* 2009's printed shape function
      (Eq. 37, distinct-monomial reading) is correct term by term and equals this vertex sum; their
      three quoted amplitudes are each exactly twice their own polynomial's limits;
   3. the **δN / comoving reconciliation**: `f^ρ = 5(ε−7)/8 = −55/16` on uniform-density slices and
      `f^c = −5` on comoving slices are correct for their own variables, with `ζ_ρ = 2ζ_c` at linear
      order in a non-attractor phase and the shear dropped by the isotropic separate-universe route;
   4. the **orientation dependence** `−35/16 + (15/16)μ²` presented as **consistent with — and in fact
      contained in — Li+2016 Eq. (4.19) at c_s=1**, previously unremarked, here made explicit,
      attributed per vertex, and interpreted as the non-attractor shear (Namjoo+2012 analogue).
      Delete "We report a new result" from the abstract.
   5. Add the verified fact that **Quintin *et al.* 2015 §III.3 already quotes `−35/16`, attributing it
      to Cai 2009** — this is the cleanest evidence that the literature record is inconsistent and is
      what the Letter actually repairs.

**(b) Fix the forecast.** Per Table II row, state the amplitude tested: isoceles `−35/16` vs `−35/8`
   (bare) and the shape-projected version `r·Δf_NL/σ` with `r = 0.84` **defined** (noise-weighted overlap
   of the bounce shape with the local template), **sourced** (the parent P2 forecast), and **caveated**
   (A3-4: not yet re-derived at the `−35/16` fiducial). Give σ per row with its citation
   (Heinrich+2023 arXiv:2311.13082 for 0.7 and 0.5; Chaussidon+2024 arXiv:2411.17623, σ≈9.0, for DESI
   DR1) and print 0.24σ, not "≲0.2σ". Fix the abstract to 2.6–4.4σ or name the channel. Add one
   sentence noting that a local-template estimator is sensitive to a projection of the full μ-dependent
   shape, not to the μ=0 slice — this is what removes the internal tension between §III and §V.

**(c) DP2L-01 and every reference.** Print `f_{\rm NL}^\rho = 5(\epsilon-7)/8`. Rebuild [2] as
   Y.-B. Li, J. Quintin, D.-G. Wang, Y.-F. Cai, *Matter bounce cosmology with a generalized single
   field: non-Gaussianity and an extended no-go theorem*, JCAP **03** (2017) 031, arXiv:1612.02036.
   Decide the Chen citation: use arXiv:1411.2349 (JCAP 02 (2015) 006) for *Quantum Primordial Standard
   Clocks*, or arXiv:1301.5699 (Chen, Firouzjahi, Namjoo, Sasaki, EPL **102** 59001) for the
   non-attractor large-local-NG argument — the text's "non-attractor clock argument" fits the latter's
   physics and the former's title; pick one and match author list to it. Fix [12]'s given names, drop or
   cite [8]. Pin [13]–[15] to commit hashes or a Zenodo DOI (DP2L-05).

**(d) Venue / novelty recommendation — see §4.**

## 4. Venue recommendation

**Recommendation: do not submit as a PRD Letter. Submit as a regular Physical Review D article
(secondary option: a Comment on Cai *et al.*, JCAP 0905:011, if the scope is cut to the factor of two
alone).** Reasons, all evidence-based:

1. **The strongest genuinely-new element is a correction/confirmation, not a discovery.** Once DP2L-02
   is closed honestly, the μ² is a property of a shape function published in 2009 and 2016. What
   remains new is: an independent recomputation, the per-vertex table, the located factor of two, the
   δN reconciliation, and the shear reading. That is real, useful, citable work — it is not the
   "importance and urgency to a broad audience" bar PRD Letters applies.
2. **The literature record is already partly corrected.** Li+2016 print `−35/16` at c_s=1, and
   Quintin+2015 §III.3 quotes `−35/16` (verified live this session). The Letter's own §III says as
   much. A Letter whose thesis is "the value in circulation is already the right one, and here is where
   the wrong one came from" reads as a Comment/erratum-class contribution, which is exactly what a
   regular article or a Comment is for.
3. **The Letter's most interesting physics is explicitly not computed.** §IV is honest that the bounce
   cubic term is uncomputed and that linear transfer only bounds `T ≤ 1/2`. Both Grok and Gemini keyed
   on this (Grok wrongly, as a claim of an observable; correctly, as a self-containedness gap). A
   regular article has the room to derive `T = [1−ρ]/2` and `ζ_ρ = 2ζ_c` in-text, which closes DP2L-05
   without the "move it to a companion" amputation.
4. **Four pages cannot carry the required additions.** Closing DP2L-02/03/05 needs: the Eq. (4.19)
   route to the μ², a defined and caveated `r`, per-row amplitude statements, and two short
   derivations. That is 2–4 additional pages of a format that has none.
5. **Directive-Q1 check:** the framing must be the pure contribution (the computation, the located
   factor of two, the reconciliation), never "we redo an earlier error." The current draft already
   does this correctly and should keep doing so under the new venue.

**Counter-consideration, recorded fairly:** if Houston prefers a Letter, the honest Letter is a
narrower one — *"The matter-contraction f_NL is −35/16: an independent computation and the origin of the
factor of two"* — dropping §IV and §V entirely and keeping the μ² as a one-paragraph remark on the
published shape function. That version would be defensible at Letter length, but it discards the
transmission and reach work, which is the part with forward research value.

**Readiness:** this round does **not** clear DP2L-01…05; the Letter is not at automated-review
convergence and no readiness uplift is warranted. Verdict words recorded verbatim as
Fable = MAJOR REVISIONS, Grok = REJECT, Gemini = MAJOR REVISIONS; Perplexity ABSENT. No ACCEPT was
faked, no finding was dismissed without a source-cited verdict, and no derivation was fabricated.
