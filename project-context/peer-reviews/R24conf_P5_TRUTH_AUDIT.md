# R24conf P5 — TRUTH AUDIT (remaining findings after INSESSION wave)

**Auditor**: Claude (in-session), 2026-06-10, against `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.53 → v0.1.54 working tree)
**Scope**: all R24conf SYNTHESIS + META_REVIEW findings NOT already closed in the Claude_brutal_INSESSION wave.
**CLOSED-PRIOR (untouched, STALE here)**: INSESSION M1 (abstract sample-ledger sentence), M2 (≲0.002 framing + 1.2σ counting-floor parenthetical, 3 sites); Claude_brutal m1–m20 are recompute all-clears (paper numbers reproduced) — no action by construction.

## ESSENTIAL findings

| ID | Sev | Claim | Verdict | Disposition |
|----|-----|-------|---------|-------------|
| META-E1 | ESS | T-Web density field CIC-deposited from 14,622,283 rows, not 14,100,704 unique TARGETIDs → multiply-coadded targets over-weighted | **VERIFIED** | Factually correct per §IV.A/§VIII.F. §IV.A step 4 now discloses the row-level deposit (521,579 repeat rows, 3.6%) and queues the deduplicated rebuild (pod). **CLOSED (disclosure) + Queue #15 (rebuild).** |
| Grok-E1 | ESS | Raw σ values juxtaposed with headline null without comparability qualifier at the juxtaposition | **STALE** | Abstract states "scale as √n … not mutually comparable" immediately after the four values (R23conf closure); §V + Table II caption repeat it. |
| Grok-E2 | ESS | Remove "earlier draft / superseded" language | **HOUSTON-DECISION** | Deliberate disclosure policy (standing rule). Not touched. |
| Grok-E3 | ESS | Post-hoc primary-path designation violates pre-registration | **STALE** | §V.B declares the post-hoc designation explicitly and reports all paths (R23conf OpenAI-E4 closure). |

## MAJOR findings

| ID | Sev | Verdict | Disposition |
|----|-----|---------|-------------|
| META-M1 (angular completeness) | MAJ | **VERIFIED→QUEUED** | No tiling/completeness weighting in δ — true. §IX.A limitation sentence added (mask/buffer/NSIDE-64 are the current controls); randoms-weighted rebuild = Queue #16. |
| META-M2 (Jeffreys CIs on duplicate parent) | MAJ | **VERIFIED** | Fig 3 caption now carries the worst-case design-effect bound √(812,793/783,820)=1.018 (≤1.9% width underestimate) + pointer to unique-subset χ². **CLOSED (textual, arithmetic shown).** |
| META-M3 (monopole-reference uncertainty unpropagated) | MAJ | **VERIFIED** | §V now propagates: Paper-IV reference se=2.8×10⁻⁴ → δσ_pred≈0.36 at N≈4×10⁵; f_CW^P5 reference se=5.5×10⁻⁴ → ≈0.7; 1.87 Phase-2 max residual read against this band; fixed-total-CW shuffle incorporates it by construction. **CLOSED (textual, arithmetic shown).** |
| META-M4 (Phase-2 LEE stratification + global multiplicity) | MAJ | **VERIFIED (partial)** | Table VI caption now states p_LEE is family-corrected only (not global) and shuffles are free; stratified Phase-2 rerun = Queue #17. |
| META-M5 (VoidFinder inside-any-hole permissive) | MAJ | **VERIFIED (partial)** | §VIII.E clarifier added (hole aggregation; over-counting at edges); VoidFinder-native membership comparison = Queue #18. |
| META-M6 (1.7<z≤2.0 clamped into top shell) | MAJ | **VERIFIED→QUEUED** | Clamp already disclosed; sensitivity run (drop/separate shell) queued in-text + Queue #19. |
| META-M7 (ASTRA variance independence approximation) | MAJ | **VERIFIED** | §X now states the across-object independence assumption and within-object negative correlation among class weights. **CLOSED (textual).** MC validation = optional Queue #20. |
| Grok-M1 (abstract 56,981 vs n=428) | STALE | Abstract sample ledger (INSESSION M1) + per-class n inline + 4.8 pp floor already present. |
| Grok-M2 (LEE on 1.87σ) | STALE | Per-cell p_LEE 0.13–0.56 in Table VI; Bonferroni-9=2.77 (R23conf OpenAI-M6); now also family-correction scope note. |
| Grok-M3 (Fig 5 panels mislead) | STALE/OPINION | Caption labels left = raw σ_from_half, right = monopole-prediction overlay with explicit Δf_CW; residuals tabulated in Table III/X. |
| Grok-M4 (Tempel sensitivity inconsistency) | STALE | §IX.B states |z|=0.49 + "1σ two-sample floor ~0.6 pp" + supporting-not-load-bearing scope (R23conf closure). |
| Grok-M5 (Table II "range 0.0198" under σ column) | **FALSIFIED** | Source row: `range & --- & --- & 0.0198 & ---` — the 0.0198 sits in the f_CW column; σ column is "---". PDF-extraction misalignment on reviewer side. |
| OpenAI-M1 (V-Web/T-Web nomenclature) | STALE | Title footnote + §IV.A nomenclature reminder (R23conf closure). |
| OpenAI-M2 (Paper IV monopole not peer-reviewed) | STALE/PARTIAL | f_CW^P5-referenced residuals already primary in §VIII.F/Table X; Paper IV labeled not-yet-peer-reviewed at first use; META-M3 closure adds uncertainty band. |
| OpenAI-M3 (RSD point-in-sphere) | STALE/QUEUED | "RSD-insensitive (not immune)" rewording + displacement bound in place (R23conf); pyrecon rerun already queued (R23conf #13). |
| OpenAI-M4 (mask dilation nonstandard) | STALE | §IV.A step 5 documents the exact operation; NSIDE-64 + interior-buffer cross-checks published. |
| OpenAI-M5 (0/6 overgeneralization) | **VERIFIED** | One-sided 95% Clopper–Pearson upper bound 1−0.05^{1/6}=39% added; purity claim downgraded to "indicative." **CLOSED (textual, arithmetic shown).** |
| OpenAI-M6 (three σ baselines mixed) | **VERIFIED (partial)** | META-M3 §V passage + existing Table X/XII baseline labels; Table VI caption now flags the Paper-IV baseline scope. Remaining per-caption cross-stamps = opinion-level. |
| OpenAI-M7 (T-Web volume-fraction tracer mixing) | STALE | §IX.C already states the comparison is approximate (differing target selection, z coverage, volume; no per-galaxy cross-match). |
| OpenAI-M8 (HEALPix stats on duplicate parent) | PARTIAL→QUEUED | Unique-subset χ² + weighted-r recomputes done (R23conf artifact 21); per-pixel σ distribution on unique parent = Queue #21. |
| OpenAI-M9 (per-shell counts unshown) | VERIFIED→QUEUED | "Every shell ≥2.16×10⁵" claim from artifact; per-shell histogram = Queue #22. |

## MINOR/NIT findings

| ID | Verdict | Disposition |
|----|---------|-------------|
| OpenAI-m1 (caveat juxtapositions) | STALE | Abstract + §V + Table II caption carry it. |
| OpenAI-m2 (gray/footnote R_s=10 rows) | VERIFIED | Table VI caption now carries the R_s=10 under-resolution exclusion note. **CLOSED.** |
| OpenAI-m3 (binomial floor next to 0.29 pp) | STALE | §IX.B already prints "1σ two-sample floor ~0.6 pp". |
| OpenAI-m4 (non-disjointness caveat placement) | OPINION | Caveat exists in §VI.D; placement = editorial. |
| OpenAI-m5 (Poisson normalization sentence) | STALE | §IV.A step 9 conventions note (R23conf META-N8). |
| OpenAI-m6 (length) | HOUSTON-DECISION | |
| OpenAI-m7 (σ_λ undefined) | VERIFIED | Definition added: rms width of the per-cell smoothed-eigenvalue distribution, canonical R_s=25 run. **CLOSED.** |
| OpenAI-m8 (ASTRA baseline note) | STALE | Table XII reports "max |σ| vs 1/2" with explicit label; §X text states EDR-cross-check design. |
| OpenAI-m9 (GALZONE EDGE/DEPTH) | PARTIAL→QUEUED | Criterion documented; flag-inclusion shift test = Queue #23. |
| OpenAI-m10 (Fig 8 colorbar) | QUEUED (figure regen) | Queue #24. |
| OpenAI-m12 (h-units example) | OPINION/STALE | Step 2 already gives sanity value χ(z=0.2)=570.4 h⁻¹Mpc. |
| OpenAI-m13 (monotone footnote) | STALE | R23conf META-M3 closure states monotone invariance at step 12. |
| OpenAI-m14 (boundary-cell fraction) | VERIFIED→QUEUED | Queue #25. |
| OpenAI-m15 (toy-EFT dimensions) | PARTIAL/HOUSTON | App A already labeled toy/schematic (R23conf); explicit dimension bookkeeping = optional editorial. |
| OpenAI-n1 ("imbalance" wording) | VERIFIED | Reworded to counting-noise/monopole framing. **CLOSED.** |
| OpenAI-n2 (pp parenthetical in body) | STALE/OPINION | Abstract defines "pp (percentage points)" at first use. |
| OpenAI-n3 (hyphenation/σfrom half) | FALSIFIED/OPINION | Source uses `$\sigma_{\rm from\,half}$` and "non-void" consistently; extraction artifacts. |
| OpenAI-n4/n8 (Fig 5 σ_pred label) | OPINION/N-A | Fig 5 right panel explicitly labels "Paper IV-monopole prediction" — accurate for that figure's baseline; conditional-on-M2-adoption rewording not triggered. |
| OpenAI-n7 (0.61 vs 0.607 rounding) | OPINION | Standard abstract rounding; Table V carries full precision. |
| Grok-N1 (axis units on figures) | QUEUED (figure regen) | Queue #24 bundle. |
| Grok-N2 (update arXiv→published refs) | QUEUED (network bib pass) | Queue #26; no entry removed (never-falsify-citations rule; bib check requires ADS network pass). |
| Grok-N3 (Δf=0.0007 class sizes) | STALE | Abstract ledger + Table VII n columns. |
| Grok-N4 (CI widths in Fig 3 caption) | OPINION/PARTIAL | Void-bin ±4.8 pp 2σ half-width already in abstract + §VI.A; per-class interval printing = editorial. |
| Grok-NIT1 (DESIVAST in title) | HOUSTON-DECISION | Title naming = author prerogative; DESIVAST is the published catalog name. |
| META-m1 (kNN mask-edge buffer) | VERIFIED→QUEUED | Queue #27. |
| META-m2 (shared RNG seed across families) | VERIFIED | Code check: scripts 05/07/09 all seed from `cfg["statistics"]["random_seed"]` — §V now discloses the shared config seed and cites the distinct-stream re-draws (§VIII.E) as stream-independence confirmation. **CLOSED (textual, code-verified).** |
| META-N1 (std=1.050 note) | VERIFIED | Heteroscedasticity parenthetical added §VIII.F. **CLOSED.** |
| Claude m1–m20 / INSESSION twins | STALE/CLOSED-PRIOR | Recompute all-clears; m7 self-withdrawn by reviewer. |

## Verdict counts (P5, this wave)
- ESSENTIAL audited: 4 distinct → 1 VERIFIED (META-E1: disclosure closed, rebuild queued), 2 STALE, 1 HOUSTON
- MAJOR audited: 17 distinct → 4 closed textual (META-M2, M3, M7, OpenAI-M5), 3 partial-closed+queued (META-M1, M4, M5), 2 queued (META-M6, OpenAI-M8/M9), 1 FALSIFIED (Grok-M5), 6 STALE, 1 HOUSTON-adjacent
- MINOR/NIT: 5 closed textual, 1 FALSIFIED, ~10 STALE/OPINION, 6 queued, 2 HOUSTON

**Pre-closure verified-and-open ESSENTIAL/MAJOR count: 10** (1 ESS + 9 MAJ requiring action), of which 5 closed textually this wave, 5 carry queued compute. **Not a clean round** (compute-class items outstanding), but no arithmetic error in any published number was verified — all recompute spot-checks reproduced the paper.
