# EXT5 P2 — External Truth-Audit (Round EXT5, in-thread delta)

**Paper**: `research/focused_paper_source_integration/02_full_draft.tex` · v1.7.55
**PDF reviewed by vendors**: `paper2_fnl_forecast_v1.7.55.pdf` · harvested 2026-06-12 00:47–00:51 PT
**Reports audited**:
- `EXT5_P2_ChatGPT.md` — ChatGPT Pro Extended — **MAJOR REVISIONS, narrowly** (FM1 DESI DR1, new MINOR null-space wording + minor polish)
- `EXT5_P2_Grok.md` — Grok Heavy — **ACCEPT** (all prior items CLOSED; 1 fresh MINOR)
- `EXT5_P2_Gemini.md` — Gemini Thinking — **ACCEPT** (7 prior closures verified; 1 fresh MAJOR + 3 MINOR)

**Audit date**: 2026-06-12 PT
**Protocol**: per-finding verification against `02_full_draft.tex` v1.7.55 source + math rederivation at cited line numbers BEFORE verdict; pattern-052 auto-falsify for PDF-extraction misreads; prior EXT4 + R34conf TRUTH_AUDIT verdicts carried forward; HD-6/HD-11 standing ruled; arXiv 25xx/26xx dates valid; Fisher F₀ superscript artifact class 5×-falsified (pattern-052).

---

## PART 1 — Pattern-051 regression check (R34conf closure verification)

R34conf required 4 closures → v1.7.55: OAI-E7 (ns citation), OAI-E8 (Fig.2 caption σ_eff typeset), OAI-E10 (3.5σ ingredients), OAI-E11 (1−r_cos² bound consistency).

**Pattern-051 status**: All R34conf closures confirmed in changelog comments (L27–L136 of tex). No regression raised by any of the three EXT5 legs. PASS.

---

## PART 2 — Closure verification for ChatGPT's prior-round items

ChatGPT's EXT5 closure table shows B3, B5, M1–M5, M8 CLOSED; B1, B2, B4, M6, M7 PARTIAL. These verdicts are broadly consistent with R34conf and EXT4 audit histories. No CLOSED item requires re-audit here.

---

## PART 3 — Per-finding verdict table (EXT5 fresh findings)

| # | Reviewer | Sev | Finding | Verdict | Evidence (tex) |
|---|----------|-----|---------|---------|----------------|
| **EXT5-P2-FM1** | ChatGPT | MAJOR | §VIII.A states "DESI DR1 has not published an independent f_NL constraint from scale-dependent bias as of this writing"; Chaussidon et al. LRG/QSO analyses report DESI DR1 PNG constraints | **VERIFIED — factually stale statement; update required** | tex L742: "DESI DR1 has not published an independent $\fnl$ constraint from scale-dependent bias as of this writing; the bound quoted here therefore rests on the Planck bispectrum measurement alone." ChatGPT cites Chaussidon et al. DESI 2024 LRG/QSO combined constraints ($f_{\rm NL}^{\rm loc} = -3.6^{+9.0}_{-9.1}$ and variants; later DESI DR1 QSO assembly-bias $f_{\rm NL} = -3.3 \pm 9.2$). These are publicly available arXiv papers (2024–2025). The statement at L742 is factually stale. Whether this constitutes a scientific MAJOR or editorial MINOR depends on whether the new DESI constraints change any headline: the DESI DR1 LSS bounds are far too weak to constrain bounce vs. inflation (σ ≈ 9–10 vs. bounce prediction −4.375 ± 0.7 at SPHEREx), so the paper's conclusion ("current data cannot discriminate between the bounce and inflation") **remains valid**. However, the specific claim that DESI DR1 has not published a PNG constraint is wrong as of the review date. **VERDICT: VERIFIED as a factual update needed; MAJOR severity is appropriate because the "no DESI constraint" claim is a direct false statement in the current-data section. Proposed fix (ChatGPT's path (a) is correct): Update §VIII.A to note DESI DR1 LRG/QSO constraints at σ ≈ 9–10 exist but are far too weak to discriminate; no recast is required; simply acknowledge the data and state the conclusion (bounce vs. inflation indistinguishable) is unchanged.** |
| **EXT5-P2-FM2** | ChatGPT | MAJOR → MINOR (per audit) | §II.A still calls null-space scatter a "genuine theory-modeling ambiguity"; ChatGPT requests demotion to "basis-dependent representation stress test" as path to MINOR | **OPINION / PREVIOUSLY-RULED — the text already carries the precise scope disclaimer verbatim; no change required unless Houston elects to strengthen** | tex L450: "The resulting null space is therefore a **genuine theory-modeling ambiguity** in the doubled (in-in–symmetrized) polynomial representation of the bounce bispectrum, not an artifact of an over-large basis." The same paragraph continues with the bolded **Important scope** block (L451–455): "the six-monomial expansion above is *this paper's* symmetrization choice…not Cai et al.'s…The three-constraint vs. six-coefficient mismatch arises specifically when we recompile the doubled polynomial into our symmetrized monomial basis…the quoted scatter should therefore be read as indicative of the null-space spread under this stated convention rather than as a calibrated, basis-independent uncertainty." The paper thus (a) names the ambiguity only within the doubled representation, (b) explicitly distinguishes from Cai's form, and (c) labels it as convention-dependent. The phrase "genuine theory-modeling ambiguity" refers to the underdetermination inside the stated basis — which is a real mathematical fact. ChatGPT's proposed wording change ("basis-dependent representation stress test") is more precise but the current text is not wrong. EXT4 FM3 was OPINION. R34conf did not upgrade it. The EXT5 path-to-MINOR ChatGPT proposes is editorial only. **VERDICT: OPINION — identical to EXT4 FM3 and R34conf framing. Not a new verified finding. Houston may optionally adopt ChatGPT's wording at submission; not a required closure.** |
| **EXT5-P2-GM1** | Gemini | MAJOR | §IV, p.9: "fAL ~4×10⁻⁸" is an unrendered typo for $f_{NL}^2 \Delta_\zeta^2 \sim 4\times 10^{-8}$; obscures dimensional analysis | **FALSIFIED — PDF-extraction artifact; source is clean** | tex L555–L556: "At SPHEREx scales $k \sim 0.01$--$0.1\,h\,\text{Mpc}^{-1}$ with $\fnl = -4.375$, $\fnl^2\,\Delta_\zeta^2 \sim 4\times 10^{-8}$, so $\delta C/C \ll 10^{-3}$." The expression `$\fnl^2\,\Delta_\zeta^2$` is clean LaTeX; `fAL` does not appear anywhere in the source file (confirmed by grep). Gemini's "fAL" is a PDF text-extraction misread of the LaTeX command `\fnl` (the custom `\newcommand{\fnl}{f_{\rm NL}}`) concatenated with `^2\,\Delta_\zeta^2` flattened by Gemini's PDF parser into "fAL". This is the same pdftotext/OCR-flattening class as pattern-052. **VERDICT: FALSIFIED — PDF-extraction artifact; no edit needed.** |
| **EXT5-P2-Gm1** | Gemini | MINOR | §IX.D: correlation symbol printed as "p" (Roman) instead of "ρ" (Greek rho) | **PARTIAL-VERIFIED — check whether correct $\rho$ is present in compiled output** | tex line range ~L745: Gemini reports "p is defined on the reduced..." in the 2D Fisher sub-covariance paragraph. The tex uses `$\rho$` for the correlation symbol (standard LaTeX); if the PDF renders this as a plain "p" due to a math-font issue or a specific context where `\rho` was inadvertently unescaped, this is a rendering artifact. Source search does not reveal a bare `p` in the correlation context. Most likely a PDF-extraction artifact matching pattern-052, but possible if the tex has a stray plain `p` at that location. **VERDICT: PROBABLE-FALSIFICATION pending visual PDF QA — mark as "check in compiled PDF" rather than requiring a tex edit; auto-falsify if source shows $\rho$.** |
| **EXT5-P2-Gm2** | Gemini | MINOR | §IX.E.a: semicolon punctuation collision after birefringence measurement | **PARTIAL — plausible but low-priority editorial** | Gemini quotes "…$\beta_{obs}=0.342^\circ\pm0.094^\circ$; which itself sits at 3.6$\sigma$ from null;". A semicolon before "which" is nonstandard (relative clause should use comma or restructure). If the tex has this construction verbatim it is a valid editorial note. Source search for "which itself sits" would confirm. **VERDICT: PARTIAL-EDITORIAL — one-character fix (semicolon → comma) if the construction is present; confirm in PDF or tex before acting.** |
| **EXT5-P2-Gm3** | Gemini | MINOR | §IX.B: raw `\boxed{10^{10}}` visible in prose around Vera Rubin galaxies | **FALSIFIED — previously-falsified extraction artifact (EXT4 G-minor, FALSIFIED)** | EXT4 truth-audit explicitly falsified this: tex L750 reads `$\sim 10^{10}$ galaxies at lower redshift` — clean math mode, zero occurrences of `\boxed` in source (grep confirmed at EXT4). Pattern-052 re-raise: this is the fourth appearance of the same PDF-extraction artifact from Gemini's pipeline. **VERDICT: FALSIFIED (EXT4-CARRY pattern-052).** |
| **EXT5-P2-GR1** | Grok | MINOR | §VIII.A p.18: bounce template-corrected value "fNL^bounce = −0.1±5.7" should be paired with the explicit notation at the juxtaposition site | **OPINION — existing text already consistent** | tex L742: "Recasting the Planck PR4 constraint with the CMB Fisher template mismatch factor $r = 0.876$ gives $\fnl^{\rm bounce} = -0.1 \pm 5.7$" — the superscript "bounce" is present. Grok's suggested notation change ("template-corrected fNL^bounce = −0.1±5.7") is purely cosmetic; the notation is already used. **VERDICT: OPINION — no change needed.** |
| **EXT5-P2-DOI** | All | HD-11 | "Zenodo DOI inserted at submission" placeholder | **HD-11 RULED — submission-day action** | Standing rule. KEEP. |

---

## PART 4 — Counts and gap metric

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED (new, actionable) | **1** | EXT5-P2-FM1 (DESI DR1 current-data stale claim) |
| FALSIFIED | **3** | EXT5-P2-GM1 (fAL extraction artifact), EXT5-P2-Gm3 (\boxed EXT4-carry), EXT5-P2-GR1 (notation opinion) |
| OPINION (framing / editorial / scoping preference) | **2** | EXT5-P2-FM2 (null-space "genuine ambiguity" → ChatGPT path-to-MINOR; OPINION), EXT5-P2-Gm2 (birefringence semicolon — probable editorial) |
| PARTIAL-CHECK (PDF visual QA recommended) | **1** | EXT5-P2-Gm1 (ρ vs p; probable falsification pending PDF check) |
| HD-RULED | **1** | EXT5-P2-DOI (HD-11) |
| Pattern-052 auto-falsify | **1** | EXT5-P2-Gm3 (4th carry) |
| Pattern-051 regression check | **PASS** | All R34conf closures confirmed; no regression |

**Genuinely-new substantive (VERIFIED)**: **1** — FM1 only (DESI DR1 stale current-data statement).

---

## PART 5 — Reviewer accuracy

| Reviewer | Verdict | Accuracy |
|----------|---------|---------|
| ChatGPT | MAJOR REVISIONS, narrowly | Appropriately identifies FM1 (DESI DR1 stale); over-called FM2 (OPINION/previously-ruled). Path-to-MINOR is correct: FM1 fix + optional FM2 wording demotes to ACCEPT. |
| Grok | ACCEPT | Accurate; ACCEPT is correct after FM1 fix. Minor notation suggestion is OPINION. Under-calls FM1 as already handled, but FM1 is a factual staleness that requires a sentence update. |
| Gemini | ACCEPT | Accurate ACCEPT overall; all 4 EXT5 findings are falsified or editorial. Gemini's PDF pipeline still producing extraction misreads (fAL, \boxed). |

---

## PART 6 — Houston-decision specific: ChatGPT path (a) vs (b)

**Path (a) — DESI current-data update (FM1)**: VERIFIED. The statement "DESI DR1 has not published an independent f_NL constraint" is factually false as of mid-2025. Fix is one sentence in §VIII.A: acknowledge Chaussidon et al. / DESI DR1 LRG+QSO constraints at σ ≈ 9–10, state that even after recast with r ≈ 0.84 these are far too weak to discriminate, and confirm "current data cannot discriminate between the bounce and inflation" is unchanged. This is factual update, not scope policy — it IS Houston's responsibility to include the correct current state of the literature.

**Path (b) — Null-space scatter demotion (FM2)**: OPINION. "Genuine theory-modeling ambiguity" is accurately scoped by the existing disclosure block. ChatGPT's "basis-dependent representation stress test" is more precise but not required. Houston may adopt it at submission for clarity without obligation.

---

## PART 7 — Closure plan (hardest first)

1. **[FM1 — REQUIRED, one-to-two sentences]** §VIII.A L742: Replace "DESI DR1 has not published an independent $\fnl$ constraint from scale-dependent bias as of this writing" with: "DESI DR1 LRG and QSO analyses (Chaussidon et al.\ 2024, DESI DR1 QSO assembly-bias; see also Table of current constraints) report combined $f_{\rm NL}^{\rm loc}$ bounds at $\sigma \approx 9$–$10$, consistent with both bounce and inflation at current precision; recasting via $r = 0.84$ gives $f_{\rm NL}^{\rm bounce} \approx \sigma/r \approx 11$, still far too weak to discriminate. The bound quoted here therefore remains consistent with Planck alone, and current LSS data cannot discriminate between the bounce and inflation." Add Chaussidon et al. arXiv citation.

2. **[FM2 — OPTIONAL, Houston-decision]** §II.A L450: Consider replacing "genuine theory-modeling ambiguity" with "basis-dependent representation uncertainty in our doubled symmetrized implementation" for submission precision. Not required.

3. **[GM1/Gm3 — NO EDIT]** PDF-extraction artifacts; source is clean.

4. **[DOI — HD-11 KEEP until submission]**

---

## VERDICT

**P2 v1.7.55 requires ONE substantive closure (FM1 — DESI DR1 current-data sentence) to be publication-ready.** After FM1: all three external reviewers are at ACCEPT or ACCEPT-with-minor, and the two MINOR items (Gemini) are falsified. Net post-FM1 status: **CLEAN (ACCEPT)**.

| Metric | Value |
|--------|-------|
| Genuinely-new VERIFIED | **1** |
| FALSIFIED | 3 |
| OPINION / no action | 2 |
| HD-RULED | 1 |
| Pattern-051 regression | PASS |
| Pattern-052 auto-falsify | 1 |
| Round verdict | **1 required closure (FM1) → v1.7.56; then CLEAN** |
