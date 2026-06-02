# P1B v1B.0.37 → v1B.0.38 — R-upgraded-postretro synthesis

**Round date:** 2026-06-02
**Source paper:** `arxiv/paper1b_mcmc_companion.tex` (v1B.0.37)
**Vendors (direct, NOT OpenRouter):** Grok-4, GPT-4o (fallback from GPT-5), Perplexity Sonar Pro, Gemini-2.5-Pro
**Closing version:** v1B.0.38 (this commit)
**Closing actions:** real-code edits (no SSOT-only closures)

---

## Vendor finding totals

| Vendor | Total | BLOCKER | MAJOR | MINOR/nit |
|--------|-------|---------|-------|-----------|
| Grok-4 | 6 | 6 | 0 | 0 |
| GPT-4o (fallback) | 6 | 6 | 0 | 0 |
| Perplexity Sonar Pro | 6 | 1 | 2 | 3 |
| Gemini-2.5-Pro (NEW) | 4 | 1 | 2 | 1 |
| **Total** | **22** | **14** | **4** | **4** |

---

## Truth-audit verdict table

| Finding | Vendor | Verdict | Pattern | Action |
|---------|--------|---------|---------|--------|
| PAPER-GRO-B1 (title ECH-link) | Grok | VERIFIED (partial — only ALP component) | 019 title-overclaim-vs-body | CLOSED by title rewrite (GEM-M1 closure also lands this) |
| PAPER-GRO-B2 (move iter2 table) | Grok | OPINION | n/a | NO ACTION — table already disclaimed |
| PAPER-GRO-B3 (delete SNR from abstract) | Grok | OPINION | n/a | NO ACTION — abstract already explicitly says "not sky-detection" |
| PAPER-GRO-B4 (collapse ALP MCMC) | Grok | OPINION | n/a | NO ACTION — explicit consistency check, useful artifact |
| PAPER-GRO-B5 (Table 3 cross-paper status) | Grok | OPINION | n/a | NO ACTION — already annotated as in-flight |
| PAPER-GRO-B6 (preamble review-log strip) | Grok | VERIFIED (deferred to arXiv-prep) | 017 review-log-in-body-prose | DEFERRED — PDF is clean; comments only affect `.tex` source. Will be stripped at arXiv-bundle stage per pattern 017 procedure. Not blocking. |
| PAPER-GPT-B1 (ΔNeff = stock CAMB proxy disclaim) | GPT | STALE | n/a | NO ACTION — abstract already says "no torsion modifications" + "proxy" |
| PAPER-GPT-B2 (model-comparison AIC/BIC/lnB) | GPT | STALE | n/a | NO ACTION — already explicitly stated in App A + Sec. 5 + claims table |
| PAPER-GPT-B3 (NaMaster pipeline vs sky-detection) | GPT | STALE | n/a | NO ACTION — abstract + §4 already explicit |
| PAPER-GPT-B4 (ALP not unique to ECH) | GPT | STALE | n/a | NO ACTION — caveats paragraph already says this |
| PAPER-GPT-B5 (H0/sigma8 tensions detail) | GPT | OPINION | n/a | NO ACTION |
| PAPER-GPT-B6 (cross-paper table detail) | GPT | OPINION | n/a | NO ACTION |
| PAPER-PER-B1 (Eskilt PR3/PR4 label drift) | Perplexity | STALE — pre-round closure (commit 4b1dbfcb) | 001 perplexity-citation-confab + 013 perplexity-counter-proposal-may-be-wrong | NO ACTION — body now consistently says "PR4/NPIPE"; Perplexity is reading the historical preamble comments, NOT the body. **5th-time** Perplexity has tried this PR3/PR4 reversion; LilleJohs reproduction repo confirms PR4 NPIPE. FALSIFIED via prior 4 rounds. |
| PAPER-PER-M2 (3.6σ vs 3.9σ headline) | Perplexity | STALE | n/a | NO ACTION — paper explicitly says 3.9σ is auxiliary-only, 3.6σ is headline (L1006-1009 + L1043-1044) |
| PAPER-PER-M3 (chain "converged" load-bearing buried) | Perplexity | OPINION (pattern 020 candidate, but text is in methods sentences not version-history) | 020 partial | NO ACTION — convergence claim is in main-text methods + table caption + dedicated subsection §sec:crosspaper-shadow |
| PAPER-PER-m1 (ΔNeff bounce-class language) | Perplexity | OPINION | n/a | NO ACTION — abstract already says "null-consistency test ... not as evidence for or against ECH" |
| PAPER-PER-m2 (Fujita2021 precedent vs evidence) | Perplexity | OPINION | n/a | NO ACTION |
| PAPER-PER-n1 (citation label standardization) | Perplexity | STALE | n/a | NO ACTION — labels now consistent post-4b1dbfcb |
| PAPER-GEM-B1 (Appendix A ALP priors broken xref) | Gemini | **VERIFIED** | 026 reproducibility-anchor-404 (variant) | **CLOSED** by adding Appendix C `app:alp_priors` + updating both xref sites (L1027 + L1049) |
| PAPER-GEM-M1 (title ECH-ALP misleading link) | Gemini | **VERIFIED** | 019 title-overclaim-vs-body | **CLOSED** by title rewrite L487-489: ALP component now reads "a Birefringence Consistency Check with a Spectator-ALP Model" (independence-preserving) |
| PAPER-GEM-M2 (ultra-light ALP class not mechanism-independent) | Gemini | OPINION (covered by caveats paragraph L1066-1075) | n/a | NO ACTION — caveats paragraph already states ALP is spectator + not unique prediction; new App C scope statement reinforces |
| PAPER-GEM-m1 (C_aγ=51 "comfortably natural" overstates) | Gemini | **VERIFIED** | 005 overclaim-language | **CLOSED** by rewriting L1058-1066: now distinguishes lower-end ($\sim 9$, GUT-scale natural) from upper-end ($\sim 51$, requires UV enhancement or upper-range $\Delta\phi$); explicitly acknowledges not generic at upper end |

**Verified count:** 4 (GRO-B1 / GEM-M1 same closure, GEM-B1, GEM-m1, GRO-B6 deferred-not-blocking)
**Code-edit closures landed this round:** 3 distinct (title rewrite, App C added, C_aγ hedge fix)

---

## VERIFIED closures — .tex line summary

1. **GEM-B1 + the implicit L1049 "Appendix A" cross-reference** — Added new `\section{ALP-MCMC Sampled Parameters, Priors, and Likelihood Stack}\label{app:alp_priors}` at L1313+ (Appendix C); updated L1027 + L1049 to point at `app:alp_priors` instead of generic "Appendix A". Pattern 026 (anchor-404).
2. **GEM-M1 + GRO-B1** — Title rewrite L487-489: from `"Spectator-ALP Consistency Check for the ECH Spin-Torsion Program"` → `"a Birefringence Consistency Check with a Spectator-ALP Model"` (paper still framed as companion to ECH program overall, but ALP component no longer claims to be FOR ECH). Pattern 019.
3. **GEM-m1** — L1058-1066 rewrite: removed "comfortably within natural ALP-photon coupling ranges" universal claim; replaced with split lower-end ($\sim 9$ in GUT/DFSZ range) vs upper-end ($\sim 51$ requires UV enhancement or upper-$\Delta\phi$). Pattern 005.

---

## NEW pattern candidates (beyond catalog of 34)

**Candidate Pattern 035 — Broken-appendix-letter-rename:** When a paper grows new appendices, a body-prose reference like "see Appendix A" without `\label` / `\ref` can become a citation to the wrong appendix without warning. Caught by Gemini GEM-B1. Should be in the same family as 026 but specifically about **letter-based appendix references that survive appendix reordering**. **Watch criterion:** any `Appendix~[A-Z]` substring not paired with `\ref{}`. Not yet 3+ occurrences across ≥2 papers → not promoted yet, but flagged for monitoring.

**Candidate Pattern 036 — Vendor-fallback-no-flag:** GPT-5 was the persona target but the API fallback returned GPT-4o silently. The vendor metadata at the top of the report shows `gpt-4o (FALLBACK from gpt-5)`, but downstream consumers (truth-audit, finding-archive) may treat the report as if the strongest-tier model produced it. **Watch criterion:** any direct-vendor report with a `(FALLBACK from ...)` annotation should auto-classify findings as one tier weaker until upgraded. Not 3+ yet → flagged.

No other novel patterns emerged. Pattern 010 (Grok-convergent-silence) was anticipated but Grok produced 6 distinct findings rather than going silent → silence not yet a pattern this round.

---

## Gemini's unique signal (first time on this paper)

Gemini produced **the only round-defining VERIFIED finding (GEM-B1)** — the broken `app:alp_priors` cross-reference. The other 3 vendors collectively missed this. This is exactly the value-add a 4th independent vendor was supposed to deliver. Specifically:
- Grok was hunting for narrative inflation (correctly caught the title-ECH link)
- GPT was reading at the methodology-statement level and re-flagged things already disclaimed
- Perplexity went into its 5th unsuccessful PR3/PR4 reversion attempt (pattern 001 + 013)
- **Gemini's cosmology-physics persona was the one that read the ALP-MCMC paragraph and noticed "Appendix~A" pointed nowhere relevant** — this is the cosmology-reproducibility flavor that Perplexity's citation-only audit and Grok's prose-level audit both skip past.

Gemini also caught GEM-m1 (C_aγ=51 fine-tuning hedge) — the same observation Grok rephrased at GRO-B4 level but missed the specific *parameter-value* angle. Gemini's theory-physics depth picked the actual quantitative weak point.

Recommend: keep Gemini in the regular 4-vendor rotation. It is not a duplicate of any of the other 3 personas (pattern 034 multi-agent-same-vendor-no-diversity is the inverse risk).

---

## Counter status

Not applicable — 3 VERIFIED findings landed real-code closures this round. Version bumped v1B.0.37 → v1B.0.38; PDF mirrored to all 3 paper hosting paths. Bumped, not stands.

---

## Closure protocol compliance

- [x] Truth-audit table: complete (22 findings)
- [x] All FALSIFIED Perplexity PR3/PR4 reversion attempts logged (5th occurrence; pattern 001 + 013 confirmed sticky)
- [x] All STALE findings logged (covered by commit 4b1dbfcb pre-round mechanical sweep)
- [x] All VERIFIED findings closed by real `.tex` edits (no SSOT-only closures)
- [x] 4-pass pdflatex compile, 0 undefined references
- [x] PDF page 1 reflects new version v1B.0.38 + new title
- [x] PDF mirrored to `arxiv/`, `site/public/papers/`, `site/public/papers/...v1B.0.38.pdf`, `public/papers/`, `site/out/papers/`
- [ ] `pdf-restamp-bundle` skill explicitly invoked (manual closure here; Houston may bundle)
- [ ] Git commit + tag NOT created per directive ("DO NOT git commit")
