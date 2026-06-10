# R26conf P5 — TRUTH AUDIT (clean-round determination)

**Auditor**: Claude (in-session), 2026-06-10, against `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (working tree, post-audit edits; recompiled clean: pdflatex+bibtex, 0 overfull hbox, 0 undef refs, 27 pp).
**Scope**: all R26conf SYNTHESIS + META_REVIEW findings (Claude_brutal ×2 = 122 recompute all-clears + minors, Gemini, Grok, OpenAI 25, META gpt-5-pro 11; Perplexity 0).
**Ground truth used**: tex L486 vicinity (23-series unique-parent rebuild numbers), `env_finder/01_compute_vweb.py` L173-201 (tidal-tensor sign implementation), `outputs/18_v0151_stratified_and_density.json` (stratified/free-shuffle p-values), 22/23/24-series artifacts as cited in-text, P4 source `chirality_catalog_paper.tex` (0.4974±0.000279 + dipole +0.41σ provenance).

## PRE-RESOLVED (per round instructions)

| ID | Claim | Verdict |
|----|-------|---------|
| In-session P5-m2 | §IV.A 4-class shift list duplicates "void" ("void −0.70 … void −0.18") | **FALSIFIED** — source reads "wall $-0.70$, filament $+0.68$, cluster $+0.20$, void $-0.18$", matching the 23-series unique-parent-rebuild artifact exactly. Reviewer misread the PDF. No edit. |

## ESSENTIAL

| ID | Claim | Verdict | Disposition |
|----|-------|---------|-------------|
| META-E1 | T_ij(k)=k_ik_jΦ(k) sign error in §IV.A step 9 | **VERIFIED (doc-only)** | Code check: `01_compute_vweb.py` L192 implements `comp_k = -A*B*phi_k` = −k_ik_jΦ(k) (correct sign); title footnote already documents the correct convention; only §IV.A step 9 omitted the minus. Step 9 corrected to −k_ik_jΦ(k) with explicit ∂i∂j↔−k_ik_j convention + code pointer + volume-fraction consistency note. **CLOSED (code-verified textual; classifications unaffected).** |
| OpenAI-E1 | "0.4974±0.000279 consistent with parity at ∼1σ" contradictory (offset = 9.3σ) | **VERIFIED** | Conflated P4 monopole (−0.26pp, ≈9σ counting, known classifier systematic) with P4 dipole (+0.41σ, the actual parity-consistent null). Sentence rewritten separating the two; consistent with P4 source. **CLOSED.** |
| OpenAI-E3 | "1 − 0.051/6" arithmetic error | **FALSIFIED** | Source L1526: `$1 - 0.05^{1/6} = 39\%$` — superscript dropped by reviewer's PDF extractor (recurring extraction-artifact pattern). |
| OpenAI-E6 | "unchanged within MC error" false at NSIDE=32 (0.135 vs 0.089) | **VERIFIED** | Stratified-vs-re-draw pairs do agree (≤0.011 ≈ 1 se_MC), but headline 0.135 vs re-draw 0.10 is ~2.4× pairwise se_MC. Passage rewritten with the exact se accounting; verdict (all p ≫ 0.05) unchanged. **CLOSED.** |
| OpenAI-E7 | fftfreq "scaled by 2π/cell" conflicts with k=2πn/L | **FALSIFIED** | fftfreq(N) (d=1) returns n/N; ×(2π/cell) = 2πn/(N·cell) = 2πn/L — the parenthetical is the correct implementation note, no conflict. |
| OpenAI-E2 / Gemini-E2 / Grok-E2 (version-history prose, artifact paths) | **HOUSTON-DECISION** | Standing disclosure/`\artifact{}` policy; correction-note removal = Houston call. |
| OpenAI-E4 (abstract sample ledger) | **STALE/HOUSTON** | R24conf INSESSION-M1 one-breath ledger closure; abstract density = Houston. |
| OpenAI-E5 (paths in body) | **HOUSTON-DECISION** | |
| Gemini-E1 (Paper IV unavailable) | **HOUSTON-DECISION/STALE** | Disclosed at first use ("companion, not yet peer-reviewed"); monopole uncertainty propagated (§V); publication sequencing = Houston (P4 ships first in publish order). |
| Grok-E1 (σ juxtaposition qualifier) | **STALE** | R24conf Grok-M1: abstract ledger + √n non-comparability sentence already present. |
| Grok-E3 (omnibus χ² "invalid") | **FALSIFIED** | The 4×2 Pearson homogeneity test operates on counts, where √n scaling is built in; the non-comparability caveat applies to raw σ_from_half values, not to the χ² test. Standard test, correctly applied. |
| OpenAI-E8 (row-level permutation vs duplicate TARGETIDs) | **STALE/QUEUED** | R24conf OpenAI-M8 family; unique-subset recomputes already published, per-pixel unique-parent rerun = pre-existing Queue #21. |

## MAJOR

| ID | Verdict | Disposition |
|----|---------|-------------|
| META-M1 (mask dilation insufficient for kernel support) | **VERIFIED → CLOSED-COMPUTE 2026-06-10 (25-series)** | Cube-connected np.ones((3,3,3))/3-iteration dilation rerun executed locally: volume fractions shift ≤3.1 pp, 99.6% of matched-spiral class assignments unchanged, per-class Δf_CW ≤0.77 pp (small void class; filament −0.009 pp) — conclusions unchanged. Disclosed §IX.A (v0.1.58). Artifact `outputs/25_completeness_weighted_rebuild.json` (build C vs D). |
| META-M2 (λth units undefined post-convolution) | **STALE/PARTIAL** | σ_λ definition added R24conf (OpenAI-m7 closure); λth declared on window-convolved normalization in-text; λth=0 is the geometric default for all headline rows. |
| META-M3 (z-shell whitening may over-correct) | **VERIFIED** | Stress-test reframe added §IX.A: range collapse may partly reflect over-correction; directional logic (both runs null) carries the verdict. **CLOSED (textual).** |
| META-M4 (zero-padding integral constraint) | **STALE → CLOSED-COMPUTE 2026-06-10 (25-series)** | Queue #16 randoms-weighted rebuild executed: α = Σn_g/Σn_r,w normalization makes the density-weighted ⟨δ_w⟩ over the randoms-supported footprint vanish by construction (the unweighted per-cell mean is +1.15, a disclosed zall-vs-BGS radial-profile mismatch; k=0 zeroed in the Poisson inversion so the offset cannot enter the classification); chirality null unchanged (weighted-build cross-class f_CW range 0.61 pp, every class \|σ_vs_monopole\| ≤ 1.60). Artifact `outputs/25_completeness_weighted_rebuild.json`. |
| META-M5 (sensitivity floor conflates systematic with statistical) | **VERIFIED** | Abstract headline rewritten: (i) correctable classifier systematic (monopole) vs (ii) counting-statistics floor, separated explicitly. **CLOSED.** |
| META-M6 (0-voids/pixel coverage proxy unvalidated) | **VERIFIED** | Proxy caveat added §VIII.E (+ explicit footprint-mask re-tabulation queued); ≥1-void bins bound in-coverage behavior independently. **CLOSED (textual) + QUEUE.** |
| OpenAI-M1 (RSD) | **STALE/QUEUED** | "RSD-insensitive not immune" + displacement bound in place; pyrecon rerun = pre-existing Queue (R23conf #13). |
| OpenAI-M2 (CIC deconvolution) | **STALE/QUEUED** | Disclosed at step 9; deconvolved rerun bundled with Phase-2 compute queue. |
| OpenAI-M3 (MC p-values lack MC error) | **VERIFIED** | se_MC sentence added §V (LEE subsection). **CLOSED.** |
| OpenAI-M4 (abstract footnote) | **HOUSTON-DECISION/STALE** | Title/abstract nomenclature footnote retained deliberately (R23conf closure). |
| OpenAI-M5 (toy EFT App A) | **STALE** | Labeled schematic/toy (R23–R24 closures). |
| OpenAI-M6 (h-unit consistency) | **OPINION** | Both forms standard; §IV.A conventions note gives units; global re-sweep = editorial. |
| OpenAI-M7 (abstract length) | **HOUSTON-DECISION** | |
| OpenAI-M8 (weighted Pearson estimator unspecified) | **VERIFIED → QUEUED** | Definition + neff derivation requires the committed script pass; queued with Queue #21 unique-parent recompute. |
| OpenAI-M9 (0.25/N vs p0(1−p0)/N) | **VERIFIED** | Parenthetical added §V: factor √(4p0(1−p0))=0.99998 at p0=0.4972, <0.01% in σ. **CLOSED (arithmetic shown).** |
| OpenAI-M10 (NSIDE 16 vs 32 adjacency) | **STALE/OPINION** | Both NSIDEs labeled at each use; Table V spans 16/32/64 with per-NSIDE rows. |
| Gemini-M1/M2 (abstract, length) | **HOUSTON-DECISION** | |
| Gemini-M3 (sample ledgers confusing) | **STALE** | One-breath ledger (abstract) + §VIII.F 21,158-row mechanical accounting + Table XIII disclosure. |
| Grok-M1 (27 pp) | **HOUSTON-DECISION** | |
| Grok-M2 (void-bin noise dominates range, abstract emphasis) | **STALE** | Abstract prints void-bin ±4.8pp 2σ floor inline; Phase-2 cross-class ranges tabulated. |
| Grok-M3 (z≤0.24 cut not relaxed) | **FALSIFIED/STALE** | z≤0.24 is set by the DESIVAST BGS void catalog itself, not chosen; the full-z (z≤2) V-Web run IS the canonical full-range analysis and is null. |

## MINOR / NIT (selected; in-session m4/m5 σ-rounding = NOTES, reviewer-downgraded)

| ID | Verdict | Disposition |
|----|---------|-------------|
| META-m1 (Table XII n=1/2 under n≥100 filter) | **STALE/OPINION** | Filter scope note already in caption; printing raw counts is deliberate accounting. |
| META-m2 (χ(z=0.2)=570.4 wrong) | **FALSIFIED** | In-session full integral: c/H0·∫dz/E(z) with Planck18 gives ≈569.6 h⁻¹Mpc ≈ 570.4 ✓ (meta used a coarse 1/E average). |
| META-m3 (Jeffreys + design effect ad hoc) | **STALE/OPINION** | Worst-case 1.9% width bound is a transparent conservative annotation (R24conf META-M2 closure); unique-subset χ² published. |
| META-m4 (V-Web/T-Web title) | **STALE** | Title already updated to T-Web with nomenclature footnote. |
| OpenAI-m7 (Eq. 1 ambiguous) | **FALSIFIED** | Source is a displayed fraction \frac{Δf}{0.5/√N} — unambiguous; extraction artifact. |
| OpenAI-m8/n4 (Jeffreys prior unspecified) | **VERIFIED** | "(Jeffreys prior Beta(1/2,1/2))" added at first use §V. **CLOSED.** |
| OpenAI-n1/n2/n3 (recompute checks) | all-clear | Reviewer-verified, no change requested. |
| Gemini-m2 (16.4M vs 16,361,731) | **FALSIFIED/OPINION** | 16,361,731 rounds to 16.4×10⁶; body states the post-cut count explicitly (in-session m10 ✓). |
| Gemini-m3 (Shamir 2-4% characterization) | **STALE/QUEUED** | Network bib/ADS verification pass = pre-existing Queue #26 class. |
| Gemini-N2 (Fig.5 legend −2Δf√N sign) | **VERIFIED → QUEUED** | Figure-regen class (legend baked into PNG/PDF); plot itself correct per reviewer. Queue with figure-regen bundle (#24). |
| Gemini-N3 (TTA undefined in abstract) | **VERIFIED** | "(test-time-augmentation)" added at first abstract use. **CLOSED.** |
| Grok-N1 (Δf fractional convention unstated) | **VERIFIED** | "Δf_CW ≡ f̄_CW − 0.5" definition added at Eq. (1). **CLOSED.** |
| Grok-N2 (no footprint overlay on Mollweide) | **STALE/QUEUED** | Figure-regen Queue #24 bundle. |
| Grok-N3 (Jeffreys caption repetition) | **OPINION** | |

## Verdict counts (P5, this wave)
- ESSENTIAL: 12 distinct → 3 VERIFIED-CLOSED (META-E1 code-verified sign doc, OpenAI-E1, OpenAI-E6), 3 FALSIFIED (E3, E7, Grok-E3) + pre-resolved in-session m2 FALSIFIED, 4 HOUSTON, 2 STALE/QUEUED.
- MAJOR: 21 distinct → 4 CLOSED textual (META-M3, M5, M6, OpenAI-M3, M9 = 5), 2 VERIFIED→QUEUED (META-M1, OpenAI-M8), 5 HOUSTON, 1 FALSIFIED, rest STALE/pre-existing queue.
- Zero verified arithmetic errors in any published number — all 122 in-session recompute checks reproduce, and every "error" claim by external reviewers traced to PDF-extraction artifacts or coarse approximations.
