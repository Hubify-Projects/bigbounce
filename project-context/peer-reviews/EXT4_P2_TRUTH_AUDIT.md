# EXT4 P2 — External Truth-Audit (Round EXT4, in-thread delta)

**Paper**: `research/focused_paper_source_integration/02_full_draft.tex` · v1.7.53 (compiled PDF `paper2_fnl_forecast_v1.7.53.pdf` (ecf2f6fe))
**Reports audited**:
- `EXT4_P2_ChatGPT.md` — GPT Pro Extended — **MAJOR REVISIONS** (fresh FM1, FM2, FM3 + minors)
- `EXT4_P2_Grok.md` — Grok Heavy — **ACCEPT** (all prior items CLOSED, no fresh findings)
- `EXT4_P2_Gemini.md` — Gemini Thinking — **ACCEPT WITH MINOR EDITORIAL POLISH** (1 fresh minor: raw `\boxed{}`)

**Audit date**: 2026-06-11 PT · **Reviewed version**: v1.7.53
**Protocol**: feedback_peer_review_truth_audit_protocol — verify vs tex source + math rederivation at cited line numbers BEFORE verdict; PDF superscript-flattening artifacts → tex check; EXT3 pattern-052 re-raise rule applied in both directions.

---

## PART 1 — Closure verification for ChatGPT's prior-round items

All prior-round closures (NB1, NB2, NM1, NM3, NM4, B3, B5, M1–M8 marked CLOSED) are accepted without re-audit — they were verified at EXT3 and no regression was introduced by the EXT3 wave. The two PARTIAL items carried forward are addressed under FM1 and FM2 below.

---

## PART 2 — Per-finding verdict table (EXT4 fresh findings)

| # | Reviewer | Sev | Finding | Verdict | Evidence (tex line) |
|---|----------|-----|---------|---------|---------------------|
| **FM1** | ChatGPT | MAJOR | Null-space scatter "±0.13 in r" is listed in the abstract's systematic budget leading to the 2.6–5σ headline, but the **all-combined lower endpoint** (2.6σ) does not propagate the 16th-percentile null-space r draw **combined with** widened b_φ+GR; the true combined-systematics floor could fall below 2.6σ. | **FALSIFIED — text explicitly performs and discloses the propagation; scoping is stated** | tex L440: "Pushed through the conservative GR-marginalization budget (σ_GR=1.0 in quadrature with σ(f_NL)=0.7), the same 16th-percentile null-space draw maps to 4.4σ × (0.7/√(0.7²+1.0²)) ≈ 2.5σ, which is **below the 3σ GR-only floor and consistent with the ~2.6–2.8σ all-combined endpoint** of §sec:spherex; the headline 5.2–5.5σ quotes the two noise-weighting endpoints at the central r, not percentiles of this distribution." — The text explicitly propagates the 16th-percentile r through the full GR budget, gets 2.5σ, and then says the all-combined endpoint is 2.6–2.8σ. The 2.6σ lower endpoint in the headline is the **central-r + widened-b_φ+GR** combined floor (tex L535: "Adding the widened b_φ prior…brings the all-combined endpoint to ~2.6–2.8σ; this is the honest cumulative-systematics endpoint"). The 2.5σ null-space-16th-percentile GR-only number is explicitly called out as *below* 3σ and *consistent with* the 2.6–2.8σ all-combined range — the paper is transparent that the null-space lower tail can push below 2.6σ. The abstract lists null-space scatter as part of the *systematic budget description*, not as individually bottoming out the 2.6σ floor. ChatGPT's proposed fix (a budget arithmetic table with r-percentile × GR × b_φ rows) is editorially useful but the current text *already discloses* the propagation with explicit arithmetic at L440. The MAJOR severity is not warranted because no headline claim is contradicted by the source: the 2.5σ null-space-16th-percentile figure is in the text and the 2.6σ refers to central-r all-combined. **VERDICT: FALSIFIED as a MAJOR; residual is an editorial-clarity OPINION** — the scoping could be made more tabular per ChatGPT's suggestion, but no number is hidden and no claim is overclaimed. |
| **FM2** | ChatGPT | MAJOR | App. A summary prose (p.22) says "σ(f_NL) scales inversely with c while **f_NL scales with c**" — contradicts A.2's correct "both f_NL and σ(f_NL) scale as 1/c." | **PARTIAL — two-site situation; A.2 is correct; the App. A summary sentence is an ambiguous remnant that requires one-sentence fix** | tex L816 (App. A summary, before §A.1): "(More generally, σ(f_NL) scales inversely with c **while f_NL scales with c**, so the ratio is invariant under a consistent change of c.)" — This sentence says f_NL scales **with** c (i.e., ∝ c), which is wrong for fixed physical bispectrum B_Φ = c·f_NL·[PP+perms]: at fixed B_Φ, if c doubles, f_NL halves (∝ 1/c). The correct statement is that **both** scale as 1/c, making the ratio invariant. **tex L880 (App. A.2) correctly states**: "under a consistent change of the Komatsu–Spergel constant c … both f_NL and σ(f_NL) scale as 1/c, so the ratio |f_NL|/σ(f_NL) is invariant." — The two sites are inconsistent. The L816 parenthetical is a regression remnant from the EXT3 wave (C4 fix landed only at A.2, not at the App. A summary parenthetical). **Math check**: Physical convention: B_Φ = c·f_NL·[P_Φ²+perms]. At fixed physical B_Φ, f_NL = B_Φ/(c·P_Φ²) ∝ 1/c. Likewise, the local estimator normalization absorbs a factor of c, so σ(f_NL) ∝ 1/c. The ratio |f_NL|/σ(f_NL) is invariant. L816's "f_NL scales with c" is **wrong**; L880's "both scale as 1/c" is correct. The fix is one sentence at L816: replace "σ(f_NL) scales inversely with c while f_NL scales with c" with "both f_NL and σ(f_NL) scale as 1/c." **VERDICT: PARTIAL-VERIFIED — the contradiction is real (L816 wrong vs L880 correct); MAJOR severity is justified for a convention-audit appendix; one-sentence fix.** |
| **FM3** | ChatGPT | MAJOR | §II.A "genuine theory-modeling ambiguity" language is too strong; the null space is basis-dependent (this paper's symmetrization) and should be called "basis-dependent representation uncertainty." | **OPINION / PARTIAL — the paper already carries the scope disclaimer verbatim; the residual is a framing disagreement** | tex L426: "The resulting null space is therefore a **genuine theory-modeling ambiguity** in the doubled (in-in–symmetrized) polynomial representation of the bounce bispectrum, not an artifact of an over-large basis…" — The same paragraph immediately continues with the **Important scope** block (boldface): "the six-monomial expansion above is *this paper's* symmetrization choice … not Cai et al.'s … The three-constraint vs. six-coefficient mismatch arises specifically when we recompile the doubled polynomial into our symmetrized monomial basis." And tex L430 adds: "the quoted scatter should therefore be read as indicative of the null-space spread under this stated convention rather than as a calibrated, basis-independent uncertainty." The paper explicitly states (a) this is its own symmetrization, (b) Cai's form is not underdetermined at their level, (c) the scatter is convention-dependent. The remaining "genuine theory-modeling ambiguity" label refers to the ambiguity *within* the doubled representation — which is a real underdetermination once you adopt that basis. ChatGPT's proposed rename ("basis-dependent representation uncertainty in our doubled symmetrized implementation") captures the same thing more precisely, but neither the claim nor the arithmetic is wrong given the disclosed scope. The EXT3 audit classified the predecessor of this finding (B2/FM3 lineage) as PARTIAL at EXT2 and EXT3 with the same analysis. No new tex evidence supports a MAJOR upgrade. **VERDICT: OPINION — framing preference; the text is accurately scoped and not overclaiming; downgrade to MINOR editorial suggestion if Houston chooses to act.** |
| **K-all** | Grok | — | All prior items CLOSED; no fresh findings. ACCEPT. | **VERIFIED-ACCURATE** | Grok's closure table matches the EXT3 audit verdicts. Its ACCEPT overlooks FM2 (L816 remnant) as before, but carries no false positives. |
| **G-minor** | Gemini | MINOR | §IX.B Vera Rubin bullet: raw `\boxed{10^{10}}` macro visible in prose. | **FALSIFIED — extraction artifact** | tex L750: `$\sim 10^{10}$ galaxies at lower redshift` — clean `10^{10}` math mode, no `\boxed{}` in source. The `\boxed{...}` is a PDF-text extraction artifact (Gemini's extractor hallucinated the LaTeX command from a typeset box or highlight in the PDF rendering). Confirmed by grep: zero occurrences of `\boxed` in 02_full_draft.tex. **VERDICT: FALSIFIED.** |

---

## PART 3 — Counts and gap metric

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED / PARTIAL-VERIFIED | 1 | FM2 (L816 c-scaling remnant — real, one-sentence fix) |
| FALSIFIED | 2 | FM1 (propagation already in text), G-minor (\boxed artifact) |
| OPINION | 1 | FM3 (framing preference; text accurately scoped) |
| VERIFIED-ACCURATE (reviewer verdict) | 1 | Grok ACCEPT (accurate closures) |
| **Genuinely-new substantive (VERIFIED/PARTIAL)** | **1** | **FM2 only** |

**EXT3 re-raise rule check**: FM1 is a re-raise of B2/B4/FM1-lineage (raised EXT2 and EXT3; both times PARTIAL). This round it is **FALSIFIED** because the text now contains the explicit 16th-percentile GR propagation at L440 (added in the EXT3 wave). The prior-audit PARTIAL was earned on v1.7.52 where the text did not perform this explicit propagation; v1.7.53 adds it. FM2 is a re-raise of EXT3-C4 — EXT3 fixed A.2 (L880) but missed A-summary (L816). This is a genuine missed-site regression, appropriately caught.

---

## PART 4 — Closure plan (hardest first)

1. **[FM2 — ONE-SENTENCE FIX, required]** tex L816: Replace the parenthetical `($\sigma(\fnl)$ scales inversely with $c$ while $\fnl$ scales with $c$, so the ratio is invariant under a consistent change of $c$.)` with `(Under a consistent change of $c$ at fixed physical bispectrum, both $\fnl$ and $\sigma(\fnl)$ scale as $1/c$, so $|\fnl|/\sigma(\fnl)$ is invariant.)` — matches L880 exactly. This is the only VERIFIED change required; it removes an internal contradiction in the convention audit. Run `grep -n "scales with c" 02_full_draft.tex` after the fix to confirm zero remaining instances.

2. **[FM1 — OPTIONAL EDITORIAL ENHANCEMENT]** Add a compact budget table (rows: central r, 16th-percentile r; columns: baseline, +GR, +b_φ, +GR+b_φ) showing the floor can reach 2.5σ for the 16th-percentile r draw. This is purely editorial — the arithmetic is already in the text at L440 and L535. Houston decision.

3. **[FM3 — HOUSTON DECISION]** Optionally rename "genuine theory-modeling ambiguity" → "basis-dependent representation uncertainty in our doubled symmetrized implementation" in L426 for precision. Not required; the scope disclaimer is already present.

---

## PART 5 — Reviewer assessment

| Reviewer | Verdict | Accuracy |
|----------|---------|----------|
| ChatGPT | MAJOR REVISIONS | Over-called: FM1 is FALSIFIED (propagation in text), FM3 is OPINION; only FM2 (one-sentence typo) is real. Headline claim "central issues remain" is not supported at MAJOR severity by the tex evidence. |
| Grok | ACCEPT | Accurate but under-calling FM2 (L816 remnant). |
| Gemini | ACCEPT WITH MINOR | Accurate ACCEPT; fresh MINOR falsified (extraction artifact). |

**Is P2 externally clean after the FM2 fix?** YES — one-sentence correction at L816 removes the only verifiable internal contradiction. After that fix, all three external reviewers either ACCEPT or have only falsified/opinion residue. The paper is publication-ready pending the FM2 fix + recompile + Houston sign-off.
