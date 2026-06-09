# P2 R22prov2 — Truth audit (v1.7.44, correct-PDF re-run)

**Headline: 3 of 5 vendors + meta-reviewer returned ZERO findings**
(Claude_brutal 0, Gemini 0, OpenAI 0, META 0). All 35 findings come from
Grok (9) and Perplexity (26). Round verdict after audit: **NOT CLEAN but
near-clean** — 8 small VERIFIED text items → v1.7.45 mini-wave; zero
compute-bound items; bispectrum headline untouched.

## Perplexity citation forensics — 5/5 FALSIFIED (pattern-001 confab)

| Finding | Claim | Verdict | Evidence (web-verified 2026-06-09) |
|---|---|---|---|
| E3 | Zhu & Cai arXiv:2603.13924 "non-existent; 2603 invalid" | **FALSIFIED** | Exists: "Smoking-gun signatures of bounce cosmology from echoes of relic GWs", Zhu & Cai, posted 2026-03-14; 2603=YYMM is valid |
| E4 | Jolicoeur arXiv:2511.09466 "fabricated" | **FALSIFIED** (minor author fix) | Exists, posted 2025-11-12 — but first author is C. Addis (Jolicoeur 7th, Maartens 8th) → fix bib author list |
| E5 | Diego-Palazuelos & Komatsu arXiv:2509.13654 "fabricated" | **FALSIFIED** | Exists; β=0.215°±0.074° (2.9σ) exactly as cited portfolio-wide |
| E6 | Cosmoglobe DR1 II "A&A 679 A144 + 2305.02268 don't jointly exist" | **FALSIFIED** | Both jointly correct (Eskilt, Watts et al. 2023) |
| E7 | 1712.09998 author list "suspicious fusion" | **FALSIFIED** | Author list is exactly Cai, Chen, Namjoo, Sasaki, D.-G. Wang, Z. Wang (JCAP 05(2018)012) |

## VERIFIED items → v1.7.45 mini-wave

| # | Finding | Vendor | Fix |
|---|---|---|---|
| V1 | Provenance bracket carries version numbers + repo path in body prose (pattern-017) | Perplexity E1+E9 | Neutralize: keep the fact of the correction, move script path + version detail to Data Availability |
| V2 | AI acknowledgment phrasing risks authorship ambiguity | Perplexity E2 (style) | Reword to software-infrastructure framing; responsibility statement |
| V3 | BF vs SSFSR prior not defined where the large BFs are quoted | Perplexity E8 | State the SSFSR prior explicitly at Table II/III |
| V4 | Abstract presents Heinrich-rescaled σ(fNL)≈0.7 as internal | Grok E2 | Attribute "rescaled from Heinrich et al. 2024" in abstract |
| V5 | Composite 3–5σ headline not traceable to one place | Grok E1 (PARTIAL) | One sentence pointing to the systematics-budget table chain |
| V6 | 10k random-coefficient scan: ball radius/measure unjustified | Grok M2 | Robustness sentence (or honest caveat) at §II.A |
| V7 | Fig 2 error-bar definition ("optimistic-to-conservative") undefined | Grok M3 | Caption: state which budget factors each bar folds in |
| V8 | σ juxtapositions lack local non-comparability notes at 3-4 sites | Perplexity (last) | Add at abstract + §IV + §V + §VIII.A |

## FALSIFIED / no-action (beyond the 5 citation confabs)

- Grok E3 "no derivation/code supplied for 0.295/0.596" — **FALSIFIED**: the
  provenance bracket cites scripts/c8_fnl_running_fisher.py (Perplexity E9
  complains about that very path). V1 moves it to Data Availability.
- Grok N1 + consensus "future date June 2026" — **FALSIFIED**: it IS June 2026
  (reviewer training-cutoff artifact; same as P4 D17).
- Grok M1 22pp length — OPINION (consistent with portfolio C18 disposition).

## Pattern-archive note

Perplexity citation-confab rate this round: 5/5 ESSENTIAL citation claims
false. Feed to findings-archive + pattern-001 stats.

## POST-AUDIT CORRECTION (2026-06-09, ~14:30 PT)

The "3 of 5 vendors returned ZERO findings" headline is overstated: the
Claude_brutal leg FAILED (Anthropic API credit exhaustion, billing 400) and
its 0 count is an error artifact, not a clean review. True round composition:
Gemini + OpenAI + META genuinely zero; Grok + Perplexity findings audited
above; Claude ABSENT. Round is DEGRADED — a Claude-inclusive confirmation
round is required after credit top-up before P2 counts a clean round.
Same applies to the Claude legs of R22prov P3/P4/P5.
