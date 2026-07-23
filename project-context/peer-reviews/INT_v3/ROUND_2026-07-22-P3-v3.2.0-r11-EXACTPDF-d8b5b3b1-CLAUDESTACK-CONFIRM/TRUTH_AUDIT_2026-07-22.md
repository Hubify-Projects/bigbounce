# TRUTH AUDIT — P3 v3.2.0-r11 confirmation board (2026-07-22)

- **Paper:** P3 "Public-ID Recovery for a Historical DESI DR1 Anomaly List" — ApJS catalog paper
- **Version / PDF SHA-256:** v3.2.0-r11 / `d8b5b3b1e7cb802a2661f9e800b2b7a5fc4c09dcda7771ae731771afdb6f297a`
- **Round:** ROUND_2026-07-22-P3-v3.2.0-r11-EXACTPDF-d8b5b3b1-CLAUDESTACK-CONFIRM
- **Tex source of truth:** `pipelines/p3_anomaly_engine/paper3_apjs.tex`
- **Board:** Grok API = ACCEPT (2 minor); Gemini API = MAJOR-REVISIONS (3 MAJOR + 1 minor); Claude INT = MINOR-REVISIONS (1 MAJOR-severity + 1 minor)
- **Auditor:** Claude Opus 4.8 (truth-audit leg), verdict-first, source-cited

## Verdict rule
Each finding → exactly one of ALREADY-TRACKED-GATE / DISCLOSED-RE-FLAG / SCOPE-VENUE-OPINION / FALSIFIED / GENUINELY-NEW-REAL (in doubt → GENUINELY-NEW-REAL).

---

## Finding-by-finding matrix

| # | Reviewer / severity | Finding (short) | Verdict | Source-cited basis |
|---|---------------------|-----------------|---------|--------------------|
| 1 | Claude / MAJOR | Paper asserts r11 "added to the same Zenodo record as a new version," but concept DOI 21461887 resolves to record 21461888 = r10 only | **GENUINELY-NEW-REAL** | tex L913–915 states as-completed; `curl -sIL doi.org/10.5281/zenodo.21461887` → `records/21461888`; Zenodo API `records/21461888` → `version:"3.2.0-r10"`, `pubdate 2026-07-20`, `conceptdoi 10.5281/zenodo.21461887`. No r11 version record exists on the concept. The self-referential archival claim is verifiably premature. |
| 2 | Gemini / MAJOR-3 | Text calls the 11-observed vs 75.56-expected 0.1–1″ annulus comparison "chance-compatible"; that is a ~7σ deficit | **GENUINELY-NEW-REAL** | tex L419 "consistent with chance" and L437 caption "chance-compatible." Recompute: λ=75.56, k=11 → P(X≤11)=2.05×10⁻²⁰; deficit = 7.43σ (Poisson) / 4.96σ (empirical shifted SD 13.01); 11 is far below the shifted range 61–101. The words mislabel a large **deficit** as compatible. Honesty-critical wording fix. NOTE: the *body already gives the correct origin* (L420–423: core self-recovery consumes each cluster's nearest-neighbor slot inside 0.1″), so Gemini's suggested fiber-collision/dedup origin is NOT needed and must not be fabricated — fix wording only. |
| 3 | Gemini / MAJOR-1 | No astrophysical context: paper should summarize what physical features / spectral morphologies the upstream BigAE flagged | **SCOPE-VENUE-OPINION** | Paper deliberately scopes this out: §1 L121–127 "The recovery uses the historical anomaly stream only as a source of coordinates and score metadata … rather than a claim about the prevalence, novelty, or physical origin of anomalous spectra"; abstract L70 states it "cannot reconstruct the unavailable production normalization or physical-feature sensitivity." Ledger: DP3-16 (OPEN-VENUE / presentation OPINION, Houston-gated) + DP3-07/-09/-11 (not-a-discovery framing). Requesting physical characterization the paper honestly declares unavailable = venue-scope opinion, not a defect. |
| 4 | Gemini / MAJOR-2 | No plots of the actual DESI spectra for representative candidates | **SCOPE-VENUE-OPINION** | Paper is an ID-recovery/provenance catalog: §1 L121–127 + abstract L96–97 "reproducible follow-up lists, not validated detections or unbiased samples." Reviewer explicitly wants to "bridge the gap between a database join and an astrophysical resource" — precisely the scope the paper deliberately declines. Ledger: DP3-16 (OPEN-VENUE). A representative-spectra figure is an OPTIONAL non-blocking strengthener Houston may add at discretion; its absence is not a real finding against a deliberately-scoped provenance paper. |
| 5 | Gemini / minor | Forward-dated July 20 2026 timestamps + "unreleased Apple M5" hardware | **FALSIFIED** | Today is **2026-07-22** → the July 20 2026 timestamp (tex L32 `\paperTimestamp`) is 2 days in the PAST, not forward-dated. Apple M5 exists; tex L272–276 states the "Apple M5 (10-core, 24 GB RAM) reference machine used to reproduce it here," and L272–273 honestly notes "the release does not pin that machine's hardware." Reviewer training-cutoff artifact — the paper reports actual dates and actual hardware. |
| 6 | Claude / minor | Version-tag key footnote defines r2/r5/r7/r11 but body uses r1/r3/r4/r6/r10 | **GENUINELY-NEW-REAL** | Footnote tex L167–172 enumerates only `\releaseVersion`/`\warnedAuxVersion`/`\bundleVersion`/`\paperVersion` = r2/r5/r7/r11 (macro defs L45–48, L31). Body additionally uses r1, r3, r4, r6, r10 (per Claude INT report; e.g. Zenodo "reviewed v3.2.0-r10," aas_submission…-r4, r6 controls). Footnote presents itself as *the* key but doesn't map every RC tag. Minor-severity real gap. |
| 7 | Grok / minor-1 | 0.1″ quality-tier boundary introduced post-hoc, could appear circular | **DISCLOSED-RE-FLAG** | Paper already discloses the tier is descriptive-only and not a selection cut: abstract L82–83 "A quality-tier column exposes this contract without silently changing the declared 1″ list; neither tier is a secure object-identity or purity claim." Grok itself notes it is "explicitly acknowledged as descriptive only." Placement suggestion only. |
| 8 | Grok / minor-2 | Zenodo DOI listed "pending" in one place while minted DOI given elsewhere | **DISCLOSED-RE-FLAG** | The paper distinguishes two DOIs: the **AAS journal digital-asset DOI** (honestly "pending / not yet assigned," tex L905, L916–919) vs the **Zenodo archival DOI** (minted, L910–911). No contradiction — different objects. (The genuinely-real Zenodo issue is finding #1's tense, not a pending/minted conflict.) |

---

## GENUINELY-NEW-REAL FIX LIST (exact tex edits, `pipelines/p3_anomaly_engine/paper3_apjs.tex`)

### FIX 1 — Zenodo r11 tense (finding #1)
The archived record pins the reviewed r10 bytes; r11 is one patch ahead and is NOT yet on the concept DOI. Reword to the accepted P2/P4 convention (archive pins reviewed prior version; current version added on next re-stage). **Do NOT fabricate an r11 deposit.**

- **L913–915**, replace:
  `That deposit archives the reviewed \texttt{v3.2.0-r10} bytes; the present manuscript is \texttt{v3.2.0-r11}, added to the same Zenodo record as a new version.`
  **with:**
  `That deposit archives the reviewed \texttt{v3.2.0-r10} bytes exactly; the present manuscript is \texttt{v3.2.0-r11}, one patch ahead, and will be added to the same Zenodo concept record as a new version on the next re-stage.`

- **L912–913**, replace the parenthetical tail:
  `resolves to the latest deposited version, to which this and later versions are added`
  **with:**
  `presently resolves to the latest deposited version (\texttt{v3.2.0-r10}), to which subsequent versions will be added`

### FIX 2 — "chance-compatible" mislabel (finding #2)
Report the 11-vs-75.56 relationship truthfully as a large **deficit**, keep the already-in-paper origin (core self-recovery slot-consumption), do NOT introduce a fiber-collision/dedup claim.

- **L418–420**, replace:
  `The local-shift control is informative only for the $0.1$--$1\arcsec$ tail, where the 11 observed rows against a shifted mean of 75.56 are consistent with chance and do not acquire secure candidate-level identity from positional coincidence alone.`
  **with:**
  `The local-shift control is informative only for the $0.1$--$1\arcsec$ tail. There the 11 observed rows fall well below the shifted mean of 75.56 --- a deficit, not an excess. The shifted realizations are correlated local controls rather than an independent Poisson null, but the shortfall is large and is a direct corollary of the core self-recovery described below, so the 11 tail rows do not acquire secure candidate-level identity from positional coincidence alone.`

- **L436–437** (figure caption), replace:
  `alongside the shift-controlled $0.1$--$1\arcsec$ tail, where the observed and shifted counts are chance-compatible.`
  **with:**
  `alongside the shift-controlled $0.1$--$1\arcsec$ tail, where the observed count (11) falls well below the shifted mean (75.6) because each core cluster's nearest-neighbor slot is consumed by its own seed inside $0.1\arcsec$; the tail is therefore not treated as secure candidate identity.`

### FIX 3 — Version-tag key completeness (finding #6)
- **L167–172 footnote**, either (a) enumerate the missing tags, or (b) mark the key illustrative. Minimal edit (append inside the footnote, after `\paperVersion{} this manuscript.`):
  `Body references to intermediate release-candidate tags (e.g.\ \texttt{r1}, \texttt{r3}, \texttt{r4}, \texttt{r6}, \texttt{r10}) denote further frozen build/audit/submission checkpoints of the same program; this key lists the load-bearing component versions rather than every checkpoint.`

---

## Verdict-class summary

| Class | Count | Findings |
|-------|-------|----------|
| GENUINELY-NEW-REAL | 3 | #1 Zenodo r11 tense, #2 chance-compatible mislabel, #6 version-tag key |
| SCOPE-VENUE-OPINION | 2 | #3 astrophysical context, #4 spectra plots |
| FALSIFIED | 1 | #5 July-20 dates + Apple M5 (reviewer training-cutoff artifact) |
| DISCLOSED-RE-FLAG | 2 | #7 0.1″ tier placement, #8 Zenodo pending/minted |
| ALREADY-TRACKED-GATE | 0 | — |

**Board disposition:** 3 genuinely-new real items, all discrete factual/wording corrections touching NO catalog science and requiring no re-review of substance. Gemini's two remaining MAJORs are venue-scope opinions against a deliberately-declared ID-recovery paper; its minor is a training-cutoff artifact (FALSIFIED). Grok's two minors are disclosed re-flags. Applying FIX 1–3 closes every genuinely-new real finding.
