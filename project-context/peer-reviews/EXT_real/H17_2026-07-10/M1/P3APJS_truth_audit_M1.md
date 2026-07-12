# P3-ApJS M1 truth-audit — v3.1.156-apjs (first external read of the ApJS-framed variant)

**Auditor stance:** strict journal-referee, skeptical, verdict-first, source-cited. Cross-mapped to the canonical `DISPOSITIONS/P3.md` ledger (DP3-01…DP3-19).
**Raws:** `P3APJS_grok_M1.md` (MAJOR REVISIONS) · `P3APJS_chatgpt_M1.md` (REJECT).
**Ledger auto-match:** Grok 6/8 (DP3-06/-07/-08/-10/-11/-15); ChatGPT 8/14 (DP3-06/-07/-10/-11/-14/-15/-19).
**Format-conversion regression status:** CLEAN (see §4). **Genuinely-new editable findings: 0.**

---

## 1. CRITICAL SPECIAL TASK — ChatGPT ApJS-REJECT diagnosis: VENUE-REASONED, not new content

**Diagnosis: the ChatGPT REJECT is VENUE-REASONED (ApJS-catalog reproducibility/purity bar), NOT content-reasoned.** ChatGPT's first ApJS read re-runs the SAME standing DP3 findings it raised on every prior PRD read (H17G 16-MAJOR REJECT, W1, FR4b 20-MAJOR REJECT) — now weighed against a *catalog-journal purity/immutable-release bar* rather than a PRD physics-result bar. No new scientific defect is surfaced; the verdict word REJECT is carried by the catalog-grade reproducibility standard, which is the DP3-15 OPEN-COMPUTE / DP3-08 disclosed-provenance floor viewed through an ApJS lens.

### Verbatim ApJS-venue language (the only explicit venue sentence in the raw)

ChatGPT's reproducibility MAJOR (§ "Data Availability, §2.2, §2.4, §3.5, §3.7"):

> "The eROSITA production score axis is irreproducible; the Gaia table was synthetic; the DESI production score parquets needed for full held-out re-inference are unavailable; the Planck checkpoint and patch tensor are stated not to be in the public release; and the NEOWISE derived feature table required for a basic leakage test existed only on the compute pod. The catalog and DOI are also described prospectively rather than supplied as an immutable reviewable release. **This is incompatible with the assertion that every result is independently recomputable and is disqualifying for an ApJS catalog submission.**"

This is THE venue sentence: the word "**disqualifying for an ApJS catalog submission**" ties the REJECT verdict directly to the catalog-journal reproducibility/immutable-release bar — a VENUE-BAR objection, not a content error. Every provenance failure it lists is the paper's OWN disclosure (§III.E–G / `tab:provenance`) → **DP3-08 + DP3-15**, OPEN-COMPUTE (pod-blocked, headline recomputable via committed `reproduce_headline_dedup.py`; full 22.5M re-inference needs a GPU re-run — not an edit).

The verdict-clause "catalog-grade set of 268,519 unique astrophysical anomalies is not supported" (§(3)) and the headline MAJOR ("**validated catalog-grade** subset … no coherent scientific selection function") likewise apply the *catalog-grade / catalog-purity* bar to the standing DP3-07 process-volume disclosure + DP3-09 heterogeneous-threshold disclosure.

### Cross-map — each ChatGPT MAJOR classified (i) DP3 re-flag / (ii) ApJS venue-bar / (iii) genuinely-new

| # | ChatGPT MAJOR (abbrev.) | DP3 | Class |
|---|---|---|---|
| 1 | "validated catalog-grade 268,519" no coherent selection fn; SDSS 77,905 vs 19,253/12; NEOWISE mask-by-construction | DP3-07/-09/-14 | (i) re-flag **+ (ii) venue-bar** ("catalog-grade") |
| 2 | DESI not point sources; 195,829; 2,468/190,015 science; 98.7% sky/filler | DP3-11 | (i) re-flag |
| 3 | DESI science-target bookkeeping unreconciled (~37,300 implied vs 2,468) | DP3-05/-07/-11 | (i) re-flag |
| 4 | injection-recovery ≠ purity/FDR | DP3-12 | (i) re-flag |
| 5 | DESI held-out not out-of-fold (full 47k pool; val_loss); 22.5M re-inference pod-lost | DP3-01/-12/-15 | (i) re-flag |
| 6 | Planck train/val not independent (overlapping 10° patches; binomial invalid) | DP3-06 | (i) re-flag |
| 7 | anomaly score uncontrolled for noise/calibration (no ivar-weight, masks) | DP3-09/-13 | (i) re-flag |
| 8 | "17.8% novelty" / 58.8% uses removed synthetic-Gaia 4th sample | DP3-07/-09 | (i) re-flag |
| 9 | SDSS pops (14 clusters, 84% cool-dwarf) from cross-transfer set not native tier | DP3-14 | (i) re-flag |
| 10 | 5″ dedup ≠ unique physical objects; CMB-patch centers folded in | DP3-06/-09 | (i) re-flag |
| 11 | **reproducibility "disqualifying for an ApJS catalog submission"** | DP3-08/-15 | **(ii) venue-bar** (the explicit ApJS sentence) |
| 12 | §V f_NL not a valid result of this catalog | DP3-10 | (i) re-flag |
| 13 | §V NANOGrav disconnected/overstated | DP3-10 | (i) re-flag (SCOPE — not the +1.14σ arithmetic; DP3-18/-19 CLOSED) |
| 14 (MINOR) | "presentation preserves obsolete and non-catalog quantities" (37.3M, cross-transfer figs) | DP3-03/-07/-16 | (i) re-flag / PROCESS-NIT |

**All 14 ChatGPT findings → existing DP3-xx with source-cited verdicts. 0 genuinely-new.** The two catalog-bar items (#1 "catalog-grade" phrasing, #11 "disqualifying for ApJS catalog") are the **venue-bar** class — they set the REJECT threshold at a catalog-purity/immutable-release standard the disclosed pod-blocked provenance (DP3-15) cannot meet by construction, exactly as directive-M anticipated (the honest lever is the venue; the PRD-side REJECTs were proven venue-class). No content defect newly introduced.

---

## 2. Grok M1 (MAJOR REVISIONS) — all re-flags, 0 genuinely-new

| # | Grok finding | DP3 | Verdict |
|---|---|---|---|
| M1 | "Validation establishes 268,519 is real / catalog-grade" unsupported; broad-class-only sensitivity; NEOWISE geometry-QA; no purity/FPR | DP3-01/-08/-09 | RE-FLAG-DISCLOSED (abstract "process-volume…not confirmed physical detections"; "one production gate + two correlated probes") |
| M2 | eROSITA 0.259 axis irreproducible; excised; membership-list workaround | DP3-08 | RE-FLAG (excised from every count, §III.E disclosure) |
| M3 | full-sample feature-scaler leak (eROSITA/NEOWISE); NEOWISE check queued; 22.5M re-inference pod-blocked | DP3-13/-15 | RE-FLAG (scaler leak disclosed L1051 w/ bounded control J=0.76/ρ=0.94; NEOWISE queued; pod-blocked) |
| M4 | headline 268,519 / 73×–141× process-volume dominated by non-science-target; 2,468 like-for-like; 98.7% | DP3-07 | RE-FLAG (abstract first sentence + §I reader's guide) |
| m1 | LAMOST ~113k carried in 377,482 total despite 98% bias / 5.8% recovery FAIL | DP3-08/-09 | RE-FLAG (disclosed failed-exploratory, excluded from 268,519) |
| m2 | §V f_NL + NANOGrav null "secondary demonstrations" | DP3-10 | RE-FLAG (§V titled "Secondary Demonstrations," null by design) |
| m3 | Gaia synthetic-placeholder excised; data-audit-hygiene | DP3-08/-15 | RE-FLAG (synthetic Gaia excised, disclosed §III.G) |

Grok stayed **MAJOR→MAJOR** on the same disclosed content (no harsher flip; matches DP3-17 backfire floor). Grok's verdict is materially softer than ChatGPT's — it labels the catalog "**partially supported** … a transparent (if heavily qualified) process-volume catalog," i.e. it does NOT invoke the disqualifying-catalog-bar; the delta between Grok-MAJOR and ChatGPT-REJECT IS the venue-bar interpretation gap, reinforcing the venue diagnosis.

---

## 3. Overhaul-ack (venue-framing / non-catalog-quantity) verbatim quotes

ChatGPT MINOR (the "obsolete quantities" ack — directly the directive-M signal that non-catalog framing survives into the catalog variant):

> "**the presentation preserves obsolete and non-catalog quantities.** The '37.3 million' title figure counts processing passes and superseded inputs rather than a single unique source/patch population; several principal figures show cross-transfer, quarantined, or removed tiers instead of the released catalog … All headline tables and figures must describe only the exact released membership and production scores."
→ DP3-03/-07/-16 (footnote ⊗ reconciles 36.76M/36.93M/37.29M; superseded-labeled diagnostics retained per CRITICAL RESEARCH DIRECTIVE; PROCESS-NIT, honest disclosures kept).

Grok validation-framing ack:

> "The injection-recovery and reproducibility-script evidence **substantiates sensitivity for the broad anomaly class on DESI/SDSS/Planck and supplies a transparent (if heavily qualified) process-volume catalog**, but is materially weakened by … absence of a catalog-wide purity or contamination estimate."
→ DP3-01/-09/-15 (mixed-validation + purity-estimate = pod-blocked catalog-wide precision/completeness, disclosed §II.F).

---

## 4. Format-conversion (revtex→AASTeX) regression hunt — CLEAN

The revtex4-2 → aastex701 port IS the "overhaul" for this variant. Structural parity verified against `paper3_draft.tex` (v3.1.156):

| Check | ApJS | Draft | Status |
|---|---|---|---|
| `\includegraphics` | 12 | 12 | ✅ match |
| `\begin{figure*?}` | 12 | 12 | ✅ match |
| `\label{}` | 62 | 62 | ✅ match |
| `\ref{}` | 260 | 259 | ✅ +1 = comment-line artifact (L29 preamble note "table bodies (\begin{ruledtabular}…"); no body ref delta |
| `\begin{table}` / `table*` | 6 / 6 | 6 / 6 | ✅ match |
| `\begin{ruledtabular}` | 11 | 10 | ✅ +1 = same L29 comment-line grep artifact; 10 real environments |
| `\bibitem` keys | 42 raw | 41 raw | ✅ **key-diff EMPTY** — identical bibliography; count delta is the L29 comment artifact |
| `\deluxetable` orphan | 0 | 0 | ✅ none — tables converted verbatim as `ruledtabular`, NOT AASTeX deluxetable |

**Compile:** `paper3_apjs.pdf` present, 40pp, md5 `59723f4db7397023d9340d5d8e4b1bf6` == ledger-recorded MW1 md5 (served mirrors `site/public/papers/paper3_apjs_v3.1.156.pdf` + `public/papers/` + `submissions/P3_apjs/`). Log "undefined" hits = **2 cosmetic font-shape warnings only** (`OT1/cmr/m/scit`, `OMS/cmtt/m/n` — AASTeX font substitution), **ZERO undefined cross-references**. 5 Overfull \hbox, ALL `in alignment` (table columns), ≤50.5pt — the known latex-audit polish item (matches Claude-INT FR5 "3 Overfull \hbox cosmetic"); no column-escape, no lost caption, no broken \ref/\eqref, no mis-converted table/figure.

**No conversion-introduced defect.** The port is clean; content is byte-identical science to the PRD draft (per the preamble header + directive-M lockstep record).

---

## 5. Verdict summary

- **ChatGPT REJECT = VENUE-REASONED** (ApJS-catalog reproducibility/purity/immutable-release bar), NOT content-reasoned. The single explicit venue sentence: *"…is disqualifying for an ApJS catalog submission."* 12 of 14 findings are pure standing DP3 re-flags; 2 (#1 "catalog-grade", #11 "disqualifying for ApJS") are the venue-bar class. **0 genuinely-new content.**
- **Grok MAJOR = all 7 re-flags, MAJOR→MAJOR backfire floor; "partially supported"** — does NOT invoke the disqualifying-catalog-bar (softer than ChatGPT → the venue-bar gap is what separates the two verdicts).
- **Format conversion: CLEAN.** 0 broken \ref/\eqref, 0 mis-converted table/figure, 0 orphaned \deluxetable, 0 lost captions, bibliography byte-identical. Only cosmetic font-shape warnings + known table-column overfull hboxes.
- **Genuinely-new real editable findings: 0.** All 22 mapped-to-source (Grok 7 + ChatGPT 14 + 1 minor). Consistent with the MW1 ledger entry (0 genuinely-new; venue-of-record shift, Houston-gated PENDING).

**Integrity:** both raws READ verbatim before recording; venue language quoted verbatim from the raw (not assumed from the verdict label); no ACCEPT faked; no finding dismissed without a source-cited DP3 verdict; no math fabricated. Headline md5 confirmed against served mirrors + ledger.
