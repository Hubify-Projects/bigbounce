# EXT6 P1A — Truth Audit

**Round**: EXT6 (external delta round 6 — 3-vendor: ChatGPT Pro Extended, Grok Heavy, Gemini Thinking)
**Paper**: 1A (`arxiv/paper1a_ech_nogo.tex`)
**Version reviewed**: v1A.0.65 (PDF hash `418777c6`, 28 pp, dated 12 June 2026 PDT)
**Audit date**: 2026-06-12 PT
**Reports**:
- `project-context/peer-reviews/EXT6_P1A_ChatGPT.md` — MAJOR REVISIONS (1 BLOCKER, 4 MAJORS, 5 MINORS)
- `project-context/peer-reviews/EXT6_P1A_Grok.md` — ACCEPT (0 BLOCKER, 0 MAJOR, 4 MINORS)
- `project-context/peer-reviews/EXT6_P1A_Gemini.md` — ACCEPT WITH MINOR REVISIONS (0 BLOCKER, 1 MAJOR, 1 MINOR)

**Verdict schema**: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION
**Auto-falsify rules applied**: HD-6 (changelog comment block = deliberate transparency); current-date = June 2026; pattern-052 re-raise (prior falsification must have cited primary tex/artifact evidence to auto-falsify a re-raise).

---

## Findings table

| # | Leg | Finding (severity) | Verdict | Evidence (tex lines / quotes) | Disposition |
|---|-----|--------------------|---------|-------------------------------|-------------|
| 1 | ChatGPT F65-B1 | Sec. IV E "condensate mechanism yields a vacuum energy that is parametrically too large by many orders of magnitude" contradicts the corrected Route 1 result (BLOCKER) | **VERIFIED** | `arxiv/paper1a_ech_nogo.tex` L1786-1791: `"The condensate mechanism / yields a vacuum energy that is parametrically too large by many orders / of magnitude and is not a viable DE source; its role is therefore / documented in / Sec.~\ref{sec:r1_njl} as a quantitative closure rather than a / viable channel."` Direct contradiction with corrected Route 1 body L1420-1422: `"\rho_{\rm NJL} \sim n_\psi^2/\MPl^2 \approx 4\times 10^{-81}\,\text{eV}^4, / i.e.\ roughly 4\times 10^{-69}\,\rho_\Lambda ... far below \rho_\Lambda, not above it."` This is a real internal-inconsistency regression introduced when R34conf wrote the §IV E synthesis paragraph but never re-synced it after R35conf split Route 1 into legs (i)+(ii). NOT in changelog comment block — it is live body text in Sec. IV E. | **FIX**: rewrite L1786-1791 to: "The NJL contact term is parametrically far below $\rho_\Lambda$ at any cosmologically relevant Standard-Model number density ($\sim$69 orders below), parity-even with $\langle J^5\rangle\!\approx\!0$, and lacks any coherent $w\!=\!-1$ mean-field structure; incoherent thermal variance $\langle J^5 J^5\rangle$ is permitted but does not source coherent dark energy." Then grep for "too large", "overshoot", "parametrically" near "condensate" to confirm no other residues. |
| 2 | ChatGPT F65-M1 | Sec. IV opening (and Paper Organization §I) still says "each route is closed at the amplitude level" without the R4 naturalness carve-out (MAJOR) | **VERIFIED** | L755 (Paper Organization): `"Section~\ref{sec:fourroute} closes each of the four standard ECH routes ... at the amplitude level under explicitly-labeled scaling assumptions for R2--R3 and a naturalness limit for R4"` — this one is actually calibrated (mentions naturalness limit for R4). But L1334-1335 (Sec. IV opening): `"Each route is closed at the / amplitude level rather than only at the structural level."` — uncalibrated. Conclusions L2624-2625 already has the correct framing: `"Routes / R1--R3 close at the amplitude level under explicitly-labeled scaling / ans\"atze; route R4 is closed instead by a naturalness ... objection"`. So Sec. IV opening is genuinely inconsistent with Conclusions. | **FIX**: replace L1334-1335 with: "R1--R3 are closed at the amplitude level under the explicitly-labeled scaling/ansatz assumptions stated below; R4 is closed at the level of a naturalness / explanatory-deficit objection rather than an amplitude exclusion (Sec.~\ref{sec:r4_birefringence})." |
| 3 | ChatGPT F65-M2 | Fig. 4 caption (`fig:obs_timeline`) says surveys deliver "parameter-independent" discrimination and joint outcome "falsifies the surviving ECH framework or leaves it as the unique surviving minimal-ECH channel" (MAJOR) | **VERIFIED** | L1860-1864: `"Both surveys deliver / parameter-independent, ECH-independent class-level discrimination tests; the / joint outcome falsifies the surviving ECH framework or leaves it as the / unique surviving minimal-ECH channel under the stated / ans\"atze."` Body already says the surviving tests are *class-level* probes of (a) a scalar-only $w\!=\!0$ matter-bounce and (b) a uniform spectator-ALP benchmark, neither of which is a unique ECH prediction (L2436: `"neither is / uniquely an ECH prediction"`). Caption overstates relative to body. | **FIX**: replace L1860-1864 with: "Both surveys deliver ECH-independent class-level discrimination tests; under the stated ans\"atze they can falsify the relevant matter-bounce and uniform spectator-ALP benchmarks, but they do not identify a unique surviving minimal-ECH channel." |
| 4 | ChatGPT F65-M3 | Public reproducibility README labels the bundle as v1A.0.64 while the reviewed PDF is v1A.0.65; Zenodo DOI still "to be inserted" (MAJOR) | **PARTIAL / HOUSTON-DECISION** | Truth-audit cannot fully verify the GitHub README state from inside the bigbounce repo without a checkout. The .tex itself (L25xx Data and Code Availability) names the Zenodo DOI as pending — this is HD-11 ruled (DOI placeholders are legitimate pre-submission state). README sync to v1A.0.65 is a real housekeeping item, but it is a public-bundle sync, not a paper-content finding. | **FIX**: in the next paper-bundle sync wave, retag the public-bundle README/BibTeX/known-gaps metadata to v1A.0.65 and state whether v1A.0.65 ↔ v1A.0.64 are byte-identical on data. Insert Zenodo DOI at submission. Not a same-commit blocker. |
| 5 | ChatGPT F65-M4 | "Tests of $\gamma$" still too strong without a derived $\gamma$-dependent observable (MAJOR) | **PARTIAL** | The paper does discuss parity-sensitive channels under "tests of $\gamma$" framing (Introduction + conclusions), while simultaneously stating that the ALP benchmark is ECH-independent and that no photon-torsion coupling is derived. ChatGPT's reframe ("parity-sensitive channels outside the scalar/tensor transparency sector ... become tests of $\gamma_{\rm BI}$ only in a model that derives a $\gamma_{\rm BI}$-dependent photon or tensor-parity coupling") is correct and cheap. | **FIX**: grep for "tests of $\gamma$" / "test of $\gamma$" and at each hit reframe to "parity-sensitive channels (model-dependent tests of $\gamma_{\rm BI}$ only under a derived $\gamma_{\rm BI}$-dependent photon or tensor-parity coupling)". |
| 6 | ChatGPT minor — Fig. 6 caption "decisive (≳5σ)" vs Table I 2.6–5σ realistic | **VERIFIED** | L2429-2431: `"The SPHEREx f_{\rm NL} forecast is / decisive (\gtrsim 5\sigma on Stage~III/IV survey timescales) against / f_{\rm NL}=0"` while Table I footnote b consistently gives 2.6–5σ realistic. Wording asymmetry. | **FIX**: replace "decisive ($\gtrsim 5\sigma$ on Stage~III/IV survey timescales) against $f_{\rm NL}=0$" with "potentially decisive in optimistic configurations; $2.6$–$5\sigma$ after the stated systematic budget (Table I footnote b)". |
| 7 | ChatGPT minor — Sec. X B Step 5 ("total derivative contributes nothing") redundant | **OPINION** | L2156-2161 already justifies why Step 5 is retained — it covers the residual Nieh–Yan boundary term $d(e_I\wedge T^I)$ at nonzero torsion, distinct from the Bianchi-vanishing of the previous step. The explicit justification is in the body. Not a closure-blocking issue. | **DEFER**: keep as written; the in-text justification is sufficient. |
| 8 | ChatGPT minor — "Four-Route No-Go" Sec. IV title too strong | **OPINION** | Sec. IV title is a stylistic choice. The body now scopes the closure correctly as channel-level under stated ans\"atze. Reviewer prefers "Four-Route Channel Audit"; both are defensible. | **DEFER**: HOUSTON-DECISION on title rename. |
| 9 | ChatGPT minor — PACS keywords | **OPINION** | L9 declares `showpacs`, L600 has the PACS line. revtex4-2 PRD style still accepts PACS. Until target journal is final, leaving them is defensible. | **DEFER**: HOUSTON-DECISION at journal submission. |
| 10 | ChatGPT minor — "Pop lawski" / "Domaga la" diacritics rendered without accents | **VERIFIED (cosmetic)** | Source uses `Poplawski` (L665) without LaTeX accent commands and `Domaga\l{}a` (L849, L850) which renders correctly in PDF but extracts oddly via pdftotext. The reviewer is seeing pdftotext-extraction artifacts. L665 `Poplawski` ↔ proper Polish is `Popławski` and could use `Pop\l{}awski`. Cosmetic. | **FIX (cheap)**: replace `Poplawski` → `Pop\l{}awski` everywhere (L665, L669, L1898). Confirm Domaga\l{}a renders. |
| 11 | Grok minor — TOC has stray "Falsification Criteria" entry (body is "Falsifiability Criteria") | **FALSIFIED** | Body L1849: `\section{Falsifiability Criteria}`. TOC (`paper1a_ech_nogo.toc` L31): `"Falsifiability Criteria"`. The only "Falsification" string in the source is the changelog comment block at L177-178 documenting the historical R29 rename. HD-6 ruled: changelog comment = deliberate transparency. Grok is reading a comment block, not a live overflow. | **NO ACTION**. |
| 12 | Grok minor — Sec. IX (Barrier 14) repeats "channel-level not operator-level" disclaimer | **OPINION** | Disclaimer redundancy across abstract / Sec. IV Scope / Sec. IX / Sec. XIII is intentional belt-and-suspenders scoping after R34conf/R35conf amplitude-closure overclaim sweep. Trimming risks reopening pattern-008 (scope drift). | **DEFER**: keep belt-and-suspenders. |
| 13 | Grok minor — Table I footnote b "stray 3–5σ" survived from earlier draft | **FALSIFIED** | grep over `arxiv/paper1a_ech_nogo.tex` for "3--5\sigma" / "3-5\sigma" / "3 to 5\sigma" returns 0 hits. Every SPHEREx forecast quote across the paper (L582, L691, L696, L1859, L1874, L1875, L1880, L2262, L2264, L2425, L2469, L2472, L2654) reads "2.6--5\sigma". Grok hallucinated the stray phrase. pattern-052 re-raise rule does not apply — there is no prior falsification record because this finding never existed in source. | **NO ACTION**. |
| 14 | Grok minor — Sec. II C 1 Eq. (4) shows "N" instead of κ in pdftotext extraction | **FALSIFIED (rendering artifact, not source bug)** | Grok itself flags this as "PDF extraction shows 'N'... context and prior versions confirm this is a rendering artifact for κ (gravitational constant). Not substantive, but visually confusing. Already correct in source .tex." This is a pdftotext extraction artifact, not a source defect. The pdftotext-driven review failure mode is exactly what `[feedback-review-gap-native-pdf]` standing directive guards against — but EXT6 used native PDF, so Grok's vision model misread the rendered glyph. | **NO ACTION**. |
| 15 | Gemini Major — Section XII.A fine-tuning score reduction (10^120 → 10^5) needs an explicit caution that it is a reparameterization, not a resolution | **FALSIFIED** | The caution Gemini requests already exists explicitly: L2336-2352 `"The "fine-tuning reduction from 10^{120} to 10^5" is a reparameterization / as sensitivity to N_{\rm tot} (the total number of inflationary e-folds), / not a resolution of the cosmological constant problem ... the "reduction from 10^{120} to 10^5" should be read as a / qualitative dimensional rearrangement rather than a quantitative / bookkeeping result."` Fig. 5 caption (L1929-1933) also says: `"per / Sec.~\ref{sec:gdp} this is a reparameterization of the / cosmological-constant problem as sensitivity to N_{\rm tot}, / \emph{not} a resolution."` Two independent sites already carry the caution. Gemini missed both. pattern-052 does not apply (no prior falsification record). | **NO ACTION**. |
| 16 | Gemini minor — Table I "Result" cell for $f_{\rm NL}$ should split ideal / degraded inline | **PARTIAL / OPINION** | L685 cell reads `"\fnl = -35/8 (Paper~II forecast$^b$)"` with footnote b at L691-696 carrying the split bounds. Gemini wants `"\fnl = -35/8 (\sigma\approx 0.7 ideal \to 1.0 sys)"` inline. Both are valid. Inline is more scannable; footnote is cleaner table layout. | **DEFER**: HOUSTON-DECISION on table-cell scannability vs. footnote convention. |

---

## Counts summary

| Verdict | Count |
|---------|-------|
| VERIFIED | 4 (#1 BLOCKER, #2 MAJOR, #3 MAJOR, #6 MINOR) + 1 cosmetic (#10) = 5 |
| PARTIAL | 2 (#4, #5) |
| OPINION | 4 (#7, #8, #9, #12) |
| FALSIFIED | 4 (#11, #13, #14, #15) |
| HOUSTON-DECISION | 2 embedded in PARTIAL/OPINION (#4 README sync timing, #16 table cell format) |
| STALE | 0 |
| **Total** | **16** |

**Genuinely-NEW-substantive count (EXT6 gap metric)**: **4**
- #1 Sec. IV E condensate stale-sign survivor (real internal contradiction, R35conf missed it)
- #2 Sec. IV opening uncalibrated amplitude-closure (real inconsistency with Conclusions)
- #3 Fig. 4 caption "parameter-independent" / "unique survivor" overstatement (real)
- #6 Fig. 6 caption "decisive ≳5σ" inconsistent with Table I 2.6–5σ realistic (real)

Findings #4, #5 are PARTIAL but already partially-acknowledged in the manuscript (DOI pending; γ-test framing already softened in places). They are real but smaller-edit closure items.

**Headline finding**: ChatGPT's BLOCKER on the NJL claim is **NOT a stale read** and **NOT an audit-trail changelog artifact** — it is a **real regression** at L1786-1791 of Sec. IV E. R35conf correctly fixed the Route 1 body prose (lines 1411-1436) into the (i)+(ii) leg split with $\rho_{\rm NJL}\!\sim\!4\!\times\!10^{-69}\rho_\Lambda$, but the Sec. IV E closure-summary paragraph still carries the pre-R34conf "parametrically too large" sentence. This is the *exact failure mode* of the R34conf → EXT5 → R35conf wave: each fix touched one site, but the closure-summary synthesis paragraph survived unedited because nobody grep'd the full manuscript for "too large" / "condensate" residues. This is a textbook pattern-026 (multi-site claim sync gap) instance.

Grok's "ACCEPT" recommendation is **unsafe** in light of finding #1 (their fresh pass missed a live internal contradiction). Gemini's "ACCEPT WITH MINOR REVISIONS" misses the same blocker. Only ChatGPT caught it.

---

## CLOSURE PLAN — one-line edits for every VERIFIED / PARTIAL

1. **#1 BLOCKER (Sec. IV E NJL stale-sign)** — rewrite `paper1a_ech_nogo.tex` L1786-1791 to the parametrically-far-below + parity-even + no-coherent-$w\!=\!-1$ phrasing in the Disposition column. Then `grep -n "too large\|overshoot\|parametrically.*condensate\|condensate.*parametrically" arxiv/paper1a_ech_nogo.tex` and sweep any remaining hits.
2. **#2 MAJOR (Sec. IV opening uncalibrated)** — rewrite L1334-1335 to the R1--R3 amplitude / R4 naturalness phrasing.
3. **#3 MAJOR (Fig. 4 caption overstates)** — rewrite L1860-1864 to drop "parameter-independent" and "unique surviving minimal-ECH channel".
4. **#5 PARTIAL ("tests of γ")** — grep + reframe each "tests of $\gamma$" / "test of $\gamma$" hit to the model-dependent caveat.
5. **#6 MINOR (Fig. 6 "decisive")** — rewrite L2429-2431 to the optimistic-configurations / 2.6–5σ after systematic budget phrasing.
6. **#10 cosmetic (Pop\l{}awski diacritic)** — replace `Poplawski` → `Pop\l{}awski` at L665, L669, L1898.
7. **#4 PARTIAL (README sync)** — deferred to next paper-bundle wave (not same-commit).
8. **#8, #9, #16 (HOUSTON-DECISION items)** — surface at next bump for Houston to call.

**Estimated closure commit**: one `chore(R36conf-stamp): EXT6 P1A → v1A.0.66 closure wave — Sec.IV E NJL stale-sign fix + Fig.4/Fig.6 caption calibration + amplitude-closure scoping sync` bundle. Single restamp.

---

## Audit notes

- **HD-6 (changelog-comment ruling)** applied to Grok minor #11 (TOC "Falsification Criteria" = changelog block reading).
- **HD-11 (DOI placeholder)** applied to ChatGPT F65-M3 (Zenodo DOI "to be inserted" pre-submission).
- **pattern-052 (re-raise vindication)** does not apply to any FALSIFIED finding here — none of the falsified items have prior falsification records that would auto-rescue a re-raise.
- **pattern-026 (multi-site claim sync gap)** triggered by finding #1; reinforces the standing requirement to grep the full manuscript for stale phrasings after every targeted scientific-content edit, not just the targeted lines.
- **No fabrication / Fisher-1/8.98² superscript artifacts** appeared in this round.
