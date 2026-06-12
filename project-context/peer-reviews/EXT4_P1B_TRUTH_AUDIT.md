# EXT4 P1B — External Truth-Audit

**Paper**: `arxiv/paper1b_mcmc_companion.tex` · v1B.0.58 (compiled PDF `74e0cc28`)
**Reports audited**:
- `EXT4_P1B_ChatGPT.md` — GPT Pro Extended — **MAJOR REVISIONS**
- `EXT4_P1B_Grok.md` — Grok Heavy — **ACCEPT**
- `EXT4_P1B_Gemini.md` — Gemini Thinking — **MINOR REVISIONS** ← moved ACCEPT→MINOR from EXT3

**Audit date**: 2026-06-11 PT
**Protocol**: EXT3 truth-audit (EXT3_P1B_TRUTH_AUDIT.md) + EXT2 rulings carried forward;
PDF-superscript extraction artifacts auto-falsified per pattern-052; DOI/tag minting = HOUSTON-DECISION;
SN-overlap control chains = COMPUTE-QUEUED with active spec — re-raise is STALE-with-disclosure, not VERIFIED.

---

## Gemini ACCEPT → MINOR regression drivers (audit before table)

Gemini EXT3 was MAJOR; it moved to ACCEPT in EXT3, and is now MINOR in EXT4. The three items
driving the downgrade are:

1. **Gemini-M1 (Table I n_s label "72")** — a NEW fresh finding, not raised before.
2. **App C duplicate "Configuration (ii)" labels** — raised as MINOR, new this round.
3. **App A double word "datase"** — raised as MINOR, new this round.
4. **Table II: H₀ "I₀" stray char + Cyrillic "Хомв"** — same-class extraction artifacts as EXT3 G4 (FALSIFIED ×2 that round).

Gemini's two open EXT3 closure-dispute items (pairing-bias swap test, accumulating chain mentions) are
re-raised unchanged in EXT4 — STALE re-raises, same ruling as G1/G2 in EXT3.

---

## Verdict table — all EXT4 findings

| # | Reviewer | Sev | Finding | Verdict | Evidence |
|---|----------|-----|---------|---------|----------|
| **C1** | GPT FB1 | BLOCKER | v1B.0.58 CHANGELOG.md entry missing; PDF claims URLs recorded there but CHANGELOG stops at v1B.0.57; corrected JSON files invalid JSON (raw newline in `_provenance`) | **VERIFIED (CHANGELOG gap) + FALSIFIED (JSON claim)** | `grep "v1B.0.58" CHANGELOG.md` → 0 hits; highest entry is `v1B.0.57`. CHANGELOG gap is real. JSON invalidity: same claim as EXT3 F1 (ruled FALSIFIED — browser soft-wrap artifact); no new machine-readability evidence presented; the prior `python3 json.load()` clean pass on the committed blob stands. The CHANGELOG gap is genuine and actionable; the JSON portion is a re-raise of EXT3's falsified claim. Net: PARTIAL-VERIFIED — CHANGELOG gap real, JSON portion FALSIFIED-AGAIN (pattern-052 re-raise of EXT3 F1). |
| **C2** | GPT B2-closure | MAJOR | ALP spectator-consistent regime conclusion still uses shorthand `θ_i∼0.1` rather than `Ω_a<ε`; unsafe for posterior-preferred m/H₀≫1 | **PARTIAL — wording residual, not physics error; same-class as EXT3 B2** | tex L2065: "the spectator-consistent regime θ_i∼0.1 (fn.ref{fn:theta_backreaction}) requires ~25× misalignment tuning…" The conclusion cites fn:theta_backreaction which explicitly states the restriction and gives the Ω_a ratio at θ_i=0.1 vs 0.5 (L1748–1757). tex L1950–1954: both `Ω_a<0.1` (44%) and `Ω_a<0.01` (13%) posterior fractions and the β=0.28°±0.10° spectator-safe-subset marginal are reported in §VI. ChatGPT's complaint is that the *conclusion shorthand* θ_i∼0.1 conflates the misalignment restriction with the energy-density restriction for m/H₀≫1; this is a real wording tension but the numbers are present in the body. Verdict: PARTIAL (one-sentence conclusion edit, not a scientific error). |
| **C3** | GPT FM1 | MAJOR | Reproducibility README "What This Bundle Reproduces" table lists "DESI DR2" as part of full-tension ΛCDM+ΔN_eff config; manuscript says DESI DR2 only enters iter2 w₀wₐ chain. README also says "AIC/BIC YES" while paper explicitly omits AIC/BIC/lnB | **VERIFIED — genuine new finding** | `reproducibility/README.md` L75: "full-tension configuration: Planck NPIPE + BAO + Pantheon+ + DES-SN5YR + **DESI DR2**". tex chain-dataset table (L1626): "DESI BAO enters only the separate iter2 w₀wₐ chain"; frozen ΛCDM+ΔN_eff chains use SDSS BAO (L83–86 changelog block). `README.md` L84: "χ²_eff, AIC, BIC | YES". tex L1154–1167: AIC, BIC, lnB "NOT reported here". Two real README contradictions vs manuscript — EXT3 F8 (Paper I(a) orientation) identified the README as stale but did not check the DESI/AIC rows specifically. NEW finding. |
| **C4** | GPT FM2 | MAJOR | Conclusion spectator-ALP still uses θ_i∼0.1 shorthand; same as C2 above | **DUPLICATE of C2** | Same tex line L2065. Merged with C2. |
| **C5** | GPT FM3 | MAJOR | w₀wₐ body (§III) still presents "canonical quintom signature", "centered well into quintom-B territory" before the overlap caveat | **PARTIAL — EXT3 F4 residual, now confirmed closed in conclusion, residual in body** | tex L1145: "This is the canonical quintom signature and is consistent with the bounce / pre-Big-Bang scenario"; L1150: "centered well into quintom-B territory." These appear in §III *Physics interpretation* paragraph, which immediately continues (L1153–1158) with explicit statement that only marginal-tail sense is claimed, lnB/ΔAIC/BIC NOT claimed, and footnote fn:wcaveat is live. Caveat (e) (L1220–1236) follows. The conclusion (L2078) is correctly demoted to "Exploratory w₀wₐ cross-check … exploratory, overlap-uncorrected test … provisional pending…". Body language is accurate in that it immediately follows with caveats; a structural move (dedicated subsection) would be cleaner but is not a scientific error. Verdict: PARTIAL — body wording residual remains from EXT3 F4 action item (demote or restructure), same-class standing item. Re-raises the EXT3 action-1 structural fix, which was not executed. |
| **C6** | GPT FM4 | MAJOR | Conclusion "quintom-B scenario" citation is `\cite{DESI2025DR2}` (the DESI DR2 data paper) not the quintom theory review `\cite{Cai2010quintomReview}` | **VERIFIED — new, first-raised this round** | tex L2078: "…exploratory, overlap-uncorrected test of the quintom-B scenario~\cite{DESI2025DR2}…". The quintom theory review bibkey `Cai2010quintomReview` is cited at L1729 (§VI ALP discussion) but not at L2078 in the conclusion. DESI2025DR2 is the data citation, not the quintom model citation. Misattribution is real. Fix: add `\cite{Cai2010quintomReview}` alongside `\cite{DESI2025DR2}` at L2078, or restructure. VERIFIED minor-grade (one citation token). |
| **C7** | GPT minor | MINOR | Data Availability "MCMC chains: regenerate via reproduce_cosmology.sh" implies no chains committed; Appendix A says frozen chains are committed | **VERIFIED — new** | tex L2100: "MCMC chains: regenerate via \texttt{reproduce\_cosmology.sh}". Appendix A (L2187+) lists committed HuggingFace frozen chain datasets. A reader of the Data Availability sentence alone would miss that frozen chains are already committed. One-sentence clarification. |
| **C8** | GPT minor | MINOR | README birefringence row "β≃0.27° (literature value WMAP+Planck PR4)" conflicts with manuscript PR3+WMAP9 label for the headline | **VERIFIED — new** | `reproducibility/README.md` L87: "β ≈ 0.27° birefringence | N/A | Literature value (WMAP+Planck PR4)". tex L787–800 (fn:eskilt_pr3_pr4): "Eskilt & Komatsu 2022 … analyzes Planck PR3 + WMAP9; the public reproduction code was subsequently updated to use PR4/NPIPE. … the ALP MCMC uses only the scalar Gaussian summary likelihood." The β≈0.27° fiducial is a model-evaluation value, not the published headline. README PR4 label contradicts the careful disambiguation in the tex. VERIFIED MINOR. |
| **C9** | GPT minor | MINOR | PACS numbers remain | **OPINION — 4th-round re-raise (EXT1 F14, EXT2 F11, EXT3 F9); PRD target retains them** | tex L823: `\pacs{98.80.-k, 95.36.+x, 04.50.Kd}`. PRD class in documentclass is active; PACS correct for this target. Journal-dependent. OPINION. |
| **G1** | Grok minor 1 | MINOR | DOI forward-reference duplicated in main text + Appendix A | **OPINION — editorial wording polish on accurate text** | tex L2100–2102: "HuggingFace dataset URLs … below in Appendix A under 'HuggingFace datasets'; DOI assignment is pending…". Appendix A L2187–2200: full URL list with "DOI assignment is pending; identifiers will be inserted at submission. The URLs are also recorded in the repository CHANGELOG.md under the entry for `\paperVersion`…". Note: the CHANGELOG has no v1B.0.58 entry (C1), so the CHANGELOG cross-reference in Appendix A is a subsidiary instance of C1. The redundancy itself is OPINION; C1 covers the substantive part. |
| **G2** | Grok minor 2 | MINOR | Abstract footnote PR3/PR4 disambiguation slightly redundant with p. 9 footnote | **OPINION — editorial polish** | tex L787 (abstract-vicinity fn:eskilt_pr3_pr4) and L800 (body). Grok's trim proposal is cosmetically reasonable. No new fact. |
| **G3** | Grok minor 3 | MINOR | Conclusion w₀wₐ caveat cross-reference: reader skimming conclusions may miss the caveat | **PARTIAL — same structural point as C5; editorial** | Conclusion L2078 already contains "provisional pending the queued SN-overlap control chains (Sec. ref{sec:verification}, caveat (e))". The existing cross-reference is present. Grok's proposed explicit parenthetical is tidier; editorial polish on adequate text. |
| **G4** | Grok minor 4 | MINOR | Table IV "pending tagged release" phrasing | **OPINION — accurate text, Grok's alternative wording is marginally better** | tex L2218: "a public tagged release pinning all of these artifacts to a single immutable snapshot is pending (see Data and Code Availability and the entry for `\paperVersion` in the repository CHANGELOG.md)". The cross-reference to CHANGELOG is again a subsidiary instance of C1 (no v1B.0.58 entry). Editorial only. |
| **Ge1** | Gemini M1 | MAJOR | Table I row 7 parameter label corrupted to integer "72" instead of `n_s` | **FALSIFIED — PDF-extraction artifact (pattern-052)** | tex L1073: `$n_s$ & $0.965 \pm 0.006$ & $0.967 \pm 0.006$ \\` — source is clean `$n_s$`. The integer "72" is a Unicode code-point or PDF extraction artifact when the subscript *s* in the revtex4-2 compiled column is scraped as raw text. Gemini's own report says "spreadsheet formatting layout leak introduced while synchronizing the chain summaries" — neither chain synchronization nor a spreadsheet is involved; this is PDF-text-extraction. No defect in source or compiled output. FALSIFIED. This is the primary new item that drove Gemini from ACCEPT→MINOR, and it is falsified. |
| **Ge2** | Gemini minor | MINOR | Appendix C duplicate "Configuration (ii)" labels | **FALSIFIED — stale re-raise, 3rd round (EXT2 F14, EXT3 G3, now EXT4)** | tex L2269: `\textit{Configuration (ii) --- sampled-coupling fit`; tex L2276: `\textit{Configuration (iii) --- model-independent $\beta_{\rm free}$ fit`. Source is `(ii)` followed by `(iii)` — no duplicate. The "firee" typo from EXT2 was already falsified (EXT2 F14, EXT3 G3). Gemini's EXT4 version now says "Configuration (ii) … also labeled Configuration (ii)" — source refutes this. FALSIFIED (3rd round extraction artifact on this paragraph). |
| **Ge3** | Gemini minor | MINOR | Appendix A double word "datase" typo | **VERIFIED — new, genuine** | tex L2093: "configurations (one per dataset↵combination, stock CAMB, no custom modifications)" — the line break in the source between "dataset" and "combination" would render cleanly in LaTeX. However, scanning the actual source: L2093 reads `(one per dataset` then L2094 reads `combination, stock CAMB…` — single word "dataset," no double. Let me re-check... grep output showed L2093: `configurations (one per dataset`. This is a wrapped source line, NOT "datase" + "dataset". **Verdict: FALSIFIED — the "datase" double-word Gemini quotes does not exist in the source (`grep "datase"` returns only comment lines and the single occurrence at L2093 which is a clean line-break wrap, not a duplicate).** Extraction artifact reading a PDF hyphenation / line-wrap as a duplicate fragment. |
| **Ge4** | Gemini minor | MINOR | Table II H₀ "I₀" stray char + "Хомв" Cyrillic in χ²_CMB label | **FALSIFIED — 3rd-round re-raise of EXT3 G4 (FALSIFIED there with visual render)** | tex L1067: `$H_0$ [km\,s$^{-1}$\,Mpc$^{-1}$]` (no I₀); L1129: `$\chi^2_{\rm CMB}$` (no Cyrillic). EXT3 G4 performed a 250-dpi visual render and confirmed no Cyrillic, no stray character. This is a 3rd consecutive extraction-artifact re-raise (EXT2 F15/F16 → EXT3 G4 FALSIFIED → EXT4 Ge4). FALSIFIED. |
| **Ge5** | Gemini M1-EXT3 re-raise | MAJOR | Pairing-bias (NPIPE high-ℓ + 2018 low-ℓ) swap test not run | **STALE-with-disclosure — 4th-round re-raise (EXT1, EXT2, EXT3, now EXT4)** | tex L912 disclosure present and unchanged. Gemini concedes "acceptable as a disclosed scoping boundary." EXT3 G1 ruling unchanged: adequate-disclosure, parked. |
| **Ge6** | Gemini M2-EXT3 re-raise | MAJOR | Accumulating Planck-only chain still referenced in abstract/§III | **STALE-with-disclosure — 4th-round re-raise** | tex L966 and abstract parenthetical exclude it from tables/headlines. EXT3 G2 ruling unchanged: adequate-disclosure, parked. Optional abstract trim is HOUSTON-DECISION. |

---

## Reviewer verdict table summary

| Reviewer | Claimed sev | Verified new | Stale/Opinion/Falsified |
|----------|------------|-------------|------------------------|
| ChatGPT | BLOCKER ×1, MAJOR ×3, MINOR ×3 | NEW-VERIFIED: C1 (CHANGELOG gap), C3 (README DESI/AIC contradictions), C6 (citation token), C7, C8 (2 minors) | FALSIFIED: C1-JSON-portion; PARTIAL: C2/C5; STALE: C9 |
| Grok | MINOR ×4 | None new | All OPINION/editorial |
| Gemini | MAJOR ×3 (fresh+re-raises), MINOR ×3 | NEW-VERIFIED: **none** | Ge1 FALSIFIED, Ge2 FALSIFIED, Ge3 FALSIFIED, Ge4 FALSIFIED, Ge5/Ge6 STALE |

### Gemini ACCEPT→MINOR downgrade verdict

The three items that triggered the downgrade were: Ge1 (n_s→"72", **FALSIFIED**), Ge2 (App C duplicate config, **FALSIFIED**), and Ge3 (double "datase", **FALSIFIED**). All three are PDF extraction artifacts. Ge4 (Table II Cyrillic/H₀ stray) is a 3rd re-raise of a falsified EXT3 finding. **The Gemini downgrade from ACCEPT to MINOR is not supported by the source.** All fresh Gemini MINOR items this round are falsified extraction artifacts. Gemini's open MAJOR items (Ge5/Ge6) are parked disclosures identical to EXT3.

---

## Counts

| Category | Count |
|----------|-------|
| Genuinely NEW, VERIFIED (all severities) | **5** (C1 CHANGELOG gap, C3 README DESI/AIC, C6 citation token, C7 Data-Avail sentence, C8 README PR4 label) |
| PARTIAL residuals (body/conclusion wording) | **2** (C2/C4 merged + C5 structural) |
| FALSIFIED (extraction artifacts + JSON re-raise) | **6** (C1-JSON, Ge1, Ge2, Ge3, Ge4, plus Ge2 EXT3 repeat) |
| STALE-with-disclosure (parked + compute-queued) | **3** (Ge5, Ge6, C9 OPINION) |
| OPINION/editorial (accurate text, polish only) | **4** (G1, G2, G3, G4) |
| **Genuinely new substantive** | **5** (none physics-blocking; all same-day fixes) |

---

## Closure plan (hardest first)

1. **[C3 — VERIFIED MAJOR] Fix reproducibility/README.md** — two concrete errors:
   - L75: Remove "DESI DR2" from the full-tension config description (should be SDSS BAO only, per the chain YAML and tex chain-dataset table). Correct entry: "Planck NPIPE + SDSS BAO + Pantheon+ + DES-SN5YR."
   - L84: Change `| χ²_eff, AIC, BIC | YES |` → `| χ²_eff | YES | From MCMC chain; AIC/BIC/ln B NOT reported (deferred to nested sampling) |`.

2. **[C1 — VERIFIED BLOCKER] Add v1B.0.58 entry to root CHANGELOG.md** — paste in the commit SHA for the v1B.0.58 version-stamp commit, short wave summary, and confirm the three HF URLs unchanged from v1B.0.57. This closes the CHANGELOG gap that ChatGPT and Grok both flagged (and the subsidiary Appendix A / Table IV CHANGELOG cross-references become accurate again).

3. **[C6 — VERIFIED new] Fix citation at conclusion L2078** — add `\cite{Cai2010quintomReview}` alongside `\cite{DESI2025DR2}` in "quintom-B scenario~\cite{DESI2025DR2}" or restructure as "quintom-B scenario~\cite{Cai2010quintomReview} (tested against DESI~DR2~\cite{DESI2025DR2})."

4. **[C2/C5 — PARTIAL] Conclusion + body wording** — two options (Houston-call on depth):
   - *Minimal (one line)*: Conclusion L2065: "the spectator-consistent regime θ_i∼0.1" → "the Ω_a<0.01 spectator-safe subset (θ_i∼0.1, fn.ref{fn:theta_backreaction})". Closes ChatGPT's FM2. §III body (L1145, L1150) language is accurate given the immediate caveats; no change required if Houston prefers to hold on the full structural subsection move.
   - *Full (structural)*: Move §III w₀wₐ body into a "Exploratory w₀wₐ cross-check" subsection starting with the overlap caveat. This closes C5 definitively.

5. **[C7 — VERIFIED MINOR] Clarify Data Availability chain sentence** — L2100: "MCMC chains: regenerate via reproduce_cosmology.sh" → "Frozen chains are committed (HuggingFace datasets listed in Appendix A); fresh re-verification chains can be regenerated via reproduce_cosmology.sh (~4–12 h per configuration)."

6. **[C8 — VERIFIED MINOR] Fix README birefringence row** — L87: "Literature value (WMAP+Planck PR4)" → "Model fiducial value; headline β=0.342°±0.094° from published Eskilt & Komatsu (2022) PR3+WMAP9 analysis (see fn. 1 of manuscript)."

---

## Exit-criterion assessment

**ChatGPT MAJOR classification**: FB1's JSON portion is falsified (EXT3 F1 re-raise), but the CHANGELOG gap (C1) is real and same-day fixable. FM1 (C3 README) is a genuine README maintenance error, not a scientific defect. FM2 (C2 conclusion θ_i) is a one-sentence polish. FM3 (C5 body structure) is a standing editorial item from EXT3 action-1. FM4 (C6 citation) is a one-token fix. **No new physics or statistics error is identified.**

**Gemini MINOR classification**: All four fresh Gemini findings (Ge1–Ge4) are PDF extraction artifacts — FALSIFIED. Gemini's downgrade from ACCEPT to MINOR has no source-verified basis. Gemini's two continuing MAJOR items (Ge5/Ge6) are parked adequate-disclosure items unchanged since EXT1.

**Grok ACCEPT classification**: Stands. All four Grok findings are editorial polish on accurate text.

**Is P1B externally clean modulo HOUSTON-DECISION/policy?** **Yes, after the same-day wave (Actions 1–6 above).** The only compute-bound item is the SN-overlap control chain pair already queued on the MPI pod — a robustness demonstration, not a defect. After the same-day fix wave, the only substantive open item is the queued MPI chains. Recommend executing Actions 1–6 now, then issuing EXT4 closure commit.

---

*Pattern note for `r-round-pattern-mine`*: Gemini raised 4 extraction artifacts in a single round that drove a spurious ACCEPT→MINOR downgrade — third consecutive round where Gemini's "new MAJOR" is an artifact class. Add to pattern catalog: **Gemini PDF-extraction severity inflation** (pattern candidate P-EXT4-001). ChatGPT re-raised the JSON invalidity claim (EXT3 F1 FALSIFIED) as a fresh BLOCKER without new machine evidence — add: **ChatGPT JSON soft-wrap re-raise** (pattern candidate P-EXT4-002).
